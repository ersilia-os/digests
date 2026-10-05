# Ersilia GitHub Digest — Week of 2026-10-05

**Connectors:** GitHub 🟢 · Airtable 🟢  
**Markers:** 🐛 Bug · ✨ Feature · 📄 Docs · 🔧 Infra · 🕒 Stale  

## ✨ Highlights
Busiest on `tcolf-antimalarials`, `ersilia` and `ersilia-mcp`. `tcolf-antimalarials` landed a five-part data-curation series (v1.10–v1.18), and `ersilia` merged a run of CLI and Python API improvements (concurrent sessions, friendly errors, docs built in CI). `lazy-qsar` shipped 3.6.1 with a fix for fit-time memory pooling, and several downstream repos moved to lazyqsar 3.6. No repos missing from the registry, but 4 Status and 3 Type values disagree with GitHub.

## ⚠️ Needs attention

### Stale pull requests
- [ersilia-stats-capstone #139](https://github.com/ersilia-os/ersilia-stats-capstone/pull/139) — **Add initial Airtable data snapshots + restrict fetch to app tables** · open 70d · last activity 70d ago · @miquelduranfrigola 🕒
- [ersilia-stats-capstone #140](https://github.com/ersilia-os/ersilia-stats-capstone/pull/140) — **Static HTML site: "Ersilia in numbers" + GitHub Pages deploy** · open 70d · last activity 69d ago · @miquelduranfrigola 🕒
- [ersilia-model-request-app #64](https://github.com/ersilia-os/ersilia-model-request-app/pull/64) — **Fix React Server Components CVE vulnerabilities** · open 207d · last activity 67d ago · @vercel[bot] 🕒

### Long-open issues
- [ersilia-gui #24](https://github.com/ersilia-os/ersilia-gui/issues/24) — **Connect to DynamoDB to store model results** · open 1194d · last activity 573d ago · @jaydenpersonnat 🕒
- [ersilia-gui #28](https://github.com/ersilia-os/ersilia-gui/issues/28) — **Small tweaks to GUI** · open 1177d · last activity 1168d ago · @GemmaTuron 🕒
- [ersilia-gui #26](https://github.com/ersilia-os/ersilia-gui/issues/26) — **API to run** · open 1177d · last activity 1172d ago · @GemmaTuron 🕒
- [ersilia #1147](https://github.com/ersilia-os/ersilia/issues/1147) — **Epic: Adding support for Authentication in Ersilia** · open 852d · last activity 34d ago · @DhanshreeA 🕒
- [west-africa-mtb-lineage-drug-responses #1](https://github.com/ersilia-os/west-africa-mtb-lineage-drug-responses/issues/1) — **Meeting minutes 2024-08-15** · open 779d · last activity 768d ago · @fafaal3107 🕒
- [west-africa-mtb-lineage-drug-responses #2](https://github.com/ersilia-os/west-africa-mtb-lineage-drug-responses/issues/2) — **Meeting minutes 2024-08-22** · open 769d · last activity 767d ago · @fafaal3107 🕒
- [west-africa-mtb-lineage-drug-responses #3](https://github.com/ersilia-os/west-africa-mtb-lineage-drug-responses/issues/3) — **Meeting minutes 29/08/2024** · open 762d · last activity 762d ago · @fafaal3107 🕒
- [west-africa-mtb-lineage-drug-responses #4](https://github.com/ersilia-os/west-africa-mtb-lineage-drug-responses/issues/4) — **Meeting_minutes_05092024** · open 753d · last activity 753d ago · @fafaal3107 🕒
- [west-africa-mtb-lineage-drug-responses #5](https://github.com/ersilia-os/west-africa-mtb-lineage-drug-responses/issues/5) — **Meeting_minutes_03/10/2024** · open 730d · last activity 730d ago · @fafaal3107 🕒
- [aws-utils #8](https://github.com/ersilia-os/aws-utils/issues/8) — **Launch Bastion host** · open 693d · last activity 552d ago · @IamEddie 🕒
_…and 51 more open issues (61 open in total)._

### 💡 Easy wins
- [ersilia-mcp #49](https://github.com/ersilia-os/ersilia-mcp/issues/49) — **Bug: predict can overwrite its input file** · fix PR #50 awaiting review · @ECD5A
- [ersilia-mcp #54](https://github.com/ersilia-os/ersilia-mcp/issues/54) — **Bug: startup logging pollutes the stdio JSON-RPC stream** · fix PR #55 awaiting review · @ECD5A

## 🔧 Registry alignment

0 missing · 0 ghost · 4 status · 3 type · 14 uncurated.

### Status / Type mismatches
- `chembl-binary-tasks` — Status: Airtable «Completed, Archived» vs GitHub «Completed»
- `eosquality` — Status: Airtable «In progress» vs GitHub «Todo»
- `h3d-mtb-metabolism` — Status: Airtable «Completed, Archived» vs GitHub «Completed»
- `zaira-chem-tdc-benchmark` — Status: Airtable «Completed, Archived» vs GitHub «Completed»
- `eosbench` — Type: Airtable «App, Package» vs GitHub «Package»
- `ersilia-stats-capstone` — Type: Airtable «Analysis, App» vs GitHub «Analysis»
- `gradi-target-prioritization` — Type: Airtable «Analysis, App» vs GitHub «Analysis»

### Needs curation
- `gradi-ai-data-working-group` — no Status, no Type
- `lazy-chemvis-paper` — no Status, no Type
- `model-launcher` — no Status, no Type
- `molecule-grids` — no Status, no Type
- `pathogen-pocketome` — no Status, no Type
- `tcolf-chemical-libraries` — no Status, no Type
- `ub-cedd-projects-workshop` — no Status, no Type

### Possibly out of date
- `ersilia` — marked Completed but had activity this week
- `ersilia-self-service` — marked Completed but had activity this week
- `lazy-qsar` — marked Completed but had activity this week
- `stylia` — marked Completed but had activity this week

## 📊 Repository overview
183 tracked repos (260 model packages tracked separately) · 46 archived.  
**By type:** Analysis 68 · Package 66 · Automation 13 · Workshop 11 · App 7 · Template 5 · Documentation 3 · unset 11  
**By status:** Completed 77 · In progress 41 · Archived 19 · Discontinued 17 · Idle 14 · Todo 4 · unset 11  

## ✅ Recent activity

### Pull requests merged
- [eosquality #2](https://github.com/ersilia-os/eosquality/pull/2) — **Cleanup: bug fixes, unified calibration, nearest-analogue support, tests, docs** · @miquelduranfrigola · 2026-10-05
- [ersilia #1927](https://github.com/ersilia-os/ersilia/pull/1927) — **Performance improvements for run/serve/close** · @miquelduranfrigola · 2026-09-28
- [ersilia #1928](https://github.com/ersilia-os/ersilia/pull/1928) — **Friendly errors instead of tracebacks for serve/info/close** · @miquelduranfrigola · 2026-09-28
- [ersilia #1929](https://github.com/ersilia-os/ersilia/pull/1929) — **Make concurrent sessions safe, including the same model in several terminals** · @miquelduranfrigola · 2026-09-28
- [ersilia #1930](https://github.com/ersilia-os/ersilia/pull/1930) — **One consistent, clean style for CLI messages** · @miquelduranfrigola · 2026-09-29
- [ersilia #1931](https://github.com/ersilia-os/ersilia/pull/1931) — **Python API: mirror the CLI and behave like a library** · @miquelduranfrigola · 2026-09-29
- [ersilia #1932](https://github.com/ersilia-os/ersilia/pull/1932) 📄 — **Docs: getting started, Python API and CLI reference, built in CI** · @miquelduranfrigola · 2026-09-29
- [ersilia #1934](https://github.com/ersilia-os/ersilia/pull/1934) — **Errors to stderr, and ERSILIA_SESSION to share a session across commands** · @miquelduranfrigola · 2026-09-29
- [ersilia-mcp #47](https://github.com/ersilia-os/ersilia-mcp/pull/47) — **Isaura read tool** · @Lehcar · 2026-10-04
- [ersilia-mcp #53](https://github.com/ersilia-os/ersilia-mcp/pull/53) — **Use isaura branch to fix integration tests** · @Lehcar · 2026-09-30
- [ersilia-mcp #56](https://github.com/ersilia-os/ersilia-mcp/pull/56) — **Add a codespace configuration** · @Lehcar · 2026-10-01
- [ersilia-skills #41](https://github.com/ersilia-os/ersilia-skills/pull/41) — **Drop the Airtable metric sync, fix the merged-PR query, update literature search landscape** · @miquelduranfrigola · 2026-09-29
- [ersilia-skills #42](https://github.com/ersilia-os/ersilia-skills/pull/42) — **Add the airtable-sync skill** · @miquelduranfrigola · 2026-09-30
- [ersilia-skills #43](https://github.com/ersilia-os/ersilia-skills/pull/43) — **Add the peer-reviewing skill** · @arnaucoma24 · 2026-09-30
- [h3d-mtb-models #1](https://github.com/ersilia-os/h3d-mtb-models/pull/1) — **Refit on lazyqsar 3.6, and serve both proba and rank for every endpoint** · @GemmaTuron · 2026-09-30
- [isaura #24](https://github.com/ersilia-os/isaura/pull/24) 🐛 — **fix: build MinIO from source instead of pulling an image** · @Marina18 · 2026-10-04
- [lazy-qsar #47](https://github.com/ersilia-os/lazy-qsar/pull/47) ✨ — **Feat/reference library ranks** · @GemmaTuron · 2026-09-30
- [lazy-qsar #48](https://github.com/ersilia-os/lazy-qsar/pull/48) 🐛 — **fix: stop the fit-time preprocessor sessions from pooling memory** · @arnaucoma24 · 2026-10-05
- [lazy-qsar #50](https://github.com/ersilia-os/lazy-qsar/pull/50) — **release: 3.6.1** · @arnaucoma24 · 2026-10-05
- [molecule-grids #1](https://github.com/ersilia-os/molecule-grids/pull/1) — **Turn the structure-grid app into the molecule-grids package** · @miquelduranfrigola · 2026-10-03
- [tcolf-antimalarials #60](https://github.com/ersilia-os/tcolf-antimalarials/pull/60) — **Stage 05 Phase 2: one drawing per compound, stable folds, MW ceiling, descriptor supplement, tracked tmp/39, RF/cp/tp_pair re-runs** · @TiagoJanela · 2026-09-30
- [tcolf-antimalarials #75](https://github.com/ersilia-os/tcolf-antimalarials/pull/75) — **Curation 1/5: chirality-aware ECFP4, single-fragment rule, strain from assay description, canonical tautomer (v1.10-v1.12)** · @TiagoJanela · 2026-10-04
- [tcolf-antimalarials #76](https://github.com/ersilia-os/tcolf-antimalarials/pull/76) — **Curation 2/5: stage-02 gates on the DR labels, per-strain 04n tables, 02l evidence, stage 02 at strain grain (v1.13-v1.14)** · @TiagoJanela · 2026-10-04
- [tcolf-antimalarials #77](https://github.com/ersilia-os/tcolf-antimalarials/pull/77) — **Curation 3/5: one relation convention for bounds; stage-03 sources follow it (v1.15-v1.16)** · @TiagoJanela · 2026-10-04
- [tcolf-antimalarials #78](https://github.com/ersilia-os/tcolf-antimalarials/pull/78) — **Curation 4/5: cross-stage audit, isolated-tree harness, single definitions and check tools (v1.17)** · @TiagoJanela · 2026-10-04
- [tcolf-antimalarials #79](https://github.com/ersilia-os/tcolf-antimalarials/pull/79) — **Curation 5/5: stage 03 collects / stage 04 processes, per-strain DR release (v1.18), stage-02 bounds on both sides** · @TiagoJanela · 2026-10-04
- `tcolf-antimalarials` #61–#73 — 13 more merged by @TiagoJanela on 2026-09-30/10-01: Chemprop and TabPFN adapters graduated to `src/`, LazyQSAR 3.6 refits and provenance notes, docs fixes.
- [zairachem-docker #47](https://github.com/ersilia-os/zairachem-docker/pull/47) — **Move to lazyqsar 3.6 and fit against its rank reference** · @GemmaTuron · 2026-10-01
- [zairachem-docker #48](https://github.com/ersilia-os/zairachem-docker/pull/48) — **Keep rank references in data/, prepare them only for trained descriptors, fix nginx config** · @GemmaTuron · 2026-10-04

### Pull requests opened
Still open (the other 33 opened this week are already merged, listed above):
- [ersilia #1935](https://github.com/ersilia-os/ersilia/pull/1935) — **Fetch and serve models as Apptainer images (Linux without Docker)** · @miquelduranfrigola · 2026-09-29
- [ersilia #1938](https://github.com/ersilia-os/ersilia/pull/1938) — **Slim the pip model Dockerfile: no duplicate model layer, one apt layer** · @SoufianeAatab · 2026-10-05
- [ersilia-mcp #50](https://github.com/ersilia-os/ersilia-mcp/pull/50) 🐛 — **fix(predict): preserve input files when writing results** · @ECD5A · 2026-09-29
- [ersilia-mcp #52](https://github.com/ersilia-os/ersilia-mcp/pull/52) 🐛 — **fix(isaura): handle smiles CSVs in cache inspection** · @ECD5A · 2026-09-29
- [ersilia-mcp #55](https://github.com/ersilia-os/ersilia-mcp/pull/55) 🐛 — **fix(logging): keep console logs off MCP stdout** · @ECD5A · 2026-09-29
- [ersilia-mcp #57](https://github.com/ersilia-os/ersilia-mcp/pull/57) 🔧 — **ci(deps): bump conda-incubator/setup-miniconda from 4.0.1 to 4.1.0** · @dependabot[bot] · 2026-09-30
- [tcolf-antimalarials #74](https://github.com/ersilia-os/tcolf-antimalarials/pull/74) — **tmp/45: run_sp_lq36.sh, the SP arm and the augmented cells under LazyQSAR 3.6.0** · @TiagoJanela · 2026-10-01

### Issues closed
- [ersilia #1922](https://github.com/ersilia-os/ersilia/issues/1922) — **Model Request: Ensemble-Conditioned Molecular Design** · @arnaucoma24 · 2026-09-29
- [ersilia #1925](https://github.com/ersilia-os/ersilia/issues/1925) — **Model Request: TransPharmer Pharmacophore-Informed Molecule Generation** · @arnaucoma24 · 2026-09-29
- [ersilia #1926](https://github.com/ersilia-os/ersilia/issues/1926) — **Model Request: Route-Based Synthesizability Score** · @TiagoJanela · 2026-09-28
- [ersilia #1933](https://github.com/ersilia-os/ersilia/issues/1933) — **Model Request: CReM Growth-Based Structure Generation** · @arnaucoma24 · 2026-09-29
- [ub-cedd-projects-workshop #1](https://github.com/ersilia-os/ub-cedd-projects-workshop/issues/1) — **push prediction results file** · @JudeBetow · 2026-09-29

### Issues opened
- [ersilia #1933](https://github.com/ersilia-os/ersilia/issues/1933) — **Model Request: CReM Growth-Based Structure Generation** · @arnaucoma24 · 2026-09-28
- [ersilia #1936](https://github.com/ersilia-os/ersilia/issues/1936) — **Model Request: Chemical Dice Molecular Embeddings** · @TiagoJanela · 2026-10-01
- [ersilia #1937](https://github.com/ersilia-os/ersilia/issues/1937) 🐛 — **ersilia deep test fails when the first deterministic example returns no output** · @arnaucoma24 · 2026-10-05
- [ersilia-mcp #49](https://github.com/ersilia-os/ersilia-mcp/issues/49) 🐛 — **Bug: predict can overwrite its input file** · @ECD5A · 2026-09-29
- [ersilia-mcp #51](https://github.com/ersilia-os/ersilia-mcp/issues/51) 🐛 — **Bug: smiles CSVs cause false cache misses in Isaura inspection** · @ECD5A · 2026-09-29
- [ersilia-mcp #54](https://github.com/ersilia-os/ersilia-mcp/issues/54) 🐛 — **Bug: startup logging pollutes the stdio JSON-RPC stream** · @ECD5A · 2026-09-29
- [ersilia-self-service #462](https://github.com/ersilia-os/ersilia-self-service/issues/462) — **Model Inference Run eos8v1a: Antimicrobial activity prediction against Schistosoma mansoni from public ChEMBL data** · @miquelduranfrigola · 2026-10-04
- [lazy-qsar #49](https://github.com/ersilia-os/lazy-qsar/issues/49) 🐛 — **fit() exhausts 96 GB on a 101k-compound task with 14 actives (73 batches/descriptor); trained fine under 3.4.2** · @GemmaTuron · 2026-10-04
- [stylia #6](https://github.com/ersilia-os/stylia/issues/6) 🐛 — **import stylia is not safe in parallel: unguarded rmtree of matplotlib's cache dir crashes concurrent processes** · @GemmaTuron · 2026-10-03

**Model repos (eosXXXX):** 7 PRs merged · 6 opened · 1 issues closed · 6 opened — across 29 repos. Managed via the model-incorporation flow.
