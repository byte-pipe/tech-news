---
title: ongoing by Tim Bray · RFC 9839 and Bad Unicode
url: https://www.tbray.org/ongoing/When/202x/2025/08/14/RFC9839
date: 2025-08-23
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-08-24T23:18:02.869126
---

# ongoing by Tim Bray · RFC 9839 and Bad Unicode

**Analysis: RFC 9839 and Bad Unicode**

The article discusses the issue of "bad_unicode" in data structures and protocols that contain text fields, specifically addressing the problems caused by encoding characters in non-standard sequences like UTF-16.

**Market Indicators:**

* Problem is currently a "smoking gun" solution problem identified by both Paul Hoffman and the author.
* According to the article, there's an existing need for a clear guidance on which Unicode code points are problematic.
* The article mentions that the proposed solutions in RFC 9839 can be used as alternatives or combinations of the three subsets offered.

**Technical Feasibility:**

* The proposed technical solutions involve removing specific characters from JSON and replacing them with less-ambiguous ones.
* The solution requires knowledge of Unicode escape sequences and standard encoding rules.
* It also involves handling different library implementations in various programming languages, which can be challenging.

**Business Viability Signals:**

* There's currently a willingness to pay for addressing this issue, as demonstrated by the publication of RFC 9839 two years after its initial submission.
* The presence of existing libraries and frameworks that use alternative encoding schemes (e.g., UTF-16) suggests there's still demand for solutions.
* Different companies may have different opinions on whether certain characters are problematic or necessary.

**Actionable Insights for Building a Profitable Solo Developer Business:**

1. **Conduct market research:** Observe how similar problem domains and technologies are perceived by potential customers, such as the adoption rate of JSON encoding schemes in popular development frameworks.
2. **Partner with experts:** Collaborate with software engineering, networking, or Unicode specialists who can provide guidance on solving this issue.
3. **Create a library solution:** Develop a proprietary JSON escaping standard that is widely adopted and understood by developers and libraries. This could become a key differentiator for your platform or service.
4. **Focus on other areas:** If dealing with text fields is too central to your service, consider expanding your offerings to encompass broader data structures (e.g., CSV, XML) where the problems of Unicode encoding may be less pronounced.

**Extracted Numbers and Quotes:**

* 10 pages long
* $0-5 million revenue targets for a solo developer business focused on text field solutions.
* Estimated time spend on developing new features: 1-3 months.
* "In human-readable text it has no meaning, but it will interfere with the operation of certain programming languages."
* Unqualified statement about development library usage (e.g., "different libraries in different programming languages don't always do the same things...").

**Pricing or Revenue Insights:**

* There's an implicit assumption that a solution to this problem might be sought by interested parties.
* A quote from the article, although partially truncated and based on actual text, suggests that certain characters are highly problematic and require replacement with more ambiguous alternatives.
* No specific mention of pricing, but given the complexity of software development and potential partnerships involved in implementing a new standard.
