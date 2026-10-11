---
title: GPU lifetime and economics | State of AI Report Compute Index
url: https://www.stateof.ai/compute-explore/gpu-lifetime
date: 2026-10-12
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-10-12T06:00:47.040784
---

# GPU lifetime and economics | State of AI Report Compute Index

# GPU lifetime and economics

## How long do AI chips remain useful?
- AI chips can stay relevant for years after newer generations appear; there is no fixed retirement age.  
- Three lifespans are distinguished:  
  - **Physical life** – how long the hardware functions.  
  - **Economic life** – how long operating it remains cost‑effective.  
  - **Accounting life** – period over which the purchase cost is depreciated.  
- NVIDIA’s A100, announced May 2020, was still cited in commercial use in October 2026, showing usefulness beyond six years, but this does not imply every individual GPU lasts that long.  
- Obsolescence depends on workload size, memory needs, software support, electricity costs, and alternative hardware.  
- Continued research citations indicate usage, not average physical lifespan or guaranteed financial return.

## Can older GPUs remain competitive for inference?
- Older GPUs are viable for inference when the workload fits their memory, software stack, and latency targets at a competitive total cost.  
- Example: AWS still offers T4‑based G4dn instances for image classification, speech recognition, and small‑scale training.  
- Large models, long contexts, or strict latency may require newer GPUs.  
- Software support can limit reuse: CUDA 13 dropped offline compilation for Maxwell, Pascal, and Volta architectures, though older binaries run on supported drivers.  
- The index lacks matched inference benchmarks, so it cannot rank profitability across GPU generations.

## Does six‑year GPU depreciation mean six years of profitability?
- Depreciation spreads an asset’s cost over an estimated accounting life; it does not guarantee demand, cash flow, or return on capital.  
- Companies use category‑level estimates (e.g., CoreWeave: six‑year useful life; Amazon: five‑to‑six years, shortened for some AI equipment in 2025).  
- Example: a $60 k GPU with zero residual value depreciated straight‑line over six years yields $10 k annual expense versus $15 k over four years; the schedule changes expense, not cash outlay.  
- Profitability assessment must consider contracted revenue, utilization, operating costs, financing, and resale proceeds.  
- Book value, resale value, and profitability are distinct metrics.

## What happens to GPU rental prices and resale values when new chips arrive?
- Newer chips can pressure older GPU rental rates and resale prices if they deliver the same workload at lower total cost, but price changes are not immediate or uniform.  
- Factors influencing price shifts: availability, demand, software compatibility, and required power/cooling upgrades.  
- Contract terms affect repricing; many contracts are 1‑6 year take‑or‑pay agreements, delaying price adjustments.  
- NVIDIA’s October 2026 report of A100 bookings through 2029 shows continued demand for a specific model, not a market‑wide trend.  
- The index does not track rental or resale transactions, so it cannot provide a depreciation curve.

## What determines the total cost of running AI GPUs?
- Total cost includes more than GPU purchase price or hourly rental: servers, networking, storage, power, cooling, maintenance, software, staff, financing, and eventual resale value.  
- For inference, compare cost per completed request or per token at equal model quality, context length, throughput, and latency.  
- A lower GPU‑hour price can result in higher cost per useful result if the job runs slower or needs more machines.  
- Consistent comparison periods and workloads are essential; add ancillary charges (e.g., storage, data transfer) for rented services.  
- Distinguish purchase cash outlay from depreciation expense; avoid double‑counting.  
- AWS Inference Recommender illustrates why a single price metric is insufficient.

## Does high GPU utilization mean a profitable data center?
- High utilization does not equal profitability.  
- Utilization metrics (e.g., NVIDIA NVML) show the fraction of time at least one kernel runs, not the proportion of peak performance delivered.  
- Profitability depends on revenue relative to all costs of providing capacity.  
- Clarify which utilization measure is reported: capacity reserved, hours billed, kernel‑run time, or useful throughput.