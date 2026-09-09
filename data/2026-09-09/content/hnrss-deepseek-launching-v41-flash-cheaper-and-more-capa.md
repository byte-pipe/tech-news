---
title: DeepSeek launching v4.1 flash cheaper and more capable than v4 pro | Hacker News
url: https://news.ycombinator.com/item?id=49624603
site_name: hnrss
content_file: hnrss-deepseek-launching-v41-flash-cheaper-and-more-capa
fetched_at: '2026-09-09T15:30:01.278047'
original_url: https://news.ycombinator.com/item?id=49624603
date: '2026-09-09'
description: DeepSeek launching v4.1 flash cheaper and more capable than v4 pro
tags:
- hackernews
- hnrss
---

Hacker News
new
 | 
past
 | 
comments
 | 
ask
 | 
show
 | 
jobs
 | 
submit
login
DeepSeek launching v4.1 flash cheaper and more capable than v4 pro
262 points
 by 
nickweb
 
4 hours ago
 
 | 
hide
 | 
past
 | 
favorite
 | 
130 comments
DSeek plans to officially release the V4.1 Flash model around September 10, 2026 (Beijing Time). After extensive internal and external testing, V4.1 Flash has comprehensively surpassed V4 Pro across all key metrics, including performance, cost, speed, and task completion time. In keeping with our commitment to user responsibility, following the official launch of V4.1 Flash and prior to the release of V4.1 Pro, all requests to the Pro model will be routed to V4.1 Flash and billed at Flash's price. If you encounter any issues during your comparative testing between V4 Pro and V4.1 Flash, please do not hesitate to reach out to us with your feedback. Thank you for your support!

We will adjust the pricing for the Flash series effective from 12:00 Beijing Time on September 10, 2026. During off-peak hours, the unit price will be $0.003 for input cache hits, $0.15 for input cache misses, and $0.6 for output. Peak-hour prices will be double the off-peak rates. Please plan your usage accordingly.

 
help

aftbit
 
1 hour ago
 
 | 
next
 
[–]

>In keeping with our commitment to user responsibility, following the official launch of V4.1 Flash and prior to the release of V4.1 Pro, all requests to the Pro model will be routed to V4.1 Flash and billed at Flash's price

Please don't do this kind of thing. If a user has validated a workflow on V4 Pro, they might not want to suddenly start testing it in production on V4.1 Flash. Instead, keep V4 Pro around but deprecated for a defined period of time, then remove it.At least as open weights models, it's possible to use something like Together.ai or OpenRouter to run the V4 Pro model as long as other providers keep it up.

reply

jmathai
 
0 minutes ago
 
 | 
parent
 | 
next
 
[–]

LLMs add enough nondeterminism to a workflow. Swapping them without the user knowing adds substantially more.

reply

nolok
 
42 minutes ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Usually I would very much agree with you, but those things are not deterministic so if that's an issue for you you're probably not making the right choices.

reply

tomrod
 
37 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Nope, strong disagree. The model is one small part of the process harness; behaviors are usually routable with expected propensities. Unexpected model changes avoiding change management messes with monitoring and observability thresholds. Stochastic controls are a real thing when you have your distributions defined; your workflows on a new model will throw that expected prior out the window.

reply

gcanyon
 
35 minutes ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

They’re nondeterministic at a fine level, but can be “deterministic” at a more general level: e.g. you might know that one model will always return properly formatted json when asked. That might not be true of the replacement, even if it is in general “better” and cheaper.

Just the risk of such a thing means regression testing every time you update the model, and you want to be able to run that testing on your schedule rather than having it forced on you.

reply

packetlost
 
32 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> They’re nondeterministic at a fine level, but can be “deterministic” at a more general level: e.g. you might know that one model will always return properly formatted json when asked. That might not be true of the replacement, even if it is in general “better” and cheaper.

This isn't true. Even Sol messes up JSON formatting for me on occasion.Do not delude yourself into thinking these things are reliable. They are not.

reply

idiotsecant
 
32 minutes ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Models are not deterministic, but they do have a 
flavor
. When that flavor changes it can change the nature of output in a way that is undesirable.

Sort of like shooting a rifle - where the bullets hit is (to some order of magnitude, no philosophizing please) non-deterministic, but different very similar rifles will group differently and need to be appropriately adjusted to hit anything.

reply

tomrod
 
23 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

This is a great way to think of it, idiotsecant.

That flavor profile is known -- it's typical behavioral distribution is somewhat understood (and, often, common failure modes addressed). If JSON breaks about 20% of the time, and that drops for 2% or blows up to 90%, it can drive all sorts of issues (not the least, costs for retries).

reply

samuelknight
 
7 minutes ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

In this case, Deepseek organization is under a lot of pressure due to compute constraints. It would be better if they just throw a 404 instead of rerouting though so customers are not surprised by subtle changes in behavior.

reply

KoolKat23
 
1 hour ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I imagine they need the compute. Can expand market share with more users for same amount of compute.

But I agree with you. I have a dumb workflow that worked well with v4-flash-0731 and I suspect is directing to a newer model that now breaks it.

reply

petu
 
33 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

4.1 releases tomorrow, right now you're supposed to be served by same old model

reply

weego
 
36 minutes ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

You absolutely cannot consider an LLM production build number something to be pinned against as a static dependency in a product chain, so it's a non-issue.

reply

samuelknight
 
11 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yes you can and you should. Providers have SLAs for when models roll off support and this has been the case for APIs long before LLMs. For example 
https://platform.claude.com/docs/en/about-claude/model-depre...
 and 
https://developers.openai.com/api/docs/deprecations

reply

weird-eye-issue
 
31 minutes ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

It's very easy to tell who is not running production applications using these models based on comments like this

reply

Xunjin
 
15 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Let me give you the benefit of the doubt, can you expand what you run in production?

reply

m3kw9
 
1 hour ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

They expect vibe coders to use their models only lol

reply

jiehong
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

Sounds nice!

But, the web ui chat version of flash has very poor language following abilities in my experience:You may ask it something in English, and get a thinking chain in Chinese with an answer in Chinese, or an English thinking chain and an English answer. Using the retry button on the same question has a 50/50 chance of any of those results.Sometimes, asking something in English, but where information are mostly in another language may make the answer in the language where data has been found. The other day, I asked something about a local German thing, in English, and I got an answer in German instead. It’s as if all the language data stirred it away from the language of the user’s question.

reply

lampe3
 
31 minutes ago
 
 | 
parent
 | 
next
 
[–]

All flash llms have this problems. gemini. I start to a new chat write in german and suddenly it answers in english.

I take the free chat gpt one writ with it in polish suddenly english.

reply

djeastm
 
10 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

You see this on Reddit where the bot accounts will just comment in German, French or Italian randomly (and other bot accounts responding to it won't even bat an eye, responding in English as if it's the most natural thing in the world)

reply

prussia
 
0 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It's a bit more complicated than that because Reddit now automatically tries to translate comments not in the user's language.
swiftcoder
 
2 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I've hit this too, but you can just add "in English" to steer it

reply

gentlewater
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I finally uninstalled the app yesterday after giving it plenty of chances over several months. Yesterday, I asked it whether «DeepSeek has fixed the issue where it erroneously answers in Chinese?» and it answered in Chinese.

reply

elaus
 
35 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

So you did not do what the post you replied to suggested?

reply

gentlewater
 
13 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Oh, I’ve tried that too. It will promise to keep it in English from here on out, then switch back to Chinese after two or three exchanges. When ever it needs to do a web search, it seems to load so much Chinese text that it forgets any language instructions. Just thought my experience yesterday was more to the point. Right now the chat is absolutely hopeless.

reply

swiftcoder
 
5 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

huh. mine only does this on the first turn on a new computer. Once I've told it once it seems to be entirely sticky on that device from then on
michimagdesign
 
27 minutes ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

This shouldn’t be a user-facing issue. The web UI should inject the account’s language setting or solve it like competitors. They’ve mentioned giving it multiple chances but it’s still not fixed.

reply

alightsoul
 
11 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Anthropic does the same thing but it's not problem

reply

mattmcal
 
1 hour ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

It's not just web chat, V4 Flash 7/31 suffers from a lot of pathological behavior in coding harnesses as well, e.g. infinite loops, hallucinations, premature termination, and invalid tool calls.

reply

pimeys
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

