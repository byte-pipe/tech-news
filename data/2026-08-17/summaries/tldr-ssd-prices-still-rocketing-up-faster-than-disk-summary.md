---
title: SSD prices still rocketing up faster than disk
url: https://www.theregister.com/flash/2026/08/11/ssd-prices-still-rocketing-up-faster-than-disk/5286189
date: 2026-08-17
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-08-17T08:44:47.377629
---

# SSD prices still rocketing up faster than disk

# SSD prices still rocketing up faster than disk

## Overview
- Article by Chris Mellor, Storage Editor, published 11 Aug 2026.
- Reports a continued sharp rise in SSD prices compared with HDDs, based on VDURA’s Flash Volatility Index.

## Price trends (July 2026)
- SSD prices increased 5 % month‑over‑month.
- 30 TB TLC enterprise SSDs: $22,600 (up from $3,460 in Q3 2025).
- 30 TB QLC SSDs: $18,080 (up from $2,768 a year ago).
- 30 TB HDDs: $1,216 (up from $495 a year ago).
- Price multiple SSD/HDD:
  - TLC vs HDD: 18.6 × (down from 23.2 × in Q1 2026, still ≈3 × the level a year ago).
  - QLC vs HDD: similar trajectory.

## Cost impact on AI‑focused storage architectures
- VDURA’s Storage Economics Optimizer models a 25 PB deployment delivering 1,000 GB/s sustained read for ~2,000 GPUs.
- 3‑year total cost estimates:
  - All‑flash with 30 TB TLC SSDs: $51.60 M.
  - All‑flash with 30 TB QLC SSDs: $48.42 M.
  - Hybrid SSD+HDD (5.78 PB flash, 22.68 PB HDD) in a single namespace: $12.86 M.
- Mixed‑fleet system provides 1,040 GB/s sustained performance while costing roughly one‑quarter of an all‑flash solution.

## Financial perspective
- Erik Salo (VDURA SVP) states flash pricing has stabilized at a higher level, breaking assumptions behind many all‑flash designs.
- Storage architecture is now a major financial decision in AI infrastructure, second only to GPU costs.
- “Cost per token” is highlighted as the key metric; storage choices significantly affect it.

## Tools and resources
- Flash Volatility Index and Storage Economics Optimizer Tool are available from VDURA (links provided in the original article).
- Supporting technical analysis accompanies the tools.

## Related headlines (selected)
- Hitachi Vantara storage sales rise.
- Dell announces 200 PB rack storage block.
- SK Hynix expands Solidigm NAND plant in Dalian.
- Various AI/ML, HCI, and tape news items listed in the article’s ticker.