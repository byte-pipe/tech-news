---
title: 1.5 TB of VRAM on Mac Studio - RDMA over Thunderbolt 5 | Jeff Geerling
url: https://www.jeffgeerling.com/blog/2025/15-tb-vram-on-mac-studio-rdma-over-thunderbolt-5
date: 2025-12-18
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-12-20T11:11:19.380029
screenshot: hackernews_api-1-5-tb-of-vram-on-mac-studio-rdma-over-thunderbolt.png
---

# 1.5 TB of VRAM on Mac Studio - RDMA over Thunderbolt 5 | Jeff Geerling

## 1.5 TB of VRAM on Mac Studio - RDMA over Thunderbolt 5

The author reviews Apple's M3 Ultra Mac Studio with RDMA support and compares it to Nvidia DGX Spark AMD AI Max+ 395 systems in various HPC applications.

### Introduction
Apple provides access to the M3 Ultra Mac Studio for testing a new feature called Direct Rendezvous and Memory Access (RDMA) over Thunderbolt 5. The author evaluates this cluster's performance using open-source clustering tool Exo 1.0.

## Cluster Configuration
The author tests different configurations:

- A 4-post rack with 1.5 TB unified memory (512 GB) in the Mac Studio
- Two lower-end models ($11,699 each) each having 512 GB of unified memory and 32 CPU cores
- One higher-end model at a reduced power consumption cost

## Comparisons to Other Solutions
The author mentions competitor systems:

* Nvidia DGX Spark: A more expensive option (lowering VRAM by four times)
* AMD AI Max+: Lowered VRAM to four GB while increasing compute cores
