---
title: I tested every IP KVM in my Homelab - Jeff Geerling
url: https://www.jeffgeerling.com/blog/2026/i-tested-every-ip-kvm/
date: 2026-06-05
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-06-06T11:50:46.399910
---

# I tested every IP KVM in my Homelab - Jeff Geerling

# I tested every IP KVM in my Homelab

## Overview
- IP KVMs let you control a computer’s keyboard, video, and mouse over a network, useful when you cannot run remote‑desktop software on the target machine (e.g., locked BIOS, crashed OS, or to avoid consuming resources).  
- High‑end server boards have built‑in IPMI/ILO/iDRAC, but many hobbyist or low‑cost setups need separate devices.  
- Devices range from sub‑$50 “no‑frills” units to $400+ feature‑rich models.  
- Security is a major concern: outdated firmware, open ports, or insecure implementations can become attack vectors (the author mentions an FBI visit linked to a cheap model). Keep firmware updated, firewall the device, and only buy from trusted vendors.

## PiKVM
- Originator of the modern open‑source IP KVM ecosystem; uses Raspberry Pi hardware.  
- Price points: ~ $270 (v4 Mini, no CM4) to ~ $400 (v4 Plus, CM4).  
- Features: 1080p @ 60 fps, HDMI passthrough, two‑way audio, ATX power control, optional 4G/5G backup, multi‑computer switching, ~3 W power draw.  
- Fully open‑source (GPLv3); source code publicly available.  
- Recommended despite higher cost because purchases support the open‑source project.

## BliKVM
- Commercial product built on the same PiKVM software but with proprietary hardware.  
- Price: $235–$300 (AliExpress).  
- Chipsets: Allwinner H616 or Raspberry Pi CM4; also offers a PCIe card version that installs inside a PC.  
- Provides similar features to PiKVM but without contributing back to the open‑source project.  
- Open‑source (GPLv3) with source available.

## GL‑iNet Comet
- Low‑cost ($99.99) single‑core ARM SoC device, forked from PiKVM software.  
- Chipset: RV1126.  
- Supports 4K @ 30 fps, 8 GB eMMC, optional ATX power board and FingerBot for remote power‑button presses.  
- Includes a self‑hosted cloud feature; UI based on PiKVM.

## GL‑iNet Comet Pro
- Mid‑range upgrade ($179.99).  
- Adds built‑in Wi‑Fi, 32 GB eMMC, touchscreen, HDMI passthrough, retains ATX and FingerBot add‑ons.  
- Chipset: RV1126B (unconfirmed).  
- Same open‑source foundation as the basic Comet.

## Sipeed NanoKVM Cube
- Very cheap ($69 on AliExpress); notable for being used in espionage cases, raising security concerns.  
- Chipset: SG2002 (RISC‑V) with a built‑in microphone.  
- 1080p @ 60 fps, 32 GB microSD, optional ATX breakout kit.  
- Firmware was slow to be open‑sourced, affecting trust.  
- Demonstrates that sub‑$100 IP KVMs are feasible.

## Sipeed NanoKVM PCIe
- Untested by the author but offered as a PCIe card for internal installation.  
- Price: $73.  
- Same SG2002 chipset; specs include 4K @ 30 fps, 32 GB eMMC, HDMI passthrough, optional PoE, Wi‑Fi, ATX breakout (up to ~$120 total).  
- Open‑source UI.

## Sipeed NanoKVM Pro / Pro PCIe
- Pro line adds touchscreen, control wheel, Wi‑Fi, HDMI passthrough; still under $100.  
- Uses Axera AX630C dual‑core ARM chip (vs. SG2002 in cheaper models).  
- Multiple form factors (standalone and PCIe).  
- Author reports solid performance across all tested variants.  

## Security Note
- All IP KVMs expose BIOS‑level remote access; treat them as open doors.  
- Keep firmware current, restrict network access with firewalls, and prefer vendors with transparent open‑source code.  
- Refer to linked article on serious vulnerabilities found in several reviewed devices.