---
title: 'GitHub - google-ai-edge/LiteRT: LiteRT, successor to TensorFlow Lite. is Google''s On-device framework for high-performance ML & GenAI deployment on edge platforms, via efficient conversion, runtime, and optimization · GitHub'
url: https://github.com/google-ai-edge/LiteRT
site_name: github
content_file: github-github-google-ai-edgelitert-litert-successor-to-te
fetched_at: '2026-03-12T11:15:50.973627'
original_url: https://github.com/google-ai-edge/LiteRT
author: google-ai-edge
description: LiteRT, successor to TensorFlow Lite. is Google's On-device framework for high-performance ML & GenAI deployment on edge platforms, via efficient conversion, runtime, and optimization - google-ai-edge/LiteRT
---

google-ai-edge

 

/

LiteRT

Public

* NotificationsYou must be signed in to change notification settings
* Fork206
* Star1.6k

 
 
 
 
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

4,078 Commits
4,078 Commits
.github/
workflows
.github/
workflows
 
 
ci
ci
 
 
cmake_example
cmake_example
 
 
docker_build
docker_build
 
 
g3doc
g3doc
 
 
google3/
third_party/
odml/
litert/
opensource_only/
rust
google3/
third_party/
odml/
litert/
opensource_only/
rust
 
 
litert
litert
 
 
tflite
tflite
 
 
third_party
third_party
 
 
weight_loader
weight_loader
 
 
.bazeliskrc
.bazeliskrc
 
 
.bazelrc
.bazelrc
 
 
.bazelversion
.bazelversion
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
BUILD
BUILD
 
 
BUILD.darts_clone
BUILD.darts_clone
 
 
BUILD.sentencepiece
BUILD.sentencepiece
 
 
BUILD.tomlplusplus
BUILD.tomlplusplus
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
PATCH.protobuf_port_msvc_compat
PATCH.protobuf_port_msvc_compat
 
 
PATCH.sentencepiece
PATCH.sentencepiece
 
 
PATCH.tf_xla_tsl_win_copts
PATCH.tf_xla_tsl_win_copts
 
 
README.md
README.md
 
 
RELEASE.md
RELEASE.md
 
 
SECURITY.md
SECURITY.md
 
 
WORKSPACE
WORKSPACE
 
 
configure
configure
 
 
configure.py
configure.py
 
 
View all files

## Repository files navigation

# LiteRT

Google's on-device framework for high-performance ML & GenAI deployment on edge
platforms, via efficient conversion, runtime, and optimization

📖Get Started| 🤝Contributing| 📜License| 🛡Security Policy| 📄Documentation

## Build Status

Nightly Builds

Continuous Builds

Other Builds

 
 
 
 

 
 
 
 

## Description

LiteRT continues the legacy of TensorFlow Lite as the trusted, high-performance
runtime for on-device AI.

LiteRT features advanced GPU/NPU acceleration, delivers superior ML & GenAI
performance, making on-device ML inference easier than ever.

### 🌟 What's New

* 🆕 New LiteRT Compiled Model API: Streamline development with automated accelerator
selection, true async execution, and efficient I/O buffer handling.Automated accelerator selection vs explicit delegate creationAsync execution for faster overall execution timeEasy NPU runtime and model distributionEfficient I/O buffer handling
* Automated accelerator selection vs explicit delegate creation
* Async execution for faster overall execution time
* Easy NPU runtime and model distribution
* Efficient I/O buffer handling
* 🤖 Unified NPU Acceleration: Offer seamless access to NPUs from major
chipset providers with a consistent developer experience. LiteRT NPU,
previously under Early access program is available to all
users:https://ai.google.dev/edge/litert/next/npu
* ⚡ Best-in-class GPU Performance: Use state-of-the-art GPU acceleration for
on-device ML. The new buffer interoperability enables zero-copy and minimizes
latency across various GPU buffer types.
* 🧠 Superior Generative AI inference: Enable the simplest integration with
the best performance for GenAI models.

## 💻 Platforms Supported

LiteRT is designed for cross-platform deployment on a wide range of hardware.

Platform

CPU Support

GPU Support

NPU Support

🤖 Android

✅

✅OpenCL
✅OpenGL

Google Tensor*
✅ Qualcomm
✅ MediaTek
S.LSI*
Intel*

🍎 iOS

✅

✅ Metal

ANE*

🐧 Linux

✅

✅ WebGPU

N/A

🍎 macOS

✅

✅ WebGPU
✅ Metal

ANE*

💻 Windows

✅

✅ WebGPU

Intel*

🌐 Web

✅

✅ WebGPU

Coming soon

🧩 IoT

✅

✅ WebGPU

Broadcom*
Raspberry Pi*

*Coming soon

## Model Coverage and Performance

Coming soon...

## 🏁 Installation

For a comprehensive guide to setting up your application with LiteRT, see
theGet Started guide.

You can build LiteRT from source:

1. Start a docker daemon.
2. Runbuild_with_docker.shunderdocker_build/

The script automatically creates a Linux Docker image, which allows you to build
artifacts for Linux and Android (through cross compilation). See build
instructions inCMake build instructionsandBazel build instructionsfor more
information on how to build runtime libraries with the docker container.

For more information about using docker interactive shell or building different
targets, please refer todocker_build/README.md.

## 🗺 Choose Your Adventure

Every developer's path is different. Here are a few common journeys to help you
get started based on your goals:

### 1. 🔄 I have a PyTorch model...

* Goal: Convert a model from PyTorch to run on LiteRT.
* Path1 (classic models): Use theLiteRT Torch Converterto
transform your PyTorch model into the.tfliteformat, and use AI Edge
Quantizer to optimize the model for optimal performance under resource
constraints. From there, you can deploy it using the standard LiteRT runtime.
* Path2 (LLMs): UseLiteRT Generative Torch APIto
reauthor and convert your PyTorch LLMs into Apache format, and deploy it usingLiteRT LM.

### 2. 🌱 I'm new to on-device ML...

* Goal: Run a pre-trained model (like image segmentation) in a mobile app
for the first time.
* Path1 (Beginner dev): Follow step-by-step instructions via Android Studio
to create aReal-time segmentation Appfor CPU/GPU/NPU inference. Source codelink.
* Path2 (Experienced dev): Start with theGet Started guide, find
a pre-trained .tflite model onKaggle Models,
and use the standard LiteRT runtime to integrate it into your Android or iOS
app.

### 3. ⚡ I need to maximize performance...

* Goal: Accelerate an existing model to run faster and more efficiently
on-device.
* Path:Explore theLiteRT APIto
easily leverage hardware acceleration.For working with Generative AI: Dive intoLiteRT LM, our specialized
solution for running GenAI models.
* Explore theLiteRT APIto
easily leverage hardware acceleration.
* For working with Generative AI: Dive intoLiteRT LM, our specialized
solution for running GenAI models.

### 4. 🧠 I'm working with Generative AI...

* Goal: Deploy a large language model (LLM) or diffusion model on a mobile
device.
* Path: Dive intoLiteRT LM,
our specialized solution for running GenAI models. You'll focus on model
quantization and optimizations specific to large model architectures.

## 🗺 Roadmap

Our commitment is to make LiteRT the best runtime for any on-device ML
deployment. Our product strategies are:

* Expanding Hardware Acceleration: Broadening our support for NPUs and
improving performance across all major hardware accelerators.
* Generative AI Optimizations: Introducing new optimizations and features
specifically for the next wave of on-device generative AI models.
* Improving Developer Tools: Building better tools for debugging, profiling,
and optimizing models.
* Platform Support: Enhancing support for core platforms and exploring new
ones.

## 🙌 Contributing

We welcome contributions to LiteRT. Please see theCONTRIBUTING.mdfile for more information on how to
contribute.

## 💬 Getting Help

We encourage you to reach out if you need help.

* GitHub Issues: For bug reports and feature requests, please file a new
issue on ourGitHub Issuespage.
* GitHub Discussions: For questions, general discussions, and community
support, please visit ourGitHub Discussions.

## 🔗 Related Products

LiteRT is part of a larger ecosystem of tools for on-device machine learning.
Check out these other projects from Google:

* LiteRT Samples: A
collection of LiteRT sample apps.
* LiteRT Torch Converter:
A tool in LiteRT to convert PyTorch models into the LiteRT(.tflite) format for
on-device deployment.
* LiteRT Generative Torch API: A
library in LiteRT to reauthor LLMs for efficient conversion and on-device
inference.
* LiteRT-LM: A library to
efficiently run Large Language Models (LLMs) across edge platforms, built on
top of LiteRT.
* XNNPACK: A highly optimized library
of neural network inference operators for ARM, x86, and WebAssembly
architectures that provides high-performance CPU acceleration for LiteRT.
* MediaPipe: A framework for
building cross-platform, customizable ML solutions for live and streaming
media.

## ❤️ Code of Conduct

This project is dedicated to fostering an open and welcoming environment. Please
read ourCode of Conductto understand the standards of
behavior we expect from all participants in our community.

## 📜 License

LiteRT is licensed under theApache-2.0 License.

## About

LiteRT, successor to TensorFlow Lite. is Google's On-device framework for high-performance ML & GenAI deployment on edge platforms, via efficient conversion, runtime, and optimization

ai.google.dev/edge/litert/next/overview

### Resources

 Readme

 

### License

 Apache-2.0 license
 

### Code of conduct

 Code of conduct
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

1.6k

 stars
 

### Watchers

15

 watching
 

### Forks

206

 forks
 

 Report repository

 

## Releases12

v2.1.2

 Latest

 

Jan 28, 2026

 

+ 11 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* C++71.3%
* MLIR7.7%
* HTML5.6%
* Python4.6%
* Starlark3.9%
* C2.0%
* Other4.9%