---
title: I Love Tailwind. Sorry Not Sorry - DEV Community
url: https://dev.to/sylwia-lask/i-love-tailwind-sorry-not-sorry-5cfh
site_name: devto
content_file: devto-i-love-tailwind-sorry-not-sorry-dev-community
fetched_at: '2026-05-05T00:51:24.144704'
original_url: https://dev.to/sylwia-lask/i-love-tailwind-sorry-not-sorry-5cfh
author: Sylwia Laskowska
date: '2026-05-04'
description: I’m going on a short vacation this week, so this post is coming out a bit earlier than usual. I... Tagged with css, tailwindcss, frontend, discuss.
tags: '#discuss, #css, #tailwindcss, #frontend'
---

A CSS veteran’s take on speed vs purity

I’m going on a short vacation this week, so this post is coming out a bit earlier than usual. I actually had a different, more “useful” topic in mind — something educational, something responsible. But then I came across this fascinating article:I don’t like Tailwind. Sorry not sorrywritten by@freshcaffeine, and I couldn’t get it out of my head.

So I decided to write a response instead.Useful content will have to wait 😄

I actually agree with many of the points in the original article — especially around learning fundamentals. I just have a different perspective shaped by a different kind of work.

Let me start with a small disclaimer: I’ve written a lot — and I meana lot— of handcrafted CSS in my life. Entire design systems. In fact, I got my first job in IT mostly thanks to my CSS skills, because my programming skills at the time were… let’s say “a work in progress” 😉

There was even a period when I made extra money building simple websites for clients. People literally paid me for delivering clean, aesthetic CSS.

So in theory, I should be the first person to defend handcrafted CSS and criticize Tailwind for polluting HTML.

And yet… I’m not.

Despite all its flaws, I love Tailwind. Deeply, sincerely, and yes — unapologetically.Because it gives us something incredibly valuable in real-world development:speed and predictability.

## Pumpkin pie: homemade or store-bought?

The author of the original article uses a pumpkin pie analogy. Handcrafted CSS is like baking a pie from scratch — roasting the pumpkin, making the dough, carefully preparing everything with love. Tailwind, on the other hand, is like using pre-made ingredients. You open a can, use ready-made crust, assemble everything quickly. Sure, it’s still a pie, but not quite like the one your grandma would make.

It’s a nice analogy. It really is.

The problem is — most businesses are not running artisan bakeries.They’re running factories.And those factories aren’t even in the pie business.

In reality, business rarely needs a handcrafted pie. Honestly, it often doesn’t even need a “semi-handmade” one. What it really wants is mass production: something that’s sweet enough, looks good enough, doesn’t cause stomachache, and can be delivered fast. If you can add a small decorative touch on top to make it feel slightly more unique — great. But even that is optional.

And there’s no point being offended by this. We can absolutely build beautiful, handcrafted CSS when we want to. But most of the time, businesses choose speed — because they are selling a product, not CSS.

I’m not building a piece of art.I’m building software that five teams won’t break next week.

## Repetition isn’t always a bug

One of the arguments against Tailwind is that everything starts to look the same. And honestly — that’s true.

But here’s the thing: very often, that’s exactly what the client wants.

Back when I was building websites for clients, the happiest ones were those who got three templates to choose from and a bit of customization on top. They didn’t want a masterpiece. They wanted something clean, modern, and effective — something that sells.

Tailwind is often simplygood enoughfor that.

And in many cases,good enough delivered fast beats perfect delivered late.

## “Messy HTML”

Yes — if you just throw classes around randomly, your HTML will look messy.

But let’s be honest: if we’re “craft-oriented developers,” we can organize our components properly, right? In real projects, that long Tailwind class list usually lives inside a component anyway. You don’t copy-paste that everywhere.

Also:

HTML is “noisy”? Sure.But at least the rules are right next to what they affect.

I’ve seen plenty of “beautiful” CSS codebases where styling logic was scattered across multiple files, overridden in unexpected places, and impossible to trace without jumping through five layers of abstraction. I’ll take explicit over “hidden magic” any day.

## Junior developers and “not learning CSS”

I actually agree with one part: Tailwind doesn’t replace learning CSS. I even wrote about that in my article:Is Learning CSS a Waste of Time in 2026?

But the argument that Tailwind is somehow “hurting juniors” always makes me smile a bit.

On one hand, we have mass layoffs in tech and endless discussions about AI replacing developers. On the other, we worry that juniors might not learn CSS because things are… too easy?

Let’s be real for a second.

“Junior” doesn’t mean “child.” These are adults. If someone wants to grow as a frontend developer, learning CSS is part of the job. It’s not some hidden, mystical knowledge. And we don’t need to choose our entire tech stack based on making things harder just so people are forced to learn.

Also — I’ve seen plenty of experienced developers who still struggle with CSS after years in the industry. At that point, I’d honestly rather have them use Tailwind and ship something consistent than fight yet another specificity war.

Tailwind doesn’t create bad developers.Lack of fundamentals does.

## About “craft”

There’s this idea that writing CSS is a form of craftsmanship — something closer to art, something deeply satisfying.

And yes, it can be.

But the last few years — especially with the rise of LLMs — have made it pretty clear where our “craft” actually sits in the bigger picture. In most business applications, CSS is not art. It’s not painting. It’s not sculpture.

It’s closer to baking pumpkin pies at scale.

There will always be places where handcrafted work matters — just like there are bakeries selling beautiful, artisanal cakes. But if you’re selling paper clips and organizing a corporate event, you’re probably not baking everything from scratch. You’re ordering something decent that gets the job done.

And that’s fine.

## Why I actually like Tailwind

Let’s be clear — Tailwind is not perfect. It has trade-offs.

But it solves very real problems.

It gives you:

* speed— you don’t context-switch between files every 10 seconds
* predictability— no guessing what some class name means
* consistency— especially across large teams
* simple selectors— which are often easier for browsers to process than deeply nested CSS
* less dead code— thanks to modern build setups

And most importantly:

It removes ambiguity.

The real problem in large codebases isn’t that CSS isn’t “beautiful” enough.It’s that it becomes inconsistent, fragile, and slow to evolve.

I’ve never seen a project fail because CSS wasn’t handcrafted enough.I’ve seen plenty fail because things were inconsistent and took forever to build.

## When handcrafted CSS still makes sense

I don’t think Tailwind (or something similar) should replace handcrafted CSS everywhere.

There are cases where writing CSS by hand is not just useful — it’s the better choice.

Design systems and shared UI foundations— where you need full control and long-term consistencyHighly custom or experimental UI— where utility classes start to fight you instead of helpingPerformance-critical interfaces— where you want precise control over what gets shippedLearning and understanding the fundamentals— because at some point, abstractions always leak

## Final thoughts

Tailwind isn’t about replacing CSS.It’s about making frontend development survivable at scale.

And no — this post is not sponsored by Tailwind. (But if someone from Tailwind happens to read this… feel free to reach out 😄)

And what do you guys think? Are you Team Tailwind or more into 'craft' CSS? Or maybe something in between?

Thanks for reading! If you enjoyed this post, I'd love to have you follow me here onLinkedIn.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (21 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse