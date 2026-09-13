---
title: Introducing JetKVM Mini - JetKVM
url: https://jetkvm.com/blog/introducing-jetkvm-mini
site_name: hackernews_api
content_file: hackernews_api-introducing-jetkvm-mini-jetkvm
fetched_at: '2026-09-13T14:49:48.007450'
original_url: https://jetkvm.com/blog/introducing-jetkvm-mini
author: taubek
date: '2026-09-13'
published_date: '2026-09-11'
description: A JetKVM from $33, wired or wireless. New open-source firmware, the same web interface.
tags:
- hackernews
- trending
---

Press releaseSep 11, 2026

* Share onReddit
* Share onX
* Share onBluesky
* Share onMastodon
* Share onHacker News

JetKVM Mini is a smaller, more affordable JetKVM. It comes in two models:JetKVM Miniwith Ethernet for$39andJetKVM Mini W, wireless, for$42. In packs of three, they become even more affordable and drop to$33and$36per unit.

The case is aluminium,42 × 42 × 23 mm(1.7 × 1.7 × 0.9 in), about the footprint of a matchbox. It does what a JetKVM does: native video capture at 1080p (up to 4K with JetKVM OS Services), keyboard and mouse over USB, the same web interface, the same cloud, the same updates.

JetKVM Mini. The display is on top, the buttons on the side.

## Wired or wireless

JetKVM Minihas an RJ45 port. Plug in Ethernet, video, and the USB cable to the target computer, read the IP address off the display, and open it in a browser. Setup is the same as on every JetKVM.

JetKVM Mini Wdrops the RJ45 for a2.4 and 5 GHzradio. It is for machines a cable does not reach: a PC in another room, a box under the TV, a rack with no free switch ports. Video and USB are the only cables. Setup happens over Bluetooth from a browser on your phone or laptop: pick a network, enter the password, and the Mini W joins it.

JetKVM Mini · Ethernet

JetKVM Mini W · Wireless

The port face of JetKVM Mini and JetKVM Mini W.

## Why a Mini

We wanted a JetKVM affordable enough to put on every machine, and getting there meant starting over.The Mini isn't a stripped-down JetKVM. It's a JetKVM re-engineered around the things a KVM needs to do well:capture video, control keyboard and mouse, mount virtual media, and stay reachable when the machine it manages is not.

The result is a much simpler architecture: an ESP32-P4X handles video capture, H.264 encoding, USB, and the JetKVM firmware without the separate DRAM and eMMC required by a Linux system. Around it, we built a compact aluminium enclosure, a simple status display with physical controls, and the same web interface, cloud, extensions, and update system as JetKVM.

It does the job of a JetKVM, in a smaller design that starts at $33.

IP address, USB, and video status on the display.

## The hardware

The Mini runs on an ESP32-P4X, a microcontroller with a hardware H.264 encoder. Video is captured at1080p at 30 fpsor 720p at 60 fps, encoded on the chip, and streamed over WebRTC to your browser. The Mini W adds an ESP32-C5 for wireless. It has IEEE 802.11a/b/g/n/ac/ax on 2.4 and 5 GHz for networking, Bluetooth LE for setup, and IEEE 802.15.4 for Zigbee and Thread.

The Mini has two USB ports. One goes to the target computer: it runs at USB 2.0 High Speed (480 Mbps), presents keyboard, mouse, and virtual media to the machine, and draws power from it. Virtual media runs off a TF Card in the slot on the side — drop in your own card and load it with the ISOs you need.

The other is a general-purpose USB port.It runs at USB 2.0 Full Speed (12 Mbps) and can also serve as a backup or secondary power input. It is where our extensions connect: we're reworking the ATX, DC power, and serial extensions to use standard USB, with new versions coming in a later release. With an external power supply, the port can even operate as a USB host, opening it up to essentially any USB device you choose to support in your own firmware.

## The software

We rewrote the firmware for the ESP32-P4X, and it will be open source from day one. It speaks the same protocols, so the web interface and the cloud carry over unchanged.

That means the interface you already know: keyboard and mouse control, text paste, keyboard layouts, virtual media from an ISO on the TF Card, JetKVM Cloud for access from outside your network, Wake-on-LAN, MQTT and Home Assistant, OIDC login, and over-the-air updates with automatic rollback.

It also gets JetKVM OS Services.The OS service for the machine your KVM is plugged into comes out in the next few weeks, and it supports the Mini from day one. It captures the target computer's screen at up to 4K, and adds a shared clipboard, a guest terminal, and file transfer.Read more.

The JetKVM interface on the Mini, in the BIOS of the connected machine.

Secure boot, when you want it.JetKVM Mini comes ready for secure boot. A digest of JetKVM's public signing key is preinstalled in the chip's eFuse, so you can permanently lock the Mini to JetKVM-signed firmware with a single setting in the web interface.

## Pricing and Availability

Both models are availableOctober 26, 2026through our authorized resellers.

Model
1x
3x
JetKVM Mini
Ethernet
$39
$99
JetKVM Mini W
Wireless
$42
$108

MSRP in USD.

#### Get notified when JetKVM Mini is available

I'm interested in
Ethernet
Wireless
Notify me
Share this post
* Share onReddit
* Share onX
* Share onBluesky
* Share onMastodon
* Share onHacker News

### Stay in the loop

#### Join our Discord

Connect with our community, get support, and follow along with development.

#### Join us on GitHub

Show your support and help others discover the project.

Back to top