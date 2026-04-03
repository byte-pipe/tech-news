---
title: Cloudflare outage on November 18, 2025
url: https://blog.cloudflare.com/18-november-2025-outage/
date: 2025-11-18
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-11-19T11:16:56.515693
screenshot: hackernews_api-cloudflare-outage-on-november-18-2025.png
---

# Cloudflare outage on November 18, 2025

# Cloudflare Outage on November 18, 2025

November 18, 2025

## Overview

* Cloudflare network experienced significant failures to deliver core network traffic between 11:20 UTC and 14:30 UTC
* The issue was caused by a change in database permissions that output multiple entries into a "feature file" used by the Bot Management system
* **Feature file doubled in size**, causing errors to propagate to customers' sites

## Symptoms and Error Messages

* Customers experienced an error page indicating a failure within Cloudflare's network
* Volume of 5xx error HTTP status codes increased significantly, peaking around 11:20 UTC

## Impact and Corrective Actions

* The issue was quickly identified as a problem with the Bot Management system's ability to keep up with changing threats
* A later version of the "feature file" was released to correct the issue, allowing traffic to resume flowing freely by 14:30 UTC
* Systems were mitigated over the next few hours to reduce increased load on network components

## Analysis and Conclusion

* The failure was an unusual exception, and Cloudflare is taking steps to prevent similar outages in the future
* A review of the systems will be performed to learn from this event and improve overall resilience
