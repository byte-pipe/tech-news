---
title: Despite everything, a small praise of GitHub — David Poblador i Garcia
url: https://davidpoblador.com/blog/despite-everything-a-small-praise-of-github.html
site_name: tldr
content_file: tldr-despite-everything-a-small-praise-of-github-david
fetched_at: '2026-05-03T11:40:55.980131'
original_url: https://davidpoblador.com/blog/despite-everything-a-small-praise-of-github.html
author: David Poblador i Garcia
date: '2026-05-03'
published_date: '2026-04-28T23:02:34Z'
description: Discover why GitHub, despite recent challenges and growing pains from skyrocketing usage, remains a quietly indispensable pillar of internet developer infrastructure—and learn how the trade-offs we've made for convenience are shaping its evolving future.
tags:
- tldr
---

Apr 28, 2026

# Despite everything, a small praise of GitHub

Discover why GitHub, despite recent challenges and growing pains from skyrocketing usage, remains a quietly indispensable pillar of internet developer infrastructure—and learn how the trade-offs we've made for convenience are shaping its evolving future.

It’s hard to ignore the current mood aroundGitHub. Something feels off.

AsGergely Oroszhas been hinting in recent posts and discussions, it’s becoming increasingly difficult to understand what the strategy is, or where leadership is taking things. You don’t need insider knowledge to feel it: outages, degraded services, indexing inconsistencies, security vulnerabilities surfacing in uncomfortable clusters.

None of this is catastrophic on its own. But together, it paints the picture of a system under strain rather than one confidently evolving. At the same time, there’s a broader conversation happening.

Armin Ronacherrecently publishedBefore GitHub, a piece worth reading in full: It’s not nostalgia for the sake of it. It’s a reminder that we built a lot before centralization, and that perhaps we’ve over-rotated toward convenience.

In parallel, you see people likeMitchell Hashimotoopenlyexploring pathsthat don’t put GitHub at the center of everything anymore. Not as a reactionary move, but as a natural evolution of tooling.

All of that criticism is fair. And yet.

## The infrastructure we stopped seeing

For more than a decade, GitHub hasn’t just been a git host. It has quietly become a massive layer of the internet’s developer infrastructure:

1. CI/CD through Actions
2. compute through runners
3. hosting via Pages
4. distribution via Packages
5. security scanning and advisories

All of this, for millions of developers, often on the free tier. The introduction ofunlimited private repositorieswas a turning point. That was the moment many of us stopped hedging and fully committed our workflows, our companies, and in many cases our products to GitHub.

And it worked.

It worked so well that we stopped thinking about it. Somewhere along the way, we also forgot something fundamental:gitwas designed to bedistributed. GitHub was supposed to be a convenience layer, not the center of gravity.

We traded that for simplicity and speed. And to be fair, it was a very good trade for a long time.

## The load has changed

What’s different now is not just scale. It’s the nature of the workload. We are no longer pushing code in the same way.

With agents, automation, and increasingly interconnected systems, the volume of activity has exploded. Not linearly. Not even exponentially in the traditional sense. It’s closer to multiplicative chaos:

1. automated PR generation
2. cross-repository workflows
3. CI pipelines triggering other pipelines
4. tools committing on behalf of users
5. side effects propagating across projects

10x, 20x…probably much more. This kind of load was predictable. If anything, it was inevitable. And it stresses a centralized system in very different ways than the old “developer pushes code, CI runs, done” loop.

So yes, things are creaking.

But it’s hard not to feel for the people inside GitHub right now. They are effectively running critical infrastructure for the internet, under a usage model that has fundamentally shifted beneath their feet.

## Centralization was a choice

None of this happened by accident. We chose this.

We chose convenience over distribution. We chose a single place where everything “just works.” We chose tight integration over loose coupling.

And again, that choice made sense.

But the trade-offs are becoming morevisible:

1. outages ripple globally
2. indexing issues affect entire workflows
3. vulnerabilities have systemic blast radii
4. platform decisions impact entire ecosystems

GitHub is not unique in this. Look atnpm. Look atPyPI. Look at container registries. Look at CI providers. We’ve built a large part of the internet’s production pipeline on top of a relatively small set of centralized services.

## What comes next?

The interesting question is not whether GitHub is struggling. It’s what a less centralized developer stack actually looks like.

Not in theory, but in practice. Just for fun, I’ve been exploring a small piece of that with alittle toy project. The idea is: remove theinternet dependencyfrom some of the new coding workflows. Keep things local-first, reduce reliance on always-on centralized services, and see what still works. It’s early. Incomplete and non functional. But it feels like a direction worth exploring.

Because if the current trajectory continues, we’re going to need alternatives, not as replacements, but as complements. I see a future where github could play the role of the source of truth, or the archival tool. But not the transactional tool forEVERYTHING.

## Discovery is breaking too

There’s another angle that gets less attention: discovery. With the explosion of tools we’re seeing, especially in the AI-assisted development space, the old mechanisms are starting to break down.

GitHub used to be, the hosting platform, the discovery engine and a reputation system. But is it still any of those, effectively? We’re seeing hundreds of new tools, libraries, frameworks, wrappers, agents… every week. The signal-to-noise ratio is collapsing.

So what replaces discovery? Do we need a modern equivalent offreshmeat.net? How do we curate, index, and preserve this explosion of software?

More importantly: how do we keep an archive of the world that isn’t implicitly tied to a single platform?

## Are we replacing our own primitives?

We’ve seen this pattern before.

Stack Overflowwas once the default interface to programming knowledge. Today, its role is diminished, partially replaced by AI systems that synthesize answers instead of indexing them. Is GitHub next?

Not necessarily disappearing, but becoming less central as the interface shifts from “browse and contribute” to “generate and orchestrate”. If that’s the case, then what we’re seeing now might not just be operational strain. It might be the early stages of a deeper transition.

AI doesn’t just accelerate workflows. It changes the primitives those workflows rely on.

## A small praise

And still, despite everything. It’s worth saying this clearly: GitHub has been an extraordinary piece of infrastructure.

It lowered the barrier to collaboration. It standardized workflows across the industry. It enabled millions of developers to build, share, and ship software.

And… often for free.

It’s easy to criticize when things wobble. Harder to acknowledge the scale of what has been built and maintained for so long.

So maybe this moment is not about dunking on GitHub.

A bit less blind reliance on centralization. A bit more investment in resilience and distribution. A bit closer to the original spirit of the tools we use.

GitHub doesn’t have to disappear for that to happen. But it can’t remain the same, either.

Github

Developer Tools

Software Development

Infrastructure

Automation