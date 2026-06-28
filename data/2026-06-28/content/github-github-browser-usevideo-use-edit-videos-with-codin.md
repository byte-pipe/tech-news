---
title: 'GitHub - browser-use/video-use: Edit videos with coding agents · GitHub'
url: https://github.com/browser-use/video-use
site_name: github
content_file: github-github-browser-usevideo-use-edit-videos-with-codin
fetched_at: '2026-06-28T11:36:51.983574'
original_url: https://github.com/browser-use/video-use
author: browser-use
description: Edit videos with coding agents. Contribute to browser-use/video-use development by creating an account on GitHub.
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 browser-use

 

/

video-use

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.5k
* Star10.6k

 
 
 
 
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

16 Commits
16 Commits
helpers
helpers
 
 
skills/
manim-video
skills/
manim-video
 
 
static
static
 
 
.env.example
.env.example
 
 
.gitignore
.gitignore
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SKILL.md
SKILL.md
 
 
install.md
install.md
 
 
poster.html
poster.html
 
 
pyproject.toml
pyproject.toml
 
 
View all files

## Repository files navigation

# video-use

Introducingvideo-use— edit videos with Claude Code. 100% open source.

Drop raw footage in a folder, chat with Claude Code, getfinal.mp4back. Works for any content — talking heads, montages, tutorials, travel, interviews — without presets or menus.

## What it does

* Cuts out filler words(umm,uh, false starts) and dead space between takes
* Auto color gradesevery segment (warm cinematic, neutral punch, or any custom ffmpeg chain)
* 30ms audio fadesat every cut so you never hear a pop
* Burns subtitlesin your style — 2-word UPPERCASE chunks by default, fully customizable
* Generates animation overlaysviaHyperFrames,Remotion,Manim, or PIL — spawned in parallel sub-agents, one per animation
* Self-evaluates the rendered outputat every cut boundary before showing you anything
* Persists session memoryinproject.mdso next week's session picks up where you left off

## Setup prompt

Paste into Claude Code, Codex, Hermes, Openclaw, or any agent with shell access:

Set up https://github.com/browser-use/video-use for me.

Read install.md first to install this repo, wire up ffmpeg, register the skill with whichever agent you're running under, and set up the ElevenLabs API key — ask me to paste it when you need it. Then read SKILL.md for daily usage, and always read helpers/ because that's where the editing scripts live. After install, don't transcribe anything on your own — just tell me it's ready and wait for me to drop footage into a folder.

The agent handles the clone, dependencies, skill registration, and prompts you once for your ElevenLabs API key (grab one atelevenlabs.io/app/settings/api-keys).

Then point your agent at a folder of raw takes:

cd
 /path/to/your/videos
claude 
#
 or codex, hermes, etc.

For always-on editing from your own VPS or Telegram, run the agent throughBrowser Use Box.Watch the 15-second demo.

And in the session:

edit these into a launch video

It inventories the sources, proposes a strategy, waits for your OK, then producesedit/final.mp4next to your sources. All outputs live in<videos_dir>/edit/— the skill directory stays clean.

## Manual install

If you'd rather do it by hand:

#
 1. Clone and symlink into your agent's skills directory

git clone https://github.com/browser-use/video-use 
~
/Developer/video-use
ln -sfn 
~
/Developer/video-use 
~
/.claude/skills/video-use 
#
 Claude Code

#
 ln -sfn ~/Developer/video-use ~/.codex/skills/video-use # Codex

#
 2. Install deps

cd
 
~
/Developer/video-use
uv sync 
#
 or: pip install -e .

brew install ffmpeg 
#
 required

brew install yt-dlp 
#
 optional, for downloading online sources

#
 3. Add your ElevenLabs API key

cp .env.example .env

$EDITOR
 .env 
#
 ELEVENLABS_API_KEY=...

## How it works

The LLM never watches the video. Itreadsit — through two layers that together give it everything it needs to cut with word-boundary precision.

Layer 1 — Audio transcript (always loaded).One ElevenLabs Scribe call per source gives word-level timestamps, speaker diarization, and audio events ((laughter),(applause),(sigh)). All takes pack into a single ~12KBtakes_packed.md— the LLM's primary reading view.

## C0103 (duration: 43.0s, 8 phrases)
 [002.52-005.36] S0 Ninety percent of what a web agent does is completely wasted.
 [006.08-006.74] S0 We fixed this.

Layer 2 — Visual composite (on demand).timeline_viewproduces a filmstrip + waveform + word labels PNG for any time range. Called only at decision points — ambiguous pauses, retake comparisons, cut-point sanity checks.

Naive approach: 30,000 frames × 1,500 tokens =45M tokens of noise.
Video Use:12KB text + a handful of PNGs.

Same idea as browser-use giving an LLM a structured DOM instead of a screenshot — but for video.

## Pipeline

Transcribe ──> Pack ──> LLM Reasons ──> EDL ──> Render ──> Self-Eval
 │
 └─ issue? fix + re-render (max 3)

The self-eval loop runstimeline_viewon therendered outputat every cut boundary — catches visual jumps, audio pops, hidden subtitles. You see the preview only after it passes.

## Design principles

1. Text + on-demand visuals.No frame-dumping. The transcript is the surface.
2. Audio is primary, visuals follow.Cuts come from speech boundaries and silence gaps.
3. Ask → confirm → execute → self-eval → persist.Never touch the cut without strategy approval.
4. Zero assumptions about content type.Look, ask, then edit.
5. 12 hard rules, artistic freedom elsewhere.Production-correctness is non-negotiable. Taste isn't.

SeeSKILL.mdfor the full production rules and editing craft.

## About

Edit videos with coding agents

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

10.6k

 stars
 

### Watchers

61

 watching
 

### Forks

1.5k

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

* Python76.0%
* HTML22.9%
* Shell1.1%