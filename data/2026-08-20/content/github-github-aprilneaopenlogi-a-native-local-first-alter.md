---
title: 'GitHub - AprilNEA/OpenLogi: ⚡️A native, local-first alternative to Logitech Options+, written in Rust 🦀 — remap buttons, DPI, and SmartShift over HID++. No account, no telemetry. · GitHub'
url: https://github.com/AprilNEA/OpenLogi
site_name: github
content_file: github-github-aprilneaopenlogi-a-native-local-first-alter
fetched_at: '2026-08-20T11:23:53.229378'
original_url: https://github.com/AprilNEA/OpenLogi
author: AprilNEA
description: ⚡️A native, local-first alternative to Logitech Options+, written in Rust 🦀 — remap buttons, DPI, and SmartShift over HID++. No account, no telemetry. - AprilNEA/OpenLogi
---

AprilNEA

 

/

OpenLogi

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork305
* Star11k

 
 
 
master
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

846 Commits
846 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.agents
.agents
 
 
.cargo
.cargo
 
 
.claude/
rules
.claude/
rules
 
 
.github
.github
 
 
.zed
.zed
 
 
crates
crates
 
 
design
design
 
 
docs
docs
 
 
packaging
packaging
 
 
xtask
xtask
 
 
.envrc
.envrc
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
LICENSE-APACHE
LICENSE-APACHE
 
 
LICENSE-MIT
LICENSE-MIT
 
 
README.md
README.md
 
 
cliff.toml
cliff.toml
 
 
crowdin.yml
crowdin.yml
 
 
deny.toml
deny.toml
 
 
devenv.lock
devenv.lock
 
 
devenv.nix
devenv.nix
 
 
devenv.yaml
devenv.yaml
 
 
flake.lock
flake.lock
 
 
flake.nix
flake.nix
 
 
prek.toml
prek.toml
 
 
release-plz.toml
release-plz.toml
 
 
rust-toolchain.toml
rust-toolchain.toml
 
 
rustfmt.toml
rustfmt.toml
 
 
View all files

## Repository files navigation

Warning

OpenLogi is under active developmentand not yet stable — features and config may still change. Give the repo aStar⭐ andWatch👀 it to get notified when a new release lands.

#### English|简体中文|日本語|Deutsch|Français|한국어

# OpenLogi

⚡️ A native, local-first alternative to Logitech Options+, written in Rust 🦀Unlock the full capabilities of Logitech mice, keyboards, and webcams over HID++ and UVC

Fed up with Options+? Try OpenLogi.

Runs on macOS, Linux, and Windows.

## Beyond Options+

Things OpenLogi does that Options+ won't:

* Stay light.Native Rust + GPUI.
* Run on Linux.Linux is a first-class platform in OpenLogi.
* Gestures on any button.Give the gesture role to any physical button — or turn gestures off entirely.
* Plain-text config.Everything is one TOML file you can sync between machines however you like.
* Script it.A real CLI alongside the GUI.

## Features

* Devices connected over Logi Bolt receivers, Unifying receivers, Bluetooth, or a wired connection, with battery percentage and charge state
* Button remapping via the OS input hook: a built-in action catalog plus custom keyboard shortcuts authored in the TOML config¹
* Per-application profile overlays that auto-switch on app focus (macOS + Windows; Linux on X11 / XWayland only)
* Litra lights: power, brightness, and color temperature, with optional auto power that follows camera activity

Mouse

* Capture and remap the middle, mode-shift, and thumbwheel buttons (middle everywhere, the rest where the device exposes them)
* Per-direction gesture bindings with live capture, on any capable button
* Actions Ring: a cursor-centred, eight-slot overlay of actions (ShowActionsRing), with per-application layouts
* DPI control with presets and Cycle / Set-preset actions (0x2201)
* SmartShift wheel: mode toggle, sensitivity, and a permanent-ratchet panel (0x2111)
* Per-device native scroll inversion (0x2121, supported devices)

Keyboard

* Global F-key remapping: the same action catalog as the mouse, plus power-user actions — typed text, key combos, multi-step workflows (macOS + Windows)
* Static RGB lighting (0x8070/0x8080, supported devices)

Camera

* Any Logitech UVC webcam (Brio, StreamCam, the C920 series, …), plug and play
* Live preview that opens the camera only while you watch — leaving it releases the camera entirely and the LED goes off
* Image controls written straight to the UVC hardware — zoom, focus, exposure, brightness, contrast, saturation, sharpness, white balance, tint, with auto-mode toggles for focus / exposure / white balance — so changes apply in Meet / Zoom / OBS and every other app using the camera
* One-click profiles: built-in Default / Streaming / Video call plus custom snapshots; settings persist per camera and are written back to the hardware on the next view

¹ Media key actions use D-Bus MPRIS on Linux; a handful of macOS-specific actions have no universal Linux equivalent and are no-ops. Windows maps platform actions to native equivalents where available.

## Install

Important

QuitLogi Options+first: the two applications fight over HID++ access, and only one can own a given receiver at a time.

### macOS

Requires macOS 13 or later.

Download the signed, notarized.dmgfrom thelatest releaseand dragOpenLogi.appto/Applications.

Or install viaHomebrew:

brew install --cask openlogi

The official Homebrew cask is the default installation path. To explicitly
track the latest GitHub release fromaprilnea/tapinstead:

brew tap aprilnea/tap
brew install --cask aprilnea/tap/openlogi@latest

openlogi@latestis maintained by OpenLogi's release workflow and may update
before the official cask autobump lands. Install eitheropenlogioropenlogi@latest, not both.

### Linux

Download the package for your distribution from thelatest release:

#
 Debian / Ubuntu

sudo dpkg -i openlogi_
*
.deb

#
 Fedora / RHEL

sudo rpm -i openlogi-
*
.rpm

#
 Arch Linux

sudo pacman -U openlogi-
*
.pkg.tar.zst

Packages are published for bothx86_64/amd64andarm64/aarch64.

NixOS users can instead import the repository's module, which installs the
package and udev rules and starts the agent with the graphical session:

{

 
inputs
.
nixpkgs
.
url
 
=
 
"github:NixOS/nixpkgs/nixos-unstable"
;

 
inputs
.
openlogi
 
=
 
{

 
url
 
=
 
"github:AprilNEA/OpenLogi"
;

 
inputs
.
nixpkgs
.
follows
 
=
 
"nixpkgs"
;

 
}
;

 
outputs
 
=
 
{
 
nixpkgs
,
 
openlogi
,
 ... 
}
: 
{

 
nixosConfigurations
.
my-host
 
=
 
nixpkgs
.
lib
.
nixosSystem
 
{

 
system
 
=
 
"x86_64-linux"
;
 
# or aarch64-linux

 
modules
 
=
 
[

 
openlogi
.
nixosModules
.
default

 
{
 
programs
.
openlogi
.
enable
 
=
 
true
;
 
}

 
]
;

 
}
;

 
}
;

}

All Linux packages install udev rules that grant your user access to/dev/hidraw*,/dev/uinputand your Logitech mouse's/dev/input/event*node withoutsudo. The NixOS module starts the agent automatically; after a.deb,.rpm, or.pkg.tar.zstinstallation, enable it for your user:

systemctl --user 
enable
 --now openlogi-agent.service

Seedocs/INSTALL-linux.mdfor complete NixOS options,
manual / source installs, and distros without systemd.

### Windows

Signed portable.ziparchives and per-user.msiinstallers (x86_64 and
arm64) are attached to each release. Both ship the GUI (OpenLogi.exe)
together with the background agent (openlogi-agent.exe), which owns all
device I/O. Keep the two files side by side when using the portable zip, or
the GUI has nothing to connect to.

Windows support has been validated end-to-end on Windows 11 with real
hardware (a wired keyboard and a Unifying-receiver mouse), including
install, in-place upgrade, and uninstall of the MSI. It is newer than the
macOS build, so if you hit a rough edge pleasereport it. The agent shows a
system-tray icon (Show Main Window / Quit) so the app stays reachable after
the main window is closed. To disable it on Windows, setshow_in_menu_bar = falsein the TOML[app_settings]block and restart the
agent; the GUI toggle is currently macOS-only.

To build from source, seeDEVELOPMENT.md.

## Usage (CLI)

SeeUSAGE.md

## Configuration

SeeCONFIGURATION.md

## Developing

SeeDEVELOPMENT.md

## Acknowledgments

* Windows, cameras, and i18nby@davidbudnick— keyboard RGB, Windows support, Logitech webcam support
* Linux portby@cserby— Linux support
* Solaarby@pwr— open-source HID++ implementation
* Mouserby@TomBadash— a local, account-free Options+ replacement

## License

The code in this repository is dual-licensed under either of

* Apache License, Version 2.0 (LICENSE-APACHE)
* MIT license (LICENSE-MIT)

at your option.

### Third-party code

crates/openlogi-hidppis a vendored fork ofhidppby@lus, licensed 0BSD.

### Logo & brand assets

Thanks to@kubai087for designing the OpenLogi
logo. The OpenLogi logo and app icon (the brand assets underdesign/) are © 2026 AprilNEA, all rights reserved, and are not covered by the MIT/Apache
licenses above; seedesign/LICENSE. Forking the code grants
no right to the OpenLogi name, logo, or icon; please don't use them to represent
your own projects, forks, or distributions without prior written permission.

Not affiliated with Logitech."Logitech", "MX Master", and "Options+" are trademarks of Logitech International S.A.

## Repo activity