---
version: alpha
name: Ersilia Digests
description: >-
  Design system for the Ersilia Digests site (ersilia-os.github.io/digests): a calm,
  information-dense reading surface for periodic literature, GitHub, model-incorporation
  and event digests. Built on the Ersilia house style — plum identity, periwinkle
  interaction, soft off-black ink — and written to the DESIGN.md specification
  (google-labs-code/design.md) with Material 3 token names.
colors:
  primary: "#6C5CE7"
  on-primary: "#FFFFFF"
  primary-container: "#EEEBFC"
  on-primary-container: "#2A1F7A"
  brand-identity: "#50285A"
  background: "#FAFAFC"
  on-background: "#2C3E50"
  surface: "#FFFFFF"
  surface-container-low: "#F7F7FA"
  surface-container: "#F4F4F8"
  surface-container-high: "#ECECF2"
  on-surface: "#2C3E50"
  on-surface-variant: "#6B6675"
  outline: "#9A93A6"
  outline-variant: "#E6E6EE"
  shadow: "rgba(80,40,90,0.07)"
  family-literature: "#BEE6B4"
  family-github: "#FAA08C"
  family-events: "#8CC8FA"
  family-models: "#EEC95F"
  family-multiple: "#50285A"
  dark-primary: "#AA96FA"
  dark-on-primary: "#1B1531"
  dark-primary-container: "#272040"
  dark-brand-identity: "#C9B6F5"
  dark-family-multiple: "#8A6BE0"
  dark-background: "#17161C"
  dark-surface: "#1E1D24"
  dark-surface-container-low: "#1B1A20"
  dark-surface-container: "#26252D"
  dark-surface-container-high: "#302F38"
  dark-on-surface: "#E4E2EA"
  dark-on-surface-variant: "#A19DAB"
  dark-outline: "#7A7585"
  dark-outline-variant: "#2E2D36"
typography:
  wordmark:
    fontFamily: Inter
    fontSize: 17px
    fontWeight: 700
    lineHeight: 22px
    letterSpacing: -0.015em
  headline-lg:
    fontFamily: Inter
    fontSize: 28px
    fontWeight: 700
    lineHeight: 36px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: 600
    lineHeight: 26px
    letterSpacing: -0.01em
  title-sm:
    fontFamily: Inter
    fontSize: 15px
    fontWeight: 600
    lineHeight: 22px
  body-md:
    fontFamily: Inter
    fontSize: 15px
    fontWeight: 400
    lineHeight: 26px
  body-sm:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: 400
    lineHeight: 20px
  label-md:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: 500
    lineHeight: 18px
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: 500
    lineHeight: 16px
  data:
    fontFamily: JetBrains Mono
    fontSize: 13px
    fontWeight: 400
    lineHeight: 18px
    fontFeature: tnum
rounded:
  xs: 3px
  sm: 6px
  DEFAULT: 10px
  lg: 14px
  full: 9999px
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  xxl: 64px
  gutter: 16px
  sidebar: 280px
  prose-max: 720px
  wide-max: 1100px
components:
  sidebar:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface-variant}"
    typography: "{typography.label-md}"
    width: "{spacing.sidebar}"
  nav-item-active:
    backgroundColor: "{colors.primary-container}"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
  wordmark:
    textColor: "{colors.brand-identity}"
    typography: "{typography.wordmark}"
  eyebrow:
    textColor: "{colors.on-surface-variant}"
    typography: "{typography.label-sm}"
  page-header:
    textColor: "{colors.on-surface}"
    typography: "{typography.headline-lg}"
  legend-block:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface-variant}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.DEFAULT}"
    padding: 12px 16px
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    rounded: "{rounded.DEFAULT}"
    padding: 12px 16px
  card-hover:
    backgroundColor: "{colors.primary-container}"
  calendar-cell:
    backgroundColor: "{colors.surface-container}"
    rounded: "{rounded.xs}"
    size: 13px
  data-table:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    typography: "{typography.body-sm}"
  footer:
    textColor: "{colors.outline}"
    typography: "{typography.label-sm}"
---

# Ersilia Digests — design system

## Overview

The Ersilia Digests are periodic reports — weekly literature and GitHub digests, monthly
model-incorporation digests and twice-yearly event scans — published for the Ersilia team
and for anyone following open-source AI for global-health drug discovery. Readers arrive
mostly from a shared link (Slack, LinkedIn), read one digest top to bottom, and leave.

So the site is a **quiet reading surface**: a narrow prose column, a sidebar archive, and
nothing competing with the text. It follows the Ersilia house style — sleek rather than
populated, technical but plain, never salesy. The only colourful element is the year
calendar on the home page, where colour encodes which kind of digest landed on which day.

## Colors

