---
title: How NVIDIA DSX MaxLPS Maximizes AI Factory Throughput and Efficiency | NVIDIA Technical Blog
url: https://developer.nvidia.com/blog/how-nvidia-dsx-maxlps-maximizes-ai-factory-throughput-and-efficiency
date: 2026-09-28
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-09-28T13:22:56.001512
---

# How NVIDIA DSX MaxLPS Maximizes AI Factory Throughput and Efficiency | NVIDIA Technical Blog

# How NVIDIA DSX MaxLPS Maximizes AI Factory Throughput and Efficiency

## Overview
- DSX MaxLPS uses policy‑governed power sharing to reallocate unused power dynamically, enabling up to 40 % more GPUs within the same approved power budget.  
- The approach was evaluated by NVIDIA and Nscale on Kimi K2.5 workloads running on NVIDIA GB300 NVL72 systems at Nscale’s Verne campus in Keflavík, Iceland (powered entirely by renewable energy).

## Limitations of Static Provisioning
- AI factories have power limits at multiple levels: utility service, substations, distribution equipment, racks, nodes, and GPUs.  
- Traditional static planning reserves peak power for every node simultaneously, leaving large portions of capacity idle because AI workloads are bursty and rarely hit peak power at the same time.  
- Unused power in one reservation cannot be transferred to another node, capping overall GPU count despite available facility headroom.

## DSX MaxLPS Control Loop
The control process consists of five technical elements:

1. **Topology and resource groups** – Operators map infrastructure and define managed groups with aggregate power budgets.  
2. **Telemetry** – Continuous collection of GPU, node, rack, and group power data to detect headroom and emerging power events.  
3. **Policy** – Operator‑defined rules set node limits, group limits, allocation priorities, reserve requirements, and responses to maintenance or emergencies.  
4. **Allocation and control** – When some resources draw less than their allocation, the software adjusts GPU power limits so other resources can use the available capacity.  
5. **Validation and enforcement** – Measured power is compared against the approved group budget, and allocations are adjusted as consumption approaches limits.

Dynamic Power Software provides the control layer for this policy‑governed allocation, allowing more productive work under the same managed power budget without increasing the site’s power supply.

## Evaluation Methodology
- **Baseline configuration:** 35 four‑GPU nodes (140 GPUs) running two high‑throughput instances (52 GPUs each) and one low‑latency instance (36 GPUs).  
- **DSX MaxLPS configuration:** 48 four‑GPU nodes (192 GPUs) adding a third high‑throughput instance while keeping the low‑latency instance.  
- Both setups used the same provisioned power budget of 264.4 kW.  
- Workloads were confined to single racks to control for cross‑rack performance differences.  
- Measured metrics included normalized aggregate throughput, per‑instance throughput, time to first token, end‑to‑end latency (median, P75, P99), interactivity, and power telemetry.

## Key Results
| Metric | Static baseline | DSX MaxLPS | Change |
|--------|-----------------|------------|--------|
| Managed GPUs | 140 | 192 | +37.1 % |
| Aggregate throughput | 1,084,503 tokens/s | 1,618,443 tokens/s | +49.2 % |
| High‑throughput output per instance | 59,153 tokens/s | 59,220 tokens/s | +0.1 % |
| Low‑latency output per instance | 2,265 tokens/s | 2,265 tokens/s | 0 % |
| Mean GPU power | 97.0 kW | 131.8 kW | +35.9 % |
| Total measured power | 166.2 kW | 198.9 kW | +19.7 % |
| Power‑budget utilization | 62.9 % | 75.2 % | +12.3 pp |
| Throughput per provisioned watt | 4.10 tokens/s/W | 6.12 tokens/s/W | +49.2 % |

- Median and P75 latency stayed within 5 % of the baseline.  
- P99 time‑to‑first‑token increased 17 %, indicating a tail‑latency trade‑off that operators should evaluate alongside capacity gains.

## Validation Process for Operators
1. Define the managed boundary (topology, groups, budget).  
2. Establish a representative baseline performance and power profile.  
3. Introduce policies conservatively and monitor compliance.  
4. Incrementally add capacity, testing at each stage.  
5. Set production operating limits only after all objectives are met.

## Next Steps
- Review NVIDIA DSX MaxLPS documentation to understand the framework for turning workload variability into managed capacity.  
- Read the NVIDIA Dynamic Power Software guide for details on the control layer that enables policy‑governed power allocation.