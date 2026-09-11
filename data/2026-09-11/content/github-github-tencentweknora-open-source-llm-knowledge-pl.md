---
title: 'GitHub - Tencent/WeKnora: Open-source LLM knowledge platform: turn raw documents into a queryable RAG, an autonomous reasoning agent, and a self-maintaining Wiki. · GitHub'
url: https://github.com/Tencent/WeKnora
site_name: github
content_file: github-github-tencentweknora-open-source-llm-knowledge-pl
fetched_at: '2026-09-11T14:51:30.335718'
original_url: https://github.com/Tencent/WeKnora
author: Tencent
description: 'Open-source LLM knowledge platform: turn raw documents into a queryable RAG, an autonomous reasoning agent, and a self-maintaining Wiki. - Tencent/WeKnora'
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 Tencent

 

/

WeKnora

Public

* NotificationsYou must be signed in to change notification settings
* Fork3.2k
* Star22.3k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

2,990 Commits
2,990 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
Formula
Formula
 
 
cli
cli
 
 
client
client
 
 
cmd
cmd
 
 
config
config
 
 
dataset
dataset
 
 
deploy
deploy
 
 
docker
docker
 
 
docreader
docreader
 
 
docs
docs
 
 
examples
examples
 
 
frontend
frontend
 
 
helm
helm
 
 
internal
internal
 
 
licenses
licenses
 
 
mcp-server
mcp-server
 
 
migrations
migrations
 
 
miniprogram
miniprogram
 
 
misc
misc
 
 
packages
packages
 
 
patches/
browserskill
patches/
browserskill
 
 
scripts
scripts
 
 
testdata
testdata
 
 
tests/
miniprogram
tests/
miniprogram
 
 
third_party/
anydoc-go
third_party/
anydoc-go
 
 
website-docs
website-docs
 
 
.air.toml
.air.toml
 
 
.dockerignore
.dockerignore
 
 
.env.example
.env.example
 
 
.env.lite.example
.env.lite.example
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.golangci.yml
.golangci.yml
 
 
CHANGELOG.md
CHANGELOG.md
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
README_CN.md
README_CN.md
 
 
README_JA.md
README_JA.md
 
 
README_KO.md
README_KO.md
 
 
SECURITY.md
SECURITY.md
 
 
THIRD_PARTY_NOTICES.md
THIRD_PARTY_NOTICES.md
 
 
VERSION
VERSION
 
 
docker-compose.dev.yml
docker-compose.dev.yml
 
 
docker-compose.yml
docker-compose.yml
 
 
go.mod
go.mod
 
 
go.sum
go.sum
 
 
package-lock.json
package-lock.json
 
 
rerank_server_demo.py
rerank_server_demo.py
 
 
test_agent_config.sh
test_agent_config.sh
 
 
View all files

## Repository files navigation

|English|简体中文|日本語|한국어|

#### Overview•Architecture•Key Features•Getting Started•API Reference•Developer Guide

# 💡 WeKnora — Turn Documents into Living Knowledge with RAG, Agents and Auto-Wiki

## 📌 Overview

WeKnorais an open-source, LLM-powered knowledge framework built for enterprise-grade document understanding, semantic retrieval, and autonomous reasoning.

weknora-narrated.mp4

2:25 · 1080p · English narration & captions.

It is organized around three core capabilities:RAG-based Quick Q&Afor everyday lookups, aReAct Agentthat autonomously orchestrates retrieval, MCP tools, atenant skill catalog, session-persistentDocker / E2B / Cube sandboxesand web search to handle complex multi-step tasks, and a brand-newWiki Modein which agents distill raw documents into a self-maintaining, interlinked markdown knowledge base with an interactive knowledge graph, complete with manual editing, revision history and one-click rollback.Cross-session long-term memoryremembers who you are and what you keep asking about. Knowledge curation is equally hands-on: atree-structured folder viewpreserves the directory layout of uploads, andchunk editing with revision historylets retrieval chunks be edited, diffed and reverted like documents. Combined with multi-source ingestion (Feishu wiki / Feishu Drive / GitLab / Tencent IMA / Notion / Yuque / RSS, and growing),website embed widgetsfor publishing agents to external sites,scoped API keys with a principal modelfor programmatic integrations,multi-instance storage backendsper workspace for flexible data placement, 20+ LLM provider integrations (including LiteLLM), full Langfuse observability plus aruntime task-queue dashboard with worker-pool governance,enterprise-ready multi-workspace RBAC(4-tier role matrix + per-resource ownership + per-workspace audit log), and a fully self-hostable modular architecture, WeKnora turns scattered documents into a queryable, reasoning-capable, continuously evolving knowledge asset.

