---
title: 'GitHub - Anil-matcha/Open-Generative-AI: Uncensored, open-source alternative to Higgsfield AI, Freepik AI, Krea AI, Openart AI — Free, unrestricted AI image & video generation studio with 200+ models (Flux, Midjourney, Kling, Sora, Veo). No content filters. Self-hosted, MIT licensed. · GitHub'
url: https://github.com/Anil-matcha/Open-Generative-AI
site_name: github
content_file: github-github-anil-matchaopen-generative-ai-uncensored-op
fetched_at: '2026-04-24T19:51:15.943409'
original_url: https://github.com/Anil-matcha/Open-Generative-AI
author: Anil-matcha
description: Uncensored, open-source alternative to Higgsfield AI, Freepik AI, Krea AI, Openart AI — Free, unrestricted AI image & video generation studio with 200+ models (Flux, Midjourney, Kling, Sora, Veo). No content filters. Self-hosted, MIT licensed. - Anil-matcha/Open-Generative-AI
---

Anil-matcha

 

/

Open-Generative-AI

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.4k
* Star7.6k

 
 
 
 
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

115 Commits
115 Commits
app
app
 
 
build
build
 
 
components
components
 
 
docs/
assets
docs/
assets
 
 
electron
electron
 
 
packages
packages
 
 
public
public
 
 
scripts
scripts
 
 
src
src
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
README.md
README.md
 
 
afterPack.js
afterPack.js
 
 
index.html
index.html
 
 
jsconfig.json
jsconfig.json
 
 
middleware.js
middleware.js
 
 
models_dump.json
models_dump.json
 
 
next.config.mjs
next.config.mjs
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
postcss.config.js
postcss.config.js
 
 
project_knowledge.md
project_knowledge.md
 
 
tailwind.config.js
tailwind.config.js
 
 
vite.config.mjs
vite.config.mjs
 
 
View all files

## Repository files navigation

# Open Generative AI — Uncensored Open-Source Alternative to Higgsfield AI, Freepik AI, Krea AI, Openart AI

The free, open-source, unrestricted alternative to Higgsfield AI, Freepik, Krea, Openart AI.Generate AI images and videos using 200+ state-of-the-art models — no content filters, no closed ecosystem, no subscription fees.

🐎Early access to Happy Horse 1.0— Alibaba's #1 ranked AI video model. Check outAwesome HappyHorse 1.0 API & Prompts— a Python wrapper plus a curated library of high-performing community prompts for native 1080p text-to-video and image-to-video generation with jointly generated audio.

💡Looking for GPT-Image-2 prompts?Check outAwesome GPT-Image-2 API Prompts— a curated collection of 40+ ready-to-use prompts for the OpenAIgpt-image-2API covering portraits, posters, UI mockups, game screenshots, and more.

🤖Automate Higgsfield, Freepik, Krea, Openart & more with AI coding agents:Generative-Media-Skills— a library of skills that let agents likeClaude Code,Codex, and other coding assistants drive 200+ image/video models end-to-end (prompt → generate → edit → stitch) directly from your terminal. Perfect for building automated media pipelines without touching a UI.

### Related projects

Open-source Weavy, Flora Fauna Freepik Spaces, Krea nodes alternative->https://github.com/SamurAIGPT/Vibe-Workflow

Open-source multi-modal chatbot and Poe alternative->https://github.com/Anil-matcha/Open-Poe-AI

## 🌐 Try it Online — No Install Required

Hosted version:https://dev.muapi.ai/open-generative-ai

Use all four studios (Image, Video, Lip Sync, Cinema) directly in your browser — no Node.js, no setup. Sign up for a free account to start generating. The hosted version is always up to date with the latest models.

Community:JoinDiscordfor discussions and support

Followthecreatorfor updates

Happy Horse top video model coming soon:FollowHappy Horse AIfor updates

## ⬇️ Download Desktop App

One-click installers — no Node.js or terminal required.

Platform

Download

macOS Apple Silicon (M1/M2/M3/M4)

Open Generative AI-1.0.2-arm64.dmg

macOS Intel (x64)

Open Generative AI-1.0.2.dmg

Windows (x64 + ARM64)

Open Generative AI Setup 1.0.2.exe

Linux (Ubuntu x64)

Build locally with 
npm run electron:build:linux

All releases:github.com/Anil-matcha/Open-Generative-AI/releases

### macOS Installation Guide

Because the app is not notarized by Apple, macOS Gatekeeper will block it on first launch. Follow these steps:

Step 1— Mount the DMG and drag the app to/Applications

Step 2— Open Terminal and run:

xattr -cr 
"
/Applications/Open Generative AI.app
"

Step 3— Right-click the app in/Applications→ clickOpen→ clickOpenagain on the dialog

You only need to do this once. After that, the app opens normally.

Alternative (no Terminal):

1. Try to open the app — macOS will block it
2. Go toSystem Settings → Privacy & Security
3. Scroll down to find"Open Generative AI was blocked"
4. ClickOpen Anyway→Open

### Windows Installation — SmartScreen warning fix

Windows SmartScreen may show a warning because the installer is not code-signed:

1. ClickMore infoon the SmartScreen dialog
2. ClickRun anyway

The app will install silently to%LocalAppData%with a Start Menu shortcut.

### Ubuntu / Linux Installation

Linux artifacts are available when building with Electron Builder:

#
 Build Linux installers (AppImage + .deb)

npm run electron:build:linux

Generated files are written to therelease/folder:

* AppImage— portable, run directly after making executable:chmod +x"release/Open Generative AI-*.AppImage"./release/Open\Generative\AI-*.AppImage
* .deb— install on Debian/Ubuntu:sudo apt install ./release/open-generative-ai_*_amd64.deb

If AppImage fails to start on older systems, installlibfuse2:

sudo apt install libfuse2

#### Ubuntu 24.04+ / AppArmor sandbox restriction

Ubuntu 24.04 and later enable a kernel security policy (apparmor_restrict_unprivileged_userns) that blocks Chromium's user-namespace sandbox. If the app fails to start silently or crashes immediately, you have two options:

Option A — Recommended: install the.debinstead.The.debpackage ships an AppArmor profile that grants the required permission automatically on install with no system-wide changes.

Option B — Temporary system fix (AppImage users):

sudo sysctl -w kernel.apparmor_restrict_unprivileged_userns=0

This lasts until next reboot. To make it permanent:

echo
 
'
kernel.apparmor_restrict_unprivileged_userns=0
'
 
|
 sudo tee /etc/sysctl.d/99-userns.conf

Open Generative AI is a free, uncensored, open-source AI image, video, cinema, and lip sync studio that brings unrestricted creative workflows to everyone. No content filters, no prompt rejections, no guardrails — just full creative freedom. Powered byMuapi.ai, it supports text-to-image, image-to-image, text-to-video, image-to-video, and audio-driven lip sync generation across models like Flux, Nano Banana, Midjourney, Kling, Sora, Veo, Seedream, Infinite Talk, LTX Lipsync, Wan 2.2, and more — all from a sleek, modern interface you can self-host and customize.

Why Open Generative AI instead of Higgsfield AI, Freepik, Krea AI, Openart AI?

* Uncensored & unrestricted— no content filters, no nanny guardrails, no prompt rejections
* Free & open-source— no subscription, no vendor lock-in
* Self-hosted— your data stays on your machine, full creative control
* 200+ models— text-to-image, image-to-image, text-to-video, image-to-video, lip sync
* Multi-image input— feed up to 14 reference images into compatible models
* Lip Sync Studio— animate portraits or sync lips to any audio with 9 dedicated models
* Extensible— add your own models, modify the UI, build on top of it

For a deep dive into the technical architecture and the philosophy behind the "Infinite Budget" cinema workflow, see ourcomprehensive guide and roadmap.

## ⚡ Local Model Inference (Desktop App Only)

The desktop app includes a built-inlocal generation enginepowered bystable-diffusion.cpp— generate images entirely on your own machine with no API key and no internet connection required.

### Supported Local Models

Model

Type

Size

Speed

Z-Image Turbo
 ⚡

Diffusion Transformer

2.5 GB + 2.7 GB aux

8-step turbo

Z-Image Base
 ⚡

Diffusion Transformer

3.5 GB + 2.7 GB aux

50-step high-quality

Dreamshaper 8

SD 1.5

2.1 GB

20-step versatile

Realistic Vision v5.1

SD 1.5

2.1 GB

25-step photorealistic

Anything v5

SD 1.5

2.1 GB

20-step anime/illustration

SDXL Base 1.0

SDXL

6.9 GB

30-step high-res

Z-Image modelsrequire two shared auxiliary files (downloaded once, shared across both models):

* Qwen3-4B Text Encoder— 2.4 GB
* FLUX VAE— 335 MB

### How to Use Local Models

