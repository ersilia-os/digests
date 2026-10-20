# Ersilia GitHub Digest — Week of 2026-10-20

**Connectors:** GitHub 🟢 · Airtable 🟢  
**Markers:** 🐛 Bug · ✨ Feature · 📄 Docs · 🔧 Infra · 🕒 Stale  

## ✨ Highlights
Activity was concentrated in `tcolf-antimalarials`, which merged 25 PRs: the stage-07 screening pipeline, a Dash screening dashboard, chirality-aware fingerprints and a new Enamine library run. `ersilia-mcp` gained isaura write, persist and remove operations, and `lazy-qsar` released 3.7.0 with smoother ranking between anchors (#53). The registry has 2 repos missing and 7 Status/Type mismatches, and 6 repos marked Completed were active this week.

## ⚠️ Needs attention

### Stale pull requests
- [ersilia-model-request-app #64](https://github.com/ersilia-os/ersilia-model-request-app/pull/64) — **Fix React Server Components CVE vulnerabilities** · open 222d · last activity 82d ago · @vercel[bot] 🕒
- [ersilia-stats-capstone #139](https://github.com/ersilia-os/ersilia-stats-capstone/pull/139) — **Add initial Airtable data snapshots + restrict fetch to app tables** · open 85d · last activity 85d ago · @miquelduranfrigola 🕒
- [ersilia-stats-capstone #140](https://github.com/ersilia-os/ersilia-stats-capstone/pull/140) — **Static HTML site: "Ersilia in numbers" + GitHub Pages deploy** · open 85d · last activity 85d ago · @miquelduranfrigola 🕒

### Long-open issues
- [ersilia-gui #24](https://github.com/ersilia-os/ersilia-gui/issues/24) — **Connect to DynamoDB to store model results** · open 1209d · last activity 588d ago · @jaydenpersonnat 🕒
- [ersilia-gui #26](https://github.com/ersilia-os/ersilia-gui/issues/26) — **API to run** · open 1192d · last activity 1187d ago · @GemmaTuron 🕒
- [ersilia-gui #28](https://github.com/ersilia-os/ersilia-gui/issues/28) — **Small tweaks to GUI** · open 1192d · last activity 1183d ago · @GemmaTuron 🕒
- [ersilia #1147](https://github.com/ersilia-os/ersilia/issues/1147) — **🐅 Epic: Adding support for Authentication in Ersilia** · open 867d · last activity 49d ago · @DhanshreeA 🕒
- [west-africa-mtb-lineage-drug-responses #1](https://github.com/ersilia-os/west-africa-mtb-lineage-drug-responses/issues/1) — **Meeting minutes 2024-08-15** · open 795d · last activity 783d ago · @fafaal3107 🕒
- [west-africa-mtb-lineage-drug-responses #2](https://github.com/ersilia-os/west-africa-mtb-lineage-drug-responses/issues/2) — **Meeting minutes 2024-08-22** · open 784d · last activity 782d ago · @fafaal3107 🕒
- [west-africa-mtb-lineage-drug-responses #3](https://github.com/ersilia-os/west-africa-mtb-lineage-drug-responses/issues/3) — **Meeting minutes 29/08/2024** · open 777d · last activity 777d ago · @fafaal3107 🕒
- [west-africa-mtb-lineage-drug-responses #4](https://github.com/ersilia-os/west-africa-mtb-lineage-drug-responses/issues/4) — **Meeting_minutes_05092024** · open 769d · last activity 769d ago · @fafaal3107 🕒
- [west-africa-mtb-lineage-drug-responses #5](https://github.com/ersilia-os/west-africa-mtb-lineage-drug-responses/issues/5) — **Meeting_minutes_03/10/2024** · open 745d · last activity 745d ago · @fafaal3107 🕒
- [aws-utils #8](https://github.com/ersilia-os/aws-utils/issues/8) — **Launch Bastion host** · open 708d · last activity 567d ago · @IamEddie 🕒

_…and 84 more open issues (94 open in total)._

### 💡 Easy wins
- [ersilia-mcp #49](https://github.com/ersilia-os/ersilia-mcp/issues/49) — **🐛 Bug: predict can overwrite its input file** · guard one output path · @ECD5A
- [ersilia #1942](https://github.com/ersilia-os/ersilia/issues/1942) — **Update remaining LazyQSAR models to v3.6.3** · repeat a pinned version bump · @arnaucoma24

## 🔧 Registry alignment

2 missing · 0 ghost · 4 status · 3 type · 14 uncurated.

### Missing from registry
- [h3d-mtb-models-round2](https://github.com/ersilia-os/h3d-mtb-models-round2) — in GitHub, not in the Repositories table
- [lazy-sim](https://github.com/ersilia-os/lazy-sim) — in GitHub, not in the Repositories table

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
- `ersilia-model-workflows` — marked Completed but had activity this week
- `ersilia-pack` — marked Completed but had activity this week
- `ersilia-self-service` — marked Completed but had activity this week
- `lazy-qsar` — marked Completed but had activity this week
- `tuimux` — marked Completed but had activity this week

## 📊 Repository overview
185 tracked repos (264 model packages tracked separately) · 46 archived.  
**By type:** Analysis 68 · Package 67 · Automation 13 · Workshop 11 · App 7 · Template 5 · Documentation 3 · unset 12  
**By status:** Completed 78 · In progress 41 · Archived 19 · Discontinued 17 · Idle 14 · Todo 4 · unset 12  

## ✅ Recent activity

### Pull requests merged
- [ersilia-mcp #60](https://github.com/ersilia-os/ersilia-mcp/pull/60) — **Add a tool to write to the isaura store** · @Lehcar · 2026-10-15
- [ersilia-mcp #63](https://github.com/ersilia-os/ersilia-mcp/pull/63) — **Add isaura persist and remove operations** · @Lehcar · 2026-10-16
- [ersilia-mcp #64](https://github.com/ersilia-os/ersilia-mcp/pull/64) — **Codespace config for qwen** · @Lehcar · 2026-10-16
- [ersilia-skills #47](https://github.com/ersilia-os/ersilia-skills/pull/47) — **model-incorporation-release: new skill for the post-merge release step** · @TiagoJanela · 2026-10-16
- [lazy-qsar #53](https://github.com/ersilia-os/lazy-qsar/pull/53) — **Smooth rank between anchors (3.7.0)** · @miquelduranfrigola · 2026-10-20
- [mtb-public-models #2](https://github.com/ersilia-os/mtb-public-models/pull/2) — **Serve with lazyqsar 3.6.3 and add SIF build/validation workflows** · @GemmaTuron · 2026-10-17
- [tcolf-antimalarials #93](https://github.com/ersilia-os/tcolf-antimalarials/pull/93) — **tmp/37: refactor the stage-37 analysis into a package (outputs byte-identical)** · @TiagoJanela · 2026-10-13
- [tcolf-antimalarials #94](https://github.com/ersilia-os/tcolf-antimalarials/pull/94) — **tools: regenerate the chemotype panel (order drift vs chemotypes_final.csv)** · @TiagoJanela · 2026-10-13
- [tcolf-antimalarials #95](https://github.com/ersilia-os/tcolf-antimalarials/pull/95) — **tmp/37: tool and record of the out/ rename to the registry names** · @TiagoJanela · 2026-10-13
- [tcolf-antimalarials #96](https://github.com/ersilia-os/tcolf-antimalarials/pull/96) — **tools: regenerate the chemotype similarity reference (order drift, companion of #94)** · @TiagoJanela · 2026-10-13
- [tcolf-antimalarials #97](https://github.com/ersilia-os/tcolf-antimalarials/pull/97) — **tmp/37: chemotype class order aligned with the panel; class samples seeded by class name** · @TiagoJanela · 2026-10-13
- [tcolf-antimalarials #98](https://github.com/ersilia-os/tcolf-antimalarials/pull/98) — **tmp/37: liabilities family (37_12), structural-alert flags of the screening candidates** · @TiagoJanela · 2026-10-14
- [tcolf-antimalarials #99](https://github.com/ersilia-os/tcolf-antimalarials/pull/99) — **tmp/37: screening dashboard (Dash): views, prediction context, library bundles** · @TiagoJanela · 2026-10-19
- [tcolf-antimalarials #100](https://github.com/ersilia-os/tcolf-antimalarials/pull/100) — **screening: move the stage-37 pilot to src/screening and scripts/07a-07k (stage 07, PR 1)** · @TiagoJanela · 2026-10-16
- [tcolf-antimalarials #101](https://github.com/ersilia-os/tcolf-antimalarials/pull/101) — **screening: the open review fixes (stage 07, PR 2)** · @TiagoJanela · 2026-10-16
- [tcolf-antimalarials #102](https://github.com/ersilia-os/tcolf-antimalarials/pull/102) 📄 — **stage 07 PR 3: docs, indexes and the graduation marks** · @TiagoJanela · 2026-10-16
- [tcolf-antimalarials #103](https://github.com/ersilia-os/tcolf-antimalarials/pull/103) — **screening: import chemutils lazily (stage 07 follow-up)** · @TiagoJanela · 2026-10-16
- [tcolf-antimalarials #104](https://github.com/ersilia-os/tcolf-antimalarials/pull/104) — **review: REVIEW.md, PR template, verify-before-PR table, Copilot on open only** · @TiagoJanela · 2026-10-19
- [tcolf-antimalarials #105](https://github.com/ersilia-os/tcolf-antimalarials/pull/105) — **screening: liabilities writes the Lipinski H-bond counts (version-stable)** · @TiagoJanela · 2026-10-19
- [tcolf-antimalarials #106](https://github.com/ersilia-os/tcolf-antimalarials/pull/106) — **screening: chirality-aware library ECFP4 and chemotype similarity** · @TiagoJanela · 2026-10-19
- [tcolf-antimalarials #107](https://github.com/ersilia-os/tcolf-antimalarials/pull/107) 📄 — **docs: commit policy, the tmp/39 TabPFN write-up, refactor record and notes** · @TiagoJanela · 2026-10-19
- [tcolf-antimalarials #108](https://github.com/ersilia-os/tcolf-antimalarials/pull/108) — **tmp/47: DR max-padding experiment (sandbox)** · @TiagoJanela · 2026-10-19
- [tcolf-antimalarials #109](https://github.com/ersilia-os/tcolf-antimalarials/pull/109) — **tmp/48: novel Enamine library through the stage-07 pipeline** · @TiagoJanela · 2026-10-19
- [tcolf-antimalarials #110](https://github.com/ersilia-os/tcolf-antimalarials/pull/110) — **dashboard: chirality-aware fingerprints, like the training data** · @TiagoJanela · 2026-10-19
- [tcolf-antimalarials #111](https://github.com/ersilia-os/tcolf-antimalarials/pull/111) — **log: carry over entries of 2026-10-15 to 2026-10-19** · @TiagoJanela · 2026-10-19
- [tcolf-antimalarials #112](https://github.com/ersilia-os/tcolf-antimalarials/pull/112) — **gitignore: tmp/\*\*/out/ is generated, not source** · @TiagoJanela · 2026-10-19
- [tcolf-antimalarials #113](https://github.com/ersilia-os/tcolf-antimalarials/pull/113) — **dashboard: harmonised Map labels, concise scaffold cards, Models heatmap labels** · @TiagoJanela · 2026-10-19
- [tcolf-antimalarials #114](https://github.com/ersilia-os/tcolf-antimalarials/pull/114) 📄 — **docs: experiment log entries of 2026-10-19** · @TiagoJanela · 2026-10-19
- [tcolf-antimalarials #115](https://github.com/ersilia-os/tcolf-antimalarials/pull/115) — **dashboard: shared core of a pair no longer collapses to a methyl when the search is cut short** · @TiagoJanela · 2026-10-19
- [tcolf-antimalarials #116](https://github.com/ersilia-os/tcolf-antimalarials/pull/116) — **dashboard: name the signal 'Training similarity' (eosquality wording)** · @TiagoJanela · 2026-10-19
- [tcolf-antimalarials #117](https://github.com/ersilia-os/tcolf-antimalarials/pull/117) — **tools: block gh pr create/ready until the branch review is recorded** · @TiagoJanela · 2026-10-19
- [tcolf-chemical-libraries #1](https://github.com/ersilia-os/tcolf-chemical-libraries/pull/1) — **Add Enamine library pipeline and final library table** · @TiagoJanela · 2026-10-14

### Pull requests opened
- [ersilia-pack #93](https://github.com/ersilia-os/ersilia-pack/pull/93) — **Warm serving: keep migrated models loaded between batches** · @SoufianeAatab · 2026-10-15
- [ersilia-pack #94](https://github.com/ersilia-os/ersilia-pack/pull/94) — **Warm serving: keep migrated models loaded between batches** · @SoufianeAatab · 2026-10-16
- [ersilia-skills #49](https://github.com/ersilia-os/ersilia-skills/pull/49) — **Model incorporation: PR and merge skill, request checks, eosvc-only checkpoints** · @arnaucoma24 · 2026-10-16
- [tuimux #10](https://github.com/ersilia-os/tuimux/pull/10) — **Make the dashboard responsive over high-latency tailnets** · @miquelduranfrigola · 2026-10-20
- [zairachem-docker #67](https://github.com/ersilia-os/zairachem-docker/pull/67) 🔧 — **build(deps): bump onnx from 1.22.0 to 1.23.2** · @dependabot[bot] · 2026-10-13
- [zairachem-docker #68](https://github.com/ersilia-os/zairachem-docker/pull/68) 🔧 — **build(deps): bump rdkit from 2024.3.6 to 2026.9.1** · @dependabot[bot] · 2026-10-13

_The other 30 PRs opened this week were merged in the same window and are listed above._

### Issues closed
- [ersilia #1914](https://github.com/ersilia-os/ersilia/issues/1914) — **🦠 Model Request: CapMolPred** · @arnaucoma24 · 2026-10-15
- [ersilia #1940](https://github.com/ersilia-os/ersilia/issues/1940) — **🦠 Model Request: ANNalog Scaffold Hopping** · @arnaucoma24 · 2026-10-16
- [ersilia #1941](https://github.com/ersilia-os/ersilia/issues/1941) — **🦠 Model Request: Human Liver Microsome Half-Life (PredHLM)** · @TiagoJanela · 2026-10-15

### Issues opened
- [ersilia #1940](https://github.com/ersilia-os/ersilia/issues/1940) — **🦠 Model Request: ANNalog Scaffold Hopping** · @arnaucoma24 · 2026-10-14
- [ersilia #1941](https://github.com/ersilia-os/ersilia/issues/1941) — **🦠 Model Request: Human Liver Microsome Half-Life (PredHLM)** · @TiagoJanela · 2026-10-15
- [ersilia #1942](https://github.com/ersilia-os/ersilia/issues/1942) — **Update remaining LazyQSAR models to v3.6.3** · @arnaucoma24 · 2026-10-19
- [ersilia #1943](https://github.com/ersilia-os/ersilia/issues/1943) — **🦠 Model Request: Ersilia Reference Library Similarity** · @arnaucoma24 · 2026-10-19
- [ersilia #1944](https://github.com/ersilia-os/ersilia/issues/1944) — **🦠 Model Request: MtbAIM Antitubercular Activity** · @arnaucoma24 · 2026-10-20
- [ersilia-model-workflows #8](https://github.com/ersilia-os/ersilia-model-workflows/issues/8) 🐛 — **Slack "new issue" notifier fails in all model repos: archived announcements channel** · @arnaucoma24 · 2026-10-15
- [ersilia-self-service #486](https://github.com/ersilia-os/ersilia-self-service/issues/486)–[#493](https://github.com/ersilia-os/ersilia-self-service/issues/493) — **🚀 Model Inference Run 🤖 eos9f7c: Permeation of compounds across the outer membrane of P. aeruginosa** · 8 run requests · @miquelduranfrigola · 2026-10-15 to 2026-10-16

**Model repos (eosXXXX):** 4 PRs merged · 5 opened · 15 issues closed · 4 opened — across 39 repos. Managed via the model-incorporation flow.
