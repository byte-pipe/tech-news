---
title: OpenAI and Anthropic cut their LLM prices by up to 80% within a few months. Why? | Max Woolf's Blog
url: https://minimaxir.com/2026/10/cheap-llms/
site_name: hackernews_api
content_file: hackernews_api-openai-and-anthropic-cut-their-llm-prices-by-up-to
fetched_at: '2026-10-26T17:16:00.182013'
original_url: https://minimaxir.com/2026/10/cheap-llms/
date: '2026-10-25'
published_date: '2026-10-25T14:00:00-07:00'
description: What is “the true cost of a token”?
tags:
- hackernews
- trending
---

Let’s look at a quick timeline of the major LLM model announcements from bothOpenAIandAnthropicover the past few months. All pricing numbers provided areinput MTok / output MTok / cache read MTok.

### June 26, 2026#

OpenAIannouncedGPT-5.6 Sol and Luna. Sol is the direct successor to GPT 5.5 at the same price of$5 / $30 / $0.50, while Luna is a small model specifically designed for cheaper use cases at$1 / $6 / $0.10. They also announced a Terra model that’s in between those two models, but few cared about it.

### June 30, 2026#

AnthropicannouncedClaude Sonnet 5, which Anthropic claimed to be closer to their Opus models, but feedback was mixed. Notably, it had launch pricing of$2 / $10 / $0.20which was initially supposed to be temporary but would go up.

### July 24, 2026#

AnthropicannouncedClaude Opus 5, which was a long-awaited major-version update given theimpactOpus 4.5 had on the rise of agentic coding, at a price of$5 / $25 / $0.50(similar to GPT-5.6 Sol). Although some of the provided benchmark results surprisingly exceeded those of the much larger Fable 5, real-world feedback was more mixed.

### July 30, 2026#

OpenAIannouncesthat they cut the price of GPT-5.6 Luna by80%(???) to$0.20 / $1.20 / $0.02.

Model quality vs. Cost-per-task for GPT-5.6 Luna after the massive price reduction. Top-and-left is better, and if OpenAI didn’t do the 80% price cut, it would have lost to DeepSeek V4 Pro. via OpenAI

### August 10, 2026#

Anthropicannouncesthe temporary Sonnet 5 price cut for the launch is now permanent.

### August 21, 2026#

OpenAIannouncesthat they are cutting the price for GPT-5.6 Sol by ~20% ($4 / $20 / $0.40) for the next three months.

### September 1, 2026#

AnthropicannouncedFable 5.1 at a price of$10 / $50 / $0.25, which, in addition to having strictly better benchmark performance in all areas than Fable 5 from June at$10 / $50 / $1, cut the cache read cost by 75%.

Cache read costs

When using agents for coding, cache read costs are the vast majority (96% - 99%) of the total token expenditure as the cache is what contains the entire previous conversation each turn. Additionally, the cache tends to be hit around 90 - 100% of the time (varies by the infrastructure of the LLM inference provider). Taken together, a 75% reduction in the cache read cost correlates to a 70-75% reduction in the cost of using the model—obviously notable, even if cache costs are typically a footnote!

### September 3, 2026#

OpenAIannouncedGPT-6 Astra, which is similar in size to Fable 5.1 and has similar pricing at$10 / $50 / $1but without the lower cache read cost. Astra’s model performance is indeed comparable to Fable.

### September 22, 2026#

OpenAIannouncedGPT-6 Sol at at a shocking price of$2 / $10 / $0.20that halves the input and output price relative to the temporarily-discounted GPT-5.6 Sol! They simultaneously released GPT-6 Luna also at half the input and output price ($0.10 / $0.50 / $0.01) of the previous version.

On thesame exact day, AnthropicannouncedClaude Opus 5.5, where it’s explicitly stated “Opus 5.5 requires less compute to serve than Opus 5, and its pricing reflects that”. Its price of$4 / $20 / $0.20is much lower in total than Opus 5’s due to a 20% input/output cost cut and a larger cache read cut, resulting in a total cost reduction of40-60%for a model that’s even better than Fable 5.1 (I have quite a lot of things to say about Opus 5.5, but that’s for another post).

### September 29, 2026#

It turned out that GPT-6 Sol was a dud performancewise, so a week later OpenAIannouncedGPT-6.1 Sol, which surprisingly has comparable performance to Astra (can confirm after personal use), but OpenAI casually cut the cache price in half ($2 / $10 / $0.10) matching Anthropic’s 5%-of-input cache read cost, making this model family cumulatively75%cheaper.

Overall, starting from the release of the GPT-5.6 model families in June to now, the cost of using these popular LLMs has cratered, which is not something I would have expected a year ago. These price cuts also apply to model usage from subscription agentic harnesses such asCodexandClaude Code. More importantly, these models do not appear to have cut any corners in terms of output quality to achieve their price cuts.

Data from Vercel’s AI model gateway supporting the decreasing cost-per-token trend to 43.3% of the April 2026 cost. However, aggregate spend has been increasing because the models are getting better faster than they’re getting cheaper!via Vercel

From the timeline above, there is a clear tit-for-tat between Anthropic and OpenAI, and it is reasonable to assume that these particular price cuts from OpenAI and Anthropic are in reaction to each other. However, no one cuts prices by80%unless there is some externality in play. So, what gives?

## The Behavioral Economics of LLMs and Competitor Pricing Pressure#

If you have been testing agents with new LLMs as they are released, it can be very difficult to differentiate them outside of subjective vibes. Since last November that launched the hypergrowth of agentic LLMs, models have become more of a commodity where it’s trivial to try a new model on your codebase with just a toggle in a harness likeOpenCodeandZed Agent, or a different API endpoint string throughOpenRouter, and as a result there is little moat. Additionally, there aremanycompetitors—not just large companies likeGoogleandMeta—who can provide models which aresufficient substitutesand therefore allow pricing pressure.

For open weight models, let’s take another look atDeepSeek Flash V4.1, which also recently released anupdated 1017 variant.

OpenRouter at this point is the place you go for open-weight models. Retrieved October 24th, 2026.

The original DeepSeek V4 Flash 0420was releasedin April 2026 at a price of$0.14 / $0.28 / $0.0028and went megaviral as a result, especially as OpenAI didn’t have a small-class model for simple tasks at the time. That$0.0028turned out to be the key, as a cache read proportion of 2% is substantially lower than the 5%-10% of the OpenAI and Anthropic models above, which makes the effective costevenlower than what is advertised. I suspect the 80% GPT-5.6 Luna price cut in July was meant to specifically compete with these smaller open-weight models. Now, the new DeepSeek Flash V4.1 1017 model performssignificantlybetter than DeepSeek Flash V4 benchmark-wise (45on theArtificial Analysisindex vs.24) and the cost from DeepSeek remains similar at$0.15 / $0.60 / $0.003. Note the operative words “from DeepSeek”.

On OpenRouter, any inference provider can list a model that they host, and when a user hits the OpenRouter API, the request is routed to one of those models—it’s routed to any available model by default for load balancing but the developer canspecify preferencessuch as “lowest price” in the API request. Back in May, Inotedthat there were 13 distinct providers hosting DeepSeek V4 Flash on OpenRouter. For the updated 1017 variant, there are now29distinct providers.

Providers for DeepSeek V4.1 Flash 1017 sorted by cache read cost. Retrieved October 24th, 2026.

However, looking at the effective input costs (which account for the interaction between cache read costs and cache hit rates), many distinct providers are close costwise.

Effective costs by endpoint, withCloudflareandDeepInfrawithin 10% of DeepSeek’s cost. Despite the fact that these models are the cheapest, note that these models only have a minority of the total token share. Retrieved October 24th, 2026.

OpenAI and Anthropic will have to differentiate from these open weight models with higher-quality models—they are currently doing a good job with that particularly with Opus 5.5—but they need tokeepdoing that, which is why billions of dollars are being invested into R&D. Open-weight models are catching up fast: just a few days ago,Moonshot AIannouncedKimi K3.1 Prowhich has comparable performance to Opus 5.5 (Kimi at55vs. Opus 5.5 at58) at half the input/output price and the same cache read cost ($2 / $10 / $0.20). It’s the same size and architecture asKimi K3which is currently being hosted by over 20 distinct inference providers: once the weights drop on November 4th, you can therefore expect most of them to support the new Kimi K3.1 Pro model at a roughly equivalent price. Notably, Moonshot AI itself is joining the price cut fun and priced Kimi K3.1 Pro at less than the original Kimi K3 ($3 / $15 / $0.30).

