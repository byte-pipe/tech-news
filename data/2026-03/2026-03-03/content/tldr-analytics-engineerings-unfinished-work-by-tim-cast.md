---
title: Analytics Engineering’s Unfinished Work - by Tim Castillo
url: https://loglevelinfo.substack.com/p/analytics-engineerings-unfinished
site_name: tldr
content_file: tldr-analytics-engineerings-unfinished-work-by-tim-cast
fetched_at: '2026-03-03T06:01:08.084661'
original_url: https://loglevelinfo.substack.com/p/analytics-engineerings-unfinished
author: Tim Castillo
date: '2026-03-03'
description: The role stagnated before it reached its potential. The problems it was built for are bigger than ever.
tags:
- tldr
---

# Analytics Engineering’s Unfinished Work

### The role stagnated before it reached its potential. The problems it was built for are bigger than ever.

Feb 25, 2026
17
7
3
Share

I became an analytics engineer because I saw a gap in how organizations understood their own data. The role felt like the answer: a technical discipline focused on structuring and making a business’s knowledge usable. I left when it stopped growing toward that promise. I’m writing this because I think the window is open again, and I don’t want to watch it close twice.

The way I see it, an analytics engineer is someone who captures how a business understands itself and gives it structure. They identify the meaningful entities, define how those entities relate to each other, and formalize what the business measures and how. They take knowledge that would otherwise live in people’s heads or scattered across tools and make it explicit, reusable, and trustworthy.

Thanks for reading Tim’s Substack! Subscribe for free to receive new posts and support my work.

Subscribe

That’s the core of it. The tools, frameworks, and job descriptions are all expressions of that spirit. And the best analytics engineers I’ve ever worked with understood this intuitively because they were always greater than a single title or role.

## The Best Ones I’ve Worked With

The best analytics engineers I’ve worked with had an instinct I’ve never seen replicated in any other role. They couldn’t leave data alone until it made sense. They obsessed over getting definitions right and badgered relentlessly to ensure the entities and metrics in their models accurately reflected how the business worked. They treated data modeling as seriously as the best software engineers treat software architecture.

These people are still out there, and I still learn from them. When I describe the ideas in this post, I’m mostly saying out loud what they’ve been practicing quietly for years.

But a handful of brilliant practitioners can raise the ceiling for a role without moving the floor.

## Where It Stagnated

The analytics engineer role had every opportunity to keep evolving. Semantic layers matured, the conversation around data modeling deepened, and the problems that needed solving got more interesting and more consequential.

But the role settled. dbt was a massive part of the analytics engineering story, and rightfully so. It gave the role a home, a community, and a shared language. But over time the role’s identity calcified around it. “Analytics engineer” started to mean “writes SQL in dbt” and the scope stopped growing very much past that. The spirit of the role was always bigger than any single tool, but that’s where things landed.

## What I’ve Come to Believe About Where Logic Lives

Here’s what I’ve come to believe, largely through conversations with those same practitioners.

Business logic lives in three distinct layers. Being deliberate about what goes where is the whole game.

The dimensional data modelowns structural logic. What entities exist, how they connect, at what grain. If your organization has teams that roll up to other teams, the model is where that hierarchy lives. If you have customers with multiple accounts, the model captures that relationship. This layer describes the shape of the business.

The semantic layerowns measurement logic. This is where the term “active customer” is defined. Where revenue gets calculated. Where the filter that distinguishes one department’s view from another’s gets formalized. Sales says active means one thing. HR says it means another. Finance has a third definition. All of those are valid, and they all live in the semantic layer as different measures or filters on top of the same structural foundation.

If the semantic layer can’t derive a definition from what’s in the model, that’s a signal that the model is missing something.

The AI context layerowns interpretive logic. This is business logic too. It’s the subjective, human knowledge that doesn’t fit in a structured definition:

* The institutional memory of why the company stopped tracking a metric two quarters ago and what replaced it
* The unwritten understanding that when leadership asks about “the platform team,” they mean the org inclusive of subteams, not the Slack channel with that name
* The context that “closed won” at your company includes verbal agreements pending signature, which contradicts the textbook definition

When someone asks an AI agent a question about the business, the context layer carries the judgment that determines how the question gets interpreted before any data gets queried.

All three layers contain business logic, but they differ in kind: structural, measurement, and interpretive. Each one should be deliberately scoped, and when logic starts creeping from one layer into another, that’s usually a sign something isn’t pulling its weight.

The boundaries between these layers are still fuzzy in places. I’m actively working through where exactly they are in practice. But the framework holds.

I’ve been writing about how the structural and measurement layers play out in practice in a series onmedallion architecture, where Silver owns the dimensional model and Gold owns the semantic layer.

## This Is the Same Work

Here’s what I keep coming back to. Context engineering, semantic layers, and AI agents all require the same core skill: someone who cares deeply about capturing how a business understands itself and giving that knowledge a structure that humans and machines can use.

That’s the same skill analytics engineers have always practiced. Even during the dbt era, the best people in the role were already doing this. They were making decisions about where business logic lives and how to make data legible. The tools were narrower and the layers were less explicit, but the instinct was identical.

The difference now is that the stakes are higher. When dashboards were the primary consumer, a loose metric definition meant two reports disagreed and someone sent a confused email. When an AI agent is the consumer, a loose definition means it confidently gives the wrong answer to your VP and nobody catches it until the decision is already made.

## The Second Chance

The analytics engineer role is perfectly positioned for this moment, specifically the original spirit of it: the version that cares about meaning, structure, and legibility across every layer of the stack.

This is the second chance. The first time around, the role had room to grow and it settled instead. The problems emerging right now are asking for exactly what analytics engineering was supposed to become.

Don’t let it stagnate again.

If you’re an analytics engineer, or a data engineer, or anyone who works with business data and cares about this, try something. Pick a question your stakeholders ask all the time. Something like “how many active customers do we have” or “what’s our revenue this quarter.” Now imagine an AI agent has to answer it correctly.

Trace what it would need. Does the data exist somewhere well modeled? Is the definition owned in one place or scattered across a dozen dashboards? Would the agent know what the question actually means in your organization’s specific context? Would it know which definition of “active” to use?

Pay attention to where it breaks. That’s where the work is. And that’s the work analytics engineers were built for.

## Where I Landed, and Where I’m Looking

After analytics engineering, I went back to my roots as a data engineer. But I never stopped doing the work I’m describing here. I kept modeling, defining metrics, thinking about where business logic lives, and structuring knowledge across layers. The title changed. The work didn’t.

I don’t care what the role is called. I’m doing this work regardless. But I’d love to see analytics engineering become what it was always supposed to be. The people and the potential have always been there. Now the moment is too.

If you’re working on this too, I want to hear from you.

Thanks for reading Tim’s Substack! Subscribe for free to receive new posts and support my work.

Subscribe
17
7
3
Share