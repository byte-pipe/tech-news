---
title: Model Training as Code — Aleph Alpha
url: https://aleph-alpha.com/en/blog/model-training-as-code/
date: 2026-06-25
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-06-29T19:25:36.401108
---

# Model Training as Code — Aleph Alpha

# Model Training as Code — Aleph Alpha

## TL;DR
- Model training has become so complex that manual coordination across specialised teams no longer scales.  
- Aleph Alpha built **Savanna**, a “model factory” that encodes the entire training pipeline in code, making end‑to‑end runs hermetic and launchable with a single click.  
- The post explains Savanna, why it’s required, and the engineering culture that supports it.

## Introduction
- Rapid advances add new stages and increase intricacy of existing ones, creating three main challenges:  
  1. **Complexity → errors** – bugs or mis‑configurations can cause whole runs to fail.  
  2. **Cost of failure** – larger models, higher GPU prices, and massive data make mistakes expensive.  
  3. **Organisational** – many specialised teams must coordinate without breaking each other’s work or losing improvements.  
- Traditional manual processes do not address these challenges.

## Hidden Cost of Manual Model Training
- **Iterative, compute‑bound workflow**: pre‑training → post‑training (SFT → RL), each requiring multiple experiments and heavy GPU usage.  
- **First hidden cost – human error**: manual hand‑offs (e.g., sharing dataset paths via Slack) lead to crashes, idle GPUs, and ad‑hoc reconstruction of setups.  
- **Second hidden cost – lost learnings**: hyperparameter decisions, data‑mix provenance, and experiment results are scattered across Slack, filesystems, wikis, making them hard to reuse.  
- **Third hidden cost – fragmented ownership**: teams only optimise their slice of the pipeline; infrequent hand‑offs cause divergence and obscure root‑cause analysis.  
- Overall, the pipeline exists only in people’s heads, not in a durable, shared artifact.

## Introducing Model Training as Code (MTaC)
- **Savanna** implements the full training pipeline as imperative code, turning the process into a collaborative software project.  
- Example pseudocode shows asynchronous composition of SFT, evaluation, RL, and final evaluation steps.  
- **Key benefits**:  
  1. **Composability** – functions with typed inputs/outputs can be combined, reused, and tested; pipelines can be run with a single command.  
  2. **Consensus** – version‑controlled main branch holds the collective “best” training recipe; no missing flags or forgotten setup steps.  
  3. **Provenance** – code comments and commit history capture reasoning; past runs are reproducible by checking out the exact commit.

## Organizational Practices
- With the pipeline in code, standard software collaboration practices apply.  
- **Integrate little, integrate often**: adopt trunk‑based development, landing small, frequent changes on `main` so teams can build on each other’s work early and maintain a shared, up‑to‑date training definition.  

## Overall Impact
- MTaC enables any team to launch the full pipeline, run other teams’ stages, and iterate on the model holistically.  
- It shifts decomposition from temporal (each team owns a stage) to capability‑based (teams own behaviours like multilinguality end‑to‑end), fostering better collaboration, reproducibility, and scalability.