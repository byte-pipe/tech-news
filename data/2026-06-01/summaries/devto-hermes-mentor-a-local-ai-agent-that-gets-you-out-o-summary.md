---
title: Hermes Mentor — A Local AI Agent That Gets You Out of Tutorial Hell - DEV Community
url: https://dev.to/aditya_007/hermes-mentor-a-local-ai-agent-that-gets-you-out-of-tutorial-hell-5910
date: 2026-05-27
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-06-01T04:20:21.457948
---

# Hermes Mentor — A Local AI Agent That Gets You Out of Tutorial Hell - DEV Community

# Hermes Mentor — A Local AI Agent That Gets You Out of Tutorial Hell

## Overview
- A fully local, privacy‑first AI mentorship agent built with Hermes Agent.
- Scans public GitHub repositories to identify skill gaps and creates a personalized 4‑week project roadmap.
- Delivers daily challenges via Telegram and tracks progress through two‑way conversation.
- Runs entirely on the user’s machine using Ollama (qwen2.5‑coder:7b); no cloud services or API keys required.

## Core Features
- **Audit** – Reads languages, CI/CD configurations, test files, and README quality across all public repos.
- **Gap Identification** – Local LLM reasons over the code to pinpoint missing skills.
- **Roadmap Generation** – Four weekly projects, each designed to close a specific gap without relying on tutorials.
- **Daily Nudges** – Scheduled Telegram messages at 08:30 on weekdays with hints, encouragement, and celebration.
- **Two‑Way Telegram Agent** – Accepts repo links, creates TODO tasks, updates status, and can open pull requests.
- **Persistent Memory** – Developer profile stored in `~/.hermes/memory/` and loaded on each run.
- **Autonomous Cron** – `hermes_cron.py` installs a weekday 08:30 cron job for daily actions.

## Demo Highlights
- Audited 20 repositories in real time.
- Printed a roadmap with identified gaps.
- Showed two‑way interaction via Telegram.
- Automatically saved the memory file.
- Installed cron and delivered the first daily nudge.
- Created a real GitHub pull request after receiving a repository link.

## Technical Stack
- Agent orchestration: Hermes Agent (NousResearch)
- Local LLM: Ollama with qwen2.5‑coder 7B
- GitHub access: PyGithub (REST API)
- Messaging: python‑telegram‑bot
- Scheduling: Linux crontab via Hermes cron
- Memory storage: `~/.hermes/memory/`
- Skill system: Hermes skill files (`agentskills.io` format)
- Environment: WSL2 on Windows
- Language: Python 3.12

## Project Structure
```
hermes-mentor/
├── mentor_agent.py          # Core agent: audit, roadmap, Telegram
├── hermes_cron.py           # Daily nudge scheduler
├── setup.sh                 # Automated setup wizard
├── requirements.txt
├── .env.example
├── hermes-mentor.html       # Landing page
├── config/
│   └── hermes-config.yaml   # Ollama & Telegram configuration
└── skills/
    └── github-audit-mentor.md  # Reusable Hermes skill file
```

## How Hermes Agent Is Used
- Persistent Memory: after each audit, a markdown profile is written to `~/.hermes/memory/` and automatically reloaded in future sessions.
- Skill Learning (GEPA Loop): the skill file updates with new findings, improving accuracy for subsequent audits.
- Cron Scheduling: hands‑off daily nudges that advance the roadmap without user intervention.
- Two‑Way Telegram Gateway: the bot parses repository URLs, creates tasks, replies with next steps, and can execute commands such as opening a pull request.
- Multi‑Step Reasoning: fetch repos → extract signals → reason gaps → generate projects → deliver via Telegram → save memory → update skill → listen for replies → plan next steps.

## Motivation
- Personal experience with “tutorial hell”: many hours of tutorials but difficulty building real projects.
- Existing tools (Roadmap.sh, GitHub Copilot) provide static paths or code suggestions but do not analyze a developer’s actual work.
- Hermes Mentor bridges that gap by analyzing real code, generating actionable projects, and acting as a private mentor.

## Links
- Landing page: https://thecoderadi.github.io
- Repository: https://github.com/TheCoderAdi/hermes-mentor
- Author: Aditya Swayam Siddha (@TheCoderAdi)