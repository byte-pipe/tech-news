---
title: Obsidian Plugin Abused in Social Engineering Campaign to Deliver New PHANTOMPULSE RAT - CyberNetSec.io
url: https://cyber.netsecops.io/articles/obsidian-plugin-abused-in-campaign-to-deploy-phantom-pulse-rat/
site_name: hackernews_api
content_file: hackernews_api-obsidian-plugin-abused-in-social-engineering-campa
fetched_at: '2026-05-11T19:47:24.706452'
original_url: https://cyber.netsecops.io/articles/obsidian-plugin-abused-in-campaign-to-deploy-phantom-pulse-rat/
author: CyberNetSec.io
date: '2026-05-10'
published_date: '2026-04-16T00:00:00.000Z'
description: A sophisticated campaign is abusing the Obsidian note-taking app to deliver a new RAT, PHANTOMPULSE, to targets in the finance and crypto sectors using social engineering and malicious plugins.
tags:
- hackernews
- trending
---

Print
Home
Analysis

Obsidian Plugin Abused in Social Engineering Campaign to Deliver New PHANTOMPULSE RAT

Articles

# Novel Campaign Abuses Obsidian Note-Taking App to Target Finance and Crypto Professionals with PHANTOMPULSE RAT

## Obsidian Plugin Abused in Social Engineering Campaign to Deliver New PHANTOMPULSE RAT

 HIGH
April 16, 2026
5m read
Malware
Threat Actor
Phishing

### Related Entities

#### Threat Actors

REF6598

#### Products & Tech

Obsidian 
PowerShell 
Telegram

#### Other

PHANTOMPULSE
PHANTOMPULL
LinkedIn

### MITRE ATT&CK Techniques

T1566.002
Initial Access

#### Spearphishing Link

T1204.002
Execution

#### Malicious File

T1059.001
Execution

#### PowerShell

T1102.002
Command and Control

#### Bidirectional Communication

T1055
Defense Evasion

#### Process Injection

T1112
Defense Evasion

#### Modify Registry

### Full Report

 Export Markdown 

## Executive Summary

Security researchers have identified a highly targeted social engineering campaign (REF6598) that weaponizes theObsidiannote-taking application to deliver a previously undocumented Remote Access Trojan (RAT) namedPHANTOMPULSE. The campaign targets individuals in the financial and cryptocurrency sectors on both Windows and macOS. Attackers use platforms like LinkedIn and Telegram to build trust before luring victims into a malicious shared Obsidian vault. The attack chain relies on tricking the user into enabling a community plugin, which then executes code to deploy the RAT.PHANTOMPULSEdemonstrates advanced capabilities, including using the Ethereum blockchain to dynamically resolve its command-and-control (C2) server address, making it highly resilient to takedowns.

## Threat Overview

The attack, designated REF6598, is a multi-stage social engineering effort. Threat actors pose as venture capitalists and engage with targets on professional networking sites before moving the conversation to a private Telegram group. The primary lure is an invitation to collaborate via a shared, cloud-hostedObsidianvault.

Once the victim opens the shared vault, the infection is triggered by social engineering. The victim is prompted to enable the "Installed community plugins" synchronization feature. This seemingly innocuous action, which requires manual user approval, is the key to the compromise. It enables malicious versions of legitimateObsidianplugins ('Shell Commands' and 'Hider') that are present in the shared vault.

## Technical Analysis

The attack chain differs slightly between Windows and macOS but follows the same general principle:

1. Initial Access (T1566.002):The attacker uses social engineering on LinkedIn/Telegram to convince the target to open a malicious sharedObsidianvault.
2. Execution (T1204.002):The user is manipulated into enabling community plugins within Obsidian. This action executes a malicious script via the compromised 'Shell Commands' plugin.
3. Staging:On Windows, a PowerShell script is executed. This script drops a loader known asPHANTOMPULL. On macOS, a similar process occurs using AppleScript.
4. Payload Delivery:ThePHANTOMPULLloader decrypts and launches the final payload, thePHANTOMPULSERAT, directly into memory to evade file-based detection (T1055).
5. Command and Control (T1102.002):PHANTOMPULSEuses a novel C2 mechanism. It queries the Ethereum blockchain for the latest transaction from a hard-coded wallet address. The C2 server's IP address is embedded within this transaction data, providing a decentralized and censorship-resistant way for the malware to receive instructions.

Once active,PHANTOMPULSEcan capture keystrokes, take screenshots, exfiltrate files, and execute arbitrary commands.

## Impact Assessment

A successful compromise gives the attacker full access to the victim's machine. For professionals in finance and crypto, this could lead to the theft of sensitive corporate data, intellectual property, trading strategies, and, most critically, cryptocurrency wallet keys and exchange credentials. The cross-platform nature of the attack broadens its potential victim pool. The use of a blockchain-based C2 demonstrates a high level of sophistication, making the threat infrastructure difficult to disrupt.

## Cyber Observables for Detection

Type
process_name
Value
Obsidian.exe
Description
Monitor for Obsidian spawning child processes like 
powershell.exe
, 
cmd.exe
, or 
osascript
.
Type
command_line_pattern
Value
powershell -ExecutionPolicy Bypass
Description
Suspicious PowerShell execution, especially when initiated by a non-standard application like Obsidian.
Type
network_traffic_pattern
Value
Outbound connections to Ethereum blockchain nodes or gateways from unexpected processes.
Description
Could indicate PHANTOMPULSE attempting to resolve its C2 address.
Type
file_path
Value
[Vault]/.obsidian/plugins/
Description
Monitor for the creation or modification of files within the Obsidian plugins directory, especially outside of the official plugin marketplace.

## Detection & Response

1. Process Monitoring (D3-PA: Process Analysis):Implement EDR rules to detect and alert when theObsidianprocess spawns command-line interpreters (powershell.exe,cmd.exe,bash,osascript). This is highly anomalous behavior.
2. User Training:Educate users, especially those in high-risk industries, about the dangers of social engineering and the specific tactic of abusing collaboration tool features like shared vaults and plugins.
3. Application Control (D3-EAL: Executable Allowlisting):Where possible, use application control policies to restrict the installation and execution of unapproved community plugins in applications like Obsidian.
4. Network Monitoring (D3-NTA: Network Traffic Analysis):Monitor for unusual DNS queries or direct IP connections related to blockchain services from endpoints where such activity is not expected.

## Mitigation

1. Vet Community Plugins:Be extremely cautious when enabling third-party or community-developed plugins in any application. Only install plugins from the official, trusted marketplace and review their permissions.
2. Disable Auto-Sync for Untrusted Vaults:Do not enable plugin synchronization when connecting to anObsidianvault from an unknown or untrusted source.
3. Principle of Least Privilege:Run applications likeObsidianas a standard user, not with administrative privileges, to limit the potential impact of a compromise.
4. Endpoint Security:Ensure up-to-date EDR and antivirus solutions are deployed to detect and block suspicious script execution and process injection techniques.

### Timeline of Events

1
April 16, 2026
This article was published

### MITRE ATT&CK Mitigations

#### User Training

M1017
enterprise

Training users to recognize social engineering tactics and be suspicious of unsolicited collaboration requests is the primary defense against this attack vector.

#### Execution Prevention

M1038
enterprise

Using application control to prevent applications like Obsidian from executing scripts (e.g., PowerShell) can break the attack chain.

Mapped D3FEND Techniques:

D3-EAL

#### Software Configuration

M1054
enterprise

Configuring applications to disable or require strict approval for installing third-party plugins reduces the attack surface.

Mapped D3FEND Techniques:

D3-ACH

### Sources & References

Obsidian Plugin Abuse Delivers PHANTOMPULSE RAT in Targeted Finance, Crypto Attacks 
The Hacker News
 (thehackernews.com) 
•
April 16, 2026
New malware scam targets crypto users through Obsidian notes app 
Cryptopolitan
 (cryptopolitan.com) 
•
April 15, 2026
Phantom in the vault: Obsidian abused to deliver PhantomPulse RAT 
SOC Prime
 (socprime.com) 
•
April 14, 2026
Phantom in the vault: Obsidian abused to deliver PhantomPulse RAT - Osint Advisory 
IBM X-Force Exchange
 (exchange.xforce.ibmcloud.com) 
•
April 14, 2026

### Article Author

#### Jason Gomes

• Cybersecurity Practitioner

Cybersecurity professional with over 10 years of specialized experience in security operations, threat intelligence, incident response, and security automation. Expertise spans SOAR/XSOAR orchestration, threat intelligence platforms, SIEM/UEBA analytics, and building cyber fusion centers. Background includes technical enablement, solution architecture for enterprise and government clients, and implementing security automation workflows across IR, TIP, and SOC use cases.

Threat Intelligence & Analysis
Security Orchestration (SOAR/XSOAR)
Incident Response & Digital Forensics
Security Operations Center (SOC)
SIEM & Security Analytics
Cyber Fusion & Threat Sharing
Security Automation & Integration
Managed Detection & Response (MDR)
LinkedIn

### Tags

Malware
RAT
PHANTOMPULSE
Obsidian
Social Engineering
Cryptocurrency
Finance
REF6598

### 📢 Share This Article

Help others stay informed about cybersecurity threats

X
Mastodon
Bluesky
LinkedIn
Reddit
HN
Telegram
Email

### 🎯MITRE ATT&CK Mapped

Every tactic, technique, and sub-technique used in this threat has been identified and mapped to the MITRE ATT&CK framework for consistent, actionable threat language.

### 🧠Enriched & Analyzed

Observables and indicators of compromise (IOCs) have been extracted and cataloged. Risk has been assessed and correlated with known threat actors and historical campaigns.

### 🛡️Actionable Guidance

Detection rules, incident response steps, and D3FEND-aligned mitigation strategies are included so your team can act on this intelligence immediately.

### 🔗STIX Visualizer

Structured threat data is packaged as a STIX 2.1 bundle and can be visualized as an interactive graph — relationships between actors, malware, techniques, and indicators.

### ⚡Sigma Generator

Sigma detection rules are derived from the threat techniques in this article and can be converted for deployment across any major SIEM or EDR platform.

Feedback