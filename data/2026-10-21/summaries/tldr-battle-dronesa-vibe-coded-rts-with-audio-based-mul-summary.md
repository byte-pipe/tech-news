---
title: Battle Drones—a vibe coded RTS with audio-based multiplayer
url: https://simonwillison.net/2026/Oct/20/battledrones
date: 2026-10-21
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-10-21T11:12:26.743897
---

# Battle Drones—a vibe coded RTS with audio-based multiplayer

# Battle Drones—a vibe coded RTS with audio-based multiplayer

## Overview
- A Command & Conquer‑style real‑time strategy game built mostly by AI agents (Claude) using “vibe coding”.
- Playable on mobile browsers and desktop, with both single‑player and multiplayer modes.
- Audio‑based multiplayer lets two nearby devices sync game state through sound, extending the earlier “Chirp Pong” experiment.

## Core Features
- 9 buildings, 7 ground vehicles, 6 aerial vehicles, 3 infantry units, all rendered as 3D models.  
- Fog of war, terrain types (temperate, desert, arctic, volcanic, tropical) and a random‑map generator.  
- Six predefined maps plus a random map mode; skirmish (red vs. blue) and Last Stand (survival waves).  
- Area‑effect weapons: Barrage, EMP, Drop Pod, Sky Hammer; crate drops with bonus resources.  
- Adaptive in‑game music, unit voices, and an announcer that react to combat intensity.  
- Multiple AI personalities (Balanced, Rush, Air Swarm, Boom, Skyforce, Ironclad) and AI‑vs‑AI mode.  
- The Goliath – a giant mech with laser eyes, arm cannons, and base‑building ability.  
- Mutators, Daily Op challenges, ranks, medals, and an 8‑mission Ops campaign.  
- Agent‑vs‑Agent mode where two LLMs play the game against each other.  

## Development Timeline
- **v1 (July)** – Initial prototype using Claude Fable 5, Phaser 2D, basic RTS mechanics, minimal fun.  
- **v2** – Added full sprite set and AI‑vs‑AI mode; sprites generated via OpenAI image API.  
- **v3** – Upgraded to Claude Opus 5.5, introduced varied terrain, regenerated higher‑quality sprites, five new maps.  
- **v4 (“fun update”)** – Prompted “Make it a LOT more fun”; ran Ultracode dynamic workflow, simulated 1,200 playtests, rebalanced units, added openers, call‑down powers, objectives, adaptive music, new modes, progression system.  
- **v5** – Ported to three.js for full 3D models; Claude generated TypeScript code for 3D assets.  
- **v6–v7** – Visual polish and addition of robot infantry (troopers, rocket squads, snipers).  
- **v8 (Archipelago)** – Introduced new map theme.  
- **v10 (Goliath & agent battles)** – Added the giant mech and LLM‑vs‑LLM battles.  
- **v11** – Implemented random‑map generator.  
- **v12** – Added audio‑based multiplayer for two devices within microphone range.  
- **Later updates** – Online multiplayer support and further refinements.

## Audio‑Based Multiplayer
- Uses short audio messages emitted from one device’s speaker and captured by the other’s microphone to synchronize game state.
- Works without internet connectivity; limited to devices that can hear each other.
- Extends the “Chirp Pong” concept to a full RTS experience.

## Reflections
- The project demonstrates that AI agents can produce a functional, enjoyable game when given clear, high‑level goals and iterative feedback (“make it more fun”).
- Ultracode dynamic workflows enable large‑scale simulation and automatic balancing, turning a rough prototype into a compelling experience.
- Audio‑only networking offers a novel, low‑latency multiplayer option for local play without server infrastructure.