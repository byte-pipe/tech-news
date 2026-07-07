---
title: "98% isn't very much · WhyNotHugo (雨果)"
url: https://whynothugo.nl/journal/2026/07/03/98-isnt-very-much/
date: 2026-07-07
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-07-08T01:55:40.232755
---

# 98% isn't very much · WhyNotHugo (雨果)

# 98% isn’t very much · WhyNotHugo (雨果)

## Misinterpretation of “98 %”
- 98 % sounds impressive when it describes exceptional outcomes (lottery wins, perfect exam scores).  
- The same figure is inadequate for basic expectations (food‑poisoning safety, regular salary payments, reliable restaurant billing).

## Real‑world implications
- A restaurant that avoids food poisoning only 98 % of the time still makes customers sick weekly or monthly.  
- An employer who pays employees only 98 % of the time creates an unreliable workplace.  
- Paying a bill only 98 % of the time would lead to frequent trouble for the payer.

## Audience‑specific considerations
- “Works for 98 % of the population” can exclude millions of users (≈150 million on a global scale).  
- For a specific site, the 98 % figure may drop to 70 % of actual visitors, meaning a large portion of the target audience is left out.  
- Relying on a generic statistic ignores the mismatch between general population data and a product’s actual user base.

## Example: nested CSS support
- Although nested CSS is officially standard since 2023 and marketed as “widely supported,” the author’s site saw only ~70 % of browsers supporting the feature.  
- Deploying it would have broken the experience for 30 % of the site’s visitors, despite the “98 %” claim in broader surveys.

## Core argument
- The 98 % statistic is a lazy shortcut; robust engineering must handle edge cases, not just the majority.  
- If a new feature cannot degrade gracefully, it fails the basic minimum for the remaining 2 % of users, and therefore cannot be considered truly “widely supported.”