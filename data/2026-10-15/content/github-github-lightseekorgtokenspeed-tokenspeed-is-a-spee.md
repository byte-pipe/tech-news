---
title: 'GitHub - lightseekorg/tokenspeed: TokenSpeed is a speed-of-light LLM inference engine. · GitHub'
url: https://github.com/lightseekorg/tokenspeed
site_name: github
content_file: github-github-lightseekorgtokenspeed-tokenspeed-is-a-spee
fetched_at: '2026-10-15T15:30:37.609752'
original_url: https://github.com/lightseekorg/tokenspeed
author: lightseekorg
description: TokenSpeed is a speed-of-light LLM inference engine. - lightseekorg/tokenspeed
---

main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

1,824 Commits
1,824 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
.skills
.skills
 
 
assets
assets
 
 
docker
docker
 
 
docs
docs
 
 
python
python
 
 
requirements
requirements
 
 
test
test
 
 
tokenspeed-kernel-amd
tokenspeed-kernel-amd
 
 
tokenspeed-kernel-npu
tokenspeed-kernel-npu
 
 
tokenspeed-kernel
tokenspeed-kernel
 
 
tokenspeed-mla
tokenspeed-mla
 
 
tokenspeed-scheduler
tokenspeed-scheduler
 
 
.dockerignore
.dockerignore
 
 
.gitignore
.gitignore
 
 
.isort.cfg
.isort.cfg
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
ACKNOWLEDGEMENTS.md
ACKNOWLEDGEMENTS.md
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
GOVERNANCE.md
GOVERNANCE.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
REVIEW.md
REVIEW.md
 
 
SECURITY.md
SECURITY.md
 
 
View all files

## Repository files navigation

TokenSpeed is a speed-of-light LLM inference engine designed foragentic workloads, with TensorRT-LLM-level performance and vLLM-level usability. The goal is to be the most performant inference engine for production agentic workloads.

Core components:

* Scheduler: C++ control plane and Python execution plane. Request
lifecycle, KV cache ownership, and overlap timing are encoded as a
finite-state machine, with safe KV resource reuse enforced by the type system at compile time.
* Kernels: pluggable, layered kernel system with a portable public API and
a centralized registry including one of the fastestMLA(Multi-head Latent Attention) implementations on Blackwell for agentic workloads.
* Entrypoint: SMG-integrated AsyncLLM for low-overhead CPU-side request
handling.

## Differentiation

TokenSpeed takes a fundamentally different architectural approach from existing LLM inference engines. ThePyTorch Foundation highlighted these architectural differentiatorswhenwelcoming TokenSpeedto the PyTorch Ecosystem Landscape:

TokenSpeed is an open source LLM inference engine and the first to separate the control plane from the execution plane. The control plane is implemented in C++ as a finite-state machine, using the type system to enforce safe resource management, including request lifecycles and KV cache state, at compile time rather than runtime. The execution plane is implemented in Python, enabling fast iteration and lowering the cognitive load for researchers and engineers. This architecture combines strong correctness guarantees in the core scheduling system with the development velocity of a high-level execution layer.

TokenSpeed also treats kernels as a first-class, modular subsystem, separating them from the core engine through a portable public API, centralized registry and selection model, and an extensible plugin mechanism for heterogeneous accelerators.

More importantly, TokenSpeed is theSwitzerlandof open-source LLM inference engines: neutral because it's backed by the non-profitLightSeek Foundationrather than a commercial company, withserious hardware and engineering supportfrom vendors like NVIDIA and AMD.

## News

* [2026/10] 🔥 685 tokens/s per user: serving Qwen3.8-Flash-Next on NVIDIA GB300 with TokenSpeed. [blog]
* [2026/10] 🔥 Advancing Kimi K3 inference on AMD Instinct MI355X GPUs with TokenSpeed. [AMD blog]
* [2026/09] Kimi K3 Optimization on GB300 — Part I. [blog]
* [2026/08]Qwen3.8 Flash Nextat Day 0 andGLM 5.3 Flashat Day 0.
* [2026/08]Qwen3.8at Day 0: 2.4T-Scale Inference with TokenSpeed. [blog]
* [2026/08] TokenSpeed joins thePyTorch Ecosystem.
* [2026/07]Kimi K3at Day 0: Frontier Model Enablement on Leading Platforms with TokenSpeed. [blog]
* [2026/07]TML Inklingat Day 0: FP4 Inference on NVIDIA andAMDwithTokenSpeed. [blog]
* [2026/06] Deep dive into the design and optimization of TokenSpeed-Kernel. [PyTorch blog]
* [2026/05] 🚀 TokenSpeed hits 580 TPS on Qwen3.5-397B-A17B for agentic workloads. [PyTorch blog]
* [2026/05] TokenSpeed announced — a speed-of-light LLM inference engine for agentic workloads. [blog]

## Blogs and talks

For technical blogs, conference talks, and engineering articles from LightSeek Foundation, visit theLightSeek Blog.

## Sponsors and partners

LightSeek's work is advanced by the support ofsponsors and partnersacross the AI ecosystem.

## Performance comparison

TokenSpeed vs. TensorRT-LLM Pareto curves on agentic workloads (Kimi K2.5, B200)

## Documentation

Start here:

* Docs Index
* Getting Started
* Launching a Server
* Model Recipes
* Server Parameters
* Compatible Parameters
* Parallelism

## Citation

@misc
{
tokenspeed2026
,
 
author
 = 
{
{TokenSpeed Team}
}
,
 
title
 = 
{
{TokenSpeed}: A Speed-of-Light {LLM} Inference Engine
}
,
 
year
 = 
{
2026
}
,
 
howpublished
 = 
{
\url{https://github.com/lightseekorg/tokenspeed}
}

}