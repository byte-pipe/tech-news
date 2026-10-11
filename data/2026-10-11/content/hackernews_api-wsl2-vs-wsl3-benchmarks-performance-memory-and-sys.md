---
title: 'WSL2 vs WSL3 Benchmarks: Performance, Memory, and Syscall Scaling // Tony Metzidis'
url: https://tonym.us/wsl2-vs-wsl3-benchmarks.html
site_name: hackernews_api
content_file: hackernews_api-wsl2-vs-wsl3-benchmarks-performance-memory-and-sys
fetched_at: '2026-10-11T13:38:33.116571'
original_url: https://tonym.us/wsl2-vs-wsl3-benchmarks.html
author: Tony Metzidis
date: '2026-10-08'
published_date: '2026-10-07T00:00:00+00:00'
tags:
- hackernews
- trending
---

With the release of the WSL 3.x stack, Microsoft bumped the default virtualization runtime and advanced the shipped guest kernel from the 6.6 LTS branch up to 6.18.

WSL upgrades often claim generalized performance gains, but marketing bullet points rarely translate directly to developer workloads. To see what actually changed under the hood, I ran side-by-side benchmark suites comparingWSL 2.6.3.0(Linux kernel6.6.87.2) againstWSL 3.0.2.0(Linux kernel6.18.40.1).

Here is what the empirical numbers look like across kernel primitives, memory bandwidth, and an end-to-end Go compiler workload.

### The Test Environment

To keep the test clean and reproducible, the guest environment was provisioned using an Alpine Linux 3.23.0 root filesystem (minirootfs) running Go 1.27.1:

* Guest OS:Alpine Linux 3.23.0 (x86_64)
* Guest Kernel (WSL3):6.18.40.1-microsoft-standard-WSL2
* Go Version:Go 1.27.1
* Host Machine:HP ProDesk 400 G4 Desktop Mini (DM)
* Processor:Intel Core i5-8500T (6C/6T Coffee Lake @ 2.10 GHz base)
* Host RAM:16 GB DDR4
* Host OS:Windows 11 Pro (Build 26200.9550, VBS active)
* WSL Resource Allocations (.wslconfig):processors=2(pinned to 2 vCPUs)memory=4GBnetworkingMode=natfirewall=true
* processors=2(pinned to 2 vCPUs)
* memory=4GB
* networkingMode=nat
* firewall=true

### Low-Level Kernel Microbenchmarks

Using standardperf benchsuites, we can isolate raw scheduler latency, IPC throughput, and memory bandwidth independent of user-space tooling.

Benchmark Suite

Metric

WSL 2.6.3 (
6.6.87
)

WSL 3.0.2 (
6.18.40
)

Delta

syscall/basic

getppid()
 throughput

1,474,691 ops/s

1,533,399 ops/s

+3.98%

Entry/exit latency

0.6781 µs/op

0.6521 µs/op

-3.83%

sched/pipe

100k process ping-pong

48,445 ops/s

54,589 ops/s

+12.68%

Context switch latency

20.64 µs/op

18.32 µs/op

-11.25%

sched/messaging

Hackbench (20 groups, 800 tasks)

14.507 s

13.047 s

-10.06%

mem/memcpy

glibc default bandwidth (1GB)

7.84 GB/s

12.64 GB/s

+61.35%

#### What the Kernel Deliberations Tell Us

1. Memory Bandwidth Surge (+61.35%):The single largest jump is sequential memory throughput, climbing from 7.84 GB/s to 12.64 GB/s. A primary contributor in the 3.x kernel command line ispage_reporting.page_reporting_order=5. Raising the page reporting granularity reduces hypervisor trap frequency and page-table walking overhead when the guest interacts with Hyper-V’s dynamic memory reclamation interface.
2. Scheduler & IPC Latency (-11%):Bothsched/pipeandsched/messagingshow noticeable drops in latency. The upstream kernel 6.18 scheduler refinements, paired with tighter Hyper-V VMBus synthetic interrupt handling, reduce the CPU-to-CPU wake penalties when bouncing messages between runnable tasks across the two pinned vCPUs.
3. Basic Syscall Transition (-3.8%):Raw system call entry and exit (getppid) saw a modest bump. Trivial ring transitions on 8th-Gen Intel hardware remain governed by fixed CPU architectural boundaries, leaving less room for hypervisor software tuning alone to alter entry costs.

### Real-World Workload: GoReleaser Compilation

To test how these micro-level improvements map to developer tooling, I compiled the GoReleaser codebase (go build -a -o /dev/null) with an empty compiler cache (go clean -cache) and a primed module cache:

Metric

WSL 2.6.3 (
6.6.87
)

WSL 3.0.2 (
6.18.40
)

Delta

Real (Wall-clock)

3m 11.27s (191.27s)

3m 03.80s (183.80s)

-7.47s (-3.91%)

User (CPU Time)

4m 58.99s (298.99s)

4m 49.38s (289.38s)

-9.61s (-3.21%)

Sys (Kernel Time)

0m 57.39s (57.39s)

0m 48.22s (48.22s)

-9.17s (-15.98%)

#### Breaking Down the Runtime Split

While top-line wall-clock compilation speed moved by roughly4%, the underlying distribution of execution time highlights where the stack actually improved:

* Kernel Overhead (sys) Collapsed by ~16%:The compiler repeatedly executesopenat,newfstatat,mmap, andfutexcalls while scanning the package graph and coordinating compilation workers. The lower kernel trap overhead and improved slab caching in 6.18 directly shaved over 9 seconds off time spent inside the kernel.
* The Wall-Clock Ceiling:The reason total real time only moved by ~7.5 seconds is straightforward: compilation is predominantly a user-space compute workload. Lexing, AST construction, type checking, and SSA optimization account for over 80% of the total clock cycles. Because the VM is capped at two physical cores running at a 2.10 GHz base clock, raw CPU execution bounds dominate the overall duration.

### Takeaways

Upgrading from WSL 2.x to WSL 3.x is a worthwhile jump, but where you see the benefit depends heavily on your workload profile:

* High-Churn IPC and Memory-Intensive Systems Win:Local workloads running in-memory databases (Redis, SQLite), container-dense workflows, or microservices passing payloads over Unix domain sockets benefit immediately from the +61% memory bandwidth boost and 10–11% lower context-switching latency.
* Compute-Bound Compilers Hit Hardware Ceilings:If your build toolchain spends most of its time executing user-space code on constrained vCPUs, WSL 3.x will significantly cut your kernel time (sys), but your overall build duration will still be dictated by core frequency and thread count.

### See Also

* The Security Tax in WSL3: Benchmarking Kernel Mitigations Against WSL 2.x
* The "Security Tax": Reclaiming 30% Performance in WSL 2
* Taming GCE Memory Tax: Disabling OS Login and OS Config on Small Instances
* Isolated & Sandboxed WSL Environments with Debian Slim
* Lightweight Efficiency: Porting Alpine Linux RootFS to WSL2