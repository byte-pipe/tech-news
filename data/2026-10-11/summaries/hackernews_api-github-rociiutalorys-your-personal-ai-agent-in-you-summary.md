---
title: GitHub - rociiu/talorys: Your personal AI agent in your own Cloudflare account. Chat, memory, tasks, notes and scheduled reminders, deployed with one...
url: https://github.com/rociiu/talorys
date: 2026-10-10
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-10-11T13:38:57.295857
---

# GitHub - rociiu/talorys: Your personal AI agent in your own Cloudflare account. Chat, memory, tasks, notes and scheduled reminders, deployed with one...

# Talorys – Personal AI Agent on Cloudflare

## Overview
- Open‑source AI assistant that runs entirely inside a single Cloudflare account.  
- Provides chat, memory, tasks, notes, projects, and scheduled automations.  
- No external server, database, or telemetry; all data stored in a SQLite‑backed Durable Object.  
- Designed for a single user; installer sets an owner password.

## Core Features
- Private chat with streaming responses, Markdown, and tool activity indicators.  
- Persistent memory of personal facts; only relevant memories are sent to the model each turn.  
- Full CRUD for tasks, notes, and projects via UI or chat commands.  
- Automations: one‑time/recurring reminders, daily digests, optional AI routines; executed by Durable Object alarms.  
- Operates without Workers AI; non‑AI features remain functional when AI quota is exhausted.

## Architecture
- Browser → Cloudflare Pages (React UI + API function) → Private Worker (Hono router) → TalorysAgent (Durable Object).  
- Durable Object stores SQLite tables for conversations, memories, tasks, notes, projects, automations, sessions, settings, and usage.  
- Workers AI model `@cf/zai-org/glm-4.7-flash` used for chat (streaming + tool calls).  
- Alarms drive scheduled reminders; the agent Worker has no public URL.

## Cloudflare Services Used (Free‑Tier Friendly)
| Service | Purpose | Free Plan |
|---------|---------|-----------|
| Cloudflare Pages | Frontend + Pages Function | Yes |
| Cloudflare Workers | Private API Worker | Yes |
| Durable Objects (SQLite) | Data storage & scheduling alarms | Yes |
| Workers AI | Chat model (`@cf/zai-org/glm-4.7-flash`) | Yes (daily allocation) |

Talorys does not provision R2, D1, KV, Vectorize, AI Search, Workflows, or any paid service.

## Deployment
- Single command: `npx create-talorys@latest`.  
- Installer steps:  
  1. Checks Node 20.18+ and uses bundled Wrangler CLI.  
  2. Authenticates with Cloudflare (OAuth flow).  
  3. Lets you select an account and agent name.  
  4. Prompts for an owner password (hashed locally, stored as a Cloudflare secret).  
  5. Generates a 256‑bit session secret and unique resource names.  
  6. Deploys the private Worker, creates the SQLite Durable Object, stores secrets, and deploys the Pages project with service binding.  
  7. Verifies deployment without running AI inference.  
  8. Prints the live `https://…pages.dev` URL.  
- Creates a `talorys/` directory containing `talorys.json` (installation metadata, no secrets) for future updates.  
- Re‑running the command reconciles existing resources; no data loss.  
- Non‑interactive install example:  
  `TALORYS_OWNER_PASSWORD=... npx create-talorys@latest --yes --account-id <id>` (requires `CLOUDFLARE_API_TOKEN` if not logged in).  

### Required Permissions
- Account › Workers Scripts › Edit  
- Account › Cloudflare Pages › Edit  
- Account › Workers AI › Read  
- Account › Account Settings › Read  
- User › User Details › Read (optional, shows email)

## Access & Management
- Open the printed URL, enter the owner password, and start chatting.  
- Sessions can be managed under **Settings → Security**.  
- Password reset: `npx create-talorys@latest reset-password` (replaces secret and signs out all devices).

## Data Privacy & Security
- All user data resides in a single SQLite‑backed Durable Object within the user’s Cloudflare account.  
- No telemetry, analytics, tracking, or advertising code; nothing is sent to the developers.  
- Cloudflare processes data only to provide its services (including AI inference).  
- Security model and threat mitigations described in `docs/security.md`.

## Cost Model
- Designed to fit the Cloudflare Workers Free plan; does not enable paid features automatically.  
- Free plan quotas apply (requests, Durable Object usage, daily AI Neuron allocation).  
- When AI allocation is exhausted, chat shows a clear message; other features continue unchanged.  
- Paid plans incur Cloudflare charges for usage beyond free limits.  
- Guardrails configurable in **Settings → AI**: max output tokens, max context tokens, max tool calls, max reasoning steps, daily AI request caps, and daily scheduled AI run caps.  
- Simple reminders and task digests never use AI.  
- Usage panel shows local estimates and links to the Cloudflare dashboard for exact Neuron usage.

## Local Development
- Requirements: Node 20.18+.  
- Steps:  
  ```bash
  git clone https://github.com/rociiu/talorys.git
  cd talorys
  npm install
  npm run dev
  ```  
- `npm run dev` starts the agent Worker (port 8787), the Pages Function proxy (port 8788), and the Vite UI (`http://localhost:5173`).  
- Uses a deterministic mock AI provider; no Cloudflare login needed.  
- State persists in `.wrangler/state`.  
- Additional scripts: `npm run build`, `npm test`, `npm run test:e2e`, `npm run test:pack`, `npm run typecheck`, `npm run lint`.  
- Development details in `docs/development.md`.

## Backup & Restore
- Export via **Settings → Privacy → Download backup** → `talorys-backup.json` (includes conversations, memories, tasks, notes, projects, settings, automations; excludes sessions and credentials).  
- Import validates the file and merges it in a single transaction; importing the same backup twice is ignored.