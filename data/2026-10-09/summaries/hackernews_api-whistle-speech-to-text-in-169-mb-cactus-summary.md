---
title: Whistle: Speech to Text in 16.9 MB | Cactus
url: https://cactuscompute.com/blog/whistle
date: 2026-10-09
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-10-09T10:17:10.162950
---

# Whistle: Speech to Text in 16.9 MB | Cactus

# Whistle: Speech to Text in 16.9 MB

## Overview
- Open‑source speech recognition model designed for mobiles, wearables, robots, smart‑home devices, automotive and micro‑controllers.  
- Single 16.9 MB file, runs on CPU with no external dependencies.  
- Loads into the same C++ engine and quantisation as the Needle model, enabling one binary to handle both speech and text tasks.  
- Supports seven languages (English, German, French, Spanish, Italian, Dutch, Polish) with automatic language detection.  
- Processes up to 30 seconds of 16 kHz mono audio per clip; audio never leaves the device.

## Capabilities
- **Transcription** – produces a text transcript from raw audio.  
- **Word timestamps** – returns start/end time and probability for each word, derived from decoder attention.  
- **Speech embedding** – outputs encoder representations (one row per 80 ms frame) without decoding.

## Architecture
- **Front‑end**: 16 kHz mono audio → 80‑bin log‑mel spectrogram (25 ms window, 10 ms hop, 250‑3500 Hz), normalized per channel → 3 000 frames for 30 s.  
- **Encoder**:  
  - Convolutional stem (128 channels, kernel 9) with three halvings → 375 frames (one per 80 ms).  
  - Eight Simple Attention blocks shared with Needle (self‑attention over all frames, 4 mHC lanes, Monarch Hadamard MLP).  
- **Decoder**:  
  - Cross‑memory projection of K and V once per clip (375 frames × 8 layers).  
  - Eight Laddered Simple Attention blocks (width 512, 8 query heads, 2 KV heads, 48‑dim queries/keys, 64‑dim values, 3‑tap causal conv, engram lookups at layers 3 & 7).  
  - Gated cross‑attention per layer: `x ← x + σ(g)·softmax(q̂K̂ᵀ/√d)V`.  
  - Beam search with 5 beams, length‑normalised log probability, keyword bias via Aho‑Corasick automaton.  
  - Vocabulary: 8 192 subword tokens + 7 language tokens; transcript limited to 320 tokens.  
- **Silence handling**: clips below a loudness threshold return empty transcript and language without invoking beam search.

## Benchmarks (relative to Whisper base and Moonshine tiny v2)

| Metric | Whistle | Whisper base | Moonshine tiny v2 |
|--------|---------|--------------|-------------------|
| Model size (MB) | 16.9 | 145.3 | 41.9 |
| Time to first token (ms) | 11.1 | 73.2 | 22.8 |
| Decode speed (tokens / s) | 1 319 | 266 | 262 |
| Word error rate (selected sets) | Best on LibriSpeech test‑clean & test‑other, SPGISpeech, Earnings‑22, FLEURS avg. | Best on TED‑LIUM, AMI, MLS avg. | English‑only, limited reporting |

- Benchmarks run on an Apple M4 Pro CPU, using each model’s official runtime and default settings.  
- Whistle processes the clip length‑dependently (e.g., 5 s → 5.9 ms to first token, 30 s → 36.3 ms).  
- All test audio is unseen during training; verification performed via audio checksums and speaker IDs.

## One Engine, Multiple Loading Modes
- The same `needle` binary can load a text model, a speech model, or both:

```
needle --model whistle.cact --audio clip.wav
needle --model needle3.cact --tools tools.json --prompt "turn off the kitchen lights"
needle --model needle3.cact --model whistle.cact --tools tools.json --audio clip.wav
```

- In the third form, `needle_complete` returns a JSON object containing:
  - `function_calls` with detected tool invocations,
  - `confidence`,
  - `audio_text` (transcript),
  - `audio_language`.

## Getting Started
- Install the base package:

```
pip install cactus-needle
```

- Basic transcription example:

```python
import needle
result = needle.transcribe("clip.wav")
print(result["text"])
# turn off the kitchen lights
```

- Optional extras (`[mic]`) add `soxr` and `sounddevice` for other sample rates and live microphone capture.  
- Additional arguments:
  - `word_timestamps=True` → include timestamps and probabilities per word.  
  - `keywords=["Siobhan", "Krzysztof"]` → boost log‑probability of specified phrases.  
  - `language="de"` → force German detection.  
  - `needle.Whistle()` creates a reusable model object for embedding or tuned `.cact` files.