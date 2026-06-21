---
title: One-Character Linux Kernel Flaw Enables Local Root Access, Exploits Now Public
url: https://thehackernews.com/2026/06/one-character-linux-kernel-flaw-enables.html
site_name: tldr
content_file: tldr-one-character-linux-kernel-flaw-enables-local-root
fetched_at: '2026-06-22T00:53:12.725511'
original_url: https://thehackernews.com/2026/06/one-character-linux-kernel-flaw-enables.html
author: The Hacker News
date: '2026-06-22'
description: CVE-2026-23111 is a Linux kernel nf_tables use-after-free that lets an unprivileged local user escalate to root and escape a container.
tags:
- tldr
---

# One-Character Linux Kernel Flaw Enables Local Root Access, Exploits Now Public


Swati Khandelwal

Jun 08, 2026
Linux / Vulnerability

Security researchers have published a detailed, working exploit for a Linux kernel use-after-free that lets an unprivileged local user escalate to root and break out of a container.

The flaw, CVE-2026-23111, sits in the kernel's nf_tables packet-filtering code and waspatched upstreamon February 5, 2026. Exodus Intelligence released itsfull technical walkthroughon June 8, and it is not even the first public exploit: FuzzingLabs published anindependent reproductionback in April.

The flaw came down to a single stray character, an inverted check in nf_tables, and the upstream fix removed it in one line. Ubuntu rates the flaw CVSS 7.8 (high). If your distribution's kernel package does not yet include the fix, update and reboot.

The reachable setup is common: nf_tables plus unprivileged user namespaces, a Linux feature that lets an ordinary account act as root inside a private sandbox and reach kernel code it otherwise could not.

Both ship by default on most desktops and many server builds. There is no remote vector on its own. This is a bug that an attacker reaches for after getting a foothold, turning a low-privileged shell, a compromised container, or a service account into root on the host.

Exodus researcher Oliver Sieber, who found the bug in early 2025, chained it into a full local root. The exploit sets off the use-after-free, works around the kernel's built-in memory protections, then seizes control of execution to grant itself root and break out of the container's namespace.

He demonstrated it on Debian Bookworm, Debian Trixie, Ubuntu 22.04 LTS, and Ubuntu 24.04 LTS.

FuzzingLabs reproduced the bug on RHEL 10 ahead of Pwn2Own Berlin 2026, building its own root exploit by a different route. The timeline is tight: the fix shipped February 5, FuzzingLabs published April 16, and Exodus's detailed write-up landed June 8.

The technique is now documented across Debian, Ubuntu, and Red Hat. Because the bug is in the mainline, any distribution that shipped a vulnerable kernel with both features enabled is exposed, unless a distribution's hardening or namespace restrictions block the path.

CVE-2026-23111 lands in the middle of a heavy run of Linux local-root disclosures. Recent weeks have broughtCopy Fail, theDirty Fragchain, itsFragnesiavariant,DirtyDecrypt, and anine-year-old ptrace flawthat reads /etc/shadow and runs commands as root.

They differ in the details, but share the part that should worry defenders: an unprivileged foothold keeps turning into root on ordinary installs.

Update the kernel and reboot. The bug is local-only and needs unprivileged user namespaces, so focus first on systems that let untrusted users or workloads create them.

Ubuntu has fixes for 22.04, 24.04, and 25.10, and Debian fixed Bookworm and Trixie, with a 6.1 backport for Bullseye LTS. Red Hat, SUSE, and Amazon Linux track the flaw as well; check your distribution's advisory for the kernel package that matches yours, since the exact fixed version varies. The fix upstream was a single line of code.

There is a bigger picture. In arecent review of the LPE surge, Synacktiv links the pace to AI-assisted research and patch-diffing that put working exploits out before fixes spread, and makes the case that ordinary hardening still buys defenders time.

Most of these bugs lean on optional kernel features or loose defaults, so cutting off what unprivileged users can reach, user namespaces in this case, holds the exploit off until the patch is in.

There are no public reports of exploitation in the wild, and no threat actor has been tied to it. The patch has been out since February, and exploit code has been public since April.

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

Container Security
, 
Debian
, 
Kernel
, 
linux
, 
privilege escalation
, 
Ubuntu
, 
Vulnerability

⚡ Top Stories This Week

Chrome V8 Zero-Day CVE-2026-11645 Exploited in the Wild - Patch Now

Researchers Build Self-Replicating AI Worm That Operates Entirely on Local, Open-Weight Models

Microsoft Defender RoguePlanet Zero-Day Grants SYSTEM Access on Updated Windows

Anthropic Releases Claude Fable 5, Its Most Powerful AI Yet, With Cyber Safeguards

Microsoft Patches Record 206 Flaws, Including Three Zero-Days and Critical RCE Bugs

Ivanti, Fortinet, and SAP Release Patches for Multiple Critical Vulnerabilities

Cybersecurity Stars Awards 2026: Winners Announced Across 95 Categories

ThreatsDay Bulletin: Worm Code Leaked, AI Agent Phished, Claude Code Patch + 28 New Stories

New GreatXML Exploit Bypasses Windows BitLocker via Recovery Partition XML Files

Agentjacking Attack Tricks AI Coding Agents Into Running Malicious Code

China-Linked Hackers Backdoored Linux Login Software to Hide for Nearly a Decade

Critical Splunk Enterprise Flaw Lets Attackers Run Code Without Authentication

U.S. Orders Anthropic to Suspend Fable 5 and Mythos 5 Access for Foreign Nationals

Over 400 Arch Linux AUR Packages Hijacked to Deploy Infostealer and eBPF Rootkit

Palo Alto Warns of Active Exploitation of PAN-OS GlobalProtect VPN Flaw

⚡ Weekly Recap: Chrome 0-Day, UniFi Exploits, macOS Stealers, VPN Flaw and More

⭐ Featured Resources

Get the 2026 Guide to Govern and Secure Enterprise AI Agents at Scale

[Watch Demo] See Which Security Gaps Attackers Could Exploit First

AI Can’t Stop Every Attack. Learn How Zero Trust Can Block What’s Unknown

Have You Outgrown Your MDR? 7 Warning Signs Every CISO Should Check