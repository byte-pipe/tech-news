---
title: "How I found a bypass in Google's big anti-adblock update"
url: https://0x44.xyz/blog/web-request-blocking/
date: 2025-07-13
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-07-15T23:13:57.684157
---

# How I found a bypass in Google's big anti-adblock update

**Analysis**

The article from Erin Eryilmaz discusses a bug in how Google's Chrome extension is handling web requests, specifically related to adblockers. The author found this issue due to its presence in future versions of MV3, which replaced MV2.

In essence, the problem lies in how Google injects JavaScript into pages using Chrome APIs, such as `chrome.runtime`. This injection allows an extension (in this case, an adblocker) to run privileged JavaScript on a user's website without proper permissions.

**Market Indicators**

* User adoption: None mentioned.
* Revenue mentions: Ads revenue is likely impacted, but not discussed in detail.
* Growth metrics: No specific growth metrics are provided.
* Customer pain points:
	+ Users with adblockers who want to use their extensions or websites will be affected by the change in webRequestBlocking permissions.

**Technical Feasibility for a Solo Developer**

* Complexity: Moderate (involves JavaScript, C++, and Chrome-specific APIs).
* Required skills: Proficiency in JavaScript, C++, and knowledge of extension development.
* Time investment: Several weeks to months to understand the issue, design fixes, and implement them in the codebase.

**Business Viability Signals**

* Willingness to pay:
	+ Adblockers may be willing to pay for a bypass or find alternative solutions.
	+ Eryilmaz mentions that Google has moved most API bindings to pure C++ but still uses JavaScript binding files from 2016, which is a good sign that they're willing to invest in their APIs and user experience.
* Existing competition:
	+ Adblockers are already dealing with extensions blocking ads without proper permissions. This niche market might provide an opportunity for Eryilmaz's bypass solution.
* Distribution channels:
	+ Google Chrome, extension repositories (e.g., Chrome Web Store), and adblocker communities will likely be impacted by this change.

**Actionable Insights**

1. **Identify a specific pain point**: Before investing time in fixing the bug, define what exactly is wrong with the issue and who might benefit from a solution.
2. **Assess market demand**: Research potential customers (adblockers) and gauge their willingness to pay or use alternative solutions.
3. **Develop and test custom solutions**: Create a test version of your bypass solution using Eryilmaz's codebase as a starting point, focusing on pure C++ implementation for security reasons.
4. **Evaluate Google's investment in JavaScript binding files**: If you can create a reliable, secure solution that fixes the current issue without relying on proprietary file formats, it might be a viable alternative.
5. **Communicate with adblockers and users**: Share your findings and solution with relevant communities to gauge interest and feedback.

By considering these factors, Erin Eryilmaz can evaluate the potential of her bypass solution and build a profitable solo developer business focusing on this niche market.
