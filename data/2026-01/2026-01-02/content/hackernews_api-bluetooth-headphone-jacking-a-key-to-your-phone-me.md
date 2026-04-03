---
title: 'Bluetooth Headphone Jacking: A Key to Your Phone - media.ccc.de'
url: https://media.ccc.de/v/39c3-bluetooth-headphone-jacking-a-key-to-your-phone
site_name: hackernews_api
fetched_at: '2026-01-02T11:07:35.107741'
original_url: https://media.ccc.de/v/39c3-bluetooth-headphone-jacking-a-key-to-your-phone
author: AndrewDucker
date: '2026-01-01'
description: Bluetooth headphones and earbuds are everywhere, and we were wondering what attackers could abuse them for. Sure, they can probably do th...
tags:
- hackernews
- trending
---

# Bluetooth Headphone Jacking: A Key to Your Phone

Dennis HeinzeandFrieder Steinmetz

One

Security

Playlists:

'39c3' videos starting here

/

audio

* 59 min
* 2025-12-27
* 2025-12-28
* 23.4k
* Fahrplan

Bluetooth headphones and earbuds are everywhere, and we were wondering what attackers could abuse them for. Sure, they can probably do things like finding out what the person is currently listening to. But what else? During our research we discovered three vulnerabilities (CVE-2025-20700, CVE-2025-20701, CVE-2025-20702) in popular Bluetooth audio chips developed by Airoha. These chips are used by many popular device manufacturers in numerous Bluetooth headphones and earbuds.The identified vulnerabilities may allow a complete device compromise. We demonstrate the immediate impact using a pair of current-generation headphones. We also demonstrate how a compromised Bluetooth peripheral can be abused to attack paired devices, like smartphones, due to their trust relationship with the peripheral.This presentation will give an overview over the vulnerabilities and a demonstration and discussion of their impact. We also generalize these findings and discuss the impact of compromised Bluetooth peripherals in general. At the end, we briefly discuss the difficulties in the disclosure and patching process. Along with the talk, we will release tooling for users to check whether their devices are affected and for other researchers to continue looking into Airoha-based devices.Examples of affected vendors and devices are Sony (e.g., WH1000-XM5, WH1000-XM6, WF-1000XM5), Marshall (e.g. Major V, Minor IV), Beyerdynamic (e.g. AMIRON 300), or Jabra (e.g. Elite 8 Active).Airoha is a vendor that, amongst other things, builds Bluetooth SoCs and offers reference designs and implementations incorporating these chips. They have become a large supplier in the Bluetooth audio space, especially in the area of True Wireless Stereo (TWS) earbuds. Several reputable headphone and earbud vendors have built products based on Airoha’s SoCs and reference implementations using Airoha’s Software Development Kit (SDK).During our Bluetooth Auracast research we stumbled upon a pair of these headphones. During the process of obtaining the firmware for further research we initially discovered the powerful custom Bluetooth protocol called *RACE*. The protocol provides functionality to take full control of headphones. Data can be written to and read from the device's flash and RAM.The goal of this presentation is twofold. Firstly, we want to inform about the vulnerabilities. It is important that headphone users are aware of the issues. In our opinion, some of the device manufacturers have done a bad job of informing their users about the potential threats and the available security updates. We also want to provide the technical details to understand the issues and enable other researchers to continue working with the platform. With the protocol it is possible to read and write firmware. This opens up the possibility to patch and potentially customize the firmware.Secondly, we want to discuss the general implications of compromising Bluetooth peripherals. As smart phones are becoming increasingly secure, the focus for attackers might shift to other devices in the environment of the smart phone. For example, when the Bluetooth Link Key, that authenticates a Bluetooth connection between the smart phone and the peripheral is stolen, an attacker might be able to impersonate the peripheral and gain its capabilities.Licensed to the public under http://creativecommons.org/licenses/by/4.0

### Download

### Embed

<iframe width="1024" height="576" src="https://media.ccc.de/v/39c3-bluetooth-headphone-jacking-a-key-to-your-phone/oembed" frameborder="0" allowfullscreen></iframe>

### Share:

### Tags

1491

2025

39c3

Security

One

39c3-eng

39c3-deu

39c3-fra

Day 1
