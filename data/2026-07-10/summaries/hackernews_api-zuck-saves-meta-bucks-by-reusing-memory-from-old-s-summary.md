---
title: Zuck saves Meta bucks by reusing memory from old servers with a custom CXL ASIC
url: https://www.theregister.com/systems/2026/06/29/zuck-saves-meta-bucks-by-reusing-memory-from-old-servers-with-a-custom-cxl-asic/5263483
date: 2026-07-04
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-07-10T09:11:33.542499
---

# Zuck saves Meta bucks by reusing memory from old servers with a custom CXL ASIC

# Zuck saves Meta bucks by reusing memory from old servers with a custom CXL ASIC

## Overview
- Meta is reclaiming DDR4 DIMMs from de‑commissioned servers and reinstalling them in new machines that use DDR5.  
- The reclaimed memory is pooled and shared across applications via a custom Compute Express Link (CXL) ASIC called **Vistara**.  
- The approach reduces the number of servers required for certain inference workloads by up to 25 % and avoids the high cost of new RAM.

## Why the solution was needed
- About 40 % of Meta’s server fleet cannot have its memory capacity increased, limiting the ability to run memory‑intensive jobs.  
- Server hardware is typically refreshed every 3‑5 years, while DDR4 memory remains usable for 7‑10 years, creating a mismatch between server and memory lifecycles.  
- Off‑the‑shelf CXL products bundle DRAM with the controller, lack DDR4 support, consume high power, and are expensive, making them unsuitable for reusing old DIMMs.

## Vistara ASIC design
- Bridges DDR4 memory to host CPUs via a CXL 2.0/1.1‑compliant PCIe Gen5 x16 interface.  
- Each ASIC contains two independent 72‑bit DDR4 channels, supporting up to 3,200 MT/s and up to 256 GB per chip (64 GB DIMMs).  
- Driven by a pair of custom RISC‑V processors.  

## Hardware platform: MemServer
- Built around an AMD Turin processor (158 cores, 316 threads).  
- Combines 768 GB of DDR5 with 256 GB of DDR4 accessed through Vistara ASICs.  
- Vistara cards are installed in rear‑accessible slots; chassis use directed airflow and high‑capacity fans to manage thermal load.

## Software integration
- DDR4 memory appears to the operating system as a separate, CPU‑less NUMA node.  
- Meta’s workloads first consume local DDR5, then fall back to the CXL‑exposed DDR4 when needed.  
- Custom tweaks to the Linux CXL driver are either already upstream or slated for upstream inclusion.

## Workloads and benefits
- Deployed across millions of servers for:
  - Disaggregated ML inference (e.g., recommendation‑system embedding tables)  
  - Big‑data processing (Spark, Hive)  
  - Databases, distributed caches, CI/CD build systems  
- Reduces out‑of‑memory (OOM) events, cutting job‑failure and restart overhead by ~33 %.  
- Lowers infrastructure cost by up to 25 % for disaggregated inference workloads.  
- Mitigates the impact of the “RAMpocalypse” by reusing existing DDR4 stock.

## Related context
- Memory‑intensive “godboxes” and high‑RAM pricing are driving interest in CXL‑based disaggregation.  
- Industry moves include VMware’s stance on RAM prices, PCIe 7.0 drafts doubling bandwidth, and Micron’s 256 GB CXL 2.0 memory expanders.  

---  
*The article was originally published by Simon Sharwood, APAC Editor, on 29 June 2026.*