---
title: The Tor Project is Making a Switch to Rust, Ditches C
url: https://itsfoss.com/news/tor-rust-rewrite-progress/
site_name: hackernews
fetched_at: '2025-12-12T19:08:15.579193'
original_url: https://itsfoss.com/news/tor-rust-rewrite-progress/
author: giuliomagnifico
date: '2025-12-12'
published_date: '2025-12-11T12:32:52.000Z'
description: Arti, the Rust rewrite of Tor, brings circuit isolation and onion service improvements in its 1.8.0 release.
---

# The Tor Project is Making a Switch to Rust, Ditches C

Arti, the Rust rewrite of Tor, brings circuit isolation and onion service improvements in its 1.8.0 release.











Sourav Rudra

11 Dec 2025

2 min read

On this page



TheTor Projecthas been busy with the rustification of their offering for quite some time now.

If you have used Tor Browser, you know what it does. Anonymous browsing through encrypted relay chains. The network itself has been running since the early 2000s. All of it is built onC.

But that C codebase is an issue. It is known to have buffer overflows, use-after-free bugs, and memory corruption vulnerabilities. That is why they introducedArti, aRustrewrite of Tor thattackles these flawsby leveraging the memory safety of the programming language.

Anew release of Artijust dropped last week, so let's check it out!

## Arti 1.8.0: What's New?

Source: The Tor Project

We begin with the main highlight of this release, the rollout of thecircuit timeout reworkthat was laid out inproposal 368. Tor currently uses something calledCircuit Dirty Timeout(CDT). It is a single timer that controls when your connection circuits become unavailable and when they close down.

Unfortunately, it is predictable. Someone monitoring traffic can spot these patterns and potentially track your activity. Arti 1.8.0 fixes this by implementing usage-based timeouts with separate timers. One handles when circuits accept new connections. Another closes idle circuits at random times instead of fixed intervals.

This should reduce the risk offingerprintingfrom predictable timeout behavior.

Next up is the new experimentalarti hsc ctor-migratecommand that lets onion service operators migrate their restricted discovery keys from the C-based Tor to Arti's keystore.

These keys handle client authorization foronion services. The command transfers them over without requiring operators to do the manual legwork. The release also delivers improvements for routing architecture, protocol implementation, directory cache support, and OR port listener configuration.

You can go throughthe changelogto learn more about the Arti 1.8.0 release.

Via:Sam Bent

Suggested Read 📖: Is Heliumthe Browser Brave Was Meant to Be?

Is Helium the Browser Brave Was Meant to Be?
An in-depth look at ’another new Chromium-based web browser” that is “different from the other Chromium-based web browsers”.
It's FOSS
Roland Taylor

News

About the author



## Sourav Rudra

A nerd with a passion for open source software, custom PC builds, motorsports, and exploring the endless possibilities of this world.
