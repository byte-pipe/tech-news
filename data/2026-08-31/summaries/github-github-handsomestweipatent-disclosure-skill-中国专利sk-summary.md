---
title: GitHub - handsomestWei/patent-disclosure-skill: 中国专利.skill：专利点挖掘与交底书（发明/实用/外观）编写，通俗解读专利，嗅探政策动向，辅助审查答复。 · GitHub
url: https://github.com/handsomestWei/patent-disclosure-skill
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-08-31T02:23:23.939384
---

# GitHub - handsomestWei/patent-disclosure-skill: 中国专利.skill：专利点挖掘与交底书（发明/实用/外观）编写，通俗解读专利，嗅探政策动向，辅助审查答复。 · GitHub

# 中国专利.skill 项目概述

## 初衷
- **专利交底书编写**：帮助研发人员从项目材料中自动挖掘可申请的专利点、完成查新、脱敏、生成结构图/外观图并输出 Markdown 与 Word，支持发明、实用新型、外观设计三类专利。
- **专利通俗解读**：将公开专利转化为易读笔记与知识图谱，存入 Obsidian 私有库，实现检索、关联、持续增长的专利情报层。
- **政策感知与自进化**：抓取国家知识产权局等官方政策动向，生成参考清单，供技能升级使用。
- **审查答复辅助**：自动整理历史审查案例、标签化法条缺陷，利用向量或标签检索生成答复草稿。

## 运行效果
- **交底书**：首次生成 → 落盘交付 → 多轮迭代、版本并存、对话记录保存。
- **实用新型/外观**：自动提取产品线稿、结构轮廓、CAD 三维投影等图形。
- **专利解读**：Obsidian 关系图、Canvas 叙事视图，形成可检索的知识网络。

## 功能特性

### 专利交底书编写
- 支持三种专利类型（默认发明），可通过自然语言或指令 `/交底书`、`/patent-disclosure-skill` 调用。
- **项目扫描**：读取 `.docx`、`.pptx`、`.step/.stp` 等文件，先转 Markdown 再分析。
- **线稿生成**：优先使用已有合格线稿，必要时自动生成并嵌入 Markdown 与 Word。
- **专利点挖掘**：按类型生成候选点文件，支持讨论与融合。
- **查新**：优先调用国知局公开公告，失败后降级 WebSearch，结果写入第一章。
- **交底书成稿**：脱敏模板、Mermaid 框图（发明）或结构图（实用/外观），输出 `.md` 与 `.docx`，文件命名 `{案件名}_{时间戳}`。
- **自检与迭代**：逻辑/公式自检，合并纠错后另存新稿并记录对话。

### 专利通俗解读
- 推荐配合 Obsidian 使用（索引、Canvas、插件）。
- **全文抽取** → 权要树、术语表、特征‑说明书‑附图对应。
- **叙事化**：一句话概览 + 连贯叙事，降低阅读门槛。
- **知识图谱**：单篇 `_图谱.canvas`、多篇 `_专利关联.canvas`，自动生成 CSS/Bases。
- **公开线索**：联网检索 ≤3 条公开材料，生成摘要与行业语境注释。

### 政策感知与技能自进化
- 通过指令「技能进化 / 政策雷达」抓取近 12 个月国知局政策与审查动向，生成 `outputs/evolution/EVOL-*.md`，供手动确认后更新技能。

### 审查答复辅助
- 指令「审查答复」自动导入历史案例，标签化法条/缺陷，支持向量或标签检索，生成答复草稿（需人工审校后提交）。

## 示例与使用场景
| 类型 | 示例材料 | 调用方式 |
| ---- | -------- | -------- |
| 发明交底 | `examples/example_batch_job_scheduler/` | 「按发明写交底，项目路径 …/knowledge/」 |
| 实用新型交底 | `examples/example_utility_model_ev_powertrain/` | 「实用新型交底，材料在 …/example_utility_model_ev_powertrain/」 |
| 外观设计交底 | `examples/example_design_desk_lamp/` | 「外观设计交底，材料在 …/example_design_desk_lamp/」 |
| 专利通俗解读 | `examples/example_patent_reader/`（本地 PDF） | 「读专利」+ 公开号或 PDF |
| 政策感知 | 无本地样例 | 「技能进化 / 政策雷达」 |
| 审查答复 | `examples/example_oa_response/`（2 历史案 + 1 待答复） | 「审查答复」+ 案例路径 |

## 安装与接入
- 详见 `INSTALL.md`，支持 Python、Node，STEP 文件可选解析。
- 推荐安装 Obsidian 并参考 `docs/obsidian-setup-guide.md` 配置插件。

## 支持作者
- 如项目对您有帮助，可通过「请我喝杯咖啡」方式随缘赞助。

## 参考文档
- 技能入口与 Agent 流程
- 详细安装说明
- 交底书图示与转换、国知局工具
- 专利解读工具
- 审查答复案例 RAG
- Obsidian 安装与社区插件（Windows）
- 示例案件与原材料
- 交底书模板细则

---  
MIT License ©handsomestWei