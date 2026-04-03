---
title: Agency
url: https://www.anantjain.xyz/posts/agency
site_name: tldr
content_file: tldr-agency
fetched_at: '2026-03-25T19:21:53.354500'
original_url: https://www.anantjain.xyz/posts/agency
date: '2026-03-25'
published_date: '2026-03-24'
description: Holding the entire loop in your head and acting on it
tags:
- tldr
---

## Anant Jain

Earlier in my career, I sat in on an interview debrief for a senior product engineer role. The candidate had nine years of experience, three of them at a large public company where he'd owned a significant chunk of their payments infrastructure. His system design was clean. He could talk about distributed systems tradeoffs for hours. The panel gave him strong marks across the board.

Then the "bar raiser" on the panel asked: "Has he ever shipped something from scratch?"

Silence. Nobody could point to a moment in the interview where he'd talked about going from a blank editor to something a user could touch. He'd maintained systems, scaled systems, improved systems. He'd never started one. After a follow-up conversation, the hiring manager decided on passing on him, and I finally understand why it was the right call. The role needed someone who could take a vague idea and turn it into something real in weeks, not someone who could make an existing thing 20% better over a quarter.

I've been thinking about why that decision feels so clear to me, especially in 2026 in the age of AI abundance, and I keep coming back to a single word: agency.

## What I mean by agency

I don't mean "self-starter." That word shows up on every resume and means nothing. I don't mean someone who raises their hand a lot in meetings, either.

Agency is the ability to hold the entire loop in your head and act on it. What does the user actually need? What should this feel like to use? What's the fastest way to build it that isn't embarrassing? How do we know if it worked? A high-agency person can move through that whole sequence without waiting for someone else to hand them the next step.

Most engineers I've worked with in my career are good at a few of those stages. They can build the thing if you tell them what to build. They can architect the system if someone else has already validated the idea. Agency is what you call it when one person can cover the full distance. They can talk to the user, sketch a solution, build a working version, and ship it on Friday with some lightweight instrumentation to see if anyone cares.

This doesn't require being world-class at any single piece. The code doesn't have to be the most beautiful. The design doesn't have to be pixel-perfect. What matters is that the whole thing exists, in a user's hands, and was driven there by one person's judgment. And it was built fast.

## Why I'd take agency over seniority right now

I want to be clear: I'm not saying seniority is bad, or that experienced people lack agency. I think the two are not correlated at all. Plenty of senior engineers are enormously high-agency. The argument I'm making is narrower. For product engineering teams, especially ones doing zero-to-one work, agency should be the primary filter. Seniority should be secondary.

Product engineering is a breadth game. The problems are rarely deep computer science problems. Nobody's asking you to invent a new consensus algorithm or optimize a query planner. The hard part is bringing everything together. Can you hold the user's needs, the design implications, the technical tradeoffs, and the business context in your head at the same time? Can you make a judgment call that accounts for all of them, and then go execute on it?

That's a breadth skill. And breadth correlates more with how many things you've shipped end-to-end than with how many years you've spent writing code.

Seniority used to be a reasonable proxy because building software required years of accumulated knowledge. You needed to know the platform, the frameworks, the deployment options, the failure modes. That knowledge took time to build. Today, a lot of that depth work is being compressed by AI tools. The person who can write a working implementation in a few hours with the help of an LLM, and who knows whether that implementation actually solves the user's problem, is more valuable on a product team than the person who can write the same implementation from scratch but needs a PM to tell them what to build and a designer to tell them what it should look like every time.

This is especially true in the early stages of a product, when you're still figuring out whether you're building the right thing. You don't need deep expertise in the stack. You need someone who can move fast across every part of the problem, learn what's not working, and adjust.

## How to tell if someone is high-agency

I look for one thing above all else: has this person built something where they were the sole reason it exists? I don't mean "contributed to." I don't mean "was on the team." I mean: is there a thing in the world, used by real people, that would not exist if this person hadn't decided it should?

