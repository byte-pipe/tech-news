---
title: 'GitHub - abus-aikorea/voice-pro: Gradio WebUI for creators and developers, featuring key TTS (Edge-TTS, kokoro) and zero-shot Voice Cloning (E2 & F5-TTS, CosyVoice), with Whisper audio processing, YouTube download, Demucs vocal isolation, and multilingual translation. · GitHub'
url: https://github.com/abus-aikorea/voice-pro
site_name: github
content_file: github-github-abus-aikoreavoice-pro-gradio-webui-for-crea
fetched_at: '2026-08-01T11:29:51.364226'
original_url: https://github.com/abus-aikorea/voice-pro
author: abus-aikorea
description: Gradio WebUI for creators and developers, featuring key TTS (Edge-TTS, kokoro) and zero-shot Voice Cloning (E2 & F5-TTS, CosyVoice), with Whisper audio processing, YouTube download, Demucs vocal isolation, and multilingual translation. - abus-aikorea/voice-pro
---

abus-aikorea

 

/

voice-pro

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork1.7k
* Star11.5k

 
 
 
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

120 Commits
120 Commits
.github
.github
 
 
app
app
 
 
cosyvoice
cosyvoice
 
 
docs
docs
 
 
model
model
 
 
rvc/
infer
rvc/
infer
 
 
src
src
 
 
third_party/
Matcha-TTS
third_party/
Matcha-TTS
 
 
.env.example
.env.example
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.python-version
.python-version
 
 
CLAUDE.md
CLAUDE.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
configure.bat
configure.bat
 
 
configure.sh
configure.sh
 
 
one_click.py
one_click.py
 
 
pyproject.toml
pyproject.toml
 
 
start-abus.py
start-abus.py
 
 
start-voice.py
start-voice.py
 
 
start.bat
start.bat
 
 
start.sh
start.sh
 
 
uninstall.bat
uninstall.bat
 
 
uninstall.sh
uninstall.sh
 
 
update.bat
update.bat
 
 
update.sh
update.sh
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

# Voice-Pro

The best AI speech recognition, translation, and multilingual dubbing solution 🚀

## 🎙️ An AI-powered web application for speech recognition, translation, and dubbing

한국어∙English∙中文简体∙中文繁體∙日本語∙Deutsch∙Español∙Português

Voice-Pro is a state-of-the-art web app that transforms multimedia content creation. It integrates YouTube video downloading, voice separation, speech recognition, translation, and text-to-speech into a single, powerful tool for creators, researchers, and multilingual professionals.

* 🔊 Top-tier speech recognition:Whisper,Faster-Whisper,Whisper-Timestamped
* 🎤 Zero-shot voice cloning:F5-TTS,E2-TTS,CosyVoice(incl.Fun-CosyVoice3— Korean and 8 more languages)
* 📢 Multilingual text-to-speech:Edge-TTS,kokoro(optionalAzure TTSwith your own keys — seeAzure services)
* 🎥 YouTube processing & audio extraction:yt-dlp
* 🌍 Instant translation for 100+ languages:Deep-Translator(optionalAzure Translatorwith your own keys)

A robust alternative toElevenLabs, Voice-Pro empowers podcasters, developers, and creators with advanced voice solutions.

## ⚠️Please Note

* Due toWeConnectdevelopment work, Voice-Pro development and updates are not possible for the time being.
* We have made all Voice-Pro code open source and completely free. Voice-Pro can now be freely distributed and modified by anyone.
* It works well on Windows with NVIDIA GPU. Operation on Mac and Linux has not been verified.
* Please leave your requests on theorpages.
* Troubleshooting: In most cases, issues can be resolved by deleting theinstaller_filesfolder and then runningstart.batagain (a clean reinstall takes only a few minutes; downloaded AI models inmodel/are kept). Errors are shown in the WebUI as red toasts that stay until closed.

## 📰 News & History

version 4.0

* ⚡Migrated the installer from Miniconda/pip touv— dramatically faster, fully reproducible installs from a committeduv.lock. Everything stays insideinstaller_files/(uv, Python, packages).
* 🐍 Upgraded runtime:Python 3.12, Torch 2.8.0+cu128 (RTX 50-series supported), Gradio 6.20.
* 🎙️ Latest ASR stack:faster-whisper 1.2.1(large-v3-turbo, distil-large-v3.5), openai-whisper 20250625, whisper-timestamped 1.15.9. whisperX was removed (its dependency pins blocked the Gradio 6 upgrade; existing configs fall back to faster-whisper).
* 🗣️ Latest TTS stack:F5-TTS 1.1.21, kokoro 0.9.4, edge-tts 7.x, and re-vendoredCosyVoice(upstream main).
* 🇰🇷 New optional TTS model:Fun-CosyVoice3-0.5B— 9 languages including Korean, selectable in the CosyVoice tab (downloads from the official HF repo on first use).
* 🧹 CUDA Toolkit and Visual Studio Build Tools areno longer required— all dependencies ship prebuilt wheels, and PyTorch bundles the CUDA runtime.
* 🛡️ Friendly torestricted / corporate PCs: no administrator rights needed —start.batauto-downloads a portableffmpegif it is not installed, Whisper model downloads self-heal after interrupted/corrupted transfers, and translation automatically retries with backoff when the network rate-limits the free Google endpoint (failed lines are reported, originals kept).
* 🚨Errors are now visible in the WebUI: every failure shows a red error toast that stays on screen until you close it (previously a 10-second warning that was easy to miss), with actionable messages for common causes (missing ffmpeg, no media registered, etc.).
* 🖥️ UI: migrated toGradio 6(full-width layout for all tabs, subtitle tracks shown directly in the video players).
* 🧽uninstall.batno longer requires administrator rights and no longer force-reboots;uninstall.bat silentruns unattended.

version 3.2

* We have been focusing onWeConnectdevelopment for the past few months and have not been able to manage Voice-Pro at all.
* We have decided to open source all Voice-Pro code.
* Voice-Pro is completely free and supports Windows, Mac, Linux.
* WeConnectis an application for global cultural exchange.
* Connect with people from all over the world for meaningful cultural exchanges, language learning, and international friendships.

version 3.1

* 🪄 Support for fine-tuned models ofF5-TTS
* 🌍 Supported languagesEnglish &Chinese:SWivid/F5-TTS_v1Finnish:AsmoKoskinen/F5-TTS_Finnish_ModelFrench:RASPIAUDIO/F5-French-MixedSpeakers-reducedHindi:SPRINGLab/F5-Hindi-24KHzItalian:alien79/F5-TTS-italianJapanese:Jmica/F5TTS/JA_21999120Russian:hotstone228/F5-TTS-RussianSpanish:jpgallegoar/F5-Spanish
* English &Chinese:SWivid/F5-TTS_v1
* Finnish:AsmoKoskinen/F5-TTS_Finnish_Model
* French:RASPIAUDIO/F5-French-MixedSpeakers-reduced
* Hindi:SPRINGLab/F5-Hindi-24KHz
* Italian:alien79/F5-TTS-italian
* Japanese:Jmica/F5TTS/JA_21999120
* Russian:hotstone228/F5-TTS-Russian
* Spanish:jpgallegoar/F5-Spanish

version 3.0

* 🔥 Removed theAI Coverfeature.
* 🚀 Added support form-bain/whisperX.

version 2.0

* 🐍 Built with Python 3.10.15, Torch 2.5.1+cu124, and Gradio 5.14.0.
* 🆓 Free trial supports media up to60 secondsin length.
* 🔥 Added theAI Coverfeature.
* 🎤 Introduced support forCosyVoiceandkokoro.
* ⏳ Initial run downloadsCozyVoice2-0.5B (9GB), which may take over an hour depending on network speed.
* 🎧 Voice samples for cloning will be continuously updated.
* 📝 AddedspaCyfor natural sentence-by-sentence translation and TTS.
* ☁️ Subscription version includesMicrosoft AzureTranslator and TTS.
* 🏪 Subscription offersunlimited usage(no 60-second limit) during the subscription period, available via.

## 🎥 YouTube Showcase

Demo for Voice-Pro (v2.0)

F5-TTS: Voice Cloning

Live Transcription & Translation

Multi-Lingual Voice Cloning: Korean - German

Multi-Lingual Voice Cloning: English - Korean

Multi-Lingual Voice Cloning: Korean - Japanese

NVIDIA RTX Video Super-Resolution

AI Karaoke

Multi-Lingual Voice Cloning: English - Korean

## ⭐ Key Features

### 1. Dubbing Studio

* YouTube video downloads & audio extraction
* Voice separation withDemucs
* Supports 100+ languages for speech recognition & translation

### 2. Speech Technologies

