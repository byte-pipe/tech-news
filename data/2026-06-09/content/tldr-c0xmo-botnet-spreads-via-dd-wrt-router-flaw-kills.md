---
title: C0XMO botnet spreads via DD-WRT router flaw, kills rival malware
url: https://www.bleepingcomputer.com/news/security/c0xmo-botnet-spreads-via-dd-wrt-router-flaw-kills-rival-malware/
site_name: tldr
content_file: tldr-c0xmo-botnet-spreads-via-dd-wrt-router-flaw-kills
fetched_at: '2026-06-09T12:03:16.255324'
original_url: https://www.bleepingcomputer.com/news/security/c0xmo-botnet-spreads-via-dd-wrt-router-flaw-kills-rival-malware/
date: '2026-06-09'
description: A new variant of the Gafgyt botnet called C0XMO is targeting DD-WRT router firmware and can move to other device types with various CPU architectures.
tags:
- tldr
---

# C0XMO botnet spreads via DD-WRT router flaw, kills rival malware

 By 

###### Bill Toulas

* June 7, 2026
* 10:17 AM
* 0

A new variant of the Gafgyt botnet called C0XMO is targeting DD-WRT router firmware and can move to other device types with various CPU architectures.

The researchers found samples for ARM, MIPS, PowerPC, SuperH, x86, x86_64, and other architectures, featuring exploits for DVRs, routers, video management platforms, and Android-based devices.

The botnet was seen targeting a Japanese technology company, but researchers discovered that the source IP address was for a device located in Germany.

Fortinet researchers discovered C0XMO and highlighted its modular design, which allows operators to update its exploitation techniques, add/remove targeted architectures, and expand its lateral movement capabilities independently of the main payload.

Fundamentally, C0XMO remains a malware for launching distributed denial-of-service (DDoS) attacks and supports 19 methods, including UDP/TCP/SYN/ICMP floods, “ping of death,” NTP/Memcached amplification, Discord voice UDP floods, and Valve-specific floods.

According to the researchers, the C0XMO botnet malware is delivered by exploiting CVE-2021-27137, a buffer overflow vulnerability caused by insufficient user input. It can be leveraged without authentication and leads to executing arbitrary code.

### Gafgyt scanner

For wider distribution, C0XMO downloads a Python script that installs additional packages such as ‘requests,’ ‘paramiko,’ and ‘beautifulsoup4,’ which are required for network scanning and communication, and for running activities over SSH and telnet protocols.

The scanner then uses worker threads to randomly scan internet-facing systems on common ports like 22 (SSH), 23 (Telnet), 80/443 (HTTP/HTTPS), 7547, 8080, 8443, 8888, and others.

After finding a target, the malware attempts to brute-force weak Telnet and SSH credentials, detects the CPU architecture, and deploys a compatible C0XMO binary.

The script contains almost two dozen functions for various tasks for scanning, exploiting HTTP and ADB-based vulnerabilities, detecting the CPU architecture, SSH/telenet login, and checking IP addresses. Its main purpose is to move laterally on the network.

Once it gains access to a device, the malware copies itself to hidden locations such as ‘/tmp/.sys,’ ‘/var/tmp/.sys,’ and ‘/dev/shm/.sys,’ and then creates cron jobs that relaunch it every 15 minutes. Also, shell startup files are modified to enable automatic execution.

Furthermore, C0XMO actively scans running processes to identify competitor botnet clients on the host, as well as red-team tools, programming tools, and network services that may interfere with its operation, and terminates them.

It does so by deleting binaries and removing their persistence mechanisms, including cron jobs, init scripts, system services, and shell profile entries.

List of processes the malware checks for
Source: Fortinet

After that, it connects to a hardcoded command-and-control (C2) address using a custom multi-stage handshake that includes magic strings and shared secrets, and then awaits commands.

The supported commands include heartbeat checks, starting and stopping scans, and launching DDoS attacks using one of the 19 supported methods.

The general recommendation for defending against C0XMO and other botnet malware is to keep devices up to date, use unique admin credentials, and disable remote access capabilities when not needed.

Fortinet describes C0XMO as having "a considerably more advanced architecture and feature set compared to earlier IoT botnets."

The researchers note that the overall design of the malware indicates "a greater degree of operational sophistication and complexity than typical Gafgyt malware."

## Test every layer before attackers do

Security teams log 54% of successful attacks and alert on just 14%. The rest move through your environment unseen.

The Picus whitepaper shows how breach and attack simulation tests your SIEM and EDR rules so threats stop slipping by detection.

Get the whitepaper

### Related Articles:

Dutch govt disrupts malware botnet with 17 million infected devices

US and Canada arrest and charge suspected Kimwolf botnet admin

Google accidentally exposed details of unfixed Chromium flaw

Russian hackers turn Kazuar backdoor into modular P2P botnet

New Mirai campaign exploits RCE flaw in EoL D-Link routers