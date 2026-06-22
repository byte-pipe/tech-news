---
title: Moebius Project Page
url: https://hustvl.github.io/Moebius/
site_name: hnrss
content_file: hnrss-moebius-project-page
fetched_at: '2026-06-22T20:05:47.712447'
original_url: https://hustvl.github.io/Moebius/
date: '2026-06-22'
description: 'Moebius: 0.2B Lightweight Image Inpainting Framework with 10B-Level Performance'
tags:
- hackernews
- hnrss
---

While 10B-level industrial foundation models have pushed the boundaries of image inpainting, their prohibitive computational costs severely hinder practical deployment. Constructing a highly optimized task-specific specialist offers a promising solution; however, extreme structural compression inevitably triggers a severe representation bottleneck. To conquer this, we propose Moebius, a highly efficient lightweight inpainting framework. We systematically reconstruct the diffusion backbone by introducing the Local-λ Mix Interaction (LλMI) block. Comprising Local-λ and Interactive-λ modules, it elegantly summarizes spatial contexts and global semantic priors into fixed-size linear matrices, preserving complex latent interactions while drastically shedding parameters. Furthermore, to unlock the full representational capacity of this highly compact architecture, we synergistically pair it with an adaptive multi-granularity distillation strategy. Operating strictly within the latent space to avoid expensive pixel-space decoding, this strategy dynamically balances multiple gradient-based losses to achieve high-fidelity alignment. Extensive experiments across natural and portrait benchmarks demonstrate that this optimal synergy enables Moebius to rival or even surpass the generation quality of the 10B-level industrial generalist FLUX.1-Fill-Dev. Remarkably, Moebius achieves this using less than 2\% of the parameters (0.22B vs. 11.9B) while delivering a >15× acceleration in total inference time, setting a new efficiency standard for high-fidelity inpainting.