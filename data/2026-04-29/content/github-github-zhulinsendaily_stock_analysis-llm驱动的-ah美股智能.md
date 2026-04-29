---
title: 'GitHub - ZhuLinsen/daily_stock_analysis: LLM驱动的 A/H/美股智能分析器：多数据源行情 + 实时新闻 + LLM决策仪表盘 + 多渠道推送，零成本定时运行，纯白嫖. LLM-powered stock analysis system for A/H/US markets. · GitHub'
url: https://github.com/ZhuLinsen/daily_stock_analysis
site_name: github
content_file: github-github-zhulinsendaily_stock_analysis-llm驱动的-ah美股智能
fetched_at: '2026-04-29T12:16:33.309284'
original_url: https://github.com/ZhuLinsen/daily_stock_analysis
author: ZhuLinsen
description: LLM驱动的 A/H/美股智能分析器：多数据源行情 + 实时新闻 + LLM决策仪表盘 + 多渠道推送，零成本定时运行，纯白嫖. LLM-powered stock analysis system for A/H/US markets. - ZhuLinsen/daily_stock_analysis
---

ZhuLinsen

 

/

daily_stock_analysis

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork32.8k
* Star32.4k

 
 
 
 
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

557 Commits
557 Commits
.claude/
skills
.claude/
skills
 
 
.github
.github
 
 
api
api
 
 
apps
apps
 
 
bot
bot
 
 
data_provider
data_provider
 
 
docker
docker
 
 
docs
docs
 
 
patch
patch
 
 
scripts
scripts
 
 
sources
sources
 
 
src
src
 
 
strategies
strategies
 
 
templates
templates
 
 
tests
tests
 
 
.dockerignore
.dockerignore
 
 
.env.example
.env.example
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SKILL.md
SKILL.md
 
 
analyzer_service.py
analyzer_service.py
 
 
litellm_config.example.yaml
litellm_config.example.yaml
 
 
main.py
main.py
 
 
pyproject.toml
pyproject.toml
 
 
requirements-ci.txt
requirements-ci.txt
 
 
requirements.txt
requirements.txt
 
 
review.md
review.md
 
 
server.py
server.py
 
 
setup.cfg
setup.cfg
 
 
test.sh
test.sh
 
 
test_env.py
test_env.py
 
 
webui.py
webui.py
 
 
View all files

## Repository files navigation

# 📈 股票智能分析系统

🤖 基于 AI 大模型的 A股/港股/美股自选股智能分析系统，每日自动分析并推送「决策仪表盘」到企业微信/飞书/Telegram/Discord/Slack/邮箱

功能特性·快速开始·推送效果·完整指南·常见问题·更新日志

简体中文 |English|繁體中文

## 💖 赞助商 (Sponsors)

## ✨ 功能特性

模块

功能

说明

AI

决策仪表盘

一句话核心结论 + 评分 + 买卖点位 + 风险警报 + 操作检查清单

分析

多维度分析

技术面、实时行情、筹码分布、新闻舆情、公告、资金流与基本面聚合

市场

全球市场

支持 A股、港股、美股、美股指数及常见 ETF

策略

市场策略系统

内置 A股复盘、美股 Regime、均线、缠论、波浪、情绪周期等策略能力

复盘

大盘复盘

每日市场概览、指数表现、涨跌统计与板块强弱（支持 cn / hk / us / both）

Web

双主题工作台

支持手动分析、配置管理、任务进度、历史报告、回测、持仓管理

导入

智能导入与补全

支持图片、CSV/Excel、剪贴板导入，自选股输入支持代码/名称/拼音/别名补全

历史

报告管理

支持历史报告查看、完整 Markdown 报告、重新分析与批量管理

回测

AI 回测验证

对历史分析进行事后验证，查看方向准确率和模拟收益

Agent 问股

策略对话

多轮策略问答，支持均线金叉/缠论/波浪等 11 种内置策略，Web/Bot/API 全链路

推送

多渠道通知

支持企业微信、飞书、Telegram、Discord、Slack、邮件等主流渠道

自动化

定时运行

支持 GitHub Actions、Docker、本地定时任务和 FastAPI 服务模式

功能细节、字段契约、基本面 P0 超时语义、交易纪律、数据源优先级、Web/API 行为请看完整配置与部署指南。

### 技术栈与数据来源

类型

支持

AI 模型

AIHubMix
、Gemini、OpenAI 兼容、DeepSeek、通义千问、Claude、Ollama 本地模型等

行情数据

TickFlow
、AkShare、Tushare、Pytdx、Baostock、YFinance、Longbridge

新闻搜索

Anspire
、
SerpAPI
、
Tavily
、
Bocha
、
Brave
、
MiniMax
、SearXNG

社交舆情

Stock Sentiment API
（Reddit / X / Polymarket，仅美股，可选）

完整规则见数据源配置。

## 🚀 快速开始

### 方式一：GitHub Actions（推荐）

5 分钟完成部署，零成本，无需服务器。

#### 1. Fork 本仓库

点击右上角Fork按钮（顺便点个 Star⭐ 支持一下）

#### 2. 配置 Secrets

Settings→Secrets and variables→Actions→New repository secret

AI 模型配置（至少配置一个）

默认先选一个模型服务商并填写 API Key；需要多模型、图片识别、本地模型或高级路由时，再参考LLM 配置指南。

💡推荐AIHubMix：一个 Key 即可使用 Gemini、GPT、Claude、DeepSeek 等全球主流模型，无需科学上网，含免费模型（glm-5、gpt-4o-free 等），付费模型高稳定性无限并发。本项目可享10% 充值优惠。

Secret 名称

说明

必填

AIHUBMIX_KEY

AIHubMix
 API Key，一 Key 切换使用全系模型

可选

GEMINI_API_KEY

Google Gemini API Key

可选

ANTHROPIC_API_KEY

Anthropic Claude API Key

可选

OPENAI_API_KEY

OpenAI 兼容 API Key（支持 DeepSeek、通义千问等）

可选

OPENAI_BASE_URL
 / 
OPENAI_MODEL

使用 OpenAI 兼容服务时填写

可选

Ollama 更适合本地 / Docker 部署，GitHub Actions 推荐使用云端 API。

通知渠道配置（至少配置一个）

Secret 名称

说明

WECHAT_WEBHOOK_URL

企业微信机器人

FEISHU_WEBHOOK_URL

飞书机器人

TELEGRAM_BOT_TOKEN
 + 
TELEGRAM_CHAT_ID

Telegram

DISCORD_WEBHOOK_URL

Discord Webhook

SLACK_BOT_TOKEN
 + 
SLACK_CHANNEL_ID

Slack Bot

EMAIL_SENDER
 + 
EMAIL_PASSWORD

邮件推送

更多渠道、签名校验、分组邮件、Markdown 转图片等配置见通知渠道详细配置。

自选股配置（必填）

Secret 名称

说明

必填

STOCK_LIST

自选股代码，如 
600519,hk00700,AAPL,TSLA

✅

新闻源配置（推荐）

新闻源会显著影响舆情、公告、事件和催化因素质量，建议至少配置一个搜索服务。

Secret 名称

说明

必填

ANSPIRE_API_KEYS

Anspire AI Search
：中文内容特别优化，可增强 A 股分析效果

推荐

SERPAPI_API_KEYS

SerpAPI
：搜索引擎结果补强，适合实时金融新闻

推荐

TAVILY_API_KEYS

Tavily
：通用新闻搜索 API

可选

BOCHA_API_KEYS

博查搜索
：中文搜索优化，支持 AI 摘要

可选

BRAVE_API_KEYS

Brave Search
：隐私优先，美股资讯补强

可选

MINIMAX_API_KEYS

MiniMax
：结构化搜索结果

可选

SEARXNG_BASE_URLS

SearXNG 自建实例：无配额兜底，适合私有部署

可选

更多搜索源、社交舆情和降级规则见搜索服务配置。

#### 3. 启用 Actions

Actions标签 →I understand my workflows, go ahead and enable them

#### 4. 手动测试

Actions→每日股票分析→Run workflow→Run workflow

#### 完成

默认每个**工作日 18:00（北京时间）**自动执行，也可手动触发。默认非交易日（含 A/H/US 节假日）不执行；强制运行、交易日检查、断点续传等规则见完整指南。

### 方式二：本地运行 / Docker 部署

#
 克隆项目

git clone https://github.com/ZhuLinsen/daily_stock_analysis.git 
&&
 
cd
 daily_stock_analysis

#
 安装依赖

pip install -r requirements.txt

#
 配置环境变量

cp .env.example .env 
&&
 vim .env

#
 运行分析

python main.py

常用命令：

python main.py --debug
python main.py --dry-run
python main.py --stocks 600519,hk00700,AAPL
python main.py --market-review
python main.py --schedule
python main.py --serve-only

Docker 部署、定时任务、云服务器访问请参考完整指南；桌面客户端打包请参考桌面端打包说明。

## 📱 推送效果

### 决策仪表盘

🎯 2026-02-08 决策仪表盘
共分析3只股票 | 🟢买入:0 🟡观望:2 🔴卖出:1

📊 分析结果摘要
⚪ 中钨高新(000657): 观望 | 评分 65 | 看多
⚪ 永鼎股份(600105): 观望 | 评分 48 | 震荡
🟡 新莱应材(300260): 卖出 | 评分 35 | 看空

⚪ 中钨高新 (000657)
📰 重要信息速览
💭 舆情情绪: 市场关注其AI属性与业绩高增长，情绪偏积极，但需消化短期获利盘和主力流出压力。
📊 业绩预期: 基于舆情信息，公司2025年前三季度业绩同比大幅增长，基本面强劲，为股价提供支撑。

🚨 风险警报:

风险点1：2月5日主力资金大幅净卖出3.63亿元，需警惕短期抛压。
风险点2：筹码集中度高达35.15%，表明筹码分散，拉升阻力可能较大。
风险点3：舆情中提及公司历史违规记录及重组相关风险提示，需保持关注。
✨ 利好催化:

