---
title: Making Postgres 42,000x slower because I am unemployed
url: https://byteofdev.com/posts/making-postgres-slow/
date: 2025-07-29
site: hackernews
model: llama3.2:1b
summarized_at: 2025-07-29T23:38:04.431420
---

# Making Postgres 42,000x slower because I am unemployed

Here's a 4-paragraph analysis:

**Problem or Opportunity**: The author is discussing a common problem faced by developers who need to optimize performance in PostgreSQL: making the database too slow. They acknowledge that most companies focus on speeding up the database, but from their perspective, don't actually understand how to make it slower. This is a classic example of a bored problem that people pay professionals to solve.

**Market Indicators**: The author mentions several market indicators to support their argument, including:
* TPC-C with 128 warehouses: A widely used benchmark for measuring database performance.
* Baseline test results: Postgres achieves 7082 TFPS (thousand pages per second) with basic tweaks.
* Increased effort required: The author admits that making Postgres slow is a challenging and time-consuming task, even for experienced developers.

**Technical Feasibility**: Given the author's experience as an unemployed solo developer, it's clear that optimizing PostgreSQL requires significant technical expertise. The author mentions that they can only set the `shared_buffers` knob to 8MB in their baseline test, which is a very tight configuration. They acknowledge that Postgres also uses shared memory for various aspects of database operation, making it even more challenging to optimize.

**Business Viability Signals**: While the author doesn't mention pricing or revenue directly, their focus on optimizing a specific problem (making PostgreSQL slower) suggests that they are willing to invest significant time and effort into solving this challenge. However, if the solution requires additional resources (e.g., expertise, hardware), it may be more viable for companies to hire professionals rather than solo developers to solve similar problems.
