---
title: 'GitHub - deepseek-ai/DeepInfer: DeepInfer: High-performance, large-scale inference framework for DeepSeek models · GitHub'
url: https://github.com/deepseek-ai/DeepInfer
site_name: hackernews_api
content_file: hackernews_api-github-deepseek-aideepinfer-deepinfer-high-perform
fetched_at: '2026-10-20T15:34:56.138332'
original_url: https://github.com/deepseek-ai/DeepInfer
author: ggcr
date: '2026-10-20'
description: 'DeepInfer: High-performance, large-scale inference framework for DeepSeek models - deepseek-ai/DeepInfer'
tags:
- hackernews
- trending
---

main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

3 Commits
3 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
csrc
csrc
 
 
deep_cluster
deep_cluster
 
 
deepinfer
deepinfer
 
 
doc
doc
 
 
eval
eval
 
 
examples
examples
 
 
scripts
scripts
 
 
tests
tests
 
 
vendor
vendor
 
 
.clang-format
.clang-format
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
build.sh
build.sh
 
 
pyproject.toml
pyproject.toml
 
 
requirements-ascend.txt
requirements-ascend.txt
 
 
requirements-dev.txt
requirements-dev.txt
 
 
requirements-nvidia.txt
requirements-nvidia.txt
 
 
requirements.txt
requirements.txt
 
 
setup.py
setup.py
 
 
View all files

## Repository files navigation

# DeepInfer

DeepInfer is the high-performance inference framework that powers DeepSeek's large-scale production services. This open-source release provides offline inference with the core features needed for serving at scale.

Supported models:

* DeepSeek-V4.1-Flash

Supported features:

* Optimized kernels, model and sampler runtime
* Parallelism: Attention DP / balanced CP, MoE EP + EPLB
* DSpark and confidence-scheduled verification
* SWA bounded replay
* Asynchronous scheduling (zero-overhead batch scheduler)
* Batch-invariant inference
* Deterministic sampling
* Structured outputs

Feature details and configuration

* Optimized kernels:FlashMLA,DeepGEMM,DeepEP,TileKernels,DeepSelect, and customTileLang kernels.
* DSpark and confidence-scheduled verification:accelerate decoding with draft tokens and use confidence estimates to schedule verification. SetDEEPINFER_ENABLE_MTP_VARLEN=1;DEEPINFER_USE_NEXTN_DECODEcontrols the maximum draft length (default: 5).
* Decoder SWA bounded replay:reduce decoder prefill work by replaying only a bounded suffix. SetDEEPINFER_YOCO_PREFILL_TRUNCATION_MODE=compactandDEEPINFER_YOCO_PREFILL_KEEP_TOKENS=140for the default V4.1 settings; the retained suffix must cover the SWA window plus the maximum backtracking length.
* Asynchronous scheduling:overlap CPU batch scheduling with device execution. Enabled by default.
* Batch-invariant inference:keep model results identical across different batch compositions. Enable withDEEPINFER_BATCH_INVARIANT=1(NVIDIA only).
* Deterministic sampling:produce identical outputs for identical input tokens and sampling parameters. SetDEEPINFER_BATCH_INVARIANT=1 DEEPINFER_ENABLE_MTP_VARLEN=0and pass a fixedseq_seedtoSamplingParams(NVIDIA only).
* Structured outputs:constrain generation to a regex, JSON schema, or EBNF grammar. Passso_args={"schema_type": ..., "schema": ...}toSamplingParams; seeexamples.

Supported hardware:

* NVIDIA SM100 GPUs
* Huawei Ascend 950 NPUs

Required for a complete inference service (not included in this release):

* A KV cache system
* VE/Prefill/Decode disaggregation (most required engine functionality is already implemented)
* Load balancing across data-parallel replicas for both prefill and decode

## Getting started

### Prerequisites

* Linux
* GCC >= 13.0
* Python 3.12
* CUDA 13 (NVIDIA only)
* CANN 9.2 (Ascend only)

### Build from source

Before building DeepInfer, please create and activate an empty Python 3.12 environment.

#
 Use `ascend` instead for the Ascend platform

#
 Keep it exported in the environment where you run DeepInfer

export
 DEEPINFER_ACCELERATOR=nvidia
./build.sh

### Offline inference

The default checkpoint,deepseek-ai/DeepSeek-V4.1-Flash-1017, is
downloaded into the Hugging Face cache on the first run; setDEEPINFER_HF_MODEL_DIR=/path/to/DeepSeek-V4.1-Flash-1017to
run from a local copy instead.

python examples/offline_inference.py

Seeexamplesfor details.

## Performance benchmarks

Prefill

Decode

Measured on 4 SM100 GPUs for prefill and 64 for decode — each within one scale-up domain. To reproduce the benchmarks, seerun_sweep.sh.

## Evaluation benchmarks

Seeeval/README.md.

## License

DeepInfer is released under the Apache License 2.0. SeeLICENSEfor details.

## Acknowledgments

DeepInfer was originally built primarily onvLLM, with additional inspiration fromSGLangandTensorRT-LLM. We thank their developers.

## Citation

@misc
{
deepinfer2026
,
 
title
 = 
{
DeepInfer: High-performance, large-scale inference framework for DeepSeek models
}
,
 
author
 = 
{
DeepSeek-AI
}
,
 
year
 = 
{
2026
}
,
 
publisher
 = 
{
GitHub
}
,
 
howpublished
 = 
{
\url{https://github.com/deepseek-ai/DeepInfer}
}
,
}