All of these flash models have this. You have to build your harness so that it deals with it. Infinite loops are solved by having an error message that says what to do differently on failure, invalid tool calls are solved by making the tool schema less strict and detect things in the runtime etc.

Hallucinations you can't fix. Gemini is a bit worse there than DeepSeek, but there's not much research on how to fix that. The only one is the CaMeL paper by Google, where you tag every prompt and result and then for every assistant response or tool call you first check where it got that data and error if you notice fabrication. This one is really annoying to implement.With larger models the fabrication starts when the context grows or if you have too many tools, for flash models it's much earlier. We use the flash models for repetitive agentic tasks, where the prompt defines clearly what to do and how. The whole run is about 4-5 steps typically, and context size stays in the comfort zone.

reply

K0IN
 
30 minutes ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I have used the flash model for over 3b tokens and ofc. I saw some hallucinations and premature termination (I also get this on Astra - way more often than with deepseek v4 flash), but I never had a infinite loop (using the copilot as harness).

reply

CharlesW
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

FWIW, I haven’t experienced any of that using V4 Flash via DeepSeek in omp. What’s your coding harness and inference provider?

reply

bendangelo
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

This never happens on the deepseek api. It’s always a different provider using lower quants.

reply

cheema33
 
7 minutes ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Yep. I faced the exact same issue. Too many times. And then just gave up.

reply

apexalpha
 
2 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I have the same issue, sometimes.

I initially thought it was a trick, that using Chinese chars is somehow more info dense and it saves tokens to 'think' in Chinese.But later on it became more erratic. I still wonder if token reduction would work that way.

reply

el_io
 
2 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I'm also totally not sure why it do that, but I guess because they're searching from China and web results comeback in Chinese so the model start using that.

reply

kgeist
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

The web UI's system prompt is also probably in Chinese

reply

miroljub
 
1 hour ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Yep, the same issue. I even defined a dictionary shortcut on my phone to expand aie to "Answer in English!", but every so often it takes 5 times to force it to switch to English.

Interesting though, when I ask questions in German or my native language, I rarely get Chinese answers. Looks like English is most affected.API never answers in Chinese.

reply

tinyhouse
 
1 hour ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I've been working with Pro and it's been great so far.

reply

epolanski
 
2 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I've occasionally got chinese characters in anthropic/openai's responses too, locally on codex/claude.

Hasn't happened in a while, last time was when I was testing fable 5 in june.

reply

oefrha
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I don’t know what model codex uses for session summarization (I use Pro subscription, no third party models), but I get Chinese summaries from time to time, when the only Chinese that could have appeared in the session would be an i18n strings file that it may or may not have loaded. Very puzzling. Last happened yesterday.

reply

oefrha
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

Source is apparently a banner announcement on 
https://platform.deepseek.com/usage
. Had me searching for a couple minutes...

reply

nickweb
 
3 hours ago
 
 | 
parent
 | 
next
 
[–]

I swear I put that at the start of the post. Must've managed to miss it when copy and pasting!

reply

NooneAtAll3
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

can't you edit it?

reply

nickweb
 
21 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

No. Posts are only editable for a small window of time.

reply

simonw
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

> all requests to the Pro model will be routed to V4.1 Flash and billed at Flash's price

If I'd carefully tested and optimized prompts against Pro I wouldn't be keen on this particular news. I feel like API model providers should lean towardsnotswapping out models on their paying customers, no matter how much "better" the new model is meant to be.

reply

tjwebbnorfolk
 
1 hour ago
 
 | 
parent
 | 
next
 
[–]

Sure, but if a company decided to place a remote chinese hedge fund's API at the center of a critical business workflow, this is a lesson better learned sooner rather than later.

reply

k__
 
55 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

At least they can use another provider or self-host.

reply

EbNar
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

Since a few months, I almost exclusively use the Chinese "flash" models for my needs. They are a joy and they cost pennies per answer. Great job.

reply

ActionHank
 
2 hours ago
 
 | 
parent
 | 
next
 
[–]

I am legitimately more excited for this release than any frontier models at this point.

I don't need a model that can invent new mathematics. I need something that is fast, cheap, and consistent. Give me that and I can build and scale.

reply

Oras
 
10 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

LLMs are not consistent

reply

pimeys
 
