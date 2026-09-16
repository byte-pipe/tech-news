---
title: 'My Agents Never Get Tired. I Do: On Satisficing - DEV Community'
url: https://dev.to/earlgreyhot1701d/my-agents-never-get-tired-i-do-on-satisficing-1mb
site_name: devto
content_file: devto-my-agents-never-get-tired-i-do-on-satisficing-dev
fetched_at: '2026-09-16T15:21:45.354061'
original_url: https://dev.to/earlgreyhot1701d/my-agents-never-get-tired-i-do-on-satisficing-1mb
author: Earl Grey
date: '2026-09-11'
description: I approved a prompt on a Tuesday morning and went to make a cup of Irish Afternoon tea. By the time I... Tagged with ai, buildinpublic, agents, discuss.
tags: '#discuss, #ai, #buildinpublic, #agents'
---

The hidden trap of micro-approvals

I approved a prompt on a Tuesday morning and went to make a cup of Irish Afternoon tea. By the time I came back the block was done, tested, and more thorough than what I had asked for. I stood there with the mug and realized I had never decided whether that thoroughness belonged in that block. I had not really decided on the block either.

Sixty-two public repositories since July 2025. Three hackathon wins, two challenge wins, two talks on AI in the public sector, and a weekday job running court operations for the county. Kiro, the agent that writes my code, does not get tired. Neither does Claude, which reviews it. I do, and I keep working through it anyway.

I have not fixed this. I am still in it.

Most of what I see us talk about is speed. Faster down the road, faster through the build, faster into the code. Faster is good. There are only so many hours in a day and we are maintaining, prototyping, and sprinting through all of them. What I have not seen much of is how to set up an ending, or how to decide what deserves a beginning. Have you?

## I tagged a folder throwaway and we shipped it production-grade

Short version, and the long one ishereif you missed it. Block Zero onPorch Light, a civic tool that reads Ventura's public meeting agendas, existed to answer one question. Does the stack deploy. I tagged the folder[THROWAWAY]that morning and budgeted two hours.

It took a build day. By the end there was a byte-identity test protecting a vendored logging module, exact dependency pinning, and a sync script with drift detection, all inside a folder already marked for deletion. Kiro proposed them. Claude reviewed and did not object. I approved them. Each decision was defensible on its own.

What I did not have then was a reason, beyond nobody checking the tag. I had gone into that build determined not to over-engineer, and over-engineered anyway.Mikhail, in the comments, put his finger on why that is worth saying out loud: knowing about a trap is not immunity to it. It is the same reason checklists carry items everybody already knows.

## The reason I stop is the reason they do not

I found the reason in a sports article, which is not where I was looking. I read basketball, almost exclusively. This one I clicked anyway.

Chris Borland quit the NFL at 24 over concerns about brain damage. Inan essay for The Athletiche writes about the decade since, and about trying to be both driven and content. That is where I ran into the word. Satisficing. Not a lowering of standards, he writes, a stop sign at the point of diminishing returns.

The word belongs to Herbert Simon, who built it from satisfy and suffice. Simon won theNobel in economics in 1978for bounded rationality, the idea that people are not decision machines. We cannot take in all the information, weigh it, and produce the optimal choice, because we have limited time, limited information, and limited attention (Simon, 1955).

His strategy for living inside that limit has three steps.

1. Set a standard for what would be good enough.
2. Take the first thing that meets it.
3. Move on.

Step three does the work. Most of the waste is in hunting for an answer only slightly better than the first acceptable one. Note to self here!

Simon also argued that environments shape decisions through problem spaces, the ground your mind has to cross to get from a problem to a solution (Simon, 1956). Some ground is simple and effort pays directly. Need to get stronger, lift weights. Other ground is complicated, and effort alone does not pay. Grinding harder there produces indecision and overload instead of a better outcome.

Here is the part that reframed Block Zero for me. Satisficing is an adaptation to scarcity. We stop because we run out of hours. That is the whole reason the instinct exists.

My agents do not have that scarcity. Kiro will keep hardening a throwaway folder until something stops it, and everything it adds will be locally correct. It is not tired at midnight. It has no sense that the project has a shape or that the shape has an end. The constraint that used to stop the work was mine, and I handed the work to something that does not share it.

And it is not only the building. Claude drafts architecture and documentation. ChatGPT weighs in on what to build with. Gemini makes the visuals. Kiro writes the code. Every stage got faster, including the stage where I decide whether something is worth starting at all. That stage has no test suite, no checkpoint, and no diff to hold a decision against. It is the one I was standing in with the mug.

So the stop sign has to be installed by hand now. Is that a new job, or an old one I was doing without noticing I was doing it? I think it is new, and I would be interested to hear if you read it differently.

## The stop sign goes in the plan, not in my willpower

Two places, because there are two scales.

Per block: a rigor budget.I used that phrase in the Block Zero post without knowing how to build one. Two people in the comments handed me the shape.

Suzanne Chartiersuggested a steering document that defines levels of rigor by whether the work is exploratory, temporary, or production-bound, with the human deciding which level applies.anassBlddescribed the rule his team enforces on spikes: zero abstraction in Phase 0. One flat script, a direct credentials check, one invocation, assert the output, print the receipt, exit. Architecture only after raw execution is proven against reality.

What I am running now is both of those. Every block gets a tier before the prompt goes out, decided by one question. What happens to this code after the block passes? Discarded is spike tier. Kept and built on is working tier. Touched by a user is full tier.

The part that made it enforceable was writing the tiers as prohibitions rather than effort levels. "Spike rigor" is a feeling nobody can check. "No test files, no dependency pinning, no sync scripts, no refactors outside this folder" is a list you can hold against a diff, and so can an agent. The tier goes in the prompt itself, not only in the steering document, next to the "do not refactor other code" line that has been in every prompt for a year.

Some things no tier defers. Outbound rate limiting, because a scraping loop hits somebody's city server on its first run. What logs must never contain, which is how a real leak got into Porch Light through a framework default that printed the model's thinking to stdout. A try/catch on every fetch. Cost and loop bounds. Those are not code quality. They are harm that lands outside my repo before any checkpoint could catch it.

Per project: a wind down block, written on day one.I have not come across this one elsewhere, which may say more about what I read than about what exists. I built it because the rule I had been following was failing.

My standing rule was to shelve a project when the excitement is gone. The problem is that a rule without a mechanism feels identical to quitting. So Porch Light's build plan has Block 7, written before Block 1: what happens on the day after winners are announced, decided in advance rather than in the moment. A monthly dollar ceiling past which it goes dormant on its own. A handoff note to future me covering what it does, what is stubbed and why, and what would make it worth picking back up. A final honest entry in the wins file, including if it does not place.

The mechanism is what turns shelving into a completed step instead of an abandonment. At least that is the theory. Block 7 has not run yet, so ask me in October.

## Sometimes more is right, and the tell is who is on the other end

Block Zero taking a day is why I asked the next question, and I asked it about the whole build. Was this pipeline over-engineered for reading fifteen agendas? Run lock, retry layers, spend ceiling, honest empty states, all for one small city.

My answer was no, and the reason had nothing to do with the code. Tools that watch public meeting agendas already exist. They are sold to lobbyists and government affairs teams, priced for people whose job is watching agendas. The resident who might lose a parking lot has nothing. A flaky civic version of that tool proves the enterprise pricing was correct, that this is hard, that ordinary people should not expect it. A reliable one proves the opposite.

So the reliability work was the argument, not decoration around it. I cannot get to that answer by asking how the code feels. I get there by asking who is on the other end and what a shaky version would prove about them.

## Where this leaves me

Both of those mechanisms stop the work. Neither one decides how much work there should be, and that is the question I am stuck on. My agents do not tire, so all of the tiring happens to me, which makes what I take on my problem alone.

I do not have this solved. I have two mechanisms that work at two scales and a pace I have not decided whether to keep.

What I keep turning over: what should I take on next, and what is the honest reason for taking it. When is the right time to stop something that is still working. Whether this pace is a season or a habit, and whether the difference matters. Whether the answer is to slow down or to reorganize, which are not the same choice.

I would like to know how other people are handling it. Not the productivity answer. The real one. What have you cut, what did it cost you, and what finally told you it was time.

## References

Borland, C. (2026, September 9).I walked away from the NFL at the age of 24. Here's what I've learned since.The Athletic.https://www.nytimes.com/athletic/7574837/2026/09/09/chris-borland-nfl-lessons-retirement/

Cordero, L. (2026).Block Zero: Oh no. Claude, Kiro, and I over-engineered the throwaway.DEV Community.https://dev.to/earlgreyhot1701d/block-zero-oh-no-claude-kiro-and-i-over-engineered-the-throwaway-5d42

Simon, H. A. (1955). A behavioral model of rational choice.The Quarterly Journal of Economics, 69(1), 99–118.https://academic.oup.com/qje/article-abstract/69/1/99/1919737

Simon, H. A. (1956). Rational choice and the structure of the environment.Psychological Review, 63(2), 129–138.https://doi.org/10.1037/h0042769

The Nobel Foundation. (1978).The Sveriges Riksbank Prize in Economic Sciences in Memory of Alfred Nobel 1978.NobelPrize.org.https://www.nobelprize.org/prizes/economic-sciences/1978/summary/

Quick context if you are new here. I work in the California courts, running court operations for the county. I started building with AI in July 2025 and I have been learning in public ever since. I do not write the code. I direct, the agents generate, I validate and decide. I build theClew Suite, a set of civic tech tools for making complex systems easier to inspect. That is the lens I am writing from.

AI Assisted. Human Approved. Powered by NLP.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (27 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse