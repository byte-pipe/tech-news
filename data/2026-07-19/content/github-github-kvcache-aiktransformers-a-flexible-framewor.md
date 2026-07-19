---
title: 'GitHub - kvcache-ai/ktransformers: A Flexible Framework for Experiencing Heterogeneous LLM Inference/Fine-tune Optimizations · GitHub'
url: https://github.com/kvcache-ai/ktransformers
site_name: github
content_file: github-github-kvcache-aiktransformers-a-flexible-framewor
fetched_at: '2026-07-19T11:27:27.369276'
original_url: https://github.com/kvcache-ai/ktransformers
author: kvcache-ai
description: A Flexible Framework for Experiencing Heterogeneous LLM Inference/Fine-tune Optimizations - kvcache-ai/ktransformers
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 kvcache-ai

 

/

ktransformers

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.4k
* Star18.1k

 
 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

1,302 Commits
1,302 Commits
.github
.github
 
 
archive
archive
 
 
doc
doc
 
 
docker
docker
 
 
kt-kernel
kt-kernel
 
 
third_party
third_party
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
LICENSE
LICENSE
 
 
MAINTAINERS.md
MAINTAINERS.md
 
 
MANIFEST.in
MANIFEST.in
 
 
README.md
README.md
 
 
README_ZH.md
README_ZH.md
 
 
book.toml
book.toml
 
 
install.sh
install.sh
 
 
ktransformers.py
ktransformers.py
 
 
pyproject.toml
pyproject.toml
 
 
setup.py
setup.py
 
 
version.py
version.py
 
 
View all files

## Repository files navigation

### A Flexible Framework for Experiencing Cutting-edge LLM Inference/Fine-tune Optimizations

🎯 Overview
 | 
🚀 Inference
 | 
🎓 SFT
 | 
🔥 Citation
 | 
🚀 Roadmap(2026Q2)
 

## 🎯 Overview

KTransformers is a research project focused on efficient inference and fine-tuning of large language models through CPU-GPU heterogeneous computing. The project now exposes two user-facing capabilities from the kt-kernel source tree:InferenceandSFT.

## 🔥 Updates

* June 21, 2026: MiniMax-M3 Day0 Support! (Tutorial)
* June 17, 2026: GLM-5.2 Day0 Support! (Tutorial)
* May 6, 2026: KTransformers atGOSIM Paris 2026— "Agentic AI on Edge" track. We'll present KT's inference performance on consumer hardware.
* May 02, 2026: DeepSeek-V4-Flash Support! (Tutorial)
* Apr 30, 2026: KTransformers v0.6.1 refreshes kt-kernel inference and SFT docs with separateInferenceandSFT Quick Startentry points.
* Mar 26, 2026: Support AVX2-only CPU backend for KT-Kernel inference. (Tutorial)
* Feb 13, 2026: MiniMax-M2.5 Day0 Support! (Tutorial)
* Feb 12, 2026: GLM-5 Day0 Support! (Tutorial)
* Jan 27, 2026: Kimi-K2.5 Day0 Support! (Tutorial) (SFT Tutorial)
* Jan 22, 2026: SupportCPU-GPU Expert Scheduling,Native BF16 and FP8 per channel PrecisionandAutoDL unified fine-tuning and inference
* Dec 24, 2025: Support Native MiniMax-M2.1 inference. (Tutorial)
* Dec 22, 2025: Support RL-DPO fine-tuning with LLaMA-Factory. (Tutorial)
* Dec 5, 2025: Support Native Kimi-K2-Thinking inference (Tutorial)
* Nov 6, 2025: Support Kimi-K2-Thinking inference (Tutorial) and fine-tune (Tutorial)
* Nov 4, 2025: KTransformers Fine-Tuning × LLaMA-Factory Integration. (Tutorial)
* Oct 27, 2025: Support Ascend NPU. (Tutorial)
* Oct 10, 2025: Integrating into SGLang. (Roadmap,Blog)
* Sept 11, 2025: Support Qwen3-Next. (Tutorial)
* Sept 05, 2025: Support Kimi-K2-0905. (Tutorial)
* July 26, 2025: Support SmallThinker and GLM4-MoE. (Tutorial)
* July 11, 2025: Support Kimi-K2. (Tutorial)
* June 30, 2025: Support 3-layer (GPU-CPU-Disk)prefix cachereuse.
* May 14, 2025: Support Intel Arc GPU (Tutorial).
* Apr 29, 2025: Support AMX-Int8、 AMX-BF16 and Qwen3MoE (Tutorial)
* Apr 9, 2025: Experimental support for LLaMA 4 models (Tutorial).
* Apr 2, 2025: Support Multi-concurrency. (Tutorial).
* Mar 15, 2025: Support ROCm on AMD GPU (Tutorial).
* Mar 5, 2025: Support unsloth 1.58/2.51 bits weights andIQ1_S/FP8 hybridweights. Support 139KLonger Contextfor DeepSeek-V3 and R1 in 24GB VRAM.
* Feb 25, 2025: SupportFP8 GPU kernelfor DeepSeek-V3 and R1;Longer Context.
* Feb 15, 2025: Longer Context (from 4K to 8K for 24GB VRAM) & Slightly Faster Speed （+15%, up to 16 Tokens/s), updatedocsandonline books.
* Feb 10, 2025: Support Deepseek-R1 and V3 on single (24GB VRAM)/multi gpu and 382G DRAM, up to 3~28x speedup. For detailed show case and reproduction tutorial, seehere.
* Aug 28, 2024: Decrease DeepseekV2's required VRAM from 21G to 11G.
* Aug 15, 2024: Update detailedtutorialfor injection and multi-GPU.
* Aug 14, 2024: Support llamfile as linear backend.
* Aug 12, 2024: Support multiple GPU; Support new model: mixtral 8*7B and 8*22B; Support q2k, q3k, q5k dequant on gpu.
* Aug 9, 2024: Support windows native.

