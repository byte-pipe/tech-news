---
title: 'GitHub - inclusionAI/AReaL: Lightning-Fast RL for LLM Reasoning and Agents. Made Simple & Flexible. · GitHub'
url: https://github.com/inclusionAI/AReaL
site_name: github
content_file: github-github-inclusionaiareal-lightning-fast-rl-for-llm
fetched_at: '2026-03-05T11:16:00.791460'
original_url: https://github.com/inclusionAI/AReaL
author: inclusionAI
description: Lightning-Fast RL for LLM Reasoning and Agents. Made Simple & Flexible. - inclusionAI/AReaL
---

inclusionAI



/

AReaL

Public

* NotificationsYou must be signed in to change notification settings
* Fork335
* Star3.9k




 
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

741 Commits
741 Commits
.claude
.claude
 
 
.github
.github
 
 
.opencode
.opencode
 
 
areal
areal
 
 
assets
assets
 
 
benchmark
benchmark
 
 
blog
blog
 
 
docs
docs
 
 
examples
examples
 
 
notebook
notebook
 
 
tests
tests
 
 
.clang-format
.clang-format
 
 
.dockerignore
.dockerignore
 
 
.gitignore
.gitignore
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Dockerfile
Dockerfile
 
 
LEGAL.md
LEGAL.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
ROADMAP.md
ROADMAP.md
 
 
pyproject.toml
pyproject.toml
 
 
skills-lock.json
skills-lock.json
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

# AReaL: A Large-Scale Asynchronous Reinforcement Learning System

|Paper|Documentation|Ask DeepWiki|🤗 Models & Data|WeChat (微信) Group|

AReaL is an open-sourcefully asynchronousreinforcement learning training system
for largereasoning and agentic models, developed by members from Tsinghua IIIS and
the AReaL Team at Ant Group. Built upon the open-source projectReaLHF, we are fully committed to
open-source principles by providing the training details, data, and infrastructure
required to reproduce our results, along with the models themselves. AReaL aims to help
everyone build their own AI agents easily and affordably. Our team loves milk tea
because it's delicious, customizable, and affordable—we hope you enjoy our project just
as much as you'd enjoy real milk tea. Cheers!

AReaL Highlights

* ⚡Flexibility: Seamless customization foragentic RLandonline RL trainingby simply replacing thebase_url.
* 📈Scalability:Stablefully asynchronous RL training withindustry-leading
speed.
* ✨Cutting-Edge Performance: State-of-the-artmath,coding,search, andcustomer serviceagents.

## 📰 News

[2026/03/02]We providea complete exampleto train your
own 🦞 OpenClaw agent by simply replacing thebase_urlandapi_keywith AReaL's RL
service - no complicated dependencies, no code changes, works with any agentic runtime!

[2026/02/06]We are delighted to introduceAReaL-SEA, a self-evolving data
synthesis engine. Combined with RL training on AReaL, the 235B MoE model surpasses GPT 5
and achieves comparable performance with Gemini 3.0 Pro on$\tau^2$-bench! Check out
thepaper,model,data, andcode.

[2026/01/15]Congrats to our friends atCAMEL-AIfor
open-sourcingSETA, their terminal agent RL project
trained with AReaL! Check outtheir training workflowand theannouncement on X.

📋 Previous Releases

[2026/01/01]Happy New Year! Thanks to the outstanding contribution from
@HwVanICI, we are excited to officially announce stable support for AReaL training onAscend NPU devices! The code is actively maintained and continuously updated in theascendbranch. Check outour documentationto get started, and feel free to report any issues!

[2025/08/30]Introducing ASearcher, a state-of-the-art search agent built with
AReaL's end-to-end asynchronous RL training. Check out thepaperand
theopen-source repository!

[2025/07/31] (AReaL-lite)We introduce AReaL-lite, alightweightversion of
AReaL designed specifically for AI researchers and rapid prototyping. AReaL-lite
features analgorithm-firstAPI design that prioritizes ease of use and algorithm
development, while natively supportingfully asynchronous agentic RL. With 80% fewer
lines of code, AReaL-lite maintains 90% of AReaL's performance and core functionality.
Check outour AReaL-lite design documentationandthe quickstart guideto
begin your journey withAReaL-lite!

[2025/06/03] (v0.3, boba²)We releaseboba²(double-boba) for fully
asynchronous RL training, which achieves2.77× speedup while delivering comparable or
superior training performancecompared to synchronous systems. Furthermore,
asynchronous RL significantly simplifies multi-turn agentic RL training setup! Check outour v0.3 overview blogand theresearch paper.

[2025/03/31] (v0.2, boba)Introducing our milestone release—boba! Please call it
A-ReaL-boba! This release features significantly faster training with SGLang support and
state-of-the-art 7B and 32B models for mathematical reasoning. Check out ourv0.2 technical blog.

[2025/02/24] (v0.1)Our initial release includes reproducible results for 1.5B and
7B Large Reasoning Models (LRMs). Check out ourv0.1 technical blog.

