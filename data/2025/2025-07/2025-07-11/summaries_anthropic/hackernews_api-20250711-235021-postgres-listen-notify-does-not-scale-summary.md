---
title: Postgres LISTEN/NOTIFY does not scale
url: https://www.recall.ai/blog/postgres-listen-notify-does-not-scale
date: 2025-07-08
site: hackernews_api
model: anthropic/claude-3-haiku-20240307
summarized_at: 2025-07-11T23:50:21.094387
---

# Postgres LISTEN/NOTIFY does not scale

The article "Postgres LISTEN/NOTIFY does not scale" discusses a problem encountered by the team at Recall.ai, a company that records millions of hours of meetings every month and stores the structured data in a Postgres database.

Key points:

1. Problem/Opportunity:
   - The article discusses the problem of Postgres not scaling well with a high-concurrency, write-heavy workload, specifically when using the LISTEN/NOTIFY feature.
   - This is a common problem that businesses with large-scale data processing needs may face, and it represents an opportunity for a solo developer to provide a solution.

2. Market Indicators:
   - The article mentions that Recall.ai records millions of hours of meetings every month, indicating a significant market demand for their services.
   - However, the Postgres scaling issues they faced led to downtime, which likely impacted their business and customer satisfaction. This represents a pain point that customers would be willing to pay to solve.

3. Technical Feasibility for a Solo Developer:
   - The article provides a detailed technical analysis of the problem, including the root cause (LISTEN/NOTIFY acquiring a global lock during the commit phase) and the impact on the database (massive spikes in load, drop in throughput, and reduced CPU/I/O).
   - This level of technical complexity may be challenging for a solo developer, as it requires a deep understanding of Postgres internals and database scaling strategies.

4. Business Viability Signals:
   - The article does not mention any pricing or revenue information, but the fact that Recall.ai is running a large-scale, mission-critical service suggests that customers are willing to pay for reliable and scalable data processing solutions.
   - The article does not mention any direct competitors, indicating that there may be an opportunity for a solo developer to provide a specialized solution in this space.
   - The article suggests that the LISTEN/NOTIFY feature in Postgres may not be suitable for high-concurrency, write-heavy workloads, which could be an opportunity for a solo developer to create a more scalable alternative or provide guidance on best practices for such workloads.

In summary, the article highlights a common problem faced by businesses with large-scale data processing needs, which represents a potential opportunity for a solo developer. However, the technical complexity involved may require significant time and skill investment to develop a viable solution. Careful market research, understanding customer pain points, and identifying potential distribution channels would be crucial for a solo developer to build a profitable business in this space.
