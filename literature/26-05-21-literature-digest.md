# Ersilia Literature Digest — Week of 2026-05-21

**Connectors:** Alerts and Newsletters 🟢 · Slack 🟢 · Europe PMC 🟢 · bioRxiv 🟢

**Markers:** ⭐ very-high-impact venue · 🌍 LMIC-led · 🤖 candidate model for the Ersilia Model Hub · 🗃️ dataset useful for Ersilia modelling · 💻 open code linked from the paper

## AI agents and foundation models for science

- [Ghareeb et al., *Nature*, 2026-05-19](https://www.nature.com/articles/s41586-026-10652-y) ⭐ — **A multi-agent system for automating scientific discovery.** FutureHouse end-to-end agentic system that proposes hypotheses, runs experiments, and reports results across chemistry and biology — sets the bar for an Ersilia-style agent layer on top of the Ersilia Model Hub.
- [Gottweis et al., *Nature*, 2026-05-19](https://www.nature.com/articles/s41586-026-10644-y) ⭐ — **Accelerating scientific discovery with Co-Scientist.** Google DeepMind multi-agent research assistant validated on drug-repurposing and AMR case studies that overlap *E-AMR-CC* directly; the workflow is worth dissecting for an open-source reimplementation on top of the Hub.
- [Aygün et al., *Nature*, 2026-05-19](https://www.nature.com/articles/s41586-026-10658-6) ⭐ — **An AI system to help scientists write expert-level empirical software.** DeepMind agent that writes, runs, and debugs scientific code end-to-end — directly relevant to the autonomous-lab-unit direction in Ersilia's current grant portfolio.

## AI/ML methods for drug discovery

- [Škrinjar et al., *Nat Struct Mol Biol*, 2026-05](https://doi.org/10.1038/s41594-026-01797-5) — **Evaluating generalization in protein–ligand cofolding methods.** Benchmarks AlphaFold-Multimer, RoseTTAFold-AllAtom, Boltz, and Chai-1 on out-of-distribution complexes and shows where headline accuracy hides — load-bearing before scaling Boltz-2 to billions in *E-AMR-CC*.

## Antibiotic and antimicrobial discovery

- [Barman et al., *ACS Infect Dis*, 2026-05-19](https://doi.org/10.1021/acsinfecdis.5c01093) 🌍 — **A divergent MBL-fold metallo-hydrolase (Kmh-1) from Klebsiella pneumoniae.** IIT-affiliated structural/enzymatic characterisation of a new β-lactamase fold — Kmh-1 should be added to the *E-AMR-CC* Klebsiella target panel.
- [Brahma et al., *bioRxiv*, 2026-05-20](https://www.biorxiv.org/content/10.64898/2026.05.18.725845v1) 🌍 — **Therapeutic relevance of NLPA lipoprotein to combat biofilm-associated infection in Acinetobacter.** NIPER-led identification of NLPA as a biofilm target with small-molecule leads — broadens the *E-AMR-CC* and H3D AMR target panel into persister and biofilm biology.
- [Matsumoto et al., *bioRxiv*, 2026-05-15](https://www.biorxiv.org/content/10.64898/2026.05.15.725309v1) — **Structures of the Pseudomonas aeruginosa MlaC–MlaD complexes.** Yamagata University cryo-EM data illuminating the phospholipid retrograde-transport machinery of Gram-negative outer membranes — substrate for a future deep-docking campaign.

## Global health and open science

- [Parveen et al., *bioRxiv*, 2026-05-19](https://www.biorxiv.org/content/10.64898/2026.05.17.725751v1) 🌍 — **Computational drug repurposing identifies Artemisinin and Mebendazole as potential inhibitors.** University of Allahabad network-pharmacology screen — a useful external check against the antimalarial pyrazole / partner-drug ideas in the current grant portfolio.
- [Oni et al., *bioRxiv*, 2026-05-19](https://www.biorxiv.org/content/10.64898/2026.05.16.725619v1) 🌍 — **Computational design of novel selective PDE4B inhibitors from natural products.** University of Ilorin (Nigeria) natural-product virtual screen — exactly the kind of African-led NP pipeline that should be visible inside the Ersilia Model Hub.

## Potential models for the Ersilia Model Hub

### Property prediction or calculation

- [Zhou et al., *Nucleic Acids Res*, 2026-05-19](https://doi.org/10.1093/nar/gkag478) 🤖💻 — **DeepCYP: an integrated deep learning web server for "pathway–site–product" prediction of CYP-mediated metabolism.** Cao group (Central South University); CYP prediction is a known Hub gap and DeepCYP fits the NAR-web-server incorporation pattern the Hub already uses for ADMET-style endpoints.
- [Rath et al., *J Cheminform*, 2026-05-15](https://doi.org/10.1186/s13321-026-01207-4) 🤖💻 — **Deep learning for assay nuisance compound detection using a gated co-attention graph embedding.** Combines representations into a PAINS-style filter — drop-in candidate for the Hub's pre-screening layer in antimalarial and AMR cascades.

### Activity prediction

- [McFee et al., *bioRxiv*, 2026-05-20](https://www.biorxiv.org/content/10.64898/2026.05.04.722713v2) 🤖 — **SLiMNet: a deep learning model to detect short linear motifs using protein language models.** SLiMs are the recognition codes used by E3 ligases — directly load-bearing for the E3-target prioritisation step in *glueAI*.
- [Jimenez-Castro et al., *bioRxiv*, 2026-05-15](https://www.biorxiv.org/content/10.64898/2026.02.27.708593v2) 🤖 — **Explainable AI for end-to-end pathogen target discovery and molecular design.** An interpretable -omics-to-target ML pipeline — maps cleanly to the *E-AMR-CC* WP1B target-prioritisation workplan and adds an explainability layer the current Ersilia pipeline lacks.

### Featurization

- [Wadell et al., *arXiv*, 2025-10-20](https://arxiv.org/abs/2510.18900) 🤖💻 — **Foundation models for discovery and exploration in chemical space (MIST).** CMU-led open molecular foundation model benchmarked on 400+ property-prediction tasks — credible drop-in featurizer or baseline for the Ersilia Model Hub.

### Similarity search

- [Shin et al., *J Cheminform*, 2026-05-14](https://doi.org/10.1186/s13321-026-01224-3) 🤖💻 — **PL-PatchSurfer3: improved structure-based virtual screening using patch-based features.** A free, scalable docking-surrogate worth benchmarking against the Gentile-style deep-docking pipeline planned for *E-AMR-CC*.

### Generative

- [Park et al., *J Cheminform*, 2026-05-19](https://doi.org/10.1186/s13321-026-01221-6) 🤖💻 — **Novel molecular design via a scaffold-aware transformer with multi-scale attention.** Scaffold-conditioned generation directly matches the hit-to-lead need around MMV1794 in the antimalarial pyrazole program.

## Interesting datasets for Ersilia modelling

- [Molaei et al., *Sci Rep*, 2026-05-18](https://doi.org/10.1038/s41598-026-53762-3) 🌍🗃️ — **Synthesis and anti-leishmanial profile of novel thiazolidine-4-one derivatives.** Ardabil University of Medical Sciences (Iran); small but Hub-loadable IC50 dataset against *Leishmania* promastigotes and amastigotes — candidate seed for a *Leishmania* activity model trained beyond the published series.
