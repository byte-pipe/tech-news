---
title: moonshotai/Kimi-K2.7-Code · Hugging Face
url: https://huggingface.co/moonshotai/Kimi-K2.7-Code
site_name: hackernews_api
content_file: hackernews_api-moonshotaikimi-k27-code-hugging-face
fetched_at: '2026-06-12T19:41:58.052797'
original_url: https://huggingface.co/moonshotai/Kimi-K2.7-Code
author: nekofneko
date: '2026-06-12'
description: We’re on a journey to advance and democratize artificial intelligence through open source and open science.
tags:
- hackernews
- trending
---

## 1. Model Introduction

Kimi K2.7 Code is a coding-focused agentic model built upon Kimi K2.6. With substantial improvements on real-world long-horizon coding tasks, it strengthens end-to-end task completion across complex software engineering workflows while improving token efficiency, reducing thinking-token usage by approximately 30% compared with Kimi K2.6.

## 2. Model Summary

Architecture

Mixture-of-Experts (MoE)

Total Parameters

1T

Activated Parameters

32B

Number of Layers
 (Dense layer included)

61

Number of Dense Layers

1

Attention Hidden Dimension

7168

MoE Hidden Dimension
 (per Expert)

2048

Number of Attention Heads

64

Number of Experts

384

Selected Experts per Token

8

Number of Shared Experts

1

Vocabulary Size

160K

Context Length

256K

Attention Mechanism

MLA

Activation Function

SwiGLU

Vision Encoder

MoonViT

Parameters of Vision Encoder

400M

## 3. Evaluation Results

Benchmark

Kimi K2.6

Kimi K2.7 Code

GPT-5.5

Claude Opus 4.8

Coding

Kimi Code Bench v2

50.9

62.0

69.0

67.4

Program Bench

48.3

53.6

69.1

63.8

MLS Bench Lite

26.7

35.1

35.5

42.8

Agentic

Kimi Claw 24/7 Bench

42.9

46.9

52.8

50.4

MCP Atlas

69.4

76.0

79.4

81.3

MCP Mark Verified

72.8

81.1

92.9

76.4

Footnotes

1. General Testing Details* Unless stated otherwise, Kimi K2.7 Code and K2.6 were tested with thinking mode enabled via Kimi Code CLI at temperature = 1.0, top-p = 0.95, and a 262,144-token context length; GPT-5.5 ran in Codex with xhigh mode, and Opus 4.8 in Claude Code with xhigh mode. Aside from these differences, all benchmarks were evaluated under the same conditions.
2. Coding Benchmarks* Kimi Code Bench V2 is our in-house benchmark designed to evaluate coding agents on realistic tasks. It has diversed software engineering tasks across 10+ mainstream programming languages and a full production tech stack covering tasks from internal engineering use cases, production incidents, and real-world open-source projects, with emphasis on backend services, infrastructure, performance engineering, systems programming, security, frontend development, and ML/data engineering.
* Program Benchevaluates code-generation agents by asking them to recreate a program’s behavior from only a compiled binary and its documentation. It spans 200 tasks, from small CLI tools to large systems like FFmpeg and SQLite. Submissions are judged against over 248,000 fuzz-generated behavioral tests. In each task, the agent is given an executable and its documentation, but no source code, decompilation, or internet access. It must choose its own implementation language, build the full program from scratch, and pass a behavioral test suite comparing its output against the original binary.
* MLS-Benchevaluates whether AI systems can invent generalizable and scalable ML methods. MLS-Bench-Lite is the official 30-task subset of MLS-Bench, covering LLM pretraining and post-training, robotics, world models, computer vision, reinforcement learning, optimization, ML systems, AI for Science, and more. Agents are given 5 hours to explore before submitting their solutions. Opus 4.8 is evaluated with the max effort setting in Claude Code.
3. Agentic Benchmarks* Kimi Claw 24/7 Bench is our in-house benchmark for evaluating long-horizon agentic performance in persistent, multi-day coworking tasks. It spans 17 professional scenarios across 610 evaluation points, covering domains such as software engineering, ML research, recruiting, trading, marketing. All tasks are executed through the OpenClaw harness. The final score is the average pass rate across all evaluation points, and is averaged over 3 runs.
* MCP-Atlasevaluates LLM performance on realistic tool-use tasks through the scalable MCPs. We followed the official MCP-Atlas evaluation configuration with a 100 tool-call budget, and with 32k max tokens per step. The final result is averaged over 3 runs.
* MCPMark-Verified is a human-verified edition ofMCPMark, a benchmark for evaluating MCP tool use across five real server environments — Notion, GitHub, Filesystem, Postgres, and Playwright. Each task has been re-checked by our team and the benchmark offical and will be open-sourced soon. We followed the official MCPMark evaluation configuration with a 100-step tool-call budget and 32k max tokens per step. The final result is averaged over 3 runs.

## 4. Native INT4 Quantization

Kimi-K2.7-Code adopts the same native int4 quantization method asKimi-K2-Thinking.

## 5. Deployment

You can access Kimi-K2.7-Code's API onhttps://platform.moonshot.aiand we provide OpenAI/Anthropic-compatible API for you.
Currently, Kimi-K2.7-Code is recommended to run on the following inference engines:

* vLLM
* SGLang
* KTransformers

Kimi-K2.7-Code has the same architecture as Kimi-K2.5/Kimi-K2.6, and the deployment method can be directly reused.

The version requirement fortransformersis>=4.57.1, <5.0.0.

Deployment examples can be found in theModel Deployment Guide.

## 6. Model Usage

The usage demos below demonstrate how to call our official API. Note that Kimi-K2.7-Code forces thinking and preserve_thinking as True.

For third-party APIs deployed with vLLM or SGLang, please note that:

* Chat with video content is an experimental feature and is only supported in our official API for now.
* The recommendedtemperaturewill be1.0for Thinking mode.
* The recommendedtop_pis0.95.
* Instant mode is not supported.

### Chat Completion

This is a simple chat completion script which shows how to call K2.7-Code API in Thinking mode.

import
 openai

import
 base64

import
 requests

def
 
simple_chat
(
client: openai.OpenAI, model_name: 
str
):
 messages = [
 {
'role'
: 
'system'
, 
'content'
: 
'You are Kimi, an AI assistant created by Moonshot AI.'
},
 {
 
'role'
: 
'user'
,
 
'content'
: [
 {
'type'
: 
'text'
, 
'text'
: 
'which one is bigger, 9.11 or 9.9? think carefully.'
}
 ],
 },
 ]
 response = client.chat.completions.create(
 model=model_name, messages=messages, stream=
False
, max_tokens=
4096

 )
 
print
(
'====== Below is reasoning content in Thinking Mode ======'
)
 
print
(
f'reasoning content: 
{response.choices[
0
].message.reasoning}
'
)
 
print
(
'====== Below is response in Thinking Mode ======'
)
 
print
(
f'response: 
{response.choices[
0
].message.content}
'
)

### Chat Completion with visual content

K2.7-Code supports Image and Video input.

The following example demonstrates how to call K2.7-Code API with image input:

import
 openai

import
 base64

import
 requests

def
 
chat_with_image
(
client: openai.OpenAI, model_name: 
str
):
 url = 
'https://huggingface.co/moonshotai/Kimi-K2.7-Code/resolve/main/figures/kimi-logo.png'

 image_base64 = base64.b64encode(requests.get(url).content).decode()
 messages = [
 {
 
'role'
: 
'user'
,
 
'content'
: [
 {
'type'
: 
'text'
, 
'text'
: 
'Describe this image in detail.'
},
 {
 
'type'
: 
'image_url'
,
 
'image_url'
: {
'url'
: 
f'data:image/png;base64,
{image_base64}
'
},
 },
 ],
 }
 ]

 response = client.chat.completions.create(
 model=model_name, messages=messages, stream=
False
, max_tokens=
8192

 )
 
print
(
'====== Below is reasoning content in Thinking Mode ======'
)
 
print
(
f'reasoning content: 
{response.choices[
0
].message.reasoning}
'
)
 
print
(
'====== Below is response in Thinking Mode ======'
)
 
print
(
f'response: 
{response.choices[
0
].message.content}
'
)

The following example demonstrates how to call K2.7-Code API with video input:

import
 openai

