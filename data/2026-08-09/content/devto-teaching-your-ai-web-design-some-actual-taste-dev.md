---
title: Teaching Your AI Web Design Some Actual Taste - DEV Community
url: https://dev.to/lovestaco/teaching-your-ai-web-design-some-actual-taste-4p13
site_name: devto
content_file: devto-teaching-your-ai-web-design-some-actual-taste-dev
fetched_at: '2026-08-09T19:31:55.648894'
original_url: https://dev.to/lovestaco/teaching-your-ai-web-design-some-actual-taste-4p13
author: Athreya aka Maneshwar
date: '2026-08-08'
description: Hello, I'm Maneshwar. I'm building git-lrc, a Micro AI code reviewer that runs on every commit. It is... Tagged with ai, webdev, claude, design.
tags: '#ai, #webdev, #claude, #design'
---

Hello, I'm Maneshwar. I'm building git-lrc, a Micro AI code reviewer that runs on every commit. It is free and source-available on Github.Star git-lrcto help devs discover the project. Do give it a try and share your feedback.

Let me guess.

You opened Claude Code, typed "build me a modern landing page," hit enter, and got back something that technically works but somehow looks like every other site you have ever scrolled.

Purple to blue gradients.

Inter for everything.

Little rounded icon tiles floating above every heading.

A hero section that could belong to literally any SaaS on earth.

Congratulations, you have been served a fresh bowl of AI slop.

I have been fighting this exact fight for a while now, and I want to walk you through how I actually beat it.

Not with one magic prompt, and definitely not with a 10,000 lineDESIGN.mdyou copied from a thread.

Just three moves, a couple of tools, and a way of working that stops leaving your output to the gods of the one shot.

## First, why does slop even happen?

Here is the uncomfortable truth, and it is worth sitting with for a second.

The problem with slop is not technical.

The models are not bad at writing CSS.

They are frankly great at it.

The problem is that the output isgeneric, and generic is a moving target.

If the models got ten times better tomorrow, they would just raise the bar on what counts as basic.

The floor moves up, the slop moves with it.

Why? Because a model trained on the public internet learns the statistical center of the public internet, and the center of the design internet in 2026 is Tailwind templates, Vercel starters, and other AI generated landing pages.

Ask for "modern" and you get the mathematical average of every landing page ever shipped. That average is the slop.

So the fix is not a better model.

The fix isyou. Specifically, your taste. And that is where a lot of us cope instead of cook.

Yeah. That is the cope.

The rest of this post is about doing the opposite.

Here is the whole game on one screen before we dig in:

## Step 1: Cultivate some taste (you cannot inject what you do not have)

You have heard "AI has no taste" a hundred times. Fine.

But the sneaky corollary nobody says out loud is thatyouneed taste to hand over, and most of us have not deliberately built any. We just vibe.

So step one is boring and unglamorous and completely non negotiable: go collect stuff you like.

Become a magpie. OpenDribbble, search "web design," sort by popular, and start screenshotting the hero pages that make you feel something.

Do the same onPinterest.

Then, and this is my personal favorite, go toTwitter slash X, where a genuinely absurd amount of the best UI work gets posted before it lands anywhere else.

Save screenshots. Save links to live sites too, since a real page tells the model way more than a flat image.

Now, youcouldjust let those screenshots rot in a folder calledinspo_FINAL_v3. Or you could do the fun version and have Claude Code spin up a tiny inspiration library web app for you.

Mine groups everything by design style, names the aesthetic in actual design vocabulary, and gives me keywords for each piece.

Click a screenshot and I can copy an image prompt (for generating a matching hero background later) or copy a full brief (for generating the whole page).

It turns a pile of pretty pictures into a reusable palette ofyourtaste.

The point of this step is not to copy anyone.

It is to give your future self a base to point at, so you are never starting from a blank prompt and an average result.

You are starting from a direction you already know you like.

## Step 2: Arm Claude Code with tools it does not ship with

Out of the box, Claude Code is a strong developer with the visual judgment of a coin flip.

So we hand it better eyes and better hands. Three categories are enough.

### A real design skill

The default Anthropic frontend-design skill was a fine start, but at this point it kind of produces the slop it was meant to prevent.

The one I reach for now isImpeccable, an open source Claude Code skill by Paul Bakaus.

Instead of vaguely begging the model to "not look AI generated" (which never works), it does something clever: itnames the specific slop patternsand tells the model to avoid them.

It ships as one skill with a stack of commands you invoke like slash commands. A few that I use constantly:

* /critiquefor an honest UX review of hierarchy and clarity
* /bolderto push a safe, boring design toward actual impact
* /quieterto pull an over caffeinated design back down
* /polishfor a final alignment and spacing pass before shipping

Under the hood it hunts slop across seven areas: typography, color, spatial design, responsiveness, interaction, motion, and UX writing.

There is even a Chrome extension that highlights slop patterns on a live site, which is a little bit rude and extremely useful.

Thebefore and after examples in the docssell it better than I can.

If Impeccable is not your flavor, there are other "taste" style skills in the same spirit floating around GitHub, and they work on the same principle.

### An image and video MCP

Claude Code cannot draw. It cannot generate that moody cinematic mountain range you want behind your hero text.

So give it the ability with theHiggsfield MCP, which basically hands your agent a backstage pass to 30 plus image and video models through a single connection.

You describe the hero image, it generates it, drops it into the section, done. No tab hopping to five other tools.

### A component registry

For the smaller stuff, buttons, cards, pricing sections, pagination (when was the last timeyouthought hard about pagination?), I browse21st.dev.

It is an open registry where each component ships with a "copy prompt" button.

