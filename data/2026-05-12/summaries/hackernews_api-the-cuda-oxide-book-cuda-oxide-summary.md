---
title: The cuda-oxide Book — cuda-oxide
url: https://nvlabs.github.io/cuda-oxide/index.html
date: 2026-05-12
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-05-12T06:01:56.903593
---

# The cuda-oxide Book — cuda-oxide

# The cuda-oxide Book

## Project Status
- v0.1.0 is an early‑stage alpha release.  
- Expect bugs, incomplete features, and possible API breakage.  
- Feedback from users is encouraged to guide development.

## Quick start
- **Imports**  
  ```rust
  use cuda_device::{cuda_module, kernel, thread, DisjointSlice};
  use cuda_core::{CudaContext, DeviceBuffer, LaunchConfig};
  ```
- **Kernel definition** (`vecadd`) using `#[kernel]` and `thread::index_1d()` to compute element‑wise addition of two slices into a `DisjointSlice`.
- **Host program** steps:
  1. Create a `CudaContext` and obtain the default stream.  
  2. Load the compiled module with `kernels::load(&ctx)`.  
  3. Allocate device buffers `a`, `b` (initialized from host data) and `c` (zeroed).  
  4. Launch the kernel via `module.vecadd(&stream, LaunchConfig::for_num_elems(1024), &a, &b, &mut c)`.  
  5. Copy the result back to host with `c.to_host_vec(&stream)` and verify with `assert_eq!(result[0], 3.0)`.  
- Build and run with `cargo run --example vecadd` after installing prerequisites.  
- `#[cuda_module]` embeds the device artifact into the host binary and generates a typed `load` function plus a launch method per kernel; lower‑level APIs remain available for custom use.

## Why cuda-oxide?
- **Rust on the GPU** – write kernels using Rust’s type system and ownership model; safety is a primary goal, with a dedicated safety model for GPU subtleties.  
- **SIMT compiler** – a custom `rustc` codegen backend that compiles pure Rust directly to PTX, eliminating the need for DSLs or foreign language bindings.  
- **Async execution** – compose GPU work as lazy `DeviceOperation` graphs, schedule across stream pools, and await results with `.await`.  

## Prerequisites
- Familiarity with Rust (ownership, traits, generics).  
- Understanding of async/await and runtimes such as Tokio for later chapters on async GPU programming.  
- Reference material: *The Rust Programming Language*, *Rust by Example*, or the *Async Book*.