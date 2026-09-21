---
title: 'GitHub - FlashML-org/FreeToken: FreeToken brings datacenter-scale model serving to your desktop. Run massive models locally, fast and efficiently. · GitHub'
url: https://github.com/FlashML-org/FreeToken
site_name: github
content_file: github-github-flashml-orgfreetoken-freetoken-brings-datac
fetched_at: '2026-09-21T16:50:00.675205'
original_url: https://github.com/FlashML-org/FreeToken
author: FlashML-org
description: FreeToken brings datacenter-scale model serving to your desktop. Run massive models locally, fast and efficiently. - FlashML-org/FreeToken
---

FlashML-org

 

/

FreeToken

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.3k
* Star13.4k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

83 Commits
83 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
assets
assets
 
 
benchmarks
benchmarks
 
 
docs
docs
 
 
freetoken-kernel-cache
freetoken-kernel-cache
 
 
python/
freetoken
python/
freetoken
 
 
scripts
scripts
 
 
tests
tests
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
install.sh
install.sh
 
 
pyproject.toml
pyproject.toml
 
 
setup.py
setup.py
 
 
View all files

## Repository files navigation

|Download|Paper|Developer Slack|Community Discord|Community WeChat|

Unlock datacenter-class intelligence on the hardware you already own — Run 290B+ frontier MoE models locally on your gaming PC at blistering interactive speeds.

## About

FreeToken is an edge-native Mixture-of-Experts (MoE) serving engine designed for running frontier-scale open-weight models on personal and consumer hardware. It treats heterogeneous edge resources—GPUs, CPUs, host memory, and interconnects—as a unified, elastic inference platform. Its core features include:

* Fast Edge-Native Runtime: Provides efficient MoE serving with bandwidth-adaptive CPU–GPU co-execution ($q^\star$policy), full-layer double-buffered prefill streaming, global LRU expert caching, graph-compatible execution, and the FTW fast weight format.
* Semantic-Aware Caching: Features semantic anchor checkpoints for recurrent state and KV caches, allowing agentic context edits (e.g., tool calls, thinking blocks) to avoid redundant context recomputation.
* Elastic Memory Management: Supports dynamic, runtime VRAM re-allocation between expert caches and KV memory without engine restarts or weight reloading.
* Broad MoE & Ecosystem Support: Supports frontier open-weight MoE models (e.g., DeepSeek-V4-Flash, Qwen3.6-35B-A3B, GLM-5.2) across various parameter scales and quantization formats (e.g., MXFP4, NVFP4, FP8, BF16), with Anthropic/OpenAI-compatible APIs for seamless integration with real-world coding and tool-calling agents (e.g., Codex, Claude Code, OpenCode, OpenClaw, DeepSeek Harness).
* Diverse Consumer Hardware: Scales across consumer laptops, gaming desktops, and workstation GPUs, with native support for NVIDIA RTX 30, RTX 40, and RTX 50 series GPUs.

## Getting Started

### Desktop app

Download FreeToken for Windows or Linux atflashml.ai. It sets the engine up for you and gives you a GUI for running models, chatting, and tuning the engine.

### CLI

Install FreeToken withuv(recommended) or pip:

uv pip install 
"
freetoken[accel]
"

Or build from source:

git clone https://github.com/FlashML-org/FreeToken.git 
&&
 
cd
 FreeToken
uv venv 
&&
 
source
 .venv/bin/activate
uv pip install -e 
"
.[accel]
"

For More details:

* Install FreeToken
* Quick start
* Supported models
* CLI reference
* Repairing old FTW checkpoints

## Citation

If you use FreeToken for your research, please cite ourpaper:

@article
{
yang2026freetoken
,
 
title
=
{
FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution
}
,
 
author
=
{
Yang, Shuo and Fan, Xiaoze and Pan, Melissa and Xi, Haocheng and Wang, Zhe and Sun, Shanlin and Keutzer, Kurt and Han, Song and Zaharia, Matei and Xu, Chenfeng and Stoica, Ion
}
,
 
journal
=
{
arXiv preprint arXiv:2608.16157
}
,
 
year
=
{
2026
}

}

## Acknowledgment

FreeToken was deeply inspired bymini-sglang, and
learned the design and reused code from the following projects:SGLang,vLLM,FlashInfer,flash-linear-attention,LightLLMandllama.cpp.

## License

Apache License 2.0.