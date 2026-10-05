---
title: GitHub - PowderworksCode/headstart: Start dependent crates before their dependencies finish type-checking · GitHub
url: https://github.com/PowderworksCode/headstart
date: 2026-10-04
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-10-05T12:20:49.920883
---

# GitHub - PowderworksCode/headstart: Start dependent crates before their dependencies finish type-checking · GitHub

# headstart – Parallelizing Dependent Crate Compilation

## Overview
- **Purpose**: Allows a dependent crate to start compiling after only the interface of its dependencies is checked, rather than waiting for full type‑checking of function bodies.
- **Mechanism**:  
  - `rustc` writes an *early metadata* file (`.rmeta`) once the dependency’s interface is verified.  
  - `cargo` receives a notification and launches dependent crates using this early metadata.  
  - Full metadata is swapped in later, just before code generation.

## Core Components
- **rustc patches (`-Zearly-metadata`)**  
  - Split analysis into interface and body phases.  
  - Emit early metadata between phases.  
  - Loader can accept early metadata and later replace it with full metadata, waiting on a lock if necessary.
- **cargo patches (`-Zheadstart`)**  
  - Propagate early‑metadata notifications to dependents for both `check` and `build`.  
  - Release a paused compilation’s job slot for other work.  
  - Emit crate output only after all dependencies have succeeded.

## Performance Results
- **Clean builds of 13 real projects** (e.g., rust‑analyzer, bevy, lemmy) on a 16‑core machine:  
  - Up to **54 % faster** for `cargo check`.  
  - Up to **42 % faster** for `cargo build`.  
  - No project became slower.
- **Parallel front‑end (`-Zthreads=8`)** adds up to **25 %** improvement on the same hardware.
- **Smaller machines** see proportionally smaller gains (e.g., 4 cores: 24 % faster check for rust‑analyzer, 13–15 % faster build).
- **Codex‑rs workspace**: 37 % faster build on 16 cores because crates start as soon as early metadata is available.

## Correctness Guarantees
- Errors in function bodies still cause the build to fail with identical diagnostics and exit status as the standard workflow.
- Cargo only reports a crate’s output after all its dependencies have completed successfully; if a dependency fails, downstream work is discarded.
- Memory usage increases because more work may be in flight simultaneously.

## Usage Instructions
1. Run `scripts/setup.sh` to checkout patched `rustc` and `cargo` and build them.  
2. In any Rust project, invoke the patched tools:  
   ```bash
   RUSTC=/path/to/headstart/rustc/build/host/stage1/bin/rustc \
   /path/to/headstart/cargo/target/release/cargo check -Zheadstart
   ```
   - For builds, replace `check` with `build`.  
   - Environment variable `CARGO_UNSTABLE_HEADSTART=true` or `[unstable] headstart = true` in `.cargo/config.toml` also enables the feature.

## Test Suite
- **tests/smoke**: Demonstrates reduced waiting time for a slow library.  
- **scripts/check-errors.sh**: Verifies identical error reporting with and without headstart.  
- **scripts/check-incremental.sh**: Checks behavior across incremental edits.  
- **scripts/check-swap.sh**: Ensures swapping from early to full metadata yields identical binaries.  
- **scripts/sweep.sh**: Runs all 53 `rustc-perf` benchmarks in both modes, confirming identical diagnostics.

## Benchmarking Tools
- `scripts/bench.sh` – measures median times for clean `cargo check`/`build`.  
- `scripts/real-projects.sh` – clones the 13 measured real projects.  
- `scripts/bench-suite.sh` – runs the full benchmark suite (real projects, rustc‑perf, codex‑rs).  
- Additional scripts (`bench-mem.sh`, `bench-incremental.sh`, `log-rustc`) provide memory profiling, incremental timing, and schedule logging.

## Documentation
- **Design details**: `docs/design.md` (what early metadata contains, risks).  
- **Results**: `docs/results.md` (full performance tables).  
- **Readiness assessment**: `docs/readiness.md` (evaluation for upstream integration).