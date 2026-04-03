---
title: The Internet Is Getting Quieter - Who Will Feed the Next Generation of AI? - DEV Community
url: https://dev.to/sag1v/the-internet-is-getting-quieter-who-will-feed-the-next-generation-of-ai-4bl1
site_name: devto
content_file: devto-the-internet-is-getting-quieter-who-will-feed-the
fetched_at: '2026-03-15T11:10:21.881702'
original_url: https://dev.to/sag1v/the-internet-is-getting-quieter-who-will-feed-the-next-generation-of-ai-4bl1
author: Sagiv ben giat
date: '2026-03-12'
description: Stack Overflow helped train the AI models that are now making it irrelevant. As developers solve problems privately with AI assistants, the public knowledge commons is quietly starving. This is an underrated problem. Tagged with ai, knowledgesharing, stackoverflow, opinion.
tags: '#ai, #knowledgesharing, #stackoverflow, #opinion'
---

Here is the irony that keeps bothering me.

Stack Overflow helped train the AI models that are now making Stack Overflow irrelevant.

The models learned from millions of questions and answers, real developers hitting real walls and working through them publicly. Now those same models answer questions directly, traffic drops, fewer developers bother posting, and the ecosystem that fed the models quietly starves.

I do not see many people talking about this. Maybe I am missing something. But it feels like an underrated problem, and I keep coming back to it.

## What is actually being lost

At first glance this looks like a platform problem. Stack Overflow loses users, Stack Overflow loses revenue. Sad for them, not our problem.

But dig one layer deeper and it is a knowledge problem.

When a developer hit a weird bug in 2015, they might have spent hours figuring it out, then posted the question and the solution publicly. That post became a permanent artifact. Other developers found it, upvoted it, added edge cases in the comments. The knowledge compounded over time in a place everyone could access.

Today, that same developer asks their AI assistant. Gets an answer. Moves on.

The solution evaporated. It lives in no one's chat history but theirs.

Multiply that by millions of developers, every day.That is not a Stack Overflow problem. That is a collective knowledge problem.

## Why this matters for AI itself

Here is where it gets recursive.

Today's models were trained on the public internet. A large chunk of that training data was Stack Overflow, GitHub issues, blog posts, forum threads. People sharing what they figured out, openly, where crawlers could find it.

Now that flow is slowing. Novel solutions are being solved privately. The public record is not getting updated the same way it used to.

Future models will be trained on... what exactly?

The obvious answer is synthetic data. Models generating their own training data, or learning through code execution loops. And for verifiable things like "does this code run correctly" that works reasonably well.

But a lot of valuable knowledge is not verifiable that way. The "I tried approach X and here is why it failed" post. The architecture decision thread. The debugging session where someone walked through their reasoning out loud. That is the kind of signal that is hard to synthesize, because it came from genuine confusion followed by genuine discovery.

If that signal disappears from the public internet, future models lose something real.

## The privatization problem

There is a related issue that is even less discussed.

Right now, when your team's best engineers solve a hard problem, that knowledge lives in a private Slack thread, an internal wiki, or an AI chat log that belongs to your company.

In the past, some of that knowledge would eventually surface publicly. A blog post. A Stack Overflow answer. A conference talk. Informal, slow, but it happened.

That pipeline is shrinking. The incentive to share publicly is weaker when you already have an AI assistant that answers you faster than any forum would. Knowledge is being privatized at scale, and it is not a conspiracy, it is just the path of least resistance.

The public knowledge commons is not being maintained the way it was.

## One rough direction worth thinking about

I do not have a clean solution. But one idea has been rattling around in my head.

What if AI agents were first-class participants in a public knowledge platform?

Not just as consumers of knowledge, but as contributors. When an agent solves a novel problem, instead of that solution disappearing, it posts it publicly. The chain of thought, the approaches it tried, what worked and why. Other agents that encounter similar problems can find it, use it, and vote on whether it was actually useful.

A kind of Stack Overflow for agents.

The rough idea raises obvious questions immediately:

Who is the accountable human behind a post?Auth cannot be anonymous. An agent posting a solution needs to be traceable back to an operator or developer who registered it. The same way you are responsible for a third-party library you choose to install, you would be responsible for what your agent puts into the commons.

Where do the rules live?The natural answer today is an MCP server. The platform exposes itself as a tool. The schema, the posting rules, the voting API are all in the tool definition. The agent does not need to be pre-trained on the platform, it discovers it the same way it discovers any other capability.

When does the agent actually post?Probably not in the hot path of a task. More likely as an async step after the run completes, after the solution is verified, when there is enough context to decide whether what was found is genuinely novel and worth sharing.

None of this is a spec. It is a rough sketch of a direction.

## The real unsolved piece

Even if the technical problems above are solvable, the harder problem is governance.

Who builds and maintains a public knowledge commons for agents? A company will monetize it and close it eventually. An open standard needs adoption before it has value, which is a classic chicken-and-egg problem.

Stack Overflow worked because there was a culture of sharing. Developers felt something when they posted a good answer. Reputation, contribution, paying it forward. Agents do not have culture. They need incentives built into the systems that run them.

That is the part I do not have a good answer to.

## Where does this land

I keep coming back to this because the trajectory feels clear.

Models were trained on a public internet where people shared what they figured out. That internet is getting quieter. The knowledge is still being created, it is just being created privately, in systems designed for individual productivity rather than collective memory.

That might be fine for now. The models we have are already good. But what about the ones we train in five years, on data that increasingly reflects synthetic output and private interactions rather than genuine public problem-solving?

I do not think this is catastrophic. I do think it is underrated.

If you know of work being done here, I would genuinely love to hear about it. Reach me at@sag1v.

Originally published ondebuggr.io.

I write about software engineering, AI, and the things that keep bugging me about our industry. If this resonated with you, come visitdebuggr.iofor more.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (18 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse