---
title: Kimi K3 Architecture Notes | Sebastian Raschka, PhD
url: https://sebastianraschka.com/blog/2026/kimi-k3-architecture-notes.html
site_name: hackernews_api
content_file: hackernews_api-kimi-k3-architecture-notes-sebastian-raschka-phd
fetched_at: '2026-07-29T12:28:27.695831'
original_url: https://sebastianraschka.com/blog/2026/kimi-k3-architecture-notes.html
author: Sebastian Raschka
date: '2026-07-29'
published_date: '2026-07-28T08:38:20+00:00'
description: Short architecture note on Kimi K3, including LatentMoE, Kimi Delta Attention, Attention Residuals, NoPE, multimodality, and inference-efficiency choices.
tags:
- hackernews
- trending
---

The Kimi K3 architecture figure for yesterday’s big open-weight model release, along with some observations and thoughts.

1. Yes, it looks relatively complicated, but it’s essentially a scaled-up production version of theirKimi Linear modelthey released last year (scaled up from 48B -> 2.8T; K3 is by far the biggest open-weight model right now)
2. The one new component compared to Kimi Linear is theLatentMoE. I omitted it in the figure below since it’s already very crowded, but that’s essentially the same LatentMoE as in Nemotron 3 Ultra (you can find it in myLLM Architecture Galleryif you are curious). The idea here is to compress (down-project) large linear layers similar tomulti-head latent attention.
3. Kimi K3’s overall trend (similar to Nemotron 3, DeepSeek V4, and others) is also towards better inference efficiency. That is, there are many components that replace existing components with efficiency-tweaked versions. I.e.,MoE-> LatentMoE, regular attention -> multi-head latent attention andKimi Delta Attention. (I also have short tutorials and write-ups in mygalleryif you are curious about additional details).
4. The one component change that is not an efficiency tweak isattention residuals. Like DeepSeek V4 improved the residual path with mHC (manifold-constrained Hyper-Connections), attention residuals are a way to improve the residual path, but it works a bit differently. I.e., mHC made the residual path wider. Attention residuals (also already part of Kimi Linear) connect the residuals across layers; the connection itself uses an attention score for an important/contribution weight. According to the report, it improves the validation loss and downstream performance (a bit) consistently and adds about 4% in training cost and 2% in inference cost.
5. Interestingly, Kimi K3 got rid of all RoPE layers and usesNoPE(No Positional Embeddings) everywhere instead. (Again, this is inherited from Kimi Linear). In other architectures, the recent trend was towards RoPE in local attention layers (likesliding window attention) and NoPE in the global layers. There were a few architectures that only used NoPE everywhere, but this is the first frontier-level one as far as I know.
6. Kimi K3 now also has native multimodal support, which is great!

There are several other interesting training tidbits in the technical report, but that’s it from the architecture front so far. A really great release overall.

Figure 1. Kimi K3 architecture and release-time benchmark comparisons. See 
K3
 in the architecture gallery for more details.

Source: website version of mySubstack note.

## Read Next

A Few Notable Open-Weight Models This Week

Short note on the architectures of six new open-weight models, including Nanbeige 4.2, Laguna S 2.1, Motif-3-Beta, Solar Open 2, Antares 1B, and BTL-3.

Correction for Listing 6.5 in Build a Reasoning Model From Scratch

Short correction note for the random seed in Listing 6.5 on page 198 of Build a Reasoning Model From Scratch.

Inkling: A New Open-Weight 975B MoE with a Few Surprises

Short note on Thinking Machines Lab's 975B Inkling model, including benchmarks, sparse MoE design, short convolutions, RMSNorm, and position bias.

RSS

Subscribe via Email