## 📦 Capabilities

### 🚀Inference- High-Performance kt-kernel Serving

CPU-optimized kernel operations for heterogeneous LLM inference.

Key Features:

* AMX/AVX Acceleration: Intel AMX and AVX512/AVX2 optimized kernels for INT4/INT8 quantized inference
* MoE Optimization: Efficient Mixture-of-Experts inference with NUMA-aware memory management
* Quantization Support: CPU-side INT4/INT8 quantized weights, GPU-side GPTQ support
* Easy Integration: Clean Python API for SGLang and other frameworks

Quick Start:

cd
 kt-kernel
pip install 
.

Use Cases:

* CPU-GPU hybrid inference for large MoE models
* Integration with SGLang for production serving
* Heterogeneous expert placement (hot experts on GPU, cold experts on CPU)

Performance Examples:

Model

Hardware Configuration

Total Throughput

Output Throughput

DeepSeek-R1-0528 (FP8)

8×L20 GPU + Xeon Gold 6454S

227.85 tokens/s

87.58 tokens/s (8-way concurrency)

👉Full Documentation →

### 🎓SFT- Fine-Tuning with LLaMA-Factory

KTransformers × LLaMA-Factory integration for ultra-large MoE model fine-tuning.

Key Features:

* Multi-Backend Support: CPU/GPU hybrid fine-tuning with INT8/INT4 quantization
* Ultra-Large MoE Support: Fine-tune models like DeepSeek-V3/R1 on limited GPU memory
* Faster than ZeRO-Offload: 6-12x training speedup in benchmarked MoE SFT workloads
* Lower CPU Memory: About half the CPU memory of the previous KT SFT path in the benchmarked setup
* LLaMA-Factory Integration: Seamless integration with popular fine-tuning framework

Model

GPU Memory

Training Speed

Hardware

DeepSeek-V3

~80GB total

3.7 it/s

4x RTX 4090

DeepSeek-R1

~80GB total

3.7 it/s

4x RTX 4090

Qwen3-30B-A3B

~24GB total

8+ it/s

1x RTX 4090

Quick Start:

cd
 /path/to/LLaMA-Factory
pip install -e 
.

pip install -r requirements/ktransformers.txt
CUDA_VISIBLE_DEVICES=0,1,2,3 accelerate launch \
 --config_file examples/ktransformers/accelerate/fsdp2_kt_int8.yaml \
 src/train.py \
 examples/ktransformers/train_lora/qwen3_5moe_lora_sft_kt.yaml

👉Quick Start →👉Full Documentation →

## 🔥 Citation

If you use KTransformers in your research, please cite our paper:

@inproceedings
{
10.1145/3731569.3764843
,
 
title
 = 
{
KTransformers: Unleashing the Full Potential of CPU/GPU Hybrid Inference for MoE Models
}
,
 
author
 = 
{
Chen, Hongtao and Xie, Weiyu and Zhang, Boxin and Tang, Jingqi and Wang, Jiahao and Dong, Jianwei and Chen, Shaoyuan and Yuan, Ziwei and Lin, Chen and Qiu, Chengyu and Zhu, Yuening and Ou, Qingliang and Liao, Jiaqi and Chen, Xianglin and Ai, Zhiyuan and Wu, Yongwei and Zhang, Mingxing
}
,
 
booktitle
 = 
{
Proceedings of the ACM SIGOPS 31st Symposium on Operating Systems Principles
}
,
 
year
 = 
{
2025
}

}

## 👥 Contributors & Team

Developed and maintained by:

* MADSys Lab@ Tsinghua University
* Approaching.AI
* 9#AISoft
* Community contributors

We welcome contributions! Please feel free to submit issues and pull requests.

## 💬 Community & Support

* GitHub Issues:Report bugs or request features
* WeChat Group: Seearchive/WeChatGroup.png

## 📦 KT original Code

The original integrated KTransformers framework has been archived to thearchive/directory for reference. The project now organizes the two capabilities above from the kt-kernel source tree for clearer documentation and maintenance.

For the original documentation with full quick-start guides and examples, see:

* archive/README.md(English)
* archive/README_ZH.md(中文)

## About

A Flexible Framework for Experiencing Heterogeneous LLM Inference/Fine-tune Optimizations

kvcache-ai.github.io/ktransformers/

### Resources

 Readme

 

### License

 Apache-2.0 license
 

### Code of conduct

 Code of conduct
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

18.1k

 stars
 

### Watchers

118

 watching
 

### Forks

1.4k

 forks
 

 Report repository

 

## Releases29

KTransformers v0.6.3

 Latest

 

Jun 21, 2026

 

+ 28 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python57.1%
* C++34.0%
* Cuda5.0%
* Shell1.0%
* CMake0.8%
* Vue0.7%
* Other1.4%