The framework supports auto-syncing knowledge from Feishu, GitLab, Tencent IMA, Notion, and Yuque (more data sources coming soon), handles 10+ document formats including PDF, Word, images, Excel and XMind, and can serve Q&A directly through IM channels like WeCom, Feishu, Slack, and Telegram. It is compatible with major LLM providers including OpenAI, DeepSeek, Qwen (Alibaba Cloud), Zhipu, Hunyuan, Gemini, MiniMax, NVIDIA, LiteLLM, and Ollama. Office files can be parsed in-process withanydoc. Its fully modular design allows swapping LLMs, vector databases, and storage backends, with support for local and private cloud deployment ensuring complete data sovereignty. WeKnora also integrates withLangfusefor comprehensive observability into agent reasoning, token usage, and pipeline tracing.

## ✨ Latest Updates

* v0.8.0—Skill sandbox runtime(session-persistent Docker / E2B / Cube backends with per-tenant network policy; Local host-process backend removed; Docker opt-in);tenant skill catalog(install from ClawHub / SkillHub / git / zip, per-sandbox snapshots, live progress, file browse/edit, personal and workspace env vars);cross-session long-term memory(profile / preference / fact / task / interest, auto-extract with confirm,search_memory);in-process anydoc office parser; officialDeepSeek Harness plugin@wxg-prc-cpg/dsh-weknora; GitLab and Tencent IMA data sources; LiteLLM; Exa and Metaso web search; XMind parsing; chat artifacts, question outline and timestamps; context compaction and provider prompt-cache markers. Plus OIDC JWKS verification, optional complex passwords, document auto-tagging, and broad sandbox/security hardening. SeeCHANGELOG.md.
* v0.7.2— Launched theofficial product documentation site(VitePress; six sections, ~50 pages covering ~360 API endpoints and ~150 environment variables, with standalone Docker/Nginx deployment, quickstart sample data and a local MCP demo);knowledge base folder tree(upload paths stored as first-class data, browse/rename/re-file documents like a file manager);chunk editing with revision history(edit retrieval chunks in the UI, per-version diff and rollback, automatic reindexing, plus custom document metadata);Wiki page revision history(snapshots + line-level diff + one-click rollback + in-browser manual editing);directly loadable file URLsviaresource_urls=public/RESOURCE_URL_MODE(third-party apps render images and files without a second authenticated proxy call);Feishu Drive data sourceand docx sync through the blocks API; batch document tagging;MCP Server 1.1.x(migrated to the mcp 2.x high-level API, official PyPI packagetencent-weknora-mcp, newcreate_knowledge_from_textandlist_shared_knowledge_basesfor 29 tools total); AWS S3 default credential chain (IAM Role / IRSA); local HTML upload parsing; QQBot markdown replies; new PR CI checks for app / frontend / docreader / mcp-server. Plus large-scale router andmodelcontextrefactors, rerank and chunking quality work, and broad stability fixes. SeeCHANGELOG.md.
* v0.7.1— NewYunzhijia (云之家) IM integration(WebSocket + image messages + markdown replies);Volcengine rerankprovider (with request batching) andZhipu AI web searchprovider;platform-scoped API keysfor control-plane automation (tenant management, system settings, runtime queues, audit logs);per-KB activity audit trail; FAQ management enhancements (filtering, tagging, export, import tracking);Langfuse OTLP/OTel tracingmigration with W3C traceparent propagation; chat header actions with one-clickMarkdown exportand wiki tool results in the references drawer; prompt-cache observability; session channel governance (admin-scoped IM/embed/API sessions); resilient Feishu large-wiki sync; and removal of the legacy Neo4j conversation-memory dependency. Plus broad slug-integrity, SSRF-transport, and state-sync hardening. SeeCHANGELOG.md.
* v0.7.0— Fine-grainedscoped API keys & principal model(capability-level grants + per-KB restriction + API integration playground);runtime task-queue observability dashboard & worker-pool governance(per-stage pools + per-model concurrency governors + failed-task inspection/retry);multi-instance storage backends(multiple storage instances per workspace, per-KB binding, default instance);session-scoped temporary attachments(async image/doc parsing + combined limits); question & follow-up suggestions; stable resource registry with LLM-context alias compaction;@Skill / @MCPmentions with scoped agent runtime; mid-conversation MCP OAuth; QQBot & Lark (Feishu International) IM integration; Redis TLS; Requesty model provider + Keenable web search; tenantless provisioning & gated self-service workspaces; admin password reset; knowledge base duplicate flow;weknoraCLI v0.10. Plus broad security hardening (SSRF, secret redaction, SQL validation, IDOR). SeeCHANGELOG.md.
* v0.6.3— Website embed widget & Integrations Center (secure-mode token exchange + rate limits); chat experience overhaul (citation popovers, RAG pipeline progress, streaming markdown); document multi-tag & batch reparse; Wiki folders & hierarchy navigation; RSS data source; MCP OAuth2; EPUB / MHTML parsing; agent model-readiness checks; model test debugger; session source filter; workspace deletion UI. SeeCHANGELOG.md.
* v0.6.2— Per-upload process configuration with upload-confirm dialog; document reparse withprocess_config;weknoraCLI v0.9 (bundled Agent Skills,session stop, auth/profile harmonization); KB marquee multi-select; HNSW index for 1024-dim pgvector embeddings; chat resources store refactor; Langfuse-only tracing (Jaeger removed). SeeCHANGELOG.md.
* v0.6.1— Document parsing trace timeline (Langfuse-style span tree with stage-by-stage progress + stop-parse); OpenSearch vector store driver; declarative built-in models via YAML; system admin & consolidated platform settings + audit log; new-user onboarding guide; settings UI redesign;weknoraCLI v0.7 / v0.8 (agent-first wire contract, NDJSON,--dry-run); OpenDataLoader + PaddleOCR-VL parsers; MCP server multi-transport (stdio / SSE / HTTP); per-model thinking-mode config; Tencent LKEAP rerank + native Gemini embeddings + MiniMax-M3. SeeCHANGELOG.md.
* v0.6.0— Workspace RBAC (4-tier role matrixOwner/Admin/Contributor/Viewer+ per-KB ownership + per-workspace audit log), workspace member management & multi-workspace UX, self-service workspaces;weknoraCLI v0.4 GA withmcp serve; KB retrieval fan-out across vector stores; AES-256-GCM credential encryption + docreader gRPC TLS + Token; Zhipu embedder + Huawei OBS; server-side user preferences; Go 1.26.0. Seedocs/RBAC说明.mdandCHANGELOG.md.
* v0.5.2— Wiki ingest scales to 40k-document KBs (task queue + DLQ); MCP human-in-the-loop tool approval; Anthropic / Apache Doris / Tencent VectorDB / KS3 / SearXNG backends; adaptive 3-tier chunking with live preview; global ⌘K command palette; Yuque connector + WeChat Mini Program;weknoraCLI preview.
* v0.5.1— Knowledge-base batch management; workspace-wide IM channels overview; session search + user-scoped pinning; unified Model / Web Search / MCP settings cards; per-agent LLM timeout; desktop workspace switching.
* v0.5.0— Wiki Mode GA — agents auto-generate structured, interlinked Markdown wiki pages with a knowledge graph; wiki browser + visual graph in the UI.
* v0.4.0— WeKnora Cloud (hosted LLM + parsing); Chrome Extension; ClawHub Skill; WeChat IM; attachment processing; Azure OpenAI / Alibaba OSS; Notion connector; Baidu + Ollama web search; VectorStore management.
* v0.3.6— ASR (audio); Feishu data-source auto-sync; OIDC; IM quote-reply context + thread-based sessions; document summarization; Tavily search; parallel tool calling; agent @mention scope restriction.
* v0.3.5— Telegram / DingTalk / Mattermost IM; IM slash commands + QA queue; suggested questions; VLM auto-describe MCP tool images; Novita AI; channel tracking.
* v0.3.4— WeCom / Feishu / Slack IM; multimodal image support; NVIDIA model API; Weaviate; AWS S3; AES-256-GCM API-key encryption; built-in MCP service; hybrid-search optimization;final_answertool.
* v0.3.3— Parent-child chunking; KB pinning; fallback response; passage cleaning for rerank; storage auto-creation; Milvus.
* v0.3.2— Knowledge Search entry; per-source parser & storage engine config; image rendering in local storage; document preview; Volcengine TOS; Mermaid rendering; batch session management; memory graph preview.
* v0.3.0— Shared Space; Agent Skills + sandboxed execution; custom agents; Data Analyst agent; thinking mode; Bing / Google web search; API Key auth; Helm chart; Korean i18n; Qdrant.
* v0.2.0— Agent Mode (ReACT); multi-type knowledge bases (FAQ + document); conversation strategy config; DuckDuckGo web search; MCP tool integration; new UI with agent mode switching; MQ async task management.