import
 base64

import
 requests

def
 
chat_with_video
(
client: openai.OpenAI, model_name:
str
):
 url = 
'https://huggingface.co/moonshotai/Kimi-K2.7-Code/resolve/main/figures/demo_video.mp4'

 video_base64 = base64.b64encode(requests.get(url).content).decode()
 messages = [
 {
 
"role"
: 
"user"
,
 
"content"
: [
 {
"type"
: 
"text"
,
"text"
: 
"Describe the video in detail."
},
 {
 
"type"
: 
"video_url"
,
 
"video_url"
: {
"url"
: 
f"data:video/mp4;base64,
{video_base64}
"
},
 },
 ],
 }
 ]

 response = client.chat.completions.create(model=model_name, messages=messages)
 
print
(
'====== Below is reasoning content in Thinking Mode ======'
)
 
print
(
f'reasoning content: 
{response.choices[
0
].message.reasoning}
'
)
 
print
(
'====== Below is response in Thinking Mode ======'
)
 
print
(
f'response: 
{response.choices[
0
].message.content}
'
)

### Preserve Thinking

Kimi K2.7 Code forcespreserve_thinkingmode, which retains full reasoning content across multi-turn interactions and enhances performance in coding agent scenarios.

This feature is enabled by default and can't be disabled. The following example demonstrates how to call K2.7-Code API inpreserve_thinkingmode:

def
 
chat_with_preserve_thinking
(
client: openai.OpenAI, model_name: 
str
):
 messages = [
 {
 
"role"
: 
"user"
,
 
"content"
: 
"Tell me three random numbers."

 },
 {
 
"role"
: 
"assistant"
,
 
"reasoning_content"
: 
"I'll start by listing five numbers: 473, 921, 235, 215, 222, and I'll tell you the first three."
,
 
# Some API (e.g. vLLM) may not support reasoning_content, you can try reasoning instead

 
"content"
: 
"473, 921, 235"

 },
 {
 
"role"
: 
"user"
,
 
"content"
: 
"What are the other two numbers you have in mind?"

 }
 ]

 response = client.chat.completions.create(
 model=model_name,
 messages=messages,
 stream=
False
,
 max_tokens=
4096
,
 )
 
# the assistant should mention 215 and 222 that appear in the prior reasoning content

 
print
(
f"response: 
{response.choices[
0
].message.reasoning}
"
)
 
return
 response.choices[
0
].message.content

### Interleaved Thinking and Multi-Step Tool Call

K2.7-Code shares the same design of Interleaved Thinking and Multi-Step Tool Call as K2 Thinking. For usage example, please refer to theK2 Thinking documentation.

### Coding Agent Framework

Kimi K2.7-Code works best with Kimi Code CLI as its agent framework — give it a try athttps://www.kimi.com/code.

## 7. License

Both the code repository and the model weights are released under theModified MIT License.

## 8. Third Party Notices

SeeTHIRD PARTY NOTICES

## 9. Contact Us

If you have any questions, please reach out atsupport@moonshot.ai.

 
 
Downloads last month
 
-
 
 

 
 
Safetensors
 
Model size
 
1.1T params
 
Tensor type
 
BF16 
·
F32 
·
I32 
·
 
 

Chat template

 
 

Files info

 
 
 
 
 
 
 
 
 
Inference Providers
 
NEW
 
 
 
Novita
 
 
 
 
 
 
Image-Text-to-Text
 
 
 
Examples
 
 
 
 
Input a message to start chatting with 
moonshotai/Kimi-K2.7-Code
.
 
 
 
 
 
 
 
 
 
 
 
Send
 
 
 
View Code 
Snippets
 
 
 
 
 
 Compare providers
 
 
 
 
 
 
 

## Model tree formoonshotai/Kimi-K2.7-Code

 
 
 
 
Finetunes
 
 
 
3 models
 
 
Quantizations
 
 
 
1 model
 
 
 

## Spaces usingmoonshotai/Kimi-K2.7-Code2

 
 
 

## Collection includingmoonshotai/Kimi-K2.7-Code

 
 
Moonshot's most powerful model
 
•
 
4 items
 
•
 
Updated 
about 8 hours ago
 
•
 
 74