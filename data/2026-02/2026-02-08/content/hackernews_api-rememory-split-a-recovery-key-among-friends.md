---
title: ReMemory - Split a recovery key among friends
url: https://eljojo.github.io/rememory/
site_name: hackernews_api
content_file: hackernews_api-rememory-split-a-recovery-key-among-friends
fetched_at: '2026-02-08T15:30:55.877781'
original_url: https://eljojo.github.io/rememory/
author: eljojo
date: '2026-02-07'
description: An offline tool that encrypts files and splits the decryption key among trusted friends using Shamir's Secret Sharing. Open source.
tags:
- hackernews
- trending
---

# 🧠 ReMemory

This is a tool that encrypts files and splits the decryption key among trusted friends
 usingShamir's Secret Sharing.
 For example, you can give pieces to 5 friends and require any 3 of them to cooperate to recover the key.
 No single friend can access your data alone.

Each friend receives a self-contained bundle withrecover.html—a browser-based tool that works
 offline, with no servers or internet required. If this website disappears, recovery still works.

Create bundles

Read the guide

Source on GitHub

## How it works

Your file is encrypted, the key is split into shares, and friends combine shares to recover it.

Different friend combinations can recover the file (any 3 of 5)

Your File→Encrypt→Split key into 5 shares→Distribute to friends↓Any 3 friends→Combine shares→Decrypt→File recovered

## What this is and isn't

### It is:

* An offline tool that runs in your browser
* A way to split a recovery key among friends
* Open source (Apache-2.0)
* Self-contained—recovery works without this site

### It isn't:

* A service or a company
* An account system or cloud product
* Something that stores your data anywhere
* A backup solution by itself

## Try it in 2 minutes

1. Download the demo bundles(contains 3 sample bundles)
2. Openbundle-alice/recover.htmlin your browser
3. Add Bob's and Carol's shares (drag their README.txt files onto the page)
4. Watch the automatic decryption when threshold is met

This is the best way to understand what your friends would experience during a real recovery.

## On trust and verification

* The code is open source—you canread it on GitHub
* There's aself-audit documentexplaining the cryptographic choices
* Everything runs locally in your browser; your files don't leave your device
* Try the demo bundles first to see exactly how it works before using it with real secrets
* Usesagefor encryption—a well-regarded modern tool

## Why I built this

I wanted a way to ensure trusted friends could access important files if something happened to me—without
 trusting any single person or service with everything. Shamir's Secret Sharing seemed like the right approach,
 but I couldn't find a tool that gave friends a simple, self-contained way to recover files together.
 So I built one. I'm sharing it in case it's useful to others.
