# Ersilia Literature Digest — Week of 2026-11-10

**Connectors:** Alerts and Newsletters 🟢 · Slack 🟢 · Europe PMC 🟢 · bioRxiv 🟢 · Web hunt 🟢  
**Markers:** ⭐ High impact · 🌍 LMIC · 🤖 Candidate model · 🗃️ Interesting dataset · 💻 Code available  
**Tasks:** 🧪 Property · 🎯 Activity · 🧩 Featurization · 🗺️ Projection · 🔍 Similarity · 🎨 Generative

## 🤖 Models that could join the Hub

### 🎨 Generative

- [Li et al., *arXiv*, 2026-11-06](https://arxiv.org/abs/2611.09142) 🤖💻 — **Learning Generative Dynamics for 3D Molecule Generation via Sequential Neuro-Symbolic Constraints (SensDiff).** Open-source generative model producing 3D molecules (atom types, coordinates, SMILES) from a diffusion process constrained by symbolic chemistry rules; code is released under MIT. Plausible Hub addition because it targets chemical validity of generated molecules, a common weakness of diffusion generators (weights: pending; infra: unverified). · [code](https://github.com/WanyuGroup/NeurIPS2026_SensDiff) · 🎨

## 🗃️ Datasets that could join the Hub

### Bioactivity datasets

- [Lu et al., *Nucleic Acids Res*, 2026-11-06](https://doi.org/10.1093/nar/gkag1141) 🗃️ — **BioLiP3: a protein–ligand affinity database integrating curated data with LLM-enabled literature mining.** 593,423 records · Ki / Kd / IC50 / EC50 · article CC BY 4.0, database licence to be confirmed · zhanggroup.org/BioLiP. Plausible Hub input because 528,732 BindingDB-derived records and 45,386 PDB complexes give a large, structure-linked affinity set for compound–protein models. · 🎯

## AI/ML methods for drug discovery

- [Blake et al., *arXiv*, 2026-11-05](https://arxiv.org/abs/2611.08420) — **On the limitations of molecular representations.** Systematic test of fingerprints and learned embeddings: no state-of-the-art embedding captures graph structure better than fingerprints or physicochemical descriptors, and many Enamine REAL molecules receive non-unique representations. Directly relevant to the choice of featurisers in the Ersilia Model Hub.
- [Petersen et al., *arXiv*, 2026-10-06](https://arxiv.org/abs/2610.08400) 💻 — **Atom-JEPA: Joint-Embedding Predictive Architecture for 3D Atomistic Systems.** Self-supervised pretraining on unlabelled 3D structures with reported gains on ADMET and quantum-chemical property tasks; code and checkpoints released under MIT. (Input: 3D structures — Hub-eligible only with a conformer-generation step.) · [code](https://github.com/khelverskovp/atom-jepa)
- [Shi et al., *bioRxiv*, 2026-11-03](https://doi.org/10.64898/2026.10.28.762420) — **Ark-ADMET: endpoint-specific selection of molecular representations and hyperparameters for gradient-boosted ADMET models.** CatBoost models with a per-endpoint choice of representation for 22 TDC ADMET endpoints, matching or beating the best leaderboard score on 7 of 21 rankable endpoints. Would suit the Hub's ADMET coverage, but no code link was found (code: not linked).
- [Qiao et al., *Digital Discovery*, 2026-10-21](https://doi.org/10.1039/d6dd00444j) — **MetaPLI: retrieval-augmented in-context regression for protein–ligand binding affinity.** Updates affinity predictions from a few new assay measurements without retraining. (Input: protein–ligand 3D complexes; licence: CC BY-NC.)
- [Li et al., *arXiv*, 2026-11-06](https://arxiv.org/abs/2611.09235) — **Controllable Molecule Generation via Sparse Representation Editing (SpaRE).** Property-controllable molecule generation with public code. (Licence: not asserted on the repository, so redistribution is unclear.) · [code](https://github.com/WanyuGroup/ICML2026_SpaRE)
- [Ostarkov et al., *arXiv*, 2026-10-30](https://arxiv.org/abs/2610.41899) — **General-purpose foundation models surpass specialized ones on chemical property prediction tasks.** With about 60 examples, a general LLM beat ChemBERTa and MoLFormer on five regression tasks. A useful baseline when judging chemistry foundation models for the Hub (no code or weights).
- [Busch et al., *arXiv*, 2026-10-30](https://arxiv.org/abs/2610.41745) — **Do LLMs Know When They Are Wrong About Molecules?** Seven frontier LLMs predict molecular properties in context; self-reported uncertainty ranks errors only weakly (Spearman up to 0.46), and ESOL appears memorised. Cautions against LLM property predictors without calibration.
- [Kim et al., *arXiv*, 2026-11-05](https://arxiv.org/abs/2611.07488) — **OPRD-Imp: experimentally observed impurities and side products in multi-step pharmaceutical syntheses.** 229 reactions and 784 impurity entries as SMILES with mechanistic-origin labels, on Figshare under CC BY 4.0. Too small for the Hub, but a useful reaction-outcome benchmark.

## Antibiotic and antimicrobial discovery

- [Kresse et al., *Nature*, 2026-11-04](https://doi.org/10.1038/s41586-026-11212-0) ⭐ — **Comprehensive mapping of essential-gene interactions in *M. tuberculosis*.** Dual-sgRNA CRISPRi maps thousands of genetic interactions among essential genes and links them to drug targets and combination-therapy opportunities. Informs target selection for Ersilia's *Mtb* work.
- [Huber et al., *ACS Infect Dis*, 2026-10-30](https://doi.org/10.1021/acsinfecdis.6c00657) — **A Machine Learning-Enhanced Ligand-Based Workflow Identifies Novel *Cryptosporidium parvum* Inhibitors.** Thompson sampling, a pharmacophore model and an ML classifier screened about 51 million virtual compounds; 69 were tested and 20 were new micromolar hits. A neglected-pathogen example of ML-guided screening (no code or data link found).
- [Fei et al., *J Med Chem*, 2026-09-01](https://doi.org/10.1021/acs.jmedchem.6c00893) — **Structural and Mechanistic Studies of ADEPs Yield Potent Antibacterials and a Drug Formulation Strategy for Tuberculosis.** The lead ClpP activator ADEP 19 is up to 12-fold more potent than ADEP 4 against *Mtb* and synergises with bedaquiline in zebrafish. Relevant to protease-targeting strategies in tuberculosis.

## AI agents and foundation models for science

- [Zhang et al., *arXiv*, 2026-10-29](https://arxiv.org/abs/2610.39714) — **MoLRSI: A Recursive Self-Improving AI agent for Molecular Discovery.** An agent that rewrites its own discovery workflows and models; in antibiotic discovery it reached a 15.9% experimental hit rate against 8.7% for an expert workflow. Worth dissecting for an open reimplementation (no code linked).
