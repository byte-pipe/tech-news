---
title: How We Built Our Own DNS Server - DEV Community
url: https://dev.to/code42cate/how-we-built-our-own-dns-server-4d3k
date: 2026-04-17
site: devto
model: llama3.2:1b
summarized_at: 2026-04-22T20:18:20.839059
---

# How We Built Our Own DNS Server - DEV Community

**How We Built Our Own Production DNS Server: A 90-Minute Cut in Propagation Time**

In this article, we tell you how we migrated thousands of records off Hetzner DNS, which was causing propagation times to reach up to 90 minutes. To summarize:

*   **Why chose another DNS provider**: Unfortunately, many managed providers are slow, expensive, and hard to sell to.
*   **Addressing pricing constraints and billing models**: By using a per-record price model or no-price at all, we avoided this uncertainty.
*   **Why we used the hidden primary pattern instead of Direct Access**: This approach has proven surprisingly easy.

**Breaking Down Our DNS Server's Features**

Our implementation used:

*   Postgres as an event bus
*   AXFR and IXFR to fetch zone records from public secondaries.