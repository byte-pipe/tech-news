---
title: 'GitHub - SnailSploit/Claude-Red: claude-red is a curated library of offensive security skills designed for the Claude skills system. Each skill is a structured SKILL.md file that primes Claude with expert-level methodology for a specific attack surface — from SQLi to shellcode, EDR evasion to exploit development. · GitHub'
url: https://github.com/SnailSploit/Claude-Red
site_name: github
content_file: github-github-snailsploitclaude-red-claude-red-is-a-curat
fetched_at: '2026-09-12T13:52:45.340901'
original_url: https://github.com/SnailSploit/Claude-Red
author: SnailSploit
description: claude-red is a curated library of offensive security skills designed for the Claude skills system. Each skill is a structured SKILL.md file that primes Claude with expert-level methodology for a specific attack surface — from SQLi to shellcode, EDR evasion to exploit development. - SnailSploit/Claude-Red
---

SnailSploit

 

/

Claude-Red

Public

* NotificationsYou must be signed in to change notification settings
* Fork541
* Star3.4k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

34 Commits
34 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github/
workflows
.github/
workflows
 
 
Skills
Skills
 
 
assets
assets
 
 
tools
tools
 
 
.DS_Store
.DS_Store
 
 
.gitattributes
.gitattributes
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
MINDMAP.md
MINDMAP.md
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
claude-skills.json
claude-skills.json
 
 
convert_skills.py
convert_skills.py
 
 
install.sh
install.sh
 
 
View all files

## Repository files navigation

# claude-red

Offensive security skills for Claude — drop-inSKILL.mdfiles that turn Claude into a context-aware red team operator.

Overview•Quickstart•Categories•Skill Index•Roadmap•Contributing

## Overview

claude-redis a curated library of offensive security skills for theClaude Skills system. Each skill is a structuredSKILL.mdfile that primes Claude with expert-level methodology for a specific attack surface — from SQL injection to shellcode, EDR evasion to ADCS abuse.

Drop a skill into your Claude environment and it behaves like a domain specialist: it knows the techniques, the tooling, the edge cases, and the escalation paths. Skills load on demand based on conversational triggers — you don't pay context for skills you aren't using.

Use cases:authorized red team engagements, bug bounty triage, security research, CTF preparation, operator training, and methodical attack surface exploration.

## Quickstart

### Claude Skills System (Recommended)

git clone https://github.com/SnailSploit/claude-red 
~
/.claude/skills/claude-red

Claude auto-loads matching skills based on conversational triggers (e.g., mentioning SQL injection loadsoffensive-sqli).

To install a single category:

git clone --filter=blob:none --sparse https://github.com/SnailSploit/claude-red

cd
 claude-red 
&&
 git sparse-checkout 
set
 Skills/web Skills/active-directory

### Claude Code

cat Skills/web/offensive-sqli/SKILL.md 
|
 claude --system-file -

cat Skills/active-directory/
**
/SKILL.md 
|
 claude --system-file -

### Claude.ai (Manual)

Paste the contents of aSKILL.mdinto a Project's system prompt or prepend it to your conversation.

### Install Script

./install.sh 
#
 interactive

./install.sh --target 
~
/.claude/skills 
#
 explicit target

./install.sh --category web 
#
 single category

## Categories

Category

Skills

Focus

Web Application

16

OWASP Top 10, business logic, advanced web vulnerability classes

Auth & Identity

2

JWT exploitation, OAuth/OIDC abuse

Active Directory

1

On-prem AD attack methodology

Wireless

14

802.11, WPA2/3, EAP, WPS, evil-twin, BLE, Zigbee, Z-Wave, LoRa, sub-GHz

Cloud

1

AWS, Azure, GCP attack paths

Mobile

1

Android and iOS application testing

IoT & Embedded

1

Hardware, firmware, RTOS, ICS/OT

Infrastructure & Red Team

7

Initial access, EDR evasion, advanced red team operations, Windows internals

Exploit Development

6

Stack/heap corruption, ROP, mitigations, crash analysis, TOCTOU

