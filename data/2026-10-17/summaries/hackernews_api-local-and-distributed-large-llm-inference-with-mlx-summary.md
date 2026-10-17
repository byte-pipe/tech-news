---
title: Local and Distributed Large LLM Inference with MLX and RDMA on Mac Studio - Apple Machine Learning Research
url: https://machinelearning.apple.com/research/mlx-distributed-inference
date: 2026-10-17
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-10-17T13:53:15.180197
---

# Local and Distributed Large LLM Inference with MLX and RDMA on Mac Studio - Apple Machine Learning Research

# Local and Distributed Large LLM Inference with MLX and RDMA on Mac Studio

## Overview
- MLX leverages Apple silicon’s unified memory architecture to run large language models locally and in private environments.  
- The latest release enables inference of Muse Spark Open (≈ 816 B parameters) on a single Mac Studio and across multiple machines using RDMA over Thunderbolt.  
- Performance scales from a single Mac Studio (up to 512 GB unified memory) to clusters of two or four Mac Studios.

## Muse Spark Open Decode Speed
- Measured with a context size of 8,192 tokens.  
- Three parallelization schemes evaluated:  
  * 2‑Mac pipeline parallelism (2 M5 Pipeline)  
  * 2‑Mac tensor parallelism (2 M5 Tensor)  
  * 4‑Mac tensor parallelism (4 M5 Tensor)  
- Achieves > 36 tokens / second, surpassing average human reading speed.

## Benchmark Models
| Model | Total Parameters | Active Parameters | Native Precision | Evaluation Precision |
|---|---|---|---|---|
| Muse Spark Open | 816 B | 42 B | BF16 | NVFP4 |
| Mistral Medium 3.5 | 128 B | 128 B | FP8 | FP8 |
| Qwen 3.8 | 27 B | 27 B | BF16 | BF16 |

- Muse Spark Open is a mixture‑of‑experts (MoE) model; only a fraction of experts are active during inference, reducing compute.  
- Mistral Medium 3.5 and Qwen 3.8 are dense models where all parameters are active.

## Single‑Mac Studio Performance
- Qwen 3.8 (27 B) and Mistral Medium 3.5 (128 B) fit comfortably on a 512 GB Mac Studio, using 68 GB and 158 GB RAM respectively at a 65,536‑token context.  
- **Time‑to‑first‑token (TTFT)** is compute‑bound; the M5 Ultra GPU Neural Accelerator delivers up to **4.6×** faster TTFT than the M3 Ultra.  
- **Generation throughput** is memory‑bandwidth bound; M5 Ultra’s 1.2 TB/s unified memory bandwidth yields **1.6×** higher tokens / second compared to M3 Ultra.  
- **Power consumption** remains modest: peak ~200 W for M3 Ultra and ~300 W for M5 Ultra, comparable to a household toaster.

## Scaling Beyond a Single Machine
- Muse Spark Open requires > 1.6 TB RAM in native BF16 precision; 4‑bit NVFP4 quantization reduces the footprint to ~493 GB, still exceeding a single Mac Studio’s capacity.  
- Multi‑Mac parallelism is required.

### Pipeline Parallelism (2 Macs)
- Model split depth‑wise: first half of layers on Mac A, second half on Mac B.  
- Simple to implement with minimal code changes using MLX pipeline parallelism.

### Tensor Parallelism (2–4 Macs)
- Model split width‑wise across GPUs.  
- Supported by MLX v0.30.1+ with “jaccl” collectives built on macOS 26.2’s low‑latency RDMA driver over Thunderbolt 5.

## Distributed Communication Stack
- macOS 26.2 introduces an RDMA driver for Thunderbolt 5, providing low‑latency inter‑machine communication.  
- MLX leverages this driver to enable high‑performance collectives for both pipeline and tensor parallelism.

## Takeaway
- MLX on Apple silicon delivers fast, energy‑efficient LLM inference locally.  
- The M5 Ultra chip markedly improves compute‑bound (TTFT) and memory‑bound (throughput) performance over the M3 Ultra.  
- With RDMA‑enabled Thunderbolt, clusters of Mac Studios can run frontier‑class models such as Muse Spark Open that exceed single‑machine memory limits, enabling private, high‑performance AI workloads in home or office environments.