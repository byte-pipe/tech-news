---
title: GitHub - FlashML-org/FreeToken: FreeToken brings datacenter-scale model serving to your desktop. Run massive models locally, fast and efficiently. · G...
url: https://github.com/FlashML-org/FreeToken
date: 
site: github
model: llama3.2:1b
summarized_at: 2026-09-21T16:55:07.266180
---

# GitHub - FlashML-org/FreeToken: FreeToken brings datacenter-scale model serving to your desktop. Run massive models locally, fast and efficiently. · G...

**FreeToken Overview**
====================

FreeToken is an edge-native mixture-of-experts (MoE) serving engine designed for running frontier-scale open-weight models on personal and consumer hardware. It provides fast, efficient MoE serving with bandwidth-adaptive CPU-GPU co-execution, semantic-aware caching, and elastic memory management.

**Key Features**
================

*   Fast Edge-Native Runtime with bandwidth-adaptive CPU-GPU co-execution ($q^\star$ policy)
*   Semantic-aware caching with semantic anchor checkpoints for recurrent state and KV caches
*   Elastic memory management with dynamic, runtime VRAM re-allocation
*   Broad MoE and ecosystem support with Anthropic/OpenAI-compatible APIs

**Getting Started**
================-----

### Desktop app

*   Download FreeToken for Windows or Linux at `https://github.com/FlashML-org/FreeToken`.
*   Set up the engine using the GUI.

### CLI

*   Install FreeToken with `uv` (recommended) or `pip`.
*   Run the command `freetoken[accel]` to set up the engine.
*   Alternatively, install from source and activate the virtual environment.

**Supported Hardware**
================--------

*   Consumer laptops
*   Gaming desktops
*   Workstation GPUs, including NVIDIA RTX 30-50 series
*   Anthropic/OpenAI-compatible APIs for seamless integration with real-world coding and tool-calling agents.