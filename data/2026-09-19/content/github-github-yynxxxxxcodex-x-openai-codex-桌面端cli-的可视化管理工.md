---
title: 'GitHub - yynxxxxx/Codex-X: OpenAI Codex 桌面端/CLI 的可视化管理工具，具有Provider/API 切换、会话同步、提示词注入、Skills/MCP 管理、TOML 配置可视化的跨平台工具。 · GitHub'
url: https://github.com/yynxxxxx/Codex-X
site_name: github
content_file: github-github-yynxxxxxcodex-x-openai-codex-桌面端cli-的可视化管理工
fetched_at: '2026-09-19T14:10:38.526718'
original_url: https://github.com/yynxxxxx/Codex-X
author: yynxxxxx
description: OpenAI Codex 桌面端/CLI 的可视化管理工具，具有Provider/API 切换、会话同步、提示词注入、Skills/MCP 管理、TOML 配置可视化的跨平台工具。 - yynxxxxx/Codex-X
---

yynxxxxx

 

/

Codex-X

Public

* NotificationsYou must be signed in to change notification settings
* Fork440
* Star3.3k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

155 Commits
155 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github/
workflows
.github/
workflows
 
 
apps/
desktop
apps/
desktop
 
 
assets
assets
 
 
docs
docs
 
 
examples
examples
 
 
scripts
scripts
 
 
services/
star-history-worker
services/
star-history-worker
 
 
.gitignore
.gitignore
 
 
CHANGELOG.md
CHANGELOG.md
 
 
LICENSE
LICENSE
 
 
README.en.md
README.en.md
 
 
README.md
README.md
 
 
THIRD_PARTY_NOTICES.md
THIRD_PARTY_NOTICES.md
 
 
codex-instruct.py
codex-instruct.py
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
pnpm-workspace.yaml
pnpm-workspace.yaml
 
 
View all files

## Repository files navigation

# Codex-X

Codex 可视化提示词注入 · Provider · 会话 · Skills / MCP 管理工具

一款面向OpenAI Codex 桌面端 / Codex CLI的跨平台桌面工具。把提示词模板、自定义 Prompt、第三方 API 供应商、会话同步、Skills / MCP 和 TOML 配置都放进可视化界面里，不用反复手改文件。

## Codex-X 是什么？

当你同时使用 Codex 桌面端、CLI、第三方 API、Skills / MCP 和多套提示词时，配置很容易散落在不同文件里。Codex-X 把这些高频操作集中到一个桌面界面中，让当前状态看得见、常用操作点一下就能完成。

你可以用它：

* 像管理插件一样管理提示词：分类、导入 Markdown、自定义编辑、一键启用 / 禁用
* 内置 5 套提示词模板，同时支持用户把自己的提示词变成可视化模板库
* 管理多个可命名的官方 Codex 登录与第三方 API，一键复制、切换，并从 cc-switch 导入现有供应商
* 同步、检查、搜索和删除本地会话，按项目路径整理 Codex 历史记录
* 集中管理 Skills 与 MCP，查看当前config.toml、auth.json和操作备份
* 在设置中按日期、模型查看 Token 用量趋势，子代理用量归入所属主会话

## 软件预览

新版 UI：指令提示词管理中心

分类管理

把提示词按破甲 / 逆向、软件开发、写作辅助等分类维护

自定义提示词

直接添加、编辑或导入自己的 Markdown 提示词

Skills / MCP 可视化管理

## 功能特性

你想做的事

Codex-X 能帮你

提示词注入管理

内置 
5 套
提示词模板，支持分类、GitHub 同步、本地缓存、导入 
.md
、添加自定义提示词、编辑说明、一键启用 / 禁用。

启用方式切换

可选择“保留原提示词”追加写入，也可选择“替换原提示词”完整切换；适合在不同模型、不同任务、不同 Prompt 之间快速切换。

Provider / API

保存多个可命名的官方 Codex 登录配置，与第三方供应商统一管理、一键复制和切换；第三方供应商支持连接检测、模型获取 / 测试及从 cc-switch 导入。

会话管理

搜索本地会话、按项目路径分组、同步当前供应商、检查会话状态，并支持单选 / 多选 / 项目级永久删除。

Skills / MCP

可视化查看 Skills 与 MCP，导入已有配置，从 ZIP 安装 Skill，逐项启用 / 禁用，并检查更新状态。

配置与登录

集中查看 
config.toml
 与 
auth.json
；官方登录和第三方供应商编辑页均可在 
config.toml
 旁勾选“开启 1M 上下文窗口”，保存后生效，需模型支持；重要写入前自动备份。

用量统计

设置页提供“通用设置 / 用量统计”标签，按日期与模型筛选本地 Token 用量，查看每日趋势、缓存命中率、模型分布及最近 10 个主会话；子代理用量归入所属主会话，不单独计为会话。

跨平台使用

提供 macOS Apple Silicon / Intel、Windows MSI / 便携版和 Linux 安装包；安装版可在应用内直接下载、校验并安装更新，便携版继续使用手动下载。

## 核心亮点

### 1. 可视化提示词注入中心

Tip

安装后就能用，联网后自动补齐，也能维护自己的提示词库。

安装包离线自带 5 套模板；软件启动后会从 GitHubexamples/同步另外 6 套软件开发与写作辅助模板，以及后续更新。同步成功的在线版本会缓存到本地，临时离线仍可继续使用。你也可以导入自己的.md、新增分类、编辑说明，并像切换插件一样启用或禁用任意提示词。

Codex-X 现在不只是“几套内置 Prompt”的启动器，而是一个可视化提示词注入与管理工具：

* 按分类管理提示词，例如破甲 / 逆向、软件开发、写作辅助，也可以新增自己的分类
* 支持同步 GitHub 模板、导入 Markdown、手动添加提示词、编辑标题 / 文件名 / 内容
* 每个提示词都有独立开关，打开时自动按当前启用方式写入 Codex 指令文件
* 支持“保留原提示词”和“替换原提示词”两种模式，适合日常叠加或完整切换
* 本地缓存可离线使用，后续模板更新不会影响你自己维护的自定义提示词

模板

适合场景

获取方式

gpt5.5-unrestricted.md

短小通用，适合日常 coding 与常规技术任务

离线内置
GitHub 更新

gpt5.4-unrestricted.md

面向 GPT-5.4 / Codex CLI，偏 CTF 与安全研究工作流

离线内置
GitHub 更新

gpt5.5-jeli.md

大白话通用版，提供更完整的工程与逆向执行流程

离线内置
GitHub 更新

gpt-5.6-sol-unrestricted.md

gpt5.6-sol 破甲提示词，偏直接执行与中英文任务

离线内置
GitHub 更新

海鸥3.0破甲.md

中文技术操作员人格，覆盖 coding、CTF、逆向、内存与协议任务路由

离线内置
GitHub 更新

software-development-maintainer.md

长期维护正式项目，强调复用、最小改动、安全、测试与可维护性

GitHub 在线同步

software-development-debugging.md

从稳定复现和证据采集推进到根因修复与回归验证

GitHub 在线同步

software-development-code-review.md

按严重级别审查缺陷、回归、安全风险和测试缺口

GitHub 在线同步

writing-clarity-editor.md

在保留原意和事实的前提下润色中英文表达

GitHub 在线同步

writing-technical-docs.md

基于代码与事实编写 README、指南、API 和发布文档

GitHub 在线同步

writing-structured-draft.md

将零散材料组织成报告、方案、复盘或文章初稿

GitHub 在线同步

保留原提示词

 适合已经有个人规则的用户。Codex-X 只追加自己管理的内容，禁用时也只移除这一部分，不动原有提示词。
 

替换原提示词

 将所选模板设为当前主要指令入口，适合希望完整切换到某套模板的用户。
 

每次启用或禁用前都会自动创建备份。除了模板库，你也可以导入、编辑、删除自己的.md提示词，并通过分类管理把常用提示词整理成自己的工作流。

Note

如果你有好用的提示词模板，欢迎在Issues提交：请附上模板名称、适用场景、Markdown 内容、推荐启用方式和必要说明。合适的模板会考虑收录到examples/，让更多用户可以一键同步使用。

### 2. Provider / API：添加、检测、获取模型、随时切换

Note

启用新的第三方供应商后，新建或重新打开 Codex 会话即可使用新的中转，不需要重启整个 Codex 客户端。

* 保存多个可命名的官方 Codex 登录配置与第三方供应商，随时查看当前正在使用哪一个
* 点击“复制”直接新增独立副本，无需确认或进入编辑页；名称可稍后修改
* 切换前可检测连接，并可获取模型进行测试
* 在同一页面编辑 Base URL、API Key、Model、Wire API 和完整 TOML
* 从 cc-switch 导入时自动区分新增、更新、合并与跳过；相同 URL + Key 不再重复显示
* 切回 OpenAI Official 时保留当前官方登录态，第三方配置也不会凭空消失

### 3. 会话管理：同步、检查与永久删除

同步和检查

 检查本地会话是否和当前 Provider / 模型一致，需要时一键同步到当前供应商配置，不修改聊天内容。
 

查找和整理

 按标题、项目路径、供应商或 ID 搜索会话，也可以按项目路径分组查看，适合清理长期使用后积累的会话列表。
 

精确删除

 支持单选、多选，也可以勾选一个或多个项目，一次选中项目下的全部会话；确认后会从 Codex 自身存储中删除对应会话及其派生子会话。
 

Caution

永久删除不可恢复。删除前请先关闭仍在使用这些会话的 Codex 窗口或 CLI，并在确认窗口中再次核对待删除列表。

### 4. Skills / MCP 管理

在【技能和 MCP】页面集中管理 Codex 的能力扩展，不必再到多个目录和配置文件中逐项查找。

Skills

 查看当前 Skill，导入已有内容或从 ZIP 安装；可以逐项启用 / 禁用，并检查已安装 Skill 是否有更新。
 

MCP

 导入前先预览现有 MCP Server，再决定哪些需要纳管；启用或禁用后由 Codex-X 自动维护 Codex 配置。
 

### 5. TOML 与官方 Auth 管理

* 自动读取 Codex 官方auth.json
* 支持查看 / 编辑 ChatGPT 登录态 Auth
* 区分官方 Auth 与第三方 API Key
* 官方配置可和第三方 Provider 在 UI 中统一管理
* 查看当前 Codex 正在使用的 liveconfig.toml
* 深色代码预览与语法高亮
* Provider 编辑页可直接编辑完整 TOML
* 保存后同步到 Codex 配置目录

### 6. 逆向 Skills 导航

在线教程页
：解释什么是“破甲”、Codex-X 如何启用 GPT-5.5 / unrestricted jeli、以及如何搭配不同领域的逆向 Skills。
 

分类覆盖
：Android APK / Windows EXE / Web 协议逆向。
 

内容包含
：Skill 用途、安装方式、来源地址、推荐使用流程。
 

* 🧩 GPT-5.5 / unrestricted jeli 使用流程
* 📱 Android APK 逆向 Skills
* 🪟 Windows EXE / DLL 逆向 Skills
* 🌐 Web / API / 协议逆向 Skills
* 📋 安装命令一键复制

🚀 打开 Codex-X 逆向 Skills 导航

### 7. 跨平台桌面软件

* macOS Apple Silicon.dmg
* macOS Intel.dmg
* Windows.msi
* Windows Portable.zip
* Linux.deb/.rpm/.AppImage
* GitHub Releases 自动构建发布
* 安装版支持应用内自动更新，Windows 便携版保留手动更新

## 技术栈

类型

技术

桌面框架

Tauri 2

前端

React 18 / TypeScript / Vite

后端

Rust

本地数据

SQLite / rusqlite

配置编辑

TOML / JSON

发布

GitHub Actions / GitHub Releases

## 配置路径

Codex-X 默认读取 Codex 配置目录：

~/.codex/config.toml
~/.codex/auth.json

也支持环境变量：

CODEX_HOME=/path/to/.codex
CODEXX_HOME=/path/to/codex-x-data
CC_SWITCH_HOME=/path/to/.cc-switch

Codex-X 自身数据库默认位于：

~/.codexx/codexx.db

## 下载

请前往 Releases 页面下载：

https://github.com/yynxxxxx/Codex-X/releases

## 开发运行

pnpm install
pnpm dev

构建桌面端：

pnpm --dir apps/desktop tauri build

## 桌面端安装说明

如果你在未签名 / 未公证的 DMG 中看到“软件已损坏”提示，这是 macOS Gatekeeper 的正常行为。

* 最佳方式：使用 Apple Developer ID 签名并 notarize
* 仅本地测试：可手动移除 quarantine 属性

xattr -dr com.apple.quarantine /Applications/Codex-X.app

## 许可证

本项目基于MIT License开源。

## 致谢 / Thanks

感谢LINUX DO 论坛社区的关注、反馈与支持。

## Star History

Important

使用声明

本项目仅用于大模型与智能体相关技术的学习、研究与交流，软件本身不包含主动破坏性功能。请在合法、合规并获得授权的范围内使用，禁止将其用于攻击、侵害他人权益或其他违法用途。使用者应自行判断使用边界，并对相关行为与后果承担责任。