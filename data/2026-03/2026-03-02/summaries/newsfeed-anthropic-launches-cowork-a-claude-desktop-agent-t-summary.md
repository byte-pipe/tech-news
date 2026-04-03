---
title: Anthropic launches Cowork, a Claude Desktop agent that works in your files — no coding required | VentureBeat
url: https://venturebeat.com/technology/anthropic-launches-cowork-a-claude-desktop-agent-that-works-in-your-files-no
date: 2026-01-12
site: newsfeed
model: gpt-oss:120b-cloud
summarized_at: 2026-03-02T08:25:59.524284
---

# Anthropic launches Cowork, a Claude Desktop agent that works in your files — no coding required | VentureBeat

# Anthropic launches Cowork, a Claude Desktop agent that works in your files — no coding required

## Overview
- Cowork is a new AI agent that extends Claude Code’s capabilities to non‑technical users.
- Released as a research preview for Claude Max subscribers (US $100–$200/month) via a macOS desktop app.
- Positions Anthropic against OpenAI, Google, and Microsoft’s Copilot in the AI‑productivity market.

## Origin and Inspiration
- Claude Code, a terminal‑based tool for developers, was adopted by users for many non‑coding tasks (e.g., vacation research, slide decks, email cleanup).
- Observing this “shadow usage,” Anthropic stripped away command‑line complexity to create a consumer‑friendly interface called Cowork.

## Folder‑Based Architecture
- Users grant Claude access to a specific local folder, creating a sandbox where the AI can read, edit, or create files.
- Example tasks: reorganizing downloads, generating expense spreadsheets from receipt images, drafting reports from scattered notes.
- Operates via an “agentic loop”: plan → execute steps in parallel → self‑check → ask for clarification when needed.
- Built on the Claude Agent SDK, sharing the same core as Claude Code.

## Rapid Development and Recursive AI Building
- The Cowork feature was built in roughly a week and a half, largely using Claude Code itself.
- Internal comments suggest Claude Code may have written much of Cowork’s code, illustrating a recursive improvement loop where AI helps create its own successors.

## Connectors, Browser Automation, and Skills
- Integrates with Anthropic’s existing connectors (e.g., Asana, Notion, PayPal) for data access beyond the local file system.
- Works with Claude’s Chrome extension to perform web navigation, form filling, and data extraction.
- Introduces “skills” tailored for Cowork to enhance document and presentation creation, extending the Skills for Claude framework.

## Safety and Risk Disclosure
- Anthropic warns that Claude can perform destructive actions, such as deleting local files, if instructed or misinterpreted.
- Users are advised to give clear guidance for sensitive operations and to monitor the agent’s actions.
- The announcement includes explicit safety features: built‑in VM isolation, clarification prompts, and out‑of‑the‑box browser automation safeguards.