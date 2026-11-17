# Ersilia GitHub Digest — Week of 2026-11-17

**Connectors:** GitHub 🟢 · Airtable 🟢  
**Markers:** 🐛 Bug · ✨ Feature · 📄 Docs · 🔧 Infra · 🕒 Stale  

## ✨ Highlights
Busiest repos were `ersilia-self-service` (133 model-inference-run issues opened, up from 15 last week, which lifts open issues to 258), `tcolf-antimalarials` and `tuimux` (12 PRs merged each). The most important change is `lazy-qsar` 3.9.0 (#65), which fixes the CLAMP and CDDD descriptors and was followed by two ONNX export fixes (#67, #69); `tcolf-antimalarials` and `h3d-mtb-bioactivity` have already refitted their models on it. Model repos were unusually active, with 32 PRs merged across 45 repos. Registry has 2 missing repos, 3 Status and 3 Type mismatches, and 8 repos still uncurated.

## ⚠️ Needs attention

### Stale pull requests
- [ersilia-stats-capstone #139](https://github.com/ersilia-os/ersilia-stats-capstone/pull/139) — **Add initial Airtable data snapshots + restrict fetch to app tables** · open 113d · last activity 113d ago · @miquelduranfrigola 🕒
- [ersilia-stats-capstone #140](https://github.com/ersilia-os/ersilia-stats-capstone/pull/140) — **Static HTML site: "Ersilia in numbers" + GitHub Pages deploy** · open 113d · last activity 113d ago · @miquelduranfrigola 🕒
- [ersilia-model-request-app #64](https://github.com/ersilia-os/ersilia-model-request-app/pull/64) — **Fix React Server Components CVE vulnerabilities** · open 250d · last activity 110d ago · @vercel[bot] 🕒
- [ersilia-mcp #50](https://github.com/ersilia-os/ersilia-mcp/pull/50) — **fix(predict): preserve input files when writing results** · open 49d · last activity 49d ago · @ECD5A 🕒
- [ersilia-mcp #41](https://github.com/ersilia-os/ersilia-mcp/pull/41) — **ci(deps): bump actions/setup-python from 5 to 7** · open 82d · last activity 48d ago · @dependabot[bot] 🕒
- [ersilia-mcp #42](https://github.com/ersilia-os/ersilia-mcp/pull/42) — **ci(deps): bump actions/checkout from 4 to 7** · open 82d · last activity 48d ago · @dependabot[bot] 🕒

### Long-open issues
- [ersilia-gui #24](https://github.com/ersilia-os/ersilia-gui/issues/24) — **Connect to DynamoDB to store model results** · open 1237d · last activity 616d ago · @jaydenpersonnat 🕒
- [ersilia-gui #28](https://github.com/ersilia-os/ersilia-gui/issues/28) — **Small tweaks to GUI** · open 1220d · last activity 1211d ago · @GemmaTuron 🕒
- [ersilia-gui #26](https://github.com/ersilia-os/ersilia-gui/issues/26) — **API to run** · open 1220d · last activity 1215d ago · @GemmaTuron 🕒
- [ersilia #1147](https://github.com/ersilia-os/ersilia/issues/1147) — **🐅 Epic: Adding support for Authentication in Ersilia** · open 895d · last activity 77d ago · @DhanshreeA 🕒
- [west-africa-mtb-lineage-drug-responses #1](https://github.com/ersilia-os/west-africa-mtb-lineage-drug-responses/issues/1) — **Meeting minutes 2024-08-15** · open 823d · last activity 811d ago · @fafaal3107 🕒
- [west-africa-mtb-lineage-drug-responses #2](https://github.com/ersilia-os/west-africa-mtb-lineage-drug-responses/issues/2) — **Meeting minutes 2024-08-22** · open 812d · last activity 810d ago · @fafaal3107 🕒
- [west-africa-mtb-lineage-drug-responses #3](https://github.com/ersilia-os/west-africa-mtb-lineage-drug-responses/issues/3) — **Meeting minutes 29/08/2024** · open 805d · last activity 805d ago · @fafaal3107 🕒
- [west-africa-mtb-lineage-drug-responses #4](https://github.com/ersilia-os/west-africa-mtb-lineage-drug-responses/issues/4) — **Meeting_minutes_05092024** · open 797d · last activity 797d ago · @fafaal3107 🕒
- [west-africa-mtb-lineage-drug-responses #5](https://github.com/ersilia-os/west-africa-mtb-lineage-drug-responses/issues/5) — **Meeting_minutes_03/10/2024** · open 774d · last activity 774d ago · @fafaal3107 🕒
- [aws-utils #8](https://github.com/ersilia-os/aws-utils/issues/8) — **Launch Bastion host** · open 736d · last activity 595d ago · @IamEddie 🕒

_…and 248 more open issues (258 open in total)._

### 💡 Easy wins
- [ersilia-model-workflows #14](https://github.com/ersilia-os/ersilia-model-workflows/issues/14) — **PR test runs on the fork's default branch, not the PR's code** · clone the PR's branch instead · @arnaucoma24
- [eosframes #4](https://github.com/ersilia-os/eosframes/issues/4) — **New-functionalities branch outdated** · merge or delete one branch · @GemmaTuron
- [chem-sampler #7](https://github.com/ersilia-os/chem-sampler/issues/7) — **Remove models from the store** · one well-specified CLI command · @arnaucoma24

## 🔧 Registry alignment

2 missing · 0 ghost · 3 status · 3 type · 8 uncurated.

### Missing from registry
- [gradi-clpp-engaging-ligands](https://github.com/ersilia-os/gradi-clpp-engaging-ligands) — in GitHub, not in the Repositories table
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
- `ersilia` — marked Completed but had activity this week
- `ersilia-model-workflows` — marked Completed but had activity this week
- `ersilia-self-service` — marked Completed but had activity this week
- `lazy-qsar` — marked Completed but had activity this week
- `tuimux` — marked Completed but had activity this week

## 📊 Repository overview
186 tracked repos (270 model packages tracked separately) · 46 archived.  
**By type:** Analysis 68 · Package 67 · Automation 13 · Workshop 11 · App 7 · Template 5 · Documentation 3 · unset 13  
**By status:** Completed 78 · In progress 42 · Archived 19 · Discontinued 17 · Idle 14 · Todo 3 · unset 13

## ✅ Recent activity

### Pull requests merged
- [chemicl #20](https://github.com/ersilia-os/chemicl/pull/20) — **Feat/tem product integration** · @OhhMoo · 2026-11-11
- [ersilia-book #4](https://github.com/ersilia-os/ersilia-book/pull/4) 📄 — **Clarify model release versioning and add a pre-release checklist** · @arnaucoma24 · 2026-11-10
- [ersilia-skills #61](https://github.com/ersilia-os/ersilia-skills/pull/61) 🐛 — **fix(model-fixing): compare example output with run_output.csv** · @GemmaTuron · 2026-11-10
- [ersilia-skills #62](https://github.com/ersilia-os/ersilia-skills/pull/62) — **literature-digest: pin Slack and reserve Gmail slots in the pool; drop requests dependency** · @miquelduranfrigola · 2026-11-10
- [ersilia-skills #63](https://github.com/ersilia-os/ersilia-skills/pull/63) — **literature-digest: score small-molecule Hub fit, weight titles, ignore generic keywords** · @miquelduranfrigola · 2026-11-10
- [ersilia-skills #64](https://github.com/ersilia-os/ersilia-skills/pull/64) — **literature-digest: fill missing abstracts before ranking** · @miquelduranfrigola · 2026-11-10
- [h3d-mtb-bioactivity #1](https://github.com/ersilia-os/h3d-mtb-bioactivity/pull/1) — **Publication prep: four-bucket layout, Round 2 funnel, private-model ids** · @GemmaTuron · 2026-11-10
- [h3d-mtb-bioactivity #2](https://github.com/ersilia-os/h3d-mtb-bioactivity/pull/2) — **round2_lq39: Round 2 models refit on lazyqsar 3.9, selections re-scored** · @GemmaTuron · 2026-11-13
- [lazy-qsar #65](https://github.com/ersilia-os/lazy-qsar/pull/65) — **3.9.0: fix CLAMP and CDDD descriptors, reference library v2** · @GemmaTuron · 2026-11-10
- [lazy-qsar #67](https://github.com/ersilia-os/lazy-qsar/pull/67) 🐛 — **Fix OnnxExportMismatch on Intel AVX-512 CPUs (power transform)** · @arnaucoma24 · 2026-11-13
- [lazy-qsar #69](https://github.com/ersilia-os/lazy-qsar/pull/69) 🐛 — **fix(preprocessing): keep lambda = 1 on power columns with lambda near 0 or 2 (#68)** · @arnaucoma24 · 2026-11-16
- [tcolf-antimalarials #163](https://github.com/ersilia-os/tcolf-antimalarials/pull/163) — **CLAMP fix record, fold-SD plan, LazyQSAR 3.9 work, ZairaChem comparison figures** · @TiagoJanela · 2026-11-12
- [tcolf-antimalarials #164](https://github.com/ersilia-os/tcolf-antimalarials/pull/164) — **05c fold SD for every metric, backfill tool, SD bars in 06l/06o** · @TiagoJanela · 2026-11-12
- [tcolf-antimalarials #165](https://github.com/ersilia-os/tcolf-antimalarials/pull/165) — **tmp/45: rename to 45_lazyqsar_versions, merge the CLAMP fix (tmp/55) [after #163]** · @TiagoJanela · 2026-11-12
- [tcolf-antimalarials #166](https://github.com/ersilia-os/tcolf-antimalarials/pull/166) — **screening: stage 07/08 on the LazyQSAR 3.9 (lq39) models** · @TiagoJanela · 2026-11-13
- [tcolf-antimalarials #167](https://github.com/ersilia-os/tcolf-antimalarials/pull/167) — **backup: uncommitted main-checkout work (tmp/52-56, plans, reviews, log)** · @TiagoJanela · 2026-11-13
- [tcolf-antimalarials #168](https://github.com/ersilia-os/tcolf-antimalarials/pull/168) — **tmp/README: fold module 55 into 45, free the number 55** · @TiagoJanela · 2026-11-13
- [tcolf-antimalarials #169](https://github.com/ersilia-os/tcolf-antimalarials/pull/169) 📄 — **docs: 2026-11-13 log lines, lq39 promotion record, tmp/53 status** · @TiagoJanela · 2026-11-13
- [tcolf-antimalarials #170](https://github.com/ersilia-os/tcolf-antimalarials/pull/170) 📄 — **docs/tmp/45: lq39 promotion closed, 08d check passed** · @TiagoJanela · 2026-11-13
- [tcolf-antimalarials #171](https://github.com/ersilia-os/tcolf-antimalarials/pull/171) — **tmp/55: rename tmp/56_pf_antitargets to tmp/55_pf_offtargets; antitarget -> off-target** · @TiagoJanela · 2026-11-13
- [tcolf-antimalarials #172](https://github.com/ersilia-os/tcolf-antimalarials/pull/172) — **stage06: give arm-less stage-05 files an arm in 06a; 06b no longer crashes** · @TiagoJanela · 2026-11-13
- [tcolf-antimalarials #173](https://github.com/ersilia-os/tcolf-antimalarials/pull/173) 📄 — **docs: experiment log, 2026-11-13 afternoon (06b fix, #170-#172)** · @TiagoJanela · 2026-11-13
- [tcolf-antimalarials #174](https://github.com/ersilia-os/tcolf-antimalarials/pull/174) 📄 — **docs: next-week focus agenda (week of 2026-11-16)** · @TiagoJanela · 2026-11-13
- [tuimux #11](https://github.com/ersilia-os/tuimux/pull/11) — **Routines, a calmer look, and a responsive dashboard** · @miquelduranfrigola · 2026-11-14
- [tuimux #12](https://github.com/ersilia-os/tuimux/pull/12) — **Add unattended routines** · @miquelduranfrigola · 2026-11-15
- [tuimux #13](https://github.com/ersilia-os/tuimux/pull/13) — **Show each routine's mode in the routines panel** · @miquelduranfrigola · 2026-11-15
- [tuimux #14](https://github.com/ersilia-os/tuimux/pull/14) — **Fix the repository audit findings** · @miquelduranfrigola · 2026-11-15
- [tuimux #15](https://github.com/ersilia-os/tuimux/pull/15) 🔧 — **Bump actions/setup-python from 5 to 7** · @dependabot[bot] · 2026-11-15
- [tuimux #16](https://github.com/ersilia-os/tuimux/pull/16) 🔧 — **Bump actions/checkout from 4 to 7** · @dependabot[bot] · 2026-11-15
- [tuimux #17](https://github.com/ersilia-os/tuimux/pull/17) 🔧 — **Bump ruff from 0.17.1 to 0.17.5** · @dependabot[bot] · 2026-11-15
- [tuimux #18](https://github.com/ersilia-os/tuimux/pull/18) 🔧 — **Bump pytest from 9.1.1 to 9.2.0** · @dependabot[bot] · 2026-11-15
- [tuimux #19](https://github.com/ersilia-os/tuimux/pull/19) — **Remove dead code, read dashboard settings from the config file, call this machine local** · @miquelduranfrigola · 2026-11-15
- [tuimux #20](https://github.com/ersilia-os/tuimux/pull/20) — **THIS RUN: say what to do, and since when** · @miquelduranfrigola · 2026-11-15
- [tuimux #21](https://github.com/ersilia-os/tuimux/pull/21) — **Use one colour rule in both panels** · @miquelduranfrigola · 2026-11-15
- [tuimux #22](https://github.com/ersilia-os/tuimux/pull/22) — **Routine menu on space, visible pauses, tidier routine form** · @miquelduranfrigola · 2026-11-15

### Pull requests opened
- [ersilia-book #7](https://github.com/ersilia-os/ersilia-book/pull/7) 📄 — **Versioning: format conversions of the same weights and random generative models** · @TiagoJanela · 2026-11-10
- [ersilia-skills #65](https://github.com/ersilia-os/ersilia-skills/pull/65) — **Add the github-inbox-zero skill** · @miquelduranfrigola · 2026-11-12
- [ersilia-skills #66](https://github.com/ersilia-os/ersilia-skills/pull/66) — **Add the ai-text-detection skill** · @miquelduranfrigola · 2026-11-15

_The other 34 of the 37 PRs opened this week were also merged and are listed above._

### Issues closed
- [ersilia #1917](https://github.com/ersilia-os/ersilia/issues/1917) — **🐅 Epic: Optimization of Ersilia Models** · @Marina18 · 2026-11-13
- [lazy-qsar #51](https://github.com/ersilia-os/lazy-qsar/issues/51) — **CDDD descriptor raises on unparseable SMILES instead of falling through to the NaN path, taking the whole batch down at predict time** · @GemmaTuron · 2026-11-10
- [lazy-qsar #66](https://github.com/ersilia-os/lazy-qsar/issues/66) — **OnnxExportMismatch in slow mode on Intel AVX-512 CPUs** · @arnaucoma24 · 2026-11-13
- [lazy-qsar #68](https://github.com/ersilia-os/lazy-qsar/issues/68) — **OnnxExportMismatch on every CPU when a Yeo–Johnson λ is at or near 0 (skl2onnx float32 cancellation)** · @arnaucoma24 · 2026-11-16
- [ersilia-self-service](https://github.com/ersilia-os/ersilia-self-service/issues) — **7 model-inference-run issues** (#451–#458) · @miquelduranfrigola · 2026-11-15

### Issues opened
- [ersilia #1967](https://github.com/ersilia-os/ersilia/issues/1967) — **🐅 Epic: One storage rule for model checkpoints (Git or eosvc, no Git LFS)** · @arnaucoma24 · 2026-11-10
- [ersilia #1968](https://github.com/ersilia-os/ersilia/issues/1968) ✨ — **📑 Feature Request: Adapt deep test to Generative models** · @Marina18 · 2026-11-16
- [ersilia-model-workflows #14](https://github.com/ersilia-os/ersilia-model-workflows/issues/14) — **PR test runs on the fork's default branch, not the PR's code** · @arnaucoma24 · 2026-11-12
- [lazy-qsar #66](https://github.com/ersilia-os/lazy-qsar/issues/66) — **OnnxExportMismatch in slow mode on Intel AVX-512 CPUs** · @arnaucoma24 · 2026-11-11
- [lazy-qsar #68](https://github.com/ersilia-os/lazy-qsar/issues/68) — **OnnxExportMismatch on every CPU when a Yeo–Johnson λ is at or near 0 (skl2onnx float32 cancellation)** · @arnaucoma24 · 2026-11-16
- [ersilia-self-service](https://github.com/ersilia-os/ersilia-self-service/issues) — **133 model-inference-run issues** (#520–#652) · @miquelduranfrigola · 2026-11-10 to 2026-11-17

**Model repos (eosXXXX):** 32 PRs merged · 34 opened · 3 issues closed · 2 opened — across 45 repos. Managed via the model-incorporation flow.
