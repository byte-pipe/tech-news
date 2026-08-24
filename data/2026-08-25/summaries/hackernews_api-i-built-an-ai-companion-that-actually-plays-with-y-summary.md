---
title: I Built an AI Companion That Actually Plays With You
url: https://pantel.is/projects/ai-gaming-companion/
date: 2026-08-24
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-08-25T06:05:50.501691
---

# I Built an AI Companion That Actually Plays With You

# I Built an AI Companion That Actually Plays With You

## Goal and Motivation
- Create a next‑level gaming companion that feels alive, useful, and fast.
- Address two common issues in existing LLM‑driven NPCs: weak world agency and noticeable latency.
- Desired traits:
  1. **Instant utility** – fight, fetch, loot, follow multi‑step instructions, especially in VR where menu navigation is cumbersome.
  2. **Presence and personality** – endearing, remembers shared experiences, reacts in real time without needing a dialogue menu.
  3. **Local and private** – minimize cloud calls to reduce cost, latency, and privacy concerns; aim for on‑device operation where possible.

## Complex Command Handling
- Varkos can interpret and execute conditional, deferred, and multi‑step plans that persist across game events.
- Examples:
  - **Conditional arrow trigger** – registers a future event, waits for projectile impact, then picks up a potion.
  - **Item search** – queries the actual game world for a requested object, retrieves it, and can continue searching if the first result is incorrect.
  - **Hide‑and‑seek** – maintains a persistent goal with movement, waiting, monitoring, and completion conditions.
  - **Looting and transferring items** – interacts with containers, filters loot, and moves items to the player using grounded references.
  - **Collect all items** – executes a bounded collection plan over real world objects rather than a single “magic” action.

## Combat Integration
- Receives real‑time grounded events, warns the player via a fast reflex path, and controls the companion’s body.
- Plans can include strategic sequences (attack, retreat) and are influenced by the companion’s emotional state.

## Personality Evolution
- Fully customizable; initial traits are authored, later changes are driven by player interactions.
- Personality updates rely on slower, cloud‑based LLM calls separate from real‑time action.
- Demo progression:
  - Starts as a demon‑reincarnated dog, mistrustful and sarcastic.
  - Gradually becomes domesticated, affectionate, and playful, bringing toys and seeking affirmation.
- Trait and emotional homeostasis changes are versioned and reversible.

## “Void Mode” – Companion Outside the Game
- Varkos can exist across multiple games; when a game closes, he enters a dormant “void mode.”
- In void mode he can still interact via voice, reflecting his current personality.
- Enables seamless transition between games (e.g., from Skyrim to Microsoft Flight Simulator) with adaptive reactions.

## Technical Reflections
- Ideal solution: a council of high‑capacity LLMs handling perception, reasoning, and action at high refresh rates—currently too slow and costly.
- Practical approach: hack together using existing game AI systems (behavioral graphs) and lightweight LLM components.
- Reminder that speech‑processing AI has existed since the 1970s (e.g., SmarterChild), suggesting that modern LLM hype overlooks earlier intelligent systems.