---
title: The End of Undetectable AI Text? Claude’s New Watermark Explained - DEV Community
url: https://dev.to/sylwia-lask/the-end-of-undetectable-ai-text-claudes-new-watermark-explained-45g2
site_name: devto
content_file: devto-the-end-of-undetectable-ai-text-claudes-new-waterm
fetched_at: '2026-08-14T19:48:44.420464'
original_url: https://dev.to/sylwia-lask/the-end-of-undetectable-ai-text-claudes-new-watermark-explained-45g2
author: Sylwia Laskowska
date: '2026-08-11'
description: For the past few hours, the whole world,&nbsp; or at least my LinkedIn feed,&nbsp;has been talking... Tagged with ai, llm, news.
tags: '#news, #ai, #llm'
---

Separating AI provenance from detection myths

For the past few hours, the whole world,  or at least my LinkedIn feed, has been talking about one thing: Anthropic signed theEU AI Act’s Code of Practice on Transparency of AI-Generated Content.

Is this the end of generating funny cat stories, LinkedIn posts, and boring docs? Are we doomed? Will we have to write all those boring things manually, like animals, because otherwise some mysterious detector will expose us? 😅

I just couldn't resist writing about this! The internet has already managed to produce a surprising number of myths around the topic, so let's quickly go through what we actually know for sure, which, by the way, is pretty easy to find on Claude's official pages, where the documentation is more pleasant to read than many industry articles.

And as you'll see, there's really not that much to be afraid of. Also... Anthropic isn't even the first company to do this.

## Wait, Why Do We Even Need This Law? Did AI-Generated Text Become Illegal in Europe?

Of course not!

If you're an EU citizen like me, you can still ask an AI to write a reply to a boring email or generate a ridiculous poem, and you won't go to jail for it. 😉

The goal isn't to ban AI. It's about making AI-generated and manipulated content machine-detectable and, in specific contexts, transparent to users — especially when we're talking about things like deepfakes or content concerning matters of public interest.

And there is an important nuance here: the AI Act also provides an exception for certain AI-generated or manipulated text where the content has undergone human review or editorial control and a natural or legal person holds editorial responsibility for its publication.

So no, the EU has not declared war on your ChatGPT-generated emails.

## What Do We Actually Know So Far?

Here's what we know for sure today:

* Anthropic really did sign theEU AI Act Article 50(2) Code of Practice on Transparency of AI-Generated Content, and as part of its implementation, it is providing machine-readable marking. The relevant transparency obligations started applying on August 2, 2026. So yes, we're already there.
* Claude models released on or after August 2 have marking capabilities from launch. Older models don't necessarily have them yet; Anthropic is rolling this out gradually.
* The system works globally. Yes, even outside the EU.
* It applies to supported Claude models used throughClaude, the Claude Platform/API, Claude Code, Claude Cowork, and Claude Tag.
* Using Claude through AWS, Google Cloud, Microsoft Foundry, or another supported platform? The marking is applied at the model level, so using another interface doesn't magically make it disappear.
* There are two different mechanisms involved: an imperceptible watermark for generated text and provenance metadata for supported files.

## So... How Does This Watermark Actually Work?

Anthropic calls it an"imperceptible watermark" embedded directly into the text.

According to Anthropic, it survives copy-paste and can even survive some amount of editing. It's implemented at the model level rather than being something the Claude frontend simply adds afterward.

But here's the important part:Anthropic still hasn't told us exactly how it works!

The company says more technical documentation is coming, so... expect a follow-up from me when it arrives. 😀

We can make an educated guess that it might be some form ofstatistical token watermarking. In such systems, we're not talking about weird spaces or invisible Unicode characters that could be removed in a second. Instead, the model can slightly and statistically prefer certain tokens during generation.

In a single sentence, that kind of signal might be impossible or unreliable to detect. Across a longer piece of text, however, statistics can start revealing the pattern.

So, very roughly, you could imagine something like this (if Anthropic has implemented its watermark this way):

Normal generation

P(next_token | context)

Enter fullscreen mode

Exit fullscreen mode

vs.

Watermarked generation

P(next_token | context) + secret statistical bias

Enter fullscreen mode

Exit fullscreen mode

But again:Anthropic has NOT confirmed yet that this is how Claude's watermark works.

This is simply an educated guess based on existing text-watermarking techniques. 🙂

## Is Claude the Only Model Watermarking Text?

Nope!

Google has actually been doing this for years.

Google DeepMind introducedSynthID Textback in 2024, and it works along the general lines I described above: the watermark is introduced during token generation, creating a statistical signal that can later be detected.

OpenAI, meanwhile, has said that it has developed text-watermarking technology, although while it already uses provenance or watermarking technologies for things like images, video, and audio, it has not publicly rolled out comparable watermarking for ordinary GPT text responses.

So Anthropic definitely didn't invent the idea of watermarking LLM output.

## Will Everyone Have Access to a Watermark Detector?

We don't really know yet.

For supported files, the situation is somewhat simpler because Anthropic uses provenance metadata, such as C2PA credentials, that can be inspected with appropriate verification tools.

Text is more interesting.

Anthropic says it plans to make watermark detection available tothird parties and researchers, but we don't yet know exactly who those third parties will be, what access will look like, or whether regular users will eventually get a simple public detector.

So GPTZero and similar garbage may still have a job for a while.

## What Does This Actually Mean for Us?

Will everything finally become crystal clear? Will every LLM-generated article suddenly get a giant redCHEATER!warning next to it? xD Of course not!

Anthropic itself openly talks about the limitations of this technology. And we've discussed variations of this problem thousands of times here on DEV already.

First of all, the presence of a watermark doesnotnecessarily mean that the author didn't write the text themselves.

Maybe they wrote the entire thing and then asked Claude to edit it, fix grammar mistakes, polish the wording, or translate it into another language. The resulting output could contain a watermark even though the actual ideas, and potentially most of the original text, came from the human author.

So yes, the final article could still be chaotic, unnecessarily long, and full of a million digressions, exactly like my posts here.

Anthropic explicitly points out that the opposite can happen too.

Someone can take fully AI-generated slop and heavily edit it, paraphrase it, translate it, mix it with other content, or otherwise transform it enough that the watermark may no longer be detectable.

So:

watermark detected ≠ AI wrote everything

and

no watermark detected ≠ human wrote everything

That's a pretty important distinction.

## What About Images, Audio, and Video?

With supported files, provenance can be easier to verify because we can use embedded metadata and content credentials. But even that isn't bulletproof.

What happens if someone takes a screenshot of an AI-generated image, for example Metadata doesn't magically survive every possible transformation.

And that's exactly why provenance is useful evidence, but not some perfect universal AI detector.

## And What the Hell Happens With Code?

This is probably the part I'm most curious about. How exactly are they planning to handle watermarking in generated code, where the model has significantly less freedom in choosing equivalent tokens?

In natural language, there can be dozens of perfectly valid ways to express essentially the same thought. But if we have something like:

const
 
result
 
=
 
await
 
fetchData
();

Enter fullscreen mode

Exit fullscreen mode

then how the hell do we add a statistical watermark to that?

Sure, there are still choices: variable names, formatting, and so on. But the space of valid substitutions is obviously much more constrained than it is in natural language, and formatters, refactoring, minification, or even small manual edits could make the problem even more interesting.

Claude Code is included in Anthropic's marking rollout, but Anthropic hasn't yet published enough technical detail for us to know exactly how the text watermark behaves with generated source code.

And I really want to know how they solved this one.

## So, Should You Care?

As you can see, Claude watermarking generated text is actually a logical and important, although obviously still imperfec, move.

It probably won't change our everyday lives very much.

Sure, the flood of AI slop across social media is annoying. Unfortunately, I have a feeling this watermark isn't going to magically solve that problem either. 😐

What interests me much more ishow this watermark is actually implemented.

Anthropic, I'm waiting for the docs!

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (38 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse