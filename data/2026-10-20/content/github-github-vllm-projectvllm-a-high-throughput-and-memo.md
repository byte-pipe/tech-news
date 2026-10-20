---
title: 'GitHub - vllm-project/vllm: A high-throughput and memory-efficient inference and serving engine for LLMs · GitHub'
url: https://github.com/vllm-project/vllm
site_name: github
content_file: github-github-vllm-projectvllm-a-high-throughput-and-memo
fetched_at: '2026-10-20T15:34:53.418661'
original_url: https://github.com/vllm-project/vllm
author: vllm-project
description: A high-throughput and memory-efficient inference and serving engine for LLMs - vllm-project/vllm
---

main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

23,446 Commits
23,446 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.agents/
skills
.agents/
skills
 
 
.buildkite
.buildkite
 
 
.claude/
skills
.claude/
skills
 
 
.github
.github
 
 
benchmarks
benchmarks
 
 
cmake
cmake
 
 
csrc
csrc
 
 
docker
docker
 
 
docs
docs
 
 
examples
examples
 
 
recipes
recipes
 
 
requirements
requirements
 
 
rust
rust
 
 
tests
tests
 
 
tools
tools
 
 
vllm
vllm
 
 
.clang-format
.clang-format
 
 
.dockerignore
.dockerignore
 
 
.git-blame-ignore-revs
.git-blame-ignore-revs
 
 
.gitignore
.gitignore
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
.readthedocs.yaml
.readthedocs.yaml
 
 
AGENTS.md
AGENTS.md
 
 
CMakeLists.txt
CMakeLists.txt
 
 
DCO
DCO
 
 
LICENSE
LICENSE
 
 
MANIFEST.in
MANIFEST.in
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
mkdocs.yaml
mkdocs.yaml
 
 
pyproject.toml
pyproject.toml
 
 
rust-toolchain.toml
rust-toolchain.toml
 
 
setup.py
setup.py
 
 
View all files

## Repository files navigation

### Easy, fast, and cheap LLM serving for everyone

|Documentation|Blog|Paper|Twitter/X|User Forum|Developer Slack|

🔥 We have built a vLLM website to help you get started with vLLM. Please visitvllm.aito learn more.
For events, please visitvllm.ai/eventsto join us.

## About

vLLM is a fast and easy-to-use library for LLM inference and serving.

Originally developed in theSky Computing Labat UC Berkeley, vLLM has grown into one of the most active open-source AI projects built and maintained by a diverse community of many dozens of academic institutions and companies from over 2000 contributors.

vLLM is fast with:

* State-of-the-art serving throughput
* Efficient management of attention key and value memory withPagedAttention
* Continuous batching of incoming requests, chunked prefill, prefix caching
* Fast and flexible model execution with piecewise and full CUDA/HIP graphs
* Quantization: FP8, MXFP8/MXFP4, NVFP4, INT8, INT4, GPTQ/AWQ, GGUF, compressed-tensors, ModelOpt, TorchAO, andmore
* Optimized attention kernels including FlashAttention, FlashInfer, TRTLLM-GEN, FlashMLA, and Triton
* Optimized GEMM/MoE kernels for various precisions using CUTLASS, TRTLLM-GEN, CuTeDSL
* Speculative decoding including n-gram, suffix, EAGLE, DFlash
* Automatic kernel generation and graph-level transformations using torch.compile
* Disaggregated prefill, decode, and encode

vLLM is flexible and easy to use with:

* Seamless integration with popular Hugging Face models
* High-throughput serving with various decoding algorithms, includingparallel sampling,beam search, and more
* Tensor, pipeline, data, expert, and context parallelism for distributed inference
* Streaming outputs
* Generation of structured outputs using xgrammar or guidance
* Tool calling and reasoning parsers
* OpenAI-compatible API server, plus Anthropic Messages API and gRPC support
* Efficient multi-LoRA support for dense and MoE layers
* Support for NVIDIA GPUs, AMD GPUs, Intel GPUs, and x86/ARM/PowerPC CPUs. Additionally, diverse hardware plugins such as Google TPUs, Intel Gaudi, IBM Spyre, Huawei Ascend, Rebellions NPU, Apple Silicon, MetaX GPU, and more.

vLLM seamlessly supports 200+ model architectures on Hugging Face, including:

* Decoder-only LLMs (e.g., Llama, Qwen, Gemma)
* Mixture-of-Expert LLMs (e.g., Mixtral, DeepSeek-V3, Qwen-MoE, GPT-OSS)
* Hybrid attention and state-space models (e.g., Mamba, Qwen3.5)
* Multi-modal models (e.g., LLaVA, Qwen-VL, Pixtral)
* Embedding and retrieval models (e.g., E5-Mistral, GTE, ColBERT)
* Reward and classification models (e.g., Qwen-Math)

Find the full list of supported modelshere.

## Getting Started

Install vLLM withuv(recommended) orpip:

uv pip install vllm
vllm download-kernels 
#
 precompiled kernels for faster startup

Orbuild from sourcefor development.

Visit ourdocumentationto learn more.

* Installation
* Quickstart
* List of Supported Models

## Contributing

We welcome and value any contributions and collaborations.
Please check outContributing to vLLMfor how to get involved.

## Citation

If you use vLLM for your research, please cite ourpaper:

@inproceedings
{
kwon2023efficient
,
 
title
=
{
Efficient Memory Management for Large Language Model Serving with PagedAttention
}
,
 
author
=
{
Woosuk Kwon and Zhuohan Li and Siyuan Zhuang and Ying Sheng and Lianmin Zheng and Cody Hao Yu and Joseph E. Gonzalez and Hao Zhang and Ion Stoica
}
,
 
booktitle
=
{
Proceedings of the ACM SIGOPS 29th Symposium on Operating Systems Principles
}
,
 
year
=
{
2023
}

}

## Contact Us

* For technical questions and feature requests, please use GitHubIssues
* For discussing with fellow users, please use thevLLM Forum
* For coordinating contributions and development, please useSlack
* For security disclosures, please use GitHub'sSecurity Advisoriesfeature
* For collaborations and partnerships, please contact us atcollaboration@vllm.ai

## Media Kit

* If you wish to use vLLM's logo, please refer toour media kit repo