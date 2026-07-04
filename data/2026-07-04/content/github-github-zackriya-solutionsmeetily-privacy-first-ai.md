---
title: 'GitHub - Zackriya-Solutions/meetily: Privacy first, AI meeting assistant with 4x faster Parakeet/Whisper live transcription, speaker diarization, and Ollama summarization built on Rust. 100% local processing. no cloud required. Meetily (Meetly Ai - https://meetily.ai) is the #1 Self-hosted, Open-source Ai meeting note taker for macOS & Windows. · GitHub'
url: https://github.com/Zackriya-Solutions/meetily
site_name: github
content_file: github-github-zackriya-solutionsmeetily-privacy-first-ai
fetched_at: '2026-07-04T11:32:34.310997'
original_url: https://github.com/Zackriya-Solutions/meetily
author: Zackriya-Solutions
description: 'Privacy first, AI meeting assistant with 4x faster Parakeet/Whisper live transcription, speaker diarization, and Ollama summarization built on Rust. 100% local processing. no cloud required. Meetily (Meetly Ai - https://meetily.ai) is the #1 Self-hosted, Open-source Ai meeting note taker for macOS & Windows. - GitHub - Zackriya-Solutions/meetily: Privacy first, AI meeting assistant with 4x faster Parakeet/Whisper live transcription, speaker diarization, and Ollama summarization built on Rust. 100% local processing. no cloud required. Meetily (Meetly Ai - https://meetily.ai) is the #1 Self-hosted, Open-source Ai meeting note taker for macOS & Windows.'
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 Zackriya-Solutions

 

/

meetily

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.6k
* Star14.4k

 
 
 
 
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

556 Commits
556 Commits
.github
.github
 
 
backend
backend
 
 
docs
docs
 
 
frontend
frontend
 
 
llama-helper
llama-helper
 
 
scripts
scripts
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
BLUETOOTH_PLAYBACK_NOTICE.md
BLUETOOTH_PLAYBACK_NOTICE.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
LICENSE.md
LICENSE.md
 
 
PRIVACY_POLICY.md
PRIVACY_POLICY.md
 
 
README.md
README.md
 
 
View all files

## Repository files navigation

# Privacy-First AI Meeting Assistant

 
 

### Open Source • Privacy-First • Enterprise-Ready

Get latestProduct updatesWebsite•LinkedIn•Meetily Discord•Privacy-First AI•Reddit

A privacy-first AI meeting assistant that captures, transcribes, and summarizes meetings entirely on your infrastructure. Built by expert AI engineers passionate about data sovereignty and open source solutions. Perfect for enterprises that need advanced meeting intelligence without compromising on privacy, compliance, or control.

View full Demo Video

Meetily PRO Upgrade Offer- Meetily PRO is available for users who need enhanced accuracy, advanced exports, custom summary workflows, and team-ready features. Use coupon codeLAUNCH20for20% offuntil the next Meetily Community Edition release. Speaker diarization is also planned for PRO in mid-June.Explore Meetily PRO →

Table of Contents

* Introduction
* Why Meetily?
* Features
* Installation
* Key Features in Action
* System Architecture
* For Developers
* Meetily PRO
* Contributing
* License

## Introduction

Meetily is a privacy-first AI meeting assistant that runs entirely on your local machine. It captures your meetings, transcribes them in real-time, and generates summaries, all without sending any data to the cloud. This makes it the perfect solution for professionals and enterprises who need to maintain complete control over their sensitive information.

## Why Meetily?

While there are many meeting transcription tools available, this solution stands out by offering:

* Privacy First:All processing happens locally on your device.
* Cost-Effective:Uses open-source AI models instead of expensive APIs.
* Flexible:Works offline and supports multiple meeting platforms.
* Customizable:Self-host and modify for your specific needs.

The Privacy Problem

Meeting AI tools create significant privacy and compliance risks across all sectors:

* $4.4M average cost per data breach(IBM 2024)
* €5.88 billion in GDPR finesissued by 2025
* 400+ unlawful recording casesfiled in California this year

Whether you're a defense consultant, enterprise executive, legal professional, or healthcare provider, your sensitive discussions shouldn't live on servers you don't control. Cloud meeting tools promise convenience but deliver privacy nightmares with unclear data storage practices and potential unauthorized access.

Meetily solves this:Complete data sovereignty on your infrastructure, zero vendor lock-in, and full control over your sensitive conversations.

## Features

* Local First:All processing is done on your machine. No data ever leaves your computer.
* Real-time Transcription:Get a live transcript of your meeting as it happens.
* AI-Powered Summaries:Generate summaries of your meetings using powerful language models.
* Multi-Platform:Works on macOS, Windows, and Linux.
* Open Source:Meetily is open source and free to use.
* Flexible AI Provider Support:Choose from Ollama (local), Claude, Groq, OpenRouter, or use your own OpenAI-compatible endpoint.

## Installation

### 🪟Windows

1. Download the latestx64-setup.exefromReleases
2. Run the installer

### 🍎macOS

1. Downloadmeetily_0.4.0_aarch64.dmgfromReleases
2. Open the downloaded.dmgfile
3. DragMeetilyto your Applications folder
4. OpenMeetilyfrom Applications folder

### 🐧Linux

Build from source following our detailed guides:

* Building on Linux
* General Build Instructions

Quick start:

git clone https://github.com/Zackriya-Solutions/meeting-minutes

cd
 meeting-minutes/frontend
pnpm install
./build-gpu.sh

