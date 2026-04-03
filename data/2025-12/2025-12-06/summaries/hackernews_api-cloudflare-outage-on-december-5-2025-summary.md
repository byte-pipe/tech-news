---
title: Cloudflare outage on December 5, 2025
url: https://blog.cloudflare.com/5-december-2025-outage/
date: 2025-12-05
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-12-06T11:11:22.100581
screenshot: hackernews_api-cloudflare-outage-on-december-5-2025.png
---

# Cloudflare outage on December 5, 2025

# Cloudflare outage on December 5, 2025

On December 5, 2025, at UTC:

* A portion of Cloudflare's network experienced significant failures due to a combination of factors
* The incident was resolved in approximately 25 minutes with all services restored
* Approximately 28% of all HTTP traffic served by Cloudflare were impacted

### Cause of the Outage

The issue was not caused by a cyber attack on Cloudflare's systems or malicious activity. Instead, it was triggered by changes made to the body parsing logic while attempting to detect and mitigate an industry-wide vulnerability in React Server Components.

### What Happened During the Incident

This graph shows HTTP 500 errors served during the incident timeframe compared to unaffected total Cloudflare traffic.

* The Web Application Firewall (WAF) provides protection against malicious payloads
* The proxy buffers HTTP request body content in memory for analysis, with a previous size set at 128KB but increased to 1MB for improved security

### Aftermath

As part of the incident response:

* A second change was made to turn off an internal WAF testing tool due to compatibility issues with updated React Server Components code
* This caused an error state in certain circumstances, leading to a sequence of Lua exceptions
* The error resulted in 500 HTTP error codes being served from the network

### Future Work

We will be publishing details next week about our efforts to mitigate similar incidents following this experience.
