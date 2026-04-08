---
title: 'When Chrome Ate My RAM: Designing a Pressure-Aware Tab Orchestrator with Rust - DEV Community'
url: https://dev.to/tasenikol/when-chrome-ate-my-ram-designing-a-pressure-aware-tab-orchestrator-with-rust-1g05
site_name: devto
content_file: devto-when-chrome-ate-my-ram-designing-a-pressure-aware
fetched_at: '2026-04-08T11:23:53.035672'
original_url: https://dev.to/tasenikol/when-chrome-ate-my-ram-designing-a-pressure-aware-tab-orchestrator-with-rust-1g05
author: Tasos Nikolaou
date: '2026-04-01'
description: Chrome wasn't "crashing." It was just...slowly suffocating my system. Over time, RAM usage would... Tagged with rust, chromeextension, architecture, performance.
tags: '#rust, #chromeextension, #architecture, #performance'
---

Prioritizes system metrics over idle timers

Chrome wasn't "crashing."

It was just...slowly suffocating my system.

Over time, RAM usage would creep up. Background tabs accumulated state. Other applications started freezing. The fan would spin up. And yet, nothing looked obviously wrong. No single tab was the culprit.

The problem wasn'ttoo many tabs.The problem was a lack of coordination between the browser and the system.So I built something to experiment with that idea.

This article explains the architecture and reasoning behind a hybrid Chrome extension & Rust native host that manages tab lifecycle based on real system pressure and user context.

## The Problem: Browser Entropy

Modern browsers are operating systems.

They manage:

* Dozens of isolated processes
* Background timers
* Network activity
* Memory-heavy applications (Jira, GitHub, Gmail, ChatGPT, Claude 😊 etc.)

Most tab suspension tools rely on a simple rule:

"If a tab hasn't been used inXminutes, suspend it."

That's convenient, but blind.

They don't know:

* Whether the system is under memory pressure
* Whether CPU is spiking
* Whether you're on battery
* Whether the tab is part of your active workflow

They operate on time, not state.

What I wanted was:

A deterministic, pressure-aware, context-sensitive lifecycle engine.

Not AI. Not cloud analytics. Just a well-structured system.

## Design Goals

Before writing any code, I defined constraints:

* Deterministic behavior (no black-box magic)
* No cloud, no telemetry
* Respect user intent (never discard active or pinned tabs)
* Pressure-aware decisions
* Context-aware heuristics
* Clean separation of responsibilities

This last one became the most important architectural decision.

## Architecture Overview

The system consists of two components:

Chrome Extension (MV3)
 - Tab activity tracking
 - Focus clustering
 - TTL gating & guardrails
 ↓ Native Messaging
Rust Native Host
 - System metrics (RAM, CPU, Battery)
 - Pressure scoring engine
 - Deterministic classification

Enter fullscreen mode

Exit fullscreen mode

### Why split it?

Chrome extensions cannot access low-level system metrics like real memory pressure in a reliable way.

So I separated concerns:

* Theextensionmanages browser lifecycle.
* TheRust native hostunderstands system state.

They communicate through Chrome's Native Messaging API.

This keeps the system clean:

* Browser logic stays in the browser.
* System logic stays native.

## The Pressure Engine (Rust)

Instead of checking raw RAM percentage, I built a weighted pressure scoring model.

The Rust host collects:

* Total RAM
* Used RAM
* Free RAM
* CPU usage
* Battery state (if available)

From these, it computes:

* pressure_score(0-100)
* pressure_level(LOW / MEDIUM / HIGH)
* pressure_reasons(RAM_HIGH, CPU_ELEVATED, ON_BATTERY, etc.)

RAM is the dominant signal.CPU acts as a modifier.Battery adds a small aggressiveness bias.

The goal is not to be perfect, it's to be consistent and explainable.

Instead of saying:

"System busy."

It says:

HIGH pressure because RAM_HIGH + ON_BATTERY.

That reason tagging matters for transparency.

## Context Awareness - Focus Clustering

Not all inactive tabs are equal. A tab opened 30 minutes ago in your active workflow is very different from a forgotten tab in another window.

So I introducedFocus Mode.

Focus clustering is based on:

* Same hostname as active tab
* Recent activity window
* Same window constraint
* Cluster size cap

Tabs inside the active "cluster" use a longer TTL.Tabs outside the cluster expire faster under pressure. This makes the system:

* Less disruptive
* More aligned with user context
* Less likely to discard something you'll immediately need

It's still deterministic, but just smarter.

## Guardrails & Safety

Aggressive resource management can easily become destructive. So, strict guardrails were built in:

* Never discard active tabs
* Never discard pinned tabs
* Never discard audible tabs
* Respect protected domains
* Enforce TTL minimums
* Apply cooldown between prune cycles

This prevents oscillation and surprise behavior. The goal is not maximum efficiency. The goal is controlled stability.

## Why Rust?

Rust was chosen for the native host because:

* Memory safety
* Explicit modeling
* Strong type system
* Clean modular architecture
* Lightweight binary

The Rust side is structured into modules:

* metrics, system state collection
* battery, optional battery signal
* pressure, scoring logic
* protocol, native messaging transport
* state, API contract

This makes the native host feel like a real subsystem, not a script.

## What It Achieves

In practice, this system:

* Reduces RAM pressure under load
* Keeps active workflows intact
* Makes browser behavior predictable
* Avoids blind "time-based" suspension
* Plays nicer with other system applications

It doesn't eliminate memory usage. It orchestrates it.

## What I Learned

A few things stood out during this project:

### 1. MV3 Service Workers Have Quirks

Extension background scripts are ephemeral. State management must be deliberate.

### 2. Determinism Beats "Smartness"

Clear, explainable rules feel safer than opaque heuristics.

### 3. Separation of Concerns Changes Everything

Keeping system logic in Rust and browser logic in the extension made experimentation much easier.

### 4. Observability Matters

Reason tagging and structured logging made debugging and tuning far easier.

## Future Directions

This project is still evolving. Some experimental directions:

* Event-driven pressure signals (instead of polling)
* Chrome process memory integration
* Predictive return probability modeling
* Offline data analysis of tab lifecycle patterns
* Adaptive TTL tuning

The architecture supports these without becoming tangled.

That was intentional.

## Conclusion

Chrome didn't have a bug. It was just operating without coordination. By introducing a pressure-aware, context-sensitive orchestration layer, the browser becomes less chaotic and more cooperative with the system.

This project started as frustration with RAM usage. It turned into an exploration of how browsers and operating systems can communicate more intelligently, without AI hype, and without cloud dependencies.

Just clean architecture and deterministic policy!

Checkout the project here:Github:https://github.com/tase-nikol/tab-memory-orchestrator

Sometimes the problem isn’t that a system is brokenIt’s that its parts aren’t talking to each other.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse