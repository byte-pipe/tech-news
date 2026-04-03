---
title: How I Built a Free AnyDesk Alternative Using Sunshine, Moonlight & Tailscale - DEV Community
url: https://dev.to/thevenice/how-i-built-a-free-anydesk-alternative-using-sunshine-moonlight-tailscale-3lh8
site_name: devto
fetched_at: '2025-10-23T11:13:16.483600'
original_url: https://dev.to/thevenice/how-i-built-a-free-anydesk-alternative-using-sunshine-moonlight-tailscale-3lh8
author: Prakash Pawar
date: '2025-10-22'
description: As a Engineer (and gamer), I’ve always wanted a fast, free, and secure way to access my Windows PC... Tagged with opensource, networking, security, tooling.
tags: '#opensource, #networking, #security, #tooling'
---

As a Engineer (and gamer), I’ve always wanted afast, free, and secure way to access my Windows PC remotely— without paying for tools like AnyDesk or TeamViewer.

After trying a bunch of solutions, I finally found the perfect stack:👉Sunshine + Moonlight + Tailscale

This trio gives me ahardware-accelerated,self-hosted, andend-to-end encryptedsetup that’s better than most commercial options.And yes — it’scompletely free.

## 💡 Why This Setup?

Here’s why I switched:

* ⚡Full GPU acceleration— buttery-smooth 60 FPS streaming.
* 🔐Zero trust networking— no cloud dependency or logins.
* 💰100% free & open source.
* 🌍Remote anywhere access(thanks to Tailscale).
* 🧠Control over my data and latency.

## 🖥️ Step 1: Install Sunshine on Your Windows PC

Sunshine is the open-source host app that handles all the encoding and streaming from your Windows machine.

### Setup:

1. Download fromSunshine’s GitHub releases.
2. Install it normally (run as Administrator).
3. Once it’s running, open your browser and go to:

 https://localhost:47990

Enter fullscreen mode

Exit fullscreen mode

1. Set a username and password.
2. UnderApplications, add “Desktop” (or any app you want to access).
3. Allow Sunshine through Windows Firewall when prompted.
4. Make sure GPU acceleration is enabled (NVENC / AMD VCE / Intel QuickSync).

That’s it — Sunshine is now your personal “streaming server”.

## 🍎 Step 2: Install Moonlight on Your MacBook Air

Moonlight is the open-source client that connects to Sunshine.Think of it as your portable window into your PC.

### Setup:

1. Download fromMoonlight’s official site(or from the Mac App Store).
2. Launch Moonlight — it should auto-detect your PC.
3. If it doesn’t, manually add your PC’s IP address.
4. Enter the pairing PIN shown on your Mac into Sunshine’s web dashboard.

After pairing, you’ll see your PC and the list of apps (or the full desktop).Click “Desktop”, and boom — you’re controlling your PC from your Mac with near-zero latency.

## 🌐 Step 3: Go Truly Remote with Tailscale

This is where it gets powerful.Tailscale gives you a private, encrypted mesh VPN — so you can connect to your PC fromanywhere in the world.

### Setup:

1. Install Tailscale on both devices:

* Windows
* macOSLog in using the same account (Google, GitHub, etc.).Both devices will now appear in your Tailscale network.Copy your Windows PC’sTailscale IP (100.x.x.x).Add that IP to Moonlight — and you’re done.
* Log in using the same account (Google, GitHub, etc.).
* Both devices will now appear in your Tailscale network.
* Copy your Windows PC’sTailscale IP (100.x.x.x).
* Add that IP to Moonlight — and you’re done.

Now you can connect to your PC even when it’s on a different Wi-Fi or behind NAT. No port forwarding. No headache.

## ⚙️ Step 4: Optimize for Best Performance

Inside Moonlight settings:

* Resolution:1080p / 60 FPS for most networks
* Bitrate:20–40 Mbps (depending on Wi-Fi)
* Audio:Enable “Stereo” for minimal lag
* Input:Enable “Low Latency Mode”

If you’re gaming or coding remotely, it feels almost native.

## 🔧 Optional: Auto-start Sunshine on Boot

If you want your PC to be accessible anytime:

1. OpenServicesin Windows.
2. Find “Sunshine Service”.
3. SetStartup Type → Automatic.

Now it’ll always be ready to stream whenever your PC is on.

## ✅ Final Stack Overview

Tool

Purpose

Notes

Sunshine

Streams your Windows desktop

Uses GPU encoding

Moonlight

Client on macOS

Smooth, low-latency viewer

Tailscale

Secure remote tunnel

Access from anywhere

## 🧠 My Experience

I’ve been using this setup daily — fordevelopment,remote debugging, and evengaming sessions.It’s beenstable, fast, and secure, with no external servers or fees.

Once you try this combo, you’ll never look back at AnyDesk.

## 🚀 TL;DR

If you want afree, open-source, and self-hostedAnyDesk alternative:

1. InstallSunshineon Windows.
2. InstallMoonlighton your Mac (or any device).
3. AddTailscaleto access it from anywhere.

That’s it — your private remote desktop system is ready.

If you have any Query regarding this post let me know in comment orTweetme. thank you for reading this.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