利好1：公司被市场定位为AI服务器HDI核心供应商，受益于AI产业发展。
利好2：2025年前三季度扣非净利润同比暴涨407.52%，业绩表现强劲。
📢 最新动态: 【最新消息】舆情显示公司是AI PCB微钻领域龙头，深度绑定全球头部PCB/载板厂。2月5日主力资金净卖出3.63亿元，需关注后续资金流向。

---
生成时间: 18:00

### 大盘复盘

🎯 2026-01-10 大盘复盘

📊 主要指数
- 上证指数: 3250.12 (🟢+0.85%)
- 深证成指: 10521.36 (🟢+1.02%)
- 创业板指: 2156.78 (🟢+1.35%)

📈 市场概况
上涨: 3920 | 下跌: 1349 | 涨停: 155 | 跌停: 3

🔥 板块表现
领涨: 互联网服务、文化传媒、小金属
领跌: 保险、航空机场、光伏设备

## ⚙️ 配置说明

完整环境变量、模型渠道、通知渠道、数据源优先级、交易纪律、基本面 P0 语义和部署说明请参考完整配置指南。

## 🖥️ Web 界面

Web 工作台提供配置管理、任务监控、手动分析、历史报告、回测、持仓管理、智能导入和浅色 / 深色主题。启动方式：

python main.py --webui
python main.py --webui-only

访问http://127.0.0.1:8000即可使用。认证、智能导入、搜索补全、历史报告复制、云服务器访问等细节见本地 WebUI 管理界面。

## 🤖 Agent 策略问股

配置任意可用 AI API Key 后，Web/chat页面即可使用策略问股；如需显式关闭可设置AGENT_MODE=false。

* 支持均线金叉、缠论、波浪理论、多头趋势等内置策略
* 支持实时行情、K 线、技术指标、新闻和风险信息调用
* 支持多轮追问、会话导出、发送到通知渠道和后台执行
* 支持自定义策略文件与多 Agent 编排（实验性）

Agent 具体参数、skill命名兼容、多 Agent 模式和预算护栏见完整指南与LLM 配置指南。

## 相关项目 (Related Projects)

DSA 聚焦日常分析报告；下面两个同系列项目分别覆盖选股、策略验证与策略进化，适合按需延伸使用。它们当前独立维护，后续会优先探索与 DSA 的候选股导入、回测验证和报告联动。

* AlphaSift：多因子选股与全市场扫描，用于从股票池中提取候选标的。
* AlphaEvo：策略回测与自我进化，用于验证策略规则，并通过迭代探索策略参数与组合。

## 🗺️ Roadmap

查看已支持的功能和未来规划：更新日志

有建议？欢迎提交 Issue

⚠️UI 调整提示：项目当前正在持续进行 Web UI 调整与升级，部分页面在过渡阶段可能仍存在样式、交互或兼容性问题。欢迎通过Issue反馈问题，或直接提交Pull Request一起完善。

## ☕ 支持项目

如果本项目对你有帮助，欢迎支持项目的持续维护与迭代，感谢支持 🙏赞赏可备注联系方式，祝股市长虹

支付宝 (Alipay)

微信支付 (WeChat)

小红书

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

详见贡献指南

### 本地门禁（建议先跑）

pip install -r requirements.txt
pip install flake8 pytest
./scripts/ci_gate.sh

如修改前端（apps/dsa-web）：

cd
 apps/dsa-web
npm ci
npm run lint
npm run build

## 📄 License

MIT License© 2026 ZhuLinsen

如果你在项目中使用或基于本项目进行二次开发，
非常欢迎在 README 或文档中注明来源并附上本仓库链接。
这将有助于项目的持续维护和社区发展。

## 📬 联系与合作

* 合作邮箱：zhuls345@gmail.com
* GitHub Issues：提交 Issue

## ⭐ Star History

如果觉得有用，请给个 ⭐ Star 支持一下！

## ⚠️免责声明

本项目仅供学习和研究使用，不构成任何投资建议。股市有风险，投资需谨慎。作者不对使用本项目产生的任何损失负责。

## About

LLM驱动的 A/H/美股智能分析器：多数据源行情 + 实时新闻 + LLM决策仪表盘 + 多渠道推送，零成本定时运行，纯白嫖. LLM-powered stock analysis system for A/H/US markets.

### Topics

 agent

 ai

 stock

 gemini

 quant

 quantitative-trading

 rag

 aigc

 llm

### Resources

 Readme

 

### License

 MIT license
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

32.4k

 stars
 

### Watchers

150

 watching
 

### Forks

32.8k

 forks
 

 Report repository

 

## Releases16

v3.14.1

 Latest

 

Apr 26, 2026

 

+ 15 releases

## Sponsor this project

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 
* https://github.com/ZhuLinsen/daily_stock_analysis#sponsor

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python79.6%
* TypeScript17.2%
* CSS1.5%
* JavaScript1.0%
* Shell0.3%
* Jinja0.2%
* Other0.2%