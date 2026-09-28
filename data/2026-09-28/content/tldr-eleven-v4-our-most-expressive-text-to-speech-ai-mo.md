---
title: 'Eleven v4: Our most expressive text-to-speech AI model yet'
url: https://elevenlabs.io/blog/eleven-v4
site_name: tldr
content_file: tldr-eleven-v4-our-most-expressive-text-to-speech-ai-mo
fetched_at: '2026-09-28T23:42:06.903418'
original_url: https://elevenlabs.io/blog/eleven-v4
date: '2026-09-28'
description: 'Eleven v4 and v4 Turbo: more emotional nuance, faster responses, stronger voice cloning. Live now in ElevenAgents, ElevenCreative and API.'
tags:
- tldr
---

Introducing Eleven v4Introducing Eleven v4, our fastest and most emotive voice model

Discover
Skip to content
Log in
Sign up
Contact sales
Log in
* Discover Eleven v4
* Sign up

A line of text can change significantly depending on how it’s spoken. “I need you to stay calm" should sound different depending on who's saying it, whether that's a doctor delivering it gently to a frightened patient, or a character in a game shouting to his squad before dropping into battle.

Today we're launchingEleven v4, our most emotive text-to-speech model yet, and its low-latency variant, Eleven v4 Turbo.

Ranked #1 by Artificial Analysis1, and preferred by ~75% of listeners in blind head-to-head tests over competing models2, Eleven v4 was designed to interpret tone, pacing, emotion, character, and context. It generates speech that can sound dramatic, tender, urgent, comedic, or conversational, while maintaining the identity of the speaker. More natural multi-speaker dynamics make conversations feel responsive, rather than like separate lines assembled together. Speakers respond to the context of the conversation, producing more natural dialogue and character interactions.

## A new architecture built for performance

Built on an entirely new architecture, Eleven v4 is our most emotiveText to Speechmodel ranked #1 by Artificial Analysis1. Eleven v4 Turbo brings that same technology to low-latency use cases like agents. With a median inference latency of ~100ms, it can respond faster than the average pause between two people talking.

Both models can generate speech that feels emotive, rather than mechanical. Underlying audio fidelity is also higher across the board, with cleaner, more natural-sounding output.

Earlier generations of text-to-speech models can read text aloud, but Eleven v4 provides an emotional depth to speech that feels far more natural. The model can interpret the intended tone, how the speech should be paced, the character of the writing, and context from the text to deliver emotionally resonant speech.

[excited, happy] Big news, everyone. Our summer menu drops this Friday. And yes, the mango sticky rice is finally back.
0:00
[sleepy drowsy voice] Mmm, five more minutes. [yawning] I promise I'll get up right after this dream finishes.
0:00

Users also have fine-grained control over outputs, and can describe how a line should be delivered in natural language. They can also add specific instructions on how to say certain phrases, what emotion they should convey, and even sound effects, using inline tags like [laughs], [said angrily in French accent], [light rain], or [phone buzzing]. Eleven v4 follows these audio tags and direction prompts more accurately than prior models, so the delivery you describe is what you get. This makes it easier to direct narration, flesh out characters or their dialogue, and other places where delivery matters.

TheElevenLabs developer documentationcovers the full tag syntax and how to apply these tags through the API. Support for the International Phonetic Alphabet (IPA) phonemes has also been significantly improved, so custom pronunciations behave more reliably.

Eleven v4 also brings improvements in consistency and dynamic conversations between multiple speakers. Using a new method for capturing speakers’ identities, Eleven v4 preserves the unique qualities of each voice. It’s able to keep speech consistent through agent conversations, audiobooks, or ads. Because the model understands the context of a whole scene, it generates natural dialogue where speakers respond to what's just been said, rather than stitching together isolated lines.

## A Turbo model for low-latency use cases

High-quality voice models have tended to be slower to generate speech, meaning users have had to choose between fast or expressive voice agents. Many have opted for proficient, but monotone, agents that can seem robotic to a flustered customer just looking to resolve their issue.

Eleven v4 Turbo combines speed and emotion with a median time to first speech of ~150ms3, making it possible to deploy powerful agents in countless industries, from warm, reassuring agents that can accurately pronounce medical terms in healthcare, to fast-talking, slang-wielding agents to entertain players in gaming.

The Eleven v4 Turbo model is built to work with ElevenLabs’ conversational agents platform, ElevenAgents. Other agent builders stitch together models and software from different vendors, meaning users are left without a way to refine or improve the model outputs for their individual use cases. ElevenLabs’ research and engineering teams optimized Eleven v4 Turbo and ElevenAgents together as one system, delivering more expressive, reliable, and low latency agents.

## One voice, myriad languages

The way we communicate varies by context, location, even the time of day. Building expressive speech that mirrors that, across languages, remains one of the hardest challenges in audio AI.

Eleven v4 is a step up in all these areas, and the improvements extend beyond just how the model pronounces phrases. Eleven v4 better captures rhythm, emotion, and delivery across languages, helping creators produce speech that feels natural to the language and context. The way you’d speak to an elderly stranger in Japan is quite different from the way you’d speak to them in Italy, for example.

Both Eleven v4 and Eleven v4 Turbo support more than 90 languages. Now, a voice recorded in one language also speaks any other fluently, adopting the accent of a native speaker while retaining the identity of the original. That accent adherence is noticeably stronger than before, so the voice no longer drifts back toward its source accent over the course of a generation.

Catalan

Sovint caminem per la vida amb la mirada fixada en l'horitzó, preocupats pel demà, sense adonar-nos que el miracle real està passant just sota els nostres peus.
0:00

Spanish

El viento susurra historias olvidadas entre las hojas secas del parque. La ciudad aún duerme bajo un manto de neblina dorada, ajena al bullicio que pronto inundará sus calles. Un viejo farol parpadea por última vez antes de ceder su lugar a los primeros rayos del sol. En este preciso instante, el tiempo parece detenerse.
0:00

For dubbing and localization, this means the voice of the brand you’ve decided on — whether that’s a celebrity actor you’re working with or a tone that best fits your company’s style — will sound great in any language supported by Eleven v4.

## More authentic, consistent voice cloning

Voice cloning is more authentic, powerful, and consistent across Eleven v4 and Eleven v4 Turbo, with significantly better speaker similarity to the original source voice. Instant Voice Clones can now capture voices with high fidelity using just 10 seconds of audio.

Real voice

Hey, thanks so much for holding. Um, so I've got your account pulled up now and it does look like the charge did go through twice on the eleventh which, yeah, definitely shouldn't have happened. Let me get that refund started for you right now.
0:00

Eleven v4

Hey, thanks so much for holding. Um, so I've got your account pulled up now, and it does look like the charge did go through twice on the 11th, which, yeah, definitely shouldn't have happened. Um, let me get that refund started for you right now.
0:00

Eleven v4 also preserves speaker identity more reliably across generations, dialogue, narration, and regenerated lines. This means for long-form projects, the characters, narrators, and cloned voices stay consistent throughout a production. Eleven v4 also adds support for Professional Voice Clones (PVC), for the highest-fidelity cloning use cases.

Request stitching — chaining generations together for longer-form content — is also significantly more reliable in Eleven v4, which improves the experience of working in ElevenLabs Studio and the ElevenLabs Reader App.

## Hear the difference for yourself

Eleven v4 and Eleven v4 Turbo are the culmination of our latest research in expressive speech generation. They're built for content where delivery matters as much as the words themselves, whether that’s audiobooks, character performances, voiceovers, dubbing, or localizing conversational agents.

Both models are available now in ElevenAgents, ElevenCreative, and via ElevenAPI.Create a free accountto start generating with Eleven v4 or Eleven v4 Turbo today.

1. Artificial Analysis, Provider Voice Arena Leaderboard, Sept 2026
2. Based on blind head-to-head user preference testing against Cartesia Sonic 3.6, Inworld TTS-2, Google Gemini 3.8 Flash-Lite TTS, and Google Gemini 3.8 Flash TTS, September 2026. For each pair, graders heard the same line from Eleven v4 and one competitor, presented blind, and judged which was more expressive and which sounded more natural; ties counted as half.
3. Median time from request to audible speech. Measured September 2026 with identical scripts and default settings against Cartesia Sonic 3.6, xAI TTS, Google Gemini 3.8 Flash-Lite TTS, and OpenAI GPT-4o mini TTS; network latency measured and removed for all systems. Eleven v4 Turbo over WebSocket streaming.

## Similar articles

* ### The first AI that can laughCategoryResearchDateNov 24, 2022
* ### Valiant Finance deploys ElevenLabs across customer support and campaign productionCategoryCustomer StoriesDateJul 29, 2026
* ### Eliane and Alberto: The 1 Million Voices Initiative Expands to BrazilCategoryImpactDateSep 4, 2026
* ### How to transcribe a YouTube video: Step-by-step guideCategoryResourcesDateJul 22, 2026

Create with the highest quality AI Audio

Talk to sales
Sign up