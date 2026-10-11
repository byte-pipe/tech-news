---
title: GPU lifetime and economics | State of AI Report Compute Index
url: https://www.stateof.ai/compute-explore/gpu-lifetime
site_name: tldr
content_file: tldr-gpu-lifetime-and-economics-state-of-ai-report-comp
fetched_at: '2026-10-12T06:00:33.133129'
original_url: https://www.stateof.ai/compute-explore/gpu-lifetime
author: Nathan Benaich
date: '2026-10-12'
description: GPU useful life, inference, depreciation, rental prices, operating costs, and utilization.
tags:
- tldr
---

# GPU lifetime and economics

By Nathan Benaich (Air Street Capital)

GPU useful life, inference, depreciation, rental prices, operating costs, and utilization.

## Questions in this topic

How long do AI chips remain useful?
Can older GPUs remain competitive for inference?
Does six-year GPU depreciation mean six years of profitability?
What happens to GPU rental prices and resale values when new chips arrive?
What determines the total cost of running AI GPUs?
Does high GPU utilization mean a profitable data center?

## Questions and answers

Evidence reviewed · October 11, 2026

### How long do AI chips remain useful?

AI chips can remain useful for years after a newer generation arrives, but there is no universal retirement age. Physical life is how long the hardware works; economic life is how long operating it remains worthwhile; accounting life is the period over which its cost is depreciated. NVIDIA announced A100 shipments on May 14, 2020 and reported continued commercial use in October 2026. That establishes relevance more than six years after the model launched, not six years of service for every individual GPU.

How quickly do GPUs become obsolete? It depends on the workload, memory needs, software support, electricity costs, and available alternatives. A chip can lose its place in frontier training while remaining useful for smaller models, inference, or scientific computing. A100 also leads the index’s 2026 NVIDIA citation estimate, which includes second-half projections. Citations show research use, not chip age, utilization, realized revenue, or investment returns. Continued use does not establish an average physical lifespan or guarantee recovery of the original purchase price.

NVIDIA’s May 2020 A100 announcement·NVIDIA’s October 2026 longevity discussion·NVIDIA usage chart·Citation methodology

Read this answer 

Evidence reviewed · October 11, 2026

### Can older GPUs remain competitive for inference?

Yes, for workloads that fit their memory, software, and latency requirements at a competitive total cost. AWS still offers NVIDIA T4-based G4dn instances for machine learning inference and small-scale training, including applications such as image classification and speech recognition. That is evidence of an ongoing use case, not proof that older GPUs are the cheapest choice for every model. Compare the cost of delivering the required throughput and response time, rather than hourly rental price alone.

Large models, long contexts, or demanding response-time targets can favor newer systems. Software support can also constrain reuse: CUDA 13 removed offline compilation and library support for Maxwell, Pascal, and Volta architectures. NVIDIA says applications built with older toolkits can continue running on supported drivers; the change does not make those chips stop working. This index has no matched inference benchmark or total-cost dataset, so it cannot rank old and new GPUs by profitability or recommend a universal replacement date.

AWS G4 instance specifications and workloads·NVIDIA CUDA 13 release notes·NVIDIA guidance on older GPU support

Read this answer 

2025 annual filings · reviewed October 11, 2026

### Does six-year GPU depreciation mean six years of profitability?

No. Depreciation allocates an asset’s cost over its estimated accounting life; it does not guarantee customer demand, cash flow, or an adequate return on capital. CoreWeave’s 2025 annual report assigns technology equipment a six-year useful life. Amazon reports five to six years for servers and networking equipment, after shortening the estimate for a subset from six to five years effective January 1, 2025 because of faster technological development, particularly in AI and machine learning. These are equipment-category estimates, not measured lifespans for every GPU model.

For a simplified $60,000 asset with zero residual value, straight-line depreciation is $10,000 a year over six years versus $15,000 over four. The longer schedule reduces annual depreciation expense by $5,000 while leaving the purchase cash outlay unchanged. This is an illustration, not a GPU price quote. To assess returns, examine contracted and renewal revenue, utilization, operating costs, financing, and eventual resale proceeds. A fully depreciated GPU can still earn revenue; one with remaining book value can become uneconomic. Book value, resale value, and profitability measure different things.

