---
title: Most 'AI Agents' Are Just If-Statements in a Trench Coat - DEV Community
url: https://dev.to/james_anderson_h/most-ai-agents-are-just-if-statements-in-a-trench-coat-3960
site_name: devto
content_file: devto-most-ai-agents-are-just-if-statements-in-a-trench
fetched_at: '2026-09-08T14:53:52.969049'
original_url: https://dev.to/james_anderson_h/most-ai-agents-are-just-if-statements-in-a-trench-coat-3960
author: James Anderson
date: '2026-09-08'
description: I built an agent last year, and I was proud of it. It had a planner. It had tools. It had a... Tagged with ai, softwareengineering, webdev, agents.
tags: '#ai, #softwareengineering, #webdev, #agents'
---

Production reality checks over demos

I built an agent last year, and I was proud of it.

It had a planner. It had tools. It had a reasoning loop that decided what to do next, reflected on its own output, and chained steps together to get real work done. In the demo, it was genuinely impressive — the kind of thing that makes a room go "ooh."

Then it went to production, and it was slow, expensive, and failed in ways I couldn't reproduce. Same input on Tuesday, different behavior on Wednesday. When it broke, the cause was three "autonomous decisions" upstream that I didn't control and couldn't see.

So I did the unglamorous thing: I rewrote it as a boring, linear pipeline. Fixed steps. No reasoning loop. And it was better on every axis that mattered — faster, cheaper, testable, debuggable.

Then I looked at the logs from the old "agent" and felt slightly sick. It didthe same three steps every single time.Extract, transform, respond. Every run. It never once used its precious autonomy to do anything different. I had built a for-loop, given it a system prompt, and called it an agent.

I don't think I'm alone. I think most of what's being called an "agent" in 2026 is a pipeline in a trench coat — and I want to make the case that this is not an insult. It's a relief.

## What an "agent" actually is (the definition nobody pins down)

"Agent" has become one of those words that means everything and therefore nothing. So let me pin the one distinction that actually matters, because the whole argument rests on it.

An agent decides its own control flow at runtime.Which tool to call, which step comes next, whether to loop again, when to stop — themodelchooses the path, dynamically, based on what it sees.

A pipeline has that control flow fixed by you, at design time.Step one, then step two, then step three. Same path every time. The LLM does workinsidethe steps, but it doesn't get to choose the steps.

That's the entire difference. And here's the part people skip:an LLM doing something smart inside a fixed step is not agency.Extracting fields, classifying a ticket, generating a summary — that's justusing an LLM. It's a smart function call. Agency is specifically when the model is handed the steering wheel and gets to pick the route.

Most "agents" never actually hand over the wheel. They just narrate the fixed route in fluent natural language and call the narration "reasoning."

## The test: can you draw the flowchart in advance?

Here's the one-line litmus that does all the work:

If you can draw the flowchart of what your system doesbeforeit runs, you don't have an agent. You have a pipeline.

Sit with your "agent" for a second. Step 1: it retrieves some context. Step 2: it calls a tool. Step 3: it formats a response. Could you have drawn that on a whiteboard before writing a line of code? Then it's a pipeline. The model isn't deciding the path — you already decided it. The model is just doing the work at each node whilesoundinglike it's deciding.

You only need real agency when the flowchart genuinelycannotbe drawn ahead of time — when the next step depends on discovering something you couldn't have known in advance. That's rare. Most business tasks have a shape you already understand. You know the steps. You're just letting the model improvise them, at great expense, for no benefit.

## Why the costume is expensive

"Fine," you might say, "so it's technically a pipeline. But it works, so who cares?" Here's who cares: everyone who has to run it, pay for it, or debug it at 2 a.m. Pretending a pipeline is an agent has a real bill, and it's itemized.

Nondeterminism.When the model chooses the path, the same input can take different paths on different runs. Great for a demo, miserable in production, because now your bugs don't reproduce. "It worked when I tried it" becomes a permanent state.

Debuggability collapse.When a fixed pipeline breaks, you know exactly which step failed. When an agent breaks, it failed at step 12 because of a decision it made at step 4 that you didn't control and can't easily replay. You're not debugging code anymore; you're doing forensics on a choice.

Multiplied failure surface.Every autonomous decision is another place to go wrong, and the failurescompoundacross steps. A pipeline with five fixed steps has five things to check. An agent that makes five decisions has five decisions each of which can be wrong, in combination, in an order that changes each run.

Cost and latency.A reasoning loop makes many more model calls than a fixed sequence — it thinks, it re-thinks, it reflects, it decides to loop again. You're paying per token to have the model deliberate about a route you already knew.

You can't test it.Regression testing needs a fixed set of paths to test against. An agent, by definition, doesn't have one. So the thing making autonomous decisions in production is also the thing you can't write reliable tests for. Fantastic.

Add it up and the punchline is brutal: you paid all of that — the nondeterminism, the debugging nightmares, the token bill — to let the model decide somethingyou already knew the answer to.

## What you actually wanted was a pipeline

Here's the boring thing that wins.

A pipeline is a fixed sequence of steps, with LLM calls at the specific points where a model genuinely adds value, and deterministic control flow thatyouown. It's reproducible: same input, same path. It's testable: fixed paths mean real regression tests. It's cheap: no reasoning loop burning tokens to re-decide the obvious. It's debuggable: when step 3 fails, you look at step 3.

And here's the thing people miss —the LLM still does all the smart parts.It still extracts, classifies, reasons about content, generates language. You haven't dumbed anything down. You've just stopped letting it improvise thestructureof the work, because the structure was never the part that needed intelligence. The structure was the part you already understood.

Look closely at the "agentic" systems that actually work in production and you'll usually find this: a mostly-fixed pipeline with one or two carefully-constrained decision points, not a free-roaming reasoning loop. The good ones minimized the autonomy to the smallest possible surface. They're pipelines that occasionally, deliberately, ask the model to make one bounded choice — not agents that were trusted to run the whole show.

## When youdoneed a real agent

Now let me argue against myself, because "agents are always bad" would be as dumb as "everything must be an agent." Real agency earns its cost — genuinely — in specific cases:

* The steps truly can't be known in advance.Open-ended research, exploration, debugging an unknown problem — tasks where the path genuinely emerges from what you find. You can't draw that flowchart because the flowchart is the thing being discovered.
* Each step depends on discovering the last.Real multi-hop work: "find the thing, then based on what the thing is, figure out the next thing." If step 2 is genuinely unknowable until step 1 runs, you need something that can decide at runtime.
* Branching is unbounded and real— not "an if-statement with three cases," which is just a pipeline with a switch, but a space of possibilities too large to enumerate ahead of time.

If one of those describes your task, build the agent — you've earned it. And even then, the move is tominimize the agency: hard-code everything you can, and reserve the model's runtime decision-making for the one place that genuinely needs it. Autonomy is a cost. Spend it only where it buys something.

The point was never "agents are bad." It's thatagency is a cost you should have to justify, and most systems calling themselves agents never justified it — they just liked the word.

## Why everyone builds the agent anyway

So if pipelines are cheaper, safer, and more debuggable, why is everyone building agents? Here's the uncomfortable answer:agents are built for the builder, not the task.

An agent demos better. "Watch it reason through the problem autonomously" makes a room lean in; "I wrote a function that calls the model three times" does not. An agentfeelslike real AI, like the future, like the thing you got into this for. And "agentic" is a resume word and a fundraising word — it signals sophistication in a standup and in a pitch deck in a way "deterministic pipeline" never will.

None of those reasons have anything to do with whether your task needs an agent. They're about how the architecture makesyoufeel and look. And that's exactly why the boring pipeline is the senior move — because choosing the less impressive thing that actually works, when the flashier thing would've gotten more claps, is the discipline the hype actively punishes. Nobody screenshots your while-loop. Your while-loop just quietly stays up.

## The takeaway

"Agent" should be the thing youescalate towhen a pipeline provably can't do the job — not the default you reach for because the word sounds advanced.

Start boring. Draw the flowchart. If youcandraw it, build the pipeline — fixed steps, LLM calls where they earn their place, control flow you own. Add real agency only at the specific point where a fixed path demonstrably fails, and no further. The system that ships and stays up in production is almost always more boring than the one that wins the demo.

Most of what's being called an agent right now is a pipeline in a trench coat. And I'll say again what I said at the top: that's not an insult. It's a relief. Because a pipeline is the thing you can actually run, test, afford, and debug — and "impressive in a demo" was never the goal. "Still working on Wednesday" was.

Take the coat off. You'll like what's underneath better.

Two questions, and I want both in the comments. First, the fun one: what did you build as an "agent" that turned out to be a pipeline in disguise? And the real argument — where's the line for you? What's the smallest task where you think a genuine agent actually earns its complexity? I suspect we'll all draw that line in a different place, which is exactly why it's worth arguing about.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse