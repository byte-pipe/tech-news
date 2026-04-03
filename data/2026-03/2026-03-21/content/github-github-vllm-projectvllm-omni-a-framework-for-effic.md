---
title: 'GitHub - vllm-project/vllm-omni: A framework for efficient model inference with omni-modality models · GitHub'
url: https://github.com/vllm-project/vllm-omni
site_name: github
content_file: github-github-vllm-projectvllm-omni-a-framework-for-effic
fetched_at: '2026-03-21T11:08:54.882422'
original_url: https://github.com/vllm-project/vllm-omni
author: vllm-project
description: A framework for efficient model inference with omni-modality models - vllm-project/vllm-omni
---

vllm-project

 

/

vllm-omni

Public

* NotificationsYou must be signed in to change notification settings
* Fork578
* Star3.4k

 
 
 
 
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

939 Commits
939 Commits
.buildkite
.buildkite
 
 
.github
.github
 
 
apps/
ComfyUI-vLLM-Omni
apps/
ComfyUI-vLLM-Omni
 
 
benchmarks
benchmarks
 
 
docker
docker
 
 
docs
docs
 
 
examples
examples
 
 
requirements
requirements
 
 
scripts
scripts
 
 
tests
tests
 
 
tools
tools
 
 
vllm_omni
vllm_omni
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
.readthedocs.yml
.readthedocs.yml
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
collect_env.py
collect_env.py
 
 
mkdocs.yml
mkdocs.yml
 
 
pyproject.toml
pyproject.toml
 
 
setup.py
setup.py
 
 
View all files

## Repository files navigation

### Easy, fast, and cheap omni-modality model serving for everyone

|Documentation|User Forum|Developer Slack|WeChat|Paper|Slides|

Latest News🔥

* [2026/03] Check out our first publicproject deepdiveat the vLLM Hong Kong Meetup!
* [2026/03]vllm-omni-skillsis a community-driven collection of AI assistant skills that help developers work with vLLM-Omni more effectively. These skills can be used with popular agentic AI coding assistants likeCursor IDE,Claude,Codex, and more.
* [2026/02] We released0.16.0- A major alignment + capability release that rebases ontoupstream vLLM v0.16.0and significantly expands performance, distributed execution, and production readiness acrossQwen3-Omni / Qwen3-TTS,Bagel,MiMo-Audio,GLM-Imageand theDiffusion (DiT) image/video stack—while also improving platform coverage (CUDA / ROCm / NPU / XPU), CI quality, and documentation.
* [2026/02] We released0.14.0- This is the firststable releaseof vLLM-Omni that expands Omni’s diffusion / image-video generation and audio / TTS stack, improves distributed execution and memory efficiency, and broadens platform/backend coverage (GPU/ROCm/NPU/XPU). It also brings meaningful upgrades to serving APIs, profiling & benchmarking, and overall stability. Please check our latestpaperfor architecture design and performance results.
* [2026/01] We released0.12.0rc1- a major RC milestone focused on maturing the diffusion stack, strengthening OpenAI-compatible serving, expanding omni-model coverage, and improving stability across platforms (GPU/NPU/ROCm).
* [2025/11] vLLM community officially releasedvllm-project/vllm-omniin order to support omni-modality models serving.

## About

vLLMwas originally designed to support large language models for text-based autoregressive generation tasks. vLLM-Omni is a framework that extends its support for omni-modality model inference and serving:

* Omni-modality: Text, image, video, and audio data processing
* Non-autoregressive Architectures: extend the AR support of vLLM to Diffusion Transformers (DiT) and other parallel generation models
* Heterogeneous outputs: from traditional text generation to multimodal outputs

vLLM-Omni is fast with:

* State-of-the-art AR support by leveraging efficient KV cache management from vLLM
* Pipelined stage execution overlapping for high throughput performance
* Fully disaggregation based on OmniConnector and dynamic resource allocation across stages

vLLM-Omni is flexible and easy to use with:

* Heterogeneous pipeline abstraction to manage complex model workflows
* Seamless integration with popular Hugging Face models
* Tensor, pipeline, data and expert parallelism support for distributed inference
* Streaming outputs
* OpenAI-compatible API server

vLLM-Omni seamlessly supports most popular open-source models on HuggingFace, including:

* Omni-modality models (e.g. Qwen-Omni)
* Multi-modality generation models (e.g. Qwen-Image)

## Getting Started

Visit ourdocumentationto learn more.

* Installation
* Quickstart
* List of Supported Models

## Contributing

We welcome and value any contributions and collaborations.
Please check outContributing to vLLM-Omnifor how to get involved.

## Citation

If you use vLLM-Omni for your research, please cite ourpaper:

@article
{
yin2026vllmomni
,
 
title
=
{
vLLM-Omni: Fully Disaggregated Serving for Any-to-Any Multimodal Models
}
,
 
author
=
{
Peiqi Yin, Jiangyun Zhu, Han Gao, Chenguang Zheng, Yongxiang Huang, Taichang Zhou, Ruirui Yang, Weizhi Liu, Weiqing Chen, Canlin Guo, Didan Deng, Zifeng Mo, Cong Wang, James Cheng, Roger Wang, Hongsheng Liu
}
,
 
journal
=
{
arXiv preprint arXiv:2602.02204
}
,
 
year
=
{
2026
}

}

## Join the Community

Feel free to ask questions, provide feedbacks and discuss with fellow users of vLLM-Omni in#sig-omnislack channel atslack.vllm.aior vLLM user forum atdiscuss.vllm.ai.

## Star History

## License

Apache License 2.0, as found in theLICENSEfile.

## About

A framework for efficient model inference with omni-modality models

docs.vllm.ai/projects/vllm-omni

### Topics

 inference

 pytorch

 transformer

 image-generation

 diffusion

 model-serving

 multimodal

 video-generation

 audio-generation

### Resources

 Readme

 

### License

 Apache-2.0 license
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

3.4k

 stars
 

### Watchers

37

 watching
 

### Forks

578

 forks
 

 Report repository

 

## Releases8

v0.16.0

 Latest

 

Feb 28, 2026

 

+ 7 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python99.4%
* Other0.6%