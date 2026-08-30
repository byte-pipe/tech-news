---
title: Critical Keycloak Password Reset Flaw Could Let Unauthenticated Attackers Take Over Any Account
url: https://thehackernews.com/2026/08/critical-keycloak-password-reset-flaw.html
site_name: tldr
content_file: tldr-critical-keycloak-password-reset-flaw-could-let-un
fetched_at: '2026-08-30T15:12:06.341320'
original_url: https://thehackernews.com/2026/08/critical-keycloak-password-reset-flaw.html
author: The Hacker News
date: '2026-08-30'
description: Keycloak CVE-2026-18963 could let unauthenticated attackers skip the emailed action token and reset any user's password.
tags:
- tldr
---

# Critical Keycloak Password Reset Flaw Could Let Unauthenticated Attackers Take Over Any Account


Swati Khandelwal

Aug 24, 2026
Vulnerability / Identity Security

Red Hat and the Keycloak project have released patches to address a critical security flaw in the open-source identity and access management server that could allow an unauthenticated remote attacker to take over any user account by forcing a password reset.

The vulnerability, assigned the CVE identifierCVE-2026-18963, is rated 9.1 on the CVSS scoring system by Red Hat, which acts as the CVE Numbering Authority (CNA) for the flaw. It has been classified as a weak password recovery mechanism for a forgotten password (CWE-640).

Users of upstream Keycloak are advised to update to version 26.7.2, released August 19, 2026, while customers running Red Hat build of Keycloak (RHBK) should apply the updates shipped for 26.4.15 and 26.6.6.

There is no evidence that the flaw has been exploited, and no verified public exploit has been located as of August 24, 2026.

Red Hat said inits CVE advisorythat the root cause is "improper state validation within the reset-credentials authentication flow," the sequence Keycloak runs when a user requests password recovery. The company assessed the severity as Critical because an unauthenticated remote attacker can exploit the flaw without any user interaction.

The defect lies in how the flow's state is managed, according tothe Red Hat bug report. An attacker sends a specially crafted request to the reset-credentials endpoint. The authentication session then transitions directly to the password update phase. The action token that Keycloak normally sends via email is never required.

Successful exploitation results in a complete account takeover of any user, "including administrative accounts," by resetting their password.

Escape researcher Enzo Mongin, writing abouta separate Keycloak access-control flawhe disclosed in July, said an attacker who crosses one of the server's boundaries does not stop at Keycloak, and that "they get into everything sitting behind it."

Red Hat issued four errata on August 18, 2026 (RHSA-2026:56519,RHSA-2026:56520,RHSA-2026:56523andRHSA-2026:56524), covering the standalone server packages and the container images for two RHBK streams. Thefixed versionsare as follows -

* Red Hat build of Keycloak 26.4is unaffected from operator bundle 26.4.15-1, and from the rhbk/keycloak-rhel9 and rhbk/keycloak-rhel9-operator images 26.4-23
* Red Hat build of Keycloak 26.6is unaffected from operator bundle 26.6.6-1 and from the keycloak-rhel9 and operator containers 26.6-12
* Upstream Keycloakis fixed in 26.7.2

The GitHub advisoryfor the flaw lists both the affected and the patched versions as unknown, and the CVE record carries only Red Hat product references.

The initial CVE record listed Red Hat Single Sign-On 7 as unaffected and the Red Hat JBoss Enterprise Application Platform Expansion Pack as affected. A later revision narrowed the product list, and NVD's display truncates it, so the current status of both is not established.

For deployments that cannot be updated immediately, Red Hat has published a temporary mitigation -- turn off the "Forgot password" functionality across all realms. In the RHBK administration console, the setting sits under Realm settings, then Login, then Forgot password. Red Hat said the setting must be applied to every realm and that customers should upgrade to a fixed version as soon as possible.

CVE-2026-18963 was one of eight CVE identifiers listed as fixed inthe Keycloak 26.7.2 release notes. The same release addressed CVE-2026-15571, a predictable account-linking hash that enables account takeover through a malicious OpenID Connect (OIDC) client.

Two weeks earlier, on August 5, 2026, Keycloak 26.7.1 shippedfixes for twelve CVEs, including a SAML identity-provider-initiated broker login that bypassed a link-only restriction and a default dynamic client registration policy that allowed role forgery via user property mappers.

Separately, Univention said in a post published August 20 that "Nubus is not affected by this issue" because the forgotten-password feature is not activated in its Keycloak deployments. Red Hat credited James Paremain with reporting the flaw.

No source addresses whether the fix fully resolves the flaw.

Whether every realm with the forgotten-password feature enabled is exploitable, or only certain reset-credentials flow configurations, is not stated by any of the published sources.

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
enterprise security
, 
Open Source
, 
password security
, 
Software Security
, 
Vulnerability

⚡ Top Stories This Week

Critical Keycloak Password Reset Flaw Could Let Unauthenticated Attackers Take Over Any Account

⚡ Weekly Recap: AI-Powered PLC Attacks, GitLab Attacks, Stripe Key Leaks and More

Actively Exploited Oracle WebLogic Flaw Lets Unauthenticated Attackers Access Critical Data

WhatsApp Adds Multiple Passkeys for Phishing-Resistant Sign-Ins Across iOS and Android

A Malicious Webpage Could Poison Your Local AI Model Behind NVIDIA NemoClaw

Critical Gitea RCE Actively Exploited as Reported Attack Drops Miner-Like Payload

Claude Opus 4.6 Bypasses Gym Booking Limit, Cancels Other Users' Reservations in Tests

CISA Red Team Compromised Two Critical Infrastructure Orgs, One Detected Nothing

FBI Disrupts China-Linked QTFY Infrastructure Used to Steal Data From U.S. Organizations

New GPUThor Rowhammer Defeats ECC on NVIDIA RTX A6000 to Gain Host Root Access

Alleged TeamPCP Hackers Charged in Australia Over Major Supply Chain Attacks

ThreatsDay: 296K IoT Botnet, 100+ Water Systems Targeted, SharePoint RCE Chain + 27 New Stories

Next.js Patches Critical AVIF and Windows Flaws Enabling Unauthenticated RCE

OpenAI Says Reward Hacking Drove AI Agents to Exploit Zero-Days and Breach Hugging Face

Critical cPanel Flaw Could Let One Hosting Customer Take Root Control of a Whole Server

PaperCut Zero-Day Exploited in Attacks, Affecting All NG and MF Versions

Three CVSS 10.0 ServiceNow Flaws Could Let Unauthenticated Attackers Execute Code and SQL

Attackers Chain Two PaperCut Flaws to Execute Code Without Authentication

Learn How to Build Security Operations Ready for AI-Powered Attacks

Imagine the SOC Without a Queue: From Alert Backlog to AI Hypothesis Engine

Mirage2FA Surge Hits 4,500 US and EU Companies, Abusing Microsoft 365 Login Flows

Frontier AI: Vulnerability Management's Systemic Revolution

Why AI Teams Need Verifiable Search Data Instead of Black-Box Signals

Why Threat Intelligence Needs OT Context to Protect Critical Infrastructure

⭐ Featured Resources

See How Keeper Secrets Manager Removes Hard-Coded Credentials

Download the CISO's Guide to Smarter AI Security Investment

Phishing Is Costing Security Teams More Than Ever — Read the New Report

Build AI Agents and Automations Without Losing Security Control