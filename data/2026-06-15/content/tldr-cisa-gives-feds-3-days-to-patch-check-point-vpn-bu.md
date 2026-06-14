---
title: CISA gives feds 3 days to patch Check Point VPN bug exploited as zero-day
url: https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-check-point-flaw-exploited-by-ransomware-gangs/
site_name: tldr
content_file: tldr-cisa-gives-feds-3-days-to-patch-check-point-vpn-bu
fetched_at: '2026-06-15T06:00:25.733429'
original_url: https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-check-point-flaw-exploited-by-ransomware-gangs/
date: '2026-06-15'
description: CISA has ordered U.S. government agencies to secure their Check Point Remote Access VPN and Mobile Access deployments against a critical vulnerability exploited in zero-day attacks by Qilin ransomware affiliates.
tags:
- tldr
---

# CISA gives feds 3 days to patch Check Point VPN bug exploited as zero-day

 By 

###### Sergiu Gatlan

* June 9, 2026
* 04:18 AM
* 0

CISA has ordered U.S. government agencies to secure their Check Point Remote Access VPN and Mobile Access deployments against a critical vulnerability exploited in zero-day attacks by Qilin ransomware affiliates.

Unauthenticated remote attackers can exploit this security flaw (tracked asCVE-2026-50751) to bypass authentication and establish a remote access VPN connection on targeted Mobile Access/SSL VPNs, Remote Access VPNs, or Spark firewalls.

The vulnerability affects only instances configured to use the deprecated IKEv1 key exchange protocol, with security gateways that don't require a machine certificate for connections and accept legacy Remote Access clients.

Israeli cybersecurity company Check Point releasedsecurity updates to address CVE-2026-50751on Monday, flagging it as exploited in attacks that began on May 7 and surged over the weekend.

Although these attacks have only led to breaches at "a few dozen" organizations worldwide, Check Point has linked at least one incident to the Qilin Ransomware-as-a-Service (RaaS) operation, which has claimed over 400 victims on its dark web leak site since it surfaced in August 2022.

"To date, the observed exploitation has been limited to a few dozen targeted organizations globally. One case involved confirmed post-compromise activity associated with Qilin ransomware affiliate," the company said. "Customers using IKEv1 key exchange protocol are strongly encouraged to apply the available security updates immediately."

Check Point has also shared mitigation measures for those who can't patch, advising them to remove support for the legacy remote access client, configure global properties for Remote Access VPN Authentication to IKEv2 only, enable IPS and download the signatures, and configure Machine Certificate Authentication as mandatory.

## Feds ordered to patch by June 11

Yesterday, CISA alsoaddedCVE-2026-50751 to itsKnown Exploited Vulnerabilities (KEV) Catalog, ordering Federal Civilian Executive Branch (FCEB) agencies to secure their devices by June 11, as mandated byBinding Operational Directive (BOD) 22-01.

"This type of vulnerability is a frequent attack vector for malicious cyber actors and poses significant risks to the federal enterprise," the cybersecurity agency noted.

"Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable."

While this binding operational directive applies only to U.S. federal agencies, CISA urged all security teams (including those in the private sector) to deploy patches for CVE-2026-50751 and secure their organizations' networks as soon as possible.

Two years ago, CISA tagged another vulnerability (CVE-2024-24919) in Check Point's Quantum Security Gateways as actively exploited by ransomware gangs, confirming an Orange Cyberdefense CERT reportlinking it to NailaoLocker ransomware attacks.

## Test every layer before attackers do

Security teams log 54% of successful attacks and alert on just 14%. The rest move through your environment unseen.

The Picus whitepaper shows how breach and attack simulation tests your SIEM and EDR rules so threats stop slipping by detection.

Get the whitepaper

### Related Articles:

Check Point links VPN zero-day attacks to Qilin ransomware gang

Palo Alto Networks firewall zero-day exploited for nearly a month

CISA orders feds to patch actively exploited Ivanti flaw by Sunday

CISA orders feds to patch exploited Ivanti EPMM flaw by Saturday

CISA flags new SD-WAN flaw as actively exploited in attacks