2 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Yes. I'm working in the agent industry and my god are we excited on new versions of Chinese flash models. The direct competition is Gemini Flash, and these models are much better on agentic tasks with fraction of the task price compared to Gemini. Things like oh here's a set of simple instructions for you to follow, call these tools, return this report. 20-30% of the price per task. And especially Deepseek Flash produces better quality than Gemini does.

Where Gemini still wins is non-text input what Deepseek cannot do, yet, and Deepseek Flash has this thing of cheaper models where a failing tool call can derail your agent to a retry loop if you're not careful on instructions in the error message.If they fix and make the tool calls to work better in non-optimal situations, it's much easier to switch from Gemini without a few weeks of evals and bugfixing.

reply

bitexploder
 
21 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Which versions of flash and at what thinking levels? Which chinese flash models and at what thinking levels? What tasks? What completion rates? How was quality evaluated?

reply

pimeys
 
13 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

- Which versions: 3.6 vs 3.7 vs. 3.8 for Gemini Flash, and v4 0731 for Deepseek v4 Flash, and GLM 5.3 Flash

- Medium for Gemini, high for Deepseek.- Things like find information, then understand something about it, then send a slack message or email etc.- Completion rates somewhere in 80-90%, Deepseek a bit better than Gemini- Quality evaluated by Fable 5.1 and Astra 6.0 acting as a rubric judge.Gemini quality would probably be better with high thinking level, but that would be 40% more expensive. And Deepseek is already third the price of Gemini.

reply

urieiejr
 
59 minutes ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

translation

I make vaporware that doesnt do shit reliably and this chinese crap spouts plausible demos and spam calls more cheaply than the competition saaar

reply

pimeys
 
43 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Well, it's much more than that. In general everybody's building agents now. You see these things that can help you to do things like adding things like OCR an appointment from a picture of a hand-written paper and add it to your calendar, search things from the internet, find that email with a PDF and add it to your local paperless instance.

Building an agent like this by yourself is really easy. Now, we have Gemini's subscription, OpenAI's ChatGPT subscription and all those, 20 bucks a month right?What if you can spend that 20 bucks in tokens to do your own. And you pay 15 bucks _a year_ in tokens to run that? And you own the data, you own your code and integrations. It's really easy to do, and these flash models are _more than enough_ for simple agentic tasks.

reply

darkoob12
 
2 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

My mental bias always kept me away from Chinese models. Because i know that china is a surveillance state and all the things we know about CCP. But after what we learned about OpenAI and how they most likely used user data to basically cheat in an open competition i think it does not matter which AI provider you use all of them will own your data and all of them can spy on you. So I am willing to switch to Chinese models. This way we help them develop and improve models some day we can run them locally.

reply

ricardobeat
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

These models are open-weights. Anyone can host them, you don’t have to use chinese servers even though most of them offer zero data-retention policies.

reply

m00dy
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

>>zero data-retention policies

Yeah, that’s basically an industry-wide scam.

reply

Xiol32
 
11 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

But it makes the compliance team happy.

reply

jsw97
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Even you think both cheat, you can't possibly think they both cheat the same amount.

reply

Mashimo
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

The new meta model is fast and very cheap as well, and when used through OpenCode you get quite a lot of free tokens. But meta is also THE surveillance company, so probably also not a good choice in your case.

reply

miroljub
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

If you work on open source projects, I don't care about surveilance. It's right there on Github with full history anyways.

reply

hn8726
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Is it? You're still putting a lot of thought and guidance into the agent's harness, the final code is just a tiny bit of that. It's like giving a junior developer final code vs explaining the whys and nuance. Which I'm not sure I want to give Meta

reply

el_io
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

You can use those models from Openrouter, they have many Non-Chinese providers.

reply

epolanski
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

You're naive if you're thinking the scumbags running the US companies aren't using your data.

In any case old rules apply: if privacy is a concern don't share the data. I share all my work-related code because it's worthless, but I don't and would never share company business and process details, access to production/user data, etc.Meanwhile I know of people connecting all the kind of MCPs for datadog/sentry/jira/concluce/production databases to their harnessess..lol.

reply

serf
 
2 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I recently had to config my harness to watch for cybersecurity flags from astra and funnel requests to flash when they occur because Astra gets queezy when you talk to it about UDP packets in games.

Works fantastic. Glad there is a more 'uncensored' thing to fall back to when the frontier folk are too sensitive.

reply

nicce
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

The only positive side is that it is harder for students to feed university exercises to the agent in cybersecurity and expect it to make them all.

reply

XzAeRosho
 
2 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Same for me. DeepSeek models are incredibly good at implementation and light planning. I still default to Opus models for feature planning, but for most simple features the Pro models suffice.

Incredible good value and product they have built.

reply

k__
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

Beta testers report >400 TPS.

https://www.geeky-gadgets.com/deepseek-v4-1-flash-review/I hope some of those speed increases will make it to production.

reply

esafak
 
1 hour ago
 
 | 
parent
 | 
next
 
[–]

That ought to be DeepSeek's real differentiator; all the other Chinese models are slow.

reply

eli
 
10 minutes ago
 
 | 
prev
 | 
next
 
[–]

You can test it now on the official deepseek api. Just set your model to deepseek-v4.1-flash-expires-on-0910

It’s good and very fast.(Note that the deepseek API trains on your data)

reply

postalcoder
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

I hope DeepSeek takes some time to improve their tuning for reasoning effort. Right now, there are only three reasoning efforts: low, high, and max.

For all intents and purposes, "low" is pretty much the same as turning reasoning off, and "high" is similar to "max". "High/max" performs way too much reasoning, takes forever, and causes costs to balloon. They need a proper "medium" setting.I get it that they're probably focused on pushing performance right now, but the ergonomics of the model aren't great.

reply

iamniels
 
2 hours ago
 
 | 
parent
 | 
next
 
[–]

I switched to GLM-5.3 flash on high for this reason. Too many "but wait" in the Deepseek-v4 reasoning.

reply

tarruda
 
2 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I would rather have just 3 levels: low, medium and high.

reply

tarruda
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

Hopefully it will be open weights and have the same architecture and size as the current v4 flash vision, which is probably the best LLM that can be run on 128G devices.

reply

fluoridation
 
3 hours ago
 
 | 
parent
 | 
next
 
[–]

Interesting, I had assumed it'd be too large to fit. What quant and context size are you running?

reply

tarruda
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

IQ3_XXS (~3.2 BPW). For me this is an option because my Mac studio is only used for serving LLMs, so I can afford to dedicate most of its RAM to this. I can run with 256k context and only uses ~117G, with the remaining (up to 125G which I can allocate to VRAM) being used for prompt caching and context checkpoints.

I'm making my own quants, though the Vision-Exp version is outdated and won't work on llama.cpp master branch (I built it before llama added support):-https://huggingface.co/tarruda/DeepSeek-V4-Flash-0731-GGUF-https://huggingface.co/tarruda/DeepSeek-V4-Flash-Vision-Exp-...For the Vision-exp version, I also ran perplexity + KLD against the original MXFP4. Seems quite OK:https://huggingface.co/tarruda/DeepSeek-V4-Flash-Vision-Exp-...

reply

fluoridation
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thanks, I'll give that a try. I basically have the same use case, only on Strix Halo.

reply

tarruda
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Don't use my Vision-Exp GGUF though. As I said I built those GGUFs before llama.cpp supported, and they can't be loaded on current master (require my own branch).

I already have new GGUFs but haven't uploaded yet. If you want Vision-Exp, maybe use bartowski or unsloth's GGUFs.Side note:As an alternative to deepseek v4, you might want to give it a shot at qwen 3.8 flash next. I have IQ4_NL GGUFs that can be loaded fully into 128G, or Q5_K GGUFs that can offload the PLE to disk (use --load-mode none --lazy-mode on for that):https://huggingface.co/tarruda/Qwen3.8-Flash-Next-GGUF.llama.cpp master is still somewhat bad in Qwen 3.8 next performance, but I was able to achieve 40tps tg and 600 tps pp on my private branch.

reply

kamranjon
 
50 minutes ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Hey there! I do the same but I use dwarfstar at a 2-bit quant: 
https://github.com/antirez/ds4

I'm curious if you've tried dwarfstar and decided to move to llama.cpp and 3 bit quants or what made you go that route instead? I've been using ds4 for months now and it's already got support for the new vision model, haven't tried it yet, still on 0731 but it's been very solid for me.

reply

NitpickLawyer
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

It's interesting that this is the third lab to find problems with larger models. Earlier last year oAI was rumoured to have failed their large pretrain. Now google has problems with their pro series, and ds just announced the same. There are some rumours on chinese forums talking about problems with the pretraining phase, so this is not mid/post training related.

I wonder if this comes from using the bad architecture scaled up (and it hits some limits) or if this is a data problem (undertrained? bad data? bad pre-processing using smaller models?)...

reply

wolttam
 
1 hour ago
 
 | 
parent
 | 
next
 
[–]

Just my intuition about it but it does seem like a data issue.

V4 flash and V4 pro feel very similar, which would make sense if they were pre-trained on largely the same corpus.All that would suggest to me is that V4 Flash is capable of absorbing the data they’re throwing at it, and we’re still nowhere near the data limits of their larger 1.6T model

reply

pixelesque
 
1 hour ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Where are you seeing them having an issue with the larger (Pro) model?

The announcement specifically says 4.1 Pro will be released in the future.

reply

petu
 
6 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

A month ago new V4 Flash 0731 checkpoint was better than existing V4 Pro. They've kept serving Pro, it was updated 13 days later (0813 checkpoint).

Now, 4 weeks later new Flash checkpoint (0910?) is again better than existing Pro. Same situation, but Pro is taken offline this time.

reply

edude03
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

I've been watching a bunch of bycloud on YouTube recently, and although he's done a great job reviewing papers from the big AI labs, I feel like I'm missing something - how have all the labs seemingly made a model that's cheaper, faster AND has better performance? Historically `flash` variants (like codex spark as well) have been faster but perform worse

reply

_3u10
 
1 hour ago
 
 | 
parent
 | 
next
 
[–]

That’s how increasing performance works. You make a model 10x faster, then you make it think 2x as much.

Its cost is now 1/10th per token, and 1/5th per task.Basically they have shitty hardware so they have to do a lot of optimization. Think of it like replacing an O(n) algorithm with O(log n).Anthropic / Open AI think the best path is the most intelligent models deepseek is more focused on tok/$

reply

wg0
 
57 minutes ago
 
 | 
prev
 | 
next
 
[–]

DeepSeek v4 Flash with high is already a really great work horse. Reliable. But this time, not only that it is better but they are reducing the price by 50% so that's great.

I also find the DeepSeek models to be more precise than Claude models (last I used 4.7) in that I yet had not the occasion where model did something unintentional that I did not direct it to.EDIT: Updated percentage reduction.

reply

kennywinker
 
52 minutes ago
 
 | 
parent
 | 
next
 
[–]

Reducing the price by 100% means it’s free. I think you mean reducing the price by 50%

reply

wg0
 
49 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

What I mean is that price has been effectively halved.

During off-peak hours, the unit price is reduced from $0.007 for input cache hits to $0.003, $0.22 for input cache misses to $0.15, and $0.12 for output to $0.6

reply

riknos314
 
28 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Halved would be a 50% percent reduction.

0.15/0.22 ≈ 0.68, meaning a roughly 32% reduction on inputs. The 50% reduction is only outputs and cached inputs.

reply

kakacik
 
25 minutes ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Sounds like 50% reduction to me. 100% reduction means price -> 0

reply

nicman23
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

qwen3.8-flash-next on a single rtx6000 (~1 euro per hour on a spot vm) with buun-llama is i think the cheapest reasoning / euro atm.

hope deepseek makes me change my setup again

reply

a-ve
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

I've been using deepseek-v4-flash as a "worker" model with Claude Code to implement a tool using Rust/Iroh for my personal use, and it works fairly nicely when I use Opus as the planner/reviewer model. It seems to follow the plan generated by Opus, albeit with a few misses here and there that it cleans up later after being reviewed by Opus.

Fairly excited for the v4.1 launch. Input cache hit prices have been halved, which looks nice.

reply

bitexploder
 
14 minutes ago
 
 | 
parent
 | 
next
 
[–]

If you are okay with waiting use GLM 5.3 max. It costs more but still cheap. It is slow, but a very strong worker. Still dollars per day (at most) with heavy concurrent agent running. I load up planning and tasks in Opus or Sol, and just have glm flash workers go to town every night. My project has never advanced more smoothly.

reply

nickweb
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