## Key Features in Action

### 🎯 Local Transcription

Transcribe meetings entirely on your device usingWhisperorParakeetmodels. No cloud required.

### 📥 Import & EnhanceBeta

Import existing audio files to generate transcripts, or enhance to re-transcribe any recorded meeting with a different model or language, all processed locally.

Contributed byJeremi Joslin, improved byVishnu P SandMohammed Safvan

### 🤖 AI-Powered Summaries

Generate meeting summaries with your choice of AI provider.Ollama(local) is recommended, with support for Claude, Groq, OpenRouter, and OpenAI.

### 🔒 Privacy-First Design

All data stays on your machine. Transcription models, recordings, and transcripts are stored locally.

### 🌐 Custom OpenAI Endpoint Support

Use your own OpenAI-compatible endpoint for AI summaries. Perfect for organizations with custom AI infrastructure or preferred providers.

### 🎙️ Professional Audio Mixing

Capture microphone and system audio simultaneously with intelligent ducking and clipping prevention.

### ⚡ GPU Acceleration

Built-in support for hardware acceleration across platforms:

* macOS: Apple Silicon (Metal) + CoreML
* Windows/Linux: NVIDIA (CUDA), AMD/Intel (Vulkan)

Automatically enabled at build time - no configuration needed.

## System Architecture

Meetily is a single, self-contained application built withTauri. It uses a Rust-based backend to handle all the core logic, and a Next.js frontend for the user interface.

For more details, see theArchitecture documentation.

## For Developers

If you want to contribute to Meetily or build it from source, you'll need to have Rust and Node.js installed. For detailed build instructions, please see theBuilding from Source guide.

## Meetily Pro

Meetily PROis a professional-grade solution with enhanced accuracy and advanced features for serious users and teams. Built on a different codebase with superior transcription models and enterprise-ready capabilities.

### Community Thank-You Offer

Meetily Community Edition will remain free and open source. PRO exists for users and teams who want a more advanced meeting workflow, including higher transcription accuracy, custom summary templates, advanced exports, auto-meeting detection, and self-hosted deployment options.

For the community that helped Meetily grow, we are making the upgrade easier: use coupon codeLAUNCH20for20% off Meetily PROuntil the next Meetily Community Edition release.

Speaker diarization is planned for mid-June, bringing automatic speaker separation to PRO meetings.

### Key Advantages Over Community Edition:

* Enhanced Accuracy: Superior transcription models for professional-grade accuracy
* Custom Summary Templates: Tailor summaries to your specific workflow and needs
* Advanced Export Options: PDF, DOCX, and Markdown exports with formatting
* Auto-detect and Join Meetings: Automatic meeting detection and joining
* Speaker Identification: Distinguish between speakers automatically(Coming Soon)
* Chat with Meetings: AI-powered meeting insights and queries(Coming Soon)
* Calendar Integration: Seamless integration with your calendar(Coming Soon)
* Self-Hosted Deployment: Deploy on your own infrastructure for teams
* GDPR Compliance Built-In: Privacy by design architecture with complete audit trails
* Priority Support: Dedicated support for PRO users

### Who is PRO for?

* Professionalswho need the highest accuracy for critical meetings
* Teams and organizations(2-100 users) requiring self-hosted deployment
* Power userswho need advanced export formats and custom workflows
* Compliance-focused organizationsrequiring GDPR readiness

Note:Meetily Community Edition remainsfree & open source foreverwith local transcription, AI summaries, and core features. PRO is a separate professional solution for users who need enhanced accuracy and advanced capabilities.

For organizations needing 100+ users or managed compliance solutions, exploreMeetily Enterprise.

Learn more about pricing and features:https://meetily.ai/pro/

## Contributing

We welcome contributions from the community! If you have any questions or suggestions, please open an issue or submit a pull request. Please follow the established project structure and guidelines. For more details, refer to theCONTRIBUTING.mdfile.

Thanks for all the contributions. Our community is what makes this project possible.

## License

MIT License - Feel free to use this project for your own purposes.

## Acknowledgments

* We borrowed some code fromWhisper.cpp.
* We borrowed some code fromScreenpipe.
* We borrowed some code fromtranscribe-rs.
* Thanks toNVIDIAfor developing theParakeetmodel.
* Thanks toistupakovfor providing theONNX conversionof the Parakeet model.

## Star History

## About

Privacy first, AI meeting assistant with 4x faster Parakeet/Whisper live transcription, speaker diarization, and Ollama summarization built on Rust. 100% local processing. no cloud required. Meetily (Meetly Ai -https://meetily.ai) is the #1 Self-hosted, Open-source Ai meeting note taker for macOS & Windows.

meetily.ai

### Topics

 windows

 rust

 mac

 ai

 offline-first

 self-hosted

 speech-to-text

 transcription

 whisper

 meeting-minutes

 meeting-notes

 privacy-tools

 parakeet

 privacy-focused

 llm

 whisper-cpp

 local-ai

 ollama

 ai-meeting-assistant

 sortformer

### Resources

 Readme

 

### License

 MIT license
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

14.4k

 stars
 

### Watchers

71

 watching
 

### Forks

1.6k

 forks
 

 Report repository

 

## Releases11

Meetily v0.4.0

 Latest

 

Jun 5, 2026

 

+ 10 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Rust46.2%
* TypeScript29.7%
* C++9.9%
* PowerShell4.3%
* Shell4.1%
* Python3.1%
* Other2.7%