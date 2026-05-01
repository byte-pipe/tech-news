---
title: OpenWarp — 为 Warp 解锁自定义 AI 提供商
url: https://openwarp.zerx.dev
site_name: hackernews_api
content_file: hackernews_api-openwarp-为-warp-解锁自定义-ai-提供商
fetched_at: '2026-05-02T08:46:21.429883'
original_url: https://openwarp.zerx.dev
author: zero-lab
date: '2026-05-01'
description: OpenWarp 是 Warp 的开放式增强项目。通过 genai 适配层原生接入 OpenAI / Anthropic / Gemini / DeepSeek / Ollama 等多协议提供商,自定义系统提示词,享受真正属于你的智能终端。
tags:
- hackernews
- trending
---

社区版 · 进行中 
 

# 把任意 AI 模型装进你的终端

 

OpenWarp 在 Warp 之上加入 BYOP(自带提供商)能力 —— 通过 genai 适配层原生支持 6 种 API 协议、自定义模型与系统提示词、原生多语言。

 
 
 
 查看 GitHub 
 
 阅读文档 
 
 
 
 
 
$
 
git clone -b openWarp https://github.com/zerx-lab/warp
 
 
 
 
 
 
 
deepseek-r1
·
推理
zsh
openwarp
agent
~/projects/openwarp
❯
帮我重构这个 Rust trait
就绪
·
deepseek-r1
0
 
tokens
·
0
ms
·
本地
 
 
 
 

兼容主流提供商

 
 
OpenAI
Anthropic
DeepSeek
Qwen
Ollama
Groq
 
 
 
 
 
 
 
 
 
 
 
 ∞ 
 

可接入提供商

 
 
 
 2 
 

内置语言

 
 
 
 AGPL 
 

开源许可

 
 
 
 100% 
 

本地凭证存储

 
 
 
 
 
 
 
 
 
 
工作方式
 

## 三步,把 AI 完全握在自己手里

 
 

保留 Warp 全部交互,只把 AI 层完全开放 —— 密钥、模型、提示词全部由你掌控。

 
 
01

### 接入任意提供商

在设置中显式选择 API 协议、粘贴 Base URL 与 API Key —— OpenAI / Anthropic / Gemini / Ollama / DeepSeek 6 种原生协议任意切换,凭证仅保存在本地。

02

### 编写动态提示词

基于 minijinja 的模板引擎,根据当前工作目录、语言、角色实时渲染系统提示词,精准引导模型。

03

### 在终端立即启用

一键切换模型、对话、命令补全 —— 体验与 Warp 一致,但完全由你掌控。

Custom Provider
connected
name
DeepSeek (Personal)
base_url
https://api.deepseek.com/v1
api_key
sk-••••••••••••••••••••
model
deepseek-r1
 
 
 
 
 
 
 
核心特性
 

## 所有你期待的,我们都开放

 
 

基于 Warp 上游持续合并,完整保留块、AI 命令、工作流、键位。

 
 
 
 
 
 
 
 
模型路由
 

### BYOP 自定义提供商

 

通过 genai 适配层原生支持 6 种 API 协议,Base URL / API Key / Model 自由组合。

 
 
 
 
 
6 种 API 协议原生路由,不再「OpenAI 兼容硬塞」
 
 
 
推理思考多轮回传:DeepSeek reasoning_content / Claude thinking / Gemini
 
 
 
minijinja 模板渲染系统提示词
 
 
 
 
 
 
 
 
 
 
 
~/.config/openwarp.toml
 
 
 
 
 DeepSeek 
 
 Anthropic 
 
 Ollama 
 
 
 
 
提供商名称
 
DeepSeek · OpenAI 兼容
 
 
Base URL
 
https://api.deepseek.com
 
 
默认模型
 
deepseek-reasoner
 
 
 
 
 
系统提示词模板
 
就绪
 
 
{% 
if locale
 %}

Reply in 
{{
 locale 
}}

{% 
endif
 %}
 
 
 
 
 
 
 
 
 
本地存储
 

### 隐私优先

 
 
 
 
 
 
 
 
 

关闭 Cloud Agent / Computer Use,默认不上传云端,凭证仅本地保存。

 
 
 
本地凭证存储
 
100%
 
 
 
 
 
 
* 不上传云端
* 不收集遥测
* 凭证零外发
 
 
 
 
 
 02 · minijinja 
 
 {} 
 
 

### 系统提示词模板

 

基于 minijinja 的强大模板,根据上下文动态渲染指令。

 

渲染输出 →

 
 
 
 
 03 · 可扩展 
 
 Aa 
 
 

### 多语言界面

 

原生中文与英文 UI,后续社区可继续扩展更多语种。

 

简体中文 · English · 日本語 · Español

 
 
 
 
 04 · 体验保留 
 
 ⌘ 
 
 

### 保留 Warp 体验

 

基于 Warp 上游持续合并,完整保留块、AI 命令、工作流、键位。

 

Blocks · Workflows · AI 命令 · Keymaps · 主题

 
 
 
 
 05 · 完全开源 
 
 ↗ 
 
 

### 开源协议

 

与 Warp 上游一致,采用 AGPL / MIT 双许可,代码全部公开。

 

AGPL-3.0 · MIT

 
 
 
 
 
 
 
 
 
自定义提供商
 

## 一次配置,全模型可用

 

OpenWarp 通过 genai 适配层原生支持 6 种 API 协议:OpenAI / OpenAI Responses / Anthropic / Gemini / Ollama / DeepSeek —— 显式选择协议,绕过「按模型名识别」的猜测,密钥与请求直连 provider。

 
* ✓ 6 种 API 协议原生路由,不再「OpenAI 兼容硬塞」
* ✓ 推理思考多轮回传:DeepSeek reasoning_content / Claude thinking / Gemini
* ✓ minijinja 模板渲染系统提示词
* ✓ 凭证仅本地保存,直连 provider 端点不经任何中转
 
 
 
 
DeepSeek
OpenAI 兼容
Anthropic
原生协议
Ollama
本地
● connected · genai

提供商名称

DeepSeek (OpenAI 兼容)

API 协议

OpenAI

Base URL

https://api.deepseek.com

请求端点

POST /v1/chat/completions

API Key

sk-•••••••••••••••••••••

默认模型

deepseek-reasoner
 
 
 

系统提示词模板

 
{% 
if user.role
 %}

You are an expert 
{{
 user.role 
}}
.

{% 
endif
 %}

Reply in 
{{
 locale 
}}
.
 
 
 
 
 
 
 OpenAI 
 Anthropic 
 DeepSeek 
 Qwen 
 Ollama 
 Groq 
 Together 
 Mistral 
 Gemini 
 LM Studio 
 OpenRouter 
 Azure 
 OpenAI 
 Anthropic 
 DeepSeek 
 Qwen 
 Ollama 
 Groq 
 Together 
 Mistral 
 Gemini 
 LM Studio 
 OpenRouter 
 Azure 
 
 
 
 
 
 
 
 
 
 
常见问题
 

## 关于 OpenWarp

 
 
 
 
 
 
OpenWarp 与 Warp 官方是什么关系?
 
 
 
 
 
 OpenWarp 是基于 Warp 开源代码的社区分支,与 Warp 官方公司无附属关系,遵循上游的 AGPL / MIT 双许可。 
 
 
 
我的 API Key 会被上传吗?
 
 
 
 
 
 不会。所有自定义提供商凭证仅保存在本地配置文件中,直接由 OpenWarp 与你指定的 Base URL 通信,不经任何中转。 
 
 
 
支持哪些模型提供商?
 
 
 
 
 
 OpenWarp 内置 genai 多协议适配,原生支持 OpenAI / OpenAI Responses / Anthropic / Gemini / Ollama / DeepSeek 共 6 种协议;OpenAI 兼容端点(Qwen / Groq / Together / OpenRouter / SiliconFlow / LM Studio 等)选 OpenAI 协议并填 Base URL 即可接入。 
 
 
 
能继续收到 Warp 上游更新吗?
 
 
 
 
 
 会持续合并 Warp 上游主线,在保留体验的同时叠加 BYOP 与多语言增强。 
 
 
 
 
 
 
 
 
 
 
 
OpenWarp
 

### 想第一时间体验?

 

克隆仓库本地构建,或关注 GitHub 接收每次发布更新。

 
 
 
克隆仓库
 
~/dev
 
 
$
git clone -b openWarp https://github.com/zerx-lab/warp
复制
 
 
 
 
1
 cargo build --release 
 
2
 ./target/release/openwarp 
 
3
 在设置中添加自定义提供商 
 
 
 
 
 前往 GitHub 
 
 特性 
→