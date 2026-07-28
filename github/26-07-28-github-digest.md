# Ersilia GitHub Digest — Week of 2026-07-28

**Connectors:** GitHub 🟢 · Airtable 🟢
**Markers:** 🐛 Bug · ✨ Feature · 📄 Docs · 🔧 Infra · 🕒 Stale

## ✨ Highlights
Busiest on `ersilia-mcp`, `ersilia-self-service`, and `ersilia-stats`. The `ersilia-stats` repo was rebuilt around the capstone Streamlit app plus a new "Ersilia in numbers" static site (#138–#140), and `ersilia-mcp` saw a wave of dependency/lockfile housekeeping alongside a new `delete_model` tool (#25); nothing was merged this window. The registry is nearly aligned — 2 repos missing, 3 ghost records, and one Type mismatch, with no curation gaps. Metrics were refreshed for 20 repo records.

## ⚠️ Needs attention

### Stale pull requests
- [zairachem-docker #34](https://github.com/ersilia-os/zairachem-docker/pull/34) — **ZairaChem Interpretability Step with XAI4Chem** · open 186d · last activity 166d ago · @JHlozek 🕒
- [ersilia-model-request-app #64](https://github.com/ersilia-os/ersilia-model-request-app/pull/64) — **Fix React Server Components CVE vulnerabilities** · open 137d · last activity 137d ago · @vercel[bot] 🕒

### Long-open issues
- [ersilia-gui #24](https://github.com/ersilia-os/ersilia-gui/issues/24) — **Connect to DynamoDB to store model results** · open 1125d · last activity 503d ago · @jaydenpersonnat 🕒
- [ersilia-gui #28](https://github.com/ersilia-os/ersilia-gui/issues/28) — **Small tweaks to GUI** · open 1108d · last activity 1098d ago · @GemmaTuron 🕒
- [ersilia-gui #26](https://github.com/ersilia-os/ersilia-gui/issues/26) — **API to run** · open 1108d · last activity 1103d ago · @GemmaTuron 🕒
- [ersilia #891](https://github.com/ersilia-os/ersilia/issues/891) — **🦠 Model Request: PGMG pharmacophore-based generative model** · open 978d · last activity 675d ago · @miquelduranfrigola 🕒
- [model-inference-pipeline #9](https://github.com/ersilia-os/model-inference-pipeline/issues/9) — **Processing user input containing both cached and uncached molecules** · open 958d · last activity 958d ago · @raul-bermejo 🕒
- [model-inference-pipeline #8](https://github.com/ersilia-os/model-inference-pipeline/issues/8) — **Implement validation tests on `input.csv`** · open 958d · last activity 958d ago · @raul-bermejo 🕒
- [model-inference-pipeline #11](https://github.com/ersilia-os/model-inference-pipeline/issues/11) — **Include validation test step in `serve.yml`** · open 957d · last activity 957d ago · @raul-bermejo 🕒
- [model-inference-pipeline #10](https://github.com/ersilia-os/model-inference-pipeline/issues/10) — **Include validation test step in `predict.yml`** · open 957d · last activity 957d ago · @raul-bermejo 🕒
- [chembl-binary-tasks #1](https://github.com/ersilia-os/chembl-binary-tasks/issues/1) — **ChEMBL SQL query warning** · open 838d · last activity 838d ago · @GemmaTuron 🕒
- [model-inference-pipeline #15](https://github.com/ersilia-os/model-inference-pipeline/issues/15) — **Meet with Dhanshree and go over the API design and security** · open 820d · last activity 820d ago · @kartikey-vyas 🕒
_…and 51 more open issues (61 open in total)._

### 💡 Easy wins
No obvious quick wins this week. _(The four pre-flagged candidates were all model-run/request or vaguely-scoped items — dropped.)_

## 🔧 Registry alignment

2 missing · 3 ghost · 0 status · 1 type · 0 uncurated.

### Missing from registry
- [tuimux](https://github.com/ersilia-os/tuimux) — in GitHub, not in the Repositories table
- [zaira-chem-v1](https://github.com/ersilia-os/zaira-chem-v1) — in GitHub, not in the Repositories table

### Ghost records
- `chembl-antimicrobial-hub-incorporation` — in the registry (status In progress) but no longer in the org (renamed/deleted)
- `eos` — in the registry (status In progress) but no longer in the org (renamed/deleted)
- `zaira-chem` — in the registry (status Completed) but no longer in the org (renamed/deleted)

### Status / Type mismatches
- `gradi-target-prioritization` — Type: Airtable «Analysis, App» vs GitHub «Analysis»

### Possibly out of date
- `ersilia` — marked Completed but had activity this week
- `ersilia-self-service` — marked Completed but had activity this week

## 📊 Repository overview
174 tracked repos (240 model packages tracked separately) · 45 archived.
**By type:** Analysis 68 · Package 67 · Automation 13 · Workshop 11 · App 7 · Template 5 · Documentation 3 · unset 1
**By status:** Completed 77 · In progress 42 · Archived 18 · Discontinued 18 · Idle 14 · Todo 4 · unset 1

## ✅ Recent activity

### Pull requests opened
- [chem-icl #1](https://github.com/ersilia-os/chem-icl/pull/1) — **Add provenance-safe Isaura lake recommendations** · @OhhMoo · 2026-07-27
- [chem-icl #2](https://github.com/ersilia-os/chem-icl/pull/2) 📄 — **Streamline project documentation** · @OhhMoo · 2026-07-27
- [chem-icl #3](https://github.com/ersilia-os/chem-icl/pull/3) 🔧 — **Keep local development files out of Git** · @OhhMoo · 2026-07-27
- [ersilia #1891](https://github.com/ersilia-os/ersilia/pull/1891) 🐛 — **Fix fetch validation failing on a single empty example row** · @arnaucoma24 · 2026-07-26
- [ersilia-mcp #17](https://github.com/ersilia-os/ersilia-mcp/pull/17) — **Update docs and tests** · @Lehcar · 2026-07-21
- [ersilia-mcp #18](https://github.com/ersilia-os/ersilia-mcp/pull/18) 🔧 — **ci(deps): bump actions/checkout from 7.0.0 to 7.0.1** · @dependabot[bot] · 2026-07-22
- [ersilia-mcp #19](https://github.com/ersilia-os/ersilia-mcp/pull/19) 🔧 — **chore(deps): bump ruff from 0.15.13 to 0.16.0** · @dependabot[bot] · 2026-07-22
- [ersilia-mcp #20](https://github.com/ersilia-os/ersilia-mcp/pull/20) 🔧 — **Fix dependabot** · @Lehcar · 2026-07-23
- [ersilia-mcp #21](https://github.com/ersilia-os/ersilia-mcp/pull/21) 🔧 — **ci(deps): bump actions/checkout from 7.0.0 to 7.0.1 in the github-actions group** · @dependabot[bot] · 2026-07-23
- [ersilia-mcp #22](https://github.com/ersilia-os/ersilia-mcp/pull/22) 🔧 — **Update python lockfile** · @Lehcar · 2026-07-23
- [ersilia-mcp #23](https://github.com/ersilia-os/ersilia-mcp/pull/23) 🔧 — **Update pyproject.toml and poetry.lock to get dependabot updates** · @Lehcar · 2026-07-23
- [ersilia-mcp #24](https://github.com/ersilia-os/ersilia-mcp/pull/24) 🔧 — **chore(deps): bump the python group with 4 updates** · @dependabot[bot] · 2026-07-23
- [ersilia-mcp #25](https://github.com/ersilia-os/ersilia-mcp/pull/25) ✨ — **Add delete_model tool to delete a fetched model from local storage** · @Lehcar · 2026-07-24
- [ersilia-mcp #26](https://github.com/ersilia-os/ersilia-mcp/pull/26) 🔧 — **chore(deps): bump the python group across 1 directory with 3 updates** · @dependabot[bot] · 2026-07-24
- [ersilia-stats #138](https://github.com/ersilia-os/ersilia-stats/pull/138) — **Rebuild repo around the capstone Streamlit app (read-only)** · @miquelduranfrigola · 2026-07-24
- [ersilia-stats #139](https://github.com/ersilia-os/ersilia-stats/pull/139) — **Add initial Airtable data snapshots + restrict fetch to app tables** · @miquelduranfrigola · 2026-07-27
- [ersilia-stats #140](https://github.com/ersilia-os/ersilia-stats/pull/140) — **Static HTML site: "Ersilia in numbers" + GitHub Pages deploy** · @miquelduranfrigola · 2026-07-27
- [tcolf-antimalarials #12](https://github.com/ersilia-os/tcolf-antimalarials/pull/12) — **Stage-00/01: presentation-format figure variants + panel_plots helpers** · @TiagoJanela · 2026-07-22
- [tcolf-antimalarials #13](https://github.com/ersilia-os/tcolf-antimalarials/pull/13) — **Stage-02 relabel/layout + docs + tmp layout migration & prototype scripts** · @TiagoJanela · 2026-07-22
- [tcolf-antimalarials #14](https://github.com/ersilia-os/tcolf-antimalarials/pull/14) 📄 — **docs: experiment log entries + Meeting #3 link** · @TiagoJanela · 2026-07-26
- [tcolf-antimalarials #15](https://github.com/ersilia-os/tcolf-antimalarials/pull/15) — **tmp: Stage-09 SureChEMBL/patent-intent + other-species prototype backup** · @TiagoJanela · 2026-07-26
- [zairachem-docker #46](https://github.com/ersilia-os/zairachem-docker/pull/46) — **Warnings instead of exceptions** · @JHlozek · 2026-07-23

### Issues closed
- [ersilia-stats #134](https://github.com/ersilia-os/ersilia-stats/issues/134) — **Deprecate old scripts** · @GemmaTuron · 2026-07-24
- [ersilia-stats #135](https://github.com/ersilia-os/ersilia-stats/issues/135) 🔧 — **🚨 Model eos59kh repository not registered in AirTable 🚨** · @github-actions[bot] · 2026-07-24
- [ersilia-stats #136](https://github.com/ersilia-os/ersilia-stats/issues/136) 🔧 — **🚨 Model eos8sgp repository not registered in AirTable 🚨** · @github-actions[bot] · 2026-07-24
- [ersilia-stats #137](https://github.com/ersilia-os/ersilia-stats/issues/137) 🔧 — **🚨 Model eos4d2y repository not registered in AirTable 🚨** · @github-actions[bot] · 2026-07-24

### Issues opened
- [ersilia-self-service #452](https://github.com/ersilia-os/ersilia-self-service/issues/452) — **Model Inference Run: chembl-multitask-descriptor** · @shangyaxin08-arch · 2026-07-21
- [ersilia-self-service #453](https://github.com/ersilia-os/ersilia-self-service/issues/453) — **🚀 Model Inference Run 🤖 eos2gth: MAIP distillation: antimalarial potential prediction** · @miquelduranfrigola · 2026-07-21
- [ersilia-self-service #454](https://github.com/ersilia-os/ersilia-self-service/issues/454) — **🚀 Model Inference Run 🤖 eos11sm: Resemblance to a curated list of known antibiotics** · @miquelduranfrigola · 2026-07-21
- [ersilia-self-service #455](https://github.com/ersilia-os/ersilia-self-service/issues/455) — **🚀 Model Inference Run 🤖 eos7m30: ADMET properties prediction** · @miquelduranfrigola · 2026-07-24
- [ersilia-self-service #456](https://github.com/ersilia-os/ersilia-self-service/issues/456) — **🚀 Model Inference Run 🤖 eos7m30: ADMET properties prediction** · @miquelduranfrigola · 2026-07-24
- [ersilia-self-service #457](https://github.com/ersilia-os/ersilia-self-service/issues/457) — **🚀 Model Inference Run 🤖 eos7m30: ADMET properties prediction** · @miquelduranfrigola · 2026-07-24
- [ersilia-self-service #458](https://github.com/ersilia-os/ersilia-self-service/issues/458) — **🚀 Model Inference Run 🤖 eos7m30: ADMET properties prediction** · @miquelduranfrigola · 2026-07-24
- [ersilia-skills #19](https://github.com/ersilia-os/ersilia-skills/issues/19) — **Improving paper-summary skill** · @arnaucoma24 · 2026-07-22

**Model repos (eosXXXX):** 0 PRs merged · 0 opened · 0 issues closed · 1 opened — across 15 repos. Managed via the model-incorporation flow.

## 🔄 Airtable sync
Refreshed 20 repo records (28 field updates) from GitHub. Notable: gradi-target-prioritization Total Commits 27→79 · ersilia-self-service Open Issues 3→11 · chembl-antimicrobial-models Total Commits 124→136.
