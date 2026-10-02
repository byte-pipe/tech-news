---
title: Critical Cisco Catalyst SD-WAN Manager API authentication bypass exploited in the wild (CVE-2026-76504)
url: https://www.rapid7.com/blog/post/etr-critical-cisco-catalyst-sd-wan-manager-api-authentication-bypass-exploited-in-the-wild-cve-2026-76504
site_name: tldr
content_file: tldr-critical-cisco-catalyst-sd-wan-manager-api-authent
fetched_at: '2026-10-03T03:07:11.221163'
original_url: https://www.rapid7.com/blog/post/etr-critical-cisco-catalyst-sd-wan-manager-api-authentication-bypass-exploited-in-the-wild-cve-2026-76504
author: Rapid7
date: '2026-10-03'
description: On September 30, 2026, Cisco published a security advisory for CVE-2026-76504, a critical API authentication bypass vulnerability affecting Cisco Catalyst SD-WAN Manager. The vulnerability has a CVSSv3.1 score of 9.8 and results from improper handling of URL encoding (CWE-177). An unauthenticated, remote attacker can send a crafted HTTP request that bypasses an authentication rule for a specific API endpoint, gaining access to the API with the privileges of the admin user.
tags:
- tldr
---

Emergent Threat Response

# Critical Cisco Catalyst SD-WAN Manager API authentication bypass exploited in the wild (CVE-2026-76504)

Rapid7
Sep 30, 2026
|
Last updated on
 
Oct 1, 2026
|
4
 
min read

Critical Cisco Catalyst SD-WAN Manager API authentication bypass exploited in the wild (CVE-2026-76504)

Table of contents

Critical Cisco Catalyst SD-WAN Manager API authentication bypass exploited in the wild (CVE-2026-76504)

Table of contents

## Overview

On September 30, 2026, Ciscopublished a security advisoryforCVE-2026-76504, a critical API authentication bypass vulnerability affecting Cisco Catalyst SD-WAN Manager. The vulnerability has a CVSSv3.1 score of9.8and results from improper handling of URL encoding (CWE-177). An unauthenticated, remote attacker can send a crafted HTTP request that bypasses an authentication rule for a specific API endpoint, gaining access to the API with the privileges of the admin user.

According to Cisco, CVE-2026-76504 is being actively exploited in the wild; Cisco PSIRT became aware of the activity in September 2026. Cisco Catalyst SD-WAN Manager systems with ports exposed to the internet are at risk of compromise. The vulnerability affects the product regardless of system configuration, and Cisco has not provided a workaround, however vendor supplied updates are available. Rapid7 strongly recommends that organizations upgrade affected systems to a fixed release on an emergency basis, outside of normal patch cycles, and investigate internet-facing systems for signs of exploitation.

Cisco Catalyst SD-WAN Manager was also affected by two critical, unauthenticated peering authentication flaws earlier in 2026:CVE-2026-20127and Rapid7-discoveredCVE-2026-20182. Both were distinct issues in thevdaemonservice and similar parts of its networking stack. CVE-2026-76504 targets a separate API authentication path, but the recurrence of authentication bypasses in internet-facing Catalyst SD-WAN control components reinforces the need for emergency remediation.

On September 30, 2026, CVE-2026-76504 wasadded to the U.S. Cybersecurity and Infrastructure Security Agency's (CISA) list of known exploited vulnerabilities (KEV), based on evidence of active exploitation. CISA set a remediation due date of October 3, 2026.

## Mitigation guidance

Cisco has released software updates that remediate CVE-2026-76504. Organizations running affected instances of Cisco Catalyst SD-WAN Manager should upgrade to an appropriate fixed release listed below without waiting for a regular patch cycle:

Cisco Catalyst SD-WAN Software release

First fixed release

Earlier than20.9

Migrate to a fixed release

20.9

20.9.10.1

20.12

20.12.8.2

20.15

20.15.6.1

20.18

20.18.4.1

26.1

26.1.2.1

26.2

26.2.1

Cisco has addressed the vulnerability in the cloud-based Cisco SD-WAN Cloud (Cisco Managed) release20.15.605, and indicates that no customer action is required for that service.

There are no workarounds. As a temporary mitigation, Cisco recommends that on-premises customers prevent access to the system from unsecured networks. If internet access is required, restrict access to known, trusted hosts and protect Cisco Catalyst SD-WAN control components behind a filtering device. Cisco indicates that this mitigation is already deployed in Cisco Catalyst SD-WAN Cloud Hosted environments. Organizations should apply updates even when the mitigation is in place.

Because active exploitation has occurred, Rapid7 strongly recommends that organizations audit affected systems for compromise. For help assessing a potentially compromised system, Cisco customers may open a Severity 3 TAC case with CVE-2026-76504 in the title and provide anadmin-techfile generated with therequest admin-techcommand.

For the latest mitigation guidance and release compatibility information, please refer to thevendor's security advisory.

## Rapid7 customers

### Exposure Command, Vulnerability Management, and Nexpose

Exposure Command, Vulnerability Management, and Nexpose customers can assess exposure to CVE-2026-76504 with vulnerability checks expected to be available in the October 1 content release.

## Indicators of compromise

Cisco recommends reviewing the following logs for requests related toj_security_checkfrom unknown or unauthorized IP addresses:

* /var/log/nms/containers/service-proxy/serviceproxy-access.log: Requests with an encoded character in thej_security_checkpath, such asPOST /%6a_security_check HTTP/1.1.
* /var/log/nms/vmanage-server.log: Requests toj_security_checkassociated with usernames beginning withviptela-reserved-.

The%6avalue, which URI-encodes the characterj, is only an example. According to Cisco, an attacker can exploit the vulnerability by encoding any single character in the request. The vendor cautions that these log entries can also occur during standard operations and should be evaluated against normal network posture to avoid false positives.

## Updates

* September 30, 2026: Initial publication.
* October 1, 2026: Updated to reflect CVE-2026-76504 being added to the CISA KEV list.

## Article tags

* Emergent Threat Response
* Vulnerability Management
* Labs

## Explore more from Rapid7

### Vulnerability & Exploit Database

Rapid7s curated database of vulnerabilities, featuring exploit modules and check methods integrated into the Metasploit Framework.

Search the database

### Rapid7 Labs

The threat research behind the alerts: adversary tracking, curated intelligence, and flagship threat reports.

Explore the research

### Rapid7 MDR

Gain 24x7 XDR monitoring, remediation, and DFIR from experts that extend your team to help secure your extended ecosystem.

Explore MDR

### Exposure management

Get continuous assessment of your attack surface with the critical context to validate and extinguish vulnerabilities and policy gaps.

See how it works