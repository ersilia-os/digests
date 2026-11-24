# Ersilia GitHub Digest — Week of 2026-11-24

**Connectors:** GitHub 🟢 · Airtable 🟢  
**Markers:** 🐛 Bug · ✨ Feature · 📄 Docs · 🔧 Infra · 🕒 Stale  

## ✨ Highlights
Busiest repo was `ersilia-self-service`, which was deprecated in favour of hub.ersilia.io (#687) and had 232 issues closed, taking open issues across non-model repos from 258 last week to 38. `zairachem-docker` (10 PRs merged) and `ersilia-model-workflows` (6) followed; the most important change is in the model CI, where PR tests now check out the PR head commit (`ersilia-model-workflows` #21) and arm64 images are published only when they build and pass (#20). `lazy-qsar` reached 3.9.5 (#76), and model repos saw 169 PRs merged across 156 repos. Registry has no missing or uncurated repos, but 9 Status mismatches remain.

## ⚠️ Needs attention

### Stale pull requests
- [ersilia-model-request-app #64](https://github.com/ersilia-os/ersilia-model-request-app/pull/64) — **Fix React Server Components CVE vulnerabilities** · open 257d · last activity 117d ago · @vercel[bot] 🕒
- [ersilia-mcp #50](https://github.com/ersilia-os/ersilia-mcp/pull/50) — **fix(predict): preserve input files when writing results** · open 56d · last activity 56d ago · @ECD5A 🕒
- [ersilia-mcp #41](https://github.com/ersilia-os/ersilia-mcp/pull/41) — **ci(deps): bump actions/setup-python from 5 to 7** · open 90d · last activity 55d ago · @dependabot[bot] 🕒
- [ersilia-mcp #42](https://github.com/ersilia-os/ersilia-mcp/pull/42) — **ci(deps): bump actions/checkout from 4 to 7** · open 90d · last activity 55d ago · @dependabot[bot] 🕒
- `ersilia-stats-capstone` (private) — 2 stale PRs · last activity 120d ago 🕒

### Long-open issues
- [ersilia #1147](https://github.com/ersilia-os/ersilia/issues/1147) — **🐅 Epic: Adding support for Authentication in Ersilia** · open 902d · last activity 84d ago · @DhanshreeA 🕒
- [ersilia #1640](https://github.com/ersilia-os/ersilia/issues/1640) — **🐅 Epic: GPU Support for the Ersilia Model Hub** · open 568d · last activity 21d ago · @miquelduranfrigola
- [eosframes #2](https://github.com/ersilia-os/eosframes/issues/2) — **Feedback 19th August** · open 462d · last activity 230d ago · @miquelduranfrigola 🕒
- [zairachem-docker #32](https://github.com/ersilia-os/zairachem-docker/issues/32) — **xai4chem compatibility with zairachem** · open 308d · last activity 0d ago · @JHlozek
- [ersilia-maintenance #461](https://github.com/ersilia-os/ersilia-maintenance/issues/461) — **Another mid-term maintenance feature** · open 253d · last activity 253d ago · @GemmaTuron 🕒
- [ersilia-pack #92](https://github.com/ersilia-os/ersilia-pack/issues/92) — **Currently no support for Uvicorn / FastAPI `root_path`** · open 249d · last activity 1d ago · @jepdavidson
- [eosframes #3](https://github.com/ersilia-os/eosframes/issues/3) — **Consolidate h5 keys with Ersilia** · open 230d · last activity 230d ago · @GemmaTuron 🕒
- [ersilia-skills #28](https://github.com/ersilia-os/ersilia-skills/issues/28) — **Gap Generative Modeling** · open 112d · last activity 15d ago · @arnaucoma24
- [stylia #5](https://github.com/ersilia-os/stylia/issues/5) — **stylia.label's panel letter (abc) sits right of the ylabel/tick numbers instead of left of them** · open 106d · last activity 106d ago · @arnaucoma24 🕒
- [ersilia #1913](https://github.com/ersilia-os/ersilia/issues/1913) — **🐈 Task: Debug logs and temporary files are removed on execution failure** · open 77d · last activity 11d ago · @SoufianeAatab

_…and 28 more open issues (38 open in total)._

### 💡 Easy wins
- [eosframes #4](https://github.com/ersilia-os/eosframes/issues/4) — **New-functionalities branch outdated** · merge or delete one branch · @GemmaTuron
- [ersilia #1973](https://github.com/ersilia-os/ersilia/issues/1973) — **🐛 Bug: Publish command** · delete unused legacy code · @GemmaTuron
- [ersilia-pack #98](https://github.com/ersilia-os/ersilia-pack/issues/98) — **Ersilia Warm parameter** · pass one environment variable through · @GemmaTuron
- [chem-sampler #7](https://github.com/ersilia-os/chem-sampler/issues/7) — **Remove models from the store** · one well-specified CLI command · @arnaucoma24
- [ersilia-skills #52](https://github.com/ersilia-os/ersilia-skills/issues/52) — **GitHub Digest check for idle branches** · one extra check in a script · @miquelduranfrigola

## 🔧 Registry alignment

0 missing · 0 ghost · 9 status · 0 type · 0 uncurated.

### Status / Type mismatches
- `chembl-binary-tasks` — Status: Airtable «Completed, Archived» vs GitHub «Completed»
- `ersilia-app` — Status: Airtable «Archived» vs GitHub «Completed»
- `ersilia-gui` — Status: Airtable «Archived» vs GitHub «Completed»
- `ersilia-self-service` — Status: Airtable «Archived» vs GitHub «Completed»
- `ffwd-ersilia-game` — Status: Airtable «Archived» vs GitHub «Completed»
- `h3d-mtb-metabolism` — Status: Airtable «Completed, Archived» vs GitHub «Completed»
- `nairobi-meeting-network-mapping-2023` — Status: Airtable «Archived» vs GitHub «Completed»
- `outreachy-contributions` — Status: Airtable «Archived» vs GitHub «Completed»
- `zaira-chem-tdc-benchmark` — Status: Airtable «Completed, Archived» vs GitHub «Completed»

### Possibly out of date
- `aws-utils` — marked Completed but had activity this week
- `digests` — marked Completed but had activity this week
- `eos-analysis-template` — marked Completed but had activity this week
- `eos-template` — marked Completed but had activity this week
- `ersilia` — marked Completed but had activity this week
- `ersilia-gui` — marked Archived but had activity this week
- `ersilia-metadata-annotation` — marked Archived but had activity this week
- `ersilia-model-workflows` — marked Completed but had activity this week
- `ersilia-pack` — marked Completed but had activity this week
- `ersilia-self-service` — marked Archived but had activity this week
- `lazy-qsar` — marked Completed but had activity this week
- `tuimux` — marked Completed but had activity this week

## 📊 Repository overview
182 tracked repos (270 model packages tracked separately) · 52 archived.  
**By type:** Analysis 74 · Package 70 · Automation 13 · Workshop 13 · App 9 · Documentation 3 · Template 3  
**By status:** Completed 77 · In progress 54 · Discontinued 18 · Archived 17 · Idle 13 · Todo 3

## ✅ Recent activity

### Pull requests merged
- [coadd-binary-tasks #2](https://github.com/ersilia-os/coadd-binary-tasks/pull/2) — **Pin LazyQSAR 3.9.2** · @arnaucoma24 · 2026-11-24
- [digests #10](https://github.com/ersilia-os/digests/pull/10) — **Add maintenance digests as a new digest family** · @Marina18 · 2026-11-24
- [eos-analysis-template #3](https://github.com/ersilia-os/eos-analysis-template/pull/3) — **No Git LFS: large files go to eosvc** · @arnaucoma24 · 2026-11-17
- [eos-template #99](https://github.com/ersilia-os/eos-template/pull/99) — **Storage rule: Git under 100 MiB, eosvc otherwise, fit/ to eosvc once it holds training code or data, no Git LFS; align versioning with the Book** · @arnaucoma24 · 2026-11-17
- [ersilia #1969](https://github.com/ersilia-os/ersilia/pull/1969) — **Robustness check: retry variable models when no output file is written** · @arnaucoma24 · 2026-11-23
- [ersilia #1971](https://github.com/ersilia-os/ersilia/pull/1971) — **Install Miniconda in the approve workflow** · @GemmaTuron · 2026-11-23
- [ersilia-book #5](https://github.com/ersilia-os/ersilia-book/pull/5) — **Add Apptainer (Singularity) images page and SIF workflow jobs** · @SoufianeAatab · 2026-11-18
- [ersilia-book #6](https://github.com/ersilia-os/ersilia-book/pull/6) — **Add Warm serving page and update main.py to load_tool/run_tool** · @SoufianeAatab · 2026-11-18
- [ersilia-book #7](https://github.com/ersilia-os/ersilia-book/pull/7) — **Versioning: format conversions of the same weights and random generative models** · @TiagoJanela · 2026-11-17
- [ersilia-book #8](https://github.com/ersilia-os/ersilia-book/pull/8) — **Storage rule: Git under 100 MiB, eosvc otherwise, fit/ to eosvc once it holds training code or data, no Git LFS** · @arnaucoma24 · 2026-11-17
- [ersilia-model-workflows #15](https://github.com/ersilia-os/ersilia-model-workflows/pull/15) — **Download only model/checkpoints via eosvc; authenticate repo date lookup** · @GemmaTuron · 2026-11-23
- [ersilia-model-workflows #17](https://github.com/ersilia-os/ersilia-model-workflows/pull/17) — **Keep Status Test in post-model-upload** · @GemmaTuron · 2026-11-24
- [ersilia-model-workflows #18](https://github.com/ersilia-os/ersilia-model-workflows/pull/18) — **Run the source test before writing metadata; keep an existing Incorporation Date** · @GemmaTuron · 2026-11-24
- [ersilia-model-workflows #19](https://github.com/ersilia-os/ersilia-model-workflows/pull/19) — **Update Airtable from the checked-out metadata file, not the raw GitHub cache** · @GemmaTuron · 2026-11-24
- [ersilia-model-workflows #20](https://github.com/ersilia-os/ersilia-model-workflows/pull/20) — **Require amd64; publish arm64 only when it built and passed (1b-i+ii)** · @GemmaTuron · 2026-11-24
- [ersilia-model-workflows #21](https://github.com/ersilia-os/ersilia-model-workflows/pull/21) — **PR test: check out the PR head commit, from a fork or a branch (fixes #14)** · @GemmaTuron · 2026-11-24
- [ersilia-pack #95](https://github.com/ersilia-os/ersilia-pack/pull/95) 📄 — **Document warm serving in README** · @SoufianeAatab · 2026-11-24
- [ersilia-pack #100](https://github.com/ersilia-os/ersilia-pack/pull/100) — **Fail the pack when installing the model dependencies fails** · @GemmaTuron · 2026-11-24
- [ersilia-self-service #687](https://github.com/ersilia-os/ersilia-self-service/pull/687) — **Deprecate Self Service in favour of hub.ersilia.io** · @GemmaTuron · 2026-11-23
- [ersilia-skills #67](https://github.com/ersilia-os/ersilia-skills/pull/67) — **Storage rule: checkpoints in Git under 100 MiB, fit/ to eosvc once it holds training code or data, no Git LFS (org-wide), no run-time downloads** · @arnaucoma24 · 2026-11-17
- [eu-openscreen-antimicrobial-tasks #2](https://github.com/ersilia-os/eu-openscreen-antimicrobial-tasks/pull/2) — **Pin LazyQSAR 3.9.2** · @arnaucoma24 · 2026-11-24
- [isaura #27](https://github.com/ersilia-os/isaura/pull/27) 🐛 — **fix: make push concurrency configurable and fail when uploads fail** · @arnaucoma24 · 2026-11-20
- [isaura #33](https://github.com/ersilia-os/isaura/pull/33) 🐛 — **fix: support repeated wide writes (#32) and duckdb 2 reads (#31);** · @Marina18 · 2026-11-24
- [lazy-qsar #70](https://github.com/ersilia-os/lazy-qsar/pull/70) 🐛 — **fix(ad): fit the applicability domain in about one copy of X, bit-identical** · @TiagoJanela · 2026-11-20
- [lazy-qsar #72](https://github.com/ersilia-os/lazy-qsar/pull/72) 🐛 — **fix(linear): allow each bind-check row its float32 rounding bound (#71)** · @arnaucoma24 · 2026-11-23
- [lazy-qsar #75](https://github.com/ersilia-os/lazy-qsar/pull/75) — **Remove the unrelated chemeleon PyPI package from the descriptors extra** · @arnaucoma24 · 2026-11-24
- [lazy-qsar #76](https://github.com/ersilia-os/lazy-qsar/pull/76) — **release: 3.9.5, drop the unrelated chemeleon PyPI package** · @arnaucoma24 · 2026-11-24
- [tuimux #23](https://github.com/ersilia-os/tuimux/pull/23) — **Call a disabled routine "off" instead of "paused"** · @miquelduranfrigola · 2026-11-19
- [zairachem-docker #78](https://github.com/ersilia-os/zairachem-docker/pull/78) — **Keep duckdb below 2 in the isaura extra** · @TiagoJanela · 2026-11-24
- [zairachem-docker #79](https://github.com/ersilia-os/zairachem-docker/pull/79) 🔧 — **Update matplotlib requirement from 3.10.0 to 3.11.2** · @dependabot[bot] · 2026-11-24
- [zairachem-docker #80](https://github.com/ersilia-os/zairachem-docker/pull/80) 🔧 — **Update click requirement from 8.4.2 to 8.5.0** · @dependabot[bot] · 2026-11-24
- [zairachem-docker #81](https://github.com/ersilia-os/zairachem-docker/pull/81) — **Write held descriptor matrices to the store in chunks** · @TiagoJanela · 2026-11-24
- [zairachem-docker #82](https://github.com/ersilia-os/zairachem-docker/pull/82) — **Bump isaura extra to 2.4.3** · @GemmaTuron · 2026-11-24
- [zairachem-docker #83](https://github.com/ersilia-os/zairachem-docker/pull/83) — **Stop when the installed LazyQSAR is not the pinned release** · @TiagoJanela · 2026-11-24
- [zairachem-docker #84](https://github.com/ersilia-os/zairachem-docker/pull/84) — **Name each descriptor left out for want of a transformer** · @TiagoJanela · 2026-11-24
- [zairachem-docker #85](https://github.com/ersilia-os/zairachem-docker/pull/85) — **Pin lazyqsar 3.9.3** · @TiagoJanela · 2026-11-24
- [zairachem-docker #86](https://github.com/ersilia-os/zairachem-docker/pull/86) — **Score the training matrix's applicability domain once and reuse the scores** · @TiagoJanela · 2026-11-24
- [zairachem-docker #88](https://github.com/ersilia-os/zairachem-docker/pull/88) 🐛 — **Fix two fresh-install setup issues: containerd image check and isaura migrate message** · @GemmaTuron · 2026-11-24
- `ersilia-skills-private` (private) — 1 PR
- `h3d-mtb-bioactivity` (private) — 1 PR
- `tcolf-antimalarials` (private) — 6 PRs

### Pull requests opened
_44 opened in total; the 37 that were also merged this week are listed above._
- [eos-template #100](https://github.com/ersilia-os/eos-template/pull/100) — **Release every merged PR from its semver label** · @GemmaTuron · 2026-11-23
- [ersilia-book #9](https://github.com/ersilia-os/ersilia-book/pull/9) — **Model incorporation workflow: align with the skills, fix broken links** · @TiagoJanela · 2026-11-23
- [ersilia-model-workflows #16](https://github.com/ersilia-os/ersilia-model-workflows/pull/16) — **Automate semantic version releases for models** · @GemmaTuron · 2026-11-23
- [ersilia-pack #97](https://github.com/ersilia-os/ersilia-pack/pull/97) — **Leave model/framework/fit out of the bundle** · @GemmaTuron · 2026-11-23
- [ersilia-pack #99](https://github.com/ersilia-os/ersilia-pack/pull/99) — **Leave model/framework/fit out of the bundle** · @GemmaTuron · 2026-11-24
- [lazy-qsar #74](https://github.com/ersilia-os/lazy-qsar/pull/74) — **SVM head off by default: allow_kernel_svm (3.10.0)** · @arnaucoma24 · 2026-11-24
- `ersilia-skills-private` (private) — 1 PR

### Issues closed
- [ersilia #1730](https://github.com/ersilia-os/ersilia/issues/1730) — **🦠 Model Request: dotP** · @arnaucoma24 · 2026-11-23
- [ersilia #1904](https://github.com/ersilia-os/ersilia/issues/1904) — **🐈 Task: Update metadata for all models** · @GemmaTuron · 2026-11-23
- [ersilia #1970](https://github.com/ersilia-os/ersilia/issues/1970) — **🦠 Model Request: Workflow Sandbox Test** · @GemmaTuron · 2026-11-23
- [ersilia-hub #9](https://github.com/ersilia-os/ersilia-hub/issues/9) — **Upcoming changes to Bitnami images and charts** · @bitnami-bot · 2026-11-24
- [ersilia-metadata-annotation #1](https://github.com/ersilia-os/ersilia-metadata-annotation/issues/1) — **Initial thoughts** · @miquelduranfrigola · 2026-11-24
- [ersilia-model-workflows #8](https://github.com/ersilia-os/ersilia-model-workflows/issues/8) — **Slack "new issue" notifier fails in all model repos** · @arnaucoma24 · 2026-11-24
- [ersilia-model-workflows #14](https://github.com/ersilia-os/ersilia-model-workflows/issues/14) — **PR test runs on the fork's default branch, not the PR's code** · @arnaucoma24 · 2026-11-24
- [ersilia-pack #82](https://github.com/ersilia-os/ersilia-pack/issues/82) — **Improve CI/CD for Ersilia Pack** · @GemmaTuron · 2026-11-23
- [ersilia-pack #91](https://github.com/ersilia-os/ersilia-pack/issues/91) — **Add Release endpoint** · @GemmaTuron · 2026-11-23
- [ersilia-self-service](https://github.com/ersilia-os/ersilia-self-service/issues) — **229 model-inference-run issues** (#452–#686) · @miquelduranfrigola and 2 others · 2026-11-23
- [ersilia-self-service #171](https://github.com/ersilia-os/ersilia-self-service/issues/171) — **In the Ersilia Self Service streamlit app, change PAT** · @miquelduranfrigola · 2026-11-23
- [ersilia-self-service #176](https://github.com/ersilia-os/ersilia-self-service/issues/176) — **Reflect correctly in bot response whether the model run failed instead of uploading an empty CSV** · @DhanshreeA · 2026-11-23
- [ersilia-self-service #265](https://github.com/ersilia-os/ersilia-self-service/issues/265) — **ADMETs Prediction_MB** · @mariscalbrice · 2026-11-23
- [isaura #29](https://github.com/ersilia-os/isaura/issues/29) — **IsauraReader.read(df=...) returns the first call's rows on every later call (_prepare_read caches its result)** · @miquelduranfrigola · 2026-11-24
- [isaura #31](https://github.com/ersilia-os/isaura/issues/31) — **Narrow-model reads fail with duckdb 2.x (fetch_record_batch removed); released versions lack the duckdb<2 pin** · @TiagoJanela · 2026-11-24
- [isaura #32](https://github.com/ersilia-os/isaura/issues/32) — **Second `IsauraWriter.write()` on a wide model fails with "Cannot operate on a closed database"** · @TiagoJanela · 2026-11-24
- [lazy-qsar #71](https://github.com/ersilia-os/lazy-qsar/issues/71) — **OnnxExportMismatch in the linear classifier when SGD weights grow large (float32 rounding exceeds the fixed 1e-4 bind tolerance)** · @arnaucoma24 · 2026-11-23
- [zairachem-docker #31](https://github.com/ersilia-os/zairachem-docker/issues/31) — **Ersilia unregistered models** · @GemmaTuron · 2026-11-24
- [zairachem-docker #45](https://github.com/ersilia-os/zairachem-docker/issues/45) — **Pipeline Tweaks** · @JHlozek · 2026-11-24
- [zairachem-docker #87](https://github.com/ersilia-os/zairachem-docker/issues/87) — **Release candidate `rc/lazyqsar-3.9.3`: please test before the PRs merge** · @TiagoJanela · 2026-11-24
- `aws-utils` (private) — 6 issues
- `ersilia-gui` (private) — 3 issues
- `west-africa-mtb-lineage-drug-responses` (private) — 5 issues

### Issues opened
- [ersilia #1970](https://github.com/ersilia-os/ersilia/issues/1970) — **🦠 Model Request: Workflow Sandbox Test** · @GemmaTuron · 2026-11-23
- [ersilia #1972](https://github.com/ersilia-os/ersilia/issues/1972) ✨ — **📑 Feature Request: Remove git lfs activation when creating a model repo** · @GemmaTuron · 2026-11-23
- [ersilia #1973](https://github.com/ersilia-os/ersilia/issues/1973) 🐛 — **🐛 Bug: Publish command** · @GemmaTuron · 2026-11-23
- [ersilia-pack #98](https://github.com/ersilia-os/ersilia-pack/issues/98) — **Ersilia Warm parameter** · @GemmaTuron · 2026-11-23
- [ersilia-self-service](https://github.com/ersilia-os/ersilia-self-service/issues) — **59 model-inference-run issues** (#628–#686) · @miquelduranfrigola · 2026-11-17 to 2026-11-18
- [isaura #32](https://github.com/ersilia-os/isaura/issues/32) — **Second `IsauraWriter.write()` on a wide model fails with "Cannot operate on a closed database"** · @TiagoJanela · 2026-11-24
- [lazy-qsar #71](https://github.com/ersilia-os/lazy-qsar/issues/71) — **OnnxExportMismatch in the linear classifier when SGD weights grow large (float32 rounding exceeds the fixed 1e-4 bind tolerance)** · @arnaucoma24 · 2026-11-23
- [lazy-qsar #73](https://github.com/ersilia-os/lazy-qsar/issues/73) — **Kernel SVM heads store training rows in saved checkpoints** · @arnaucoma24 · 2026-11-24
- [zairachem-docker #87](https://github.com/ersilia-os/zairachem-docker/issues/87) — **Release candidate `rc/lazyqsar-3.9.3`: please test before the PRs merge** · @TiagoJanela · 2026-11-23

**Model repos (eosXXXX):** 169 PRs merged · 176 opened · 13 issues closed · 0 opened — across 156 repos. Managed via the model-incorporation flow.
