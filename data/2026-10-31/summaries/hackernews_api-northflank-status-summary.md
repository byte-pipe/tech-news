---
title: Northflank - Status
url: https://status.northflank.com
date: 2026-10-31
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-10-31T19:04:07.826124
---

# Northflank - Status

# Northflank – Status Summary

## Security Incident Overview
- **Timeline of updates (UTC):**
  - Oct 31 2026 01:04 – Audit logs enabled for all customers, including free users.  
  - Oct 30 2026 23:38 – Reports of unauthorized use of AI API keys supplied to the platform. Users are urged to rotate all user‑provided secrets, revoke existing credentials, generate replacements, and update workloads. Review AI provider usage and billing for anomalies; report suspicious activity to Northflank support and the provider.  
  - Oct 30 2026 19:28 – Investigation ongoing; no further confirmed findings. Guidance: assume all environment variables are compromised, rotate all secrets (workloads, secret groups, global secrets), and disable public access to addons.  
  - Oct 30 2026 15:12 – Secret rotation for Postgres and MongoDB enabled for all users; recommendation to disable public exposure on addons. All users should treat environment variables as decrypted and rotate immediately.  
  - Oct 30 2026 13:58 – Directive to assume all environment variables have been decrypted; disable/rotate all keys.  
  - Oct 30 2026 13:40 – Immediate rotation of environment variables advised. Detailed timeline of engineering response includes network policy patches, additional patching, and engagement with Wiz CIRT support.  

- **Key observations:**
  - Multiple users confirmed unauthorized usage of AI keys.  
  - The pattern aligns with broader attacks on AI credentials (referenced in Wiz’s “Black October” report).  

## Outage Impact
- **Affected components (major outage):**
  - Networking  
  - Certificates  
  - Services  
  - Addons  
  - Jobs  
  - Builds  
  - Logs and Metrics  

- **Operational components (no outage):**
  - Northflank App – 99.82 % uptime  
  - Northflank API – 100 % uptime  
  - Marketing Site – 100 % uptime  
  - Documentation – 100 % uptime  

- **Overall platform status:** 7 components reported, overall uptime 99.12 %.

## Recommended Actions for Users
- Rotate all environment variables, secrets, and credentials immediately.  
- Revoke and regenerate any compromised API keys, especially AI provider keys.  
- Disable public exposure on any addons or services that were publicly accessible.  
- Review billing and usage logs for unexpected activity and report anomalies.  
- Monitor Northflank communications for further updates and patches.  

## Current Status
- Investigation remains ongoing; no additional confirmed findings at this time.  
- Audit logging is now active for all accounts to aid in detection and response.  

---  
*For the latest information, subscribe to updates or check the Northflank status page.*