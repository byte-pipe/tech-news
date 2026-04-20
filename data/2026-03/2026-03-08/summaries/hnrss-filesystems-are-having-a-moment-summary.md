---
title: Filesystems are having a moment
url: https://madalitso.me/notes/why-everyone-is-talking-about-filesystems/
date: 2026-03-07
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-03-08T07:26:17.981158
---

# Filesystems are having a moment

# Filesystems are having a moment

## Everyone is talking about files
- Recent AI‑agent discussions (LlamaIndex, LangChain, Oracle, Dan Abramov, Archilis) highlight the resurgence of POSIX‑style filesystems as a core tool for agents.
- Jerry Liu (LlamaIndex) notes a shift from agents with hundreds of tools to agents that mainly need a filesystem, a code interpreter, and web access.
- Karpathy argues that Claude Code succeeds because it runs locally on the user’s machine, using the user’s environment and data, unlike cloud‑centric approaches.
- Commercially, coding agents dominate current AI usage; Anthropic’s profitability is largely driven by Claude Code, a CLI that reads and writes files rather than a chatbot.

## Context windows aren't memory
- Human memory stores long‑term information and retrieves selectively; LLM context windows act like a volatile whiteboard that is constantly erased.
- Filesystems provide a simple persistence layer: write context to files, read it back when needed (e.g., `CLAUDE.md`, Cursor’s searchable chat files, `aboutme.md`).
- A recent ETH Zurich paper found that adding extensive repository‑level context files often *reduces* task success and raises inference cost by >20 %, because agents treat the files as exhaustive checklists.
- The takeaway is not to discard context files but to keep them concise and focused on minimal requirements, highlighting the need for standards around file content.

## The file format is the API (but which file?)
- Multiple ad‑hoc files exist (`CLAUDE.md`, `AGENTS.md`, `copilot‑instructions.md`, `.cursorrules`), with no consensus on naming or structure.
- Dan Abramov’s “social filesystem” concept (AT Protocol) shows that apps can interoperate by namespacing their own file formats, treating user data as files rather than requiring a shared schema.
- Anthropic’s open `SKILL.md` standard is gaining traction; Microsoft, OpenAI, Atlassian, GitHub, and Cursor have adopted it, enabling skills written for one agent to work with others.
- NanoClaw exemplifies a “skills over features” model: adding functionality is done by dropping a markdown skill file (e.g., `add‑telegramskill.md`) into a folder, eliminating the need for plugin marketplaces or centralized MCP servers.
- This file‑based interoperability sidesteps formal standards bodies or dominant platforms—shared file formats become the de‑facto API.

## The bottleneck shifted
- Traditional architectures treated storage as the bottleneck; modern systems decouple compute from storage (e.g., S3 + ephemeral compute).
- In AI agents, the limiting factor is now *context* rather than model capability or raw compute.
- Filesystems, despite their simplicity, offer a scalable way to manage persistent context, addressing the new bottleneck and reshaping how agents are built and deployed.