- **Primary (#6C5CE7, periwinkle)** is the interactive colour: links, the active nav item,
  focus rings, card hover. It harmonises with the data hues where plum would be too heavy.
- **Brand identity (#50285A, plum)** is Ersilia's signature. It appears only in the
  wordmark and the "multiple digests" calendar cell. Used sparingly.
- **Ink (#2C3E50)** is the body text — Ersilia's soft off-black, never pure black.
- **Surfaces** are cool near-whites: page `background` #FAFAFC, the sidebar and cards on
  `surface` #FFFFFF, recessed fills (code, empty calendar cells) on `surface-container`.
- **Family hues** encode the digest type and nothing else: mint = literature, orange =
  GitHub, blue = events, amber = model incorporations, plum = more than one on the same day.
  They appear in the calendar and its legend, never as decoration.

**Dark mode:** the `dark-*` tokens apply under `prefers-color-scheme: dark`. Periwinkle
lightens to lavender (#AA96FA) to keep AA contrast on the dark surfaces.

## Typography

- **Inter** for everything textual. Base size 15px; a dense, readable scale rather than
  big marketing type.
- **JetBrains Mono with tabular numerals** for dates and numbers — the archive dates in the
  sidebar and cards line up in a column.
- Labels are **sentence case**, muted, weight 500. No uppercase micro-labels; they read as
  techy and shouty.
- Weight belongs on content: 400 body, 500 labels, 600 section headings, 700 for the
  wordmark and the page title.
- Organism and gene names are italic, as in the digests' source Markdown.

## Layout

- Desktop: a fixed 280px sidebar (wordmark, tagline, archive by family) beside a single
  content column. Prose is capped at 720px for line length; table-first families (events,
  model incorporations) take the 1100px wide column so headers and tables end on one edge.
- Below 860px the sidebar becomes an off-canvas drawer behind a sticky top bar; content
  uses a 16–22px gutter and the page never scrolls horizontally (wide tables and the
  calendar scroll inside their own containers).
- Spacing is a 4px scale; sections are separated by 40px plus a hairline rule.

## Elevation & Depth

Almost flat. Depth comes from the surface step between `background` and `surface` and a
1px `outline-variant` hairline. Where a shadow is used (cards on hover, calendar cells with
a digest) it is **plum-tinted** (`rgba(80,40,90,…)`), never neutral grey — a subtle brand
signature.

## Shapes

Small, consistent radii: 3px calendar cells, 6px nav items and inline code, 10px cards,
legend blocks and code blocks. Nothing pill-shaped except where a control is genuinely a
pill.

## Components

- **Favicon:** the official Ersilia mark (plum grid) as served by ersilia.io; never a
  redrawn or invented icon.
- **Wordmark:** "Ersilia" in plum + "*Digests*" in italic periwinkle, above a muted
  one-line tagline. Typographic, no logo image.
- **Sidebar archive:** one collapsible group per family (chevron, sentence-case title,
  mono count). Each group is **bounded**: the latest 5 digests, the current page if it is
  older (after a ⋯), then "All N →" to the family archive page — the sidebar never grows
  with the number of digests. Dates in mono. The current page is periwinkle text on a light
  periwinkle wash — no bold pill, no coloured left bar. Families are defined once in
  `website/_data/families.yml`.
- **Archive page:** one per family (`/archive/<family>.html`), all digests newest first,
  grouped under month headings, as cards.
- **Older / newer:** three tiles under each digest — previous issue, the family archive,
  next issue — so readers can walk a series without the sidebar listing it.
- **Page header:** an eyebrow ("Literature digest · Ersilia Open Source Initiative") above
  the H1, then the digest's legend paragraph (connectors, markers, tasks) set as a quiet
  bordered block.
- **Card list (home):** one row per recent digest — family label on the left, mono date and
  an arrow on the right. Hover tints periwinkle.
- **Year calendar (home):** a GitHub-style day grid, one cell per day, coloured by family.
  Legend underneath.
- **Data tables:** hairline borders, sentence-case header row on `surface-container-low`,
  fixed per-family column widths.
- **Footer:** one muted line crediting the Ersilia Open Source Initiative, with links to
  ersilia.io and the source repository.
- **Social card:** every page ships Open Graph and Twitter meta tags. The card image is a
  1200×630 screenshot of the top of that page (wordmark, eyebrow, title, first lines),
  generated at build time — the page *is* the card. `og:title` is the page title,
  `og:description` one plain sentence per digest family.

## Do's and Don'ts

- **Do** take every colour, size and radius from a token; derive tints with `color-mix()`.
- **Do** keep family hues for encoding digest type only.
- **Do** keep WCAG AA contrast in both themes.
- **Do** keep the source Markdown untouched — styling happens in the layout and CSS.
- **Don't** use plum for links or buttons; it is identity, not interaction.
- **Don't** use uppercase labels, coloured nav text or decorative dots.
- **Don't** write a separate "punchier" social title or marketing copy for the card.
- **Don't** commit generated card images; they are build output.
