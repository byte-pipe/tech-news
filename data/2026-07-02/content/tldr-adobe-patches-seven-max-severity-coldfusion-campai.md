---
title: Adobe patches seven max severity ColdFusion, Campaign flaws
url: https://www.bleepingcomputer.com/news/security/adobe-patches-seven-max-severity-coldfusion-campaign-flaws/
site_name: tldr
content_file: tldr-adobe-patches-seven-max-severity-coldfusion-campai
fetched_at: '2026-07-02T19:33:58.526371'
original_url: https://www.bleepingcomputer.com/news/security/adobe-patches-seven-max-severity-coldfusion-campaign-flaws/
date: '2026-07-02'
description: Adobe has released security patches for seven maximum-severity vulnerabilities in the ColdFusion web app development platform and the Campaign Classic marketing automation platform.
tags:
- tldr
---

# Adobe patches seven max severity ColdFusion, Campaign flaws

 By 

###### Sergiu Gatlan

* July 1, 2026
* 03:34 AM
* 0

Adobe has released security patches for seven maximum-severity vulnerabilities in the ColdFusion web app development platform and the Campaign Classic marketing automation platform.

All these vulnerabilities can be exploited in low-complexity attacks that don't require user interaction and were tagged with priority 1, indicating a high risk of being targeted.

"This update resolves vulnerabilities being targeted, or which have a higher risk of being targeted, by exploit(s) in the wild for a given product version and platform. Adobe recommends administrators install the update as soon as possible. (for example, within 72 hours),"Adobe says.

" Adobe is not aware of any exploits in the wild for any of the issues addressed in these updates," the company added in advisories released on Tuesday.

Six of these critical security flaws (tracked as CVE-2026-48276, CVE-2026-48277, CVE-2026-48281, CVE-2026-48316, and CVE-2026-48282) affectColdFusion versions 2025.9, 2023.20 and earlier, and can be exploited by attackers without privileges to gain remote code execution on unpatched systems.

TheCampaign Classicmax severity vulnerability (tracked as CVE-2026-48286) affects versions 7.4.3 build 9396 and earlier and could lead to arbitrary code execution in the current user's context after successful exploitation.

According to Adobe's security advisory, CVE-2026-48286 only affects on-premises Adobe Campaign instances (including fully on-premises deployments and on-premises components in hybrid deployments), as the flaw has already been patched on Adobe-hosted instances.

Aanchal Gupta, Adobe's Chief Security Officer (CSO), also announced on Thursday that the company will switch to twice-monthly security bulletins to deploy security updates faster.

"Effective July 14, 2026, Adobe is moving from monthly to twice-monthly publication of Adobe Security Bulletins and Advisories on the second and fourth Tuesday of each month,"Gupta said. "For actively exploited vulnerabilities or externally discovered zero-day vulnerabilities, our out-of-band response process remains in effect."

In early April, Adobe alsorolled out emergency patchesto fix an Acrobat Reader vulnerability (CVE-2026-34621) that had been exploited in zero-day attackssince at least December.

Over the last five years, the Cybersecurity and Infrastructure Security Agency (CISA)has added 79 security flaws in Adobe productsto its catalog of actively exploited vulnerabilities, 10 of which have also been abused by ransomware gangs.

## Test every layer before attackers do

Security teams log 54% of successful attacks and alert on just 14%. The rest move through your environment unseen.

The Picus whitepaper shows how breach and attack simulation tests your SIEM and EDR rules so threats stop slipping by detection.

Get the whitepaper

### Related Articles:

Over 900 Oracle E-Business instances exposed to ongoing attacks

Critical SimpleHelp flaw exploited to deploy new stealer malware

Hackers now exploit critical Oracle E-Business flaw in attacks

CISA sets urgent deadline to fix Cisco flaw exploited in attacks

CISA warns of max severity Ubiquiti flaws exploited in attacks