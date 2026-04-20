---
title: 'GitHub - lsdefine/GenericAgent: Self-evolving agent: grows skill tree from 3.3K-line seed, achieving full system control with 6x less token consumption · GitHub'
url: https://github.com/lsdefine/GenericAgent
site_name: github
content_file: github-github-lsdefinegenericagent-self-evolving-agent-gr
fetched_at: '2026-04-15T11:55:51.055030'
original_url: https://github.com/lsdefine/GenericAgent
author: lsdefine
description: 'Self-evolving agent: grows skill tree from 3.3K-line seed, achieving full system control with 6x less token consumption - lsdefine/GenericAgent'
---

lsdefine



/

GenericAgent

Public

* NotificationsYou must be signed in to change notification settings
* Fork215
* Star1.5k




 
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

339 Commits
339 Commits
assets
assets
 
 
frontends
frontends
 
 
memory
memory
 
 
reflect
reflect
 
 
tests
tests
 
 
.gitignore
.gitignore
 
 
GETTING_STARTED.md
GETTING_STARTED.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
TMWebDriver.py
TMWebDriver.py
 
 
agent_loop.py
agent_loop.py
 
 
agentmain.py
agentmain.py
 
 
ga.py
ga.py
 
 
hub.pyw
hub.pyw
 
 
launch.pyw
launch.pyw
 
 
llmcore.py
llmcore.py
 
 
mykey_template.py
mykey_template.py
 
 
simphtml.py
simphtml.py
 
 
View all files

## Repository files navigation

English|中文

## 🌟 Overview

GenericAgentis a minimal, self-evolving autonomous agent framework. Its core is just~3K lines of code. Through9 atomic tools + a ~100-line Agent Loop, it grants any LLM system-level control over a local computer — covering browser, terminal, filesystem, keyboard/mouse input, screen vision, and mobile devices (ADB).

Its design philosophy:don't preload skills — evolve them.

Every time GenericAgent solves a new task, it automatically crystallizes the execution path into an skill for direct reuse later. The longer you use it, the more skills accumulate — forming a skill tree that belongs entirely to you, grown from 3K lines of seed code.

🤖 Self-Bootstrap Proof— Everything in this repository, from installing Git and runninggit initto every commit message, was completed autonomously by GenericAgent. The author never opened a terminal once.

## 📋 Core Features

* Self-Evolving: Automatically crystallizes each task into an skill. Capabilities grow with every use, forming your personal skill tree.
* Minimal Architecture: ~3K lines of core code. Agent Loop is ~100 lines. No complex dependencies, zero deployment overhead.
* Strong Execution: Injects into a real browser (preserving login sessions). 9 atomic tools take direct control of the system.
* High Compatibility: Supports Claude / Gemini / Kimi / MiniMax and other major models. Cross-platform.

## 🧬 Self-Evolution Mechanism

This is what fundamentally distinguishes GenericAgent from every other agent framework.

[New Task] --> [Autonomous Exploration] (install deps, write scripts, debug & verify) -->
[Crystallize Execution Path into skill] --> [Write to Memory Layer] --> [Direct Recall on Next Similar Task]

What you say

What the agent does the first time

Every time after

"Read my WeChat messages"

Install deps → reverse DB → write read script → save skill

one-line invoke

"Monitor stocks and alert me"

Install mootdx → build selection flow → configure cron → save skill

one-line start

"Send this file via Gmail"

Configure OAuth → write send script → save skill

ready to use

After a few weeks, your agent instance will have a skill tree no one else in the world has — all grown from 3K lines of seed code.

##### 🎯 Demo Showcase

🧋 Food Delivery Order

📈 Quantitative Stock Screening

"Order me a milk tea"
 — Navigates the delivery app, selects items, and completes checkout automatically.

"Find GEM stocks with EXPMA golden cross, turnover > 5%"
 — Screens stocks with quantitative conditions.

🌐 Autonomous Web Exploration

💰 Expense Tracking

Autonomously browses and periodically summarizes web content.

"Find expenses over ¥2K in the last 3 months"
 — Drives Alipay via ADB.

## 📅 Latest News

