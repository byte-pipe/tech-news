---
title: Running Gemma 4 on EC2 G5g: Graviton2 AMD with NVIDIA GPU - DEV Community
url: https://dev.to/gde/running-gemma-4-on-ec2-g5g-graviton2-amd-with-nvidia-gpu-25ci
date: 2026-08-13
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-08-15T04:05:08.481545
---

# Running Gemma 4 on EC2 G5g: Graviton2 AMD with NVIDIA GPU - DEV Community

# Running Gemma 4 on EC2 G5g: Graviton2 ARM host with NVIDIA T4G

## Hardware & Base Image
- **Instance**: AWS EC2 g5g.4xlarge – Graviton2 (aarch64) CPU + 1 × NVIDIA T4G (Turing, compute capability 7.5), 15 360 MiB GPU memory.  
- **Base AMI**: Deep Learning ARM64 AMI OSS Nvidia Driver GPU, Ubuntu 24.04, PyTorch 2.12.

## Software Stack
- **torch** 2.12.0 + cu132, CUDA 13.2.  
- **vLLM** 0.27.2rc0 built from source for `sm_75`.  
- **Result**: 43.1 tokens / s (single‑stream greedy) with a 329 579‑token KV cache after a single vLLM patch.

## Main Obstacles Encountered
- **Missing aarch64 + SM 7.5 build** – Official vLLM and NVIDIA images list arm64 support only from Ampere onward; Turing kernels are absent, causing immediate “no kernel image” failures.  
- **Version floor & missing compiler** – PyTorch wheels for arm64 lack SM 7.5; the AWS DLAMI provides a compatible PyTorch but ships without the CUDA toolkit, a C++ compiler, and the Rust toolchain required by vLLM.  
- **64 KiB shared‑memory ceiling** – Triton’s unified attention kernel for Gemma 4’s heterogeneous head dimensions needs ~96 KiB per block, exceeding Turing’s 64 KiB limit, leading to kernel launch errors and engine shutdown.

## How Each Issue Was Resolved
- **Found a compatible PyTorch**: The AWS Deep Learning ARM64 AMI includes a custom PyTorch 2.12 build that retains SM 7.5 (and newer) support, eliminating the need to compile PyTorch from source.  
- **Installed missing tools**: Added NVIDIA’s arm64 `cuda-toolkit-13-2` package and installed Rust plus `setuptools_rust` to satisfy vLLM’s build requirements.  
- **Used the correct vLLM version**: vLLM 0.27.2rc0 introduced handling of per‑layer `head_dim` heterogeneity required by Gemma 4; earlier tags failed on model load.  
- **Worked around the shared‑memory limit**: Modified vLLM to shrink the KV tile size and enforce a single‑stage pipeline when `device_capability < 8` (pre‑Ampere), keeping shared‑memory usage ≤ 60 KB and allowing the kernel to launch.

## Key Take‑aways
- **G5g is unique**: It is the only AWS instance that pairs an ARM host with a Turing‑class GPU; most pre‑built containers do not support this combination.  
- **Check actual CUDA architectures**: AWS‑provided PyTorch builds may retain legacy SM 7.5 support even when official wheels do not.  
- **Prefer the newest releases**: The latest vLLM tag resolved model‑loading issues that older tags could not handle.  
- **Shared‑memory limits matter**: For Turing GPUs, Triton kernels assuming >64 KiB shared memory will fail; adjusting tile sizes is a minimal, effective fix.