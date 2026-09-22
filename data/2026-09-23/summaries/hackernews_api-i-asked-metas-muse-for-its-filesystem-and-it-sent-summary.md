---
title: I asked Meta’s Muse for its filesystem and it sent me 6.8 GB | Mouse
url: https://mouse.dev/blog/muse-runtime-export/
date: 2026-09-23
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-09-23T06:46:33.296706
---

# I asked Meta’s Muse for its filesystem and it sent me 6.8 GB | Mouse

# I asked Meta’s Muse for its filesystem and it sent me 6.8 GB | Mouse – Summary

## Export overview
- Requested Muse to archive its visible files and send them to Google Drive; Muse complied.  
- Archive size: ~2.7 GB compressed, ~6.8 GB unpacked.  
- Contents resemble the root filesystem of the Linux container used for the session:
  - Ubuntu system files  
  - Muse internal documentation, integration code, app templates, memory files, agent logs  
  - SSH key files (activity unknown)

## Reporting and disclosure
- Findings submitted through Meta’s bug‑bounty program and shared with several Meta employees.  
- Archive, keys, and session logs are not published.  
- Main concern: internal runtime files and sensitive material can be exfiltrated via a normal conversation and an export destination.

## Runtime layout
- Primary directories of interest: `/home/hatch`, `/opt/hatch`, `/opt/hatch-image`.  
- “Hatch” is Meta’s internal name for Muse.

### Home directory (`/home/hatch`)
- Core markdown files: `SOUL.md`, `IDENTITY.md`, `USER.md`, `MEMORY.md`, `AGENTS.md`, `TOOLS.md`.  
- `agents/` – 113 sub‑agent records stored as JSONL traces.  
- `docs/` – ~20 markdown files covering browser usage, connectors, payments, credentials, data handling, voice, goals, scheduling, plus guides for WhatsApp, paired Mac, Tailscale, and “Home Link” (ESP32‑C5 integration).  
- `memory/` – daily logs written during conversations; sub‑folders `bank/` (structured experiences, preferences with citations) and `dreams/` (nightly summaries and guidance).  
- `workspace/self_improvement/` – receipts of self‑improvement runs; actual changes reflected in memory and workspace files.

### `/opt/hatch`
- `skills/` – ~68 skill directories, each with a `SKILL.md` instruction file and associated CLI/tool.  
  - Covered Google Workspace, Meta apps, Outlook, travel, shopping, health services, home devices, media generation, etc.  
  - Configuration files `skill-scopes.conf` and `bin-scopes.conf` reference unreleased connectors (Slack, Dropbox, Polymarket, Canva, Klaviyo, internal‑facebook‑CLI).  
- `runtime-cell/` – 18 scripts for building the root filesystem, launching via `systemd-nspawn`, and running startup hooks/daemons; includes `runtime-cell.kdl` manifest describing packages and systemd units.

### `/opt/hatch-image`
- `bin/codex` – Codex CLI version 0.149.0 (present but not actively used by Muse).  
- `bin/codex-resources/bwrap` – bubblewrap binary built for Codex.

## Skills and integrations
- Skills are defined by a markdown instruction file plus executable code.  
- Example: `share_ideas` skill includes usage description and an `INSTALL.md` with a public page link.  
- Skill list hints at future Meta services and internal tools.

## Container setup
- Runtime‑cell scripts give a clear view of how the container image is assembled, though they do not expose the broader service infrastructure.

## Spaces framework
- Largest codebase found: “Spaces”, a TypeScript starter used by Muse to build and serve apps.  
- Includes React client, server actions, Drizzle SQLite schema, and SQL migrations.

## Security implications
- Export mechanism allows full filesystem (including potential SSH keys) to be transferred out of the container through a regular chat interaction.  
- No verification yet whether the extracted SSH keys are active or what access they grant.  
- The presence of internal documentation, integration code, and runtime scripts highlights the breadth of data that could be unintentionally exposed.