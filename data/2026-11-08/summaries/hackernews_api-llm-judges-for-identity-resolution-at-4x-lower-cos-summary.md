---
title: LLM Judges for Identity Resolution at 4x Lower Cost | Hightouch | Hightouch
url: https://hightouch.com/blog/llm-judges-identity-resolution
date: 2026-11-07
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-11-08T09:04:19.114862
---

# LLM Judges for Identity Resolution at 4x Lower Cost | Hightouch | Hightouch

# LLM Judges for Identity Resolution at 4× Lower Cost

## Overview
- The study evaluates whether fast, cheap decision models (Jev and GPT‑6 Luna) can grade identity‑resolution (IDR) results as accurately as frontier LLMs.
- Combining Jev with Claude Opus yields near‑Opus accuracy while reducing cost by more than four times.
- Decision models are up to 90× cheaper and >10× faster than frontier models, though they lag by ~6 percentage points on the hardest benchmarks.

## Main Findings
- **Performance**
  - Luna outperforms Jev out‑of‑the‑box, but the gap disappears on difficult cases.
  - Jev’s confidence scores are better calibrated; most of its errors have low confidence, enabling a more effective hybrid with Opus.
  **Hybrid Model:** Jev + Opus achieves frontier‑level accuracy (>99 %) at >4× lower cost.
- **Cost & Speed**
  - Decision models cost $0.05–$0.10 per 1,000 identities and respond in ~0.15 s.
  - Opus costs $3.86 per 1,000 identities and takes ~2.2 s.
- **Accuracy Trade‑off**
  - Frontier models remain the most accurate overall.
  - Decision models trail Opus by ~6 pp on harder benchmarks but are dramatically cheaper and faster.

## What Is Identity Resolution?
- **Goal:** Map a set of data records \(D\) to a set of real‑world identities \(I\) such that each record belongs to exactly one person and no identity merges multiple people.
- **Importance:** Enables reliable outreach, personalization, and analytics (e.g., calculating customer lifetime value).
- **Challenges:** Data errors (typos, nicknames, swapped dates, blank fields) and over‑merging—incorrectly grouping distinct people under one identity.

## Detecting Over‑Merging
- No ground‑truth key exists on real data; teams must manually sample identities.
- Human sampling is slow (~50 identities/hour) and requires >1,000 samples for ±1 % error on rare over‑merge rates.
- An LLM that matches human judgment could evaluate hundreds of thousands of identities in seconds, accelerating iteration and maintenance.

## Benchmark Methodology
- **Data Generation:** Used the “pseudopeople” simulator to create a fictional US town with realistic record errors.
- **Dataset:** 1,000 identities (500 true single‑person clusters, 500 over‑merged clusters).
- **Prompt:** Instructed models to decide if a profile represents one person, output a confidence‑based count, and justify only when over‑merged.
- **Threshold Tuning:** Started with a 50 % confidence cutoff; later explored adjustments to balance false positives vs. false negatives.

## Results (50 % Confidence Cutoff)

| Model | Accuracy | False Positives | False Negatives | Time / identity | Cost / 1,000 |
|-------|----------|-----------------|----------------|-----------------|--------------|
| Claude Opus 5.5 | 99.0 % | 3 | 7 | 2.2 s | $3.86 |
| Gemini 3.1 Pro | 98.3 % | 10 | 7 | 4.2 s | $4.48 |
| GPT‑6 Sol | 98.3 % | 14 | 3 | 2.1 s | $2.50 |
| GPT‑6 Luna (Decisions API) | 97.3 % | 17 | 10 | 0.17 s | $0.10 |
| Jev (Decisions API) | 95.6 % | 31 | 13 | 0.15 s | $0.05 |

## Key Takeaways
- **Hybrid Advantage:** Jev + Opus combines Jev’s calibrated confidence with Opus’s high accuracy, achieving frontier performance at a fraction of the cost.
- **Decision Model Strengths:** Extremely low latency and cost make them attractive for large‑scale, real‑time IDR grading, especially when paired with a stronger LLM for error correction.
- **Threshold Sensitivity:** Adjusting confidence cutoffs can significantly shift the balance between false positives and false negatives, allowing teams to tailor models to specific risk tolerances.