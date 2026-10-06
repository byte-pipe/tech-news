---
title: GitHub - DuarteSantos8/openGym: Self-hosted gym & body-weight tracker — plan routines, log workouts (supersets, warm-ups, cardio), see which muscles a...
url: https://github.com/DuarteSantos8/openGym
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-10-06T16:49:47.181533
---

# GitHub - DuarteSantos8/openGym: Self-hosted gym & body-weight tracker — plan routines, log workouts (supersets, warm-ups, cardio), see which muscles a...

# openGym – Self‑hosted Gym & Body‑Weight Tracker

## Overview
- openGym is a self‑hosted workout app that lets you plan routines, log sets and body‑weight, and view progress without relying on third‑party servers.  
- Data stays in a folder you control; the app runs via Docker Compose and works offline, syncs across devices, and supports passkey (Face ID, Touch ID, fingerprint) login.  
- No subscriptions, ads, telemetry, or external accounts required.

## Core Features  

### Planning
- Weekly routine per weekday from a library of **1,324 exercises** with animated demos, searchable by muscle map and filterable by owned equipment.  
- Four starter plans (Push/Pull/Legs, Upper/Lower, Full Body, 5×5) that load as editable routines.  
- Flexible scheduling: move sessions, choose week start (Monday/Sunday), add supersets, warm‑ups, drop sets, rest‑pause, timed exercises, cardio, rest times, and planned deloads.  
- Custom exercises with personal photos/GIFs/videos; location data stripped before upload.

### Training
- Guided sessions: auto‑start today’s workout, pre‑filled weights, rest timer, real‑time PR detection.  
- Quiet workout screen with per‑exercise menus, set‑specific cards/lists, and optional classic button rows.  
- Effort column (RIR/RPE) colour‑coded with plain‑language descriptions.  
- Plate‑math for barbell, EZ bar, trap bar, Smith machine based on owned plates; body‑weight exercises handle dip belts and per‑side reps.  
- Screen stays awake; optional flashing rest‑timer alerts.

### Progress Tracking
- Routine‑ or exercise‑specific progression rules (linear, Greyskull LP, double progression, time‑based).  
- Estimated 1RM curves, Structural Balance ratios (Poliquin, Thibaudeau, ATG), year‑long activity heatmap.  
- Muscle map showing volume distribution, recovery status, and untrained areas.  
- Body‑weight chart with goal line.  
- Edit past workouts; history re‑calculates automatically.

### Accounts & Data Management
- Passkey authentication per profile; optional password login; new devices pair via one‑time code or QR.  
- Real‑time sync between multiple devices (merge, not overwrite).  
- Import from FitNotes, Strong, Hevy (CSV/API) and Apple Health weight exports; full export as a single JSON file.  
- Share plans as small files or printable PDFs.  
- Optional admin dashboard with invite‑only signup and activity log.  
- Multilingual support (17 languages, including RTL Arabic) with translated exercise names and instructions.

### Optional Extras (off by default)
- **AI Coach**: Generates weekly routines and suggests adjustments based on logged data; runs locally with your own Anthropic, OpenAI, Gemini, or Ollama key.  
- **MCP Server**: Local, read‑only assistant (e.g., Claude Desktop) that can answer training‑history questions.

## Quick Start (Docker Compose)
1. `git clone https://github.com/DuarteSantos8/openGym && cd openGym`  
2. `cp .env.example .env`  
3. `docker compose pull` (pre‑built amd64 + arm64 images)  
4. `docker compose up -d`  
5. Open `http://localhost:8080`, create a profile, and the app downloads ~140 MB of exercise media on first run.  

- For mobile access with passkeys, configure HTTPS and a domain (Cloudflare Tunnel, Caddy, Traefik, nginx, or LAN/Kubernetes guides).  
- Images are also available on GitLab Container Registry and GHCR; you can switch sources or build locally (`docker compose up -d --build`).

## Configuration (via `.env`)
| Variable | Purpose | Default |
|---|---|---|
| `RP_ID` | Hostname bound to passkeys | `localhost` |
| `ORIGIN` | Full URL the app is served from | `http://localhost:8080` |
| `WEB_PORT` | Host port for web UI | `8080` |
| `NGINX_PORT` | Internal container port for web | `80` |
| `BACKEND` | API service name proxied as `/api` | `api` |
| `PORT` | API listening port (proxied) | `3000` |
| `RP_NAME` | Name shown in passkey prompt | `openGym` |
| `SESSION_DAYS` | Sign‑in session length (days) | `90` |
| `ADMIN_UIDS` | Comma‑separated admin user IDs | *(none)* |
| `INVITE_ONLY` | Require invite code for new profiles | `off` |
| `ALLOW_GUEST` | Allow “continue without account” | `on` |
| `PASSWORD_LOGIN` | Enable name/password login | `off` |
| `AUDIT_LOG` | Record sign‑ins/admin actions | `on` |
| `AUDIT_MAX` | Max events kept in log | `5000` |
| `AUDIT_DAYS` | Days to retain audit log | `90` |
| `COACH_DISABLED` | Force AI coach off globally | *(unset)* |
| … | (additional variables control proxy trust, VAPID keys, API image, etc.) |  |

Push‑notification keys are generated on first run (`./data/vapid.json`). Data directory is mounted at `/data` inside containers.  

---  

*openGym provides a modern, privacy‑first workout tracking experience you can host yourself, with extensive planning, training, and analytics features, plus optional AI assistance.*