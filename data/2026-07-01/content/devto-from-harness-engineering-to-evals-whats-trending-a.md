---
title: 'From Harness Engineering to Evals: What’s Trending at AI Engineer - DEV Community'
url: https://dev.to/dailycontext/from-harness-engineering-to-evals-4212
site_name: devto
content_file: devto-from-harness-engineering-to-evals-whats-trending-a
fetched_at: '2026-07-01T19:35:56.905658'
original_url: https://dev.to/dailycontext/from-harness-engineering-to-evals-4212
author: Ben Halpern
date: '2026-07-01'
description: I’m at the AI Engineer conference in San Francisco this week. The event has every major brand-name... Tagged with aie, ai, agents, security.
tags: '#aie, #ai, #agents, #security'
---

AI Engineer World's Fair Coverage

I’m at theAI Engineer conference in San Franciscothis week. The event has every major brand-name sponsor you’d expect, a lineup of internet-famous project maintainers on stage, and a massive schedule covering which more or lesshas something for everyone. It’s easy to get lost in the noise. I spent my time trying to figure out what themes are actually real.

With dozens of tracks and thousands of builders, the ecosystem looks incredibly fractured. But if you look at what engineers are actually putting into production, the chaos collapses into a clear pattern. The industry is moving past simple chat interfaces and treating large language models like central processing units inside a larger, highly structured software architecture—essentially an LLM Operating System.

I cataloged everything I was seeing, dug into the technical tracks, and came away with these six themes.This is not my endorsement, and I have not separated the hype from the real. Take these brief summaries as jumping-off points to help you go deeper if any of these ideas trigger your curiosity.

## 1. The Shift to Repository-Scale “Software Factories”

For the last few years, AI in development was basically tab-complete. You wrote a line of code, an assistant suggested the next few tokens, and you moved on.

That single-file approach is quickly becoming obsolete. The focus has shifted to repository-scale, multi-agent systems—what people are callingSoftware Factories.

Instead of writing lines of code alongside an AI assistant, developers are managing fleets of agents that operate across entire codebases. For example, Uber shared details on uReview, their internal code review engine. It uses agents to autonomously review pull requests, spin up localized test suites, catch edge cases, and commit fixes back to the branch before a human even looks at it.

To make this reliable, engineers are plugging compilers and linters directly into the agent’s feedback loop. If the generated code fails to compile, the raw error output is fed right back into the system prompt. The model reads its own error, fixes the bug, and re-runs the check autonomously.

## 2. Hardening Systems with “Harness Engineering”

There’s a common realization on the conference floor right now:“Everyone is building an agent harness, but nobody calls it that.”

LLMs are inherently probabilistic and non-deterministic. Software infrastructure, however, requires predictable inputs and outputs. To fix this, teams are formalizing a core systems discipline:Harness Engineering.

The “harness” is the strict software wrapper built around a model to enforce constraints, manage state, and prevent infinite execution loops.

+--------------------------------------------------------+

| THE AGENT HARNESS |

+--------------------------------------------------------+

| 1. Durable Execution (State preservation & retries) |

+--------------------------------------------------------+

| 2. Structured Outputs (Schema enforcement / Pydantic) |

+--------------------------------------------------------+

| 3. Dynamic Guardrails (Input/Output sanitization) |

+--------------------------------------------------------+

Instead of letting an agent run unmonitored, developers are using toolchains like Temporal or Inngest to implementdurable execution. If an agent is running a complex, multi-hour workflow and hits a network timeout, the harness preserves its memory and state. The process can resume exactly where it failed without repeating expensive API calls. Paired with libraries like Pydantic or Instructor to force strict JSON schema compliance, the harness makes unpredictable models behave like stable infrastructure.

## 3. Computer Use vs. Custom APIs

For decades, integration meant writing custom API connectors or scraping endpoints. A major theme this year isComputer Use—building agents that navigate software exactly like a human operator does: by looking at a screen, moving a mouse, and typing commands.

