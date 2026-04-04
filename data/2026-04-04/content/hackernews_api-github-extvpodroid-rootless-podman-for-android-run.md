---
title: 'GitHub - ExTV/Podroid: Rootless Podman for Android — run Linux containers on your phone · GitHub'
url: https://github.com/ExTV/Podroid
site_name: hackernews_api
content_file: hackernews_api-github-extvpodroid-rootless-podman-for-android-run
fetched_at: '2026-04-04T19:15:26.107338'
original_url: https://github.com/ExTV/Podroid
author: politelemon
date: '2026-04-03'
description: Rootless Podman for Android — run Linux containers on your phone - ExTV/Podroid
tags:
- hackernews
- trending
---

ExTV

 

/

Podroid

Public

* NotificationsYou must be signed in to change notification settings
* Fork10
* Star397

 
 
 
 
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

22 Commits
22 Commits
app
app
 
 
gradle
gradle
 
 
screenshots
screenshots
 
 
.gitignore
.gitignore
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
CREDITS.md
CREDITS.md
 
 
Dockerfile
Dockerfile
 
 
Dockerfile.qemu
Dockerfile.qemu
 
 
README.md
README.md
 
 
build-qemu-android.sh
build-qemu-android.sh
 
 
build-termux-android.sh
build-termux-android.sh
 
 
build.gradle.kts
build.gradle.kts
 
 
docker-build-initramfs.sh
docker-build-initramfs.sh
 
 
gradle.properties
gradle.properties
 
 
gradlew
gradlew
 
 
gradlew.bat
gradlew.bat
 
 
init-podroid
init-podroid
 
 
settings.gradle.kts
settings.gradle.kts
 
 
test-deploy.sh
test-deploy.sh
 
 
View all files

## Repository files navigation

# Podroid

Run Linux containers on Android — no root required.

Podroid spins up a lightweight Alpine Linux VM on your phone using QEMU and gives you a fully workingPodmancontainer runtime with a built-in serial terminal.

## Highlights

Containers

Pull and run any OCI image — 
podman run --rm -it alpine sh

Terminal

Full xterm emulation with Ctrl, Alt, F1-F12, arrows, and more

Persistence

Packages, configs, and container images survive restarts

Networking

Internet access out of the box, port forwarding to Android host

Self-contained

No root, no Termux, no host binaries — just install the APK

## Requirements

* arm64Android device
* Android8.0+(API 26)
* ~150 MB free storage

## Quick Start

1. Install the APK fromReleases
2. Open Podroid and tapStart Podman
3. Wait for boot (~20 s) — progress is shown on screen and in the notification
4. TapOpen Terminal
5. Run containers:

podman run --rm alpine 
echo
 hello
podman run --rm -it alpine sh
podman run -d -p 8080:80 nginx

## Terminal

The terminal is powered byTermux'sTerminalViewwith full VT100/xterm emulation wired directly to the VM's serial console.

Extra keys bar(scrollable):

ESCTABSYNCCTRLALTarrowsHOMEENDPGUPPGDNF1–F12-/|

* CTRL / ALTare sticky toggles — tap once, then press a letter
* SYNCmanually pushes the terminal dimensions to the VM
* Terminal size auto-syncs on keyboard open/close so TUI apps (vim, btop, htop) render correctly
* Bell character triggers haptic feedback

## Port Forwarding

Forward ports from the VM to your Android device:

1. Go toSettings
2. Add a rule (e.g. TCP 8080 -> 80)
3. Access the service atlocalhost:8080on your phone

Rules persist across restarts and can be added or removed while the VM is running.

## How It Works

Android App
├── Foreground Service (keeps VM alive)
├── PodroidQemu
│ ├── libqemu-system-aarch64.so (QEMU TCG, no KVM)
│ ├── Serial stdio ←→ TerminalEmulator
│ └── QMP socket (port forwarding, VM control)
└── Alpine Linux VM
 ├── initramfs (read-only base layer)
 ├── ext4 disk (persistent overlay)
 ├── getty on ttyAMA0 (job control)
 └── Podman + crun + netavark + slirp4netns

Boot sequence:QEMU loadsvmlinuz-virt+initrd.img. A two-phase init (init-podroid) mounts a persistent ext4 disk as an overlayfs upper layer over the initramfs. Packages you install and containers you pull are written to the overlay and survive reboots.

Terminal wiring:The app cannot fork host processes, soTerminalSessionis wired to QEMU's serial I/O via reflection — keyboard input goes to QEMU stdin, QEMU stdout feeds the terminal emulator. Terminal dimensions are synced to the VM viasttyso TUI apps see the correct size.

Networking:QEMU user-mode networking (SLIRP) puts the VM at10.0.2.15. Port forwarding uses QEMU'shostfwd, managed at startup via CLI args and at runtime via QMP.

## Building from Source

### 1. Build the initramfs

Requires Docker with multi-arch support:

./docker-build-initramfs.sh

### 2. Build the APK

./gradlew assembleDebug
adb install -r app/build/outputs/apk/debug/app-debug.apk

## Project Layout

Dockerfile # Multi-stage initramfs builder (Alpine aarch64)
docker-build-initramfs.sh # One-command build script
init-podroid # Custom /init for the VM

app/src/main/
├── java/com/excp/podroid/
│ ├── engine/ # QEMU lifecycle, QMP client, VM state machine
│ ├── service/ # Foreground service with boot-stage notifications
│ ├── data/repository/ # Settings + port forward persistence
│ └── ui/screens/ # Home, Terminal, Settings (Jetpack Compose)
├── jniLibs/arm64-v8a/ # Pre-built QEMU + libslirp
└── assets/ # Kernel + initramfs (generated)

## Credits

* QEMU— machine emulation
* Alpine Linux— VM base
* Podman— container runtime
* Termux— terminal emulator libraries
* Limbo PC Emulator— pioneered QEMU on Android

## License

GNU General Public License v2.0

## About

Rootless Podman for Android — run Linux containers on your phone

### Resources

 Readme

 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

397

 stars
 

### Watchers

0

 watching
 

### Forks

10

 forks
 

 Report repository

 

## Releases9

v1.0.9

 Latest

 

Apr 4, 2026

 

+ 8 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Kotlin83.0%
* Shell15.3%
* Dockerfile1.7%