---
title: Embedding Gemma Transcribe
url: https://eg2.haku.sh/
date: 2026-10-13
site: hnrss
model: llama3.2:1b
summarized_at: 2026-10-13T18:03:02.304116
---

# Embedding Gemma Transcribe

# Embedding Gemma Transcribe

Gemma Transcribe is an embedding model that converts speech into text. It can transcribe one hour of audio in approximately 13 seconds on a base MacBook Air with Apple Silicon.

## Key Points

- Text, images, audio, and video can be shared in one space.
- A small reader extracts audio slices and moves them into the model's text space.
- The model wins by pronouncing the most similar words.
- The reader is trained for a limited time with English speech (2 hours on 8 cores) on openly licensed speech.

## Speed Performance

- IBM Granite Speech 5.0 TurboCTC (GPU): ~150x faster than Gemma Transcribe
- NVIDIA Parakeet TDT 0.6B v3 (FluidAudio): ~335x faster than Gemma Transcribe
- NVIDIA Parakeet TDT 0.6B v3 (FluidAudio) is fine-tuned using Phonon-2
- The benchmark speed is a rough guide, not a like-for-like ranking

## Advantages and Limitations

Advantages:
- Fast speed
- Can handle English text as well as speech

Limitations:
- Limited training time and data
- Requires a Mac with an Apple Silicon processor

## How to Use

1. Download the Gemma Transcribe app for Mac
2. Drag an audio file into the app or hold the Right Option key
3. Speak or dictate into the app to convert audio to text
4. The text is returned to you, and the audio is sent home unchanged