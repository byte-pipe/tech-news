---
title: 'GitHub - Niko1221/Strata: Qwen3.8-Flash-Next on any consumer hardware: one-click install for Windows / Linux. Strata inference engine, OpenAI/Anthropic API on localhost, optional image input. · GitHub'
url: https://github.com/Niko1221/Strata
site_name: hackernews_api
content_file: hackernews_api-github-niko1221strata-qwen38-flash-next-on-any-con
fetched_at: '2026-10-04T22:12:22.547942'
original_url: https://github.com/Niko1221/Strata
author: snehesht
date: '2026-10-04'
description: 'Qwen3.8-Flash-Next on any consumer hardware: one-click install for Windows / Linux. Strata inference engine, OpenAI/Anthropic API on localhost, optional image input. - Niko1221/Strata'
tags:
- hackernews
- trending
---

Niko1221

 

/

Strata

Public

* NotificationsYou must be signed in to change notification settings
* Fork947
* Star10.8k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

845 Commits
845 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
bench/
results
bench/
results
 
 
cmake
cmake
 
 
data
data
 
 
docs
docs
 
 
include/
strata
include/
strata
 
 
ref
ref
 
 
serve
serve
 
 
src
src
 
 
sycl
sycl
 
 
tests
tests
 
 
third_party/
ggml
third_party/
ggml
 
 
tools
tools
 
 
.dockerignore
.dockerignore
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
CMakeLists.txt
CMakeLists.txt
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
README.de.md
README.de.md
 
 
README.es.md
README.es.md
 
 
README.fr.md
README.fr.md
 
 
README.ja.md
README.ja.md
 
 
README.md
README.md
 
 
README.pt-BR.md
README.pt-BR.md
 
 
README.zh-CN.md
README.zh-CN.md
 
 
SECURITY.md
SECURITY.md
 
 
SETUP.bat
SETUP.bat
 
 
START-HERE.bat
START-HERE.bat
 
 
UPDATE.bat
UPDATE.bat
 
 
chat.py
chat.py
 
 
docker-entrypoint.sh
docker-entrypoint.sh
 
 
requirements.txt
requirements.txt
 
 
setup.py
setup.py
 
 
setup.sh
setup.sh
 
 
update.sh
update.sh
 
 
View all files

## Repository files navigation

# Strata

English·简体中文·日本語·Deutsch·Français·Español·Português

Run a 125-billion-parameter AI model on your own gaming PCNVIDIA or AMD graphics card (12 GB or more) · Windows or Linux · free and open source

A voxel pagoda garden, 1 shot prompt running on an RTX 5070 with Strata (IQ3_S, 128K context) ·full video (49 s)

Strata runsQwen3.8-Flash-Nexton a normal PC. This is a
large, smart AI model that usually needs a server. It chats, writes code, reads pictures and works with your apps
and coding agents. Nothing leaves your PC.

## How fast is it?

We measured it on two ordinary gaming PCs. A token is about ¾ of a word.

* Writes answers:how fast the reply appears in a short chat. 60 tokens per second is faster than you can read.
* Reads your prompt:how fast it takes in what you send (here a 32K-token document, code or chat history).

NVIDIA: RTX 5070 (12 GB), Ryzen 5 7600, 64 GB RAM
AMD: RX 9070 XT (16 GB), Ryzen 9 3900X, 47 GB RAM

Size

Writes answers

Reads your prompt

Q2_0

94 tokens/s

2,650 tokens/s

IQ2_XS

79 tokens/s

2,090 tokens/s

IQ3_XXS

62 tokens/s

1,750 tokens/s

IQ3_S

53 tokens/s

1,620 tokens/s

Coder

55 tokens/s

2,180 tokens/s

Size

Writes answers

Reads your prompt

Q2_0

60 tokens/s

1,160 tokens/s

IQ2_XS

52 tokens/s

1,110 tokens/s

Coder

44 tokens/s

1,420 tokens/s

NVIDIA: Q2_0 with engine 0.1.36, the other rows with 0.1.26 (4K answers, 32K prompts). The full tables are inDETAILS.md. A card with more VRAM is faster: an RTX 3090 (24 GB) should write
about 100-140 tokens per second. Long chats and other cards:speed of each model,community results.

Strata is free. If it runs well on your PC, a coffee keeps the work on it going.

## What you need

Graphics card

NVIDIA
 GeForce RTX 20, 30, 40 or 50 series, or 
AMD
 Radeon RX 7900 XT / XTX, RX 7800 XT / 7700 XT, RX 9060 XT, RX 9070 / 9070 XT, Radeon AI PRO R9700 or RX 6800 / 6900 series. It needs 
12 GB of VRAM or more
.

RAM

32 GB or more. Your RAM decides 
which model
 fits. 64 GB runs every size.

Disk

About 80 GB free. Use an SSD if you can: the first start is much faster.

System

Windows 10 / 11 or Linux, and a current graphics driver from NVIDIA or AMD.

The installer sets up everything else. Two or three cards can share the model (multi-GPU).

Experimental, written and tested by community members on their own machines:

* Older graphics cards(Tesla P40 / V100, GTX 10, Radeon VII / MI50, RX 6700 XT, RX 5500 XT):Older GPUs.
* Intel Arc, built from source on Linux:Intel Arc.
* Older processors without AVX2: they work, but slowly.Older CPUs.

The full list:docs/INSTALL.md.

## Install

### Let your AI set it up

Do you use an AI coding assistant (Claude Code, Cursor, Codex, GitHub Copilot, ...)? Paste this into it:

Set up Strata on this PC for me: https://github.com/Niko1221/Strata - follow docs/AI_SETUP.md in that repository.

It checks your graphics card, RAM and disk and picks the model that fits. Then it installs and starts it and tells
you how to connect your apps. AI tools can also install, start and stop Strata through itsMCP server.

### Or do it yourself

Download Strataand unzip it (orgit cloneit).Windows:double-clickSTART-HERE.bat.Linux:run./setup.shin the Strata folder.

The steps are the same for NVIDIA and AMD. The installer finds your card and sets up the right engine for it. It
asks you a few questions:

* which model and which size,
* how much context (how much text the model keeps in mind),
* whether it should read pictures.

Press Enter each time for the recommended answer. Then it downloads the model (about 70 GB) and starts it. If the
download stops, run it again: it continues where it left off. Your browser opens the Strata app athttp://127.0.0.1:8080.

While the model starts, your PC can be slow or stop responding for 1-3 minutes(longest the first time).
Strata loads 35-55 GB into your RAM and locks part of it for the graphics card. This is normal. Wait, and don't
close the window. The window shows what Strata is doing.

Next time, runSTART-HERE.bat(or./setup.sh) again. It starts right away and downloads nothing twice. Close
its window to stop the model.UPDATE.bat(./update.sh) updates Strata without starting it. Updating, Docker,
several cards, where the files go and every option:docs/INSTALL.md.

## Which model should I pick?

The installer recommends one for your RAM. The same model comes in several sizes, compressed more or less. Smaller
sizes are faster. Larger sizes are a bit smarter.

Your RAM

Take

Why

32 GB

Coder

it fits 32 GB, and it is made for code (with a 24 GB card, Q2_0 and IQ2_XS run too)

48 GB

IQ2_XS
 (or Q2_0, the fastest)

the larger sizes do not fit

64 GB

IQ2_XS
 (recommended), or IQ3_XXS / IQ3_S

every size fits; IQ3_S is the best and the slowest

96 GB or more

IQ3_S
, or Unsloth's UD-IQ4_XS (~4-bit)

room for the largest sizes with everything else open

