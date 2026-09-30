---
title: DeepSeek Builds for Huawei Ascend - Geopolitechs
url: https://www.geopolitechs.org/p/deepseek-builds-for-huawei-ascend
site_name: tldr
content_file: tldr-deepseek-builds-for-huawei-ascend-geopolitechs
fetched_at: '2026-09-30T22:51:00.885447'
original_url: https://www.geopolitechs.org/p/deepseek-builds-for-huawei-ascend
author: Geopolitechs
date: '2026-09-30'
description: Today, DeepSeek posted a short but potentially significant announcement on its official Chinese WeChat account.
tags:
- tldr
---

# DeepSeek Builds for Huawei Ascend

Geopolitechs
Sep 30, 2026
8
1
2
Share

Today, DeepSeek posted a short but potentially significant announcement on its official Chinese WeChat account.

Put simply, one of the biggest questions facing China’s AI industry has been: what do you do if you can no longer get access to NVIDIA’s most advanced GPUs? DeepSeek is now offering part of an answer. And the answer is not simply to replace NVIDIA GPUs with Huawei Ascend chips. It is also starting to rebuild one of the hardest things to replace: the software ecosystem around NVIDIA’s hardware, so that Chinese chips become genuinely easier to use and capable of training frontier AI models.

NVIDIA’s real strength in large-model training has never been just the GPUs themselves. It is also the entire software ecosystem built around them, particularly CUDA. Once you have NVIDIA GPUs, developers have a mature set of tools for writing programs, optimizing performance and getting thousands of GPUs to work together efficiently.

This has been one of the major challenges for Huawei Ascend. Building capable hardware is only part of the problem. Just as important is whether the software is easy to use and whether developers can efficiently extract the full performance of the chips.

This is the layer DeepSeek is now trying to fill in. It has developed Ascend versions of a whole set of low-level tools, including TileLang, DeepGEMM, DeepEP and FlashMLA.

In simple terms, TileLang is a high-level language that makes it easier for developers to tell the chips what to do. DeepGEMM handles the matrix operations at the heart of large-model computation. DeepEP deals with high-speed communication between large numbers of chips during training. FlashMLA and other components handle tasks such as attention and data processing.

DeepSeek says that, in a number of key tests, the compute and communication performance of these components is already approaching the limits of the Ascend hardware itself.

TileLang is probably the most interesting part. DeepSeek says that most of the operators used to train its V4 models are now implemented in TileLang, and that every TileLang operator currently used in DeepSeek training now has a corresponding high-performance implementation on Ascend.

What DeepSeek appears to be trying to do is create a layer of abstraction between the model and the underlying GPU hardware. The same development approach could potentially sit on top of either NVIDIA GPUs or Huawei Ascend chips. If this works well, the cost and difficulty of moving AI workloads from NVIDIA to Chinese AI hardware could fall significantly.

There is another important signal in the announcement: DeepSeek makes clear that it did not do this alone. Huawei’s team was deeply involved in the development. The two companies are also jointly working on a 128-card supernode based on Ascend 950, while carrying out deep optimization of both computation and inter-chip communication.

So this is no longer simply a case of “DeepSeek now supports Huawei chips.” DeepSeek and Huawei are working together on the much deeper problem of how to make Chinese hardware and software work efficiently together for frontier model training.

#### DeepSeek Open-Sources Core Infrastructure Components for Huawei Ascend

Today, we are officially open-sourcing a set of foundational infrastructure components for Huawei’s Ascend computing platform, covering the TileLang high-level language and compiler toolchain, compute libraries, and distributed communication libraries. Each of these components has a direct counterpart among the components we previously open-sourced for NVIDIA platforms.

Good tools are essential to good work. To build a new generation of independent and controllable GPU software ecosystems, the first priority is to develop a high-level language that is general-purpose, easy to program, and capable of pushing hardware performance to its limits.

TileLang was born out of this need.

Compared with NVIDIA’s CUDA, TileLang offers a simpler programming model that can significantly improve development efficiency and simplify code logic. Compared with other high-level languages of its kind, TileLang’s programming model is also designed to fully exploit the characteristics of the underlying chips and reach their hardware performance limits.

We first validated the TileLang approach on NVIDIA’s mature platform. Today, TileLang is used to implement the majority of operators in the training of the DeepSeek V4 family of models, and has become a core tool for our exploration of new AGI paradigms and development of high-performance operators.

The Ascend version of TileLang released today wraps the underlying Ascend C instructions and provides a high-level programming interface without sacrificing hardware performance. This is exactly what TileLang was originally designed to achieve. Every TileLang operator currently used in DeepSeek training now has a corresponding high-performance implementation on Ascend.

By open-sourcing TileLang for Ascend, we also hope to provide a useful reference for building highly usable software ecosystems around a broader range of AI chips.

Today’s release also includes core compute and communication components for the Ascend platform, providing reusable foundational capabilities for different workloads. DeepGEMM accelerates general matrix operations; DeepEP provides efficient large-scale cross-device communication; TileKernels provides commonly used vector computation and memory-access operators for data processing; FlashMLA provides sparse attention operators to improve long-context processing efficiency; and DeepSelect enables efficient data selection.

Across a number of key test cases, the compute and communication performance of these components is already approaching the limits of the underlying hardware.

Throughout our development work for the Ascend platform, Huawei’s team has provided strong and wholehearted support. Our teams have worked closely together on a 128-card supernode solution based on Ascend 950, while jointly carrying out deep optimization of both computation and communication.

We will continue to push forward technological innovation, work with the community to build an open software ecosystem, and make progress together.

Open-source projects:

TileLang:https://github.com/tile-ai/tilelang

DeepGEMM Ascend:https://github.com/deepseek-ai/DeepGEMM-Ascend

DeepEP Ascend:https://github.com/deepseek-ai/DeepEP-Ascend

TileKernels:https://github.com/deepseek-ai/TileKernels

FlashMLA:https://github.com/deepseek-ai/FlashMLA

DeepSelect:https://github.com/deepseek-ai/DeepSelect

8
1
2
Share
Previous