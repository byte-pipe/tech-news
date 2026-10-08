---
title: Claude Haiku 5.5 Pricing: The 100,000-Token Threshold | ImportStatic
url: https://importstatic.com/ai/claude-haiku-5-5-pricing-threshold
date: 2026-10-08
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-10-08T12:51:16.232126
---

# Claude Haiku 5.5 Pricing: The 100,000-Token Threshold | ImportStatic

# Claude Haiku 5.5 Pricing: The 100,000‑Token Threshold

## Overview
- Anthropic released Claude Haiku 5.5 on 7 Oct 2026; available via Claude API, Bedrock, Google Cloud, Microsoft Foundry, and AWS Claude Platform.  
- Base price: **$0.10 per M input tokens** (vs $1 for Haiku 4.5).  
- The cheap rate applies only to prompts **≤ 100,000 tokens**; any request exceeding that threshold is billed at **five times** the rate for the entire request.

## Two‑Tier Price Table (per M tokens)

| Tier | Input | Output | Cache read | Cache write (5 min) | Cache write (1 h) | Batch I/O |
|------|-------|--------|------------|----------------------|--------------------|-----------|
| ≤ 100k | $0.10 | $0.50 | $0.01 | $0.125 | $0.20 | $0.05 / $0.25 |
| > 100k | $0.50 | $2.50 | $0.05 | $0.625 | $1.00 | $0.25 / $1.25 |
| Haiku 4.5 | $1.00 | $5.00 | $0.10 | $1.25 | $2.00 | $0.50 / $2.50 |

- Every rate in the “> 100k” column is exactly **5×** the corresponding “≤ 100k” rate, including output tokens.

## What Counts as “Prompt”
- Prompt = `input_tokens + cache_creation_input_tokens + cache_read_input_tokens`.  
- Cached tokens are still counted; they only affect the per‑token price, not whether they count.  
- The newer tokenizer generates ~30 % more tokens than Haiku 4.5, so the effective threshold for legacy token counts is ≈ 76,900 tokens.  
- Token‑count endpoint (`/v1/messages/count_tokens`) gives an estimate; do not rely on an exact ≤ 100k check.

## Go Cost Calculator (Key Logic)
```go
type Usage struct {
    InputTokens, CacheCreationInputTokens, CacheReadInputTokens, OutputTokens int
}
type Rates struct{ Input, CacheWrite5m, CacheRead, Output float64 }

const Haiku55Threshold = 100_000

func (u Usage) PromptTokens() int {
    return u.InputTokens + u.CacheCreationInputTokens + u.CacheReadInputTokens
}
func (u Usage) at(r Rates) float64 {
    return (float64(u.InputTokens)*r.Input +
            float64(u.CacheCreationInputTokens)*r.CacheWrite5m +
            float64(u.CacheReadInputTokens)*r.CacheRead +
            float64(u.OutputTokens)*r.Output) / 1e6
}
func Haiku55Cost(u Usage) (dollars float64, long bool) {
    if u.PromptTokens() > Haiku55Threshold {
        return u.at(Haiku55Long), true
    }
    return u.at(Haiku55Short), false
}
```
- A single request of 100 k input + 2 k output costs **$0.011**; adding one extra input token pushes it to **$0.055**.

## Practical Cost Implications
- **Chunking** large inputs dramatically reduces cost: two 75 k‑token calls (each with 1 k output) cost ≈ $0.016, while one 150 k‑token call costs ≈ $0.0775.  
- For extraction/classification tasks, splitting the document into sub‑prompts is now a **pricing decision** as well as a quality one.

## Agent Loop Example
- Simulated tool‑calling agent: 8 k system prompt + per‑turn 5 k tool result + 0.5 k reply.  
- Turn 16 (≈ 95.5 k tokens) stays in cheap tier: $0.00184.  
- Turn 17 crosses 100 k → expensive tier: $0.00946 (≈ 5× cost of previous turn).  
- Append‑only loop over 40 turns costs **≈ $0.33**.  
- Adding a 3 k‑token summary before crossing the threshold reduces total to **≈ $0.06**.

## API‑Side Context Compaction
- Default compaction trigger: **150 k input tokens** (i.e., compaction starts after the price has already jumped).  
- Minimum configurable trigger: **50 k tokens**. Example payload:

```json
{
  "model": "claude-haiku-5-5",
  "max_tokens": 4096,
  "context_management": {
    "edits": [
      {
        "type": "compact_20260112",
        "trigger": { "type": "input_tokens", "value": 80000 }
      }
    ]
  },
  "messages": [{ "role": "user", "content": "..." }]
}
```

- Adjust the trigger to stay below the 100 k threshold and avoid the 5× rate increase.

## Takeaways
- The 100 k token boundary is a **hard tier switch** applied to the whole request, not a marginal rate.  
- Accurate token counting (including cache tokens) and awareness of the newer tokenizer are essential to stay in the cheap tier.  
- For large‑context workloads, **chunking** or **server‑side compaction** must be deliberately configured; otherwise costs can explode after a single turn.