* 2026-04-11:IntroducedL4 session archive memoryand scheduler cron integration
* 2026-03-23:Support personal WeChat as a bot frontend
* 2026-03-10:Released million-scale Skill Library
* 2026-03-08:Released "Dintal Claw" — a GenericAgent-powered government affairs bot
* 2026-03-01:GenericAgent featured by Jiqizhixin (机器之心)
* 2026-01-11:GenericAgent V1.0 public release

## 🚀 Quick Start

#### Method 1: Standard Installation

#
 1. Clone the repo

git clone https://github.com/lsdefine/GenericAgent.git

cd
 GenericAgent

#
 2. Install minimal dependencies

pip install streamlit pywebview

#
 3. Configure API Key

cp mykey_template.py mykey.py

#
 Edit mykey.py and fill in your LLM API Key

#
 4. Launch

python launch.pyw

Full guide:GETTING_STARTED.md

## 🤖 Bot Interface (Optional)

### Telegram Bot

# mykey.py

tg_bot_token

=

'YOUR_BOT_TOKEN'

tg_allowed_users

=
 [
YOUR_USER_ID
]

python frontends/tgapp.py

### Alternative App Frontends

Besides the default Streamlit web UI, you can also try other frontend styles:

python frontends/qtapp.py
#
 Qt-based desktop app

streamlit run frontends/stapp2.py
#
 Alternative Streamlit UI

## 📊 Comparison with Similar Tools

Feature

GenericAgent

OpenClaw

Claude Code

Codebase

~3K lines

~530,000 lines

Open-sourced (large)

Deployment

pip install
 + API Key

Multi-service orchestration

CLI + subscription

Browser Control

Real browser (session preserved)

Sandbox / headless browser

Via MCP plugin

OS Control

Mouse/kbd, vision, ADB

Multi-agent delegation

File + terminal

Self-Evolution

Autonomous skill growth

Plugin ecosystem

Stateless between sessions

Out of the Box

A few core files + starter skills

Hundreds of modules

Rich CLI toolset

## 🧠 How It Works

GenericAgent accomplishes complex tasks throughLayered Memory × Minimal Toolset × Autonomous Execution Loop, continuously accumulating experience during execution.

1️⃣Layered Memory System

Memory crystallizes throughout task execution, letting the agent build stable, efficient working patterns over time.

* L0 — Meta Rules: Core behavioral rules and system constraints of the agent
* L1 — Insight Index: Minimal memory index for fast routing and recall
* L2 — Global Facts: Stable knowledge accumulated over long-term operation
* L3 — Task Skills / SOPs: Reusable workflows for completing specific task types
* L4 — Session Archive: Archived task records distilled from finished sessions for long-horizon recall

2️⃣Autonomous Execution Loop

Perceive environment state → Task reasoning → Execute tools → Write experience to memory → Loop

The entire core loop is just~100 lines of code(agent_loop.py).

3️⃣Minimal Toolset

GenericAgent provides only9 atomic tools, forming the foundational capabilities for interacting with the outside world.

Tool

Function

code_run

Execute arbitrary code

file_read

Read files

file_write

Write files

file_patch

Patch / modify files

web_scan

Perceive web content

web_execute_js

Control browser behavior

ask_user

Human-in-the-loop confirmation

Additionally, 2memory management tools(update_working_checkpoint,start_long_term_update) allow the agent to persist context and accumulate experience across sessions.

4️⃣Capability Extension Mechanism

Capable of dynamically creating new tools.

Viacode_run, GenericAgent can dynamically install Python packages, write new scripts, call external APIs, or control hardware at runtime — crystallizing temporary abilities into permanent tools.

GenericAgent Workflow Diagram

## ⭐ Support

If this project helped you, please consider leaving aStar!🙏

You're also welcome to join ourGenericAgent Community Groupfor discussion, feedback, and co-building 👏

WeChat Group 1

WeChat Group 2

Feishu Group

## 🚩 Friendly Links

Thanks for the support from the LinuxDo community!

## 📄 License

MIT License — seeLICENSE

## 🌟 项目简介

GenericAgent是一个极简、可自我进化的自主 Agent 框架。核心仅~3K 行代码，通过9 个原子工具 + ~100 行 Agent Loop，赋予任意 LLM 对本地计算机的系统级控制能力，覆盖浏览器、终端、文件系统、键鼠输入、屏幕视觉及移动设备。

它的设计哲学是：不预设技能，靠进化获得能力。

每解决一个新任务，GenericAgent 就将执行路径自动固化为 Skill，供后续直接调用。使用时间越长，沉淀的技能越多，形成一棵完全属于你、从 3K 行种子代码生长出来的专属技能树。

🤖 自举实证— 本仓库的一切，从安装 Git、git init到每一条 commit message，均由 GenericAgent 自主完成。作者全程未打开过一次终端。

## 📋 核心特性

* 自我进化: 每次任务自动沉淀 Skill，能力随使用持续增长，形成专属技能树
* 极简架构: ~3K 行核心代码，Agent Loop 约百行，无复杂依赖，部署零负担
* 强执行力: 注入真实浏览器（保留登录态），9 个原子工具直接接管系统
* 高兼容性: 支持 Claude / Gemini / Kimi / MiniMax 等主流模型，跨平台运行

## 🧬 自我进化机制

这是 GenericAgent 区别于其他 Agent 框架的根本所在。

[遇到新任务]-->[自主摸索](安装依赖、编写脚本、调试验证)-->
[将执行路径固化为 Skill]-->[写入记忆层]-->[下次同类任务直接调用]

你说的一句话

Agent 第一次做了什么

之后每次

"监控股票并提醒我"

安装 mootdx → 构建选股流程 → 配置定时任务 → 保存 Skill

一句话启动

"用 Gmail 发这个文件"

配置 OAuth → 编写发送脚本 → 保存 Skill

直接可用

用几周后，你的 Agent 实例将拥有一套任何人都没有的专属技能树，全部从 3K 行种子代码中生长而来。

#### 🎯 实例展示

🧋 外卖下单

📈 量化选股

"Order me a milk tea"
 — 自动导航外卖 App，选品并完成结账

"Find GEM stocks with EXPMA golden cross, turnover > 5%"
 — 量化条件筛股

🌐 自主网页探索

💰 支出追踪

自主浏览并定时汇总网页信息

"查找近 3 个月超 ¥2K 的支出"
 — 通过 ADB 驱动支付宝

## 📅 最新动态

* 2026-04-11:引入L4 会话归档记忆，并接入 scheduler cron 调度
* 2026-03-23:支持个人微信接入作为 Bot 前端
* 2026-03-10:发布百万级 Skill 库
* 2026-03-08:发布以 GenericAgent 为核心的"政务龙虾" Dintal Claw
* 2026-03-01:GenericAgent 被机器之心报道
* 2026-01-11:GenericAgent V1.0 公开版本发布

## 🚀 快速开始

#### 方法一：标准安装

#
 1. 克隆仓库

git clone https://github.com/lsdefine/GenericAgent.git

cd
 GenericAgent

#
 2. 安装最小依赖

pip install streamlit pywebview

#
 3. 配置 API Key

cp mykey_template.py mykey.py

#
 编辑 mykey.py，填入你的 LLM API Key

#
 4. 启动

python launch.pyw

完整引导流程见GETTING_STARTED.md。

## 🤖 Bot 接口（可选）

### 微信 Bot（个人微信）

无需额外配置，扫码登录即可：

pip install pycryptodome qrcode requests
python frontends/wechatapp.py

首次启动会弹出二维码，用微信扫码完成绑定。之后通过微信消息与 Agent 交互。

### QQ Bot

使用qq-botpyWebSocket 长连接，无需公网 webhook：

pip install qq-botpy

在mykey.py中补充：

qq_app_id

=

"YOUR_APP_ID"

qq_app_secret

=

"YOUR_APP_SECRET"

qq_allowed_users

=
 [
"YOUR_USER_OPENID"
]
# 或 ['*'] 公开访问

python frontends/qqapp.py

在QQ 开放平台创建机器人获取 AppID / AppSecret。首次消息后，用户 openid 记录于temp/qqapp.log。

### 飞书（Lark）

pip install lark-oapi
python frontends/fsapp.py

fs_app_id

=

"cli_xxx"

fs_app_secret

=

"xxx"

fs_allowed_users

=
 [
"ou_xxx"
]
# 或 ['*']

入站支持：文本、富文本 post、图片、文件、音频、media、交互卡片 / 分享卡片出站支持：流式进度卡片、图片回传、文件 / media 回传视觉模型：图片首轮以真正的多模态输入发送给兼容 OpenAI Vision 的后端

详细配置见assets/SETUP_FEISHU.md

### 企业微信（WeCom）