* Coder:a coding version with half of the experts removed. It reaches 91% of the full
model's SWE-bench Verified score (measured by its authors) and fits 32 GB of RAM. It is weaker outside code,
including Chinese and other CJK text (#438). For those, take Q2_0, IQ2_XS or IQ3_S, which keep every expert.
* Swift 1.5:a fine-tune that thinks for a much shorter time before it answers. You
get the answer sooner, at about the same quality.
* Unsloth UD-IQ4_XS:Unsloth's ~4-bit version, between IQ3_S and
UD-Q4_K_XL in quality. A 94 GB download. With less than ~80 GB of RAM, Strata reads part of it from the SSD
while it answers, so it is slower there (an NVMe SSD helps).
* Unsloth UD-Q4_K_XL(experimental): the closest to the full
model. But Strata reads most of it from the SSD while it answers, so it writes only 7-8.5 tokens/s on a 64 GB PC.
* OrcaRouter's Uncensored IQ3_XXS:you set it up by hand. It is
not in the installer's menu.

Sizes, downloads and what fits where:docs/MODELS.md. To add another model later, runSETUP.bat(Linux:./setup.sh --setup).

## Using it

The Strata app'sMonitor(left) while a coding agent writes the pagoda garden from the video (right)

* In the browser:openhttp://127.0.0.1:8080. It hasChat, a liveMonitorof the model and your
GPU/CPU/RAM, andAboutwith the settings and addresses.
* Your apps and coding agents:add an "OpenAI-compatible" provider with the base URLhttp://127.0.0.1:8080/v1. Any API key and any model name work.Apps that use Anthropic's API:http://127.0.0.1:8080/v1/messages(Claude Code:ANTHROPIC_BASE_URL=http://127.0.0.1:8080).Codex CLI and other apps that use the OpenAI Responses API:/v1/responses(setup).
* Apps that use Anthropic's API:http://127.0.0.1:8080/v1/messages(Claude Code:ANTHROPIC_BASE_URL=http://127.0.0.1:8080).
* Codex CLI and other apps that use the OpenAI Responses API:/v1/responses(setup).
* Thinking:chooseoff, low, medium or highin the chat menu or in your app's "reasoning effort". Off is the
fastest. High is best for hard questions.
* Pictures:say yes to "Images?" in setup. Then clickPicturein the chat, or attach pictures in your app.
AMD cards read pictures on Linux through the processor; on Windows they can't yet.
* From your phone or another PC:START-HERE.bat --setup --host 0.0.0.0 --api-key <secret>. Always set a key.
* One request at a time:by default Strata answers one request, and the others wait. To answer several at once,
set"parallel": 2(BATCHING.md). On a 12 GB card this makes each answer slower.
* Long prompts:Strata reads the first message of a chat in full, about 1 minute per 30,000 tokens. Follow-up
messages start in seconds.

More:where your chats are stored,the API.

## Something went wrong?

* My PC froze the first time Strata started.This is normal while it loads the model. Wait, and don't close the
window. Still frozen after 10 minutes? Restart the PC, close other programs and try again, or pick a smaller size.
* It stopped while downloading or installing.RunSTART-HERE.bat(or./setup.sh) again. It continues where
it stopped.
* It's very slow and the disk light keeps blinking, or it says "the engine stopped unexpectedly".Your PC does
not have enough free RAM. Close other programs (browsers use a lot), or pick a smaller size (Q2_0 or IQ2_XS).
* It says port 8080 is already in use.Strata is already running. Look for its window.

More problems and their fixes:docs/TROUBLESHOOTING.md. Still stuck? Open anissueand attachstrata-<model>.logfrom the Strata folder. Found a
security problem? Report it privately:SECURITY.md.

## How does it work?

Models like this one usually run on servers with hundreds of gigabytes of graphics memory. Your graphics card has
12-24 GB. Strata makes the model fit bysharing the work across your whole PC. Think of a kitchen: the things
you use all the time stay on the counter, and the rest waits in the pantry.

* The model is a team of 24,576 small specialists ("experts").Each word needs only 10 of them.
* Your graphics cardkeeps the few thousand experts that are used most often.Your RAMholds all of them,
andyour processorworks on the rest at the same time.Your SSDholds a big lookup table.

* Guess, then check:a small helper guesses the next few words. The big model checks them all at once. You get
the same answer, 1.6-1.8x sooner.
* Long texts are read in big pieces(up to 8,192 tokens at a time), at over 1,000 tokens per second.

The longer explanation:docs/HOW_IT_WORKS.md. Every part and its numbers:the detailsand thepaper.

## Credits and license

The model isQwen3.8-Flash-Nextby the Qwen team. It was
compressed byISTA-DASLab, UkisAI (Swift 1.5)
and Unsloth. Strata uses parts ofllama.cpp / ggml. All credits:docs/HOW_IT_WORKS.md. Strata is open source under theMIT License. A few
parts and every model have their own licenses (which ones).

## Support Strata

Strata is free and open source. If it is useful to you, you can support its development: