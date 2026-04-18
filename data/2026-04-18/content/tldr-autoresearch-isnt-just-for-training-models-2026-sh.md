---
title: Autoresearch isn’t just for training models (2026) - Shopify
url: https://shopify.engineering/autoresearch
site_name: tldr
content_file: tldr-autoresearch-isnt-just-for-training-models-2026-sh
fetched_at: '2026-04-18T19:41:05.164674'
original_url: https://shopify.engineering/autoresearch
date: '2026-04-18'
description: How we cut our CI pipeline build time by 65% and open-sourced the project.
tags:
- tldr
---

blog
|
AI & Machine Learning

# Autoresearch isn’t just for training models

Tobi and I generalized Karpathy’s Autoresearch to improve 40+ metrics across Shopify, then we open-sourced our project.

 
Published on
 
Apr 15, 2026

It is 7PM and I'm still at my desk. My branch just failed CI. Again. It's the fifth time in a row. I am about to close my laptop and give up.

What I don't know yet is that days later, Tobi will send me a 32-commit pull request to my autoresearch side project that solves this problem.

Let me back up. I work on the Polaris team. Every time we do a tiny change, it triggers random visual regression failures—30 minutes of CI just to find out I broke something else. That's 30 minutes of waiting to learn that I need to wait another 30 minutes. But the next day, I wake up with a different idea: I'm not just going to fix my task. I'm going to fix the 30 minutes.

I push a couple of changes and open X while CI runs. There’s a new topic that everyone is talking about. It’s calledAutoresearch, created by Andrej Karpathy.

## The magic of Autoresearch

The concept is to emulate a human researcher with AI. Back then, training for GPT-2 took months. Using Autoresearch, Andrej got it done in hours and automatically while he slept.

Autoresearch is AI running in a loop. If you've heard aboutRalph Loops, it is quite similar but more specialized. Andrej uses it to train models. I am fine with my beloved friend Opus and not planning to train a model for now, so this is definitely not helping with my problem, right? This is for smart people that train models, not for me.

My PR now passes. I open another terminal and I start prompting to an agent:

Let’s investigate how we can reduce this CI time. Start with Polaris build time. Swap libraries, or migrate to others that are faster. Use Rust. Use whatever you want but make this problem go away. MAKE NO MISTAKES. Ultrathink.

Robots might come after me for this one.

It runs for a long time. It finds some performance tricks that make unit tests run faster. It tries to one-shot a solution. Not only does it not improve the time, it doesn't even build successfully.

I let it run and I open the Vault, our internal wiki where Shopifolk post what they’re working on and learning. If Twitter (sorry, X, keep doing that) did not help, maybe someone internally has the answer for me.

There’s another reference to Autoresearch, this time from my colleague Swati Swoboda. She has been experimenting with Autoresearch following the hype.

Maybe I missed something here? She says it can be used for more than model training. But how? She tried to let the agent improve a metric. I have a metric. Same concept, different application. How did I miss it? I stop everything.

I open Pi, my favorite agent harness, and start a new session. My plan is to create an extension for Autoresearch. I’ve made some extensions before, so this makes sense:

Pi, create an extension for Autoresearch. We’ll show a custom UI for each iteration as table rows, we will focus on a metric and see how it improves over time. It will run forever

Pi reads its own extension documentation. It is as simple as that. It might feel intimidating from the outside, but it is as simple as prompting the extension you need. I go for a coffee in the meantime, but I forget to drink it. It’s already cold when I realize it’s there, I’m lost in flow state.

In less than half an hour of back and forth, I have it working. It works nicely.

The first version is quite simple:

1. Find a metric to improve:In this case I am focusing on build time, as all CI pipelines depend on Polaris to be built.
2. Measure the baseline of the metric:It was 19.1 seconds when I started running it.
3. Hypothesis testing:For each iteration, it forms a hypothesis, writes it down and starts testing. Three things can happen at this point: runs faster than baseline (we keep it), crashes (we discard it), or runs slower (we discard it as well).
4. Repeat:It runs until you decide to stop it or it runs out of context. The system prompt even says "NEVER STOP LOOPING".

This is better than asking the agent, "Improve Polaris build time," as that didn't work before with the one-shot solution. With this new approach, it has a targeted focus on a metric. It has a clear goal, and a clear way to measure if it's going in the right direction.

Also, we are giving it the opportunity to try crazy things. While running this infinitely, it has the option to try things it wouldn't try in a normal run. With Autoresearch you get small increments of improvement over time. And even if it's 1% each iteration, those add up until you get something significant. Each in isolation wouldn't make sense. But overall it’s able to significantly optimize every metric you throw at it.

I let it run for some iterations, and prove it's working. It is simple. You don't need to be an ML researcher to make it work. Each iteration makes builds faster. Sometimes it crashes, but in this case it dismisses it and keeps going. It also does ugly hacks sometimes, like removing a lot of files. Yeah, it's faster, but that's not acceptable.

