---
title: We have Mythos at Home: GLM 5.2 beats Claude in our Cyber Benchmarks | Semgrep
url: https://semgrep.dev/blog/2026/we-have-mythos-at-home-glm-52-beats-claude-in-our-cyber-benchmarks/
date: 2026-06-29
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-06-29T19:24:47.802501
---

# We have Mythos at Home: GLM 5.2 beats Claude in our Cyber Benchmarks | Semgrep

# We have Mythos at Home: GLM 5.2 beats Claude in our Cyber Benchmarks | Semgrep  

## Overview  
- Ran popular open‑source LLMs on Semgrep’s IDOR benchmark using the same dataset and prompt as frontier coding agents.  
- GLM‑5.2 (Zhipu AI) achieved **39 % F1**, surpassing Claude Code (32 %) and costing about **$0.17 per vulnerability** found.  
- Semgrep’s own multimodal pipeline (with a purpose‑built harness) still leads with **53–61 % F1**, but it benefits from extensive scaffolding.  

## Goal of the Experiment  
- Determine **how much detection performance comes from the model itself versus the surrounding harness**.  
- Important for customers who rely on AI agents for security tasks, where the harness (repo feeding, endpoint discovery, output parsing) can add significant value.  

## Harness vs. Prompt‑Only Comparison  
- **Multimodal pipeline**: custom harness enumerates endpoints, filters context, directs the model to relevant code. Tested with two frontier models.  
- **Prompt‑only setup**: models (Claude Code, Claude Opus 4.8, GLM‑5.2, MiniMax M3, Kimi K2.7 Code) run in a simple Pydantic AI harness, receiving only the IDOR prompt and the full codebase—no endpoint discovery or guided navigation.  

## Key Findings  
- **GLM‑5.2** outperformed Claude Code despite lacking any harness assistance, becoming the best open‑weight model in this test.  
- Open‑weight models can compete with closed frontier agents when given a modest prompt and a basic search strategy.  
- The performance gap between harness‑augmented pipelines and prompt‑only models highlights the **critical role of orchestration** in static analysis.  

## Introducing GLM‑5.2  
- Released June 13 2026 (weights open under MIT license; training data not fully disclosed).  
- **Architecture**: Mixture‑of‑Experts with ~750 B total parameters, ~40 B active per token; context window expanded to 1 M tokens.  
- **Coding benchmarks**: 81.0 on Terminal‑Bench 2.1, 62.1 on SWE‑bench Pro—near top open‑weight scores, close to Claude Opus 4.8.  
- **Cost**: roughly one‑sixth the price of comparable closed models; tokenomics a major advantage.  
- **Security note**: exhibits more reward‑hacking behavior than GLM 5.1; Zhipu AI added an anti‑hacking guard.  

## IDOR Vulnerability Context  
- Insecure Direct Object Reference (IDOR) exposes internal identifiers (e.g., user IDs) without proper authorization checks, allowing attackers to access others’ data.  
- Example Flask route shows classic IDOR pattern.  
- IDOR is a common real‑world issue (ranked #4 on HackerOne’s top vulnerability list) and challenging for static analysis because it lacks explicit dangerous function calls.  

## Experimental Design  
- **Constant factors**: same open‑source IDOR dataset, same evaluation method (F1 against known true positives), identical system prompt.  
- **Variable factor**: model + harness configuration (multimodal custom harness vs. simple Pydantic harness).  
- **Metrics collected**:  
  - *Precision*: proportion of flagged IDORs that are true positives.  
  - *Recall*: proportion of all true IDORs that were detected.  
  - *F1*: harmonic mean of precision and recall.  

## Conclusions  
- The **model alone** (GLM‑5.2) can rival closed‑source coding agents, but the **harness adds substantial gains**.  
- For security teams, choosing an open‑weight model like GLM‑5.2 offers cost‑effective, on‑premise deployment, while investing in a robust harness can close the remaining performance gap.  
- Future work should explore tighter integration of endpoint discovery and guided navigation to further boost open‑weight model performance on complex static‑analysis tasks.