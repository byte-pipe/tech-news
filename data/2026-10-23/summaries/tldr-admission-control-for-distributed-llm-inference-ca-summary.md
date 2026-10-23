---
title: Admission Control for Distributed LLM Inference: Cache-Aware Routing, GPU-Aware Signals, and When to Say No | Antonello Fratepietro
url: https://www.fratepietro.com/2026/admission-control-distributed-llm-inference
date: 2026-10-23
site: tldr
model: llama3.2:1b
summarized_at: 2026-10-23T15:44:31.545749
---

# Admission Control for Distributed LLM Inference: Cache-Aware Routing, GPU-Aware Signals, and When to Say No | Antonello Fratepietro

## Introduction
The article discusses the importance of admission control in distributed large language models (LLMs) to ensure system performance, resource efficiency, and scalability. Admission control is the traffic-management layer that determines whether to accept, queue, or reject incoming requests.

## Admission Control Basics

The article highlights the challenges of admission control in distributed LLMs. A key issue is that admission control is not a single check, but rather a stack of checks that need to be spread across multiple components within the system.

## Three Components of Admission Control

The three components of admission control are:

*   **Admission (Whether and When)**
  *   Determines whether a request is accepted or rejected.
*   **Routing (Where)**
  *   Routes requests to a suitable GPU based on cache locality and per-node load.
*   **Scheduling (How)**
  *   Decides which requests to accept and how to manage the system.

## Admission Control in Practice

The article explains how admission control works in practice by highlighting the limitations of traditional load balancing methods. The author argues that stateless web services like LLM inference break the assumptions behind classical load balancing tools.

## Real-World Challenges

The article cites several real-world challenges to admission control, including:

*   **Request Cost Variation**
  *   Requests have different costs based on the number of tokens or cache footprint.
*   **GPU Saturation**
  *   Running out of GPU memory can cause severe delays and timeouts.

## Mitigating Concerns

The article offers several solutions to mitigate concerns associated with admission control, including:

*   **Batching**
  *   Grouping requests to reduce contention and improve concurrency.
*   **Asynchronous Processing**
  *   Processing requests asynchronously to avoid blocking.

## Conclusion

In conclusion, admission control is crucial for ensuring the performance, efficiency, and scalability of distributed LLMs. By understanding the complexities of admission control and its challenges, developers can design more effective systems and optimize their performance.