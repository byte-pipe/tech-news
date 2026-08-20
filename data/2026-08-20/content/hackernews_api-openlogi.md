---
title: OpenLogi
url: https://openlogi.org/en
site_name: hackernews_api
content_file: hackernews_api-openlogi
fetched_at: '2026-08-20T11:23:57.144447'
original_url: https://openlogi.org/en
author: amatheus
date: '2026-08-19'
description: A native, local-first alternative to Logitech Options+, written in Rust. Remap buttons, drive DPI and SmartShift over HID++ — no account, no telemetry.
tags:
- hackernews
- trending
---

HID++
Bolt
Unifying
Bluetooth
USB

# Your Logitechmousekeyboardcamera,finally local.

Alocal-firstalternative to Logitech Options+, written in Rust.Remap buttons, drive DPI and SmartShift over HID++.No account, no telemetry.

Download
$
brew install --cask openlogi

.dmg.deb / .rpm / .pkg.tar.zst.msiMIT / Apache-2.0Not affiliated with Logitech

HID++ 0x2111
smartShiftEnhanced
HID++ 0x2150
thumbwheel

## Click a button, bind an action.

The center of the app, working right here: a mouse diagram with clickable hotspots and a per-button action picker. Choose a hotspot, then bind any of the built-in actions.

config.toml
schema_version = 2
MX Master 4
~/.config/openlogi/config.toml
live
schema_version
 
=
 
2
selected_device
 
=
 
"
2b042
"
 
[devices.
2b042
.bindings]
MiddleClick
 
=
 
"
MissionControl
"
DpiToggle
 
=
 
"
CycleDpiPresets
"
Thumbwheel
 
=
 
"
VolumeUp
"
Forward
 
=
 
"
BrowserForward
"
Back
 
=
 
"
BrowserBack
"
GestureButton
 
=
 
"
AppExpose
"
MX Master 4
Writes straight to 
config.toml
, the file you own.

## Everything Options+ does, without the account.

OpenLogi drives your mouse over HID++ directly: buttons, DPI and SmartShift, from a native app that never phones home.

HID++ 2.0
44 actions
Back
BrowserBack
Middle
MissionControl
Forward
NextTab

### Remap any button

Bind any of 44 built-in actions to each physical button, per device. Custom shortcuts, app launchers and scripted actions too.

200
8000
1600 DPI

### DPI control & presets

Set pointer resolution and cycle your own presets, written straight to the sensor over HID++.

HID++ 0x2201
Ratchet
Free-spin
autoDisengage threshold

### SmartShift

Flip the wheel between ratchet and free-spin, or let it switch automatically by scroll speed.

HID++ 0x2111
Global
"com.google.Chrome"
"com.figma.Desktop"
Frontmost

### Per-app profilesComing soon

Per-application overlays that switch the moment your focused app does. Ships in a later release.

Bolt
Unifying
Lightspeed
Bluetooth
USB
HID++

### Bolt, Unifying, Lightspeed, Bluetooth or wired

Reach devices over a Logi Bolt, Unifying or Lightspeed receiver, a direct Bluetooth pairing, or a USB cable. No receiver required.

MX Master 4
86
%
MX Keys
62
%
Litra Glow
100
%

### Live device view

A carousel of paired devices with battery percentage and charge state for everything online.

HID++ 0x1004

## Nothing between your mouse and your machine.

No account, no telemetry, no cloud. Bindings live in a plain TOML file you own, and every change goes straight to the device over HID++.

Network
Device renders only
Your machine
IPC
HID++
Agent
GUI
MX Master 4
config.toml

## Up and running in a minute.

Signed builds for macOS, Linux and Windows. Pick your platform below. Step-by-step setup lives in the docs.

.dmg
.deb
.rpm
.msi

### macOS

$
brew install --cask openlogi
Download .dmg

Homebrew is recommended, or grab the signed .dmg for Apple silicon or Intel.

### Linux

Download .deb

Packages for amd64 and arm64, with .rpm and Arch .pkg.tar.zst builds also available.

### Windows

New
Download .msi

The newest port: signed x86_64 and arm64 installers, validated on Windows 11.

Quit Logi Options+ before launching: the two fight over HID++ access, and only one app can own a receiver at a time. On Linux, the same applies to Solaar.

## Things you might ask.

Something else? Ask inTelegramor open aGitHub issue.

Will OpenLogi support Logitech Flow?
It's on the roadmap, at the far end: a cross-computer pointer and clipboard bridge is a very large feature. The half that lives in the protocol already ships. OpenLogi drives Easy-Switch host switching over HID++ (0x1814/0x1815), and paired mice follow the keyboard when it switches hosts. If the rest lands, it will be opt-in and local-network only.
Can I pair a new device from OpenLogi?
Bolt pairing ships in the GUI, and Unifying and Lightspeed pairing is in progress. Until it lands, pair once with Logitech's tool or Solaar; OpenLogi drives the device from then on.
Can I import my Options+ settings?
Not yet, though an importer is in progress. In the meantime, bindings are a short TOML file you can rebuild in minutes, and unlike Options+ they stay in one portable, hand-editable file.
Why does macOS ask for Accessibility permission?
OpenLogi remaps the side buttons (Back, Forward, middle click) through a CGEventTap, and macOS puts event taps behind the Accessibility permission. The HID++ paths (gesture button, thumb wheel, DPI, SmartShift) don't need it.
How do updates work?
Only when you ask. The in-app update check is opt-in and off by default; new builds come from Homebrew (brew upgrade --cask openlogi) or the signed installers on the releases page.
Do my bindings move to another machine?
Copy the TOML file. Devices are keyed by physical identity (receiver serial and slot, or the device's own serial), so the same mouse keeps its bindings wherever the file goes. Built-in sync may come one day, but it's hard to square with the no-account principle.