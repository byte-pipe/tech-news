---
title: I Built a Better Codex Pet Than OpenAI Did - DEV Community
url: https://dev.to/mikachu/i-built-a-better-codex-pet-than-openai-did-eib
date: 2026-09-26
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-09-27T06:01:15.729953
---

# I Built a Better Codex Pet Than OpenAI Did - DEV Community

# Summary of “I Built a Better Codex Pet Than OpenAI Did”

## Introduction
- The author compares OpenAI’s Codex Pets (released May 2026) with a personal Linux‑only desktop companion called **Mochi**.  
- Codex Pets are a lightweight overlay for Windows/macOS that shows the status of a Codex coding agent.  
- Mochi is an open‑source, Linux‑only alpha that aims to be a persistent, context‑aware desktop mascot rather than a simple status indicator.

## What Codex Pets Actually Are
- Tied to the state of a single Codex agent thread; they display a sprite that reacts to the agent’s current activity (thinking, completed task, etc.).  
- Custom pets are created by dropping a manifest file and spritesheet into a folder; no persistent internal state beyond the current agent status.  
- Designed as a “glanceable” status light: cute, easy to understand, and quick for the community to remix.  
- No memory between sessions and no behavior independent of the Codex agent.

## What Mochi Is Instead
- Independent desktop companion that lives on the screen regardless of which application is active.  
- Built around a single authoritative **behavior‑state machine** that mediates dozens of inputs (clicks, drags, typing detection, media playback, app awareness, etc.).  
- Key subsystems:
  - **AmbiSense** – local, rule‑based ambient awareness that converts desktop activity into privacy‑safe semantic signals.  
  - **Bond progression** – non‑punitive relationship system; XP accrues from typing time and feeding, unlocking new emotes without decay.  
  - **Focus sessions** – Pomodoro‑style timer that continues running even when visual elements are interrupted.  
  - **Emote catalogue** – unlockable emotes with rarity tiers tied to bond level.  
  - **GNOME Shell helper** – uses D‑Bus to obtain coarse semantic signals about typing, idle state, app category, video focus, etc.  
- Architecture separates “truth” (actual context, progression, focus) from “presentation” (animation, movement, expression).

## Architectural Differences
- **Scope**: Codex Pets are a thin feature for a specific coding agent; Mochi is a full‑featured mascot with its own lifecycle.  
- **State management**: Codex Pets have no persistent state; Mochi maintains a robust state machine handling ownership, interruptions, and recovery.  
- **Context awareness**: Codex Pets only reflect the Codex agent’s status; Mochi processes ambient desktop signals, user interactions, and internal progression systems.  
- **Complexity**: Adding Mochi‑style architecture to Codex Pets would be overkill for their intended purpose, but it enables richer, autonomous behavior.

## Conclusion
- Codex Pets excel as a quick, cute overlay for a widely used coding agent.  
- Mochi demonstrates what is possible when the mascot itself becomes the product: persistence, context awareness, relationship mechanics, and a resilient state machine.  
- The author prefers maintaining Mochi, emphasizing that it is an open‑source project where anyone can inspect, contribute, or interact with the companion.