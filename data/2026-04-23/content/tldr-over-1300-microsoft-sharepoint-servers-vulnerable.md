---
title: Over 1,300 Microsoft SharePoint servers vulnerable to spoofing attacks
url: https://www.bleepingcomputer.com/news/security/over-1-300-microsoft-sharepoint-servers-vulnerable-to-ongoing-attacks
site_name: tldr
content_file: tldr-over-1300-microsoft-sharepoint-servers-vulnerable
fetched_at: '2026-04-23T20:06:00.483156'
original_url: https://www.bleepingcomputer.com/news/security/over-1-300-microsoft-sharepoint-servers-vulnerable-to-ongoing-attacks
date: '2026-04-23'
description: Over 1,300 Microsoft SharePoint servers exposed online remain unpatched against a spoofing vulnerability that was exploited as a zero-day and is still being abused in ongoing attacks.
tags:
- tldr
---

# Over 1,300 Microsoft SharePoint servers vulnerable to spoofing attacks

 By 

###### Sergiu Gatlan

* April 22, 2026
* 02:53 AM
* 0

Over 1,300 Microsoft SharePoint servers exposed online remain unpatched against a spoofing vulnerability that was exploited as a zero-day and is still being abused in ongoing attacks.

The security flaw, tracked asCVE-2026-32201, affects SharePoint Enterprise Server 2016, SharePoint Server 2019, and SharePoint Server Subscription Edition (the latest on-premises version, which uses a "continuous update" model).

As Microsoft explained when it patched this security issue as part of the April 2026 Patch Tuesday, successful exploitation allows threat actors without privileges to perform network spoofing by taking advantage of an improper input validation weakness in low-complexity attacks that don't require user interaction.

"An attacker who successfully exploited the vulnerability could view some sensitive information (Confidentiality), make changes to disclosed information (Integrity), but cannot limit access to the resource (Availability),"it said.

While Microsoft flagged the vulnerability as a zero-day, it has yet to disclose how it was exploited in attacks or link this malicious activity to a specific threat actor or hacking group.

On Tuesday, Internet security watchdog group Shadowserver warned thatover 1,300 unpatched Microsoft SharePoint serversexposed online are still waiting to be secured, with fewer than 200 systems patched since Microsoft released CVE-2026-32201 security updates last week.

SharePoint servers vulnerable CVE-2026-32201 attacks (Shadowserver)

​The same day Microsoft released patches for CVE-2026-32201, CISAaddedthe vulnerability to itsKnown Exploited Vulnerabilities (KEV) Catalog.

The U.S. cybersecurity agency also ordered Federal Civilian Executive Branch (FCEB) agencies (executive branch non-military agencies, such as the Department of the Treasury and the Department of Homeland Security) to patch SharePoint servers within two weeks, by April 28, as mandated by the Binding Operational Directive (BOD) 22-01.

"This type of vulnerability is a frequent attack vector for malicious cyber actors and poses significant risks to the federal enterprise," it warned.

"Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable."

One week ago, CISA also flagged a Windows Task Host privilege escalation vulnerability as exploited in the wild, warning federal agencies to secure their devices as soon as possible, as it could allow attackers to gain SYSTEM privileges on vulnerable devices.

On April 14, Microsoft released security updates addressing 167 vulnerabilities, including two zero-day flaws, as part of itsApril 2026 Patch Tuesday.

## 99% of What Mythos Found Is Still Unpatched.

AI chained four zero-days into one exploit that bypassed both renderer and OS sandboxes. A wave of new exploits is coming.

At the Autonomous Validation Summit (May 12 & 14), see how autonomous, context-rich validation finds what's exploitable, proves controls hold, and closes the remediation loop.

Claim Your Spot

### Related Articles:

Actively exploited Apache ActiveMQ flaw impacts 6,400 servers

Over 14,000 F5 BIG-IP APM instances still exposed to RCE attacks

Critical Microsoft SharePoint flaw now exploited in attacks

Over 84,000 Roundcube instances vulnerable to actively exploited flaw

CISA orders feds to patch BlueHammer flaw exploited as zero-day