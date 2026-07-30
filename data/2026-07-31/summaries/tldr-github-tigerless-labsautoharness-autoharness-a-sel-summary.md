---
title: GitHub - tigerless-labs/autoharness: Autoharness — a self-learning skill layer for Claude Code — distills skills from your real sessions, updates them...
url: https://github.com/tigerless-labs/autoharness
date: 2026-07-31
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-07-31T06:01:51.981155
---

# GitHub - tigerless-labs/autoharness: Autoharness — a self-learning skill layer for Claude Code — distills skills from your real sessions, updates them...

# AutoHarness – Self‑Learning Skills for Claude Code

## Overview
- Autoharness adds a self‑maintaining skill layer to Claude Code that learns from real sessions, merges similar skills, updates active ones, and prunes unused ones.  
- Improves performance (42 % → 78 % on CORE‑Bench) by handling the skill‑management slice automatically.  
- Operates entirely in Python with zero third‑party dependencies; it only modifies skills it generated itself.

## Core Features
- **Learning from real work** – each episode is distilled into a skill without a separate data‑collection loop.  
- **Skill consolidation** – the reflector merges same‑scenario skills instead of accumulating near‑duplicates.  
- **Usage‑based validation** – a skill persists only if it is used in later turns; no external benchmark required.  
- **Self‑authored ledger** – every create/update logs its scenario and decision, enabling later benchmark construction.  
- **Isolation** – only autoharness‑generated skills are touched; user‑written or third‑party skills remain unchanged.

## Installation
1. Ensure `python3` is on your PATH.  
2. In Claude Code input box run:  
   ```
   /plugin marketplace add tigerless-labs/autoharness
   /plugin install autoharness@autoharness
   ```  
3. Reload plugins or restart Claude Code.  
   - Autoharness then watches sessions and writes learned skills to `.claude/skills/`.  
   - Cadence and lifecycle thresholds are adjustable via environment variables (see Configuration).

## Updating
```bash
claude plugin marketplace update autoharness
claude plugin update autoharness@autoharness
```
- Restart Claude Code to apply the new version.  
- Enable auto‑update in the marketplace settings to receive future releases automatically.

## Uninstalling
```bash
claude plugin uninstall autoharness@autoharness
claude plugin marketplace remove autoharness
```
- The plugin stops running, but its generated skills and state remain on disk.  
- To delete them, remove `~/.claude/autoharness/...` directories and the self‑authored skill folders under `.claude/skills/`.

## Configuration (environment variables)
| Variable | Default | Purpose |
|---|---|---|
| AUTOHARNESS_REFLECT_EVERY_N | 10 | How often reflection runs (every N host turns). |
| AUTOHARNESS_DIGEST_EXCHANGES | 20 | Number of prior exchanges compressed into the reflector’s digest. |
| AUTOHARNESS_MATURITY_PROJECT | 100 | Requests needed before a project‑level skill is reviewed for graduation. |
| AUTOHARNESS_MATURITY_GLOBAL | 300 | Same as above for the global layer. |
| AUTOHARNESS_CAPACITY_PROJECT | 50 | Max mature skills in a project layer. |
| AUTOHARNESS_CAPACITY_GLOBAL | 20 | Max mature skills in the global layer. |

Set variables in the shell (`export AUTOHARNESS_REFLECT_EVERY_N=3`) or in `.claude/settings.json` under `env`.

## How It Works
| Component | Role |
|---|---|
| CAP (capture) | Hook‑driven pipe that records each turn (user input, agent output, tool I/O) and redirects it to the host log. |
| REF (reflect) | At episode boundaries, receives the full episode window plus a compressed prior digest, compares against the skill index, and proposes add/merge/patch/delete intents (no writes). |
| promoter | Validates intents (safety, structure, ledger) and atomically writes approved skills to the live directory. |
| MNG (lifecycle) | Runs lazily at session start; ranks symbols by usage rate (requests since creation). Handles probation, graduation, archiving, and capacity‑based eviction. No daemon required. |

- Skills are plain native symbols recalled by Claude Code via name‑and‑description, as if authored by a human.  
- Archiving moves unused symbols out of recall; they are never deleted, preserving a full history.