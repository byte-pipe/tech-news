---
title: 2026 is the year of self-hosting
url: https://fulghum.io/self-hosting
site_name: hackernews_api
fetched_at: '2026-01-13T11:07:42.037289'
original_url: https://fulghum.io/self-hosting
author: Jordan Fulghum
date: '2026-01-11'
published_date: '2026-01-05T00:00:00Z'
description: CLI agents like Claude Code make self-hosting dramatically easier and actually fun. This is the first time I would recommend it to normal software-literate people.
tags:
- hackernews
- trending
---

# 2026 is the Year of Self-hosting

CLI agents make self-hosting on a home server easier and fun

byJordan Fulghum, January 2026

I've wanted to self-host at home for years, but I always bounced off it - too much time spent configuring instead of using. It just wasn't fun.

That changed recently, because CLI agents likeClaude Codemake self-hosting on a cheapo home server dramatically easier and actually fun.

This is the first time I would recommend it to normie/software-literate people who never really wanted to sign up to become a sysadmin and stress about uptime of core personal services.

## Why now is different

Three things converged:

Cheap, capable mini PCs

You can buy a silent, low-power Linux box for less than $500

Tailscale

Simple, secure, private networking

Claude Code

Install the CLI agent
directly on the box
, and you no longer need to remember or look-up Docker syntax, Compose quirks, or config formats

So instead of Googling things like “docker compose vaultwarden caddy reverse proxy” and piecing together a bunch of old blog posts,I just ran Claude Code directly on the machineand let it sort it out.

## The hardware

Fits in one hand. Check that central cooling unit!

I previously ran my Plex server on an M1 Mac mini, which was great, but as I wanted to add more services I found myself running a lot of resource-hungry VMs (via UTM) and it was getting complicated anytime the Mac rebooted. So, I picked up aBeelink Mini N150. It is small, quiet, and just barely sips power. I paid around $379* for the device and another few hundred USD for 8TB in NVMe SSD. It's pretty wild how accessible these mini PCs have become in recent years!

## The basic flow

Install Linux

Flash USB, install Ubuntu Server (I picked 22.04 LTS)

Install Tailscale

Get it on your private network to make your life easier

SSH in

From my laptop, anywhere

Install Claude Code

On the server itself

Ask for what I want

Go get a coffee

## Claude Code is your new sysadmin

I've been using Claude Code and other agentic CLIs for my day-to-day development, but as others are realizing, they are generalized computer agents and native to the terminal.

I installed Claude Code directly on the Linux box. Then I asked it things like:

* Set up Docker
* Create a Docker Compose file
* Install a service
* Put services behind Caddy
* Persist data properly
* Keep my Docker images up to date
* Set up reasonable security packages
* Restart on boot so I never have to futz with it after an outage

Claude Code running directly on the server. Just describe what you want.

I explained the outcome I wanted and let Claude Code take care of the details and implementation.

## What's running

I focused on things I already used, but wanted more control over - effectively starting to knock down the walled garden around my core services like passwords, photos, media.

Service

What it replaces or does

Vaultwarden

Bitwarden, but self-hosted and fast

Plex

Media server - PSA get Plex Pass to unlock hardware-accelerated transcoding

Immich

Google Photos replacement

Uptime Kuma

Simple service monitoring

Caddy

Reverse proxy with automatic TLS

Home Assistant

Home automation hub

Readeck

Read-it-later. Honestly blown away by this one!

Each one lives in its own container.

I can access everything from my phone, laptop, and tablet like it is local.

Uptime Kuma keeping an eye on everything.

Automatic alerts via email give me peace of mind.

When something goes down, I get an email. When it comes back up, another email.

### Vaultwarden as the anchor

Vaultwarden is a Bitwarden-compatible password manager written in Rust. Lightweight, reliable, and you can use the existing Bitwarden clients (like native apps and browser extensions). You can even set it as the default password manager on iOS, at the OS level!

Once that was running, I exported my passwords from iCloud/Keychain, imported them easily into Vaultwarden, and haven't looked back since.

### Immich is actually great

Immich is a Google Photos replacement. I thought I'd have to compromise and flinched a bit when I installed it. But nope, it's good. Mobile apps. Face recognition via a local (but slow) machine learning thread. Timeline and map view. Automatic uploads from your photo roll.

Immich is a feature-rich replacement for Google Photos, complete with a mobile app.

This is the kind of thing that used to feel fragile and half-baked when self-hosted. It does not anymore.

Readeck. No lock-in nor surprise sunsetting.

### Readeck fills the Pocket-shaped hole

Mozilla killed Pocket. I needed a replacement.

I took a bet onReadeck. The UI is genuinely good. Clean typography, nice reading experience, good mobile support. It always remembers where I stopped reading and takes me right there. I even set up a shortcut that allows me to save an article for later right from mobile Firefox. Awesome.

This is exactly the kind of thing self-hosting is perfect for. A small, personal tool that you actually use every day.

## A custom dashboard

I initially installedLazydockerandGlancesfor monitoring. Uptime Kuma works pretty good. Still, it's so easy now to ask: why not do better?I asked Claude to build a single-page monitoring dashboard. It one-shotted it, building a local web app in Go and Svelte (what do I care?) that monitors the status and links out to each service.

Claude Code one-shotted this dashboard, which includes recurring backup jobs

In terms of utilization, 14 different containers use less than 10% of the CPU and about a third of the memory. Plenty of room to grow, perhaps indicating that the Beelink is a bit overkill for my needs.

## EZ backups

Next, I have always wanted a redundant local + remote backup system for my irreplaceable media - namely my photos going back about 25 years now. I plugged in an old USB drive to the Beelink, told Claude to backup to the drive daily, and it was done seconds later.

Finally, I created a new IAM user in the AWS dashboard, installed the AWS CLI on the server, and asked Claude to backup to S3 weekly. On its own, it suggested Glacier Deep storage, which would run me abouttwenty cents per monthfor half a terabyte of photos. A minute or two later, I had remote backups, complete with monitoring + logs from the dashboard.

## What it 'feels' like

The feeling of ownership is powerful, but a bit hard to describe. I think you just have to try it, and I hope you get a strong feeling ofindependencelike I have.

When something breaks, I SSH in, ask the agent what is wrong, and fix it. When I want to add something new, I describe it.

I am spending time using software, learning, and having fun - instead of maintaining it and stressing out about it.

## Who this is for

This is for people who:

* Are comfortable in a terminal
* Already pay for SaaS tools
* Like understanding-ish how things work (how deep your understanding goes is really up to you)
* Do not want to become infra experts

If that is you, I would encourage you to try self-hosting this year.

For the first time, I would say this is not just viable. It's fun!

*Update: I originally incorrectly listed the price of the Beelink as $200. It is actually $379. I've updated this post, but am unable to edit the original post on X. Sorry for the mistake!

Follow me onTwitterfor more.
