---
title: 'GitHub - OpenMOSS/MOSS-TTS: MOSS‑TTS Family is an open‑source speech and sound generation model family from MOSI.AI and the OpenMOSS team. It is designed for high‑fidelity, high‑expressiveness, and complex real‑world scenarios, covering stable long‑form speech, multi‑speaker dialogue, voice/character design, environmental sound effects, and real‑time streaming TTS. · GitHub'
url: https://github.com/OpenMOSS/MOSS-TTS
site_name: github
content_file: github-github-openmossmoss-tts-mosstts-family-is-an-opens
fetched_at: '2026-05-28T12:11:34.395937'
original_url: https://github.com/OpenMOSS/MOSS-TTS
author: OpenMOSS
description: MOSS‑TTS Family is an open‑source speech and sound generation model family from MOSI.AI and the OpenMOSS team. It is designed for high‑fidelity, high‑expressiveness, and complex real‑world scenarios, covering stable long‑form speech, multi‑speaker dialogue, voice/character design, environmental sound effects, and real‑time streaming TTS. - OpenMOSS/MOSS-TTS
---

OpenMOSS

 

/

MOSS-TTS

Public

* NotificationsYou must be signed in to change notification settings
* Fork202
* Star2k

 
 
 
 
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

60 Commits
60 Commits
assets
assets
 
 
clis
clis
 
 
community/
norwegian-lora
community/
norwegian-lora
 
 
configs/
llama_cpp
configs/
llama_cpp
 
 
docs
docs
 
 
moss_audio_tokenizer @ 56776e8
moss_audio_tokenizer @ 56776e8
 
 
moss_soundeffect_v2
moss_soundeffect_v2
 
 
moss_tts_delay
moss_tts_delay
 
 
moss_tts_local
moss_tts_local
 
 
moss_tts_realtime
moss_tts_realtime
 
 
scripts
scripts
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
LICENSE
LICENSE
 
 
MANIFEST.in
MANIFEST.in
 
 
README.md
README.md
 
 
README_zh.md
README_zh.md
 
 
pyproject.toml
pyproject.toml
 
 
View all files

## Repository files navigation

# MOSS-TTS Family

     
 

English|简体中文

MOSS‑TTS Family is an open‑sourcespeech and sound generation model familyfromMOSI.AIand theOpenMOSS team. It is designed forhigh‑fidelity,high‑expressiveness, andcomplex real‑world scenarios, covering stable long‑form speech, multi‑speaker dialogue, voice/character design, environmental sound effects, and real‑time streaming TTS.

## News

* 2026.5.26: 🚀 ReleasedMOSS-SoundEffect-v2.0, a new text-to-audio model using aDiT backbone with the Flow Matching objective, generating48 kHzbilingual sound effects up to30 seconds— seemoss_soundeffect_v2/.
* 2026.5.26: 🚀 ReleasedMOSS-TTS-v1.5, with stronger multilingual synthesis when language tags are provided, more stable voice cloning, better long-reference short-text cloning, punctuation-following prosody, and explicit pause control via[pause X.Ys].
* 2026.5.6: 🚀 MOSS-TTS and MOSS-Audio-Tokenizer now supportmlx-audio. Visit themlx-audio GitHub repositoryfor details.
* 2026.4.29: 📝 MOSS-TTS 2.0 is coming soon! We are collecting TTS feedback, suggestions, and feature requests via therequirements collection form.
* 2026.4.13: 🚀 MOSS-TTS-Nano, our ~100M-parameter model, is now available! It supports multilingual voice cloning, 48 kHz stereo input/output, and streaming output on just 4 CPU cores. Check theGitHub repositoryand ourblogfor more details.
* 2026.3.31: 📄 Our technical reports forMOSS-TTSDandMOSS-VoiceGeneratorare now available on arXiv!
* 2026.3.26: 📘 Added a tutorial on fine-tuning the MOSS-TTS-Realtime!
* 2026.3.20: 📄 Ourtechnical reportis now available on arXiv!
* 2026.3.18: 🚀 Added a first-class MOSS-TTSllama.cppimplementation in the companion repositoryOpenMOSS/llama.cpp, including end-to-end docs and a runnable pipeline for GGUF backbone inference plus ONNX audio codec decoding. See thefirst-class e2e guide.
* 2026.3.16: 📘 Added a tutorial on fine-tuning the MossTTSLocal architecture, suitable for MOSS-TTS-Local-Transformer!
* 2026.3.12: 🚀 Added SGLang backend support for theMossTTSDelayarchitecture, enabling efficient inference for MOSS-TTS (Delay) and MOSS-SoundEffect, with around3× fastergeneration throughput!
* 2026.3.11: 📘 Added a tutorial on fine-tuning the MossTTSDelay architecture, suitable for MOSS-TTS(Delay), MOSS-TTSD, MOSS-VoiceGenerator, and MOSS-SoundEffect!
* 2026.3.10: ⚡️ Significantly optimized the VRAM usage of llama.cpp inference pipeline. Now 8B model fits onto 8GB GPUs!
* 2026.3.4: 🚀 AddedPyTorch-free inference support— enabling lightweight on-device deployment viallama.cpp + ONNX Runtime. QuantizedGGUF weightsare released atOpenMOSS-Team/MOSS-TTS-GGUF, and theONNX audio tokenizeris available atOpenMOSS-Team/MOSS-Audio-Tokenizer-ONNX. See thellama.cpp backendfor details.
* 2026.3.4: 🎉 We add MOSS-TTS skills inClawHubof 🦞 OpenClaw:feishu-voice-ttsandmoss-tts-voice.
* 2026.2.10: 🎉🎉🎉 We have releasedMOSS-TTS Family. Check ourBlogfor more details! OurHuggingface Spaceis here:MOSS-TTS,MOSS-TTSD-v1.0,MOSS-VoiceGenerator.

## Demo

tts_promotional_video.mp4

## Contents

* MOSS-TTS FamilyNewsDemoContentsIntroductionModel ArchitectureReleased ModelsSupported LanguagesMOSS-TTS-v1.5QuickstartOpenClaw API SkillsEnvironment SetupUsing CondaUsinguv(Optional) Install FlashAttention 2MOSS‑TTS Basic UsageFine-Tuningllama.cpp Backend (Torch-Free Inference)Quick StartInstallation ProfilesModel WeightsConfigurationSGLang Backend (Accelerated Inference)Quick StartRequest and ResponseMOSS-TTS (Delay)MOSS-SoundEffectResponseEvaluationMOSS‑TTSMOSS‑TTSDObjective EvaluationSubjective EvaluationMOSS‑VoiceGeneratorMOSS‑TTS-RealtimeMOSS-TTS-NanoIntroductionModel WeightsMOSS-Audio-TokenizerIntroductionModel WeightsObjective Reconstruction Evaluation📚 More Information🌟 Community ProjectsLICENSECitationStar History
* News
* Demo
* Contents
* Introduction
* Model Architecture
* Released Models
* Supported Languages
* MOSS-TTS-v1.5
* QuickstartOpenClaw API SkillsEnvironment SetupUsing CondaUsinguv(Optional) Install FlashAttention 2MOSS‑TTS Basic Usage
* OpenClaw API Skills
* Environment SetupUsing CondaUsinguv(Optional) Install FlashAttention 2
* Using Conda
* Usinguv
* (Optional) Install FlashAttention 2
* MOSS‑TTS Basic Usage
* Fine-Tuning
* llama.cpp Backend (Torch-Free Inference)Quick StartInstallation ProfilesModel WeightsConfiguration
* Quick Start
* Installation Profiles
* Model Weights
* Configuration
* SGLang Backend (Accelerated Inference)Quick StartRequest and ResponseMOSS-TTS (Delay)MOSS-SoundEffectResponse
* Quick Start
* Request and ResponseMOSS-TTS (Delay)MOSS-SoundEffectResponse
* MOSS-TTS (Delay)
* MOSS-SoundEffect
* Response
* EvaluationMOSS‑TTSMOSS‑TTSDObjective EvaluationSubjective EvaluationMOSS‑VoiceGeneratorMOSS‑TTS-Realtime
* MOSS‑TTS
* MOSS‑TTSDObjective EvaluationSubjective Evaluation
* Objective Evaluation
* Subjective Evaluation
* MOSS‑VoiceGenerator
* MOSS‑TTS-Realtime
* MOSS-TTS-NanoIntroductionModel Weights
* Introduction
* Model Weights
* MOSS-Audio-TokenizerIntroductionModel WeightsObjective Reconstruction Evaluation
* Introduction
* Model Weights
* Objective Reconstruction Evaluation
* 📚 More Information🌟 Community Projects
* 🌟 Community Projects
* LICENSE
* Citation
* Star History

## Introduction

When a single piece of audio needs tosound like a real person,pronounce every word accurately,switch speaking styles across content,remain stable over tens of minutes, andsupport dialogue, role‑play, and real‑time interaction, a single TTS model is often not enough. TheMOSS‑TTS Familybreaks the workflow into five production‑ready models that can be used independently or composed into a complete pipeline.

* MOSS‑TTS: The flagship production model featuring high fidelity and optimal zero-shot voice cloning. It supportslong-speech generation,fine-grained control over Pinyin, phonemes, and duration, as well asmultilingual/code-switched synthesis.
* MOSS‑TTSD: A spoken dialogue generation model for expressive, multi-speaker, and ultra-long dialogues. The newv1.0 versionachievesindustry-leading performance on objective metricsandoutperformed top closed-source models like Doubao and Gemini 2.5-proin subjective evaluations. You can visit theMOSS-TTSD repositoryfor details.
* MOSS‑VoiceGenerator: An open-source voice design model capable of generating diverse voices and styles directly from text prompts,without any reference speech. It unifies voice design, style control, and synthesis, functioning independently or as a design layer for downstream TTS. Its performancesurpasses other top-tier voice design models in arena ratings.
* MOSS‑TTS‑Realtime: A multi-turn context-aware model for real-time voice agents. It uses incremental synthesis to ensure natural and coherent replies, making itideal for building low-latency voice agents when paired with text models. The TTFB (Time To First Byte) of MOSS-TTS-Realtime reaches 180 ms, and the$T_{\text{LLM-first-sentence}} + T_{\text{MOSS-TTS-Realtime-TTFB}}$is 377 ms.
* MOSS‑SoundEffect: A content creation model specialized insound effect generationwith wide category coverage and controllable duration. It generates audio for natural environments, urban scenes, biological sounds, human actions, and musical fragments, suitable for film, games, and interactive experiences.

## Model Architecture

We trainMossTTSDelayandMossTTSLocalas complementary baselines under one training/evaluation setup:Delayemphasizes long-context stability, inference speed, and production readiness, whileLocalemphasizes lightweight flexibility and strong objective performance for streaming-oriented systems. Together they provide reproducible references for deployment and research.

MossTTSRealtimeis not a third comparison baseline; it is a capability-driven design for voice agents. By modeling multi-turn context from both prior text and user acoustics, it delivers low-latency streaming speech that stays coherent and voice-consistent across turns.

Architecture

Core Mechanism

Arch Details

MossTTSDelay

Multi‑head parallel RVQ prediction with delay‑pattern scheduling

MossTTSLocal

Time‑synchronous RVQ blocks with a depth transformer

MossTTSRealtime

Hierarchical text–audio inputs for realtime synthesis

## Released Models

Model

Architecture

Size

Model Card

Hugging Face

ModelScope

MOSS-TTS-v1.5

MossTTSDelay

8B

MOSS-TTS 1.0

MossTTSDelay

8B

MOSS-TTS-Local-Transformer

MossTTSLocal

1.7B

MOSS‑TTSD‑V1.0

MossTTSDelay

8B

MOSS‑VoiceGenerator

MossTTSDelay

1.7B

MOSS‑SoundEffect

MossTTSDelay

8B

MOSS‑SoundEffect‑v2.0

MossSoundEffectPipeline

1.3B DiT

MOSS‑TTS‑Realtime

MossTTSRealtime

1.7B

## Supported Languages

MOSS-TTS-v1.5 currently supports31 languages. It keeps the 20 languages supported byMOSS-TTS 1.0and extends multilingual continued training to Cantonese, Dutch, Finnish, Hindi, Macedonian, Malay, Romanian, Swahili, Tagalog, Thai, and Vietnamese.

MOSS-TTSD and MOSS-TTS-Realtime follow their own model cards for supported language coverage.

Language

Code

Flag

Language

Code

Flag

Language

Code

Flag

Chinese

zh

🇨🇳

Cantonese

yue

🇭🇰

English

en

🇺🇸

Arabic

ar

🇸🇦

Czech

cs

🇨🇿

Danish

da

🇩🇰

Dutch

nl

🇳🇱

Finnish

fi

🇫🇮

French

fr

🇫🇷

German

de

🇩🇪

Greek

el

🇬🇷

Hebrew

he

🇮🇱

Hindi

hi

🇮🇳

Hungarian

hu

🇭🇺

Italian

it

🇮🇹

Japanese

ja

🇯🇵

Korean

ko

🇰🇷

Macedonian

mk

🇲🇰

Malay

ms

🇲🇾

Persian (Farsi)

fa

🇮🇷

Polish

pl

🇵🇱

Portuguese

pt

🇵🇹

Romanian

ro

🇷🇴

Russian

ru

🇷🇺

Spanish

es

🇪🇸

Swahili

sw

🇹🇿

Swedish

sv

🇸🇪

Tagalog

tl

🇵🇭

Thai

th

🇹🇭

Turkish

tr

🇹🇷

Vietnamese

vi

🇻🇳

## MOSS-TTS-v1.5

MOSS-TTS-v1.5is continued fromMOSS-TTS 1.0. It preserves the main 1.0 capabilities, including zero-shot voice cloning, long-form speech generation, token-level duration control, Pinyin/IPA pronunciation control, multilingual synthesis, and code-switching.

Compared with MOSS-TTS 1.0, v1.5 focuses on these improvements:

* Stronger multilingual synthesis with language tags: when the language is known, set it inprocessor.build_user_message(text=text, language="French")or the equivalent API field.
* More stable voice cloning: v1.5 improves speaker similarity and reduces cloning variance across repeated generations.
* Better long-reference, short-text cloning: v1.5 handles reference audio that is much longer than the target text more reliably.
* More stable punctuation-following prosody: v1.5 follows punctuation-driven pauses more closely, especially in long sentences.
* Explicit pause control: use inline pause markers such as[pause 3.2s], for example我今天学习了一首中国的古诗，它的名字是[pause 3.2s]静夜思！.

## Quickstart

### OpenClaw API Skills

We add MOSS-TTS skills inClawHubof 🦞 OpenClaw. You can get your API key fromMOSI AI Studio.

Skill

Description

Install

feishu-voice-tts

Send voice messages in Feishu

clawhub install feishu-voice-tts

moss-tts-voice

Call MOSS-TTS API to generate speech

clawhub install moss-tts-voice

### Environment Setup

We recommend a clean, isolated Python environment withTransformers 5.0.0to avoid dependency conflicts.

#### Using Conda

conda create -n moss-tts python=3.12 -y
conda activate moss-tts

Install all required dependencies:

git clone https://github.com/OpenMOSS/MOSS-TTS.git

cd
 MOSS-TTS
pip install --extra-index-url https://download.pytorch.org/whl/cu128 -e 
"
.[torch-runtime]
"

#### Usinguv

#
 Install uv first: https://docs.astral.sh/uv/getting-started/installation/

git clone https://github.com/OpenMOSS/MOSS-TTS.git

cd
 MOSS-TTS
uv venv --python 3.12 .venv

source
 .venv/bin/activate
uv pip install --torch-backend cu128 -e 
"
.[torch-runtime]
"

#### (Optional) Install FlashAttention 2

For better speed and lower GPU memory usage, you can install FlashAttention 2 if your hardware supports it.

If you use Conda/pip:

pip install --extra-index-url https://download.pytorch.org/whl/cu128 -e 
"
.[torch-runtime,flash-attn]
"

If your machine has limited RAM and many CPU cores, you can cap build parallelism:

MAX_JOBS=4 pip install --extra-index-url https://download.pytorch.org/whl/cu128 -e 
"
.[torch-runtime,flash-attn]
"

If you useuv:

uv pip install --torch-backend cu128 -e 
"
.[torch-runtime,flash-attn]
"

If your machine has limited RAM and many CPU cores, you can cap build parallelism:

MAX_JOBS=4 uv pip install --torch-backend cu128 -e 
"
.[torch-runtime,flash-attn]
"

Notes:

* Dependencies are managed inpyproject.toml, which currently pinstorch==2.9.1+cu128andtorchaudio==2.9.1+cu128.
* Inuv,--torch-backend cu128lets uv fetch compatible PyTorch CUDA wheels and resolve the rest from PyPI with the default safe index strategy.
* If you need another backend, replacecu128with your target (for example,cpu,cu126).
* If FlashAttention 2 fails to build on your machine, you can skip it and use the default attention backend.
* FlashAttention 2 is only available on supported GPUs and is typically used withtorch.float16ortorch.bfloat16.

### MOSS‑TTS Basic Usage

If you prefer Gradio demos, we provide 4 scripts for the main models:

Model

Script

MOSS-TTS

clis/moss_tts_app.py

MOSS-TTSD

clis/moss_ttsd_app.py

MOSS-VoiceGenerator

clis/moss_voice_generator_app.py

MOSS-SoundEffect

clis/moss_sound_effect_app.py

For the MOSS-TTS-Realtime Gradio demo, please refer toMOSS-TTS-Realtime Model Card

Tip: MOSS-TTS-v1.5 uses the same generation API as the 1.0MossTTSDelay-8Bcheckpoint. For multilingual inputs, setlanguagewhenever the language is known.

MOSS-TTS provides a convenientgenerateinterface for rapid usage. The examples below cover:

1. Direct generation (Chinese / English / multilingual text with language tags / Pinyin / IPA)
2. Voice cloning
3. Duration control
4. Explicit pause control with[pause X.Ys]

from
 
pathlib
 
import
 
Path

import
 
importlib
.
util

import
 
torch

import
 
torchaudio

from
 
transformers
 
import
 
AutoModel
, 
AutoProcessor

# Disable the broken cuDNN SDPA backend

torch
.
backends
.
cuda
.
enable_cudnn_sdp
(
False
)

# Keep these enabled as fallbacks

torch
.
backends
.
cuda
.
enable_flash_sdp
(
True
)

torch
.
backends
.
cuda
.
enable_mem_efficient_sdp
(
True
)

torch
.
backends
.
cuda
.
enable_math_sdp
(
True
)

pretrained_model_name_or_path
 
=
 
"OpenMOSS-Team/MOSS-TTS-v1.5"

device
 
=
 
"cuda"
 
if
 
torch
.
cuda
.
is_available
() 
else
 
"cpu"

dtype
 
=
 
torch
.
bfloat16
 
if
 
device
 
==
 
"cuda"
 
else
 
torch
.
float32

def
 
resolve_attn_implementation
() 
->
 
str
:
 
# Prefer FlashAttention 2 when package + device conditions are met.

 
if
 (
 
device
 
==
 
"cuda"

 
and
 
importlib
.
util
.
find_spec
(
"flash_attn"
) 
is
 
not
 
None

 
and
 
dtype
 
in
 {
torch
.
float16
, 
torch
.
bfloat16
}
 ):
 
major
, 
_
 
=
 
torch
.
cuda
.
get_device_capability
()
 
if
 
major
 
>=
 
8
:
 
return
 
"flash_attention_2"

 
# CUDA fallback: use PyTorch SDPA kernels.

 
if
 
device
 
==
 
"cuda"
:
 
return
 
"sdpa"

 
# CPU fallback.

 
return
 
"eager"

attn_implementation
 
=
 
resolve_attn_implementation
()

print
(
f"[INFO] Using attn_implementation=
{
attn_implementation
}
"
)

processor
 
=
 
AutoProcessor
.
from_pretrained
(
 
pretrained_model_name_or_path
,
 
trust_remote_code
=
True
,
)

processor
.
audio_tokenizer
 
=
 
processor
.
audio_tokenizer
.
to
(
device
)

text_1
 
=
 
"亲爱的你，
\n
你好呀。
\n
\n
今天，我想用最认真、最温柔的声音，对你说一些重要的话。
\n
这些话，像一颗小小的星星，希望能在你的心里慢慢发光。
\n
\n
首先，我想祝你——
\n
每天都能平平安安、快快乐乐。
\n
\n
希望你早上醒来的时候，
\n
窗外有光，屋子里很安静，
\n
你的心是轻轻的，没有着急，也没有害怕。
\n
\n
希望你吃饭的时候胃口很好，
\n
走路的时候脚步稳稳，
\n
晚上睡觉的时候，能做一个又一个甜甜的梦。
\n
\n
我希望你能一直保持好奇心。
\n
对世界充满问题，
\n
对天空、星星、花草、书本和故事感兴趣。
\n
当你问“为什么”的时候，
\n
希望总有人愿意认真地听你说话。
\n
\n
我也希望你学会温柔。
\n
温柔地对待朋友，
\n
温柔地对待小动物，
\n
也温柔地对待自己。
\n
\n
如果有一天你犯了错，
\n
请不要太快责怪自己，
\n
因为每一个认真成长的人，
\n
都会在路上慢慢学会更好的方法。
\n
\n
愿你拥有勇气。
\n
当你站在陌生的地方时，
\n
当你第一次举手发言时，
\n
当你遇到困难、感到害怕的时候，
\n
希望你能轻轻地告诉自己：
\n
“我可以试一试。”
\n
\n
就算没有一次成功，也没有关系。
\n
失败不是坏事，
\n
它只是告诉你，你正在努力。
\n
\n
我希望你学会分享快乐。
\n
把开心的事情告诉别人，
\n
把笑声送给身边的人，
\n
因为快乐被分享的时候，
\n
会变得更大、更亮。
\n
\n
如果有一天你感到难过，
\n
我希望你知道——
\n
难过并不丢脸，
\n
哭泣也不是软弱。
\n
\n
愿你能找到一个安全的地方，
\n
慢慢把心里的话说出来，
\n
然后再一次抬起头，看见希望。
\n
\n
我还希望你能拥有梦想。
\n
这个梦想也许很大，
\n
也许很小，
\n
也许现在还说不清楚。
\n
\n
没关系。
\n
梦想会和你一起长大，
\n
在时间里慢慢变得清楚。
\n
\n
最后，我想送你一个最最重要的祝福：
\n
\n
愿你被世界温柔对待，
\n
也愿你成为一个温柔的人。
\n
\n
愿你的每一天，
\n
都值得被记住，
\n
都值得被珍惜。
\n
\n
亲爱的你，
\n
请记住，
\n
你是独一无二的，
\n
你已经很棒了，
\n
而你的未来，
\n
一定会慢慢变得闪闪发光。
\n
\n
祝你健康、勇敢、幸福，
\n
祝你永远带着笑容向前走。"

text_2
 
=
 
"We stand on the threshold of the AI era.
\n
Artificial intelligence is no longer just a concept in laboratories, but is entering every industry, every creative endeavor, and every decision. It has learned to see, hear, speak, and think, and is beginning to become an extension of human capabilities. AI is not about replacing humans, but about amplifying human creativity, making knowledge more equitable, more efficient, and allowing imagination to reach further. A new era, jointly shaped by humans and intelligent systems, has arrived."

text_3
 
=
 
"nin2 hao3，qing3 wen4 nin2 lai2 zi4 na3 zuo4 cheng2 shi4？"

text_4
 
=
 
"nin2 hao3，qing4 wen3 nin2 lai2 zi4 na4 zuo3 cheng4 shi3？"

text_5
 
=
 
"您好，请问您来自哪 zuo4 cheng2 shi4？"

text_6
 
=
 
"/həloʊ, meɪ aɪ æsk wɪtʃ sɪti juː ɑːr frʌm?/"

text_7
 
=
 
"Bonjour, je voudrais essayer une voix française naturelle et stable."

text_8
 
=
 
"我今天学习了一首中国的古诗，它的名字是[pause 3.2s]静夜思！"

# Use audio from ./assets/audio to avoid downloading from the cloud.

ref_audio_1
 
=
 
"https://speech-demo.oss-cn-shanghai.aliyuncs.com/moss_tts_demo/tts_readme_demo/reference_zh.wav"

ref_audio_2
 
=
 
"https://speech-demo.oss-cn-shanghai.aliyuncs.com/moss_tts_demo/tts_readme_demo/reference_en.m4a"

conversations
 
=
 [
 
# Direct TTS (no reference). Language tags are recommended in v1.5.

 [
processor
.
build_user_message
(
text
=
text_1
)],
 [
processor
.
build_user_message
(
text
=
text_2
)],
 
# Direct TTS (no reference). For languages other than Chinese and English,

 
# set the language tag whenever it is known.

 [
processor
.
build_user_message
(
text
=
text_7
, 
language
=
"French"
)],
 
# Pinyin or IPA input

 [
processor
.
build_user_message
(
text
=
text_3
)],
 [
processor
.
build_user_message
(
text
=
text_4
)],
 [
processor
.
build_user_message
(
text
=
text_5
)],
 [
processor
.
build_user_message
(
text
=
text_6
)],
 
# Explicit pause control. Use [pause X.Ys], such as [pause 3.2s].

 [
processor
.
build_user_message
(
text
=
text_8
)],
 
# Voice cloning (with reference)

 [
processor
.
build_user_message
(
text
=
text_1
, 
reference
=
[
ref_audio_1
])],
 [
processor
.
build_user_message
(
text
=
text_2
, 
reference
=
[
ref_audio_2
])],
 
# Duration control

 [
processor
.
build_user_message
(
text
=
text_2
, 
tokens
=
325
)],
 [
processor
.
build_user_message
(
text
=
text_2
, 
tokens
=
600
)],
]

model
 
=
 
AutoModel
.
from_pretrained
(
 
pretrained_model_name_or_path
,
 
trust_remote_code
=
True
,
 
attn_implementation
=
attn_implementation
,
 
torch_dtype
=
dtype
,
).
to
(
device
)

model
.
eval
()

batch_size
 
=
 
1

save_dir
 
=
 
Path
(
"inference_root"
)

save_dir
.
mkdir
(
exist_ok
=
True
, 
parents
=
True
)

sample_idx
 
=
 
0

with
 
torch
.
no_grad
():
 
for
 
start
 
in
 
range
(
0
, 
len
(
conversations
), 
batch_size
):
 
batch_conversations
 
=
 
conversations
[
start
 : 
start
 
+
 
batch_size
]
 
batch
 
=
 
processor
(
batch_conversations
, 
mode
=
"generation"
)
 
input_ids
 
=
 
batch
[
"input_ids"
].
to
(
device
)
 
attention_mask
 
=
 
batch
[
"attention_mask"
].
to
(
device
)

 
outputs
 
=
 
model
.
generate
(
 
input_ids
=
input_ids
,
 
attention_mask
=
attention_mask
,
 
max_new_tokens
=
4096
,
 )

 
for
 
message
 
in
 
processor
.
decode
(
outputs
):
 
audio
 
=
 
message
.
audio_codes_list
[
0
]
 
out_path
 
=
 
save_dir
 
/
 
f"sample
{
sample_idx
}
.wav"

 
sample_idx
 
+=
 
1

 
torchaudio
.
save
(
out_path
, 
audio
.
unsqueeze
(
0
), 
processor
.
model_config
.
sampling_rate
)

For each model’s full usage, please refer to its corresponding model card.

## Fine-Tuning

Finetuning tutorials are organized by architecture.

Currently available:

* MossTTSDelay/OpenMOSS-Team/MOSS-TTS-v1.5(also compatible withOpenMOSS-Team/MOSS-TTS):moss_tts_delay/finetuning/README.md
* MossTTSLocal/OpenMOSS-Team/MOSS-TTS-Local-Transformer:moss_tts_local/finetuning/README.md
* Moss-TTS-Realtime/OpenMOSS-Team/MOSS-TTS-Realtime:moss_tts_realtime/finetuning/README.md

Additional architecture-specific finetuning tutorials will be added under their corresponding directories.

## llama.cpp Backend (Torch-Free Inference)

For lightweight or edge deployment, MOSS-TTS supports atorch-freeinference path usingllama.cppfor the Qwen3 backbone and ONNX Runtime / TensorRT for the audio tokenizer. No PyTorch installation required.

We also maintain a newer first-class MOSS-TTS path in the companion repositoryOpenMOSS/llama.cpp. Unlike the legacy bridge backend documented below, it moves multi-channel embeddings, multi-head outputs, and delay-pattern decoding directly intollama.cpp.

For that path, start from thefirst-class e2e guide.

### Quick Start

#
 1. Install (torch-free)

pip install -e 
"
.[llama-cpp-onnx]
"

#
 2. Download pre-quantized backbone + embedding/lm_head weights

huggingface-cli download OpenMOSS-Team/MOSS-TTS-GGUF --local-dir weights/MOSS-TTS-GGUF

#
 3. Download ONNX audio tokenizer

huggingface-cli download OpenMOSS-Team/MOSS-Audio-Tokenizer-ONNX --local-dir weights/MOSS-Audio-Tokenizer-ONNX

#
 4. Build the C bridge (one-time, requires llama.cpp compiled from source)

cd
 moss_tts_delay/llama_cpp 
&&
 bash build_bridge.sh /path/to/llama.cpp 
&&
 
cd
 ../..

#
 5. Run inference

python -m moss_tts_delay.llama_cpp \
 --config configs/llama_cpp/default.yaml \
 --text 
"
Hello, world!
"
 --output output.wav

#
 6. (Optional) Low-memory mode for 8 GB GPUs — loads/unloads components per stage

python -m moss_tts_delay.llama_cpp \
 --config configs/llama_cpp/trt-8gb.yaml \
 --text 
"
Hello, world!
"
 --output output.wav

### Installation Profiles

Profile

Install Command

Dependencies

Use Case

Torch-free (ONNX)

pip install -e ".[llama-cpp-onnx]"

numpy, onnxruntime-gpu, tokenizers

Recommended starting point

Torch-free (TRT)

pip install -e ".[llama-cpp-trt]"

numpy, tensorrt, cuda-python

Maximum audio tokenizer speed (build engines yourself)

Torch-accelerated

pip install -e ".[llama-cpp-onnx,llama-cpp-torch]"

+ torch

GPU-accelerated LM heads (~30x faster)

Want to convert weights yourself?See theconversion guidefor step-by-step instructions on extracting, converting, and quantizing MOSS-TTS weights with llama.cpp.

### Model Weights

Repository

Contents

Download

OpenMOSS-Team/MOSS-TTS-GGUF

Q4_K_M backbone 
.gguf
, 
embeddings/
 (
.npy
), 
lm_heads/
 (
.npy
), tokenizer

huggingface-cli download OpenMOSS-Team/MOSS-TTS-GGUF --local-dir weights/MOSS-TTS-GGUF

OpenMOSS-Team/MOSS-Audio-Tokenizer-ONNX

Encoder & decoder ONNX models

huggingface-cli download OpenMOSS-Team/MOSS-Audio-Tokenizer-ONNX --local-dir weights/MOSS-Audio-Tokenizer-ONNX

Note:We donotprovide pre-built TensorRT engines, as they are tied to your specific GPU and TensorRT version. To use TRT, build engines from the ONNX models yourself — seemoss_audio_tokenizer/trt/build_engine.sh.

### Configuration

Four pre-built configs are provided inconfigs/llama_cpp/:

* default.yaml— ONNX audio + GGUF backbone (recommended start)
* trt.yaml— TensorRT audio + GGUF backbone (max throughput, user-built engines)
* trt-8gb.yaml— Low-memory mode for 8 GB GPUs (staged loading, TRT audio)
* cpu-only.yaml— fully CPU-based (no GPU required)

Key config options:

* heads_backend: auto | numpy | torch— LM heads computation backend
* audio_backend: onnx | trt | torch— audio tokenizer backend
* low_memory: true | false— staged loading for limited VRAM (loads/unloads encoder, backbone, decoder per stage)
* kv_cache_type_k / kv_cache_type_v— KV cache quantization (e.g.q8_0,q4_0) to reduce VRAM
* flash_attn: auto | enabled | disabled— flash attention for lower peak VRAM during prefill

For full documentation, seemoss_tts_delay/llama_cpp/README.md.

## SGLang Backend (Accelerated Inference)

MOSS-TTS (Delay) supports running the fused MOSS-TTS and MOSS-Audio-Tokenizer model with the deeply extendedSGLangfrom OpenMOSS, enabling efficient inference for audio generation.

### Quick Start

#
 1. Clone the SGLang repository

git clone https://github.com/OpenMOSS/sglang.git

#
 2. Install SGLang

pip install -e ./sglang/python[all]

#
 3. (Optional) Fix the SGLang CuDNN compatibility error

#
 RuntimeError: CRITICAL WARNING: PyTorch 2.9.1 & CuDNN Compatibility Issue Detected

pip install nvidia-cudnn-cu12==9.16.0.29

#
 4. Download the model and audio tokenizer weights

huggingface-cli download OpenMOSS-Team/MOSS-TTS --local-dir weights/MOSS-TTS
huggingface-cli download OpenMOSS-Team/MOSS-Audio-Tokenizer --local-dir weights/MOSS-Audio-Tokenizer

#
 5. Fuse the model and audio tokenizer weights

python scripts/fuse_moss_tts_delay_with_codec.py --model-path weights/MOSS-TTS --codec-model-path weights/MOSS-Audio-Tokenizer --save-path weights/MOSS-TTS-Delay-With-Codec

#
 6. Start the service

sglang serve --model-path weights/MOSS-TTS-Delay-With-Codec --delay-pattern --trust-remote-code

If the fused output directory already exists, you can append--overwriteto replace it directly, or confirm the overwrite interactively when prompted.

Note:The first request after starting the service for the first time may trigger a lengthy compilation step. This is expected, not a bug, so please wait patiently.

### Request and Response

#### MOSS-TTS (Delay)

curl -X POST http://localhost:30000/generate \
 -H 
"
Content-Type: application/json
"
 \
 -d 
'
{

 "text": "Added SGLang backend support for efficient inference.",

 "audio_data": "https://cdn.jsdelivr.net/gh/OpenMOSS/MOSS-TTSD@main/legacy/v0.7/examples/zh_spk1_moon.wav",

 "sampling_params": {

 "max_new_tokens": 512,

 "temperature": 1.7,

 "top_p": 0.8,

 "top_k": 25

 }

 }
'

* textdenotes the text content to be synthesized; you can prepend${token:25}for token control, for example${token:25}Hello World
* audio_datadenotes the optional reference audio; if omitted, the model generates audio with a random timbre, and it can be either<path-to-audio-file>ordata:audio/wav;base64,{b64_audio}, whereb64_audiois the base64 string of a wav file.

#### MOSS-SoundEffect

curl -X POST http://localhost:30000/generate \
 -H 
"
Content-Type: application/json
"
 \
 -d 
'
{

 "text": "${token:125}${ambient_sound:a sports car roaring past on the highway.}",

 "sampling_params": {

 "max_new_tokens": 512,

 "temperature": 1.5,

 "top_p": 0.6,

 "top_k": 50

 }

 }
'

* textshould contain only two tagged fields:${token:125}and${ambient_sound:...}, where the content after${ambient_sound:...}is a natural-language description of the target sound effect.
* ${token:125}is recommended for more stable generation.
* Do not passaudio_data, or the model may go OOD.

#### Response

{
"text"
: 
"
<wav-base64>
"
, 
"..."
: 
"
...
"
}

The HTTP response is a JSON object and may contain multiple fields. The.textfield stores the WAV base64 string for the generated audio. In most cases, you only need to extract that field and base64-decode it; for example, after saving the response asresponse.json, you can runjq -r '.text' response.json | base64 -d -i > output.wav.

## Evaluation

This section summarizes thefamily‑level evaluation highlightsfor MOSS‑TTS, MOSS-TTSD and MOSS‑VoiceGenerator. For full details, see each model’s model card.

### MOSS‑TTS

MOSS‑TTS achieved state‑of‑the‑art results on the open‑source zero‑shot TTS benchmarkSeed‑TTS‑eval, surpassing all open‑source models and rivaling leading closed‑source systems.

Model

Params

Open‑source

EN WER (%) ↓

EN SIM (%) ↑

ZH CER (%) ↓

ZH SIM (%) ↑

DiTAR

0.6B

❌

1.69

73.5

1.02

75.3

FishAudio‑S1

4B

❌

1.72

62.57

1.22

72.1

CosyVoice3

1.5B

❌

2.22

72

1.12

78.1

Seed‑TTS

❌

2.25

76.2

1.12

79.6

MiniMax‑Speech

❌

1.65

69.2

0.83

78.3

CosyVoice

0.3B

✅

4.29

60.9

3.63

72.3

CosyVoice2

0.5B

✅

3.09

65.9

1.38

75.7

CosyVoice3

0.5B

✅

2.02

71.8

1.16

78

F5‑TTS

0.3B

✅

2

67

1.53

76

SparkTTS

0.5B

✅

3.14

57.3

1.54

66

FireRedTTS

0.5B

✅

3.82

46

1.51

63.5

FireRedTTS‑2

1.5B

✅

1.95

66.5

1.14

73.6

Qwen2.5‑Omni

7B

✅

2.72

63.2

1.7

75.2

FishAudio‑S1‑mini

0.5B

✅

1.94

55

1.18

68.5

IndexTTS2

1.5B

✅

2.23

70.6

1.03

76.5

VibeVoice

1.5B

✅

3.04

68.9

1.16

74.4

HiggsAudio‑v2

3B

✅

2.44

67.7

1.5

74

GLM-TTS

1.5B

✅

2.23

67.2

1.03

76.1

GLM-TTS-RL

1.5B

✅

1.91

68.1

0.89

76.4

VoxCPM

0.5B

✅

1.85

72.9

0.93

77.2

Qwen3‑TTS

0.6B

✅

1.68

70.39

1.23

76.4

Qwen3‑TTS

1.7B

✅

1.5

71.45

1.33

76.72

MossTTSDelay

8B

✅

1.84

70.86

1.37

76.98

MossTTSLocal

1.7B

✅

1.93

73.28

1.44

79.62

### MOSS‑TTSD

#### Objective Evaluation

We evaluate MOSS‑TTSD-v1.0 using three objective metrics: Speaker Attribution Accuracy (ACC), Speaker Similarity (SIM), and Word Error Rate (WER). Benchmarked against multiple open-source and closed-source models, the results show that MOSS‑TTSD-v1.0 consistently achieves either the best or second-best performance.

Model

ZH - SIM

ZH - ACC

ZH - WER

EN - SIM

EN - ACC

EN - WER

Comparison with Open-Source Models

MOSS-TTSD-v1.0

0.7949

0.9587

0.0485

0.7326

0.9626

0.0988

MOSS-TTSD-v0.7

0.7423

0.9391

0.0517

0.6743

0.9266

0.1612

Vibevoice 7B

0.7590

0.9222

0.0570

0.7140

0.9554

0.0946

Vibevoice 1.5 B

0.7415

0.8798

0.0818

0.6961

0.9353

0.1133

FireRedTTS2

0.7383

0.9022

0.0768

-

-

-

Higgs Audio V2

-

-

-

0.6860

0.9025

0.2131

Comparison with Proprietary Models

MOSS-TTSD-v1.0 (elevenlabs_voice)

0.8165

0.9736

0.0391

0.7304

0.9565

0.1005

Eleven V3

0.6970

0.9653

0.0363

0.6730

0.9498

0.0824

MOSS-TTSD-v1.0 (gemini_voice)

-

-

-

0.7893

0.9655

0.0984

gemini-2.5-pro-preview-tts

-

-

-

0.6786

0.9537

0.0859

gemini-2.5-flash-preview-tts

-

-

-

0.7194

0.9511

0.0871

MOSS-TTSD-v1.0 (doubao_voice)

0.8226

0.9630

0.0571

-

-

-

Doubao_Podcast

0.8034

0.9606

0.0472

-

-

-

#### Subjective Evaluation

For open-source models, annotators are asked to score each sample pair in terms of speaker attribution accuracy, voice similarity, prosody, and overall quality. Following the methodology of the LMSYS Chatbot Arena, we compute Elo ratings and confidence intervals for each dimension.

For closed-source models, annotators are only asked to choose the overall preferred one in each pair, and we compute the win rate accordingly.

### MOSS‑VoiceGenerator

MOSS‑VoiceGenerator demonstrates strong subjective preference acrossoverall preference,instruction following, andnaturalness.

### MOSS‑TTS-Realtime

We evaluated the TTFB (Time To First Byte) and RTF (Real-Time Factor) of MOSS-TTS-Realtime.

Note: SDPA + torch.compile were enabled during testing. The following results are tested on a single L20 GPU.

Model

TTFB (ms)

RTF

MOSS-TTS-Realtime

180（After warm up）

0.51

We deployed Qwen3.5-9B using vLLM to measure$T_{\text{LLM-first-sentence}}$. The time required to generate 12 tokens (the TTS prefill length) was 197 ms.

$T_{\text{LLM-first-sentence}} + T_{\text{MOSS-TTS-Realtime-TTFB}} = 197ms + 180ms = 377ms$

## MOSS-TTS-Nano

### Introduction

MOSS-TTS-Nanois our lightweight TTS model designed for CPU-first realtime deployment. It focuses on the part of speech generation that matters most in practical products: a small footprint, low-latency streaming generation, and voice-cloning quality that is strong enough for local demos, web services, and lightweight production integration. Built on a pure autoregressiveAudio Tokenizer + LLMpipeline, it keeps the deployment stack simple while making realtime speech generation accessible even without a GPU.

Its main features include:

* 0.1B parameters: a compact model size that keeps memory usage and deployment cost low, making local deployment and lightweight serving much easier.
* Realtime generation on just 4 CPU cores: streaming speech generation can run efficiently on CPU-only environments, which is practical for local applications and cost-sensitive deployment scenarios.
* Multilingual voice cloning: supports multilingual voice cloning workflows, making it suitable for cross-language synthesis with a single reference speaker.
* 48 kHz stereo input/output: natively supports high-quality stereo audio, improving both reference-audio fidelity and final listening quality.

To learn more about setup, advanced usage, and evaluation metrics, please visit theMOSS-TTS-Nano repository.

Architecture of MOSS-TTS-Nano

### Model Weights

Model

Hugging Face

ModelScope

MOSS-TTS-Nano

## MOSS-Audio-Tokenizer

### Introduction

MOSS-Audio-Tokenizerserves as the unified discrete audio interface for the entire MOSS-TTS Family. It is based on theCat(CausalAudioTokenizer withTransformer) architecture—a 1.6-billion-parameter, "CNN-free" homogeneous audio tokenizer built entirely from Causal Transformer blocks.

* Unified Discrete Bridge: It acts as the shared backbone for MOSS-TTS, MOSS-TTSD, MOSS-VoiceGenerator, MOSS-SoundEffect, and MOSS-TTS-Realtime, providing a consistent audio representation across the family.
* Extreme Compression & High Fidelity: It compresses 24kHz raw audio into a remarkably low frame rate of 12.5Hz. Utilizing a 32-layer Residual Vector Quantizer (RVQ), it supports high-fidelity reconstruction across variable bitrates from 0.125kbps to 4kbps.
* Massive-Scale General Audio Training: Trained from scratch on 3 million hours of diverse data (speech, sound effects, and music), the model achieves state-of-the-art reconstruction among open source audio tokenizers.
* Native Streaming Design: The pure Causal Transformer architecture is specifically designed for scalability and low-latency streaming inference, enabling real-time production workflows.

To learn more about setup, advanced usage, and evaluation metrics, please visit theMOSS-Audio-Tokenizer Repository

Architecture of MOSS Audio Tokenizer

### Model Weights

Model

Hugging Face

ModelScope

MOSS-Audio-Tokenizer

### Objective Reconstruction Evaluation

We compareMOSS Audio Tokenizerwith open-source audio tokenizers on the LibriSpeech test-clean subset using SIM, STOI, PESQ-NB, and PESQ-WB. Bitrate is controlled by varying the number of RVQ codebooks during decoding, and MOSS Audio Tokenizer leads reconstruction quality among open-source audio tokenizers at comparable 0–4 kbps bitrates.

## 📚 More Information

### 🌟 Community Projects

The MOSS-TTS community has been growing rapidly, and we’re delighted to showcase some outstanding projects and features built by community members:

* ComfyUI-MOSS-TTSA MOSS-TTS extension for ComfyUI.
* MOSS-TTS-OpenAIAn OpenAI-compatible TTS API for MOSS-TTS.
* AnyPodA podcast generation tool using MOSS-TTS/MOSS-TTSD as the backend.
* Norwegian LoRA for MOSS-TTS— A community-trained LoRA adapter (mlp, r=16) fine-tuned on theNbAiLab/NSTNorwegian speech dataset. Contributed byMartin BergoatTosee. LoRA weights:ToSee-Norway/MOSS-TTS-Norwegian-LoRA. Training scripts are available incommunity/norwegian-lora/.

## LICENSE

Models in MOSS-TTS Family are licensed under the Apache License 2.0.

## Citation

@misc
{
gong2026mossttstechnicalreport
,
 
title
=
{
MOSS-TTS Technical Report
}
, 
 
author
=
{
Yitian Gong and Botian Jiang and Yiwei Zhao and Yucheng Yuan and Kuangwei Chen and Yaozhou Jiang and Cheng Chang and Dong Hong and Mingshu Chen and Ruixiao Li and Yiyang Zhang and Yang Gao and Hanfu Chen and Ke Chen and Songlin Wang and Xiaogui Yang and Yuqian Zhang and Kexin Huang and ZhengYuan Lin and Kang Yu and Ziqi Chen and Jin Wang and Zhaoye Fei and Qinyuan Cheng and Shimin Li and Xipeng Qiu
}
,
 
year
=
{
2026
}
,
 
eprint
=
{
2603.18090
}
,
 
archivePrefix
=
{
arXiv
}
,
 
primaryClass
=
{
cs.SD
}
,
 
url
=
{
https://arxiv.org/abs/2603.18090
}
, 
}

@misc
{
zhang2026mossttsdtextspokendialogue
,
 
title
=
{
MOSS-TTSD: Text to Spoken Dialogue Generation
}
, 
 
author
=
{
Yuqian Zhang and Donghua Yu and Zhengyuan Lin and Botian Jiang and Mingshu Chen and Yaozhou Jiang and Yiwei Zhao and Yiyang Zhang and Yucheng Yuan and Hanfu Chen and Kexin Huang and Jun Zhan and Cheng Chang and Zhaoye Fei and Shimin Li and Xiaogui Yang and Qinyuan Cheng and Xipeng Qiu
}
,
 
year
=
{
2026
}
,
 
eprint
=
{
2603.19739
}
,
 
archivePrefix
=
{
arXiv
}
,
 
primaryClass
=
{
cs.SD
}
,
 
url
=
{
https://arxiv.org/abs/2603.19739
}
, 
}

@misc
{
huang2026mossvoicegeneratorcreaterealisticvoices
,
 
title
=
{
MOSS-VoiceGenerator: Create Realistic Voices with Natural Language Descriptions
}
, 
 
author
=
{
Kexin Huang and Liwei Fan and Botian Jiang and Yaozhou Jiang and Qian Tu and Jie Zhu and Yuqian Zhang and Yiwei Zhao and Chenchen Yang and Zhaoye Fei and Shimin Li and Xiaogui Yang and Qinyuan Cheng and Xipeng Qiu
}
,
 
year
=
{
2026
}
,
 
eprint
=
{
2603.28086
}
,
 
archivePrefix
=
{
arXiv
}
,
 
primaryClass
=
{
cs.SD
}
,
 
url
=
{
https://arxiv.org/abs/2603.28086
}
, 
}

## Star History

## About

MOSS‑TTS Family is an open‑source speech and sound generation model family from MOSI.AI and the OpenMOSS team. It is designed for high‑fidelity, high‑expressiveness, and complex real‑world scenarios, covering stable long‑form speech, multi‑speaker dialogue, voice/character design, environmental sound effects, and real‑time streaming TTS.

mosi.cn/models/moss-tts

### Topics

 audio

 text-to-speech

 multimodal

 voice-cloning

 llm

 audio-tokenizer

### Resources

 Readme

 

### License

 Apache-2.0 license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

2k

 stars
 

### Watchers

15

 watching
 

### Forks

202

 forks
 

 Report repository

 

## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python98.2%
* Shell1.3%
* C0.5%