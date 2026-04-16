---
title: Defeating Nondeterminism in LLM Inference - Thinking Machines Lab
url: https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/
date: 2026-04-16
site: tldr
model: llama3.2:1b
summarized_at: 2026-04-16T12:01:11.798114
---

# Defeating Nondeterminism in LLM Inference - Thinking Machines Lab

# The Concurrency + Floating Point Hypothesis for LLM Inference Determinism

### Background and Context

The question of determining the determinism in Language Model (LLM) inference engines has been a topic of ongoing discussion. While it is often observed that the outputs from different instances of an LLM can be different, this result may not necessarily imply indeterminacy. This paper aims to explore the notion that the combination of concurrency and floating-point arithmetic in GPU-accelerated computations contributes to non-determinism in LLM inference.

### The Concurrency + Floating Point Hypothesis

The concurrency + floating point hypothesis states that the concurrent execution of different cores in a Multi-Core processor, combined with the inherent non-associativity of floating-point operations on GPUs, lead to nondeterministic behavior in computations such as matrix multiplication.

### Analysis and Empirical Evidence

This hypothesis has been proposed by various researchers, including those mentioned in the paper. Notably, recent GPU implementations (such as vLLM or SGLang) demonstrate that even when running inference on your own hardware using Open Software Library (OSS) components like vLLM or SGLang, sampling still isn't determinism.

### Mathematical Analysis

The math behind this phenomenon is rooted in the following:

* In floating-point arithmetic, $(a + b) \neq a + (b + c)$ due to finite precision and rounding errors. This can result in different outputs when parallel operations across multiple threads are performed.
* The `torch.mm` operation on GPU results have shown that even with this math being handled correctly, the actual execution can introduce nondeterminism due to concurrent thread scheduling.
- A numerical example has been provided using the PyTorch library to demonstrate this effect.

### What Can We Learn?

By exploring the concurrency + floating point hypothesis for LLM inference determinism, researchers can refine our understanding of complex computational algorithms and consider additional mechanisms at play that may lead to non-determinacy. 

Moreover, identifying possible causes of nondeterminism in these computations can aid in building robust models that predict system behavior more accurately.

While not exhaustive proof of the conjecture is presented here with this paper's snippet, theoretical considerations are supported by recent experiments on GPUs and a review of existing work on LLM determinability.

Further studies will be required to fully establish the validity and scope of this discovery.