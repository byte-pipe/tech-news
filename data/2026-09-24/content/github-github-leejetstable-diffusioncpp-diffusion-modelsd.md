---
title: 'GitHub - leejet/stable-diffusion.cpp: Diffusion model(SD,Flux,Wan,Qwen Image,Z-Image,...) inference in pure C/C++ · GitHub'
url: https://github.com/leejet/stable-diffusion.cpp
site_name: github
content_file: github-github-leejetstable-diffusioncpp-diffusion-modelsd
fetched_at: '2026-09-24T15:44:11.009820'
original_url: https://github.com/leejet/stable-diffusion.cpp
author: leejet
description: Diffusion model(SD,Flux,Wan,Qwen Image,Z-Image,...) inference in pure C/C++ - leejet/stable-diffusion.cpp
---

leejet

 

/

stable-diffusion.cpp

Public

* NotificationsYou must be signed in to change notification settings
* Fork810
* Star7.2k

 
 
 
master
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

908 Commits
908 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
assets
assets
 
 
cmake
cmake
 
 
docker
docker
 
 
docs
docs
 
 
examples
examples
 
 
ggml @ 4bf5f60
ggml @ 4bf5f60
 
 
include
include
 
 
scripts
scripts
 
 
src
src
 
 
thirdparty
thirdparty
 
 
.clang-format
.clang-format
 
 
.clang-tidy
.clang-tidy
 
 
.dockerignore
.dockerignore
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CMakeLists.txt
CMakeLists.txt
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
View all files

## Repository files navigation

# stable-diffusion.cpp

Diffusion model(SD,Flux,Wan,...) inference in pure C/C++

Note that this project is under active development.API and command-line option may change frequently.

## 🔥Important News

* 2026/09/20🚀 stable-diffusion.cpp addsDay-0 support for Qwen-Image-2.1
* 2026/08/20🚀 stable-diffusion.cpp now supportsLTX-2.5
* 2026/08/04🚀 stable-diffusion.cpp addsDay-1 support for MiniMax-H3
* 2026/06/25🚀 stable-diffusion.cpp now supportsKrea2
* 2026/06/04🚀 stable-diffusion.cpp now supportsIdeogram4
* 2026/05/31🚀 stable-diffusion.cpp now supportsPiD
* 2026/05/27🚀 stable-diffusion.cpp now supportsLens
* 2026/05/17🚀 stable-diffusion.cpp now supportsLTX-2.3
* 2026/04/11🚀 stable-diffusion.cpp now uses a brand-new embedded web UI.
* 2026/01/18🚀 stable-diffusion.cpp now supportsFLUX.2-klein
* 2025/12/01🚀 stable-diffusion.cpp now supportsZ-Image
* 2025/11/30🚀 stable-diffusion.cpp now supportsFLUX.2-dev
* 2025/10/13🚀 stable-diffusion.cpp now supportsQwen-Image-Edit / Qwen-Image-Edit 2509
* 2025/10/12🚀 stable-diffusion.cpp now supportsQwen-Image
* 2025/09/14🚀 stable-diffusion.cpp now supportsWan2.1 Vace
* 2025/09/06🚀 stable-diffusion.cpp now supportsWan2.1 / Wan2.2

## Features

* Plain C/C++ implementation based onggml, working in the same way asllama.cpp
* Super lightweight and without external dependencies
* Supported modelsImage ModelsSD1.x, SD2.x, SD-TurboSDXL, SDXL-TurboSome SD1.x and SDXL distilled modelsSD3/SD3.5FLUX.1-dev/FLUX.1-schnellFLUX.2-dev/FLUX.2-kleinLensChromaChroma1-RadianceQwen ImageQwen Image 2.1PiDLongCat ImageZ-ImageMiniT2ISenseNova U1.5Ovis-ImageAnimaERNIE-ImageBoogu ImageKrea2Mage-FlowSeFi-ImageHiDream-O1-ImageIdeogram4LLaDA-ImageImage Edit ModelsFLUX.1-Kontext-devQwen Image Edit seriesLongCat Image EditBoogu Image EditMage-Flow-EditLLaDA-Image EditVideo ModelsWan2.1/Wan2.2MiniMax-H3LTX-2.3/LTX-2.5HunyuanVideo 1.5LingBot-VideoPhotoMakersupport.IP-Adaptersupport (SD 1.5 and SDXL, including Plus)Control Net support with SD 1.5ADetailerLoRA support, same asstable-diffusion-webuiLatent Consistency Models support (LCM/LCM-LoRA)Faster and memory efficient latent decoding withTAESDUpscale images generated withESRGAN
* Image ModelsSD1.x, SD2.x, SD-TurboSDXL, SDXL-TurboSome SD1.x and SDXL distilled modelsSD3/SD3.5FLUX.1-dev/FLUX.1-schnellFLUX.2-dev/FLUX.2-kleinLensChromaChroma1-RadianceQwen ImageQwen Image 2.1PiDLongCat ImageZ-ImageMiniT2ISenseNova U1.5Ovis-ImageAnimaERNIE-ImageBoogu ImageKrea2Mage-FlowSeFi-ImageHiDream-O1-ImageIdeogram4LLaDA-Image
* SD1.x, SD2.x, SD-Turbo
* SDXL, SDXL-Turbo
* Some SD1.x and SDXL distilled models
* SD3/SD3.5
* FLUX.1-dev/FLUX.1-schnell
* FLUX.2-dev/FLUX.2-klein
* Lens
* Chroma
* Chroma1-Radiance
* Qwen Image
* Qwen Image 2.1
* PiD
* LongCat Image
* Z-Image
* MiniT2I
* SenseNova U1.5
* Ovis-Image
* Anima
* ERNIE-Image
* Boogu Image
* Krea2
* Mage-Flow
* SeFi-Image
* HiDream-O1-Image
* Ideogram4
* LLaDA-Image
* Image Edit ModelsFLUX.1-Kontext-devQwen Image Edit seriesLongCat Image EditBoogu Image EditMage-Flow-EditLLaDA-Image Edit
* FLUX.1-Kontext-dev
* Qwen Image Edit series
* LongCat Image Edit
* Boogu Image Edit
* Mage-Flow-Edit
* LLaDA-Image Edit
* Video ModelsWan2.1/Wan2.2MiniMax-H3LTX-2.3/LTX-2.5HunyuanVideo 1.5LingBot-Video
* Wan2.1/Wan2.2
* MiniMax-H3
* LTX-2.3/LTX-2.5
* HunyuanVideo 1.5
* LingBot-Video
* PhotoMakersupport.
* IP-Adaptersupport (SD 1.5 and SDXL, including Plus)
* Control Net support with SD 1.5
* ADetailer
* LoRA support, same asstable-diffusion-webui
* Latent Consistency Models support (LCM/LCM-LoRA)
* Faster and memory efficient latent decoding withTAESD
* Upscale images generated withESRGAN
* Supported backendsCPU (AVX, AVX2 and AVX512 support for x86 architectures)CUDAVulkanMetalOpenCLSYCL
* CPU (AVX, AVX2 and AVX512 support for x86 architectures)
* CUDA
* Vulkan
* Metal
* OpenCL
* SYCL
* Supported weight formatsPytorch checkpoint (.ckptor.pthor.pt)Safetensors (.safetensors)GGUF (.gguf)
* Pytorch checkpoint (.ckptor.pthor.pt)
* Safetensors (.safetensors)
* GGUF (.gguf)
* Convert mode supports converting model weights to.ggufor.safetensors
* Supported platformsLinuxMac OSWindowsAndroid (via Termux,Local Diffusion)
* Linux
* Mac OS
* Windows
* Android (via Termux,Local Diffusion)
* Flash Attention for memory usage optimization
* Negative prompt
* stable-diffusion-webuistyle tokenizer (not all the features, only token weighting for now)
* VAE tiling processing for reduce memory usage
* Sampling methodEuler AEulerHeunDPM2DPM++ 2MDPM++ 2M v2DPM++ 2S aER-SDELCM
* Euler A
* Euler
* Heun
* DPM2
* DPM++ 2M
* DPM++ 2M v2
* DPM++ 2S a
* ER-SDE
* LCM
* Cross-platform reproducibility--rng cuda, default, consistent with thestable-diffusion-webui GPU RNG--rng cpu, consistent with thecomfyui RNG
* --rng cuda, default, consistent with thestable-diffusion-webui GPU RNG
* --rng cpu, consistent with thecomfyui RNG
* Embedds generation parameters into png output as webui-compatible text string

## Quick Start

### Get the sd executable

* Download pre-built binaries from thereleases page
* Or build from source by following thebuild guide

### Download model weights

* download weights(.ckpt or .safetensors or .gguf). For exampleStable Diffusion v1.5 fromhttps://huggingface.co/stable-diffusion-v1-5/stable-diffusion-v1-5curl -L -O https://huggingface.co/stable-diffusion-v1-5/stable-diffusion-v1-5/resolve/main/v1-5-pruned-emaonly.safetensors
* Stable Diffusion v1.5 fromhttps://huggingface.co/stable-diffusion-v1-5/stable-diffusion-v1-5

### Generate an image with just one command

./bin/sd-cli -m ../models/v1-5-pruned-emaonly.safetensors -p 
"
a lovely cat
"

For detailed command-line arguments, check outcli doc.

## Performance

If you want to improve performance or reduce VRAM/RAM usage, please refer toperformance guide.
For runtime and parameter backend placement, see thebackend selection guide.

## More Guides

* Troubleshooting
* Backend selection
* RPC
* LoRA
* LCM/LCM-LoRA
* Docker
* Quantization and GGUF
* INT8 convrot safetensors
* Inference acceleration via caching

## Bindings

These projects wrapstable-diffusion.cppfor easier use in other languages/frameworks.

* Golang (non-cgo):seasonjs/stable-diffusion
* Golang (cgo):Binozo/GoStableDiffusion
* Golang (non-cgo):l8bloom/gosd
* C#:DarthAffe/StableDiffusion.NET
* Python:william-murray1204/stable-diffusion-cpp-python
* Rust:newfla/diffusion-rs
* Flutter/Dart:rmatif/Local-Diffusion

## UIs

These projects usestable-diffusion.cppas a backend for their image generation.

* GIMP Plugins
* Jellybox
* Stable Diffusion GUI
* Stable Diffusion CLI-GUI
* Local Diffusion
* sd.cpp-webui
* LocalAI
* Neural-Pixel
* KoboldCpp

## Contributors

Thank you to all the people who have already contributed to stable-diffusion.cpp!