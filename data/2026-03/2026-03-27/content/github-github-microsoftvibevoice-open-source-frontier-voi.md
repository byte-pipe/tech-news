---
title: 'GitHub - microsoft/VibeVoice: Open-Source Frontier Voice AI · GitHub'
url: https://github.com/microsoft/VibeVoice
site_name: github
content_file: github-github-microsoftvibevoice-open-source-frontier-voi
fetched_at: '2026-03-27T11:20:04.687063'
original_url: https://github.com/microsoft/VibeVoice
author: microsoft
description: Open-Source Frontier Voice AI. Contribute to microsoft/VibeVoice development by creating an account on GitHub.
---

microsoft

 

/

VibeVoice

Public

* NotificationsYou must be signed in to change notification settings
* Fork2.7k
* Star24.4k

 
 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

91 Commits
91 Commits
Figures
Figures
 
 
demo
demo
 
 
docs
docs
 
 
finetuning-asr
finetuning-asr
 
 
vibevoice
vibevoice
 
 
vllm_plugin
vllm_plugin
 
 
.gitignore
.gitignore
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
pyproject.toml
pyproject.toml
 
 
View all files

## Repository files navigation

## 🎙️ VibeVoice: Open-Source Frontier Voice AI

### 📰 News

2026-03-06: 🚀 VibeVoice ASR is now part of aTransformers release! You can now use our speech recognition model directly through the Hugging Face Transformers library for seamless integration into your projects.

2026-01-21: 📣 We open-sourcedVibeVoice-ASR, a unified speech-to-text model designed to handle 60-minute long-form audio in a single pass, generating structured transcriptions containing Who (Speaker), When (Timestamps), and What (Content), with support for User-Customized Context. Try it inPlayground.

* ⭐️ VibeVoice-ASR is natively multilingual, supporting over 50 languages — check thesupported languagesfor details.
* 🔥 The VibeVoice-ASRfinetuning codeis now available!
* ⚡️vLLM inferenceis now supported for faster inference; seevllm-asrfor more details.
* 📑VibeVoice-ASR Technique Reportis available.

2025-12-16: 📣 We added experimental speakers toVibeVoice‑Realtime‑0.5Bfor exploration, including multilingual voices in nine languages (DE, FR, IT, JP, KR, NL, PL, PT, ES) and 11 distinct English style voices.Try it. More speaker types will be added over time.

2025-12-03: 📣 We open-sourcedVibeVoice‑Realtime‑0.5B, a real‑time text‑to‑speech model that supports streaming text input and robust long-form speech generation. Try it onColab.

2025-09-05: VibeVoice is an open-source research framework intended to advance collaboration in the speech synthesis community. After release, we discovered instances where the tool was used in ways inconsistent with the stated intent. Since responsible use of AI is one of Microsoft’s guiding principles, we have removed the VibeVoice-TTS code from this repository.

2025-08-25: 📣 We open-sourcedVibeVoice-TTS, a long-form multi-speaker text-to-speech model that can synthesize speech up to 90 minutes long with up to 4 distinct speakers.

## Overview

VibeVoice is afamily of open-source frontier voice AI modelsthat includes both Text-to-Speech (TTS) and Automatic Speech Recognition (ASR) models.

A core innovation of VibeVoice is its use of continuous speech tokenizers (Acoustic and Semantic) operating at an ultra-low frame rate of7.5 Hz. These tokenizers efficiently preserve audio fidelity while significantly boosting computational efficiency for processing long sequences. VibeVoice employs anext-token diffusionframework, leveraging a Large Language Model (LLM) to understand textual context and dialogue flow, and a diffusion head to generate high-fidelity acoustic details.

For more information, demos, and examples, please visit ourProject Page.

Model

Weight

Quick Try

VibeVoice-ASR-7B

HF Link

Playground

VibeVoice-TTS-1.5B

HF Link

Disabled

VibeVoice-Realtime-0.5B

HF Link

Colab

## Models

### 1. 📖VibeVoice-ASR- Long-form Speech Recognition

VibeVoice-ASRis a unified speech-to-text model designed to handle60-minute long-form audioin a single pass, generating structured transcriptions containingWho (Speaker), When (Timestamps), and What (Content), with support forCustomized Hotwords.

* 🕒 60-minute Single-Pass Processing:
Unlike conventional ASR models that slice audio into short chunks (often losing global context), VibeVoice ASR accepts up to60 minutesof continuous audio input within 64K token length. This ensures consistent speaker tracking and semantic coherence across the entire hour.
* 👤 Customized Hotwords:
Users can provide customized hotwords (e.g., specific names, technical terms, or background info) to guide the recognition process, significantly improving accuracy on domain-specific content.
* 📝 Rich Transcription (Who, When, What):
The model jointly performs ASR, diarization, and timestamping, producing a structured output that indicateswhosaidwhatandwhen.

📖 Documentation|🤗 Hugging Face|🎮 Playground|🛠️ Finetuning|📊 Paper

small.mp4

### 2. 🎙️VibeVoice-TTS- Long-form Multi-speaker TTS

Best for: Long-form conversational audio, podcasts, multi-speaker dialogues

* ⏱️ 90-minute Long-form Generation:
Synthesizes conversational/single-speaker speech up to90 minutesin a single pass, maintaining speaker consistency and semantic coherence throughout.
* 👥 Multi-speaker Support:
Supports up to4 distinct speakersin a single conversation, with natural turn-taking and speaker consistency across long dialogues.
* 🎭 Expressive Speech:
Generates expressive, natural-sounding speech that captures conversational dynamics and emotional nuances.
* 🌐 Multi-lingual Support:
Supports English, Chinese and other languages.

📖 Documentation|🤗 Hugging Face|📊 Paper

English

ES_._3.mp4

Chinese

default.mp4

Cross-Lingual

1p_EN2CH.mp4

Spontaneous Singing

2p_see_u_again.mp4

Long Conversation with 4 people

4p_climate_45min.mp4

### 3. ⚡VibeVoice-Streaming- Real-time Streaming TTS

VibeVoice-Realtime is alightweight real‑timetext-to-speech model supportingstreaming text inputandrobust long-form speech generation.

* Parameter size: 0.5B (deployment-friendly)
* Real-time TTS (~300 milliseconds first audible latency)
* Streaming text input
* Robust long-form speech generation (~10 minutes)

📖 Documentation|🤗 Hugging Face|🚀 Colab

VibeVoice_Realtime.mp4

## Contributing

Please seeCONTRIBUTING.mdfor detailed contribution guidelines.

## ⚠️Risks and Limitations

While efforts have been made to optimize it through various techniques, it may still produce outputs that are unexpected, biased, or inaccurate. VibeVoice inherits any biases, errors, or omissions produced by its base model (specifically, Qwen2.5 1.5b in this release).
Potential for Deepfakes and Disinformation: High-quality synthetic speech can be misused to create convincing fake audio content for impersonation, fraud, or spreading disinformation. Users must ensure transcripts are reliable, check content accuracy, and avoid using generated content in misleading ways. Users are expected to use the generated content and to deploy the models in a lawful manner, in full compliance with all applicable laws and regulations in the relevant jurisdictions. It is best practice to disclose the use of AI when sharing AI-generated content.

We do not recommend using VibeVoice in commercial or real-world applications without further testing and development. This model is intended for research and development purposes only. Please use responsibly.

## Star History

## About

Open-Source Frontier Voice AI

microsoft.github.io/VibeVoice/

### Resources

 Readme

 

### License

 MIT license
 

### Code of conduct

 Code of conduct
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

24.4k

 stars
 

### Watchers

152

 watching
 

### Forks

2.7k

 forks
 

 Report repository

 

## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python100.0%