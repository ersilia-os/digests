# Ersilia GitHub Digest — Week of 2026-10-28

**Connectors:** GitHub 🟢 · Airtable 🟢  
**Markers:** 🐛 Bug · ✨ Feature · 📄 Docs · 🔧 Infra · 🕒 Stale  

## ✨ Highlights
`tcolf-antimalarials` again led the week with 24 merged PRs, mostly moving the screening dashboard into `src/dashboard` and adding MCS and nearest-neighbour views. `olinda` now featurizes through RDKit compiled to WebAssembly, which drops `rdkit` from every install and adds a web page that runs olinda models in the browser (#22, #25). `lazy-qsar` refactored to one core shared by classification and regression and shipped a regression portfolio for 3.8.0 (#60, #61). The registry has 1 repo missing, 6 Status/Type mismatches and 8 uncurated records, and 5 repos marked Completed were active this week.

## ⚠️ Needs attention

### Stale pull requests
- [ersilia-model-request-app #64](https://github.com/ersilia-os/ersilia-model-request-app/pull/64) — **Fix React Server Components CVE vulnerabilities** · open 229d · last activity 90d ago · @vercel[bot] 🕒
- [ersilia-stats-capstone #139](https://github.com/ersilia-os/ersilia-stats-capstone/pull/139) — **Add initial Airtable data snapshots + restrict fetch to app tables** · open 92d · last activity 92d ago · @miquelduranfrigola 🕒
- [ersilia-stats-capstone #140](https://github.com/ersilia-os/ersilia-stats-capstone/pull/140) — **Static HTML site: "Ersilia in numbers" + GitHub Pages deploy** · open 92d · last activity 92d ago · @miquelduranfrigola 🕒

### Long-open issues
- [ersilia-gui #24](https://github.com/ersilia-os/ersilia-gui/issues/24) — **Connect to DynamoDB to store model results** · open 1217d · last activity 595d ago · @jaydenpersonnat 🕒
- [ersilia-gui #26](https://github.com/ersilia-os/ersilia-gui/issues/26) — **API to run** · open 1200d · last activity 1195d ago · @GemmaTuron 🕒
- [ersilia-gui #28](https://github.com/ersilia-os/ersilia-gui/issues/28) — **Small tweaks to GUI** · open 1200d · last activity 1191d ago · @GemmaTuron 🕒
- [ersilia #1147](https://github.com/ersilia-os/ersilia/issues/1147) — **🐅 Epic: Adding support for Authentication in Ersilia** · open 874d · last activity 56d ago · @DhanshreeA 🕒
- [west-africa-mtb-lineage-drug-responses #1](https://github.com/ersilia-os/west-africa-mtb-lineage-drug-responses/issues/1) — **Meeting minutes 2024-08-15** · open 802d · last activity 791d ago · @fafaal3107 🕒
- [west-africa-mtb-lineage-drug-responses #2](https://github.com/ersilia-os/west-africa-mtb-lineage-drug-responses/issues/2) — **Meeting minutes 2024-08-22** · open 791d · last activity 790d ago · @fafaal3107 🕒
- [west-africa-mtb-lineage-drug-responses #3](https://github.com/ersilia-os/west-africa-mtb-lineage-drug-responses/issues/3) — **Meeting minutes 29/08/2024** · open 785d · last activity 785d ago · @fafaal3107 🕒
- [west-africa-mtb-lineage-drug-responses #4](https://github.com/ersilia-os/west-africa-mtb-lineage-drug-responses/issues/4) — **Meeting_minutes_05092024** · open 776d · last activity 776d ago · @fafaal3107 🕒
- [west-africa-mtb-lineage-drug-responses #5](https://github.com/ersilia-os/west-africa-mtb-lineage-drug-responses/issues/5) — **Meeting_minutes_03/10/2024** · open 753d · last activity 753d ago · @fafaal3107 🕒
- [aws-utils #8](https://github.com/ersilia-os/aws-utils/issues/8) — **Launch Bastion host** · open 715d · last activity 575d ago · @IamEddie 🕒

_…and 102 more open issues (112 open in total)._

### 💡 Easy wins
- [isaura #29](https://github.com/ersilia-os/isaura/issues/29) — **IsauraReader.read(df=...) returns the first call's rows on every later call** · cause already pinned to one cache · @miquelduranfrigola
- [ersilia-mcp #49](https://github.com/ersilia-os/ersilia-mcp/issues/49) — **🐛 Bug: predict can overwrite its input file** · guard one output path · @ECD5A
- [ersilia #1942](https://github.com/ersilia-os/ersilia/issues/1942) — **Update remaining LazyQSAR models to v3.6.3** · repeat a pinned version bump · @arnaucoma24

## 🔧 Registry alignment

1 missing · 0 ghost · 3 status · 3 type · 16 uncurated.

### Missing from registry
- [h3d-mtb-models-round2](https://github.com/ersilia-os/h3d-mtb-models-round2) — in GitHub, not in the Repositories table

### Status / Type mismatches
- `chembl-binary-tasks` — Status: Airtable «Completed, Archived» vs GitHub «Completed»
- `h3d-mtb-metabolism` — Status: Airtable «Completed, Archived» vs GitHub «Completed»
- `zaira-chem-tdc-benchmark` — Status: Airtable «Completed, Archived» vs GitHub «Completed»
- `eosbench` — Type: Airtable «App, Package» vs GitHub «Package»
- `ersilia-stats-capstone` — Type: Airtable «Analysis, App» vs GitHub «Analysis»
- `gradi-target-prioritization` — Type: Airtable «Analysis, App» vs GitHub «Analysis»

### Needs curation
- `gradi-ai-data-working-group` — no Status, no Type
- `lazy-chemvis-paper` — no Status, no Type
- `lazy-sim` — no Status, no Type
- `model-launcher` — no Status, no Type
- `molecule-grids` — no Status, no Type
- `pathogen-pocketome` — no Status, no Type
- `tcolf-chemical-libraries` — no Status, no Type
- `ub-cedd-projects-workshop` — no Status, no Type

### Possibly out of date
- `eos-template` — marked Completed but had activity this week
- `ersilia` — marked Completed but had activity this week
- `ersilia-self-service` — marked Completed but had activity this week
- `lazy-qsar` — marked Completed but had activity this week
- `tuimux` — marked Completed but had activity this week

## 📊 Repository overview
185 tracked repos (269 model packages tracked separately) · 46 archived.  
**By type:** Analysis 68 · Package 67 · Automation 13 · Workshop 11 · App 7 · Template 5 · Documentation 3 · unset 12  
**By status:** Completed 78 · In progress 42 · Archived 19 · Discontinued 17 · Idle 14 · Todo 3 · unset 12  

## ✅ Recent activity

### Pull requests merged
- [chemicl #18](https://github.com/ersilia-os/chemicl/pull/18) — **Streamline chemicl setup and recommend workflow with 3-bucket selecti…** · @OhhMoo · 2026-10-22
- [eos-template #96](https://github.com/ersilia-os/eos-template/pull/96) — **Keep checkpoints and training data in git unless a file is over 100 MB** · @arnaucoma24 · 2026-10-22
- [ersilia-skills #45](https://github.com/ersilia-os/ersilia-skills/pull/45) — **Add the org-context skill** · @miquelduranfrigola · 2026-10-21
- [ersilia-skills #48](https://github.com/ersilia-os/ersilia-skills/pull/48) — **Add model-optimization skill** · @SoufianeAatab · 2026-10-21
- [ersilia-skills #49](https://github.com/ersilia-os/ersilia-skills/pull/49) — **Model incorporation: PR and merge skill, request checks, eosvc-only checkpoints** · @arnaucoma24 · 2026-10-21
- [ersilia-skills #51](https://github.com/ersilia-os/ersilia-skills/pull/51) — **Model incorporation: checkpoints and training data in git unless a file is over 100 MB** · @arnaucoma24 · 2026-10-22
- [lazy-qsar #57](https://github.com/ersilia-os/lazy-qsar/pull/57) 🐛 — **Fix fit scratch deletion and host logging takeover** · @miquelduranfrigola · 2026-10-21
- [lazy-qsar #58](https://github.com/ersilia-os/lazy-qsar/pull/58) 🐛 — **Fix: small datasets fail to fit (applicability domain)** · @miquelduranfrigola · 2026-10-21
- [lazy-qsar #59](https://github.com/ersilia-os/lazy-qsar/pull/59) — **Regression heads: fix linear, XGBoost, SVR and RF; add regression benchmark harness** · @miquelduranfrigola · 2026-10-21
- [lazy-qsar #60](https://github.com/ersilia-os/lazy-qsar/pull/60) — **Refactor: one task-neutral core shared by classification and regression** · @miquelduranfrigola · 2026-10-22
- [lazy-qsar #61](https://github.com/ersilia-os/lazy-qsar/pull/61) — **Regression portfolio v2: benchmark-selected heads, stacking, intervals; SVM ONNX budgets** · @miquelduranfrigola · 2026-10-22
- [lazy-qsar #62](https://github.com/ersilia-os/lazy-qsar/pull/62) 📄 — **docs: everything since 3.7.0 ships as 3.8.0** · @miquelduranfrigola · 2026-10-22
- [olinda #20](https://github.com/ersilia-os/olinda/pull/20) — **Speed up fit and predict** · @miquelduranfrigola · 2026-10-21
- [olinda #21](https://github.com/ersilia-os/olinda/pull/21) — **Restore the footer logo, add a command table, and use the canonical footer wording** · @miquelduranfrigola · 2026-10-21
- [olinda #22](https://github.com/ersilia-os/olinda/pull/22) — **Featurize through RDKit compiled to WebAssembly, and drop rdkit from every install** · @miquelduranfrigola · 2026-10-21
- [olinda #23](https://github.com/ersilia-os/olinda/pull/23) — **Compute qmfp from folded counts in the WebAssembly wrapper** · @miquelduranfrigola · 2026-10-21
- [olinda #24](https://github.com/ersilia-os/olinda/pull/24) — **Store exact Morgan counts in 4 bits instead of RDKit's count simulation** · @miquelduranfrigola · 2026-10-21
- [olinda #25](https://github.com/ersilia-os/olinda/pull/25) — **Add a raw web page that runs olinda models in the browser** · @miquelduranfrigola · 2026-10-21
- [olinda #26](https://github.com/ersilia-os/olinda/pull/26) — **Add an example model to the web page** · @miquelduranfrigola · 2026-10-21
- [olinda #27](https://github.com/ersilia-os/olinda/pull/27) — **Stamp the web page's files per build so browser caches cannot mix deploys** · @miquelduranfrigola · 2026-10-21
- [olinda #28](https://github.com/ersilia-os/olinda/pull/28) — **Redraw the model.onnx diagram for 1.3 and shrink the README logo** · @miquelduranfrigola · 2026-10-21
- [tcolf-antimalarials #119](https://github.com/ersilia-os/tcolf-antimalarials/pull/119) — **tmp/48: numbered chain, retire list, intended slide changes (refactor of the Enamine library analysis)** · @TiagoJanela · 2026-10-23
- [tcolf-antimalarials #120](https://github.com/ersilia-os/tcolf-antimalarials/pull/120) — **tmp/48: --park for the promotion tool; docs after the merge and the promotion** · @TiagoJanela · 2026-10-23
- [tcolf-antimalarials #121](https://github.com/ersilia-os/tcolf-antimalarials/pull/121) — **tmp/48: the back-test reads the tmp/40 held-out file from data/tmp, not from another worktree** · @TiagoJanela · 2026-10-26
- [tcolf-antimalarials #122](https://github.com/ersilia-os/tcolf-antimalarials/pull/122) — **README: stage bullets, add Stage 7, move detail to stage overview** · @TiagoJanela · 2026-10-23
- [tcolf-antimalarials #123](https://github.com/ersilia-os/tcolf-antimalarials/pull/123) — **screening: draw training compounds as 04c does (the stage-05 drawing)** · @TiagoJanela · 2026-10-26
- [tcolf-antimalarials #124](https://github.com/ersilia-os/tcolf-antimalarials/pull/124) — **screening: scaffold agreement check compares same-drawing compounds only** · @TiagoJanela · 2026-10-26
- [tcolf-antimalarials #125](https://github.com/ersilia-os/tcolf-antimalarials/pull/125) — **tmp/48: domain slide panel A: all-compounds box, any-of-8 and all-8 points, novel-set population stated** · @TiagoJanela · 2026-10-26
- [tcolf-antimalarials #126](https://github.com/ersilia-os/tcolf-antimalarials/pull/126) — **screening: logD table is written in training_actives_properties order** · @TiagoJanela · 2026-10-26
- [tcolf-antimalarials #127](https://github.com/ersilia-os/tcolf-antimalarials/pull/127) — **tmp/37: training actives' secondary properties recomputed on the 04c drawings (37_23)** · @TiagoJanela · 2026-10-26
- [tcolf-antimalarials #128](https://github.com/ersilia-os/tcolf-antimalarials/pull/128) — **tmp/40 + tmp/50: lq36 AD-validation redo, error models on scalar measures, eosquality scores (isolated)** · @TiagoJanela · 2026-10-26
- [tcolf-antimalarials #129](https://github.com/ersilia-os/tcolf-antimalarials/pull/129) — **tmp/51: error models and descriptor views on the lq36 SP classifiers (isolated study)** · @TiagoJanela · 2026-10-26
- [tcolf-antimalarials #130](https://github.com/ersilia-os/tcolf-antimalarials/pull/130) — **tmp/48: 48_37 PAINS of the full training sets and panel D of the alerts slide** · @TiagoJanela · 2026-10-26
- [tcolf-antimalarials #131](https://github.com/ersilia-os/tcolf-antimalarials/pull/131) — **tmp/48: oracle baseline refreshed for the 04c training drawings** · @TiagoJanela · 2026-10-27
- [tcolf-antimalarials #132](https://github.com/ersilia-os/tcolf-antimalarials/pull/132) 📄 — **docs: experiment log, tmp/48 entries 2026-10-23 to 2026-10-26** · @TiagoJanela · 2026-10-27
- [tcolf-antimalarials #133](https://github.com/ersilia-os/tcolf-antimalarials/pull/133) — **dashboard: MCS table, the shared substructure with the nearest training compounds** · @TiagoJanela · 2026-10-27
- [tcolf-antimalarials #134](https://github.com/ersilia-os/tcolf-antimalarials/pull/134) 📄 — **docs: tmp/48 open items closed, log entries 2026-10-27** · @TiagoJanela · 2026-10-27
- [tcolf-antimalarials #135](https://github.com/ersilia-os/tcolf-antimalarials/pull/135) — **dashboard: Nearest per model on the Neighbours page** · @TiagoJanela · 2026-10-27
- [tcolf-antimalarials #136](https://github.com/ersilia-os/tcolf-antimalarials/pull/136) — **tmp/37: MCS check compares the nearest active only for compounds no model has seen** · @TiagoJanela · 2026-10-27
- [tcolf-antimalarials #137](https://github.com/ersilia-os/tcolf-antimalarials/pull/137) — **dashboard: serve the ERL from its bundle, retire ErlSource (one source)** · @TiagoJanela · 2026-10-27
- [tcolf-antimalarials #138](https://github.com/ersilia-os/tcolf-antimalarials/pull/138) — **dashboard: independent of the library's models, words and the screening package** · @TiagoJanela · 2026-10-27
- [tcolf-antimalarials #139](https://github.com/ersilia-os/tcolf-antimalarials/pull/139) — **dashboard: graduate to src/dashboard, producers in src/dashboard_build, launcher in tools/** · @TiagoJanela · 2026-10-27
- [tcolf-antimalarials #140](https://github.com/ersilia-os/tcolf-antimalarials/pull/140) — **dashboard: clear error for an empty bundle Spec; cb sees list-form Outputs** · @TiagoJanela · 2026-10-28
- [tcolf-antimalarials #141](https://github.com/ersilia-os/tcolf-antimalarials/pull/141) — **dashboard: an active wins a tie in the nearest compound of any label** · @TiagoJanela · 2026-10-28
- [tcolf-antimalarials #142](https://github.com/ersilia-os/tcolf-antimalarials/pull/142) — **log: dashboard robustness (#140), tie rule (#141), dash restart, scratch cleanup** · @TiagoJanela · 2026-10-28
- [tuimux #10](https://github.com/ersilia-os/tuimux/pull/10) — **Make the dashboard responsive over high-latency tailnets** · @miquelduranfrigola · 2026-10-27

### Pull requests opened
- [ersilia #1946](https://github.com/ersilia-os/ersilia/pull/1946) — **Keep the README's two date sentences apart** · @arnaucoma24 · 2026-10-27
- [ersilia-book #3](https://github.com/ersilia-os/ersilia-book/pull/3) — **Checkpoints and training data in git unless a file is over 100 MB** · @arnaucoma24 · 2026-10-22
- [isaura #27](https://github.com/ersilia-os/isaura/pull/27) 🐛 — **fix: make push concurrency configurable and fail when uploads fail** · @arnaucoma24 · 2026-10-22
- [isaura #28](https://github.com/ersilia-os/isaura/pull/28) 🐛 — **fix: pin duckdb below 2** · @arnaucoma24 · 2026-10-22

_The other 42 PRs opened this week were merged in the same window and are listed above._

### Issues closed
- [ersilia #1944](https://github.com/ersilia-os/ersilia/issues/1944) — **🦠 Model Request: MtbAIM Antitubercular Activity** · @arnaucoma24 · 2026-10-22

### Issues opened
- [ersilia #1945](https://github.com/ersilia-os/ersilia/issues/1945) 🐛 — **🐛 Bug: Model README joins the incorporation and packaging dates with no space** · @arnaucoma24 · 2026-10-27
- [ersilia #1947](https://github.com/ersilia-os/ersilia/issues/1947) — **🦠 Model Request: Enamine Hit Locator Similarity** · @arnaucoma24 · 2026-10-27
- [ersilia #1948](https://github.com/ersilia-os/ersilia/issues/1948) — **🦠 Model Request: COCONUT Library Similarity** · @arnaucoma24 · 2026-10-27
- [ersilia #1949](https://github.com/ersilia-os/ersilia/issues/1949) — **🦠 Model Request: Enamine Liquid Stock Similarity** · @arnaucoma24 · 2026-10-27
- [ersilia #1950](https://github.com/ersilia-os/ersilia/issues/1950) — **🦠 Model Request: Molport Library Similarity** · @arnaucoma24 · 2026-10-27
- [ersilia #1951](https://github.com/ersilia-os/ersilia/issues/1951) — **🦠 Model Request: Enamine REAL Sample Similarity** · @arnaucoma24 · 2026-10-27
- [ersilia-self-service #494](https://github.com/ersilia-os/ersilia-self-service/issues/494)–[#497](https://github.com/ersilia-os/ersilia-self-service/issues/497) — **🚀 Model Inference Run** for eos1vms, eos93h2 and eos8fth (×2) · @miquelduranfrigola · 2026-10-24
- [ersilia-self-service #498](https://github.com/ersilia-os/ersilia-self-service/issues/498)–[#505](https://github.com/ersilia-os/ersilia-self-service/issues/505) — **🚀 Model Inference Run 🤖 eos9f7c: Permeation of compounds across the outer membrane of P. aeruginosa** (×8) · @miquelduranfrigola · 2026-10-28
- [ersilia-skills #52](https://github.com/ersilia-os/ersilia-skills/issues/52) — **GitHub Digest check for idle branches** · @miquelduranfrigola · 2026-10-28
- [isaura #29](https://github.com/ersilia-os/isaura/issues/29) — **IsauraReader.read(df=...) returns the first call's rows on every later call (_prepare_read caches its result)** · @miquelduranfrigola · 2026-10-27

**Model repos (eosXXXX):** 2 PRs merged · 2 opened · 1 issues closed · 1 opened — across 25 repos. Managed via the model-incorporation flow.
