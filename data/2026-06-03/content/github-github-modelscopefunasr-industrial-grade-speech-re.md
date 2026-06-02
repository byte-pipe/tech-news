---
title: 'GitHub - modelscope/FunASR: Industrial-grade speech recognition toolkit: 170x realtime, 50+ languages, speaker diarization, emotion detection, streaming, and OpenAI-compatible API. · GitHub'
url: https://github.com/modelscope/FunASR
site_name: github
content_file: github-github-modelscopefunasr-industrial-grade-speech-re
fetched_at: '2026-06-03T01:51:18.448775'
original_url: https://github.com/modelscope/FunASR
author: modelscope
description: 'Industrial-grade speech recognition toolkit: 170x realtime, 50+ languages, speaker diarization, emotion detection, streaming, and OpenAI-compatible API. - modelscope/FunASR'
---

modelscope

 

/

FunASR

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.7k
* Star16.9k

 
 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

5,069 Commits
5,069 Commits
.github
.github
 
 
benchmarks
benchmarks
 
 
data/
list
data/
list
 
 
docs
docs
 
 
examples
examples
 
 
fun_text_processing
fun_text_processing
 
 
funasr
funasr
 
 
gh-pages-output
gh-pages-output
 
 
model_zoo
model_zoo
 
 
runtime
runtime
 
 
scripts
scripts
 
 
tests
tests
 
 
tests_models
tests_models
 
 
web-pages
web-pages
 
 
.gitignore
.gitignore
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
Acknowledge.md
Acknowledge.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Contribution.md
Contribution.md
 
 
LICENSE
LICENSE
 
 
MODEL_LICENSE
MODEL_LICENSE
 
 
MinMo_gitlab
MinMo_gitlab
 
 
README.md
README.md
 
 
README_ja.md
README_ja.md
 
 
README_ko.md
README_ko.md
 
 
README_zh.md
README_zh.md
 
 
SECURITY.md
SECURITY.md
 
 
benchmark_vllm.py
benchmark_vllm.py
 
 
pyproject.toml
pyproject.toml
 
 
setup.py
setup.py
 
 
training.html
training.html
 
 
View all files

## Repository files navigation

(简体中文|English|日本語|한국어)

Industrial speech recognition. 170x faster than Whisper. 50+ languages.Speaker diarization · Emotion detection · Streaming · One API call

Quick Start·Colab·Benchmark·Model selection·Migration guide·Use cases·Deployment matrix·Models·Agent Integration·Docs·Contribute

## Quick Start

No local setup? Open theColab quickstartto transcribe a public sample or upload your own audio in a browser.

pip install torch torchaudio
pip install funasr

from
 
funasr
 
import
 
AutoModel

model
 
=
 
AutoModel
(
model
=
"iic/SenseVoiceSmall"
, 
vad_model
=
"fsmn-vad"
, 
spk_model
=
"cam++"
, 
device
=
"cuda"
)

result
 
=
 
model
.
generate
(
input
=
"meeting.wav"
)

Output— structured text with speaker labels, timestamps, and punctuation:

[00:00.4 → 00:03.8] Speaker 0: Let's discuss the Q3 plan.
[00:04.2 → 00:07.1] Speaker 1: Sounds good. I have three points.
[00:07.5 → 00:12.3] Speaker 0: Go ahead. We have 30 minutes.

That's it.One model, one call— VAD segmentation, speech recognition, punctuation, speaker diarization all happen automatically.

### LLM-powered ASR: Fun-ASR-Nano

For highest accuracy across 31 languages (including Chinese dialects), useFun-ASR-Nano— an LLM-based ASR combining SenseVoice encoder with Qwen3-0.6B decoder:

from
 
funasr
 
import
 
AutoModel

model
 
=
 
AutoModel
(
model
=
"FunAudioLLM/Fun-ASR-Nano-2512"
, 
vad_model
=
"fsmn-vad"
, 
device
=
"cuda"
)

result
 
=
 
model
.
generate
(
input
=
"meeting.wav"
)

With vLLM acceleration (16x faster, batch processing):

from
 
funasr
.
auto
.
auto_model_vllm
 
import
 
AutoModelVLLM

model
 
=
 
AutoModelVLLM
(
model
=
"FunAudioLLM/Fun-ASR-Nano-2512"
, 
tensor_parallel_size
=
1
)

results
 
=
 
model
.
generate
([
"audio1.wav"
, 
"audio2.wav"
], 
language
=
"auto"
)

Deploy as API server:funasr-server --device cuda→ OpenAI-compatible endpoint at localhost:8000

Use with AI agents:MCP Serverfor Claude/Cursor ·OpenAI APIfor LangChain/Dify/AutoGen

### Why FunASR?

FunASR

Whisper

Cloud APIs

Speed

170x realtime

13x realtime

~1x realtime

Speaker ID

✅ Built-in

❌ Needs pyannote

✅ Extra cost

Emotion

✅ Happy/Sad/Angry

❌

❌

Languages

50+

57

Varies

Streaming

✅ WebSocket

❌

✅

vLLM Acceleration

✅ 2-3x faster

❌

N/A

Self-hosted

✅ MIT license

✅ MIT license

❌ Cloud only

Cost

Free

Free

$0.006/min+

CPU viable

✅ 17x realtime

❌ Too slow

N/A

Trying FunASR for the first time? Use theColab quickstartbefore setting up a local environment. Choosing a first model? Start with themodel selection guide. Planning a switch from Whisper or a cloud ASR provider? Use themigration guideandbenchmark exampleto test representative audio, map features, and roll out safely.

## Benchmark

184 long-form audio files (192 min).Full report →

Model

GPU Speed

CPU Speed

vs Whisper-large-v3

SenseVoice-Small

170x
 realtime

17x
 realtime

🚀 
13x faster

Paraformer-Large

120x
 realtime

15x
 realtime

🚀 
9x faster

Whisper-large-v3-turbo

46x realtime

❌

3.4x faster

Fun-ASR-Nano

17x realtime

3.6x realtime

1.3x faster

Whisper-large-v3

13x realtime

❌

baseline

Key takeaway:FunASR models run on CPU faster than Whisper runs on GPU.

## What's new

* 2026/05/24:vLLM Inference Engine— 2-3x faster LLM decoding for Fun-ASR-Nano. Streaming WebSocket service with VAD + Speaker Diarization.Guide →
* 2026/05/24:Dynamic VAD— adaptive silence threshold (default on). Short sentences stay intact, long segments get auto-split.Details →
* 2026/05/24:v1.3.3—funasr-serverCLI, OpenAI-compatible API, MCP Server for AI agents.pip install --upgrade funasr
* 2026/05/20: Added Qwen3-ASR (0.6B/1.7B) — 52 languages, auto detection.usage
* 2026/05/20: Added GLM-ASR-Nano (1.5B) — 17 languages, dialect support.usage
* 2026/05/19: Fun-ASR-Nano and SenseVoice now support speaker diarization.
* 2025/12/15:Fun-ASR-Nano-2512— 31 languages, tens of millions of hours training.

Older

* 2024/10/10: Whisper-large-v3-turbo support added.
* 2024/07/04:SenseVoice— ASR + emotion + audio events.
* 2024/01/30: FunASR 1.0 released.

## Installation

pip install funasr

From source / Requirements

git clone https://github.com/modelscope/FunASR.git 
&&
 
cd
 FunASR
pip install -e ./

Requirements: Python ≥ 3.8. Install PyTorch + torchaudio first (pytorch.org), thenpip install funasr.

## Model Zoo

Model

Task

Languages

Params

Links

Fun-ASR-Nano

ASR + timestamps

31 languages

800M

⭐
 
🤗

SenseVoiceSmall

ASR + emotion + events

zh/en/ja/ko/yue

234M

⭐
 
🤗

Paraformer-zh

ASR + timestamps

zh/en

220M

⭐
 
🤗

Paraformer-zh-streaming

Streaming ASR

zh/en

220M

⭐
 
🤗

Qwen3-ASR

ASR, 52 languages

multilingual

1.7B

usage

GLM-ASR-Nano

ASR, 17 languages

multilingual

1.5B

usage

Whisper-large-v3

ASR + translation

multilingual

1550M

usage

Whisper-large-v3-turbo

ASR + translation

multilingual

809M

usage

ct-punc

Punctuation

zh/en

290M

⭐
 
🤗

fsmn-vad

VAD

zh/en

0.4M

⭐
 
🤗

cam++

Speaker diarization

—

7.2M

⭐
 
🤗

emotion2vec+large

Emotion recognition

—

300M

⭐
 
🤗

## Usage

Full examples with parameter docs:Tutorial →

from
 
funasr
 
import
 
AutoModel

# Chinese production (VAD + ASR + punctuation + speaker)

model
 
=
 
AutoModel
(
model
=
"paraformer-zh"
, 
vad_model
=
"fsmn-vad"
, 
punc_model
=
"ct-punc"
, 
spk_model
=
"cam++"
, 
device
=
"cuda"
)

result
 
=
 
model
.
generate
(
input
=
"meeting.wav"
, 
hotword
=
"关键词 20"
)

# 31 languages with timestamps

model
 
=
 
AutoModel
(
model
=
"FunAudioLLM/Fun-ASR-Nano-2512"
, 
hub
=
"hf"
, 
trust_remote_code
=
True
,
 
vad_model
=
"fsmn-vad"
, 
vad_kwargs
=
{
"max_single_segment_time"
: 
30000
}, 
device
=
"cuda"
)

result
 
=
 
model
.
generate
(
input
=
"audio.wav"
, 
batch_size
=
1
)

# Streaming real-time

model
 
=
 
AutoModel
(
model
=
"paraformer-zh-streaming"
, 
device
=
"cuda"
)

result
 
=
 
model
.
generate
(
input
=
"chunk.wav"
, 
cache
=
{}, 
chunk_size
=
[
0
, 
10
, 
5
])

# Emotion recognition

model
 
=
 
AutoModel
(
model
=
"emotion2vec_plus_large"
, 
device
=
"cuda"
)

result
 
=
 
model
.
generate
(
input
=
"audio.wav"
, 
granularity
=
"utterance"
)

## Deploy

#
 OpenAI-compatible API (recommended)

pip install torch torchaudio
pip install funasr vllm fastapi uvicorn python-multipart
funasr-server --device cuda

#
 → POST /v1/audio/transcriptions at localhost:8000

Verify it with a public sample:

curl -L https://isv-data.oss-cn-hangzhou.aliyuncs.com/ics/MaaS/ASR/test_audio/BAC009S0764W0121.wav -o sample.wav
curl http://localhost:8000/v1/audio/transcriptions \
 -F file=@sample.wav \
 -F model=sensevoice \
 -F response_format=verbose_json

#
 Docker streaming service

docker pull registry.cn-hangzhou.aliyuncs.com/funasr_repo/funasr:funasr-runtime-sdk-online-cpu-0.1.12

OpenAI API example →·Gradio demo →·Client recipes →·JavaScript/TypeScript recipes →·Kubernetes template →·Workflow recipes →·Postman collection →·OpenAPI spec →·Security guide →·Deployment matrix →·Deployment docs →·Agent integration →

## Community

📖 
Documentation

🐛 
Issues

💬 
Discussions

🤗 
HuggingFace

🤝 
Contributing

📈 
20k growth plan

## Star History

## License

MIT License

## Citations

@inproceedings
{
gao2023funasr
,
 
author
=
{
Zhifu Gao and others
}
,
 
title
=
{
FunASR: A Fundamental End-to-End Speech Recognition Toolkit
}
,
 
booktitle
=
{
INTERSPEECH
}
,
 
year
=
{
2023
}

}

## About

Industrial-grade speech recognition toolkit: 170x realtime, 50+ languages, speaker diarization, emotion detection, streaming, and OpenAI-compatible API.

modelscope.github.io/FunASR

### Topics

 audio

 real-time

 pytorch

 speech-recognition

 chinese

 vad

 speech-to-text

 punctuation

 transcription

 asr

 speaker-diarization

 emotion-recognition

 voice-activity-detection

 streaming-asr

 paraformer

 vllm

 openai-compatible-api

 mcp-server

 multilingual-asr

 whisper-alternative

### Resources

 Readme

 

### License

 MIT license
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

16.9k

 stars
 

### Watchers

110

 watching
 

### Forks

1.7k

 forks
 

 Report repository

 

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Used by1.4k

 + 1,358
 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python62.4%
* HTML17.5%
* C++10.3%
* Shell2.7%
* JavaScript2.7%
* C#2.2%
* Other2.2%