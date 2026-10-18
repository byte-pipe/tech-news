---
title: 'GitHub - Kruk2/jasna: Video restoration tool · GitHub'
url: https://github.com/Kruk2/jasna
site_name: github
content_file: github-github-kruk2jasna-video-restoration-tool-github
fetched_at: '2026-10-18T14:17:51.540244'
original_url: https://github.com/Kruk2/jasna
author: Kruk2
description: Video restoration tool. Contribute to Kruk2/jasna development by creating an account on GitHub.
---

main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

1,048 Commits
1,048 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github/
ISSUE_TEMPLATE
.github/
ISSUE_TEMPLATE
 
 
assets
assets
 
 
benchmarks
benchmarks
 
 
docs
docs
 
 
jasna
jasna
 
 
model_weights
model_weights
 
 
patches
patches
 
 
scripts
scripts
 
 
tests
tests
 
 
.coveragerc
.coveragerc
 
 
.dockerignore
.dockerignore
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
LICENSE
LICENSE
 
 
LICENSING.md
LICENSING.md
 
 
NOTICE
NOTICE
 
 
README.ja.md
README.ja.md
 
 
README.md
README.md
 
 
README.zh.md
README.zh.md
 
 
RELEASE_SOURCES.md
RELEASE_SOURCES.md
 
 
pyproject.toml
pyproject.toml
 
 
View all files

## Repository files navigation

The only places to get a genuine License code for the supporter models areBuy Me a Coffee,Unifans, and for China the seller in theChinese README.

支持者模型的正版许可证码只能通过Buy Me a Coffee、Unifans或闲鱼获取。

English|日本語|中文

# Jasna

Jasna restores mosaics in videos and images. It is free, has a simple app
and a command line, and runs on your GPU.

## Contents

Start here

* What Jasna does
* What you need
* Quick start
* Help and community
* Supporting the project(supporter models)

Advanced

* How Jasna works
* Command line
* All guides
* Benchmarks
* Licensing
* Acknowledgments

## What Jasna does

* Finds mosaics in a video and restores them. The rest of the picture is not
touched.
* Two restoration models: fastBasicVSR++(free) and slow but more
detailedLTX(for supporters, NVIDIA only).
* Restores only the parts you choose, with a preview, in theSegment
Editor.
* Works with VR180 videos and still images (SD 1.5, for supporters).
* Lets you watch a video restored live in theVideo Player, without making
a file.

## What you need

* NVIDIAGTX 16-series / RTX 20-series or newer, with a recent driver
(610+ on Windows, 580+ on Linux). GTX 10-series and older don't work.
* OrAMDRadeon RX 7000/9000 (experimental).
* A folder on a local disk, with no Chinese, Japanese, accented or other
non-English characters in its path.

More details

* NVIDIA: your GPU needs compute capability 7.5 or higher in NVIDIA'sGPU table.
* AMD: a GPU supported by ROCm (Radeon RX 7000/9000, Radeon 780M/760M/740M,
Ryzen AI). On Windows, AMD Adrenalin driver 26.8.1 or newer. Secondary
restoration and LTX are NVIDIA only.
* Disk format: NTFS on Windows; ext4, Btrfs, XFS or ZFS on Linux. Network disks
are not supported. Use an SSD; on a hard disk (HDD) Jasna starts and loads
models slowly.
* LTX needs an NVIDIA RTX GPU, at least 8 GB VRAM and 16 GB RAM. SeeWhat LTX needs.

## Quick start

1. Download the release for your system and GPU.
2. Unpack it into a folder with no Chinese, Japanese, accented or other
non-English characters in the path.
3. Start the app:* Windows: double-clickjasna.exe.
* Linux NVIDIA: run thejasnafile.
* Linux AMD: runrun_jasna_amd.sh.
4. Add a video, choose settings and click the▶button at the bottom.

Your first job is slow.On NVIDIA, Jasna first prepares the models for
your exact GPU. This takes about15–60 minutes, only once. Close other
apps and don't use the PC during this time. When you update Jasna, copy themodel_weightsfolder to the new version, so you don't wait again.

Every setting has a tooltip: move the mouse over the ⓘ icon. Out of GPU
memory (VRAM)? LowerMax Clip Size, for example from90to60. SeeTuning.

## Help and community

* App guide: the queue, presets, output names, the Video
Player and activation.
* SLS Discord: examples, help and settings.
Jasna has anew channel;
older posts stay in theold channel (archived).
Please don't be too weird.
* Problem? ClickLogsat the bottom of the app, thenExportto save a
log file. Attach it when you ask for help.

## Supporting the project

Jasna is free. Your support pays for training new models, mostly GPU rental.
Supporters get a License code for the supporter models:

Support

Models

$15 USD
 or more in total

UNet 4x
: makes restored areas sharper.
SD 1.5
: experimental model for still images.

$25 USD

UNet 4x
 and 
SD 1.5
, plus
LTX
: much slower than BasicVSR++, but more detail. NVIDIA only. Includes future updates of this LTX model.

Supporters who gave$15 USD or more on or before 14 October 2026get LTX for free.

Before you choose LTX:

* Look at these LTX samples:1,2,3,4,5,6,7,8.
Explore thenew channeland theold channel (archived)on SLS Discord for more samples.
* Run LTX inTrial mode (speed test)on your PC. It is free and shows if your GPU can
run LTX and how long it takes. The video is not restored. SeeWhat LTX needs.

More examples:UNet 4x,SD 1.5,more SD 1.5.

### Where to support

License codes comeonlyfrom here:

* Buy Me a Coffee(crypto works too)
* Unifans
* For China: see theChinese README

Anyone else selling Jasna, codes or modified files is a scam: their keys don't
work, and their files can run hidden code on your PC. Download Jasna only from
GitHub.

### How to activate

1. Support on one of the pages above. You get aLicense code.
2. In Jasna, openActivate Jasna, enter the License code and pressActivate online.
3. No internet on that PC, or it fails? ChooseManual, seeActivate supporter models.

One License code works on3 PCs or cloud workspaces. After activation,
Jasna works offline. Rented GPUs: seeCloud GPUs.

What counts as a new PC: on Windows, a new motherboard; on Linux, a fresh
Linux install. Each uses one of your 3 slots. Reinstalling Windows or
changing the GPU, disk or RAM does not: just activate again with the same
License code. A few Windows PCs have no real motherboard ID; on those, a new
system disk also counts as a new PC.

Have an email and key from Jasna 0.10? They no longer work. Get a new License
code from where you bought it.

## Advanced

### How Jasna works

Almost everything runs on the GPU, from reading the video to saving it.

1. Decodethe video on the GPU (NVDEC on NVIDIA, AMF on AMD).
2. Detectmosaics in each frame (default modelrfdetr-v6).
3. Trackeach mosaic over time and group its frames into clips (up toMax Clip Sizeframes). Clips end at scene cuts, so two different shots
are never mixed.
4. Restoreeach clip as a 256x256 picture with BasicVSR++. Clips overlap a
little, so there are no visible jumps between them.
5. Optionalsecondary restoration(UNet 4x, RTX Super Res or Topaz TVAI)
makes the restored picture bigger and sharper.
6. Blendthe restored picture back into the original frame. Only the
mosaic area changes.
7. Encodewith the GPU encoder (NVENC on NVIDIA, AMF on AMD). Audio is
copied (encoded again only if the output format can't hold it).

The first job is slow because the models for steps 2 and 4 (and UNet 4x, if
used) are prepared for your exact GPU (NVIDIA only). The result is saved inmodel_weightsand used again later. You can copy it to a newer Jasna
version.

LTX works differently. It goes over the video in 4 passes: find mosaics,
prepare, restore with a diffusion model, save. It is slower but can add more
real detail. SeeChoosing models.

### Command line

The command line can do most of what the app does (not the Video Player,
LTX seed previews, mask suggestions or interactive image mode).

#
 One video

jasna --input input.mp4 --output output.mkv

#
 One image

jasna --input photo.png --output restored.png

#
 A whole folder

jasna --input input_folder --output output_folder

jasna --helplists all options. See theCLI reference.

### All guides

* Using the GUI: queue, presets, output names, Video
Player, activation.
* Choosing models: detection models, BasicVSR++ or LTX,
secondary restoration, SD 1.5 for images.
* Restoring only parts of a video: Segment Editor,
mosaic scan, LTX only for big mosaics.
* VR180 videos: how side-by-side VR is handled.
* Tuning VRAM and GPU usage: clip size, overlap, what to
do when VRAM runs out.
* Advanced processing: denoise, 60→30 FPS,
color LUT, sharpening, encoder quality, actions after the queue.
* Streaming: watch in the browser or in Stash.
* Cloud GPUs: Jasna on a rented GPU (RunPod, Vast).
* CLI reference: all command line options.
* Running from source: for developers. From source
you can use the free BasicVSR++; activation and supporter models need the
official release.

### Benchmarks

Time to restore a whole 3:22 video with BasicVSR++ on an RTX 5090 (Linux).
Lower is better.

Input

Lada 0.11.0

Jasna v0.9.1

720p H.264

01:47

00:32
 (3.4x faster)

1080p H.264

02:02

00:34
 (3.6x faster)

2160p H.264

04:56

01:03
 (4.7x faster)

GPU memory, older versions and how it was measured

GPU memory used (typical / peak, in GB).—means not measured. Lada uses
less GPU memory than Jasna.

Input

Lada

v0.4.1

v0.5.0

v0.9.0

v0.9.1

720p H.264 8-bit

1.8/3.1

17.6/19.9

8.6/9.0

8.6/9.1

4.2/4.6

1080p H.264 8-bit

2.0/3.3

18.9/21.4

9.5/10.2

9.3/10.1

4.8/5.6

2160p H.264 8-bit

2.6/4.1

26.0/30.5

12.9/15.0

11.4/15.4

7.2/10.9

8K VR HEVC 60 fps (15 s)

—

—

—

17.1/18.3

—

Times for older versions (v0.4.1: 01:35 / 01:46 / 03:23; v0.5.0: 00:45 /
00:47 / 01:22; v0.9.0: 00:34 / 00:39 / 01:15 for 720p / 1080p / 2160p; 8K VR:
00:34), the test settings, RAM use and every codec are in thefull benchmark report. Older
full-length videos:legacy report.

### Licensing

Jasna's public application source is AGPL-3.0. Models and bundled dependencies
keep their own terms. Seelicensing and source availability,model noticesand therelease source correspondence.

### Acknowledgments

* Lada(Codeberg): Jasna is inspired
by Lada and in some places based on it. Themosaic_restoration_1.2model
used by Jasna was trained by ladaapp, the author of Lada.
* ZeLeFans: for the VR detection model and the detailed analysis of mosaic
shapes and VR projection.