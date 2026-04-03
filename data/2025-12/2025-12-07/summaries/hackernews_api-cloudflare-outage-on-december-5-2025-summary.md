---
title: Cloudflare outage on December 5, 2025
url: https://blog.cloudflare.com/5-december-2025-outage/
date: 2025-12-05
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-12-07T11:10:40.327880
screenshot: hackernews_api-cloudflare-outage-on-december-5-2025.png
---

# Cloudflare outage on December 5, 2025

# Cloudflare Outage on December 5, 2025

December 5, 2025
Dane Knecht

This post is also available in
Português
 and
Español (Latinoamérica)

**Incident Overview**

On December 5, 2025, at 08:47 UTC, Cloudflare experienced significant failures due to a change made to its logging logic used in detecting potential security threats. This incident was resolved approximately 25 minutes later when all services were fully restored.

**Causes of Failure**

The issue was not caused by malicious activity on Cloudflare's systems or Cyber attacks. Instead, it occurred as a result of combining two separate factors:

*   A vulnerability detection approach used in React Server Components that did not account for an industry-wide security weakness discovered this week.
*   A change made to the logging system within Cloudflare's Proxy component.

The second step was corrected after propagating changes to all affected servers using a global configuration method which doesn't require gradual rollouts. This led to unforeseen results where some of our rules modules began executing a critical Lua error upon receiving an HTTP request for one of these impacted customers.

**HTTP 500 Errors Served During the Incident**

During this incident, approximately 28% of all HTTP traffic was experienced by Cloudflare's network resulting in 500 errors being served from our WAF to clients while attempting legitimate functionality.
