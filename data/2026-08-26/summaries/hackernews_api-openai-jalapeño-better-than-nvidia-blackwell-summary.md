---
title: OpenAI Jalapeño: Better Than Nvidia Blackwell
url: https://newsletter.semianalysis.com/p/openai-jalapeno-better-than-nvidia
date: 2026-08-26
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-08-26T12:52:47.341998
---

# OpenAI Jalapeño: Better Than Nvidia Blackwell

# OpenAI Jalapeño: Better Than Nvidia Blackwell

## Overview
- OpenAI announced its first‑generation inference ASIC, “Jalapeño,” at Hot Chips 2026 after a ~16‑month design‑to‑tape‑out cycle in partnership with Broadcom.  
- The chip is positioned as a **general‑purpose** AI inference accelerator, not a model‑specific accelerator.  
- OpenAI provided lab access for hands‑on benchmarking with the InferenceX suite.

## Design and Architecture
- Built from a clean‑sheet architecture focused on hardware‑software co‑design.  
- Utilizes HBM4 memory, putting it on par with flagship GPUs from NVIDIA and AMD.  
- Emphasizes pragmatic design decisions and a “cracked” engineering team to meet aggressive timelines.  
- Targets high token‑throughput per megawatt (tok/s/MW) rather than raw FLOPs.

## Performance Highlights
- **Perf/W (tokens per MW)**: Jalapeño outperforms NVIDIA Blackwell and AMD chips across low‑latency and high‑throughput scenarios, even without Multi‑Token Prediction (MTP).  
- Single‑Token Prediction (STP) results:
  - >700 tokens / sec / user at concurrency 1 on DeepSeek R1.  
  - ~1,400 tokens / sec / user on Kimi‑K2.5 and GPT‑OSS.  
- Benchmarks were run in OpenAI’s lab; results align with OpenAI’s supplied numbers.  
- GSM8k evaluation matches NVIDIA’s performance levels.

## Comparisons with Other Chips
- **NVIDIA Blackwell**: Jalapeño shows higher perf/W across almost all tested workloads.  
- **Vera Rubin (NVL72)**: Although Rubin ships to customers, Jalapeño’s STP throughput per MW surpasses Rubin’s MTP results reported by NVIDIA and CoreWeave.  
- The article argues that comparing Jalapeño to Blackwell alone is incomplete; Rubin is a more appropriate peer due to similar HBM4 usage.

## Caveats and Limitations
- All performance numbers are provided by OpenAI; the authors verified lab runs but did not execute the full InferenceX suite or the AgentX benchmark.  
- AgentX, which stresses long‑context, multi‑turn workloads, may reveal different performance characteristics not captured by single‑turn 8k/1k tests.  
- Larger, newer models (e.g., DeepSeek V4 Pro, Kimi K3) have not been demonstrated on Jalapeño, and bringing up such models on a new ASIC can be more challenging.

## Power Efficiency Focus
- OpenAI’s design priority is tokens per megawatt, reflecting datacenter power constraints rather than budget or floor space.  
- Jensen’s Computex 2026 keynote emphasized that “throughput per watt is revenue” for power‑limited datacenters.  
- The article discusses behind‑the‑meter (BtM) power solutions (on‑site generators) as a way operators address grid capacity limits, citing xAI’s Colossus 2 as an example.

## Conclusions
- Jalapeño demonstrates that a fast‑track ASIC program can produce a competitive, general‑purpose inference chip that beats current GPU offerings on efficiency metrics.  
- While early results are promising, broader benchmark coverage (including AgentX) and validation on larger models are needed to fully assess its position against established GPUs like Vera Rubin and Blackwell.