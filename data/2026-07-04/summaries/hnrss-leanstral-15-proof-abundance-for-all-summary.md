---
title: Leanstral 1.5: Proof Abundance for All
url: https://mistral.ai/news/leanstral-1-5/
date: 2026-07-03
site: hnrss
model: llama3.2:1b
summarized_at: 2026-07-04T11:38:09.514263
---

# Leanstral 1.5: Proof Abundance for All

**Leanstral 1.5: Proof Abundance for All**

**Summary**
----------------

Leanstral 1.5 is a free, Apache-2.0 licensed model that significantly improves performance in formal verification and proof engineering. With 6B active parameters, it has achieved state-of-the-art results on several benchmarks, including FATE-H (87%) and FATE-X (34%). Leveraging mid-training, supervised fine-tuning, and reinforcement learning with CISPO, Leanstral 1.5 delivers a major performance upgrade in agentic proof engineering.

**Training Instructions**
-------------------------

Leanstral follows a three-stage process:

*   **Mid-training**: A multiturn environment where the model is given a theorem statement to prove or disprove. Its performance is refined using feedback from the Lean compiler.
*   **Code agent environment**: The model operates like a developer in a raw filesystem, editing files and running bash commands to complete proof-engineering tasks.
*   Further refinement and testing with reinforcement learning with CISPO

**Evaluation Benchmarks**
---------------------------

Leanstral has been evaluated on miniF2F, solving 587/672 PutnamBench problems and achieving an state-of-the-art result of 87% on FATE-H. Its findings also included uncovering 5 previously unknown bugs in open-source repositories.

## Key Points
---------------

•   Leanstral 1.5 delivers a major performance upgrade in formal verification, saturating miniF2F benchmarks.
•   It combines mid-training with supervised fine-tuning and reinforcement learning with CISPO.
•   Training leverages extensive training on RL environments to refine itself.
•   Leanstral is fully open-sourced and available via Hugging Face for practical proof engineering.