---
title: 'GitHub - radixark/miles: Miles is an enterprise-facing reinforcement learning framework for LLM and VLM post-training, forked from and co-evolving with slime. · GitHub'
url: https://github.com/radixark/miles
site_name: github
content_file: github-github-radixarkmiles-miles-is-an-enterprise-facing
fetched_at: '2026-09-04T14:47:52.339119'
original_url: https://github.com/radixark/miles
author: radixark
description: Miles is an enterprise-facing reinforcement learning framework for LLM and VLM post-training, forked from and co-evolving with slime. - radixark/miles
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 radixark

 

/

miles

Public

* NotificationsYou must be signed in to change notification settings
* Fork440
* Star2.5k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

2,127 Commits
2,127 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.agents
.agents
 
 
.claude
.claude
 
 
.github
.github
 
 
docker
docker
 
 
docs
docs
 
 
examples
examples
 
 
miles
miles
 
 
miles_plugins
miles_plugins
 
 
scripts
scripts
 
 
tests
tests
 
 
tools
tools
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
AGENTS.md
AGENTS.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
pyproject.toml
pyproject.toml
 
 
requirements.txt
requirements.txt
 
 
setup.py
setup.py
 
 
train.py
train.py
 
 
train_async.py
train_async.py
 
 
train_multi_lora_async.py
train_multi_lora_async.py
 
 
View all files

## Repository files navigation

### Enterprise-Grade Reinforcement Learning for Large-Scale Model Post-Training

|Website|Documentation|Quick Start|Supported Models|Miles Diffusion|Blog|Slack(#miles-rl) |

## News

* [2026/08] 🔥 Miles v0.1 is released! Read the blog post here:Miles v0.1: Production-level Post-training.
* [2026/07] Towards Blackwell-Native 8-bit and 4-bit RL: End-to-End MXFP8 and NVFP4 RL in Miles (blog).
* [2026/07] 🔥 SGLang and Miles add day-0 support for Kimi K3 (blog).
* [2026/07] On-policy distillation lands in Miles (blog).
* [2026/07] 🔥 SGLang and Miles add day-0 support for Inkling, a frontier multimodal model (blog).
* [2026/07] DeepSeek-V4 Flash RL training comes to AMD Instinct MI355X with Miles (blog).
* [2026/06] SGLang and Miles add day-0 support for NVIDIA Nemotron 3 Ultra (blog).
* [2026/05] No token left behind: token-in-token-out in Miles (blog).
* [2026/04] Updating 1 T parameters in seconds: P2P weight transfer in large-scale distributed RL (blog).
* [2026/04] 🔥 DeepSeek-V4 on day 0: from fast inference to verified RL with SGLang and Miles (blog).

## About

Miles is a high-performance, enterprise-ready reinforcement learning framework forlarge-scale model post-training. It pairsSGLangfor high-throughput rollout withMegatron-LMfor
scalable training, and ships the precision, stability, and observability features an RL run
needs at trillion-parameter scale. A PyTorch FSDP2 backend is available for runs that would
rather train the HuggingFace implementation as-is, though the recipes, the parallelism, and
the largest models all live on Megatron-LM. SeeTraining Backends.

"A journey of a thousand miles begins with a single rollout."

### Performance

* Fully async RL.Rollout and training workers are decoupled, with configurable on- and
off-policy schedules, a pipeline tuned for fewer bubbles, and customizable async rollout
and eval modes. SeeFully Async RL.
* Fast agentic rollout.Generation runs onSGLangbehind a router that spreads requests across engines, preserves per-request metadata, and
health-checks the fleet. Tuned for multi-turn agentic workloads.
* Fast weight updates.New weights reach the engines in-loop in seconds, even on a
trillion-parameter model such as Kimi-K2.6, withP2P RDMAas the fast path
for disaggregated setups.
* Low-precision training.MXFP8 and NVFP4training with a numerically stable RL recipe that reduces precision-induced divergence.
FP8,INT4 QAT, BF16, and FP16 are also
supported.
* LoRA and multi-LoRA.Low-rank adapterstrain frontier-scale models on a fraction of the GPUs, and the same adapters load straight
into SGLang for rollout.

### Correctness and resilience

* Token-in-token-out (TITO).Supported forevery model and every black-box harness,
with no detokenize/retokenize round-trip between rollout and training.
* Rollout Routing Replay (R3).Expert routing recorded during rollout isreplayed in the trainer's forward pass,
removing the MoE routing mismatch that destabilizes large runs, with compute and
communication overlapped to keep the cost down.
* Fault tolerance.When an SGLang engine dies, Milesrecovers it and resumes the run in place:
no restart, no pause.

### What Miles runs

* Day-0 model support.DeepSeek-V4, Kimi-K3, GLM-5.2, Inkling, and Nemotron landed on
release day. Beyond day 0, nearly every frontier model runs on Miles, including Kimi-K2.6
and Qwen3.5. SeeModels.
* Extensive hardware support.NVIDIA GB300, GB200, B300, B200, H200, H100, and A100, and
AMD MI300X, MI325, MI350, and MI355X via ROCm. SeeInstallationfor per-GPU status and the container image for each.
* Wide recipe support.GRPO, GSPO, PPO, and REINFORCE++ for RL, plus SFT andon-policy distillation.
* Agentic environments.Train coding and computer-use agents through connectors for
Harbor, HUD, NeMo Gym, OpenEnv, Verifiers, and more, each plugging into the rollout
layer that fits it, with task sandboxes on AgentENV, Daytona, E2B, or Modal. SeeAgentic Environments.
* Diffusion models.Flow-GRPO, DiffusionNFT and SFT on an sglang-diffusion rollout
engine and an FSDP2 trainer, inMiles-diffusion.

## Getting Started

* Install Miles
* Quick Start
* Supported Models
* Core Concepts
* Launch Script Walkthrough
* Training Backends
* Contribution Guide

## Acknowledgment

Miles was forked fromslime, and integratesSGLang,Megatron-LM, andtorch_memory_saver.

Miles is shaped by the teams that build on it and support its development,
from hardware and cloud to model labs, agent infrastructure, and academia:

## Citation

If Miles is useful in your research or your product, please cite it:

@misc
{
miles2026
,
 
title
 = 
{
Miles: Enterprise-Grade Reinforcement Learning for Large-Scale Model Post-Training
}
,
 
author
 = 
{
Miles Team
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
\url{https://github.com/radixark/miles}
}

}