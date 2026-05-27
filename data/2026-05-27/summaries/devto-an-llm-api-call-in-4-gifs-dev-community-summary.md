---
title: An LLM API call, in 4 GIFs - DEV Community
url: https://dev.to/jasmin/an-llm-api-call-in-4-gifs-33b1
date: 2026-05-26
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-05-27T13:39:50.791793
---

# An LLM API call, in 4 GIFs - DEV Community

# An LLM API call, in 4 GIFs

## 1. The request
- Shows a minimal Node.js API call: six lines, API key, JSON body `{model, messages, max_tokens}`.  
- The API is stateless; conversation history must be stored and resent with each call.  
- `max_tokens` is a hard limit; the model may stop mid‑sentence when reached.  
- Request shape is universal across providers; only URL, auth header, and prompt placement differ.

## 2. The response
- Returns a JSON object with ~10 fields; only four are typically needed.  
- `stop_reason` indicates why generation ended (`end_turn`, `max_tokens`, `tool_use`, `stop_sequence`) and should be checked to avoid bugs.  
- `usage` reports input and output token counts; log it from day one to prevent surprise bills.  
- Ignoring `stop_reason` can cause silent failures.

## 3. Tokens
- Tokens are not the same as words; a single word can be multiple tokens.  
- Code and JSON are token‑heavy (each bracket, comma, or character counts).  
- Non‑English text often uses 2–4× more tokens than English.  
- Rough rule for English: 1 token ≈ 4 characters ≈ 0.75 words; verify with a tokenizer for other languages.

## 4. The bill
- Pricing separates input and output tokens; output tokens cost ~3–5× more.  
- Cost formula:  
  `cost = (input_tokens / 1,000,000) × input_price + (output_tokens / 1,000,000) × output_price`  
- Implications:  
  1. Long prompts are cheap; long responses are expensive.  
  2. “Thinking” tokens (model reasoning) are billed as output.  
  3. Tool schemas are sent as input on every request, adding to cost.  
- Example: at $0.006 per call, 100 k calls/day ≈ $600/month.

## 5. The whole thing in 20 lines
- The article provides a complete, dependency‑free Node.js script (`Jasmin2895/TinyAgent`) that performs the described API call.

## 6. Three things to try before the next post
- **Experiment with usage:** make multiple calls, vary prompt length, observe token usage.  
- **Test `max_tokens`:** set a low limit (e.g., 20) on a long request, watch truncation, and inspect `stop_reason`.  
- **Build a multi‑turn chat manually:** maintain a `messages` array, append user and model messages, resend whole array each turn to see cost growth.

## 7. What’s next
- Future posts will extend TinyAgent beyond simple replies, adding more capabilities.  
- Encouragement to keep coding and monitoring costs.