---
title: fx - Tiny, open, native coding agent
url: https://fx.sh
site_name: hnrss
content_file: hnrss-fx-tiny-open-native-coding-agent
fetched_at: '2026-08-20T07:17:14.852234'
original_url: https://fx.sh
date: '2026-08-18'
description: Tiny, open, native coding agent. A minimal CLI written in Zig, optimized for research and embeddability as part of larger systems.
tags:
- hackernews
- hnrss
---

Tiny, open, native coding agent.

$curl -fsSL https://fx.sh/setup.sh | bashcopied

v0.0.3·6.39mib·status:experimental(i)use at your own risk, we will be making frequent changes

This demo runs the full fx CLI as WebAssembly compiled with the Zig toolchain.Networking is delegated to browserfetch, and every SDK aspect is configurable in thedocs.

fx
𝒇
x
 v0.0.3
 · Run /help for commands

┃

auto
 · glm-5.2
(i)
This demo is available in browsers with WebAssembly JSPI support, like Safari 27+ and Chrome.
This demo runs fx in WebAssembly with a browser workspace powered by
 
just-bash
.
 
Install fx
 
for the full tool suite on your own files.

fxis a coding agent harness and CLI written in Zig, optimized for research and embeddability as part of larger systems.

It focuses on minimalism and performance across the board, from system prompt design, to its tools, feature set, and 6.39mib binary.

For end users, its CLI output style and form factor aims to be closer to a Unix shell than a heavy "IDE in the terminal" TUI.

It's open source (Apache-2.0), model-agnostic, and suitable for both local and cloud inference.

***

## Tiny ~6mb binary

Designed for instant installation and embedding in resource constrained environments and agent sandboxes.

## Instant time to prompt

fx cold starts in10µsand does no unnecessary work or I/O prior to accepting user input, making it ideal for programmatic use.

## Wasm support

Optimal fx.wasm builds produced by the Zig toolchain, which further reduce fx's size, making the network stack pluggable.

## Minimal memory footprint

fx contributes single-digit megabytes of memory baseline, allowing you to pack many instances in one machine.

## Shell-like UI and ergonomics

fx preserves scroll history by default, produces minimal output, and makes sparing use of complex TUI or paints

## Context efficient

Minimal system prompt and tools, to save on token costs and to yield optimal time-to-first-token performance (TTFT).

## Embeddable and extensible

Small core, extended via skills, plugins, MCPs, with a Unix-like philosophy to extensibility.

## Model and provider agnostic

Designed to work withlocal models,gateways, direct provider API access orsubscriptions.