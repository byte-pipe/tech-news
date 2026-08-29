---
title: GitHub - THU-MAIC/OpenMAIC: Open Multi-Agent Interactive Classroom — Get an immersive, multi-agent learning experience in just one click · GitHub
url: https://github.com/THU-MAIC/OpenMAIC
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-08-30T06:03:29.830178
---

# GitHub - THU-MAIC/OpenMAIC: Open Multi-Agent Interactive Classroom — Get an immersive, multi-agent learning experience in just one click · GitHub

# OpenMAIC Repository Overview

## Highlights
- One‑click lesson generation from a topic description or uploaded materials.  
- Multi‑agent classroom where AI teachers and peers lecture, discuss, and interact in real time.  
- Supports slides, quizzes, interactive HTML simulations, and project‑based learning (PBL).  
- Whiteboard with drawing, formula writing, and text‑to‑speech for spoken explanations.  
- Export options include editable .pptx slides and interactive .html pages.  
- OpenClaw integration enables classroom generation directly from Feishu, Slack, Discord, Telegram, and over 20 other messaging apps.

## Recent Releases (News)
- **v1.0.0 (2026‑08‑27)** – Introduces an agent workbench, durable server‑backed sessions, session material uploads, 20 built‑in skills, and provider‑neutral architecture.  
- **v0.3.2 (2026‑08‑14)** – Video export hardening, full document cutover with Postgres persistence, asset registry, new locales, Amazon Bedrock, Atlas Cloud, Claude search providers, and FunASR ASR.  
- **v0.3.1 (2026‑07‑21)** – One‑click MP4 export, Postgres runtime storage, slide manipulation UI, validated JSON‑Patch “Edit with AI”, expanded document parsing, new providers (Azure OpenAI, SearXNG, ComfyUI) and GPT‑5.6 model family.  
- **v0.3.0 (2026‑06‑28)** – Project‑Based Learning UI, Pro‑mode editor agent, @openmaic/* SDK published to npm, optional per‑stage model routing, new models (GLM‑5.2, Kimi K2.7 Code, Qwen3.7 Plus/Max), vocational‑learning engine, Korean locale, license change to MIT.  
- **v0.2.2 (2026‑06‑02)** – MAIC Editor Pro Mode, editable outline, offline classroom export, new search providers (Brave, Baidu, Bocha, MiniMax) and Azure STT, new models (Claude Opus 4.8, MiniMax M3, Gemini 3.5 Flash), Traditional Chinese and Brazilian Portuguese locales.  
- **v0.2.1 (2026‑04‑26)** – Integrated VoxCPM2 TTS with voice cloning, per‑model thinking config, end‑of‑course completion page with persistent quiz state, latest models (DeepSeek‑V4, GPT‑5.5, GPT‑Image‑2, Xiaomi MiMo, Hy3).  
- **v0.2.0 (2026‑04‑20)** – Deep Interactive Mode with 3D visualizations, simulations, games, mind maps, and online programming.  
- **v0.1.1 (2026‑04‑14)** – Automatic language inference, ACCESS_CODE authentication, classroom ZIP export/import, custom TTS/ASR providers, Ollama support.  
- **v0.1.0 (2026‑03‑26)** – Discussion TTS, immersive mode, keyboard shortcuts, whiteboard enhancements, new providers.

## Quick Start
1. **Prerequisites** – Node.js ≥ 20, pnpm ≥ 10.  
2. **Clone & Install**  
   ```bash
   git clone https://github.com/THU-MAIC/OpenMAIC.git
   cd OpenMAIC
   pnpm install
   ```  
3. **Configure** – Copy `.env.example` to `.env.local` and set at least one LLM provider key (e.g., `OPENAI_API_KEY`, `AZURE_OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `GOOGLE_API_KEY`).  

## Repository Structure
- Core directories: `app`, `assets`, `components`, `configs`, `e2e`, `eval`, `lib`, `packages`, `public`, `render-service`, `scripts`, `skills`, `tests`, `types`.  
- Key files: `README.md`, `CHANGELOG.md`, `Dockerfile`, `docker-compose.yml`, `package.json`, `pnpm-lock.yaml`, `tsconfig.json`, `vercel.json`.  

## OpenClaw Integration
- Install the OpenMAIC skill via `clawhub install openmaic` or ask your Claw assistant to “install OpenMAIC skill”.  
- Choose **Hosted mode** (access code from `open.maic.chat`) or **Self‑hosted** (follow the guided setup).  
- Command the assistant, e.g., “teach me quantum physics”, and receive a generated classroom instantly.  

## License & Contribution
- Licensed under the MIT License (re‑licensed from AGPL‑3.0).  
- Contribution guidelines are provided in `CONTRIBUTING.md`.