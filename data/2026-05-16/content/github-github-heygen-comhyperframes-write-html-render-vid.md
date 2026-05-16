---
title: 'GitHub - heygen-com/hyperframes: Write HTML. Render video. Built for agents. · GitHub'
url: https://github.com/heygen-com/hyperframes
site_name: github
content_file: github-github-heygen-comhyperframes-write-html-render-vid
fetched_at: '2026-05-16T11:25:01.842407'
original_url: https://github.com/heygen-com/hyperframes
author: heygen-com
description: Write HTML. Render video. Built for agents. Contribute to heygen-com/hyperframes development by creating an account on GitHub.
---

heygen-com

 

/

hyperframes

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.7k
* Star18.5k

 
 
 
 
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

988 Commits
988 Commits
.claude-plugin
.claude-plugin
 
 
.claude
.claude
 
 
.codex-plugin
.codex-plugin
 
 
.cursor-plugin
.cursor-plugin
 
 
.github
.github
 
 
assets
assets
 
 
docs
docs
 
 
packages
packages
 
 
registry
registry
 
 
scripts
scripts
 
 
skills
skills
 
 
.editorconfig
.editorconfig
 
 
.env.example
.env.example
 
 
.filesize-allowlist
.filesize-allowlist
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.oxfmtrc.json
.oxfmtrc.json
 
 
.oxlintrc.json
.oxlintrc.json
 
 
.prettierignore
.prettierignore
 
 
ADOPTERS.md
ADOPTERS.md
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
CREDITS.md
CREDITS.md
 
 
DESIGN.md
DESIGN.md
 
 
DOCS_GUIDELINES.md
DOCS_GUIDELINES.md
 
 
Dockerfile.test
Dockerfile.test
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
bun.lock
bun.lock
 
 
commitlint.config.js
commitlint.config.js
 
 
knip.config.ts
knip.config.ts
 
 
lefthook.yml
lefthook.yml
 
 
package.json
package.json
 
 
View all files

## Repository files navigation

Write HTML. Render video. Built for agents.

Hyperframes is an open-source video rendering framework that lets you create, preview, and render HTML-based video compositions — with first-class support for AI agents.

## Quick Start

### Option 1: With an AI coding agent (recommended)

Install the HyperFrames skills, then describe the video you want:

npx skills add heygen-com/hyperframes

This teaches your agent (Claude Code, Cursor, Gemini CLI, Codex) how to write correct compositions, GSAP timelines, Tailwind v4 browser-runtime styles, and first-party adapter animations. In Claude Code, the skills register as slash commands — invoke/hyperframesto author compositions,/hyperframes-clifor the dev-loop commands (init, lint, preview, render),/hyperframes-mediafor asset preprocessing (TTS, transcription, background removal),/tailwindforinit --tailwindprojects,/gsapfor timeline animation help, or the adapter skills (/animejs,/css-animations,/lottie,/three,/waapi) when a composition uses those runtimes.

For Claude Design, opendocs/guides/claude-design-hyperframes.mdon GitHub and click the download button (↓) to save it, then attach the file to your Claude Design chat. It produces a valid first draft; refine in any AI coding agent. See theClaude Design guide.

For Codex specifically, the same skills are also exposed as anOpenAI Codex plugin— sparse-install just the plugin surface:

codex plugin marketplace add heygen-com/hyperframes --sparse .codex-plugin --sparse skills --sparse assets

For Claude Code, the repo also ships aClaude Code plugin manifest: test it locally withclaude --plugin-dir .. The manifest intentionally omitsskillsbecause Claude Code auto-discovers the rootskills/directory by convention, and for marketplace submission use the titleHyperFrames by HeyGenplus the black/white icon assets atassets/claude-code-icon-dark.svgandassets/claude-code-icon-light.svgfor the two theme slots.
For Cursor, the same skills are packaged as aCursor plugin— install from the Cursor Marketplace, or sideload by cloning this repo and pointingSettings → Plugins → Load unpackedat the repo root.

#### Try it: example prompts

Copy any of these into your agent to get started. The/hyperframesprefix loads the skill context explicitly so you get correct output the first time.

Cold start — describe what you want:

Using/hyperframes, create a 10-second product intro with a fade-in title, a background video, and background music.

Warm start — turn existing context into a video:

Take a look at this GitHub repohttps://github.com/heygen-com/hyperframesand explain its uses and architecture to me using/hyperframes.

Summarize the attached PDF into a 45-second pitch video using/hyperframes.

Turn this CSV into an animated bar chart race using/hyperframes.

Format-specific:

Make a 9:16 TikTok-style hook video about [topic] using/hyperframes, with bouncy captions synced to a TTS narration.

Iterate — talk to the agent like a video editor:

Make the title 2x bigger, swap to dark mode, and add a fade-out at the end.

Add a lower third at 0:03 with my name and title.

The agent handles scaffolding, animation, and rendering. See theprompting guidefor more patterns.

### Option 2: Start a project manually

npx hyperframes init my-video

cd
 my-video
npx hyperframes preview 
#
 preview in browser (live reload)

npx hyperframes render 
#
 render to MP4

hyperframes initinstalls skills automatically, so you can hand off to your AI agent at any point.

Requirements:Node.js >= 22, FFmpeg

## Why Hyperframes?

* HTML-native— compositions are HTML files with data attributes. No React, no proprietary DSL.
* AI-first— agents already speak HTML. The CLI is non-interactive by default, designed for agent-driven workflows.
* Deterministic rendering— same input = identical output. Built for automated pipelines.
* Frame Adapter pattern— bring your own animation runtime (GSAP, Lottie, CSS, Three.js).

## Hyperframes vs Remotion

Hyperframes is inspired byRemotion— we used Remotion at HeyGen in production, learned a ton from it, and kept attribution comments in the source for the patterns it pioneered (Chrome launch flags, image2pipe → FFmpeg streaming, frame buffering). Both tools drive headless Chrome and both are deterministic. They differ on one decision:what the primary author writes.Remotion's bet is React components; Hyperframes' bet is HTML.

Hyperframes

Remotion

Authoring

HTML + CSS + GSAP

React components (TSX)

Build step

None; 
index.html
 plays as-is

Required (bundler)

Library-clock animations (GSAP, Anime.js, Motion One)

Seekable, frame-accurate

Plays at wall-clock during render

Arbitrary HTML / CSS passthrough

Paste and animate

Rewrite as JSX

Distributed rendering

Single-machine today

Lambda, production-ready

### Licensing: fully open source vs source-available

Hyperframes is completely open source underApache 2.0— an OSI-approved license. Use it commercially at any scale, with no per-render fees, no seat caps, no company-size thresholds.

Remotion issource-available, not open source.The code is on GitHub under a custom Remotion License that requires a paid company license above small-team thresholds. It's a great product with a real team behind it — but if open-source licensing matters to you (OSI compliance, redistribution rights, no per-use fees), that's a first-order decision point.

Full write-up with benchmarks, an honest list of where each tool wins, and a GSAP side-by-side:Hyperframes vs Remotion guide.

## How It Works

Define your video as HTML with data attributes:

<
div
 
id
="
stage
" 
data-composition-id
="
my-video
" 
data-start
="
0
" 
data-width
="
1920
" 
data-height
="
1080
"
>

 
<
video

 
id
="
clip-1
"
 
data-start
="
0
"
 
data-duration
="
5
"
 
data-track-index
="
0
"
 
src
="
intro.mp4
"
 
muted

 
playsinline

 
>
</
video
>

 
<
img

 
id
="
overlay
"
 
class
="
clip
"
 
data-start
="
2
"
 
data-duration
="
3
"
 
data-track-index
="
1
"
 
src
="
logo.png
"
 
/>

 
<
audio

 
id
="
bg-music
"
 
data-start
="
0
"
 
data-duration
="
9
"
 
data-track-index
="
2
"
 
data-volume
="
0.5
"
 
src
="
music.wav
"
 
>
</
audio
>

</
div
>

Preview instantly in the browser. Render to MP4 locally or in Docker.

## Catalog

50+ ready-to-use blocks and components — social overlays, shader transitions, data visualizations, and cinematic effects:

npx hyperframes add flash-through-white 
#
 shader transition

npx hyperframes add instagram-follow 
#
 social overlay

npx hyperframes add data-chart 
#
 animated chart

Browse the full catalog athyperframes.heygen.com/catalog.

## Documentation

Full documentation athyperframes.heygen.com/introduction—Quickstart|Guides|API Reference|Catalog

## Packages

Package

Description

hyperframes

CLI — create, preview, lint, and render compositions

@hyperframes/core

Types, parsers, generators, linter, runtime, frame adapters

@hyperframes/engine

Seekable page-to-video capture engine (Puppeteer + FFmpeg)

@hyperframes/producer

Full rendering pipeline (capture + encode + audio mix)

@hyperframes/studio

Browser-based composition editor UI

@hyperframes/player

Embeddable 
<hyperframes-player>
 web component

@hyperframes/shader-transitions

WebGL shader transitions for compositions

## Skills

HyperFrames shipsskillsthat teach AI agents framework-specific patterns that generic docs don't cover.

npx skills add heygen-com/hyperframes

Skill

What it teaches

hyperframes

HTML composition authoring, captions, TTS, audio-reactive animation, transitions

hyperframes-cli

Dev-loop CLI: init, lint, inspect, preview, render, doctor

hyperframes-media

Asset preprocessing: tts (Kokoro), transcribe (Whisper), remove-background (u2net) — voice/model/codec selection

hyperframes-registry

Block and component installation via 
hyperframes add

website-to-hyperframes

Capture a URL and turn it into a video — full website-to-video pipeline

remotion-to-hyperframes

Translate a Remotion (React) composition into a HyperFrames HTML composition

gsap

GSAP timelines for HyperFrames: paused registration, deterministic seeking, easing, sequencing, performance

animejs

Anime.js animations and timelines registered on 
window.__hfAnime
 for deterministic HyperFrames seeking

css-animations

CSS keyframe animation patterns that HyperFrames can discover, pause, and seek

lottie

lottie-web
 and dotLottie players registered on 
window.__hfLottie
 with local assets and paused playback

three

Three.js scenes that render from HyperFrames 
hf-seek
 events and 
window.__hfThreeTime
 instead of wall-clock time

waapi

Web Animations API 
element.animate()
 patterns seeked through 
document.getAnimations()

## Contributing

SeeCONTRIBUTING.mdfor guidelines.

### Cloning the repo

The repo usesGit LFSfor golden regression-test baselines underpackages/producer/tests/**/output.mp4(~240 MB of.mp4files). If you're cloning the full repo for development, install Git LFS first:

#
 macOS

brew install git-lfs

#
 Ubuntu/Debian

sudo apt install git-lfs

#
 Windows

winget install GitHub.GitLFS

#
 (or install Git for Windows, which bundles Git LFS as an optional component)

#
 Then (once, per machine)

git lfs install

If you hitgit-lfs filter-process: command not foundduringgit cloneornpx skills add heygen-com/hyperframes, install Git LFS and retry. You can also skip LFS content if you only need the source files:

GIT_LFS_SKIP_SMUDGE=1 git clone https://github.com/heygen-com/hyperframes.git

## License

Apache 2.0

## About

Write HTML. Render video. Built for agents.

### Topics

 html

 framework

 typescript

 video

 ai

 ffmpeg

 animation

 mcp

 rendering

 gsap

 puppeteer

### Resources

 Readme

 

### License

 Apache-2.0 license
 

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

18.5k

 stars
 

### Watchers

55

 watching
 

### Forks

1.7k

 forks
 

 Report repository

 

## Releases129

v0.6.12

 Latest

 

May 16, 2026

 

+ 128 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript97.4%
* JavaScript1.7%
* Other0.9%