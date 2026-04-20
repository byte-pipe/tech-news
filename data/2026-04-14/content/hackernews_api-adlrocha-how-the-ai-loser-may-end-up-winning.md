---
title: '@adlrocha - How the "AI Loser" may end up winning'
url: https://adlrocha.substack.com/p/adlrocha-how-the-ai-loser-may-end
site_name: hackernews_api
content_file: hackernews_api-adlrocha-how-the-ai-loser-may-end-up-winning
fetched_at: '2026-04-14T06:00:16.812714'
original_url: https://adlrocha.substack.com/p/adlrocha-how-the-ai-loser-may-end
author: adlrocha
date: '2026-04-13'
description: Apple’s accidental moat
tags:
- hackernews
- trending
---

# @adlrocha - How the "AI Loser" may end up winning

### Apple’s accidental moat

adlrocha
Apr 12, 2026
36
6
10
Share

A few weeks ago I wrote about how I thoughtintelligence is becoming a commodity. The idea is quite straightforward, and widespread now:when everyone races to build the best model, the models get better, but so does every other model eventually.Every dollar spent on a bigger training run makes the previous one cheaper. The distance between frontier, second-best, and open-source alternatives is collapsing fast(actually Gemma4, Kimi K2.5 and GLM 5.1 are becoming my bedside models these days). Even more, as models become better, the unit of intelligence that can be deployed in local hardware with lower hardware capabilities increases significantly.

The irony of this situation is that this commoditisation of intelligenceis benefiting the company that everyone was framing as the “AI loser”: Apple

## The company that “lost”

There’s a version of the last three years where Apple genuinely failed at AI. They had Siri before anyone had a serious voice assistant, and then watched how ChatGPT ate their lunch already since their first release(even before they had introduced their native voice interaction). Apple didn’t have a flagship frontier(or even a vanity open-source)model, no $500B compute commitment with the usual suspects. Meanwhile, the rest of theAI labs and big tech companies were racing to win the next state-of-the-art benchmark by burning bags of cash.

What this also meant is that while these companies were burning money at a rate that would make a sovereign wealth fund uncomfortable, Apple was(and still is)sitting in a pile of undeployed cash (to the point of even increasing their stock buybacks)giving them optionality.

To me, OpenAI is the most paradigmatic example of this “infinite money burning machine”. OpenAI raised at a$300B valuationand then shut down Sora, the video product they’d been positioning as a creative industry flagship, because it was running atroughly $15M a day in costs against $2.1M in daily revenue. Disney had already signed a three-year licensing deal for Sora to generate content from Marvel, Pixar, and Star Wars characters. They were finalising a$1B equity stake in OpenAI. When Sora died, so did the billion. A $1B investment evaporated, because the product it was staked on couldn’t pay for itself(reducing their buffer that accommodates their daily burn).

On the infrastructure side: OpenAI signed non-binding letters of intent with Samsung and SK Hynix forup to 900,000 DRAM wafers per month, roughly 40% of global output. These were of course non-binding. Micron, reading the demand signal,shut down its 29-year-old Crucial consumer memory brandto redirect all capacity toward AI customers. ThenStargate Texas was cancelled, OpenAI and Oracle couldn’t agree terms, and the demand that had justified Micron’s entire strategic pivot simply vanished.Micron’s stock crashed.

I don’t know about you, butI don’t see these behaviours as those of someone that is winning the AI race,independently of how good their models do in benchmarks, and how much they are burning in infrastructure.A small miscalculation in the expected revenue, and you are out of the game(I am actually of the opinion that without some kind of bailout, OpenAI could be bankrupt in the next 18-24 months, but I am horrible at predictions).

## From intelligence to capabilities

My sense is that the labs’ bet was always that raw model capability, i.e. intelligence, along with the infrastructure required to run them would stay scarce.Those who manage to secure the best model and the infrastructure to run it at scale would get the best moat. But I am afraid that having the best model in itself may not be enough moving forward. Less capable models are becoming as capable as previous versions of the frontier models.

The best recent example I can think of isGemma 4, Google’s open-weight model. It was built to run on a phone, scores 85.2% on MMLU Pro and matches Claude Sonnet 4.5 Thinking on the Arena leaderboard.2 million downloads in its first week. Models that would have been state-of-the-art eighteen months ago now run on a laptop, and they get better every quarter.

If you haven’t tried Gemma4 yourself I highly recommend it. I am running it on my AMD Ryzen AI Max+, and its performance in terms of tokens per second and intelligence are so good that I have already migrated some of my personal tools to use this model as the backend without visibly impacting their output. This trend can really change in the next few months way we access intelligence.

I feel that some of the labs see this coming. Anthropic has been particularly aggressive about it and they are releasingnew(actually useful)tools every day that work like a charm with their models in order to lock users into their ecosystem.Claude Codefor developers,Claude Coworkfor teams, the recentClaude Managed Sessions to orchestrate agents, all designed to put Claude inside workflows people are already in.

The logic behind it: if the model itself won’t hold the moat, capture the usage layer and make switching painful.I think this is brilliant, and seeing how much Anthropic is growing in number of users and revenue, it seems to be paying off. The economics of their plans are still rough, though.One analysisfound a max-plan subscriber consuming $27,000 worth of compute with their 200$ Max subscription. The labs are subsidising the demand they’re chasing, which justifies their level of burn (let’s see for how long they can afford these subsidies).

Apple, by contrast, has spent almost nothing on AI infrastructure and subsidising users’ token burn. And this may begiving them more optionality and leverage than any of the other companiesthat jumped heads first into the AI race.

## Context is all you need

Inthat earlier post, I argued that if intelligence becomes abundant, context becomes the scarce resource.A model that can reason about anything but knows nothing aboutyouor the environment it operates in is a generic tool. What makes AI genuinely useful day-to-day is reasoningpluspersonal context: your messages, your calendar, your code, your tools, your health data, your photos, your habits. I think here is where Anthropic is making an amazing job with their “Claude suite”.

But Apple already has all this context and access to your environment through their 2.5 billion active devices. Each one is a context mine that users have been filling for years. Health data from Apple Watch. Every photo taken on an iPhone. Notes, messages, location history, app behaviour, emails, and awareness of your environment through the pool of sensors of your device.Why build a commodity when they already have the context that can become their moat?

And they even have the ability to keep all this data on-device, which is where the“Privacy. That’s iPhone”positioning becomes something more than a PR strategy, and which could actually make a comeback to become one of their core value propositions.Apple spent years using privacy as a differentiator against the ad-driven models of Google and Meta. It worked, but it always felt a bit abstract and, honestly, fake.Now it could become really concrete. Would you hand OpenAI your medical records and fifteen years of photos to get better AI answers? Probably not. Some are, but I personally wouldn’t like Sam to have that personal data from me. Would you let a model running entirely on your device (no network request, no data leaving your phone) access all of that? That’s a different question. The on-device model gets full contextbecauseit never leaves the hardware. Apple built the reputation and the architecture for this when no one else thought it mattered.

Of course, there are still technological barriers to make this possible, but I feel like we may be getting there.

In this context,theGemini deal, where Apple signed a $1B to license Google’s frontier model for the queries that need cloud-scale reasoning, makes total sense.Apple didn’t build a frontier model. They bought access to one, at a price that’s rounding error against OpenAI’s weekly compute bill. What they kept in-house: the context layer, the on-device stack, and the operating system that mediates everything.

## Apple’s chips turned out to matter

Turns out Apple had another unexpected lever for AI as shown with theMac Mini craze after OpenClaw’s release. Apple Silicon wasn’t built specifically for AI, it was built for efficiency, for battery life, for thermal performance, for the hardware/software co-design that Apple had been running for fifteen years. But it turned out to be the perfect architecture to run local models efficiently.

The key decision is unified memory.On a conventional architecture (that of most laptops, and even traditional data center-grade GPUs) the CPU and GPU are separate chips with separate memory pools. Moving data between them is slow and power-hungry. Nvidia’s GPUs are extremely fast at matrix operations, but they sit on the other side of a PCIe bus from the CPU, and feeding them is a constant bottleneck (as discussed when presenting thedifference between DRAM and HBM in this post from a few weeks ago).

Apple’s M-series and A-series chips put the CPU, GPU, and Neural Engine (their proprietary accelerator)on the same die, sharing one high-bandwidth memory pool.No bus crossing, no transfer overhead, no latency switching between CPU and GPU work. For video editing or compiling Xcode, this is a nice efficiency win. For LLM inference, this has been key.

As described alsoin my post about RAM memoryandTurboQuant,LLM inference is currently memory-bandwidth bound, not compute bound.The bottleneck isn’t so much how fast you can multiply matrices, it’s how fast you can stream model weights from memory into the compute units, and how big of a KV cache you can store to avoid having to re-compute it. Apple’s unified pool gives every compute unit direct, high-bandwidth access to the same memory simultaneously. That’s exactly the operation inference needs.

This is what makes theLLM in a Flashtechnique work so well on Apple hardware. Someonerecently ran Qwen 397B, a 209GB model, on an M3 Max Mac at ~5.7 tokens per second, using only 5.5GB of active RAM. The weights live on the SSD and stream in at ~17.5 GB/s as needed. This works because Qwen is a mixture-of-experts architecture: each token only activates a small subset of expert layers, so you only ever need a fraction of the 209GB resident in memory. The SSD throughput Apple achieves (faster than their own figures from the original LLM in a Flash paper) comes from storage architecture they built for iPhone responsiveness, not AI.Claude wrote the ~5,000 lines of Objective-C and Metal shadersto make it all work. A 400-billion-parameter model, on a consumer laptop, from 5.5GB of RAM (another win of theautoresearch flow discussed in this newsletter).

What I find more interesting about all of this is the platform dynamic that this can result in. Think about the App Store.Apple didn’t build the apps, they built the platform where apps ran best, and the ecosystem followed. Developers didn’t target iOS because Apple asked, they targeted it because the users were there, the tooling was good, the hardware was consistent. My feeling is that the same thing could happen now with local inference.MLX is already a de facto framework for on-device AI.Gemma, Qwen, Mistral, the most relevant model architectures have MLX support. Apple doesn’t need to win the model race if theymanage to become the de-facto platform where the models(or the agents that use them) run. Again, a great example of this is the Mac Mini craze after OpenClaw went viral.

## Pure strategy, luck, or a bit of both?

I keep going back and forth on this, honestly, andI still don’t know if this was Apple’s strategy all along, or they didn’t feel in the position to make a bet and are just flowing as the events unfoldmaximising their optionality.

The hardware/software co-design strategy has been a key focus for years, and one that I’ve always agreed on myself(as an electrical engineering by training, I’ve always been into hardware/software co-design). If you can afford it, I think that’s the right approach. The privacy positioning, the on-device processing focus, the decision to build their own silicon when the rest of the industry was happy buying Nvidia and Intel, all of those were choices Apple made when they were commercially risky and the direction wasn’t obvious. Is it true that they were made with cost and governance in mind, not AI, but it turned out well for them.

What Apple couldn’t have planned(or could they?)is thattheir unified memory architecture would be a perfect fit for LLMs, and that open-weight models would get this capable, this fast,removing the need for huge hardware investment for AI infrastructure from their side. That the model race would commoditise intelligence as quickly as it did. Or that someone would stream a 400B parameter model from an SSD and it would actually work.

So some of this is luck. But it’s the kind of luck that finds you when you built the right foundation, even if you built it for completely different reasons.They were definitely well-positioned.

The rest of the industry spent three years racing to see who could build the best model with Apple looking from the sidelines, waiting to understand how their devices and own ecosystem could fit in this future.I don’t know if this is exactly the case, but I feel this was smart. Risky but smart.

I genuinely don’t know how this plays out over the next few years. The labs are not standing still, and Apple’s AI track record(looking at you, Siri, you already suck a bit) is not exactly flawless. But it’s hard to imagine a world where 2.5 billion devices, carrying your entire personal context, running capable models locally on purpose-built silicon, with Gemini on-call for the hard stuff,incurring in variable cost for inference instead of expensive CAPEX investment could be a bad position to be in a future where AI is everywhere.

Whether that was strategy or fortune, I’ll leave for you to decide. And if you do, please let me know what you think about it. My TL;DR is that, to my surprise, I am still bullish about Apple and their relevance in an AI-centric future.

Until next week!

Disclaimer: To frame the opinion of this post, I just want to be clear about the fact that I am not one of those Apple fan boys. Proof of this is that this post was written from a Linux machine and that I don’t even own a Mac :)

36
6
10
Share
