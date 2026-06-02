---
title: 'GitHub - Open-LLM-VTuber/Open-LLM-VTuber: Talk to any LLM with hands-free voice interaction, voice interruption, and Live2D taking face running locally across platforms · GitHub'
url: https://github.com/Open-LLM-VTuber/Open-LLM-VTuber
site_name: github
content_file: github-github-open-llm-vtuberopen-llm-vtuber-talk-to-any
fetched_at: '2026-06-03T01:51:20.409727'
original_url: https://github.com/Open-LLM-VTuber/Open-LLM-VTuber
author: Open-LLM-VTuber
description: Talk to any LLM with hands-free voice interaction, voice interruption, and Live2D taking face running locally across platforms - Open-LLM-VTuber/Open-LLM-VTuber
---

Open-LLM-VTuber

 

/

Open-LLM-VTuber

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork1.1k
* Star8.2k

 
 
 
 
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

913 Commits
913 Commits
.cursor/
rules
.cursor/
rules
 
 
.gemini
.gemini
 
 
.github
.github
 
 
assets
assets
 
 
avatars
avatars
 
 
backgrounds
backgrounds
 
 
characters
characters
 
 
config_templates
config_templates
 
 
doc
doc
 
 
frontend @ 06a659b
frontend @ 06a659b
 
 
live2d-models
live2d-models
 
 
prompts
prompts
 
 
scripts
scripts
 
 
src/
open_llm_vtuber
src/
open_llm_vtuber
 
 
upgrade_codes
upgrade_codes
 
 
web_tool
web_tool
 
 
.dockerignore
.dockerignore
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
.python-version
.python-version
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
LICENSE-Live2D.md
LICENSE-Live2D.md
 
 
README.CN.md
README.CN.md
 
 
README.JP.md
README.JP.md
 
 
README.KR.md
README.KR.md
 
 
README.md
README.md
 
 
dockerfile
dockerfile
 
 
mcp_servers.json
mcp_servers.json
 
 
model_dict.json
model_dict.json
 
 
pixi.lock
pixi.lock
 
 
pyproject.toml
pyproject.toml
 
 
requirements-bilibili.txt
requirements-bilibili.txt
 
 
requirements.txt
requirements.txt
 
 
run_server.py
run_server.py
 
 
upgrade.py
upgrade.py
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

# Open-LLM-VTuber

### 📢 v2.0 Development: We are focusing on Open-LLM-VTuber v2.0 — a complete rewrite of the codebase. v2.0 is currently in its early discussion and planning phase. We kindly ask you to refrain from opening new issues or pull requests for feature requests on v1. To participate in the v2 discussions or contribute, join our developer community onZulip. Weekly meeting schedules will be announced on Zulip. We will continue fixing bugs for v1 and work through existing pull requests.ENGLISH README |中文 README|한국어 README|日本語 READMEDocumentation|

常见问题 Common Issues doc (Written in Chinese):https://docs.qq.com/pdf/DTFZGQXdTUXhIYWRq

User Survey:https://forms.gle/w6Y6PiHTZr1nzbtWA

调查问卷(中文):https://wj.qq.com/s2/16150415/f50a/

⚠️This project is in its early stages and is currently underactive development.

⚠️If you want to run the server remotely and access it on a different machine, such as running the server on your computer and access it on your phone, you will need to configurehttps, because the microphone on the front end will only launch in a secure context (a.k.a. https or localhost). SeeMDN Web Doc. Therefore, you should configure https with a reverse proxy to access the page on a remote machine (non-localhost).

## ⭐️ What is this project?

Open-LLM-VTuberis a uniquevoice-interactive AI companionthat not only supportsreal-time voice conversationsandvisual perceptionbut also features a livelyLive2D avatar. All functionalities can run completely offline on your computer!

You can treat it as your personal AI companion — whether you want avirtual girlfriend,boyfriend,cute pet, or any other character, it can meet your expectations. The project fully supportsWindows,macOS, andLinux, and offers two usage modes: web version and desktop client (with special support fortransparent background desktop pet mode, allowing the AI companion to accompany you anywhere on your screen).

Although the long-term memory feature is temporarily removed (coming back soon), thanks to the persistent storage of chat logs, you can always continue your previous unfinished conversations without losing any precious interactive moments.

In terms of backend support, we have integrated a rich variety of LLM inference, text-to-speech, and speech recognition solutions. If you want to customize your AI companion, you can refer to theCharacter Customization Guideto customize your AI companion's appearance and persona.

The reason it's calledOpen-LLM-Vtuberinstead ofOpen-LLM-CompanionorOpen-LLM-Waifuis because the project's initial development goal was to use open-source solutions that can run offline on platforms other than Windows to recreate the closed-source AI Vtuberneuro-sama.

### 👀 Demo

## ✨ Features & Highlights

* 🖥️Cross-platform support: Perfect compatibility with macOS, Linux, and Windows. We support NVIDIA and non-NVIDIA GPUs, with options to run on CPU or use cloud APIs for resource-intensive tasks. Some components support GPU acceleration on macOS.
* 🔒Offline mode support: Run completely offline using local models - no internet required. Your conversations stay on your device, ensuring privacy and security.
* 💻Attractive and powerful web and desktop clients: Offers both web version and desktop client usage modes, supporting rich interactive features and personalization settings. The desktop client can switch freely between window mode and desktop pet mode, allowing the AI companion to be by your side at all times.
* 🎯Advanced interaction features:👁️ Visual perception, supporting camera, screen recording and screenshots, allowing your AI companion to see you and your screen🎤 Voice interruption without headphones (AI won't hear its own voice)🫱 Touch feedback, interact with your AI companion through clicks or drags😊 Live2D expressions, set emotion mapping to control model expressions from the backend🐱 Pet mode, supporting transparent background, global top-most, and mouse click-through - drag your AI companion anywhere on the screen💭 Display AI's inner thoughts, allowing you to see AI's expressions, thoughts and actions without them being spoken🗣️ AI proactive speaking feature💾 Chat log persistence, switch to previous conversations anytime🌍 TTS translation support (e.g., chat in Chinese while AI uses Japanese voice)
* 👁️ Visual perception, supporting camera, screen recording and screenshots, allowing your AI companion to see you and your screen
* 🎤 Voice interruption without headphones (AI won't hear its own voice)
* 🫱 Touch feedback, interact with your AI companion through clicks or drags
* 😊 Live2D expressions, set emotion mapping to control model expressions from the backend
* 🐱 Pet mode, supporting transparent background, global top-most, and mouse click-through - drag your AI companion anywhere on the screen
* 💭 Display AI's inner thoughts, allowing you to see AI's expressions, thoughts and actions without them being spoken
* 🗣️ AI proactive speaking feature
* 💾 Chat log persistence, switch to previous conversations anytime
* 🌍 TTS translation support (e.g., chat in Chinese while AI uses Japanese voice)
* 🧠Extensive model support:🤖 Large Language Models (LLM): Ollama, OpenAI (and any OpenAI-compatible API), Gemini, Claude, Mistral, DeepSeek, Zhipu AI, GGUF, LM Studio, vLLM, etc.🎙️ Automatic Speech Recognition (ASR): sherpa-onnx, FunASR, Faster-Whisper, Whisper.cpp, Whisper, Groq Whisper, Azure ASR, etc.🔊 Text-to-Speech (TTS): sherpa-onnx, pyttsx3, MeloTTS, Coqui-TTS, GPTSoVITS, Bark, CosyVoice, Edge TTS, Fish Audio, Azure TTS, etc.
* 🤖 Large Language Models (LLM): Ollama, OpenAI (and any OpenAI-compatible API), Gemini, Claude, Mistral, DeepSeek, Zhipu AI, GGUF, LM Studio, vLLM, etc.
* 🎙️ Automatic Speech Recognition (ASR): sherpa-onnx, FunASR, Faster-Whisper, Whisper.cpp, Whisper, Groq Whisper, Azure ASR, etc.
* 🔊 Text-to-Speech (TTS): sherpa-onnx, pyttsx3, MeloTTS, Coqui-TTS, GPTSoVITS, Bark, CosyVoice, Edge TTS, Fish Audio, Azure TTS, etc.
* 🔧Highly customizable:⚙️Simple module configuration: Switch various functional modules through simple configuration file modifications, without delving into the code🎨Character customization: Import custom Live2D models to give your AI companion a unique appearance. Shape your AI companion's persona by modifying the Prompt. Perform voice cloning to give your AI companion the voice you desire🧩Flexible Agent implementation: Inherit and implement the Agent interface to integrate any Agent architecture, such as HumeAI EVI, OpenAI Her, Mem0, etc.🔌Good extensibility: Modular design allows you to easily add your own LLM, ASR, TTS, and other module implementations, extending new features at any time
* ⚙️Simple module configuration: Switch various functional modules through simple configuration file modifications, without delving into the code
* 🎨Character customization: Import custom Live2D models to give your AI companion a unique appearance. Shape your AI companion's persona by modifying the Prompt. Perform voice cloning to give your AI companion the voice you desire
* 🧩Flexible Agent implementation: Inherit and implement the Agent interface to integrate any Agent architecture, such as HumeAI EVI, OpenAI Her, Mem0, etc.
* 🔌Good extensibility: Modular design allows you to easily add your own LLM, ASR, TTS, and other module implementations, extending new features at any time

## 👥 User Reviews

Thanks to the developer for open-sourcing and sharing the girlfriend for everyone to use

This girlfriend has been used over 100,000 times

## 🚀 Quick Start

Please refer to theQuick Startsection in our documentation for installation.

## ☝ Update

⚠️v1.0.0has breaking changes and requires re-deployment. Youmaystill update via the method below, but theconf.yamlfile is incompatible and most of the dependencies needs to be reinstalled withuv. For those who came from versions beforev1.0.0, I recommend deploy this project again with thelatest deployment guide.

Please useuv run update.pyto update if you installed any versions later thanv1.0.0.

## 😢 Uninstall

Most files, including Python dependencies and models, are stored in the project folder.

However, models downloaded via ModelScope or Hugging Face may also be inMODELSCOPE_CACHEorHF_HOME. While we aim to keep them in the project'smodelsdirectory, it's good to double-check.

Review the installation guide for any extra tools you no longer need, such asuv,ffmpeg, ordeeplx.

## 🤗 Want to contribute?

Checkout thedevelopment guide.

# 🎉🎉🎉 Related Projects

ylxmf2005/LLM-Live2D-Desktop-Assitant

* Your Live2D desktop assistant powered by LLM! Available for both Windows and MacOS, it senses your screen, retrieves clipboard content, and responds to voice commands with a unique voice. Featuring voice wake-up, singing capabilities, and full computer control for seamless interaction with your favorite character.

## 📜 Third-Party Licenses

### Live2D Sample Models Notice

This project includes Live2D sample models provided by Live2D Inc. These assets are licensed separately under the Live2D Free Material License Agreement and the Terms of Use for Live2D Cubism Sample Data. They are not covered by the MIT license of this project.

This content uses sample data owned and copyrighted by Live2D Inc. The sample data are utilized in accordance with the terms and conditions set by Live2D Inc. (SeeLive2D Free Material License AgreementandTerms of Use).

Note: For commercial use, especially by medium or large-scale enterprises, the use of these Live2D sample models may be subject to additional licensing requirements. If you plan to use this project commercially, please ensure that you have the appropriate permissions from Live2D Inc., or use versions of the project without these models.

## Contributors

Thanks our contributors and maintainers for making this project possible.

## Star History

## About

Talk to any LLM with hands-free voice interaction, voice interruption, and Live2D taking face running locally across platforms

open-llm-vtuber.github.io/

### Topics

 ai

 chatbots

 live2d

 live2d-web

 llm

 ai-vtuber

 ai-waifu

 ollama

 neuro-sama

 ai-companion

### Resources

 Readme

 

### License

 View license
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

8.2k

 stars
 

### Watchers

78

 watching
 

### Forks

1.1k

 forks
 

 Report repository

 

## Releases19

v1.2.1 Release

 Latest

 

Aug 26, 2025

 

+ 18 releases

## Sponsor this project

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 
* buymeacoffee.com/yi.ting

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python96.6%
* JavaScript2.8%
* HTML0.6%