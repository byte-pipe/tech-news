---
title: Northflank - Status
url: https://status.northflank.com
site_name: hackernews_api
content_file: hackernews_api-northflank-status
fetched_at: '2026-10-31T19:03:22.619816'
original_url: https://status.northflank.com
author: js4ever
date: '2026-10-31'
description: Northflank Status
tags:
- hackernews
- trending
---

Security incident
Identified
·
Major outage
* Update·October 31, 2026 at 1:04 AMUTCWe have enabled audit logs for all customers, including free users.
* Update·October 30, 2026 at 11:38 PMUTCUsers have reported unauthorised use of AI API keys supplied to the Northflank platform.If you have not already rotated your user-provided secrets stored in Northflank, please do so immediately. Revoke existing credentials with their issuing providers, generate replacements, and update the affected secrets and workloads in Northflank. Review your AI provider usage and billing logs for unexpected activity, and report any suspicious usage to Northflank support and the relevant provider.These reports may be consistent with the broader pattern of attacks targeting AI credentials. Similar IP addresses are contained in this articleWiz’s “Black October” report.
* Update·October 30, 2026 at 7:28 PMUTCOur investigation is ongoing. We have no further confirmed findings to share at this time.Our guidance remains unchanged: assume all environment variables have been compromised and rotate all secrets and credentials immediately, including those in workloads, secret groups and global secrets. Disable public access to addons where enabled.We will share further updates as more information is confirmed.
* Update·October 30, 2026 at 3:12 PMUTCSecret rotation on Postgres and MongoDB has been enabled for all users. We recommend disabling public expose on addons if you have enabled that.All users should assume their environment variables are decrypted and begin rotation immediately.Secrets on workloadsSecret groupsGlobal secretsMultiple users are confirming that their AI keys have been used.
* Identified·October 30, 2026 at 1:58 PMUTCAssume all environment variables have been decrypted. Disable/rotate all keys.
* Investigating·October 30, 2026 at 1:40 PMUTCRotate environment variables immediately.11:43 UTC: Wiz threat alert11:44 UTC: Northflank engineers review the alert12:02 UTC: Initial network policy patch12:50 UTC: Additional patching deployed13:00 UTC: Wiz CIRT support requested13:05 UTC: Additional patching deployed13:05 UTC: Additional patching deployed
Subscribe

Collapse group

Northflank Platform
 
·
 
7 components
99.12% uptime

Networking - Major outage

Networking

Major outage

Certificates - Major outage

Certificates
Major outage

Services - Major outage

Services
Major outage

Addons - Major outage

Addons
Major outage

Jobs - Major outage

Jobs
Major outage

Builds - Major outage

Builds
Major outage

Logs and Metrics - Major outage

Logs and Metrics

Major outage

Northflank App - Operational

Northflank App
99.82% uptime
Read uptime graph for Northflank App

Northflank API - Operational

Northflank API
100.0% uptime
Read uptime graph for Northflank API

Marketing Site - Operational

Marketing Site
100.0% uptime
Read uptime graph for Marketing Site

Documentation - Operational

Documentation
100.0% uptime
Read uptime graph for Documentation
90 days ago
Today

## Recent notices

Show history
Show history
Show notice history