## 📱 Interface Showcase

🛠️ Skill Sandbox Chat · generate and preview a Word file

📦 Skill Catalog · install onto an E2B sandbox

🤖 Agent Mode · search, read a skill, write sandbox files

💬 Intelligent Q&A Conversation

📖 Wiki Browser

🕸️ Wiki Knowledge Graph

🕘 Wiki Page Revision History & Rollback

✂️ Chunk Editing & Revision History

📁 Folder Tree & Batch Operations

🔭 Observability · Langfuse Tracing

## 🏗️ Architecture

Fully modular pipeline from document parsing, vectorization, and retrieval to LLM inference — every component is swappable and extensible. Supports local / private cloud deployment with full data sovereignty and a zero-barrier Web UI for quick onboarding.

## 🧩 Feature Overview

Intelligent Conversation

Capability

Details

Intelligent Reasoning

ReACT progressive multi-step reasoning, autonomously orchestrating knowledge retrieval, MCP tools, skill sandboxes, and web search

Quick Q&A

RAG-based Q&A over knowledge bases for fast and accurate answers

Wiki Mode

Agent-driven auto-generation of structured, interlinked markdown Wiki pages from raw documents; in-browser manual editing, page revision history, line-level diff and one-click rollback

Skill Catalog & Sandbox

Workspace skill catalog (ClawHub / SkillHub / git / zip) installed onto session-persistent Docker / E2B / Cube sandboxes; 
shell_exec
, file tools, artifacts, per-config network policy; Local host-process backend removed

Long-term Memory

Cross-session memory (profile / preference / fact / task / interest) with auto-extract, user confirm, and on-demand 
search_memory

Tool Calling

Built-in tools, MCP tools (incl. OAuth2 remote services, mid-conversation OAuth), web search; 
@Skill / @MCP
 mentions to scope the agent runtime per turn

Conversation Strategy

Online Prompt editing, retrieval threshold tuning, multi-turn context awareness, per-agent citation output toggle

Suggested Questions

Auto-generated question suggestions and after-answer follow-ups based on knowledge base content

Temporary Attachments

Session-scoped image / document uploads with async parsing for one-off Q&A, with a combined image + attachment limit

Citations & RAG Progress

Inline citation popovers and a references drawer (web / KB source distinction), shared markdown rendering, and stage-by-stage RAG pipeline progress in chat

Session Management

Filter and group sidebar sessions by source (Web / IM / Embed), with inline session-title rename

Knowledge Management

Capability

Details

Knowledge Base Types

FAQ / Document / Wiki with folder import, URL import, multi-tag management, and online entry

Folder Tree

Folder uploads keep their original directory structure, with a sidebar tree for browsing, folder rename, and re-filing documents into another folder

Chunk Editing & Revisions

Edit retrieval chunks directly in the UI with per-version snapshots, diff and one-click rollback, and automatic reindexing after an edit; generated questions can be added, edited, deleted and regenerated; custom document metadata supported

Per-Upload Process Config

