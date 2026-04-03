---
title: Critical infra Honeywell CCTVs vulnerable to auth bypass flaw
url: https://www.bleepingcomputer.com/news/security/critical-infra-honeywell-cctvs-vulnerable-to-auth-bypass-flaw/
site_name: tldr
content_file: tldr-critical-infra-honeywell-cctvs-vulnerable-to-auth
fetched_at: '2026-02-22T11:08:25.465190'
original_url: https://www.bleepingcomputer.com/news/security/critical-infra-honeywell-cctvs-vulnerable-to-auth-bypass-flaw/
date: '2026-02-22'
description: The U.S. Cybersecurity and Infrastructure Security Agency (CISA) is warning of a critical vulnerability in multiple Honeywell CCTV products that allows unauthorized access to feeds or account hijacking.
tags:
- tldr
---

# Critical infra Honeywell CCTVs vulnerable to auth bypass flaw

 By

###### Bill Toulas

* February 18, 2026
* 03:58 PM
* 0

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) is warning of a critical vulnerability in multiple Honeywell CCTV products that allows unauthorized access to feeds or account hijacking.

Discovered by researcher Souvik Kanda and tracked as CVE-2026-1670, the security issue is classified as “missing authentication for critical function,” and received a crtical severity score of 9.8.

The flaw allows an unauthenticated attacker to change the recovery email address associated with a device account, enabling account takeover and unauthorized access to camera feeds.

“The affected product is vulnerable to an unauthenticated API endpoint exposure, which may allow an attacker to remotely change the "forgot password" recovery email address,”CISA says.

According to the security advisory, CVE-2026-1670 impacts the following models:

* I-HIB2PI-UL 2MP IP 6.1.22.1216
* SMB NDAA MVO-3 WDR_2MP_32M_PTZ_v2.0
* PTZ WDR 2MP 32M WDR_2MP_32M_PTZ_v2.0
* 25M IPC WDR_2MP_32M_PTZ_v2.0

Honeywell is a major global supplier of security and video surveillance equipment with a broad range of CCTV camera models and related products deployed in commercial, industrial, and critical infrastructure settings worldwide.

The company offers manyNDAA-compliantcameras that are suitable for deployment in U.S. government agencies and federal contractors.

The specific model families named in CISA’s advisory are mid-level video surveillance products used in small to medium business environments, offices, and warehouses, some of which may be part of critical facilities.

CISA stated that as of February 17th there were no known reports of public exploitation specifically targeting this vulnerability.

Nonetheless, the agency recommends minimizing network exposure of control system devices, isolating them behind firewalls, and using secure remote access methods such as updated VPN solutions when remote connectivity is necessary.

Honeywell has not published an advisory on CVE-2026-1670, but users are advised tocontact the company’s support teamfor patch guidance.

## The future of IT infrastructure is here

Modern IT infrastructure moves faster than manual workflows can handle.

In this new Tines guide, learn how your team can reduce hidden manual delays, improve reliability through automated response, and build and scale intelligent workflows on top of tools you already use.

Get the guide

### Related Articles:

CISA: BeyondTrust RCE flaw now exploited in ransomware attacks

CISA gives feds 3 days to patch actively exploited BeyondTrust flaw

Hackers breach SmarterTools network using flaw in its own software

SolarWinds Web Help Desk flaw is now exploited in attacks

CISA confirms active exploitation of four enterprise software bugs
