---
title: What happens to technical debt when AI makes code cheap? - DEV Community
url: https://dev.to/jennapederson/what-happens-to-technical-debt-when-ai-makes-code-cheap-9oa
site_name: devto
content_file: devto-what-happens-to-technical-debt-when-ai-makes-code
fetched_at: '2026-09-01T21:37:46.045677'
original_url: https://dev.to/jennapederson/what-happens-to-technical-debt-when-ai-makes-code-cheap-9oa
author: Jenna Pederson
date: '2026-09-01'
description: Dear past Jenna, I know you're used to dealing with large, complex, legacy codebases riddled with... Tagged with ai, programming, software, agents.
tags: '#ai, #programming, #software, #agents'
---

Dear past Jenna,

I know you're used to dealing with large, complex, legacy codebases riddled with technical debt. And for the longest time, that was kind of your thing. You'd unwind them, figure out how to insert a feature here without breaking functionality there, or discover that customers had come to depend on something that was technically a bug.

I recently saw this post on X (it's no longer a tweet on Twitter, but that's a story for another day):

Technical debt used to be something you just had to live with in a sufficiently large codebase. No longer.

The replies and reposts were all over the place, but a number of them went like this:

The technical debt is the whole codebase now.

The thing is, both might be right: AI makes technical debt easier to fix. Agents can refactor repetitive patterns, migrate dependencies, add tests around legacy behavior, and tackle cleanup work that might otherwise sit in the backlog forever.

Codex, go fix all the technical debt in this repo.

A reasonable request with no follow-up questions whatsoever.

But AI also makes technical debt incredibly easy to create.

## Technical debt isn't just bad code

Technical debt has never just meant bad code, and it isn't necessarily the result of bad engineering. It's often the result of intentional tradeoffs we made at a specific point in time (except for that one guy who just refused to write unit tests).

But a lot of it comes from perfectly reasonable decisions that became wrong as we learned more about how the system would actually be used and how it needed to evolve.

Codebases grew. Requirements changed. Customers started relying on buggy functionality (congrats, it's a feature now). Systems scaled across teams. Teammates came and went. Dependencies aged. The architecture that made perfect sense three years ago became the thing standing in our way today.

We made the best decisions we could with what we knew at the time.

Then we put the software in production and learned more.

Some technical debt is simply the gap between the decisions we made then and what we learned we actually needed later.

## Now we can build faster than we learn

It used to take time to turn an idea into a large system. And while we were building, we were also learning.

Remember thefriction we talked about before? Some of that friction forced us to pause and ask important questions like, "Should we build this?" Designs changed. Requirements were questioned. Implementation and learning happened somewhat concurrently.

Now, engineering teams can accumulate an entire system before they fully understand what they're building (or what they've built).

AI can compress implementation time. It can't necessarily compress the time it takes to learn what the system needs to become.

I'm not arguing that slow development was good. But some of the time we're eliminating was time we spent learning.

## You can't generate production experience

Some of my hardest lessons came from production issues that were nearly impossible to reproduce in a test environment.

Threading and concurrency bugs. Or those bugs that required a very specific alignment of the stars between customer data, system state, timing, and apparently the current phase of the moon (I'm looking at you, VAT tax calculator of 2009).

A design can appear completely reasonable until you put real traffic on it. Real traffic introduces timing problems, race conditions, and interactions you didn't anticipate.

An agent might build a system that performs exactly as expected. It might even anticipate problems we wouldn't.

But neither of us has a crystal ball.

Whileagents can help us implement faster, that's not the same thing as learning faster.

## What if we spent the speed differently?

Instead of:

build → build → build → build → build → ship → observe → learn → change

What if turning five weeks of implementation into one meant you could get to production and start learning sooner?

build → ship → observe → learn → change → repeat

Implementation has gotten much cheaper. But reviewing, testing, validating design decisions, securing, operating, and learning from production haven't gotten cheaper at the same rate.

I ran acrossBrandolini's law(the "bullshit asymmetry principle") last week:

The amount of energy needed to refute bullshit is an order of magnitude bigger than that needed to produce it.

The code can be perfectly fine and still take much longer to review than it did to generate.

Codex, refactor this module without changing its behavior.

87 files changed.

An agent can produce a giant PR in minutes. Figuring out whether it should even exist, whether it's correct and secure, fits the system, and will be maintainable can still take hours.

And all of this is happening in an environment that's now go, go, go.

The expectation that "agents make you faster, so now you can do more work, all the time" is real. If leadership sees faster implementation and responds by asking for more of everything, then we're pushing more software through engineering processes that haven't experienced the same speedup.

The problem starts when we spend all of that speed on more implementation before we’ve learned enough to know it's worth spending time on.

## Spend the speed on learning

I hope AI really does mean we won't have to live with technical debt the way we have in the past. Maybe agents will eventually manage much of it continuously, without us even thinking about it. And how we create, carry, and pay down technical debt may look completely different in a few years. I just don't know yet.

What I do know is that we don't have to spend all the time AI gives us on more code.

We can ship something, find out where we were wrong, change it, and do the whole thing again.

So for now, maybe we use faster implementation to shorten the whole learning loop.

Until the next postcard.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse