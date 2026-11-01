---
title: "Benchmarking Nvidia’s Vera CPU for the data center — standalone Vera tested against Granite Rapids-AP and EPYC Turin | Tom's Hardware"
url: https://www.tomshardware.com/pc-components/cpus/benchmarking-nvidias-vera-cpu-for-the-data-center-standalone-vera-tested-against-granite-rapids-ap-and-epyc-turin
date: 2026-11-01
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-11-01T18:53:49.046871
---

# Benchmarking Nvidia’s Vera CPU for the data center — standalone Vera tested against Granite Rapids-AP and EPYC Turin | Tom's Hardware

# Benchmarking Nvidia’s Vera CPU for the data center — standalone Vera tested against Granite Rapids‑AP and EPYC Turin

## Overview
- Nvidia’s Vera is positioned as a CPU built for the surge in agentic AI workloads in data centers.  
- Early benchmarks show strong performance in Python‑centric AI tasks and high memory bandwidth, supporting the company’s marketing claims.  
- Despite being a newcomer, Vera competes with established x86 offerings from AMD (Turin) and Intel (Granite Rapids‑AP) in both specialized and general‑purpose server workloads.

## Key Specifications
- **Cores / Threads:** 88 / 176 (Olympus core, Armv9.2‑A)  
- **Cache:** 2 MB L2 per core, 164 MB L3 per CPU  
- **Memory:** Up to 1.5 TB SOCAMM2 LPDDR5X, 9600 MT/s, up to 1.2 TB/s aggregate bandwidth (≈14 GB/s per core)  
- **PCIe:** 88 PCIe 6.4 lanes (CPU only) or 96 lanes on Vera Rubin, CXL 3.1 support, bifurcation to x2  
- **TDP:** Configurable 250 W – 450 W  
- **Interconnect:** Second‑gen Scalable Coherency Fabric (SCF) delivering up to 3.4 TB/s across the die.

## Architectural Highlights
- First Nvidia‑designed core, named **Olympus**, featuring:
  - 10‑wide decode similar to Arm’s AGI.  
  - “Spatial multithreading” delivering two threads per core.  
  - Mesh‑based SCF that distributes L3 cache and provides high intra‑die bandwidth.  
- Compared to Nvidia’s previous Grace CPU, Vera uses a custom Arm core rather than an off‑the‑shelf design, resulting in notable gains in performance, memory bandwidth, and scalability.

## Test Platforms
| Platform | CPUs Tested | Memory Configuration |
|----------|-------------|----------------------|
| 2P Nvidia MGX Vera reference | Nvidia Vera | 16 × 96 GB (1.5 TB) Samsung LPDDR5‑9600 ECC SOCAMM2 |
| 2P Supermicro SYS‑222HA | Intel Xeon 6980P (Granite Rapids‑AP) | 24 × 64 GB (1.5 TB) Micron DDR5‑8800 ECC MRDIMM |
| 2P AMD Volcano reference | AMD EPYC 9965 / 9755 (Turin) | 24 × 64 GB (1.5 TB) SK hynix DDR5‑6000 ECC RDIMM |

## Performance Highlights
- **Python / AI workloads:** Vera leads in throughput, reflecting its optimization for the Python‑heavy AI software stack.  
- **Memory‑intensive tasks:** With up to 1.2 TB/s aggregate bandwidth, Vera outpaces AMD Turin’s memory performance by more than double.  
- **General‑purpose server workloads:** Vera matches or exceeds the performance of comparable AMD and Intel chips in backend, data‑rich operations, while x86 CPUs retain an edge in frontend, core‑density‑driven tasks.  
- **Concurrency:** Vera maintains stable performance under high‑concurrency agentic workloads, benefiting from its SCF mesh and high per‑core bandwidth.

## Role in Agentic AI Workloads
- Agentic AI workloads are characterized by:
  - High concurrency: thousands of sandboxed tool calls running simultaneously.  
  - Bursty, long‑running compute patterns with periods of idle time.  
  - Heavy code compilation, graph traversal, and large database queries.  
- Vera’s architecture (high core count, strong memory subsystem, and scalable coherency) is designed to sustain performance across these bursty, concurrent workloads.  
- The CPU’s ability to handle variability and maintain throughput aligns with the needs described by industry leaders such as Google Cloud’s VP/GM of AI infrastructure.

## Conclusions
- Nvidia’s Vera demonstrates that a custom Arm‑based server CPU can compete directly with mature x86 offerings in both AI‑specific and traditional data‑center workloads.  
- Its standout memory bandwidth and strong performance in Python‑centric tasks make it a compelling option for emerging agentic AI workloads that demand high concurrency and bursty compute.  
- While x86 CPUs still lead in raw core density for certain frontend tasks, Vera’s backend performance and scalability suggest it will be a significant player as agentic AI workloads become more prevalent in data centers.