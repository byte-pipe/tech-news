---
title: Build with Notion’s Developer Platform – Notion
url: https://www.notion.com/product/dev
date: 2026-05-17
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-05-17T06:02:44.977927
---

# Build with Notion’s Developer Platform – Notion

# Build with Notion’s Developer Platform – Notion

## Sync any data source into Notion
- Workers let you continuously upsert external records into a Notion database.
- Declarative schema defines properties, primary key, and initial title.
- Persistent cursor tracks changes; schedule (e.g., every 5 minutes) drives sync.
- Example: Zendesk tickets sync using `worker.database` and `worker.sync`.

## Build any tool for your agents
- Create custom tools that generate assets, query live data, or call any API.
- **Asset generation** – read a Notion page, convert headings to slides, build a `.pptx`, upload back to the page.
- **Data warehouse query** – run arbitrary SQL against a deals table (e.g., Snowflake) from a Notion tool.
- **App actions** – define tools like `listFavorites`, `orderFavorite`, `checkOrder` to interact with external services (e.g., DoorDash) via Browserbase.

## Trigger Notion workflows from anywhere
- Listen to incoming webhooks from any app.
- Run workflows that combine Notion Agents, pages, databases, and external APIs.
- Pre‑built examples include PR merged, customer canceled, candidate signed offer, issue escalated, etc.
- Workflow actions: create incidents, send kudos, onboard pages, notify teams, update records, etc.

## All of this, on a hosted runtime
- Workers run in isolated sandboxes managed by Notion, removing the need for self‑hosted servers.
- Deploy with the Notion CLI: `ntn deploy worker`.
- Build, upload, and update workers directly on Notion’s infrastructure.

## Bring your favorite agents into Notion
- Connect external LLM agents (Claude, Cursor, Decagon, or custom) as first‑class collaborators.
- **Mention** – tag agents in pages, comments, or chats.
- **Assign** – hand off tasks or trigger agents in parallel.
- **Orchestrate** – watch agents call tools and act, with optional human review.
- **BYO Agent** – use the External Agents API to give agents triggers, tools, and permissions.

## CLI, API, MCP, SDK – LFG
- **Notion CLI (Beta)** – token‑efficient commands to build and deploy syncs and tools.
- **Notion API** – convert docs to Markdown, build internal tools with PATs or shared connections.
- **Notion MCP** – search, read, edit pages/databases with up to 91 % fewer tokens.
- **Notion Agent SDK (Alpha)** – integrate agents into any app, trigger runs via API, maintain multi‑turn threads, stream responses in real time.