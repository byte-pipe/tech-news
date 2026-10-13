---
title: Embedding Gemma Transcribe
url: https://eg2.haku.sh/
site_name: hnrss
content_file: hnrss-embedding-gemma-transcribe
fetched_at: '2026-10-13T17:58:05.287032'
original_url: https://eg2.haku.sh/
date: '2026-10-13'
description: Google's EmbeddingGemma 2, turned into a speech-to-text model. An hour of audio in about 13 seconds on a base MacBook Air, entirely on device. Free Mac app.
tags:
- hackernews
- hnrss
---

# Embedding Gemma Transcribe

Google's EmbeddingGemma 2 is an embedding model. We turned it into a speech-to-text model:an hour of audio in about 13 seconds on a base MacBook Air, entirely on device.

Download for Mac (free)

v1.6 · macOS 14+ · Apple Silicon
models download on first launch (715 MB)

## Can an embedding model transcribe speech?

EmbeddingGemma 2 is a multimodal embedding model: text, images, audio and video in one shared space.
 Say a word out loud and its audio lands close to the written word.

So we tried reading words straight out of that space.

## How it works

1. EmbeddingGemma 2's audio encoder stays exactly as it is.
2. A small reader moves each short slice of audio into the model's text space.
3. The closest of ~229,000 English words wins, and the slices become a transcript.
4. A tiny extra model adds punctuation and capitals.

Only the reader is trained: under two hours on 8×H100, on openly licensed English speech.
 The base model was never trained for speech-to-text.

## How fast?

Model
Runs on
Mac
Speed

Embedding Gemma Transcribe
Neural Engine
base M3 MacBook Air, 8 GB

288×
1 hour in 12.6 s

IBM Granite Speech 5.0 TurboCTC
GPU (MLX)
base M3 MacBook Air, 8 GB

~150×
1 hour in 25.7 s

NVIDIA Parakeet TDT 0.6B v3 (FluidAudio)
Neural Engine
M4 Pro
156×

NVIDIA Parakeet TDT 0.6B v3 (FluidAudio)
Neural Engine
M5 Pro
335×

Phonon-2, a Parakeet v3 fine-tune (FluidAudio)
Neural Engine
M5 Pro
480×

× real time: seconds of audio per second of processing. Rows 1–2: our tests on the same base M3 MacBook Air.
 Rows 3–5:FluidAudio's published benchmarkson larger, newer Macs and different audio. A rough guide, not a like-for-like ranking.

## Where it stands

Its word error rate is about 5% right now, against 2–3% for leading speech models. We believe a better-trained
 reader can close that gap; that's the next iteration.

## Use it

Drop in an audio file, or hold Right Option, speak and release to dictate into any app. It runs on the Mac's
 Neural Engine; your audio never leaves the machine.

Download for Mac (free)