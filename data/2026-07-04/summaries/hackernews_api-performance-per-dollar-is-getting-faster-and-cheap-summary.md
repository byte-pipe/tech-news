---
title: Performance per dollar is getting faster and cheaper | Wafer
url: https://www.wafer.ai/blog/glm52-amd
date: 2026-07-03
site: hackernews_api
model: llama3.2:1b
summarized_at: 2026-07-04T11:37:31.208104
---

# Performance per dollar is getting faster and cheaper | Wafer

# Performance Per Dollar is Getting Faster and Cheaper: An Overview of AMD's Advantages

## Background and Key Points

*   Demand for inference is outpacing supply, driving up GPU prices
*   AMD has emerged as a viable alternative with competitive pricing (2.75x cheaper per GPU)
*   Advantages in software and hardware compared to NVIDIA, including day-0 support for faster inference on hardware with less friction

## Main Points

*   **Sustained RPS and Success Metrics**: 
    *   80%  of performance measured on B200, despite being over 2x cheaper than Blackwells
    *   Aggregates throughput: 2626 tok/s/node @ 2.4 rps (2.5x higher)
    *   Cache hit rate: 60%
*   **Token Craziness**: 
    *   Frontier models released almost every week, including Claude Fable and GLM5.2
    *   Limited Blackwells to support inference, leading to high prices

## How We Did It:

*   Chose a quantization framework (MXFP4) for the base bf16 GLM-5.2 model, compared to z-ai's FP8 quantization, which resulted in lossless quantization
*   Evaluated performance using GPU, MXFP4 + GlmMoeDsa path, and vLLM with sglang as inference frameworks