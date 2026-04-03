---
title: Cognitive Debt
url: https://acairns.co.uk/posts/cognitive-debt
site_name: tldr
content_file: tldr-cognitive-debt
fetched_at: '2026-03-12T03:13:29.528820'
original_url: https://acairns.co.uk/posts/cognitive-debt
date: '2026-03-12'
description: The growing gap between the code your team ships and the code your team understands. It's not technical debt. It's worse.
tags:
- tldr
---

# Cognitive Debt

March 2, 2026·7 min read

Your team is shipping faster than ever. Pull requests are flowing. Features land in days that used to take weeks. Something feels off though. The code works. But nobody knowshowit works.

This is cognitive debt.

## #The Delta

There are two lines worth paying attention to right now.

The first is code volume. We're producing more code than ever. Code you'd normally spend time designing for a bit, work out its interface, what it needs to do, figure out the right responsibilities, maybe write a test first, now turns up fully formed from a prompt. Methods and all. It's there before you've finished thinking about the problem.

The second is comprehension. How much of that code does your team actually understand? This line isn't keeping up. It's falling behind as the first one pulls away.

How much code being shipped do you believe is deeply understood?
33
%
Lines of code
Code understood
Cognitive debt

The space between those two lines is cognitive debt.

## #Not Technical Debt

You've heard of technical debt. Most teams live with it. Technical debt is code youknowis bad. Shortcuts you chose to take, corners you consciously cut, with a plan to come back later. You can point at it. You can put it on a backlog.

Cognitive debt is different. It's code you don't even know is bad, because nobody understands it well enough to judge. You didn't choose to take it on. It accumulated silently, one accepted suggestion at a time.

Technical debt lives in the codebase. Cognitive debt lives in your team's heads, in the gaps between what the codebase does and what anyone can actually explain.

## #How It Accumulates

When you write code by hand, you build understanding as a side effect. You wrestle with the problem, try things that don't work, and arrive at a solution you can explain because you lived through finding it.

When AI writes code for you, the code appears fully formed. It compiles. It passes tests. You read it, it looks reasonable, you merge it. But the understanding was never constructed. The struggle that would have made you the expert on that piece of the system was skipped.

Peter Naurwrote in 1985that a program is not its source code. It's a mental model, shared between the people who built it.

the theory built by the programmers has primacy over such other products as program texts, user documentation, and additional documentation such as specifications.

For Naur, the theory comes first. The code comes second. Understanding why the code works one way, and not the other. What was tried. What was rejected. None of that made it into the code. It only ever lived in the heads of the people who thought it through.

When AI generates the code, that reasoning doesn't happen on its own. The code is there, but the mental model isn't. Not unless you make a point of building it.

## #The Warning Signs

Cognitive debt doesn't show up in failing builds. It's subtler than that.

Review times drop. Not because anyone got careless, but because there's more code coming through than anyone can thoroughly read."It passes tests"starts doing the job that a proper review used to.

Incident response slows down because nobody can trace the logic through code they didn't write. When you don't understand the code you're debugging, fixing it takes two or three times longer than it should.

Onboarding breaks down. New engineers can't learn from teammates who don't understand the system themselves."Ask the person who wrote it"falls apart when the answer is"Copilot wrote it."

And code gets rewritten more than it should. Someone accepts a generated function, moves on, and three weeks later when the requirements change, nobody can figure out how to modify it. So they rewrite it from scratch.

There's a thing nobody talks about enough: parts of the codebase that nobody wants to touch. Not because the code is bad, but because nobody knows what it does. That reluctance is cognitive debt making itself felt.

## #The Three Stages

Allstacksdescribes three stages of accumulation. The progression makes a lot of sense.

The HoneymoonDay 1–30

“Look how much we're getting done.”

In the first month or so, everything is fine. The team has full context. AI is speeding up work they already understand. Fast output, low risk.

The DriftMonth 1–6

“It’s been reliable enough so far.”

Between months one and six, things slip. The output keeps landing, so you stop double-checking every line. That’s natural. But the gap between “this works” and “I understand why this works” widens without anyone noticing.

The CliffMonth 6+

“I don’t really know how this works anymore.”

After six months, you hit the wall. Your team can’t confidently change the code you own. When something breaks, you’re not debugging. You’re guessing. And then you’re reverse-engineering your own system.

## #The Trust Paradox

Here's the part that makes this hard to address. Stack Overflow's developer surveys found that trust in AI coding tool accuracydropped from 43% to 33%year over year. In that same period,usage wentupto 84%.

2024
2025
Trust in AI output
AI tool usage
Trust paradox

We trust it less but use it more?

This makes sense as the tools are genuinely useful. But"useful for generating code"and"I understand what it generated"are not the same thing. The more comfortable the workflow becomes, the easier it is to skip the understanding part.

## #Where I Draw the Line

I use these tools every day. I'm faster because of them, and I'm not going back. But speed without understanding is a loan, not a gift.

It's worth being honest about the trade we're making. I've always thought of technical debt as borrowing future productivity. You gain speed now and repay it later. Cognitive debt is the same deal, except what you're borrowing against is understanding. Every time we accept code we don't fully understand, we're taking out a loan we might not know how to repay. Sometimes that's a trade worth making. Sometimes it isn't. The problem is when you stop noticing you're making it at all.

There's a growing movement that says AI should handle more of the codebase. Dependency updates, CI migrations, test scaffolding, configuration. All automated, all running without you. The argument is that developers shouldn't need to understand every line. They should review, calibrate, and focus on the hard problems.

I don't think that's wrong. But I don't think it's the whole picture either.

The way I think about it borrows from onion architecture. Your core domain sits in the centre. The business logic, the rules, the things that make your system yours. Wrapped around that is the application layer, the use cases that orchestrate the domain. And around all of that sits the outermost stuff: framework concerns, configuration, infrastructure wiring.

Not all of these layers carry the same weight. The core domain is where understanding matters most. That's where the mental models live. That's where Naur's "theory" gets built. If you lose touch with your domain logic, you can still debug when something breaks. You just might not know what correct looks like anymore.

But the outer layers? Dependency management. CI pipeline configuration. Framework boilerplate. I'm not sure the same standard needs to apply. These are tasks that can eat a lot of time, but they don't require the same depth of understanding. They're the kind of workbackground agentsare genuinely good at.

My approach right now is to be deliberate about the boundary. I'm meticulous about understanding my core domain. I want to know why every decision was made, what was tried, what was rejected. That's the work I do by hand, or at least closely enough that my mental model stays intact.

For the rest, the configuration, the wiring, the framework concerns, I'm increasingly comfortable handing that off. Not blindly. I still drive and review it. But I've stopped demanding I hold the full picture in my head at all times.

Cognitive debt is real. But so is the impossibility of understanding everything as systems grow. The answer isn't to understand all of it or none of it. It's to know which parts you can't afford to lose, and protect those.

Understanding is what matters. Code is just an artifact.

## #Further reading

* How Generative and Agentic AI Shift Concern from Technical Debt to Cognitive Debt
* AI can 10x developers... in creating tech debt
* Cognitive Debt Is Not Technical Debt
* Comprehension Debt: The Hidden Cost of AI-Generated Code
* Peter Naur's Legacy: Mental Models in the Age of AI Coding
* 2024 Stack Overflow Developer Survey: AI
* 2025 Stack Overflow Developer Survey: AI
* Closing the Developer AI Trust Gap
* Programming as Theory Building
* Background Agents