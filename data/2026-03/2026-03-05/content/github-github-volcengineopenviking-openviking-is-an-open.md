---
title: 'GitHub - volcengine/OpenViking: OpenViking is an open-source context database designed specifically for AI Agents(such as openclaw). OpenViking unifies the management of context (memory, resources, and skills) that Agents need through a file system paradigm, enabling hierarchical context delivery and self-evolving. · GitHub'
url: https://github.com/volcengine/OpenViking
site_name: github
content_file: github-github-volcengineopenviking-openviking-is-an-open
fetched_at: '2026-03-05T11:16:00.177889'
original_url: https://github.com/volcengine/OpenViking
author: volcengine
description: OpenViking is an open-source context database designed specifically for AI Agents(such as openclaw). OpenViking unifies the management of context (memory, resources, and skills) that Agents need through a file system paradigm, enabling hierarchical context delivery and self-evolving. - volcengine/OpenViking
---

volcengine

 

/

OpenViking

Public

* NotificationsYou must be signed in to change notification settings
* Fork357
* Star4.7k

 
 
 
 
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

280 Commits
280 Commits
.github
.github
 
 
bot
bot
 
 
crates/
ov_cli
crates/
ov_cli
 
 
docs
docs
 
 
examples
examples
 
 
openviking
openviking
 
 
openviking_cli
openviking_cli
 
 
src
src
 
 
tests
tests
 
 
third_party
third_party
 
 
.clang-format
.clang-format
 
 
.gitignore
.gitignore
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
CONTRIBUTING_CN.md
CONTRIBUTING_CN.md
 
 
Cargo.toml
Cargo.toml
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
MANIFEST.in
MANIFEST.in
 
 
README.md
README.md
 
 
README_CN.md
README_CN.md
 
 
docker-compose.yml
docker-compose.yml
 
 
pyproject.toml
pyproject.toml
 
 
setup.py
setup.py
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

### OpenViking: The Context Database for AI Agents

English /中文

Website·GitHub·Issues·Docs

👋 Join our Community

📱Lark Group·WeChat·Discord·X

## Overview

### Challenges in Agent Development

In the AI era, data is abundant, but high-quality context is hard to come by. When building AI Agents, developers often face these challenges:

* Fragmented Context: Memories are in code, resources are in vector databases, and skills are scattered, making them difficult to manage uniformly.
* Surging Context Demand: An Agent's long-running tasks produce context at every execution. Simple truncation or compression leads to information loss.
* Poor Retrieval Effectiveness: Traditional RAG uses flat storage, lacking a global view and making it difficult to understand the full context of information.
* Unobservable Context: The implicit retrieval chain of traditional RAG is like a black box, making it hard to debug when errors occur.
* Limited Memory Iteration: Current memory is just a record of user interactions, lacking Agent-related task memory.

### The OpenViking Solution

OpenVikingis an open-sourceContext Databasedesigned specifically for AI Agents.

We aim to define a minimalist context interaction paradigm for Agents, allowing developers to completely say goodbye to the hassle of context management. OpenViking abandons the fragmented vector storage model of traditional RAG and innovatively adopts a"file system paradigm"to unify the structured organization of memories, resources, and skills needed by Agents.

With OpenViking, developers can build an Agent's brain just like managing local files:

* Filesystem Management Paradigm→Solves Fragmentation: Unified context management of memories, resources, and skills based on a filesystem paradigm.
* Tiered Context Loading→Reduces Token Consumption: L0/L1/L2 three-tier structure, loaded on demand, significantly saving costs.
* Directory Recursive Retrieval→Improves Retrieval Effect: Supports native filesystem retrieval methods, combining directory positioning with semantic search to achieve recursive and precise context acquisition.
* Visualized Retrieval Trajectory→Observable Context: Supports visualization of directory retrieval trajectories, allowing users to clearly observe the root cause of issues and guide retrieval logic optimization.
* Automatic Session Management→Context Self-Iteration: Automatically compresses content, resource references, tool calls, etc., in conversations, extracting long-term memory, making the Agent smarter with use.

## Quick Start

### Prerequisites

Before starting with OpenViking, please ensure your environment meets the following requirements:

* Python Version: 3.10 or higher
* Go Version: 1.19 or higher (Required for building AGFS components)
* C++ Compiler: GCC 9+ or Clang 11+ (Required for building core extensions)
* Operating System: Linux, macOS, Windows
* Network Connection: A stable network connection is required (for downloading dependencies and accessing model services)

### 1. Installation

#### Python Package

pip install openviking --upgrade --force-reinstall

#### Rust CLI (Optional)

curl -fsSL https://raw.githubusercontent.com/volcengine/OpenViking/main/crates/ov_cli/install.sh 
|
 bash

Or build from source:

cargo install --git https://github.com/volcengine/OpenViking ov_cli

### 2. Model Preparation

OpenViking requires the following model capabilities:

* VLM Model: For image and content understanding
* Embedding Model: For vectorization and semantic retrieval

#### Supported VLM Providers

OpenViking supports three VLM providers:

Provider

Description

Get API Key

volcengine

火山引擎豆包模型

Volcengine Console

openai

OpenAI 官方 API

OpenAI Platform

litellm

统一调用多种第三方模型 (Anthropic, DeepSeek, Gemini, vLLM, Ollama, etc.)

See 
LiteLLM Providers

💡Tip:

