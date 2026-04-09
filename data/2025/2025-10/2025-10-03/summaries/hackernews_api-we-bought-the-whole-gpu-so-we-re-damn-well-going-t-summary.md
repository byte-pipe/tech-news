---
title: "We Bought the Whole GPU, So We're Damn Well Going to Use the Whole GPU · Hazy Research"
url: https://hazyresearch.stanford.edu/blog/2025-09-28-tp-llama-main
date: 2025-09-28
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-10-03T11:25:00.359117
screenshot: hackernews_api-we-bought-the-whole-gpu-so-we-re-damn-well-going-t.png
---

# We Bought the Whole GPU, So We're Damn Well Going to Use the Whole GPU · Hazy Research

# Optimizing High-Throughput GPU Workloads with Low-Latency Megakernels

## Introduction
Researchers have explored ways to optimize high-throughput GPU workloads. This paper revisits these approaches in the context of low-latency inference using Llama-70B.

## Methodology
The authors developed a new low-latency megakernel for tensor-parallel inference, which uses the whole GPU and aggressively overlaps compute, memory, and communication operations to maximize resource utilization.

## Key Findings

* The existing megakernel optimized for Llama-1B can be adapted for Llama-70B with minimal modifications.
* High-throughput inference requires distinct optimizations for low-latency and high-throughput workloads.
* The heterogeneous nature of the model and large-batch inference workload require a different approach to optimize resource utilization.

## Comparison
Previous approaches assigned different SMs to different operations, developed custom kernels for prefill and decode tasks. However, these methods may not be adaptable to heterogeneous GPU workloads, which requires a more innovative approach.

## Implications

* The new megakernel can outperform SGLang by 22% in end-to-end throughput.
* Integration with theTokasaurus inference engine can significantly improve performance (>30% improvement).
* The researchers emphasize that their code is intended for use in research, and warnings are given about its sensitivity to compiler versions, GPU setup, and usage.
