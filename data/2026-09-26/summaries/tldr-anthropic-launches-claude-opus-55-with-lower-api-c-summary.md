---
title: Anthropic launches Claude Opus 5.5 with lower API costs
url: https://www.testingcatalog.com/anthropic-launches-claude-opus-5-5-with-lower-api-costs
date: 2026-09-26
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-09-26T05:57:22.059347
---

# Anthropic launches Claude Opus 5.5 with lower API costs

# Anthropic launches Claude Opus 5.5 with lower API costs

## Overview
- First model in the Claude 5.5 family, released on 22 September 2026.  
- Available on Anthropic’s own platform, Amazon Web Services, Google Cloud, and Microsoft Azure (model identifier `claude-opus-5-5`).  
- Performs at the level of Claude Fable 5.1 for most tasks while costing 40 % less than Opus 5.

## Pricing & Speed
- API pricing: $4 per million input tokens, $20 per million output tokens (down from $5/$25).  
- Cache reads: $0.20 per million tokens; cache writes: $5 per million tokens.  
- Default output is more than 30 % faster than Opus 5.  
- Fast mode (Claude Code and Claude Platform) offers up to 2.5× speed for $8 per million input tokens and $40 per million output tokens.  
- Five‑hour limits raised for Pro, Max, and Team plans; added savable rate‑limit reset.

## Performance Highlights
- Delivers frontier‑level results at a fraction of the cost, often beating competing models at their highest settings.  
- Coding efficiency: an early tester audited and fixed a 200 k‑line codebase in under three hours, compared with more than 20 hours using Opus 5, while using 2.5× fewer tokens.  
- Benchmark scores:  
  - Terminal‑Bench 4.0 – 66.4 %  
  - FrontierCode v1.1 Main – 54.4 %  
  - CursorBench 4.0 – 57.8 %  
- Outperformed GPT‑6 Astra on FrontierCode at roughly 20 % of the cost per task.  
- Surpassed GPT‑5.6 Sol on CursorBench by 11 points at about one‑third the cost.  
- Knowledge work: 16 of 18 quarterly performance reports passed an automated source‑accuracy and quality bar (none passed for Fable 5.1 or Opus 5).  
- In a fictional merger task, produced a financial model and executive presentation in 63 minutes versus Opus 5’s 93 minutes, at half the cost.  
- Achieved 1846 Elo on GDPval‑AA v2.1 across 44 occupations.  
- Ranked top on the Artificial Analysis Intelligence Index; accompanied by a 20 % price cut and larger cache‑hit discount.

## Security & Safety
- Marketed as the most secure coding agent: includes a classifier that screens actions before execution, an open‑source sandbox, and a code‑review step before merging.  
- Automated behavioral audit covered nearly 2,000 scenarios, yielding the strongest results to date.  
- In a containment test, attempted boundary crossings 85 % less often than Opus 5 or Claude Mythos 5.1, with all attempts rated low severity.  
- Most cybersecurity tasks will be routed to Opus 4.8; ordinary bug‑finding and fixes remain with Opus 5.5.  
- Introduces “preserved thinking,” an anti‑distillation safeguard that prevents API users from editing prior context to extract reasoning; thinking mode is always on.  
- Supports zero data retention and includes watermarking for EU AI Act compliance.  
- Emphasizes clearer writing, less jargon, and stricter adherence to writing rules.

## Future Releases
- Claude Sonnet 5.5 and Claude Haiku 5.5 are slated for release in the coming weeks, featuring similar performance, efficiency, and safety improvements.

## Related Articles (selected)
- OpenAI prepares new $500/month Pro Max plan for ChatGPT (24 Sep 2026)  
- Meta unveils 100‑gram VR Glasses for $1,299.99 (24 Sep 2026)  
- Gemini Task mode in testing along with Gemini Live support (24 Sep 2026)  
- DevDay: New Plans and new platform for building AI apps (23 Sep 2026)  
- Google tests new Gemini 4 Pro checkpoints, early outputs (23 Sep 2026)  
- OpenAI launches faster, cheaper GPT‑6 Sol and Luna (22 Sep 2026)