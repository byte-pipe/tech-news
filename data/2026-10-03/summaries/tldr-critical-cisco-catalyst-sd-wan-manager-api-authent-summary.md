---
title: Critical Cisco Catalyst SD-WAN Manager API authentication bypass exploited in the wild (CVE-2026-76504)
url: https://www.rapid7.com/blog/post/etr-critical-cisco-catalyst-sd-wan-manager-api-authentication-bypass-exploited-in-the-wild-cve-2026-76504
date: 2026-10-03
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-10-03T03:07:48.480504
---

# Critical Cisco Catalyst SD-WAN Manager API authentication bypass exploited in the wild (CVE-2026-76504)

# Critical Cisco Catalyst SD-WAN Manager API authentication bypass exploited in the wild (CVE-2026-76504)

## Overview
- Cisco disclosed a critical API authentication bypass (CVE‑2026‑76504) on 30 Sep 2026.  
- CVSS v3.1 score: **9.8**; root cause: improper URL‑encoding handling (CWE‑177).  
- An unauthenticated remote attacker can craft an HTTP request that bypasses authentication for a specific API endpoint, gaining admin‑level access.  
- Cisco PSIRT observed active exploitation in September 2026; systems with internet‑exposed ports are at risk.  
- No workaround is provided; vendor‑supplied updates are available.  
- The flaw follows two earlier 2026 unauthenticated peering authentication bugs (CVE‑2026‑20127, CVE‑2026‑20182).  
- Added to CISA’s Known Exploited Vulnerabilities (KEV) list on 30 Sep 2026 with a remediation deadline of 3 Oct 2026.

## Mitigation guidance
- **Upgrade** to a fixed Cisco Catalyst SD‑WAN Manager release immediately (outside normal patch cycles). Fixed releases include:  

| Product version | First fixed release |
|-----------------|---------------------|
| < 20.9          | 20.9.10.1           |
| 20.12           | 20.12.8.2           |
| 20.15           | 20.15.6.1           |
| 20.18           | 20.18.4.1           |
| 26.1            | 26.1.2.1            |
| 26.2            | 26.2.1              |

- Cisco SD‑WAN Cloud (Managed) release 20.15.605 is already patched; no customer action required.  
- Temporary mitigation: block internet access to on‑premises controllers, or restrict it to trusted hosts behind a filtering device.  
- Even with mitigation, apply the updates.  
- Audit for compromise: open a Severity‑3 TAC case titled “CVE‑2026‑76504” and attach an `admin-tech` file generated via the `admin-tech` command.

## Indicators of compromise
- Review logs for suspicious `j_security_check` requests from unknown IPs:  
  - `/var/log/nms/containers/service-proxy/serviceproxy-access.log` – e.g., `POST /%6a_security_check HTTP/1.1`.  
  - `/var/log/nms/vmanage-server.log` – requests where the username starts with `viptela-reserved-`.  
- Any single character may be URI‑encoded; treat findings in context to avoid false positives.

## Updates
- **30 Sep 2026** – Initial publication.  
- **1 Oct 2026** – Noted addition to CISA KEV list.

## Rapid7 customers
- Exposure Command, Vulnerability Management, and Nexpose will include checks for CVE‑2026‑76504 in the 1 Oct 2026 content release.