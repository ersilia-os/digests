#!/usr/bin/env python3
"""make_og_images.py — screenshot every built page into its social-preview card.

    python scripts/make_og_images.py _site --baseurl /digests

Run after `jekyll build`. For every HTML page in the built site it writes a 1200x630 PNG
of the top of that page to <site>/og/<page path without .html>.png (the home page goes to
og/index.png). website/_includes/social-meta.html points og:image at exactly that path, so
the two must stay in sync.

The capture approach is adapted from the Ersilia html-formatting skill
(ersilia-skills/skills/html-formatting/scripts/make_og_image.py):

* The built site is SERVED over a local HTTP port, mounted under --baseurl, so the
  stylesheet and fonts resolve exactly as they do on GitHub Pages.
* The page is ZOOMED: LinkedIn renders the card a few hundred pixels wide, so a 1:1
  viewport crop turns body text into mush. At zoom z we capture 1200/z x 630/z CSS
  pixels and render them at device scale z, so the PNG is always 1200x630 but the
  wordmark, eyebrow and title fill the card.

Standard library only; needs a Chrome/Chromium binary (preinstalled on GitHub's
ubuntu-latest runners).
"""

from __future__ import annotations

import argparse
import functools
import http.server
import shutil
import socketserver
import subprocess
import sys
import tempfile
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

CHROME_CANDIDATES = (
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/usr/bin/google-chrome",
    "/usr/bin/chromium",
    "/usr/bin/chromium-browser",
)
CHROME_ON_PATH = ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser")

WIDTH, HEIGHT = 1200, 630
POLL_SECONDS = 0.25


def find_chrome(explicit: str | None = None) -> str:
    """Locate a Chrome/Chromium binary, or fail with something actionable."""
    if explicit:
        if not Path(explicit).exists():
            raise SystemExit(f"ERROR: no such browser binary: {explicit}")
        return explicit
    for candidate in CHROME_CANDIDATES:
        if Path(candidate).exists():
            return candidate
    for name in CHROME_ON_PATH:
        found = shutil.which(name)
        if found:
            return found
    raise SystemExit("ERROR: no Chrome/Chromium found; pass --chrome.")


class _QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, fmt, *args):  # noqa: D102
        pass


class _Server(socketserver.ThreadingMixIn, socketserver.TCPServer):
    daemon_threads = True


def serve(root: Path) -> tuple[socketserver.TCPServer, int]:
    """Serve `root` on an ephemeral port; return (server, port)."""
    handler = functools.partial(_QuietHandler, directory=str(root))
    httpd = _Server(("127.0.0.1", 0), handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd, httpd.server_address[1]


def og_path_for(page: Path, site: Path) -> Path:
    """Map a built page to its card path, mirroring _includes/social-meta.html."""
    rel = page.relative_to(site).with_suffix("")
    return site / "og" / rel.with_suffix(".png")


def capture(chrome: str, url: str, out: Path, zoom: float, wait_ms: int, timeout: int) -> None:
    """Write a WIDTH x HEIGHT PNG of the top of `url` to `out`."""
    css_w, css_h = round(WIDTH / zoom), round(HEIGHT / zoom)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.unlink(missing_ok=True)
    with tempfile.TemporaryDirectory(prefix="og-chrome-") as profile:
        cmd = [
            chrome,
            "--headless=new",
            "--disable-gpu",
            "--no-sandbox",
            "--hide-scrollbars",
            "--force-color-profile=srgb",
            "--force-prefers-color-scheme=light",
            "--blink-settings=preferredColorScheme=1",
            "--no-first-run",
            "--no-default-browser-check",
            f"--user-data-dir={profile}",
            f"--window-size={css_w},{css_h}",
            f"--force-device-scale-factor={zoom:g}",
            f"--virtual-time-budget={wait_ms}",
            f"--screenshot={out}",
            url,
        ]
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        # Headless Chrome sometimes lingers after writing the PNG: poll until the file
        # size is stable, then stop it.
        last = -1
        for _ in range(int(timeout / POLL_SECONDS)):
            if proc.poll() is not None:
                break
            if out.exists():
                size = out.stat().st_size
                if size > 0 and size == last:
                    proc.kill()
                    break
                last = size
            time.sleep(POLL_SECONDS)
        else:
            proc.kill()
        err = proc.communicate()[1] or ""
    if not out.exists():
        raise RuntimeError(f"no screenshot for {url}\n{err.strip()[-1500:]}")


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("site", help="built site directory (jekyll --destination)")
    p.add_argument("--baseurl", default="/digests", help="site baseurl (default: /digests)")
    p.add_argument("--zoom", type=float, default=1.5, help="page zoom inside the card (default: 1.5)")
    p.add_argument("--wait-ms", type=int, default=3000, help="virtual time for fonts/CSS (default: 3000)")
    p.add_argument("--timeout", type=int, default=60, help="seconds per page before giving up")
    p.add_argument("--jobs", type=int, default=4, help="pages captured in parallel (default: 4)")
    p.add_argument("--only", nargs="*", help="limit to these page paths, relative to the site")
    p.add_argument("--chrome", help="path to a Chrome/Chromium binary (default: autodetect)")
    args = p.parse_args(argv)

    site = Path(args.site).resolve()
    if not site.is_dir():
        raise SystemExit(f"ERROR: no such site directory: {site}")
    chrome = find_chrome(args.chrome)

    pages = sorted(
        x for x in site.rglob("*.html")
        if "og" not in x.relative_to(site).parts[:1] and x.name != "404.html"
    )
    if args.only:
        wanted = {site / o for o in args.only}
        pages = [x for x in pages if x in wanted]
    if not pages:
        raise SystemExit("ERROR: no HTML pages found")

    # Mount the site under its baseurl so /digests/assets/... resolves.
    with tempfile.TemporaryDirectory(prefix="og-root-") as tmp:
        root = Path(tmp)
        mount = root / args.baseurl.strip("/") if args.baseurl.strip("/") else root
        mount.parent.mkdir(parents=True, exist_ok=True)
        if mount != root:
            mount.symlink_to(site, target_is_directory=True)
        httpd, port = serve(root if mount != root else site)
        prefix = f"http://127.0.0.1:{port}/{args.baseurl.strip('/')}".rstrip("/")

        def job(page: Path) -> str:
            rel = page.relative_to(site).as_posix()
            out = og_path_for(page, site)
            capture(chrome, f"{prefix}/{rel}", out, args.zoom, args.wait_ms, args.timeout)
            return f"{rel} -> {out.relative_to(site)}"

        failures = 0
        try:
            with ThreadPoolExecutor(max_workers=args.jobs) as pool:
                for page, fut in [(pg, pool.submit(job, pg)) for pg in pages]:
                    try:
                        print(fut.result(), file=sys.stderr)
                    except Exception as exc:  # keep going; report at the end
                        failures += 1
                        print(f"FAILED {page}: {exc}", file=sys.stderr)
        finally:
            httpd.shutdown()
            httpd.server_close()

    print(f"{len(pages) - failures}/{len(pages)} cards written", file=sys.stderr)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
