---
title: Build real-time voice applications with Gemini 3.8 Live and 3.5 Transcribe - DEV Community
url: https://dev.to/googleai/build-real-time-voice-applications-with-gemini-38-live-and-35-transcribe-4nb5
site_name: devto
content_file: devto-build-real-time-voice-applications-with-gemini-38
fetched_at: '2026-09-16T15:21:44.825690'
original_url: https://dev.to/googleai/build-real-time-voice-applications-with-gemini-38-live-and-35-transcribe-4nb5
author: Thor 雷神 Schaeff
date: '2026-09-16'
description: Yesterday, we released new Gemini Live models in the Gemini API and Google AI Studio, expanding our... Tagged with ai, live, voice, gemini.
tags: '#ai, #live, #voice, #gemini'
---

Yesterday, wereleasednew Gemini Live models in theGemini APIandGoogle AI Studio, expanding our developer suite for building real-time, voice-first product experiences:

Gemini 3.8 Liveand3.8 Live Extended Thinking:Gemini 3.8 Live brings a step change to our native speech-to-speech models, capable of performing tasks while maintaining dialogue. For complex requests, 3.8 Live Extended Thinking delivers deeper reasoning, ranking #1 on Artificial Analysis’ Speech-to-Speech leaderboard.

Gemini 3.5 Transcribe: Our dedicated speech-to-text model brings highly precise transcription across 85+ languages. Released last month, it achieved an average Word Error Rate (WER) of 4.0% (streaming) and 2.6% (non-streaming).

## Gemini 3.8 Live & 3.8 Live Extended Thinking: Build more intelligent conversational agents

Our new models,Gemini 3.8 Liveand3.8 Live Extended Thinkingenable developers to build voice agents that can reason and execute tasks while maintaining the flow of conversations. Key capabilities include:

* Asynchronous function calling:Execute API and tool calls in the background while continuing to stream audio responses to the user
* Visual context:Ground dialogue in live visual inputs to help enable agents that can understand what users sayandsee
* Alphanumeric precision:Accurately parse confirmation codes, claim numbers, and technical data
* Multilingual support:Reach global audiences with coverage for 97+ languages and accent consistency
* Incremental content updates:Seamlessly merge real-time audio with structured data to return context-aware responses

3.8 Live Extended Thinking also supportsconfigurable thinkingto help handle complex, multi-step reasoning in the background, while responding or narrating its progress in the main conversation. These models represent a step-change from our previous live models and provide a more streamlined alternative to cascaded architectures.

Gemini 3.8 Live and Gemini 3.8 Live Extended Thinking are available via theLive API. Competitivelypricedat $0.005/min for audio input and $0.018/min* for audio output, they allow developers to scale voice applications with industry-leading performance.

Developers can also access the models throughAgora,Fishjam,LangChain,LiveKit,Pipecat,Vercel, andVision Agents, our Live API integration partners that handle media streaming infrastructure for real-world deployment.

## Gemini 3.5 Transcribe: Convert streamed speech to text

Real-time speech understanding is critical for voice-first interfaces. Last month, we released Gemini 3.5 Transcribe for low-latency transcription with high precision, achieving a 4.0% WER, and useful features:

* Automatic code-switching:Handle intra-sentence and inter-sentential code- and language-switching without manual configuration
* Custom vocabulary biasing:Steer speech recognition toward domain-specific terms, uncommon jargon, company names, and proper nouns by passing acustom_vocabularylist of up to 1,000 terms
* Smart transcription mode: Deliver polished, reader-ready transcripts with structured formatting, self-corrections, and disfluency removal that eliminates filler words

3.5 Transcribe supports 85+ languages and provides a strong listening engine for voice experiences and stateless tasks like sub-second captioning, call center agents, and real-time audio analytics. You can also access the model via the Interactions API to transcribe audio files up to 1 hour long with structured timestamps and speaker labeling. Read ourdeveloper guideto learn more.

## Our complete audio suite for developers

To get started, try out the models inai.studio/live, clone example apps fromGitHub, or equip your agent with ourlive api skill.

You can also create audio experiences with our speech and music generation models, all available in the Gemini API:

* Gemini 3.5 Live Translate: Speech-to-speech translation across more than 70 languages
* Gemini 3.1 Flash TTS: Highly configurable speech generation (with more updates coming soon)
* Lyria 3.5: Production-grade music generation

The mic is yours, and we can’t wait to hear what you build!

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse