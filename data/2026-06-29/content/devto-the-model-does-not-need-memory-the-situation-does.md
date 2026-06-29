---
title: The Model Does Not Need Memory. The Situation Does. - DEV Community
url: https://dev.to/marcosomma/the-model-does-not-need-memory-the-situation-does-196g
site_name: devto
content_file: devto-the-model-does-not-need-memory-the-situation-does
fetched_at: '2026-06-29T19:36:43.059011'
original_url: https://dev.to/marcosomma/the-model-does-not-need-memory-the-situation-does-196g
author: marcosomma
date: '2026-06-29'
description: 'I think I was asking the wrong question. For a while, the question was simple: does memory make... Tagged with ai, rag, mcp, llm.'
tags: '#ai, #rag, #mcp, #llm'
---

Value of information absent from weights

I think I was asking the wrong question.

For a while, the question was simple: does memory make agents smarter?

It sounds like the right question. It is also a trap, because it assumes that memory should be judged as a generic intelligence booster. You add a memory layer, the agent remembers more things, and somehow the output should become better. More complete. More accurate. More human. More whatever word we are currently using to avoid saying “I hope this expensive thing works.”

After running more experiments, I think that framing is wrong.

Memory does not make the model smarter in any general sense. Most of the time, it cannot. The model already has a massive amount of general procedural and domain knowledge compressed into its weights. If your memory layer recalls information the model already knows, you are not adding intelligence. You are just adding a second path to say the same thing with more latency.

That is the uncomfortable part. A lot of agent memory systems are not failing because recall is broken. They are failing because the recalled information has no marginal value.

They are giving the model something it was already going to do.

## The experiment was not a victory lap

I ran a follow-up benchmark on OrKa Brain: 250 tasks, five tracks, brain versus brainless. The point was to see whether procedural memory would show stronger results at scale and across more task types.

It did not.

The absolute rubric score was almost flat. Brain scored 8.39. Brainless scored 8.27. That is a +0.12 difference on a 10-point scale. Technically positive, but not the kind of result you use to announce that persistent memory has unlocked a new era of agent intelligence unless your relationship with evidence is mostly decorative.

The pairwise result looked slightly better at first. Brain won 53.8% of the comparisons. But then the judge showed a 74.4% first-position bias, which means the raw pairwise score was not something you can read directly. If the judge picks the first answer almost three times out of four, the measurement instrument is not exactly wearing a lab coat. It is flipping a biased coin and writing a confident explanation afterward.

Once I controlled for position, most of the supposed Brain advantage disappeared. Cross-domain transfer did not survive. Anti-pattern avoidance did not survive. Multi-skill composition collapsed into a coin flip. Routing was confounded and needs to be re-run.

Only one track survived: the long same-domain sequence. In that track, the Brain won 74% of the time even when placed in the disfavored position.

That is the part worth keeping.

Not because it proves that memory works in general. It does not. It proves something narrower and more useful: memory seems to help when the output depends on previous state in the same evolving situation.

That is a very different claim.

## The ceiling was the message

At first glance, you could say the Brain failed. I think that is too easy.

The better reading is that the benchmark exposed the wrong class of memory. Most of what OrKa Brain recalled was procedural knowledge: how to decompose a task, how to reason through trade-offs, how to avoid generic mistakes, how to structure a solution, how to transfer a pattern from one domain to another.

The problem is that capable LLMs already know a lot of this. They have seen endless examples of architecture reviews, debugging sessions, migration plans, support flows, project retrospectives, Stack Overflow arguments, incident reports, code reviews, framework docs, and corporate documents that somehow use five pages to say “we forgot the cache.”

So when the memory layer recalls a generic procedure, the model does not suddenly receive missing information. It receives a reminder of something already present in the weights.

That is why the ceiling effect matters. It is not just an implementation failure. It is a category warning. If memory stores general competence, the model can often route around it because the model already has general competence.

This is why “agent memory” can look impressive in demos and then become strangely weak in benchmarks. In a demo, remembered context feels useful because we can see the system referencing the past. In a benchmark, if the remembered thing does not change the answer, the effect disappears into style, verbosity, or judge preference.

The useful question is not “did the system remember something?”

The useful question is “did the remembered thing contain information the model could not have known or safely inferred?”

That is the line.

## Memory is for contingent information

The sharper version of the theory is this:

Memory helps when the answer depends on contingent information absent from the model weights.

Not vertical knowledge. Not domain knowledge. Not “more context” as a generic spell. Contingent information.

By contingent, I mean information whose truth depends on a specific user, system, company, customer, codebase, previous decision, local process, or moment in time. It is information that is not true in general. It is true here.

The model can know how software migrations usually fail. It cannot know that in this codebase, the last migration failed because the billing worker silently depended on a deprecated Redis key.

The model can know what concise writing is. It cannot know that a specific user prefers direct technical answers with no filler, no fake enthusiasm, and no corporate perfume sprayed over the paragraph.

The model can know how customer support triage works. It cannot know that this specific customer always reports billing bugs using the wrong product name.

The model can know how a deployment pipeline usually works. It cannot know that this team avoids Friday releases because one rollback path still depends on a manual script nobody wants to admit exists.

That is memory.

Everything else risks becoming a second copy of generic knowledge attached to a model that already has the first copy.

## Codebase AI makes the distinction obvious

Take software engineering, because the mistake becomes very clear there.

A naive approach says: “We need memory so the model knows how to code.” That sounds reasonable until you look at what the model already knows. A capable model has broad exposure to programming languages, design patterns, API conventions, testing strategies, refactoring techniques, infrastructure patterns, and the usual graveyard of best practices everyone quotes and half the industry ignores.

If you use memory to teach it generic software knowledge, you may hit the same ceiling as procedural memory. The model already knows that functions should be small, tests should cover edge cases, migrations should be reversible, and distributed systems enjoy ruining your afternoon. Storing those ideas as memory does not add much. It mostly gives the model a slower way to say what it was already going to say.

The problem is not that the model does not know software engineering. The problem is that it does not know this software system.

That means generic engineering knowledge should not be treated as the valuable memory layer. It is already in the model. The valuable layer is the local shape of the codebase: naming conventions, architectural scars, forbidden dependencies, deployment constraints, hidden coupling, flaky tests, internal abstractions, legacy decisions, and the reason why one ugly function must not be “cleaned up” unless you enjoy incident reports.

The job of repository retrieval is not to remind the model what clean code is. The job is to show it what this codebase actually is.

The model can know how authentication usually works. It cannot know that in this system, the admin role is duplicated across two services because a migration was only half-completed in 2022.

The model can know that Redis keys should have clear ownership. It cannot know that billing still depends on a deprecated cache key because one worker was never moved to the new event pipeline.

The model can know how to write a database migration. It cannot know that this team avoids destructive migrations unless the rollback plan is reviewed by the person who still remembers why the old schema exists.

That is where memory earns its keep.

A style guide tells the model how code should look. Repository history tells it why the code looks wrong but still works. Incident memory tells it where the bodies are buried. Team conventions tell it what changes will be accepted or rejected before CI even has the chance to complain.

Those are not the same layer, and treating them as one generic RAG pile is how you get a system that retrieves a lot and understands very little.

In software products, this distinction matters. Documentation grounds. Repository state shapes. Incident and decision history constrain.

If those three jobs are mixed together, the assistant may still sound like a senior engineer. It may even sound more senior than before, which usually means it has learned to say “trade-off” with confidence. The question is whether it understands the specific system in front of it.

That is where memory stops being decoration and starts being useful.

## Chat memory is the same pattern

This is not only a codebase problem. Chat memory shows the same structure in a smaller and more familiar form.

When a system remembers that a user wants concise answers, it is not helping because the model lacked the concept of concision. The model knows how to be concise. The useful information is not “what does concise mean?” The useful information is “what does concise mean for this user?”

That is an entity-bound fact. It attaches a general capability to a specific person.

This is why personalization can be useful without being intellectually deep. The value is not in teaching the model a new writing style from scratch. The value is in selecting the right behavior under a known identity.

The same thing happens inside companies. The model knows how to review code, but it does not know that this repository bans a specific library because it caused a production incident three years ago. The model knows how to process refunds, but it does not know that annual partner contracts have a different refund path. The model knows how to summarize a customer complaint, but it does not know that this customer always describes production incidents as “minor issues” because they are polite to the point of self-sabotage.

That local weirdness is not noise. It is the work.

Real systems are not made only of general rules. They are made of exceptions, scars, habits, conventions, previous mistakes, policy shortcuts, undocumented dependencies, and things everyone knows until the one person who knows leaves the company.

That is the material memory should store.

Not generic competence. Operational sediment.

## This changes the architecture

My earlier framing was closer to skill reuse. The agent learns a skill, stores it, recalls it later, and applies it to a new task. It is a clean model. It is also suspiciously diagram-friendly, which should always make us nervous.

The data pushes me toward a different architecture.

A memory system should not start by asking, “What skill is similar to this task?” That can work sometimes, but it is too weak as the central retrieval principle. Similarity is not the same as necessity. A memory can be semantically close and still useless if it does not change the answer.

The better retrieval question is: “What information about this situation would be impossible, unsafe, or expensive for the model to infer?”

That question changes everything.

You retrieve because the task depends on a known entity. You retrieve because the answer varies by product, customer, repository, environment, deployment target, or team convention. You retrieve because the user has stable preferences. You retrieve because the codebase has local rules. You retrieve because the customer has a history. You retrieve because the system has failed before in a way that looks relevant now. You retrieve because the model is about to answer with generic competence where specific state is required.

That is a different trigger from semantic similarity.

The trigger is underdetermination. The model can produce an answer, but the answer is not sufficiently determined by the prompt and general knowledge. It needs local state.

This also means memory should not be one bucket. A serious system probably needs separate stores with separate jobs.

Grounding is for authority. It gives the model exact sources, current docs, repository files, API contracts, schemas, config, and verifiable references.

Operational knowledge is for local shape. It tells the model how this product, repository, customer, workflow, team, or deployment environment behaves.

Episodic memory is for history. It tells the model what happened before with this user, customer, task, session, service, or system.

Reasoning composes the three.

When people collapse all of this into “memory,” they make the system harder to evaluate. They also make it easier to fool themselves, which is apparently the default MLOps workflow whenever agents are involved.

## The next benchmark should be crueler

The old question was whether memory improves output quality. That is too broad.

If the model can answer well using general competence, memory will struggle to show a large effect. A judge may prefer one answer over another, but you will end up measuring style, verbosity, formatting, position bias, or the judge’s breakfast.

The next benchmark should make memory necessary.

A task should require a fact that exists only in memory or grounding. Without that fact, the model should either fail, hedge, or produce a generic answer. With that fact, the model should answer correctly.

Not more beautifully. Correctly.

For a chat assistant, the answer might depend on a stored user preference. For a code assistant, it might depend on a repository-specific rule, a past incident, a banned dependency, a migration constraint, or a team convention that exists nowhere in the model weights. For support automation, it might depend on a customer-specific exception, a product-plan quirk, or a previous escalation pattern. For routing, it might depend on a previous failed path inside the same system.

The score should not be “which answer feels more complete?” That is how judge bias walks into the room, sits at the table, and starts grading vibes.

The score should be concrete. Did the system use the right repository rule? Did it respect the deployment constraint? Did it remember the user preference? Did it avoid the known failure path? Did it cite the current internal document? Did it preserve the prior product decision? Did it distinguish generic knowledge from contingent state?

That is where memory should show a real gap. Not a +0.12 polish gap. A correctness gap.

If memory cannot win there, then the memory system is probably not doing much. If it does win there, then the value is no longer mystical. It is measurable.

## The anti-hype version

I do not think “memory makes agents smarter” is the right claim. It is too vague, and vague claims are where AI hype goes to reproduce.

The sharper claim is less exciting but more useful: memory helps when the task depends on information that is not in the model weights and cannot be safely inferred from general knowledge.

This explains why generic procedural recall barely moved the needle. It explains why long same-domain recall was the only signal that survived. It explains why chat preferences matter. It explains why code assistants need repository state plus decision history, not just more documentation. It explains why enterprise assistants become useful only when they know the local weirdness of the company.

The model already has the average.

Memory is for the deviation.

And most real work is deviation.

That is the part I think we keep missing. We keep building memory systems as if the model is empty and needs to be filled. But the model is not empty. It is full of averages. Full of general patterns. Full of plausible procedures. Full of the kind of answer that is usually right until it meets a real organization, a real customer, a real codebase, or a real human being with preferences that do not fit the median.

Memory is not there to compete with pretraining.

Memory is there to correct the average when the local situation demands it.

## The boundary I would use now

I would draw the boundary like this.

Do not store what the model already knows. Do not retrieve what the model can safely infer. Do not call generic advice memory. Do not confuse domain knowledge with contingent state.

Store the things that change the answer because they are specific, current, local, personal, historical, procedural, repository-bound, customer-bound, product-bound, or system-bound.

Use grounding for authority. Use memory for contingency. Use reasoning for composition.

Mixing those three together is how you build a very expensive autocomplete with a scrapbook attached.

The benchmark did not prove that memory is useless. It proved that memory has to earn its place. If the remembered thing does not change the answer, it is not memory in any meaningful operational sense. It is just noise with a timestamp.

The model does not need memory.

The situation does.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse