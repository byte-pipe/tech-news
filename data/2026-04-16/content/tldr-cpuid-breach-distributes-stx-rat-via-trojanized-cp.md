---
title: CPUID Breach Distributes STX RAT via Trojanized CPU-Z and HWMonitor Downloads
url: https://thehackernews.com/2026/04/cpuid-breach-distributes-stx-rat-via.html
site_name: tldr
content_file: tldr-cpuid-breach-distributes-stx-rat-via-trojanized-cp
fetched_at: '2026-04-16T11:58:56.142028'
original_url: https://thehackernews.com/2026/04/cpuid-breach-distributes-stx-rat-via.html
author: The Hacker News
date: '2026-04-16'
description: CPUID breach served STX RAT via trojanized CPU-Z downloads on April 9–10, impacting 150+ victims and multiple industries.
tags:
- tldr
---

# CPUID Breach Distributes STX RAT via Trojanized CPU-Z and HWMonitor Downloads


Ravie Lakshmanan

Apr 12, 2026
Malware / Threat Intelligence

Unknown threat actors compromised CPUID ("cpuid[.]com"), a website that hosts popular hardware monitoring tools like CPU-Z, HWMonitor, HWMonitor Pro, and PerfMonitor, for less than 24 hours to serve malicious executables for the software and deploy a remote access trojan called STX RAT.

The incident lasted from approximately April 9, 15:00 UTC, to about April 10, 10:00 UTC, with the download URLs for CPU-Z and HWMonitor installers replaced with links to malicious websites.

In apostshared on X, CPUID confirmed the breach, attributing it to a compromise of a "secondary feature (basically a side API)" that caused the main site to randomly display malicious links. It's worth noting that the attack did not impact its signed original files.

According toKaspersky, the names of the rogue websites are as follows -

* cahayailmukreatif.web[.]id
* pub-45c2577dbd174292a02137c18e7b1b5a.r2[.]dev
* transitopalermo[.]com
* vatrobran[.]hr

"The trojanized software was distributed both as ZIP archives and as standalone installers for the aforementioned products," the Russian cybersecurity company said. "These files contain a legitimate signed executable for the corresponding product and a malicious DLL, which is named 'CRYPTBASE.dll' to leverage the DLL side-loading technique."

The malicious DLL, for its part, contacts an external server and executes additional payloads, but not before performing anti-sandbox checks to sidestep detection. The end goal of the campaign is to deploySTX RAT, a RAT with HVNC and broad infostealer capabilities.

STX RAT "exposes a broad command set for remote control, follow-on payload execution, and post-exploitation actions (e.g., in-memory execution of EXE/DLL/PowerShell/shellcode, reverse proxy/tunneling, desktop interaction)," eSentire said in an analysis of the malware last week.

The command-and-control (C2) server address and the connection configuration have been reused from aprior campaignthat leveraged trojanizedFileZilla installershosted on bogus sites to deploy the same RAT malware. The activity was documented by Malwarebytes early last month.

Breakglass Intelligence, in its ownanalysis of the CPUID hack, said the attack was part of a 10-month campaign that commenced in July 2025, when the earliest known sample ("superbad.exe") was observed communicating with the C2 address ("95.216.51[.]236"). It's assessed that the breach is the work of a Russian-speaking threat actor who is either financially motivated or operates as an initial access broker.

Kaspersky said it has identified more than 150 victims, mostly individuals who were affected by the incident. However, organizations in retail, manufacturing, consulting, telecommunications, and agriculture have also been impacted. Most of the infections are located in Brazil, Russia, and China.

"The gravest mistake attackers made was to reuse the same infection chain involving STX RAT, and the same domain names for C2 communication, from the previous attack related to fake FileZilla installers," Kaspersky said. "The overall malware development/deployment and operational security capabilities of the threat actor behind this attack are quite low, which, in turn, made it possible to detect the watering hole compromise as soon as it started."

(The story was updated after publication on April 13, 2026, to include additional insights from Breakglass Intelligence.)

Found this article interesting? Follow us on 
Google News
, 
Twitter
 and 
LinkedIn
 to read more exclusive content we post.

SHARE










Tweet


Share


Share


Share

SHARE 


cybersecurity
, 
data theft
, 
DLL Sideloading
, 
Incident response
, 
Malware
, 
Remote Access Trojan
, 
supply chain attack
, 
Threat Intelligence
, 
watering hole

Trending News

Microsoft Warns of WhatsApp-Delivered VBS Malware Hijacking Windows via UAC Bypass

New Chrome Zero-Day CVE-2026-5281 Under Active Exploitation — Patch Released

Apple Expands iOS 18.7.7 Update to More Devices to Block DarkSword Exploit

Hackers Exploit CVE-2025-55182 to Breach 766 Next.js Hosts, Steal Credentials

New SparkCat Variant in iOS, Android Apps Steals Crypto Wallet Recovery Phrase Images

Microsoft Details Cookie-Controlled PHP Web Shells Persisting via Cron on Linux Servers

Fortinet Patches Actively Exploited CVE-2026-35616 in FortiClient EMS

Block the Prompt, Not the Work: The End of "Doctor No"

BKA Identifies REvil Leaders Behind 130 German Ransomware Attacks

⚡ Weekly Recap: Axios Hack, Chrome 0-Day, Fortinet Exploits, Paragon Spyware and More

China-Linked Storm-1175 Exploits Zero-Days to Rapidly Deploy Medusa Ransomware

New GPUBreach Attack Enables Full CPU Privilege Escalation via GDDR6 Bit-Flips

Docker CVE-2026-34040 Lets Attackers Bypass Authorization and Gain Host Access

Anthropic's Claude Mythos Finds Thousands of Zero-Day Flaws Across Major Systems

AI Will Change Cybersecurity. Humans Will Define Its Success. A Lesson No Algorithm Can Teach

The AI Arms Race – Why Unified Exposure Management Is Becoming a Boardroom Priority

Popular Resources

Learn How to Block Breached Passwords in Active Directory Before Attacks

Get Full Visibility into Vendor and Internal Risk in One Platform

[Guide] Get Practical Steps to Govern AI Agents with Runtime Controls

Secure Your AI Systems Across the Full Lifecycle of Risks