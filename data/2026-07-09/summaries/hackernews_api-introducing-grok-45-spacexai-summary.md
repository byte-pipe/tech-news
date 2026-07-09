---
title: Introducing Grok 4.5 | SpaceXAI
url: https://x.ai/news/grok-4-5
date: 2026-07-09
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-07-09T15:20:04.849375
---

# Introducing Grok 4.5 | SpaceXAI

# Introducing Grok 4.5

## Overview
- SpaceXAI’s newest model, positioned as the most capable for coding, agentic tasks, and knowledge work.  
- Launched with free trial options and integration in Grok Build and Cursor.

## Real‑world engineering excellence
- Trained on extensive datasets covering coding, science, engineering, and mathematics.  
- Benchmark performance (higher pass@1 scores indicate stronger problem‑solving):
  - **DeepSWE 1.0**: Grok 4.5 – 62.0 % (behind Fable 66.1 % and GPT 5.5 64.31 %).  
  - **DeepSWE 1.1**: Grok 4.5 – 53 % (behind Fable 70 % and GPT 5.5 67 %).  
  - **SWE Marathon**: Grok 4.5 – 29 % resolution rate (top among listed models).  
  - **Terminal Bench 2.1**: Grok 4.5 – 83.3 % (near‑top, just below Fable 84.3 %).  
  - **SWE Bench Pro**: Grok 4.5 – 64.7 % resolve rate (second to Fable 80.4 %).  

## Training methodology
- Utilized tens of thousands of NVIDIA GB300 GPUs with large‑scale stability techniques.  
- Data pipeline emphasized deduplication, quality scoring, and domain‑focused curation.  
- Reinforcement learning covered hundreds of thousands of multi‑step software‑engineering tasks, employing automated and model‑based grading.  
- Asynchronous training allowed long‑running agentic rollouts while scaling across GPUs.

## Capabilities
- **Coding**: Handles complex Rust, C/C++, and full‑stack app generation from a single prompt (e.g., three‑js solar‑system simulation).  
- **Office productivity**: Generates sophisticated Excel models, PowerPoint decks, and Word documents, including research‑driven content and design elements.  

## Performance and efficiency
- Serves at ~80 TPS, delivering results faster than comparable “flash” models.  
- Token efficiency: averages 15,954 output tokens per SWE Bench Pro task, about 4.2 × fewer than Opus 4.8 (67,020 tokens).  

## Pricing
- $2 per million input tokens.  
- $6 per million output tokens.  
- Claims roughly 2 × token efficiency versus leading competitors, reducing both cost and step count.

## Availability & Getting started
- Accessible today in Grok Build, Cursor (all plans), and via the SpaceXAI console.  
- API example provided for bug‑fixing task; requires an API key.  
- Not yet available in the EU; rollout expected mid‑July.  
- Free limited‑time usage offered in Grok Build and Cursor; installation via `curl -fsSL https://x.ai/cli/install.sh | bash`.