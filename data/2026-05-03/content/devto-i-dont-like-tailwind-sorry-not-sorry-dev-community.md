---
title: I Don't Like Tailwind. Sorry Not Sorry - DEV Community
url: https://dev.to/freshcaffeine/i-dont-like-tailwind-sorry-not-sorry-50b5
site_name: devto
content_file: devto-i-dont-like-tailwind-sorry-not-sorry-dev-community
fetched_at: '2026-05-03T19:54:52.867951'
original_url: https://dev.to/freshcaffeine/i-dont-like-tailwind-sorry-not-sorry-50b5
author: Andy Robinson
date: '2026-05-01'
description: An opinionated defence of hand-crafted CSS in a utility-class world There. I said it. Call me a... Tagged with css, webdev, discuss, frontend.
tags: '#discuss, #css, #webdev, #frontend'
---

A pumpkin pie analogy for hand-crafted code

An opinionated defence of hand-crafted CSS in a utility-class world

There. I said it. Call me a dinosaur. Call me a purist. Tell me I'm fighting progress. I'll be over here, writing beautiful, considered,mineCSS — and enjoying every second of it.

Tailwind CSS is enormously popular. Millions of developers reach for it on every project. The tooling is great, the community is huge, and the documentation is genuinely excellent. I respect all of that. And I still don't want it anywhere near my projects.

Let me explain why.

## The Pumpkin Pie Problem

Here's an analogy that I can't shake.

Making a pumpkin pie from scratch means: roasting a whole pumpkin, scooping and blending the flesh, building your custard from scratch with cream and eggs and warming spices — nutmeg, cinnamon, a little ginger — making your pastry by hand, feeling the butter come together with the flour under your fingertips, crimping the edges, blind baking the shell, pouring in the filling, baking it until the kitchen smells incredible.

Using Tailwind is more like: buying a ready-made pastry crust from the supermarket, cracking open a tin of pumpkin purée, stirring in a spice packet, pouring it in, and then telling everyone you made a pumpkin pie from scratch.

And here's the thing about pumpkin pie specifically — unlike apple, there's almostnothingto hide behind. The filling comes out of a tin. The crust came from a packet. There's no chopping, no layering, no real technique involved. You've essentially just operated an oven. Sure, there'sapie at the end. It'll probably taste fine. People will eat it. But you didn'tmakeit. Not really. You assembled it.

I know some of you are already typing your rebuttals. "But the end user doesn't care how you made it!" "Efficiency is what matters!" "Ship faster, iterate quicker!"

And you're not wrong — those things matter. But they're not the only things that matter. And in the rush to ship faster, I think we've lost sight of something important.

## CSS Is a Craft. Treat It Like One.

Writing CSS well is a skill. A genuine, hard-won, takes-years-to-really-get-good-at skill.

Understanding the cascade. Knowing when to use custom properties and why. Building a coherent spacing system thatbreathesconsistently across a whole design. Writing selectors that are specific enough to do their job and no more. Reaching forclamp()and letting the browser do the responsive work for you. Crafting animations that feel like they belong to the design rather than being bolted on.

This is craft in the same way that woodwork is craft, or cooking is craft. It's the difference between a furniture maker who understands grain and joinery, and someone who assembles flat-pack with an Allen key. Both produce a table. Only one of them reallymadea table.

Kevin Powell — if you don't follow him on YouTube, stop reading this and go watch a few videos, then come back — has spent years demonstrating exactly this. His channel is a masterclass in what CSScando when you actually sit down and learn it properly. He makes CSS look joyful, because when you understand it, it genuinely is. He doesn't need utility classes to achieve elegant, responsive, maintainable layouts. He uses the language.

The thing that strikes me watching his content is howconfidentit is. There's no wrestling with tooling, no hunting through documentation to remember which arbitrary class name produces which pixel value. Just a developer who knows their medium, working with it directly.

That confidence only comes from practice. And you can't practice what you outsource.

## What We Give Up

When you reach for Tailwind by default, here's what actually happens — whether you notice it or not.

You stop learning CSS.If you're always translating design intent into utility classes, you never develop the intuition for writing a rule directly. The gap between "I know what I want this to look like" and "I know how to write the CSS to achieve it" never closes. Junior developers especially suffer here — they can ship Tailwind fast, but ask them to debug a stacking context issue or explain why their flexbox isn't aligning the way they expect, and they're lost.

Your HTML becomes noise.Look at a component written in Tailwind. Really look at it.className="flex items-center justify-between px-4 py-2 text-sm font-medium text-gray-900 bg-white border border-gray-200 rounded-lg hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"— that's abutton. The semantic signal is completely buried. The HTML is no longer a document; it's a stylesheet written in the wrong place.

Every project looks the same.Tailwind has a house style. It has a default scale. It has a palette. Even when you customise it, the bones are the same. I've reviewed codebases from companies across the industry and I can almost always tell instantly whether they're using Tailwind. Not because the designs are bad — they're often quite good — but because there's a sameness to them. A kind of interchangeable quality. The quirks, the character, the intentional weirdness that makes a product feeldesignedrather than generated — that tends to get smoothed away.

You become dependent on the abstraction.What happens when Tailwind changes its API? Whenclass-variance-authoritygoes out of fashion and everyone moves on to the next thing? You've written tens of thousands of lines of code tightly coupled to a specific flavour of a specific tool. Hand-crafted CSS doesn't have this problem. CSS is CSS. It was there before Tailwind, and it'll be there long after.

## "But What About Large Teams?"

This is the serious argument for Tailwind, and I'll give it its due. On large teams, shared conventions matter. If everyone is writing their own CSS in their own style, you get chaos. Inconsistent spacing, competing naming conventions, specificity wars, dead code that nobody dares delete.

Tailwind solves arealproblem here. I understand why teams reach for it.

But the solution to inconsistent CSS isn't to stop writing CSS — it's to writebetterCSS together. A well-maintained design token system. A sensible component architecture. A style guide that the team actually follows. These are harder things to build than installing a package, yes. But they produce better outcomes. They produce a codebase that a developer — any developer — can open and understand without needing to know whattext-slate-700means.

## The Feeling of Writing Good CSS

I want to end on something that doesn't get talked about enough in these conversations, because it's subjective, and subjective things get dismissed as irrelevant in technical discussions.

There's a feeling to writing CSS well. To building a component from scratch and having itsing. To watching a layout adapt gracefully across viewport sizes because you set it up correctly with a bit ofgridand some thoughtfulmin()andmax(). To seeing an animation you hand-crafted land exactly right — easing, timing, all of it — and knowing you built that.

It's the same feeling the baker gets when the crust comes out perfect. The same feeling the woodworker gets when two joints fit together without a gap.

Tailwind is a very good ready-made pastry crust. But I'd rather learn to make my own.

If you want to fall back in love with CSS as a language, start withKevin Powell's YouTube channel. He's the most patient, thorough, genuinely enthusiastic CSS educator working today — and watching his content will make you a better developer.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (11 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse