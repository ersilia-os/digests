# Ersilia GitHub Digest — Week of 2026-11-08

**Connectors:** GitHub 🟢 · Airtable 🟢  
**Markers:** 🐛 Bug · ✨ Feature · 📄 Docs · 🔧 Infra · 🕒 Stale  

## ✨ Highlights
`gradi-target-prioritization` led the week with 20 merged PRs: v2 of the target browser (per-axis pipeline, E. coli shortlist, #1) followed by a run of webapp polish rounds. Apptainer images and warm serving landed across the model stack (`eos-template` #97–#98, `ersilia-pack` #94, `ersilia-model-workflows` #10–#12, `ersilia` #1965), and GPU image support is now open as PRs in `ersilia` #1966, `ersilia-pack` #96 and `ersilia-model-workflows` #13. `ersilia-mcp` has five open hardening PRs (#68–#72) covering structured errors, output caps, progress reporting and release pins. The registry has 2 repos missing, 6 Status/Type mismatches and 8 uncurated records, and 7 parked repos were active this week.

## ⚠️ Needs attention

### Stale pull requests
- [ersilia-stats-capstone #140](https://github.com/ersilia-os/ersilia-stats-capstone/pull/140) — **Static HTML site: "Ersilia in numbers" + GitHub Pages deploy** · open 104d · last activity 104d ago · @miquelduranfrigola 🕒
- [ersilia-stats-capstone #139](https://github.com/ersilia-os/ersilia-stats-capstone/pull/139) — **Add initial Airtable data snapshots + restrict fetch to app tables** · open 104d · last activity 104d ago · @miquelduranfrigola 🕒
- [ersilia-model-request-app #64](https://github.com/ersilia-os/ersilia-model-request-app/pull/64) — **Fix React Server Components CVE vulnerabilities** · open 241d · last activity 101d ago · @vercel[bot] 🕒
- [ersilia-mcp #50](https://github.com/ersilia-os/ersilia-mcp/pull/50) — **fix(predict): preserve input files when writing results** · open 40d · last activity 40d ago · @ECD5A 🕒
- [ersilia-mcp #42](https://github.com/ersilia-os/ersilia-mcp/pull/42) — **ci(deps): bump actions/checkout from 4 to 7** · open 73d · last activity 39d ago · @dependabot[bot] 🕒
- [ersilia-mcp #41](https://github.com/ersilia-os/ersilia-mcp/pull/41) — **ci(deps): bump actions/setup-python from 5 to 7** · open 73d · last activity 39d ago · @dependabot[bot] 🕒
- [ersilia-stats #1](https://github.com/ersilia-os/ersilia-stats/pull/1) — **Drop the Conferences table, removed from Airtable** · open 32d · last activity 32d ago · @miquelduranfrigola 🕒


### Long-open issues
- [ersilia-gui #24](https://github.com/ersilia-os/ersilia-gui/issues/24) — **Connect to DynamoDB to store model results** · open 1228d · last activity 607d ago · @jaydenpersonnat 🕒
- [ersilia-gui #28](https://github.com/ersilia-os/ersilia-gui/issues/28) — **Small tweaks to GUI** · open 1211d · last activity 1202d ago · @GemmaTuron 🕒
- [ersilia-gui #26](https://github.com/ersilia-os/ersilia-gui/issues/26) — **API to run** · open 1211d · last activity 1206d ago · @GemmaTuron 🕒
- [ersilia #1147](https://github.com/ersilia-os/ersilia/issues/1147) — **🐅 Epic: Adding support for Authentication in Ersilia** · open 886d · last activity 68d ago · @DhanshreeA 🕒
- [west-africa-mtb-lineage-drug-responses #1](https://github.com/ersilia-os/west-africa-mtb-lineage-drug-responses/issues/1) — **Meeting minutes 2024-08-15** · open 814d · last activity 802d ago · @fafaal3107 🕒
- [west-africa-mtb-lineage-drug-responses #2](https://github.com/ersilia-os/west-africa-mtb-lineage-drug-responses/issues/2) — **Meeting minutes 2024-08-22** · open 803d · last activity 801d ago · @fafaal3107 🕒
- [west-africa-mtb-lineage-drug-responses #3](https://github.com/ersilia-os/west-africa-mtb-lineage-drug-responses/issues/3) — **Meeting minutes 29/08/2024** · open 796d · last activity 796d ago · @fafaal3107 🕒
- [west-africa-mtb-lineage-drug-responses #4](https://github.com/ersilia-os/west-africa-mtb-lineage-drug-responses/issues/4) — **Meeting_minutes_05092024** · open 788d · last activity 788d ago · @fafaal3107 🕒
- [west-africa-mtb-lineage-drug-responses #5](https://github.com/ersilia-os/west-africa-mtb-lineage-drug-responses/issues/5) — **Meeting_minutes_03/10/2024** · open 765d · last activity 765d ago · @fafaal3107 🕒
- [aws-utils #8](https://github.com/ersilia-os/aws-utils/issues/8) — **Launch Bastion host** · open 727d · last activity 586d ago · @IamEddie 🕒
_…and 119 more open issues (129 open in total)._

### 💡 Easy wins
- [chem-sampler #7](https://github.com/ersilia-os/chem-sampler/issues/7) — **Remove models from the store** · fully specified CLI subcommand · @arnaucoma24
- [ersilia-skills #52](https://github.com/ersilia-os/ersilia-skills/issues/52) — **GitHub Digest check for idle branches** · small addition to one script · @miquelduranfrigola

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
- `chem-sampler` — marked Idle but had activity this week
- `digests` — marked Completed but had activity this week
- `eos-template` — marked Completed but had activity this week
- `ersilia` — marked Completed but had activity this week
- `ersilia-model-workflows` — marked Completed but had activity this week
- `ersilia-pack` — marked Completed but had activity this week
- `ersilia-self-service` — marked Completed but had activity this week

## 📊 Repository overview
186 tracked repos (270 model packages tracked separately) · 46 archived.  
**By type:** Analysis 68 · Package 67 · Automation 13 · Workshop 11 · App 7 · Template 5 · Documentation 3 · unset 13  
**By status:** Completed 78 · In progress 42 · Archived 19 · Discontinued 17 · Idle 14 · Todo 3 · unset 13

## ✅ Recent activity

### Pull requests merged
- [chemicl #19](https://github.com/ersilia-os/chemicl/pull/19) — **Ai2ase/paper v1** · @OhhMoo · 2026-11-06
- [digests #7](https://github.com/ersilia-os/digests/pull/7) — **Redesign site from DESIGN.md + LinkedIn social previews** · @miquelduranfrigola · 2026-11-05
- [digests #8](https://github.com/ersilia-os/digests/pull/8) — **Fit the year calendar to its card** · @miquelduranfrigola · 2026-11-05
- [digests #9](https://github.com/ersilia-os/digests/pull/9) — **Bounded sidebar, archive pages and older/newer links** · @miquelduranfrigola · 2026-11-05
- [eos-template #97](https://github.com/ersilia-os/eos-template/pull/97) — **Warm serving: split template main.py into load_tool and run_tool** · @SoufianeAatab · 2026-11-04
- [eos-template #98](https://github.com/ersilia-os/eos-template/pull/98) — **Build and upload the Apptainer image after release and for new models** · @SoufianeAatab · 2026-11-04
- [ersilia #1965](https://github.com/ersilia-os/ersilia/pull/1965) — **Add Apptainer image URL to model metadata** · @SoufianeAatab · 2026-11-04
- [ersilia-book #3](https://github.com/ersilia-os/ersilia-book/pull/3) 📄 — **Checkpoints and training data in git unless a file is over 100 MB** · @arnaucoma24 · 2026-11-05
- [ersilia-model-workflows #10](https://github.com/ersilia-os/ersilia-model-workflows/pull/10) — **Apptainer sif** · @Marina18 · 2026-11-04
- [ersilia-model-workflows #11](https://github.com/ersilia-os/ersilia-model-workflows/pull/11) — **Apptainer follow-up: created-release output, dry_run cleanup and README** · @SoufianeAatab · 2026-11-04
- [ersilia-model-workflows #12](https://github.com/ersilia-os/ersilia-model-workflows/pull/12) — **Allow unprivileged user namespaces before the SIF smoke test** · @SoufianeAatab · 2026-11-05
- [ersilia-pack #94](https://github.com/ersilia-os/ersilia-pack/pull/94) — **Warm serving: keep migrated models loaded between batches** · @SoufianeAatab · 2026-11-04
- [ersilia-skills #55](https://github.com/ersilia-os/ersilia-skills/pull/55) — **Release skill: post-upload in progress is running, not failed; retry GitHub 5xx** · @arnaucoma24 · 2026-11-03
- [ersilia-skills #56](https://github.com/ersilia-os/ersilia-skills/pull/56) — **literature-digest: fix DOI truncation and Gmail per-entry parsing** · @miquelduranfrigola · 2026-11-02
- [ersilia-skills #57](https://github.com/ersilia-os/ersilia-skills/pull/57) — **Add model-speedup skill** · @SoufianeAatab · 2026-11-05
- [ersilia-skills #58](https://github.com/ersilia-os/ersilia-skills/pull/58) — **Add model-gpu skill** · @SoufianeAatab · 2026-11-05
- [ersilia-skills #59](https://github.com/ersilia-os/ersilia-skills/pull/59) 📄 — **Add model-speedup to the README** · @SoufianeAatab · 2026-11-06
- [ersilia-stats #2](https://github.com/ersilia-os/ersilia-stats/pull/2) — **Second round of team feedback, private projects, shorter chart notes** · @SoufianeAatab · 2026-11-06
- [ersilia-stats #3](https://github.com/ersilia-os/ersilia-stats/pull/3) — **Chart fixes: histogram mean line, task-tree labels, full star history** · @SoufianeAatab · 2026-11-06
- [gradi-target-prioritization #1](https://github.com/ersilia-os/gradi-target-prioritization/pull/1) — **v2: per-axis pipeline, E. coli shortlist, new target browser** · @miquelduranfrigola · 2026-11-06
- [gradi-target-prioritization #2](https://github.com/ersilia-os/gradi-target-prioritization/pull/2) — **webapp: validate saved/shared state, remove Previous version link** · @miquelduranfrigola · 2026-11-06
- [gradi-target-prioritization #3](https://github.com/ersilia-os/gradi-target-prioritization/pull/3) — **webapp: laptop layout polish, no visual redesign** · @miquelduranfrigola · 2026-11-06
- [gradi-target-prioritization #4](https://github.com/ersilia-os/gradi-target-prioritization/pull/4) — **webapp: pin the band-row corner cell on horizontal scroll** · @miquelduranfrigola · 2026-11-06
- [gradi-target-prioritization #5](https://github.com/ersilia-os/gradi-target-prioritization/pull/5) 🔧 — **ci: bump Pages workflow actions to Node 24 majors** · @miquelduranfrigola · 2026-11-06
- [gradi-target-prioritization #6](https://github.com/ersilia-os/gradi-target-prioritization/pull/6) 🔧 — **ci: pin Pages runner to ubuntu-24.04** · @miquelduranfrigola · 2026-11-06
- [gradi-target-prioritization #7](https://github.com/ersilia-os/gradi-target-prioritization/pull/7) — **webapp: social preview card** · @miquelduranfrigola · 2026-11-06
- [gradi-target-prioritization #8](https://github.com/ersilia-os/gradi-target-prioritization/pull/8) — **Pockets score on native scales, Ligand precedence label, sidebar filter polish** · @miquelduranfrigola · 2026-11-07
- [gradi-target-prioritization #9](https://github.com/ersilia-os/gradi-target-prioritization/pull/9) — **webapp: merge Unknown + No COG hit chips; remove Evidence level menu** · @miquelduranfrigola · 2026-11-07
- [gradi-target-prioritization #10](https://github.com/ersilia-os/gradi-target-prioritization/pull/10) — **webapp: weighted score as a radar (Novelty axis, equal defaults)** · @miquelduranfrigola · 2026-11-07
- [gradi-target-prioritization #11](https://github.com/ersilia-os/gradi-target-prioritization/pull/11) — **webapp: tidy the radar and the table header** · @miquelduranfrigola · 2026-11-07
- [gradi-target-prioritization #12](https://github.com/ersilia-os/gradi-target-prioritization/pull/12) — **webapp: map slider fix, same columns on both species, table polish** · @miquelduranfrigola · 2026-11-07
- [gradi-target-prioritization #13](https://github.com/ersilia-os/gradi-target-prioritization/pull/13) — **webapp: Compare says "Ligand prec."** · @miquelduranfrigola · 2026-11-07
- [gradi-target-prioritization #14](https://github.com/ersilia-os/gradi-target-prioritization/pull/14) — **webapp: glitch pass (phone tabs, localization legend, short names, Compare)** · @miquelduranfrigola · 2026-11-07
- [gradi-target-prioritization #15](https://github.com/ersilia-os/gradi-target-prioritization/pull/15) — **webapp: map tooltip, legend scale, card title without gene** · @miquelduranfrigola · 2026-11-07
- [gradi-target-prioritization #16](https://github.com/ersilia-os/gradi-target-prioritization/pull/16) — **webapp: map labels, localization names on the map, header clipping** · @miquelduranfrigola · 2026-11-07
- [gradi-target-prioritization #17](https://github.com/ersilia-os/gradi-target-prioritization/pull/17) — **webapp: card title clear of the navigation buttons** · @miquelduranfrigola · 2026-11-07
- [gradi-target-prioritization #19](https://github.com/ersilia-os/gradi-target-prioritization/pull/19) — **webapp: gene card redesign** · @miquelduranfrigola · 2026-11-08
- [gradi-target-prioritization #20](https://github.com/ersilia-os/gradi-target-prioritization/pull/20) — **webapp: feedback round** · @miquelduranfrigola · 2026-11-08
- [gradi-target-prioritization #21](https://github.com/ersilia-os/gradi-target-prioritization/pull/21) — **webapp: audit round** · @miquelduranfrigola · 2026-11-08
- [olinda #35](https://github.com/ersilia-os/olinda/pull/35) — **Docstrings, console package, shorter functions; release 1.4.1** · @miquelduranfrigola · 2026-11-04
- [olinda #36](https://github.com/ersilia-os/olinda/pull/36) — **Split hard/train.py, shorten the last long functions; release 1.4.2** · @miquelduranfrigola · 2026-11-04
- [tcolf-antimalarials #160](https://github.com/ersilia-os/tcolf-antimalarials/pull/160) — **log: stage-08 entries of 2026-10-31 that never reached main** · @TiagoJanela · 2026-11-02
- [tcolf-antimalarials #161](https://github.com/ersilia-os/tcolf-antimalarials/pull/161) — **stage08: the Lilly rules exclude unusual elements (log + note)** · @TiagoJanela · 2026-11-03
- [tcolf-antimalarials #162](https://github.com/ersilia-os/tcolf-antimalarials/pull/162) — **dashboard: real-data test numbers for the fixed-CLAMP scores** · @TiagoJanela · 2026-11-07

### Pull requests opened
- [ersilia #1958](https://github.com/ersilia-os/ersilia/pull/1958) 🔧 — **build(deps): bump actions-js/push from 1.5 to 1.6** · @dependabot[bot] · 2026-11-01
- [ersilia #1959](https://github.com/ersilia-os/ersilia/pull/1959) 🔧 — **build(deps): bump actions/setup-python from 6 to 7** · @dependabot[bot] · 2026-11-01
- [ersilia #1960](https://github.com/ersilia-os/ersilia/pull/1960) 🔧 — **build(deps): bump GrantBirki/comment from 2.1.1 to 3.0.3** · @dependabot[bot] · 2026-11-01
- [ersilia #1961](https://github.com/ersilia-os/ersilia/pull/1961) 🔧 — **build(deps): bump GrantBirki/json-yaml-validate from 4.0.0 to 5.0.1** · @dependabot[bot] · 2026-11-01
- [ersilia #1962](https://github.com/ersilia-os/ersilia/pull/1962) 🔧 — **build(deps): bump actions/checkout from 6.0.0 to 7.0.1** · @dependabot[bot] · 2026-11-01
- [ersilia #1966](https://github.com/ersilia-os/ersilia/pull/1966) — **GPU images: -gpu Dockerfiles, Device metadata field, fetch --gpu and GPU serving** · @SoufianeAatab · 2026-11-06
- [ersilia-book #4](https://github.com/ersilia-os/ersilia-book/pull/4) 📄 — **Clarify model release versioning and add a pre-release checklist** · @arnaucoma24 · 2026-11-04
- [ersilia-book #5](https://github.com/ersilia-os/ersilia-book/pull/5) 📄 — **Add Apptainer (Singularity) images page and SIF workflow jobs** · @SoufianeAatab · 2026-11-06
- [ersilia-book #6](https://github.com/ersilia-os/ersilia-book/pull/6) 📄 — **Add Warm serving page and update main.py to load_tool/run_tool** · @SoufianeAatab · 2026-11-06
- [ersilia-mcp #67](https://github.com/ersilia-os/ersilia-mcp/pull/67) 🔧 — **chore(deps): bump the python group across 1 directory with 3 updates** · @dependabot[bot] · 2026-11-04
- [ersilia-mcp #68](https://github.com/ersilia-os/ersilia-mcp/pull/68) 🐛 — **Fix release hygiene: PyPI isaura, exact pins, version sync** · @miquelduranfrigola · 2026-11-04
- [ersilia-mcp #69](https://github.com/ersilia-os/ersilia-mcp/pull/69) — **Return structured errors from the core model tools** · @miquelduranfrigola · 2026-11-04
- [ersilia-mcp #70](https://github.com/ersilia-os/ersilia-mcp/pull/70) — **Cap tool output sizes and note that fetch_model is idempotent** · @miquelduranfrigola · 2026-11-04
- [ersilia-mcp #71](https://github.com/ersilia-os/ersilia-mcp/pull/71) — **Log the duration of every tool call** · @miquelduranfrigola · 2026-11-04
- [ersilia-mcp #72](https://github.com/ersilia-os/ersilia-mcp/pull/72) — **Report real progress for fetch, serve and predict; keep Ersilia output off stdout** · @miquelduranfrigola · 2026-11-04
- [ersilia-model-workflows #13](https://github.com/ersilia-os/ersilia-model-workflows/pull/13) — **Build, test and tag GPU images in CI** · @SoufianeAatab · 2026-11-06
- [ersilia-pack #95](https://github.com/ersilia-os/ersilia-pack/pull/95) 📄 — **Document warm serving in README** · @SoufianeAatab · 2026-11-05
- [ersilia-pack #96](https://github.com/ersilia-os/ersilia-pack/pull/96) — **Add --device gpu: build from the gpu: section of install.yml** · @SoufianeAatab · 2026-11-06
- [gradi-target-prioritization #18](https://github.com/ersilia-os/gradi-target-prioritization/pull/18) 📄 — **docs: v2.0.1 notes** · @miquelduranfrigola · 2026-11-07
- [zairachem-docker #79](https://github.com/ersilia-os/zairachem-docker/pull/79) 🔧 — **Update matplotlib requirement from 3.10.0 to 3.11.2** · @dependabot[bot] · 2026-11-02
- [zairachem-docker #80](https://github.com/ersilia-os/zairachem-docker/pull/80) 🔧 — **Update click requirement from 8.4.2 to 8.5.0** · @dependabot[bot] · 2026-11-02
- [zairachem-docker #81](https://github.com/ersilia-os/zairachem-docker/pull/81) — **Write held descriptor matrices to the store in chunks** · @TiagoJanela · 2026-11-02

_The other 41 PRs opened this week were merged in the same window and are listed above._

### Issues closed
- [chem-sampler #8](https://github.com/ersilia-os/chem-sampler/issues/8) — **Define how a run handles several seeds** · @arnaucoma24 · 2026-11-03
- [ersilia #1937](https://github.com/ersilia-os/ersilia/issues/1937) — **ersilia deep test fails when the first deterministic example returns no output** · @arnaucoma24 · 2026-11-03
- [ersilia #1945](https://github.com/ersilia-os/ersilia/issues/1945) 🐛 — **🐛 Bug: Model README joins the incorporation and packaging dates with no space** · @arnaucoma24 · 2026-11-03
- [ersilia #1950](https://github.com/ersilia-os/ersilia/issues/1950) — **🦠 Model Request: Molport Library Similarity** · @arnaucoma24 · 2026-11-02
- [ersilia #1951](https://github.com/ersilia-os/ersilia/issues/1951) — **🦠 Model Request: Enamine REAL Sample Similarity** · @arnaucoma24 · 2026-11-03

### Issues opened
- [chem-sampler #6](https://github.com/ersilia-os/chem-sampler/issues/6) — **Give annotators on the command line, with prompts for their settings** · @arnaucoma24 · 2026-11-02
- [chem-sampler #7](https://github.com/ersilia-os/chem-sampler/issues/7) — **Remove models from the store** · @arnaucoma24 · 2026-11-02
- [chem-sampler #8](https://github.com/ersilia-os/chem-sampler/issues/8) — **Define how a run handles several seeds** · @arnaucoma24 · 2026-11-02
- [ersilia #1963](https://github.com/ersilia-os/ersilia/issues/1963) — **ersilia test: output CSV reader ignores quoting, so columns with commas skip the consistency check** · @arnaucoma24 · 2026-11-02
- [ersilia #1964](https://github.com/ersilia-os/ersilia/issues/1964) — **Post-upload can leave 'null' performance values that fail every later image-test re-run** · @arnaucoma24 · 2026-11-03
- [ersilia-mcp #65](https://github.com/ersilia-os/ersilia-mcp/issues/65) 🐛 — **🐛 Bug: Fetching a model is flaky** · @Lehcar · 2026-11-02
- [ersilia-mcp #66](https://github.com/ersilia-os/ersilia-mcp/issues/66) 🐛 — **🐛 Bug: Lots of error output when using a codespace with Ollama** · @Lehcar · 2026-11-02
- [ersilia-model-workflows #9](https://github.com/ersilia-os/ersilia-model-workflows/issues/9) — **Reduce the CI cost of slow models** · @arnaucoma24 · 2026-11-04
- [ersilia-self-service #514](https://github.com/ersilia-os/ersilia-self-service/issues/514)–[#519](https://github.com/ersilia-os/ersilia-self-service/issues/519) — **🚀 Model Inference Run** for eos18ie, eos3f8h, eos9ei3, eos1klk and eos3804 (×2) · @miquelduranfrigola · 2026-11-03 to 2026-11-06

**Model repos (eosXXXX):** 2 PRs merged · 2 opened · 1 issues closed · 2 opened — across 23 repos. Managed via the model-incorporation flow.