Override parser, chunking, multimodal (VLM / ASR), graph extraction, and question generation per upload batch via upload-confirm dialog or 
process_config
 API; reparse with new settings

Batch Reparse

Re-queue parsing for multiple documents at once with optional per-batch 
process_config

Data Source Import

Auto-sync from Feishu wiki / Feishu Drive / Lark / GitLab / Tencent IMA / Notion / Yuque / RSS feeds (more data sources coming soon); incremental and full sync

Document Formats

PDF / Word / Txt / Markdown / HTML / EPUB / MHTML / Images / CSV / Excel / PPT / JSON / XMind

Auto-Tagging

After parse, pick matching tags from the knowledge base's existing set without creating tags or overwriting manual ones

Retrieval Strategies

BM25 sparse / Dense retrieval / GraphRAG / parent-child chunking / HNSW-accelerated pgvector (1024-dim) / multi-dimensional indexing

Batch Selection & Tagging

Marquee drag-select multiple documents in the KB list for batch reparse and batch tagging (common tags pre-selected)

E2E Testing

Full-pipeline visualization with recall hit rate, BLEU / ROUGE metric evaluation

Integrations & Extensions

Capability

Details

LLMs

OpenAI / Azure OpenAI / Anthropic (Claude) / DeepSeek / Qwen (Alibaba Cloud) / Zhipu / Hunyuan / Doubao (Volcengine) / Gemini / MiniMax / NVIDIA / Novita AI / SiliconFlow / OpenRouter / Requesty / LiteLLM / Ollama

Embeddings

Ollama / BGE / GTE / Zhipu / OpenAI-compatible APIs

Vector DBs

PostgreSQL (pgvector) / Elasticsearch / OpenSearch / Milvus / Weaviate / Qdrant / Apache Doris / Tencent VectorDB

Object Storage

Local / MinIO / AWS S3 (IAM Role / IRSA default credential chain) / Volcengine TOS / Alibaba Cloud OSS / Kingsoft Cloud KS3 / Huawei Cloud OBS; 
multiple storage instances per workspace
 with per-KB binding and a default instance

IM Channels

WeCom / Feishu / Lark (Feishu International) / QQBot / Slack / Telegram / DingTalk / Mattermost / WeChat / Yunzhijia

Website Embed

Publish agents via embed widget with domain allowlists, rate limits, and secure-mode token exchange

Web Search

DuckDuckGo / Bing / Google / Tavily / Baidu / Ollama / SearXNG / Keenable / Zhipu AI / Exa / Metaso

API Integration

Scoped API keys (capability-level grants + per-KB restriction + throttled last-used tracking) with an API integration playground; MCP OAuth and embed sessions isolated per principal; 
resource_urls=public
 returns directly loadable file/image URLs, removing the second authenticated proxy call

MCP Server

Official PyPI package 
tencent-weknora-mcp
 with 29 tools over stdio / SSE / HTTP transports

Platform

Capability

Details

Deployment

Local / Docker / Kubernetes (Helm) with private and offline support

UI

Web UI / RESTful API / CLI (
weknora
) / Chrome Extension / Website Embed Widget / WeChat Mini Program

Access Control

Workspace RBAC with 4-tier role matrix (Owner / Admin / Contributor / Viewer), per-KB resource ownership, per-workspace audit log, invite-only workspaces, tenantless provisioning & gated self-service workspace creation, admin password reset (session revocation), cross-workspace superuser, scoped API keys

Security

AES-256-GCM at-rest encryption for API keys and MCP / data-source credentials with graceful key rotation; gRPC TLS + Token between app and docreader; Redis TLS; SSRF-safe HTTP client (data sources, URL import, redirect chains); secret redaction in responses; skill sandbox isolation (Docker opt-in / E2B / Cube) with per-config network policy; OIDC ID-token JWKS verification; optional complex-password policy

Observability

Integrated Langfuse (sole tracing backend) for ReAct loops, token tracking, tool calls, and pipeline tracing; built-in Langfuse-style document parsing trace timeline with stage-by-stage progress; system-admin runtime task-queue dashboard (queue depth, per-model concurrency, failed-task inspection & manual retry)

