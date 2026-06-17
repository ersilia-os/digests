# Ersilia Literature Digest — Week of 2026-06-17

**Connectors:** Alerts and Newsletters 🟢 · Slack 🟢 · Europe PMC 🟢 · bioRxiv 🟢 · Web hunt 🟢
**Markers:** ⭐ High impact · 🌍 LMIC · 🤖 Candidate model · 🗃️ Interesting dataset · 💻 Code available
**Tasks:** 🧪 Property · 🎯 Activity · 🧩 Featurization · 🗺️ Projection · 🔍 Similarity · 🎨 Generative

## 🤖 Models that could join the Hub

### 🎯 Activity prediction

- [Zhang et al., *Bioinformatics*, 2026-06-15](https://doi.org/10.1093/bioinformatics/btag392) 🤖 — **DrugDL: dual-modal deep learning for multi-property drug prediction.** Open compound–protein model taking SMILES + target sequence → DTI, binding affinity, binding site and physicochemical/toxicity outputs via cross-modal contrastive learning; published with an availability statement (confirm repo/license before packaging). Plausible Hub addition because one backbone covers several activity-prediction endpoints the Hub serves piecemeal today. · 🎯
- [Zhou et al., *Interdiscip Sci*, 2026-06-15](https://doi.org/10.1007/s12539-026-00839-2) 🤖 — **Deep3D-DTA: tri-modal binding-affinity prediction.** Open activity model taking SMILES (plus 2D/3D structure) → drug–target affinity; fuses 1D/2D/3D molecular views to sharpen affinity estimates. Plausible Hub addition because affinity regressors that work without a resolved pocket fit the Hub's CPI niche. · 🎯
- [Wang et al., *J Chem Inf Model*, 2026-06-15](https://doi.org/10.1021/acs.jcim.6c01212) 🤖 — **MVR-DTI: multimodal molecular visual representation for drug–target interaction.** Open model taking SMILES + a rendered molecular image → interaction score; adds a visual modality to the usual graph/sequence encoders. Plausible Hub addition because it is a self-contained small-molecule-input DTI predictor. · 🎯
- [Çevik et al., *Sci Rep*, 2026-06-12](https://doi.org/10.1038/s41598-026-57478-2) 🤖 — **Fully sequence-based drug–target binding prediction.** Open activity model taking SMILES + protein sequence → binding prediction with no 3D-structure dependency, lowering the barrier to whole-proteome screening. Plausible Hub addition because structure-free CPI predictors run cheaply inside a model container. · 🎯

### 🧪 Property prediction

- [Du et al., *Sci Rep*, 2026-06-13](https://doi.org/10.1038/s41598-026-57761-2) 🤖 — **KAN-PROSPECT: Kolmogorov–Arnold Networks for natural-product effects.** Open property model taking small-molecule input → predicted efficacy and adverse effects, pairing transfer learning with KAN layers to cut reliance on wet-lab profiling. Plausible Hub addition because natural-product property prediction is a thin spot in current Hub coverage. · 🧪
- [Chitikela et al., *bioRxiv*, 2026-06-12](https://www.biorxiv.org/content/10.64898/2026.06.10.731399v1) 🤖 — **Graph-based QSAR pipeline for PubChem assays and in vivo toxicity.** Open model taking SMILES → caspase-3/7 apoptosis-assay activity and human toxicity readouts, framed as a chemical risk-assessment tool. Plausible Hub addition because graph QSAR over public bioassays is exactly the Activity/Property task family the Hub leans on. · 🧪

### 🧩 Featurization

- [Nguyen et al., *arXiv*, 2026-06-09](https://arxiv.org/abs/2606.11382) 🤖💻 — **GLACIER: a multimodal student–teacher foundation model for molecular property prediction.** Open featurization model taking molecular graph + SMILES + physicochemical descriptors → fused embeddings (and property heads); released with weights/code on GitHub under CC-BY-4.0, distilling teacher models into one lightweight encoder. Plausible Hub addition because a permissively-licensed multimodal embedder is a drop-in featurizer alongside ChemBERTa/MolFormer. · [code](https://github.com/eemokey/glacier) · 🧩

### 🎨 Generative

- [Österbacka et al., *chemRxiv*, 2026-06](https://doi.org/10.26434/chemrxiv.15004669) 🤖 — **OmniInvent: unified generative chemical language models via blank infilling.** Open generative model operating directly on SMILES to infill/complete molecules under multiple property constraints, from the REINVENT-lineage group (confirm weights/license at release). Plausible Hub addition because a single infilling backbone subsumes de novo, scaffold-decoration and linker tasks the Hub's generative family handles separately. · 🎨
- [Falcone et al., *J Chem Inf Model*, 2026-06-15](https://doi.org/10.1021/acs.jcim.6c00689) 🤖 — **PyMolGen: database-driven molecular generation of drug-like compounds.** Open rule-based generator that learns fragment-combination rules from a user database to emit synthetically tractable, drug-like molecules for constrained optimisation (confirm repo/license). Plausible Hub addition because a lightweight, dependency-light generator slots cleanly into the Hub's Generation task. · 🎨

## 🗃️ Datasets that could join the Hub

### ADMET / property datasets

- [OpenADMET–ExpansionRx, *Hugging Face*, 2026](https://huggingface.co/datasets/openadmet/openadmet-expansionrx-challenge-data) 🗃️ — **OpenADMET–ExpansionRx full ADMET dataset.** 15,226 compounds · 9 experimental ADMET endpoints (LogD, kinetic solubility, mouse/human microsomal clearance, Caco-2 permeability, plasma/brain protein binding) · CC-BY-4.0 · Hugging Face (CSV with SMILES). Plausible Hub input because it is real prosecuted-campaign ADMET data at training scale, ideal for benchmarking or training Hub ADMET predictors. · 🧪

## AI/ML methods for drug discovery

- [Xing et al., *Cell*, 2026-04](https://doi.org/10.1016/j.cell.2026.02.016) ⭐ — **Deep-learning de novo discovery and design of therapeutics that reverse disease-associated transcriptional phenotypes.** The GPS platform predicts gene-expression profiles from chemical structures, screens large libraries and optimises leads toward phenotype-reversing molecules; worth dissecting as a reference architecture (input couples chemical structure with transcriptomic signatures, so not a pure small-molecule model).
- [Yu et al., *Nat Chem Biol*, 2026-06-12](https://doi.org/10.1038/s41589-026-02241-x) ⭐ — **PBCNet2.0: atomic-level protein–ligand recognition for probe discovery.** Cartesian-tensor Siamese network trained on 8.6 M complexes for relative binding-affinity ranking; strong lead-optimisation signal but needs a protein–ligand complex as input (gated from the small-molecule-only Hub interface).
- [Fan et al., *J Chem Inf Model*, 2026-06-15](https://doi.org/10.1021/acs.jcim.6c00265) — **EC-Dock: a fast equivariant consistency model for molecular docking and virtual screening.** Speeds diffusion-style docking while improving physical validity; useful as a screening surrogate but requires the target pocket as input (input: protein structure + ligand).
- [Luo et al., *Nat Commun*, 2026-06-13](https://doi.org/10.1038/s41467-026-74101-0) — **Generative flow on distance geometry for reaction transition states.** Chemically-constrained generative model predicting transition-state geometries via an optimal-transport evolution path; a retrosynthesis-adjacent method (task is reaction TS prediction, not small-molecule design).
- [Aguilar-Bejarano et al., *J Cheminform*, 2026-06-12](https://doi.org/10.1186/s13321-026-01236-z) 💻 — **Benchmarking molecular representations and ML algorithms for asymmetric catalysis.** Systematic representation/algorithm comparison with open code; relevant to the under-represented Featurization/representation task family even though exemplified on metal–ligand catalysis rather than drug design.
- [Qiao et al., *Commun Chem*, 2026-06-17](https://doi.org/10.1038/s42004-026-02092-6) — **TAME-VS: target-driven ML-enabled virtual screening.** Addresses cross-scaffold generalisation and prospective validation under realistic synthesis constraints, demonstrated on AKR1C3; a workflow blueprint for ML-guided hit prioritisation.

## Antibiotic and antimicrobial discovery

- [Brown et al., *bioRxiv*, 2026-06-12](https://www.biorxiv.org/content/10.64898/2026.06.12.731830v1) — **BacPROTACs outperform inhibitors in *Mycobacterium tuberculosis*.** Targeted protein degradation beats occupancy-driven inhibition on Mtb targets, opening previously undruggable space relevant to the antitubercular pipelines Ersilia supports.
- [Shalaby et al., *bioRxiv*, 2026-06-16](https://www.biorxiv.org/content/10.64898/2026.06.12.731178v1) — **Induced alanine auxotrophy as an antitubercular strategy.** A repurposing screen surfaces hit TI-374 with sub-micromolar Mtb potency acting through a previously unexploited mechanism — a candidate scaffold for activity modelling.
- [Chacha et al., *bioRxiv*, 2026-06-08](https://www.biorxiv.org/content/10.1101/2026.06.08.730784) 🌍 — **Natural-product efflux inhibitors restore bedaquiline susceptibility in drug-resistant Mtb.** Kenyatta University (Kenya) work using efflux-pump inhibition to resensitise MDR/XDR Mtb — directly on-theme for antitubercular AMR and African-led drug discovery.
- [Jibrin et al., *Curr Pharm Anal*, 2026-06](https://doi.org/10.1016/j.cpan.2026.05.003) 🌍 — **In silico design of pyrazolopyridine PanC inhibitors as anti-TB leads.** Ahmadu Bello University (Nigeria) QSAR/docking campaign on pantothenate synthetase, an LMIC-led computational antitubercular effort whose series could seed Hub activity models.
- [Exapicheidou et al., *J Med Chem*, 2026-06](https://doi.org/10.1021/acs.jmedchem.5c02721) — **Hit-to-lead optimisation of ECF-transporter inhibitors as novel antibiotics.** Multiparameter optimisation of an antibacterial class targeting energy-coupling-factor transporters, with confirmed in vivo efficacy — a fresh Gram-positive target class.
- [Ganesamoorthy et al., *Biochimie*, 2026-06](https://doi.org/10.1016/j.biochi.2026.06.007) — **AdeABC efflux-pump inhibition reverts levofloxacin resistance in *Acinetobacter baumannii*.** Mechanistic AMR work on an ESKAPE priority pathogen, reinforcing efflux as a resensitisation strategy in Gram-negatives.

## AI agents and foundation models for science

- [Liu et al., *arXiv*, 2026-06](https://arxiv.org/abs/2606.12736) — **Benchmarking AI agents for scientific challenges across scales.** A multi-domain benchmark probing what research agents can actually do in real settings; a useful yardstick before betting on agentic workflows for cheminformatics and bioinformatics.
- [Vishwanath et al., *Nat Med*, 2026-06-12](https://doi.org/10.1038/s41591-026-04431-5) ⭐ — **General-purpose LLMs outperform specialised clinical models.** Evidence that broad foundation models plus good context beat narrowly-trained specialists — a signal that the same "build context, not bespoke models" lesson may hold for chemistry and bioinformatics tooling.

## Global health and open science

- [Xing et al., *npj Digit Med*, 2026-06-15](https://doi.org/10.1038/s41746-026-02880-3) — **Scoping review of traditional and AI methods in malaria diagnostics.** Maps where deep learning can address microscopy and rapid-test limitations, framing the diagnostic gaps that open-source tooling for endemic settings should target.
- [Ngor et al., *JMIR Public Health Surveill*, 2026-06-12](https://doi.org/10.2196/85881) — **Digital health-centre app for community and national malaria surveillance in Cambodia.** Implementation study supporting elimination efforts against multidrug-resistant *P. falciparum* in the Greater Mekong Subregion — a deployment-side complement to molecular antimalarial work.
- [Innocent et al., *BMC Infect Dis*, 2026-06-15](https://doi.org/10.1186/s12879-026-13784-8) — **Image-based ML for neglected-tropical-disease diagnosis.** Systematic appraisal of where image-based models do and do not yet deliver clinical utility in LMIC settings, a sober counterweight to diagnostic-AI hype.
