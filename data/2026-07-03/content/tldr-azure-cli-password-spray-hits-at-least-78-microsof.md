---
title: Azure CLI Password Spray Hits at Least 78 Microsoft Accounts in 81M+ Attempts
url: https://thehackernews.com/2026/07/azure-cli-password-spray-hits-at-least.html
site_name: tldr
content_file: tldr-azure-cli-password-spray-hits-at-least-78-microsof
fetched_at: '2026-07-03T11:49:48.453509'
original_url: https://thehackernews.com/2026/07/azure-cli-password-spray-hits-at-least.html
author: The Hacker News
date: '2026-07-03'
description: Huntress says attackers made 81M Azure CLI password spray attempts from June 12-26, 2026, using ROPC to bypass weak CAPs.
tags:
- tldr
---

# Azure CLI Password Spray Hits at Least 78 Microsoft Accounts in 81M+ Attempts


Ravie Lakshmanan

Jul 01, 2026
Password Security / Cloud Security

Cybersecurity researchers have warned of a "massive, ongoing, automated password spray attack" aimed at Microsoft's Azure command-line interface (CLI), compromising dozens of accounts in the process.

The activity, perHuntress, originates from an IPv6 address range (2a0a:d683::/32) controlled by internet infrastructure providerLSHIY LLC(AS32167).

"Between June 12 and June 26, the threat actor behind it made more than 81 million login attempts and successfully compromised at least 78 Microsoft accounts across 64 organizations," the company said in a statement. "The targeting of these attacks seems to be based entirely on password prevalence on compromised password combo lists, and is not specific to business type or industry."

What makes the password spray attack noteworthy is not only the scale, but also the fact that many of the compromised organizations had Conditional Access policies enabled. Specifically, the campaign has been found to leverage a deprecated OAuth flow called Resource Owner Password Credentials (ROPC) to bypass Conditional Access Policy (CAP) protections.

ROPCis a legacy OAuth 2.0 grant type where a user directly provides their username and password to a client application, which then sends these credentials to an authorization server to exchange them for an access token. It was deprecated in OAuth 2.1.

In its documentation, Microsoft recommends customers against using the ROPC flow, arguing it's incompatible with multi-factor authentication (MFA).

"In most scenarios, more secure alternatives are available and recommended," the tech giantsays. "This flow requires a very high degree of trust in the application, and carries risks that aren't present in other flows. You should only use this flow when more secure flows aren't viable."

The credential and token spray attacks are said to have resulted in a handful of successful logins per day between June 12 and 21, 2026, averaging two to four accounts being compromised daily, with the exception of June 19, when 12 user accounts (aka identities) were compromised. The steady cadence changed on June 22, with 30 identities across 23 businesses impacted.

In all, 78 user accounts were compromised across 64 organizations as part of the campaign. The vast majority of the password spraying activity emanated from LSHIY LLC. Some of the IP addresses resolve to the U.S., while a few others resolve to China.

"These attacks are part of a large wave of credential spray attacks across a few different ASNs," Huntress said, adding it has witnessed the volume of credential spray attacks surge by over 155 times across its customer base. "Attacks surged in particular in late May through early June, with a current mean value of about 1,964 failed attacks per month per Huntress-protected tenant."

The activity appears to specifically weaponize old username/password combinations that were previously breached but had never been rotated. The use of the ROPC vector meant that the attackers were able to target enterprises that had implemented MFA, but it wasn't enforced or configured to account for Azure CLI ROPC logins.

This included scenarios where MFA wasn't triggered -

* Enforcing MFA only for specific apps, as opposed to "All Cloud Apps," thereby failing to cover Azure CLI logins used by the threat actors
* Enforcing MFA only for specific user groups, such as Admins
* Enforcing MFA only when requests originate from non-trusted locations

"It's worth noting that eight businesses impacted by the campaign had no MFA policy at all," Huntress said. "While threat actors in this campaign were able to get in despite MFA being set up, the takeaway should not be that MFA doesn't work at all; instead, organizations should ensure that their MFA policies are properly configured to address the authorization flow used across these incidents."

To counter this line of attack, organizations are advised to require MFA for All Users, All Cloud Apps, and All Client App types when enabling CAP, restrict the Azure CLI application for non-admin users, and prioritize response by credential validity.

"This attack reveals cracks in CAPs that haven't been appropriately configured," Huntress researchers concluded. "There are still potential weaknesses in how CAPs are deployed that can allow threat actors to slip through. One glaring error here is that legacy protocols like ROPC can bypass some poorly-configured CAPs entirely since they don't go through the authorization endpoint where policies are enforced."

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

Azure CLI
, 
Cloud security
, 
Credential Attack
, 
Huntress
, 
MFA
, 
Microsoft
, 
OAuth
, 
Password Spray

⚡ Top Stories This Week

ThreatsDay: AI Compute Hijacking, Apple Email Flaw, BlueHammer Ransomware + 14 Stories

Chrome Ad Blocker with 10M+ Installs Found with Dormant Script Injection Capability

New DirtyClone Linux Kernel Flaw Lets Local Users Gain Root via Cloned Packets

Amazon Q Developer Flaw Could Let Malicious Repos Run Code via MCP Configs

New Linux pedit COW Exploit Enables Root Access by Poisoning Cached Binaries

OpenAI Previews GPT-5.6 Sol With Restricted Access and Stronger Cyber Safeguards

FBI Warns Russian Intelligence Hackers Target Signal Backup Recovery Keys

Public PoC Released for Critical libssh2 CVE-2026-55200 Client-Side SSH Flaw

Microsoft Removes 119 Edge Extensions That Hid Malware in Images and Fonts

⚡ Weekly Recap: Linux Kernel Flaws, AI Malware Tricks, Turla Backdoor, Infostealers and More

Mustang Panda Uses Zoho WorkDrive as Command Channel in Indian Government Attacks

WhatsApp is Finally Getting Usernames to Help Keep Phone Numbers Private

Oracle E-Business Suite Flaw CVE-2026-46817 Actively Exploited in the Wild

New BioShocking Attack Tricks AI Browsers Into Leaking User Credentials

AirDrop and Quick Share Flaws Let Nearby Attackers Trigger Crashes and Bypass Checks

282 iOS AI Apps Leak API Keys and Open AI Proxy Access in Network Traffic Study

GuardFall Exposes Open-Source AI Coding Agents to Decades-Old Shell Injection Risks

Microsoft Warns Poisoned MCP Tool Descriptions Can Make AI Agents Leak Data

RustDuck Botnet Rebuilds in Rust to Hijack Routers and Servers for DDoS

⭐ Featured Resources

What 200+ Security Teams Reveal About Using IP Intelligence in 2026

Get Hands-On SANS Training for Today’s Cyber Defense and Offensive Security Challenges

See What’s Really Exposed Across Your IT, OT, IoT, Cloud, and Mobile Assets

Get Gartner’s Guide to AI Agent Supervision and Runtime Controls