---
title: GitHub - marciopuga/cog: Cognitive architecture for Claude Code — persistent memory, self-reflection, and foresight · GitHub
url: https://github.com/marciopuga/cog
date: 2026-03-30
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-03-30T01:03:09.678420
---

# GitHub - marciopuga/cog: Cognitive architecture for Claude Code — persistent memory, self-reflection, and foresight · GitHub

# Cog – Plain‑text Cognitive Architecture for Claude Code

## Overview
- Cog is a set of plain‑text conventions that guide Claude Code to build, organize, and maintain its own persistent memory.
- No server, runtime, or custom application code is required; the filesystem and standard Unix tools (grep, find, git diff) serve as the interface.
- Memory files are markdown, enabling Claude to search, diff, and manipulate them with familiar commands.
- The architecture is transparent: every rule, change, and decision is visible in the git history.

## Quick Start
- Install Claude Code, then clone the repository:  
  `git clone https://github.com/marciopuga/cog && cd cog`
- Open the project in Claude Code and run the `/setup` command.
- `/setup` converses about your life and work, then generates:
  - a domain manifest,
  - memory directories,
  - skill files,
  - a routing table.
- After setup, you can start interacting with Claude directly.

## Permissions
- The repository includes `.claude/settings.json` that pre‑approves needed tools (file read/write, search, git operations).
- Accepting the project‑level permissions once prevents further prompts.
- To review each permission manually, delete `settings.json`; Claude Code will then ask for confirmation on every operation.

## How It Works

### Three‑Tier Memory Structure
```
memory/
├─ hot-memory.md          ← always loaded, <50 lines
├─ personal/              ← warm, loaded when relevant
│  ├─ hot-memory.md
│  ├─ observations.md    ← append‑only event log
│  ├─ action-items.md
│  └─ entities.md
├─ work/acme/             ← domain‑specific (created by /setup)
└─ glacier/               ← cold archive, indexed via glacier/index.md
```
- **Hot**: current priorities, loaded every conversation.  
- **Warm**: domain‑specific files loaded on demand.  
- **Glacier**: archived YAML‑front‑matter files, retrieved when needed.

### Memory Content Examples
- `hot-memory.md` holds a concise overview of identity, watch items, and system notes.
- `personal/observations.md` records raw, timestamped events in an append‑only fashion.
- `work/acme/entities.md` stores compact entity stubs with status and last‑seen metadata.

### Progressive Condensation
- **Condensation**: observations → patterns → hot‑memory, reducing size while increasing actionability.
- **Archival**: older observations move to the glacier; nothing is deleted, only relocated.

### Threads – Zettelkasten Layer
- When a topic appears across multiple observations, Cog creates a **thread** file:
  - *Current State*: up‑to‑date synthesis.
  - *Timeline*: dated raw entries.
  - *Insights*: extracted patterns and learnings.
- Threads are raised automatically (≥3 observations over ≥2 weeks) or via explicit commands (`raise X`, `thread X`).
- Fragments remain in their original files; threads reference them with wiki‑links.

### Tiered Loading (L0 / L1 / L2)
- Each file begins with a one‑line summary comment (`<!-- L0: … -->`).
  - **L0**: decides whether to open the file.
  - **L1**: scans section headers to locate relevant parts.
  - **L2**: reads the full file when deeper context is required.

### Single Source of Truth
- Facts live in a single canonical file; other files contain only pointers (wiki‑links) to avoid duplication.

### Wiki‑Links
- Files cross‑reference each other using `[[domain/filename]]` syntax.
- An auto‑generated link index (via `/housekeeping`) helps discover connections.

### Domain Registry
- Domains categorize life areas (personal, work, side‑project, system).  
- `/setup` creates a `domains.yml` file, which drives directory creation, skill generation, and routing.

## Built‑in Skills (located in `.claude/commands/`)
- `/setup` – conversational domain configuration.  
- `/personal` – manage family, health, calendar, daily life.  
- `/reflect` – mine conversations, extract patterns, condense memory.  
- `/evolve` – audit architecture and propose rule changes.  
- `/foresight` – provide cross‑domain strategic nudges.  
- `/scenario` – simulate decisions with timeline projections.  

These skills read the conventions in `CLAUDE.md`, manipulate the memory files, and keep the knowledge base coherent across sessions.