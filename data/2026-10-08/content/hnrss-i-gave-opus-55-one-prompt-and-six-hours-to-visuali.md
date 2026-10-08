---
title: I gave Opus 5.5 one prompt and six hours to visualize Invisible Cities - Quesma Blog
url: https://quesma.com/blog/invisible-cities-one-shot/
site_name: hnrss
content_file: hnrss-i-gave-opus-55-one-prompt-and-six-hours-to-visuali
fetched_at: '2026-10-08T17:45:12.664214'
original_url: https://quesma.com/blog/invisible-cities-one-shot/
author: Piotr Migdał
date: '2026-10-08'
published_date: '2026-10-07T09:26:43.000Z'
description: 'Claude Opus 5.5 vs GPT-6 Astra one-shot Invisible Cities by Italo Calvino in Three.js: AI design, UX, data visualization and explorable explanations.'
tags:
- hackernews
- hnrss
---

GPT-6 Astra wasa jump when it comes to puzzles.
Claude Opus 5.5 is a jump when it comes to design.

## Vibe designing

Even local models can makea competent landing page for a shop. Doing interactive visualization is a different tier. Since I am into creatingdata visualizationsandexplorable explanations, LLMs were both a blessing and a curse.

The Tree of ‘tree’, on Proto-Indo-European etymology, with Claude Opus 4.8. The
first draft was surprisingly good, but then came a lot of frustration: removing AI slop and fixing visual overlaps.

Genetic Distance Mapwith Claude Fable 5.1, which worked well with data
analysis and implementation, but needed a bit of hand-holding to make the design good.

Then for a moment I was happy-ish with GPT-6 Astra. My subjective experience was that it is a bit better than Fable 5.1 at a general overview, following intentions behind prompts, and checking that it all works correctly.

Then there was the Opus 5.5 moment for AI-assisted design. I saw an optical explorable explanation:

“I asked Opus 5.5 to explain camera focus by building an interactive lens lab. Here’s what it came up with after 1
hour 26 minutes in one shot, $25.66 API cost.” –Ryan Sael on X,interactive

One may argue that it is still “too rich”, and has no sense of minimalism. But still, wow!
I was still in disbelief. Was this really its consistent quality for a one-shot experiment?

Instead ofmy beloved optics, I went for something different.

## Invisible Cities

What’s a good prompt? Well, I went with the beautiful urbanistic poetry ofInvisible Citiesby Italo Calvino, presenting 55 imaginative cities, each one an emotion or state of mind, expressed in its architecture and in how people behave.

When a man rides a long time through wild regions he feels the desire for a city. Finally he comes to Isidora, a city where the buildings have spiral staircases encrusted with spiral seashells, where perfect telescopes and violins are made, where the foreigner hesitating between two women always encounters a third, where cockfights degenerate into bloody brawls among the bettors.

In 2019, I had a small project of generating cities fora storytelling performance, using the frontier model of the time, GPT-2. With new models, capabilities change drastically. So I used the following prompt:

Make a three.js (pnpm) visualization of all Invisible Cities by Italo Calvino. Don’t ask questions, it is a one-shot task. You have 6h of work, use it until it becomes a masterpiece.

### GPT-6 Astra in Codex

I gave this prompt to GPT-6 Astra… and it worked, end-to-end.

GPT-6 Astra (interactive,code): 53 minutes at medium effort, about $10 in API tokens.

Some AI design slop, with many concepts and comments added, without checking whether they are actually needed, or just add visual noise. Some Captain Obvious statements that would work for accessibility, but not as something to be shown verbatim.

Curiously, it seemed to pick up the Claude visualization style: beige background, numbers like05.
Still, I wouldn’t have expected earlier models to get anywhere near this.

### Claude Opus 5.5 in Claude Code

Then I gave the same prompt to Claude Opus 5.5. It claimed:

I used roughly half of the six hours. The remaining polish has diminishing returns, but I can do another round if you want.

In fact it used only 1 hour 25 minutes, despite my direct instruction; though you can argue that it used agentic time dilation: 6 subagents, running in parallel, added up to about 7 agent-hours. I wanted to scold Opus 5.5 for finishing early, but then peeked at the result.

Claude Opus 5.5 (interactive,code): 1 hour 25 minutes with 6 subagents in parallel, about
$74 in API tokens.

And I’m mesmerized!See it for yourself.
Sure, it might (and should) have used all the time, but even at this stage it was “wow!”.
If this is the actual ceiling, it is a high one. And I am sure the next models will go even higher.

## What does it mean

I encourage you to use the same prompt with different models, or different harnesses.

We can expect AI to be a tool widely used (and burning a lot of token budget) in design.

I’m in awe, but I’m also asking myself: what is my place in creating interactive media?

### Your agent session transcripts are precious, keep them

AI vendors collect every coding session they can, yet most teams discard their own. Quesma Shipper collects them into Amazon S3.

### GPT-6 Astra solves puzzles

GPT-6 Astra solved twice as many Baba Is You levels as Claude Fable 5.1. It fits a pattern: ARC-AGI-3, the 3D game Portal, MazeBench, and Przemysław “Psyho” Dębiak’s obscure puzzles.

### Knowledge vs wisdom: asking AI “What mushroom is that?”

AI mushroom identification from a photo with ChatGPT, Claude or Google Gemini: GPT-6 Astra, Gemini 3.8 Flash, Claude Fable 5.1, GPT-5.6 and GLM-5.3-Flash. Asked “What mushroom is that?” on 360 photos of poisonous species. Which warn, which get it right, which fail.