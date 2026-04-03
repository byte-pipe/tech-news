---
title: We Made Postgres Writes Faster, but it Broke Replication
url: https://www.paradedb.com/blog/lsm_trees_in_postgres
date: 2025-07-22
site: hackernews
model: llama3.2:1b
summarized_at: 2025-07-22T23:37:40.302998
---

# We Made Postgres Writes Faster, but it Broke Replication

**Analysis Overview**

The article discusses an issue with Postgres' LSM (Log-Structured Merge) tree, which caused it to break physical replication in the solo developer business. To resolve this, the authors developed a custom solution that leverages hot standby feedback. This analysis focuses on identifying market indicators, technical feasibility, business viability signals, and actionable insights for building a profitable solo developer business.

**Market Indicators**

* The issue is a common problem in search and analytics applications, where high write-throughput is critical.
* Postgres is an established solution with a large user base, but it may have limitations when handling complex data structures like LSM trees.

**Technical Feasibility**

* Developing a custom solution for PostgreSQL requires proficiency in the underlying technology as well as knowledge of replication mechanisms and data architecture.
* The authors acknowledge that their approach involved custom modifications to Postgres' existing implementation, which can be challenging but potentially rewarding.

**Business Viability Signals**

* User adoption: Although not mentioned explicitly, if Postgres has seen a surge in growth, it could indicate an opportunity for development and sales.
* Revenue mentions: No specific revenue figures are provided, but the authors suggest that resolving this issue could lead to increased business stability and revenue potential.
* Customer pain points: The problem of replication can be frustrating for users involved with complex data structures. Solving this issue may help alleviate these pain points and drive customer satisfaction.

**Specific Insights**

* Hot standby feedback is a powerful tool that allows database systems like Postgres to maintain consistency even in the presence of failures or concurrent writes.
* Atomic logging was necessary because traditional logical replication is not replica-safe for complex data structures like LSM trees. Developing custom solutions requires a deep understanding of replication mechanisms and database internals.

**Actionable Insights**

1. **Focus on Replication Challenges**: Companies targeting search and analytics applications should prioritize addressing replication issues, as they are common pain points for users.
2. **Develop Custom Solutions**: Engineers who specialize in PostgreSQL or similar databases may have opportunities to develop custom solutions that address the authors' LSM tree issue.
3. **Prioritize Market Research**: Identify market trends, customer preferences, and growth indicators to inform development decisions and business planning.

**Key Takeaways**

* Postgres' physical replication mechanism can be challenged by complex data structures like LSM trees.
* Developing a custom solution requires a deep understanding of database internals and replication mechanisms.
* Companies in the search and analytics space should prioritize replication challenges as they are common issues for users.
* By identifying market indicators, technical feasibility assessments, and business viability signals, companies can inform development decisions and drive growth.
