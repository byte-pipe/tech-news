---
title: Models & Pricing | DeepSeek API Docs
url: https://api-docs.deepseek.com/quick_start/pricing
date: 2026-05-23
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-05-23T06:01:42.718556
---

# Models & Pricing | DeepSeek API Docs

# Models & Pricing Summary

## Model Details
- **Models**: deepseek‑v4‑flash, deepseek‑v4‑pro  
- **Base URLs**  
  - OpenAI format: `https://api.deepseek.com`  
  - Anthropic format: `https://api.deepseek.com/anthropic`  
- **Versions**: DeepSeek‑V4‑Flash, DeepSeek‑V4‑Pro  
- **Thinking Mode**: Supports both non‑thinking and thinking (default); see “Thinking Mode” for switching.  
- **Context Length**: 1 M tokens  
- **Maximum Output**: 384 K tokens  
- **Features** (available for both models)  
  - JSON output  
  - Tool calls  
  - Chat prefix completion (beta)  
  - FIM completion (beta, non‑thinking mode only)  

## Pricing Overview (per 1 M tokens)
| Item | deepseek‑v4‑flash | deepseek‑v4‑pro |
|------|------------------|----------------|
| Input (cache hit) | $0.0028 | $0.003625 (75 % off) |
| Input (cache miss) | $0.14 | $0.435 (75 % off) |
| Output | $0.28 | $0.87 (75 % off) |
| Concurrency limit | 2500 requests | 500 requests |

- Prices are billed on the total number of input **and** output tokens.  
- Cache‑hit input price was reduced to 1/10 of the launch price effective 2026‑04‑26 12:15 UTC.  
- deepseek‑v4‑pro pricing will revert to 1/4 of the original price after the 75 % discount ends on 2026‑05‑31 15:59 UTC.  
- Model names `deepseek-chat` and `deepseek-reasoner` will be deprecated; they map to the non‑thinking and thinking modes of deepseek‑v4‑flash.  

## Deduction Rules
- Expense = number of tokens × applicable price.  
- Fees are deducted first from granted balance, then from topped‑up balance if both exist.  
- Prices may change; users should top up based on actual usage and review this page regularly for updates.