Via nitter: 
https://xcancel.com/JustinGorya/status/2097287080128708930

Looks like the new model can be used if summoned via the API but the API won't list it.

reply

swiftcoder
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

If they can keep up this cadence of Flash leap-frogging the previous Pro, we're in for a good time

reply

dude250711
 
1 hour ago
 
 | 
parent
 | 
next
 
[–]

Anthropic/OpenAI might step up their anti-distillation defences though.

reply

swiftcoder
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Nah, we're long past the point where that would make a difference - if they could have done so effectively, they would have before K3 and GLM 5.3 were nipping at their heels...

reply

_aavaa_
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

They might need to step up their product offerings and offer cheaper.

reply

igleria
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

v4 pro was decent then a better cheaper faster model comes now?

As a consumer I feel like hansel and gretel combined, deepseek could be the witch.

reply

throwaway473825
 
2 hours ago
 
 | 
parent
 | 
next
 
[–]

It's not unprecedented given that GLM 5.3 Flash was better and cheaper than GLM 5.2.

reply

calgoo
 
2 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

v4 flash has been working quite well for the majority of my personal projects, with occasional v4 pro or Kimi 3 for the most complicated tasks or to check the overall project progress (when vibe coding).

reply

HansHamster
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I must be doing something wrong. I gave v4 pro a try a couple of days ago, gave it a simple prompt like "clean up functions x and y in file z" and it would always start off promising, just to quickly get sidetracked, start hallucinating problems in the code, and just get stuck for hours until I interrupt it:

— hmm — 0x2D696370 — little-endian bytes: 70 63 69 2D = 'p','c','i','-' — hmm — WAIT — WAIT — !!!!! — *WAIT — WAIT — WAIT — WAIT — WAIT — WAIT — *HOLD ON — HOLD ON — HOLD ON — WAIT — WAIT — WAIT — WAIT — WAIT — WAIT — WAIT — !!!!!!!! — *WAIT — WAIT — WAIT — WAIT — WAIT — WAIT — WAIT — WAIT — *OK — WAIT — I THINK I FINALLY SEE THE WHOLE PICTURE — I NEVER READ IT — AND — THE LAYOUT — hmm — !!!!! — *WAIT — WAIT — WAIT — WAIT — WAIT — WAIT — WAIT — WAIT — WAIT — HOLD ON — HOLD ON — HOLD ON — HOLD ONThen gave the same to Sonnet 5 and it was done 15 - 30 minutes later.
I tried v4 pro both in claude code and codewhale with similar results. Haven't tried the new deepseek harness.

reply

atwrk
 
15 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I guess this was a heavily quantized version from openrouter? I've never had that experience in the last months of quite intensive use of the official deepseek api.

reply

KyleTheDev
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I've been using the 0731 Flash V4 model, via Opencode, and I've had no major issues. It feels very comparable to Opus 4.6/4.7, that I use at work. I haven't ran into any of the problem you mention, so that might be a quirk of V4 pro, the specific harness, or maybe the host you're using?

reply

k__
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I used flash with pi and it worked pretty well.

It built this whole IaC plugin from scratch:https://github.com/fllstck/nebius-alchemy

reply

damsta
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

> all requests to the Pro model will be routed to V4.1 Flash and billed at Flash's price

While V4.1 Flash performance and cost looks promising this auto re-routing sounds concerning

reply

tensegrist
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

In keeping with our commitment to user responsibility, following the official launch of V4.1 Flash and prior to the release of V4.1 Pro, all requests to the Pro model will be routed to V4.1 Flash and billed at Flash's price.just in terms of user perception when selling this sort of service, this is what they call a "good look"

reply

coopykins
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

I really enjoy using V4 Flash for digging though data and such. Its a very good model for the price. Looking forward to this one.

reply

stanac
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

My problem with V4 flash is output limit. When I need to write or rewrite a larger file (~1000 lines of code) it will fail with message like output limit reached.

reply

aftbit
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

Will V4.1 Flash and V4.1 pro be open-weights?

reply

npn
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

Crazy that they still keep the price -- or actually decrease it, even -- despite it is a big improvement. I hope it retains some of the tps speed of the preview release though, 300 tps means gemini flash is no longer "the fastest option" any more.

reply

c0rruptbytes
 
24 minutes ago
 
 | 
