---
title: @adlrocha - Base Models Stopped Being the Bottleneck
url: https://adlrocha.substack.com/p/adlrocha-base-models-stopped-being
date: 2026-09-01
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-09-01T09:52:13.392004
---

# @adlrocha - Base Models Stopped Being the Bottleneck

# @adlrocha – Base Models Stopped Being the Bottleneck

## Overview
- The post explains why GLM‑5.3 and Qwen‑3.8‑27B show noticeable performance gains despite having the same architecture as their predecessors.
- The improvements stem from an extended **post‑training** phase rather than architectural changes, larger pre‑training corpora, or distillation alone.

## What GLM‑5.3 Is
- Released on August 14, built on the exact same base as GLM‑5.2 (identical size and parameters).
- Received **one extra month of post‑training**; no changes to pre‑training or mid‑training.
- After this additional training the model climbed to the top of CyberGym and GDP‑val rankings, even surpassing larger open models such as Kimi K3 on several benchmarks.
- User experience: feels faster, smarter, and more concise, reducing token usage per task.

## Training Stages of an LLM
1. **Pre‑training**  
   - Learns next‑token prediction from massive internet‑scale data.  
   - Provides “latent capabilities” (e.g., programming knowledge, language fluency).  
   - Most expensive stage; unchanged for GLM‑5.3.

2. **Mid‑training** (often overlooked)  
   - Fine‑tunes the pre‑trained model on curated, domain‑specific data, longer contexts, etc.  
   - Also unchanged for GLM‑5.3.

3. **Post‑training** (the focus of the improvement)  
   - **Supervised fine‑tuning**: model imitates demonstrated good behavior (instruction following, response format, refusal).  
   - **Preference optimization** (RLHF/DPO): humans rank outputs, a reward model is trained, and the policy is optimized against it.  
   - **Reinforcement learning with verifiable rewards (RLVR)**: model interacts with an environment, receives concrete success/failure signals, and learns from execution outcomes.

## Why Post‑training Made the Difference
- Z.ai upgraded the **training environments** used in the RLVR stage.  
- Earlier environments resembled isolated coding puzzles; the new ones simulate **real expert‑work units** that can take days for a human engineer (e.g., diagnosing ML‑infrastructure bottlenecks, running experiments, delivering speed‑up without breaking correctness).  
- As agent capability rises, the bottleneck shifts from the model itself to the **quality and realism of the environment**.

## Scaling the Environment
- Manually crafting thousands of multi‑day expert tasks is infeasible.  
- Z.ai built an **environment factory**:
  - Research agents extract task patterns from real work and generate runnable, long‑horizon environments with hidden state and multi‑step dependencies.  
  - A judge agent validates that a solver actually completes the task; unsolvable “exams” are never set.  
  - Solver agents probe for shortcuts; identified shortcuts are closed, ensuring genuine skill acquisition.  
  - The curriculum self‑writes and self‑grades, with human oversight on edge cases.

## Analogy to Coding Workflows
- The author’s “Spec‑Test‑Lint” flow mirrors this approach: detailed specifications and tight test suites create autonomous coding agents.  
- Z.ai applied the same principle at scale for LLM training, turning the post‑training phase into a self‑sustaining curriculum that drives measurable capability gains.

## Takeaway
- **Base model architecture is no longer the primary limitation**; the richness of post‑training environments now dictates performance improvements.  
- Extending and automating realistic, multi‑step tasks enables LLMs like GLM‑5.3 and Qwen‑3.8‑27B to achieve frontier‑level results without additional parameters or architectural tweaks.