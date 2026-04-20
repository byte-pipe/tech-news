---
title: Closed Source vs Open Source AI: A Cage Fight Few People Understand
url: https://davefriedman.substack.com/p/closed-source-vs-open-source-ai-a
date: 2026-03-30
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-03-30T01:02:43.782198
---

# Closed Source vs Open Source AI: A Cage Fight Few People Understand

# Closed Source vs Open Source AI: A Cage Fight Few People Understand

## Overview
- The article argues that the **monetizable spread**—the portion of the capability gap that customers actually pay a premium for—is shrinking faster than the raw **capability spread** between closed‑source and open‑source models.
- This compression is not reflected in current market valuations of frontier AI companies.

## Compression of Capability Gap
- End‑2023: best closed model ~88 % on MMLU vs best open model ~70.5 %.
- Early‑2026: gap on knowledge benchmarks is essentially zero; reasoning tasks differ by only single digits.
- Open models now lag state‑of‑the‑art by roughly **three months** on average, down from about a year in late‑2024.
- Training efficiency has improved dramatically (e.g., DeepSeek V3 used 2.6 M GPU‑h vs 30.8 M GPU‑h for Llama 3 405B).
- Frontier models still lead on the hardest tasks (complex agentic coding, multi‑step tool chaining, long‑horizon workflows), but the set of tasks where they have a clear edge is shrinking each quarter.

## The Monetizable Spread
- Defined as the gap between the “good enough” threshold (where open models become interchangeable with closed ones) and the top of the capability stack, weighted by revenue density at each layer.
- As open models improve, the “good enough” line moves upward, eroding the slice of paying customers that justify a premium for closed models.
- Revenue is heavily concentrated in the middle band (summarization, basic Q&A, translation, routine code assistance), which has already become “good enough” for open models.
- Supporting data (proxied, not exact):
  - Anthropic’s Economic Index: 36 % of API usage is for computer/mathematical tasks; the rest is writing, research, education—areas where frontier capability adds little value.
  - Menlo Ventures survey: spending driven by code completion and productivity tools, not agentic systems.
  - Deloitte 2026 report: 37 % of organizations use AI at a “surface level,” 30 % redesign key processes, only 34 % undertake deep transformation requiring frontier models.
- Even if the raw capability spread stays steady, the monetizable spread contracts because the high‑revenue “fat” layer is being captured by open models.

## Valuation Implications
- **OpenAI** seeks $100 B funding at an $850 B valuation; projected $14 B loss in 2026, $115 B cumulative loss through 2029, with profitability possibly only in the 2030s.
  - Revenue run‑rate ≈ $25 B, gross margin ~33 % (limited by inference costs).
  - Pays Microsoft 20 % of revenue through 2032, a structural drag often ignored.
  - Valuation reflects a **distribution bet** (massive consumer user base), not a pure technology moat.
- **Anthropic** closed a $30 B Series G at a $380 B valuation; $14 B run‑rate revenue, $2.5 B from Claude Code.
  - Implies ~27× price‑to‑sales.
  - Revenue is ~80 % enterprise, making it highly exposed to monetizable‑spread compression as enterprises evaluate premium versus “good enough.”

## Where Value Is Likely to Migrate
- **Infrastructure layer**: financing, operating, and trading compute resources (GPU‑backed lending, compute derivatives, data‑center financing).
- **Model‑layer margin compression** will shift investor focus from proprietary model providers to those controlling the underlying compute and data pipelines, where margins are structurally different.

## Takeaway
- The market is pricing AI companies on the assumption that a durable premium for closed‑source, frontier models will persist.
- As open‑source models become “good enough” for the bulk of revenue‑generating tasks, that premium erodes, suggesting current valuations may be significantly overstated.
