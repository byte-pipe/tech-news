---
title: I Built a Better Codex Pet Than OpenAI Did - DEV Community
url: https://dev.to/mikachu/i-built-a-better-codex-pet-than-openai-did-eib
site_name: devto
content_file: devto-i-built-a-better-codex-pet-than-openai-did-dev-com
fetched_at: '2026-09-27T06:00:28.665159'
original_url: https://dev.to/mikachu/i-built-a-better-codex-pet-than-openai-did-eib
author: Mika Flowers
date: '2026-09-26'
description: Sometimes you just have to let the agent cook. Mika vs. a multi-billion-dollar... Tagged with opensource, python, linux, showdev.
tags: '#showdev, #opensource, #python, #linux'
---

Linux desktop pet vs OpenAI's official release

Sometimes you just have to let the agent cook.

## Mika vs. a multi-billion-dollar corporation, and a stupid little desktop pet.

When OpenAI shipped Codex Pets in May 2026, they wanted to give your coding agent a face. The pets float as an overlay on Windows and macOS, showing real-time status updates about what Codex is doing, and can notify users when a task completes or when the agent needs input. The feature launched with eight built-in pets and a way to generate custom, AI-animated pets from user images.

Before I go further, a caveat: this isn't really a fair fight. Codex Pets is a small feature bolted onto a coding agent used by millions of people, built by a team with the resources to ship across two operating systems on day one. Mochi is a solo, Linux-only alpha. They're not competing for the same thing, and if you're after "which is the more polished, widely-used product," Codex Pets wins that easily. What theydoshare is one idea — a little creature that lives on your screen — and this is a look at what happens when you take that same idea and refuse to stop at "cute status light."

It's a clever idea. It's also, underneath the cute art, kind of nothing. Strip away the sprite and a Codex Pet is a status light with a tail — a red clock when it's waiting on you, a green check when it's done. Cute, sure. Impressive, not really. So I built the version I actually wanted:Mochi, an open-source Linux desktop companion with a real state machine, real memory, and a real reason to exist beyond one app's notification stream.

## What Codex Pets actually are

Functionally, a Codex Pet is tied to one thing: the state of a Codex agent thread. It's a pixel-art animated companion that floats over the desktop while Codex codes, reacting to mouse interaction and Codex status — scratching its head when thinking, popping a speech bubble when a task completes. Custom pets are just a manifest file plus a spritesheet, dropped into a folder. There's no persistent internal state beyond "what is the agent doing right now," no memory between sessions, and no behavior that isn't ultimately a reflection of Codex's own status.

To be fair, that's the correct amount of engineering for the job. A glanceable agent-status widget doesn't need a state machine. It needs to be cute, legible at a glance, and easy for a community to remix. OpenAI nailed that brief. But itisjust a brief, and a narrow one — the pet doesn't outlive the thread it's watching.

## What Mochi is instead

Mochi doesn't report on anything external. It's not a status light for some other tool — it's meant to feel like it lives on your desktop, full stop, independent of whatever app you happen to have open. That's a different, harder problem, and it shows in the architecture.

Under the hood, Mochi runs on a single authoritative behavior-state machine that mediates between dozens of competing systems — clicking, dragging, sleep, typing detection, media playback, contextual app awareness, and more — all of which have to agree on one question at any given moment: what does Mochi currently own, and what's it allowed to do next? That's before you even get to the systems a Codex Pet has no equivalent for at all:

* AmbiSense— a local, rule-based ambient-awareness layer that reduces desktop activity (typing, video playback, file browsing, active app) into privacy-safe semantic signals. Not an LLM, not a cloud service, and built to never see actual keystrokes, file names, or window titles.
* Bond progression— a slow, deliberately non-punitive relationship system. No streaks, no decay, no penalty for missing a day. XP accrues from typing time and feeding, and leveling up triggers its own presentation sequence.
* Focus sessions— a full Pomodoro-style domain model with its own clock that keeps running even when the visual gets interrupted by a drag or a click. What Mochi looks like and what's actually true in the background are deliberately different questions.
* An Emote Cataloguewith bond-gated unlocks and rarity tiers, so what Mochi can do actually grows the longer you've had it.
* A GNOME Shell helperthat taps into real desktop context — typing pulses, idle/active state, app category, video focus — over D-Bus, again reduced to coarse semantic signals rather than raw data.

flowchart TD
 Desktop["Linux Desktop"]
 GNOME["GNOME Shell Helper<br/>D-Bus"]
 Ambi["AmbiSense<br/>Local Rule-Based Context Layer"]

 Desktop --> GNOME
 GNOME -->|"coarse semantic signals"| Ambi

 Ambi --> Typing["Typing Activity"]
 Ambi --> Video["Video / Media Focus"]
 Ambi --> Apps["App Category"]
 Ambi --> Idle["Idle / Active State"]
 Ambi --> Files["File Browsing Activity"]

 User["User"]

 Click["Click"]
 Drag["Drag / Pickup"]
 Feed["Feed"]
 Media["Media Controls"]

 User --> Click
 User --> Drag
 User --> Feed
 User --> Media

 State["Authoritative<br/>Behavior State Machine"]

 Typing --> State
 Video --> State
 Apps --> State
 Idle --> State
 Files --> State

 Click --> State
 Drag --> State
 Media --> State

 Sleep["Sleep System"]
 Context["Contextual App Behavior"]
 Animation["Animation / Emote Playback"]

 Sleep --> State
 Context --> State

 State -->|"Who owns Mochi?"| Animation
 State -->|"What may happen next?"| Sleep
 State -->|"Allowed reactions"| Context

 Bond["Bond Progression<br/>XP · Levels · No Decay"]
 Focus["Focus Sessions<br/>Independent Pomodoro Clock"]
 Catalogue["Emote Catalogue<br/>Rarity + Bond Unlocks"]

 Feed --> Bond
 Typing --> Bond

 Bond --> Catalogue
 Catalogue --> State

 User --> Focus
 Focus --> State

 State -. "visual state may be interrupted" .-> Focus
 Focus -. "session truth keeps running" .-> State

 Presentation["Mochi Presentation Layer<br/>animation · movement · expression"]

 Animation --> Presentation
 Sleep --> Presentation
 Context --> Presentation
 State --> Presentation

Mochi’s architecture separates what is true from what is currently visible. Desktop context, user interaction, progression, focus state, and autonomous behavior all converge on a single behavior-state machine that decides who currently “owns” Mochi and which transitions are legal.

None of that is decoration. Most of Mochi's codebase manual is about lifecycle and ownership: making sure a stale animation callback can't fire after a feature's been interrupted, that a context menu closing visually doesn't leave an invisible input grab behind, that recovery always reevaluates thecurrentlive context instead of blindly replaying whatever was happening before something interrupted it. That's the kind of problem you only run into once a system has enough moving parts to actually collide with itself — which is exactly the problem a Codex Pet is small enough to never have.

## The real difference

Here's the honest version, not just the flex: a Codex Pet issupposedto be thin. It's a feature bolted onto a coding agent, meant to be authored in minutes and understood in one glance. Giving it Mochi's architecture would be overkill for what it's for.

But that's also exactly the point. OpenAI built a mascot for their product. I built a product whose whole job isbeingthe mascot — one with persistence, context-awareness, care mechanics that don't depend on any single app, and a state machine robust enough to survive being dragged around, interrupted, and left alone for a week. Codex Pets are a nice feature riding on the back of a multi-billion-dollar coding agent. Mochi is the thing itself, built by one person who wanted the version that actually commits to the bit.

I know which one I'd rather maintain.

Codex Pets details in this post are drawn from public reporting and documentation, not insider access. Mochi is open-source —browse the code, file an issue, or just come say hi to the little guy.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse