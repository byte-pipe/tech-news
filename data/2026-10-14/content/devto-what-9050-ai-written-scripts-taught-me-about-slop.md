---
title: What 9,050 AI-Written Scripts Taught Me About Slop - DEV Community
url: https://dev.to/dailycontext/what-9050-ai-written-scripts-taught-me-about-slop-1g5n
site_name: devto
content_file: devto-what-9050-ai-written-scripts-taught-me-about-slop
fetched_at: '2026-10-14T22:04:10.478630'
original_url: https://dev.to/dailycontext/what-9050-ai-written-scripts-taught-me-about-slop-1g5n
author: Louis-Francois Bouchard
date: '2026-10-12'
description: 'You’ve read way too many versions of this paragraph already. Probably even this week: “In today’s... Tagged with ai, llm, aie, openweight.'
tags: '#ai, #llm, #aie, #openweight'
---

AI Engineer Conference Coverage

You’ve read way too many versions of this paragraph already. Probably even this week:

“In today’s fast-paced world, AI isn’t just a tool, it’s a paradigm-shifting tapestry. Let’s delve into this transformative realm, where the real magic happens.”

My team at Towards AI drafts a lot with AI now: videos, courses, books, articles… thousands of them. My team and I use Claude for almost everything, and too often what I have to review sounds exactly like that.

So since June, I’ve been measuring which models can actually write like me. After 9,050 scripts, the surprise is that these “slop words” are quite easy to fix.

## The setup

In June this year, I took ten of my own video scripts, some published and some held back to catch contamination. Four of us spent a month near full-time, about 400 hours, polishing them and turning what makes them work into (as clear and detailed as possible) rubrics.

We then measure whether a model can regenerate something decent, having access to my voice guide, a storytelling guide, output rules, past examples, the brief, and the research.

We then have four LLM judges score every draft against my final version and the rubric: one GPT, one Claude, one open model, and Jev as a recent add-on.

We’ve measured 181 configurations so far, including every thinking level, and plan to measure all upcoming models as well.

But most importantly, here’s what we learned from building this new benchmark, reviewing thousands of generations, and iterating on the rubrics.

## Less slop doesn’t mean better writing

Our top 15 configurations all score above 90 on the slop check, so with a detailed prompt, phrases like the one above are mostly under control.

If you can’t deal with slop anymore, the cleanest of all models we’ve released out of the 181 is GPT-6 Astra at max effort: 94.9.

Still, be careful: this is just one metric we track. Astra currently ranks 62nd because it doesn’t sound like me: 82 on tone and voice, against 90 for Opus. Claude models altogether hold the top 11 spots.

The main thing I learned iterating with both models is that cutting a few Claude-isms is a quick edit. Annoying, but it takes one easy edit pass to fix. Rebuilding a voice is not. It requires a lot of mental effort, restructuring the text, changing examples… which currently makes me stick to Claude for writing.

## Max effort buys very little

Opus 5.5 at max effort is the best writer we’ve measured, at 90.8 out of 100. At xhigh, it scores 90.0 for $0.69 a script instead of $2.75.

That’s 4x the price for a score less than 1% higher. I settle on xhigh and keep max for the rare piece where every sentence matters.

## Cheap models change the unit of work

GLM-5.3 Flash, an open-weight model, scores 88.2 for 1.5 cents a script. Opus 5.5 at max costs nearly 190 times more for a score about 3% higher.

It doesn’t only mean generating similar writing with GLM is almost 200 times cheaper. It means that, used right, you can generate BETTER results than Claude for cheaper with an open model.

We also measured variability between generations. If you generate 10 drafts with GLM and pick the best one, you’ll have extremely similar results to Opus 5.5 and still be 20 times cheaper. If you add a powerful judge with a good rubric and the ability to merge sections from one draft to another to create the best Frankenstein draft possible, it should produce much better results than Opus 5.5 while costing less.

Generating is cheap now. Picking is the challenge. Spend your money on judging and picking, not on generating.

## Every judge has a favorite lab

Compared with the other judges, our GPT judge adds 2.75 points to OpenAI drafts and takes 2.14 off Anthropic’s.

The DeepSeek judge adds about a point to DeepSeek and Kimi.

The Claude judge has the smallest tilt, about half the others’, though it still bumps its own lab and surprisingly likes Google even more.

Jev is pretty neutral, with a small preference for the Gemini models as well, but not being able to justify its reasoning in the ratings seems to make it less consistent for our tasks, maybe because writing is more of a “system 2” type of judging.

No judge is neutral. Use a panel, and never let your writer’s lab be the only scorer.

## The pipeline I’d use for writing with AI

Pick the model that gets you there with the fewest edits without making you mad, not the one that writes the most “amazing” text. Then:

1. Write long, very specific instructions: your voice, your structure, your rules.
2. Show examples of what to do, and examples of what not to do. Name the phrases you hate, and check drafts for them in code instead of trusting the prompt.
3. Add your best past pieces, in full, and ideally details on why they are good.
4. Generate several drafts with a cheap open model.
5. Let a high-thinking judge from another lab pick or merge the best, against a clear rubric.
6. Run one or two review-and-edit rounds with a separate judge. Beyond two, I haven’t seen much help.
7. Keep a human at the end. Even Opus 5.5 drafts need one.

One caveat: this measures my voice on my scripts. It’s one data point, not the truth. Test on your own writing before you switch anything! Building this evaluation pipeline has been so useful that we’ve adapted it for many of our clients’ custom tasks with great results.

I’m releasing the full benchmark, ToneBench, with the methodology behind every number here, in my talk on Tuesday, October 13 (10:40 a.m., Turing room — Evals Track). Come say hi; I’d love to chat and improve the benchmark.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse