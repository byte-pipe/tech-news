---
title: WSL2 vs WSL3 Benchmarks: Performance, Memory, and Syscall Scaling // Tony Metzidis
url: https://tonym.us/wsl2-vs-wsl3-benchmarks.html
date: 2026-10-08
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-10-11T13:39:03.323361
---

# WSL2 vs WSL3 Benchmarks: Performance, Memory, and Syscall Scaling // Tony Metzidis

# WSL2 vs WSL3 Benchmarks: Performance, Memory, and Syscall Scaling // Tony Metzidis

## Test Environment
- Guest OS: Alpine Linux 3.23.0 (x86_64) with Go 1.27.1  
- Kernels compared:  
  - WSL 2.6.3 (Linux 6.6.87.2)  
  - WSL 3.0.2 (Linux 6.18.40.1‑microsoft‑standard‑WSL2)  
- Host: HP ProDesk 400 G4 Mini, Intel Core i5‑8500T (6 cores/6 threads, 2.10 GHz), 16 GB DDR4, Windows 11 Pro (Build 26200.9550, VBS active)  
- WSL resources (via `.wslconfig`): 2 vCPUs, 4 GB RAM, NAT networking, firewall enabled  

## Low‑Level Kernel Microbenchmarks
| Metric | WSL 2 | WSL 3 | Δ |
|--------|------|------|---|
| `syscall/basic` getppid() throughput | 1,474,691 ops/s | 1,533,399 ops/s | +3.98 % |
| Entry/exit latency | 0.6781 µs/op | 0.6521 µs/op | –3.83 % |
| `sched/pipe` 100k process ping‑pong | 48,445 ops/s | 54,589 ops/s | +12.68 % |
| Context switch latency | 20.64 µs/op | 18.32 µs/op | –11.25 % |
| `sched/messaging` Hackbench (20 groups, 800 tasks) | 14.507 s | 13.047 s | –10.06 % |
| `mem/memcpy` glibc default bandwidth (1 GB) | 7.84 GB/s | 12.64 GB/s | +61.35 % |

**Interpretation**
- Memory bandwidth jumps 61 % thanks to `page_reporting.page_reporting_order=5`, which reduces hypervisor traps.  
- Scheduler and IPC latency improve 10–12 % due to 6.18 scheduler refinements and tighter VMBus interrupt handling.  
- Basic syscall entry/exit sees a modest 4 % gain; hardware limits dominate this path.  

## Real‑World Workload: GoReleaser Compilation
| Metric | WSL 2 | WSL 3 | Δ |
|--------|------|------|---|
| Real (wall‑clock) | 3 m 11.27 s (191.27 s) | 3 m 03.80 s (183.80 s) | –3.91 % |
| User (CPU) | 4 m 58.99 s (298.99 s) | 4 m 49.38 s (289.38 s) | –3.21 % |
| Sys (kernel) | 0 m 57.39 s (57.39 s) | 0 m 48.22 s (48.22 s) | –15.98 % |

**Breakdown**
- Kernel time drops ~16 % (≈9 s) because openat, fstatat, mmap, futex calls benefit from lower trap overhead and better slab caching.  
- Overall wall‑clock improvement is limited (~4 %) since >80 % of compilation work is user‑space compute bound by the two pinned vCPUs.  

## Takeaways
- **Workloads with heavy IPC or memory traffic** (in‑memory databases, container‑dense pipelines, microservices using Unix sockets) gain the most from the +61 % memory bandwidth and 10–11 % lower context‑switch latency.  
- **Compute‑bound toolchains** (e.g., large Go builds) see a clear reduction in kernel overhead but remain limited by CPU core count and frequency; overall build time improves only modestly.  

## See Also
- The Security Tax in WSL3: Benchmarking Kernel Mitigations Against WSL 2.x  
- The “Security Tax”: Reclaiming 30 % Performance in WSL 2  
- Taming GCE Memory Tax: Disabling OS Login and OS Config on Small Instances  
- Isolated & Sandboxed WSL Environments with Debian Slim  
- Lightweight Efficiency: Porting Alpine Linux RootFS to WSL2