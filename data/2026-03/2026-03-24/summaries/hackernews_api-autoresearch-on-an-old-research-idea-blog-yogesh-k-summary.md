---
title: Autoresearch on an old research idea | Blog | Yogesh Kumar
url: https://ykumar.me/blog/eclip-autoresearch/
date: 2026-03-24
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-03-24T20:03:28.292418
---

# Autoresearch on an old research idea | Blog | Yogesh Kumar

# Autoresearch on an old research idea

## Core Idea
- Autoresearch is a constrained optimization loop with an LLM (Claude Code) at its core.  
- The agent repeatedly: hypothesize → edit `train.py` → train → evaluate → commit or revert.  
- Instructions are read from `program.md`; a `scratchpad.md` serves as working memory.  
- Exploration is divided into phases: hyper‑parameter tuning, small architectural tweaks, and “moonshot” ideas.  
- Each experiment is limited to ~5 minutes wall‑clock time to encourage rapid iteration and avoid over‑fitting.  

## Sandboxing
- The training loop runs inside a container with no network access.  
- `run.sh` orchestrates the process; Claude Code can only edit `program.md`, `train.py`, and invoke `run.sh`.  
- Direct Python execution, pip installs, git pushes, and other privileged actions are blocked.  

## Dataset
- Original medical X‑ray data were unavailable, so the Ukiyo‑eVG dataset (~11 K Japanese woodblock prints) was used.  
- Each image has phrase‑to‑bounding‑box annotations; boxes are converted to Gaussian heatmaps and fed to the model as an extra input, mimicking radiologist eye‑gaze heatmaps.  

## Hello — Claude Code
- Claude upgraded the old codebase, added data ingestion for Ukiyo‑eVG, and scaffolded the experiment loop.  
- CV splits, evaluation logic, and initial `program.md` ideas were set up.  
- Evaluation metric: **Mean Rank** of retrieved embeddings (chosen for simplicity; Median Rank would have been more robust).  
- Model details: ViT‑Small (22 M) + DistilBERT (66 M) + HeatmapProcessor ≈ 90 M parameters.  
- Training: 800 steps (~3 min per run on RTX 4090).  
- Baseline validation Mean Rank = 344.68; Recall@1 ≈ 17 % (image→text) and 16 % (text→image).  

## Results
- Over one day: 42 experiments (13 committed, 29 reverted).  
- Validation Mean Rank improved from 344.68 to 157.43 (≈ 54 % reduction).  
- Final full‑dataset run yielded better test scores than validation, indicating under‑fitting in short runs.  

| Metric | Test |
|--------|------|
| Mean Rank | 34.30 |
| img→txt R@5 | 53.0 % |
| txt→img R@5 | 51.4 % |

## Key Findings (AGI?)
- **Temperature clamp fix**: Removing a hard cap on the learnable temperature parameter dropped Mean Rank by 113 points – the single biggest gain.  
- **Optuna++ style tuning**: Adjusting projection dimension and learning rate contributed another ~30‑point improvement; the agent behaved like an automated hyper‑parameter optimizer.  
- **Diminishing returns**: In later phases, architectural and moonshot ideas rarely succeeded; many changes were reverted.  
- **Sandbox importance**: Occasionally the agent attempted unauthorized bash commands, halted, or stopped looping when training took too long, confirming the need for strict permission controls.  

## Closing Thoughts
- The first 90 % of the workflow proceeded smoothly with minimal human input; the final 10 % required manual nudging.  
- When the search space is well‑defined, the commit‑or‑revert loop is an effective strategy for LLM‑driven ML research.  
- The “one change per experiment” constraint may be too restrictive for ambitious ideas; adding a planning stage or sub‑agents could improve outcomes.  

## Acknowledgements
- Ukiyo‑eVG dataset: ~11 K Japanese woodblock prints with phrase‑to‑bounding‑box annotations (CIGA paper, ECCV 2024 VISART).  
- Autoresearch concept by Andrej Karpathy.