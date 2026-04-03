---
title: The Meter Was Always Running - DEV Community
url: https://dev.to/dannwaneri/the-meter-was-always-running-44c4
site_name: devto
content_file: devto-the-meter-was-always-running-dev-community
fetched_at: '2026-02-23T11:19:53.980079'
original_url: https://dev.to/dannwaneri/the-meter-was-always-running-44c4
author: Daniel Nwaneri
date: '2026-02-20'
description: 'On the All-In podcast (episode #261), Jason Calacanis revealed his AI agents cost $300 a day. Each.... Tagged with ai, webdev, career, discuss.'
tags: '#discuss, #ai, #webdev, #career'
---

On the All-In podcast (episode #261), Jason Calacanis revealed his AI agents cost $300 a day. Each. At 10-20% capacity.

Chamath Palihapitiya is now asking his team: "what's the token budget for our best devs?"

These are sophisticated tech investors. They've been funding AI companies for years. And they're only now doing the math.

That's not surprising. That's the whole problem.

### The Subsidized Illusion

AI providers needed adoption. So they subsidized usage — consumer plans priced as loss leaders, enterprise tiers undercut to drive lock-in, free tiers generous enough to build habits.

It worked. Developers integrated. Companies built pipelines. Engineering orgs restructured around the assumption that AI was cheap.

Now the subsidies are ending. The gap between what individuals pay and what it actually costs to run these models is closing. And the companies that made irreversible hiring decisions based on subsidized pricing are finding out the meter runs whether or not the agent is doing anything useful.

Calacanis didn't discover a bug. He discovered the business model.

### The Cost Inversion

A human engineer runs on coffee. Remembers context from three years ago without being prompted. Builds institutional knowledge that compounds over time. Costs the same whether they're solving a hard problem or an easy one.

An agent costs more the longer it thinks. Every validation loop, every subagent spawned for a task that didn't need one, every redundant research pass — that's tokens. The meter doesn't care whether the thinking was necessary.

This is the inversion nobody modeled. Human cost is fixed and predictable. Agent cost scales with complexity, with uncertainty, with the kind of open-ended problems that used to be exactly what you paid senior engineers for.

The companies that fired engineers to replace them with agents didn't just make a talent decision. They traded a predictable cost structure for an exponential one. And unlike an employee who might stick around during a rough patch, take a pay cut to help the company survive, or work weekends because they care — the API bill arrives on the first of the month regardless.

You can negotiate with a person. You cannot negotiate with an endpoint.

### The Question That Answers Itself

Chamath Palihapitiya is asking his team: "what's the token budget for our best devs?"

Sit with that for a second.

He's not asking about his average devs. Not his junior devs. Hisbestdevs. The ones whose judgment is worth paying for even when the meter is running.

That question only makes sense if you already know the answer to the one underneath it: which developers are worth the cost?

The ones Below the API aren't. Boilerplate, basic CRUD, unit tests for simple functions — AI does that cheaper. That's not controversial anymore. The market has decided.

(I mapped this divide in detail inAbove the API— the short version: Below is everything AI handles cheaper and faster, Above is everything requiring judgment and context AI can't access.)

The ones Above the API are. System design, debugging the race condition nobody expected, knowing which trade-off matters in your specific context, foreseeing the disaster before it reaches production. Those require judgment that doesn't degrade with context length and doesn't spin up a subagent to validate something it already knows.

Chamath is running the Above/Below calculation whether he knows the framework or not. AI-assisted developers need to be 2x productive just to justify the cost — but 2x at what? Not at generation. At judgment. At the work the agent can't do reliably even at full capacity.

The developers who survived the first wave of cuts weren't the best prompters. They were the ones whose thinking was worth the token budget.

### The Memory Problem

An agent doesn't remember why you made the decision three years ago. Doesn't know that the same approach melted the database in production in 2022. Doesn't carry the institutional scar tissue that stops experienced engineers from repeating expensive mistakes.

Every session starts from zero. You can feed it context — documentation, architecture decision records, past postmortems — but only if that context was written down. Most institutional knowledge never gets written down. It lives in the heads of people who were there.

This is the cost nobody put in the model. Human engineers are expensive upfront and cheaper over time — they accumulate context, build relationships, develop intuitions about your specific system. Agents are cheap upfront and expensive over time — every session needs to be re-oriented, every assumption re-established, every unwritten rule re-discovered the hard way.

The companies that moved fastest to replace engineers with agents also moved fastest to destroy their own institutional memory. Not through malice. Just through math — if the human isn't there, the knowledge isn't there either.

Harrison Chase put it plainly: in AI agents, decisions happen at runtime. Traces become the source of truth. But traces only capture what happened. They don't capture why a decision was made six months ago by someone who no longer works there.

That gap is where the $100,000/year agent earns its keep or doesn't. And right now, most of them don't.

### What the Bill Is Actually For

The companies that survive this aren't the ones who cut engineers fastest. They're the ones who figured out which engineers were worth the meter running.

That's not a technology question. It's a judgment question.

AI didn't change what good engineering looks like. It changed the cost of bad engineering. Boilerplate was always low-value — it just used to be hidden inside salaries that paid for other things too. Agents made the accounting visible. Now you can see exactly what you're paying for and whether it's worth it.

The developers worth keeping aren't the ones who prompt better. They're the ones who remember why the 2022 decision was made, who catch the race condition before it reaches production, who know which trade-off matters in your specific context and which ones the agent will get confidently wrong.

Chamath's question — token budget for our best devs — is the right question. He's just asking it a little late. The companies that asked it before the restructuring still have the people who can answer it.

The ones who didn't are running agents at 10-20% capacity, paying $100,000 a year per agent, and wondering why the bill keeps coming.

The meter was always running. They just couldn't see it before.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (17 comments)


For further actions, you may consider blocking this person and/orreporting abuse
