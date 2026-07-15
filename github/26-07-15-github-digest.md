# Ersilia GitHub Digest — Week of 2026-07-15

**Connectors:** GitHub 🟢 · Airtable 🟢
**Markers:** 🐛 Bug · ✨ Feature · 📄 Docs · 🔧 Infra · 🕒 Stale

## ✨ Highlights
Busiest on `ersilia` and the new `tcolf-antimalarials` analysis repo, which landed its initial burst of Stage-01/02 antimalarial chemotype-curation PRs (#1–#7, @TiagoJanela). The standout core change is `ersilia` dropping Python 3.8/3.9 and hardening `eval()` usage (#1888, #1890). Nothing merged this week; 11 PRs open (2 stale). Registry is close to aligned — 2 repos missing, 2 ghost records, 3 status mismatches — and metrics were refreshed for 15 repos (25 field updates).

## ⚠️ Needs attention

### Stale pull requests
- [zairachem-docker #34](https://github.com/ersilia-os/zairachem-docker/pull/34) — **ZairaChem interpretability step with XAI4Chem** · open 173d · last activity 153d ago · @JHlozek 🕒
- [ersilia-model-request-app #64](https://github.com/ersilia-os/ersilia-model-request-app/pull/64) — **Fix React Server Components CVE vulnerabilities** · open 124d · last activity 124d ago · @vercel[bot] 🕒

### Long-open issues
- [ersilia-gui #24](https://github.com/ersilia-os/ersilia-gui/issues/24) — **Connect to DynamoDB to store model results** · open 1112d · last activity 490d ago · @jaydenpersonnat 🕒
- [ersilia-gui #28](https://github.com/ersilia-os/ersilia-gui/issues/28) — **Small tweaks to GUI** · open 1095d · last activity 1085d ago · @GemmaTuron 🕒
- [ersilia-gui #26](https://github.com/ersilia-os/ersilia-gui/issues/26) — **API to run** · open 1095d · last activity 1090d ago · @GemmaTuron 🕒
- [ersilia #891](https://github.com/ersilia-os/ersilia/issues/891) — **Model Request: PGMG pharmacophore-based generative model** · open 965d · last activity 662d ago · @miquelduranfrigola 🕒
- [model-inference-pipeline #11](https://github.com/ersilia-os/model-inference-pipeline/issues/11) — **Include validation test step in `serve.yml`** · open 945d · last activity 945d ago · @raul-bermejo 🕒
- [model-inference-pipeline #10](https://github.com/ersilia-os/model-inference-pipeline/issues/10) — **Include validation test step in `predict.yml`** · open 945d · last activity 945d ago · @raul-bermejo 🕒
- [model-inference-pipeline #9](https://github.com/ersilia-os/model-inference-pipeline/issues/9) — **Processing user input with both cached and uncached molecules** · open 945d · last activity 945d ago · @raul-bermejo 🕒
- [model-inference-pipeline #8](https://github.com/ersilia-os/model-inference-pipeline/issues/8) — **Implement validation tests on `input.csv`** · open 945d · last activity 945d ago · @raul-bermejo 🕒
- [chembl-binary-tasks #1](https://github.com/ersilia-os/chembl-binary-tasks/issues/1) — **ChEMBL SQL query warning** · open 825d · last activity 825d ago · @GemmaTuron 🕒
- [model-inference-pipeline #15](https://github.com/ersilia-os/model-inference-pipeline/issues/15) — **Meet to go over the API design and security** · open 807d · last activity 807d ago · @kartikey-vyas 🕒
_…and 48 more open issues (58 open in total)._

### 💡 Easy wins
- [isaura #20](https://github.com/ersilia-os/isaura/issues/20) — **Reader returns previous read data** · likely a small caching bug · @GemmaTuron

## 🔧 Registry alignment

2 missing · 2 ghost · 3 status · 0 type · 0 uncurated.

### Missing from registry
- [tuimux](https://github.com/ersilia-os/tuimux) — in GitHub, not in the Repositories table
- [zaira-chem-v1](https://github.com/ersilia-os/zaira-chem-v1) — in GitHub, not in the Repositories table

### Ghost records
- `eos` — in the registry (status In progress) but no longer in the org (renamed/deleted)
- `zaira-chem` — in the registry (status Completed) but no longer in the org (renamed/deleted)

### Status / Type mismatches
- `chembl-binary-tasks` — Status: Airtable «Archived, Completed» vs GitHub «Completed»
- `h3d-mtb-metabolism` — Status: Airtable «Archived, Completed» vs GitHub «Completed»
- `zaira-chem-tdc-benchmark` — Status: Airtable «Archived, Completed» vs GitHub «Completed»

### Possibly out of date
- `chembl-antimicrobial-tasks` — marked Completed but had activity this week
- `ersilia` — marked Completed but had activity this week

## 📊 Repository overview
175 tracked repos (240 model packages tracked separately) · 45 archived.
**By type:** Analysis 68 · Package 67 · Automation 14 · Workshop 11 · App 7 · Template 5 · Documentation 3 · unset 1
**By status:** Completed 77 · In progress 43 · Archived 18 · Discontinued 18 · Idle 14 · Todo 4 · unset 1

## ✅ Recent activity

### Pull requests opened
- [ersilia #1888](https://github.com/ersilia-os/ersilia/pull/1888) 🔧 — **Upgrade Python version (3.8 is EoL; virtualenv no longer supported)** · @Lehcar · 2026-07-08
- [ersilia #1890](https://github.com/ersilia-os/ersilia/pull/1890) 🔧 — **Drop Py3.8/3.9, harden eval, add license check and serve-close fix** · @Marina18 · 2026-07-09
- [ersilia-mcp #13](https://github.com/ersilia-os/ersilia-mcp/pull/13) ✨ — **Add MCP tools for serving and closing models** · @Lehcar · 2026-07-11
- [tcolf-antimalarials #1](https://github.com/ersilia-os/tcolf-antimalarials/pull/1) — **Antimalarial chemotype-flagging panel + SMARTS-tier confidence ranking** · @TiagoJanela · 2026-07-08
- [tcolf-antimalarials #2](https://github.com/ersilia-os/tcolf-antimalarials/pull/2) — **Type-based output layout + shared constants** · @TiagoJanela · 2026-07-10
- [tcolf-antimalarials #3](https://github.com/ersilia-os/tcolf-antimalarials/pull/3) — **Graduate Stage-01 SMARTS-panel evaluation + chemotype selection** · @TiagoJanela · 2026-07-10
- [tcolf-antimalarials #4](https://github.com/ersilia-os/tcolf-antimalarials/pull/4) — **Graduate Stage-02 Pf activity curation + provenance** · @TiagoJanela · 2026-07-10
- [tcolf-antimalarials #5](https://github.com/ersilia-os/tcolf-antimalarials/pull/5) — **Vendor Lilly-Medchem-Rules runtime (Stage-02 dependency)** · @TiagoJanela · 2026-07-10
- [tcolf-antimalarials #6](https://github.com/ersilia-os/tcolf-antimalarials/pull/6) — **Back up tmp/ prototype scripts (scratch)** · @TiagoJanela · 2026-07-11
- [tcolf-antimalarials #7](https://github.com/ersilia-os/tcolf-antimalarials/pull/7) — **Stage-02 landscape/modeling figures + sibling-ID correctness** · @TiagoJanela · 2026-07-13

### Issues closed
- [chembl-antimicrobial-tasks #7](https://github.com/ersilia-os/chembl-antimicrobial-tasks/issues/7) — **Skipped merged datasets are not stored in any report** · @arnaucoma24 · 2026-07-14
- [ersilia #1877](https://github.com/ersilia-os/ersilia/issues/1877) 🐛 — **Arbitrary code execution risk from unsafe eval() usage** · @pranjal2004838 · 2026-07-10
- [ersilia #1882](https://github.com/ersilia-os/ersilia/issues/1882) — **Model Request: Bioactivity Signature Predictor** · @arnaucoma24 · 2026-07-09
- [ersilia #1883](https://github.com/ersilia-os/ersilia/issues/1883) 🐛 — **Validate license field against license.txt before creating model** · @arnaucoma24 · 2026-07-09
- [ersilia #1889](https://github.com/ersilia-os/ersilia/issues/1889) — **Model Request: MycoPermeNet** · @GemmaTuron · 2026-07-10

### Issues opened
- [ersilia #1889](https://github.com/ersilia-os/ersilia/issues/1889) — **Model Request: MycoPermeNet** · @GemmaTuron · 2026-07-08
- [zairachem-docker #45](https://github.com/ersilia-os/zairachem-docker/issues/45) — **Pipeline tweaks** · @JHlozek · 2026-07-08

**Model repos (eosXXXX):** 0 PRs merged · 2 opened · 0 issues closed · 1 opened — across 13 repos. Managed via the model-incorporation flow.

## 🔄 Airtable sync
Refreshed 15 repo records (25 field updates) from GitHub. Notable: mtb-targeted-protein-degradation Total Commits 276→308 · ersilia-maintenance Total Commits 766→796 · tcolf-antimalarials Total Commits 7→24.