1. OpenSettings → Local Modelsin the desktop app
2. Install thesd.cpp inference engine(one click — auto-downloaded)
3. Download your chosen model (and auxiliary files for Z-Image)
4. InImage Studio, click the⚡ Localtoggle next to the model selector
5. Select your local model and generate — no API key needed

All downloads happen inside the app. Nothing is installed system-wide.

Local inference is only available in the desktop app.The hosted web version always uses cloud APIs.

### Hardware Notes

* Runs on CPU (all platforms) andMetal GPU(macOS Apple Silicon — M1/M2/M3/M4)
* Metal GPU acceleration is built into the macOS desktop binary — significantly faster than CPU-only
* Recommended: 16 GB RAM for Z-Image models (7.4 GB weights + 2.4 GB compute buffer)
* The system may slow during generation — the process uses all available CPU cores while running

## ✨ Features

* Image Studio— Generate images from text prompts (50+ text-to-image models) or transform existing images (55+ image-to-image models). Switches model set automatically based on whether a reference image is provided. Quality and resolution controls visible for models that support them.
* Local Inference— Generate images on-device with no API key using Z-Image Turbo/Base, Dreamshaper, Realistic Vision, Anything v5, or SDXL — powered by stable-diffusion.cpp with Metal GPU acceleration on Apple Silicon.
* Multi-Image Input— Upload up to 14 reference images for compatible edit models (Nano Banana 2 Edit, Flux Kontext Dev, GPT-4o Edit, and more). Multi-select picker with order badges, batch upload, and a "Use Selected" confirmation flow.
* Video Studio— Generate videos from text prompts (40+ text-to-video models) or animate a start-frame image (60+ image-to-video models). Same intelligent mode switching as Image Studio.
* Lip Sync Studio— Animate portrait images or sync lips on existing videos using audio. 9 dedicated models across two modes: portrait image + audio → talking video, and video + audio → lipsync video.
* Cinema Studio— Interface for photorealistic cinematic shots with pro camera controls (Lens, Focal Length, Aperture)
* Workflow Studio— Build and run multi-step AI pipelines visually. Chain image, video, and audio models into automated flows. Browse community templates, create your own with a node-based editor, and run them via an interactive playground.
* Upload History— Reference images are uploaded once and stored locally. A picker panel lets you reuse any previously uploaded image across sessions — no re-uploading.
* Smart Controls— Dynamic aspect ratio, resolution/quality, and duration pickers that adapt to each model's capabilities (including t2i models with resolution or quality options)
* Generation History— Browse, revisit, and download all past generations (persisted in browser storage)
* Image & Video Download— One-click download of generated outputs in full resolution
* API Key Management— Secure API key storage in browser localStorage (never sent to any server except Muapi)
* Responsive Design— Works seamlessly on desktop and mobile with dark glassmorphism UI

### 🖼️ Image Studio — Dual Mode

The Image Studio automatically switches between two model sets:

Mode

Trigger

Models

Prompt

Text-to-Image

Default (no image)

50+ t2i models (Flux, Nano Banana 2, Seedream 5.0, Ideogram, GPT-4o, Midjourney…)

Required

Image-to-Image

Reference image uploaded

55+ i2i models (Kontext, Nano Banana 2 Edit, Seedream 5.0 Edit, Seededit, Upscaler…)

Optional

#### Newly Added Models

Model

Type

Key Features

Nano Banana 2

Text-to-Image

Google Gemini 3.1 Flash Image · Resolution 1K/2K/4K · Google Search enhancement · aspect ratio 
auto

Nano Banana 2 Edit

Image-to-Image

Up to 
14 reference images
 · Resolution 1K/2K/4K · Google Search enhancement

Seedream 5.0

Text-to-Image

ByteDance · Quality basic/high · 8 aspect ratios · up to 4K

Seedream 5.0 Edit

Image-to-Image

ByteDance · Natural language style transfer · Quality basic/high

MiniMax Image 01

Text-to-Image

MiniMax · 8 aspect ratios · up to 4 images per request · 1500 char prompt

#### Multi-Image Input

Models that accept multiple reference images expose a multi-select picker when active:

Model

Max Images

Nano Banana 2 Edit

14

Nano Banana Edit

10

Flux Kontext Dev I2I

10

Kling O1 Edit Image

10

GPT-4o Edit / GPT Image 1.5 Edit

10

Bytedance Seedream Edit v4 / v4.5

10

Vidu Q2 Reference to Image

7

Flux 2 Flex/Pro Edit

8

Nano Banana Pro Edit

8

Flux Kontext Pro/Max I2I

2

Wan 2.5/2.6 Image Edit

2–3

Qwen Image Edit Plus / 2511

3

GPT-4o Image to Image

5

Flux 2 Klein 4b/9b Edit

4

When a multi-image model is selected the upload trigger switches to multi-select mode:

* Checkboxes with order numbers— images are sent to the model in the order you select them
* Batch upload— pick multiple files at once from your file dialog
* Count badgeon the trigger shows how many images are active; a+badge appears when more slots are available
* "Use Selected" buttonconfirms and closes the picker

### 🎬 Video Studio — Dual Mode

The Video Studio follows the same pattern:

Mode

Trigger

Models

Prompt

Text-to-Video

Default (no image)

40+ t2v models (Kling, Sora, Veo, Wan, Seedance 2.0, Hailuo, Runway…)

Required

Image-to-Video

Start frame uploaded

60+ i2v models (Kling I2V, Veo3 I2V, Runway I2V, Wan I2V, Seedance 2.0 I2V, Midjourney I2V…)

Optional

#### Newly Added Models

Model

Type

Key Features

Seedance 2.0

Text-to-Video

ByteDance · Aspect ratios 16:9 / 9:16 / 4:3 / 3:4 · Duration 5 / 10 / 15s · Quality basic/high

Seedance 2.0 I2V

Image-to-Video

ByteDance · Animate images into video · Up to 9 reference images · Aspect ratios 16:9 / 9:16 / 4:3 / 3:4 · Duration 5 / 10 / 15s · Quality basic/high

Seedance 2.0 Extend

Video Extension

ByteDance · Seamlessly continue any Seedance 2.0 generation · Preserves style, motion & audio · Optional continuation prompt · Duration 5 / 10 / 15s · Quality basic/high

Grok Imagine T2V

Text-to-Video

xAI · Duration 6 / 10 / 
15s
 · Modes: fun / normal / spicy · Aspect ratios 9:16 / 16:9 / 2:3 / 3:2 / 1:1

Grok Imagine I2V

Image-to-Video

xAI · Duration 6 / 10 / 
15s
 · Modes: fun / normal / spicy · Cinematic motion from still images

MiniMax Hailuo 02 / 2.3 Standard & Pro

Text-to-Video / Image-to-Video

MiniMax · Full HD video · Multiple aspect ratios · Fast variant included

### 🎙️ Lip Sync Studio

TheLip Sync Studiogenerates audio-driven talking videos using 9 models across two input modes:

Mode

Trigger

Description

Portrait Image

Default

Upload a portrait image + audio file → animated talking video

Video

Switch to Video mode

Upload an existing video + audio file → lipsync video

#### Image-based Models (Portrait Image + Audio → Video)

Model

Endpoint

Resolutions

Prompt

Infinite Talk

infinitetalk-image-to-video

480p, 720p

Optional

Wan 2.2 Speech to Video

wan2.2-speech-to-video

480p, 720p

Optional

LTX 2.3 Lipsync

ltx-2.3-lipsync

480p, 720p, 1080p

Optional

LTX 2 19B Lipsync

ltx-2-19b-lipsync

480p, 720p, 1080p

Optional

#### Video-based Models (Video + Audio → Lipsync Video)

Model

Endpoint

Resolutions

Prompt

Sync Lipsync

sync-lipsync

—

—

LatentSync

latentsync-video

—

—

Creatify Lipsync

creatify-lipsync

—

—

Veed Lipsync

veed-lipsync

—

—

Infinite Talk V2V

infinitetalk-video-to-video

480p, 720p

Optional

How it works:

1. SelectPortrait ImageorVideomode using the toggle
2. Upload your portrait image (or video) using the image/video upload button
3. Upload your audio file using the audio upload button
4. Optionally enter a prompt to guide the motion style
5. Select a model and resolution (where supported), then clickGenerate

Generation history is saved separately inlipsync_historyand pending jobs resume automatically on page reload.

### 🔀 Workflow Studio

TheWorkflow Studiolets you build and run multi-step AI pipelines without writing code.

Key capabilities:

* Templates— Start from pre-built workflows (image chains, video pipelines, and more)
* My Workflows— Save and manage your own custom pipelines
* Community— Browse and run workflows published by other users
* Node-based Builder— Drag-and-drop visual editor to connect models and route outputs between steps
* Playground— Run any workflow interactively with a form UI; results render inline
* API execution— Every workflow is also callable via the Muapi API

💡Want to add workflows to your own app?Check outVibe Workflow— the open-source workflow engine powering this feature. Drop it into any project.

### 🎥 Cinema Studio Controls

TheCinema Studiooffers precise control over the virtual camera, translating your choices into optimized prompt modifiers:

Category

Available Options

Cameras

Modular 8K Digital, Full-Frame Cine Digital, Grand Format 70mm Film, Studio Digital S35, Classic 16mm Film, Premium Large Format Digital

Lenses

Creative Tilt, Compact Anamorphic, Extreme Macro, 70s Cinema Prime, Classic Anamorphic, Premium Modern Prime, Warm Cinema Prime, Swirl Bokeh Portrait, Vintage Prime, Halation Diffusion, Clinical Sharp Prime

Focal Lengths

8mm (Ultra-Wide), 14mm, 24mm, 35mm (Human Eye), 50mm (Portrait), 85mm (Tight Portrait)

Apertures

f/1.4 (Shallow DoF), f/4 (Balanced), f/11 (Deep Focus)

### 📁 Upload History & Picker

Every image you upload is saved locally (URL + thumbnail) so you never upload the same file twice:

* Click the upload button to open thereference image picker
* Previously uploaded images appear in a 3-column grid with thumbnails
* Single-image models— click a thumbnail to instantly select and close
* Multi-image models— toggle multiple thumbnails (shown with order numbers), then clickUse Selected
* Upload new images with theUpload filesbutton (supports multi-file selection in multi-image mode)
* Remove individual images from history with the ✕ button
* History persists across browser sessions (stored inlocalStorage)

## 🚀 Quick Start

### Prerequisites

* Node.js(v18+)
* AMuapi.aiAPI key

### Setup

#
 Clone the repository

git clone https://github.com/Anil-matcha/Open-Generative-AI.git

cd
 Open-Generative-AI

#
 Install dependencies (installs root + packages/studio workspace)

npm install

#
 Start the development server

npm run dev

Openhttp://localhost:3000in your browser. You'll be prompted to enter your Muapi API key on first use.

### Production Build

npm run build
npm run start

### Desktop App Build

Build native desktop apps with Electron:

#
 macOS (DMG — Intel + Apple Silicon)

npm run electron:build

#
 Windows (NSIS installer — x64 + ARM64)

npm run electron:build:win

#
 Linux (AppImage + DEB — x64)

npm run electron:build:linux

#
 Both platforms in one pass

npm run electron:build:all

Installers are output to therelease/folder. Pre-built binaries are also available on theReleases page.

## 🏗️ Architecture

The app is aNext.js monorepowith a sharedpackages/studiocomponent library.

Open-Generative-AI/
├── app/ # Next.js App Router
│ ├── layout.js # Root layout (Tailwind, fonts)
│ ├── page.js # Redirects → /studio
│ └── studio/
│ └── page.js # Studio page — renders StandaloneShell
├── components/
│ ├── StandaloneShell.js # Tab nav + BYOK (API key from localStorage)
│ └── ApiKeyModal.js # API key entry modal
├── packages/
│ └── studio/ # Shared React component library
│ └── src/
│ ├── index.js # Exports: ImageStudio, VideoStudio, LipSyncStudio, CinemaStudio, WorkflowStudio
│ ├── models.js # 200+ model definitions (single source of truth)
│ ├── muapi.js # API client (named exports, apiKey as first param)
│ └── components/
│ ├── ImageStudio.jsx # Dual-mode t2i/i2i studio
│ ├── VideoStudio.jsx # Dual-mode t2v/i2v studio
│ ├── LipSyncStudio.jsx # Portrait/video + audio → talking video
│ ├── CinemaStudio.jsx # Pro studio with camera controls
│ └── WorkflowStudio.jsx # Multi-step pipeline builder & playground
├── next.config.mjs # transpilePackages: ['studio']
├── tailwind.config.js
└── package.json # workspaces: ["packages/studio"]

Thepackages/studiolibrary is also consumed by the hosted version onmuapi.ai— model updates made inpackages/studio/src/models.jsapply to both the self-hosted app and the hosted version automatically.

## 🔌 API Integration

The app communicates withMuapi.aiusing a two-step pattern:

1. Submit—POST /api/v1/{model-endpoint}with prompt and parameters
2. Poll—GET /api/v1/predictions/{request_id}/resultuntil status iscompleted

Authentication uses thex-api-keyheader. During development, a Vite proxy handles CORS by routing/apirequests tohttps://api.muapi.ai.

File uploads usePOST /api/v1/upload_file(multipart/form-data) and return a hosted URL that is passed to image-conditioned models. For multi-image models the fullimages_listarray is forwarded to the API in one request.

Lip sync jobs use the same two-step pattern: a dedicatedprocessLipSync()method acceptsimage_urlorvideo_urlalongsideaudio_url, dispatches to the model's endpoint, and polls until the output video URL is available.

## 🎨 Supported Model Categories

Category

Count

Examples

Text-to-Image

50+

Flux Dev, Nano Banana 2, Seedream 5.0, Ideogram v3, Midjourney v7, GPT-4o, SDXL

Image-to-Image

55+

Nano Banana 2 Edit (×14), Flux Kontext Pro, GPT-4o Edit, Seededit v3, Upscaler, Background Remover

Text-to-Video

40+

Kling v3, Sora 2, Veo 3, Wan 2.6, Seedance 2.0, Seedance 2.0 Extend, Seedance Pro, Hailuo 2.3, Runway Gen-3

Image-to-Video

60+

Kling v2.1 I2V, Veo3 I2V, Runway I2V, Seedance 2.0 I2V, Midjourney v7 I2V, Hunyuan I2V, Wan2.2 I2V

Lip Sync

9

Infinite Talk I2V, Wan 2.2 Speech to Video, LTX 2.3 Lipsync, LTX 2 19B Lipsync, Sync, LatentSync, Creatify, Veed, Infinite Talk V2V

## 🛠️ Tech Stack

* Next.js 14— App Router, server components, fast dev server
* React 18— Studio UI components
* Tailwind CSS v3— Utility-first styling
* npm workspaces— Monorepo with sharedpackages/studiolibrary
* Muapi.ai— AI model API gateway

## 🤔 How is this different from Higgsfield AI, Freepik, Krea, Openart AI?

Open Generative AIis a community-driven, open-source alternative that provides similar creative capabilities without the closed ecosystem:

Other providers

Open Generative AI

Cost

Subscription-based

Free (open-source)

Content filters

Yes — prompts blocked or altered

None — fully uncensored

Restrictions

Platform guardrails enforced

Unrestricted creative freedom

Models

Proprietary

200+ open & commercial models

Multi-image input

Limited

Up to 14 images per request

Lip sync

No

9 models, image & video modes

Hosted version

Subscription

Free at 
muapi.ai/open-generative-ai

Self-hosting

No

Yes

Customizable

No

Fully hackable

Data privacy

Cloud-based

Your data stays local

Source code

Closed

MIT licensed

## 📄 License

MIT

## 🙏 Credits

Built withMuapi.ai— the unified API for AI image and video generation models.

Deep Dive: For more details on the "AI Influencer" engine, upcoming "Popcorn" storyboarding features, and the future of this project, read thefull technical overview.

Looking for a free, uncensored Higgsfield AI, Freepik, Krea, Openart AI alternative? Open Generative AI is an open-source, unrestricted AI image and video generation studio — a Higgsfield AI, Freepik, Krea, Openart AI replacement with no content filters that you can self-host, customize, and extend.

This project is an independent, experimental, and open-source initiative and is not affiliated with, endorsed by, or associated with Higgsfield Inc., Freepik, Krea AI, OpenArt AI, or any of their respective companies, products, or services. Any references to third-party platforms, models, or technologies are made solely for interoperability, benchmarking, research, or educational purposes. All trademarks, logos, and brand names are the property of their respective owners. If any content in this repository creates confusion or raises concerns, please contact us and we will promptly review and address it.

## About

Uncensored, open-source alternative to Higgsfield AI, Freepik AI, Krea AI, Openart AI — Free, unrestricted AI image & video generation studio with 200+ models (Flux, Midjourney, Kling, Sora, Veo). No content filters. Self-hosted, MIT licensed.

dev.muapi.ai/open-generative-ai

### Topics

 javascript

 open-source

 uncensored

 muapi

 image-to-video

 unrestricted

 text-to-video

 creative-tools

 generative-ai

 ai-image-generation

 ai-art-generator

 midjourney-alternative

 ai-video-generation

 wan-video

 kling-ai

 higgsfield-ai

 higgsfield

 flux-1

 sora-alternative

 higgsfield-alternative

### Resources

 Readme

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

7.6k

 stars
 

### Watchers

62

 watching
 

### Forks

1.4k

 forks
 

 Report repository

 

## Releases5

v1.0.4 — Agents & Workflows tabs

 Latest

 

Apr 22, 2026

 

+ 4 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* JavaScript99.0%
* Other1.0%