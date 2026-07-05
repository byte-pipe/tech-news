---
title: AI: Are AI employees more expensive than humans?
url: https://lex.substack.com/p/ai-tokens-are-cheaper-but-ai-bills
date: 2026-07-06
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-07-06T07:32:50.830391
---

# AI: Are AI employees more expensive than humans?

# AI: Are AI employees more expensive than humans?

## Overview
- The newsletter outlines the paradox that while per‑token prices are dropping, overall AI bills for enterprises are soaring.
- Finance teams must reconcile cheaper tokens with higher total spend driven by massive consumption.

## Token Price Decline vs. Consumption Rise
- Nvidia’s Vera Rubin data‑center platform claims a 10× reduction in token generation cost by tripling memory bandwidth.
- Unit price has fallen dramatically:
  - From $60 per million tokens in 2021 to $0.60 in 2024 (a ten‑fold annual decline) – Andreessen Horowitz.
  - Benchmark data shows performance‑per‑dollar improving 9× to 900× per year – Epoch AI.
- Consumption is climbing faster than price drops:
  - Goldman Sachs projects token usage to reach 120 quadrillion tokens per month by 2030 (≈24× growth).
  - An agent‑based software‑development tool consumes ~6 M input and 0.82 M output tokens daily.

## What Drives the Cost?
- **Memory bandwidth** is the bottleneck; inference spends 60‑40 % of time waiting for data, not computing.
- Vera Rubin’s savings stem from HBM4 delivering 22 TB/s per chip, while memory cost in servers has risen >400 % over the previous generation.
- **Energy consumption** adds significantly:
  - A single frontier query uses ~0.33 Wh; scaling to 15× tokens raises energy ≈13×.
  - Agent loops can consume 60×‑140× the energy of a one‑shot request.

## Financial Comparison: AI vs. Human Labor
- Some executives (e.g., Glean’s Arvind Jain) see AI compute costs equaling employee costs for the first time.
- Nvidia’s Bryan Catanzaro notes compute costs already exceed employee expenses in his deep‑learning group.
- Gartner predicts token spend will match a software engineer’s salary by 2028, based on a global average wage of $2 k/month; in high‑cost cities the parity is farther off, while in places like Bangalore parity may already exist.
- The “advisor model” (cheap open‑weight models routing to frontier models only when needed) can cut bills by an order of magnitude.
- Chinese open‑weight models (DeepSeek, Zhipu) achieve near‑frontier performance at ≤20 % of the cost.

## Key Takeaways for Stakeholders
- **Investors:** Monitor inference margins; AI‑native SaaS companies allocate 40‑50 % of revenue to inference cost versus 10‑20 % for traditional SaaS.
- **Founders:** Measure cost per completed task, keep model layers interchangeable, and treat context engineering as a cost centre requiring human oversight.
- **Operators:** Price AI agents against human equivalents, especially where compliance overhead is high; assume frontier‑reasoning unit costs may plateau.

## Implications
- As token pricing becomes dominated by memory bandwidth and electricity rather than model sophistication, competitive advantage shifts to those controlling power and routing infrastructure.
- The industry’s previous focus on dependence on a few model providers may give way to price competition as the decisive factor.