---
title: LLMs Are Not Deterministic. And Making Them Reliable Is Expensive (In Both the Bad Way and the Good Way) - DEV Community
url: https://dev.to/marcosomma/llms-are-not-deterministic-and-making-them-reliable-is-expensive-in-both-the-bad-way-and-the-good-5bo4
site_name: devto
content_file: devto-llms-are-not-deterministic-and-making-them-reliabl
fetched_at: '2026-02-26T19:22:11.987074'
original_url: https://dev.to/marcosomma/llms-are-not-deterministic-and-making-them-reliable-is-expensive-in-both-the-bad-way-and-the-good-5bo4
author: marcosomma
date: '2026-02-22'
description: 'Let’s start with a statement that should be obvious but still feels controversial: Large Language... Tagged with ai, mcp, programming, llm.'
tags: '#ai, #mcp, #programming, #llm'
---

Let’s start with a statement that should be obvious but still feels controversial: Large Language Models are not deterministic systems. They are probabilistic sequence predictors. Given a context, they sample the next token from a probability distribution. That is their nature. There is no hidden reasoning engine, no symbolic truth layer, no internal notion of correctness.

You can influence their behavior. You can constrain it. You can shape it. But you cannot turn probability into certainty.

Somewhere between keynote stages, funding decks, and product demos, a comforting narrative emerged: models are getting cheaper and smarter, therefore AI will soon become trivial. The logic sounds reasonable. Token prices are dropping. Model quality is improving. Demos look impressive. From the outside, it feels like we are approaching a phase where AI becomes a solved commodity.

From the inside, it feels very different.

There is a massive gap between a good demo and a reliable product. A demo is usually a single prompt and a single model call. It looks magical. It sells. A product cannot live there. The moment you try to ship that architecture to real users, reality shows up fast. The model hallucinates. It partially answers. It ignores constraints. It produces something that sounds fluent but is subtly wrong. And the model has no idea it failed.

This is not a moral flaw. It is a design property.

So engineers do what engineers always do when a component is powerful but unreliable. They build structure around it.

The moment you care about reliability, your architecture stops being “call an LLM” and starts becoming a pipeline. Input is cleaned and normalized. A generation step produces a candidate answer. Another step evaluates that answer. A routing layer decides whether the answer is acceptable or if the system should try again. Sometimes it retries with a modified prompt. Sometimes with a different model. Sometimes with a corrective pass. Only after this loop does something reach the user.

At no point did the LLM become deterministic. What changed is that the system gained control loops.

This distinction matters. We are not converting probability into certainty. We are reducing uncertainty through redundancy and validation. That reduction costs computation. Computation costs money.

This is why quoting token prices in isolation is misleading. A single model call might be cheap. A serious system rarely uses a single call. One user request can trigger several model invocations: generation, evaluation, regeneration, formatting, tool calls, memory lookups. The user experiences “one answer.” The backend executes a small workflow.

Token cost is component cost. Reliable AI is system cost.

Saying “tokens are cheap, therefore AI is cheap” is like saying screws are cheap, therefore airplanes are cheap.

This leads to an uncomfortable but important truth. AI becomes expensive in two very different ways.

If you implement it poorly, it becomes expensive because you burn money and still do not get reliability. You keep tweaking prompts. You keep firefighting. You keep patching symptoms. Nothing stabilizes.

If you implement it well, it becomes expensive because you intentionally pay for control. You pay for evaluators. You pay for retries. You pay for observability. You pay for redundancy. But you get something in return: a system that behaves in a bounded, inspectable, and improvable way.

There is no cheap version of “reliable.”

Another source of confusion comes from mixing up different kinds of expertise. High-profile founders and executives are excellent at describing futures. They talk about where markets are going and what will be possible. That is their role. It is not their role to debug why an evaluator prompt leaks instructions or why a routing threshold oscillates under load. Money success does not imply operational intimacy.

On the ground, building serious AI feels much closer to distributed systems engineering than to science fiction. You worry about data quality. You worry about regressions. You worry about latency and cost per request. You design schemas. You version prompts. You inspect traces. You run benchmarks. You tune thresholds. It is slow, unglamorous, and deeply technical.

LLMs made AI more accessible. They did not make serious AI simpler. They shifted complexity upward into systems.

So when someone says, “Soon we’ll just call an API and everything will work,” what they usually mean is, “Soon an enormous amount of engineering will be hidden behind that API.”

That is fine. That is progress.

But pretending that reliable AI is cheap, trivial, or solved is misleading.

The honest version is this: LLMs are powerful probabilistic components. Turning them into dependable products requires layers of control. Those layers cost money. They also create real value.

Serious AI today is expensive in the bad way if you do not know what you are doing.

Serious AI today is expensive in the good way if you actually want it to work.

And anyone selling “cheap deterministic AI” is selling a story, not a system.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (17 comments)


Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse
