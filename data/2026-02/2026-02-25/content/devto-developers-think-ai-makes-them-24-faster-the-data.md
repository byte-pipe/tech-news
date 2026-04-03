---
title: Developers Think AI Makes Them 24% Faster. The Data Says 19% Slower. - DEV Community
url: https://dev.to/matthewhou/the-metr-study-changed-how-i-think-about-ai-coding-4i84
site_name: devto
content_file: devto-developers-think-ai-makes-them-24-faster-the-data
fetched_at: '2026-02-25T11:53:13.652026'
original_url: https://dev.to/matthewhou/the-metr-study-changed-how-i-think-about-ai-coding-4i84
author: Matthew Hou
date: '2026-02-24'
description: Developers predicted AI made them 24% faster. They were actually 19% slower. The problem isn't AI — it's where we spend our attention. Tagged with ai, testing, discuss, codequality.
tags: '#discuss, #ai, #testing, #codequality'
---

Last month, METR published a study that should make every developer uncomfortable.

They took 16 experienced open-source developers — people who knew their codebases inside out — and randomly assigned tasks to be done with or without AI tools.

Predicted

Measured

Post-study belief

Speed impact

+24% faster

-19% slower

"It helped me"

I've been using AI coding tools daily for the better part of a year. When I read that study, my first reaction was "well, those developers must have been doing it wrong." My second reaction was:that's exactly the kind of thinking the study warns about.

## The perception gap is the real finding

The speed numbers get all the attention, but I think the important finding is the perception gap. Wefeelfaster because AI handles the boring parts — boilerplate, syntax, the stuff that feels like work but isn't where the actual difficulty lives. Meanwhile, the hard parts get harder: understanding what AI changed, verifying it's correct, keeping a mental model of code you didn't write.

Simon Willison — the guy behind Datasette and one of the most prolific AI-assisted developers I know of — wrote something that stuck with me:

"I no longer have a solid mental model of what my projects can do and how they work."

This is a developer who's built 80+ tools with AI assistance. If he's struggling with mental models, maybe the issue isn't experience level.

## Attention is the actual bottleneck

Here's how I think about it now:

Before AI: Think → Write → Test → Debug
With AI: Describe → Review → Verify → Debug AI → Debug your understanding

Enter fullscreen mode

Exit fullscreen mode

The writing step got cheaper. Everything else got more expensive. And "reviewing code you didn't write" is cognitively harder than "writing code you understand" — anyone who's done code review knows this.

"AI turned us all into Jeff Bezos — automated the easy work, left all the hard decisions." — Steve Yegge

The METR study essentially confirmed what a lot of us have been feeling but didn't want to admit: AI coding tools don't save time. At best, theyredistributewhere your attention goes. At worst, they create an illusion of productivity while the cognitive load actually increases.

## What I actually changed

I stopped optimizing for speed. Instead, I started asking:"where is my attention going?"

### 1. I front-load the thinking, not the prompting.

Before I touch any AI tool, I write down — in plain text — what I want, why I want it, and what "done" looks like. Not for the AI. For me. This takes 5-10 minutes and it's the most impactful thing I do all day, because it forces me to think before generating.

Kent Beck calls this the distinction between "augmented coding" and "vibe coding." The latter is hoping the AI gives you working code. The former is knowing what working code looks likebeforethe AI writes it.

### 2. I treat verification as the actual job.

I used to think of code review as a chore you do after the real work. Now it IS the real work. StrongDM's team took this to the extreme — their "Dark Factory" setup has zero human code review. All investment goes into tests, tools, and simulations. The humans define what correct looks like. The machines do everything else.

I'm not there yet, but the direction is clear: my value isn't in writing code. It's in defining what "correct" means for my specific context.

### 3. I stopped measuring productivity in output.

More lines of code is not more productivity. More PRs is not more productivity. The Harness 2025 survey found that67% of developersspendmoretime debugging AI-generated code than they would have spent writing it themselves. If that's you, generating more code faster is making things worse, not better.

The metric I care about now: how much of my attention went to decisions only I can make? Architecture choices, user-facing trade-offs, "should we even build this" — that's the stuff AI can't do. Everything else, I want to automate not because it's faster, but because it frees up mental bandwidth for the hard problems.

## The uncomfortable implication

If the METR study is right — if AI tools don't actually save time for experienced developers on familiar codebases — then the value proposition of AI coding isn't "10x productivity." It's something more subtle:

The ability to spend your attention on higher-impact work, if you're disciplined enough to actually do it.

That's a much harder sell than "write code faster." It requires you to know what high-impact work looks like, and to resist the dopamine hit of watching AI generate 200 lines in 3 seconds.

I don't have this figured out. Some days I still catch myself vibe coding and pretending the output is good because it compiled. The METR study's perception gap isn't just about their participants — it's about all of us.

But at least now, when I feel productive with AI, I stop and ask:am I actually productive, or does it just feel that way?

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (19 comments)


Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse
