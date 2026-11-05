---
title: GitHub - Thysrael/Horizon: 📡 Your own AI-powered news radar. Generates daily briefings in English & Chinese. | 用 AI 构建你专属的新闻雷达 · GitHub
url: https://github.com/Thysrael/Horizon
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-11-05T15:24:20.784639
---

# GitHub - Thysrael/Horizon: 📡 Your own AI-powered news radar. Generates daily briefings in English & Chinese. | 用 AI 构建你专属的新闻雷达 · GitHub

# Horizon 项目概览

## 项目定位
- AI 驱动的新闻雷达，能够每日生成中英文简报  
- 汇聚 RSS、Hacker News、Reddit、Telegram、X、GitHub、金融新闻等多源信息  
- 通过自定义 **profiles** 实现过滤、去重、评分和内容加工  

## 主要功能
- **多源聚合**：统一抓取多种渠道的新闻与讨论  
- **可配置评分**：基于 profiles 定义评分规则、阈值和去重策略  
- **内容加工**：支持摘要、背景、解决方案、要点等多种 Markdown 提示与 JSON 定义  
- **社区补充**：可加入网络调研的背景信息和社区讨论  
- **平衡摘要**：限制整体篇幅及各类别占比，防止单一话题占据太多空间  
- **多渠道输出**：生成 Markdown 简报，可发布至 Pages、邮件、Webhook、飞书、微信等  

## Profiles 示例
| Profile | 适用场景 | 输出内容 |
|---|---|---|
| tech-news | 技术新闻 | 事件与影响、社区讨论 |
| tech-blog | 工程深度文章 | 背景、解决方案、实用要点 |
| ai-creator | AI 创作材料 | 摘要、时效钩子、内容角度 |

## 工作原理
1. **源数据** 按配置路由到对应 profile  
2. **分析、过滤、去重** 在 enrichment 前完成  
3. **内容加工** 根据 profile 的 Markdown/JSON 提示生成 enriched 项目  
4. **生成简报** 按 profile 分组输出  

## 快速上手

### 安装方式
- **本地**：`git clone https://github.com/Thysrael/Horizon.git && cd Horizon && uv sync`（推荐）或 `pip install -e .`  
- **Docker**：`docker compose build --build-arg EXTRAS=openbb horizon`  

### 配置
- **交互式向导**（推荐）：`uv run horizon-wizard`  
- **手动**：复制 `.env.example` 与 `data/config.example.json` 为实际文件，填入 API Key、源配置等  

### 运行
- 本地：`uv run horizon [OPTIONS]`  
- Docker：`docker compose run --rm horizon [OPTIONS]`  

常用选项示例  
| 选项 | 默认 | 说明 |
|---|---|---|
| `--hours N` | 24 | 抓取最近 N 小时的内容 |
| `-d, --data-dir PATH` | `data` | 数据目录路径 |
| `-c, --config PATH` | `<data-dir>/config.json` | 配置文件路径 |
| `-l, --log-level LEVEL` | `WARNING` | 日志级别 |

### 自动化
- 可使用 GitHub Actions（`daily-summary.yml` 模板）定时执行摘要生成  

## 支持的内容源
- Hacker News（含评论）  
- RSS / Atom  
- Reddit（含评论）  
- Telegram（公开频道）  
- Twitter / X（Apify，含回复）  
- GitHub（事件、发布）  
- OpenBB（金融公司新闻）  

## 其他资源
- Live Demo、配置指南、QQ 群、简体中文与日文文档均在仓库根目录的 `README*` 中提供。