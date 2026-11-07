---
title: My Local AI Invented 162 Python Packages. I Reran Everything From Scratch, and 161 Came Back. - DEV Community
url: https://dev.to/soumyadeepdey/my-local-ai-invented-162-python-packages-i-reran-everything-from-scratch-and-161-came-back-4j73
date: 2026-11-01
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-11-08T09:03:42.087816
---

# My Local AI Invented 162 Python Packages. I Reran Everything From Scratch, and 161 Came Back. - DEV Community

# Summary of “My Local AI Invented 162 Python Packages. I Reran Everything From Scratch, and 161 Came Back.”

## TL;DR
- **Phantom Packages** is a study, a detector, and a guard that prevents AI‑generated pip install commands from referring to non‑existent packages.  
- Three small local models (gemma‑4, qwen‑3, phi‑4‑mini) produced 1,199 short Python scripts; 212 of the 1,410 suggested installs (15 %) were “ghost” packages that never existed on PyPI.  
- A TabPFN‑3.5 model trained to recognise ghost names achieved AUROC 0.975 offline and blocked all 212 ghosts when wired into a Claude Code hook, while mistakenly rejecting only 13 of 1,165 real packages.  
- The guard intercepts an install in about 1.7 seconds (ghosts blocked in 2.2 seconds) and works even with Wi‑Fi disabled.

## Key Findings (30 seconds)
1. **Ghosts are reproducible** – after deleting all generations and rerunning, 98.7 % of outputs matched word‑for‑word and 161 of 162 ghost names reappeared.  
2. **Ghost names mirror the prompt** – 56.5 % are the task’s own words concatenated; 27 of the 40 repeatedly appearing ghosts are exact repeats of the same prompt.  
3. **“Does this package exist?” is a poor model query** – gemma‑4 incorrectly claimed 143 of 271 real packages did not exist; a hosted model mis‑identified 60 of 161 ghosts as real.

## Methodology
- **Tasks**: 200 prompts across 15 domains, split into everyday (50), specialised (70), and obscure (80) categories. Each prompt asked for a short Python script beginning with an exact `pip install` line.  
- **Models**: gemma‑4:e4b, qwen‑3:4b‑instruct, phi‑4‑mini:3.8b run via Ollama with fixed seeds (1001, 1002) and temperature 0.7.  
- **Generation time**: 1,199 of 1,200 calls completed in 3.9 hours on a laptop with RTX 3050 (4 GB VRAM).  
- **Ghost detection**: TabPFN‑3.5 trained on package‑name features (no registry lookup) and evaluated offline; a Claude Code hook applied the model in‑line during script generation.  
- **Reproducibility test**: All generations deleted and rerun; 1,183 of 1,199 outputs identical, 161 of 162 ghosts returned.

## Results
- **Ghost rates by model**  
  - gemma‑4: 8.1 % (39/483)  
  - phi‑4‑mini: 16.7 % (78/467)  
  - qwen‑3: 20.7 % (95/460)  
  - Overall: 15.0 % (212/1,410) with 95 % CI 11.9–18.4.  
- **Task difficulty effect**  
  - Everyday: 1.7 % ghost rate  
  - Specialised: 8.8 % ghost rate  
  - Obscure: 30.0 % ghost rate (≈18× higher than everyday).  
- **Ghost name composition**  
  - 56.5 % are prompt words glued together.  
  - 27.9 % appear wholly invented.  
  - 8.7 % combine a real package name with an affix.  
  - 5.6 % are one‑ or two‑character edits of real names.  
- **Detection performance**  
  - TabPFN AUROC 0.975 on unseen prompts, 0.978 on a model it never trained on, 0.948 on completely novel names.  
  - Calibration error 0.015 (best among tested methods; gradient boosting error 0.056).  
  - Gradient boosting beats TabPFN on precision at 90 % recall; a paid hosted model ties TabPFN on unseen names.  

## Guard Implementation
- **Workflow**: Agent generates script → Claude Code hook queries TabPFN → if P(ghost)=1.00, block install and suggest closest real package.  
- **Latency**: Ghost blocked in 2.2 s; legitimate install passes in 1.7 s.  
- **Offline capability**: With Wi‑Fi off, still catches 90.1 % of ghosts.  

## Security Implications
- A ghost package can be turned into a malicious payload by registering the name on PyPI (slopsquatting).  
- Real‑world example: a recurring ghost was registered as an empty package and received >30 k authentic downloads in three months.  
- Agents that automatically run `pip install` without verification can unintentionally install attacker‑controlled code.  

## Open‑Source Release
- All code, evaluation scripts, figures, and an anonymised “name‑free” dataset are available at `T‑RexBytes/phantom-packages`.  
- A single command reproduces every number and figure presented in the article.  

## Take‑away
- Small local LLMs frequently hallucinate non‑existent package names, especially on obscure tasks.  
- Ghost names are predictable from the prompt, making them exploitable.  
- An offline, model‑based guard can reliably filter out these hallucinations with minimal latency, providing a practical defence for AI‑assisted coding pipelines.