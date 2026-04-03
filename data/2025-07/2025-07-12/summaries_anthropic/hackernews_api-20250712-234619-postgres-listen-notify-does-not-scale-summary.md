---
title: Postgres LISTEN/NOTIFY does not scale
url: https://www.recall.ai/blog/postgres-listen-notify-does-not-scale
date: 2025-07-08
site: hackernews_api
model: anthropic/claude-3-haiku-20240307
summarized_at: 2025-07-12T23:46:19.806159
---

# Postgres LISTEN/NOTIFY does not scale

The article "Postgres LISTEN/NOTIFY does not scale" discusses a problem encountered by the team at Recall.ai, a company that records millions of hours of meetings every month and stores the structured data in a Postgres database.

Key points:

1. Problem or Opportunity:
   - The article discusses a performance issue with the Postgres LISTEN/NOTIFY feature, which is used to notify running processes about changes in the database.
   - The problem arises when a NOTIFY query is issued during a transaction, as it acquires a global lock on the entire database during the commit phase, effectively serializing all commits.
   - This issue becomes particularly problematic for Recall.ai, which has a write-heavy workload with tens of thousands of concurrent writers (meeting bots) updating the database.

2. Market Indicators:
   - The article does not provide explicit revenue or growth metrics, but it does mention that Recall.ai records "millions of hours of meetings every month", indicating a significant user base and potential market opportunity.
   - The pain point of the LISTEN/NOTIFY performance issue is clearly articulated, as it leads to "massive spikes in database load, drops in throughput, and periods of downtime" for Recall.ai.

3. Technical Feasibility for a Solo Developer:
   - The issue described in the article is quite complex, involving an in-depth understanding of Postgres internals and concurrency control mechanisms.
   - Resolving this problem would likely require significant time and effort, as well as a strong background in database systems and performance optimization.
   - For a solo developer, this may be a challenging problem to tackle, as it may require extensive research, testing, and potentially even contributions to the Postgres project itself.

4. Business Viability Signals:
   - The article does not mention pricing or revenue, but the problem being solved is clearly a pain point for businesses that rely on Postgres for write-heavy workloads.
   - There may be an opportunity for a solo developer to create a solution or tool that addresses this issue, potentially by building on top of Postgres or creating a complementary service.
   - However, the competition in the Postgres ecosystem and the technical complexity of the problem may make it challenging for a solo developer to build a viable business around this specific issue.

In summary, the article highlights a significant performance problem in Postgres that affects businesses with write-heavy workloads, such as Recall.ai. While this represents a potential opportunity, the technical complexity and the need for deep Postgres expertise may make it a challenging problem for a solo developer to tackle. Careful consideration of the market, competition, and one's own technical capabilities would be necessary to assess the business viability of a solution in this domain.
