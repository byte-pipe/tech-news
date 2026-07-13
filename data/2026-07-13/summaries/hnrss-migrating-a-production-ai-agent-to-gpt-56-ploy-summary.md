---
title: Migrating a production AI agent to GPT-5.6 | Ploy
url: https://ploy.ai/blog/migrating-a-production-ai-agent-to-gpt-5-6
date: 2026-07-12
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-07-13T12:27:22.991462
---

# Migrating a production AI agent to GPT-5.6 | Ploy

# Migrating Ploy’s Production AI Agent to GPT‑5.6 Sol  

## Overview  
- Ploy switched its default agent model from Claude Opus 4.8 to OpenAI’s GPT‑5.6 Sol after head‑to‑head tests showed the new model was faster, cheaper, and at least as good on completed builds.  
- The agent builds and edits full marketing websites, so the model must handle planning, code generation, image creation, screenshots, and task completion judgment.  

## Evaluation Findings  
- Initial cross‑model runs exposed many false failures caused by the evaluation harness being tuned to Opus (e.g., tool‑call budgets, lack of batched file reads). About one‑third of failures were harness‑related, not model‑related.  
- After fixing the harness, GPT‑5.6 Sol achieved:  
  - 2.2× lower wall‑clock time (3 m 42 s vs 8 m).  
  - 27 % lower cost ($2.22 vs $3.06).  
  - Roughly half the output tokens (17.1 K vs 33 K).  
  - Higher visual score (0.970 vs 0.936).  

## Design Quality  
- GPT‑5.6 produces clean, modern, grid‑based layouts but tends toward a uniform look unless explicitly steered.  
- Additional prompting and engineering are required to achieve brand‑specific designs.  

## Migration Steps  

### Step 0 – Clean the Evaluation Harness  
- Verify tool‑call budgets, support batched file reads, and ensure scoring thresholds are explicit.  
- Triaging full traces prevents mis‑attributing harness assumptions to model performance.  

### Step 1 – Align Tool‑Call Schemas  
- Claude omitted unused optional parameters; GPT‑5.6 sent all 25 parameters, inventing values (e.g., `offset: 0`).  
- This caused many empty file reads and unnecessary calls.  
- Solution: transform optional fields to “required but nullable” for OpenAI models, then strip `null` values before the tool runs.  
- Result: empty reads dropped to 0 % and tool calls reduced by ~30 %.  

### Step 2 – Rebuild Prompt Caching  
- Claude’s cache allowed a 29 K‑token static prefix to be shared organization‑wide via `cache_control`.  
- GPT‑5.6’s cache behaved differently, leading to ~50 % higher apparent cost before adjustment.  
- Reconfiguring the cache to match the provider’s semantics eliminated the cost discrepancy.  

## Takeaways  
- Model migrations expose hidden dependencies on provider‑specific behaviors (tool argument handling, caching, reasoning replay).  
- A systematic, trace‑driven approach—first fixing the harness, then tool schemas, then caching—ensures a fair comparison and a successful switch.  
- Even with superior raw performance, engineering effort is needed to preserve design fidelity and workflow stability.