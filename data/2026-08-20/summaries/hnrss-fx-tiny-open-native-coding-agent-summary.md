---
title: fx - Tiny, open, native coding agent
url: https://fx.sh
date: 2026-08-18
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-08-20T07:17:57.546657
---

# fx - Tiny, open, native coding agent

# Tiny, open, native coding agent

## Overview
- **fx** is a coding‑agent harness and CLI written in Zig, targeting research and embeddability.
- Open‑source under Apache‑2.0, model‑agnostic, works with local or cloud inference.
- Designed to feel like a Unix shell rather than a heavyweight terminal IDE.

## Key Characteristics
- **Tiny binary**: ~6 MB (6.39 MiB) for instant installation in constrained environments.
- **Fast cold start**: initializes in ~10 µs, ready for prompt without extra I/O.
- **WebAssembly support**: builds with Zig produce `fx.wasm`, enabling browser demos on Safari 27+ and Chrome.
- **Low memory usage**: single‑digit megabytes baseline, allowing many instances per machine.
- **Shell‑like UI**: preserves scroll history, minimal output, avoids complex TUI graphics.
- **Context efficiency**: small system prompt and toolset reduce token costs and improve time‑to‑first‑token.
- **Extensible**: core can be expanded via skills, plugins, MCPs following a Unix‑style philosophy.
- **Provider agnostic**: compatible with local models, gateways, direct API access, or subscriptions.

## Usage
- Demo runs full fx CLI in the browser using `just-bash` and fetch‑based networking.
- Full tool suite can be installed locally via the provided setup script.