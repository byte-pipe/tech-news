---
title: Agents are building their own UIs now. Here's when that's worth doing. - DEV Community
url: https://dev.to/gde/agents-are-building-their-own-uis-now-heres-when-thats-worth-doing-o9d
site_name: devto
content_file: devto-agents-are-building-their-own-uis-now-heres-when-t
fetched_at: '2026-05-01T20:03:46.015692'
original_url: https://dev.to/gde/agents-are-building-their-own-uis-now-heres-when-thats-worth-doing-o9d
author: Sireesha Pulipati
date: '2026-04-29'
description: This is a submission for the Google Cloud NEXT Writing Challenge During the developer keynote at... Tagged with devchallenge, googlecloud, cloudnextchallenge, genui.
tags: '#devchallenge, #googlecloud, #cloudnextchallenge, #genui'
---

Google Cloud NEXT '26 Challenge Submission

This is a submission for theGoogle Cloud NEXT Writing Challenge

During the developer keynote at Google Cloud NEXT '26, Google built an entire multi-agent system live on stage: a marathon planner that simulates routing a race through Las Vegas. The demo wasn’t just about the agents coordinating route planning, logistics, and runner simulation. It was about the interfaces those agents generated on the fly.

The route planning view showed a map with the proposed path, landmarks, and distance markers. The evaluation view displayed score breakdowns with both deterministic criteria (exactly 26.2 miles) and nondeterministic ones (community impact). The simulation view tracked live runner positions, traffic patterns, hydration stations, and Port-A-Potties. Each phase needed a different interface, and the agent built what it needed in real time using A2UI and the GenUI SDK for Flutter.

The keynote also highlighted FinnishIt, an AI-powered Finnish language tutor built with GenUI. Give it a topic and it generates custom flashcard decks specific to that context. Role-play scenarios shift from text exercises to tap-and-drag word puzzles to fill-in-the-blank modules depending on what the AI assesses you need right now.

Every session produces a different interface.

That's the point where I stopped treating A2UI as conference noise and started paying attention.

A2UI is an open standard Google donated to the community at NEXT '26. It lets agents generate UI dynamically at runtime. The GenUI SDK for Flutter is the developer-facing layer that makes it practical to build with. Most coverage either skipped it or described it without asking the more useful question: when does this actually make sense to use?

## Where GenUI earns it

The marathon planner works because the interface IS the orchestration experience. Different workflow phases need different visualizations: route planning requires a map, evaluation needs scoring charts, simulation shows a live timeline.

FinnishIt works the same way for adaptive learning. There's no predetermined layout that serves a user practicing spoken conversational Finnish the same as one drilling grammar for the YKI citizenship test.

The right exercise type, difficulty, and interaction pattern depend on what the AI assesses the user needs right now. Hardcoding any of that produces a worse product.

The dynamic generation isn't a feature on top of the app. It is the app.

The same logic applies to onboarding flows, and this is where I think GenUI has untapped potential.

Most onboarding flows are static decision trees in disguise. You collect preferences on screen one, goals on screen two, then route users down one of two or three predetermined paths. The result feels personalized but is just filtered content behind a fixed interface.

Consider a personal finance app. Someone who opens it saying "I want to stop overspending" has a completely different mental model than someone who says "I want to start investing" or "I have irregular income and need to plan around it." Those aren't just different content buckets. They're different journeys, with different concepts to introduce, different decisions to make up front, and a different definition of what "getting to value" even means.

A GenUI-powered onboarding flow could read what a user brings to that first session and generate the next step as a direct response: not a static screen two, but a computed one.

A personal style app makes the case even more clearly, because here the interaction type itself changes, not just the content.

Someone who opens a style app saying "I have a job interview next week" needs an occasion-specific outfit construction flow: clear goal, tight timeline, specific constraints. Someone who says "I'm trying to figure out my personal style" needs a discovery experience: visual-first, exploratory, maybe swipe-on-images or mood board style. Someone who says "I want to build a capsule wardrobe on a budget" might need a wardrobe audit flow that starts with photographing what they already own.

These are not variations on the same form. They require different interface primitives: camera, swipe cards, visual grids, checklists. GenUI earns it here because you genuinely cannot know which one to show until the user tells you what they're trying to do.

The right interaction depends on the context. The context arrives at runtime.

## A decision filter

Before reaching for GenUI, three questions:

Is the interface the experience, or is it a container for a fixed one?In FinnishIt, the dynamically generated exercise is the product. That's different from a news reader or a task manager, where content arrives through a stable interface. Not every app benefits from a layout that changes each session.

Does the user need to find the same thing in the same place next time?Adaptive learning, personalized onboarding, style discovery: each session is meant to feel different. An e-commerce checkout, a settings screen, a navigation menu: users build trust and speed through repetition. Those interfaces earn nothing from variation.

Is this an exploratory action, or one that requires confident understanding of what's about to happen?Payment confirmation, account deletion, anything irreversible: users need to know exactly what they're looking at. Dynamic layout introduces uncertainty at exactly the wrong moment.

## Where it doesn't fit

The failure cases aren't about regulation or compliance. They're about what users need from an interface to trust it.

A checkout flow that looks different each time isn't personalization. It's friction.

High-frequency task interfaces derive part of their value from the fact that users can operate them without thinking. Email, task management, booking flows: variability works against that entirely.There's also a quieter design system concern. Most product teams ship against a component library: specific tokens, spacing rules, interaction patterns. An agent that approximately matches those patterns is not the same as one that respects the contract. That gap shows up in production in ways that are hard to articulate and easy to notice.

## The open bet

A2UI and GenUI aren't solutions looking for a problem. There's a real category of app where static UI has always been the wrong answer: the kind where the right interaction depends on context that only arrives at runtime.

FinnishIt is an early, polished example of what that looks like when it's done well. Personalized onboarding, adaptive learning, style discovery: same category.

What I'm watching is whether developers build intuition for where this pattern belongs, or whether the next few years surface a wave of apps that introduced variability in exactly the places their users needed stability.

If you've seen agent-generated UI get it right, or quietly get in the way, I'd like to hear about it.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse