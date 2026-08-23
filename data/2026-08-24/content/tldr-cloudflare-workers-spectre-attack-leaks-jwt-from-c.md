---
title: Cloudflare Workers Spectre Attack Leaks JWT From Co-Located Worker at 12 Bits/Second
url: https://thehackernews.com/2026/08/cloudflare-workers-spectre-attack-leaks.html
site_name: tldr
content_file: tldr-cloudflare-workers-spectre-attack-leaks-jwt-from-c
fetched_at: '2026-08-24T07:46:53.421534'
original_url: https://thehackernews.com/2026/08/cloudflare-workers-spectre-attack-leaks.html
author: The Hacker News
date: '2026-08-24'
description: Researchers leak a JWT from a co-located Cloudflare Worker via Spectre at up to 12 bits per second; Cloudflare says the attack is mitigated.
tags:
- tldr
---

# Cloudflare Workers Spectre Attack Leaks JWT From Co-Located Worker at 12 Bits/Second


Swati Khandelwal

Aug 19, 2026
Cloud Security / Vulnerability

Cybersecurity researchers have disclosed details of aremote Spectre attackagainst Cloudflare Workers that leaked a JSON Web Token (JWT) from a co-located Worker in the production environment at up to 12 bits per second, 360 times the rate of an earlier attack demonstrated in 2021.

The end-to-end experiment used an attacker Worker and a victim Worker controlled by the researchers, with the JWT intentionally placed in the victim's memory. The research paper stated that no customer data was accessed.

Cloudflare said the attack has already been mitigated in production after it improved Dynamic Process Isolation (DyPrIs), integrated theV8 Sandbox, and deployed Memory Protection Keys (MPK)-based in-process isolation, adding that it found no indicators of active exploitation over the last three years.

"We demonstrate that the production implementation of DyPrIs was insufficient," the researchers said inthe paper.

Cloudflare Workers runs code from multiple tenants in separate V8 isolates within the same operating-system process, relying on language-level isolation instead of strict process isolation to reduce startup latency.

A memory read within a shared Worker process can lead to cross-tenant leakage, according toCloudflare. The attack requires the attacker and victim Workers to be co-located in separate V8 isolates within the same Worker process.

The attacker controls valid code in its own isolate. Native code execution is outside the threat model, and the attack does not depend on a V8 software exploit or sandbox escape.

Cloudflare said Workers restrict local timing sources by freezing or coarsening timers during CPU execution, and do not expose shared memory or multithreading to Worker scripts.

The researchers found that WebSocket communications could provide a remote timing source, while Durable Objects could keep a single Worker isolate alive for five to more than 20 hours.

DyPrIs isolates suspicious scripts into a separate process after an invocation finishes, and the researchers found that a long-lived Durable Object invocation could continue running before the isolation took place.

The researchers also found that WebSocket-heavy input/output (I/O) activity increased instruction translation lookaside buffer (iTLB) activity, reducing the normalized branch-misprediction signal used by DyPrIs below its detection threshold.

Cloudflare described the issue as a limitation in its DyPrIs implementation, while the paper said the two weaknesses reflected fundamental limitations of the detection approach rather than implementation oversights. The researchers said robust detection should take place during execution and use a signal that cannot be suppressed by I/O activity.

The paper said the production tests were conducted on Linux servers using AMD EPYC Zen 2 and Zen 3 processors, with the researchers intentionally running measurements at night, when CPU utilization was between 10% and 25%, to observe the best possible results.

The researchers said higher system load reduced the leakage rate, although slower attacks remained feasible under high load.

The paper reported leakage of up to 12 bits per second at 99.16% accuracy, compared with 2 bits per minute in the earlier attack.

The disclosure comes nearly five years after Cloudflare and TU Grazpublished researchdemonstrating a remote Spectre attack against Workers at 120 bits per hour and introducing DyPrIs as a defense.

The earlier paper reported a 0.61% false-positive rate and concluded that DyPrIs statistically provided the same security guarantees as strict process isolation against the Spectre attacks evaluated at the time.

Cloudflare published additionalWorkers hardening measuresin September 2025. The mitigations deployed by Cloudflare are listed below -

* Improved DyPrIsimproves the detection capabilities of the existing isolation mechanism.
* V8 Sandboxlimits transient access to 64-bit pointers.
* MPK-based in-process isolationplaces Worker heaps behind hardware-enforced protection keys. Cloudflare said modern x64 systems leave about 12 keys available for this purpose, and its design combines the keys with the V8 Sandbox and a rotating memory layout to prevent nearby sandboxes from sharing a key.

Cloudflare's September 2025 description said that random MPK assignment alone would trap about 92% of cross-isolate accesses because two isolates can receive the same key, and that the stricter rotating layout is used to remove that gap for the covered in-sandbox threat model.

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

Application Security
, 
Cloud security
, 
CloudFlare
, 
Cybersecurity Research
, 
data security
, 
hardware security
, 
Side-Channel Attack
, 
Vulnerability
, 
Web Security

⚡ Top Stories This Week

Microsoft Patches Severe Entra ID Flaw (CVSS 10.0) Allowing Remote Code Execution

ThreatsDay: Gogs 10.0 RCE, n8n Workflow-to-RCE, $10M Reward, GLM-5.3 AI Exploit, and More

New Cryptographic Context Injection Attack Could Let Web Pages Steal Grok Chat Data

Zombie Card Attack Can Revive Expired Visa Cards for Contactless Payments

CDN Tsunami Attack Abuses HTTP/3 Translation for Up to 350x DoS Amplification

Manic Android Malware Exfiltrates Data From Offline Phones via Nearby Infected Devices

Cloudflare Workers Spectre Attack Leaks JWT From Co-Located Worker at 12 Bits/Second

OpenAI Pauses Frontier RL Training as It Tightens Defenses Against Unsafe AI Behavior

Hackers Compromised 14,500+ Dahua Devices Using Credential Attacks, Auth Bypasses, and P2P

Microsoft Copilot Personal Flaws Could Let One Click Exfiltrate Data From Connected Apps

AI "Mind Viruses" Can Spread Between Agents Through Persistent Prompt Files

SafePal Hardware Wallet Maker Says Flaw Exposed Data of Nearly 40,000 Customers

Critical GitLab GraphQL Flaw Could Let Unauthenticated Attackers Delete Public Projects

⚡ Weekly Recap: VMware Exploits, Windows 0-Day, MCP Attacks, Browser Hijacks and More

Unisoc VoLTE Video Call Exploit Chain Can Give Attackers Full Android Kernel Access

Evooo1Bot Linux Botnet Exploits Known Flaws to Turn Edge Devices Into SOCKS5 Proxies

SAP Commerce Cloud CVE-2026-58231 Targeted in Exploitation Attempts Days After Patch

Hackers Spend Nearly $7 Million on Expired Domains to Redirect Traffic to Scams and Malware

Apple Warns Users in 110 Countries They May Be Targets of Mercenary Spyware

Trump Memo Paves Way for U.S. Firms to Hack and Disrupt Foreign Crime Groups

GeoServer Zero-Day Targeted in Active Exploitation Attempts, Can Lead to RCE

Attackers Exploit SharePoint Authentication Bypass After Public PoC Release

Lazarus Exploits Windows Zero-Day to Gain SYSTEM Access and Deploy Backdoor

Attackers Exploit VMware vCenter Vulnerability to Gain Persistent Remote Access

ShieldBreak Zero-Day PoC Claims Microsoft Defender Patch Bypass With SYSTEM Access

⭐ Featured Resources

See How Keeper Secrets Manager Removes Hard-Coded Credentials

Download the CISO's Guide to Smarter AI Security Investment

Phishing Is Costing Security Teams More Than Ever — Read the New Report

Build AI Agents and Automations Without Losing Security Control