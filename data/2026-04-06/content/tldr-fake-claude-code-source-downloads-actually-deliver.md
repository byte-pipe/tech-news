---
title: Fake Claude Code source downloads actually delivered malware • The Register
url: https://www.theregister.com/2026/04/02/trojanized_claude_code_leak_github/
site_name: tldr
content_file: tldr-fake-claude-code-source-downloads-actually-deliver
fetched_at: '2026-04-06T01:01:37.477040'
original_url: https://www.theregister.com/2026/04/02/trojanized_claude_code_leak_github/
date: '2026-04-06'
description: Fake Claude Code source downloads actually delivered malware (2 minute read)
tags:
- tldr
---

#### Security

# They thought they were downloading Claude Code source. They got a nasty dose of malware instead

 

## Source code with a side of Vidar stealer and GhostSocks

Tens of thousands of people eagerly downloaded the leaked Claude Code source code this week, and some of those downloads came with a side of credential-stealing malware.

A malicious GitHub repository published by idbzoomh uses theClaude Code exposureas a lure to trick people into downloading malware, includingVidar, an infostealer that snarfs account credentials, credit card data, and browser history; andGhostSocks, which is used to proxy network traffic.

Zscaler's ThreatLabz researchers came across the repo while monitoring GitHub for threats, and said it's disguised as a leaked TypeScript source code for Anthropic's Claude Code CLI.

"The README file even claims the code was exposed through a .map file in the npm package and then rebuilt into a working fork with 'unlocked' enterprise features and no message limits," the security sleuthssaidin a Thursday blog.

They added that the GitHub repository link appeared near the top of Google results for searches like "leaked Claude Code." While that was no longer the case atThe Register's time of publication, at least two of the developer's trojanized Claude Code source leak repos remained on GitHub, and one of them had 793 forks and 564 stars.

* Anthropic goes nude, exposes Claude Code source by accident
* Claude Code source leak reveals how much info Anthropic can hoover up about you and your system
* Malware-laced OpenClaw installers get Bing AI search boost
* AI agents are 'gullible' and easy to turn into your minions

The malicious .7z archive in the repository's releases section is named Claude Code - Leaked Source Code, and it includes a Rust-based dropper named ClaudeCode_x64.exe.

Once it's executed, the malware drops Vidar v18.7 and GhostSocks onto users' machines, and then the Vidar stealer gets to work collecting sensitive data while GhostSocks turns infected devices intoproxy infrastructurethat criminals can use to mask their true online location and carry out additional activity through compromised computers.

In March, security shop Huntress warned about asimilar malware campaign using OpenClaw, the already risky AI agent platform, as a GitHub lure to deliver the same two payloads.

Both of these illustrate how quickly criminals move to take a buzzy new product or news event (like OpenClaw and the Claude Code leak) and then abuse it for online scams and financial gain. "That kind of rapid movement increases the chance of opportunistic compromise, especially through trojanized repositories," the Zscaler team wrote.

The blog also includes a list of indicators of compromise, including the GitHub repositories with the trojanized Claude Code leak and malware hashes to help defenders in their threat-hunting efforts, so be sure to check that out - and, as always, be careful what you download. ®

 

Get our
 
Tech Resources

Share

#### More about

* AI
* Claude
* Cybercrime

More like these

×

### More about

* AI
* Claude
* Cybercrime
* Security
* Zscaler

### Narrower topics

* 2FA
* Advanced persistent threat
* AIOps
* Application Delivery Controller
* Authentication
* BEC
* Black Hat
* BSides
* Bug Bounty
* Center for Internet Security
* CHERI
* CISO
* Common Vulnerability Scoring System
* Cybersecurity
* Cybersecurity and Infrastructure Security Agency
* Cybersecurity Information Sharing Act
* Data Breach
* Data Protection
* Data Theft
* DDoS
* DeepSeek
* DEF CON
* Digital certificate
* Encryption
* End Point Protection
* Exploit
* Firewall
* Gemini
* Google AI
* Google Project Zero
* GPT-3
* GPT-4
* Hacker
* Hacking
* Hacktivism
* Identity Theft
* Incident response
* Infosec
* Infrastructure Security
* Kenna Security
* Large Language Model
* Machine Learning
* MCubed
* NCSAM
* NCSC
* Neural Networks
* NLP
* Palo Alto Networks
* Password
* Personally Identifiable Information
* Phishing
* Quantum key distribution
* Ransomware
* Remote Access Trojan
* Retrieval Augmented Generation
* REvil
* RSA Conference
* Software Bill of Materials
* Spamming
* Spyware
* Star Wars
* Surveillance
* Tensor Processing Unit
* TLS
* TOPS
* Trojan
* Trusted Platform Module
* Vulnerability
* Wannacry
* Zero trust

### Broader topics

* Anthropic
* Self-driving Car

#### More about

Share

#### More about

* AI
* Claude
* Cybercrime

More like these

×

### More about

* AI
* Claude
* Cybercrime
* Security
* Zscaler

### Narrower topics

* 2FA
* Advanced persistent threat
* AIOps
* Application Delivery Controller
* Authentication
* BEC
* Black Hat
* BSides
* Bug Bounty
* Center for Internet Security
* CHERI
* CISO
* Common Vulnerability Scoring System
* Cybersecurity
* Cybersecurity and Infrastructure Security Agency
* Cybersecurity Information Sharing Act
* Data Breach
* Data Protection
* Data Theft
* DDoS
* DeepSeek
* DEF CON
* Digital certificate
* Encryption
* End Point Protection
* Exploit
* Firewall
* Gemini
* Google AI
* Google Project Zero
* GPT-3
* GPT-4
* Hacker
* Hacking
* Hacktivism
* Identity Theft
* Incident response
* Infosec
* Infrastructure Security
* Kenna Security
* Large Language Model
* Machine Learning
* MCubed
* NCSAM
* NCSC
* Neural Networks
* NLP
* Palo Alto Networks
* Password
* Personally Identifiable Information
* Phishing
* Quantum key distribution
* Ransomware
* Remote Access Trojan
* Retrieval Augmented Generation
* REvil
* RSA Conference
* Software Bill of Materials
* Spamming
* Spyware
* Star Wars
* Surveillance
* Tensor Processing Unit
* TLS
* TOPS
* Trojan
* Trusted Platform Module
* Vulnerability
* Wannacry
* Zero trust

### Broader topics

* Anthropic
* Self-driving Car

#### TIP US OFF

Send us news