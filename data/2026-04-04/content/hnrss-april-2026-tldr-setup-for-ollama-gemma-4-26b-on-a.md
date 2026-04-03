---
title: April 2026 TLDR setup for Ollama + Gemma 4 26B on a Mac mini (Apple Silicon) — auto-start, preload, and keep-alive · GitHub
url: https://gist.github.com/greenstevester/fc49b4e60a4fef9effc79066c1033ae5
site_name: hnrss
content_file: hnrss-april-2026-tldr-setup-for-ollama-gemma-4-26b-on-a
fetched_at: '2026-04-04T01:03:01.588635'
original_url: https://gist.github.com/greenstevester/fc49b4e60a4fef9effc79066c1033ae5
date: '2026-04-03'
description: April 2026 TLDR setup for Ollama + Gemma 4 26B on a Mac mini (Apple Silicon) — auto-start, preload, and keep-alive - how-to-setup-ollama-on-a-macmini.md
tags:
- hackernews
- hnrss
---

Instantly share code, notes, and snippets.

# greenstevester/how-to-setup-ollama-on-a-macmini.md

 Last active
 
April 3, 2026 13:52

 

Show Gist options

 

* Download ZIP

 

 

* Star29(29)You must be signed in to star a gist
* Fork0(0)You must be signed in to fork a gist

* Embed# Select an optionEmbedEmbed this gist in your website.ShareCopy sharable link for this gist.Clone via HTTPSClone using the web URL.## No results foundLearn more about clone URLsClone this repository at &lt;script src=&quot;https://gist.github.com/greenstevester/fc49b4e60a4fef9effc79066c1033ae5.js&quot;&gt;&lt;/script&gt;
* EmbedEmbed this gist in your website.
* ShareCopy sharable link for this gist.
* Clone via HTTPSClone using the web URL.
* Save greenstevester/fc49b4e60a4fef9effc79066c1033ae5 to your computer and use it in GitHub Desktop.

 

Embed

# Select an option

 

* EmbedEmbed this gist in your website.
* ShareCopy sharable link for this gist.
* Clone via HTTPSClone using the web URL.

## No results found

 

 
 
Learn more about clone URLs

 

 

 Clone this repository at &lt;script src=&quot;https://gist.github.com/greenstevester/fc49b4e60a4fef9effc79066c1033ae5.js&quot;&gt;&lt;/script&gt;

 

 

Save greenstevester/fc49b4e60a4fef9effc79066c1033ae5 to your computer and use it in GitHub Desktop.

Download ZIP

 April 2026 TLDR setup for Ollama + Gemma 4 26B on a Mac mini (Apple Silicon) — auto-start, preload, and keep-alive
 

 

Raw

 how-to-setup-ollama-on-a-macmini.md
 

# April 2026 TLDR Setup for Ollama + Gemma 4 26B on a Mac mini (Apple Silicon)

## Prerequisites

* Mac mini with Apple Silicon (M1/M2/M3/M4/M5)
* At least 24GB unified memory for Gemma 4 26B
* macOS with Homebrew installed

## Step 1: Install Ollama

Install the Ollama macOS app via Homebrew cask (includes auto-updates and MLX backend):

brew install --cask ollama-app

This installs:

* Ollama.appin/Applications/
* ollamaCLI at/opt/homebrew/bin/ollama

## Step 2: Start Ollama

open -a Ollama

The Ollama icon will appear in the menu bar. Wait a few seconds for the server to initialize.

Verify it's running:

ollama list

## Step 3: Pull Gemma 4 26B

ollama pull gemma4:26b

This downloads ~17GB. Verify:

ollama list

#
 NAME ID SIZE MODIFIED

#
 gemma4:26b 5571076f3d70 17 GB ...

## Step 4: Test the Model

ollama run gemma4:26b 
"
Hello, what model are you?
"

Check that it's using GPU acceleration:

ollama ps

#
 Should show CPU/GPU split, e.g. 14%/86% CPU/GPU

## Step 5: Configure Auto-Start on Login

### 5a. Ollama App — Launch at Login

Click the Ollama icon in the menu bar >Launch at Login(enable it).

Alternatively, go toSystem Settings > General > Login Itemsand add Ollama.

### 5b. Auto-Preload Gemma 4 on Startup

Create a launch agent that loads the model into memory after Ollama starts and keeps it warm:

cat 
<<
 '
EOF
' > ~/Library/LaunchAgents/com.ollama.preload-gemma4.plist

