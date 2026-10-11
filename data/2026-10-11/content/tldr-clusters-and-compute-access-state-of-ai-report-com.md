---
title: Clusters and compute access | State of AI Report Compute Index
url: https://www.stateof.ai/compute-explore/clusters-and-access
site_name: tldr
content_file: tldr-clusters-and-compute-access-state-of-ai-report-com
fetched_at: '2026-10-11T16:32:59.114627'
original_url: https://www.stateof.ai/compute-explore/clusters-and-access
author: Nathan Benaich
date: '2026-10-11'
description: The largest reported clusters, frontier-lab compute access, and the power and networks that support them.
tags:
- tldr
---

# Clusters and compute access

By Nathan Benaich (Air Street Capital)

The largest reported clusters, frontier-lab compute access, and the power and networks that support them.

## Questions in this topic

Who has the largest GPU cluster in this index?
How many GPUs do OpenAI and Anthropic have?
How many GPUs does Europe’s JUPITER supercomputer have?
What is a GPU cluster, and how is it different from a fleet?
How much power does a GPU cluster need?
Why does networking matter in a GPU cluster?

## Questions and answers

Index cutoff · October 1, 2026

### Who has the largest GPU cluster in this index?

SpaceXAI’s Colossus 2 has the largest deployed entry, with 550,000 GB200/GB300 GPUs. Its additional 440,000 announced GPUs are excluded from that deployed count.

The count is based on the operator’s reported figures, not an independent hardware audit. The index is a selected inventory; its rows include both individual clusters and combined fleets, and chip counts do not measure usable computing performance.

Grace-Blackwell chart·Count and source notes·Operator’s September 25 post

Read this answer 

Index cutoff · October 1, 2026

### How many GPUs do OpenAI and Anthropic have?

This index does not establish a complete GPU total for either lab. Anthropic has disclosed access to more than 220,000 NVIDIA GPUs through its Colossus agreement, but access to a partner’s cluster is not ownership or a complete inventory.

A gigawatt measures power capacity and cannot be converted into a reliable chip count without knowing the hardware and facility assumptions. The lab chart mixes existing access, future commitments, “up to” ceilings, and OpenAI’s NVIDIA letter of intent; it is not a measure of capacity operating today.

Frontier-lab compute chart·Deal-by-deal sources·Anthropic’s Colossus agreement

Read this answer 

Index cutoff · October 1, 2026

### How many GPUs does Europe’s JUPITER supercomputer have?

The index records 23,536 deployed GH200 GPUs in JUPITER’s Booster module at Jülich. The operator specifies 5,884 compute nodes, each with four Grace-Hopper Superchips, matching that count.

This counts the GPUs in the Booster’s standard compute nodes, not every processor or login node in the wider system. A GPU inventory is also different from a supercomputer performance ranking such as TOP500.

Hopper cluster chart·Jülich hardware configuration

Read this answer 

Reading the inventory

### What is a GPU cluster, and how is it different from a fleet?

A GPU cluster connects GPU-equipped servers so workloads can use multiple machines together. A GPU fleet is an inventory that can span several clusters or locations; it does not necessarily form one interconnected system.

The index includes both individual clusters and aggregate fleet entries, as identified in the row labels and sources. Compare the same scope and deployment status. GPU generation, memory, networking, and workload also affect performance, so twice as many GPUs does not automatically mean twice as much useful compute.

Cluster inventory·Scope and source notes·NVIDIA cluster networking

Read this answer 

Engineering illustration · reviewed October 11, 2026

### How much power does a GPU cluster need?

Power requirements depend on the GPUs, server design, networking, storage, cooling, and workload. NVIDIA specifies a maximum system power of 10.2 kW for an eight-GPU DGX H100. As an illustration, 1,000 H100 GPUs in 125 of those systems would have a combined maximum server power of 1.275 MW. That excludes external networking, storage, and facility overhead such as cooling; it is not a measurement of a particular cluster’s electricity use.

Maximum rated power is different from average consumption. Megawatts measure power at a point in time; megawatt-hours measure energy over a period. A system drawing 1 MW continuously for one hour uses 1 MWh. GPU power ratings alone do not describe the whole facility, and an announced gigawatt of future site capacity is not proof of installed chips. This index does not meter electricity use, so its GPU counts cannot establish a global AI power total or a universal conversion between gigawatts and GPUs.

NVIDIA DGX H100/H200 system and power specifications·Compute inventory and scope

Read this answer 

Architecture explanation · reviewed October 11, 2026

### Why does networking matter in a GPU cluster?

Large AI workloads can split a model or its data across many GPUs. Those GPUs must exchange intermediate results and synchronize their work, so slow communication can leave computing capacity waiting. The network’s bandwidth, latency, and topology therefore affect how efficiently a job uses a cluster. Adding GPUs does not guarantee a proportional increase in useful performance.

NVIDIA distinguishes scale-up communication within a GB200 NVL72 rack, using NVLink, from scale-out connections between racks, using Ethernet or InfiniBand. Storage networking also matters because the GPUs need a steady supply of data. These are different parts of the system, not interchangeable specifications. The index counts hardware; it does not benchmark each cluster’s interconnect, storage throughput, or performance on the same training job. Compare those details before treating two equal-sized GPU clusters as equivalent.

NVIDIA data-center network architecture·Cluster inventory·Inventory sources

Read this answer 

## Charts and sources

1. Grace-Blackwell chart
2. Count and source notes
3. Operator’s September 25 post
4. Frontier-lab compute chart
5. Deal-by-deal sources
6. Anthropic’s Colossus agreement
7. Hopper cluster chart
8. Jülich hardware configuration
9. Cluster inventory
10. Scope and source notes
11. NVIDIA cluster networking
12. NVIDIA DGX H100/H200 system and power specifications
13. Compute inventory and scope
14. NVIDIA data-center network architecture
15. Inventory sources

Citation estimates use inputs through September 1, 2026; fleet counts have an October 1, 2026 cutoff. The research-topic sample covers January 1 to June 1, 2025. See each answer for its period and limitations.

All data sources