Paste that into Claude Code and it rebuilds the component inside your codebase, wired to your stack.

Think of it as step one's taste hunting, but zoomed all the way in to the component level.

### One warning before you go tool shopping

Here is the trap, and I have fallen in it more than once.

It is very easy to convince yourself you are one skill away from all your design problems being solved. You are not.

You will find flashy skills that build gorgeous sites.

The catch is they tend to be narrow and extremely prescriptive, so they hand you exactly one kind of output every time.

That is not taste, that is a template with extra steps.

I like Impeccable and Higgsfield precisely because they areflexible.

The downside of flexible is that they will not magically produce greatness. That still depends on your prompting and your taste. Which is the point.

## Step 3: Build in loops, not in one shots

This is the mindset shift that changed everything for me, so read it twice:stop trying to one shot.

The one shot is a lottery ticket.

You type "make it premium," hit enter, and pray.

Sometimes you win. Usually you get slop with a slightly nicer font.

Instead, cast a very wide net up front, then narrow down.

Here is the actual sequence I run:

Let me make that concrete.

Say I am building a landing page for a made up AI analytics startup called Kestrel, and the goal is to get people to book a demo.

First, five versions in five styles, all at once.Not one, five.

If you built that inspiration library from step one, you can just tell Claude Code to look at it, pull five aesthetic families, and build a page in each.

Seeing them side by side on one screen makes it obvious which direction has legs, in a way that squinting at a terminal one attempt at a time never does.

Say I land on a "vast quiet" minimalist look with a big cinematic image behind the hero.

Then, three variations of that one direction.

Same aesthetic, different body layouts.

Maybe one is super vertical and minimal, one is a "ledger" style with an index that scrolls alongside you, one frames each section with edges.

I pick the ledger, because that scrolling index is genuinely cool.

Then I nail the hero image before fussing with anything else.

I fire up the Higgsfield MCP, ask for four 2K options that fit the quiet aesthetic, and look at them in the actual hero slot.

Too black and white? Ask for variations with a splash of color.

That gentle golden "alpenglow" one? Sold.

Then transitions and weight.

I ask for the hero to fade into the body instead of hard cutting, and for elements to load in with a bit of heft so the whole thing feels premium rather than snappy and cheap.

Notice what is happening.

At every stage I amseeing options and choosing, not blindly trusting a single generation. That is the whole trick.

### The four things worth putting in your prompt

You do not need a giant design doc.

When those get too specific, they just produce the same thing every time, which is the slop problem wearing a fancier coat.

I pass four things, loosely:

1. Aesthetic.The general family of design you are going for.
2. Reference image.This is where your taste library earns its keep. Drop a screenshot, or better, an actual URL of a site you like. You are matching afeeling, not copying content.
3. Intent.What is this and why does it exist? SaaS product? Event page? Who is the audience and what do you want them to do, read, click, or fill out?
4. Guardrails.The always and the never. This is your anti slop clause. "Never use purple gradients. Never use Inter. No 3D SaaS blobs."

### The secret weapon: a live tweak bar

Even after all that, the page feltalmostright but a touch too minimal.

Instead of guessing with more "make it pop" prompts, I asked Claude Code to add a live tweak bar to the dev server, the kind of panel you see inside Claude Design.

Font family, font size, accent color, motion, reveal distance, anything where a design decision lives.

Now I iterate by eye.

I flip through fonts in real time instead of asking for ten rebuilt pages and comparing them like a lunatic.

Being able to see differences instantly is the thing that finally gets you to something you actually like. And do not forget: references are not just for the hero.

Feed the model URLs and screenshots for how you want thebodylaid out too, since Claude Code can look at a live page and apply its structure.

## Wrapping up

None of this is a rulebook. Do not follow it to the letter, because the second something becomes a rigid formula, it starts producing its own flavor of slop.

The point is a flexible workflow you can bend to any project:

Cultivate taste so you have something to hand over.

Arm your agent with a design skill, an image MCP, and a component registry.

Then build in loops, wide net first, tweak by eye last, so you are never at the mercy of a single roll of the dice.

The moat was never the toolbox.

It was always your taste.

Go build something that looks likeyou, and leave the purple gradients where they belong.

If you try this, I would love to see what you ship. Drop a link in the comments and let us compare notes.

AI agents write code fast. They also silently remove logic, change behavior, and introduce bugs — without telling you. You often find out in production.

git-lrc fixes this. It hooks into git commit and reviews every diff before it lands. 60-second setup. Completely free.

Any feedback or contributors are welcome! It's online, source-available, and ready for anyone to use.

⭐ Star it on GitHub:

## HexmosTech/git-lrc

### Free, Micro AI Code Reviews That Run on Git Commit

|🇩🇰 Dansk|🇪🇸 Español|🇮🇷 Farsi|🇫🇮 Suomi|🇯🇵 日本語|🇳🇴 Norsk|🇵🇹 Português|🇷🇺 Русский|🇦🇱 Shqip|🇨🇳 中文|🇮🇳 हिन्दी|

# git-lrc

## Free, Micro AI Code Reviews That Run on Commit

 

 
 
 
 
 
 

GenAI today is arace car without brakes. It accelerates fast -- you describe something, and large blocks of code appear instantly. But AI agentssilently break things: they remove logic, relax constraints, introduce expensive cloud calls, leak credentials, and change behavior -- without telling you. You often find out in production.

git-lrcis your braking system.It hooks intogit commitand runs an AI review on every diffbeforeit lands. 60-second setup. Completely free.

In short, git-lrc helpsPrevent Outages, Breaches, and Technical Debt Before They Happen

At a glance:10 risk categories·100+ failure patterns tracked· every commit…

View on GitHub

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse