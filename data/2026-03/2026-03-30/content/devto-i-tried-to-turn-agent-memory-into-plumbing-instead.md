---
title: I Tried to Turn Agent Memory Into Plumbing Instead of Philosophy - DEV Community
url: https://dev.to/marcosomma/i-tried-to-turn-agent-memory-into-plumbing-instead-of-philosophy-3a8e
site_name: devto
content_file: devto-i-tried-to-turn-agent-memory-into-plumbing-instead
fetched_at: '2026-03-30T19:26:28.989858'
original_url: https://dev.to/marcosomma/i-tried-to-turn-agent-memory-into-plumbing-instead-of-philosophy-3a8e
author: marcosomma
date: '2026-03-26'
description: There is a special genre of AI idea that sounds brilliant right up until you try to build it. It... Tagged with agents, ai, architecture, softwareengineering.
tags: '#agents, #ai, #architecture, #softwareengineering'
---

There is a special genre of AI idea that sounds brilliant right up until you try to build it. It usually arrives dressed as a grand sentence.

"Agents should learn transferable skills.""Systems should accumulate experience over time.""We need durable adaptive cognition."

Beautiful. Elegant. Deep. Completely useless for about five minutes, until somebody has to decide what Redis key to write, what object to persist, what gets recalled, what counts as success, what decays, and how not to fool themselves with a benchmark made of warm air and wishful thinking.

That is usually the point where the magic dies. Good. I like ideas that survive contact with plumbing. So after thinking for a while about procedural memory and transferable knowledge in agent systems, I did the only thing that matters if you want to know whether an idea is real or just very well moisturized language.I wired the whole thing end to end. Or at least I try so.The question was simple enough to sound harmless.

Can an agent system learn a procedure from one task, persist it, retrieve it later, try to reuse it in a different task, record feedback, and let weak patterns decay instead of growing into a trash heap with a logo?In other words, can you build a procedural memory loop that behaves like a system and not like a TED Talk?

So I built OrKa Brain as a first implementation insideOrKa, a YAML-first agent orchestration framework.

## The Loop

The loop was straightforward on paper. Learn. Persist. Retrieve. Apply. Feedback. Decay. Of course, "straightforward on paper" is the native language of future suffering.

Thelearnstage extracted a structured skill from the execution trace. Thepersiststage stored it in Redis. Therecallstage searched for something structurally relevant. Theapplystage injected that recalled skill back into the solving process. Thefeedbackstage updated confidence. Thedecaystage made sure old and weak patterns did not live forever like some cursed enterprise configuration file from 2017.

That is the kind of sentence people read quickly.Each verb hides a small swamp.

## What Is a Skill, Concretely?

Not in the spiritual sense. In the schema sense.

I ended up with a skill object carrying ordered steps (each with an action, description, parameters, and optionality flag), preconditions and postconditions expressed as testable predicates, a confidence score, a transfer history recording every cross-context attempt, usage count, tags, timestamps, and a TTL computed from actual use.

The TTL formula was designed to reward skills that prove their worth: base of 168 hours (one week), scaled logarithmically by usage and linearly by confidence. A fresh skill with one use and 50% confidence lives for a week. A well-exercised skill used 16 times with 90% confidence survives 49 days. Skills that nobody calls on quietly expire. Redis handles the tombstone.

Enough structure to be useful. Not enough structure to become its own religion.

## The Intentionally Primitive First Version

Was it elegant? Reasonably. Was it semantic? Not really.

The first implementation was intentionally primitive. Rule-based context extraction. Keyword-driven pattern detection across ten task structures and ten cognitive patterns. Jaccard similarity for structural matching. Full scan retrieval no vector index, no embedding-based recall. Deterministic feature extraction.

Basically the cognitive equivalent of saying, "Let us begin with a wrench before we start writing poems about self-improving systems."

This was not because I think keyword matching is the future. It was because I wanted to know whether the loop itself was worth taking seriously before adding semantic frosting and pretending the cake had already been baked.

The scoring system weighted four dimensions: structural similarity at 0.35 (Jaccard over task structures and cognitive patterns, plus shape matching), semantic similarity at 0.25 (keyword overlap in v1, embeddings when available), transfer history at 0.25 (historical success rate of cross-context application), and skill confidence at 0.15.

## The Benchmark

Then came the benchmark. Thirty tasks. Two tracks.

Track Atested cross-domain transfer. Three learning phases, then seven recall phases in structurally similar but semantically different domains. Learn a decomposition procedure from text analysis, then see whether it helps with supply chain planning.

Track Btested same-domain accumulation. Twenty sequential veterinary diagnostic cases, because diagnostics has enough repeated structure to expose whether prior procedures are helping or whether the system is just cosplaying wisdom.

I compared two conditions. The Brain condition ran a six-agent pipeline: reasoner, learn, recall, applier, feedback, result. The Brainless condition ran three agents: reasoner, applier, result. Same model. Same temperature. Same prompts where applicable. All running locally through LM Studio, completely offline. No API calls. No cloud. Just a GPU and Redis.Then I used an LLM judge to score outputs in two ways: independently against a six-dimension rubric (reasoning quality, structural completeness, depth of analysis, actionability, domain adaptability, confidence calibration), and through blind pairwise comparison where the judge saw both outputs side by side without knowing which was which.

## What Happened

This is the part where half the internet would like me to say the system awakened, generalized, and began cultivating its own cognitive farmland while Gregorian chanting played softly in the background.

That did not happen! :(What happened was better. Something real, and smaller.Pairwise comparison:Brain won 63% of head-to-head matchups (19 out of 30). That is not nothing. There was a detectable, consistent preference. The strongest signal was in perceived trustworthiness Brain won 68% of trustworthiness comparisons which is interesting because trustworthiness in LLM systems is often just a more polite word for "this output feels less like it was assembled by a caffeinated raccoon."

Rubric scores:Nearly flat. Overall delta plus 0.10 on a 10-point scale. Reasoning quality showed the largest individual improvement at plus 0.28. Depth of analysis showed exactly zero delta a ceiling effect where neither condition could push further.

That is not breakthrough territory. That is not even "start writing your Nobel acceptance speech in a local markdown file" territory. That is exactly the kind of result I wanted. Not because the gain is impressive, but because the benchmark forced the system to confess what it actually is.

## What the Skills Looked Like

Across 30 tasks, the system created 21 distinct skills after deduplicating 9 that were structurally equivalent. Average confidence settled at 72%. The most popular skill, "Evaluation via Validation," was recalled 9 times and reached 79% confidence. TTLs ranged from 8 to 37 days based on usage.

One detail was revealing: the system never recorded a transfer failure. Every recalled skill, when applied to a new context, was marked as successful. This makes the feedback loop suspect. Either the feedback criteria were too permissive, or the skill-context matching was conservative enough to avoid clear mismatches. Either way, it means the confidence updates were asymmetric skills could only grow, never seriously shrink which is a measurement problem I need to fix.

## The Biggest Finding

The model already knew most of what the Brain was recalling. The system was remembering procedural patterns like decompose, analyse, synthesize. Validate, classify, route. Iterative refinement. All useful patterns. All patterns the underlying model had almost certainly already absorbed during pre-training.

So the Brain was not teaching the model some exotic new craft from the mountains. It was mostly reminding it to behave a little more consistently.

That matters. It also kills a lot of hype.

Because once you see that, you stop fantasizing about "agent memory" as some magical layer that turns a model into a wise little apprentice blacksmith forging general intelligence in your terminal.

Sometimes memory is just structured context with better bookkeeping.And to be clear, that is still useful.Useful is underrated.Useful pays rent while hype writes threads.

## Honest Confounds

The other thing the benchmark made painfully clear is that bad evaluation can flatter almost anything if you let it.

A few things I had to stare at honestly:

Pipeline length.The Brain condition passes through three extra LLM calls. That alone could be enriching context in ways that have nothing to do with skill retrieval. The 15% time overhead (595 seconds vs. 517 seconds for the full benchmark) is cheap, but the extra context injection is a real confound.

Position bias.The pairwise judge preferred the first position 61% of the time, regardless of which condition was placed there. I randomized positions, which mitigates but does not eliminate this.

Single run, single model.I did not run this 50 times and average. The results are from one end-to-end execution. Non-determinism is present but unquantified.

Outlier sensitivity.A catastrophic failure in one condition can pretend to be proof of another. A single badly generated veterinary case could shift aggregate scores in a 30-task benchmark.

If you want to lie to yourself in AI, you are never alone. The tooling is ready to help.

That is why I published the result with the weak parts exposed.

No heroic framing. No fake certainty. No "this changes everything" perfume sprayed over a modest engineering result.

## What I Know Now

Just this:

The loop is buildable.The full learn-persist-retrieve-apply-feedback-decay cycle works end to end. Thirty task procedures deduplicated into 21 skills. Transfer histories are tracked. Skills expire. The plumbing works.

The signal exists.63% pairwise preference is consistent and non-trivial.

The cause of that signal is still ambiguous.It could be genuine procedural transfer, or it could be richer context from extra LLM passes, or some combination.

The current bottleneck is abstraction, not storage.The v1 system stores procedures as structured versions of traces. It does not truly abstract them. It does not generalize them semantically. It does not compress them into domain-independent tactics with actual conceptual teeth. The context analyzer runs on hardcoded keyword dictionaries, not semantic understanding. Retrieval is a full scan, not an index.

That last part matters most.

## What Comes Next

So now the next question is finally the right one.

Not "can we talk beautifully about agent memory?"

We already know the answer to that. Absolutely. People can talk beautifully about almost anything. Especially if nobody asks for logs.

The real question is whether better abstraction and better retrieval change the outcome materially.

If I replace deterministic trace structuring with actual procedural abstraction compressing "decompose input into parts, then analyse each part, then synthesise results" across domains into a generalised decompose-analyse-synthesise tactic and if I replace keyword overlap with embedding-based retrieval or something even smarter, does the loop start doing something that a well-trained model does not already do by default?

That is the threshold.

That is where plumbing starts becoming research instead of respectable mechanical honesty.

And honestly, I prefer it this way.

I would rather publish a first implementation with modest results and sharp limits than one more dramatic post about the dawn of adaptive cognition from someone who has never had to decide what expires, what merges, what fails, and what gets written back after the benchmark finishes.

There is enough incense in AI already.I am more interested in pipes.Because pipes, unlike vibes, occasionally carry water.

OrKa Brain is part ofOrKa, an open-source YAML-first AI agent orchestration framework. The full benchmark, including task definitions, raw results, judge transcripts, and the technical paper, is available in the repository.tech-paper

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
