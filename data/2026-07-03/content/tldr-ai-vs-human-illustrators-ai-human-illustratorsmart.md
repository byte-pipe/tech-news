---
title: AI vs. human illustrators? AI + human illustrators!—Martian Chronicles, Evil Martians’ team blog
url: https://evilmartians.com/chronicles/ai-vs-human-illustrators-ai-plus-human-illustrators
site_name: tldr
content_file: tldr-ai-vs-human-illustrators-ai-human-illustratorsmart
fetched_at: '2026-07-03T19:33:11.703394'
original_url: https://evilmartians.com/chronicles/ai-vs-human-illustrators-ai-plus-human-illustrators
date: '2026-07-03'
published_date: '2026-07-01'
description: Evil Martians went from attempting to one-shot AI illustrations to a human-in-the-loop workflow with a dedicated illustrator. When a human owns first and last mile of this process, illustrations are crisp, high-quality and fun. Go BTS of our illustration production.
tags:
- tldr
---

# AI vs. human illustrators? AI + human illustrators!

July 1, 2026

## Topics

* AI
* Design
* Developer Community
* Design for devtools
* Victoria MelnikovaHead of New Business, Host of Dev Propulsion Labs
* Travis TurnerTech Editor

Evil Martians take huge pride in our blog. Illustrations are there to support the vision. We fantasized that image gen tools are ready for us to one-shot illustrations, but we were wrong. Instead we built a process where blog editor owns the first mile, AI does bulk of the work and an illustrator owns the last mile. The quality is where we want it to be, and our team is finally happy.

Evil Martians is a developer-focused product studio that’s been at it for over 20 years. We build developer-facing brands, products and infrastructure. We also run one of the larger devtools blogs on the internet: 50+ technical articles a year, written by pretty much every Martian, for an audience of 500K+ developers.

Here’s what you may not know: the engineers who work on the blog are encouraged to do so, but it’s entirely optional for them. It’s a real labour of love, and that level of care passes on to the cover illustration for each article.

Technically speaking we don’t really have to have these pictures. If Evil Martians itself is a cake, the blog is like the cherry on top, and the blog cover illustrations are like the cherries on top of those cherries. If any team should have been able to prompt their way to a fully automated illustration pipeline, it probably should have been us.

Irina NazarovaCEO at Evil Martians

Evil Martians builds and ships design systems for startups to enable cohesive agentic development.

Book a call

## The problematic past of the Evil Martians blog illustration workflow

Illustrations have always been part of how the blog reads, and our mascot, a green alien chasing a humanoid, anchors every illustration. For years, we sourced those illustrations through a small bench of contract illustrators. Even though we have a strong design department, doing this character illustration work (with AI or not) is not our specialization, nor is it something our busy designers are often free to do.

There were multiple factors which made this process a real headache:

1. The turnaround was unpredictable. We worked with numerous illustrators over the years and their availability would constantly vary, and one illustrator could only take on one illustration at a time.
2. The mascot drifted between hands and different illustrators interpreted the character differently.
3. Timing concerns went beyond turnaround speed. Authors weren’t always satisfied with the first pass, and a back-and-forth on a single illustration could stretch over days, even into the next week.
4. Although the budget and cost was relatively low, we always wanted to bring production of our brand materials in-house.

As far back as 2023, we were experimenting with simple AI images to augment the availability of our in-house and external illustrators:

But in 2025, once LLMs really caught up with image generation, the conversation on our team changed.

## The folie à deux effect

Folie à deux is a shared delusion that takes hold inside a tight group, where each member’s confidence reinforces everyone else’s. That’s basically what happened to us as image models from Recraft, ChatGPT, Midjourney, and others kept getting better. Every time a new model landed, the illustration conversation on our team started again. This was early 2025, so we tried a few things:

1. Raw-doggin it with Midjourney.We actually spent hours prompt-engineering and trying to even understand what it is that we want for our blog. We landed on isometric Pixar-looking 3D objects, however, it didn’t always work.
2. Recraft.They had proprietary models that produced vector and a user-friendly canvas UI. As Nanobanana came out, we wanted to play with it within Recraft, but that didn’t work, so we decided to move to other platforms.
3. Nanobanana.It came out and really seemed to have it all. With good references we could get close to perfection, but any edit—even a minor one—would muddy the image and lose quality. We tried Flora Fauna for background removal and Topaz Upscaler for upscaling, but quality still suffered, and fixing things by hand drained our time.
4. We even built a custom GPT appfor different styles. Our design team spent a few weeks on creating a tool that would be convenient to use, but at the time GPT was not great with images and we just stalled having to reach for other tools.

In most instances we were able to get 90% there, but those odd last 10% really threw us for a loop. In situations where we managed to produce an image without attracting designers, the results weren’t always excellent.

## What the models still couldn’t reliably do

After enough iterations, a few failure modes kept showing up.

Mascot integrity across a series.A single shot of our mascot looked fine in almost any modern model. But we couldn’t produce consistent proportions, expression, and silhouette without per-asset human cleanup.

As another note, in-house attempts to adapt our 2D mascot properly into the world of 3D were not optimal.

Small details sucked.You know that feeling when an illustration looks good at a first glance, but as you look at it longer, it starts to fall apart? That was us. Texts, weird hallucinations, odd shadows and tiny details became a huge headache for my team. As a lean team, we tried to handle it ourselves. But that wasn’t the best use of our time, and the process felt unnecessary.

For example, before we manually fixed it, this microscope seemed pretty hard to actually use:

Composition and transparency.Our illustrations ship at 1200×1000 px, often with transparent backgrounds. AI image models default to opaque output and a single aspect ratio, which meant cleanup on every asset before it could ship. (We also love to use colors in our blog; after all, we pioneered OKLCH for the web.)

Tokenmaxxing and time drain.To our disappointment, what initially looked like a promising cost-saving workflow ended up completely draining our resources. We ended up with each illustration costing us $600-700 in our time equivalent, caught in the smallest Photoshop manipulations cleaning up slop at 7pm on a Friday.

Things were (literally) going off the rails:

Author’s note: None of these are arguments against AI in the workflow. They’re arguments against AI as the entire workflow.

It eventually became soul-suckingly chaotic to deal with all of these quirks. And I remember the specific moment when it all ended. By that point Travis and I were completely exhausted.

We had an article that needed an illustration. I used Flora Fauna, it came out ALMOST perfectly. I went to fix the small inconsistency in Photoshop, and 2 hours flew by. Travis asked: “Vica, it might sound rough, but are you sure this is the best use of your time?”

The reality of the situation hit me, and I decided to look for help.

## How the workflow looks now

What kept the slop out is what we callthe last human mile. In our case, that human, a professional designer, sits inside an AI-first design agency calledKOJIthat pairs AI generation with a human illustrator who owns the cleanup, the shadows, and the small things the model still gets wrong. Each illustration costs us $100.

The author of the post and our editor agree on a one-line visual thesis for the illustration. This is the part that requires editorial taste and a sense of what the post is actually about. We hand the one-liner over to KOJI along with any references or must-haves the author wants visible.

From there, KOJI runs the whole creative process internally. The AI generation, the selection of the strongest direction, and the human illustrator’s cleanup all happen inside the agency.

Let’s be clear here: KOJI is not one-shotting this. There was anextensive preparation processthat allowed them to take the flat mascot and make it into a versatile 3D model that now can be effectively used in the AI pipeline.

First of all, we were finally able to translate our guys into the third dimension:

A bit unflattering for the human, but they would clean it up later on.

Then the models are placed in various settings and scenarios only bound by author imagination. To demonstrate, we haven’t even used most of these iterations yet, but they’re out there:

In terms of the process, KOJI sends us a first draft, the author gets a 24-hour window to flag specific issues against the brief, and KOJI returns the final version before it ships.

What stayed exactly the same is that humans own the brand at both ends of the pipeline. We own the visual thesis at the start, and a human illustrator at KOJI owns the final pixels at the end.

Our publication bottleneck has been significantly reduced, and because each illustration costs less,we actually now commission 2-3× more illustrations than we used to:

cost
our time
quality
bottleneck
human
$200-300
1-2 hours
medium
high
AI
$20
8+ hours
inconsistent
medium
hybrid
$100
1-2 hours
consistent
low

## Lessons learned beyond the illustrations

The illustration pipeline is a specific case of a more general pattern that’s worth paying attention to even if you don’t care about how a devtools blog gets its illustrations made.

Many devtools founders shipping AI features will recognize the beats of this story from their own products: the demo works, the first batch of production runs works. Then, a failure mode shows up that wasn’t visible in the demo, because that demo was selected from a distribution where the model happened to be lucky.

Pretending a model can cross that final mile is the most common and most expensive mistake we see devtools teams making in 2026.

Irina NazarovaCEO at Evil Martians

Evil Martians builds and ships design systems for startups to enable cohesive agentic development.

Book a call
Send email
 instead