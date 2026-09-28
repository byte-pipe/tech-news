---
title: How NVIDIA DSX MaxLPS Maximizes AI Factory Throughput and Efficiency | NVIDIA Technical Blog
url: https://developer.nvidia.com/blog/how-nvidia-dsx-maxlps-maximizes-ai-factory-throughput-and-efficiency
site_name: tldr
content_file: tldr-how-nvidia-dsx-maxlps-maximizes-ai-factory-through
fetched_at: '2026-09-28T13:22:35.588610'
original_url: https://developer.nvidia.com/blog/how-nvidia-dsx-maxlps-maximizes-ai-factory-throughput-and-efficiency
date: '2026-09-28'
published_date: '2026-09-28T01:00:00+00:00'
description: Every unused watt is capacity left on the table. AI factories are typically provisioned for the unlikely moment when every GPU reaches peak power…
tags:
- tldr
---

Data Center / Cloud

# How NVIDIA DSX MaxLPS Maximizes AI Factory Throughput and Efficiency

 Sep 27, 2026
 

 By 
Sarah McKenney
 and 
Harry Petty
 

 
 

 Like

* L
* T
* F
* R
* E
 

## AI-Generated Summary

* NVIDIA DSX MaxLPSuses policy-governed power sharing to dynamically allocate power across participating resources, enabling up to 40% more GPUs within the same approved power budget.
* A joint NVIDIA and Nscale evaluation ran Kimi K2.5 workloads on NVIDIA GB300 NVL72 systems at Nscale's Verne campus in Keflavík, Iceland, comparing a static baseline of 140 GPUs with a DSX MaxLPS configuration of 192 GPUs under the same 264.4 kW provisioned power budget.
* DSX MaxLPS increased normalized aggregate throughput by 49.2% and throughput per provisioned watt from 4.10 to 6.12 tokens/s/W, while per-instance throughput for high-throughput and low-latency workloads remained effectively unchanged.
* Median and P75 latency stayed within 5% of baseline, but P99 time to first token increased 17%, highlighting the need to evaluate tail latency alongside capacity gains.
* Operators can validate DSX MaxLPS using a five-stage process: define the managed boundary, establish a representative baseline, introduce policies conservatively, add capacity incrementally with testing at each stage, and set production operating limits only when all objectives are met.

### Next Steps

* ReviewNVIDIA DSX MaxLPSto understand the framework for turning workload variability into managed capacity.
* ReadNVIDIA Dynamic Power Software documentationfor the control layer that enables policy-governed power allocation.
 

Powered by NVIDIA Nemotron. AI-generated content may summarize information incompletely. Verify important information. 
Learn more

Every unused watt is capacity left on the table. AI factories are typically provisioned for the unlikely moment when every GPU reaches peak power, creating a protective buffer that can leave valuable infrastructure underused during normal operation. NVIDIA DSX MaxLPS uses policy-governed power sharing to allocate power across participating resources dynamically, enabling customers to deploy up to 40% more GPUs within the same approved power budget.

This technical walkthrough examines a joint NVIDIA and Nscale evaluation of this approach with Kimi K2.5 workloads running on NVIDIA GB300 NVL72 systems at Nscale’s data center at the Verne campus in Keflavík, Iceland, powered entirely by renewable energy. It covers the measured trade-offs between power and performance, explains the controls used to maintain electrical limits, and presents a repeatable validation method operators can use before deploying at scale.

## How static provisioning leaves usable power stranded

An AI factory operates within a hierarchy of electrical limits. Utility service, substations, power-distribution equipment, racks, nodes, and GPUs all impose constraints. Operators must keep each managed boundary within its approved limit while meeting application throughput and latency objectives.

Static power planning typically reserves enough power for every node to reach its specified peak at the same time. This conservative approach is straightforward, but AI workloads rarely draw constant power. Training workloads move through compute, communication, synchronization, and checkpointing. Inference workloads alternate among prefill, decode, memory-bound work, network activity, and idle intervals. Even instances of the same model can draw different power as request shapes and concurrencies change.

This variability creates a gap between reserved peak power and actual consumption. With static per-node reservations, unused capacity inside one reservation cannot be applied to another node. The aggregate facility can remain below its limit while additional GPU capacity stays offline.

DSX MaxLPSmonitors actual power consumption and dynamically reallocates available power across participating resources while preserving the operator’s aggregate budget and policy boundaries.

Figure 1. Static MaxP can leave reserved power unused; static MaxQ can constrain performance; DSX MaxLPS dynamically reallocates power within operator-defined limits

## Inside the DSX MaxLPS control loop

DSX MaxLPS combines chip, system, thermal, and software technologies to maximize AI factory output within land, power, and shell (LPS) constraints. Dynamic Power Software provides the control layer for policy-governed power allocation.

The control process has five technical elements:

* Topology and resource groups. Operators map the participating infrastructure and organize nodes into a managed group with an aggregate power budget.
* Telemetry. The system collects GPU, node, rack, and group power telemetry at intervals sufficient to detect available headroom and emerging power events.
* Policy. Operator-defined rules establish node limits, group limits, allocation priorities, reserve requirements, and responses to maintenance or emergency events.
* Allocation and control. When some resources draw less than their allocation, the software adjusts participating GPU power limits so other resources can use the available capacity.
* Validation and enforcement. The system compares measured power against the approved group budget and adjusts allocations when consumption approaches a limit.

This is coordinated allocation, not an increase in the site’s power supply. The control loop enables more productive work beneath the same managed power budget.

## How the method was evaluated

For the evaluation, Nscale deployed the MaxLPS software in its data center and collected telemetry while NVIDIA ran the workloads. The evaluation measured control behavior and workload trade-offs.

The evaluation used NVIDIA Blackwell Ultra GPUs, Kimi K2.5 in FP4, NVIDIA Dynamo, NVIDIA TensorRT LLM, an 8K input sequence length, and a 1K output sequence length. The workload mix combined high-throughput and low-latency inference instances, creating distinct power and service profiles within the managed group.

The static baseline used 35 four-GPU nodes, or 140 GPUs. It ran two high-throughput instances using 52 GPUs each and one low-latency instance using 36 GPUs. The DSX MaxLPS configuration used 48 four-GPU nodes, or 192 GPUs. It added a third 52-GPU high-throughput instance while retaining the same 36-GPU low-latency instance.

Jobs ran across four racks, with each distributed workload confined to a single rack in both configurations. This controlled for cross-rack performance differences. Confining distributed workloads to a single rack is not required when the test environment has been validated for equivalent performance across racks.

The team measured normalized aggregate and per-instance throughput, time to first token, end-to-end latency, interactivity, GPU, CPU, and rack power telemetry. Comparing these metrics prevents a throughput gain from hiding latency, stability, or power-compliance regressions.

Figure 2. The baseline combined two 52-GPU high-throughput instances with one 36-GPU low-latency instance. DSX MaxLPS added a third 52-GPU high-throughput instance, increasing the fleet from 140 to 192 GPUs

## What the measurements show

Table 1 compares capacity, throughput, and power use for the static baseline and DSX MaxLPS configurations.

Metric
Static baseline
DSX MaxLPS
Change
Managed GPUs
140
192
+37.1%
Aggregate throughput
1,084,503 tokens/s
1,618,443 tokens/s
+49.2%
High-throughput output per instance
59,153 tokens/s
59,220 tokens/s
+0.1%
Low-latency output per instance
2,265 tokens/s
2,265 tokens/s
0%
Mean GPU power
97.0 kW
131.8 kW
+35.9%
Total measured power
166.2 kW
198.9 kW
+19.7%
Power-budget utilization
62.9%
75.2%
+12.3 percentage points
Throughput per provisioned watt
4.10 tokens/s/W
6.12 tokens/s/W
+49.2%
Table 1. Static baseline and DSX MaxLPS performance and power results

Both configurations used the same264.4 kW provisioned power budget. Throughput per provisioned watt divides normalized aggregate throughput by this fixed denominator. The baseline delivered 4.10 tokens/s/W, and DSX MaxLPS delivered 6.12 tokens/s/W, a 49.2% increase. Because the provisioned-power denominator remained unchanged, this percentage matches the aggregate-throughput increase.

The per-instance results remained effectively unchanged at the displayed precision. This shows that the larger managed fleet increased aggregate throughput without materially reducing the throughput of the existing high-throughput or low-latency instances.

For latency,P75 is the 75th-percentile result, meaning 75% of requests completed at or below that latency.P99 is the 99th-percentile result, representing tail behavior: 99% of requests completed at or below that latency, while the slowest 1% took longer. Median and P75 latency remained within 5% of baseline. P99 time to first token increased 17% from the 15.7-second baseline, showing the importance of evaluating tail latency alongside capacity and throughput.

Figure 3. DSX MaxLPS increased normalized aggregate throughput by 49.2%, from 1.085 million to 1.618 million tokens per second. With the same 264.4 kW provisioned power budget, throughput per provisioned watt increased from 4.10 to 6.12 tokens per second per watt