CoreWeave 2025 annual report: property and equipment·Amazon 2025 annual report: useful-life estimates

Read this answer 

Evidence reviewed · October 11, 2026

### What happens to GPU rental prices and resale values when new chips arrive?

New chips can put pressure on older GPUs’ rental prices and resale values when they deliver the same workload at lower total cost. A launch does not dictate an immediate or uniform price drop: availability, demand, software compatibility, and the cost of adapting power and cooling also matter. Rental prices measure payment for access; resale prices measure what a buyer will pay to own the hardware. Neither is the same as accounting book value or an operator’s profit.

Contract structure matters. CoreWeave’s 2025 annual report describes committed contracts generally lasting one to six years, typically with take-or-pay terms, alongside hourly on-demand services. Those terms can delay repricing compared with new rentals; renewal economics remain a separate question. NVIDIA’s October 2026 account cites CoreWeave A100 bookings extending through 2029, a vendor-reported example of continued demand, not a market-wide price series or proof of future margins. The index does not track rental transactions or resale prices and therefore cannot quantify a depreciation curve. Compare equivalent GPU configurations, regions, contract terms, and service bundles before drawing a price trend.

CoreWeave 2025 annual report: customer contracts·NVIDIA’s October 2026 account of A100 bookings

Read this answer 

Cost framework · reviewed October 11, 2026

### What determines the total cost of running AI GPUs?

The GPU purchase price or hourly rental rate is only part of the cost. An owned deployment also needs servers, networking, storage, power, cooling, maintenance, software, and staff. Financing and the hardware’s eventual resale value affect the economics. For inference, compare cost per completed request or per token at the same model quality, context length, throughput, and latency requirements. A cheaper GPU-hour can cost more per useful result if the job takes longer or requires more machines.

Choose a consistent comparison period and workload. For rented capacity, identify what the service price includes and add charges such as storage or data transfer where applicable. For owned capacity, distinguish purchase cash spending from depreciation expense; do not count both as separate cash costs. AWS’s Inference Recommender reports cost per hour and per inference alongside throughput and latency, illustrating why one price metric is insufficient. This index does not contain a matched cost benchmark and cannot name the cheapest GPU or cloud provider.

AWS inference cost and performance metrics·CoreWeave 2025 annual report: operating costs

Read this answer 

Metric definitions · reviewed October 11, 2026

### Does high GPU utilization mean a profitable data center?

No. GPU utilization, billable occupancy, and profitability measure different things. A hardware utilization metric can show that a GPU is busy without showing how much useful work it completes or what a customer pays. NVIDIA’s NVML GPU-utilization measure records the share of a sampling interval during which at least one kernel runs; it is not a percentage of peak computing performance. Profitability depends on revenue relative to the costs of providing that capacity.

Ask which utilization measure is being reported: capacity reserved by customers, hours billed, time running kernels, or useful throughput relative to a workload benchmark. These measures are not interchangeable. Take-or-pay contracts can produce revenue even when a customer leaves reserved hardware idle, while a busy internal research cluster may have no external rental revenue. Neither case alone establishes a return on investment. The index records selected hardware counts and reported access, not utilization, customer payments, or operator margins.

NVIDIA NVML utilization definition·CoreWeave 2025 annual report: committed contracts and costs·Index scope

Read this answer 

## Charts and sources

1. NVIDIA’s May 2020 A100 announcement
2. NVIDIA’s October 2026 longevity discussion
3. NVIDIA usage chart
4. Citation methodology
5. AWS G4 instance specifications and workloads
6. NVIDIA CUDA 13 release notes
7. NVIDIA guidance on older GPU support
8. CoreWeave 2025 annual report: property and equipment
9. Amazon 2025 annual report: useful-life estimates
10. CoreWeave 2025 annual report: customer contracts
11. NVIDIA’s October 2026 account of A100 bookings
12. AWS inference cost and performance metrics
13. CoreWeave 2025 annual report: operating costs
14. NVIDIA NVML utilization definition
15. CoreWeave 2025 annual report: committed contracts and costs
16. Index scope

Company filings and hardware documentation reviewed October 11, 2026. Accounting examples use 2025 annual reports; vendor claims are attributed. Research citations do not measure profitability, and this index has no rental-price or resale-value series.

All data sources