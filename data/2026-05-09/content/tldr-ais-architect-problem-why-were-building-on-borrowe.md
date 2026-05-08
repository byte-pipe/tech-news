---
title: 'AI''s Architect Problem: Why We''re Building on Borrowed Land :: Notes from the Rabbit Hole'
url: https://magnus919.com/2026/05/ais-architect-problem-why-were-building-on-borrowed-land/
site_name: tldr
content_file: tldr-ais-architect-problem-why-were-building-on-borrowe
fetched_at: '2026-05-09T07:54:15.112181'
original_url: https://magnus919.com/2026/05/ais-architect-problem-why-were-building-on-borrowed-land/
date: '2026-05-09'
published_date: 2026-05-05 08:00:00 -0400 -0400
description: Kanupriya Yakhmi's AgileRTP talk on AI portability exposes the uncomfortable truth that most companies scaling AI are building on rented ground, with no exit strategy when the landlord changes terms.
tags:
- tldr
---

# AI’s Architect Problem: Why We’re Building on Borrowed Land

2026-05-05
7 min read (1438 words)
#
AI
 
#
ai-strategy
 
#
vendor-lock-in
 
#
software-architecture
 
#
engineering-leadership
 

## Table of Contents

I spent Tuesday evening at anAgileRTP meetupwhereKanupriya Yakhmigave a talk that landed harder than most conference keynotes I’ve sat through. The title wasThe Architect’s Trap: Scaling AI Beyond Ecosystem Monopolies and Vendor Lock-in. It was a systems thinker walking a Zoom room of tech professionals, mostly Agile coaches and product managers, through the quiet catastrophe inside companies that bet everything on a single AI provider and forgot to ask what happens when the landlord changes the terms.

Kanupriya is a PhD candidate in AI/ML, a product manager, and a former systems architect at Waymo. She also holds an Executive MBA. That combination, someone who has designed safety-critical systems at the hardware layer, understands product strategy, and can read a P&L, is vanishingly rare. And it showed. She wasn’t speculating about AI risk from an armchair. She was describing failure patterns she’s already watched play out.

## The Three Questions Every Company Should Be Asking#

Kanupriya opened with a simple framework: three questions that any business building on top of AI models should be able to answer before they ship.

First: can your business logic run on a different model without a rewrite?This is the expensive one. If your product’s core behavior is tangled up in a specific model’s quirks and output patterns, migration becomes a rebuild. Not a refactor. A rebuild. For a small B2B company operating on thin margins, that’s existential.

Second: can your training data, embeddings, and evaluation sets migrate?The cost here isn’t just money; it’s time and labor. RAG pipelines fine-tuned against one provider’s embedding model don’t necessarily produce the same results when you swap the model underneath. Evaluation harnesses, the thing that tells you whether your AI product is actually working, are frequently the first thing teams skip. Kanupriya called evaluation gaps “the most expensive form of technical debt,” and I wrote that down twice.

Third: can your deployment move across providers without fundamentally changing your architecture?If the answer is no, you don’t have an AI product. You have a managed service with your name on it, and your provider sets your roadmap by default.

These three questions, she argued, are the minimum due diligence before adopting any AI product. Not an aspirational checklist. The floor.

## The Portability Spectrum#

The talk worked because it was specific. Kanupriya laid out a four-stage model of AI integration: not an abstract framework, but something that maps directly to real decisions teams are making right now.

AtStage 1, all AI calls go directly to one provider’s SDK. This is the default. It’s fast to build, easy to reason about, and catastrophically expensive to unwind. She acknowledged this can work; she compared it to the iOS ecosystem, where deep coupling creates a genuinely good experience for users who’ve chosen that dependency consciously. The problem isn’t coupling. The problem is coupling you didn’t know you were choosing.

Stage 2wraps provider calls behind an internal interface. Same models underneath, but swapping becomes a configuration change rather than a rebuild. She was blunt about how few teams actually do this. Most should.

Stage 3is the “portable builder.” Open-weight alternatives have been evaluated, data pipelines are owned, and you only need to change the evaluation harness when you move. If you have an actual AI strategy, this is where you live.

Stage 4is full infrastructure portability: hardware-agnostic serving, provider diversity, and the ability to move across model, data, and compute independently. Few organizations are here. The ones that are tend to treat architecture as a competitive advantage rather than a cost center.

“The failure point is never the model. It’s an assumption that the model will stay the same.”

* Kanupriya Yakhmi

## The Hidden Cost of Speed#

A more nuanced point, and one I hadn’t fully appreciated before: vendor lock-in isn’t always a mistake. Speed to market genuinely matters for small companies; sometimes the right call is to lean hard on external services to capture customers before a competitor does. She described companies that did exactly this: built fast on cloud AI, captured the market, and later migrated to in-house infrastructure when costs became prohibitive. That was a deliberate trade-off, not an oversight.

The trap, she said, is treating a proof-of-concept decision as permanent. Many organizations make dependency choices during prototyping and never revisit them in production. By the time the bills arrive or the model behavior changes, the switching costs have become unknown and the product’s addressable market has already shifted.

She used the term serviceable obtainable market (SOM) to make this concrete. You might have a large total addressable market, but if your AI dependencies limit which segments you can actually serve at a viable cost, your real market is smaller than you think. Teams that never re-evaluate their model choices are leaving money on the table and don’t know it.

She also made a sharp observation about engineering morale. Teams inherit architecture decisions made before they joined, often without documentation of the assumptions behind those decisions. When a model changes behavior and things break, the team that has to fix it wasn’t in the room when the dependency was chosen. “The team tends to inherit the decisions before they even join,” Kanupriya said, “which is like operating from blind sides.”

## Agile for External Dependencies#

The most original thread in the talk was what Kanupriya called “Agile 2.0.” Traditional Agile solved for internal coordination: how teams work together, how work is prioritized, how blockers are surfaced. But AI development introduces dependencies that live entirely outside the organization: model providers, API stability, pricing changes, terms of service.

Her proposal was straightforward: Agile ceremonies should explicitly surface and track external vendor risks. Put “what changed upstream that might break us?” into standups. Account for model deprecation timelines in sprint planning. Use retrospectives to ask whether vendor behavior is creating technical debt the team didn’t choose.

She also argued that different teams within an organization face different external dependencies and should run their own Agile processes shaped by those specific risks, rather than conforming to a monolithic standard. An ML team depending on a specific inference provider has a different risk surface than a frontend team using a managed AI chatbot widget, and pretending otherwise with one-size-fits-all process is self-defeating.

“AI cannot replace people because people think through the failures that can happen in the future.”

* Kanupriya Yakhmi

## Why AI Can’t Replace People#

It sounds obvious until you sit with it. Current AI systems are pattern matchers, not failure modelers. They can generate code that works under expected conditions, but they can’t anticipate what breaks when those conditions change, because they don’t understand the system they’re operating inside. A senior engineer looking at an architecture diagram sees not just what’s there, but what isn’t: the missing error handler, the unstated rate limit, the assumption about response format that the provider never documented.

This is why human-in-the-loop governance actually matters. Not as a checkbox. As the mechanism that catches what the model can’t foresee. Kanupriya recommended hiring domain specialists specifically to test AI products, and paying external users to find flaws. Not because the AI is unreliable in a generic sense, but because reliability is always contextual, and context is exactly what these systems lack.

## What This Means for Builders#

If you’re building on AI infrastructure today, Kanupriya’s talk offers a practical starting point that doesn’t require a corporate mandate or a six-figure architecture engagement:

1. Never call a provider SDK directly from your business logic. Wrap it behind an internal interface. It’s one file. It might save your company.
2. Build an evaluation harness before you ship. If you can’t detect when your AI product degrades, you don’t have a product; you have a hope.
3. Treat open-weight models as strategic alternatives, not academic curiosities. When the capability gap closes (and it’s closing fast), having already evaluated alternatives means you can move without panicking.
4. Document your assumptions about model behavior. When the model changes and something breaks six months from now, the engineer debugging it won’t be you. Leave them a trail.

And if you’re a small company that made a conscious bet on a single provider to move fast: that’s fine. Just write down that it was a conscious bet, and set a calendar reminder to re-evaluate it. The difference between a strategic dependency and accidental lock-in is whether you remember you chose it.

Kanupriya Yakhmi is a PhD candidate in AI/ML and a product manager. She previously worked in system architecture at Waymo. You can find her onLinkedIn,Substack, or at herproduct portfolio. Her talk was hosted byAgileRTP, organized byCatherine Louis.

Read other posts
[
The Plot Twist Inside the Octopus Brain
] >