* Speech-to-Text:Whisper,Faster-Whisper,Whisper-Timestamped
* Text-to-Speech:Edge-TTS: 100+ languages, 400+ voicesE2-TTS,F5-TTS,CosyVoice: Zero-shot cloningkokoro: Ranked #2 in HuggingFace TTS Arena
* Edge-TTS: 100+ languages, 400+ voices
* E2-TTS,F5-TTS,CosyVoice: Zero-shot cloning
* kokoro: Ranked #2 in HuggingFace TTS Arena

### 3. Real-Time Translation

* Instant speech recognition
* Multilingual translation on the fly
* Customizable audio inputs

## 🤖 WebUI

### Dubbing StudioTab

* All-in-one hub: YouTube downloads, noise removal, subtitles, translation, & TTS
* Supports all ffmpeg-compatible formats
* Output options: WAV, FLAC, MP3
* Subtitles & recognition for 100+ languages
* TTS with speed, volume, & pitch controls

### Whisper CaptionTab

* Subtitle-focused: 90+ languages
* Video-integrated subtitle display
* Word-level highlighting & denoise options

### TranslateTab

* Translation for 100+ languages
* Supports subtitle files (ASS, SSA, SRT, etc.)
* Real-time voice recognition & translation

### Speech GenerationTab

* Options:Edge-TTS,F5-TTS,CosyVoice,kokoro
* Celeb voice podcasts & multilingual support

## 🎤✨ Reference Voice

* Please request the voice you want to add on the Issues page.Issues

English

 

Andrew Bustamante

Andrew Huberman

Avi Loeb

Ben Shapiro

Brett Johnson

Brian Keating

Coffeezilla

Dan Carlin

David Buss

David Fravor

David Kipping

Dennis Whyte

Donald Hoffman

Donald Trump

Douglas Murray

Duncan Trussell

Elon Musk

Garry Nolan

Jack Barsky

James Sexton

Jeff Bezos

Joe Rogan

John Mearsheimer

Jordan Peterson

Kanye 'Ye' West

Mark Zuckerberg

Michael Levin

Michael Saylor

Michio Kaku

MrBeast

Nick Lane

Paul Rosolie

Ryan Graves

Sam Altman

Sam Harris

Stephen Wolfram

Tucker Carlson

Vitalik Buterin

Yuval Harari

Chinese

 

迪丽热巴 (Dílì Rèbā)

蔡依林 (Cài Yīlín)

吴亦凡 (Wú Yìfán)

李易峰 (Lǐ Yìfēng)

杨幂 (Yáng Mì)

赵丽颖 (Zhào Lìyǐng)

Korean

 

BTS 진 (Jin)

BTS RM

IU (아이유)

이병헌

이정재

유재석

Japanese

 

綾瀬はるか (Ayase Haruka)

## 💻 System Requirements

* OS:Windows 10/11 (64-bit), Linux, Mac (Apple Silicon)
* GPU:NVIDIA GPU with a recent driver (>= 570 recommended; RTX 50-series supported). CUDA Toolkit installation is NOT required.
* VRAM:4GB+ (8GB+ preferred)
* RAM:4GB+
* Storage:20GB+ free space
* Internet:Required

## 📀 Installation

Install Voice-Pro with ease usingconfigure.batandstart.bat(use configure.sh and start.sh on Mac/Linux).

### 1. Get the Package

* Clone or download the latest release (Source code (zip)) from

git clone https://github.com/abus-aikorea/voice-pro.git

### 2. Install & Run

1. 🚀configure.bat(optional)* Sets up git and ffmpeg system-wide (CUDA Toolkit / Visual Studio are no longer needed)
* Requires administrator rights; run once
* No admin rights? Skip it —start.batdownloads a portable ffmpeg automatically
2. 🚀start.bat* Launches Voice-Pro WebUI
* First run downloads uv + Python 3.12 and installs all dependencies from the lockfile (minutes, not hours), then downloads AI models (~10GB — this is the slow part)
* GPU/CPU is auto-detected; override with theGPU_CHOICEenvironment variable (G=NVIDIA,C=CPU) or by deletinginstaller_files\gpu_choice.txt
* Retry after deletinginstaller_filesif issues arise

### 3. Update

* 🚀update.bat: Re-syncs the Python environment exactly to the committed lockfile (fast)

### 4. Uninstall