## Trade-offs exposed by the evaluation

Dynamic power allocation makes engineering trade-offs observable and controllable at the fleet level; it does not eliminate them.

### Workload mix shapes available headroom

DSX MaxLPS uses previously unused headroom, so added capacity still increases average power utilization. The available headroom also depends on the workload mix: complementary power profiles create more opportunity than workloads that peak simultaneously. Operators should therefore test representative production workloads against the aggregate power limit. Typical AI factories run heterogeneous workloads with different power profiles. The study therefore used a workload mix designed to reflect that variability.

### Tail latency reveals service trade-offs

Stable median latency can mask changes in tail latency. In this evaluation, median and P75 latency remained within 5% of baseline, but P99 time to first token increased by 17%. Production acceptance criteria should be defined as part of the study.

### Telemetry supports reliable control

Dynamic allocation depends on reliable telemetry. Missing, delayed, or incorrectly mapped measurements can undermine fleet-level decisions. For this evaluation, site-level telemetry was used to verify rack-level power measurements. Before deployment, operators should confirm that added throughput does not compromise service quality or compliance with power limits.

Together, these trade-offs define what operators should validate before deployment.

## How operators can validate DSX MaxLPS

Use a staged validation process with explicit boundaries and acceptance criteria.

1. Define the managed boundary.Map utility, distribution, rack, node, and GPU topology. Set the resource-group budget, reserve requirements, and escalation behavior. Confirm which measurement represents the enforceable limit.
2. Establish a representative baseline.Run the representative AI factory workload mix under static provisioning, using the intended deployment and placement rules. Measure performance and power long enough to capture workload variation and confirm repeatability.
3. Introduce policies conservatively.Begin with limits close to the validated baseline. Confirm telemetry, topology, control response, and budget compliance before adding nodes.
4. Add capacity and test each stage.Increase the managed population incrementally, comparing aggregate and per-instance performance at each step. Before proceeding, verify service behavior under peak demand, operating transitions, telemetry failure, and reduced power availability.
5. Set production operating limits.Approve a configuration only when it meets throughput and latency objectives, stays within the managed budget, preserves the required reserve, and behaves predictably during faults and transitions.

This evaluation shows how DSX MaxLPS can reclaim stranded capacity in a power-constrained AI factory. The same policy-governed approach can increase useful compute across diverse environments. Operators can tune the optimal operating point for each deployment based on hardware, workload mix, software, cooling, network topology, and service objectives.

## Plan the site for the validated operating target

Dynamic allocation is an operational capability, but the site must be able to host the capacity it enables. Electrical distribution, cooling, network fabric, floor space, and rack positions should be sized for the validated lifecycle target even if fewer racks are populated on day one.

For future NVIDIA Vera Rubin NVL72 AI factories, DSX MaxLPS also combines dynamic power management with performance-per-watt techniques and infrastructure designed for 45°C liquid-cooling inlet operation. Any Vera Rubin capacity projection should remain separate from this measured GB300 NVL72 evaluation.

DSX MaxLPS gives operators a framework for turning workload variability into managed capacity. The engineering work is to define the boundary, measure representative behavior, tune policy against service objectives, and prove compliance under both normal and adverse conditions.

ReviewNVIDIA DSX MaxLPSandNVIDIA Dynamic Power Software documentation, then use this validation sequence to establish production operating limits for your own AI factory.

 
 

 Like

## Tags

Data Center / Cloud
 | 
Energy
 | 
Blackwell
 | 
DSX
 | 
Dynamo
 | 
TensorRT-LLM
 | 
Intermediate Technical
 | 
Benchmark
 | 
GB300 NVL72
 | 
Vera Rubin
 

## About the Authors

 About Sarah McKenney
 

 
 Sarah McKenney is a senior product manager for data center platform software at NVIDIA. Previously, she was a product manager at Intel spanning networking, software, and early-stage product launches. Prior to Intel, Sarah led engineering teams building large-scale capital energy projects across North and South America. Sarah has an MBA from Rice Business School and a bachelor’s degree in Mechanical Engineering from the University of Arizona.
 
 
 

 View all posts by Sarah McKenney

 About Harry Petty
 

 
 Harry Petty is a senior technical marketing manager for HPC and AI edge applications at NVIDIA. Previously, he was a principal engineer and marketing director at Cisco Systems where he brought SDN innovations to market for hybrid cloud, multitenant security, and data center application performance. Harry has an MBA from Booth Graduate School of Business and a BS in mathematics and computer science from the University of Dayton.
 
 
 

 View all posts by Harry Petty