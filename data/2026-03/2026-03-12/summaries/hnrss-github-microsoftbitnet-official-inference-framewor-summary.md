---
title: GitHub - microsoft/BitNet: Official inference framework for 1-bit LLMs · GitHub
url: https://github.com/microsoft/BitNet
date: 2026-03-11
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-03-12T03:15:04.764156
---

# GitHub - microsoft/BitNet: Official inference framework for 1-bit LLMs · GitHub

# BitNet Repository Overview

## Project Description
- `bitnet.cpp` is the official inference framework for 1‑bit large language models (LLMs) such as BitNet b1.58.
- Provides optimized kernels for fast, lossless inference on CPU and GPU (NPU support planned).
- First release focuses on CPU inference, delivering speedups of 1.37×‑5.07× on ARM and 2.37×‑6.17× on x86, with energy reductions of 55.4%‑82.2%.
- Enables running a 100B BitNet b1.58 model on a single CPU at human‑reading speed (5‑7 tokens / second).
- Latest optimizations add parallel kernels, configurable tiling, and embedding quantization, giving an extra 1.15×‑2.1× speedup.

## Demo
- Video demo shows a BitNet b1.58 3B model running on Apple M2.

## Recent Updates
- 01/15/2026 – CPU inference optimization.
- 05/20/2025 – Official GPU inference kernel.
- 04/14/2025 – 2B‑parameter model released on Hugging Face.
- 02/18/2025 – Efficient edge inference for ternary LLMs.
- 11/08/2024 – 4‑bit activations for 1‑bit LLMs.
- 10/21/2024 – Part 1 of fast, lossless BitNet b1.58 CPU inference.
- 10/17/2024 – `bitnet.cpp` 1.0 released.
- Earlier posts (2023‑2024) discuss training tips, FAQs, and the era of 1‑bit LLMs.

## Acknowledgements
- Built on the `llama.cpp` framework.
- Kernels extend the Lookup Table methods from T‑MAC.
- For low‑bit LLMs beyond ternary, T‑MAC is recommended.

## Official Model Support
| Model | Parameters | CPU (x86) | CPU (ARM) | I2_S | TL1 | TL2 |
|-------|------------|----------|-----------|------|-----|-----|
| BitNet‑b1.58‑2B‑4T | 2.4 B | ✅ | ✅ | ✅ | ❌ | ✅ |
| bitnet_b1_58‑large | 0.7 B | ✅ | ✅ | ✅ | ❌ | ✅ |
| bitnet_b1_58‑3B | 3.3 B | ❌ | ❌ | ❌ | ✅ | ❌ |
| Llama3‑8B‑1.58‑100B‑tokens | 8.0 B | ✅ | ✅ | ✅ | ❌ | ✅ |
| Falcon3 Family (1‑10 B) | – | ✅ | ✅ | ✅ | ❌ | ✅ |
| Falcon‑E Family (1‑3 B) | – | ✅ | ✅ | ✅ | ❌ | ✅ |

## Installation Guide
### Requirements
- Python ≥ 3.9
- CMake ≥ 3.22
- Clang ≥ 18 (Windows: Visual Studio 2022 with C++ desktop development, CMake tools, Git, Clang, MS‑Build)
- Conda (highly recommended)

### Build Steps
1. Clone the repository recursively.
   ```bash
   git clone --recursive https://github.com/microsoft/BitNet.git
   cd BitNet
   ```
2. Create and activate a conda environment, then install Python dependencies.
   ```bash
   conda create -n bitnet-cpp python=3.9
   conda activate bitnet-cpp
   pip install -r requirements.txt
   ```
3. Download a model from Hugging Face and set up the environment.
   ```bash
   huggingface-cli download microsoft/BitNet-b1.58-2B-4T-gguf --local-dir models/BitNet-b1.58-2B-4T
   python setup_env.py -md models/BitNet-b1.58-2B-4T -q i2_s
   ```

## Basic Usage
Run inference with a quantized model:
```bash
python run_inference.py -m models/BitNet-b1.58-2B-4T/ggml-model-i2_s.gguf -p "You are a helpful assistant" -cnv
```
Command‑line options include:
- `-n` / `--n-predict` – number of tokens to generate.
- `-t` / `--threads` – thread count.
- `-c` / `--ctx-size` – prompt context size.
- `-temp` / `--temperature` – controls randomness.
- `-cnv` / `--conversation` – enable chat mode.
