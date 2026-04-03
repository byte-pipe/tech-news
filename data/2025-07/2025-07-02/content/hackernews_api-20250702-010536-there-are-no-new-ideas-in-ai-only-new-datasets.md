---
title: There Are No New Ideas in AI… Only New Datasets
url: https://blog.jxmo.io/p/there-are-no-new-ideas-in-ai-only
site_name: hackernews_api
fetched_at: '2025-07-02T01:05:36.238047'
original_url: https://blog.jxmo.io/p/there-are-no-new-ideas-in-ai-only
author: Jack Morris
date: '2025-07-01'
description: LLMs were invented in four major developments... all of which were datasets
tags:
- hackernews
- trending
---

#### Share this post

Jack Morris
There Are No New Ideas in AI… Only New Datasets
Copy link
Facebook
Email
Notes
More

# There Are No New Ideas in AI… Only New Datasets

### LLMs were invented in four major developments... all of which were datasets

Jack Morris
Apr 09, 2025
197

#### Share this post

Jack Morris
There Are No New Ideas in AI… Only New Datasets
Copy link
Facebook
Email
Notes
More
12
24
Share

Most people know that AI has made unbelievable progress over the last fifteen years– especially in the last five. It might feel like that progress is*inevitable*– although large paradigm-shift-level breakthroughs are uncommon, we march on anyway through a stream of slow & steady progress. In fact, some researchers have recently declared a“Moore’s Law for AI”where the computer’s ability to do certain things (in this case, certain types of coding tasks) increases exponentially with time:

the proposed “Moore’s Law for AI”. (by the way, anyone who thinks they can run an autonomous agent for an hour with no intervention as of April 2025 is fooling themselves)

Although I don’t really agree with this specific framing for a number of reasons, I can’t deny the trend of progress. Every year, our AIs get a little bit smarter, a little bit faster, and a little bit cheaper, with no end in sight.

Thanks for reading! Subscribe for free to receive new posts and support my work.

Subscribe

Most people think that this continuous improvement comes from a steady supply of ideas from the research community across academia – mostly MIT, Stanford, CMU – and industry – mostly Meta, Google, and a handful of Chinese labs, with lots of research done at other places that we’ll never get to learn about.

And we certainly have made a lot of progress due to research, especially on the systems side of things. This is how we’ve made models cheaper in particular. Let me cherry-pick a few notable examples from the last couple years:

- in 2022 Stanford researchers gave usFlashAttention, a better way to utilize memory in language models that’s used literally everywhere;

- in 2023 Google researchers developedspeculative decoding, which all model providers use to speed up inference (also developed atDeepMind, I believe concurrently?)

- in 2024 a ragtag group of internet fanatics developedMuon, which seems to be a better optimizer than SGD or Adam and may end up as the way we train language models in the future

- in 2025 DeepSeek releasedDeepSeek-R1, an open-source model that has equivalent reasoning power to similar closed-source models from AI labs (specifically Google and OpenAI)

So we’re definitely figuring stuff out. And the reality is actually cooler than that: we’re engaged in a decentralized globalized exercise of Science, where findings are shared openly onArXivand at conferences and on social media and every month we’re getting incrementally smarter.

If we’re doing so much important research, why do some argue that progress is slowing down?People are still complaining. The two most recent huge models,Grok 3andGPT-4.5, only obtained a marginal improvement on capabilities of their predecessors. In one particularly salient example, whenlanguage models were evaluated on the latest math olympiad exam, they scored only 5%, indicating thatrecent announcements may have been overblownwhen reporting system ability.

And if we try to chronicle the*big*breakthroughs, the real paradigm shifts, they seem to be happening at a different rate. Let me go through a few that come to mind:

### LLMs in four breakthroughs

1. Deep neural networks: Deep neural networks first took off after theAlexNet modelwon an image recognition competition in 2012

2. Transformers + LLMs: in 2017 Google proposed transformers inAttention Is All You Need, which led toBERT(Google, 2018) and the originalGPT(OpenAI, 2018)

3. RLHF: first proposed (to my knowledge) in theInstructGPT paperfrom OpenAI in 2022

4. Reasoning: in 2024 OpenAI released O1, which led to DeepSeek R1

If you squint just a little, these four things (DNNs → Transformer LMs → RLHF → Reasoning) summarize everything that’s happened in AI. We had DNNs (mostly image recognition systems), then we had text classifiers, then we had chatbots, now we have reasoning models (whatever those are).

Say we want to make a fifth such breakthrough; it could help to study the four cases we have here. What new research ideas led to these groundbreaking events?

It’s not crazy to argue thatall the underlying mechanisms of these breakthroughs existed in the 1990s,if not before. We’re applying relatively simple neural network architectures and doing either supervised learning (1 and 2) or reinforcement learning (3 and 4).

