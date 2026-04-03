---
title: Apple Intelligence Foundation Language Models Tech Report 2025 - Apple Machine Learning Research
url: https://machinelearning.apple.com/research/apple-foundation-models-tech-report-2025
site_name: hackernews
fetched_at: '2025-07-18T10:19:55.008694'
original_url: https://machinelearning.apple.com/research/apple-foundation-models-tech-report-2025
author: 2bit
date: '2025-07-18'
description: We introduce two multilingual, multimodal foundation language models that power Apple Intelligence features across Apple devices and…
---

research area
Speech and Natural Language Processing
content type
paper
 |
published
July 2025

# Apple Intelligence Foundation Language Models Tech Report 2025

View publication

Copy Bibtex

We introduce two multilingual, multimodal foundation language models that power Apple Intelligence features across Apple devices and services: (i) a ∼3B-parameter on-device model optimized for Apple silicon through architectural innovations such as KV-cache sharing and 2-bit quantization-aware training; and (ii) a scalable server model built on a novel Parallel-Track Mixture-of-Experts (PT-MoE) transformer that combines track parallelism, mixture-of-experts sparse computation, and interleaved global–local attention to deliver high quality with competitive cost on Apple’s Private Cloud Compute platform. Both models are trained on large-scale multilingual and multimodal datasets sourced via responsible web crawling, licensed corpora, and high-quality synthetic data, then further refined with supervised fine-tuning and reinforcement learning on a new asynchronous platform. The resulting models support several additional languages while understanding images and executing tool calls. In public benchmarks and human evaluations, both the server model and the on-device model match or surpass comparably sized open baselines.

A new Swift-centric Foundation Models framework exposes guided generation, constrained tool calling, and LoRA adapter fine-tuning, allowing developers to integrate these capabilities with a few lines of code. The latest advancements in Apple Intelligence models are grounded in our Responsible AI approach with safeguards like content filtering and locale-specific evaluation, as well as our commitment to protecting our users’ privacy with innovations like Private Cloud Compute.

This paper provides technical details for Updates to Apple's On-Device and Server Foundation Language Models, introduced on June 9, 2025, in thispost.

## Related readings and updates.

### Apple Intelligence Foundation Language Models

July 29, 2024|research areaSpeech and Natural Language Processing

We present foundation language models developed to power Apple Intelligence features, including a ∼3 billion parameter model designed to run efficiently on devices and a large server-based language model designed for Private Cloud Compute. These models are designed to perform a wide range of tasks efficiently, accurately, and responsibly. This report describes the model architecture, the data used to train the model, the training process, how the…
Read more

### Introducing Apple’s On-Device and Server Foundation Models

June 10, 2024

At the 2024Worldwide Developers Conference, we introduced Apple Intelligence, a personal intelligence system integrated deeply into iOS 18, iPadOS 18, and macOS Sequoia.

Apple Intelligence is comprised of multiple highly-capable generative models that are specialized for our users’ everyday tasks, and can adapt on the fly for their current activity. The foundation models built into Apple Intelligence have been fine-tuned for user experiences such as writing and refining text, prioritizing and summarizing notifications, creating playful images for conversations with family and friends, and taking in-app actions to simplify interactions across apps.

Read more

## Discover opportunities in Machine Learning.

Our research in machine learning breaks new ground every day.

Work with us
