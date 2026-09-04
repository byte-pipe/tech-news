---
title: 'GitHub - OpenWhispr/openwhispr: Voice-to-text dictation app with local (Nvidia Parakeet/Whisper) and cloud models (BYOK). Privacy-first and available cross-platform. · GitHub'
url: https://github.com/OpenWhispr/openwhispr
site_name: github
content_file: github-github-openwhispropenwhispr-voice-to-text-dictatio
fetched_at: '2026-09-04T14:47:50.942727'
original_url: https://github.com/OpenWhispr/openwhispr
author: OpenWhispr
description: Voice-to-text dictation app with local (Nvidia Parakeet/Whisper) and cloud models (BYOK). Privacy-first and available cross-platform. - OpenWhispr/openwhispr
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 OpenWhispr

 

/

openwhispr

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork896
* Star6.6k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

2,137 Commits
2,137 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
.superpowers/
sdd
.superpowers/
sdd
 
 
agent-skills
agent-skills
 
 
docs
docs
 
 
examples
examples
 
 
native/
meeting-aec-helper
native/
meeting-aec-helper
 
 
nix
nix
 
 
resources
resources
 
 
scripts
scripts
 
 
src
src
 
 
test
test
 
 
.env.example
.env.example
 
 
.gitignore
.gitignore
 
 
.npmrc
.npmrc
 
 
.nvmrc
.nvmrc
 
 
.prettierignore
.prettierignore
 
 
.prettierrc
.prettierrc
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
DEBUG.md
DEBUG.md
 
 
LICENSE
LICENSE
 
 
LOCAL_WHISPER_SETUP.md
LOCAL_WHISPER_SETUP.md
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
TROUBLESHOOTING.md
TROUBLESHOOTING.md
 
 
cleanup.js
cleanup.js
 
 
electron-builder.json
electron-builder.json
 
 
electron-builder.unsigned-win.json
electron-builder.unsigned-win.json
 
 
eslint.config.js
eslint.config.js
 
 
flake.lock
flake.lock
 
 
flake.nix
flake.nix
 
 
main.js
main.js
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
preload.js
preload.js
 
 
View all files

## Repository files navigation

# OpenWhispr

The open-source and free alternative to WisprFlow and Granola.Privacy-first voice-to-text dictation with AI agents, meeting transcription, and notes. Cross-platform for macOS, Windows, and Linux.

Website·Docs·Download·API·Changelog

OpenWhispr turns your voice into text, notes, and actions from your desktop. Press a hotkey, speak, and your words appear at your cursor. Choose between fully private offline transcription with local speech-to-text engines like Whisper and NVIDIA Parakeet — where your audio never leaves your device — or cloud processing for speed. No data collection, no telemetry, fully open source.

## Download

Platform

Download

macOS (Apple Silicon)

.dmg

macOS (Intel) *

.dmg

Windows

.exe

Linux

.AppImage
 / 
.deb
 / 
.rpm
 / 
.tar.gz

* On Intel Macs, live speaker identification and voice fingerprinting are unavailable: they depend on ONNX Runtime, whichstopped shipping macOS x86_64 binaries in 1.24. Meetings still record and transcribe normally, and notes search falls back to keyword matching instead of semantic search.

## Features

* Voice dictation— global hotkey to dictate into any app with automatic pasting
* Dictation translation— dedicated hotkey to dictate in one language and paste the text in another
* AI agent— talk to GPT-5, Claude, Gemini, Groq, Tinfoil, OpenRouter, or local models with a named voice assistant
* Voice Assistant hotkey— dedicated hotkey that sends what you say straight to your AI assistant as a command, no wake word needed and no cleanup pass; highlighted text is edited in place. With auto-paste enabled, answers paste at a focused text cursor or stream into a floating panel and copy to the clipboard when no writable cursor is available. You can also opt in to sending a screenshot of your current screen as context
* Meeting transcription— auto-detect Zoom, Teams, and FaceTime calls with live speaker diarization, voice fingerprinting, and Google, Microsoft, or Apple Calendar integration
* Local speaker diarization— on-device speaker labelling with voice fingerprint recognition across meetings, no cloud required
* Notes— create, organize, and search notes with folders, semantic search, cloud sync, and AI actions
* Team spaces & sharing— free for signed-in users; share notes on the web with link, domain, or invite-only visibility, and collaborate in team spaces with roles, invitations, and server-enforced membership
* Audio import— transcribe existing audio and video: drag in files, batch-upload, or paste a YouTube/audio URL, with optional speaker detection
* Local or cloud — your choice— all core features (transcription, AI reasoning, speaker diarization, semantic search) work with local models or cloud providers — including GPU-accelerated local Whisper on Metal, CUDA, and Vulkan (AMD/Intel)
* Enterprise controls— enforce organization policy, company SSO and SCIM, and centrally managed Amazon Bedrock or Azure OpenAI access without distributing cloud keys
* Public API & MCP— manage notes and transcriptions programmatically or connect your AI assistant via theMCP server

## Quick start

git clone https://github.com/OpenWhispr/openwhispr.git

cd
 openwhispr
npm install
npm run dev

Requires Node.js 24+. See thefull documentationfor setup guides, platform-specific instructions, and build details.

## Documentation

Visitdocs.openwhispr.comfor:

* Getting started
* Platform guides(macOS, Windows, Linux)
* API reference
* MCP server setup
* Troubleshooting

Repo examples:

* Custom ASR shimfor Self-Hosted transcription against non-OpenAI-compatible ASR APIs

## Tech stack

React 19, TypeScript, Tailwind CSS v4, Electron 41, better-sqlite3, whisper.cpp, sherpa-onnx, shadcn/ui

## Star History

## Sponsors

Neonis the serverless Postgres platform powering OpenWhispr Cloud.

## Contributing

We welcome contributions. Fork the repo, create a feature branch, and open a pull request. See thecontributing guidefor development setup and guidelines.

## License

MIT— free for personal and commercial use.

## Acknowledgments

* OpenAI Whisper— speech recognition model powering local and cloud transcription
* whisper.cpp— high-performance C++ implementation for local processing
* NVIDIA Parakeet— fast multilingual ASR model
* sherpa-onnx— cross-platform ONNX runtime for Parakeet inference
* Hugging Face— model hub hosting Whisper, Parakeet, and embedding model weights
* llama.cpp— local LLM inference for AI text processing
* Electron— cross-platform desktop framework
* React— UI component library
* shadcn/ui— accessible components built on Radix primitives
* Neon— serverless Postgres powering OpenWhispr Cloud