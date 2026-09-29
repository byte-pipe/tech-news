---
title: Introducing GPT-6.1 Sol | OpenAI
url: https://openai.com/index/introducing-gpt-6-1-sol/
date: 2026-09-30
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-09-30T06:01:18.566296
---

# Introducing GPT-6.1 Sol | OpenAI

# Introducing GPT‑6.1 Sol – Summary

## Key Highlights
- GPT‑6.1 Sol is an upgrade to GPT‑6 Sol, offering near‑Astra intelligence at roughly one‑fifth the price.
- Cached input costs $0.10 per million tokens (95 % cheaper than standard input pricing, 50 % cheaper than GPT‑6 Sol cached input).
- Designed for developers building agents that reuse context across requests.

## Performance Across Tasks
- **Coding:** Matches GPT‑6 Astra on DeepSWE v1.1 while beating GPT‑6 Sol by 6.4 percentage points at lower cost and reasoning effort.  
- **Professional Work:** Outperforms Opus 5.5 on GDP.pdf and AutomationBench, achieving scores close to GPT‑6 Astra at about one‑third to one‑fifth the cost.  
- **Computer Use:** Surpasses GPT‑6 Sol by 7 percentage points on OSWorld 2.0 offline set, within 2.1 points of Astra at roughly one‑seventh the cost.  
- **Scientific Research:** More than doubles GPT‑6 Sol’s score on Terminal‑Bench Science 0.1, costing $5.47 per task versus $23+ for Opus 5.5 and Astra.  
- **Factuality:** Reduces factual error rate from 11.4 % to 7.7 % at low reasoning effort (≈32 % reduction), staying within 1.9 percentage points of Astra’s error rate.

## Safety and Alignment
- Shows lower failure rates than GPT‑6 Sol in transparency, respecting restrictions, and avoiding unauthorized outcomes during agentic tasks.
- No attempts to bypass automated safety reviewers, matching GPT‑6 Astra and GPT‑6 Sol.
- Detailed alignment information is available in the GPT‑6.1 Sol system‑card addendum.

## Pricing and Availability
- Available today to Plus, Pro, Business, Enterprise, and Edu users in ChatGPT Work and Codex (not yet in Chat).
- API model name: `gpt-6.1-sol`.
- Standard API pricing: $2 / M input tokens, $0.10 / M cached input tokens, $10 / M output tokens.
- Upcoming “GPT‑6.1 Sol Ultrafast” variant will provide up to 8× faster token generation in Codex.

## Additional Context
- Evaluations were conducted in OpenAI’s research environment or via API; results may differ slightly from production ChatGPT.
- Competitor model results are taken from publicly available reports.