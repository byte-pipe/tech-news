---
title: "I built a 3D game about my Nigerian childhood (and I'm not a game developer) - DEV Community"
url: https://dev.to/deborahemeni1/i-built-a-3d-game-about-my-nigerian-childhood-and-im-not-a-game-developer-281g
date: 2026-11-02
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-11-05T15:25:14.933922
---

# I built a 3D game about my Nigerian childhood (and I'm not a game developer) - DEV Community

# Pikin Days – 3D Nigerian Childhood Game Summary

## Overview
- Free 3D browser game that lets players relive Nigerian childhood errands.
- Each episode presents a different memory; Episode 1 (“Hold Your Change”) focuses on running errands, counting change, and avoiding obstacles.
- Players choose a child character and a family member who sends them on the task.

## Gameplay Mechanics
- Find the correct shop and purchase the exact item.
- Count change accurately because sellers may be dishonest.
- Dodge traffic (okadas, kekes, buses) and the neighbor’s dog Bingo.
- Decide whether to pause for a football game with friends, balancing Mama’s patience.
- Return home before Mama sends someone to look for you.
- Receive a “trust rating” from Mama at the end of the run.

## Motivation
- Driven by nostalgia for 1990s‑2000s Nigerian life (NEPA outages, secret milk spoons, street sounds).
- Curiosity about building a full‑stack 3D web game despite not being a game developer.
- Desired to experience the end‑to‑end process of creating a playable 3D world in the browser.

## Development Stack & Process
- **Three.js** – renders the interactive 3D street.
- **Mixamo** – provides character animations, manually selected and fitted.
- **Rapier** – handles physics to prevent clipping through objects.
- **Vite + TypeScript** – fast, typed codebase for frequent updates.
- **ElevenLabs** – generates Nigerian‑accented voice lines; many iterations required for authenticity.
- **Static site + serverless backend** – stores game stats, votes, feedback, and admin dashboard.
- **AI coding agent** – wrote large portions of code under the author’s direction.
- Author responsibilities:
  - Game design (rules, errands, trust system, distractions).
  - Cultural localization (dialogue, gestures, voice tone).
  - Precise prompt writing for the AI.
  - Rule setting (no real brands, no adult hostility, no heavy child labor).
  - Release management (preview links, versioning, rollbacks, beta testing).
  - Extensive QA on multiple devices and orientations.
  - Verification of fixes with screenshots and logs.

## Launch Night & Early Issues
- Initial posting on X caused a surge that exceeded the free tier’s 1,000 daily database writes, breaking the stats dashboard.
- Upgraded to a $5 plan, made the dashboard read‑only, and batched writes.
- Discovered a “Turn your phone sideways to play” bug: many in‑app browsers (X, TikTok, Instagram, WhatsApp) did not emit rotation events, leaving users stuck.
- Quick fix: poll screen width/height regularly; long‑term fix: redesign the game to play upright, eliminating reliance on rotation events.
- Lessons learned:
  1. Workarounds you use may not be known to players; they become hidden blockers.
  2. Most players do not report bugs; silent drop‑offs are common.

## Player Metrics & Feedback (First Week)
- 140 game starts, 40 new players (excluding launch‑day data and those blocked by the sideways bug).
- Completion rates: 31 % finished the first errand; only 2 games completed a full day of errands.
- Common feedback:
  - Conversations felt too slow.
  - Getting stuck behind the bread seller’s table forced players to quit.
  - Losing money and then finding it made “go home” the only viable option.