---
title: GitHub Status
url: https://www.githubstatus.com
date: 2026-04-27
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-04-28T06:04:36.643616
---

# GitHub Status

# GitHub Status Summary

## Subscription Options
- **Email notifications** for incident creation, updates, and resolution (requires OTP verification).  
- **SMS/text message alerts** with selectable country codes (global list provided).  
- **Slack integration** to receive incident updates directly in a Slack channel.  
- **Webhook** configuration to receive JSON payloads for incident events (create, update, resolve, component changes).  
- **Atom/RSS feeds** for status updates.  
- All subscription methods are subject to the GitHub Privacy Policy, Atlassian Terms of Service, and reCAPTCHA protection.

## Recent Incident: “GitHub search is degraded” (April 27 2026)
- **Primary issue:** Users experienced intermittent failures when viewing issues, pull requests, projects, and Actions workflow runs; overall search functionality was degraded.  
- **Root cause:** Excessive load on ElasticSearch clusters caused connectivity problems and downstream service interruptions.  
- **Mitigation steps:**  
  - Identified and disabled the source of additional load on ElasticSearch.  
  - Observed signs of recovery after load reduction.  
  - Ongoing investigation into connectivity issues and performance degradation across multiple components (Pull Requests, Packages, Issues, Actions).  
- **Timeline of updates:**  
  - 19:50 UTC – Source of load disabled; recovery signs noted.  
  - 18:19 UTC – Pull Requests degraded; investigation ongoing.  
  - 18:17 UTC – Continued ElasticSearch connectivity issues; intermittent downstream impact.  
  - 17:35 UTC – Users reporting intermittent failures across issues, PRs, projects, and Actions.  
  - 16:53 UTC – Packages performance degraded.  
  - 16:39 UTC – Issues performance degraded.  
  - 16:36 UTC – Broad search failures affecting workflow runs and project loading.  
  - 16:33 UTC – Investigation into Actions performance degradation.  

## How to Stay Informed
- Subscribe via the preferred channel (email, SMS, Slack, webhook, or feed).  
- Acknowledge the relevant privacy policies and terms of service when subscribing.  
- Follow the official @githubstatus Twitter account for real‑time updates.