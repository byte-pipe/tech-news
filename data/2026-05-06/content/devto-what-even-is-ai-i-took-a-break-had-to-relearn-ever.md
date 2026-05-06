---
title: What Even Is AI? (I Took a Break & Had to Relearn Everything) - DEV Community
url: https://dev.to/aws/what-even-is-ai-i-took-a-break-had-to-relearn-everything-3dpj
site_name: devto
content_file: devto-what-even-is-ai-i-took-a-break-had-to-relearn-ever
fetched_at: '2026-05-06T11:30:02.861228'
original_url: https://dev.to/aws/what-even-is-ai-i-took-a-break-had-to-relearn-everything-3dpj
author: Rohini Gaonkar
date: '2026-05-05'
description: I just came back from maternity leave. And honestly? I felt like I'd missed a decade in six months. I... Tagged with ai, beginners, aws, learning.
tags: '#ai, #beginners, #aws, #learning'
---

I just came back from maternity leave. And honestly? I felt like I'd missed a decade in six months. I talked about starting small in my other blogLost in the AI Hype, I Started Small

I've spent the last fifteen years designing cloud systems. And even I felt behind. AI went from a thing people were experimenting with to a thing everyone's apparentlybuildingwith, and I had no idea where to start.

So I did what any architect would do. I went back to first principles.

I'm rebuilding my AI mental model from scratch in public. No math. No expert-level coding. Just real problems, the architecture underneath, and honest notes on where things might break.

If you prefer video, please watchEpisode 1 of my video series. If you prefer reading, you're in the right place.

## The demo: AI adapts a recipe in under a minute

Before any theory, let me show you what these models can actually do.

I openedAmazon BedrockPlayground, pasted a real recipe, and asked three questions with each one pushing the model a little further:

1. Extract and summarise

"What are the core techniques in this recipe, strip off the fluff?"

Clean, fast, useful. You might think: that's a fancy Ctrl+F (search).

2. Interpret and advise

"Looking at this recipe, what's the thing that's most likely to go wrong for someone cooking it for the first time?"

Now we're somewhere a search tool genuinely can't go. The model isreasoningabout the recipe like spotting the bit where people actually mess up.

3. Personalise

"I'm cooking this for six people on Saturday. One is vegan, one is gluten-free. Adapt the recipe, give me a shopping list, and a timeline starting from 4pm."

This is the moment. I asked it something I'd normally spend twenty minutes thinking through. It gave me a starting point in ten seconds.

If you're curious but not technical, that's already useful.

If you're a builder, you're probably already thinking so what happened here.

## So what actually happened?

Here's the architecture, as simply as I can put it.

I sent text called apromptto afoundation model.

People throw around terms like AI, LLMs, and foundation models like they all mean the same thing but they don’t.

AI is the broad umbrella. It includes everything from recommendation engines and fraud detection systems to generative AI tools like ChatGPT.

Foundation models are a subset of AI, they are large models trained on massive datasets that can be adapted for different tasks. These aren’t just text models; they can generate images, video, speech, code, and more. Platforms likeAmazon Bedrockgive access to many of these models.

LLMs (Large Language Models) are a specific type of foundation model built for language tasks like answering questions, summarizing text, writing, or coding. So in my recipe demo, I was technically interacting with an LLM.

The simplest way to think about it:

AI → Foundation Models → LLMs

Enter fullscreen mode

Exit fullscreen mode

So, in our case it means its a big model trained on a huge mix of data for your day to day general purpose.

The model is a piece of software trained on an enormous amount of text: books, articles, code, conversations. It isnotsearching the internet. It learned patterns from all that text beforehand.

When I give it my prompt, itpredicts the most useful responsebased on everything it learned.

Input (prompt) → Foundation Model → Output (response)

Enter fullscreen mode

Exit fullscreen mode

I've been building distributed systems for years, and a foundation model call is simpler than most of the APIs I'm used to. It's an HTTP request with text in, text out.

The complexity isn't in the call itself, it is in what the model learned before you or I ever showed up.

And this exact loop is what the entire current wave of AI is built on.

Every time you see a new Claude, or GPT, or Llama land, what's actually happening is someone trained a bigger or smarter version of this same idea.

Same loop. More data. Better prediction.

## Where it breaks

The model doesn't know if it's right. It's predicting what a useful answerlooks like. Sometimes that prediction is brilliant. Sometimes it invents something that sounds plausible and is completely wrong.

Every time you use one of these tools, ask yourself:what would I need to double-check before I trusted this?

That question is the single most useful habit you can build right now. We'll dig intowhythis happens in the next post.

## Where the models live: Amazon Bedrock

You might've noticed I wasn't using ChatGPT or Claude's own website. I was usingAmazon Bedrock.

Bedrock is where a bunch of foundation models live on AWS. Anthropic's Claude, Meta's Llama, Mistral, Amazon's own models, they are all callable through Bedrock, no need to run or train anything yourself.

The Playground is the easy door in, just type and go. Later in this series, when we start building, we'll call these same models from code. Same models, different door.

## A note on my stack

I work at AWS. So the tools I use in this series are AWS tools like Bedrock for the models, and later, an AI-powered IDE called Kiro for building.

Theconcepts, though, aren't AWS specific. Foundation models, tokens, context windows, RAG, agents, these work the same way on any cloud. I'm showing you my stack. And honestly, I'm still figuring out which parts of it are great and which parts are a pain. You'll know which is which.

## Try it yourself

If you're just getting started:open any AI chat tool (Bedrock Playground, Claude, ChatGPT, whatever you have access to), paste a recipe, a contract, a long email and ask it three questions:

1. One to summarise.
2. One to interpret.
3. One that's personal to you.

See what happens. That's your homework.

If you're more on the builder side:the mental model is simple: text in, model, text out. Everything we build in this series is a variation on that loop.

## What's next

Next up: when AI sounds confident and is completely wrong. Why it happens, how to spot it, how to stop it.

This is a series. I'm learning this in public, building as I go, and being honest when things don't work. If that sounds useful, please follow along.

This post is part of the "Learning AI Out Loud" series, a cloud architect learning AI from first principles.Watch the video versionor follow the series on dev.to.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse