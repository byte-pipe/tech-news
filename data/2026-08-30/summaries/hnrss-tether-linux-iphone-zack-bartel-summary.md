---
title: Tether: Linux + iPhone - Zack Bartel
url: https://zackbartel.com/blog/2026/08/tether/
date: 2026-08-24
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-08-30T06:01:35.831101
---

# Tether: Linux + iPhone - Zack Bartel

# Tether: Linux + iPhone

## Overview
- The author switched to Linux full‑time and missed macOS Continuity features such as iMessage/SMS, file sharing, clipboard sync, and OTP autofill.
- Tether was created to bring as many of these capabilities as technically possible to Linux.
- KDE Connect is acknowledged but does not cover the author’s specific needs.

## Origins
- Initial focus was on clipboard synchronization, which also enabled the OTP workflow.
- The iOS app was released first, offering only clipboard sync; a minimal tether daemon existed on the Linux side.
- Security was prioritized from the start with mutual TLS (mTLS) for all communications and regular security audits.

## Security
- Networking between iOS and Linux uses mTLS, requiring mutual agreement before any data exchange.
- Ongoing security reviews include Opus and Fable bug sweeps.

## Feature Expansion
- File transfer was added shortly after the initial release.
- OTP handling is achieved via a browser extension (Zen Browser/Firefox) and a mail extension (Betterbird/Thunderbird) that detect OTP codes in mail and autofill them in web pages.
- Current limitation: OTP extensions work only with the author’s chosen mail and browser clients.

## Bluetooth Integration
- Direct access to iMessage/SMS was previously thought impossible without a Mac proxy.
- Discoveries of `ancs4linux` and `BlueFerry` provided protocol documentation, enabling a clean‑room C++ implementation despite licensing differences (GPL vs. MIT).
- Integration faced numerous Bluetooth quirks, but ultimately succeeded.
- Supported Bluetooth‑based features now include iMessage, SMS, notifications, and contact sync.

## Current Capabilities
- Clipboard synchronization
- File transfer
- OTP detection and autofill in browsers
- iMessage and SMS sending/receiving
- Notification mirroring
- Contact synchronization

## Motivation
- The project started as a personal solution but aims to serve the broader Linux‑iPhone community.
- The author seeks satisfaction from creating useful software rather than monetary gain.

## Call for Contributions
- Contributions of any kind—bug reports, feature ideas, translations, documentation, or code—are welcomed.
- Linux users with iPhones are encouraged to try Tether and provide feedback.