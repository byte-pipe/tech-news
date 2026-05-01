---
title: OpenWarp — 为 Warp 解锁自定义 AI 提供商
url: https://openwarp.zerx.dev
date: 2026-05-01
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-05-02T08:47:31.220814
---

# OpenWarp — 为 Warp 解锁自定义 AI 提供商

# OpenWarp — 为 Warp 解锁自定义 AI 提供商

## 核心特性
- BYOP（自带提供商）能力，原生支持 6 种 API 协议：OpenAI、Anthropic、DeepSeek、Gemini、Ollama、Groq 等  
- 本地凭证存储，默认关闭 Cloud Agent，凭证仅保存在本地配置文件，不上传云端  
- 基于 minijinja 的系统提示词模板，可根据工作目录、语言、角色等上下文动态渲染  
- 多语言 UI，已提供简体中文、English、Japanese、Español，社区可继续扩展  
- 完全保留 Warp 的交互体验：块、AI 命令、工作流、键位、主题等均保持一致  
- 完全开源，采用 AGPL‑3.0 与 MIT 双许可，代码全部公开  

## 使用流程（三步）
1. **接入任意提供商**  
   - 在设置中显式选择 API 协议，填写 Base URL 与 API Key  
   - 支持 OpenAI、Anthropic、Gemini、Ollama、DeepSeek 等 6 种原生协议，凭证仅本地保存  

2. **编写动态提示词**  
   - 使用 minijinja 模板引擎，根据当前工作目录、语言、角色实时渲染系统提示词  
   - 示例模板：  
     ```jinja
     {% if locale %}
     Reply in {{ locale }}
     {% endif %}
     ```  

3. **终端立即启用**  
   - 一键切换模型、对话、命令补全  
   - 体验与 Warp 完全一致，但所有 AI 层（密钥、模型、提示词）由用户自行掌控  

## 配置示例
- 配置文件路径：`~/.config/openwarp.toml`  
- 示例提供商（DeepSeek，兼容 OpenAI）  
  ```toml
  [providers.DeepSeek]
  name = "DeepSeek (OpenAI 兼容)"
  api_protocol = "OpenAI"
  base_url = "https://api.deepseek.com"
  api_key = "sk-••••••••••••••••••••"
  default_model = "deepseek-reasoner"

  [providers.DeepSeek.system_prompt]
  template = """
  {% if user.role %}
  You are an expert {{ user.role }}.
  {% endif %}
  Reply in {{ locale }}.
  """
  ```  

## 常见问题
- **OpenWarp 与 Warp 官方的关系**：基于 Warp 开源代码的社区分支，无官方附属关系，遵循上游的双许可。  
- **API Key 是否会上传**：不会，所有凭证仅保存在本地配置文件，直接与指定的 Base URL 通信。  
- **支持哪些模型提供商**：原生支持 OpenAI、Anthropic、DeepSeek、Gemini、Ollama、Groq；兼容端点（如 Qwen、Groq、Together、OpenRouter、SiliconFlow、LM Studio 等）可通过 OpenAI 协议并填写 Base URL 接入。  
- **是否会持续收到 Warp 上游更新**：会持续合并 Warp 主线更新，保持体验一致的同时叠加 BYOP 与多语言增强。  

## 快速上手
```bash
git clone -b openWarp https://github.com/zerx-lab/warp
cargo build --release
./target/release/openwarp
# 在设置中添加自定义提供商
```  

关注 GitHub 获取最新发布与更新。