Supervised learning via cross-entropy, the main way we pre-train language models, emerged from Claude Shannon’s work in the 1940s.

Reinforcement learning, the main way we post-train language models via RLHF and reasoning training, is slightly newer. It can be traced to theintroduction of policy-gradient methods in 1992(and these ideas were certainly around for the first edition of the Sutton & Barto “Reinforcement Learning” textbook in 1998).

### If our ideas aren’t new, then what is?

Ok, let’s agree for now that these “major breakthroughs” were arguably fresh applications of things that we’d known for a while. First of all – this tells us something about the*next*major breakthrough (that “secret fifth thing” I mentioned above). Our breakthrough is probably not going to come from a completely new idea, rather it’ll be the resurfacing of something we’ve known for a while.

But there’s a missing piece here: each of these four breakthroughsenabled us to learn from a new data source:

1. AlexNet and its follow-ups unlockedImageNet, a large database of class-labeled images that drove fifteen years of progress in computer vision

2. Transformers unlocked training on “The Internet” and a race to download, categorize, and parse all the text onThe Web(whichit seemswe’ve mostly doneby now)

3. RLHF allowed us to learn from human labels indicating what “good text” is (mostly a vibes thing)

4. Reasoning seems to let us learn from“verifiers”, things like calculators and compilers that can evaluate the outputs of language models

Remind yourself that each of these milestones marks the first time the respective data source (ImageNet, The Web, Humans, Verifiers) was used at scale. Each milestone was followed by a frenzy of activity: researchers compete to (a) siphon up the remaining useful data from any and all available sources and (b) make better use of the data we have through new tricks to make our systems more efficient and less data-hungry. (I expect we’ll see this trend in reasoning models throughout 2025 and 2026 as researchers compete to find, categorize, and verify everything that might be verified.)

Progress in AI may have been inevitable once we gathered
ImageNet
, at the time the largest public collection of images from the Web

### How much do new ideas matter?

There’s something to be said for the fact that our actual technical innovations may not make a huge difference in these cases. Examine the counterfactual. If we hadn’t invented AlexNet, maybe another architecture would have come along that could handle ImageNet. If we never discovered Transformers, perhaps we would’ve settled with LSTMs or SSMs or found something else entirely to learn from the mass of useful training data we have available on the Web.

This jibes with the theory some people have that nothing matters but data. Some researchers have observed that for all the training techniques, modeling tricks, and hyperparameter tweaks we make, the thing that makes the biggest difference by-and-large is changing the data.

As one salient example, some researchers worked ondeveloping a new BERT-like model using an architecture other than transformers. They spent a year or so tweaking the architecture in hundreds of different ways, and managed to produce a different type of model (this is a state-space model or “SSM”) that performed about equivalently to the original transformer when trained on the same data.

This discovered equivalence is really profound because it hints that*there is an upper bound to what we might learn from a given dataset*. All the training tricks and model upgrades in the world won’t get around the cold hard fact that there is only so much you can learn from a given dataset.

And maybe this apathy to new ideas is what we were supposed to take away fromThe Bitter Lesson. If data is the only thing that matters, why are 95% of people working on new methods?

### Where will our next paradigm shift come from?*(YouTube…maybe?)

The obvious takeaway is that our next paradigm shift isn’t going to come from an improvement to RL or a fancy new type of neural net. It’s going to come when we unlock a source of data that we haven’t accessed before, or haven’t properly harnessed yet.

One obvious source of information that a lot of people are working towards harnessing is video. According toa random site on the Web, about 500 hours of video footage are uploaded to YouTube *per minute*. This is a ridiculous amount of data, much more than is available as text on the entire internet. It’s potentially a much richer source of information too as videos contain not just words but the inflection behind them as well as rich information about physics and culture that just can’t be gleaned from text.

It’s safe to say that as soon as our models get efficient enough, or our computers grow beefy enough, Google is going to start training models on YouTube. They own the thing, after all; it would be silly not to use the data to their advantage.

A final contender for the next “big paradigm” in AI is a data-gathering systems that some wayembodied– or, in the words of a regular person, robots. We’re currently not able to gather and process information from cameras and sensors in a way that’s amenable to training large models on GPUs. If we could build smarter sensors or scale our computers up until they can handle the massive influx of data from a robot with ease, we might be able to use this data in a beneficial way.

It’s hard to say whether YouTube or robots or something else will be the Next Big Thing for AI. We seem pretty deeply entrenched in the camp of language models right now, but we also seem to be running out of language data pretty quickly. But if we want to make progress in AI, maybe we should stop looking for new ideas, and start looking for new data.

Subscribe
197

#### Share this post

Jack Morris
There Are No New Ideas in AI… Only New Datasets
Copy link
Facebook
Email
Notes
More
12
24
Share
