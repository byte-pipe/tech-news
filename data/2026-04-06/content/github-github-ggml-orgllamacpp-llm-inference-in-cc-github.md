---
title: 'GitHub - ggml-org/llama.cpp: LLM inference in C/C++ · GitHub'
url: https://github.com/ggml-org/llama.cpp
site_name: github
content_file: github-github-ggml-orgllamacpp-llm-inference-in-cc-github
fetched_at: '2026-04-06T11:21:44.532985'
original_url: https://github.com/ggml-org/llama.cpp
author: ggml-org
description: LLM inference in C/C++. Contribute to ggml-org/llama.cpp development by creating an account on GitHub.
---

ggml-org



/

llama.cpp

Public

* NotificationsYou must be signed in to change notification settings
* Fork16.4k
* Star102k




 
master
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

8,674 Commits
8,674 Commits
.devops
.devops
 
 
.gemini
.gemini
 
 
.github
.github
 
 
benches
benches
 
 
ci
ci
 
 
cmake
cmake
 
 
common
common
 
 
docs
docs
 
 
examples
examples
 
 
ggml
ggml
 
 
gguf-py
gguf-py
 
 
grammars
grammars
 
 
include
include
 
 
licenses
licenses
 
 
media
media
 
 
models
models
 
 
pocs
pocs
 
 
requirements
requirements
 
 
scripts
scripts
 
 
src
src
 
 
tests
tests
 
 
tools
tools
 
 
vendor
vendor
 
 
.clang-format
.clang-format
 
 
.clang-tidy
.clang-tidy
 
 
.dockerignore
.dockerignore
 
 
.ecrc
.ecrc
 
 
.editorconfig
.editorconfig
 
 
.flake8
.flake8
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
AGENTS.md
AGENTS.md
 
 
AUTHORS
AUTHORS
 
 
CLAUDE.md
CLAUDE.md
 
 
CMakeLists.txt
CMakeLists.txt
 
 
CMakePresets.json
CMakePresets.json
 
 
CODEOWNERS
CODEOWNERS
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
build-xcframework.sh
build-xcframework.sh
 
 
convert_hf_to_gguf.py
convert_hf_to_gguf.py
 
 
convert_hf_to_gguf_update.py
convert_hf_to_gguf_update.py
 
 
convert_llama_ggml_to_gguf.py
convert_llama_ggml_to_gguf.py
 
 
convert_lora_to_gguf.py
convert_lora_to_gguf.py
 
 
flake.lock
flake.lock
 
 
flake.nix
flake.nix
 
 
mypy.ini
mypy.ini
 
 
poetry.lock
poetry.lock
 
 
pyproject.toml
pyproject.toml
 
 
pyrightconfig.json
pyrightconfig.json
 
 
requirements.txt
requirements.txt
 
 
ty.toml
ty.toml
 
 
View all files

## Repository files navigation

# llama.cpp

Manifesto/ggml/ops

LLM inference in C/C++

## Recent API changes

* Changelog forlibllamaAPI
* Changelog forllama-serverREST API

## Hot topics

* Hugging Face cache migration: models downloaded with-hfare now stored in the standard Hugging Face cache directory, enabling sharing with other HF tools.
* guide : using the new WebUI of llama.cpp
* guide : running gpt-oss with llama.cpp
* [FEEDBACK] Better packaging for llama.cpp to support downstream consumers 🤗
* Support for thegpt-ossmodel with native MXFP4 format has been added |PR|Collaboration with NVIDIA|Comment
* Multimodal support arrived inllama-server:#12898|documentation
* VS Code extension for FIM completions:https://github.com/ggml-org/llama.vscode
* Vim/Neovim plugin for FIM completions:https://github.com/ggml-org/llama.vim
* Hugging Face Inference Endpoints now support GGUF out of the box!#9669
* Hugging Face GGUF editor:discussion|tool

## Quick start

Getting started with llama.cpp is straightforward. Here are several ways to install it on your machine:

* Installllama.cppusingbrew, nix or winget
* Run with Docker - see ourDocker documentation
* Download pre-built binaries from thereleases page
* Build from source by cloning this repository - check outour build guide

Once installed, you'll need a model to work with. Head to theObtaining and quantizing modelssection to learn more.

Example command:

#
 Use a local model file

llama-cli -m my_model.gguf

#
 Or download and run a model directly from Hugging Face

llama-cli -hf ggml-org/gemma-3-1b-it-GGUF

#
 Launch OpenAI-compatible API server

llama-server -hf ggml-org/gemma-3-1b-it-GGUF

## Description

The main goal ofllama.cppis to enable LLM inference with minimal setup and state-of-the-art performance on a wide
range of hardware - locally and in the cloud.

* Plain C/C++ implementation without any dependencies
* Apple silicon is a first-class citizen - optimized via ARM NEON, Accelerate and Metal frameworks
* AVX, AVX2, AVX512 and AMX support for x86 architectures
* RVV, ZVFH, ZFH, ZICBOP and ZIHINTPAUSE support for RISC-V architectures
* 1.5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit, and 8-bit integer quantization for faster inference and reduced memory use
* Custom CUDA kernels for running LLMs on NVIDIA GPUs (support for AMD GPUs via HIP and Moore Threads GPUs via MUSA)
* Vulkan and SYCL backend support
* CPU+GPU hybrid inference to partially accelerate models larger than the total VRAM capacity

Thellama.cppproject is the main playground for developing new features for theggmllibrary.

Models

Typically finetunes of the base models below are supported as well.

Instructions for adding support for new models:HOWTO-add-model.md

#### Text-only

* LLaMA 🦙
* LLaMA 2 🦙🦙
* LLaMA 3 🦙🦙🦙
* Mistral 7B
* Mixtral MoE
* DBRX
* Jamba
* Falcon
* Chinese LLaMA / AlpacaandChinese LLaMA-2 / Alpaca-2
* Vigogne (French)
* BERT
* Koala
* Baichuan 1 & 2+derivations
* Aquila 1 & 2
* Starcoder models
* Refact
* MPT
* Bloom
* Yi models
* StableLM models
* Deepseek models
* Qwen models
* PLaMo-13B
* Phi models
* PhiMoE
* GPT-2
* Orion 14B
* InternLM2
* CodeShell
* Gemma
* Mamba
* Grok-1
* Xverse
* Command-R models
* SEA-LION
* GritLM-7B+GritLM-8x7B
* OLMo
* OLMo 2
* OLMoE
* Granite models
* GPT-NeoX+Pythia
* Snowflake-Arctic MoE
* Smaug
* Poro 34B
* Bitnet b1.58 models
* Flan T5
* Open Elm models
* ChatGLM3-6b+ChatGLM4-9b+GLMEdge-1.5b+GLMEdge-4b
* GLM-4-0414
* SmolLM
* EXAONE-3.0-7.8B-Instruct
* FalconMamba Models
* Jais
* Bielik-11B-v2.3
* RWKV-7
* RWKV-6
* QRWKV-6
* GigaChat-20B-A3B
* Trillion-7B-preview
* Ling models
* LFM2 models
* Hunyuan models
* BailingMoeV2 (Ring/Ling 2.0) models

#### Multimodal

* LLaVA 1.5 models,LLaVA 1.6 models
* BakLLaVA
* Obsidian
* ShareGPT4V
* MobileVLM 1.7B/3B models
* Yi-VL
* Mini CPM
* Moondream
* Bunny
* GLM-EDGE
* Qwen2-VL
* LFM2-VL

Bindings

* Python:ddh0/easy-llama
* Python:abetlen/llama-cpp-python
* Go:go-skynet/go-llama.cpp
* Node.js:withcatai/node-llama-cpp
* JS/TS (llama.cpp server client):lgrammel/modelfusion
* JS/TS (Programmable Prompt Engine CLI):offline-ai/cli
* JavaScript/Wasm (works in browser):tangledgroup/llama-cpp-wasm
* Typescript/Wasm (nicer API, available on npm):ngxson/wllama
* Ruby:yoshoku/llama_cpp.rb
* Rust (more features):edgenai/llama_cpp-rs
* Rust (nicer API):mdrokz/rust-llama.cpp
* Rust (more direct bindings):utilityai/llama-cpp-rs
* Rust (automated build from crates.io):ShelbyJenkins/llm_client
* C#/.NET:SciSharp/LLamaSharp
* C#/VB.NET (more features - community license):LM-Kit.NET
* Scala 3:donderom/llm4s
* Clojure:phronmophobic/llama.clj
* React Native:mybigday/llama.rn
* Java:kherud/java-llama.cpp
* Java:QuasarByte/llama-cpp-jna
* Zig:deins/llama.cpp.zig
* Flutter/Dart:netdur/llama_cpp_dart
* Flutter:xuegao-tzx/Fllama
* PHP (API bindings and features built on top of llama.cpp):distantmagic/resonance(more info)
* Guile Scheme:guile_llama_cpp
* Swiftsrgtuszy/llama-cpp-swift
* SwiftShenghaiWang/SwiftLlama
* DelphiEmbarcadero/llama-cpp-delphi
* Go (no CGo needed):hybridgroup/yzma
* Android:llama.android

UIs

(to have a project listed here, it should clearly state that it depends onllama.cpp)

* AI Sublime Text plugin(MIT)
* BonzAI App(proprietary)
* cztomsik/ava(MIT)
* Dot(GPL)
* eva(MIT)
* iohub/collama(Apache-2.0)
* janhq/jan(AGPL)
* johnbean393/Sidekick(MIT)
* KanTV(Apache-2.0)
* KodiBot(GPL)
* llama.vim(MIT)
* LARS(AGPL)
* Llama Assistant(GPL)
* LlamaLib(Apache-2.0)
* LLMFarm(MIT)
* LLMUnity(MIT)
* LMStudio(proprietary)
* LocalAI(MIT)
* LostRuins/koboldcpp(AGPL)
* MindMac(proprietary)
* MindWorkAI/AI-Studio(FSL-1.1-MIT)
* Mobile-Artificial-Intelligence/maid(MIT)
* Mozilla-Ocho/llamafile(Apache-2.0)
* nat/openplayground(MIT)
* nomic-ai/gpt4all(MIT)
* ollama/ollama(MIT)
* oobabooga/text-generation-webui(AGPL)
* PocketPal AI(MIT)
* psugihara/FreeChat(MIT)
* ptsochantaris/emeltal(MIT)
* pythops/tenere(AGPL)
* ramalama(MIT)
* semperai/amica(MIT)
* withcatai/catai(MIT)
* Autopen(GPL)

Tools

* akx/ggify– download PyTorch models from Hugging Face Hub and convert them to GGML
* akx/ollama-dl– download models from the Ollama library to be used directly with llama.cpp
* crashr/gppm– launch llama.cpp instances utilizing NVIDIA Tesla P40 or P100 GPUs with reduced idle power consumption
* gpustack/gguf-parser- review/check the GGUF file and estimate the memory usage
* Styled Lines(proprietary licensed, async wrapper of inference part for game development in Unity3d with pre-built Mobile and Web platform wrappers and a model example)
* unslothai/unsloth– 🦥 exports/saves fine-tuned and trained models to GGUF (Apache-2.0)

Infrastructure

* Paddler- Open-source LLMOps platform for hosting and scaling AI in your own infrastructure
* GPUStack- Manage GPU clusters for running LLMs
* llama_cpp_canister- llama.cpp as a smart contract on the Internet Computer, using WebAssembly
* llama-swap- transparent proxy that adds automatic model switching with llama-server
* Kalavai- Crowdsource end to end LLM deployment at any scale
* llmaz- ☸️ Easy, advanced inference platform for large language models on Kubernetes.
* LLMKube- Kubernetes operator for llama.cpp with multi-GPU and Apple Silicon Metal
support"

Games

* Lucy's Labyrinth- A simple maze game where agents controlled by an AI model will try to trick you.

## Supported backends

Backend

Target devices

Metal

Apple Silicon

BLAS

All

BLIS

All

SYCL

Intel and Nvidia GPU

OpenVINO [In Progress]

Intel CPUs, GPUs, and NPUs

MUSA

Moore Threads GPU

CUDA

Nvidia GPU

HIP

AMD GPU

ZenDNN

AMD CPU

Vulkan

GPU

CANN

Ascend NPU

OpenCL

Adreno GPU

IBM zDNN

IBM Z & LinuxONE

WebGPU [In Progress]

All

RPC

All

Hexagon [In Progress]

Snapdragon

VirtGPU

VirtGPU APIR

## Obtaining and quantizing models

TheHugging Faceplatform hosts anumber of LLMscompatible withllama.cpp:

* Trending
* LLaMA

You can either manually download the GGUF file or directly use anyllama.cpp-compatible models fromHugging Faceor other model hosting sites, by using this CLI argument:-hf <user>/<model>[:quant]. For example:

llama-cli -hf ggml-org/gemma-3-1b-it-GGUF

By default, the CLI would download from Hugging Face, you can switch to other options with the environment variableMODEL_ENDPOINT. TheMODEL_ENDPOINTmust point to a Hugging Face compatible API endpoint.

After downloading a model, use the CLI tools to run it locally - see below.

llama.cpprequires the model to be stored in theGGUFfile format. Models in other data formats can be converted to GGUF using theconvert_*.pyPython scripts in this repo.

The Hugging Face platform provides a variety of online tools for converting, quantizing and hosting models withllama.cpp:

* Use theGGUF-my-repo spaceto convert to GGUF format and quantize model weights to smaller sizes
* Use theGGUF-my-LoRA spaceto convert LoRA adapters to GGUF format (more info:#10123)
* Use theGGUF-editor spaceto edit GGUF meta data in the browser (more info:#9268)
* Use theInference Endpointsto directly hostllama.cppin the cloud (more info:#9669)

To learn more about model quantization,read this documentation

## llama-cli

#### A CLI tool for accessing and experimenting with most ofllama.cpp's functionality.

* Run in conversation modeModels with a built-in chat template will automatically activate conversation mode. If this doesn't occur, you can manually enable it by adding-cnvand specifying a suitable chat template with--chat-template NAMEllama-cli -m model.gguf#> hi, who are you?#Hi there! I'm your helpful assistant! I'm an AI-powered chatbot designed to assist and provide information to users like you. I'm here to help answer your questions, provide guidance, and offer support on a wide range of topics. I'm a friendly and knowledgeable AI, and I'm always happy to help with anything you need. What's on your mind, and how can I assist you today?##> what is 1+1?#Easy peasy! The answer to 1+1 is... 2!
* Run in conversation mode with custom chat template#use the "chatml" template (use -h to see the list of supported templates)llama-cli -m model.gguf -cnv --chat-template chatml#use a custom templatellama-cli -m model.gguf -cnv --in-prefix'User:'--reverse-prompt'User:'
* Constrain the output with a custom grammarllama-cli -m model.gguf -n 256 --grammar-file grammars/json.gbnf -p'Request: schedule a call at 8pm; Command:'#{"appointmentTime": "8pm", "appointmentDetails": "schedule a a call"}Thegrammars/folder contains a handful of sample grammars. To write your own, check out theGBNF Guide.For authoring more complex JSON grammars, check outhttps://grammar.intrinsiclabs.ai/

## llama-server

#### A lightweight,OpenAI APIcompatible, HTTP server for serving LLMs.

* Start a local HTTP server with default configuration on port 8080llama-server -m model.gguf --port 8080#Basic web UI can be accessed via browser: http://localhost:8080#Chat completion endpoint: http://localhost:8080/v1/chat/completions
* Support multiple-users and parallel decoding#up to 4 concurrent requests, each with 4096 max contextllama-server -m model.gguf -c 16384 -np 4
* Enable speculative decoding#the draft.gguf model should be a small variant of the target model.ggufllama-server -m model.gguf -md draft.gguf
* Serve an embedding model#use the /embedding endpointllama-server -m model.gguf --embedding --pooling cls -ub 8192
* Serve a reranking model#use the /reranking endpointllama-server -m model.gguf --reranking
* Constrain all outputs with a grammar#custom grammarllama-server -m model.gguf --grammar-file grammar.gbnf#JSONllama-server -m model.gguf --grammar-file grammars/json.gbnf

## llama-perplexity

#### A tool for measuring theperplexity1(and other quality metrics) of a model over a given text.

* Measure the perplexity over a text filellama-perplexity -m model.gguf -f file.txt#[1]15.2701,[2]5.4007,[3]5.3073,[4]6.2965,[5]5.8940,[6]5.6096,[7]5.7942,[8]4.9297, ...#Final estimate: PPL = 5.4007 +/- 0.67339
* Measure KL divergence#TODO

## llama-bench

#### Benchmark the performance of the inference for various parameters.

* Run default benchmarkllama-bench -m model.gguf#Output:#| model | size | params | backend | threads | test | t/s |#| ------------------- | ---------: | ---------: | ---------- | ------: | ------------: | -------------------: |#| qwen2 1.5B Q4_0 | 885.97 MiB | 1.54 B | Metal,BLAS | 16 | pp512 | 5765.41 ± 20.55 |#| qwen2 1.5B Q4_0 | 885.97 MiB | 1.54 B | Metal,BLAS | 16 | tg128 | 197.71 ± 0.81 |##build: 3e0ba0e60 (4229)

## llama-simple

#### A minimal example for implementing apps withllama.cpp. Useful for developers.

* Basic text completionllama-simple -m model.gguf#Hello my name is Kaitlyn and I am a 16 year old girl. I am a junior in high school and I am currently taking a class called "The Art of

## Contributing

* Contributors can open PRs
* Collaborators will be invited based on contributions
* Maintainers can push to branches in thellama.cpprepo and merge PRs into themasterbranch
* Any help with managing issues, PRs and projects is very appreciated!
* Seegood first issuesfor tasks suitable for first contributions
* Read theCONTRIBUTING.mdfor more information
* Make sure to read this:Inference at the edge
* A bit of backstory for those who are interested:Changelog podcast

## Other documentation

* cli
* completion
* server
* GBNF grammars

#### Development documentation

* How to build
* Running on Docker
* Build on Android
* Performance troubleshooting
* GGML tips & tricks

#### Seminal papers and background on the models

If your issue is with model generation quality, then please at least scan the following links and papers to understand the limitations of LLaMA models. This is especially important when choosing an appropriate model size and appreciating both the significant and subtle differences between LLaMA models and ChatGPT:

* LLaMA:Introducing LLaMA: A foundational, 65-billion-parameter large language modelLLaMA: Open and Efficient Foundation Language Models
* Introducing LLaMA: A foundational, 65-billion-parameter large language model
* LLaMA: Open and Efficient Foundation Language Models
* GPT-3Language Models are Few-Shot Learners
* Language Models are Few-Shot Learners
* GPT-3.5 / InstructGPT / ChatGPT:Aligning language models to follow instructionsTraining language models to follow instructions with human feedback
* Aligning language models to follow instructions
* Training language models to follow instructions with human feedback

## XCFramework

The XCFramework is a precompiled version of the library for iOS, visionOS, tvOS,
and macOS. It can be used in Swift projects without the need to compile the
library from source. For example:

// swift-tools-version: 5.10
// The swift-tools-version declares the minimum version of Swift required to build this package.

import
 PackageDescription

let

package

=

Package
(

 name
:

"
MyLlamaPackage
"
,

 targets
:

[


.
executableTarget
(

 name
:

"
MyLlamaPackage
"
,

 dependencies
:

[


"
LlamaFramework
"


]
)
,


.
binaryTarget
(

 name
:

"
LlamaFramework
"
,

 url
:

"
https://github.com/ggml-org/llama.cpp/releases/download/b5046/llama-b5046-xcframework.zip
"
,

 checksum
:

"
c19be78b5f00d8d29a25da41042cb7afa094cbf6280a225abe614b03b20029ab
"


)


]

)

The above example is using an intermediate buildb5046of the library. This can be modified
to use a different version by changing the URL and checksum.

## Completions

Command-line completion is available for some environments.

#### Bash Completion

$ build/bin/llama-cli --completion-bash
>

~
/.llama-completion.bash
$
source

~
/.llama-completion.bash

Optionally this can be added to your.bashrcor.bash_profileto load it
automatically. For example:

$
echo

"
source ~/.llama-completion.bash
"

>>

~
/.bashrc

## Dependencies

* yhirose/cpp-httplib- Single-header HTTP server, used byllama-server- MIT license
* stb-image- Single-header image format decoder, used by multimodal subsystem - Public domain
* nlohmann/json- Single-header JSON library, used by various tools/examples - MIT License
* miniaudio.h- Single-header audio format decoder, used by multimodal subsystem - Public domain
* subprocess.h- Single-header process launching solution for C and C++ - Public domain

## Footnotes

1. https://huggingface.co/docs/transformers/perplexity↩

## About

LLM inference in C/C++

### Topics

 ggml

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

102k

 stars


### Watchers

666

 watching


### Forks

16.4k

 forks


 Report repository



## Releases5,000+

b8672

 Latest



Apr 6, 2026



+ 5,727 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.





### Uh oh!

There was an error while loading.Please reload this page.





## Contributors1,579

+ 1,565 contributors

## Languages

* C++57.0%
* C12.4%
* Python7.5%
* Cuda5.9%
* HTML3.7%
* TypeScript2.9%
* Other10.6%
