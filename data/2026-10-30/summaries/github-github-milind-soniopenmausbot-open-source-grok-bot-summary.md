---
title: GitHub - milind-soni/OpenMausBot: Open-source Grok Bot alternative with a virtual machine that bots can use · GitHub
url: https://github.com/milind-soni/OpenMausBot
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-10-30T12:48:20.206975
---

# GitHub - milind-soni/OpenMausBot: Open-source Grok Bot alternative with a virtual machine that bots can use · GitHub

# OpenMausBot – Open‑source Grok Bot Alternative

## Overview
- OpenMausBot (also called MausBot or formerly OpenGrokBot) is an open‑source, local‑first chat application that hosts a roster of AI agents, each with its own personality, model, and compute environment.  
- Inspired by Grok Bot, Meta Muse, OpenAI Dots, and Manus Cue, it lets users bring their own agents (Claude, Codex, Grok, etc.) without relying on third‑party cloud services.  
- The project is independent, not affiliated with xAI, Meta, OpenAI, or Manus, and contains no cryptocurrency token.

## Why It Exists
- **Bring‑your‑own agents** – Bots run on CLIs installed locally, using existing logins and subscriptions; any engine can be pointed to a custom CLI binary via Settings → Engines.  
- **Local‑first architecture** – A small harness server on `127.0.0.1` owns all agent processes; transcripts, keys, and events are stored in `~/.openmausbot`.  
- **Agents with hands** – Each bot can control a cloud Linux desktop, an isolated local VM, or the host computer (macOS and Ubuntu Xorg with explicit opt‑in). Integration with 500+ apps is provided through Composio.

## Comparison with Closed Alternatives
| Closed product | Provider | Key differences |
|---|---|---|
| Grok Bot (xAI) | Single shared cloud computer, Grok‑only | Same roster shape; OpenMausBot supports any model, runs on your machine, uses approval cards |
| Meta Muse | Meta cloud VM, limited to US/Canada | Team of agents instead of one, runs anywhere, data stored locally |
| OpenAI Dots | GPT‑only, requires Pro/Business plan | Multiple agents, supports Claude, Codex, Grok; no subscription needed |
| Manus Cue | Invite‑only, phone/email/wallet per agent | Open source, OAuth login, no invite required |
| Instinct AI (Spear Street) | Invite‑only, cloud‑stored passwords | Approval workflow, OAuth login, runs on your machine |

A decision guide with five questions helps users choose the appropriate AI agent.

## Core Features
- **Model picker per bot** – Switch between Claude, Codex, and other providers mid‑conversation; unavailable providers are dimmed with explanations.  
- **Dedicated computer for each bot** – Cloud desktop preview, “Open desktop” to take control in a browser, or direct the bot to the local Mac.  
- **Permission broker** – Shell commands, file edits, and questions appear as inline Allow/Deny cards; the user decides before any risky action.  
- **One‑click app marketplace** – Composio Sessions provide OAuth integration for Gmail, Slack, GitHub, Notion, Linear, etc.; a single OAuth grants access to all bots.  
- **Chat‑style bot management** – Right‑click actions: pin, mark unread, edit profile, duplicate, copy conversation ID, hide, delete.  
- **Centralized credentials** – Paste keys once in App Settings; they persist locally, are write‑only, and instantly hot‑reload across agents.  
- **Channel organization** – Separate Work, Personal, and project channels; each channel has its own transcript, instructions, folder, responder rules, and bot roster.  
- **Fast decision routing (Jev)** – With a TypeSafe Jev or OpenRouter key, the system auto‑picks the appropriate bot for unmentioned messages in milliseconds.  
- **Team import via Markdown** – Browse outcome‑driven teams on BotMRR and add them with a single review step.

## Release Information
- Latest releases include macOS (Apple silicon & Intel) signed & notarized `.dmg`, Windows x64 installer, and Ubuntu 24.04 x64 (`.deb` or AppImage beta).  
- Powered by boat.dev.

## Repository Highlights
- **Key directories**: `apps/`, `docs/`, `electron/`, `server/`, `shared/`, `src/`, `third_party/`.  
- **Configuration files**: `Dockerfile`, `compose.yaml`, `vite.config.ts`, various `tsconfig*.json`.  
- **Documentation**: `README.md`, `AGENTS.md`, `CLA.md`, `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `SECURITY.md`.  
- **License**: Apache 2.0 (see `LICENSE` and `LICENSING.md`).  

OpenMausBot provides a flexible, privacy‑respecting alternative to commercial AI‑assistant suites, enabling users to assemble and control their own team of agents on their own hardware.