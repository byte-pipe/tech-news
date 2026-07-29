---
title: Kimi K3 Architecture Notes | Sebastian Raschka, PhD
url: https://sebastianraschka.com/blog/2026/kimi-k3-architecture-notes.html
date: 2026-07-29
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-07-29T12:32:36.077287
---

# Kimi K3 Architecture Notes | Sebastian Raschka, PhD

# Kimi K3 Architecture Notes

## Overview
- The Kimi K3 model is a scaled‑up production version of the previous Kimi Linear model, expanding from 48 B to 2.8 T parameters, making it the largest open‑weight model released to date.  
- The only new architectural component compared to Kimi Linear is the **LatentMoE**, which is the same as the LatentMoE used in Nemotron 3 Ultra and serves to compress (down‑project) large linear layers similarly to multi‑head latent attention.

## Efficiency‑Focused Changes
- The overall design follows a trend toward better inference efficiency, seen in models like Nemotron 3 and DeepSeek V4.  
- Several components are replaced with efficiency‑tuned versions:  
  - MoE → LatentMoE  
  - Regular attention → multi‑head latent attention and Kimi Delta Attention  
- **Attention residuals** improve the residual path by connecting residuals across layers with attention‑based weighting. This yields consistent improvements in validation loss and downstream performance, at the cost of about 4 % more training compute and 2 % more inference compute.

## Positional Embedding Strategy
- All RoPE (Rotary Positional Embedding) layers are removed; the model uses **NoPE** (no positional embeddings) everywhere, a design inherited from Kimi Linear.  
- This contrasts with the recent trend of mixing RoPE in local attention layers and NoPE in global layers; Kimi K3 is the first frontier‑level model to adopt NoPE universally.

## Multimodal Support
- Kimi K3 now includes native multimodal capabilities.

## Additional Remarks
- The technical report contains further training details not covered here.  
- Figure 1 (referenced in the note) shows the Kimi K3 architecture and benchmark comparisons; more details are available in the architecture gallery.

## Related Reads
- “A Few Notable Open‑Weight Models This Week” – brief overviews of six new open‑weight models.  
- Correction for Listing 6.5 in *Build a Reasoning Model From Scratch*.  
- “Inkling: A New Open‑Weight 975B MoE with a Few Surprises” – summary of the Inkling model’s design and benchmarks.