# Ersilia Literature Digest — Week of 2026-10-13

**Connectors:** Alerts and Newsletters 🟢 · Slack 🟢 · Europe PMC 🟢 · bioRxiv 🟢 · Web hunt 🔴  
**Markers:** ⭐ High impact · 🌍 LMIC · 🤖 Candidate model · 🗃️ Interesting dataset · 💻 Code available  
**Tasks:** 🧪 Property · 🎯 Activity · 🧩 Featurization · 🗺️ Projection · 🔍 Similarity · 🎨 Generative

## 🤖 Models that could join the Hub

### 🎯 Activity prediction

- [Singh et al., *bioRxiv*, 2026-10-02](https://doi.org/10.64898/2026.09.28.754881) 🌍🤖❓💻 — **MtbAIM: AI/ML-guided endpoint-specific prediction of small-molecule activity across drug-susceptible and drug-resistant *Mycobacterium tuberculosis*.** Conditional Hub candidate via One-to-many deployment. Paper contributes: SMILES → active/inactive and pMIC (MIC, MIC90, MIC99) models for *M. tuberculosis* H37Rv, trained on ChEMBL v37 (about 25.6k drug-susceptible and 3.7k drug-resistant compounds). Hub would do: wrap the classification and regression endpoints as separate Activity entries. Prerequisite: the GitHub repository declares no licence and weight release is not stated, so both need confirming. Priority: High because TB whole-cell activity is a named Hub gap. · [code](https://github.com/jasdeep002/MtbAIM) · 🎯

### 🧪 Property prediction

- [Jang et al., *bioRxiv*, 2026-07-08](https://doi.org/10.64898/2026.07.02.736062) 🤖💻 — **PredHLM: quantitative and interpretable prediction of metabolic half-life in human liver microsomes.** Open-source property-prediction model taking SMILES → log10 HLM half-life (regression, 30 min binarisation available); released with trained models, curated data (11,790 compounds) and code under MIT. Plausible Hub addition because microsomal stability is a core ADMET endpoint (test R² 0.43, modest) and the XGBoost-on-RDKit-descriptor design is cheap to containerise. Posting date is the first bioRxiv version; the feed listed it in this window. · [code](https://github.com/joshua-416/PredHLM) · 🧪
- [Muskal et al., *bioRxiv*, 2026-10-11](https://doi.org/10.64898/2026.10.04.756566) 🤖❓ — **Toxicity by Consortium Revisited: Structural Neighbors and Cross-Family Reach.** Conditional Hub candidate via Surrogate distillation. Paper contributes: a nearest-neighbour toxicity method (rat oral LD50 on 11,989 compounds plus 28 endpoints over 34,162 compounds) served with data at toxpred.ai. Hub would do: query the server or train on the released pool → Property entry for acute toxicity. Prerequisite: licence of the software and data is unstated and no code repository is confirmed. Priority: Medium because the Hub already covers several toxicity endpoints. · 🧪

## 🗃️ Datasets that could join the Hub

_Nothing this week — no openly-released ≥10k-row datasets cleared the dataset checklist._

## AI/ML methods for drug discovery

- [Seo et al., *bioRxiv*, 2026-10-08](https://doi.org/10.64898/2026.10.01.755933) 💻 — **Synthesis-aware generative design in trillion-scale chemical spaces for automated drug discovery.** RxnFlow, an MIT-licensed generative flow network over reaction logic, searches an 11-trillion-compound make-on-demand space and is demonstrated on a structure-based target. (Input: protein structure in the reported application; unconditional use for the Hub generator interface is untested.) · [code](https://github.com/SeonghwanSeo/RxnFlow)
- [Hirte et al., *J Cheminform*, 2026-10-06](https://doi.org/10.1186/s13321-026-01312-4) — **The NERDD microservices platform for deploying machine learning models in drug discovery.** Open-access platform for serving predictive models as services; its design choices are worth comparing with how the Ersilia Model Hub packages and exposes models. Code repository not verified here.
- [Muskal et al., *bioRxiv*, 2026-10-11](https://doi.org/10.64898/2026.10.03.756481) — **Human Intestinal Absorption Revisited: The 1998 Descriptors Survive, and the Method Extends to Permeability.** Random-forest absorption and permeability models served at predicthia.ai with downloadable data and fitted models. Training sets are small (780 absorption compounds, 3,771 Caco-2) and no licence is stated, so it stays context.
- [Cao et al., *Nat Commun*, 2026-10-01](https://doi.org/10.1038/s41467-026-78105-8) — **Evaluating generative models for structure-based drug discovery from de novo design to lead optimization.** Benchmark of structure-based generators across the design-to-optimisation range; useful for judging which pocket-conditioned generators merit attention once the Hub supports protein input. (License: CC-BY-NC-ND; input: protein pocket.)
- [Cretu et al., *arXiv*, 2026-10-08](https://arxiv.org/abs/2610.11454) — **Zatom-2: Multitask Pretraining on Atomistic Data for Generative Modeling across Domains.** Multiscale transformer with conditional flow matching pretrained on about 5 million molecule and material structures. (Input: atomistic 3D structures; no code or weights linked from the abstract page.)
- [Cropsal et al., *arXiv*, 2026-10-06](https://arxiv.org/abs/2610.07997) — **Can phenotypic activity be predicted without experimental readouts?** Tests whether encoders pretrained on molecule–morphology pairs (CLOOME, CellCLIP) can replace Cell Painting for phenotypic activity prediction; they show no clear advantage over plain physicochemical descriptors, a useful caution for phenotypic featurizers. No code linked.
- [Kim et al., *ACS Omega*, 2026-09-28](https://doi.org/10.1021/acsomega.6c07302) — **DEG2MOL: Conditional Latent Flow Matching for Transcriptome-Guided *de novo* Drug Design.** (Input: differential-expression signatures, outside the current small-molecule-input Hub surface; CC-BY.)

## Antibiotic and antimicrobial discovery

- [Kulkarni et al., *Sci Transl Med*, 2026-10-07](https://doi.org/10.1126/scitranslmed.aed8353) — **Transient receptor potential channel activation targets multiple stages of the schistosome parasite.** Schistosomiasis target biology with direct relevance to antiparasitic screening beyond praziquantel.
- [Deans et al., *bioRxiv*, 2026-10-10](https://doi.org/10.64898/2026.10.09.757903) — **Repurposing clofarabine against enteric pathogens via metabolic starvation.** A phenotypic screen identifies the anticancer drug clofarabine as an inhibitor of EPEC/EHEC growth and virulence, a repurposing lead for diarrhoeal pathogens.
- [Zhong et al., *RSC Med Chem*, 2026](https://doi.org/10.1039/d6md00631k) — **Fluorination of amino-quinones enhances anti-*Trypanosoma cruzi* activity.** SAR campaign on a Chagas disease chemotype; a candidate source of labelled data for kinetoplastid models.
- [Wolf et al., *bioRxiv*, 2026-10-12](https://doi.org/10.64898/2026.10.10.758198) — **Isoindole-benzohydrazide derivative potentiates colistin activity to overcome resistance conferred by MCR-1 variants in *Escherichia coli*.** Adjuvant approach to restore colistin activity against plasmid-borne resistance.
- [Adeyina et al., *bioRxiv*, 2026-10-11](https://doi.org/10.64898/2026.10.10.758085) — **Forecasting next-year change in antimicrobial resistance genes in *Klebsiella pneumoniae* and *Acinetobacter baumannii* from genomic surveillance data.** Predicts gene-level turnover (AUROC 0.91 in *K. pneumoniae*) and emergence (0.79 in *A. baumannii*) from AMRFinderPlus-annotated genomes. (Input: genomes, not molecules.)

## AI agents and foundation models for science

- [Llompart et al., *arXiv*, 2026-10-05](https://arxiv.org/abs/2610.06411) — **From Benchmark to Bench: Can Agents Survive Real-World Drug Discovery?** The open modular agent MAGI was run on nine retrospective lead-optimisation campaigns from three pharma companies; LLM proposals stayed closer to local chemistry and matched or beat activity in fewer operations, while success tracked predictive-model accuracy rather than generation route.
- [Smbatyan et al., *bioRxiv*, 2026-10-08](https://doi.org/10.64898/2026.10.01.755314) — **Evaluating Autonomous LLM Agents Across Molecular Prediction and Optimization Benchmarks.** LLM coding agents built ADMET, PXR and optimisation methods that often matched human-developed ones, though some wins held only under standard benchmark setups. No code or reuse licence is stated.

## Global health and open science

- [Yadav et al., *bioRxiv*, 2026-10-09](https://doi.org/10.64898/2026.10.04.756602) 🌍 — **Anti-target chemical-space coverage of Indian medicinal plant phytochemicals.** India-led analysis of how natural-product libraries cover anti-targets, relevant to safety profiling of traditional-medicine chemistry. (License: CC-BY-NC.)
