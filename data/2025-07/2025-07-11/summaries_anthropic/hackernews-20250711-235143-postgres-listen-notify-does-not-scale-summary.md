---
title: Postgres LISTEN/NOTIFY does not scale
url: https://www.recall.ai/blog/postgres-listen-notify-does-not-scale
date: 2025-07-11
site: hackernews
model: anthropic/claude-3-haiku-20240307
summarized_at: 2025-07-11T23:51:43.537004
---

# Postgres LISTEN/NOTIFY does not scale

The article "Postgres LISTEN/NOTIFY does not scale" discusses a problem encountered by the Recall.ai team, a company that records millions of hours of meetings every month and stores the structured data in a Postgres database. The key insights from the article are:

1. **Problem/Opportunity**: The article highlights a scalability issue with the Postgres LISTEN/NOTIFY feature, which is used to trigger real-time updates for the meeting data. Under a high-concurrency, write-heavy workload, the LISTEN/NOTIFY feature can cause a global lock on the entire database during the commit phase, effectively serializing all commits and leading to significant performance issues and downtime.

2. **Market Indicators**: The article provides some insights into Recall.ai's business:
   - They record millions of hours of meetings every month, indicating a large user base and significant demand for their services.
   - They have a write-heavy workload, with tens of thousands of simultaneous writers (meeting bots) writing data to the Postgres database.
   - The performance issues and downtime experienced were significant enough to warrant an in-depth investigation and a solution.

3. **Technical Feasibility**: The article suggests that the LISTEN/NOTIFY issue is a complex problem that requires a deep understanding of Postgres internals and database performance optimization. While a solo developer could potentially investigate and implement a solution, it would likely require significant time and effort, as well as specialized knowledge in areas like database internals, concurrency control, and performance tuning.

4. **Business Viability**: The article does not provide any direct information about Recall.ai's pricing or revenue, but the fact that they are recording millions of hours of meetings and experiencing significant performance issues suggests that there is a willingness to pay for a reliable and scalable solution in this market. However, the technical complexity of the problem may make it challenging for a solo developer to build a viable business around it without significant expertise and resources.

In summary, the article highlights a "boring" but potentially lucrative problem that businesses like Recall.ai are willing to pay to solve. However, the technical complexity and the level of expertise required to address the LISTEN/NOTIFY scalability issue may make it a challenging proposition for a solo developer to tackle, at least without significant time and effort invested in learning the necessary skills.
