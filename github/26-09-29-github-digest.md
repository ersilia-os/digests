# Ersilia GitHub Digest — Week of 2026-09-29

**Connectors:** GitHub 🟢 · Airtable 🟢  
**Markers:** 🐛 Bug · ✨ Feature · 📄 Docs · 🔧 Infra · 🕒 Stale  

## ✨ Highlights
Busiest on `ersilia` (21 events) and `tcolf-antimalarials` (16). `ersilia` merged a run of CLI hardening PRs, the most important being safe concurrent sessions for the same model across terminals (#1929), alongside friendly errors, performance work and a cleanup of orphaned model servers. `tcolf-antimalarials` merged eight PRs, including TabPFN as a fourth model family (#58). Registry drift is up: 9 repos missing, 4 ghost records (two look like renames) and 7 Status/Type mismatches.

## ⚠️ Needs attention

### Stale pull requests
- [ersilia-stats-capstone #140](https://github.com/ersilia-os/ersilia-stats-capstone/pull/140) — **Static HTML site: "Ersilia in numbers" + GitHub Pages deploy** · open 63d · last activity 63d ago · @miquelduranfrigola 🕒
- [ersilia-stats-capstone #139](https://github.com/ersilia-os/ersilia-stats-capstone/pull/139) — **Add initial Airtable data snapshots + restrict fetch to app tables** · open 63d · last activity 63d ago · @miquelduranfrigola 🕒
- [ersilia-model-request-app #64](https://github.com/ersilia-os/ersilia-model-request-app/pull/64) — **Fix React Server Components CVE vulnerabilities** · open 200d · last activity 60d ago · @vercel[bot] 🕒

### Long-open issues
- [ersilia-gui #24](https://github.com/ersilia-os/ersilia-gui/issues/24) — **Connect to DynamoDB to store model results** · open 1188d · last activity 566d ago · @jaydenpersonnat 🕒
- [ersilia-gui #28](https://github.com/ersilia-os/ersilia-gui/issues/28) — **Small tweaks to GUI** · open 1171d · last activity 1161d ago · @GemmaTuron 🕒
- [ersilia-gui #26](https://github.com/ersilia-os/ersilia-gui/issues/26) — **API to run** · open 1171d · last activity 1166d ago · @GemmaTuron 🕒
- [ersilia #1147](https://github.com/ersilia-os/ersilia/issues/1147) — **Epic: Adding support for Authentication in Ersilia** · open 845d · last activity 27d ago · @DhanshreeA
- [west-africa-mtb-lineage-drug-responses #1](https://github.com/ersilia-os/west-africa-mtb-lineage-drug-responses/issues/1) — **Meeting minutes 2024-08-15** · open 773d · last activity 761d ago · @fafaal3107 🕒
- [west-africa-mtb-lineage-drug-responses #2](https://github.com/ersilia-os/west-africa-mtb-lineage-drug-responses/issues/2) — **Meeting minutes 2024-08-22** · open 762d · last activity 760d ago · @fafaal3107 🕒
- [west-africa-mtb-lineage-drug-responses #3](https://github.com/ersilia-os/west-africa-mtb-lineage-drug-responses/issues/3) — **Meeting minutes 29/08/2024** · open 756d · last activity 756d ago · @fafaal3107 🕒
- [west-africa-mtb-lineage-drug-responses #4](https://github.com/ersilia-os/west-africa-mtb-lineage-drug-responses/issues/4) — **Meeting_minutes_05092024** · open 747d · last activity 747d ago · @fafaal3107 🕒
- [west-africa-mtb-lineage-drug-responses #5](https://github.com/ersilia-os/west-africa-mtb-lineage-drug-responses/issues/5) — **Meeting_minutes_03/10/2024** · open 724d · last activity 724d ago · @fafaal3107 🕒
- [aws-utils #8](https://github.com/ersilia-os/aws-utils/issues/8) — **Launch Bastion host** · open 686d · last activity 546d ago · @IamEddie 🕒
_…and 46 more open issues (56 open in total)._

### 💡 Easy wins
- [ub-cedd-projects-workshop #1](https://github.com/ersilia-os/ub-cedd-projects-workshop/issues/1) — **push prediction results file** · push one missing CSV · @JudeBetow

## 🔧 Registry alignment

9 missing · 4 ghost · 4 status · 3 type · 0 uncurated.

### Missing from registry
- [chemicl](https://github.com/ersilia-os/chemicl) — in GitHub, not in the Repositories table
- [gradi-ai-data-working-group](https://github.com/ersilia-os/gradi-ai-data-working-group) — in GitHub, not in the Repositories table
- [lazy-chemvis-paper](https://github.com/ersilia-os/lazy-chemvis-paper) — in GitHub, not in the Repositories table
- [model-launcher](https://github.com/ersilia-os/model-launcher) — in GitHub, not in the Repositories table
- [mtb-trna-synthetases-screening](https://github.com/ersilia-os/mtb-trna-synthetases-screening) — in GitHub, not in the Repositories table
- [pathogen-pocketome](https://github.com/ersilia-os/pathogen-pocketome) — in GitHub, not in the Repositories table
- [rafiki-workshop-2026](https://github.com/ersilia-os/rafiki-workshop-2026) — in GitHub, not in the Repositories table
- [tcolf-chemical-libraries](https://github.com/ersilia-os/tcolf-chemical-libraries) — in GitHub, not in the Repositories table
- [ub-cedd-projects-workshop](https://github.com/ersilia-os/ub-cedd-projects-workshop) — in GitHub, not in the Repositories table

### Ghost records
- `chem-icl` — in the registry (status In progress) but no longer in the org (possibly renamed to `chemicl`)
- `mtb-targeted-protein-degradation` — in the registry (status In progress) but no longer in the org (renamed/deleted)
- `rafiki-workshop` — in the registry (status Completed) but no longer in the org (possibly renamed to `rafiki-workshop-2026`)
- `slack` — in the registry (status Discontinued) but no longer in the org (renamed/deleted)

### Status / Type mismatches
- `chembl-binary-tasks` — Status: Airtable «Completed, Archived» vs GitHub «Completed»
- `ersilia-stats-capstone` — Status: Airtable «Archived» vs GitHub «In progress»
- `h3d-mtb-metabolism` — Status: Airtable «Completed, Archived» vs GitHub «Completed»
- `zaira-chem-tdc-benchmark` — Status: Airtable «Completed, Archived» vs GitHub «Completed»
- `eosbench` — Type: Airtable «App, Package» vs GitHub «Package»
- `ersilia-stats-capstone` — Type: Airtable «Analysis, App» vs GitHub «Analysis»
- `gradi-target-prioritization` — Type: Airtable «Analysis, App» vs GitHub «Analysis»

### Possibly out of date
- `ersilia` — marked Completed but had activity this week
- `lazy-qsar` — marked Completed but had activity this week

## 📊 Repository overview
182 tracked repos (259 model packages tracked separately) · 46 archived.  
**By type:** Analysis 68 · Package 66 · Automation 13 · Workshop 11 · App 7 · Template 5 · Documentation 3 · unset 10  
**By status:** Completed 77 · In progress 42 · Archived 18 · Discontinued 17 · Idle 14 · Todo 4 · unset 10  

## ✅ Recent activity

### Pull requests merged
- [ersilia #1924](https://github.com/ersilia-os/ersilia/pull/1924) 🐛 — **fix: kill orphaned model servers and stream large run output to disk** · @Marina18 · 2026-09-23
- [ersilia #1927](https://github.com/ersilia-os/ersilia/pull/1927) — **Performance improvements for run/serve/close** · @miquelduranfrigola · 2026-09-28
- [ersilia #1928](https://github.com/ersilia-os/ersilia/pull/1928) — **Friendly errors instead of tracebacks for serve/info/close** · @miquelduranfrigola · 2026-09-28
- [ersilia #1929](https://github.com/ersilia-os/ersilia/pull/1929) — **Make concurrent sessions safe, including the same model in several terminals** · @miquelduranfrigola · 2026-09-28
- [ersilia #1930](https://github.com/ersilia-os/ersilia/pull/1930) — **One consistent, clean style for CLI messages** · @miquelduranfrigola · 2026-09-29
- [ersilia-mcp #45](https://github.com/ersilia-os/ersilia-mcp/pull/45) ✨ — **Add an Isaura inspect tool** · @Lehcar · 2026-09-23
- [ersilia-mcp #46](https://github.com/ersilia-os/ersilia-mcp/pull/46) 📄 — **Update installation instructions** · @Lehcar · 2026-09-22
- [isaura #23](https://github.com/ersilia-os/isaura/pull/23) 🐛 — **fix: pin MinIO image to quay.io release** · @Marina18 · 2026-09-23
- [tcolf-antimalarials #52](https://github.com/ersilia-os/tcolf-antimalarials/pull/52) — **06c: parse the full model name from a prediction filename, not the first token** · @TiagoJanela · 2026-09-25
- [tcolf-antimalarials #53](https://github.com/ersilia-os/tcolf-antimalarials/pull/53) — **figures: rotate bar value labels at 4+ models, and scale the panel letter with the fonts** · @TiagoJanela · 2026-09-25
- [tcolf-antimalarials #54](https://github.com/ersilia-os/tcolf-antimalarials/pull/54) — **05a: emit the four strain-resolvable sidelined sets at (strain, depositor) grain too** · @TiagoJanela · 2026-09-25
- [tcolf-antimalarials #55](https://github.com/ersilia-os/tcolf-antimalarials/pull/55) — **06m: say when a model is drawn on only some strains, and give each arm its own legend** · @TiagoJanela · 2026-09-25
- [tcolf-antimalarials #56](https://github.com/ersilia-os/tcolf-antimalarials/pull/56) — **06a: refuse to collect a result twice; 06n: build the fade from any palette colour** · @TiagoJanela · 2026-09-25
- [tcolf-antimalarials #57](https://github.com/ersilia-os/tcolf-antimalarials/pull/57) — **stage00: add a stacked 2x1 layout for 00i** · @TiagoJanela · 2026-09-25
- [tcolf-antimalarials #58](https://github.com/ersilia-os/tcolf-antimalarials/pull/58) ✨ — **TabPFN as a fourth model family, the stage-07 persistence seam, and the ERL screening stage** · @TiagoJanela · 2026-09-25
- [tcolf-antimalarials #59](https://github.com/ersilia-os/tcolf-antimalarials/pull/59) 📄 — **stage04: move the documentation out of the scripts, and consolidate the rules it described** · @TiagoJanela · 2026-09-25

### Pull requests opened
- [ersilia #1923](https://github.com/ersilia-os/ersilia/pull/1923) — **Stop the model server child process in ersilia close** · @DrVelvetFog · 2026-09-22
- [ersilia #1931](https://github.com/ersilia-os/ersilia/pull/1931) — **Python API: mirror the CLI and behave like a library** · @miquelduranfrigola · 2026-09-26
- [ersilia #1932](https://github.com/ersilia-os/ersilia/pull/1932) 📄 — **docs/revamp** · @miquelduranfrigola · 2026-09-26
- [ersilia-mcp #48](https://github.com/ersilia-os/ersilia-mcp/pull/48) 🔧 — **Remove image retag step** · @Lehcar · 2026-09-27
- [lazy-qsar #47](https://github.com/ersilia-os/lazy-qsar/pull/47) ✨ — **Feat/reference library ranks** · @GemmaTuron · 2026-09-22
_Plus 14 opened and merged in the window (listed above)._

### Issues closed
- [ersilia #1844](https://github.com/ersilia-os/ersilia/issues/1844) 🐛 — **Bug: Loading in memory when preparing output** · @GemmaTuron · 2026-09-23
- [ersilia #1921](https://github.com/ersilia-os/ersilia/issues/1921) 🐛 — **Bug: ersilia close doesn't kill the served process** · @arnaucoma24 · 2026-09-23
- [ersilia #1926](https://github.com/ersilia-os/ersilia/issues/1926) — **Model Request: Route-Based Synthesizability Score** · @TiagoJanela · 2026-09-28

### Issues opened
- [ersilia #1922](https://github.com/ersilia-os/ersilia/issues/1922) — **Model Request: Ensemble-Conditioned Molecular Design** · @arnaucoma24 · 2026-09-22
- [ersilia #1925](https://github.com/ersilia-os/ersilia/issues/1925) — **Model Request: TransPharmer Pharmacophore-Informed Molecule Generation** · @arnaucoma24 · 2026-09-24
- [ersilia #1933](https://github.com/ersilia-os/ersilia/issues/1933) — **Model Request: CReM Growth-Based Structure Generation** · @arnaucoma24 · 2026-09-28
- [ub-cedd-projects-workshop #1](https://github.com/ersilia-os/ub-cedd-projects-workshop/issues/1) — **push prediction results file** · @JudeBetow · 2026-09-26
_Plus #1921 and #1926, opened and closed in the window (listed above)._

**Model repos (eosXXXX):** 7 PRs merged · 10 opened · 1 issues closed · 2 opened — across 27 repos. Managed via the model-incorporation flow.
