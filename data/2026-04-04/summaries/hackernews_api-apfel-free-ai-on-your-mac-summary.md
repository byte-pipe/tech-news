---
title: apfel - Free AI on Your Mac
url: https://apfel.franzai.com
date: 2026-04-03
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-04-04T01:04:50.403456
---

# apfel - Free AI on Your Mac

# apfel – Free AI on Your Mac

## Overview
- Provides access to the built‑in large language model (LLM) on Apple Silicon Macs.
- Runs entirely on‑device: no API keys, subscriptions, or network calls.
- Distributed under the MIT license; implemented as a Swift 6.3 binary.

## Core Capabilities
- **Three access modes**
  - UNIX command‑line tool (`apfel "prompt"`).
  - OpenAI‑compatible HTTP server (`apfel --serve`) listening on `localhost:11434`.
  - Interactive chat with automatic context management (`apfel --chat`).
- **Model specifications**
  - Approximately 3 billion parameters.
  - 4,096‑token combined input/output context window.
  - Mixed 2‑/4‑bit quantization, running on the Neural Engine and GPU.
  - Supports English, German, Spanish, French, Italian, Japanese, Korean, Portuguese, Chinese.

## Technical Details
- Uses Apple’s `FoundationModels` framework (Swift API) to access `SystemLanguageModel`.
- Wraps `LanguageModelSession` and adds:
  - Proper exit codes and JSON output.
  - File attachment handling.
  - Five context‑trimming strategies for the limited token window.
  - Real token counting via the SDK.
  - Conversion of OpenAI tool schemas to Apple’s native `Transcript.ToolDefinition` format.
- Server built on the Hummingbird Swift web framework.

## Power Tools (included in `demo/`)
- `cmd`: generate shell commands from natural language.
- `oneliner`: create pipeline commands (awk, sed, sort, etc.) from plain English.
- `mac-narrator`: narrate system activity.
- `explain`: describe commands, errors, or code snippets.
- `wtd`: give a quick orientation of any directory’s purpose.
- `gitsum`: summarize recent Git commits.

## OpenAI Compatibility
- Implements the full OpenAI chat completion API:
  - `POST /v1/chat/completions` (including streaming via SSE).
  - Tool/function calling.
  - Model listing (`GET /v1/models`).
  - Parameters such as `temperature`, `max_tokens`, `seed`, and `response_format`.
  - CORS support for browser clients.
- Any OpenAI client library can be pointed at `http://localhost:1144` to use the on‑device model.

## Adoption
- Over 500 GitHub stars as of April 3 2026, with rapid growth after the first public release.
- 15 forks.

## Installation
- **Homebrew (recommended)**
  ```bash
  brew install Arthur-Ficial/tap/apfel
  apfel "Hello, Mac!"
  ```
- **Build from source** (requires CLT and macOS 26.4 SDK)
  ```bash
  git clone https://github.com/Arthur-Ficial/apfel.git
  cd apfel && make install
  ```

## Related Projects
- **apfel‑gui**: upcoming SwiftUI debugging interface for chat, request inspection, speech‑to‑text, and text‑to‑speech.
- **apfel‑clip**: menu‑bar clipboard utility for grammar fixing, translation, code explanation, summarization, etc. (under heavy development).
