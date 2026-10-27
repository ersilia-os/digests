# Ersilia Literature Digest — Week of 2026-10-27

**Connectors:** Alerts and Newsletters 🟢 · Slack 🟢 · Europe PMC 🟢 · bioRxiv 🟢 · Web hunt 🟢  
**Markers:** ⭐ High impact · 🌍 LMIC · 🤖 Candidate model · 🗃️ Interesting dataset · 💻 Code available  
**Tasks:** 🧪 Property · 🎯 Activity · 🧩 Featurization · 🗺️ Projection · 🔍 Similarity · 🎨 Generative

## 🤖 Models that could join the Hub

### 🧪 Property prediction

- [Almeida et al., *arXiv*, 2026-10-21](https://arxiv.org/abs/2610.29589) 🤖💻 — **Fragment-Level Graph Encoding for Interpretable Molecular Property Prediction.** Open-source property-prediction framework taking SMILES → property label plus per-fragment attributions; released with code under MIT (weights: pending, train-your-own CLI). Plausible Hub addition because its benchmark tasks include PTR1, a kinetoplastid target, and the attributions would add interpretability to the Hub. · [code](https://github.com/4D-Lab/frame) · 🧪

### 🧩 Featurization

- [Kulczykowski et al., *Research Square*, 2026-10-22](https://doi.org/10.21203/rs.3.rs-11151541/v1) 🤖💻 — **Self-Supervised Pretraining of Molecular Graph Encoders with LeJEPA.** Open-source featurization model taking SMILES → graph embedding (GPS and D-MPNN encoders pretrained on ~2.9M ChEMBL molecules); released with three pretrained backbones (~55 MB) and code under MIT. Plausible Hub addition because embeddings add signal beyond Morgan fingerprints (molhiv ROC-AUC 0.803 → 0.830) and were tested on an antibiotic dataset, though the gain is modest. · [code](https://github.com/GlockPL/MolecularLeJEPA) · 🧩

## 🗃️ Datasets that could join the Hub

_Nothing this week — no openly-released ≥10k-row datasets cleared the dataset checklist._

## AI/ML methods for drug discovery

- [Kaminski et al., *J Cheminform*, 2026-10-18](https://doi.org/10.1186/s13321-026-01317-z) — **χ-SOM: emergent self-organizing maps for large chemical space visualization.** Projection method for large chemical spaces; repo and licence could not be verified, so no 🤖. Projection is one of the thinnest Hub task families, so worth a follow-up for code.
- [Sun et al., *J Chem Inf Model*, 2026-10-20](https://doi.org/10.1021/acs.jcim.6c02297) — **Structure Prototype Learning for Federated Molecular Property Prediction under Scaffold Heterogeneity.** Federated learning across private chemical libraries, relevant to data-sharing with partners; beat FedAvg in only 7 of 15 settings and no code was verified.
- [Rich et al., *ChemMedChem*, 2026-10-18](https://doi.org/10.1002/cmdc.70531) — **Evaluating Machine Learning Affinity Prediction Methods on Novel Lead Optimization Data: A 15-PGDH Case Study.** Prospective benchmark of ML affinity predictors, including Boltz-2, on novel lead-optimisation data; a useful reality check for structure-based scoring, no model released.
- [Qi et al., *PLOS Comput Biol*, 2026-10-21](https://doi.org/10.1371/journal.pcbi.1014861) 💻 — **SADRP: A structurally aware multi-modal framework for drug response prediction.** Drug-response model that also needs cell-line omics input, so outside the current small-molecule-only Hub surface. · [code](https://github.com/userabc11/SADRP)
- [Zhuang et al., *Findings of EMNLP*, 2026-10](https://aclanthology.org/2026.findings-emnlp.1796/) — **MppReasoner: Reasoning-Enhanced LLMs for Molecular Property Prediction.** Reasoning-trace LLM property predictor (input: SMILES plus 2D image; ≥4×A100; weights pending; repo has no licence), so not Hub-ready; revisit when weights and a licence appear.
- [Liu et al., *Findings of EMNLP*, 2026-10](https://aclanthology.org/2026.findings-emnlp.1524/) — **FragmentGPT: Unified Fragment Growing, Linking, and Merging.** Chemical language model covering all three fragment operations, evaluated on SARS-CoV-2 3CLpro; no code or weights listed.
- [Chen et al., *arXiv*, 2026-10-19](https://arxiv.org/abs/2610.25605) — **PRISM: Prior Relational Information for Self-supervised Modeling to Enhance Solubility OOD Generalization.** Label-free relational-prior pretraining for out-of-distribution solubility prediction; no code listed, so not 🤖 for now.
- [Saadi et al., *arXiv*, 2026-10-22](https://arxiv.org/abs/2610.30903) — **Same molecule, Different Knowledge: Cross-Identifier Binding Failures in LLMs for Chemistry.** Shows LLMs retrieve facts from molecule names but not from SMILES and proposes Binding Self-Distillation; a caution for LLM-based chemistry agents.
- [Park et al., *arXiv*, 2026-10-11](https://arxiv.org/abs/2610.15284) — **FragFlex: Fragment-Based Flexible Molecular Generation for Exploring Vast Chemical Space.** Fragment-based generator posted just before the window; no repo located on the abstract page, so not a 🤖 candidate yet.

## Antibiotic and antimicrobial discovery

- [Westrate et al., *ACS Infect Dis*, 2026-10-20](https://doi.org/10.1021/acsinfecdis.6c00472) — **An AI Modeling and Structural Clustering Approach to QAC Disinfectant Development.** Applies ML and structural clustering to quaternary ammonium disinfectants; no code or weights verified.
- [Qin et al., *arXiv*, 2026-10-24](https://arxiv.org/abs/2610.33809) — **MechGate: combining mechanism-derived measures of permeation and efflux to screen small molecule drugs targeting *Escherichia coli*.** SMILES → five *E. coli* scores (porin and membrane permeation, efflux, antibacterial activity). The abstract says all code is open-source, but no repo URL or licence was found, so no 🤖 until one appears; high priority to re-check.
- [Wang et al., *Access Microbiol*, 2026-10-20](https://doi.org/10.1099/acmi.0.001315.v2) — **An automated, open-source pipeline for anti-virulence compound discovery.** Multi-target docking pipeline described as open-source, but no repository was found.
- [Malik et al., *ACS Omega*, 2026-10-22](https://doi.org/10.1021/acsomega.6c08419) — **Thiochromene Analogues as Antiparasitic Chemotype: Synthesis, Antiplasmodial and Antitrypanosomal activity.** New chemotype with activity against *Plasmodium* and trypanosomes; relevant to antiparasitic coverage.
- [de Lima et al., *ACS Omega*, 2026-10-22](https://doi.org/10.1021/acsomega.6c06826) — **Nitrile-Based *Leishmania* Cysteine Protease B Inhibitors with In Vivo Efficacy against Visceral Leishmaniasis.** Nitrile inhibitors of a *Leishmania* protease with in vivo efficacy; an SAR series of interest for kinetoplastid activity models.
- [Ng'etich et al., *bioRxiv*, 2026-10-26](https://doi.org/10.64898/2026.10.25.761520) — **Structural insights and mechanistic inhibition of *Plasmodium falciparum* dihydroorotate dehydrogenase.** Structural study of a validated antimalarial target.
- [Yang et al., *npj Antimicrob Resist*, 2026-10-22](https://doi.org/10.1038/s44259-026-00287-4) — **LLM-powered construction of antibiotic resistance datasets and knowledge graphs.** LLM-built gene-level resistance resources; released under CC-BY-NC-ND and gene-level rather than compound-level, so not a Hub dataset.
- [Hy et al., *arXiv*, 2026-10-21](https://arxiv.org/abs/2610.29096) 💻 — **AMP Atlas: A Browser-Only Workbench for Antimicrobial Peptide Exploration and Interactive Helical-Wheel Design.** DRAMP-derived workbench (5,183 SMILES annotations, below the dataset bar; input: peptide sequence, outside the Hub small-molecule surface). · [code](https://github.com/HySonLab/amp-atlas)

## AI agents and foundation models for science

- [Seo et al., *Sci Rep*, 2026-10-20](https://doi.org/10.1038/s41598-026-76339-6) — **Natural-language prompting builds and operates an open-source software workflow for virtual drug discovery.** Uses natural-language prompting to build and operate an open-source virtual drug-discovery workflow; relevant to LLM-driven tooling around the Hub.

## Global health and open science

- [Pallett et al., *Commun Med*, 2026-10-24](https://doi.org/10.1038/s43856-026-01866-2) — **Understanding diagnostic challenges and identifying priorities to tackle antimicrobial resistance in conflict zones.** Diagnostic priorities for AMR in armed-conflict settings; context for equity-focused AMR work.
- [Knight et al., *npj Antimicrob Resist*, 2026-10-23](https://doi.org/10.1038/s44259-026-00279-4) — **What are the roles of sex and gender in antimicrobial resistance? Evidence across infection, selection and transmission.** Synthesises evidence on how sex and gender shape AMR; useful framing for equity analyses.
- [Kimera et al., *Discover Public Health*, 2026-10-18](https://doi.org/10.1186/s12982-026-02998-5) — **A One Health scoping review of genomic and machine learning approaches for predicting AMR in LMICs.** Maps ML approaches to AMR prediction in low- and middle-income countries; context for data gaps in the Global South.