Task Management

MQ async tasks with per-stage worker-pool governance (core / post-process / enrichment / maintenance + elastic shared pool, plus an independent Wiki pool) and per-model background concurrency governors; automatic database migration on version upgrade

Model Management

Centralized config, declarative built-in models via YAML, per-knowledge-base model selection, per-model thinking-mode and embedding-dimension overrides, interactive model test debugger, multi-workspace built-in model sharing, WeKnora Cloud hosted models and parsing

## 🧩 Chrome Extension

WeKnora Chrome Extensionlets you capture web content directly into your WeKnora knowledge base. Select text, images, or entire pages in the browser and save them as knowledge entries with one click — no copy-paste or file upload needed.

## 📱 WeChat Mini Program

TheWeKnora Mini Programprovides a lightweight mobile client for configuring WeKnora API access, selecting knowledge bases, importing URLs, and asking knowledge chat from WeChat.

## 🦞 ClawHub Skill

WeKnora ClawHub Skillis a WeKnora skill published on the ClawHub platform. Once installed, it enables document import (file / URL / Markdown), hybrid search (vector + keyword) across knowledge bases, and knowledge entry management — all through the WeKnora REST API.

* Document Import— Upload files, import web pages, or write Markdown knowledge via the agent
* Hybrid Search— Search within or across knowledge bases with vector + keyword retrieval
* Knowledge Management— List, browse, edit, and delete knowledge entries programmatically

## 🐋 DeepSeek Harness Plugin

@wxg-prc-cpg/dsh-weknorais the officialDeepSeek Harness(dsh) plugin (docs). The harness ships no retrieval, embedding or knowledge-base capability of its own, so the plugin gives a coding agent your documents:dsh plugin --profile web add @wxg-prc-cpg/dsh-weknora, point it at a deployment, and four read-only tools appear in the agent's tool set.

* weknora_search— hybrid retrieval returning source passages verbatim, each with a reusableknowledge_id
* weknora_read_document— one document's passages reassembled in order, with paging
* weknora_ask— WeKnora's own composed answer with citations, over the RAG or the ReAct pipeline
* weknora_list_knowledge_bases— knowledge base names and ids, so the agent can scope its own search

## ⌨️ Command-Line Interface

weknorais the official CLI for driving the API from a terminal or an AI
agent. It isagent-first: every command emits a stable JSON envelope by
default (with typed error codes mapped to exit codes), and--format textrenders for humans. It also serves a curated MCP tool surface
(weknora mcp serve) and ships bundled Agent Skills.

weknora profile add prod --host https://kb.example.com --use
weknora auth login
weknora kb list
weknora link --kb my-knowledge-base 
#
 bind the current directory

weknora doc upload notes.md
weknora chat 
"
summarise the design doc
"

For headless / CI use, setWEKNORA_API_KEY+WEKNORA_HOSTand skipauth loginentirely — no credentials written to disk.

Seecli/README.mdfor install + 5-minute quickstart andcli/AGENTS.mdfor the operational contract AI agents rely on.

## 🚀 Getting Started

### 🛠 Prerequisites

* Docker&Docker Compose
* Git

### 📦 Installation & Launch

git clone https://github.com/Tencent/WeKnora.git

cd
 WeKnora
cp .env.example .env 
#
 Edit .env as needed, see comments in the file

docker compose pull 
#
 Pull the latest images

docker compose up -d 
#
 Start core services

Once started, visithttp://localhostto get started.

To use a local Ollama model, runollama serve > /dev/null 2>&1 &first.

### 🔄 Upgrading

If you already have WeKnora running and downloaded a newer release:

#
 Set WEKNORA_VERSION in .env to the target release (e.g. 0.7.0), or keep latest

docker compose pull 
#
 Pull images matching WEKNORA_VERSION

docker compose up -d 
#
 Recreate containers with new images

docker compose up -dalone reuses locally cached images and may leave the UI version out of sync with the release you downloaded.

### 🔧 Optional Services (Docker Compose Profiles)

Add--profileflags to enable additional components. Multiple profiles can be combined:

Profile

Description

Command

(default)

Core services

docker compose pull && docker compose up -d

full

All features

docker compose --profile full pull && docker compose --profile full up -d

neo4j

Knowledge Graph (Neo4j)

docker compose --profile neo4j pull && docker compose --profile neo4j up -d

minio

Object Storage (MinIO)

docker compose --profile minio pull && docker compose --profile minio up -d

langfuse

Tracing (Langfuse)

docker compose --profile langfuse pull && docker compose --profile langfuse up -d

Combine profiles:docker compose --profile neo4j --profile minio pull && docker compose --profile neo4j --profile minio up -d

Stop services:docker compose down

### 🌐 Service URLs

Service

URL

Web UI

http://localhost

Backend API

http://localhost:8080

Langfuse Tracing

http://localhost:3000

## MCP Server

Please refer to theMCP Configuration Guidefor the necessary setup.

## 🔌 Using WeChat Dialog Open Platform

WeKnora serves as the core technology framework for theWeChat Dialog Open Platform, providing a more convenient usage approach:

* Zero-code Deployment: Simply upload knowledge to quickly deploy intelligent Q&A services within the WeChat ecosystem, achieving an "ask and answer" experience
* Efficient Question Management: Support for categorized management of high-frequency questions, with rich data tools to ensure accurate, reliable, and easily maintainable answers
* WeChat Ecosystem Integration: Through the WeChat Dialog Open Platform, WeKnora's intelligent Q&A capabilities can be seamlessly integrated into WeChat Official Accounts, Mini Programs, and other WeChat scenarios, enhancing user interaction experiences

## 📘 API Reference

Official product documentation:website-docs/— the complete documentation set organized as Getting Started → Architecture → Features → API → Clients → Development, covering ~360 API endpoints, ~150 environment variables, and 9 extension points. The directory is also a VitePress site: runcd website-docs && npm install && npm run devto preview locally, or deploy it standalone with theDockerfileinside.

Troubleshooting FAQ:Troubleshooting FAQ

Detailed API documentation is available at:API Docs

Product plans and upcoming features:Roadmap

## 🧭 Developer Guide

### ⚡ Fast Development Mode (Recommended)

If you need to frequently modify code,you don't need to rebuild Docker images every time! Use fast development mode:

#
 Start infrastructure

make dev-start

#
 Start backend (new terminal)

make dev-app

#
 Start frontend (new terminal)

make dev-frontend

Development Advantages:

* ✅ Frontend modifications auto hot-reload (no restart needed)
* ✅ Backend modifications quick restart (5-10 seconds, supports Air hot-reload)
* ✅ No need to rebuild Docker images
* ✅ Support IDE breakpoint debugging

Detailed Documentation:Development Environment Quick Start

## 🤝 Contributing

Welcome to submitIssuesor Pull Requests.

Process:Fork → Create branch → Commit changes → Open PR

Standards:Format code withgofmt, followConventional Commits(feat:/fix:/docs:/test:/refactor:)

### Validation

For a focused PR, validate the changed scope first:

git fetch origin main
git diff --check origin/main...HEAD
golangci-lint run --new-from-rev=origin/main ./...
go 
test
 ./path/to/changed/package -count=1

Rungofmton changed Go files before committing. For frontend changes, run the relevant tests fromfrontend/and usenpm run type-checkwhen the change affects TypeScript or Vue components.

The full maintainer gate remains:

make fmt
make lint
make 
test

make fmtformats the entire Go repository, so run it only with a clean worktree and review the resulting diff. Some full-suite tests require local infrastructure or service configuration. If a full check fails for an unrelated baseline or environment reason, include the exact command and failure in the PR while still providing passing targeted tests for your change.

## 🔒 Security Notice

Important:Starting from v0.1.3, WeKnora includes login authentication functionality to enhance system security. For production deployments, we strongly recommend:

* Deploy WeKnora services in internal/private network environments rather than public internet
* Avoid exposing the service directly to public networks to prevent potential information leakage
* Configure proper firewall rules and access controls for your deployment environment
* Regularly update to the latest version for security patches and improvements

## 👥 Contributors

Thanks to these excellent contributors:

## 📄 License

This project is licensed under theMIT License.
You are free to use, modify, and distribute the code with proper attribution.