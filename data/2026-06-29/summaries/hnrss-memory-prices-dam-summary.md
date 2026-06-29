---
title: Memory Prices | DAM
url: https://dam.stanford.edu/memory-prices.html
date: 2026-06-28
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-06-29T19:23:43.825349
---

# Memory Prices | DAM

# Memory Prices | DAM – Summary

## Overview
- Interactive collection of historic and current memory and storage prices, inspired by John C. McCallum’s classic dataset.  
- Raw data downloadable as CSV.

## Price per gigabyte over time
- Log‑scale chart shows the lowest recorded $/GB for three memory types: DRAM, NAND flash, and HBM.

## DRAM price by generation
- DRAM line split by generation across the full history:  
  - Pre‑DDR (SDRAM/core)  
  - DDR, DDR2, DDR3, DDR4, DDR5  
- Generation inferred from product descriptions; older points are approximate.

## Accelerator cost breakdown
- Quarterly accelerator cost estimates from Epoch AI for the four largest AI‑accelerator designers (Nvidia, AMD, Google TPU, Amazon Trainium).  
- Costs stacked by component: HBM, logic die, packaging/CoWoS, auxiliary.  
- Presented as absolute dollars ( $ B / quarter) and share percentages.

## HBM price by generation
- Prices per GB and per TB/s of bandwidth for HBM generations: HBM2e → HBM3 → HBM3e → HBM4 (projected launch Q3 2026).  
- Based on sparse industry‑analyst estimates (TrendForce, SemiAnalysis); no public spot market exists.

## Methodology note
- $/GB reflects the cheapest listed retail price in nominal USD, not contract, average, or inflation‑adjusted prices.  
- **DRAM**: McCallum dataset (1957‑2024) plus Keepa Amazon prices (mid‑2024 onward).  
- **NAND**: Keepa cheapest consumer NVMe SSD price (2016‑present); earlier years use approximate anchor points.  
- **HBM**: Modeled estimates from Epoch AI and analyst reports.

## Sources and reliability
| Category | What is tracked | Source & method | Reliability |
|----------|----------------|----------------|-------------|
| DRAM $/GB | Cheapest retail $/GB overall and by generation | McCallum dataset (1957‑2024) + Keepa Amazon price history (mid‑2024 onward) | Reference + live |
| NAND $/GB | Cheapest retail SSD $/GB (2010‑present) | Keepa cheapest consumer NVMe SSD (2016‑present); pre‑2016 anchor points | Live + approximate |
| HBM spend & cost breakdown | Quarterly HBM spend ($B) and component share (%) | Epoch AI modeled estimate, production‑volume‑weighted across Nvidia, AMD, Google, Amazon | External estimate |
| HBM $/GB & $/TBps | Price per GB and per bandwidth unit by generation | TrendForce & SemiAnalysis analyst estimates; bandwidth from JEDEC/Rambus | Sparse estimate |

## Caveats
- Prices are the cheapest listed retail values in nominal USD; they do not represent contract or average pricing and may lag contract prices.  
- Cheapest listings often correspond to end‑of‑life clearance rather than leading‑edge products; per‑generation chart highlights this effect.  
- Data are based on listings, not confirmed sales; obvious posting errors are filtered out (e.g., listings >60 % below typical price are dropped).  
- HBM figures are modeled estimates, not measured market prices.

## Updates
- DRAM and NAND $/GB refreshed monthly from Keepa.  
- HBM data refreshed quarterly (Epoch AI).  
- The McCallum backbone and HBM generation estimates remain fixed.  
- The downloadable CSV includes every data point with its source.

## Contact
Compiled and maintained by David Shim, Stanford DAM project.  
Questions or corrections: hsshim@stanford.edu