* Rununinstall.bator delete the folder (portable install)
* No administrator rights required; addsilentfor unattended removal (uninstall.bat silent)
* Only theinstaller_filesfolder is removed — yourmodel/andworkspace/folders are kept

## 🔑 Azure services (optional, .env)

By default Voice-Pro usesfreeservices: Deep-Translator (Google's free web endpoint) for translation and Edge-TTS for speech synthesis. If you have your ownMicrosoft Azuresubscription, you can switch both to the Azure APIs:

1. Copy.env.exampleto.envin the project root:copy .env.example .env#Windowscp .env.example .env#Mac/Linux
2. Fill in your Azure credentials:#Azure Speech Service (TTS)AZURE_SPEECH_KEY=your_azure_speech_key_hereAZURE_SPEECH_REGION=eastus#Azure Translator ServiceAZURE_TRANSLATOR_KEY=your_azure_translator_key_hereAZURE_TRANSLATOR_ENDPOINT=https://your-translator-resource.cognitiveservices.azure.com/AZURE_TRANSLATOR_REGION=eastus
3. Restart Voice-Pro. Valid keys are detected automatically at startup — translation switches toAzure Translatorand the first Speech Generation tab becomesAzure-TTS.

When is this worth setting up?

* 🏢Corporate / restricted networks: security appliances often rate-limit or block the freetranslate.google.comendpoint, which slows down or fails long subtitle translations. Voice-Pro retries with backoff and keeps the original text for failed lines (you will see a warning with the failure count), but Azure Translator avoids the problem entirely.
* 🗣️ Higher-quality/consistent TTS voices and higher rate limits.
* DoNOTcommit.envto version control — it contains your private keys.

## ❓Tips & Tricks

#### If Browser does not run automatically

* Close the Windows-Commnad window and run start.bat again.
* Run the browser directly and enter the address displayed in the Windows-Command window (e.g.http://127.0.0.1:7870) in the address bar.

#### If a CUDA Out-Of-Memory error occurs

* Check the GPU memory status in Windows Task Manager - Performance tab.
* Set the Denoise level to 0 or 1. Denoise level 2 requires at least 8GB of GPU memory.
* Set Compute Type to int type. The float type has better quality, but requires more GPU memory.

#### How to improve the quality of subtitles?

* The quality of subtitles tends to improve with larger Whisper models, but this is not necessarily the case. large > medium > small > base > tiny
* Among compute types, float type has good performance. The int type is a model that reduces GPU usage and increases speed through model quantization. On the other hand, performance decreases.
* If you increase the denoise level, more background sounds will be removed, and only the remaining voice will be used for voice recognition. It does not always guarantee good results.

## 🚨 Notice

* Due toWeConnectdevelopment work, there will be no Voice-Pro updates for the time being.
* All Voice-Pro code has been made open source. It is now completely free to use.
* WeConnectis a communication platform for global cultural exchange.

## ⏳ SaaS Platforms for Subtitling, Translation, and TTS

The following table lists SaaS platforms supporting subtitling, translation, and text-to-speech (TTS/dubbing) functionalities. Costs are calculated for processing a 60-minute Korean video, including subtitle generation, English translation, and English dubbing, based on the latest available pricing data as of April 15, 2025.

Platform

Subtitling

Translation

TTS/Dubbing

Cost for 60-min Video (USD, Approx.)

Key Features

Maestra

✅

✅

✅

$23.70

125+ languages, real-time captions, SEO keyword extraction, 15-min free trial.

Kapwing

✅

✅

✅

$30~$40 (Pro plan, per minute)

AI subtitles, 100+ language translations, auto lip-sync dubbing, free tier.

VEED.IO

✅

✅

❌

$24~$36 (Pro plan, partial)

99.9% accurate subtitles, Instagram-optimized captions, intuitive editor.

HappyScribe

✅

✅

✅

$36~$48 (Pay-as-you-go)

120+ languages, professional proofreading, secure, meeting transcription.

Sonix

✅

✅

✅

$30~$40 (Standard plan)

54+ languages, 30-min free transcription, YouTube/Zoom integration.

Descript

✅

✅

✅

$36~$48 (Creator plan)

Text-based editing, Overdub TTS, filler word removal, 1-hour free transcription.

AppTek

✅

✅

✅

Custom pricing (Contact)

Media-focused, custom models, metadata generation, cloud-based Workbench.

Transkriptor

✅

✅

❌

$12~$18 (Pay-as-you-go)

100+ languages, YouTube link transcription, 99% accuracy, simple editor.

### Cost Calculation Details

* Maestra: Premium Plan ($158/month, 1200 credits). 60-min video: 60 credits (subtitles) + 60 credits (translation) + 60 credits (dubbing) = 180 credits. Cost = (180/1200) * $158 = $23.70.
* Kapwing: Pro plan (~$24/month, limited minutes). Estimated $0.50~$0.67/min for subtitles+translation+dubbing (based on per-minute pricing trends). 60-min cost: $30~$40. Exact pricing requires confirmation.
* VEED.IO: Pro plan (~$24/month). Subtitles+translation estimated at $0.40~$0.60/min. No TTS, so partial processing. 60-min cost: $24~$36. Confirm atveed.io.
* HappyScribe: Pay-as-you-go (~$0.20/min transcription, $0.20/min translation, $0.20/min dubbing). 60-min cost: $36~$48 (assuming combined services). Confirm athappyscribe.com.
* Sonix: Standard plan (~$10/hour transcription, additional for translation/dubbing). Estimated $0.50~$0.67/min total. 60-min cost: $30~$40. Confirm atsonix.ai.
* Descript: Creator plan (~$24/month, limited hours). Estimated $0.60~$0.80/min for subtitles+translation+dubbing. 60-min cost: $36~$48. Confirm atdescript.com.
* AppTek: Custom pricing for enterprise. No public per-minute rates. Contactapptek.aifor quotes.
* Transkriptor: Pay-as-you-go ($0.05~$0.10/min transcription, similar for translation). No TTS, so partial processing. 60-min cost: $12~$18. Confirm attranskriptor.com.

### Notes

* Cost for 60-min Video: Costs are approximate and assume processing a 60-minute Korean video for subtitles, English translation, and English dubbing (where available). Platforms without TTS (e.g., VEED.IO, Transkriptor) reflect partial processing costs.
* Language Support: Most platforms support Korean and English. Verify specific language availability on their websites.
* Use Cases:Media/Entertainment: AppTek, MaestraSocial Media: Kapwing, VEED.IOPodcasts/Interviews: Sonix, DescriptE-learning/Global Content: Transkriptor, HappyScribe
* Media/Entertainment: AppTek, Maestra
* Social Media: Kapwing, VEED.IO
* Podcasts/Interviews: Sonix, Descript
* E-learning/Global Content: Transkriptor, HappyScribe
* Pricing Updates: Pricing may vary due to plan changes or promotions. Check official websites for the latest details.
* For contributions or specific use case recommendations, open an issue or submit a pull request in this repository!

## ☕ Contributions

Hello, I'm David from the Voice-Pro team.
Our team discovers the best AI technologies in the industry and provides them for anyone to use easily and conveniently.
We are a small startup in Korea that has only been around for a year. We are working hard to help you and other creators produce great content.

Your ⭐⭐⭐⭐⭐ review would be greatly appreciated as it helps our business grow with you. Please help support our small team.

Thank you,
ABUS Customer Service

* If you want to participate in and help us with this project, feel free to create anIssues
* If something goes wrong, please submit aPull requeststo improve this project.
* Any type of contribution is welcome.
* For inquiries related to purchases, business partnerships, technical tuning, investments, and other matters, please contact us by email. (abus.aikorea@gmail.com)."
* If you like this project, please star this repository. We would greatly appreciate it. ⭐⭐⭐
* You can support Voice-Pro with a donation here:

## 📬 Contact

* Email:abus.aikorea@gmail.com
* Homepage (Korean):https://www.wctokyoseoul.com

## 🙏 Credits

* Demucs:https://github.com/facebookresearch/demucs
* yt-dlp:https://github.com/yt-dlp/yt-dlp
* gradio:https://github.com/gradio-app/gradio
* edge-TTS:https://github.com/rany2/edge-tts
* F5-TTS:https://github.com/SWivid/F5-TTS.git
* openai-whisper:https://github.com/openai/whisper
* faster-whisper:https://github.com/SYSTRAN/faster-whisper
* whisper-timestamped:https://github.com/linto-ai/whisper-timestamped
* CosyVoice:https://github.com/FunAudioLLM/CosyVoice
* kokoro:https://github.com/hexgrad/kokoro
* Deep-Translator:https://github.com/nidhaloff/deep-translator
* spaCy:https://github.com/explosion/spaCy

## ©️ Copyright

byABUS