One idea stuck: the VRT build was running the full component pipeline—IIFE bundle, type declarations, all of it—before handing off to Storybook, which recompiles from source anyway. Pure waste. It also found that the TypeScript transform was processing all 580 component files when only 105 actually needed it. All of a sudden the build was 65% faster. I throw away all the hacks and keep the good stuff.

Before autoresearch, AI agents were doing the same work humans did, just faster. Autoresearch is different—it does work nobody would attempt manually. No one's sprint plan includes "spend three months reducing build time by 30%." It's valuable, everyone agrees it's valuable, but it's boring, it competes with feature work, and it lives in the cracks of the day. An agent has no competing priorities. It doesn't get bored, doesn't need to justify ROI to a product manager, and doesn't have a deadline pulling it elsewhere. The toil that humans correctly deprioritize turns out to be the perfect workload for an autonomous loop.

## Pair programming with Tobi

I screenshot the extension and post about it on our #pi Slack channel. “WIP autoresearch extension. I’ll keep you posted.” I also let autoresearch run in the background with three other metrics that will make CI faster.

Otherpeople of pistart showing up. Slack reactions go up, as well as my dopamine levels. Then, something I wasn't expecting: Tobi says he likes it. I have to read it twice. I open the door and tell my wife: "Tobi liked what I did!"

Tobi says I should make it easy for other people to install. I immediately create a repo and I answer in the channel: “Just runpi install repo-url.” It needs to be simple, otherwise no one will use it.

The next day, I continue making improvements on the extension. At this point I’ve already forgotten that Tobi was a fan. Until he DMs me: “Hey I really liked this thing you created. I worked on it.” He has just created 32 commits. He added multi-metric support, a script to execute every iteration consistently, improvements in the skill that runs, auto commits, among many other things. He is now the main contributor of the extension.

I find a few things I'd do differently. After thinking about it for a minute, I add a comment in the PR. Five minutes later, he's already pushed a fix. We continue working on it for the next few hours. I’ve never had a pair programming experience as intense as this one. We went from idea to execution in minutes. Should we try avoiding commits if the metric is bad? Decided. Implemented. On to the next thing.

It’s now the end of the day for me. I’m in Barcelona, so that means I’m six hours ahead of Toronto. At 9PM my time Tobi is still making changes, when he tells me, “I think it’s done. Let’s open source it.”

What? Now? Already? What if we expose something internal? I should do this carefully. Also, it was both of us working on it, so I don’t feel comfortable publishing this in my name. But he insists: “Your idea, your repo.”

I realize that yeah, he means actuallyright now.

## Open-sourcing

We finish dinner and I put the kids to sleep. Then I grab the laptop again, go to my couch, and start preparing everything to make it open source.

It’s been a while since I’ve worked open source—last time was withFlashListrepo. I rungitleaks. It makes sure there are no secrets exposed in the code. All fine.

I also run an agent on it: “Am I about to release something internal? No, all good.

So, I guess… we publish it? I am sweating.

F*ck it. I tell the agent: “Make it public.” And there it is. That was it? Okay, so it’s done.

I close my laptop and my body speaks to me right away. I'd been tense all day without realizing it.

It’s two days later now. When I wake up and check my phone, my X has exploded. I went from 600 followers to 800 in a couple of hours. Tobi just posted about our project on X. That explains it.

OK, well. I ran /autoresearch on the the liquid codebase.53% faster combined parse+render time, 61% fewer object allocations.This is probably somewhat overfit, but there are absolutely amazing ideas in this.pic.twitter.com/dpEJw7NpL4

— tobi lutke (@tobi) 
March 12, 2026

The best news: our project,pi-autoresearch, is getting a lot of attention. 100 stars. 200 stars. 500 stars. Dang, I’ve never seen something like this. At this point I realize that my Github account is full of dummy projects from 10 years ago. I feel a bit ashamed of my PHP past, so I start making everything private. Please don’t tell anyone.

At the moment of this writing,pi-autoresearchhas more than 3,600 stars on Github, and 200+ forks with variations of it. I still work actively on making it better, and internally we have an#autoresearch-winschannel where people from across the company share their achievements. So far we've seen cases of unit tests running 300 times faster, mounting react components 20% faster, reducing build time of multiple projects, improving the speed of playwright tests... We even managed to makepnpm run fasterthanks to it.

At this point, I hope I gave you enough reasons to try this out. Now it's your turn.Run it, and watch the numbers go down.

DC
 
by 
David Cortés
Published on
 
Apr 15, 2026
Share article
* Facebook
* Twitter
* LinkedIn
 
by 
David Cortés
Published on
 
Apr 15, 2026
 • 
8 minute read
Development
Introducing Ruvy
Developer Tooling
Building a ShopifyQL Code Editor
Apps
Shopify’s platform is the Web platform
Development
The Engineering Story Behind Flex Comp
Development
Introducing Ruvy

2023-10-18

Developer Tooling
Building a ShopifyQL Code Editor

2023-09-11

Apps
Shopify’s platform is the Web platform

2023-07-26

Development
The Engineering Story Behind Flex Comp

2022-10-05

Work from anywhere 
 with Shopify

See our open roles and learn more about our digital by design culture.

See open roles