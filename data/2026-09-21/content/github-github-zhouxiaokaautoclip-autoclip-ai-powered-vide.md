---
title: 'GitHub - zhouxiaoka/autoclip: AutoClip : AI-powered video clipping and highlight generation · 一款智能高光提取与剪辑的二创工具 · GitHub'
url: https://github.com/zhouxiaoka/autoclip
site_name: github
content_file: github-github-zhouxiaokaautoclip-autoclip-ai-powered-vide
fetched_at: '2026-09-21T16:50:01.293242'
original_url: https://github.com/zhouxiaoka/autoclip
author: zhouxiaoka
description: 'AutoClip : AI-powered video clipping and highlight generation · 一款智能高光提取与剪辑的二创工具 - zhouxiaoka/autoclip'
---

zhouxiaoka

 

/

autoclip

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.6k
* Star8.1k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

114 Commits
114 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
backend
backend
 
 
docs
docs
 
 
frontend
frontend
 
 
prompt
prompt
 
 
scripts
scripts
 
 
skills/
autoclip
skills/
autoclip
 
 
src-tauri
src-tauri
 
 
.dockerignore
.dockerignore
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.taurignore
.taurignore
 
 
BUILD_GUIDE.md
BUILD_GUIDE.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
DESIGN.md
DESIGN.md
 
 
DOCKER.md
DOCKER.md
 
 
Dockerfile
Dockerfile
 
 
Dockerfile.dev
Dockerfile.dev
 
 
HANDOFF.md
HANDOFF.md
 
 
LICENSE
LICENSE
 
 
README-EN.md
README-EN.md
 
 
README-ES.md
README-ES.md
 
 
README-FR.md
README-FR.md
 
 
README-JA.md
README-JA.md
 
 
README-KO.md
README-KO.md
 
 
README-PT.md
README-PT.md
 
 
README-RU.md
README-RU.md
 
 
README.md
README.md
 
 
RELEASE_CHECKLIST.md
RELEASE_CHECKLIST.md
 
 
RELEASE_NOTES.md
RELEASE_NOTES.md
 
 
ROADMAP.md
ROADMAP.md
 
 
SECURITY.md
SECURITY.md
 
 
STARTUP_GUIDE.md
STARTUP_GUIDE.md
 
 
check_whisper_status.sh
check_whisper_status.sh
 
 
clean_database.py
clean_database.py
 
 
docker-compose.dev.yml
docker-compose.dev.yml
 
 
docker-compose.yml
docker-compose.yml
 
 
docker-dev-entrypoint.sh
docker-dev-entrypoint.sh
 
 
docker-entrypoint.sh
docker-entrypoint.sh
 
 
docker-start.sh
docker-start.sh
 
 
docker-status.sh
docker-status.sh
 
 
docker-stop.sh
docker-stop.sh
 
 
env.example
env.example
 
 
init_database.py
init_database.py
 
 
install_llm_dependencies.py
install_llm_dependencies.py
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
pyproject.toml
pyproject.toml
 
 
quick_start.sh
quick_start.sh
 
 
requirements.txt
requirements.txt
 
 
start_autoclip.sh
start_autoclip.sh
 
 
status_autoclip.sh
status_autoclip.sh
 
 
stop_autoclip.sh
stop_autoclip.sh
 
 
View all files

## Repository files navigation

# AutoClip

把长视频变成值得分享的精彩片段。

简体中文·English·日本語·한국어·Español·Português·Русский·Français

项目网站·反馈问题

桌面安装包:macOS · Apple Silicon·Windows · x64

安装与第一次出片·完整排错指南

自 v1.3.1 起，产品界面、官网和 README 均支持中、英、日、韩、西、葡、俄、法。顶栏可切换界面语言或跟随系统；用户素材和生成内容保留原文。

AutoClip 用 AI 分析视频字幕、定位高光、生成标题，并自动剪出片段与合集。适合访谈、播客、课程和直播回放，提供桌面应用、Docker Web 界面和 CLI / MCP 三种使用方式。

## 界面预览

v1.3.0 真实 Web 界面：在文件导入区添加本地视频，可同时提供 SRT 字幕。

## 社区成就

以下徽章由 Trendshift 提供，点击可查看 AutoClip 的上榜记录。GitHub Trending 与 Trendshift 是不同榜单；徽章展示平台记录的成就，不代表当前实时排名。

## 你可以做什么

能力

说明

导入素材

支持本地视频、YouTube 与 B 站链接，可附带 SRT 字幕。

发现高光

从字幕提取大纲、话题时间线、精彩度评分和片段标题。

剪辑与合集

自动生成视频切片，组合推荐合集，也可手动调整顺序。

发布导出

提供抖音、小红书、YouTube Shorts 和 B 站导出预设，支持烧录字幕与标题卡。

自由选择模型

支持通义千问、OpenAI 兼容接口、Gemini、硅基流动，以及 Ollama / LM Studio 本地模型。

接入自动化

通过 CLI 批量编排，或让支持 MCP 的客户端调用同一条处理流水线。

导入视频 → 准备字幕 / 语音转写 → AI 分析与评分 → 生成切片与合集 → 导出成片

## 快速开始

### 1. 桌面版

从GitHub Releases下载适合你的安装包：

平台

安装方式

macOS · Apple Silicon

.dmg

Windows 10 / 11 · x64

-setup.exe

Intel Mac / Linux

使用下方 Docker 或 CLI

桌面安装包内置 Python 和 FFmpeg。实际支持的平台与首次启动说明以对应 Release 为准。安装后先在设置中选择模型提供商、测试连接并保存，再导入视频。

### 2. Docker / Web

需要 Docker 和 Docker Compose v2。以下命令在仓库根目录执行：

git clone https://github.com/zhouxiaoka/autoclip.git

cd
 autoclip

cp env.example .env

启动前编辑.env：选择LLM_PROVIDER，填写对应服务的 API Key 和模型名；也可以启动后在设置页配置。

mkdir -p data logs uploads
docker compose up -d --build

打开Web 界面；API 文档在后端启动后可用。部署细节见Docker 指南（中文）。

Linux 上若绑定目录出现权限错误，先执行以下命令修正项目数据目录的归属，再重新启动服务：

docker compose run --rm --no-deps --user root --entrypoint sh autoclip -c 
'
chown -R autoclip:autoclip /app/data /app/logs /app/uploads
'

docker compose up -d

### 3. CLI / MCP

需要 Python 3.10+（建议 3.11）和 PATH 中可用的 FFmpeg。以下安装示例使用 macOS / Linux shell；Windows PowerShell 用venv\Scripts\Activate.ps1激活虚拟环境。CLI 本地处理不需要 Redis。

git clone https://github.com/zhouxiaoka/autoclip.git

cd
 autoclip
python3 -m venv venv

source
 venv/bin/activate
python -m pip install -r requirements.txt
python -m pip install -e 
.

本地模型示例：先安装并启动 Ollama，再下载模型。无字幕视频需要faster-whisper，首次转写会下载语音模型；已有字幕可用--srt talk.srt。

ollama pull qwen2.5:7b
python -m pip install faster-whisper
autoclip doctor --provider ollama
autoclip run talk.mp4 --provider ollama --json

把PROJECT_ID替换为处理结果中的项目 ID，即可导出 Shorts 格式；用autoclip mcp启动 stdio MCP 服务：

autoclip 
export
 PROJECT_ID --preset shorts
autoclip mcp

在 MCP 客户端中将command设为虚拟环境里autoclip的绝对路径，args设为["mcp"]。详见CLI / MCP 指南（中文）和Agent skill（中文）。

## 模型配置

方式

配置

云端模型

在设置中选择通义千问、OpenAI 兼容接口、Gemini 或硅基流动，填写 API Key；兼容接口可配置 Base URL。

Ollama

服务地址默认为 
http://localhost:11434/v1
，默认模型 
qwen2.5:7b
，无需 API Key。

LM Studio

加载模型并启动 Local Server，默认地址 
http://localhost:1234/v1
，选择服务实际提供的模型。

Docker 访问宿主机模型服务时，localhost指向容器自身；需配置容器能访问的宿主机地址。详见 CLI / MCP 指南。视频剪辑在本地进行，云端模型分析会向所选服务发送字幕文本；下载视频与模型仍需要网络。

## 常见问题

需要付费或 API Key 吗？

AutoClip 本身免费、开源（MIT）。云端模型由所选服务商计费，需要自己的 API Key；Ollama / LM Studio 本地预设无需云端 Key，但需要模型和相应硬件。

我的视频会上传吗？

本地剪辑在你的设备上完成；使用云端模型时，字幕文本会发送给该服务商。主动使用发布上传功能时，视频会发送到目标平台。统计与错误报告取决于版本和设置，详见隐私说明。

没有字幕也能使用吗？

可以，需要先准备本地 Whisper 组件和语音模型。已有字幕时可同时导入 SRT；准确字幕通常能减少转写等待和识别错误。

为什么没有生成片段？

先检查失败阶段：字幕是否为空、模型连接是否成功、评分阈值是否过高，以及 FFmpeg 和磁盘是否正常。可以尝试把评分阈值从 0.7 降到 0.5，但不保证一定有片段。

什么视频更适合？处理要多久？

当前分析主要基于字幕，适合访谈、播客、课程和口播。纯视觉动作或音乐类视频效果可能有限。耗时取决于时长、硬件、模型与导出设置，建议先用短样本验证。

完整排错指南·已知问题

## 文档

README 提供八种语言；以下深入文档目前以中文为主。README 翻译语言不代表应用界面或转写模型支持的语言范围。

* 安装与第一次出片
* Docker 部署（中文）
* CLI、MCP 与本地模型（中文）
* 模型提供商配置（中文）
* 常见问题（中文）
* 贡献指南（中文）
* 更新日志
* 隐私说明（中文 / English）
* README 翻译与徽章维护（中文）

## 参与贡献与联系

欢迎提交修复、使用反馈和翻译改进。报告问题时请附上系统、版本、所选模型、复现步骤及已脱敏的错误日志。

个人业余维护，回复时间不固定，不提供即时客服或一对一部署服务。联系前请先查看常见问题与已知问题。

* 邮箱:christine_zhouye@163.com

感谢 FastAPI、React、Tauri、FFmpeg、yt-dlp、Whisper，以及所有贡献者。项目采用MIT License。如果 AutoClip 帮到了你，欢迎给项目一个 Star。