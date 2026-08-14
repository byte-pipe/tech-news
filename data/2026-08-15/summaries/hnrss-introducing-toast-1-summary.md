---
title: Introducing Toast 1
url: https://www.mixedbread.com/blog/toast-1
date: 2026-08-14
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-08-15T04:04:10.421667
---

# Introducing Toast 1

# Introducing Toast 1 – Summary

## Overview
- First specialised search agent from Mixedbread, released 13 August 2026.  
- Provides frontier‑level search quality, matching or surpassing Claude Opus 5 and GPT‑5.6 Sol.  
- Up to 10× cheaper and 12× faster than comparable frontier models.  
- Optimised for Mixedbread Search but compatible with any search backend.  
- Takes full control of the search loop: decomposes queries, runs sub‑queries, gathers and inspects evidence, curates context, and returns results for the downstream reasoning model.

## Performance Highlights
- Executes a typical employment‑rate comparison query in 5.33 seconds with 16 tool calls across 3 rounds.  
- Establishes a new Pareto frontier for agentic workloads, improving both cost‑per‑task and speed‑per‑task.  

## Financial Benchmark (OfficeQA Pro V2)
- Integrated as a sub‑agent within Codex, GPT‑5.6 Sol + Toast 1 achieves **70 % answer correctness** at **≈ $1.15 per task**.  
- Outperforms the previous best (Claude Fable 5 on Databricks Genie) which reached 60 % correctness at ≈ $4 per task.  
- Without Toast 1, GPT‑5.6 Sol only reaches 33 % correctness, highlighting the impact of specialised evidence gathering.

## Legal Benchmark (Harvey LAB Firm‑Knowledge)
- On 33 tasks, all configurations obtain the same task score (55).  
- Token usage reduced from 80.6 M (vanilla agent) → 47 M with Mixedbread Search → **23 M with Toast 1** (‑ 42 % then ‑ 51 %).  
- Turns per task drop from 21.7 → 14.6 → **11.2**.  
- Result: **3.5× fewer tokens** and > 60 % cost reduction while preserving answer quality.

## Demo
- Interactive demo searches deep into Dwarkesh’s podcast transcripts, illustrating real‑time retrieval capabilities.  

## Frontier‑Class Retrieval
- Works as a standalone model trained for deep search; part of Mixedbread’s co‑design of embedding models, agent harness, and retrieval primitives.  
- On benchmarks (BrowseComp Plus, OfficeQA Pro, LongSeal) matches or approaches the best frontier‑model sweeps while costing a fraction per query.  
- Typical cost per query: **$0.016 – $0.023**; latency: **8 – 10 seconds** (p50).  

## Key Takeaways
- Toast 1 delivers frontier‑level search quality at a fraction of the cost and latency of existing large models.  
- By handling evidence collection efficiently, it frees the main model’s context window for higher‑level reasoning.  
- Demonstrated superior performance on both financial and legal enterprise benchmarks, with significant token and cost savings.  
- Available now as a specialised sub‑agent or as a standalone retrieval model.