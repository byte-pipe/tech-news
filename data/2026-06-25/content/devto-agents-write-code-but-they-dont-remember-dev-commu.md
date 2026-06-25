---
title: Agents write code, but they don't remember - DEV Community
url: https://dev.to/lizziepika/agents-write-code-but-they-dont-remember-4ob0
site_name: devto
content_file: devto-agents-write-code-but-they-dont-remember-dev-commu
fetched_at: '2026-06-25T11:56:05.759434'
original_url: https://dev.to/lizziepika/agents-write-code-but-they-dont-remember-4ob0
author: Lizzie Siegle
date: '2026-06-23'
description: Code generation is solved, but memory isn't. Here's an argument for why the SDLC is inverting with intent becoming the spine and code becoming a layer you drill into, explaining what teams lose every time an agent's reasoning disappears. Tagged with ai, sdlc, llms, agents.
tags: '#ai, #sdlc, #llms, #agents'
---

Intent as the spine of a new SDLC

For twenty years, the software development lifecycle (SDLC) was like a relay race (I love relays--something about the teamwork and team sports!) It involved a team: one person wrote a ticket, another designed, someone built, and another reviewed. Each handoff had its own tool, artifact, and meeting.

With the rise of AI agents, that process has been unevenly compressed.

Addy Osmani makes this point very well inhis write-up of Google's new SDLC paper--worth reading in full, IMO: implementation time drops from weeks to hours, but requirements, architecture, and verification remain slow because they're judgment work.

Generation is pretty much solved and what's left is specification, verification, and the systems that hold them together.

This blog post will go over how those systems keep dropping context.

## The 80% problem is a context problem

Addy calls the ceiling the "80% problem": agents get the first 80% of a feature quickly, and the last 20% (ie edge cases and seams between systems) still needs context the models don't usually have.

I'd phrase it slightly differently. That last 20% is hard not just because the code is hard, but because the reasoning that produced the first 80% is already gone. When an agent builds something, thewhyevaporates when the session ends, leaving developers/builderswith a large diff and a fuzzy memory of what they asked for. Did the agent make the right call on an edge case? Did the plan change halfway through?

Let's say you ask an agent to help you ship a feature. A month later, a teammate gets paged: a big customer is getting throttled. She opens the code and has so many questions that the commit can't answer. The agent that made all those calls (and had a reason for each, because you watched it reason through them and you're a 10x engineer!) is gone, and so is the session.

So she does the only thing she can do: reverse-engineer a decision that was already carefully made, compressing an hour of agent reasoning into a diff that keeps the conclusion and throws away the argument. The agent actually had it right, but none of it survived.

We've gotten very good at generating code, but also very bad at remembering how the code got where it did--leaving the hardest 20% getting done by someone debugging code they didn't write, along with none of the context that produced it.

## Verification needs the trajectory, not just the output

The most useful distinction in Addy's post is between two kinds of evaluation. Output evaluation asks whether the final result is correct. Trajectory evaluation asks whether thepathit took (ie tool calls and reasoning) was sound. You want to have both. An answer that looks correct but skipped its checks is more dangerous than one that's clearly broken.

This is the difference between a box score and game film. The box score tells us the result, whereas the film tells us whether the result was earned or lucky. Most of our developer tooling only keeps the box score. The PR queue we all still use was built for human-speed output including a diff, description, and a thumbs-up. Throwing the path away, it displays the output, and at the same time, agents ship volume. This gives developers two not-so-great options: review every diff and become the bottleneck, or ship blindly and hope.

A diff can't answer the question that really matters:did we build the right thing the right way?That answer lives in the path the agent took--and for most teams at the moment, that lives nowhere.

## Where this goes next

I don't believe that the SDLC will die. I think it will invert.

Today, code is the artifact and intent is a ticket nobody reopens. That will flip with intent becoming the spine and code turning into just one layer you drill into. The unit of work is no longer the PR— it's the whole arc, including the ask, decisions, path, and evidence it works.

That's the bet we're making at Entire. Capture the reasoning chain, attach it to the code in git, and makethatwhat you review, not a wall of diff. It's also how you close the last 20%: not by waiting for a smarter model, but by never losing the context that makes the hard part hard.

The future of building software isn't "agents write code faster." That's already here (41% of new code is AI-generated, per the numbers in the post)--and it's not enough. The future is teams that can understand, continue, and trust the work an agent did, even after the session ended.

The agents sped up. Now it's our turn to give the work a memory.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (32 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse