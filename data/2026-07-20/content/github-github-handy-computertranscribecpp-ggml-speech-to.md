---
title: 'GitHub - handy-computer/transcribe.cpp: ggml speech-to-text inference for 16+ model families · GitHub'
url: https://github.com/handy-computer/transcribe.cpp
site_name: github
content_file: github-github-handy-computertranscribecpp-ggml-speech-to
fetched_at: '2026-07-20T11:58:00.688605'
original_url: https://github.com/handy-computer/transcribe.cpp
author: handy-computer
description: ggml speech-to-text inference for 16+ model families - handy-computer/transcribe.cpp
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 handy-computer

 

/

transcribe.cpp

Public

* NotificationsYou must be signed in to change notification settings
* Fork25
* Star1k

 
 
 
 
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

489 Commits
489 Commits
.cargo
.cargo
 
 
.claude/
skills
.claude/
skills
 
 
.github
.github
 
 
bindings
bindings
 
 
cmake
cmake
 
 
docs
docs
 
 
examples
examples
 
 
ggml
ggml
 
 
include
include
 
 
reports/
porting
reports/
porting
 
 
samples
samples
 
 
scripts
scripts
 
 
src
src
 
 
tests
tests
 
 
tools
tools
 
 
.clang-format
.clang-format
 
 
.git-blame-ignore-revs
.git-blame-ignore-revs
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CMakeLists.txt
CMakeLists.txt
 
 
CMakePresets.json
CMakePresets.json
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
RELEASING.md
RELEASING.md
 
 
THIRD-PARTY-LICENSES.md
THIRD-PARTY-LICENSES.md
 
 
pyproject.toml
pyproject.toml
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

# transcribe.cpp

C/C++ speech-to-text inference library. Runs diverse STT model families viaGGUFmodels on theggmlruntime, with Metal, Vulkan, and CUDA backends for fast GPU inference plus a tinyBLAS-accelerated CPU path.

16 model families and 60+ variants, streaming and batch. Every model we publish underhandy-computeris numerically verified and WER-tested against its reference implementation

Supported models:

Family

Variants

Docs

Parakeet

10 variants: TDT, RNN-T, CTC, TDT+CTC (110M–1.1B)

docs/models/parakeet.md

Canary

canary-1b
, 
canary-1b-v2
, 
canary-1b-flash
, 
canary-180m-flash

docs/models/canary.md

Canary-Qwen

canary-qwen-2.5b
 (FastConformer + Qwen3-1.7B SALM)

docs/models/canary-qwen-2.5b.md

Whisper

12 variants (
tiny
 through 
large-v3-turbo
, plus 
.en
 siblings)

docs/models/whisper.md

GigaAM

gigaam-v3-{e2e-rnnt,e2e-ctc,rnnt,ctc}

docs/models/gigaam.md

Moonshine

moonshine-tiny
, 
moonshine-base

docs/models/moonshine.md

Moonshine Streaming

moonshine-streaming-{tiny,small,medium}

docs/models/moonshine-streaming.md

Qwen3-ASR

qwen3-asr-0.6b
, 
qwen3-asr-1.7b

docs/models/qwen3-asr.md

Cohere Transcribe

cohere-transcribe-03-2026

docs/models/cohere-transcribe-03-2026.md

SenseVoice

sensevoice-small

docs/models/sensevoice-small.md

FunASR Nano

fun-asr-nano-2512
, 
fun-asr-mlt-nano-2512

docs/models/fun-asr-nano.md

Nemotron Speech Streaming

nemotron-speech-streaming-en-0.6b

docs/models/nemotron-speech-streaming-en-0.6b.md

Nemotron 3.5 ASR Streaming

nemotron-3.5-asr-streaming-0.6b
 (multilingual, 40 locales)

docs/models/nemotron-3.5-asr-streaming-0.6b.md

Multitalker Parakeet Streaming

multitalker-parakeet-streaming-0.6b-v1
 (single-speaker ASR path only)

docs/models/multitalker-parakeet-streaming-0.6b-v1.md

Granite Speech 4 / 4.1

granite-4.0-1b-speech
, 
granite-speech-4.1-2b{,-plus,-nar}

docs/models/granite-speech.md

Voxtral

voxtral-mini-3b-2507
, 
voxtral-small-24b-2507
 (audio-LLM; transcription + translation)

docs/models/voxtral.md

Voxtral Realtime

voxtral-mini-4b-realtime-2602
 (streaming audio-LLM)

docs/models/voxtral-realtime.md

MedASR

medasr
 (Conformer + CTC, English medical-dictation, gated)

docs/models/medasr.md

MOSS Transcribe-Diarize

moss-transcribe-diarize
 (audio-LLM; English + Chinese ASR with inline speaker diarization)

docs/models/moss-transcribe-diarize.md

Per-variant model cards live underdocs/models/.

## Build

cmake -B build
cmake --build build

Metal is enabled automatically on Apple Silicon. For Vulkan (Linux/Windows):

#
 Ubuntu/Debian

sudo apt install build-essential cmake libvulkan-dev glslc libopenblas-dev

cmake -B build -DTRANSCRIBE_VULKAN=ON
cmake --build build

On Windows, see thecomplete build guidefor Vulkan
SDK setup, Visual Studio commands, and the short-build-root fallback for
unusually deep checkouts.

For CUDA (Linux + NVIDIA GPU):

#
 requires the CUDA toolkit (nvcc) on PATH

cmake -B build -DTRANSCRIBE_CUDA=ON
cmake --build build

libopenblas-devis optional but recommended. It accelerates the host-side decoder ~10-15x. Without it the build falls back to a scalar path automatically.

tinyBLAS (Justine Tunney'sllamafile_sgemmkernels) is on by default.

To build the quantization tool:

cmake -B build -DTRANSCRIBE_BUILD_TOOLS=ON
cmake --build build

## Models

Pre-built GGUFs for all supported models are hosted on Hugging Face underhandy-computer. Each per-model doc
(linked in the table above) includes direct download links for every quant.
Convert from source only if you need a different dtype or a checkpoint that
isn't pre-built.

### Convert to GGUF

The converter loads directly from NVIDIA's NeMo checkpoints viaASRModel.from_pretrained. Requiresuv;
the parakeet env ships NeMo and its deps.

uv run --project scripts/envs/parakeet \
 scripts/convert-parakeet.py nvidia/parakeet-tdt-0.6b-v2

This writesmodels/parakeet-tdt-0.6b-v2/parakeet-tdt-0.6b-v2-F32.gguffollowing
the llama.cpp-style<slug>-<QUANT>.ggufnaming convention. Pass a local.nemopath or extracted directory for offline conversion.

### Quantize

Thetranscribe-quantizetool produces smaller models from the
reference GGUF. Available presets:F16,Q8_0,Q6_K,Q5_K_M,Q4_K_M.

build/bin/transcribe-quantize \
 models/parakeet-tdt-0.6b-v2/parakeet-tdt-0.6b-v2-F32.gguf \
 models/parakeet-tdt-0.6b-v2/parakeet-tdt-0.6b-v2-Q4_K_M.gguf \
 --quant Q4_K_M

## Usage

build/bin/transcribe-cli -m models/parakeet-tdt-0.6b-v2/parakeet-tdt-0.6b-v2-F32.gguf samples/jfk.wav

Input must be 16 kHz mono WAV. Useffmpegorsoxto convert other formats:

ffmpeg -i input.mp3 -ar 16000 -ac 1 output.wav

## Bindings

Official bindings wrap the C API for other languages:

Language

Path

Python

bindings/python

TypeScript / JavaScript

bindings/typescript

Rust

bindings/rust/transcribe-cpp

Swift / ObjC

bindings/swift

Seedocs/bindings.mdfor how the bindings are generated
and kept in sync with the header.

## Tests

cd
 build 
&&
 ctest

Some tests require a real model file. Enable them with:

cmake -B build -DTRANSCRIBE_BUILD_REAL_MODEL_TESTS=ON
cmake --build build
TRANSCRIBE_PARAKEET_GGUF=path/to/model.gguf ctest --test-dir build

For the model-family smoke-test, numerical-validation, and benchmark
pattern expected of new ports, seedocs/model-family-testing.md.

## Sponsors & Supporting Organizations

### Mozilla AI & BiR Program

A huge thanks toMozilla AIand theirBiR Program.
This whole project started out as an idea, not even an implementation direction. It was a research project in how
to accelerate transcription models across all platforms as easily as possible. The BiR program and Davide helped
support the research, and my eventual direction to choose to implement and inference engine backed by ggml. And
also experimenting with automated model porting using agentic programming tools.

### Hugging Face

Hugging Faceprovided the project extra storage so we can host all of the models
which we support. We want to provide canonical references for as many models as reasonably possible,
the support from Hugging Face helps to enable this.

### Modal

Modalhelped to provide GPU credits so the project can test and validate the projects
implementations match the transformers or nemo reference source. This is critical to ensuring that we have
as close to a production grade inference engine that works everywhere. We believe it is critical to have
accurate transcriptions and the only way to ensure this is through long running WER checks which Modal
helps to provide. Every model published underhandy-computeron hugggingface has had the WER checked, so you can trust the results. And if there are any regressions, you
bet we will be fixing them.

### Blacksmith

Blacksmithprovides many of the CI runners for this project. That helps to keep
transcribe.cpp well tested and ensure our releases are as smooth as possible. The CI is quick and a drop
in replacement for the standard Github Actions runners. I ran into limits very fast with them and super happy
upon reaching out to Blacksmith they were able to provide runners for the project.

## Project layout

include/transcribe.h Public C API (single header)
src/ Library internals (C++17)
src/arch/parakeet/ Parakeet family implementation
src/arch/cohere/ Cohere Transcribe family implementation
examples/cli/ CLI binary source
tools/transcribe-quantize/ Quantization tool source
bindings/ Python, TypeScript, Rust, and Swift bindings
docs/ Porting and validation guidance
scripts/ Python converter + test tooling
ggml/ Vendored ggml (see ggml/UPSTREAM for pinned SHA)
src/third_party/miniz/ Vendored miniz deflate codec (see its UPSTREAM file)
samples/ Test audio files
tests/ Unit and smoke tests

## License

transcribe.cpp is MIT-licensed. SeeLICENSEfor details. Vendored
third-party components (ggml, miniz — both MIT) are attributed inTHIRD-PARTY-LICENSES.md.

## About

ggml speech-to-text inference for 16+ model families

huggingface.co/handy-computer

### Topics

 speech-to-text

 asr

 ggml

 gguf

### Resources

 Readme

 

### License

 MIT license
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

1k

 stars
 

### Watchers

9

 watching
 

### Forks

25

 forks
 

 Report repository

 

## Releases12

v0.1.3

 Latest

 

Jul 12, 2026

 

+ 11 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* C++58.8%
* C17.4%
* Python8.6%
* Cuda6.4%
* Metal1.8%
* GLSL1.3%
* Other5.7%