---
title: Zed is 1.0 — Zed's Blog
url: https://zed.dev/blog/zed-1-0
site_name: hackernews_api
content_file: hackernews_api-zed-is-10-zeds-blog
fetched_at: '2026-04-29T20:09:24.214242'
original_url: https://zed.dev/blog/zed-1-0
author: salkahfi
date: '2026-04-29'
published_date: 04/29/2026
description: 'From the Zed Blog: The editor we set out to build is now 1.0.'
tags:
- hackernews
- trending
---

# Zed is 1.0

# Zed is 1.0

Nathan Sobo

April 29th, 2026

To create a fundamentally better editor, we had to invent a new approach to building desktop software. Our previous editor,Atom, was built as a fork of Chromium, spawning the Electron framework in the process. Electron eventually became the foundation of VS Code (which today seems to be forked into a new AI code editor every other week). Web technology offered an easy path to shipping flexible software, but it also imposed a ceiling. No matter how hard we worked, we couldn't make Atom better than the platform it was built on.

So we started over. Instead of building Zed like a web page, we built itlike a video game, organizing the entire application around feeding data to shaders running on the GPU. That meant writing our own UI framework,GPUI, from scratch in Rust.

Owning every layer of our stack lets us take Zed places that no one building on borrowed foundations can go, but we knew from the beginning that it wasn't going to be an easy path. Thanks to years of hard work by our team and community, Zed is closer than ever to that ideal tool we set out to create. We've added a ton of capabilities while remaining true to our core ethos of craft and performance, and hundreds of thousands of developers now rely on Zed to ship software each day. That's part of what gives us the confidence to declare version 1.0.

Zed is 1.0

## What 1.0 Means

Developers expect a modern editor to support dozens of languages and their ecosystems, endless variations and edge cases across every stack:Git integration,SSH remoting, aDebugger, and, yes,rainbow brackets. We've spent five years building that surface area across Mac,Windows, andLinux, exceeding a million lines of code.

Zed is also an AI-native editor. You can runmultiple agents in parallel, andedit predictionssuggest your next change at keystroke granularity and with the speed you've come to expect from Zed. TheAgent Client Protocolopens Zed up to a growing number of the best agents out there, including Claude Agent, Codex, OpenCode, and more recently Cursor. We built AI into our editor's foundation instead of bolting it on top.

We're also launching Zed for Business. Companies have been asking us for a way to roll out Zed to their engineering teams, and very soon they can, with centralized billing, role-based access controls, and team management.

1.0 doesn't mean "done". It also doesn't mean "perfect". It means we've reached a tipping point where most developers can quickly feel at home in Zed. If you tried Zed a year or two ago and bounced because something was missing, 1.0 is our invitation to try again. Zed is more capable than it's ever been, and still more performant.

## Where We're Going

Our vision hasn't changed since we started: we're building the most performant and collaborative coding environment. What's changed is what collaboration means while creating software. It used to mean humans working together in real time. Now it means humans and AI agents, working in the same space, on the same code.

Building our own foundations is what got us to 1.0, and it's also what makes the next chapter possible. We're actively developingDeltaDB, a synchronization engine built onCRDTsthat tracks every change with character-level granularity. DeltaDB lets multiple humans and agents share a single, consistent view of the codebase as it evolves. DeltaDB will allow you to invite teammates into conversations with agents to review and evolve agentic code directly in the context from which it's generated.

This vision depends on deep ownership of our fundamental primitives. It's not an experience we'd be able to ship inside of someone else's browser engine.

## A Milestone, Not a Finish Line

Zed v0.13

We've shipped over a thousand versions of Zed, but all of them began with zero. Today, that changes.

We'll keep shipping every week, the way we always have. The list of things to build will never end, and that's exactly how we like it. Each release moves the craft forward.

If you want to try Zed,download now. If you want to help us build it,join us!

### Related Posts

Check out similar blogs from the Zed team.

## The Case for Software Craftsmanship in the Era of Vibes

|
Agentic Engineering
|

Jun 12, 2025

## Building a platform that open sources itself

Jun 14, 2023

## Sequoia Backs Zed's Vision for Collaborative Coding

|
Featured
|

Aug 20, 2025

### Looking for a better editor?

You can try Zed today on macOS, Windows, or Linux.Download now!

### We are hiring!

If you're passionate about the topics we cover on our blog, please considerjoining our teamto help us ship the future of software development.