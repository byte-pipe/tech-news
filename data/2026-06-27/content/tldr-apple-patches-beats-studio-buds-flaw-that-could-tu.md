---
title: Apple patches Beats Studio Buds flaw that could turn earbuds into a wiretap | Malwarebytes
url: https://www.malwarebytes.com/blog/bugs/2026/06/apple-patches-beats-studio-buds-flaw-that-could-turn-earbuds-into-a-wiretap
site_name: tldr
content_file: tldr-apple-patches-beats-studio-buds-flaw-that-could-tu
fetched_at: '2026-06-27T19:33:22.426166'
original_url: https://www.malwarebytes.com/blog/bugs/2026/06/apple-patches-beats-studio-buds-flaw-that-could-turn-earbuds-into-a-wiretap
author: Pieter Arntz
date: '2026-06-27'
published_date: '2026-06-19T11:47:16+00:00'
description: Apple has patched a year-old Bluetooth vulnerability that could have let nearby attackers listen through Beats Studio Buds' microphone.
tags:
- tldr
---

Bugs
, 
News
 

# Apple patches Beats Studio Buds flaw that could turn earbuds into a wiretap

 

 by 
Pieter Arntz
 |
 
June 19, 2026

Apple has patched a Bluetooth flaw in Beats Studio Buds that could potentially turn your earbuds into a nearby wiretap.

When you buy a pair of Bluetooth earbuds, you expect them to play your music and your calls—not someone else’s. But a vulnerability in Apple’s Beats Studio Buds shows how that trust can be abused, turning everyday audio gear into a potential eavesdropping tool for anyone close enough and skilled enough to exploit it.

The vulnerability is tracked asCVE-2025-20701. Researchersdisclosedflaws in Airoha system-on-a-chip (SoCs) devices at a security conference in Germany in 2025. Because Airoha chips are used in a wide range of audio products, the issue affected multiple devices, including Beats Studio Buds.

The researchers also showed how the vulnerability could be combined with flaws theyfound in the same Airoha component. By chaining these flaws, attackers could:

* Eavesdrop via headphone microphones.
* Extract pairing keys.
* Impersonate trusted headphones.
* Compromise the user’s phone, enabling call hijacking, contact extraction, triggering voice assistants, and more.

The good news is that these attacks are not easy to pull off. Exploitation is complex, and the attacker must be within Bluetooth range of the target device.

Basically, CVE-2025-20701 is a flaw in the authentication process and affects devices that are not yet paired and are actively looking for something to connect to. In a normal scenario, your headphones and your phone go through a pairing process that establishes keys and trust before any sensitive operations—like using the microphone—are allowed.

In this case, devices in pairing mode did not properly verify who they were talking to. That opened a window where any nearby attacker could pose as a legitimate partner and connect to the earbuds before the user completes the pairing process.

As Apple describes it:

“An attacker within Bluetooth range may be able to listen through the microphone of a device which is not yet paired and actively seeking pair requests.”

## How to stay safe

To address this vulnerability, Apple shipped Beats Firmware Update 1B211, which rolls out automatically once the earbuds are near and connected to an iPhone, iPad, or Mac.

For the average user, the need for physical proximity, specialized hardware and software, and some patience means opportunistic criminals are more likely to stick with phishing and credential stuffing than stalking Bluetooth signals in public spaces.

But for a motivated attacker targeting a high-profile individual, this is exactly the kind of bug they’d use.

There is no “Update now” button, but if you own Beats Studio Buds and use them with an iPhone, iPad, or Mac, you should automatically receive the update when:

* The earbuds are paired with your Apple device
* They are in their charging case, with the lid closed
* The case and buds have sufficient charge, and the Apple device is nearby with Bluetooth enabled

To check whether you’re protected:

* On iOS or iPadOS, go toSettings>Bluetooth
* Tap theinfoicon next to your Beats Studio Buds
* Look at the firmware or version number. It should read1B211if the security update has been applied. If it says anything else, your earbuds may not have received the update yet. If you see an older version, keep the earbuds in their case near your iPhone, iPad, or Mac for a while to give them time to update. This can take some time and may happen silently in the background, so checking again later is worth the effort.

Scammers know more about you than you think.

Malwarebytes Mobile Security protects you from phishing, scam texts, malicious sites, and more. With real-time AI-powered Scam Guard built right in.

Download for iOS →Download for Android →

SHARE THIS ARTICLE

### About the author

Pieter Arntz

Malware Intelligence Researcher

Was a Microsoft MVP in consumer security for 12 years running. Can speak four languages. Smells of rich mahogany and leather-bound books.

 

#### LATEST ARTICLES

News
 

 

#### Malware steals Chrome session cookies to take over your accounts

June 26, 2026

A phishing campaign installs a malicious Chrome extension to hijack browser sessions and compromise Windows devices.

Bugs
 

 

#### PixelSmash flaw turns video files into attack tools

June 24, 2026

Researchers have found a critical FFmpeg flaw that could let attackers use a malicious video file to compromise vulnerable systems.

Product
 

 

#### Watch out for renewal scams pretending to be Malwarebytes

June 24, 2026

Scammers are sending fake software renewal notices that claim you've been charged for a subscription. Some even impersonate Malwarebytes.

 

Contributors

Threat Center

Podcast

Glossary

Scams