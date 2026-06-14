---
title: Check Point links VPN zero-day attacks to Qilin ransomware gang
url: https://www.bleepingcomputer.com/news/security/check-point-links-vpn-zero-day-attacks-to-qilin-ransomware-gang/
site_name: tldr
content_file: tldr-check-point-links-vpn-zero-day-attacks-to-qilin-ra
fetched_at: '2026-06-14T19:34:11.914977'
original_url: https://www.bleepingcomputer.com/news/security/check-point-links-vpn-zero-day-attacks-to-qilin-ransomware-gang/
date: '2026-06-14'
description: Israeli cybersecurity company Check Point has released security updates to patch a critical flaw affecting Remote Access VPN and Mobile Access deployments, which was exploited in zero-day attacks.
tags:
- tldr
---

# Check Point links VPN zero-day attacks to Qilin ransomware gang

 By 

###### Sergiu Gatlan

* June 8, 2026
* 09:05 AM
* 0

Israeli cybersecurity company Check Point has released security updates to patch a critical flaw affecting Remote Access VPN and Mobile Access deployments, which was exploited in zero-day attacks.

Tracked asCVE-2026-50751, this vulnerability can be exploited by unauthenticated, remote attackers to bypass authentication on targeted Mobile Access / SSL VPNs, Remote Access VPNs, or Spark firewalls and establish a remote access VPN connection.

According to the company, this security flaw affects only deployments configured to use the deprecated IKEv1 key exchange protocol, with security gateways that accept legacy Remote Access clients and do not require a machine certificate for connections.

The attacks began on May 7, surged in early June, and have affected only "a few dozen" organizations worldwide, with at least one incident linked to the Qilin ransomware operation.

"Check Point Research has identified active exploitation of CVE-2026-50751, a critical authentication bypass vulnerability affecting Check Point Remote Access VPN and Mobile Access deployments configured to use the deprecated IKEv1 key exchange protocol,"the company warned.

"To date, the observed exploitation has been limited to a few dozen targeted organizations globally. One case involved confirmed post-compromise activity associated with Qilin ransomware affiliate. Customers using IKEv1 key exchange protocol are strongly encouraged to apply the available security updates immediately."

Check Point also shared mitigation measures for customers who can't immediately patch vulnerable systems and advised them to remove support for the legacy remote access client, configure global properties for Remote Access VPN Authentication to IKEv2 only, set the Machine Certificate Authentication as mandatory, and enable IPS and download the signatures.

While investigating the CVE-2026-50751 flaw, Check Point found a second vulnerability (tracked as CVE-2026-50752) that affects certificate validation in deprecated IKEv1 key exchange that can be exploited in man-in-the-middle attacks on site-to-site VPN connections.

Although Check Point has not yet found evidence of CVE-2026-50752 exploitation in the wild, it advised customers to apply updates to mitigate potential exposure.

Qilin surfaced in August 2022 as a Ransomware-as-a-Service (RaaS) operation under the "Agenda" name and has since claimed responsibility for nearly 400 victims on its dark web leak site.

The gang's list of victims also includes high-profile organizations such as automotive giantYangfeng,Nissan, Japanese beer companyAsahi, publishing giantLee Enterprises,pathology services provider Synnovis, andAustralia's Court Services Victoria.

## Test every layer before attackers do

Security teams log 54% of successful attacks and alert on just 14%. The rest move through your environment unseen.

The Picus whitepaper shows how breach and attack simulation tests your SIEM and EDR rules so threats stop slipping by detection.

Get the whitepaper

### Related Articles:

CISA gives feds 3 days to patch Check Point VPN bug exploited as zero-day

Palo Alto Networks firewall zero-day exploited for nearly a month

Palo Alto Networks warns of firewall RCE zero-day exploited in attacks

Oracle mitigates PeopleSoft zero-day exploited in data theft attacks

Ivanti warns of new actively exploited MobileIron zero-day bug