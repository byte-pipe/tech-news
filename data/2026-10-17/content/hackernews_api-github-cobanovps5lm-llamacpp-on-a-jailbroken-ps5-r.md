---
title: 'GitHub - cobanov/PS5LM: llama.cpp on a jailbroken PS5: run any GGUF model natively on the console, starting with Qwen 3.8 · GitHub'
url: https://github.com/cobanov/PS5LM
site_name: hackernews_api
content_file: hackernews_api-github-cobanovps5lm-llamacpp-on-a-jailbroken-ps5-r
fetched_at: '2026-10-17T14:04:05.140362'
original_url: https://github.com/cobanov/PS5LM
author: Anon84
date: '2026-10-16'
description: 'llama.cpp on a jailbroken PS5: run any GGUF model natively on the console, starting with Qwen 3.8 - cobanov/PS5LM'
tags:
- hackernews
- trending
---

main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

80 Commits
80 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
docs
docs
 
 
patches
patches
 
 
probes
probes
 
 
ps5
ps5
 
 
scripts
scripts
 
 
site
site
 
 
third_party
third_party
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
CHANGELOG.md
CHANGELOG.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
View all files

## Repository files navigation

# PS5LM

Your PS5 runs the language model. Every device on your network uses it.llama.cpp on the console's GPU, with OpenAI and Anthropic APIs and a screen made for the TV.

Get the app·Website·Get started·Issues

New: decision models, powered byOllaya.PS5LM now runs Jev-like
decision models (d1, Clef, OpenJev and more) on the GPU and answers the same/v1/systemoneAPI as Ollaya: typed decisions with calibrated probabilities, in a fraction of a second.

PS5LM is for anyone with a jailbroken PS5 who wants a private model server at home. It loads a GGUF
model onto the console's GPU and serves it to your laptop, your phone and your coding tools. It needs
no PC while it runs, no cloud and no account.

Qwen 3.5 9B answering requests from a laptop on a PS5 Slim. Click for the video.

Home, Models, Console, API and Settings on the TV.

## A model server under your TV

* It runs on the GPU.llama.cpp's Vulkan backend on the console's RDNA 2 GPU, with 11.4 GB of the
shared memory for the model and its context. Every architecture and quantization llama.cpp knows
comes along.
* It answers your network.OpenAI's/v1/chat/completions, Anthropic's/v1/messages(Claude Code
works against it) and a chat page in any browser. Point a client athttp://<console>:8081and use
any model name: the loaded one answers.
* It decides, too.Load a decision model and the console answers TypeSafe's/v1/systemone:
choice, score and yes-or-no questions about text and images, the API Ollaya serves on a PC.
* It shows its work.Every request streams across the TV as a chat: which device asked, what it
asked, and the reply as it is written. Square sends a demo and Triangle opens a keyboard, so the
console can be tried from the couch.
* It watches the console.A Console page charts temperature, power, GPU and CPU load over the
last two minutes or the last hour, beside a table of every reading.
* It picks what fits.The planner reads each GGUF and gives it the longest context and best cache
that fit the memory free. A Suggested list holds models measured on the console, and the app
downloads from Hugging Face by itself, to internal storage, the M.2 drive or a USB drive.
* It reads images.Models with an image projector (Gemma 4, MiniCPM-V, d1) take pictures in chat
and in decisions.

Model

Size

On a PS5 Slim

Qwen 3.5 0.8B, Q4_K_M

0.5 GB

207 tokens a second

Qwen 3.5 9B, Q4_K_M

5.3 GB

55 tokens a second

Qwen 3.8 27B, UD-Q2_K_XL

9.2 GB

about 20 tokens a second, 64k context

d1 Omni 600M, a decision model

1.1 GB

3 questions in 0.3 s; a 720p image and 7 questions in 2.9 s

## Decision models, powered by Ollaya

Ollayaruns open decision models on a PC the way Ollama runs
language models. PS5LM brings the same idea to the console: a decision model reads a state and
answers typed questions in one forward pass, with no text generated.

curl http://
<
console
>
:8081/v1/systemone -H 
'
Content-Type: application/json
'
 -d 
'
{

 "state": "I was charged twice this month. Refund me or I cancel.",

 "questions": {

 "intent": {"type": "choice", "instructions": "What does the customer want?",

 "criteria": {"refund": null, "information": null, "cancel": null}},

 "angry": {"type": "noul", "instructions": "Is the customer angry?"}

 }

}
'

The Suggested list has d1 Omni 600M, d1 3B and Clef Flash. Any GGUF that carries llama.cpp's
decision metadata loads the same way, and the app labels it a decision model.

## Try it

You need a PS5 on firmware 7.00 to 13.60, jailbroken, with these payloads loaded:

Payload

For

kstuff-lite

the kernel patches homebrew runs on

required

etaHEN

homebrew support

required

ShadowMountPlus

puts PS5LM on the home screen from 
/data/homebrew

required

elfldr
 (port 9021)

temperature, power and real free space, through ps5-exporter

recommended

ftpsrv
 (port 2121)

installing the app, copying models from a PC

recommended

1. Downloadps5lm-app-vX.Y.Z.zipfrom thelatest releaseand unzip it.
2. Copy thePPSA99575folder to/data/homebrewover FTP. ShadowMountPlus addsPS5LMto the
home screen.
3. Open PS5LM, go toModels > Suggestedand get a model. Or copy a.ggufto/data/PS5LM/models, or toPS5LM/modelson a USB drive.
4. Load it. Once Home says Ready, openhttp://<console>:8081in a browser, or point your OpenAI or
Anthropic client at it.

To update, copy the new folder over the old one. Settings, models and downloads stay in/data/PS5LM. Using it from coding tools (opencode, Codex, Claude Code) is indocs/CLI.md.

Where

Button

Does

Everywhere

L1 / R1

Home, Models, API, Console, Settings

Home

Cross

change the model

Home

Square / Triangle

send a demo request / type a message

Models

D-pad, Cross

choose a section and a model; load, unload or download it

Models, Search

L2 / R2, Square

change the search; check whether a file fits

Models, Downloads

Cross, Square

pause or resume; cancel (press twice) or clear

Console

L2 / R2

the last two minutes / the last hour

Settings

D-pad, Cross

choose a category and a row; flip it, or pick from its list

Settings, Diagnostics

Square, Triangle

app or server log; errors only

## Want to tinker?

C++ onps5-homebrew-ui, llama.cpp with
ggml-vulkan onPS5_Vulkan's RADV, built on Linux.

Building·Console notes·Porting·Research·Models that fit·Roadmap·Changelog·The original payload

## Thanks

* abhi245y, who built the native GPU app this one grew from (PS5LM Plus).
* llama.cpp and ggml, which do the actual work.
* Mihawk-99for PS5_Vulkan and RADV on the PS5, andPS5CEMU-HARfor the driver patches inpatches/mesa.
* BlackBearReloadedfor ps5-homebrew-ui, ps5-opengl and
ps5-homebrew-dev-protocol, andJohn Törnblomfor the SDK.
* Maricefor ps5-exporter, which the app carries.
* Manrope(OFL) for the type, andPocketVibefor the interface sounds.

GPL-3.0-or-later, seeLICENSE. llama.cpp keeps its MIT licence, Manrope its OFL. No Sony
SDK files, keys, firmware or model weights are in this repository.

PS5LM is not affiliated with Sony Interactive Entertainment. "PlayStation" and "PS5" are trademarks
of Sony Interactive Entertainment.