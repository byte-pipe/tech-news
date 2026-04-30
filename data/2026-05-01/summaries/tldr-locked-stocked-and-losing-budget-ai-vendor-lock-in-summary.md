---
title: Locked, stocked, and losing budget: AI vendor lock-in bites • The Register
url: https://www.theregister.com/2026/04/28/locked_stocked_and_losing_budget/
date: 2026-05-01
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-05-01T03:53:51.279930
---

# Locked, stocked, and losing budget: AI vendor lock-in bites • The Register

# Locked, stocked, and losing budget: AI vendor lock‑in bites back

## Executive over‑confidence vs. reality  
- C‑suite leaders assumed they could swap frontier AI models within days; the survey shows most are wrong.  
- 90 % of executives believed a vendor change could be done in four weeks, 41 % thought it could be done in 2–5 business days.  
- In practice, only 42 % of migrations were smooth; 58 % faced failure or far‑greater effort.

## Why switching is hard  
- AI solutions depend on vendor‑specific APIs, proprietary training data, custom deployment tooling, and deep workflow integrations.  
- These dependencies create undocumented “temporary” adaptations that are costly to replicate elsewhere.  
- Switching now involves moving context, workflows, and institutional memory, not just an API rewrite.  
- Most operators have not mapped these dependencies, making migration riskier.

## Rising AI pricing pressure  
- Providers that have been loss leaders are raising prices dramatically.  
  - OpenAI: GPT‑5.2 input token price jumped from $1.25 (GPT‑5.1) to $5.75.  
  - Anthropic: moved Claude Enterprise from fixed to dynamic usage‑based pricing, potentially doubling or tripling costs for heavy users.  
- Ancillary services (e.g., GitHub Copilot, Microsoft 365) are also tightening compute limits and ending “all‑you‑can‑eat” plans.  
- Underlying infrastructure costs (memory chips, GPU capacity, energy) are becoming structural, recurring expenses that vendors can no longer absorb.

## Business implications  
- AI is not SaaS‑style software; every query incurs a real token‑based cost that scales with usage.  
- Fixed‑price tiers are disappearing; token‑based pricing will dominate, reducing compute per dollar.  
- Companies relying on a single vendor risk price spikes, vendor disappearance, or acquisition that could strip functionality.  
- Even “self‑hosted” models like Meta Llama are not truly open source and can be abandoned, leaving users stranded.

## Outlook and recommendations  
- Enterprises must audit and document all AI‑related dependencies (APIs, data, tooling, workflow customizations).  
- Develop multi‑vendor or hybrid strategies to avoid single‑point lock‑in.  
- Budget for token‑based usage costs and build monitoring to detect price‑driven budget overruns early.  
- Consider long‑term total cost of ownership, including infrastructure and energy, when selecting AI providers.  
- Stay prepared for vendor‑driven pricing baselines that will likely stay elevated throughout the AI era.