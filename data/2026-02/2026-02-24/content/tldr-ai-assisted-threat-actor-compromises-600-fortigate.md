---
title: AI-Assisted Threat Actor Compromises 600+ FortiGate Devices in 55 Countries
url: https://thehackernews.com/2026/02/ai-assisted-threat-actor-compromises.html
site_name: tldr
content_file: tldr-ai-assisted-threat-actor-compromises-600-fortigate
fetched_at: '2026-02-24T11:20:06.287209'
original_url: https://thehackernews.com/2026/02/ai-assisted-threat-actor-compromises.html
author: The Hacker News
date: '2026-02-24'
description: AI-augmented actor breached 600+ FortiGate devices in 55 countries using weak credentials and exposed ports, Amazon reports.
tags:
- tldr
---

# AI-Assisted Threat Actor Compromises 600+ FortiGate Devices in 55 Countries


Ravie Lakshmanan

Feb 21, 2026
Threat Intelligence / Artificial Intelligence

A Russian-speaking, financially motivated threat actor has been observed taking advantage of commercial generative artificial intelligence (AI) services to compromise over 600 FortiGate devices located in 55 countries.

That's according to new findings from Amazon Threat Intelligence, which said it observed the activity between January 11 and February 18, 2026.

"No exploitation of FortiGate vulnerabilities was observed—instead, this campaign succeeded by exploiting exposed management ports and weak credentials with single-factor authentication, fundamental security gaps that AI helped an unsophisticated actor exploit at scale," CJ Moses, Chief Information Security Officer (CISO) of Amazon Integrated Security,saidin a report.

The tech giant described the threat actor as having limited technical capabilities, a constraint they overcame by relying on multiple commercial generative AI tools to implement various phases of the attack cycle, such as tool development, attack planning, and command generation.

While one AI tool served as the primary backbone of the operation, the attackers also relied on a second AI tool as a fallback to assist with pivoting within a specific compromised network. The names of the AI tools were not disclosed.

The threat actor is assessed to be driven by financial gain and not associated with any advanced persistent threat (APT) with state-sponsored resources. As recentlyhighlightedby Google, generative AI tools are being increasingly adopted by threat actors to scale and accelerate their operations, even if they don't equip them with novel uses of the technology.

If anything, the emergence of AI tools illustrates how capabilities that were once off-limits to novice or technically challenged threat actors are becoming increasingly feasible, further lowering the barrier to entry for cybercrime and enabling them to come up with comprehensive attack methodologies.

"They are likely a financially motivated individual or small group who, through AI augmentation, achieved an operational scale that would have previously required a significantly larger and more skilled team," Moses said.

Amazon's investigation into the threat actor's activity has revealed that they have successfully compromised multiple organizations’ Active Directory environments, extracted complete credential databases, and even targeted backup infrastructure, likely in a lead-up to ransomware deployment.

What's interesting here is that rather than devising ways to persist within hardened environments or those that had employed sophisticated security controls, the threat actor chose to drop the target altogether and move to a relatively softer victim. This indicates the use of AI as a way to bridge their skill gap for easy pickings.

Amazon said it identified publicly accessible infrastructure managed by the attackers that hosted various artifacts pertinent to the campaign. This included AI-generated attack plans, victim configurations, and source code for custom tooling. The entire modus operandi is akin to an "AI-powered assembly line for cybercrime," the company added.

At its core, the attacks enabled the threat actor to breach FortiGate appliances, allowing it to extract full device configurations that, in turn, made it possible to glean credentials, network topology information, and device configuration information.

This involved systematic scanning of FortiGate management interfaces exposed to the internet across ports 443, 8443, 10443, and 4443, followed by attempts to authenticate using commonly reused credentials. The activity was sector-agnostic, indicating automated mass scanning for vulnerable appliances. The scans originated from the IP address212.11.64[.]250.

The stolen data was then used to burrow deeper into targeted networks and conduct post-exploitation activities, including reconnaissance for vulnerability scanning using Nuclei, Active Directory compromise, credential harvesting, and efforts to access backup infrastructure that align with typical ransomware operations.

Data gathered by Amazon shows that the scanning activity resulted in organizational-level compromise, causing multiple FortiGate devices belonging to the same entity to be accessed. The compromised clusters have been detected across South Asia, Latin America, the Caribbean, West Africa, Northern Europe, and Southeast Asia.

"Following VPN access to victim networks, the threat actor deploys a custom reconnaissance tool, with different versions written in both Go and Python," the company said.

"Analysis of the source code reveals clear indicators of AI-assisted development: redundant comments that merely restate function names, simplistic architecture with disproportionate investment in formatting over functionality, naive JSON parsing via string matching rather than proper deserialization, and compatibility shims for language built-ins with empty documentation stubs."

Some of the other steps undertaken by the threat actor following the reconnaissance phase are listed below -

* Achieve domain compromise viaDCSync attacks.
* Move laterally across the network via pass-the-hash/pass-the-ticket attacks, NTLM relay attacks, and remote command execution on Windows hosts.
* Target Veeam Backup & Replication servers to deploy credential harvesting tools and programs aimed at exploiting known Veeam vulnerabilities (e.g.,CVE-2023-27532andCVE-2024-40711).

Another noteworthy finding is the threat actor's pattern of repeatedly running into failures when trying to exploit anything beyond the "most straightforward, automated attack paths," with their own documentation recording that the targets had either patched the services, closed the required ports, or had no vulnerable exploitation vectors.

With Fortinet appliances becoming anattractive target for threat actors, it's essential that organizations ensure management interfaces are not exposed to the internet, change default and common credentials, rotate SSL-VPN user credentials, implement multi-factor authentication for administrative and VPN access, and audit for unauthorized administrative accounts or connections.

It's also recommended to isolate backup servers from general network access, ensure all software programs are up-to-date, and monitor for unintended network exposure.

"As we expect this trend to continue in 2026, organizations should anticipate that AI-augmented threat activity will continue to grow in volume from both skilled and unskilled adversaries," Moses said. "Strong defensive fundamentals remain the most effective countermeasure: patch management for perimeter devices, credential hygiene, network segmentation, and robust detection for post-exploitation indicators."

### Update

In a separate research, Cyber and Ramen alsodiscloseddetails of the same campaign, highlighting the threat actor's use of DeepSeek and Anthropic Claude to generate the attack plans. A prior exposure of the same server in December 2025 has revealed that the earlier instance hosted a copy of an offensive AI framework known asHexStrike AI.

"DeepSeek is used to generate attack plans from reconnaissance data," an anonymous threat researcher behind the security blog said. "Claude's coding agent produced vulnerability assessments during the intrusions and was configured to execute offensive tools on the victim systems. A previously unreported model context protocol (MCP) server acts as a bridge to the language models, maintaining a knowledge base which grows with each target."

The server, 212.11.64[.]250, has been found to host over 1,400 files across 139 subdirectories. This included CVE exploit code, FortiGate configuration files, Nuclei scanning templates, Veeam credential extraction tools, and BloodHound collection data.

Also present among the exposed files was a custom Model Context Protocol (MCP) server named ARXON to process scan results and reconnaissance data, invoke DeepSeek to generate attack plans, and leverage scripts to modify victim infrastructure. Another custom tool used by the attacker is a Go-based orchestrator called CHECKER2 for parallel VPN scanning and target processing.

"What sets this activity apart is the integration of LLMs: a (likely) single operator managing simultaneous intrusions across multiple countries with analytical support at every stage," the researcher said. "Language models only assisted a low-to-average skilled actor in removing the number of targets one person can work at any given time."

(The story was updated after publication to include additional details of the campaign from Cyber and Ramen.)

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

Active Directory
,
artificial intelligence
,
Cloud security
,
Credential Theft
,
cybersecurity
,
Fortinet
,
network security
,
ransomware
,
Threat Intelligence
,
Vulnerability

Trending News

OT Security, In Practice: 4 Cross‑Industry Trends from Global Assessments and How CISOs Should Respond

Reynolds Ransomware Embeds BYOVD Driver to Disable EDR Security Tools

Microsoft Patches 59 Vulnerabilities Including Six Actively Exploited Zero-Days

SSHStalker Botnet Uses IRC C2 to Control Linux Systems via Legacy Kernel Exploits

First Malicious Outlook Add-In Found Stealing 4,000+ Microsoft Credentials

ThreatsDay Bulletin: AI Prompt RCE, Claude 0-Click, RenEngine Loader, Auto 0-Days and 25+ Stories

Google Reports State-Backed Hackers Using Gemini AI for Recon and Attack Support

Researchers Observe In-the-Wild Exploitation of BeyondTrust CVSS 9.9 Vulnerability

Malicious Chrome Extensions Caught Stealing Business Data, Emails, and Browsing History

New Chrome Zero-Day (CVE-2026-2441) Under Active Attack — Patch Released

Microsoft Discloses DNS-Based ClickFix Attack Using Nslookup for Malware Staging

New ZeroDayRAT Mobile Spyware Enables Real-Time Surveillance and Data Theft

Study Uncovers 25 Password Recovery Attacks in Major Cloud Password Managers

Weekly Recap: Outlook Add-Ins Hijack, 0-Day Patches, Wormable Botnet and AI Malware

Infostealer Steals OpenClaw AI Agent Configuration Files and Gateway Tokens

Keenadu Firmware Backdoor Infects Android Tablets via Signed OTA Updates

Popular Resources

100+ Domains Multiply Attack Risk 6× - Download the CTEM Divide Research

Boost SOC Efficiency with AI-Guided Triage — Download Investigator Overview

Silent Residency Is the New Threat Model — Download the Red Report

Exposed Cloud Training Apps Are Letting Hackers In — Download the Research