A side project that actual users downloaded. A feature at a previous company that they drove from idea to production with minimal oversight. An open source tool that solved a problem they personally had. The artifact matters more than the story they tell about it.

In interviews, I now pay attention to a few things:

When they describe past work, are they the protagonist or the narrator? There's a difference between "I built a notification system that reduced churn by 15%" and "I was part of the team that worked on notifications." Both might describe the same person, but agency tends to show up in how people frame their own involvement. High-agency people talk about what they decided, what they traded off, what they got wrong. Low-agency people talk about the project as if it happened to them.

I also ask about decisions they made without being asked to. Not "tell me about a time you showed initiative," which is a question that produces rehearsed answers. Something more specific like "tell me about a time you built something that never would have gotten built otherwise." The answer tells you a lot. Some people light up because they do this constantly. Others struggle to find an example, and that's a signal in itself.

## What high agency isn't

I want to draw some boundaries here because "high agency" can easily become a euphemism for "cowboy engineer who ignores everyone and pushes to production whatever they want."

Agency isn't about working alone. The most high-agency people I know are often excellent collaborators. They look at the usage data or talk to customers before they start building. They pull in a designer for a second opinion. They loop in teammates when the scope grows beyond what one person should own. The difference is they don't sit and wait for collaboration to come to them. They initiate it and keep moving.

Agency isn't recklessness. Shipping fast without understanding the problem is actually low-agency behavior. If you skip the "what does the user need" step and go straight to "let me build something," you're not demonstrating ownership of the full loop. You're demonstrating comfort with burning tokens and discomfort with ambiguity.

Agency isn't heroics. Pulling an all-nighter to hit a deadline isn't agency. Making the right decisions and communicating better two weeks earlier so that the all-nighter was never necessary is.

And agency isn't ignoring process. High-agency people aren't allergic to coordination, standups, or planning. They just don't treat the absence of those things as a reason to stop moving. If the process is there, they use it. If the process is bad (more on this later), they update it. If it's not there at all, they get stuff done anyway.

## How to build more of it

I think agency is part disposition and part environment. You can develop it, but you need to put yourself in the right conditions.

The most direct path: take on a project where you are the single point of failure. Where if you don't figure it out, nobody will. Side projects work well for this because there's no safety net. No PM is going to write the spec for your weekend app. No designer is going to hand you mockups. No engineer will code it for you. You have to do everything, and everything you skip becomes a gap the user feels. That experience rewires how you think about work even when you're back in a team environment with all the support structures around you.

At work, volunteer for the scrappy, undefined thing over the well-scoped ticket. The well-scoped ticket will teach you how to execute. The undefined thing will teach you how to figure out how to prioritize and what to execute on. Both skills matter, but most engineers get way more practice at the first one, and the AI agents are getting scarily good at it too.

If you're a manager, your job is to build an environment where agency is possible. Every approval gate you add, every review cycle you require for small changes, every meeting that exists to "align" rather than to decide ("bad process"), is friction against agency. Some of that friction is necessary. A lot of it isn't, and it accumulates until even your most high-agency people slow down to the speed of the lowest common denominator.

Look at how long it takes for someone on your team to go from having an idea to having it in front of a user. If the answer is measured in weeks, something is broken.(Hint: it should be hours. Minutes for small fixes)

## Where this goes next

Agency gets you to the point where you can ship anything. Be able to"just do things". You can move through the full loop, from problem to product, without getting stuck. That's necessary and it's increasingly rare and I think teams should select for it much more aggressively than they currently do.

But agency alone isn't enough. Two equally high-agency engineers can ship two completely different versions of the same product. One will feel right and the other won't. Both products get the job done, but one will have that quality where users immediately understand it, where every interaction feels considered, where the whole thing hangs together. The other will work fine but feel like it was built by committee even if it wasn't.

The difference is taste. And taste, I think, is even harder to talk about than agency. I want to try in a future post.