pip install wecom_aibot_sdk
python frontends/wecomapp.py

wecom_bot_id

=

"your_bot_id"

wecom_secret

=

"your_bot_secret"

wecom_allowed_users

=
 [
"your_user_id"
]

wecom_welcome_message

=

"你好，我在线上。"

### 钉钉（DingTalk）

pip install dingtalk-stream
python frontends/dingtalkapp.py

dingtalk_client_id

=

"your_app_key"

dingtalk_client_secret

=

"your_app_secret"

dingtalk_allowed_users

=
 [
"your_staff_id"
]
# 或 ['*']

### 其他 App 前端

除默认的 Streamlit Web UI 外，还可以尝试不同风格的前端：

python frontends/qtapp.py
#
 基于 Qt 的桌面应用

streamlit run frontends/stapp2.py
#
 另一种 Streamlit 风格 UI

## 📊 与同类产品对比

特性

GenericAgent

OpenClaw

Claude Code

代码量

~3K 行

~530,000 行

已开源（体量大）

部署方式

pip install
 + API Key

多服务编排

CLI + 订阅

浏览器控制

注入真实浏览器（保留登录态）

沙箱 / 无头浏览器

通过 MCP 插件

OS 控制

键鼠、视觉、ADB

多 Agent 委派

文件 + 终端

自我进化

自主生长 Skill 和工具

插件生态

会话间无状态

出厂配置

几个核心文件 + 少量初始 Skills

数百模块

丰富 CLI 工具集

## 🧠 工作机制

GenericAgent 通过分层记忆 × 最小工具集 × 自主执行循环完成复杂任务，并在执行过程中持续积累经验。

1️⃣分层记忆系统

记忆在任务执行过程中持续沉淀，使 Agent 逐步形成稳定且高效的工作方式

* L0 — 元规则（Meta Rules）：Agent 的基础行为规则和系统约束
* L1 — 记忆索引（Insight Index）：极简索引层，用于快速路由与召回
* L2 — 全局事实（Global Facts）：在长期运行过程中积累的稳定知识
* L3 — 任务 Skills / SOPs：完成特定任务类型的可复用流程
* L4 — 会话归档（Session Archive）：从已完成任务中提炼出的归档记录，用于长程召回

2️⃣自主执行循环

感知环境状态 → 任务推理 → 调用工具执行 → 经验写入记忆 → 循环

整个核心循环仅约百行代码（agent_loop.py）。

3️⃣最小工具集

GenericAgent 仅提供9 个原子工具，构成与外部世界交互的基础能力

工具

功能

code_run

执行任意代码

file_read

读取文件

file_write

写入文件

file_patch

修改文件

web_scan

感知网页内容

web_execute_js

控制浏览器行为

ask_user

人机协作确认

此外，还有 2 个记忆管理工具（update_working_checkpoint、start_long_term_update），使 Agent 能够跨会话积累经验、维持持久上下文。

4️⃣能力扩展机制

具备动态创建新的工具能力

通过code_run，GenericAgent 可在运行时动态安装 Python 包、编写新脚本、调用外部 API 或控制硬件，将临时能力固化为永久工具。

GenericAgent 工作流程图

## ⭐ 支持

如果这个项目对您有帮助，欢迎点一个Star!🙏

同时也欢迎加入我们的GenericAgent体验交流群，一起交流、反馈和共建 👏

微信群 1

微信群 2

飞书群

## 🚩 友情链接

感谢LinuxDo社区的支持！

## 📄 许可

MIT License — 详见LICENSE

## About

Self-evolving agent: grows skill tree from 3.3K-line seed, achieving full system control with 6x less token consumption

github.com/lsdefine/GenericAgent

### Topics

 python

 lightweight

 automation

 gemini

 desktop-automation

 task-automation

 browser-automation

 skill-tree

 claude

 computer-control

 autonomous-agent

 ai-agent

 llm-agent

 memory-system

 self-evolving

### Resources

 Readme



### License

 MIT license


### Uh oh!

There was an error while loading.Please reload this page.





Activity


### Stars

1.5k

 stars


### Watchers

6

 watching


### Forks

215

 forks


 Report repository



## Releases

1

tags

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.





## Contributors

### Uh oh!

There was an error while loading.Please reload this page.





## Languages

* Python95.4%
* JavaScript3.9%
* Other0.7%