One recurring trend among vocal AI detractors is that the price of tokens has been kept artificially low to hook people into the LLM ecosystem, but then the prices will increase to “the true cost of a token” and the AI boosters will be screwed once the free ride ends. The theory is that OpenAI and Anthropic areloss-leadingjust likewhat Uber and Lyft did to the ridesharing industry in the 2010s, but unlike then, OpenAI and Anthropic are not a duopoly who have the sole power to set prices in the ecosystem and the barrier to entry for the inference industry is not as high. As long as these many inference providers can continue to serve models at a similar price and a similar quality to what OpenAI and Anthropic can provide, and switching cost is negligible, then the prices may continue to decreasemore. It’s no surprise both companies are trying to build moats to defend against this trend, such as a focus onenterprise commitmentsand personal agentic assistants likeOpenAI DotsandClaude Duet.

The idea that token prices will suddenly rise is more a fantasy that is not supported by both behavioral economics and the actual trends of LLM prices going downsignificantlyover the last few months for better models, and not just from OpenAI and Anthropic. As long as scalers can price at a cost-per-token lower than the revenue-per-token, then those inference providers will reduce token costs to compete with each other to a point that OpenAI/Anthropic will have to lower their prices to compete too. The 29 distinct providers on OpenRouter have little incentive to serve an unprofitable model (they would just stop serving it and use the compute capacity for a profitable model instead) and “the true cost of a token” may end up being where price equals marginal cost.

On that note, both OpenAI and Anthropic are indeed close to IPOing, which raises further questions about the price cuts.

## IPO Pumping#

The timing of these price cuts is notable because both OpenAI and Anthropic are rumored to be IPOing soon—OpenAI in 2027, and Anthropic within a couple months. So far, leaked financials from bothOpenAIandAnthropicshow unsurprisingly that they are losing billions due to R&D/scaling, albeit in both cases these reports do not account for the hyperexpansion of agentic LLM use over the past few months. Investors will scrutinize the massive negative profits and demand that they have a plan to turn things back around.

So, why did they cut their primary revenue source by up to 80%? That’s theoppositeof what you would want to do to look good on an S-1 prospectus! The profit margins on inference themselves likely tell a different story, with some reports saying the profit-per-token margins areas healthy as 80%with caveats. How much of a profit margin do they have after these major cuts?

Speaking personally, the price cuts have indeed affected how I spend on LLM agents, but not in the way I expect OpenAI/Anthropic want their typical customer to behave. I used to have a $100/month subscription to Codex (the 5x Pro plan) when GPT-5.6 Sol was the top model, and I managed to just fully exhaust all the usage included in the subscription despite getting annoyed withrandom usage resets. Once GPT-6.1 Sol released and I noticed that the cost of using it was effectively cut by 75%, you know what I did?

I cut the max usage quota to 1/5th after getting 4x more efficient usage of the same model, so it ends up roughly neutral and the obvious choice.

In fairness, the profit margins for subscriptions such as Claude Code and Codex are uncertain given their immense value relative to the API usage, and if there are capital crunches I suspect subscription value will be cut before the base price of the models. For example, at the same time GPT-6.1 Sol was announced, OpenAIcut the usage allowanceby 50% for the $200/month tier in Codex under the argument “to reflect our increasingly efficient models”—which istechnicallycorrect but it’s funny to put in writing.

I will beverycurious to see the Anthropic IPO prospectus and the inference profit margins once it becomes public soon.

I also question whether it’s good for OpenAI/Anthropic if they intentionally obsolete their more expensive models. After Opus 5.5 released a month ago, there hasn’t beenanydiscussion about either Fable 5.1 or GPT-6 Astra because Opus 5.5 is just that good.

Top-and-left.via Anthropic

I fully expect a Fable 5.2/GPT-6.1 Astra to release in a couple weeks and prove me wrong, and I will beverycurious to see how it will be priced.

Another less-cynical factor that could explain the price cuts is that LLM infrastructurehasimproved over the past few months—when Anthropic said “Opus 5.5 requires less compute to serve than Opus 5, and its pricing reflects that,” I believe it. One outcome that would be genuinely ironic is that if these models are more compute efficient, it reduces the need for these massive data center buildouts, which could cause cascading economic failures. However, that likely won’t happen since inference is only one part of the compute mix and those data centers are still needed for other parts of the pipeline.

Overall, the price cut is weird, but as a user I’m certainly not complaining! Open-weight models and secondary inference providers will continue to serve as an economic check on the prices of LLMs and other business shenanigans the large labs may concoct. Even if Anthropic’s and OpenAI’s IPOs are catastrophic and cause both companies to fold, it will not suddenly cause LLMs and agents as an industry to die.

* Max Woolf(@minimaxir) is formerly a Senior Data Scientist atBuzzFeedin San Francisco who works with AI/ML tools and open source projects.Max’s projects are funded by hisPatreon.