## 🚀 Getting Started

First, install the package:

git clone https://github.com/inclusionAI/AReaL

cd
 AReaL
pip install uv
uv sync --extra cuda

Our training scripts automatically download the required dataset (openai/gsm8k) and
model (Qwen/Qwen2-1.5B-Instruct). To run on a single node:

python3 examples/math/gsm8k_rl.py --config examples/math/gsm8k_grpo.yaml scheduler.type=local

To run on a Ray cluster with 2 nodes and 8 GPUs per node (remember to update paths in
the YAML file to point to your shared storage):

python3 examples/math/gsm8k_rl.py --config examples/math/gsm8k_grpo.yaml \
 cluster.n_nodes=2 cluster.n_gpus_per_node=8 \
 scheduler.type=ray

For comprehensive setup instructions, seeour quickstart guide.

## 📚 Examples

### Math & Reasoning

Task

Description

Performance

Math

GSM8K math reasoning with GRPO, PPO, DAPO, REINFORCE, RLOO, LitePPO, DR-GRPO, GSPO, and more

-

Multi-Turn Math

Multi-turn math agent with reward discounting across turns

Training Curve

LoRA Math

Parameter-efficient math training with LoRA (SGLang/vLLM backends)

-

Countdown

Countdown numbers game with custom rewards

Training Curve

### Agentic RL

Task

Description

Performance

General Agent

General agentic training with any agentic frameworks

Guide

Tau2 Customer Service

Customer service agent on Tau2-Bench (retail, airline, telecom)

Paper

Search Agent

End-to-end search agent with Tongyi-DeepResearch workflow

Training Curve

Tool-Integrated Reasoning

Multi-turn tool calling during reasoning (Python executor, calculator)

Training Curve

OpenAI Agents Integration

Integration with OpenAI Agents SDK for agentic workflows

-

CAMEL-AI Integration

Integration with CAMEL-AI framework for agentic RL

-

### Vision-Language Models

Task

Description

Performance

VLM

Geometry3K and CLEVR Count 70K visual reasoning with GRPO

-

VLM on NPU

VLM training on Huawei NPU hardware

Benchmark Results

### Alignment & Infrastructure

Task

Description

Performance

RLHF Reward Modeling

Bradley-Terry reward modeling on Anthropic HH-RLHF

Training Curve

SkyPilot Deployment

Cloud deployment with SkyPilot (GCP, AWS, Kubernetes)

Screenshots

## 🔧 Support Matrix

### 🧠 Algorithms

All RL algorithms support both asynchronous and synchronous versions by settingmax_head_offpolicyness=0. SeeAsynchronous RL Guide.

Algorithm

Documentation

Paper

Configuration

GRPO

📖 Docs

📄 Paper

🔗 GSM8K Example

GSPO

📖 Docs

📄 Paper

🔗 GSM8K Example

PPO

📖 Docs

📄 Paper

🔗 GSM8K Example

DAPO

📖 Docs

📄 Paper

🔗 GSM8K Example

LitePPO

📖 Docs

📄 Paper

🔗 GSM8K Example

Dr.GRPO

📖 Docs

📄 Paper

🔗 GSM8K Example

REINFORCE++

-

📄 Paper

🔗 GSM8K Example

RLOO

📖 Docs

📄 Paper

🔗 GSM8K Example

SAPO

📖 Docs

📄 Paper

🔗 GSM8K Example

M2PO

📖 Docs

📄 Paper

🔗 GSM8K Example

RLHF Reward Modeling

-

-

🔗 RLHF Example

SFT

-

-

🔗 GSM8K Example

### Models

Model Family

Megatron

PyTorch FSDP

PyTorch Archon

Notes

Qwen2/3

✅

✅

✅

-

Qwen3-MoE

✅

✅

✅

-

Qwen2.5-VL

❌

✅

❌

Vision-language model

Qwen3-VL

❌

✅

❌

Vision-language model

Gemma 3

❌

✅

❌

Vision-language model

Other Hugging Face LLM

❌

✅

❌

Compatibility depending on the version of
transformers

Check theAI Coding Assistant GuideandArchon Referencefor how to integrate new models into AReaL.

### Training Backends

Backend

DP

Tensor Parallel

Sequence Parallel within TP

Context Parallel

Pipeline Parallel

Expert Parallel

1D Sequence Packing

LoRA

Megatron

✅ (ZeRO-1)

✅

✅

✅

✅

✅

✅

❌

PyTorch FSDP

✅ (FSDP2)

✅

✅

✅

❌

❌

✅

✅

PyTorch Archon

✅ (FSDP2)

✅

✅

✅

✅

✅

✅

❌

### Inference Backends

Backend

Tensor Parallel

Context Parallel

Pipeline Parallel

Data Parallel Attention

Expert Parallel

vLLM

✅

❓

✅

❓

❓

SGLang

✅

❌

❌

✅

✅

## 📖 Resources

### Tutorial

* Installation
* Quickstart
* Agentic RL
* Evaluation
* Large MoE with Megatron
* Large MoE with PyTorch Archon

### Code Walkthrough

* Running GRPO on GSM8K dataset

### Best Practices

* Improving Algorithm Performance
* Agent Workflow Best Practices
* Debugging
* Handling OOM Issues
* Performance Profiling

### Customization

* Customize Dataset
* Customize Agentic/RVLR Rollout Workflows

### Algorithms

* Asynchronous RL Explained
* PPO, GRPO, and Related Algorithms
* M2PO

### Reference

* CLI Configurations
* Checkpointing
* Metrics Tracking
* Allocation Mode
* Rollout Workflow
* Agent Workflow
* AI-Assisted Development

## 🤝 Contributing

We warmly welcome contributions from the community! Whether you're fixing bugs, adding
features, improving documentation, or helping others, your contribution is valued.
Please check ourContributing Guidefor detailed information.

#
 Fork and clone the repository

git clone https://github.com/YOUR-USERNAME/AReaL

cd
 AReaL

#
 Install uv and sync dependencies

pip install uv

#
 Use `--extra cuda` on Linux with CUDA for full functionality

uv sync --extra cuda --group dev

#
 Or without CUDA support

#
 uv sync --group dev

#
 Set up pre-commit hooks for automatic formatting

pre-commit install

#
 Make changes

git checkout -b feat/gpt-o5
git add
.

#
 `git commit` will automatically format your file

git commit -m
"
Implement gpt-o5 training loop
"

git push

## 🗺️ Future Roadmap

* Full Roadmap
* 2025 Q4 Roadmap

AReaL is under active development with planned minor releases weekly and major releases
monthly. We warmly welcome community engagement and contributions. We are alsoactively hiring interns and full-time employeeswith open positions in both the US
and China.

## 🙏 Acknowledgments

We gratefully acknowledge that major contributors are from the AReaL Team at the
Institute for Interdisciplinary Information Sciences (IIIS), Tsinghua University and Ant
Group.

We have also received invaluable assistance from the following groups (listed
alphabetically):

* The Data Intelligence Lab at Ant Research for their data support
* @HwVanICI for support on vLLM, LoRA, NPU integration, and more
* TheRelaxed System Labat HKUST for seamless
collaboration on numerous system-related aspects
* TheSGLang teamfor supporting custom weight
update features and their contributions during AReaL-lite development
* The Super Computing Technology (SCT) team at Ant Group for their expertise in
large-scale cluster operations and maintenance
* Special thanks to @Lyken17 for providing valuable suggestions throughout the API
design process

We also deeply appreciate all pioneering work from the community, particularly theReaLHFproject from OpenPsi Inc. and other
outstanding projects, including but not limited toDeepScaleR,Open-Reasoner-Zero,OpenRLHF,VeRL,SGLang,QwQ,Light-R1, andDAPO.

## 📄 Citation

@inproceedings
{
mei2025real
,

author
 =
{
Mei, Zhiyu and Fu, Wei and Li, Kaiwei and Wang, Guangju and Zhang, Huanchen and Wu, Yi
}
,

title
 =
{
ReaL: Efficient RLHF Training of Large Language Models with Parameter Reallocation
}
,

booktitle
 =
{
Proceedings of the Eighth Conference on Machine Learning and Systems,

 MLSys 2025, Santa Clara, CA, USA, May 12-15, 2025
}
,

publisher
 =
{
mlsys.org
}
,

year
 =
{
2025
}
,
}

@misc
{
fu2025areal
,

title
=
{
AReaL: A Large-Scale Asynchronous Reinforcement Learning System for Language Reasoning
}
,

author
=
{
Wei Fu and Jiaxuan Gao and Xujie Shen and Chen Zhu and Zhiyu Mei and Chuyi He and Shusheng Xu and Guo Wei and Jun Mei and Jiashu Wang and Tongkai Yang and Binhang Yuan and Yi Wu
}
,

year
=
{
2025
}
,

eprint
=
{
2505.24298
}
,

archivePrefix
=
{
arXiv
}
,

primaryClass
=
{
cs.LG
}
,

url
=
{
https://arxiv.org/abs/2505.24298
}
,
}

## About

Lightning-Fast RL for LLM Reasoning and Agents. Made Simple & Flexible.

inclusionai.github.io/AReaL/

### Topics

 agent

 reinforcement-learning

 rl

 machine-learning-systems

 mlsys

 llm

 llm-agent

 llm-reasoning

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

3.9k

 stars


### Watchers

33

 watching


### Forks

335

 forks


 Report repository



## Releases21

v1.0.1

 Latest



Mar 4, 2026



+ 20 releases

### Uh oh!

There was an error while loading.Please reload this page.





## Contributors

### Uh oh!

There was an error while loading.Please reload this page.





## Languages

* Python77.7%
* Jupyter Notebook22.2%
* Other0.1%
