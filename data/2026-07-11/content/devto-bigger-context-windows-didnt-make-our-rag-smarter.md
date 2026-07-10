---
title: Bigger Context Windows Didn't Make Our RAG Smarter - DEV Community
url: https://dev.to/valerykot/bigger-context-windows-didnt-make-our-rag-smarter-4d0l
site_name: devto
content_file: devto-bigger-context-windows-didnt-make-our-rag-smarter
fetched_at: '2026-07-11T01:37:05.994731'
original_url: https://dev.to/valerykot/bigger-context-windows-didnt-make-our-rag-smarter-4d0l
author: ValeryKot
date: '2026-07-08'
description: We stopped measuring retrieval quality by how many tokens we could fit into the prompt. When... Tagged with ai, llm, machinelearning, rag.
tags: '#ai, #llm, #machinelearning, #rag'
---

Keyword density vs original decision logic

We stopped measuring retrieval quality by how many tokens we could fit into the prompt.

When long-context models became available, many of us made the same assumption.

If an LLM can read 128K tokens, retrieval suddenly feels less important. Why spend time carefully selecting documents if the model can simply read everything?

It sounds reasonable.

In practice, it wasn't.

## More context, worse answers

Imagine asking your internal assistant:

Why did we abandon microservices?

Retrieval returns thirty documents.

* an architecture decision record
* a few Jira tickets
* Slack discussions
* meeting notes
* a glossary page

Everything is related.

Almost nothing answers the question.

The actual decision lives in a single ADR written months earlier. It explains the trade-offs: team size, latency, deployment complexity, operational cost.

But that document isn't especially similar to the query. It doesn't repeat the same vocabulary. It doesn't even mention "microservices" very often.

So it gets buried.

The model now receives thirty relevant documents and does what language models are very good at: it produces a coherent explanation.

The problem is that coherence is not the same thing as faithfulness.

Instead of recovering the original decision, it often synthesizes one from recurring themes across the retrieved documents.

The answer sounds plausible.

It just isn't the answer that was originally made.

## Bigger windows don't fix retrieval

Research has already shown that models struggle with information buried inside very long contexts. TheLost in the Middlepaper is probably the best-known example.

Our experience suggested something slightly different.

Sometimes the answer isn't lost because the context is long.

It's lost because the retrieval stage couldn't distinguishthe document that contains the decisionfromdocuments that merely discuss the same topic.

Adding more context doesn't necessarily solve that problem.

Sometimes it simply gives the model more material to average together.

## We were optimizing the wrong thing

For a while we treated retrieval as a packing exercise.

How many useful chunks can we fit into the prompt?

Over time the question changed.

Why is this document here?

Should it be here at all?

Does it explain the decision, or does it merely mention the same technology?

Those questions turned out to matter much more than the size of the context window.

## Retrieval is a selection problem

The biggest shift wasn't moving from 8K to 128K tokens.

It was realizing that retrieval isn't about fitting more information into a prompt.

It's about selecting the few pieces of information that actually explain the answer.

Large context windows are incredibly useful.

They just don't compensate for weak retrieval.

If anything, they make weak retrieval look convincing.

Next time I'll look at another assumption I no longer believe: that documents should be treated as bags of chunks.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (23 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse