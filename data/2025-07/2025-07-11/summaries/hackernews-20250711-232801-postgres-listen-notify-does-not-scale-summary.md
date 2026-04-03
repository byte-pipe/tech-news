---
title: Postgres LISTEN/NOTIFY does not scale
url: https://www.recall.ai/blog/postgres-listen-notify-does-not-scale
date: 2025-07-11
site: hackernews
model: llama3.2:1b
summarized_at: 2025-07-11T23:28:01.408113
---

# Postgres LISTEN/NOTIFY does not scale

**Analysis**

The article discusses a problem faced by the solo developer business, Recall.ai, where their Postgres database experiences stalling out due to insufficient scale. The issue is caused by an overly concurrent workload, resulting in excessive load and downtime.

**Market Indicators:**

* User adoption: There is no mention of user activity, but this could indicate a smaller market.
* Revenue mentions: Unfortunately, there are no revenue-related mentions to analyze.
* Growth metrics: No specific growth metrics mentioned.
* Customer pain points:
	+ The article highlights the problem of increased load and downtime due to insufficient scalability.

**Technical Feasibility:**

* Required skills: Postgres development skills would be required to tackle this issue. Elliot Leviin is a skilled developer, but the complexity of optimizing for concurrent writes suggests it may require knowledge in database optimization, concurrency control, and distributed systems.
* Time investment: This issue requires significant time investment, as optimized solutions like indexing, buffering, queuing, or data sharding might not have been considered initially. The article mentions extended investigation efforts, which implies the complexity of solving this problem.

**Business Viability Signals:**

* Willingness to pay:
	+ A specific price or revenue mention is missing.
* Existing competition:
	+ No mention of competitors or potential market entrants.
* Distribution channels:
	+ The article focuses on Postgres and its development, rather than external distribution channels.

**Actionable Insights for Building a Profitable Solo Developer Business:**

1. **Optimize database configuration:** Consider implementing indexing, buffering, queuing, or data sharding to optimize performance for Postgres.
2. **Consider concurrency control:** Elliot Leviin mentions investigating log lock waits (log_lock_waits) but notes this requires substantial effort.
3. **Invest in automation:** Develop scripts that can handle tasks like queuing events, freeing up human resources to focus on more complex tasks.
4. **Monitor and troubleshoot:** Implement a monitoring system to track database performance, potential bottlenecks, and troubleshoot issues quickly.

**Specific Numbers and Quotes:**

* "tens of thousands" number for meeting bots writing to the Postgres database
* 20841, Wait queue indicating concurrent writer activity on a specific Postgres connection.
