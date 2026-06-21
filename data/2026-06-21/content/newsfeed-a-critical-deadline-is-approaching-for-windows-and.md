---
title: A Critical Deadline Is Approaching for Windows and Linux Security | WIRED
url: https://www.wired.com/story/a-critical-deadline-is-approaching-for-windows-and-linux-security/
site_name: newsfeed
content_file: newsfeed-a-critical-deadline-is-approaching-for-windows-and
fetched_at: '2026-06-21T11:57:35.088021'
original_url: https://www.wired.com/story/a-critical-deadline-is-approaching-for-windows-and-linux-security/
author: Dan Goodin, Ars Technica
date: '2026-06-21'
published_date: '2026-06-21T09:00:00.000Z'
description: The cryptographic keys that secure your computer's boot sequence will start to expire on June 24. Here's what that means for you.
tags:
- wired
- security
- security / security news
- ars technica
---

Save Story
Save this story
Save Story
Save this story

The clock isticking forWindowsandLinuxusers to update cryptographic keys that protect their systems against firmware-basedUEFI infections, a pernicious form of malware that loads before operating system and antimalware protections start.

Beginning June 24, three certificates that cryptographically verify that each piece of firmware and software that loads during system boot will expire. The Microsoft-signed certificates are the linchpins of Secure Boot, a Microsoft-designed chain of trust. Secure Boot checks the digital signatures of all firmware that loads during system startup to ensure it originates from a trusted provider, such as the manufacturer of the motherboard the system runs on.

Secure Boot is designed to thwart UEFI bootkits, a form of malware that alters the Unified Extensible Firmware Interface, the successor to the BIOS, both of which begin the initial boot sequence. Because these bootkits load before the OS and most other code, they can be difficult to detect. Once installed, they typically load malware onto the OS that steals credentials, backdoors the system, or performs other malicious actions. Even when the OS is disinfected, the bootkit can reinfect the system. Bootkits survive OS reinstallations as well.

## A Brief History of Bootkits

The genesis of bootkits dates back to the early 1980s with the creation ofseveral pieces of malwarethat targeted Apple II machines during the boot process. They spread in the wild through floppy disks that ostensibly contained pirated games.

Windows bootkits gained notice in the early 2000s as proofs of concept developed by researchers of offensive security. BootRoot, a bootkitdemonstratedat the 2005 Black Hat security conference, is likely the first such instance. The malware infected the Network Driver Interface, which streamlined communications between network protocol drivers enabling service such as TCP/IP network adapter drivers. In the years following, similar PoCs includedVbootkit, theStoned Bootkit, andMebroot. There were many more.

In 2012, a new form of bootkit was demonstrated. Instead of targeting machines through the BIOS or master boot record,onesuch bootkit attacked Mac OS X systems by infecting the EFI, a package of firmware that started the boot process. Asecondvery primitive bootkit targeted Windows 8 machines by infecting the​​UEFI bootkit, the predecessor to the UEFI. Around 2013, a researcher demonstrated a more advanced UEFI bootkit for Windows namedDreamboat.

The first known case of a real-world attack targeting the UEFI came in 2018 with the discovery of malware dubbedLoJax. A repurposed version of legitimate anti-theft software known as LoJack, it was created by the Kremlin-backed hacking group tracked under names including Sednit, Fancy Bear, and APT 28. The malware was installed remotely using malware tools that can read and overwrite parts of the UEFI firmware’s flash memory.

In 2020, researchers unearthed the second known instance of real-world malware attacking the UEFI. Each time an infected device rebooted, its UEFI checked whether a malicious file was present in the Windows startup folder and, if not, installed it. Researchers from Kaspersky, the security provider that discovered the malware, named it “MosaicRegressor.” Researchers have yet to determine how the compromised UEFIs became infected. Since then, a handful of new UEFI bootkits have come to light. They are tracked under names including ESpecter, FinSpy, and MoonBounce.

## Necessity Is the Mother of Invention

In response to the more menacing threat of UEFI bootkits, Microsoft worked with device makers to develop Secure Boot, an industry-wide standard that uses cryptographic signatures to ensure that each piece of firmware loaded during startup is trusted by a computer’s manufacturer. Secure Boot is designed to create a chain of trust that prevents attackers from replacing the intended bootup firmware with malicious firmware. If a single link in the startup chain isn’t recognized, Secure Boot will prevent the device from starting.

Then in 2023, researchers discoveredLogoFail, a series of critical vulnerabilities found UEFIs booting up just about every Windows and Linux system in the world. An image-parsing bug in the software that presented hardware manufacturers’ logos during bootup allowed attackers to bypass Secure Boot and infect the UEFI with malicious firmware.

The discovery of LogoFail requires Microsoft to replace the existing cryptographic signatures underpinning Secure Boot with new ones. Three older signatures, which are dated 2011, are being removed. In their place are ones dated 2023. Microsoft is in the process of updating Windows 10 and Windows 11 machines. Linux distributors are also in the process of updating “shims,” a small, first-stage UEFI bootloader that acts as a trusted bridge between Secure Boot keys and the Linux bootloader.

Machines that fail to update the Secure Boot-related keys will continue to function, but they will no longer be protected against new UEFI threats. To be clear, they were already vulnerable to new UEFI threats that exploited the industry-wide LogoFail vulnerability. The key refresh is designed to mitigate that risk and prevent unrelated UEFI attacks that may arise in the future.

To check the status of the keys on Windows machines, users can open Windows Security settings > Device Security > Secure Boot. A green checkmark means the update has been completed. Most Windows machines automatically update the keys during regular monthly patch distributions, but older machines may require manual attention. Linux users should watch for the release of new shims.

Microsoft recommends people stay current with all firmware updates, because they’re sometimes needed for Secure Boot certificates to update smoothly. The company has more information on applying firmware updateshere.

This story originally appeared onArs Technica.

## Comments

Back to top
Triangle

## You Might Also Like

* In your inbox:Inside WIRED’s newsroom with Katie Drummond
* Peter Thiel’ssecretive ‘Dialog’ society
* Big Story:'Fishtank' isthe OnlyFans of reality TV
* How Apple is making your old iPhonerun faster and live longer
* Special edition:The future of home
Dan Goodin is IT Security Editor at Ars Technica. ... 
Read More
* X
Topics
Ars Technica
malware
vulnerabilities
Linux
Windows
security
Websites Can Now Spy on You Through Your Hard Drive
Thanks to the newly detailed FROST technique, telltale SSD activity can be measured in the browser using simple JavaScript.
Dan Goodin, Ars Technica
Scammers Are Using Your Real Hotel Reservations to Trick You With Spear-Phishing Attacks
Customer data from more than 350 hotels around the world may have been accessed as part of realistic reservation-hijacking scams.
Matt Burgess
Use Tiny11 to Rescue a Computer Running Windows 10
If you can’t—or don’t want to—upgrade to full Windows 11, consider this lightweight version of Microsoft’s operating system that works on a wide range of computers.
David Nield
Signal Alums Reveal ‘Encrypted Spaces,’ a System for Making Private Collaboration Apps
The new open-source project could serve as the basis for a future of apps with features as complex as Slack, Discord, or Google Docs—but with added protection against surveillance.
Andy Greenberg
Cybercrime Crew Claims It Hacked Mike Lindell’s MyPillow
Plus: A ransomware group is now stealing data in person, BusPatrol wants to hand its license plate surveillance data to the cops, and more.
Matt Burgess
The AI Era Is Creating a Bug-Hunting Arms Race
As attackers ramp up their AI exploit development, the search for software vulnerabilities is changing rapidly.
Lily Hay Newman
AI Agents Plunged the Tech World Into Chaos. Here’s Exactly How That Happened
The definitive story of how Claude Code and OpenClaw kicked off computing’s biggest transformation possibly ever.
Steven Levy
Anthropic Offers Mythos Upgrade for Cyber Partners and a ‘Safe’ Version for the Rest of You
Anthropic is releasing Claude Mythos 5 to trusted organizations and Claude Fable 5 to the public, a version it says can’t be used for cyberattacks.
Maxwell Zeff
Top 1Password Coupons This June 2026
Save up to 28% on business and personal memberships with 1Password promo codes and deals.
Scott Gilbertson
CISA Tells US Agencies to Fix Security Bugs in as Little as 3 Days Thanks to AI Threats
“Defenders cannot afford to take weeks to patch,” one Cybersecurity and Infrastructure Security Agency official warned on Wednesday.
Lily Hay Newman
Here’s How AI Agents Can Protect EV Chargers
An AI agent system proposed by researchers in Spain promises to prevent energy theft and damage to EV chargers, as well as the critical energy infrastructure that powers them.
Fernanda González
Norton Coupon Codes and Deals: 58% Off
Whether you’re looking to protect your small business or your personal computer, we have the top coupons and deals to help you save at Norton.
Scott Gilbertson