Enabled by better vision-language models (VLMs), these systems don’t need structured backend APIs. They take continuous screenshots of a graphical user interface (GUI), parse the visual layout to locate fields and buttons, and execute precise pixel coordinates.

This has forced a shift in local developer setups. Engineers are building isolated, sandboxed terminals and open-source desktop companions (like OpenClaw) that give background agents their own virtual environments. This lets agents spin up local servers and debug files in isolation without taking over the engineer’s active screen and keyboard.

## 4. Context Engineering & “Tokenmaxxing”

Context windows have scaled to millions of tokens, but dumping an entire codebase into a prompt is an expensive, high-latency anti-pattern.

Time-to-first-token and API costs are the real bottlenecks today. Because of this, developers are focusing heavily onContext Engineering—treating the context window as a highly optimized, dynamic memory cache rather than a static text dump.

The optimization strategy generally follows a three-layer approach:

* Prefix Caching: Inference engines like vLLM cache the Key-Value (KV) states of static system instructions or documentation headers. Subsequent requests reuse this cache, significantly cutting down latency and cost.
* Context Compression: Middleware layers are introduced to run semantic compression algorithms, pruning irrelevant tokens and summarizing messy chat logs before sending data to the provider.
* Graph RAG & Hybrid Retrieval: Instead of pulling raw text blocks indiscriminately, systems use structured knowledge graphs to pass only high-signal data into the active context window.Finish reading at link.dev.to/aie39.

## 5. Moving Past “Vibe-Based” Evaluations

If there is one clear operational shift, it’s that vibe-based engineering is dead. Reviewing a few outputs, deciding they look reasonable, and shipping them to production is no longer an acceptable practice.

The core focus of theEvalscommunity is on automated, multi-step simulation benchmarks. Evaluating an agent now requires spinning up an isolated virtual environment—a temporary sandbox with mock databases and network access—and letting the agent attempt a complex task. The evaluation framework doesn't grade the style of the response; it checks if the task was completed successfully, notes how many steps it took, and verifies that no security protocols were broken.

Engineers are also moving away from the “Persona Trap”—giving a model a prompt like “You are a senior staff engineer.” Studies shared at the event show this approach evaluates a stylistic vibe rather than a rigorous technical capability, often introducing silent biases that degrade performance. The standard now is rigid, task-oriented testing.

## 6. Secure Micro-Sandboxes for Runtime Safety

Giving an agent the authority to write code, modify files, and run terminal commands introduces severe security risks.

Platform engineers are tackling this by focusing on the underlying execution layer. The industry standard has normalized aroundMicro-Sandboxes. Agent-generated code is executed inside lightweight, ephemeral micro-VMs (like those from E2B or Docker) that spin up in milliseconds, handle the specific computation, and are immediately destroyed to prevent container escape or persistent file system tampering.

There is also a major push toward credential masking. When agents need access to enterprise databases or third-party tools, engineers are using new delegation layers like the AAuth protocol. This grants the agent mission-bounded authority to call a tool, but prevents the agent from ever seeing or interacting with the raw API keys, neutralizing prompt injection leaks.

## The Bottom Line

It’s easy to skim these topics, feel a wave of FOMO, and think you’re already lagging behind if you aren’t running a fleet of micro-sandboxes or an autonomous software factory.

Don’t buy into the hype. You don’t need to overhaul your entire stack by next Monday.

The real takeaway from all the noise at Moscone is actually pretty reassuring: AI is just becoming regular software infrastructure. The developers who build useful things over the next few years won't be the ones chasing every flashing new model drop or complex multi-agent framework. They’ll be the ones applying basic, boring engineering principles—making their inputs predictable, testing their code rigorously, and keeping their environments secure.

If you're looking for a place to start, don’t overcomplicate it. Pick a single, repetitive workflow in your day-to-day. Wrap a clean, defensive code harness around it, build a straightforward evaluation script to check its work, and see what happens. Inspiration is great, but pragmatism is what actually ships.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse