---
title: GitHub - google-ai-edge/LiteRT-LM · GitHub
url: https://github.com/google-ai-edge/LiteRT-LM
site_name: github
content_file: github-github-google-ai-edgelitert-lm-github
fetched_at: '2026-04-05T11:12:29.732289'
original_url: https://github.com/google-ai-edge/LiteRT-LM
author: google-ai-edge
description: Contribute to google-ai-edge/LiteRT-LM development by creating an account on GitHub.
---

google-ai-edge



/

LiteRT-LM

Public

* NotificationsYou must be signed in to change notification settings
* Fork171
* Star1.3k




 
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

1,350 Commits
1,350 Commits
.github/
workflows
.github/
workflows
 
 
build_config
build_config
 
 
c
c
 
 
cmake
cmake
 
 
cxxbridge_cmd
cxxbridge_cmd
 
 
docs
docs
 
 
kotlin
kotlin
 
 
prebuilt
prebuilt
 
 
python
python
 
 
runtime
runtime
 
 
rust
rust
 
 
schema
schema
 
 
src
src
 
 
tools/
test
tools/
test
 
 
.bazeliskrc
.bazeliskrc
 
 
.bazelrc
.bazelrc
 
 
.bazelversion
.bazelversion
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
BUILD
BUILD
 
 
BUILD.antlr4
BUILD.antlr4
 
 
BUILD.llguidance
BUILD.llguidance
 
 
BUILD.miniaudio
BUILD.miniaudio
 
 
BUILD.minizip
BUILD.minizip
 
 
BUILD.minja
BUILD.minja
 
 
BUILD.nanobind_json
BUILD.nanobind_json
 
 
BUILD.sentencepiece
BUILD.sentencepiece
 
 
BUILD.stb
BUILD.stb
 
 
BUILD.tokenizers_cpp
BUILD.tokenizers_cpp
 
 
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
 
 
PATCH.llguidance
PATCH.llguidance
 
 
PATCH.llguidance_grammar
PATCH.llguidance_grammar
 
 
PATCH.llguidance_numeric
PATCH.llguidance_numeric
 
 
PATCH.llguidance_parser
PATCH.llguidance_parser
 
 
PATCH.llguidance_perf
PATCH.llguidance_perf
 
 
PATCH.llguidance_regexvec
PATCH.llguidance_regexvec
 
 
PATCH.minja
PATCH.minja
 
 
PATCH.nanobind_json
PATCH.nanobind_json
 
 
PATCH.rules_rust
PATCH.rules_rust
 
 
PATCH.sentencepiece
PATCH.sentencepiece
 
 
PATCH.tensorflow
PATCH.tensorflow
 
 
PATCH.toktrie
PATCH.toktrie
 
 
README.md
README.md
 
 
WORKSPACE
WORKSPACE
 
 
__init__.py
__init__.py
 
 
android_ndk_env.bzl
android_ndk_env.bzl
 
 
cargo-bazel-lock.json
cargo-bazel-lock.json
 
 
requirements.txt
requirements.txt
 
 
rust_cxx_bridge.bzl
rust_cxx_bridge.bzl
 
 
version.bzl
version.bzl
 
 
View all files

## Repository files navigation

# LiteRT-LM

LiteRT-LM is Google's production-ready, high-performance, open-source inference
framework for deploying Large Language Models on edge devices.

🔗Product Website

## 🔥 What's New: Gemma 4 support with LiteRT-LM

DeployGemma 4across a broad range of hardware with stellar performance
(blog).

👉 Try on Linux, macOS, Windows (WSL) or Raspberry Pi with theLiteRT-LM CLI:

litert-lm run \
 --from-huggingface-repo=litert-community/gemma-4-E2B-it-litert-lm \
 gemma-4-E2B-it.litertlm \
 --prompt=
"
What is the capital of France?
"

## 🌟 Key Features

* 📱Cross-Platform Support: Android, iOS, Web, Desktop, and IoT (e.g.
Raspberry Pi).
* 🚀Hardware Acceleration: Peak performance via GPU and NPU accelerators.
* 👁️Multi-Modality: Support for vision and audio inputs.
* 🔧Tool Use: Function calling support for agentic workflows.
* 📚Broad Model Support: Gemma, Llama, Phi-4, Qwen, and more.

## 🚀 Production-Ready for Google's Products

LiteRT-LM powers on-device GenAI experiences inChrome,Chromebook Plus,Pixel Watch, and more.

You can also try theGoogle AI Edge Galleryapp to run
models immediately on your device.

Install the app today from Google Play

Install the app today from App Store



### 📰 Blogs & Announcements

Link

Description

Bring state-of-the-art agentic skills to the edge with Gemma 4

Deploy Gemma 4 in-app and across a broader range of devices with stellar performance and broad reach using LiteRT-LM.

On-device GenAI in Chrome, Chromebook Plus and Pixel Watch

Deploy language models on wearables and browser-based platforms using LiteRT-LM at scale.

On-device Function Calling in Google AI Edge Gallery

Explore how to fine-tune FunctionGemma and enable function calling capabilities powered by LiteRT-LM Tool Use APIs.

Google AI Edge small language models, multimodality, and function calling

Latest insights on RAG, multimodality, and function calling for edge language models.

## 🏃 Quick Start

### 🔗 Key Links

* 👉Technical Overviewincluding performance benchmarks, model support, and more.
* 👉LiteRT-LM CLI Guideincluding installation, getting started, and advanced usage.

### ⚡ Quick Try (No Code)

Try LiteRT-LM immediately from your terminal without writing a single line of code usinguv:

uv tool install litert-lm

litert-lm run \
 --from-huggingface-repo=google/gemma-3n-E2B-it-litert-lm \
 gemma-3n-E2B-it-int4 \
 --prompt=
"
What is the capital of France?
"

### 📚 Supported Language APIs

Ready to get started? Explore our language-specific guides and setup instructions.

Language

Status

Best For...

Documentation

Kotlin

✅ Stable

Android apps & JVM

Android (Kotlin) Guide

Python

✅ Stable

Prototyping & Scripting

Python Guide

C++

✅ Stable

High-performance native

C++ Guide

Swift

🚀 In Dev

Native iOS & macOS

(Coming Soon)

#### 🏗️ Build From Source

Thisguideshows how you can
compile LiteRT-LM from source.

## 📦 Releases

* v0.9.0: Improvements to function calling capabilities, better app performance stability.
* v0.8.0: Desktop GPU support and Multi-Modality.
* v0.7.0: NPU acceleration for Gemma models.

For a full list of releases, seeGitHub Releases.

## About

 No description, website, or topics provided.


### Resources

 Readme



### License

 Apache-2.0 license


### Contributing

 Contributing


### Uh oh!

There was an error while loading.Please reload this page.





Activity


Custom properties


### Stars

1.3k

 stars


### Watchers

41

 watching


### Forks

171

 forks


 Report repository



## Releases17

v0.10.1

 Latest



Apr 3, 2026



+ 16 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.





### Uh oh!

There was an error while loading.Please reload this page.





## Contributors

### Uh oh!

There was an error while loading.Please reload this page.





## Languages

* C++76.6%
* CMake7.1%
* Starlark5.0%
* Rust4.1%
* Python3.9%
* Kotlin1.8%
* Other1.5%
