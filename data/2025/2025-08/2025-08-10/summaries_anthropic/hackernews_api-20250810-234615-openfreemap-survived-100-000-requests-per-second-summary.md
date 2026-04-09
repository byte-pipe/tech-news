---
title: OpenFreeMap survived 100,000 requests per second
url: https://blog.hyperknot.com/p/openfreemap-survived-100000-requests
date: 2025-08-09
site: hackernews_api
model: anthropic/claude-3-haiku-20240307
summarized_at: 2025-08-10T23:46:15.490821
---

# OpenFreeMap survived 100,000 requests per second

This article discusses an interesting problem and opportunity for a solo developer running the OpenFreeMap service. Here's a 3-4 paragraph analysis from a solo developer business perspective:

The problem being discussed is the sudden and massive spike in traffic to the OpenFreeMap service, reaching over 100,000 requests per second. This was caused by the unexpected launch of a new collaborative drawing website, Wplace.live, which was built using OpenFreeMap and quickly gained 2 million users. The traffic surge, estimated at 3 billion requests in 24 hours, would have cost over $6 million per month on commercial map services like MapTiler or Mapbox.

This represents a significant market opportunity for the solo developer running OpenFreeMap. The service was able to mostly handle the extreme traffic load, with a 99.4% CDN cache rate and 1,000 requests per second served by the developer's own servers. This demonstrates the technical feasibility and robustness of the OpenFreeMap architecture, which the developer has carefully built and optimized. As a solo developer, the ability to handle such high traffic without major issues is an impressive feat.

The business viability signals are also positive. The developer was able to quickly reach out to Cloudflare and get sponsorship for the bandwidth, showing the willingness of companies to support a valuable open-source mapping service. The developer also offered to help the Wplace.live team set up a self-hosted OpenFreeMap instance, indicating potential for revenue through consulting or licensing the technology. Overall, the traffic surge highlights the strong demand and usefulness of OpenFreeMap, which the solo developer can leverage to grow the project and potentially turn it into a profitable business, either through sponsorships, consulting, or a commercial offering.
