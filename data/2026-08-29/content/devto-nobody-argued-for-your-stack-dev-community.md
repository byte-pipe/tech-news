---
title: Nobody Argued For Your Stack - DEV Community
url: https://dev.to/playfulprogramming/nobody-argued-for-your-stack-51fj
site_name: devto
content_file: devto-nobody-argued-for-your-stack-dev-community
fetched_at: '2026-08-29T01:30:54.489682'
original_url: https://dev.to/playfulprogramming/nobody-argued-for-your-stack-51fj
author: Ryan Carniato
date: '2026-08-27'
description: Last week, it came to light Cursor had mostly finished migrating from SolidJS to React. This... Tagged with ai, webdev, react, programming.
tags: '#ai, #webdev, #react, #programming'
---

The emotional sting of tech stack churn

Last week, it came to lightCursor had mostly finished migrating from SolidJS to React. This migration happened about seven months ago. But it became a central focus of discussion following theSolid 2.0 RC release. Then yesterday, a week later, it came to my attention that the Anthropic docs example command for their large-scale migration feature is:

I admit that mygut reactionwas not great. Out of all the examples they could have chosen... Years of my work became a canonical example of the thing you migrate away from — in the same week we shipped the biggest release in the project's history — stung in a way I won't pretend it didn't. My second reaction was to assume that, like theother trickle-down postsI'd seen this week, this rode the same week-old news cycle.

Then I checked the Internet Archive and realized this has been theresince at least April 2026. Four months before the Cursor story broke. At this point, the whole public footprint was a mention of an experiment sandwiched between bigger updates in aCursor blog postposted in January. The kind of thing that no one outside the industry would even really pick up on. No reasoning, no benchmarks, no argument.

Stop to think about what that means. I should be careful here because I can't prove anyone at Anthropic ever read that Cursor post. Nobody can. Maybe a docs writer saw the experiment. Maybe Claude drafted its own example. But think it through. Either it traveled from a buried line in one company's release notes into another company's official docs, or it needed no origin at all. It was already assumed before any public migration existed.

Our industry has quietly started broadcasting conclusions where it used to transmit arguments. We couldn't have picked a worse time, because — as I'll get to — arguments are the only source that still matters.

## Why This Matters More Than It Used To

It would be fair to ask, hasn't it always been like this? Teams cargo cult large players. Netflix or Facebook uses this predates AI by decades. Optics and politics have always beaten pure technical merit. The weight of Facebook definitely helped React's early propagation.

But a narrative used to come with friction. It was always in the race, but it couldn't outrun the argument. This has changed for two reasons:

First, execution cost has collapsed.Bun's rewrite from Zig to Rust— about a million lines — was executed almost entirely by Claude agents in days, not months. And before you start thinking "lock-in", going the opposite way, while not as easy, has never been easier. Migrating from Rust to Zig or React to Solid has never been easier.

That sounds like good news. And it is. When migrations took years of human effort, cost put a damper on fashion. Now execution is a lot cheaper in all directions. The only thing left is the reason. Which suggests, on the surface, these decisions should be rooted in technical merit. But when narrative is what sets the direction, you start to see how a line buried in documentation is worth an essay.

Second, verdict production has been industrialized.Cognition just migrated its marketing site from Astro to Next.js. A content site. Astro's home turf, by near-universal consensus, including from people with no stake in the fight. The migration was performed by Devin itself and published as a case study: the agent made the changes, tested them, recorded its own verification runs. No repository, no before-and-after numbers, no benchmark. The output wasn't the site. It was the story.

And believe me, there is no shortage of these stories. Migrations are now the demo genre of the agent industry.Theo Brownewas trying to tell me this a couple weeks back with some very good advice. But it hits a lot harder when you feel it firsthand. Migrations that demo flawlessly are, by definition, the ones moving toward what the agent writes best today. Marketing departments are generating "X → dominant library" verdicts at a rate organic engineering decisions never would.

So you see the tension. Stacks have never been more sensitive to circulating verdicts, and verdicts have never been produced faster or with less reasoning attached.

## What an Argument Looks Like

These aren't unheard of. They are just becoming rarer.

WhenBun moved from Zig to Rust, Jarred Sumner made the case in public, with receipts. He talked about bug classes and memory management issues. You can disagree with the argument.People have, point by point, in public. That's the value. An argument can be engaged, checked, narrowed, refuted, or strengthened. A verdict can only be repeated.

Or look at TanStack's journey with React Server Components on tanstack.com. They spent the year almost arguing with themselves. Whentanstack.com adopted React Server Components, they wrote it up and measured it. When theystopped using them, they did the same: What changed, what replaced it, why the tradeoff flipped for their specific case — while TanStack Start went right on supporting RSC as an opt-in primitive for everyone else. The reversal post calling the decision "uneventful" is a tell. A public reversal on React's flagship architecture, and it generated insight instead of heat. Because they delivered analysis instead of verdict.

That's what evaluation entering the public record looks like. jQuery didn't lose to React because a training set said so. It lost an argument, in public, on merit over several years. Every library you respect got where it is by winning that kind of fight. The flow of events I described earlier doesn't hold fights. It holds direction, and compounds on it.

## The Argument Nobody Published

In all fairness, Cursor never issued a verdict. An experiment that "still needs careful review", thena congratulatory post on the Solid 2.0 RC release. But that post still characterized signals as "perf footguns" and "accidental fan out" — no numbers, nothing to engage — and reached straight for the React Compiler as the cure. No bad faith required. The diagnosis and the cure just came from the same place.

When I tried to reconstruct the case Cursor could have made, it turned out to be interesting. Far more interesting than "perf footguns."

The post obviously highlighted agents were "quite bad at writing good Solid code," everything "ended up being accidentally tracked." While my "Solid-brain" struggles a bit to imagine what they were doing to get there, I don't doubt it for a second. An agent that has internalized React's mental model will write Solid like React, and Solid written like React is bad Solid. I've also seen the reverse. The difference is when the agent fumbles React, the training data catches it. When it fumbles Solid, the training data shrugs. This is a pure numbers game.

Butthe same postcontains a decision in the opposite direction. They're also moving from Tailwind to StyleX. This is a migration against volume. What StyleX offers instead is that agent mistakes get caught. Styles are typed with deterministic merge order, so a hallucinated class is a build error.

Put side by side, one conclusion can be made: make agents' mistakes cheap. Two ways to achieve that. Volume and verification. React (with its compiler) wins on volume and arguably on verification. StyleX loses on volume and wins decisively on verification. I won't pretend under this lens with Solid 1.0 this is a particularly comfortable place for signal-based reactivity. But it's also, not coincidentally, where Solid 2.0's design attention has gone.

That analysis, volume and verification as two axes, is concrete, checkable, and useful. It implies testable claims and gives every framework author a design target. It might also be wrong. I reconstructed it from a benchmark-free post and my own inferences. Cursor's actual reasoning may be entirely different.

The StyleX decision is even more interesting. Agent-driven development can move against volume when verification wins. There is a second angle that small technologies can embrace. To me, this isn't a new revelation, but one where practice confirms theory.

## What Happens If Nothing Changes

If you follow this thinking to its logical conclusion, outside of a few exceptions, each layer collapses on its most popular solution today. Frontend converges on React. Systems converges on Rust. Scripting converges on Python. Even the sites that are just pages converge on Next, fit be damned. That's a monoculture, arrived at not by anyone deciding libraries on their merits, but by a system that can no longer distinguish "abundant in the training data" from "better."

If you are a React fan, you should still be concerned. React was good because it had competition. Hooks arrived in a world where composition patterns were being explored. The React Compiler exists, in part, as an answer to the question signals-based frameworks spent years forcing: Why should the developer pay for re-rendering the world? React's greatest strength has always been its ability to metabolize pressure from outside. A monoculture doesn't just kill the alternatives. It kills the pressure. An ecosystem without pressure doesn't stay good. It stays stuck.

There is a path back. Teams publish analysis, not verdict. Model vendors evaluate what they ship in public. Libraries learn from StyleX's example and bank on verification. And the rest of us learn to distinguish output from argument before we amplify it. The last one we've been struggling with since the dawn of social media.

In the meantime, we can keep generating our rules files, llms.txt, docs over MCP, curated examples. We do all of it for Solid 2.0, and it helps a lot. But context is borrowed, not owned. It has to be injected into every session, by every tool, forever, while the inertia works against you for free.

## Where Does the Next Idea Come From?

I want to leave you with a more probing thought. The question this all comes down to isn't whether Solid survives. We're fine. We are shipping the biggest release in our history, with a community that chose this framework on purpose and, more importantly, knows why.

The question is where the next idea comes from.

Every paradigm that has mattered started as something the establishment couldn't write. React was mocked for almost a year over JSX. Markup in JavaScript? Are you insane? What about separation of concerns? If today's machinery had existed in 2013, models trained on a web that was all jQuery and Backbone, docs canonizing migrations everyone was already making, verdicts circulating months ahead of their arguments, do you think it could have gotten past that stage?

It didn't win because the defaults favored it. It won because people made a verifiable case in public. And I don't think the mechanisms are gone. Migrations have never been cheaper, in every direction. The door out of any monoculture has never been more open. We just need to keep analysis as part of the conversation even as we distance ourselves from the implementation. That's being informed. That's taking responsibility.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse