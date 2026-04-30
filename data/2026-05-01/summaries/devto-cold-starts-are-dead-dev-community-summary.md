---
title: Cold Starts Are Dead - DEV Community
url: https://dev.to/aws/cold-starts-are-dead-5fod
date: 2026-04-29
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-05-01T03:55:19.509428
---

# Cold Starts Are Dead - DEV Community

# Cold Starts Are Dead – Summary

## Current Lambda Cold Start Latencies (2026)
- Measured from production workloads, not synthetic tests.  
- Typical ranges (P50 / P99) by runtime:  
  - **Python 3.13**: 200‑400 ms / 800 ms‑1.2 s  
  - **Node.js 22**: 200‑350 ms / 600 ms‑1 s  
  - **Go**: 50‑100 ms / 150‑250 ms  
  - **Rust**: 50‑80 ms / 100‑200 ms (as low as 16 ms on arm64)  
  - **Java 21 (no SnapStart)**: 2‑5 s / 6‑10 s  
  - **Java 21 + SnapStart**: 90‑140 ms / 200‑400 ms  
- Arm64 (Graviton) instances reduce numbers further by 15‑40 %.

## VPC Impact on Cold Starts
- Pre‑2019: VPC required ENI creation, adding 10‑15 s latency.  
- 2019 migration to Firecracker microVMs eliminated most of that overhead, dropping VPC cold‑start penalty to under a second.  
- Recent eBPF optimizations cut tunnel latency to ~200 µs, making VPC‑related cold starts negligible.

## SnapStart Effect
- GA timeline: Java (Nov 2022), Python 3.12+ & .NET 8 (Nov 2024), expanded regions & arm64 (2025).  
- Works by snapshotting an initialized microVM and restoring it on cold start.  
- Real‑world reductions:  
  - Java Spring Boot: 5.8 s → 180 ms (≈97 % reduction)  
  - Python (Flask, LangChain, Pandas): several seconds → sub‑second  
  - .NET: 58‑94 % reduction in cold‑start time.  

## INIT Billing Change (Aug 2025)
- AWS began billing the INIT phase for ZIP‑packaged functions with managed runtimes.  
- The often‑cited “22× cost increase” assumes: 100 % cold‑start rate, 2 s Java INIT, 512 MB memory – a scenario that does not reflect typical usage.  
- Production data shows cold starts occur in < 1 % of invocations, so cost impact is minimal for most workloads.  
- SnapStart further reduces INIT duration, shrinking any billing impact.

## Benchmark Findings (13 functions, 6 runtimes, arm64 & x86_64, 50 cold starts each)
- Platform floor cold‑start times (P50) were at or below the production ranges:  
  - **Rust**: 14.1 ms (arm64), 17.0 ms (x86_64) – faster than claimed 50‑80 ms.  
  - **Go**: 45.0 ms (arm64), 59.8 ms (x86_64) – within 50‑100 ms range.  
  - **Python 3.13**: 88.3 ms (arm64), 106.2 ms (x86_64) – better than 200‑400 ms claim.  
  - **Node.js 22**: 121.5 ms (arm64), 155.0 ms (x86_64) – faster than 200‑350 ms claim.  
  - **Java 21**: 365.3 ms (arm64), 443.8 ms (x86_64) – far below 2‑5 s claim.  
- Arm64 advantage observed across all runtimes (17‑25 % faster P50).  
- VPC‑connected Python function was 1.4 ms faster than non‑VPC, confirming negligible VPC penalty.  
- SnapStart on a minimal Java handler showed ~670 ms restore overhead; benefit scales with the amount of init work being skipped.

## Recommendations
- Treat cold starts as a solved problem for most modern workloads; focus on other architectural concerns.  
- Prefer arm64 (Graviton) deployments to gain 15‑25 % lower latency without code changes.  
- Enable SnapStart for Java, Python, and .NET when using frameworks that incur significant init time.  
- Monitor actual cold‑start ratios with CloudWatch Logs Insights to assess any billing impact from the INIT phase.  
- Use the open‑source benchmark suite to validate cold‑start performance for your specific functions.