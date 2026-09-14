# Ersilia GitHub Digest — Week of 2026-09-14

**Connectors:** GitHub 🟢 · Airtable 🟢  
**Markers:** 🐛 Bug · ✨ Feature · 📄 Docs · 🔧 Infra · 🕒 Stale  

## ✨ Highlights
`tcolf-antimalarials` dominated the week with 15 merged pull requests, graduating the
Stage-04 *P. falciparum* activity prep and landing the Stage-04/05/06 dataset release and
modeling-engine refactor (#40) — though four of them (#36–#39) re-land PRs that had already
merged hours earlier the same day.
Elsewhere `chem-icl` gained an NLP layer (#11) and `ersilia` closed the long-running
output-column standardisation issue (#1901). The registry is *not* in sync: 4 repos are
missing from the Repositories table, 2 records are ghosts, and 7 Status/Type values drifted
from their GitHub mirror.

## ⚠️ Needs attention

### Stale pull requests
- [zairachem-docker #46](https://github.com/ersilia-os/zairachem-docker/pull/46) — **Warnings instead of exceptions** · open 52d · last activity 52d ago · @JHlozek 🕒
- [ersilia-stats-capstone #139](https://github.com/ersilia-os/ersilia-stats-capstone/pull/139) — **Add initial Airtable data snapshots + restrict fetch to app tables** · open 49d · last activity 49d ago · @miquelduranfrigola 🕒
- [ersilia-stats-capstone #140](https://github.com/ersilia-os/ersilia-stats-capstone/pull/140) — **Static HTML site: "Ersilia in numbers" + GitHub Pages deploy** · open 49d · last activity 48d ago · @miquelduranfrigola 🕒
- [ersilia-model-request-app #64](https://github.com/ersilia-os/ersilia-model-request-app/pull/64) — **Fix React Server Components CVE vulnerabilities** · open 186d · last activity 46d ago · @vercel[bot] 🕒

### Long-open issues
- [ersilia-gui #24](https://github.com/ersilia-os/ersilia-gui/issues/24) — **Connect to DynamoDB to store model results** · open 1173d · last activity 552d ago · @jaydenpersonnat 🕒
- [ersilia-gui #26](https://github.com/ersilia-os/ersilia-gui/issues/26) — **API to run** · open 1156d · last activity 1151d ago · @GemmaTuron 🕒
- [ersilia-gui #28](https://github.com/ersilia-os/ersilia-gui/issues/28) — **Small tweaks to GUI** · open 1156d · last activity 1147d ago · @GemmaTuron 🕒
- [ersilia #891](https://github.com/ersilia-os/ersilia/issues/891) — **🦠 Model Request: PGMG pharmacophore-based generative model** · open 1026d · last activity 723d ago · @miquelduranfrigola 🕒
- [ersilia #1147](https://github.com/ersilia-os/ersilia/issues/1147) — **🐅 Epic: Adding support for Authentication in Ersilia** · open 831d · last activity 13d ago · @DhanshreeA
- [west-africa-mtb-lineage-drug-responses #1](https://github.com/ersilia-os/west-africa-mtb-lineage-drug-responses/issues/1) — **Meeting minutes 2024-08-15** · open 759d · last activity 747d ago · @fafaal3107 🕒
- [west-africa-mtb-lineage-drug-responses #2](https://github.com/ersilia-os/west-africa-mtb-lineage-drug-responses/issues/2) — **Meeting minutes 2024-08-22** · open 748d · last activity 746d ago · @fafaal3107 🕒
- [west-africa-mtb-lineage-drug-responses #3](https://github.com/ersilia-os/west-africa-mtb-lineage-drug-responses/issues/3) — **Meeting minutes 29/08/2024** · open 741d · last activity 741d ago · @fafaal3107 🕒
- [west-africa-mtb-lineage-drug-responses #4](https://github.com/ersilia-os/west-africa-mtb-lineage-drug-responses/issues/4) — **Meeting_minutes_05092024** · open 732d · last activity 732d ago · @fafaal3107 🕒
- [west-africa-mtb-lineage-drug-responses #5](https://github.com/ersilia-os/west-africa-mtb-lineage-drug-responses/issues/5) — **Meeting_minutes_03/10/2024** · open 709d · last activity 709d ago · @fafaal3107 🕒
_…and 40 more open issues (50 open in total)._

### 💡 Easy wins
*No obvious quick wins this week.* All three pre-flagged candidates were model requests or
unscoped discussion. The nearest genuinely small work is the dependency backlog: 7 open
Dependabot bumps across `ersilia` (4) and `ersilia-mcp` (3).

## 🔧 Registry alignment

4 missing · 2 ghost · 4 status · 3 type · 0 uncurated.

### Missing from registry
- [gradi-ai-data-working-group](https://github.com/ersilia-os/gradi-ai-data-working-group) — in GitHub, not in the Repositories table
- [lazy-chemvis-paper](https://github.com/ersilia-os/lazy-chemvis-paper) — in GitHub, not in the Repositories table
- [mtb-trna-synthetases-screening](https://github.com/ersilia-os/mtb-trna-synthetases-screening) — in GitHub, not in the Repositories table
- [rafiki-workshop-2026](https://github.com/ersilia-os/rafiki-workshop-2026) — in GitHub, not in the Repositories table

### Ghost records
- `mtb-targeted-protein-degradation` — in the registry (status In progress) but no longer in the org (renamed/deleted)
- `rafiki-workshop` — in the registry (status Completed) but no longer in the org (renamed/deleted)

`rafiki-workshop` ↔ `rafiki-workshop-2026` above look like a single rename: one record to
update rather than one to add and one to delete.

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

## 📊 Repository overview
179 tracked repos (254 model packages tracked separately) · 46 archived.
**By type:** Analysis 68 · Package 67 · Automation 13 · Workshop 11 · App 7 · Template 5 · Documentation 3 · unset 6
**By status:** Completed 77 · In progress 42 · Archived 18 · Discontinued 18 · Idle 14 · Todo 4 · unset 6

## ✅ Recent activity

### Pull requests merged
- [chem-icl #11](https://github.com/ersilia-os/chem-icl/pull/11) ✨ — **add nlp layer into chemicl** · @OhhMoo · 2026-09-13
- [rafiki-workshop-2026 #1](https://github.com/ersilia-os/rafiki-workshop-2026/pull/1) — **Scaffold workshop app** · @GemmaTuron · 2026-09-07
- [tcolf-antimalarials #28](https://github.com/ersilia-os/tcolf-antimalarials/pull/28) — **Stage-04: graduate the Pf activity prep (tmp/24 → 04a–04j)** · @TiagoJanela · 2026-09-09
- [tcolf-antimalarials #29](https://github.com/ersilia-os/tcolf-antimalarials/pull/29) — **Stage-04 corrections: SET22 FfLuc counter-screen + three resistant strains** · @TiagoJanela · 2026-09-09
- [tcolf-antimalarials #30](https://github.com/ersilia-os/tcolf-antimalarials/pull/30) — **tmp(25): SP transfer/screening probes + cluster-extrapolation split** · @TiagoJanela · 2026-09-09
- [tcolf-antimalarials #31](https://github.com/ersilia-os/tcolf-antimalarials/pull/31) — **tmp(26): MAIP replaces the surrogate + SureChEMBL patent arm + DR-arm scores** · @TiagoJanela · 2026-09-09
- [tcolf-antimalarials #32](https://github.com/ersilia-os/tcolf-antimalarials/pull/32) — **tmp(29): antimalarial consensus models (eos4an7, eos4rta) on both arms** · @TiagoJanela · 2026-09-09
- [tcolf-antimalarials #33](https://github.com/ersilia-os/tcolf-antimalarials/pull/33) — **tmp(30): dose-response modeling arm (Phase 0–2 + cross-arm figures)** · @TiagoJanela · 2026-09-09
- [tcolf-antimalarials #34](https://github.com/ersilia-os/tcolf-antimalarials/pull/34) 📄 — **docs: experiment log, tmp/ backup notes, the stylia inches trap, and three write-ups** · @TiagoJanela · 2026-09-09
- [tcolf-antimalarials #35](https://github.com/ersilia-os/tcolf-antimalarials/pull/35) — **Stage-00: a narrative target figure, and a cross-check for target_class** · @TiagoJanela · 2026-09-09
- [tcolf-antimalarials #36](https://github.com/ersilia-os/tcolf-antimalarials/pull/36) — **Stage-04 corrections: SET22 FfLuc counter-screen + three resistant strains (re-land of #29)** · @TiagoJanela · 2026-09-09
- [tcolf-antimalarials #37](https://github.com/ersilia-os/tcolf-antimalarials/pull/37) — **tmp(25): SP transfer/screening probes + cluster-extrapolation split (re-land of #30)** · @TiagoJanela · 2026-09-09
- [tcolf-antimalarials #38](https://github.com/ersilia-os/tcolf-antimalarials/pull/38) — **tmp(29): antimalarial consensus models (eos4an7, eos4rta) on both arms (re-land of #32)** · @TiagoJanela · 2026-09-09
- [tcolf-antimalarials #39](https://github.com/ersilia-os/tcolf-antimalarials/pull/39) 📄 — **docs: experiment log, tmp/ backup notes, the stylia inches trap, three write-ups (re-land of #34)** · @TiagoJanela · 2026-09-09
- [tcolf-antimalarials #40](https://github.com/ersilia-os/tcolf-antimalarials/pull/40) — **Stage 04/05/06: the dataset release, the modeling-engine refactor, and one shared figure seam** · @TiagoJanela · 2026-09-09
- [tcolf-antimalarials #41](https://github.com/ersilia-os/tcolf-antimalarials/pull/41) 🔧 — **scaffold: generate stylia-native modules, not deprecated figkit ones** · @TiagoJanela · 2026-09-09
- [tcolf-antimalarials #42](https://github.com/ersilia-os/tcolf-antimalarials/pull/42) — **Stage-00: rebuild panel A on fetched data, and pin the InterPro release** · @TiagoJanela · 2026-09-09

### Pull requests opened
- [chem-icl #11](https://github.com/ersilia-os/chem-icl/pull/11) ✨ — **add nlp layer into chemicl** · @OhhMoo · 2026-09-13
- [ersilia-mcp #44](https://github.com/ersilia-os/ersilia-mcp/pull/44) 🔧 — **chore(deps): bump the python group across 1 directory with 2 updates** · @dependabot[bot] · 2026-09-09
- [rafiki-workshop-2026 #1](https://github.com/ersilia-os/rafiki-workshop-2026/pull/1) — **Scaffold workshop app** · @GemmaTuron · 2026-09-07
- [tcolf-antimalarials #35](https://github.com/ersilia-os/tcolf-antimalarials/pull/35) — **Stage-00: a narrative target figure, and a cross-check for target_class** · @TiagoJanela · 2026-09-09
- [tcolf-antimalarials #36](https://github.com/ersilia-os/tcolf-antimalarials/pull/36) — **Stage-04 corrections: SET22 FfLuc counter-screen + three resistant strains (re-land of #29)** · @TiagoJanela · 2026-09-09
- [tcolf-antimalarials #37](https://github.com/ersilia-os/tcolf-antimalarials/pull/37) — **tmp(25): SP transfer/screening probes + cluster-extrapolation split (re-land of #30)** · @TiagoJanela · 2026-09-09
- [tcolf-antimalarials #38](https://github.com/ersilia-os/tcolf-antimalarials/pull/38) — **tmp(29): antimalarial consensus models (eos4an7, eos4rta) on both arms (re-land of #32)** · @TiagoJanela · 2026-09-09
- [tcolf-antimalarials #39](https://github.com/ersilia-os/tcolf-antimalarials/pull/39) 📄 — **docs: experiment log, tmp/ backup notes, the stylia inches trap, three write-ups (re-land of #34)** · @TiagoJanela · 2026-09-09
- [tcolf-antimalarials #40](https://github.com/ersilia-os/tcolf-antimalarials/pull/40) — **Stage 04/05/06: the dataset release, the modeling-engine refactor, and one shared figure seam** · @TiagoJanela · 2026-09-09
- [tcolf-antimalarials #41](https://github.com/ersilia-os/tcolf-antimalarials/pull/41) 🔧 — **scaffold: generate stylia-native modules, not deprecated figkit ones** · @TiagoJanela · 2026-09-09
- [tcolf-antimalarials #42](https://github.com/ersilia-os/tcolf-antimalarials/pull/42) — **Stage-00: rebuild panel A on fetched data, and pin the InterPro release** · @TiagoJanela · 2026-09-09
- [tcolf-antimalarials #43](https://github.com/ersilia-os/tcolf-antimalarials/pull/43) 🔧 — **gitignore: stop re-reporting tmp/27, which its own branch already carries** · @TiagoJanela · 2026-09-10

### Issues closed
- [ersilia #1901](https://github.com/ersilia-os/ersilia/issues/1901) ✨ — **Standardise indexed output column names on feat_ and smi_** · @GemmaTuron · 2026-09-14
- [ersilia #1911](https://github.com/ersilia-os/ersilia/issues/1911) — **🦠 Model Request: Mol-JEPA** · @arnaucoma24 · 2026-09-09
- [ersilia #1915](https://github.com/ersilia-os/ersilia/issues/1915) — **🦠 Model Request: Monroe Molecular Embeddings** · @TiagoJanela · 2026-09-14

### Issues opened
- [ersilia #1912](https://github.com/ersilia-os/ersilia/issues/1912) — **🦠 Model Request: SIMG** · @SoufianeAatab · 2026-09-07
- [ersilia #1913](https://github.com/ersilia-os/ersilia/issues/1913) — **🐈 Task: Debug logs and temporary files are removed on execution failure** · @SoufianeAatab · 2026-09-08
- [ersilia #1914](https://github.com/ersilia-os/ersilia/issues/1914) — **🦠 Model Request: CapMolPred** · @arnaucoma24 · 2026-09-10
- [ersilia #1915](https://github.com/ersilia-os/ersilia/issues/1915) — **🦠 Model Request: Monroe Molecular Embeddings** · @TiagoJanela · 2026-09-10

**Model repos (eosXXXX):** 1 PRs merged · 2 opened · 0 issues closed · 2 opened — across 19 repos. Managed via the model-incorporation flow.