<?xml version="1.0" encoding="UTF-8"?>

<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">

<plist version="1.0">

<dict>

 <key>Label</key>

 <string>com.ollama.preload-gemma4</string>

 <key>ProgramArguments</key>

 <array>

 <string>/opt/homebrew/bin/ollama</string>

 <string>run</string>

 <string>gemma4:26b</string>

 <string></string>

 </array>

 <key>RunAtLoad</key>

 <true/>

 <key>StartInterval</key>

 <integer>300</integer>

 <key>StandardOutPath</key>

 <string>/tmp/ollama-preload.log</string>

 <key>StandardErrorPath</key>

 <string>/tmp/ollama-preload.log</string>

</dict>

</plist>

EOF

Load the agent:

launchctl load 
~
/Library/LaunchAgents/com.ollama.preload-gemma4.plist

This sends an empty prompt toollama runevery 5 minutes, keeping the model warm in memory.

### 5c. Keep Models Loaded Indefinitely

By default, Ollama unloads models after 5 minutes of inactivity. To keep them loaded forever:

launchctl setenv OLLAMA_KEEP_ALIVE 
"
-1
"

Then restart Ollama for the change to take effect.

Note:This environment variable is session-scoped. To persist across reboots, addexport OLLAMA_KEEP_ALIVE="-1"to your~/.zshrc, or set it via a dedicated launch agent.

## Step 6: Verify Everything Works

#
 Check Ollama server is running

ollama list

#
 Check model is loaded in memory

ollama ps

#
 Check launch agent is registered

launchctl list 
|
 grep ollama

Expected output fromollama ps:

NAME ID SIZE PROCESSOR CONTEXT UNTIL
gemma4:26b 5571076f3d70 20 GB 14%/86% CPU/GPU 4096 Forever

## API Access

Ollama exposes a local API athttp://localhost:11434. Use it with coding agents:

#
 Chat completion (OpenAI-compatible)

curl http://localhost:11434/v1/chat/completions \
 -H 
"
Content-Type: application/json
"
 \
 -d 
'
{

 "model": "gemma4:26b",

 "messages": [{"role": "user", "content": "Hello"}]

 }
'

## Useful Commands

Command

Description

ollama list

List downloaded models

ollama ps

Show running models & memory usage

ollama run gemma4:26b

Interactive chat

ollama stop gemma4:26b

Unload model from memory

ollama pull gemma4:26b

Update model to latest version

ollama rm gemma4:26b

Delete model

## Uninstall / Remove Auto-Start

#
 Remove the preload agent

launchctl unload 
~
/Library/LaunchAgents/com.ollama.preload-gemma4.plist
rm 
~
/Library/LaunchAgents/com.ollama.preload-gemma4.plist

#
 Uninstall Ollama

brew uninstall --cask ollama-app

## What's New in Ollama v0.19+ (March 31, 2026)

### MLX Backend on Apple Silicon

On Apple Silicon, Ollama automatically uses Apple's MLX framework for faster inference — no manual configuration needed. M5/M5 Pro/M5 Max chips get additional acceleration via GPU Neural Accelerators. M4 and earlier still benefit from general MLX speedups.

### NVFP4 Support (NVIDIA)

Ollama now leverages NVIDIA's NVFP4 format to maintain model accuracy while reducing memory bandwidth and storage requirements for inference workloads. As more inference providers scale inference using NVFP4 format, this allows Ollama users to share the same results as they would in a production environment. It further opens up Ollama to run models optimized by NVIDIA's model optimizer.

### Improved Caching for Coding and Agentic Tasks

* Lower memory utilization:Ollama reuses its cache across conversations, meaning less memory utilization and more cache hits when branching with a shared system prompt — especially useful with tools like Claude Code.
* Intelligent checkpoints:Ollama stores snapshots of its cache at intelligent locations in the prompt, resulting in less prompt processing and faster responses.
* Smarter eviction:Shared prefixes survive longer even when older branches are dropped.

## Notes

* Memory:Gemma 4 26B uses ~20GB when loaded. On a 24GB Mac mini, this leaves ~4GB for the system — close memory-heavy apps before running.

## References

* Ollama MLX Blog Post— Ollama Newsletter, March 31, 2026
* Ollama v0.20.0 Release
* Gemma 4 Announcement — Google DeepMind

Sign up for free

to join this conversation on GitHub
.
 Already have an account?
 
Sign in to comment