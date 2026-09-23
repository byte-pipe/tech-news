---
title: 'GitHub - harry7557558/spirula-studio: Cross-vendor 3D Gaussian Splatting trainer - video to splat to mesh, Vulkan or CUDA. · GitHub'
url: https://github.com/harry7557558/spirula-studio
site_name: github
content_file: github-github-harry7557558spirula-studio-cross-vendor-3d
fetched_at: '2026-09-23T15:19:20.817284'
original_url: https://github.com/harry7557558/spirula-studio
author: harry7557558
description: Cross-vendor 3D Gaussian Splatting trainer - video to splat to mesh, Vulkan or CUDA. - harry7557558/spirula-studio
---

harry7557558

 

/

spirula-studio

Public

* NotificationsYou must be signed in to change notification settings
* Fork52
* Star666

 
 
 
master
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

907 Commits
907 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github/
workflows
.github/
workflows
 
 
assets
assets
 
 
cmake
cmake
 
 
docs
docs
 
 
reference
reference
 
 
src
src
 
 
tools
tools
 
 
viewer
viewer
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.mcp.json
.mcp.json
 
 
.nojekyll
.nojekyll
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CMakeLists.txt
CMakeLists.txt
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
build_develop.bash
build_develop.bash
 
 
build_develop.bat
build_develop.bat
 
 
pyproject.toml
pyproject.toml
 
 
View all files

## Repository files navigation

# Spirula Studio

 

 

Download•Build from Source•Gallery•Web Viewer

Spirula Studio trains 3D Gaussian Splatting models – from raw photo/video to splat to textured mesh – in one self-contained binary. No Python/PyTorch, no separate COLMAP install. Runs on NVIDIA, AMD, Intel, and Apple GPUs via Vulkan, trains 10M full-SH Gaussians in 8 GB VRAM, and has native support for fisheye and 360° cameras.

Dataset credit:Garageby Simon Bethke (CC BY-SA 4.0); Flight Systems and Control Lab at UTIAS; MegaDepth-X; Mip-NeRF 360.

## Features

* Cross vendor support via Vulkan compute – Runs onNVIDIA, AMD, Intel, and AppleGPUs
* One strategy combining advantages ofMCMC/IGS+/MRNF– Sharper results, fewer floaters, from objects to large scenes
* ExtremeVRAM efficiencywith quantized training – Up to 10 million SH3 Gaussians in 8GB VRAM
* Native360° cameraandequirectangularsupport – Load a dataset and train, no undistortion needed
* ModifiedBilateral gridandPPISPfor exposure/WB correction – Improving quality without unwanted color shift or darkening
* Built-inlightning-fast SfM,AI masking, frame extraction from videos – No need to wait for COLMAP or run separate scripts
* Depth/normal, meshing, skybox, linear color... And more.

## News

* September 10, 2026: Metric scale– The dataset creation module now uses telemetry metadata in common video and image formats to recover metric scale and orientation, addressing the popular report that reconstruction results are too large/small or tilted.
* September 3, 2026: LoMa feature support– The SfM module now supportsLoMafor feature detection and matching on difficult datasets.
* August 14, 2026: macOS support– Support for training on macOS/Apple Silicon has been validated. The app can now be downloaded fromReleases page.
* August 8, 2026: Multilingual support– Multilingual support has been added, available to both GUI and CLI. Supported languages: English, 日本語, 简体中文, 繁體中文, 한국어, Deutsch, Français, Español, Português, Italiano, Nederlands, Русский, Türkçe.
* August 8, 2026: End-to-end workflow– The Vulkan backend now has components to extract frames from video, AI masking, native SfM, meshing, and batch processing, accessible from both GUI and CLI.
* July 22, 2026: Cross-vendor support– A Vulkan backend has been added, which works on NVIDIA, AMD, and Intel GPUs.

## Download

Binaries for Windows, Linux, and macOS can be downloaded fromReleases page. Simply select the one for your platform, download and unzip, and double click to open the GUI.

If you are training on remote/cloud GPUs, you may use the CLI – Runspirula --helpfor details. By default,spirula traincommand will serve a viewer on an HTTP port, one you can forward over ssh and view training progress in your web browser.

## Build from source

To build from source, Spirula Studio provides two backends:

* Vulkan (Recommended):The cross-platform and cross-vendor option. Most tested. Works on all major GPUs. Faster to build and produces smaller binary.
* CUDA:Legacy option for CUDA-capable NVIDIA GPUs.

Both provide the same training and meshing functionality. CUDA backend may be faster or slower than Vulkan depending on GPU driver, with difference generally within a few percents. Vulkan backend can be slightly more VRAM efficient in some cases.

Backend

GPU/Vendor Support

Platform Support

Dependencies

Additional Features

Vulkan

NVIDIA, AMD, Intel, Apple Silicon

Windows, Linux, macOS

Vulkan/MoltenVK, CMake/Ninja

Native support for SfM, frame extraction from videos, and AI masking

CUDA

Most NVIDIA GPUs

Windows, Linux

CUDA, CMake/Ninja

-

Details for building the Vulkan backend

Make sure you have Vulkan SDK installed. On macOS, MoltenVK is automatically fetched by CMake. Clone the repository and run the commands:

### Windows with MSVC:

cd
 spirula-studio\
.\build_develop.bat -DSS_BACKEND=vulkan -DSS_ENABLE_PATENTED=ON

If it builds successfully, you getbuild_vulkan\spirula.exe.

### Windows with GCC/Clang:

cd
 spirula-studio\
cmake -G Ninja -B build_vulkan -DCMAKE_BUILD_TYPE=Release -DSS_BACKEND=vulkan -DSS_ENABLE_PATENTED=ON -DCMAKE_MAKE_PROGRAM=Ninja
cmake --build build_vulkan -j

Pass-DCMAKE_C_COMPILERand-DCMAKE_CXX_COMPILERto the firstcmakecommand if needed.

If it builds successfully, you getbuild_vulkan\spirula.exe.

### Linux:

cd
 spirula-studio/
bash build_develop.bash -DSS_BACKEND=vulkan -DSS_ENABLE_PATENTED=ON

If it builds successfully, you getbuild_vulkan/spirulabinary.

### macOS:

cd
 spirula-studio/
bash build_develop.bash -DSS_BACKEND=vulkan -DSS_ENABLE_PATENTED=ON
cmake --build build --target macos_app
cmake --build build --target macos_dmg

macOS has only the one backend, so it builds intobuild/rather than into a per-backend tree. If it builds successfully, you getbuild/spirulabinary similar to Linux. Additionally, it wraps that binary in a double-clickablebuild/Spirula Studio.app, as well as disk imagebuild/Spirula Studio.dmg. MoltenVK is statically linked by default and will run on a Mac without dependency installed.

### Notes regarding third-party licensing

-DSS_ENABLE_PATENTED=ONenables decoding video on the GPU instead of shelling out to ffmpeg (about 15x faster frame extraction, and without need to install ffmpeg). However, AVC/HEVC bitstream parsers carry third-party patent exposure. If you turn this on, you are responsible for ensuring compliance with local patent laws regarding AVC/HEVC playback.

Masking needs a SAM checkpoint, which the GUI downloads on first use and caches. The checkpoints are Meta's models under Meta's licenses – SAM 2.1 is Apache-2.0, SAM 3 is under Meta's own, non-standard license. They are never bundled, and the GUI shows the terms before fetching anything. On the command line, point--modelat a file you downloaded yourself.

Details for building the CUDA backend

Make sure you have a recent version of CUDA installed. On Windows, you also need MSVC compiler compatible with your CUDA version. Clone the repository and run the commands:

### Windows:

cd
 spirula-studio\
.\build_develop.bat -DSS_BACKEND=cuda

If it builds successfully, you getbuild_cuda\spirula.exe.

### Linux:

cd
 spirula-studio/
bash build_develop.bash -DSS_BACKEND=cuda

If it builds successfully, you getbuild_cuda/spirulabinary.

## Gallery

You can find some professional-quality splats trained by Spirula Studio fromMegascapes Libraryand theirSuperSplat page.

Collection of splats created by the users of Spirula Studio can also be found onSuperSplat page.

Some splats created by the author of Spirula Studio can also be found on mySuperSplat page.

## Trivia

Spirula Studio (formerly spirulae-splat) is named after the now-inactive projectspirulae, which was named after thedeep-ocean cephalopod mollusk.

Spirula Studio is developed and maintained almost entirely by one person. Issues and PRs welcome – I sometimes respond late, but rest assured that I do review them all.