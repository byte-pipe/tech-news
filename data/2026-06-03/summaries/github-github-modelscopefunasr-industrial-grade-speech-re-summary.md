---
title: GitHub - modelscope/FunASR: Industrial-grade speech recognition toolkit: 170x realtime, 50+ languages, speaker diarization, emotion detection, streami...
url: https://github.com/modelscope/FunASR
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-06-03T01:52:41.639026
---

# GitHub - modelscope/FunASR: Industrial-grade speech recognition toolkit: 170x realtime, 50+ languages, speaker diarization, emotion detection, streami...

# FunASR – Industrial‑grade Speech Recognition Toolkit

## Overview
- Open‑source speech recognition framework by ModelScope, supporting 50+ languages.
- Provides VAD, ASR, punctuation, speaker diarization, emotion detection, streaming, and OpenAI‑compatible API in a single call.
- Claims up to 170× realtime speed (CPU) and 13× realtime on GPU, far faster than Whisper.

## Quick Start
- Install: `pip install torch torchaudio funasr`
- Example usage with `AutoModel`:
  ```python
  from funasr import AutoModel
  model = AutoModel(model="iic/SenseVoiceSmall",
                    vad_model="fsmn-vad",
                    spk_model="cam++",
                    device="cuda")
  result = model.generate(input="meeting.wav")
  ```
- Output includes timestamps, speaker labels, and punctuation.

## LLM‑Powered ASR – Fun‑ASR‑Nano
- Combines SenseVoice encoder with Qwen3‑0.6B decoder for high accuracy across 31 languages.
- Supports vLLM acceleration (≈16× faster) and batch processing.
- Deployable as an OpenAI‑compatible server: `funasr-server --device cuda`.

## Feature Comparison (FunASR vs Whisper vs Cloud APIs)
| Feature | FunASR | Whisper | Cloud APIs |
|---|---|---|---|
| Speed (GPU) | 170× realtime | 13× realtime | ~1× realtime |
| Speaker ID | Built‑in | External (pyannote) | Extra cost |
| Emotion detection | Yes | No | No |
| Languages | 50+ | 57 (varies) | Varies |
| Streaming | WebSocket | No | Yes |
| vLLM acceleration | 2–3× faster | N/A | N/A |
| License | MIT (self‑hosted) | MIT | Paid |
| Cost | Free | Free | $0.006/min+ |
| CPU viability | 17× realtime | Too slow | N/A |

## Benchmarks
- Tested on 184 long‑form audio files (192 min).
- Top models:
  - **SenseVoice‑Small**: 170× realtime on GPU, 17× realtime on CPU (13× faster than Whisper‑large‑v3).
  - **Paraformer‑Large**: 120× realtime GPU, 15× realtime CPU.
  - **Fun‑ASR‑Nano**: 17× realtime GPU, 3.6× realtime CPU (1.3× faster than Whisper‑large‑v3).

## Recent Updates (2026)
- vLLM inference engine for Fun‑ASR‑Nano (2–3× faster decoding) and streaming WebSocket service.
- Dynamic VAD with adaptive silence threshold.
- `funasr-server` CLI, OpenAI‑compatible API, MCP Server for AI agents.
- New models: Qwen3‑ASR (0.6B/1.7B, 52 languages) and GLM‑ASR‑Nano (1.5B, 17 languages).
- Speaker diarization added to Fun‑ASR‑Nano and SenseVoice.

## Installation
```bash
pip install funasr
# or from source
git clone https://github.com/modelscope/FunASR.git
cd FunASR
pip install -e .
```
Requires Python ≥ 3.8 and PyTorch + torchaudio.

## Model Zoo (selected)
- **Fun‑ASR‑Nano**: ASR + timestamps, 31 languages, 800 M params.
- **SenseVoiceSmall**: ASR + emotion + events, zh/en/ja/ko/yue, 234 M params.
- **Paraformer‑zh** / **Paraformer‑zh‑streaming**: ASR + timestamps, zh/en, 220 M params.
- **Qwen3‑ASR**: 52 languages, 1.7 B params.
- **GLM‑ASR‑Nano**: 17 languages, 1.5 B params.
- Supporting models: `fsmn-vad` (VAD), `cam++` (speaker diarization), `ct-punc` (punctuation), `emotion2vec+large` (emotion recognition).

## Usage Examples
- **Full pipeline (VAD + ASR + punctuation + speaker)**:
  ```python
  model = AutoModel(model="paraformer-zh",
                    vad_model="fsmn-vad",
                    punc_model="ct-punc",
                    spk_model="cam++",
                    device="cuda")
  result = model.generate(input="meeting.wav", hotword="关键词 20")
  ```
- **Multilingual with timestamps**:
  ```python
  model = AutoModel(model="FunAudioLLM/Fun-ASR-Nano-2512",
                    hub="hf",
                    trust_remote_code=True,
                    vad_model="fsmn-vad",
                    device="cuda")
  result = model.generate(input="audio.wav")
  ```
- **Streaming real‑time**:
  ```python
  model = AutoModel(model="paraformer-zh-streaming", device="cuda")
  result = model.generate(input="chunk.wav", cache={}, chunk_size=[0,10,5])
  ```
- **Emotion recognition**:
  ```python
  model = AutoModel(model="emotion2vec_plus_large", device="cuda")
  result = model.generate(input="audio.wav", granularity="utterance")
  ```

## Deployment
- **OpenAI‑compatible API**:
  ```bash
  pip install torch torchaudio funasr vllm fastapi uvicorn python-multipart
  funasr-server --device cuda
  ```
  POST `/v1/audio/transcriptions` to `http://localhost:8000`.
- **Docker streaming service**:
  ```bash
  docker pull registry.cn-hangzhou.aliyuncs.com/funasr_repo/funasr:funasr-runtime-sdk-online-cpu-0.1.12
  ```

## Resources
- Colab quickstart for zero‑setup transcription.
- Model selection guide, migration guide, benchmark scripts, and extensive documentation in the `docs/` folder.