---
title: 'GitHub - hgaiser/moonshine: Headless streaming server for Moonlight clients, written in Rust. · GitHub'
url: https://github.com/hgaiser/moonshine
site_name: hnrss
content_file: hnrss-github-hgaisermoonshine-headless-streaming-server
fetched_at: '2026-07-20T11:58:15.553322'
original_url: https://github.com/hgaiser/moonshine
date: '2026-07-20'
description: Headless streaming server for Moonlight clients, written in Rust. - hgaiser/moonshine
tags:
- hackernews
- hnrss
---

hgaiser

 

/

moonshine

Public

* NotificationsYou must be signed in to change notification settings
* Fork41
* Star576

 
 
 
 
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

564 Commits
564 Commits
.github
.github
 
 
.vscode
.vscode
 
 
assets
assets
 
 
dist
dist
 
 
moonshine-core
moonshine-core
 
 
moonshine-tools
moonshine-tools
 
 
moonshine-wsi
moonshine-wsi
 
 
src
src
 
 
.editorconfig
.editorconfig
 
 
.gitignore
.gitignore
 
 
CHANGELOG.md
CHANGELOG.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
rustfmt.toml
rustfmt.toml
 
 
View all files

## Repository files navigation

# Moonshine 🌙

Moonshine lets you stream games from your PC to any device runningMoonlight.
Your keyboard, mouse, and controller inputs are sent back to the host so you can play games remotely as if you were sitting in front of it.

## Features

* Isolated streaming sessions: Each stream runs in its own compositor, completely separate from your desktop environment. Your host PC can still be used for other things while you stream.
* No monitor required: Works on headless servers — no HDMI dummy plug needed.
* Hardware video encoding: H.264, H.265, and AV1 encoding using the GPU.

⚠️AV1 Warning: AV1 encoding is experimental and has issues on NVIDIA GPUs that cause frame sizes to grow over time (see issue). This should be fixed in driver version 595.44.3.0. Until then, stick with H.264 or H.265.

* HDR support: True 10-bit HDR streaming for supported games.
* Full input support: Mouse, keyboard, and gamepad (including motion, touchpad, and haptics).
* Audio streaming: Stereo and surround sound (5.1/7.1) with low-latency Opus encoding.

## Requirements

1. Linux only. Tested on Arch Linux, but it's been reported to work on other Linux distributions too.
2. systemd. Required for launching and managing application processes. Almost all modern Linux distributions include it by default.
3. A GPU with Vulkan video encoding. NVIDIA RTX, AMD RDNA2+, or Intel Arc.
4. Moonlight v6.0.0 or higher. Compatibility with older versions or unofficial ports is not guaranteed.

## Installation

### Arch

The simplest method is to install through the AUR using:

yay -S moonshine

To run Moonshine for your user:

1. Enable user lingering:sudo loginctl enable-linger$USERThis allows Moonshine to run applications in the user's session even when the user is not logged in.If your user is always logged in when you want to stream, you can skip this step.
2. Enable the service to start on boot and run immediately:sudo systemctlenable--now moonshine@$USER

### Source

The following dependencies are required to build:

sudo pacman -S \
 clang \
 cmake \
 gcc-libs \
 glibc \
 libc++ \
 libevdev \
 libpulse \
 libxkbcommon \
 make \
 mesa \
 opus \
 pkg-config \
 rust \
 shaderc \
 vulkan-headers \
 wayland

Then compile and run:

cargo run --release -- /path/to/config.toml

## Configuration

A configuration file is created automatically if the path you provide doesn't exist.
When using the AUR package, it defaults to$XDG_CONFIG_HOME/moonshine/config.toml.

### Pairing with a client

When you connect with Moonlight for the first time, it will show a PIN.
A notification will appear on the host that you can click to open the pairing page, or you can visit it manually athttp://localhost:47989/pin.

You can also pair from the command line:

curl -X POST 
"
http://localhost:47989/submit-pin
"
 -d 
"
uniqueid=0123456789ABCDEF&pin=<PIN>
"

### Adding applications

Each application runs in its own isolated streaming session. Add them toconfig.tomllike this:

[[
application
]]

title
 = 
"
Steam
"

boxart
 = 
"
/path/to/steam.png
"
 
#
 optional

command
 = [
"
/usr/bin/steam
"
, 
"
steam://open/bigpicture
"
]

* title: The name shown in Moonlight.
* boxart(optional): Path to a cover image.
* command: The command to run. First entry is the executable, the rest are arguments.
* pre_command(optional): Commands to run before launching the application. Each entry is a separate command, executed in order. Runs synchronously — the session waits for all to finish.
* post_command(optional): Commands to run after the streaming session ends. Each entry is a separate command, executed in order. Runs synchronously — the server waits for all to finish.

Example:

[[
application
]]

title
 = 
"
Steam
"

command
 = [
"
/usr/bin/steam
"
, 
"
steam://open/bigpicture
"
]

pre_command
 = [
 [
"
/usr/bin/systemctl
"
, 
"
stop
"
, 
"
conflicting.service
"
],
 [
"
/usr/bin/nvidia-smi
"
, 
"
pstate
"
, 
"
50
"
],
]

post_command
 = [
 [
"
/usr/bin/nvidia-smi
"
, 
"
pstate
"
, 
"
performance
"
],
]

### Application scanners

Scanners automatically detect installed applications so you don't have to add them manually.

Steam scanner— finds all installed Steam games:

[[
application_scanner
]]

type
 = 
"
steam
"

library
 = 
"
$HOME/.local/share/Steam
"

command
 = [
"
/usr/bin/steam
"
, 
"
-bigpicture
"
, 
"
steam://rungameid/{game_id}
"
]

Desktop scanner— finds applications from.desktopfiles:

[[
application_scanner
]]

type
 = 
"
desktop
"

directories
 = [
 
"
$HOME/.local/share/applications
"
,
 
"
/usr/share/applications
"
,
]

include_terminal
 = 
false

resolve_icons
 = 
true

## FAQ

1. How does this compare toSunshine?* Sunshine supports more platforms and has more features overall. Moonshine is Linux-only.
* Moonshine runs each streaming session in its own isolated environment, separate from your desktop. This means your host PC stays usable while you stream, and it works without an active desktop session.

## Security

Moonshine isnot designed for use on public networks.
The underlying GameStream protocol has limitations that mean traffic is not fully encrypted at the application level.

If you need to stream over the internet, use a VPN such asTailscale,WireGuard, orZeroTier.

Do not expose Moonshine ports directly to the internet.

## Acknowledgement

This wouldn't have been possible without the incredible work by the people behind the following projects:

1. Moonlight, without it there would be no client for Moonshine.
2. Sunshine, which laid a lot of the groundwork for the host part of the API.
3. Inputtino, for a thorough implementation of input devices.
4. magic-mirror, for inspiration of using Vulkan and a Wayland compositor for headless streaming.

## About

Headless streaming server for Moonlight clients, written in Rust.

### Resources

 Readme

 

### License

 BSD-2-Clause license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

576

 stars
 

### Watchers

4

 watching
 

### Forks

41

 forks
 

 Report repository

 

## Releases13

v0.11.0

 Latest

 

May 16, 2026

 

+ 12 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Rust99.5%
* HTML0.5%