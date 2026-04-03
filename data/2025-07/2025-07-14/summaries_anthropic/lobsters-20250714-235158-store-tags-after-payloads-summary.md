---
title: Store tags after payloads
url: https://www.scattered-thoughts.net/writing/store-tags-after-payloads/
date: 2025-07-14
site: lobsters
model: anthropic/claude-3-haiku-20240307
summarized_at: 2025-07-14T23:51:58.252899
---

# Store tags after payloads

The article "Store tags after payloads" discusses an interesting optimization opportunity for data structures involving sum types or tagged unions. The key insights are:

Problem/Opportunity:
- Storing the tag (discriminator) for a sum type before the payload can lead to significant wasted space, especially when nesting sum types. This is due to alignment requirements for the payload data.
- By storing the tag after the payload, the overall size and memory usage can be reduced substantially.

Market Indicators:
- The author notes that this optimization technique is used in Swift, but not widely documented or discussed. This suggests it may be a "boring problem" that developers are unaware of, but could provide real value.
- No specific user adoption, revenue, or growth metrics are provided, but the potential for space savings in data-heavy applications (e.g. in-memory databases, caching systems) implies a meaningful market opportunity.
- The pain point is the wasted memory and potential performance impact of poor data structure layout, which businesses would likely pay to solve.

Technical Feasibility:
- For a solo developer, implementing this optimization would be relatively straightforward, requiring an understanding of memory layout, alignment, and sum type representation.
- The required skills include compiler internals, data structure design, and low-level programming. This is likely within the capabilities of an experienced solo developer.
- The time investment would depend on the complexity of the data structures involved, but the core concept seems relatively simple to apply.

Business Viability:
- Businesses would likely be willing to pay for solutions that reduce memory usage and improve performance, especially in performance-critical applications.
- There doesn't appear to be any direct competition for this specific optimization, as it's not widely known or documented.
- Distribution could be through open-source libraries, blog posts, or consulting services targeting developers building data-intensive applications.

In summary, the "Store tags after payloads" optimization presents an interesting opportunity for a solo developer to address a "boring problem" that businesses would likely pay to solve. The technical feasibility is within reach, and the potential market impact could be significant for applications that heavily utilize sum types or tagged unions. A solo developer could explore building open-source libraries, writing educational content, or offering consulting services around this optimization technique.
