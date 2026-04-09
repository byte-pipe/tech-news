---
title: Postgres LISTEN/NOTIFY does not scale
url: https://www.recall.ai/blog/postgres-listen-notify-does-not-scale
date: 2025-07-08
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-07-11T23:16:50.828313
---

# Postgres LISTEN/NOTIFY does not scale

Analysis:

**Problem or Opportunity:**
The Postgres LISTEN/NOTIFY feature does not scale well for a business like NewRecall.ai, which receives millions of hours of meetings every month. The bottleneck is likely due to the immense load and downtime caused by repeated NOTIFY queries acquiring global locks on the entire database during transaction commits.

**Market Indicators:**

* User adoption: The business runs an unusual workload with millions of hours of data being produced and analyzed.
* Revenue mentions: None mentioned.
* Growth metrics: Not provided, but implies increased demand for scalable database solutions.
* Customer pain points: Stalled-out Postgres with extremely concurrent, write-heavy workload resulting in major downtime.

**Technical Feasibility for a Solo Developer (Complexity, Required Skills, Time Investment):**

* Complexity: The issue requires understanding of Postgres performance bottlenecks and query optimization techniques, which may require some expertise.
* Required skills: SQL, database configuration management, and troubleshooting experience.
* Time investment: Several months to develop and implement a solution.

**Business Viability Signals (Willingness to Pay, Existing Competition, Distribution Channels):**

* Willingness to pay: Investors or customers willing to pay for scalable, high-performance database solutions may be interested in NewRecall.ai's needs.
* Existing competition: Other database-as-a-service providers with similar requirements may already be offering scaled out-of-the-box solutions.

Specific insights:

* The log lines from the investigation suggest that NOTIFY queries are causing significant lock contention, which is likely affecting performance even when the writers are stopped temporarily.
* The increase in load during these downtime periods indicates that the existing solution is not scalable enough to handle concurrent writers and updates.
* The business decision to implement a more efficient solution, such as a distributed database or better performance optimization techniques, will be crucial for its scalability.

Actionable insights:

* For NewRecall.ai to improve scalability, it needs to prioritize performance optimization and design solutions that meet the specific requirements of the business.
* A thorough investigation into Postgres configuration, query optimization, and locking mechanisms is essential to find a scalable solution.
* Developing or leveraging existing third-party libraries or open-source solutions that can help optimize database performance may be an efficient way to address the bottleneck.
