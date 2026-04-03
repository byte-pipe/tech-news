---
title: 'Arming the rebels with GPUs: Gradium, Kyutai, and Audio AI | Amplify Partners'
url: https://www.amplifypartners.com/blog-posts/arming-the-rebels-with-gpus-gradium-kyutai-and-audio-ai
site_name: hnrss
content_file: hnrss-arming-the-rebels-with-gpus-gradium-kyutai-and-aud
fetched_at: '2026-02-16T11:19:18.280784'
original_url: https://www.amplifypartners.com/blog-posts/arming-the-rebels-with-gpus-gradium-kyutai-and-audio-ai
date: '2026-02-13'
description: The story of Gradium, the anatomy of audio AI models, and why smaller labs continue to edge out larger ones when it comes to voice.
tags:
- hackernews
- hnrss
---

Projects to Know Issue 128
Read Now

AI and ML

# Arming the rebels with GPUs: Gradium, Kyutai, and Audio AI

By 
Justin Gage
Rebecca Dodd
Share

February 12, 2026
Disclosure: Amplify is an investor in Gradium.

If AI research is Star Wars and OpenAI is the death star, then without a doubt the rebels are building audio models. The best models for voice – TTS, STS, STT, and the like – arenotcoming from the big labs. Instead, they’re built by their underfunded, understaffed, and underhyped siblings, a wave of incredible startups that is improbably crushing benchmarks with every model release. And if you believe that audio is the biggest future modality for AI – like many researchers do – this is one of the more interesting and underdiscussed topics in genAI today.

One of these improbably cutting edge startups isGradium, born out of the open labKyutai.

In summer 2024 on a stage in Paris, a Kyutai researcher (his name is Neil) demoedthe first realtime audio conversation with AI. This model (Moshi) could respond in real time, change its voice style and volume on request, and even recite an original poem in a French accent (research shows poems sound better this way).

You’ve probably seen audio AI demos before. You may not be particularly impressed. Didn’t OpenAI do this a few years ago? Well, not exactly:

1. This was thefirst full-duplex conversational AI model. Moshi could interrupt, be interrupted, backchannel ("uh-huh", "I see") and respond in around 160ms (faster than most human conversations).
2. This demo happenedbeforeOpenAI released Advanced Voice Mode, and a full year before xAI released a similar demo (with more latency).

This would have been a groundbreaking release from a major lab, except it wasn’t from a major lab, it was from a team of 4 (four) researchers who built it completely from scratch (without a pre-trained base) in 6 months. The model is open source, and can even run on mobile. Oh, and the team was part of a non-profit with extremely limited funding.How did they do it?

Based on extensive interviews with the Gradium team, this post is going to go in technical depth on an incredibly interesting niche of the increasingly top heavy AI world:

* A brief history of audio ML, and why it’s consistently overlooked
* Dynamics of big labs and why small teams of researchers can outperform
* Anatomy of training a voice AI model, and how it differs from text
* Core Gradium / Kyutai research: full-duplex models, audio codecs, oh my!

Let’s get to it.

## A brief history of audio ML, and why it’s consistently overlooked

If you watch any science fiction movie —2001: A Space Odyssey,HerandIron Manor incessantly invoked — the colloquial AI speaks in a distinctly natural, human-sounding voice. One simply needs to ask Siri what time it is (it took 5 seconds for me this morning) to realize how far away from this ideal our devices can be.

There’s an obvious question here:how did we let it get this bad?Why are we only now starting to see meaningful advances in audio AI, while text has been rapidly improving every single year since 2020?

This problem is actually foundational. Foryearsaudio has occupied the bottom tier of AI/ML’s informal coolness hierarchy. If you were around this scene pre-GPT, there was a clear ranking of what it was cool to work on. At the top was image classification via CNNs, which was for a while the most promising real world application of AI. Then came ML on tabular data, then text, and audio was somewhere all the way towards the bottom. For several reasonsaudio just wasn’t sexy1.

There are practical reasons for this gap: training data for audio is genuinely scarce compared to text. You can scrape trillions of tokens from Wikipedia, Stack Overflow, books, and papers. High-quality conversational audio is harder to come by, and much of it isn’t particularly informative. A Stack Overflow answer (usually) teaches you something, but a typical phone conversation is mostly filler. And generating audio is much more complex than predicting text tokens, requiring real domain expertise to execute effectively.

But there’s also a cultural problem here. In the mid-2010s, when deep learning was taking off for images and starting to work for text, audio felt impossibly hard. Neural networks were doing cool things with photos. Maybe they’d eventually be okay at writing. Very, very few people conceived that one day, audio could have realtime conversations with proper turn-taking and expressiveness. Siri put a laughably bad voice assistant in everyone’s pocket…is it possible we slowly internalized defeat?

This was undoubtedly true at larger labs. When Neil (Kyutai co-founder and Gradium CEO) was hired at Google Brain in 2019, he was one of a very small group working on voice. Management considered voice to be a “solved problem.” Meanwhile, projects like Meta’sSeamlessand Google’s various speech initiatives shipped models, published papers, then languished. These repos haven’t been updated in years!

All of this created an opportunity. When you have a hard technical problem that’s been underfunded and underexplored, and yet has promise to bethecore modality if things go right2, a few researchers who actually understand the domain can move incredibly fast. And they did.

## Dynamics of big labs and why small teams of researchers can outperform

When Neil joined Facebook AI Research for his PhD in 2015 there was a clear social hierarchy among AI research:

* Researchscientistswere the “idea guys” — with prestigious academic backgrounds, working on theoretical problems, and rarely touching code3.
* Researchengineersimplemented those ideas in code and with machines. They knew how to get theory into software and hardware.

In quite a turn from SF culture today, the scientists almost universally had higher prestige and better compensation4.

Then deep learning happened, and the hierarchy completely inverted. Ideas became very cheap because Neural nets are universal approximators, and are essentially very dumb. A lot of research became “what can we throw Deep Learning at” and the hard problems were moving down the stack: training efficiently, managing distributed systems, etc. Now the engineers were in charge!

The researchers who thrived in this new climate — people like Noam Shazeer at Google — were actually both of these people. They could have the architectural insightandimplement it themselves5.

“The biggest scam in big companies is thinking that you can lead a research organization without doing research yourself, just by being an ‘idea guy’. The only way to understand what is possible, what is challenging, how we should allocate resources, is to understand every single detail to the deepest level.”

The priority now was less how creative your idea is, and more what you can realize as a tangible outcome of an idea. And critically, this did not necessarily require massive compute budgets and teams. In a sense (perhaps a very weak sense) this was the AWS moment for startups…but for AI research. Not to mention that getting GPUs in the cloud was now a few clicks (if your clicks were fast enough).

This is the crux of why big labsstilldon’t dominate in audio like they do in text. Small groups of research engineers are able to completely outclass their larger, better staffed and funded competitors because they move fast, build their own ideas, and don’t have to deal with the incessant big lab politics that you are reading about every day on X.

Not only that, but as we’ll see, audio is a completely different beast than text. It isnotjust about scaling compute and data. There are a million little edges to creating elite audio models, from correct turn taking to backchanneling and managing latency, that require deep domain expertise. Great audio models are trained by great audio researchers, and throwing money at the problem will only get you mediocrity.

All the Gradium cofounders (Neil +Alex Défossez,Olivier Teboul, andLaurent Mazaré) worked around some combination of these labs, absolutely cooking in relative obscurity in their underfunded audio divisions. It was a fun time in Paris. Alex was working on mathematical optimization but DJing on the side. They started building an AI-based synthesizer for fun.

NOT Neil and Alex. 

The first thing Neil did at Google Brain was work on audio compression, building the very first neural audio codec –SoundStream. Better compression led Neil and Olivier to train the first model that could generate audio by predicting compressed tokens. After one week, they ran an experiment: “I passed three seconds of my voice to the model, and it kept talking in my voice.” (They had accidentally invented voice cloning). Every audio project at Google Brain started using this framework, which became the foundation forGemini Live.

Essentially, here was a small group of some of the best audio researchers on the planet all connected and working at big labs. It was only a matter of time…

ThusKyutaiin 2023 was born and all of our characters united. It was the first and is the only open audio lab, named for the Japanese word for “sphere.” In fact their two major model releases also carry Japanese names:

* Moshi, discussed earlier, the first realtime voice model (paper here)
* Hibiki, a simultaneous STS translation model in the speaker’s voice (paper here)

Kyutai is open because Neil and his cofounders believe in open research, and as competitive pressure between labs was intensifying, fewer and fewer papers were being published. With funding from Eric Schmidt and two French billionaires, they started cooking.

In addition to the above, Kyutai has released open source text-to-speech and speech-to-text models — the foundation forNVIDIA’s PersonaPlexandQwen3-TTS. Their real-time speech-to-speech translation (you can check out the demo below) was running on-device many months before Apple’s.

All of this is nice, but mostly research as research. Kyutai models are fundamentally prototypes, and real apps need much more polished models. So part of the Kyutai team started Gradium to bridge that last mile between research and product, andraised $70M to do it. You can think of this as a sort of pipeline from fundamental Kyutai research into production-grade products via Gradium. And in a few short months, they built and shipped multi-lingual models that compete with the best in class.

## Anatomy of training an audio model

When it comes to training audio is both like text and not like text.

To start with the similarities, most SOTA audio models use architectures that are pretty similar to text, e.g. they’re Transformer-based among other things. The nice thing about borrowing LLM architectures is you benefit from all of the advances in text over the past few years, RLHF techniques, distillation, and the hardware out there optimized for LLMs.

But unlike text that has the internet corpus, there is not a huge treasure trove of available high quality audio data. And what “audio data” evenmeansis a moving target, because what exactly do you want to train on: labeled transcribed conversations? Translations of a single speaker’s voice? Conversations with multiple participants?  Peruse through the typical open datasets and test sets for audio AI (Voxpopuli,MADLAD-400,NTREX) and you can get a sense of how much more disjointed this is than text.

Audio models are also very small compared to LLMs. Moshi, Kyutai’s foundation audio model, has 7B parameters and was trained on only 2.1T tokens. As a result they tend toknowa lot less ground information than a typical LLM.

All-in-all Moshi was:

* Pretrained on 7M hours of audio with transcripts.
* Post-trained on the Fisher dataset (2000 hours of phone conversations with separated channels).
* Instruction finetuned on 20k+ hours of synthetic dialogue.

One of the hardest parts of training these models, especially when it comes to reward functions in post-training, is the subjective nature of evaluations. This problem iswell documentedin the music generation space. Good conversations are completely subjective! Neil and co. completely gave up on quantitative measures and only trusted humans, doing tons of blind tests and just listening (they also supplement their efforts with freelancers).

## Audio model architectures: speech-to-speech vs. full duplex

One of the hardest problems to solve in audio AI has been theturn taking problem. How do you effectively trade conversation with an unpredictable user?When is the user done talking, and when are they just thinking? How do you handle interruptions? Should the model ever interrupt the user, and if so when? (The model should justread Dale Carnegie, duh.) It turns out it’s really hard to nail this dynamic, and among audio researchers it’s thought of as one of the most challenging problems in the space.

Accordingly, you will see “speech-to-speech” thrown around a lot, but not all S2S models are created equal.

Today’s OpenAI models aretechnicallyspeech-to-speech, but they areturn-based. They are trained to understand (predict) when the user is finished talking or asking their question, which sounds reasonable enough, but ends up creating weird dynamics. For example, if you (the user) are silent for a few seconds because you’re thinking about the right formulation, the model is going to talk even though you didn’t want it to. It also cannot interrupt you (even though sometimes it should), and until recent editions, it was impossible to interrupt the model itself. This is like talking to someone on a walkie talkie, fun but ultimately not quite the real thing.

Full duplexmodels, on the other hand, are like being on the phone. It’s more like a real conversation, where the model interacts with you dynamically, you can both interrupt each other, and it’s more intelligent when it comes to interpreting your intent. These models are proficient at backchanneling (“aha, yes, I see, mhm”) which tends to make the conversation more lively and natural feeling.

You can see (hear?) this idea in action by talking toMoshi, Kyutai’s realtime audio foundation model they released last year. It was the first realtime audio model on the planet, almost miraculously built by a non-profit team of 8 with a budget that was orders of magnitude smaller than the big labs. It’s a little rough around the edges, but the experience is pretty incredible.

Kyutaipioneered this full duplex architecture, and to build it required a few clever research ideas.

### Multi-stream modeling

First, instead of modeling the conversation as one audio stream – the user’s – they model it withtwo, one for the user and one for the machine. When the machine isn’tspeaking, it’s producing silence (or backchanneling) in the stream. This means that both can be active at the same time (or one active and one inactive), unlike turn based architectures. It’s an extremely simple architectural idea but it mostly solves turn taking, which is arguably the most challenging problems in dialogue / audio AI.

The full duplex architecture ended up being useful for more than just basic realtime audio generation. Kyutai’s second model familyHibikiuses the same idea to realtime translate audio into another language…using the speaker’s exact voice. It'sone of my favorite demosI’ve seen in a while.

Bidirectional audio, especially when you introduce multilinguality, is incredibly difficult. For example…where are you going to find data of the same person in the same voice saying the same thing in multiple different languages? Gradium’s approach here is called DSM (Delayed Streams Modeling) and though it’s beyond the scope of this post, you canread about it here.

### Audio codecs and Mimi

Second, which I mentioned earlier, is their SOTA codec called Mimi, based on earlier research from Neil at Google (SoundStream). This one requires a bit of background, so bear with me.

Codec is short for encoder-decoder and it’s how you compress audio data into something a model can use; you can think of it like embeddings but for audio6. Codecs are in a sense modular, and there are specific ones developed for different types of audio likemusicorspeech. There aretonsof these, and they implement very manual, bespoke rules that we know about the specific medium. Accordingly you can’t use a speech codec for music and vice versa. They also output completely different bitrates based on the target application. These are very bad qualities if you’re trying to train a model.

Neil’s idea while he was at Google Brain was instead to just train a model to do this. This work culminated inSoundStream, a neural codec that can compress speech, music,andgeneral audio at bitrates normally targeted by speech-only codecs. It worked pretty much just as well as domain-specific codecs with all of these ergonomic benefits, and was a big deal in the field at the time.

Another vein of research that Olivier and Neil worked on at Google,AudioLM, introduced an even more novel idea for the model’s compression system. When it comes to audio there are two types of tokens researchers deal with:

1. Semantic tokens– these representthe contentof what’s being said, the words and what they mean.
2. Acoustic tokens– these representthe acoustic styleof what’s being said, how the voice sounds, emotion, etc.

Previous work in the space modeled these two tokens separately using a hierarchical approach, starting with the semantic (content) and then moving onto the acoustic (style). But prevailing open models for generating these semantic tokens arenon-causal(likeWavLM) and so they absolutely do not work in real time. It needs future audio to compute the current embedding.

Kyutai’s approach – and how they solved the real time problem – is bycombiningthese two types of tokens into asingle generation process, thanks to some fancy footwork on summing vector quantizations. When Moshi generates speech it produces 8 tokens per timestep: token 1 is a semantic token, and 2-7 are acoustic tokens. The whole causal system processes audio as it arrives and is thus able to generate all tokens (semantic + acoustic) in real-time.