* litellm支持通过统一接口调用多种模型，model 字段需遵循LiteLLM 格式规范
* 系统自动检测常见模型（如claude-*,deepseek-*,gemini-*,hosted_vllm/*,ollama/*等），其他模型需按 LiteLLM 格式填写完整前缀

#### Provider-Specific Notes

Volcengine (Doubao)

Volcengine supports both model names and endpoint IDs. Using model names is recommended for simplicity:

{
 
"vlm"
: {
 
"provider"
: 
"
volcengine
"
,
 
"model"
: 
"
doubao-seed-2-0-pro-260215
"
,
 
"api_key"
: 
"
your-api-key
"
,
 
"api_base"
: 
"
https://ark.cn-beijing.volces.com/api/v3
"

 }
}

You can also use endpoint IDs (found inVolcengine ARK Console):

{
 
"vlm"
: {
 
"provider"
: 
"
volcengine
"
,
 
"model"
: 
"
ep-20241220174930-xxxxx
"
,
 
"api_key"
: 
"
your-api-key
"
,
 
"api_base"
: 
"
https://ark.cn-beijing.volces.com/api/v3
"

 }
}

OpenAI

Use OpenAI's official API:

{
 
"vlm"
: {
 
"provider"
: 
"
openai
"
,
 
"model"
: 
"
gpt-4o
"
,
 
"api_key"
: 
"
your-api-key
"
,
 
"api_base"
: 
"
https://api.openai.com/v1
"

 }
}

You can also use a custom OpenAI-compatible endpoint:

{
 
"vlm"
: {
 
"provider"
: 
"
openai
"
,
 
"model"
: 
"
gpt-4o
"
,
 
"api_key"
: 
"
your-api-key
"
,
 
"api_base"
: 
"
https://your-custom-endpoint.com/v1
"

 }
}

LiteLLM (Anthropic, DeepSeek, Gemini, Qwen, vLLM, Ollama, etc.)

LiteLLM provides unified access to various models. Themodelfield should follow LiteLLM's naming convention. Here we use Claude and Qwen as examples:

Anthropic:

{
 
"vlm"
: {
 
"provider"
: 
"
litellm
"
,
 
"model"
: 
"
claude-3-5-sonnet-20240620
"
,
 
"api_key"
: 
"
your-anthropic-api-key
"

 }
}

Qwen (DashScope):

{
 
"vlm"
: {
 
"provider"
: 
"
litellm
"
,
 
"model"
: 
"
dashscope/qwen-turbo
"
, 
// see https://docs.litellm.ai/docs/providers/dashscope for more details

 
"api_key"
: 
"
your-dashscope-api-key
"
,
 
"api_base"
: 
"
https://dashscope.aliyuncs.com/compatible-mode/v1
"

 }
}

💡Tip for Qwen:

* ForChina/Beijingregion, useapi_base:https://dashscope.aliyuncs.com/compatible-mode/v1
* ForInternationalregion, useapi_base:https://dashscope-intl.aliyuncs.com/compatible-mode/v1

Common model formats:

Provider

Model Example

Notes

Anthropic

claude-3-5-sonnet-20240620

Auto-detected, uses 
ANTHROPIC_API_KEY

DeepSeek

deepseek-chat

Auto-detected, uses 
DEEPSEEK_API_KEY

Gemini

gemini-pro

Auto-detected, uses 
GEMINI_API_KEY

Qwen

dashscope/qwen-turbo

Set 
api_base
 based on region (see above)

OpenRouter

openrouter/openai/gpt-4o

Full prefix required

vLLM

hosted_vllm/llama-3.1-8b

Set 
api_base
 to vLLM server

Ollama

ollama/llama3.1

Set 
api_base
 to Ollama server

Local Models (vLLM / Ollama):

#
 Start Ollama

ollama serve

// Ollama

{
 
"vlm"
: {
 
"provider"
: 
"
litellm
"
,
 
"model"
: 
"
ollama/llama3.1
"
,
 
"api_base"
: 
"
http://localhost:11434
"

 }
}

For complete model support, seeLiteLLM Providers Documentation.

### 3. Environment Configuration

#### Server Configuration Template

Create a configuration file~/.openviking/ov.conf, remove the comments before copy:

{
 
"storage"
: {
 
"workspace"
: 
"
/home/your-name/openviking_workspace
"

 },
 
"log"
: {
 
"level"
: 
"
INFO
"
,
 
"output"
: 
"
stdout
"
 
// Log output: "stdout" or "file"

 },
 
"embedding"
: {
 
"dense"
: {
 
"api_base"
 : 
"
<api-endpoint>
"
, 
// API endpoint address

 
"api_key"
 : 
"
<your-api-key>
"
, 
// Model service API Key

 
"provider"
 : 
"
<provider-type>
"
, 
// Provider type: "volcengine" or "openai" (currently supported)

 
"dimension"
: 
1024
, 
// Vector dimension

 
"model"
 : 
"
<model-name>
"
 
// Embedding model name (e.g., doubao-embedding-vision-250615 or text-embedding-3-large)

 },
 
"max_concurrent"
: 
10
 
// Max concurrent embedding requests (default: 10)

 },
 
"vlm"
: {
 
"api_base"
 : 
"
<api-endpoint>
"
, 
// API endpoint address

 
"api_key"
 : 
"
<your-api-key>
"
, 
// Model service API Key

 
"provider"
 : 
"
<provider-type>
"
, 
// Provider type (volcengine, openai, deepseek, anthropic, etc.)

 
"model"
 : 
"
<model-name>
"
, 
// VLM model name (e.g., doubao-seed-2-0-pro-260215 or gpt-4-vision-preview)

 
"max_concurrent"
: 
100
 
// Max concurrent LLM calls for semantic processing (default: 100)

 }
}

Note: For embedding models, currentlyvolcengine(Doubao),openai, andjinaproviders are supported. For VLM models, we support three providers:volcengine,openai, andlitellm. Thelitellmprovider supports various models including Anthropic (Claude), DeepSeek, Gemini, Moonshot, Zhipu, DashScope, MiniMax, vLLM, Ollama, and more.

#### Server Configuration Examples

👇 Expand to see the configuration example for your model service:

Example 1: Using Volcengine (Doubao Models)

{
 
"storage"
: {
 
"workspace"
: 
"
/home/your-name/openviking_workspace
"

 },
 
"log"
: {
 
"level"
: 
"
INFO
"
,
 
"output"
: 
"
stdout
"
 
// Log output: "stdout" or "file"

 },
 
"embedding"
: {
 
"dense"
: {
 
"api_base"
 : 
"
https://ark.cn-beijing.volces.com/api/v3
"
,
 
"api_key"
 : 
"
your-volcengine-api-key
"
,
 
"provider"
 : 
"
volcengine
"
,
 
"dimension"
: 
1024
,
 
"model"
 : 
"
doubao-embedding-vision-250615
"

 },
 
"max_concurrent"
: 
10

 },
 
"vlm"
: {
 
"api_base"
 : 
"
https://ark.cn-beijing.volces.com/api/v3
"
,
 
"api_key"
 : 
"
your-volcengine-api-key
"
,
 
"provider"
 : 
"
volcengine
"
,
 
"model"
 : 
"
doubao-seed-2-0-pro-260215
"
,
 
"max_concurrent"
: 
100

 }
}

Example 2: Using OpenAI Models

{
 
"storage"
: {
 
"workspace"
: 
"
/home/your-name/openviking_workspace
"

 },
 
"log"
: {
 
"level"
: 
"
INFO
"
,
 
"output"
: 
"
stdout
"
 
// Log output: "stdout" or "file"

 },
 
"embedding"
: {
 
"dense"
: {
 
"api_base"
 : 
"
https://api.openai.com/v1
"
,
 
"api_key"
 : 
"
your-openai-api-key
"
,
 
"provider"
 : 
"
openai
"
,
 
"dimension"
: 
3072
,
 
"model"
 : 
"
text-embedding-3-large
"

 },
 
"max_concurrent"
: 
10

 },
 
"vlm"
: {
 
"api_base"
 : 
"
https://api.openai.com/v1
"
,
 
"api_key"
 : 
"
your-openai-api-key
"
,
 
"provider"
 : 
"
openai
"
,
 
"model"
 : 
"
gpt-4-vision-preview
"
,
 
"max_concurrent"
: 
100

 }
}

#### Set Server Configuration Environment Variable

After creating the configuration file, set the environment variable to point to it (Linux/macOS):

export
 OPENVIKING_CONFIG_FILE=
~
/.openviking/ov.conf 
#
 by default

On Windows, use one of the following:

PowerShell:

$
env:
OPENVIKING_CONFIG_FILE
 
=
 
"
$HOME
/.openviking/ov.conf
"

Command Prompt (cmd.exe):

set
 
"
OPENVIKING_CONFIG_FILE
=
%USERPROFILE%
\.openviking\ov.conf
"

💡Tip: You can also place the configuration file in other locations, just specify the correct path in the environment variable.

#### CLI/Client Configuration Examples

👇 Expand to see the configuration example for your CLI/Client:

Example: ovcli.conf for visiting localhost server

{
 
"url"
: 
"
http://localhost:1933
"
,
 
"timeout"
: 
60.0
,
 
"output"
: 
"
table
"

}

After creating the configuration file, set the environment variable to point to it (Linux/macOS):

export
 OPENVIKING_CLI_CONFIG_FILE=
~
/.openviking/ovcli.conf 
#
 by default

On Windows, use one of the following:

PowerShell:

$
env:
OPENVIKING_CLI_CONFIG_FILE
 
=
 
"
$HOME
/.openviking/ovcli.conf
"

Command Prompt (cmd.exe):

set
 
"
OPENVIKING_CLI_CONFIG_FILE
=
%USERPROFILE%
\.openviking\ovcli.conf
"

### 4. Run Your First Example

📝Prerequisite: Ensure you have completed the configuration (ov.conf and ovcli.conf) in the previous step.

Now let's run a complete example to experience the core features of OpenViking.

#### Launch Server

openviking-server

or you can run in background

nohup openviking-server 
>
 /data/log/openviking.log 
2>&1
 
&

#### Run the CLI

ov status
ov add-resource https://github.com/volcengine/OpenViking 
#
 --wait

ov ls viking://resources/
ov tree viking://resources/volcengine -L 2

#
 wait some time for semantic processing if not --wait

ov find 
"
what is openviking
"

ov grep 
"
openviking
"
 --uri viking://resources/volcengine/OpenViking/docs/zh

Congratulations! You have successfully run OpenViking 🎉

## Server Deployment Details

For production environments, we recommend running OpenViking as a standalone HTTP service to provide persistent, high-performance context support for your AI Agents.

🚀Deploy OpenViking on Cloud:
To ensure optimal storage performance and data security, we recommend deploying onVolcengine Elastic Compute Service (ECS)using theveLinuxoperating system. We have prepared a detailed step-by-step guide to get you started quickly.

👉View: Server Deployment & ECS Setup Guide

## OpenClaw Memory Plugin Details

* Test Dataset: Effect testing based on LoCoMo10 (https://github.com/snap-research/locomo) long-range dialogues (1,540 cases in total after removing category5 without ground truth)
* Experimental Groups: Since users may not disable OpenClaw's native memory when using OpenViking, we added experimental groups with native memory enabled or disabled
* OpenViking Version: 0.1.18
* Model: seed-2.0-code
* Evaluation Script:https://github.com/ZaynJarvis/openclaw-eval/tree/main

Experimental Group

Task Completion Rate

Cost: Input Tokens (Total)

OpenClaw(memory-core)

35.65%

24,611,530

OpenClaw + LanceDB (-memory-core)

44.55%

51,574,530

OpenClaw + OpenViking Plugin (-memory-core)

52.08%

4,264,396

OpenClaw + OpenViking Plugin (+memory-core)

51.23%

2,099,622

* Experimental Conclusions:
After integrating OpenViking:

* With native memory enabled: 43% improvement over original OpenClaw with 91% reduction in input token cost; 15% improvement over LanceDB with 96% reduction in input token cost.
* With native memory disabled: 49% improvement over original OpenClaw with 83% reduction in input token cost; 17% improvement over LanceDB with 92% reduction in input token cost.

👉View: OpenClaw Memory Plugin

--

## Core Concepts

After running the first example, let's dive into the design philosophy of OpenViking. These five core concepts correspond one-to-one with the solutions mentioned earlier, together building a complete context management system:

### 1. Filesystem Management Paradigm → Solves Fragmentation

We no longer view context as flat text slices but unify them into an abstract virtual filesystem. Whether it's memories, resources, or capabilities, they are mapped to virtual directories under theviking://protocol, each with a unique URI.

This paradigm gives Agents unprecedented context manipulation capabilities, enabling them to locate, browse, and manipulate information precisely and deterministically through standard commands likelsandfind, just like a developer. This transforms context management from vague semantic matching into intuitive, traceable "file operations". Learn more:Viking URI|Context Types

viking://
├── resources/ # Resources: project docs, repos, web pages, etc.
│ ├── my_project/
│ │ ├── docs/
│ │ │ ├── api/
│ │ │ └── tutorials/
│ │ └── src/
│ └── ...
├── user/ # User: personal preferences, habits, etc.
│ └── memories/
│ ├── preferences/
│ │ ├── writing_style
│ │ └── coding_habits
│ └── ...
└── agent/ # Agent: skills, instructions, task memories, etc.
 ├── skills/
 │ ├── search_code
 │ ├── analyze_data
 │ └── ...
 ├── memories/
 └── instructions/

### 2. Tiered Context Loading → Reduces Token Consumption

Stuffing massive amounts of context into a prompt all at once is not only expensive but also prone to exceeding model windows and introducing noise. OpenViking automatically processes context into three levels upon writing:

* L0 (Abstract): A one-sentence summary for quick retrieval and identification.
* L1 (Overview): Contains core information and usage scenarios for Agent decision-making during the planning phase.
* L2 (Details): The full original data, for deep reading by the Agent when absolutely necessary.

Learn more:Context Layers

viking://resources/my_project/
├── .abstract # L0 Layer: Abstract (~100 tokens) - Quick relevance check
├── .overview # L1 Layer: Overview (~2k tokens) - Understand structure and key points
├── docs/
│ ├── .abstract # Each directory has corresponding L0/L1 layers
│ ├── .overview
│ ├── api/
│ │ ├── .abstract
│ │ ├── .overview
│ │ ├── auth.md # L2 Layer: Full content - Load on demand
│ │ └── endpoints.md
│ └── ...
└── src/
 └── ...

### 3. Directory Recursive Retrieval → Improves Retrieval Effect

Single vector retrieval struggles with complex query intents. OpenViking has designed an innovativeDirectory Recursive Retrieval Strategythat deeply integrates multiple retrieval methods:

1. Intent Analysis: Generate multiple retrieval conditions through intent analysis.
2. Initial Positioning: Use vector retrieval to quickly locate the high-score directory where the initial slice is located.
3. Refined Exploration: Perform a secondary retrieval within that directory and update high-score results to the candidate set.
4. Recursive Drill-down: If subdirectories exist, recursively repeat the secondary retrieval steps layer by layer.
5. Result Aggregation: Finally, obtain the most relevant context to return.

This "lock high-score directory first, then refine content exploration" strategy not only finds the semantically best-matching fragments but also understands the full context where the information resides, thereby improving the globality and accuracy of retrieval. Learn more:Retrieval Mechanism

### 4. Visualized Retrieval Trajectory → Observable Context

OpenViking's organization uses a hierarchical virtual filesystem structure. All context is integrated in a unified format, and each entry corresponds to a unique URI (like aviking://path), breaking the traditional flat black-box management mode with a clear hierarchy that is easy to understand.

The retrieval process adopts a directory recursive strategy. The trajectory of directory browsing and file positioning for each retrieval is fully preserved, allowing users to clearly observe the root cause of problems and guide the optimization of retrieval logic. Learn more:Retrieval Mechanism

### 5. Automatic Session Management → Context Self-Iteration

OpenViking has a built-in memory self-iteration loop. At the end of each session, developers can actively trigger the memory extraction mechanism. The system will asynchronously analyze task execution results and user feedback, and automatically update them to the User and Agent memory directories.

* User Memory Update: Update memories related to user preferences, making Agent responses better fit user needs.
* Agent Experience Accumulation: Extract core content such as operational tips and tool usage experience from task execution experience, aiding efficient decision-making in subsequent tasks.

This allows the Agent to get "smarter with use" through interactions with the world, achieving self-evolution. Learn more:Session Management

## Advanced Reading

### Documentation

For more details, please visit ourFull Documentation.

### Community & Team

For more details, please see:About Us

### Join the Community

OpenViking is still in its early stages, and there are many areas for improvement and exploration. We sincerely invite every developer passionate about AI Agent technology:

* Light up a preciousStarfor us to give us the motivation to move forward.
* Visit ourWebsiteto understand the philosophy we convey, and use it in your projects via theDocumentation. Feel the change it brings and give us feedback on your truest experience.
* Join our community to share your insights, help answer others' questions, and jointly create an open and mutually helpful technical atmosphere:📱Lark Group: Scan the QR code to join →View QR Code💬WeChat Group: Scan the QR code to add assistant →View QR Code🎮Discord:Join Discord Server🐦X (Twitter)：Follow us
* 📱Lark Group: Scan the QR code to join →View QR Code
* 💬WeChat Group: Scan the QR code to add assistant →View QR Code
* 🎮Discord:Join Discord Server
* 🐦X (Twitter)：Follow us
* Become aContributor, whether submitting a bug fix or contributing a new feature, every line of your code will be an important cornerstone of OpenViking's growth.

Let's work together to define and build the future of AI Agent context management. The journey has begun, looking forward to your participation!

### Star Trend

## License

This project is licensed under the Apache License 2.0 - see theLICENSEfile for details.

## About

OpenViking is an open-source context database designed specifically for AI Agents(such as openclaw). OpenViking unifies the management of context (memory, resources, and skills) that Agents need through a file system paradigm, enabling hierarchical context delivery and self-evolving.

openviking.ai

### Topics

 agent

 memory

 skill

 filesystem

 opencode

 ai-agents

 rag

 llm

 agentic-rag

 context-engineering

 context-database

 openclaw

 clawbot

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

4.7k

 stars
 

### Watchers

26

 watching
 

### Forks

357

 forks
 

 Report repository

 

## Releases14

v0.2.3

 Latest

 

Mar 3, 2026

 

+ 13 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python83.9%
* C++9.8%
* Rust3.6%
* Shell1.7%
* JavaScript0.4%
* TypeScript0.2%
* Other0.4%