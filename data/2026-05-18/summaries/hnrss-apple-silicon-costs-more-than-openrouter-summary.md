---
title: Apple Silicon costs more than OpenRouter
url: https://www.williamangel.net/blog/2026/05/17/offline-llm-energy-use.html
date: 2026-05-17
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-05-18T06:01:11.408990
---

# Apple Silicon costs more than OpenRouter

# Offline Agentic Coding part 3: Apple Silicon costs more than OpenRouter

## Overview
- I compare the cost of running inference on an M5 MacBook Pro with the price of using OpenRouter for similar models.
- The analysis includes electricity, hardware depreciation, token throughput, and resulting cost per million tokens.

## Electricity
- My local electricity rate is about $0.20 /kWh (rounded up from $0.18 /kWh).
- The MacBook draws roughly 50–100 W under load.
- Hourly electricity cost: $0.009–$0.018 (≈ $0.02 / hour).
- Daily cost at full load: about $0.48 cents.

## Hardware
- 14‑inch MBP with M5 Max and 64 GB RAM costs $4,299.
- Assuming a useful lifespan of 3, 5, or 10 years, the annual cost is $1,433, $860, or $430.
- Corresponding hourly depreciation:
  - 3 years: $0.16358
  - 5 years: $0.09815
  - 10 years: $0.04908
- I consider 5 years a reasonable estimate for normal use; 7–10 years is plausible for lighter workloads.

## Tokenomics
- Measured throughput: 10–40 tokens / second for Gemma 4‑31B.
- Tokens per hour:
  - 10 t/s → 36,000 tokens / hour
  - 40 t/s → 144,000 tokens / hour
- Cost per million tokens (including electricity and hardware):
  - Low throughput, short lifespan: $4.79 / M tokens
  - High throughput, long lifespan: $0.40 / M tokens
- Hardware cost dominates the total.

## OpenRouter Comparison
- OpenRouter pricing for Gemma 4‑31B: $0.38–$0.50 / M tokens.
- Under optimistic local conditions (50 W, 40 t/s, 10 years) the MacBook approaches OpenRouter cost.
- Under pessimistic conditions (100 W, 10 t/s, 3 years) the MacBook can be up to 10× more expensive.
- A realistic estimate: local inference costs about 3× the OpenRouter price per million tokens.

## Conclusion
- Inference speed is the primary differentiator; cloud providers on OpenRouter achieve 60–70 t/s, 3–7× faster than my MacBook’s 10–20 t/s.
- For human‑level work, employee salary far exceeds token generation cost, making large‑scale cloud services (e.g., Anthropic) more economical.
- Nonetheless, it is remarkable that a consumer‑grade device can run models near Anthropic Sonnet performance levels.