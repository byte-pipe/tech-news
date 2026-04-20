---
title: GitHub - deepseek-ai/DeepGEMM: DeepGEMM: clean and efficient FP8 GEMM kernels with fine-grained scaling · GitHub
url: https://github.com/deepseek-ai/DeepGEMM
date:
site: github
model: llama3.2:1b
summarized_at: 2026-04-18T11:36:40.692158
---

# GitHub - deepseek-ai/DeepGEMM: DeepGEMM: clean and efficient FP8 GEMM kernels with fine-grained scaling · GitHub

**DeepGEMM Overview**

DeepGEMM is a unified, high-performance tensor core kernel library that combines various computation primitives from deep learning models into a single CUDA codebase.

* **Main Features**: DeepGEMM introduces several key components:
 + Unified GEMMs (FP8, FP4, BF16) with fine-grained scaling
 + Fused MoE with overlapped communication for Mega-MoE
 + MQA scoring for lightning indexer and more
* **Key Components**:
 + Simplified structure with limited core kernel functions
 + Designed for simplicity and accessibility
 + Lightweight Just-In-Time (JIT) compilation module during installation

**Key Developments**

Recent updates include:

* Performance comparison to be posted later, providing insight into current performance
* Support for scoring kernels (weighted ReLU MQA logits) for lightning indexer in DeepSeek v3.2
* Full refactor with a low-CPU-overhead JIT module and new features

Additionally, notable improvements include:

* Weight gradient kernels for dense and MoE backward
* NVRTC and post-compilation SASS optimization are disabled due to various constraints

**Note**: Please consult the #304 and #200 repositories for more details on the recent updates and additional features.
