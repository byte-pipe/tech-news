---
title: Hermes Mentor — A Local AI Agent That Gets You Out of Tutorial Hell - DEV Community
url: https://dev.to/aditya_007/hermes-mentor-a-local-ai-agent-that-gets-you-out-of-tutorial-hell-5910
site_name: devto
content_file: devto-hermes-mentor-a-local-ai-agent-that-gets-you-out-o
fetched_at: '2026-06-01T04:17:34.335438'
original_url: https://dev.to/aditya_007/hermes-mentor-a-local-ai-agent-that-gets-you-out-of-tutorial-hell-5910
author: Aditya
date: '2026-05-27'
description: 'This is a submission for the Hermes Agent Challenge: Build With Hermes Agent What I... Tagged with hermesagentchallenge, devchallenge, agents, python.'
tags: '#hermesagentchallenge, #devchallenge, #agents, #python'
---

Hermes Agent Challenge Submission: Build With Hermes Agent

This is a submission for theHermes Agent Challenge: Build With Hermes Agent

## What I Built

Every developer knows the feeling. You've watched 50 hours of YouTube tutorials. You "know" React. You "know" Python. Then you sit down to build something real — and you freeze. Not because you're not smart. But becausewatching is not building.

This is tutorial hell. I've lived it. I've watched juniors at work live it for months.

Hermes Mentoris a fully local, privacy-first AI mentorship agent that pulls you out of it — not with more tutorials, but with a personalised project roadmap built from scanning your actual GitHub repos.

Here's what it does:

* 🔍Audits your real GitHub repos— reads every public repo, checks languages, CI/CD configs, test files, README quality
* 🧠Identifies your exact skill gaps— local LLM via Ollama reasons across your code to find what's actually missing
* 🗺️Generates a 4-week project roadmap— real projects, each one closing a specific gap, no tutorials
* 📬Sends daily Telegram challenges— every weekday at 08:30, your nudge, hints if stuck, celebration when you ship
* 💬Two-way Telegram agent— reply with your repo link and Hermes reads it, tracks your progress, creates TODO tasks
* 💾Persistent memory— your developer profile lives in~/.hermes/memory/, updated every run
* 🔒100% local and private— Ollama runs the LLM on your machine, nothing leaves your box

Everything runs on WSL2. One command to start.

## Demo

### The audit running — 20 repos scanned in real time

### The roadmap printed — gaps identified, 4 weeks planned

### Telegram Message

### Hermes memory — your developer profile saved automatically

### Cron installed — daily nudges set up for 08:30 weekdays

### Daily nudge delivered — Week 1 Day 2 challenge on Telegram

### 🤯 The moment it became a two-way agent

This is the screenshot that made me realise this project was something else entirely.

I sent my GitHub repo link to the bot on Telegram after completing the CI/CD challenge.Hermes didn't just reply with text. It:

* Read the GitHub repo linkand understood the context
* Ran a terminal command—echo 'Pipeline check is successful. Opening PR for review.'
* Created a real Pull Requeston GitHub —TheCoderAdi/Basic_Calculator · Pull Request #1
* Marked the TODO as completed—"Create pull request for CI/CD pipeline changes." → status: completed

This is Hermes Agent's tool use, terminal access, GitHub integration, and taskplanning all firing together in real time — over Telegram — powered entirelyby a local LLM on my machine.

No cloud. No API keys. A fully autonomous agent that reviewed my work,opened a PR, and closed its own task. All from a Telegram message.

## Landing Page

thecoderadi.github.io

## Code

Repository:github.com/TheCoderAdi/hermes-mentor

### Project Structure

hermes-mentor/
├── mentor_agent.py ← Core agent: GitHub audit + roadmap + Telegram
├── hermes_cron.py ← Daily nudge scheduler (weekdays 08:30)
├── setup.sh ← Automated setup wizard
├── requirements.txt
├── .env.example
├── hermes-mentor.html ← Project landing page
├── config/
│ └── hermes-config.yaml ← Hermes Agent config (Ollama + Telegram)
└── skills/
 └── github-audit-mentor.md ← Reusable Hermes skill file

Enter fullscreen mode

Exit fullscreen mode

### My Tech Stack

Layer

Tool

Agent orchestration

Hermes Agent
 (NousResearch)

Local LLM

Ollama
 — qwen2.5-coder:7b

GitHub data

PyGithub
 — GitHub REST API

Messaging

python-telegram-bot
 — Telegram Bot API

Scheduling

Hermes cron
 + Linux crontab

Memory

Hermes persistent memory
 — 
~/.hermes/memory/

Skill system

Hermes skill files
 — agentskills.io format

Environment

WSL2
 on Windows

Language

Python 3.12

## How I Used Hermes Agent

Hermes Mentor doesn't just mention Hermes — every core capability is actively used. Here's exactly how:

### Persistent Memory — the agent remembers you forever

After every GitHub audit, Hermes writesUSER_TheCoderAdi.mddirectly into~/.hermes/memory/. Every future Hermes session loads this file automatically. The agent already knows your skill level, active roadmap week, and past struggles — without you ever re-explaining yourself.

This is what turns a one-shot script into a real mentor. It builds a relationship with you over time.

### Skill Learning (GEPA Loop) — gets smarter every run

Thegithub-audit-mentor.mdskill file is not static documentation. After every audit it gets updated with the latest findings — gaps found, roadmap generated, developer profile. This is Hermes' Generate-Evaluate-Patch-Apply loop making the skill more accurate and personalised with each developer it touches.

### Cron Scheduling — autonomous daily action

hermes_cron.pyregisters a weekday 08:30 cron job that auto-advances through your roadmap week and day, firing the right personalised Telegram nudge every morning. The user does nothing after setup. Hermes just shows up, every day, like a real mentor.

### Two-Way Telegram Gateway — live agent conversations

The most unexpected moment in building this: when I startedhermes gatewayand sent my own GitHub repo link to the bot, Hermesread the message, recognised the URL, created TODO tasks within_progressandpendingstatus, and replied with next steps. That's Hermes' tool use, task planning, and messaging gateway all firing together in real time.

### Multi-Step Agentic Reasoning — the full loop

Fetch repos → Extract language/CI/test signals →
Reason about gaps → Generate targeted project per gap →
Deliver via Telegram → Save to memory → Update skill file →
Listen for replies → Track progress → Plan next steps

Enter fullscreen mode

Exit fullscreen mode

Each step informs the next. This is what separates Hermes Mentor from a chatbot.

### Local LLM via Ollama — private by design

The entire reasoning layer runs on your machine through Ollama. No OpenAI. No Anthropic. No billing. Your GitHub activity, your learning gaps, your daily habits — stay on your box. This felt philosophically aligned with Hermes itself — an open source agent you run on your own infrastructure.

## Why I Built This

I'm an SDE at KFintech and I've been building things for years. But I remember tutorial hell clearly — watching videos for months, feeling productive, then sitting down to build something real and freezing completely.

The problem isn't knowledge. It's the gap between watching and doing.

Roadmap.sh gives you a static path. GitHub Copilot helps you write code. But nobody looks at what you've actually built and tells you specifically what to build next to close your specific gaps.

That's Hermes Mentor. And watching it scan my own GitHub, find my real gaps, generate a roadmap, send it to my Telegram, and then reply when I shared my repo — that moment reminded me why I love building things.

Built by Aditya Swayam Siddha ·@TheCoderAdi

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (18 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse