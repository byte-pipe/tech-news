---
title: We Made Postgres Writes Faster, but it Broke Replication
url: https://www.paradedb.com/blog/lsm_trees_in_postgres
date: 2025-07-22
site: hackernews
model: anthropic/claude-3-haiku-20240307
summarized_at: 2025-07-22T23:57:14.894084
---

# We Made Postgres Writes Faster, but it Broke Replication

This article discusses the challenges faced by the developers of the pg_search Postgres extension in making their writes faster while maintaining replication safety. Here's a 3-4 paragraph analysis from a solo developer business perspective:

Problem/Opportunity:
The article highlights a common problem faced by many Postgres-based applications - the need to balance write throughput and replication consistency. Many real-time use cases like dashboards, e-commerce search, and recommendation systems require high write volumes that can conflict with Postgres' default replication mechanisms. This presents an opportunity for a solo developer to build a solution that addresses this pain point for Postgres users.

Market Indicators:
The article mentions that pg_search was built as an "effective alternative to Elasticsearch" for Postgres users, indicating a clear market demand for high-performance search and analytics capabilities within the Postgres ecosystem. The developers also note that many Elasticsearch use cases require "continuous writes that must be indexed and made searchable immediately", suggesting a willingness from customers to pay for a solution that can deliver this functionality. While the article doesn't provide specific revenue or growth metrics, the fact that the developers invested significant effort into solving this problem points to a potentially lucrative market opportunity.

Technical Feasibility:
Implementing a replication-safe, write-optimized data structure like an LSM tree within Postgres is a complex technical challenge that requires deep knowledge of Postgres internals and replication mechanics. As the article demonstrates, simply using an LSM tree can break Postgres' physical replication, requiring the developers to implement custom solutions like atomic logging and leveraging the "hot_standby_feedback" setting. This level of technical sophistication may be beyond the capabilities of a solo developer, unless they have extensive experience with Postgres and distributed systems design.

Business Viability:
The article suggests that there is a clear customer pain point and willingness to pay for a solution that can deliver high write throughput while maintaining replication consistency. However, the technical complexity involved in building such a solution may make it challenging for a solo developer to compete with larger teams or established products like Elasticsearch. The developer would need to carefully assess their technical skills, the resources required to build and maintain the solution, and the potential for differentiation in a market that likely has some existing competition.

Overall, this article highlights an interesting problem that could be a viable business opportunity for a solo developer, but the technical challenges involved may make it a better fit for a more experienced team or a developer with a strong Postgres background.
