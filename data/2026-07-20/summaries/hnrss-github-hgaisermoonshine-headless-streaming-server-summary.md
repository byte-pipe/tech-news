---
title: GitHub - hgaiser/moonshine: Headless streaming server for Moonlight clients, written in Rust. · GitHub
url: https://github.com/hgaiser/moonshine
date: 2026-07-20
site: hnrss
model: llama3.2:1b
summarized_at: 2026-07-20T12:07:06.759804
---

# GitHub - hgaiser/moonshine: Headless streaming server for Moonlight clients, written in Rust. · GitHub

**Moonshine**

A headless streaming server for Moonlight clients, written in Rust. **GitHub**: [hgaiser/moonshine](https://github.com/hgaiser/moonshine).

### Key Features

* Isolated streaming sessions for complete separation from the desktop environment
* No monitor required on headless servers
* Hardware video encoding using GPU acceleration (H.264, H.265, AV1)
* HDR support and full input support including mouse, keyboard, gamepad, motion, touchpad, and haptics
* Audio streaming with low-latency Opus encoding

### Requirements

* Linux only (tested on Arch Linux, but works on other distributions too)
* systemd for process management
* A GPU (NVIDIA RTX, AMD RDNA2+, or Intel Arc) for Vulkan video encoding
* Moonlight v6.0.0 or higher for compatibility with older versions and unofficial ports

### Installation

**Method 1: Arch Linux**

1. Enable user lingering:sudo loginctl enable-linger$USER on the target system.
2. Run the service to start and run immediately: sudo systemctlenable --now moonshine@$USER.

### Method 2: Source Dependencies**

```bash
sudo pacman -S clang cmake gcc-libs glibc libc++ libevdev libpulse libxkbcommon make mesa opus pkg-config rust shaderc vulkan-headers wayland
```

Compile and run:

```bash
Cargo.toml:
[dependencies]
openapi = "1.0"
serde = { version = "1.0", features = ["derive"] }
serde_json = "1.0";

rustfmt.toml:
[rust]: main = false;

# ...
```

**Repository Navigation**: 
* `main`: Branches and files
* `Folders`: Folders and files containing repository settings

### Repositories Files Navigation
#### Moonshine:

A headless streaming server for Moonlight clients, written in Rust. **GitHub**: [hgaiser/moonshine](https://github.com/hgaiser/moonshine).

#### Latest Commit:
Latest commit information, including history of changes made since the last commit.
```bash
- 564 Commits
  - GitHub
    Date
```

### README:
A brief introduction to Moonshine, its features, and requirements.
Note: This is a concise summary.