---
title: "A GPU-Hour Isn't a Commodity If You Need Four of Them"
url: https://davefriedman.substack.com/p/a-gpu-hour-isnt-a-commodity-if-you
date: 2026-07-27
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-07-27T06:52:33.709192
---

# A GPU-Hour Isn't a Commodity If You Need Four of Them

# A GPU-Hour Isn't a Commodity If You Need Four of Them

## Overview
- Survey of GPU rental prices on Vast.ai shows headline rates (e.g., $3.93 per H200 GPU‑hour) mask scarcity for multi‑GPU configurations.  
- Real workloads often require several identical GPUs in the same machine with proper interconnect and reliability, which the market does not always provide.

## Methodology
- Filtered on‑demand offers to those verified, rentable for ≥7 days, and with ≥99 % reliability.  
- Covered five accelerator models: A100 SXM4, H100 SXM, H200, B200, L40S.  
- Deduplicated by physical machine, yielding 37 machines and 93 GPUs.  
- Determined supply and median price of the three cheapest eligible machines for 1, 2, 4, and 8 GPU requests.

## Key Findings
- **Supply drops sharply with larger cluster sizes** while prices often stay flat until the configuration disappears.  
  - H200: 92 % of inventory remains for 2 GPUs, 50 % for 4 GPUs, price rises only 4 % (from $3.93 to $4.08); no 8‑GPU offers.  
  - H100 and B200: support up to 2 GPUs, zero supply for 4 or 8 GPUs.  
  - A100: price doubles from $0.60 to $1.29 per GPU‑hour when moving from 1 to 8 GPUs (114 % premium).  
  - L40S: only 35 % of inventory can meet an 8‑GPU request, but the single qualifying machine is cheap.
- **Configuration, not price, is the primary rationing mechanism.** Constraints include GPU generation, co‑location, networking, reliability, reservation length, CPU, storage, and geography.

## Market Implications
- Indexes based on 1‑ or 2‑GPU rentals suggest abundant, stable pricing, yet large‑scale buyers cannot assemble required clusters at any price.  
- Large buyers therefore prefer bilateral capacity agreements that lock in specific configurations.  
- Excess capacity from such contracts feeds the spot marketplaces.

## Implications for Compute Derivatives
- Initial compute futures will likely use standardized GPU‑hour benchmarks, exposing buyers to basis risk when they need multi‑GPU clusters.  
- Analogous to energy markets, future contracts may add premiums or separate contracts for topology, cluster size, interconnect quality, region, and availability guarantees.  
- Cluster‑hour and capacity options could become more actively traded than base GPU‑hour contracts.

## Limitations of the Sample
- Data comes from a single marketplace (Vast.ai) and reflects advertised offers, not completed transactions.  
- Larger‑cluster estimates rely on a few machines; precise premiums should be treated cautiously.  
- Findings are robust across reliability thresholds (98 %–99.5 %).  
- The sample illustrates how a seemingly liquid market for individual GPU‑hours can hide a near‑empty market for specific usable configurations.