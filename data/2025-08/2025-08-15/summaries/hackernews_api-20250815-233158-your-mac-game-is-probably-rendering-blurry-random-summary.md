---
title: Your Mac Game Is Probably Rendering Blurry – Random Thoughts
url: https://www.colincornaby.me/2025/08/your-mac-game-is-probably-rendering-blurry/
date: 2025-08-14
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-08-15T23:31:58.884852
---

# Your Mac Game Is Probably Rendering Blurry – Random Thoughts

**Problem:**
The article discusses how Mac games may render blurry on notched displays, particularly with the iOS dev community using Apple's APIs without addressing this issue. The problem lies in the way screen resolution is handled for full-screen apps that use AppKit (or Catalyst).

**Market Indicators:**

* User adoption: Not addressed by most game developers using Apple's APIs.
* Revenue mentions: Not mentioned in the given article.
* Growth metrics: No specific market trends or user engagement data are provided to estimate potential revenue.

**Technical Feasibility for a Solo Developer:**
A solo developer building a Mac game with full-screen capabilities may face significant complexity:

* Requires knowledge of AppKit and Catalyst APIs.
* Needs to account for the notch on notched displays.

Time investment would be substantial, potentially in the tens or hundreds of hours.

**Business Viability Signals:**

* Willingness to pay: The article does not provide industry pricing.
* Existing competition: Mac games are popular, but there's no indication that solo developers currently dominate this market.

**Actionable Insights for Building a Profitable Solo Developer Business:**
To mitigate the issue on Mac games:

1. **Handle notch-specific resolution calculations**: Use separate resolution calculation functions (e.g., `CGDisplaySmallestScaleResolutionKey`, `NSScreenSafeAreaMetrics`) to account for the notch's layout.
2. **Optimize output regions**: Filter the list of resolutions based on the "under menu bar" category only, as this is where Apple wants games with full-screen capabilities to render correctly.
3. **Research and apply solution methods** (e.g., using `CGDisplaySmallestScaleResolutionKey`, adding a texture or color mask specific to the notch region).

Consider implementing a patch mechanism in your codebase for future updates to better handle notch-specific display resolution calculations.

As for pricing, more research is needed on what industry games are paying for similar services. However, considering a solution with noticeable performance benefits could justify higher prices (up to 20-50% of the target price) – especially if many customers value their experience and willingness to pay premium game developers willing to solve this problem.

Note: The article mentions no Apple-approved or recommended solutions, so implementing these patch methods comes at an additional cost; you might consider sharing your solution on platforms like App Store Connect or GameKit APIs, as the costs of creating an optimized executable are likely lower for customers with an existing relationship with a game.
