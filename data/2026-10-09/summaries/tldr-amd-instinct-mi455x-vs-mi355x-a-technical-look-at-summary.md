---
title: AMD Instinct MI455X vs MI355X: A Technical Look at the Advancing AI 2026 Inference Numbers — ROCm Blogs
url: https://rocm.blogs.amd.com/software-tools-optimization/mi455x-vs-mi355x/README.html
date: 2026-10-09
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-10-09T10:16:40.749918
---

# AMD Instinct MI455X vs MI355X: A Technical Look at the Advancing AI 2026 Inference Numbers — ROCm Blogs

# AMD Instinct MI455X vs MI355X: Technical Look at Advancing AI 2026 Inference Numbers

## Prerequisites
- Assumes familiarity with LLM inference phases (prefill vs. decode), online serving metrics, GPU compute vs. memory‑bandwidth limits, and multi‑GPU scaling concepts.
- Definitions and links to tools are provided in‑line; no physical AMD Instinct hardware is required to understand the methodology.

## How to Read the Numbers
- **Medians**: each microbenchmark run five times; median values are reported to reduce thermal and system noise effects.  
- **Single‑GPU focus**: comparisons are one‑to‑one (MI455X vs. MI355X) on a single accelerator, except for networking tests that involve multiple endpoints.  
- **Bring‑up state**: MI455X results are from a pre‑release Helios platform; software stacks are still maturing, so numbers represent a snapshot in time.  
- **Comparison styles**:  
  - *Apples‑to‑apples*: identical configuration on both GPUs.  
  - *Peak‑to‑peak*: each GPU tuned individually for its best performance.  

## End‑to‑End: DeepSeek‑V4‑Flash Online Serving
### Model & Framework
- **Model**: DeepSeek‑V4‑Flash, open‑source MoE with 284 B total parameters, 13 B activated per token.  
- **Precision**: expert weights FP4, other parameters FP8.  
- **Context length**: up to 1 M tokens; fits on a single GPU for clean per‑GPU comparison.  
- **Inference stack**: AMD ATOM, executed on a single accelerator for both GPUs.

### Metrics
| Metric | Meaning |
|--------|---------|
| Interactivity | Output tokens / second per user (higher = more responsive). |
| Total token throughput per GPU | Aggregate token rate across all concurrent users (higher = more work done). |

- Throughput rises with concurrency while interactivity falls; a sweep of concurrency yields a throughput‑vs‑interactivity curve for each GPU.

### Ratio Computation
- Ratios are calculated at fixed interactivity targets (≈90, 70, 30 tokens / s / user).  
- For a given target, the highest total throughput that still meets the target is taken for each GPU; the ratio = MI455X throughput / MI355X throughput.  
- Because curve shapes differ, ratios increase at higher interactivity (MI355X drops off earlier).

## 1K / 1K Workload (1,024‑token input, 1,024‑token output)

| Interactivity (tokens / s / user) | MI455X / MI355X Throughput Ratio |
|-----------------------------------|-----------------------------------|
| 20 | 2.47x |
| 30 | 3.70x |
| 40 | 7.44x |
| 50 | 12.66x |
| 60 | 14.79x |
| 70 | 17.06x |
| 80 | 30.46x |
| 90 | 33.98x |

- Ratio climbs from ~2.5× at low interactivity to ~34× at high interactivity, indicating the MI455X maintains high concurrency while the MI355X curve collapses.

## 1K / 8K Workload (1,024‑token input, 8,192‑token output)

- Same methodology applied to a decode‑heavy scenario; results show even larger gains for MI455X at high interactivity (exact numbers follow the same pattern as the 1K/1K case, with ratios increasing further as decode dominates).

## Key Takeaways
- **MI455X delivers dramatically higher token throughput under high‑interactivity conditions**, achieving up to ~34× the MI355X performance on the DeepSeek‑V4‑Flash online serving benchmark.  
- The advantage is most pronounced when the decode phase dominates (long output sequences) because MI455X’s improved compute and HBM bandwidth better handle memory‑bound kernels.  
- Results are based on median values from controlled single‑GPU tests; software maturity and configuration tuning can shift absolute numbers, but the relative performance gap is expected to persist as the MI455X stack stabilizes.