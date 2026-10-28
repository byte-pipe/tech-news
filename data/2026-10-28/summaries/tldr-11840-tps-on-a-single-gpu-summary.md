---
title: 11,840 TPS on a single GPU
url: https://cline.ghost.io/11-840-tps-on-a-single-gpu
date: 2026-10-28
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-10-28T12:08:47.199573
---

# 11,840 TPS on a single GPU

# 11,840 TPS on a single GPU – Summary  

## Context and objective  
- NVIDIA released Nemotron 3.5 Super VL on 15 Oct; we aimed to hit the highest possible throughput on a single DGX Station (252 GB GPU memory).  
- The model is small, fast, and suitable for document intelligence, coding, finance, etc., making it attractive for post‑training on niche use‑cases.  
- Our focus was on inference engineering for maximum concurrent throughput rather than raw latency or accuracy.  

## Baseline configuration  
- Started with vLLM 0.32.0rc1.dev190+g3f1bcfd82, which used 67 GB of GPU memory.  
- Measured 6 058 aggregate tokens / s on a 512‑token input/output test with 256 concurrent streams.  

## Optimizations applied  

1. **MTP decoding**  
   - Enabled the built‑in MTP head (MTP‑3) with OMP 1 (single‑threaded) → ~7 000 t/s.  

2. **Async scheduling**  
   - Off‑loaded CPU scheduling work to run asynchronously, preventing CPU stalls while the GPU processed kernels.  

3. **FlashInfer kernel for Mamba layers**  
   - Switched the Mamba backend from its default kernel to FlashInfer, raising throughput to ~7 800 t/s.  

4. **MTP look‑ahead reduction (MTP‑1)**  
   - Changed from MTP‑3 to MTP‑1; fewer draft tokens reduced verification overhead, boosting throughput to ~9.5 K t/s.  

5. **FP16 Mamba state with stochastic rounding**  
   - Converted Mamba state from FP32 to FP16, accepting a precision drop for a final throughput of 11 840 t/s.  

## Outcome  
- Combined tricks lifted throughput from 6 058 t/s to 11 840 t/s on a single GPU with 256 concurrent requests.  
- Demonstrated that inference performance is highly contextual; the same tricks may hurt performance under different traffic patterns.  

## Take‑aways and future outlook  

- **Traffic‑shape awareness**: Optimize inference settings for the specific request distribution you expect.  
- **Cost advantage**: Fully utilizing a GPU can yield ~66 % lower cost compared with per‑API inference pricing.  
- **Agent‑driven autoscaling**: Envision self‑healing agents that run isolated load tests, tune configurations, and migrate traffic automatically, making inference autoscaling agentic.  

These findings guide anyone looking to host open‑weight models locally and extract maximum throughput from a single high‑end GPU.