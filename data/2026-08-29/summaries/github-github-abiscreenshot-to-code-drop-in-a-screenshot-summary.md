---
title: GitHub - abi/screenshot-to-code: Drop in a screenshot and convert it to clean code (HTML/Tailwind/React/Vue) · GitHub
url: https://github.com/abi/screenshot-to-code
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-08-29T01:31:53.473056
---

# GitHub - abi/screenshot-to-code: Drop in a screenshot and convert it to clean code (HTML/Tailwind/React/Vue) · GitHub

# screenshot-to-code

## Overview
- AI‑powered tool that transforms screenshots, mockups, Figma designs, and screen recordings into clean, functional code.  
- Available as a hosted product at **screenshottocode.com** and as an open‑source project that can be run locally.

## Supported Stacks
- HTML + Tailwind  
- HTML + CSS  
- React + Tailwind  
- Vue + Tailwind  
- Bootstrap  
- Ionic + Tailwind  

## Default AI Models
- Gemini 3 Flash Preview / Gemini 3.1 Pro Preview (primary, best quality)  
- GPT‑5.5 and GPT‑5.4 Mini  
- Claude Opus 4.6, Claude Opus 4.8  
- z‑image‑turbo (Replicate) for image generation and editing  

## Getting Started

### Choose a path
- **Run locally** – ideal for customization, self‑hosting, or contribution.  
- **Use the hosted app** – fastest way to try the service without any setup.

### Local setup
1. Clone the repository.  
2. Add at least one model provider key (OpenAI, Anthropic, or Gemini). Gemini and Replicate are strongly recommended.  
3. **Backend (FastAPI)**
   - Install Poetry, create a `.env` file with the required keys.  
   - `poetry install`  
   - Install Chromium for screenshot preview: `poetry run playwright install chromium` (Linux may need `--with-deps`).  
   - Start the server: `poetry run uvicorn main:app --reload --port 7001`.  
4. **Frontend (React/Vite)**
   - `cd frontend`  
   - `pnpm install && pnpm dev`  
   - Open `http://localhost:5173` in a browser.  

### Docker option
- Create a `.env` file with API keys.  
- Run `docker-compose up -d --build`.  
- The app will be reachable at `http://localhost:5173` (no hot‑reload for development).

## API Keys Overview

| Key                | Required?                     | What it unlocks                                            |
|--------------------|------------------------------|-----------------------------------------------------------|
| OPENAI_API_KEY     | One of three providers       | GPT code‑generation (GPT‑5.5, GPT‑5.4 Mini)               |
| ANTHROPIC_API_KEY  | One of three providers       | Claude code‑generation (Opus 5, Opus 4.8, etc.)           |
| GEMINI_API_KEY     | Strongly recommended         | Gemini code‑generation, real‑asset extraction, video mode |
| REPLICATE_API_KEY  | Strongly recommended         | Image editing, background removal, image generation       |

- Supplying multiple keys lets the app automatically select the strongest model mix.  
- Ollama open‑source models can be used but are not recommended due to lower quality.

## Frequently Asked Questions

- **Backend errors** – try the suggested fixes; if unresolved, open an issue.  
- **Obtaining an OpenAI key** – see `Troubleshooting.md` in the repo.  
- **Using a proxy** – set `OPENAI_BASE_URL` in `backend/.env` or via the UI settings (must include `/v1`).  
- **Changing backend host** – edit `VITE_HTTP_BACKEND_URL` and `VITE_WS_BACKEND_URL` in `frontend/.env.local`.  
- **UTF‑8 errors on Windows** – open `.env` in Notepad++ and set encoding to UTF‑8.  
- **Providing feedback** – open an issue on GitHub or contact the author on Twitter.  

## Examples
- NYTimes – original screenshot vs. generated replica.  
- Instagram – video demo (`instagram.mp4`).  
- Hacker News – video demo (`hacker.news.mp4`).