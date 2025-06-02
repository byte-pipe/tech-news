---
author: mfiguiere
date: 2025-05-31
description: Surprisingly fast AI-generated kernels we didn't mean to publish yet
enhanced_prompting: true
fetched_at: '2025-06-01T01:56:16.849557

  '
local_model: true
model: gemma3:27b
original_url: 'https://crfm.stanford.edu/2025/05/28/fast-kernels.html

  '
site_name: hackernews_api
summarization_type: local_high_quality
summarized_at: '2025-06-01T02:00:21.132235'
summary_type: local_high_quality
tags:
- hackernews
- trending
title: Stanford CRFM
url: 'https://crfm.stanford.edu/2025/05/28/fast-kernels.html

  '
---

• Here's a concise summary of the Stanford CRFM article, formatted as bullet points for technical professionals:
• **Novel Kernel Generation Approach:** The research demonstrates a test-time kernel generation method achieving performance competitive with, and sometimes exceeding, hand-optimized PyTorch kernels. This is achieved *without* relying on complex DSLs like CUTLASS or Triton, utilizing pure CUDA-C. The key is a parallel, hypothesis-driven search, moving beyond sequential refinement.
• **Exploratory Search & Optimization Strategies:**  The method employs a multi-round, parallel evaluation of kernel optimization ideas.  Successful strategies identified include leveraging read-only caches, converting convolutions to TensorCore-optimized GEMM, double-buffering for memory access, and aggressive shared memory utilization for index caching and data reuse.  The approach highlights the power of broad exploration over solely relying on model retraining.
• **Performance Benchmarks & Results:**  The generated kernels were benchmarked on an Nvidia L40S GPU using the KernelBench framework.  Results show significant speedups (up to 1.79x) for foundational ML operators (Conv2D, etc.) and a fused AlexNet block, demonstrating the potential for automated performance optimization.
