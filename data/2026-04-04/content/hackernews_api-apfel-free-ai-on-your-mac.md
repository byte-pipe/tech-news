---
title: apfel - Free AI on Your Mac
url: https://apfel.franzai.com
site_name: hackernews_api
content_file: hackernews_api-apfel-free-ai-on-your-mac
fetched_at: '2026-04-04T01:01:12.013791'
original_url: https://apfel.franzai.com
author: Arthur-Ficial
date: '2026-04-03'
description: Use Apple's built-in AI from the terminal. Free, private, 100% on-device. No API keys, no cloud, no subscriptions.
tags:
- hackernews
- trending
---

v0.6.13 · macOS 26+ · MIT


# apfel

The free AI already on your Mac.

Every Mac with Apple Silicon has a built-in LLM. Apple locked it behind Siri. apfel sets it free - as a CLI tool, an OpenAI-compatible server, and a chat.

 100% On-Device

 Zero Cost

 OpenAI Compatible

$
 brew install Arthur-Ficial/tap/apfel

 Copy


Apple Silicon · macOS Tahoe · Apple Intelligence enabled

## Watch it work.

Real commands. Real outputs. All running on Apple Silicon.

Terminal - apfel

$

## Zero everything.

The AI is already installed on your Mac. Apple ships it with macOS. apfel just gives you a way to talk to it - from your terminal, from your code, from anywhere.

$0

Token Cost

No API keys. No subscriptions. No per-token billing. It's your hardware - use it.

100%

On-device

Every token generated locally on your Apple Silicon. Nothing leaves your machine. Ever.

4,096

Tokens

Context window for input and output combined. Enough for most single-turn tasks and short chats.

### The model under the hood

Apple ML Research

~3B
Parameters

4,096
Context window

~3.5 bpw
Quantization

Mixed 2/4-bit
Precision

Neural Engine
Runs on

en, de, es, fr, it, ja, ko, pt, zh
Languages

## Three ways to use it.

CLI tool, HTTP server, or interactive chat. Pick the one that fits.

>_

### UNIX Tool

Pipe-friendly and composable. Works with jq, xargs, and your shell scripts. stdin, stdout, JSON output, file attachments, proper exit codes.

$
 apfel "What is the capital of Austria?"

The capital of Austria is Vienna.

$
 apfel -o json "Translate to German: hello" | jq .content

"Hallo"

{ }

### OpenAI Server

Drop-in replacement at localhost:11434. Point any OpenAI SDK at it and go. Streaming, tool calling, CORS, response formats.

$
 apfel --serve

Server running on http://127.0.0.1:11434

# any OpenAI client works

$
 curl localhost:11434/v1/chat/completions ...

...

### Interactive Chat

Multi-turn conversations with automatic context management. Five trimming strategies. System prompt support. All on your Mac.

$
 apfel --chat -s "You are a coding assistant"

Chat started. Type /quit to exit.

> How do I reverse a list in Python?

## How it works.

Apple built an LLM into your Mac. apfel gives it a front door.

### Apple ships an on-device LLM

Starting with macOS 26 (Tahoe), every Apple Silicon Mac includes a language model as part of Apple Intelligence. Apple exposes it through theFoundationModels framework- a Swift API that gives apps access toSystemLanguageModel. All inference runs on the Neural Engine and GPU. No network calls, no cloud, no API keys. The model is just there.

### But Apple only uses it for Siri

Out of the box, the on-device model powers Siri, Writing Tools, and system features. There is no terminal command, no HTTP endpoint, no way to pipe text through it. The FoundationModels framework exists, but you need to write a Swift app to use it. That is what apfel does.

### What apfel adds

apfel is a Swift 6.3 binary that wrapsLanguageModelSessionand exposes it three ways: as a UNIX command-line tool with stdin/stdout, as an OpenAI-compatible HTTP server (built on Hummingbird), and as an interactive chat with context management.

It handles the things Apple's raw API does not: proper exit codes, JSON output, file attachments, five context trimming strategies for the small 4096-token window, real token counting via the SDK, and conversion of OpenAI tool schemas to Apple's nativeTranscript.ToolDefinitionformat.

hardware

 Apple Silicon (Neural Engine + GPU)


|

model

 Apple's on-device LLM (shipped with macOS)


|

sdk

 FoundationModels.framework (Swift API)


|

apfel

 CLI + HTTP server + context management


|

you

 Terminal, shell scripts, OpenAI SDKs, curl


4,096 tokens

 Context window (input + output)


1 model

 Fixed, not configurable


Swift 6.3

 Strict concurrency, no Xcode


MIT license

 Open source


## Power tools included.

Shell scripts in thedemo/folder. Install apfel first, then grab the ones you want.

>_

### cmd

Natural language to shell command. Say what you want, get the command.

$ cmd "find all .log files modified today"

|>

### oneliner

Pipe chains from plain English. awk, sed, sort, uniq - generated for you.

$ oneliner "count unique IPs in access.log"

**

### mac-narrator

Narrates your Mac's system activity like a nature documentary.

$ mac-narrator --watch

?

### explain

Explain any command, error message, or code snippet in plain English.

$ explain "awk '{print $1}' file | sort -u"

./

### wtd

What's this directory? Instant project orientation for any codebase.

$ wtd

++

### gitsum

Summarize recent git commits in a few sentences.

$ gitsum

## OpenAI compatible. For real.

Change one URL. Keep your code.

### Drop-in replacement

apfel speaks the OpenAI API. Any client library, any framework, any tool that talks to OpenAI can talk to your Mac's AI instead. Just change the base URL.

* ✓POST /v1/chat/completions
* ✓Streaming (SSE)
* ✓Tool calling / function calling
* ✓GET /v1/models
* ✓response_format: json_object
* ✓temperature, max_tokens, seed
* ✓CORS for browser clients

Python

from

openai

import
 OpenAI

# Just change the base_url. That's it.

client = OpenAI(

base_url
=
"http://localhost:11434/v1"
,

api_key
=
"unused"

# no auth needed

)

resp = client.chat.completions.create(

model
=
"apple-foundationmodel"
,

messages
=[{

"role"
:
"user"
,

"content"
:
"What is 1+1?"

 }],
)

print
(resp.choices[
0
].message.content)

## Popular on GitHub.

From zero to 507 stars and counting.

507

GitHub stars

15
 forks

Two viral spikes: 123 stars on March 31, 295 on April 3. The first public release of Apple's on-device LLM as a command-line tool.

 Star on GitHub


0

100

200

300

400

500

+123

Mar 31

+295

507

Mar 24

Mar 28

Apr 1

Apr 3

Data as of April 3, 2026

## Get started.

Two commands. Ten seconds. You're in.

### Homebrew

recommended

$
 brew install Arthur-Ficial/tap/apfel

$
 apfel "Hello, Mac!"

### Build from source

requires CLT + macOS 26.4 SDK

$
 git clone https://github.com/Arthur-Ficial/apfel.git

$
 cd apfel && make install

 View on GitHub


## The apfel family.

Tools built on top of Apple's on-device AI.

### apfel-gui

Native macOS SwiftUI debug GUI. Chat with Apple Intelligence, inspect requests and responses, logs, speech-to-text, text-to-speech - all on-device.

SwiftUI

coming soon

### apfel-clip

AI-powered clipboard actions from the menu bar. Fix grammar, translate, explain code, summarize - one click on any selected text.

Under Heavy Development
