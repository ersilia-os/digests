# Ersilia GitHub Digest — Week of 2026-08-31

**Connectors:** GitHub 🟢 · Airtable 🟢  
**Markers:** 🐛 Bug · ✨ Feature · 📄 Docs · 🔧 Infra · 🕒 Stale  

## ✨ Highlights
A modest week concentrated on tooling: `ersilia` (7 events), `chem-icl` (5) and `ersilia-mcp` (4) carried nearly all the movement. The most substantial merge is the new input-generating MCP tool in `ersilia-mcp` (#40), while `chem-icl` shipped three consecutive PRs tightening its recommendation and consensus paths. Model-request triage was fast — three requests opened and closed within days — and the long-parked MolE embeddings request (#1385) was finally closed after 649 days. On the registry, two new repos are not yet catalogued and seven Status/Type mismatches surfaced, though six of them come from the same mirror limitation rather than genuine curation drift.

## ⚠️ Needs attention

### Stale pull requests
- [zairachem-docker #46](https://github.com/ersilia-os/zairachem-docker/pull/46) — **Warnings instead of exceptions** · open 38d · last activity 38d ago · @JHlozek 🕒
- [ersilia-stats-capstone #139](https://github.com/ersilia-os/ersilia-stats-capstone/pull/139) — **Add initial Airtable data snapshots + restrict fetch to app tables** · open 35d · last activity 35d ago · @miquelduranfrigola 🕒
- [ersilia-stats-capstone #140](https://github.com/ersilia-os/ersilia-stats-capstone/pull/140) — **Static HTML site: "Ersilia in numbers" + GitHub Pages deploy** · open 35d · last activity 34d ago · @miquelduranfrigola 🕒
- [ersilia-model-request-app #64](https://github.com/ersilia-os/ersilia-model-request-app/pull/64) 🔧 — **Fix React Server Components CVE vulnerabilities** · open 172d · last activity 32d ago · @vercel[bot] 🕒
- [ersilia #1835](https://github.com/ersilia-os/ersilia/pull/1835) 🔧 — **build(deps): bump dorny/paths-filter from 3 to 4** · open 152d · last activity 30d ago · @dependabot[bot] 🕒
- [ersilia #1822](https://github.com/ersilia-os/ersilia/pull/1822) 🔧 — **chore(deps): bump actions/checkout from 6.0.0 to 6.0.2** · open 183d · last activity 30d ago · @dependabot[bot] 🕒
- [ersilia #1802](https://github.com/ersilia-os/ersilia/pull/1802) 🔧 — **build(deps): bump peter-evans/slash-command-dispatch from 5.0.0 to 5.0.2** · open 242d · last activity 30d ago · @dependabot[bot] 🕒
- [ersilia #1843](https://github.com/ersilia-os/ersilia/pull/1843) 🔧 — **build(deps): bump conda-incubator/setup-miniconda from 3 to 4** · open 122d · last activity 30d ago · @dependabot[bot] 🕒

All 8 stale PRs are listed (14 open PRs in total). The security backlog is the notable one: a CVE fix on `ersilia-model-request-app` has sat 32 days, and four Dependabot bumps on `ersilia` crossed the stale threshold together.

### Long-open issues
- [ersilia-gui #24](https://github.com/ersilia-os/ersilia-gui/issues/24) — **Connect to DynamoDB to store model results** · open 1159d · last activity 538d ago · @jaydenpersonnat 🕒
- [ersilia-gui #28](https://github.com/ersilia-os/ersilia-gui/issues/28) — **Small tweaks to GUI** · open 1142d · last activity 1133d ago · @GemmaTuron 🕒
- [ersilia-gui #26](https://github.com/ersilia-os/ersilia-gui/issues/26) — **API to run** · open 1142d · last activity 1137d ago · @GemmaTuron 🕒
- [ersilia #891](https://github.com/ersilia-os/ersilia/issues/891) — **Model Request: PGMG pharmacophore-based generative model** · open 1012d · last activity 709d ago · @miquelduranfrigola 🕒
- [ersilia #1147](https://github.com/ersilia-os/ersilia/issues/1147) — **Epic: Adding support for Authentication in Ersilia** · open 817d · last activity 201d ago · @DhanshreeA 🕒
- [west-africa-mtb-lineage-drug-responses #1](https://github.com/ersilia-os/west-africa-mtb-lineage-drug-responses/issues/1) — **Meeting minutes 2024-08-15** · open 744d · last activity 733d ago · @fafaal3107 🕒
- [west-africa-mtb-lineage-drug-responses #2](https://github.com/ersilia-os/west-africa-mtb-lineage-drug-responses/issues/2) — **Meeting minutes 2024-08-22** · open 734d · last activity 732d ago · @fafaal3107 🕒
- [west-africa-mtb-lineage-drug-responses #3](https://github.com/ersilia-os/west-africa-mtb-lineage-drug-responses/issues/3) — **Meeting minutes 29/08/2024** · open 727d · last activity 727d ago · @fafaal3107 🕒
- [west-africa-mtb-lineage-drug-responses #4](https://github.com/ersilia-os/west-africa-mtb-lineage-drug-responses/issues/4) — **Meeting_minutes_05092024** · open 718d · last activity 718d ago · @fafaal3107 🕒
- [west-africa-mtb-lineage-drug-responses #5](https://github.com/ersilia-os/west-africa-mtb-lineage-drug-responses/issues/5) — **Meeting_minutes_03/10/2024** · open 695d · last activity 695d ago · @fafaal3107 🕒

_…and 37 more open issues (47 open in total)._ The three `ersilia-gui` issues and the five `west-africa-mtb-lineage-drug-responses` meeting-minutes issues are almost certainly closable in bulk rather than resolvable.

### 💡 Easy wins
- [stylia #5](https://github.com/ersilia-os/stylia/issues/5) 🐛 — **stylia.label's panel letter (abc) sits right of the ylabel/tick numbers instead of left of them** · single positioning fix, unassigned · @arnaucoma24
- [ersilia #1901](https://github.com/ersilia-os/ersilia/issues/1901) ✨ — **Standardise indexed output column names on feat_ and smi_** · scoped naming convention change · @GemmaTuron

Two of the three script-flagged candidates were dropped: `ersilia #1880` is a model request (handled by the incorporation flow) and `ersilia-skills #28` ("Gap Generative Modeling") is a scoping discussion, not a quick fix.

## 🔧 Registry alignment

2 missing · 0 ghost · 4 status · 3 type · 0 uncurated.

### Missing from registry
- [gradi-ai-data-working-group](https://github.com/ersilia-os/gradi-ai-data-working-group) — in GitHub, not in the Repositories table
- [lazy-chemvis-paper](https://github.com/ersilia-os/lazy-chemvis-paper) — in GitHub, not in the Repositories table

### Status / Type mismatches
- `ersilia-stats-capstone` — Status: Airtable «Archived» vs GitHub «In progress»
- `chembl-binary-tasks` — Status: Airtable «Completed, Archived» vs GitHub «Completed»
- `h3d-mtb-metabolism` — Status: Airtable «Completed, Archived» vs GitHub «Completed»
- `zaira-chem-tdc-benchmark` — Status: Airtable «Completed, Archived» vs GitHub «Completed»
- `eosbench` — Type: Airtable «App, Package» vs GitHub «Package»
- `ersilia-stats-capstone` — Type: Airtable «Analysis, App» vs GitHub «Analysis»
- `gradi-target-prioritization` — Type: Airtable «Analysis, App» vs GitHub «Analysis»

Six of these seven follow one pattern: Airtable holds two multi-select values and the GitHub custom property mirrors only the first. That points at the nightly cron flattening multi-values rather than at seven separate curation errors. The exception is `ersilia-stats-capstone`, where Airtable says Archived but GitHub says In progress and the repo has two PRs open from 35 days ago — a genuine disagreement worth resolving.

### Possibly out of date
- `ersilia` — marked Completed but had activity this week
- `ersilia-self-service` — marked Completed but had activity this week

Both are actively used; `Completed` looks wrong for the org's two busiest repos.

Separately, 73 of 180 records have no linked Project. That field is human-curated and never auto-filled, so it stays a standing backlog rather than new drift.

## 📊 Repository overview
178 tracked repos (250 model packages tracked separately) · 46 archived.
**By type:** Analysis 68 · Package 67 · Automation 13 · Workshop 11 · App 7 · Template 5 · Documentation 3 · unset 5
**By status:** Completed 77 · In progress 42 · Archived 18 · Discontinued 18 · Idle 14 · Todo 4 · unset 5

## ✅ Recent activity

### Pull requests merged
- [chem-icl #8](https://github.com/ersilia-os/chem-icl/pull/8) — **consensus: build the weighted rank consensus once per ranking** · @OhhMoo · 2026-08-24
- [chem-icl #9](https://github.com/ersilia-os/chem-icl/pull/9) — **recommend: parallel candidate evaluation, --auc gain presets, fast wi…** · @OhhMoo · 2026-08-26
- [chem-icl #10](https://github.com/ersilia-os/chem-icl/pull/10) — **Tool/compact portfolios** · @OhhMoo · 2026-08-26
- [ersilia-mcp #40](https://github.com/ersilia-os/ersilia-mcp/pull/40) ✨ — **Add a MCP tool that generates inputs** · @Lehcar · 2026-08-28
- [ersilia-skills #37](https://github.com/ersilia-os/ersilia-skills/pull/37) ✨ — **partner-profiling: a skill for visibility and networking partners** · @TiagoJanela · 2026-08-27

### Pull requests opened
- [ersilia-mcp #41](https://github.com/ersilia-os/ersilia-mcp/pull/41) 🔧 — **ci(deps): bump actions/setup-python from 5 to 7** · @dependabot[bot] · 2026-08-26
- [ersilia-mcp #42](https://github.com/ersilia-os/ersilia-mcp/pull/42) 🔧 — **ci(deps): bump actions/checkout from 4 to 7** · @dependabot[bot] · 2026-08-26
- [ersilia-mcp #43](https://github.com/ersilia-os/ersilia-mcp/pull/43) — **Add isaura dependency** · @Lehcar · 2026-08-28

Six PRs were opened this week; the other three (`chem-icl` #9 and #10, `ersilia-skills` #37) were also merged inside the window and are listed above.

### Issues closed
- [ersilia #1385](https://github.com/ersilia-os/ersilia/issues/1385) — **Model Request: MolE molecular embeddings** · @miquelduranfrigola · 2026-08-29
- [ersilia #1907](https://github.com/ersilia-os/ersilia/issues/1907) — **Model Request: HADES Oral Drug-Likeness** · @TiagoJanela · 2026-08-28
- [ersilia #1908](https://github.com/ersilia-os/ersilia/issues/1908) — **Model Request: CoCoGraph Formula-Preserving Generation** · @arnaucoma24 · 2026-08-31
- [ersilia #1909](https://github.com/ersilia-os/ersilia/issues/1909) — **Model Request: CoCoGraph Small-Fragment Inpainting** · @arnaucoma24 · 2026-08-31

### Issues opened
- [ersilia #1907](https://github.com/ersilia-os/ersilia/issues/1907) — **Model Request: HADES Oral Drug-Likeness** · @TiagoJanela · 2026-08-28
- [ersilia #1908](https://github.com/ersilia-os/ersilia/issues/1908) — **Model Request: CoCoGraph Formula-Preserving Generation** · @arnaucoma24 · 2026-08-28
- [ersilia #1909](https://github.com/ersilia-os/ersilia/issues/1909) — **Model Request: CoCoGraph Small-Fragment Inpainting** · @arnaucoma24 · 2026-08-28
- [ersilia-self-service #460](https://github.com/ersilia-os/ersilia-self-service/issues/460) — **Model Inference Run eos6m2k: MolE antimicrobial potential** · @miquelduranfrigola · 2026-08-29

**Model repos (eosXXXX):** 4 PRs merged · 8 opened · 1 issues closed · 1 opened — across 21 repos. Managed via the model-incorporation flow.
