---
title: AI Agents Are Great at 80% of Our Code. The Other 20% Is Why We Still Need Seniors. - DEV Community
url: https://dev.to/mickyarun/ai-agents-are-great-at-80-of-our-code-the-other-20-is-why-we-still-need-seniors-3lh5
site_name: devto
content_file: devto-ai-agents-are-great-at-80-of-our-code-the-other-20
fetched_at: '2026-05-29T04:36:04.090061'
original_url: https://dev.to/mickyarun/ai-agents-are-great-at-80-of-our-code-the-other-20-is-why-we-still-need-seniors-3lh5
author: arun rajkumar
date: '2026-05-28'
description: We let AI agents loose on a payment platform. They crushed the boring stuff. Then they silently broke... Tagged with ai, discuss, webdev, startup.
tags: '#discuss, #ai, #webdev, #startup'
---

We let AI agents loose on a payment platform. They crushed the boring stuff. Then they silently broke the stuff that matters.

A survey came out last week. 54% of all code is now AI-generated. Up from 28% last year.

I read that number and thought: yeah, that tracks. We're probably in that range too.

But here's the thing nobody's asking — which 54%?

Not all code carries equal weight. A CRUD endpoint for fetching merchant details? Low risk. The webhook handler that transitions a payment frompendingtocomplete? That's someone's rent. Someone's payroll. Get that wrong and money moves where it shouldn't, or worse, money doesn't move at all.

I'm the CTO of a payment platform. FCA-authorised, processing real money, real merchants, real consequences. We run NestJS microservices, Docker, Traefik — the usual stack. And we've been using AI agents aggressively for over a year now.

I'm not here to tell you AI is dangerous. It's not.

I'm here to tell you it's dangerous when you forget what it's actually good at.

## The 80% Where AI Agents Are Genuinely Brilliant

Let me give credit where it's due. AI agents have made our team faster in ways that would have seemed absurd two years ago.

API scaffolding. Generating service boilerplate. Writing Zod validation schemas. Spinning up new endpoints. Creating test stubs. Refactoring imports. Migrating patterns across repos.

We run multiple microservices. When we need a new service, an agent can scaffold the entire thing — module structure, base configuration, Docker setup, Traefik labels — in minutes. What used to be a half-day of copy-paste-and-tweak is now a conversation.

When we overhauled our env management across all repos, AI agents did the grunt work. They mapped every.envfile, found naming conflicts, identified common variables, and generated a unified Zod schema. What would have taken a team days of grep-and-spreadsheet work took hours.

For this 80% of the codebase — the predictable, pattern-following, structurally repetitive code — AI agents are the best junior developers money can buy. Tireless. Cheap. No ego. Almost never make a mistake on the stuff they're good at.

An army of juniors sitting at your terminal.

## Then You Hit the Other 20%

Here's where it gets interesting.

We had an agent build out a webhook handler. Webhooks in payments are critical — they're how you know a payment succeeded, failed, or needs attention. The agent wrote the handler. It looked clean. Tests passed.

But it silently ignored the edge cases.

Status transitions have rules. A payment can go frompendingtocomplete. It cannot go fromcompleteback topending. When a human developer builds this, they think about the illegal transitions because they've seen what happens when money moves backwards. They build the guard because they've felt the pain of not having it.

The agent didn't care about that. It built the happy path beautifully and treated the edge cases like they didn't exist.

When we do this work manually, this type of error never happens. A senior developer who has worked in payments for years doesn't forget the impossible transitions. It's not in their code — it's in their bones.

## The Pattern I Keep Seeing

This isn't a one-off. After months of working with AI agents on a regulated payment stack, one pattern is consistent:

AI agents optimise for completion, not correctness.

They want to finish the feature. Get to the green checkmark. And to get there efficiently, they take shortcuts that look reasonable on the surface.

The agent builds what should happen. It rarely builds what shouldnothappen. In payments, the negative cases are where all the real risk lives. What happens when a webhook arrives twice? What happens when a refund is requested on an already-refunded transaction? What happens when the bank returns an unexpected status code? The agent doesn't think about any of that unless you explicitly tell it to.

Then there's the reusability problem. We have shared utility packages. Helper functions. Common patterns that the team has standardised on over years. The agent doesn't care. It writes its own version from scratch. It works, but now you have two implementations of the same logic — one tested and trusted in production, one freshly generated and untested. The agent is focused on completingthisfeature, not maintaining the architecture.

And the subtlest one — agents seem to optimise for fewer back-and-forth turns. It looks like they're saving cost, saving context. Complex validation? Skip it, the basic case works. Error handling for a rare edge case? Not worth the tokens. The result is code that passes every test you wrote but fails on the scenarios you didn't think to test — because those are exactly the scenarios the agent also didn't think about.

## Juniors Don't Ship Products. They Write Code.

Here's the frame that made this click for me.

Claude — or any coding agent — is the best junior developer money can buy. An army of juniors. Tireless, cheap, no ego, near-zero error rate on routine work.

But juniors don't ship products. They write code.

The difference between code and a product is judgment. Knowing which transitions are illegal. Knowing that the retry logic has a specific backoff curve because you've been burned by what happens when it doesn't. Knowing that the webhook handler needs idempotency because banks sometimes send the same notification three times.

That knowledge doesn't come from training data. It comes from years of operating a system, debugging at 2am, explaining to a merchant why their settlement was delayed.

The most dangerous mistake a CTO can make in 2026 is buying AI to replace senior engineers. The right move is buying AI to enable them.

Replace your senior with AI? You get speed plus silent disasters.

Enable your senior with AI? You get an architect with an army.

## What We Actually Do About It

I'm not writing this to complain about AI. I'm writing this because we've built a system that works, and it might help you too.

The first thing we did was make our architecture machine-readable. We extract design patterns and architecture rules into formats that agents can consume. When an agent works on our codebase, it doesn't just see code — it sees boundaries, patterns, rules about what belongs where. Not documentation nobody reads. Lints and constraints that the agent can't ignore.

Then we invested heavily in testing the negative cases. Every PR — human or AI — runs through the same suite. But we specifically built tests for the stuff agents skip: illegal state transitions, duplicate webhook handling, idempotency checks. If the agent silently drops a negative case, the tests catch it before it ships.

And seniors still review everything that touches money. No AI-generated payment logic ships without a senior looking at it. Not because we don't trust AI — because we know exactly where it's blind. The review isn't checking syntax. It's checking judgment. Did the agent handle the ambiguous bank status? Did it respect our existing retry logic? Did it use the shared utility or reinvent the wheel?

This problem bothered me enough that I started buildingBodhi Orchard— an open-source agentic development framework. The core idea: don't just let agents write code. Feed them the full context — architecture, design patterns, test plans, existing utilities — so they stop making the same blind-spot mistakes. Human decisions over human busywork, with guardrails that actually enforce quality.

## The Real Question for 2026

The survey says 54% of code is AI-generated. I believe it.

But here's my question: what percentage ofbugsin 2026 will be AI-generated?

And more importantly — who's going to find them?

Not the agents. They wrote the bugs in the first place. Not the juniors — they won't know enough to spot what's missing.

It's going to be the seniors. The architects. The people who've operated these systems long enough to know where the bodies are buried.

The 80% is solved. AI won. Celebrate that.

Now invest in the humans who understand the other 20%. Because that's where your product lives or dies.

I'm Arun, CTO & Co-Founder of Atoa — a UK open banking payment platform. I write about what it's actually like to build fintech with AI, not what the conference slides say it's like. If this resonated, follow me here or onX @mickyarun.

And if you're curious about building AI-native development with proper guardrails, check outBodhi Orchard.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse