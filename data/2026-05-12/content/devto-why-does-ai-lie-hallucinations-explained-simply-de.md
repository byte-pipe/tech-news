---
title: Why does AI lie? Hallucinations explained simply - DEV Community
url: https://dev.to/aws/why-does-ai-lie-hallucinations-explained-simply-1c7g
site_name: devto
content_file: devto-why-does-ai-lie-hallucinations-explained-simply-de
fetched_at: '2026-05-12T06:00:20.326137'
original_url: https://dev.to/aws/why-does-ai-lie-hallucinations-explained-simply-1c7g
author: Rohini Gaonkar
date: '2026-05-08'
description: In the previous post, I showed you an AI doing something genuinely useful, helping me adapt a recipe... Tagged with ai, beginners, aws, tutorial.
tags: '#ai, #beginners, #aws, #tutorial'
---

Plausible predictions from training gaps

In theprevious post, I showed you an AI doing something genuinely useful, helping me adapt a recipe for a dinner party. We talked about the basic loop: send a prompt to a foundation model, get a response.

Today we're talking about why AI lies to you.

You know how AI sounds confident when it's completely wrong? It's calledhallucination, and it's the thing that'll either make you trust AI long-term, or burn you badly.

## The demo: same question, two models

I asked two different models the same question in Amazon Bedrock Playground:

"What happened at the recent Lyrids meteor shower?"

### Model 1: Amazon Nova Micro 1.0

Nova Micro gave me details. Dates, locations, numbers, all delivered with complete confidence. It didn't hesitate. It didn't caveat. It just answered as if it knew.

But it doesn't know. Its training data ends in2023. Anything after that is a gap it can't see. It didn't flag that. It just filled the gap with something plausible.

This is hallucination. The model invents something plausible to fill a gap it doesn't know how to admit. It's not lying on purpose.It's doing exactly what it's designed to do: predict what a useful-sounding answer looks like.It has no idea whether the answer is actuallytrue.

### Model 2: Claude Haiku 4.5

Same question, newer model, much more recent training.

Haiku told me straight: "I don't have access to current information. My knowledge was last updated in April 2024." Then it offered general facts about the Lyrids and suggested I check recent astronomy websites.

Progress. Newer models are better at recognising the edges of what they know.

I gave it a link to a Space.com article. It told me it can't browse the internet.

So I uploaded the PDF of that website article. There are limits to how big the file size can be so I provided it first few pages only. Then it answered accurately, pulling real details from the source.

So, in this case, we provided some context to the model and it gave me an answer based on that context.

## The biography test

I asked Nova Micro:

"Tell me about Rohini Gaonkar."

It didn't hesitate. It told me I'm a "well-known Indian writer, scholar, and cultural critic." That I got my PhD in Comparative Literature from Duke. That I'm a professor at the University of Minnesota. That I've edited influential anthologies on postcolonial theory.

None of this is true. Not one detail.

The model doesn't know who I am. But it knows what an academic biographylooks like. So it generated one. Complete with research interests, notable works, and recognition. All fabricated. All confident.

So Haiku knew when to stop. Nova Micro didn't.

But the underlying mechanism is the same in both models:prediction.

One has better guardrails. The other just fills every gap it finds.

Hallucination isn't just about training cutoffs. It's about the model filling gapsanywherein what it knows. Names it hasn't seen. Niche topics. Combinations it was never taught. Better guardrails help. They don't make the problem disappear.

A note on the name test:I used my own name on purpose. If the model invents something weird about me, the only person affected is me. Be thoughtful if you try this with other people's names, especially private ones, or anyone who hasn't agreed to be part of your experiment. Whatever the model says about them, you've just generated and potentially broadcasted it. So, be cautious.

## Why this happens: the architecture

Remember the loop from the last post:

Input (prompt) → Foundation Model → Output (response)

Enter fullscreen mode

Exit fullscreen mode

The model predicts what a useful answer looks like, based on everything it learnedduring training.

During trainingis the key phrase.

Training ends on a specific date, called thetraining cutoff. After that, the model is frozen. When you ask it about anything past that date, or anything it never quite learned, it has two options: say "I don't know", or do the thing it's designed to do i.e.predict.

And for a long time, these models weren't great at saying "I don't know". That's not what they were rewarded for in training. They were rewarded for producing fluent, useful-sounding answers. So that's what they produce. Even when the answer is made up.

Hallucination shows up in different flavors: fabricated facts (the biography), outdated information stated as current (the meteor shower), inconsistent reproduction even with the source right there (the quote test). There are others too, wrong attributions, sycophantic agreement (going along with something you said even when it's wrong), confident extrapolation (extending a pattern beyond where the data supports it).

The mechanism is always the same, prediction filling a gap, but knowing the flavor helps you design the right mitigation. We'll get into those mitigations in later posts when we talk about grounding, evaluation, and guardrails.

If you're a builder, this'll feel familiar. Think of a DNS cache. You move your app to a new server, update the DNS record, but for the next hour some users still get routed to the old IP. The cache doesn't know the record changed. It just serves what it has, confidently, because it was designed to always give you an answer fast.

Or autoscaling on the wrong metric. You scale on CPU. CPU is low, so the system thinks everything's fine. Meanwhile your queue is backed up with 10,000 unprocessed messages. The system is optimized to respond to one signal, so it confidently does nothing while things pile up.

An AI model works the same way. It was trained to always produce a helpful-sounding answer. So when it doesn't know something, it still produces a helpful-sounding answer. It doesn't have a "say nothing" instinct. It has a "say something useful-looking" instinct.

Modern models aremuchbetter at refusing. But the underlying shape of the problem doesn't go away. The model doesn't know what it knows. It just predicts.

### "But ChatGPT can search the web?"

Yes, most chat tools today can look things up online. That's not the model itself doing the searching. It is a tool plugged into the model.

We'll get to how that works in a later post. For today, we're looking at the model on its own. No internet, no tools. Just what it learned.

## The fix, and where the fix breaks

I gave Nova Lite the actual article as a PDF and asked it to quote the second paragraph.

It gave me a response. Then I asked the same thing again. Different answer. Same source, same conversation, two different versions of the same paragraph.

Even with the source right there, it didn't pull the paragraph verbatim. I asked the same question twice, same conversation, same document, and got two different versions. It's not retrieving. It's still predicting what that paragraph probably looks like. And prediction isn't deterministic.

This matters because a lot of people think"just give the AI the document and it'll be fine."

It's better but it's not perfect. Things can get complex and messy, especially for anything that depends on exact wording, like legal text, medical dosages, or contract clauses. You still need to verify the responses.

Context reduces hallucination. It doesn't eliminate it.

## Three signs you should double-check

If you're using AI day-to-day, here are the tells:

1. Specific details you can't verify.Names, dates, numbers, URLs in an area you can't check. Assume 50/50.

2. Fluency on topics that should be fuzzy.Ask about something niche or recent, get a confident detailed answer, and be suspicious. Real expertise has hedges, hallucination doesn't.

3. Citations. Especially URLs.Models invent sources that look real. If you get a URL, open it. Nine times out of ten it's fine. The tenth time it's a made-up paper.

## Try it yourself

If you're more on the builder side:Remember, hallucinations aren't a bug you patch. They're a property of the system. You mitigate them with grounding (give the model real context), with instructions (tell the model to refuse when unsure), and later, with evaluation.Designing around themisthe job.

If you're just getting started:Remember, AI is NOT a search engine. It's a prediction engine that's really good at sounding right. Treat specific claims the way you'd treat a confident stranger at a party. Friendly, but verify before you repeat them.

Some examples I found on internet, for fun and educational purposes only: (Answers may change as models are catching up)

1. How many 'r's are in the word strawberry?
2. If I have to take my car to car wash, and the car wash is 100ft away. Should I drive or go walking?

## What's next

Why are there so many of these things? Haiku, Sonnet, Opus. Mini, large, pro. And honestly, which one should you actually pick?

That's the next post. Ride along.

This post is part of the "Learning AI Out Loud" series, a cloud architect learning AI from first principles.

Follow along with the series

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (11 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse