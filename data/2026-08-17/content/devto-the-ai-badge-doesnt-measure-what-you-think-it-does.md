---
title: The "AI" Badge Doesn't Measure What You Think It Does - DEV Community
url: https://dev.to/pascal_cescato_692b7a8a20/the-ai-badge-doesnt-measure-what-you-think-it-does-3ne9
site_name: devto
content_file: devto-the-ai-badge-doesnt-measure-what-you-think-it-does
fetched_at: '2026-08-17T19:25:57.996113'
original_url: https://dev.to/pascal_cescato_692b7a8a20/the-ai-badge-doesnt-measure-what-you-think-it-does-3ne9
author: Pascal CESCATO
date: '2026-08-15'
description: Anthropic signed the EU AI Act's Code of Practice on Transparency of AI-Generated Content, and... Tagged with ai, llm, writing, discuss.
tags: '#discuss, #ai, #llm, #writing'
---

Proves watermarks track provenance poorly

Anthropic signed the EU AI Act's Code of Practice on Transparency of AI-Generated Content, and started marking text produced by Claude with an invisible statistical watermark. Within days, the same event got read two completely different ways on my feed.

The first reading, on dev.to, is by@sylwia-lask

Separating AI provenance from detection myths

 Sylwia Laskowska
 

 Sylwia Laskowska
 
 
 

Sylwia Laskowska

 Follow
 

Aug 11

## The End of Undetectable AI Text? Claude’s New Watermark Explained

#
news

#
ai

#
llm

138
 reactions

Comments

 91
 comments

 6 min read
 

She actually went and readthe official documentationand reported what Anthropic really says: the watermark doesn't prove a text was entirely AI-generated – you can write something yourself, have Claude correct it or translate it, and it can still carry the mark. The reverse holds too: no watermark detected doesn't prove a human wrote everything.

The second,on Medium, called the announcement a "nuclear bomb" for the AI-generation community, and claimed "you are effectively carrying a digital scarlet letter." No citation of the actual documentation. Just outrage, with the appropriate amount of dramatic punctuation.

Between the two, I left a comment under Sylwia's article. Written in French, translated by ChatGPT, signed off with a question:how do you classify a text thought through, written, and reviewed by a human, but whose final English phrasing came out of a model? It wasn't a rhetorical question. I still don't have an answer.

## Three things people keep conflating

The Medium article mixes together, without ever saying so, three mechanisms that have almost nothing to do with each other.

Anthropic's watermark.A statistical signal baked into the model, documented, which openly acknowledges its own limits: it can disappear after enough editing or translation, and its presence says nothing about who came up with the idea in the first place.

Third-party consumer detectors.ZeroGPT and its relatives. Tools that have existed for years, unrelated to Anthropic, whose reliability has never been seriously demonstrated at scale.

Platform decisions.A badge displayed on Medium, a curation algorithm that penalizes flagged content. These are editorial choices specific to each platform, not a mechanical consequence of the watermark.

The Medium article writes as though the first link automatically triggers the next two: Anthropic marks, so detectors will catch everything, so platforms will punish. The reasoning collapses the moment you separate the links – and for good reason: detecting that a model was involved in producing a text is not the same as determining that the text was "written by AI." That conflation hides a deeper one, which public debate almost systematically ignores.

## Assisted, generated, produced: three different verbs

A textassistedby AI stays under human editorial control from start to finish: the idea, the angle, the structure, and the final decision to publish belong to someone, no matter how many back-and-forths with a model happened along the way to correct, rephrase, translate, or pressure-test a line of reasoning. A textgeneratedby AI comes out of a prompt, without that upstream control – the idea itself came from the human, but the generated text, as it stands, belongs to the model. A textproducedby AI at industrial scale is something else again: an automated publishing pipeline, without anything resembling editorial oversight.

What separates the three, then, isn't how much the model intervened – it's who kept their hand on the decisions.

These three cases carry entirely different editorial responsibility. Treating them as a single category ("AI content") means judging a text on a binary criterion where the reality is a full spectrum of nuance – which is exactly what an undifferentiated "processed by AI" badge does.

## What an actual test shows

I ran an article I wrote in April 2021 – before any consumer-facing LLM existed – throughZeroGPT. A test about a year ago gave it a 97% AI probability. A recent test, on the exact same text, with the exact same tool, gives 8.6%.

Same tool. Same text, down to the punctuation. Two incompatible scores, a year apart.

Digging into the flagged passages in the second test, a pattern emerges. These aren't random sentences: they're consistently the most neutral, most pedagogical, most well-structured passages in the piece – a definition of what a web server is, an explanation of CentOS Stream, a step-by-step automated update procedure. The passages where my voice actually comes through – the self-deprecation, the verbal tics, the Neapolitan moka pot bought at a flea market – are never flagged.

One test doesn't prove what a detection model measures in general. But this one strongly suggests the tool reacts to stylistic neutrality and structural regularity, not to a text's actual origin. Which is precisely the problem: those characteristics existed in human writing long before LLMs did. The detector is chasing a style whose origin is human, using the machine's imitation of it as the reference point. The reasoning eats its own tail.

## How this piece was actually made

Since the whole point of this article is how hard it is to judge a text by its origin rather than its content, it's worth being transparent about how this one was produced.

The starting point wasn't this article: it was a comment under a Medium post that annoyed me enough to reply. From there, several hours of back-and-forth with Claude – not to have it write for me, but to pressure-test angles, check numbers, and go dig up original sources instead of relying on my own fuzzy memory. The ZeroGPT test wasn't improvised for the article, either: I reran it to verify what I was recalling from memory, and the result changed the conclusion I was about to draw.

First draft written in French – the language I actually think in. Several rounds of review, cross-checked across a few different AI models – ChatGPT, Kimi, Grok, Mistral – to catch inconsistencies and spots where the argument went soft. I then read and corrected it myself, outside of Claude (I use NotepadMD), because I never let a text out the door without going through it line by line. Translation into English after that, then a review of that translation, because a lexically faithful translation can still betray the tone if nobody checks it.

By the end of this process, the text probably carries a watermark. It also took up several hours of research, verification, and both automated and human review – and my own review isn't the least of it: after every rewrite, and again at the end of the process. Both facts are true at the same time, and no detector will ever be able to tell them apart.

## What a badge actually costs

Everything above is a technical demonstration. It says nothing about what happens once the text is published, and that might be the more important part.

A "processed by AI" badge, applied without distinguishing assisted, generated, and produced, puts an author who spent hours thinking, checking, and writing in the same bucket as a content farm publishing a hundred articles a day with no human oversight. A rushed reader doesn't see the nuance – they see the badge, and file the thinking author under "cheater." That's a real loss for someone who never cheated: their work gets judged on a signal that measures neither the effort nor the actual editorial control behind it, only whether a tool showed up somewhere in the chain.

And that loss has an absurd mirror image. The same readers who reject an article marked "AI" accept, without blinking, the AI-generated summary sitting at the top of their Google search results – without reading it critically, without checking the sources it pulled from, and most often without ever clicking through to the original article. Independent studies converge on this: when an AI summary appears in a Google search, clicks to third-party sites drop by half, sometimes more, depending on methodology. In other words, the reader who calls an article "AI slop" over a badge probably let an AI summarize ten other topics for them that same week, without ever checking what it kept or what it distorted. AI isn't rejected on principle. It's rejected when it's visible and claimed, and accepted when it's invisible and imposed by default.

This shift from click to summary is also a broader loss of reading, independent of any badge: a full article, nuanced, sometimes contradictory, replaced by three smoothed-over lines nobody ever questions. The reader loses the friction that would have forced them to evaluate a source, a line of reasoning, a style – exactly what the badge claims to let people judge, and what the summary skips without any debate at all.

## What this doesn't fix

None of this will stop an "AI slop" comment under this piece. I've never gotten one on dev.to. On Reddit, I have.

But look at who tends to write that kind of comment. Rarely people genuinely engaging with the topic. Often people chasing the buzz of a word that lands. On Reddit, the accounts behind these comments often show a broader pattern of reflexive, repeated downvoting across unrelated posts – a signal of rejection that has little to do with the content actually in front of them.

The technical demonstration and the social judgment are two different things, and the second doesn't get talked out of itself by the first. "AI slop" has stopped being a judgment about a text at all: it's become a blunt, reflexive rejection signal people display, regardless of whether they read anything.

If the badge doesn't measure origin, and social judgment doesn't care about the measurement, maybe the question worth asking isn't "who wrote this" but "who thought this through."

The nuance matters here. In the process I just described, the initiative never changed hands: I'm the one who opens the session, sets the topic, decides whether an angle holds up or needs to be dropped. A model doesn't come looking for me with an idea I didn't already have. And if it writes a paragraph I didn't ask for, it goes in the trash – which is perfectly observable in what I keep and what I discard from one session to the next.

Who thought through the initial disagreement with the Medium piece, and chose to separate watermark, detector, and platform instead of treating them as one thing? Who decided a test was worth more than an opinion, and reran it twice instead of republishing a fuzzy memory?

Those are questions I can answer, text by text, decision by decision. No detector asks them. It looks at the final shape and infers an origin from it – when the origin was never in the shape. It was in the chain of decisions that came before it.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (51 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse