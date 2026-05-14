---
title: 'Local-First AI Done Right: How Gemma 4 E2B and ''Thinking Mode'' Powered DiagramFlowAI - DEV Community'
url: https://dev.to/gde/local-first-ai-done-right-how-gemma-4-e2b-and-thinking-mode-powered-diagramflowai-3bop
site_name: devto
content_file: devto-local-first-ai-done-right-how-gemma-4-e2b-and-thin
fetched_at: '2026-05-14T11:37:12.346963'
original_url: https://dev.to/gde/local-first-ai-done-right-how-gemma-4-e2b-and-thinking-mode-powered-diagramflowai-3bop
author: Carlos Barbero
date: '2026-05-13'
description: What I Built DiagramFlowAI is a local-first desktop application (macOS, Windows, and... Tagged with devchallenge, gemmachallenge, gemma.
tags: '#devchallenge, #gemmachallenge, #gemma'
---

Gemma 4 Challenge: Build With Gemma 4 Submission

## What I Built

DiagramFlowAI is a local-first desktop application (macOS, Windows, and Linux) that transforms natural language descriptions into production-ready architecture diagrams. It intelligently generates standard Mermaid syntax for general workflows, or outputs structured commands mapping to official AWS icons for cloud architectures.

The application solves a very specific tension in modern software engineering:privacy versus productivity. When architects and engineers sketch out internal systems—such as authentication flows, proprietary data pipelines, or secure cloud perimeters—sending that data to a cloud-based LLM endpoint is often a compliance deal-breaker.

DiagramFlowAI is designed to be completely self-contained. Powered byflutter_gemmaand LiteRT, it runs 100% locally. After the initial model download, it requires zero internet connection, uses no API keys, and has no telemetry. It’s an AI diagramming studio that respects your company’s security posture.

## Demo

## Code

github.com/carlosrgomes/DiagramFlowAI

## How I Used Gemma 4

Most AI showcases default to the largest model available. I did the exact opposite. I deliberately built DiagramFlowAI aroundGemma 4 E2B and E4B—the edge variants—and intentionally skipped the 31B Dense and 26B MoE models. Here is why the smallest variants were the secret to making this desktop app work, and how Gemma 4's "Thinking Mode" unlocked capabilities I didn't expect.

### The Unfashionable Choice: Small over Large

If you're building a high-throughput backend, the 31B Dense or 26B MoE are obvious choices. However, my deployment constraints pointed in a completely different direction:

* Democratic Hardware Requirements:A 31B dense model in 4-bit quantization demands around 16-20 GB of RAM. The E4B model comfortably fits within 4-6 GB and runs smoothly on integrated GPUs. That’s the difference between an app anyone can use and a toy restricted to high-end workstations.
* Frictionless Onboarding:The moment a user has to paste an API key, onboarding conversion plummets. Because E2B and E4B are open weights, users can simply click "download" and start diagramming. No auth walls, no billing setups.
* Snappy Cold Starts:In a desktop app, the first interaction needs to feel immediate. The E2B model loads and responds in seconds on modern M-series Macs and modern PCs, keeping the user in their flow state.

To give users flexibility, I built in a toggle between E2B (faster) and E4B (more accurate on complex syntax), rather than hardcoding a single option.

### The Underrated Superpower: Thinking Mode

If there is one thing every developer building with Gemma 4 should internalize, it's the power of the reasoning trace. Theflutter_gemmaSDK exposes Gemma 4's internal reasoning as a distinct stream ofThinkingResponsechunks.

For diagram generation, this is a game-changer. Mermaid syntax is notoriously fragile—a stray colon, an unquoted string, or a missingendtag will break the entire render. Without Thinking Mode, a 4B parameter model will often confidently output syntactically broken DSLs in one shot.

With Thinking Mode enabled, the model spends a few hundred tokens planning its structurefirst("OK, this is a sequence diagram, I need actor -> participant -> arrow -> response..."). Consequently, the final output is dramatically more reliable.

In the UI, I expose this trace as a collapsed accordion (e.g., "Thinking · 2.4s"). This subtle UX choice builds user trust and makes the generation wait feel highly productive, without overwhelming them with raw logs.

### Pragmatic Patterns for 4B Models

Fighting with the model for a few weeks led me to a few hard-won architectural patterns:

1. Treat the System Prompt as a Grammar, Not a Personality:Small models pattern-match exceptionally well. My 500-line system prompt isn't about making the AI "helpful"; it's an output contract. I use explicit delimiters (<DIAGRAM>...</DIAGRAM>) and provide "syntax cards" showing the most common parser failures (e.g.,NEVER write X). Teaching the modelwhat not to doprevents entire classes of bugs.
2. Trust the Contract over Regex:Instead of fighting fragile markdown fences with complex Regex, I rely on the XML-style delimiters defined in the system prompt. Even when the model decides to write an explanatory paragraph, the actual code is safely wrapped and easily extracted.
3. Engineer the Recovery Loop:Even with Thinking Mode, complex diagrams might occasionally fail to parse. Instead of trying to prompt-engineer my way to a 100% success rate (which is near impossible at 4B), I built a small ReAct-style retry loop. If the Mermaid parser throws an error, the app feeds the exact error message back into a follow-up turn. The model almost always fixes its syntax on the second attempt.

Gemma 4 E2B and E4B prove that you don't need a massive, cloud-hosted LLM to ship a genuinely useful, structured AI application. If you map your deployment constraints, lean hard on the system prompt, enable Thinking Mode, and engineer a smart recovery loop, these edge models become a feature, not a compromise.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse