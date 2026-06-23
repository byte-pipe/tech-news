---
title: A new unpatchable flaw in Apple chips opens the door to an iPhone jailbreak | TechCrunch
url: https://techcrunch.com/2026/06/22/a-new-unpatchable-flaw-in-apple-chips-opens-the-door-to-an-iphone-jailbreak/
date: 2026-06-22
site: newsfeed
model: gpt-oss:120b-cloud
summarized_at: 2026-06-23T10:21:04.653411
---

# A new unpatchable flaw in Apple chips opens the door to an iPhone jailbreak | TechCrunch

# A new unpatchable flaw in Apple chips opens the door to an iPhone jailbreak

## Overview
- Paradigm Shift, a Barcelona‑based offensive cybersecurity firm, disclosed a Boot ROM vulnerability in Apple’s A12 and A13 chips, named **usbliter8**.  
- The flaw affects iPhones released between 2018‑2019 (e.g., iPhone XS, XR, up to iPhone 11) and requires physical access to the device.

## Technical Details
- usbliter8 exploits immutable code in the Boot ROM, the first code executed when an iPhone powers on.  
- Because the Boot ROM is burned into the chip, the vulnerability cannot be patched; mitigation relies on upgrading to newer hardware.  
- The published proof‑of‑concept shows how an attacker can bypass subsequent security checks after compromising the Boot ROM.

## Implications
- Enables government‑linked spyware and hacking‑tool vendors (e.g., Cellebrite, Magnet Forensics) to add a new entry point for iPhone compromises.  
- Researchers could chain usbliter8 with other vulnerabilities to develop a full iPhone jailbreak, though additional exploits are still required to access user data.  
- Highlights that, despite Apple’s strong security posture, unpatchable hardware flaws can still be leveraged by sophisticated actors.

## Context
- Public iPhone jailbreaks have become rare over the past decade; releasing such flaws publicly would prompt Apple to fix them, reducing researchers’ incentives.  
- Paradigm Shift did not answer follow‑up questions about the vulnerability.

## Key Takeaway
- The usbliter8 bug demonstrates that older iPhone models with A12/A13 chips remain vulnerable to hardware‑level attacks, and the most effective defense is to migrate to newer devices whose Boot ROMs are not affected.