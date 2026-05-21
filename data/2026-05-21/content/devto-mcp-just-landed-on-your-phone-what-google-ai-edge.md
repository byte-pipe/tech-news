---
title: 'MCP Just Landed on Your Phone: What Google AI Edge Gallery Actually Does - DEV Community'
url: https://dev.to/dannwaneri/mcp-just-landed-on-your-phone-what-google-ai-edge-gallery-actually-does-1567
site_name: devto
content_file: devto-mcp-just-landed-on-your-phone-what-google-ai-edge
fetched_at: '2026-05-21T12:05:49.207268'
original_url: https://dev.to/dannwaneri/mcp-just-landed-on-your-phone-what-google-ai-edge-gallery-actually-does-1567
author: Daniel Nwaneri
date: '2026-05-20'
description: This is a submission for the Google I/O Writing Challenge I was already running MCP servers on my... Tagged with googleiochallenge, gemma, mcp, devchallenge.
tags: '#googleiochallenge, #gemma, #mcp, #devchallenge'
---

Google I/O Challenge submission

This is a submission for theGoogle I/O Writing Challenge

I was already running MCP servers on my desktop — connected to Claude, wired into my daily workflow — when Google announced at I/O 2026 that AI Edge Gallery now supports MCP connections on Android. I pulled out my Pixel and started testing.

First attempt: "No eligible devices." The app requires capable hardware. Second device — it opened.

What I found is more interesting than the announcement.

## What Google AI Edge Gallery Is

Google AI Edge Gallery is an open-source Android app from Google Research. Large language models run entirely on your device — no internet required for inference, no data leaves your phone. Every prompt, every image, every audio clip stays local.

That part isn't new. What changed at I/O 2026: the app now supports agents. Not a chat interface with a web search button — a proper agent runtime with toggleable skills, calendar integration, scheduled reminders, and experimental MCP connections. The same protocol the rest of the serious agent ecosystem runs on.

## The Model List Surprised Me

Opening the Models panel, I expected a Gemma showcase. That's not what this is.

Model

Size

Notes

Gemma-4-E2B-it

2.6 GB

Recommended across most use cases, 32K context

Gemma-4-E4B-it

3.7 GB

Multi-modal, 32K context

Gemma-3n-E2B-it

3.7 GB

Text, vision, audio, 4096 context

Gemma-3n-E4B-it

4.9 GB

Text, vision, audio, 4096 context

Gemma3-1B-IT

584 MB

4-bit quantized

Qwen2.5-1.5B-Instruct

1.6 GB

Alibaba's model, LiteRT-LM ready

DeepSeek-R1-Distill-Qwen-1.5B

1.8 GB

Reasoning model, fully on-device

TinyGarden-270M

289 MB

Fine-tuned FunctionGemma, task automation

MobileActions-270M

289 MB

Fine-tuned FunctionGemma, device control

DeepSeek and Qwen sitting in a Google app isn't accidental. The actual product here isLiteRT-LM— Google's mobile inference runtime — not Gemma. Which model you run on top is your choice.

## Gemma 4: The Number That Matters

Gemma 4 E2B runs in 2.6 GB and opens a32K context window. Gemma 3n had 4096 tokens. Multi-modal input — text, images, and audio — in one model.

That context gap is what makes the agent use case real. Tool call outputs, calendar data, conversation history — there's room to feed all of it back to the model without truncating. Running a 32K context window offline on a phone wasn't viable when the best on-device options topped out under 2K.

All models run through LiteRT-LM — previously TensorFlow Lite, now meaningfully upgraded.

## Agent Skills: What It Actually Looks Like

This is the part I came to test. Here's what's actually inside.

### The Skills Architecture

Agent Skills runs on 12 skills total — split into two tiers:

Built-in skills(Google's own):

* calculate-hash— hash a given text
* create-calendar-event— write to OS calendar
* interactive-map— show a map view for a location

Community skills(user-created, same interface):

* read-calendar-events— read OS calendar for a specific date
* schedule-notification— schedule a one-time or repeating daily notification
* query-wikipedia— pull a Wikipedia summary on a topic
* qr-code— generate a QR code for a URL
* mood-tracker— stores daily mood and comments, tracks history
* send-email— send an email
* learn-something-new— daily learning companion with image card and scheduled notification
* kitchen-adventure— dungeon master RPG set in a world of sentient kitchen appliances
* text-spinner— "Spin the given text on my head"

Two things worth noticing. First: calendar read and calendar write areseparate skillswith separate toggles. That's a granular permissions model — the agent can write events without having read access, or vice versa. Second:send-emailmeans an offline on-device model can send emails through a skill. That's not a demo capability.

Every skill has a "View" button — inspect the full skill definition before enabling it. Each is individually toggleable. The chat bar shows a live count:Skills 8 | MCP 0. Skills and MCP are tracked separately in the same toolbar.

Four ways to add skills:

1. Featured list — curated community contributions
2. Load from URL — any web-hosted skill directory
3. Import local skill — from the device directly, no server needed
4. GitHub Discussions — browse the full community

Local import is the developer detail. You can build and test a skill entirely on-device without hosting anything. The iteration loop for custom skill development doesn't require a deployed server.

Agent Skills only accepts two models — both Gemma 4. Gemma 3, DeepSeek, Qwen: available for AI Chat, locked out of agents. Google drew a capability line and stuck to it.

### The MCP Setup

Tap the MCP counter in the toolbar → empty state with a single button:+ Add MCP server.

The dialog asks for:

1. Your MCP server URL
2. Authorization:None,Request header, orOAuth (WIP)

OAuth isn't ready yet. That's the honest limitation for anyone planning to connect enterprise or authenticated MCP servers — you're working with no auth or bearer token only, for now. Public MCP servers work today. Authenticated production servers will have to wait for OAuth to ship.

Worth noting what this architecture means even without OAuth: tool-selection logic runs on-device, and only the structured API call leaves the phone. For healthcare or legal tooling that can't send raw queries to a server, that's a meaningful trust boundary — not a workaround.

For developers already running public MCP servers: enter the URL, the app fetches the tool manifest, tool definitions load into the system prompt alongside your active skills. The model handles invocation from there.

## The Rest of the App

Each use case — AI Chat, Ask Image, Audio Scribe, Prompt Lab — links directly to API documentation and example code from its own screen. This is a teaching environment, not just a demo. Google built it for developers to read, fork, and build on.

AI Chatsupports Thinking Mode — Gemma 4's step-by-step reasoning exposed inline. Useful before you wire a model into anything production-facing.

Mobile Actionsruns on MobileActions-270M — 289 MB, fully offline. A 270M parameter model doing device automation. For context, Gemma 4 E2B is roughly 10x that size and handles general reasoning. The argument being made with that design: narrow fine-tunes at sub-300MB can do discrete tasks better than a general model, and they fit anywhere.

Tiny Garden— 289 MB, natural language gardening game — is the same point made playfully. Watch how function-calling works on-device in a consequence-free environment.

## Getting Started

1. Install Google AI Edge Gallery (Play Store)
 Requires capable Android hardware — tested on Pixel

2. Download Gemma-4-E2B-it (2.6 GB)
 Only Gemma 4 models run Agent Skills

3. Open Agent Skills → tap the Skills or MCP button in the toolbar

4. For built-in skills: toggle on what you need
 For MCP: tap MCP → Add MCP server → enter URL + auth

5. Start chatting — the model sees your active skills and connected tools

Enter fullscreen mode

Exit fullscreen mode

Source code:github.com/google-ai-edge/gallery. Community skills shareable via GitHub Discussions.

## What Developers Should Take From This

The Gemma 4-only lock on Agent Skills is the tell. This isn't a checkbox feature. Google shipped agentic tool use where the model can handle it reliably, and locked out weaker models until that changes. That's a better decision than letting anything run and degrading silently.

The OAuth (WIP) flag on MCP auth is the other honest signal. Public MCP servers work today. Enterprise-grade authenticated connections aren't there yet. That's not a failure — it's a preview of where this is going, with the current edges visible rather than hidden.

The 270M fine-tuned models are the underrated part of this release. MobileActions and TinyGarden are evidence of a different architecture: specialized micro-models for narrow tasks, general models for reasoning, LiteRT-LM as the runtime connecting them. At 289 MB each, those models fit anywhere.

MCP being here matters because it's the same protocol across Claude, Cursor, VS Code extensions, and now Google's on-device runtime. Build a tool as an MCP server once and every compatible client picks it up. That's not small.

## Verdict

AI Edge Gallery is the most developer-forward release from Google I/O 2026. Not a consumer product — a reference implementation of what on-device agents look like when an open protocol, a capable model family, and a mobile inference runtime land in the same place.

If you're building with MCP today, install the app and point it at your existing server. Your tools already work. That's not a coincidence — it's what a protocol looks like when it actually wins.

Written with assistance from Claude (Anthropic). Hands-on testing on Pixel: model list, Agent Skills interface, MCP setup flow, and skills management observed directly. Gemma-4-E2B-it downloaded; model inference and chat results not included in this article.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse