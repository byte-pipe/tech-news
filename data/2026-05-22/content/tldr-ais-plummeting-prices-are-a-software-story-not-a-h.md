---
title: AI's Plummeting Prices Are a Software Story, Not a Hardware One
url: https://weightythoughts.com/p/ais-plummeting-prices-are-a-software
site_name: tldr
content_file: tldr-ais-plummeting-prices-are-a-software-story-not-a-h
fetched_at: '2026-05-22T19:34:53.644692'
original_url: https://weightythoughts.com/p/ais-plummeting-prices-are-a-software
author: James Wang
date: '2026-05-22'
description: This has made local, open-weight models a real competitor to the frontier
tags:
- tldr
---

# AI's Plummeting Prices Are a Software Story, Not a Hardware One

### This has made local, open-weight models a real competitor to the frontier

James Wang
May 19, 2026
34
4
6
Share

Why is model inference getting cheaper? How did I drop a soon-to-be $2,000+/month bill for AI agents to next to nothing? And why are local models on commodity hardware potentially “good enough” for most people?

There are two macro trends here that feed directly into each other.

First,AI inference costs, as I’ve mentioned before, have been dropping 70-90% per year.Guido Appenzeller coined the term “LLMflation” through his original observation that costs have “dropped by a factor of 1,000 in three years.” No matter how many times I say it—and however many smart observers point it out—it still shocks most people because AIfeelslike it’s getting more expensive.

That’s because costs are dropping for thesame capacity(same model, same query), and we’re constantly ramping up what we use (bigger model, more expensive query). It’s the same reason why, despite Moore’s Law (which is slower than LLMflation), computers don’t cost $0.00001—we made computers bigger as we went, even as their cost exponentially plummeted.

This, however, is an old story. The interesting part of the piece is what drives this plummeting cost.It’s not (mainly) hardware. It’ssoftware.

A chart of the 10x drop per year from 
a16z
.

The second is a consequence of that:local, open-weight models on kind-of-old commodity hardware are becoming more and more competitive with models on the frontier.That obviously has big implications—and potential consequences—on what the frontier labs will ultimately be able to charge for the biggest models.

## Local AI + Old GPU Beats Frontier Model

I ended up researching and writing this piece accidentally.

I’ve always experimented with open-weight models myself, even when it made no sense to run them. My (public) history playing around with language models goes back to 2014, whenI published an implementation of a Google model paper for a data science certification. It’s always largely been a hobby/learning experience with no practical output—until recently.

A few weeks ago, I started playing with Qwen 3.6 27B—released about a month ago in April 2026. I didn’t run it on an Nvidia H100/B200 or some other data center GPU. I ran it on a consumer gaming card, an Nvidia RTX 3090 Ti, released in 2022.

While I heard good reviews of its capabilities, I didn’t expect much of it. To my surprise, itfeltlike running Claude Sonnet, Anthropic’s model one tier below the biggest model (the one they encourage people to run as their “everyday” model).

Sure, it isn’t Opus (Anthropic’s biggest, priciest model) or GPT-5.5 Pro (OpenAI’s biggest model), but this thing is open-weight/free and runs on a 4-year-old consumer-grade GPU!

Of course, “feelings” don’t mean much for model quality. Fortunately, Anthropic forced my hand on finding alternatives to how I run my rather extensive agent workflow.I detailed that workflow here (it’s still one of my most popular pieces ever). As a note, that was a (relative) eternity ago. I havewaymore agents running at this point—enough so that I need to actually have agents that manage my agents (I reinvented the org chart…).

How many agents 
do
 I have? Who can say anyway? I’m sure it’s like having too many children. At some point you just start rounding.

## The Coming Anthropic Agent Crackdown

Why did they force my hand? Well, starting June 15, 2026,claude -p—which, as permy agents article, is how most of my autonomous AI agents run—is no longer included in the subscription.Instead, you get $200 worth of credits, which at full API rates is 25x more expensive.So, how much does my agent stack cost? Am I somewhere close to $200?

Uh, no. My automated systems alone would run north of $2,000-$3,000/month at those rates, and the all-in personal number is, well, higher. I do not begrudge Anthropic cracking down on this. I may have been following guidelines from Boris Cherny, head of Claude Code, on acceptable use... but still, that’s a lot of money multiplied across a ton of users.

So an experiment that would otherwise have been “interesting but academic” suddenly had a budget attached to it. Dropping down from Opus to Sonnet for almost everything only got me down to around $1,000/month (and, for some of it, I didn’t get acceptable results from Sonnet).

For part of it, I could usecodex exec(OpenAI's equivalent of claude -p) on my $20 ChatGPT plan. Replace one frontier model with another. But $20 isn't enough—especially since I need GPT 5.5 for the harder tasks Sonnet fails at.

The question is, can Qwen 3.6 27B (meaning 27B parameters)reallystep in forSonnet(a model that likely has hundreds of billions of parameters)? Well, the public benchmarks seem to suggest it can.

Qwen 3.6 27B holding its own against frontier offerings on Terminal-Bench. 
Qwen’s model card has plenty of other benchmarks too.

Benchmarks don’t always reflect real performance, however. So I ran a few side-by-side benchmarks on the workloads I cared most about: daily briefing synthesis, chart annotation (especially for various medical applications and AI papers), and arXiv (research paper preprint archive) triage.

Same prompts, same context, four models. For the paper-triage task, “quality” is partly a matter of taste, so I used Opus and Codex as a consensus jury—where they agree on the threshold, that’s the closest proxy I have to ground truth without hand-labeling everything myself.

As a whole, the briefings were largely the same across all of them (so Opus was always overkill; Qwen is fine). Neither Qwen nor Sonnet was good enough for annotation (so I moved it to Codex). Finally, Sonnet was actuallyworsethan Qwen for paper scoring.

This means a 27B-parameter open-weight model, quantized to Q4, on a four-year-old consumer GPU, is doing comparable work to a paid mid-tier cloud API. Yes, it’s not Anthropic’s Opus, but it’s roughly matching Sonnet—a model still very much in Anthropic’s frontier lineup.

Qwen 3.6 27B is a particular standout, and it’s unlikely to beat Sonnet oneveryworkflow. However, it and many recent, “small” open-weight models are at everyday-use quality (not “small language models” but small “large language models”). Heck, Qwen 3.6 27B even has vision capabilities!

While, as perNathan Lambert, open-weight models have been in“perpetual catch-up”and underappreciated generally, what strikes me is how far down the hardware requirements curve we’ve come for “acceptable” results.

After all of these moves—the scoring workloadalonewas ~$120/month if done on Sonnet but became $0—I got my projectedclaude -pbudget to under $200/month with a comfortable margin.

(As a note for astute readers, my own power cost is likely not truly $0—especially not being in the Bay Area and having PG&E grace me with some of the most expensive power rates in the country. Still, even with those rates, it’s an order of magnitude less. Definitely less than $0.004 per run.)

Thanks for reading Weighty Thoughts! Subscribe for free to receive new posts and support my work.

Subscribe

## The Moving Frontier is “Model”

At one point, an old consumer card like the 3090 Ti couldn’t run anything reasonably competitive with a frontier model. Now, it’s capable of running a model in the same league as a core offering from the top AI lab in the world. Myhardwarestayed constant—no Santa Claus secretly upgraded my GPU—so obviously something else must have changed.

InAugust 2023, I wrote a piece called “Compute is Overrated as AI’s Bottleneck,”and the basic argument was that under the Model-Data-Compute framework, themodelwas doing more of the work than the breathless GPU extrapolations of the day suggested. For me, as per my book, I define “model” as all of the algorithmsandtechniques that go into making AI work—including post-training, RLHF... but also base improvements in the underlying model architectures themselves.

At the time, the prevailing view was that AI training costs would exceed US GDP by 2035 if you just drew the curve forward. My argument—which I'm pleased to say held up—was that “MOAR compute!” mattered less than the architectural and algorithmic gains.

Deep learning (and CNNs, transformers, and more) enabled the current boom, not just “infinite compute”—and new techniques are helping make it cheap enough that anything that can be AI,will be AI.

(Though, as permy book, not everything will be AI… because not everything can be.)

Source: Center for Emerging Technology and Security (AI and Compute Brief 2022). Obviously, this didn’t quite happen…

## Hardware vs. Software, with Actual Numbers

So, I have a nice anecdote. What does this look like in the broader landscape?

For the recent 2024-2025 window, the best available decompositions suggest that a majority of inference efficiency gains came from non-hardware technical progress—especially model-side or algorithmic improvements—rather than silicon alone. Hardware accounts for roughly one-quarter to one-third, depending on methodology.

MIT FutureTech (Gundlach et al., Nov 2025)
 and 
Stanford Hazy (Saad-Falcon et al., Nov 2025)
.

In MIT’s paper, the authors include non-hardware technical improvements, such as data, distillation, MoE, and related efficiency improvements. Stanford mainly focuses on model-side improvements (in local models across consumer/edge hardware).

Regardless of methodology, both reports agree that most of the decline is not silicon.

Perhaps not all of it isliteralsoftware, but it is “model” writ large, in the way I use it in Model-Data-Compute (“model” would have been confusing in the title without context, though).

There’s also a useful natural experiment beyond my own hardware.

NVIDIA’s own benchmarks show that H100 throughput on Llama 2 70B improved by roughly 1.5× over a year on identical silicon, from software updates alone. That’s a hardware-generation-sized gain delivered without buying new hardware. H200 added another ~28% on top, and Blackwell another ~3× on top of that—but the same-hardware software work is meaningfully larger than people give it credit for.

On a much smaller scale, the same thing keeps happening to my setup! Software keeps making it better.

While I was working on this piece (literally), allama.cpp pull request adding multi-token speculative decodingmerged and roughly doubled the throughput of my Qwen 3.6 27B on the same 3090 Ti:

My throughput (speed) basically doubled overnight for free (for nitpickers, yes, I did have to slightly decrease my context window—but it basically makes no difference in practice given the rather marginal change).

## Model Improvements, Spotlighted

Software improvements, tricks, and techniques… that’s great and all, but just to be clear, even though we’ve stuck with transformers, therehasbeen a substantial shift in “models.”

Among the notable advances in architecture or formulation have been MoE (Mixture of Experts), which many of the big models have been based on (most famously, DeepSeek v3/R1, which caused the “DeepSeek moment”), distillation (which helps larger models train smaller ones—enabling bigger model breakthroughs to “trickle down” to smaller ones), and quantization.

Quantization is part of what helped Qwen 3.6 27B run on my 3090 Ti—which would barely fit the full size and likely have no context window (read here for a reminderon what that is and why it’s important). However, it has also allowed many hyperscalers and labs, similar to distillation, to bring down the cost of running these models while preserving most of their capacity/performance.

## Hardware’s Still Important… Just Not as Much as Most People Think

Of course, hardware is still important.Chinese labs have a thing or two they could tell you about that…

HBM (high-bandwidth memory) on Nvidia’s H200 versus H100—which have the same compute capacity, just more memory bandwidth—gave roughly a 40% “free” inference speedup on memory-bound workloads. That’s pure hardware improvement.

Going from Ampere to Hopper to Blackwell for Nvidia has created significant improvements (that’s why people buy their chips!).Cerebras, an AI chip company, went public last week at a peak of just under $100B(and has since dropped materially...).Groq was purchased by Nvidia late last year for $20B.

These hardware improvements obviously matter. Still, the unspoken consensus is that the main binding constraint of AI is GPUs and chips. As we’ve seen in multiple ways, that’s wrong.

## Why This All Matters

Inmy book, I wrote that “everything that can be AI, will be.” The reason is this cost curve for AI inference.

It’s faster than Moore’s Law, which is what got us from giant mainframes in 1980 to smartphones in our pockets, which are a million times more powerful than those room-sized machines.

Epoch AI estimatesfrontier capability is now runnable on a single top-end consumer GPU within 6-12 months of being released at the frontier. That’s more or less what I saw (and was surprised by) when I ran Qwen 3.6 27B on my 3090 Ti.

Of course, this also means that if you try to raise your prices (or, as Anthropic did, squeeze out certain use cases I have), people have alotof other options. That puts a cap on the pricing power of the frontier labs.

A long time ago (i.e., April last year),I discussed two possible paths for frontier labs—fixed costs for training could keep increasing and they could become natural monopolies... or overall costs could fall through the floor and their capabilities could become commodities.

It’s not necessarily going to truly be that binary—and it’s still early on—but cloud prices for open-weight models are converging at the local hardware cost of electricity—roughly $0.20-$0.50 per million tokens. Anthropic commands ahugepremium per token—which I’ve been happy to pay—but would most people stay if they 10x’d their price? 100x? I suspect not.

Despite Anthropic's crackdown, I can keep running a lot of AI agents—because, for better or worse, I don't actually need Claude. I subbed it out with ChatGPT and Qwen without any issue. That says something about the future, even as Anthropic enjoys its time in the sun as the “leading lab.”

After all, if things keep going this way, we’ll be running frontier-level models on our phones in 5-10 years. That’d be because of both hardwareandsoftware (though probably still mostly software).

# Thanks for reading!

I hope you enjoyed this article. If you’d like to learn more about AI’s past, present, and future in an easy-to-understand way, I’ve published a book titledWhat You Need to Know About AI.

You can order the book onAmazon,Barnes & Noble,Bookshop, or pick up a copy in-person at alocal bookstore.

34
4
6
Share