Fuzzing & Vulnerability Research

4

libFuzzer, AFL++, coverage-guided fuzzing, vulnerability taxonomy

Reconnaissance

2

OSINT tooling and structured intelligence collection

API Security

2

REST/gRPC/WebSocket testing, business logic abuse

Container & Kubernetes

2

Container escape, Kubernetes cluster exploitation

CI/CD & Pipeline

2

Pipeline exploitation, secrets extraction

Cryptography

2

Cryptographic implementation attacks, TLS/SSL

Privilege Escalation

2

Linux and Windows privilege escalation

Post-Exploitation

3

Lateral movement, persistence mechanisms, data exfiltration

Forensics & C2

2

Anti-forensics tradecraft, C2 framework operations

Supply Chain

2

Supply chain attacks, dependency confusion

Social Engineering

2

Phishing campaigns, physical/vishing/smishing

Network Attacks

1

Layer 2/3 attacks, MITM, protocol poisoning

AI Security

1

Prompt injection, jailbreaking, RAG poisoning

Utility

2

Fast triage checklists, professional reporting

## Skill Index

### Web Application

Skills/web/

Skill

Description

offensive-sqli

SQL injection — error-based, blind, OOB, DB-specific payloads, ORM CVEs

offensive-xss

Cross-site scripting — stored, reflected, DOM-based, mutation XSS

offensive-ssrf

Server-side request forgery — cloud metadata pivots, filter bypass

offensive-ssti

Server-side template injection — engine fingerprinting, RCE chains

offensive-xxe

XML external entity — OOB exfiltration, blind XXE techniques

offensive-idor

Insecure direct object references — enumeration, authorization bypass

offensive-file-upload

File upload — extension bypass, polyglot files, webshell deployment

offensive-rce

Remote code execution — command injection, deserialization chains

offensive-deserialization

Insecure deserialization — Java, PHP, .NET gadget chains

offensive-race-condition

Race conditions — TOCTOU, single-packet attacks, limit bypass

offensive-request-smuggling

HTTP request smuggling — CL.TE, TE.CL, H2 desync

offensive-open-redirect

Open redirect — OAuth token theft, phishing, SSRF pivots

offensive-parameter-pollution

HTTP parameter pollution — WAF bypass, logic confusion

offensive-graphql

GraphQL — introspection abuse, batching attacks, alias-based IDOR

offensive-waf-bypass

WAF bypass — encoding tricks, chunked transfer, case mutation

offensive-business-logic

Business logic — workflow bypass, pricing abuse, multi-step chains

### Auth & Identity

Skills/auth/

Skill

Description

offensive-jwt

JWT attacks — alg:none, key confusion, secret cracking, claim tampering

offensive-oauth

OAuth/OIDC — redirect URI abuse, token leakage, PKCE bypass

### Active Directory

Skills/active-directory/

Skill

Description

offensive-active-directory

AD methodology — Kerberoast, ASREProast, ACL abuse, ADCS ESC1-15, delegation, hybrid AAD

### Wireless

Skills/wireless/

Skill

Description

offensive-wifi

802.11 overview — entrypoint for wireless assessments

offensive-wifi-recon

Adapter configuration, monitor mode, multi-band airspace mapping

offensive-wpa2-psk

WPA2-PSK — handshake capture, PMKID extraction, hashcat cracking

offensive-wpa3-sae

WPA3-SAE — transition-mode downgrade, Dragonblood, side-channel attacks

offensive-wpa-enterprise

802.1X/EAP — credential relay, evil-twin RADIUS, certificate abuse

offensive-wps

WPS — Pixie Dust offline attack, online PIN brute force, vendor PIN prediction

offensive-evil-twin

Evil twin — KARMA, Mana, captive portal credential capture, MITM

offensive-krack-fragattacks

KRACK and FragAttacks — supplicant vulnerability testing

offensive-deauth-disassoc

Deauthentication — targeted/broadcast frames, PMF awareness

offensive-bluetooth-ble

Bluetooth LE — GATT enumeration, pairing downgrade, sniffing, MITM

offensive-bluetooth-classic

Bluetooth BR/EDR — SDP probing, KNOB attack, BlueBorne, HID spoofing

offensive-zigbee-thread-matter

802.15.4 mesh — KillerBee, Touchlink commissioning abuse, ZCL injection

offensive-z-wave

Z-Wave — S0 key derivation, S2 commissioning attacks, hub pivots

offensive-lorawan-sub-ghz

LoRaWAN and sub-GHz — ABP/OTAA attacks, KeeLoq, fixed-code replay, TPMS

### Cloud

Skills/cloud/

Skill

Description

offensive-cloud

Multi-cloud — privilege escalation, IMDS abuse, cross-account pivots, CSPM evasion

### Mobile

Skills/mobile/

Skill

Description

offensive-mobile

Android and iOS — Frida hooking, certificate pinning bypass, storage, biometric flaws

### IoT & Embedded

Skills/iot/

Skill

Description

offensive-iot

IoT/OT — hardware interfaces, firmware extraction, RTOS, ICS protocols, MQTT/CoAP

### Infrastructure & Red Team

Skills/infrastructure/

Skill

Description

offensive-initial-access

Initial access — phishing payloads, drive-by delivery, supply chain vectors (TA0001)

offensive-advanced-redteam

Full kill chain — C2 infrastructure, OPSEC, lateral movement, persistence

offensive-edr-evasion

EDR evasion — userland unhooking, indirect syscalls, PPID spoofing

offensive-shellcode

Shellcode — writing, encoding, injection techniques, position-independent code

offensive-keylogger-arch

Input capture — keylogger architecture, hooking mechanisms

offensive-windows-mitigations

Windows mitigations — ACG, CIG, CFG, CET bypass techniques

offensive-windows-boundaries

Windows boundary defeat — sandbox escape, integrity level bypass

### Exploit Development

Skills/exploit-dev/

Skill

Description

offensive-exploit-development

Exploit development — stack/heap corruption, ROP chains, mitigation bypass

offensive-exploit-dev-course

Structured exploit development curriculum

offensive-basic-exploitation

Linux binary exploitation — beginner to intermediate, mitigations disabled

offensive-crash-analysis

Crash triage — exploitability assessment, root-cause analysis

offensive-mitigations

Modern mitigations — ASLR, CFG, CET, PAC analysis and bypass

offensive-toctou

TOCTOU race conditions — binary, kernel, web, and container contexts

### Fuzzing & Vulnerability Research

Skills/fuzzing/

Skill

Description

offensive-fuzzing

Fuzzing — libFuzzer, AFL++, coverage-guided strategies, mutation engines

offensive-fuzzing-course

Vulnerability discovery through fuzzing — structured curriculum

offensive-bug-identification

Bug identification — code review patterns, static analysis triggers

offensive-vuln-classes

Vulnerability taxonomy — real-world examples, classification frameworks

### Reconnaissance

Skills/recon/

Skill

Description

offensive-osint

OSINT tooling — recon-ng, theHarvester, Maltego, Spiderfoot

offensive-osint-methodology

OSINT methodology — structured intelligence collection and analysis

### API Security

Skills/api/

Skill

Description

offensive-api-security

API testing — OWASP API Top 10, BOLA, BFLA, mass assignment, rate limiting

offensive-api-abuse

API business logic — endpoint chaining, batching abuse, webhook hijacking

### Container & Kubernetes

Skills/container/

Skill

Description

offensive-container-escape

Container breakout — privileged mode, Docker socket, capabilities, runc CVEs

offensive-k8s-attacks

Kubernetes attacks — RBAC abuse, etcd access, kubelet API, pod escape, CRD exploitation

### CI/CD & Pipeline

Skills/cicd/

Skill

Description

offensive-cicd-pipeline

CI/CD exploitation — GitHub Actions injection, Jenkins RCE, GitLab CI abuse

offensive-cicd-secrets

CI/CD secrets — environment variable extraction, vault misconfigs, runner token abuse

### Cryptography

Skills/crypto/

Skill

Description

offensive-crypto-attacks

Cryptographic attacks — padding oracle, ECB manipulation, hash extension, weak PRNG

offensive-tls-attacks

TLS/SSL attacks — POODLE, DROWN, Heartbleed, pinning bypass, 0-RTT replay

### Privilege Escalation

Skills/privesc/

Skill

Description

offensive-linux-privesc

Linux privilege escalation — SUID, capabilities, sudo, cron, kernel exploits

offensive-windows-privesc

Windows privilege escalation — Potato family, service misconfigs, DLL hijacking, UAC bypass

### Post-Exploitation

Skills/post-exploitation/

Skill

Description

offensive-lateral-movement

Lateral movement — PTH, PTT, NTLM relay, WMI/WinRM/DCOM, tunneling

offensive-persistence

Persistence — registry, scheduled tasks, WMI subscriptions, ticket forgery, PAM backdoors

offensive-data-exfiltration

Data exfiltration — DNS/HTTPS/ICMP tunneling, cloud staging, steganography

### Forensics & C2

Skills/forensics/

Skill

Description

offensive-anti-forensics

Anti-forensics — log manipulation, timestomping, ADS abuse, memory cleanup

offensive-c2-frameworks

C2 tradecraft — Cobalt Strike, Sliver, Mythic, Havoc, redirectors, domain fronting

### Supply Chain

Skills/supply-chain/

Skill

Description

offensive-supply-chain

Supply chain attacks — dependency confusion, typosquatting, build system compromise

offensive-dependency-confusion

Dependency confusion — npm/PyPI/NuGet/Maven namespace attacks, safe PoC methodology

### Social Engineering

Skills/social-engineering/

Skill

Description

offensive-phishing

Phishing — GoPhish, EvilGinx2, payload delivery, email authentication bypass

offensive-social-engineering

Social engineering — pretexting, vishing, smishing, physical SE, USB drops

### Network Attacks

Skills/network/

Skill

Description

offensive-network-attacks

Network layer attacks — ARP spoofing, LLMNR/NBT-NS poisoning, VLAN hopping, MITM

### AI Security

Skills/ai/

Skill

Description

offensive-ai-security

AI/ML security — prompt injection, jailbreaking, RAG poisoning, model extraction

### Utility

Skills/utility/

Skill

Description

offensive-fast-checking

Fast triage — quick-win identification checklists

offensive-reporting

Professional reporting — CVSS scoring, evidence standards, executive summaries

## Roadmap

The library is being expanded across multiple phases. SeeCHANGELOG.mdfor release history.

Phase

Focus

Skills

Status

1

Internal AD/Windows — split into focused skills

+16

Planned

2

Cloud Identity — Entra, ADFS, Okta, M365

+10

Planned

3

Wireless — WPA2/3, EAP, BLE, Zigbee, Z-Wave, LoRa, sub-GHz

+12

Complete

4

IoT — UART/JTAG, flash extraction, fault injection, RTOS, ICS

+10

Planned

5

Web Fundamentals — recon, auth bypass, access control, CSRF, CORS

+8

Planned

6

Web Advanced — proto pollution, SAML, OIDC, WebSocket, SSI/ESI

+10

Planned

7

Documentation and tooling polish

—

Complete

8

New categories — 10 new domains with 20 skills

+20

Complete

9

Deep rewrites — deserialization, GraphQL, advanced red team, SSTI

—

Complete

Target: ~130 skills across 23+ categories.

## Contributing

Contributions welcome. SeeCONTRIBUTING.mdfor the skill template, frontmatter standard, and review process. Focused, single-surface skills are preferred over monolithic overviews.

## License

MIT— use freely, attribution appreciated.

## Acknowledgements

* Author:Kai Aizen(SnailSploit) — GenAI security research
* Original Checklists:Sahar Shlichov— the offensive checklist collection that many of these skills build on
* Community:Pull requests and feedback that keep the library aligned with the evolving threat landscape

Give Claude the right skill and it stops being a chatbot — it becomes an operator.

snailsploit.com•GitHub•Research•X