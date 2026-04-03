---
title: OpenFreeMap survived 100,000 requests per second
url: https://blog.hyperknot.com/p/openfreemap-survived-100000-requests
date: 2025-08-09
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-08-09T23:11:15.138099
---

# OpenFreeMap survived 100,000 requests per second

**Analysis**

From a solo developer business perspective, this article discusses the survival of OpenFreeMap after 100,000 requests per second. The author shares experiences with the service's performance under heavy loads and reports some unusual traffic spikes.

**Market Indicators**

* User Adoption: 96% of requests were successful (200 OK), while only 3.6% were broken.
* Revenue: $150k/month, $300k/mo through MapTiler and Mapbox, with a projected growth rate of 50-100 times their current revenue.
* Growth Metrics: The number of users has increased exponentially over the past 10 months, with a large increase in traffic during that time.

**Technical Feasibility for Solo Developer**

* Complexity: Moderate to high due to the need to handle heavy loads and ensure seamless tile loading and caching.
* Required Skills: Proficiency in web development, Linux, Cloudflare configurations, and some experience with caching mechanisms like Btrfs.

**Business Viability Signals**

* Willingness to Pay: Users are willing to pay for a service that can deliver up to 100k requests per second. OpenFreeMap offers premium services at higher pricing tiers.
* Existing Competition: No existing major competitors in the map-based tile serving space, but there may be smaller players that could impact market share.

**Specific Insights and Recommendations**

* Identify and address the root cause of the missing files issue to reduce support tickets and further errors.
* Utilize Cloudflare's built-in rate limiting and IP rotation features to minimize traffic spikes.
* Monitor and optimize server performance on Hetzner servers to ensure stability under heavy loads.
* Consider investing in better image caching mechanisms, such as WebP or JPEG-XR, to improve loading times.
* Develop a strategy for handling potential support ticket volume increases due to Wplace.live's sudden interest.

Some additional suggestions:

* Document the service's performance and troubleshooting process to facilitate future growth and scaling.
* Explore alternative solutions that integrate with existing infrastructure, reducing the need for bespoke services like OpenFreeMap.
* Consider offering tiered pricing plans or a subscription-based model to adapt to increasing user demands while maintaining revenue stability.
