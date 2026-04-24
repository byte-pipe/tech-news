---
title: TorchTPU: Running PyTorch Natively on TPUs at Google Scale - Google Developers Blog
url: https://developers.googleblog.com/torchtpu-running-pytorch-natively-on-tpus-at-google-scale/
date: 2026-04-24
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-04-25T08:23:51.561209
---

# TorchTPU: Running PyTorch Natively on TPUs at Google Scale - Google Developers Blog

# TorchTPU: Running PyTorch Natively on TPUs at Google Scale

## Overview
- Modern AI workloads require distributed systems with up to 100,000 accelerators, demanding performance, portability, and reliability.  
- Google’s TPUs power internal AI platforms (Gemini, Veo) and Cloud customers; making them accessible to PyTorch users is essential.  
- TorchTPU is built to let developers migrate existing PyTorch code to TPUs with minimal changes while exposing the full hardware capability.

## Architecting for Usability, Portability, and Performance
- TPU systems consist of a host, multiple chips, and an Inter‑Chip Interconnect (ICI) forming a 2‑D/3‑D torus topology.  
- Each chip contains TensorCores (dense matrix math) and SparseCores (embeddings, gather/scatter, collectives).  
- Core usability principle: “It should feel like PyTorch.” Switching the device to “tpu” should run the original training loop unchanged.  
- Achieved by deep integration with the PyTorch PrivateUse1 device and a new interaction model with the TPU compiler/runtime.

## Eager First: Flexibility Without Compromise
- Implemented three eager execution modes via the PrivateUse1 interface:
  - **Debug Eager** – one‑op dispatch with CPU synchronization after each op; useful for debugging shape mismatches, NaNs, OOMs.  
  - **Strict Eager** – asynchronous single‑op dispatch, mirroring standard PyTorch behavior; enables CPU and TPU to run concurrently.  
  - **Fused Eager** – automatically fuses streams of ops into larger kernels before sending to the TPU, boosting TensorCore utilization and reducing memory traffic; delivers 50 %–100 %+ speedup over Strict Eager with no user effort.  
- All modes share a Compilation Cache that can be host‑local or persistent across multiple hosts, reducing repeated compilation time.

## Static Compilation: Dynamo, XLA, and StableHLO
- Supports full‑graph compilation through `torch.compile`:
  1. Captures the FX graph with Torch Dynamo.  
  2. Routes the graph to XLA (instead of Torch Inductor) as the backend compiler.  
- XLA is chosen for its proven TPU support and ability to optimize dense computation together with ICI‑based collective communication.  
- Translation layer maps PyTorch operators to StableHLO, XLA’s IR, enabling highly optimized TPU binaries while reusing eager‑mode execution paths.  
- Custom operator support:
  - Kernels can be written in Pallas or JAX and registered with `@torch_tpu.pallas.custom_jax_kernel`.  
  - Ongoing work to add Helion kernel support.

## Distributed Training and the MPMD Challenge
- Full compatibility with PyTorch distributed APIs:
  - Distributed Data Parallel (DDP)  
  - Fully Sharded Data Parallel v2 (FSDPv2)  
  - DTensor  
- Third‑party libraries built on these APIs run unchanged on TorchTPU.  
- Addresses limitation of earlier PyTorch/XLA (SPMD‑only) by supporting divergent per‑rank code (MPMD).  
  - Isolates communication primitives where needed, preserving correctness with minimal overhead.  
  - Allows natural PyTorch development patterns (e.g., rank‑0 logging) while still enabling XLA’s global optimization of communication/computation overlap.

## TPU Hardware Awareness
- TorchTPU exposes the distinct capabilities of TensorCores and SparseCores, enabling models that mix dense matrix math with irregular memory accesses to achieve high performance on TPU clusters.