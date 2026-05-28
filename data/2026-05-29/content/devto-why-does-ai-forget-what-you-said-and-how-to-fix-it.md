---
title: Why does AI forget what you said (and how to fix it) - DEV Community
url: https://dev.to/aws/why-does-ai-forget-what-you-said-and-how-to-fix-it-52f6
site_name: devto
content_file: devto-why-does-ai-forget-what-you-said-and-how-to-fix-it
fetched_at: '2026-05-29T04:36:06.415065'
original_url: https://dev.to/aws/why-does-ai-forget-what-you-said-and-how-to-fix-it-52f6
author: Rohini Gaonkar
date: '2026-05-25'
description: I received following comment on my hallucinations blog post. Comment on Why... Tagged with ai, beginners, aws, tutorial.
tags: '#ai, #beginners, #aws, #tutorial'
---

The desk analogy and markdown state files

I received following comment onmy hallucinations blog post.

Comment on 
Why does AI lie? Hallucinations explained simply

Joske Vermeulen

May 9

Just yesterday I had Opus asking me after every prompt: we have been going for a long time, let me save my context and continue tomorrow 😂

Comment on 
Why does AI lie? Hallucinations explained simply

Joske Vermeulen

May 11

:D I really answered every time, you are a computer, just continue. But it became even worse, so I needed to start a new session :)

The model basically raised its hand and said "hey, we've been at this a while." That's actually the best-case scenario.

A lot of models won't do that. They'll just silently get worse. Same confident tone, less reliable answers. You won't know it's happening until something is clearly wrong.

You paste a long document in, ask about something in the middle, and you get a confident answer that's wrong. Or you have a twenty-message conversation and the model starts contradicting itself.

Not because it's hallucinating. Because it's running out of room.

In theprevious post, we talked about model sizes. Tokens were the unit of cost. Today they become the unit of memory.

## What a context window actually is

Every model has acontext window. That's the total number of tokens it can hold in its head at once. Your input, plus its output, all has to fit inside that window.

Think of it like a desk. A fixed-size desk. Everything the model needs to think about has to be on that desk at the same time. Your question. The document you pasted. The conversation history. The system instructions. All of it.

If you put too much on the desk, things start getting buried. The model doesn't tell you "hey, I can't fit all this." It just works with whatever it can focus on, and quietly loses track of the rest.

How big is the desk? Depends on the model.

Some older models had a context window of 4,000 tokens. That's roughly 3,000 words. About six pages.

Some have 128,000 tokens. That's a short novel.

Some newer models have a million tokens or more. That's multiple novels. Entire codebases.

But here's the thing most people miss. A bigger context window doesn't always mean the model pays equal attention to everything in it. It means more fits on the desk. It doesn't mean the model reads every page with the same care.

## Two shapes of the same problem

Let's see this limit in two ways.

### Documents

You paste twenty pages of text into a model. A legal contract, an insurance policy, internal documentation. You ask a question about something in section 7 of 15. The model might find it, it might miss it or it might pull from the wrong section entirely.

The more text surrounding your target information, the more the model's attention gets diluted. Even if the window isn't full.

### Conversations

This is where most people hit it first, like the commenter above.

By default, the model doesn't have a separate "memory" for your conversation. Some products layer persistence on top (ChatGPT's memory, Claude's projects), but the model underneath still works the same way. Every single time you send a message, the model re-reads the entire conversation from the beginning. Your first message, its first reply, your second message, its second reply, all the way down to whatever you just typed.

That whole transcript gets fed back in every single time. And each exchange adds more tokens to the pile.

A typical question might be 50 tokens. The model's reply might be 300. So one exchange is 350 tokens.

Ten exchanges? 3,500 tokens.Twenty exchanges? 7,000.

If you're asking detailed questions and getting long answers, you can hit 20,000 or 30,000 tokens in an afternoon.

And here's the catch, you're not just using up memory. You're re-sending and re-paying for the entire conversation history every single turn.

Tokens are the unit of memoryandthe unit of cost. Same resource, two consequences.

Models have gotten much better at handling long inputs. You can throw surprisingly large documents at them now. But the limit still exists. And the longer the input, the more likely something gets missed.

## Lost in the middle

Researchers have a name for this. They call it "lost in the middle."

When you give a model a long input, whether that's a document or a conversation history, it tends to pay the most attention to two places: the very beginning, and the very end. The stuff in the middle gets less focus.

It's like reading a long email thread. You remember how it started. You remember the latest message. But that reply from Tuesday at 2pm that's buried fourteen messages deep? Good luck.

This is why things you said early in a conversation drift as the transcript grows. Your early messages end up in the middle of the window and the middle is where attention is weakest.

Most models won't warn you. They'll just give you the same confident tone whether they are working from a clear, focused input or they are drowning in context. The commenter's experience with Opus was the rare exception, not the rule.

## What you can do about it

### Bigger window

Use a model with a bigger window if you're hitting limits. A bigger window is like a bigger backpack. You can carry more. But that doesn't mean you can instantly find what you need. So the rest of these strategies still matter.

### Chunk

Don't paste everything if you don't need everything.

If your question is about section 3, give it section 3. Not the whole document. Less noise, better signal.

### Summarise

Summarise first, then ask.

If you need the model to work with a long document, ask it to summarise the document first. Then ask your real question against the summary. Two calls instead of one, but the second call has focused context. Just make sure the summary didn't leave out something important.

### Position

Put the important stuff at the beginning or the end.

If you're writing a prompt that includes reference material, put your actual question at the very end. Or put the most critical context at the very beginning. Don't bury the important part in the middle.

### Restate

Restate important constraints.If you told the model something critical in message one and you're now on message fifteen, say it again. Costs you a few tokens. Saves you a wrong answer.

### System prompt

Use the system prompt for persistent rules.Most platforms have a place for instructions that consistently guide the model. In ChatGPT or Claude.ai it's called custom instructions. InAmazon Bedrockit's the system prompt field. Put your stable rules there, in clear, unambiguous language. But don't assume they'll be followed perfectly forever. In long conversations, repeating critical instructions in your current message still helps.

### Fresh start

Start fresh when the conversation drifts.If you've been chatting for 20 turns and the topic has shifted three times, start a new conversation. Carry over what matters. Leave behind what doesn't.

### Build your own memory layer

You can summarise older turns into a compact recap, store it somewhere (a database, a file, even a simple variable), and inject that summary at the start of each new call. That's essentially a DIY cache for conversation context. You can build a version tuned to what matters for your use case.

If you're a builder, this should feel familiar. We used to put Redis in front of Postgres so not every request hit the database. Same pattern here. Some platforms offer prompt caching where the system prompt or repeated context gets processed once and reused across calls instead of being re-tokenised every time. You're not re-paying for the same static context on every request. Same instinct, different layer: cache the expensive repeated work, only send the new stuff fresh.

If you want to dig deeper into this, read aboutprompt caching on Amazon Bedrock.

For documents, retrieval is the answer.Instead of stuffing the entire document into the context window, you retrieve just the relevant chunks and pass those in. That's what RAG (Retrieval-Augmented Generation) does, and we'll get to it in the next post.

Same principle for both: give the model less, but give it the right less.

## Key takeaways

If you're just getting started:the model has a memory limit called a context window. It applies to documents and conversations equally. Longer inputs mean thinner attention. If you're pasting something long, ask about specific sections. If you're in a long conversation, restate the important stuff. And if things start feeling off, start a new session.

If you're more on the builder side:context window size is a spec, not a guarantee. A million-token window doesn't mean a million tokens of perfect recall. Put critical information at the edges, not the middle. For conversations, implement summarisation of older turns. And start thinking about retrieval, because that's where this is heading.

## What's next

So the model forgets things when you give it too much. What if there was a way to give it just the right piece, at the right time, from a document you've never even pasted in yourself?

Next post, we're going deeper into retrieval. Giving the model just the right piece at the right time.

Ride along.

This post is part of the "Learning AI Out Loud" series, a cloud architect learning AI from first principles.

Follow along with the series

## Rohini GaonkarFollow

Love to share my experiences on building architectures with best practices, quick tips & tricks, cloud, AI, devops, and more.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (47 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse