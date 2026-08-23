---
title: Citrix urges admins to patch new NetScaler flaws as soon as possible
url: https://www.bleepingcomputer.com/news/security/citrix-urges-admins-to-patch-new-netscaler-flaws-as-soon-as-possible
site_name: tldr
content_file: tldr-citrix-urges-admins-to-patch-new-netscaler-flaws-a
fetched_at: '2026-08-23T19:21:44.597775'
original_url: https://www.bleepingcomputer.com/news/security/citrix-urges-admins-to-patch-new-netscaler-flaws-as-soon-as-possible
date: '2026-08-23'
description: Citrix has warned customers to immediately secure their systems against two vulnerabilities affecting NetScaler Gateway secure remote access solutions and NetScaler ADC networking appliances.
tags:
- tldr
---

# Citrix urges admins to patch new NetScaler flaws as soon as possible

 By 

###### Sergiu Gatlan

* August 20, 2026
* 08:14 AM
* 0

Citrix has warned customers to immediately secure their systems against two vulnerabilities affecting NetScaler Gateway secure remote access solutions and NetScaler ADC networking appliances.

The most severe of the two, tracked asCVE-2026-19490, can allow remote attackers without privileges to bypass authentication when the appliance is configured as an AAA virtual server or as a Gateway (SSL VPN, ICA Proxy, CVPN, RDP Proxy), depending on the NetScaler firmware version and whether SAML Action is configured.

Admins can check if an appliance is vulnerable to attacks targeting CVE-2026-19490 by inspecting their NetScaler configuration for SAML action configuration (add authentication samlAction .*) string and Auth or VPN vserver ('add authentication vserver .*' and 'add vpn vserver .*') strings.

The second, a high-severity memory overflow security flaw tracked asCVE-2026-19489, can be abused by remote unauthenticated threat actors in denial-of-service (DoS) attacks when SIP ALG (Session Initiation Protocol Application Layer Gateway) is enabled on a large-scale NAT group configuration.

Security teams can determine whether Citrix NetScaler appliances on their network meet the preconditions for CVE-2026-19489 exploitation by inspecting their configuration for the "add lsn group.*sipalg.*" string.

Citrix advised customers to upgrade vulnerable NetScaler ADC and NetScaler Gateway appliances to:

* NetScaler ADC and NetScaler Gateway 14.1-73.32 or later,
* NetScaler ADC and NetScaler Gateway 13.1-63.21 or later,
* NetScaler ADC FIPS 14.1-73.32 FIPS or later,
* or NetScaler ADC FIPS and NDcPP 13.1-37.277 or later, as applicable

"We strongly recommend that customers review theofficial NetScaler ADC and NetScaler Gateway security bulletin, assess whether their deployments are affected, and upgrade impacted appliances to the recommended builds as soon as possible,"Citrix warnedon Wednesday.

"The bulletin applies to supported versions of customer-managed NetScaler ADC and NetScaler Gateway, including certain FIPS and NDcPP builds. SecurAccess ZTNA Hybrid (formerly Secure Private Access Hybrid) deployments that use customer-managed NetScaler instances are also affected and should be upgraded to the recommended builds."

While these security flaws have not been flagged as exploited in attacks, Citrixurged adminsto patch two other NetScaler vulnerabilities (CVE-2026-3055andCVE-2026-4368) on March 23, just days before attackersbegan abusing them in the wild.

CISAaddedthe CVE-2026-3055 vulnerability to its Known Exploited Vulnerabilities (KEV) Catalog on March 30 and ordered federal agencies to secure vulnerable Citrix appliances within three days.

Over the last five years, the U.S. cybersecurity agencyhas flagged 22 Citrix vulnerabilitiesas exploited in the wild, six of them also abused in ransomware attacks.

The ShadowServer Foundation now tracksover 22,000 NetScaler ADCandnearly 1,800 NetScaler Gateway instancesexposed online. However, it does not provide information on the number of honeypots or how many may be vulnerable to attacks targeting CVE-2026-19489 and CVE-2026-19490.

## Once attackers have valid credentials, only 37% of their actions are blocked

Overall prevention scores can hide what happens after initial access. Once attackers are using valid credentials, prevention drops sharply.

The Blue Report 2026 measures defenses technique by technique across 338 million simulations run in customer production environments.

Get the report

### Related Articles:

Cisco warns of high-severity ClamAV flaws with public exploits

HollowByte DDoS flaw bloats OpenSSL server memory with 11-byte payload

Hackers exploit macOS Screen Sharing flaw to deploy Monero miner

Cisco warns of ASA and FTD VPN flaw exploited to crash devices

N-able warns of N-central auth bypass flaw exploited in attacks