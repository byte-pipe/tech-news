---
title: 'Ivanti: Max severity Sentry flaw allows code execution as root'
url: https://www.bleepingcomputer.com/news/security/new-max-severity-ivanti-sentry-flaw-allows-code-execution-as-root/
site_name: tldr
content_file: tldr-ivanti-max-severity-sentry-flaw-allows-code-execut
fetched_at: '2026-06-18T19:50:06.948265'
original_url: https://www.bleepingcomputer.com/news/security/new-max-severity-ivanti-sentry-flaw-allows-code-execution-as-root/
date: '2026-06-18'
description: Ivanti has patched two critical vulnerabilities in its Sentry secure mobile gateway solution, including a maximum-severity flaw that enables remote attackers to execute code with root privileges.
tags:
- tldr
---

# Ivanti: Max severity Sentry flaw allows code execution as root

 By 

###### Sergiu Gatlan

* June 10, 2026
* 02:26 AM
* 0

Security software company Ivanti has released patches to address two critical vulnerabilities in its Sentry secure mobile gateway solution, including a maximum-severity flaw that enables remote attackers to execute code with root privileges.

Formerly known as MobileIron Sentry, Ivanti Sentry is a security gateway appliance that secures traffic between back-end corporate systems and remote mobile devices.

Tracked asCVE-2026-10520, the maximum-severity vulnerability stems from an OS command injection weakness. The second Sentry security flaw patched on Tuesday (tracked asCVE-2026-10523) is a critical authentication bypass that can be exploited remotely by unauthenticated attackers to create rogue administrative accounts and gain full administrative access.

Ivanti patched both security issues on Tuesday with the release of Sentry versions R10.5.2, R10.6.2, and R10.7.1.

Luckily, the company said it has no evidence that the two vulnerabilities are being exploited in the wild and advised admins to upgrade their systems to protect against potential attacks.

"We are not aware of any customers being exploited by these vulnerabilities at the time of disclosure,"Ivanti said. "Currently, there is no known public exploitation of this vulnerability that could be used to provide a list of indicators of compromise."

In recent years, Ivanti vulnerabilities have often been targeted in attacks because they provide an easy way for cybercriminals to breach targets' enterprise networks and steal sensitive corporate and customer data.

For instance, most recently, the Cybersecurity and Infrastructure Security Agency (CISA)ordered U.S. federal agenciesin May to patch their Ivanti devices after the companywarned customersto immediately patch a high-severity remote code execution vulnerability in Endpoint Manager Mobile (EPMM) that was exploited in zero-day attacks.

Multiple other Ivanti zero-days have been exploited inrecent yearsto breach a wide range of targets, includinggovernmentagenciesworldwide, includingtwo other critical EPMM vulnerabilitiesaddressed by Ivanti in January after being exploited as zero-days in attacks against a "very limited number of customers."

In total, CISA has tagged34 vulnerabilities across various Ivanti productsas actively exploited in attacks over the past several years, with 12 of them also used in ransomware attacks.

Ivanti's IT asset management solutions are used by over 40,000 clients worldwide and are supported by a network of over 7,000 partners and over 3,000 employees.

## Test every layer before attackers do

Security teams log 54% of successful attacks and alert on just 14%. The rest move through your environment unseen.

The Picus whitepaper shows how breach and attack simulation tests your SIEM and EDR rules so threats stop slipping by detection.

Get the whitepaper

### Related Articles:

Max severity Ivanti Sentry vulnerability now exploited in attacks

CISA orders feds to patch actively exploited Ivanti flaw by Sunday

CISA gives feds three days to patch Ivanti flaw exploited as zero-day

Exploit released for Ivanti Sentry bug abused as zero-day in attacks

Ivanti warns of new actively exploited MobileIron zero-day bug