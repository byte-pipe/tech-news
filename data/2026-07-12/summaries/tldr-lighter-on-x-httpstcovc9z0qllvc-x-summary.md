---
title: "Lighter on X: \"https://t.co/Vc9Z0QlLVc\" / X"
url: https://x.com/Lighter_xyz/status/2074905536122789917
date: 2026-07-12
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-07-12T06:02:56.052579
---

# Lighter on X: "https://t.co/Vc9Z0QlLVc" / X

# Chasing Microseconds: Lighter's Latency Engineering

## Key Points
- Over several months of iterative development, Lighter reduced its overall end‑to‑end p99 latency from **280 ms** to a steady **55 ms**.  
- Transaction‑processing latency, which previously experienced spikes of **20–30 ms**, is now consistently **under 1 ms** for the p99 case.  
- The “hot path” apply time (the critical section of request handling) has been optimized to a very low, stable value (exact figure not disclosed in the excerpt).  
- The article emphasizes the systematic engineering approach taken to achieve microsecond‑level performance, highlighting measurement, profiling, and targeted code/path optimizations.