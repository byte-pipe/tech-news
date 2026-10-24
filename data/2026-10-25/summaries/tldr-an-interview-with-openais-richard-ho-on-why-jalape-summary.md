---
title: An Interview with OpenAI’s Richard Ho on Why Jalapeño Is a Groundbreaking AI Chip
url: https://taekim.substack.com/p/an-interview-with-openais-richard
date: 2026-10-25
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-10-25T02:57:34.787802
---

# An Interview with OpenAI’s Richard Ho on Why Jalapeño Is a Groundbreaking AI Chip

# Summary of Interview with Richard Ho on Jalapeño AI Chip

## Background & Recruitment
- Richard Ho’s career spans computer architecture, supercomputing (D. E. Shaw Research), and early TPU development at Google.  
- He began a PhD in AI at Stanford during the AI winter, then shifted to hardware.  
- Worked at photonics company Lightmatter, gaining insight into photonic communication and compute for AI inference.  
- Sam Altman reached out after Ho’s analysis of emerging hardware trends; Ho was recruited to evaluate and eventually build OpenAI’s own inference chip.  
- The decision to pursue a custom chip stemmed from a full‑stack analysis of workloads, models, software stack, and hardware trajectory, aligning with OpenAI’s mission to deliver intelligence efficiently.

## Design Approach & Key Innovations
- The team started from a clean slate, applying first‑principles thinking without legacy constraints.  
- Focus was on minimizing data movement, the primary source of energy consumption.  
- Adopted an intermediate processing‑in‑memory (PIM) strategy by tightly coupling high‑bandwidth memory (HBM) with compute cores, improving both energy efficiency and token latency.  
- Accepted a more complex programming model to gain the benefits of reduced data movement, betting that AI model frameworks would adapt.  
- Success attributed to converging factors: available talent, clear motivation, pressing need, and favorable timing.

## Architecture Details (HBM Slice)
- The chip contains 64 cores, each directly attached to its own HBM bank, creating isolated memory spaces per core.  
- Access to other memory banks requires routing through a network, which is slower but reduces the overhead of managing a shared address space.  
- Compared to GPUs/CPUs where a single shared memory space demands extensive coherence hardware, Jalapeño eliminates that overhead, gaining speed and efficiency.  
- The design leverages the natural layer‑wise structure of large language models (LLMs) to map computation to cores and local memory, optimizing sharding and parallelism.

## Performance & Benchmarks
- InferenceX benchmarks at Hot Chips showed Jalapeño surpassing rivals in performance‑per‑watt, including Nvidia’s Blackwell, across open‑source models such as GPT‑OSS, DeepSeek R1, and Kimi K2.5.  
- The chip’s token latency benefits stem from the close coupling of compute and memory.  
- Rankings may shift as newer AI systems (e.g., Vera Rubin) emerge, but the initial results demonstrate a strong competitive edge.

## Timing & Future Outlook
- Ho emphasizes that the right timing—team readiness, market need, and technological maturity—was crucial for the chip’s rapid development.  
- The architecture’s success suggests a broader move toward specialized, memory‑centric AI hardware.  
- Ongoing work will address the programming model challenges and continue to refine the full‑stack inference capability for lower cost and power consumption.