prev
 | 
next
 
[–]

are they releasing the weights too?

reply

thrownaway561
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

I will continue to be amazed by how much power you get from DeepSeek Flash for the cost. I have let that puppy lose on so many projects and it is has never let me down. It can build and entire Rails app in no time and even do the tests. For most things, I don't get why people pay the money for Claude. DeepSeek Flash is my default agent in Omarchy.

reply

bwfan123
 
1 hour ago
 
 | 
parent
 | 
next
 
[–]

Same, very impressed with v4 flash. It has the right balance of cost and performance.

reply

indigodaddy
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

So, will it have vision? (based on deepseek-v4-flash-vision-exp ?)

reply

ComputerGuru
 
1 hour ago
 
 | 
parent
 | 
next
 
[–]

Already available via the API as deepseek-v4.1-flash-expires-on-0910, with vision.

reply

nicce
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

> In keeping with our commitment to user responsibility, following the official launch of V4.1 Flash and prior to the release of V4.1 Pro, all requests to the Pro model will be routed to V4.1 Flash and billed at Flash's price. If you encounter any issues during your comparative testing between V4 Pro and V4.1 Flash, please do not hesitate to reach out to us with your feedback. Thank you for your support!

Wow. Imagine OpenAI/Google/Anthropic doing this! Nope.

reply

hinow
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

But what no one mentions is that the price is going from a starting point of $0.16 to $0.60, so basically they're charging nearly four times as much.

reply

KyleTheDev
 
1 hour ago
 
 | 
parent
 | 
next
 
[–]

Like _aavaa_ said, make sure you're comparing the right vals 1:1. There's different costs for cache hit, cache misses, output tokens, etc. This one seems, during non-peak hours, cheaper. Peak hours are obviously more expensive, if they're gonna be 2x non-peak pricing. But, that might end up decreasing in the future.

reply

VulgarExigency
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Deepseek already has 2x peak pricing. This is just going to be cheaper across the board.

reply

KyleTheDev
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Ah, how did I not know about this? I guess I had missed seeing this somewhere, I might just always be using it during off-peak hours. Thanks!

reply

hinow
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Take a look at the answer below, please.
:)

reply

_aavaa_
 
2 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

What are you talking about? Current flash prices are 0.66 for output, this is dropping it to 0.60.

reply

hinow
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

This is the notice from DeepSeek regarding their API:

We will adjust the pricing for the Flash series effective from 12:00 Beijing Time on September 10, 2026. During off-peak hours, the unit price will be $0.003 for input cache hits, $0.15 for input cache misses, and $0.6 for output. Peak-hour prices will be double the off-peak rates. Please plan your usage accordingly.-------------------------------------------------------
Hoje em sites como openrouter o valor é de $0.16 output .

reply

KyleTheDev
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Direct 1:1:1 comparison, for V4.1 Flash - V4 Pro 0813 - V4 Flash 0731

Input cache hits (per 1m tokens) - $0.003 Vs. $0.022 Vs. $0.007Input cache miss (per 1m tokens) - $0.15 Vs. $0.66 Vs. $0.22Output (per 1m tokens) - $0.6 Vs. $1.98 Vs. $0.66This is taken fromhttps://api-docs.deepseek.com/quick_start/pricing, and it's comparing only off-peak hours pricing. It looks like V4.1 Flash is cheaper than the current 0731 flash model, and much cheaper than the current V4 Pro model.

reply

_aavaa_
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Yes, and? This is their current off-peak pricing for their flash model [0]: $0.007 cache, $0.22 input, $0.66.

0.007 -> 0.0030.22 -> 0.150.66 -> 0.60Each one is now cheaper.[0]:https://api-docs.deepseek.com/quick_start/pricing/

reply

ThouYS
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

if this beats GLM 5.3 flash, I am sold

reply

vib08
 
1 hour ago
 
 | 
parent
 | 
next
 
[–]

i think this will beat GLM 5.3 flash,
i mean the last ds4-flash after preview was already great, and i found that more intelligent than GLM 5.3 flash

reply

neugls
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

Waiting to use it

reply

Guidelines
 | 
FAQ
 | 
Lists
 | 
API
 | 
Security
 | 
Legal
 | 
Apply to YC
 | 
Contact

Search: