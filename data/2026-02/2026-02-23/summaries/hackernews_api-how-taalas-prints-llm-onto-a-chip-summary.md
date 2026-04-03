---
title: "How Taalas \"prints\" LLM onto a chip?"
url: https://www.anuragk.com/blog/posts/Taalas.html
date: 2026-02-22
site: hackernews_api
model: gemma3n:latest
summarized_at: 2026-02-23T06:00:49.932165
---

# How Taalas "prints" LLM onto a chip?

# How Taalas "prints" LLM onto a chip?

*   Startup Taalas has released an ASIC chip running Llama 3.1 8B (quantized to 3/6 bits) achieving an inference rate of 17,000 tokens per second, significantly faster (around 10x) than state-of-the-art GPUs.
*   Taalas's chip is a fixed-function ASIC where the model's weights are "hardwired" directly onto the silicon, similar to a CD-ROM or game cartridge, enabling high inference speeds and low power consumption (claimed to be 10x cheaper in ownership cost and 10x less electricity than GPUs).
*   Traditional GPU inference is inefficient due to the Von Neumann bottleneck, where constant data transfer between the GPU's memory (VRAM/HBM) and compute cores creates latency and high energy consumption.
*   Taalas bypasses this bottleneck by physically etching the 32 layers of the Llama 3.1 model onto the chip.
*   They have also developed a "magic multiplier" hardware scheme that allows performing multiplications using a single transistor, further enhancing speed. Data flows continuously through the chip's transistors, eliminating the need for external DRAM/HBM.
*   The chip utilizes a small amount of on-chip SRAM for the KV Cache (context window) and LoRA adapters for fine-tuning, as mixing DRAM and logic gates is costly and complex.
*   While fabricating a custom chip for each model is typically expensive, Taalas uses a base chip design with a generic grid of logic gates, requiring only customization of the top two layers/masks to map a specific model onto it.
*   The development of the Llama 3.1 8B chip took two months, which is considered fast in the AI hardware development cycle.
*   The author expresses optimism about the potential of this hardware for enabling wider access to local LLM inference, especially for users without powerful GPUs.
