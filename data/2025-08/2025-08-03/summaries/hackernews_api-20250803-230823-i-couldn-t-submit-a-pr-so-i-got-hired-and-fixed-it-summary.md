---
title: "I couldn't submit a PR, so I got hired and fixed it myself"
url: https://www.skeptrune.com/posts/doing-the-little-things/
date: 2025-08-02
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-08-03T23:08:23.045974
---

# I couldn't submit a PR, so I got hired and fixed it myself

**Problem/Solution Analysis:**

The article discusses a personal experience where the author was frustrated with searching on Mintlify (a software company powering search queries for their documentation sites). They were unable to submit a PR because they couldn't find a fixed solution, resulting in buggy search results. The irony is that Mintlify's own company didn't even fix the issue until Nicholas brought it up as a concern in a shared Slack thread.

The main problem that people/businesses pay for is often frustrating bugs or issues that cause them inconvenience or frustration (opportunity). In this case, having to use an outside service (Mintlify) before discovering and fixing the problem itself indicates high demand for efficient bug removal.

**Market Indicators:**

* User adoption: Mintlify's 30,000+ documentation sites indicate a large user base that needs reliable search functionality.
* Revenue mentions: There is no mention of revenue numbers in the article, but it is implied by the fact that users need to submit PRs or use external services before fixing the issue.

**Technical Feasibility for a Solo Developer (Complexity, Required Skills)**:

* Complexity:
	+ The issue required understanding of asynchronous programming and debouncing techniques.
	+ It involved modifying the existing codebase to introduce an AbortController, which requires knowledge of JavaScript and Node.js.
* Required skills:
	+ Proficiency in JavaScript and Node.js
	+ Experience with debugging and troubleshooting

**Business Viability Signals:**

* Willingness to pay:
	+ Mintlify's willingness to fix the issue through external services suggests that they are committed to providing a high-quality product, which may justify the cost of bug fixes or support.
* Existing competition:
	+ The fact that there is no mention of competing products or solutions raises questions about whether there is already a viable alternative or workaround for users in this space.
* Distribution channels:
	+ There is no mention of Mintlify's distribution channels, such as their website or social media presence. While an active online presence could be beneficial for attracting customers.

**Actionable Insights:**

1. **Develop expertise**: Nicholas Khami recognizes the importance of debugging and fixing bugs, just like in George Hotz's legendary single week at Twitter.
2. **Partner with companies with open-source roots**: By building closed systems (Mintlify), it may be easier for users to fix bugs without needing to rely on external services.
3. **Consider self-service or community-driven fix mechanisms**: If there are large user bases, offering self-service options or community-driven fixes could address the need for bug resolution and provide additional value for users.

**Specific numbers and quotes:**

* Over a year of frustration with search results caused by a race condition on Mintlify's search queries.
* "$ [insert amount]" (no mention of revenue number).
* Fixing an AbortController introduces "something deeply satisfying," indicating the importance of accurate debugging.
* Nicholas hopes to build 2-3 new features in less than their own company budget.
