# Ersilia GitHub Digest — Week of 2026-08-13

**Connectors:** GitHub 🟢 · Airtable 🟢  
**Markers:** 🐛 Bug · ✨ Feature · 📄 Docs · 🔧 Infra · 🕒 Stale  

## ✨ Highlights
A busy week on `tcolf-antimalarials`, which merged eight staged PRs covering ReFRAME pre-ingestion gates, a strain audit, life-cycle stage separability and MAIP-surrogate scoring. The single most consequential change is `olinda`'s pre-publication cleanup landing across #18 and #19, taking the package to 1.1.0; the new org-wide repository browser also went live from `.github` #1. Fourteen non-model PRs merged and no open PR has gone stale. The registry has no missing or ghost records, but 4 Status and 3 Type values disagree with the GitHub mirror.

## ⚠️ Needs attention

### Stale pull requests
_Nothing stale this week — all 21 open PRs saw activity within the last 30 days._

### Long-open issues
- [ersilia-gui #24](https://github.com/ersilia-os/ersilia-gui/issues/24) — **Connect to DynamoDB to store model results** · open 1141d · last activity 520d ago · @jaydenpersonnat 🕒
- [ersilia-gui #28](https://github.com/ersilia-os/ersilia-gui/issues/28) — **Small tweaks to GUI** · open 1125d · last activity 1115d ago · @GemmaTuron 🕒
- [ersilia-gui #26](https://github.com/ersilia-os/ersilia-gui/issues/26) — **API to run** · open 1125d · last activity 1119d ago · @GemmaTuron 🕒
- [ersilia #891](https://github.com/ersilia-os/ersilia/issues/891) — **Model Request: PGMG pharmacophore-based generative model** · open 994d · last activity 691d ago · @miquelduranfrigola 🕒
- [ersilia #1147](https://github.com/ersilia-os/ersilia/issues/1147) — **Epic: Adding support for Authentication in Ersilia** · open 799d · last activity 183d ago · @DhanshreeA 🕒
- [west-africa-mtb-lineage-drug-responses #1](https://github.com/ersilia-os/west-africa-mtb-lineage-drug-responses/issues/1) — **Meeting minutes 2024-08-15** · open 727d · last activity 715d ago · @fafaal3107 🕒
- [west-africa-mtb-lineage-drug-responses #2](https://github.com/ersilia-os/west-africa-mtb-lineage-drug-responses/issues/2) — **Meeting minutes 2024-08-22** · open 716d · last activity 714d ago · @fafaal3107 🕒
- [west-africa-mtb-lineage-drug-responses #3](https://github.com/ersilia-os/west-africa-mtb-lineage-drug-responses/issues/3) — **Meeting minutes 29/08/2024** · open 710d · last activity 710d ago · @fafaal3107 🕒
- [west-africa-mtb-lineage-drug-responses #4](https://github.com/ersilia-os/west-africa-mtb-lineage-drug-responses/issues/4) — **Meeting_minutes_05092024** · open 701d · last activity 701d ago · @fafaal3107 🕒
- [west-africa-mtb-lineage-drug-responses #5](https://github.com/ersilia-os/west-africa-mtb-lineage-drug-responses/issues/5) — **Meeting_minutes_03/10/2024** · open 678d · last activity 678d ago · @fafaal3107 🕒

_…and 40 more open issues (50 open in total)._

### 💡 Easy wins
- [ersilia #1844](https://github.com/ersilia-os/ersilia/issues/1844) — **Bug: Loading in memory when preparing output** · labelled bug, single code path · @GemmaTuron
- [ersilia #1901](https://github.com/ersilia-os/ersilia/issues/1901) — **Standardise indexed output column names on feat_ and smi_** · narrow naming-convention change · @GemmaTuron

_Four other flagged candidates were model requests or too vaguely scoped to call quick._

## 🔧 Registry alignment

0 missing · 0 ghost · 4 status · 3 type · 0 uncurated.

### Status / Type mismatches
- `chembl-binary-tasks` — Status: Airtable «Completed, Archived» vs GitHub «Completed»
- `ersilia-stats-capstone` — Status: Airtable «Archived» vs GitHub «In progress»
- `h3d-mtb-metabolism` — Status: Airtable «Completed, Archived» vs GitHub «Completed»
- `zaira-chem-tdc-benchmark` — Status: Airtable «Completed, Archived» vs GitHub «Completed»
- `eosbench` — Type: Airtable «App, Package» vs GitHub «Package»
- `ersilia-stats-capstone` — Type: Airtable «Analysis, App» vs GitHub «Analysis»
- `gradi-target-prioritization` — Type: Airtable «Analysis, App» vs GitHub «Analysis»

### Possibly out of date
- `digests` — marked Completed but had activity this week
- `ersilia` — marked Completed but had activity this week
- `stylia` — marked Completed but had activity this week

_Every record carries a Status and a Type; 73 have no Projects link (informational)._

## 📊 Repository overview
176 tracked repos (247 model packages tracked separately) · 46 archived.
**By type:** Analysis 68 · Package 67 · Automation 13 · Workshop 11 · App 7 · Template 5 · Documentation 3 · unset 3
**By status:** Completed 77 · In progress 42 · Archived 18 · Discontinued 18 · Idle 14 · Todo 4 · unset 3

## ✅ Recent activity

### Pull requests merged
- [.github #1](https://github.com/ersilia-os/.github/pull/1) ✨ — **Add the repository browser, published to Pages and refreshed daily** · @miquelduranfrigola · 2026-08-11
- [digests #5](https://github.com/ersilia-os/digests/pull/5) ✨ — **website: add event digests to the calendar, widen event report pages** · @TiagoJanela · 2026-08-06
- [ersilia-mcp #36](https://github.com/ersilia-os/ersilia-mcp/pull/36) 📄 — **Add model provider docs** · @Lehcar · 2026-08-09
- [ersilia-skills #23](https://github.com/ersilia-os/ersilia-skills/pull/23) ✨ — **Add html-formatting skill** · @miquelduranfrigola · 2026-08-12
- [olinda #18](https://github.com/ersilia-os/olinda/pull/18) — **Pre-publication cleanup: S/H/T nomenclature, one output per column, working install tiers** · @miquelduranfrigola · 2026-08-12
- [olinda #19](https://github.com/ersilia-os/olinda/pull/19) — **Work down the pre-publication audit, and bump to 1.1.0** · @miquelduranfrigola · 2026-08-13
- [tcolf-antimalarials #20](https://github.com/ersilia-os/tcolf-antimalarials/pull/20) — **Stage-03: review-bug fixes + env-setup (folds #17)** · @TiagoJanela · 2026-08-07
- [tcolf-antimalarials #21](https://github.com/ersilia-os/tcolf-antimalarials/pull/21) — **tmp(20): ReFRAME pre-ingestion verification gates** · @TiagoJanela · 2026-08-07
- [tcolf-antimalarials #22](https://github.com/ersilia-os/tcolf-antimalarials/pull/22) — **tmp(21): life-cycle stage separability analysis** · @TiagoJanela · 2026-08-07
- [tcolf-antimalarials #23](https://github.com/ersilia-os/tcolf-antimalarials/pull/23) — **tmp(22): strain audit (ChEMBL + non-ChEMBL)** · @TiagoJanela · 2026-08-07
- [tcolf-antimalarials #24](https://github.com/ersilia-os/tcolf-antimalarials/pull/24) — **tmp(24): activity preparation (per-assay resolved)** · @TiagoJanela · 2026-08-07
- [tcolf-antimalarials #25](https://github.com/ersilia-os/tcolf-antimalarials/pull/25) — **tmp(archive/23): Pf HTS classifier (first ML pass, archived)** · @TiagoJanela · 2026-08-07
- [tcolf-antimalarials #26](https://github.com/ersilia-os/tcolf-antimalarials/pull/26) 🔧 — **ci: auto-request Copilot review on every PR update** · @TiagoJanela · 2026-08-07
- [tcolf-antimalarials #27](https://github.com/ersilia-os/tcolf-antimalarials/pull/27) — **tmp(26): MAIP-surrogate scoring of the sp arm + per-depositor evaluation** · @TiagoJanela · 2026-08-07

### Pull requests opened
- [ersilia #1900](https://github.com/ersilia-os/ersilia/pull/1900) — **Remove intermediate from accepted column directions** · @GemmaTuron · 2026-08-12
- [ersilia-mcp #38](https://github.com/ersilia-os/ersilia-mcp/pull/38) 🔧 — **Add publish workflow** · @Lehcar · 2026-08-07
- [ersilia-mcp #39](https://github.com/ersilia-os/ersilia-mcp/pull/39) — **Add a tool to read from isaura store** · @Lehcar · 2026-08-12
- [ersilia-skills #30](https://github.com/ersilia-os/ersilia-skills/pull/30) — **Rename paper-summary to paper-to-model-assessment; refine Hub eligibility criteria** · @arnaucoma24 · 2026-08-11

_Five further PRs opened this week were merged inside the window and are listed above._

### Issues closed
- [ersilia #1810](https://github.com/ersilia-os/ersilia/issues/1810) — **Task: Ersilia Gen Models Revision** · @Abellegese · 2026-08-06
- [ersilia #1896](https://github.com/ersilia-os/ersilia/issues/1896) — **Model Request: GenMol Scaffold Decoration** · @arnaucoma24 · 2026-08-06
- [ersilia #1897](https://github.com/ersilia-os/ersilia/issues/1897) — **Model Request: MolCompass Chemical Space Projection** · @arnaucoma24 · 2026-08-06
- [ersilia #1898](https://github.com/ersilia-os/ersilia/issues/1898) — **Model Request: EU OpenScreen HTS** · @GemmaTuron · 2026-08-12
- [ersilia-mcp #30](https://github.com/ersilia-os/ersilia-mcp/issues/30) 🔧 — **Add a stricter timeout to our CI action** · @Lehcar · 2026-08-09

### Issues opened
- [ersilia #1899](https://github.com/ersilia-os/ersilia/issues/1899) 🐛 — **Column-name validation does not enforce the documented all-lowercase rule** · @GemmaTuron · 2026-08-12
- [ersilia #1901](https://github.com/ersilia-os/ersilia/issues/1901) ✨ — **Standardise indexed output column names on feat_ and smi_** · @GemmaTuron · 2026-08-12
- [ersilia-skills #31](https://github.com/ersilia-os/ersilia-skills/issues/31) — **Model Incorporation code fixes** · @GemmaTuron · 2026-08-12
- [stylia #5](https://github.com/ersilia-os/stylia/issues/5) — **stylia.label's panel letter (abc) sits right of the ylabel/tick numbers instead of left of them** · @arnaucoma24 · 2026-08-10

_Two further issues opened this week (`ersilia` #1897, #1898) were closed inside the window and are listed above._

**Model repos (eosXXXX):** 4 PRs merged · 6 opened · 7 issues closed · 2 opened — across 25 repos. Managed via the model-incorporation flow.