Reading Kyutai papers, you can’t help but get this frenetic sense of depth. Most of the AI stuff I read on Arxiv has 1-3 fundamental ideas that enable whatever new architecture the paper is about. ButKyutai papers have like 13. For the Moshi paper I’m skipping over innovations in generation (Temporal+Depth transformers), differing weights on token loss, their Inner Monologue method…it’s hard to keep up.

All of this fancy work results in latency (at least theoretically) of 160ms, which is lower than the typical 200-250ms you’d expect in a human conversation. Talking to Moshi you can see that in some senses it’s eventoofast.

## Why small teams win at audio

If you want to distill the story of Gradium (and other audio labs) and why startups continue to beat big labs at audio, it's this:

### 1) Audio models are much smaller and cheaper to train than text models

Moshi has 7B parameters and was trained on 2.1T tokens. Llama 3.1 has 405B parameters trained on 15T tokens—that’s orders of magnitude of difference in cost. You don’t need a thousand people or a massive compute cluster. You need a few exceptional people who understand the domain deeply.

### 2) Audio requires genuine domain expertise in a way text doesn’t

A text tokenizer is essentially a dictionary – you break words into subword tokens and you’re done. An audio codec like Mimi relies on deep understanding of how human hearing works, acoustic psychophysics, how to balance compression against perceptual quality. The bitter lesson is like…not so bitter here.

Similarly, if you’re training a multimodal model, you’re constantly compromising—more coding data means less audio data. Voice is always negotiating with text, video, and image teams for model capacity and training budget. At a focused lab, there's no compromise. Everything optimizes for audio.

### 3) Audio innovation is still about clever ideas efficiently executed, not just scale

The full duplex architecture that Kyutai pioneered is a simple idea (model both streams simultaneously) but it solved the turn-taking problem that had stumped researchers for years. The Mimi codec’s technique for combining semantic and acoustic tokens uses novel compression rather than brute force. The opportunity in audio AI is that “very few people just need to focus on the right questions”.

Gradium is taking all of this and bringing it to the people in real, production-ready models that you can actually use to build things. You can chat with their modelson their site, and look throughtheir API docs here. But most importantly...may the voice be with you.

1For example, audio researchers at the time were contending with significantly lower acceptance rates at major conferences for their papers.

2Ironically, it’s only becoming obviousnowthat interacting with AI via voice has foundational advantages over text. Perhaps if we had realized this a decade ago things wouldn’t have moved so slowly.

3Neil admits even he couldn’t code back then. “I asked to do my coding interview with Soumith Chintalha [who then developed Pytorch] in MATLAB.”

4This, by the way, is one of the reasons you keep seeing the highly unspecific “member of technical staff” title today; it helps avoid this distinction to the outside world entirely.

5In the early days of Kyutai, the founding team had a simple heuristic for assessing candidates: “If you put them in a data center with a gun to their head and no internet, can they implement their stuff from scratch?”

6This comparison isn’t 1 to 1 since the goal of an embedding isn’t compression, it’s representation. But whatever, I’ve got a blog post to write here.

Authors
Justin Gage
Rebecca Dodd
Editors
Acknowledgments
Thanks to Neil Zeghidour and the Gradium team for most of the source material.

MoreWriting

View All

How to build AI into your technical product: lessons from top CEOs and CTOs
AI and ML
Git With It: Founding PM Panel
Misc.
CedarDB, the fastest database you’ve never heard of
Portfolio Spotlight
How Hightouch built their long-running agent harness
AI and ML

Subscribe

Join the newsletter

Success! You’re on the list, check your inbox
Oops! Something went wrong while submitting the form.

Menlo Park800 Menlo Ave, Suite 220Menlo ParkCA 94025San Francisco457 Bryant StSan FranciscoCA 94107

Our Mission
Portfolio
Our Team
Amplify Bio
Privacy

Writing
Projects to Know
Work at an Amplify company
Startup Legal Hub
Barrchives Podcast
X
LinkedIn
© 2025 Amplify Partners. All rights reserved.
