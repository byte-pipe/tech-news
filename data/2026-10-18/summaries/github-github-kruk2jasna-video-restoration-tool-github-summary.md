---
title: GitHub - Kruk2/jasna: Video restoration tool · GitHub
url: https://github.com/Kruk2/jasna
date: 
site: github
model: llama3.2:1b
summarized_at: 2026-10-18T14:23:59.603180
---

# GitHub - Kruk2/jasna: Video restoration tool · GitHub

Here is a concise and informative summary of the article:

**Jasna: A Video Restoration Tool**

Jasna is a video restoration tool that can restore missing or damaged parts of images and videos. It is free, simple to use, and runs on your GPU.

**What Jasna Does**

Jasna searches for and restores mosaics in videos and images. It has two restoration models, fastBasicVSR++ and slow LTX, which are only available for NVIDIA and AMD GPUs.

**Requirements**

* NVIDIA or AMD GPU with compute capability 7.5 or higher
* Windows or Linux operating system
* Non-Chinese, Japanese, accented, or other non-English characters in the system path
* GPU supports compute tasks (nVIDIA RTX, AMD Radeon RX 7000/9000)

**How to Use**

1. Download the release for your system and GPU.
2. Unpack the downloaded files into a folder without non-English characters.
3. Start the app: Windows - click `jasna.exe`, Linux - run `jasnafile`, Linux - run `run_jasna_amd.sh`.
4. Add a video to restore it.

**Support and Resources**

* NVIDIA: supports compute tasks, with specific requirements for GPUs and system configuration
* AMD: supports compute tasks, with specific requirements for GPUs and system configuration
* Disk format: Windows - NTFS, Linux - ext4, Btrfs, XFS, or ZFS on SSD
* Network disks: not supported
* LTX: requires NVIDIA GPU, at least 8 GB VRAM, and 16 GB RAM.