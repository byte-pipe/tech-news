---
title: 'Building a Database Performance Testing Tool With AI: The Honest Breakdown - DEV Community'
url: https://dev.to/m4rri4nne/building-a-database-performance-testing-tool-with-ai-the-honest-breakdown-3c0c
site_name: devto
content_file: devto-building-a-database-performance-testing-tool-with
fetched_at: '2026-05-28T12:11:38.369965'
original_url: https://dev.to/m4rri4nne/building-a-database-performance-testing-tool-with-ai-the-honest-breakdown-3c0c
author: Alicia Marianne Gonçalves
date: '2026-05-21'
description: It still feels a little strange to have AI writing practically all the code — but I decided to give... Tagged with ai, testing, database, performance.
tags: '#ai, #testing, #database, #performance'
---

Explores N+1 and schema regressions

It still feels a little strange to have AI writing practically all the code — but I decided to give it a real shot on this new project. A bit of context: I was running low on project ideas to share here, so I asked the AI for a list and picked one calledDatabase Performance Testing. The goal was to run performance tests against a relational database. I built it in roughly two days, and in this article I want to share my honest impressions — both technical and about the AI-assisted workflow itself.

## Why run performance tests on a database?

I think this is the first question we need to ask before starting any project. As it happens, I'm currently on a project where data performance is a critical system concern — which got me thinking:what would it look like to run performance tests directly against a relational database?

From a QA perspective, performance isn't just about how the API connects to the database. It's also abouthow queries are writtenandhow the chosen database handles query concurrency, especially in synchronous systems. A slow endpoint isn't always a slow endpoint — sometimes it's a slow query hiding behind it. That's what drove me to start here.

## What are we testing?

For this project, we have four distinct test scenarios:

* N+1 Query Detection
* Deadlock Simulation
* Query Regression Tracking Across Schema Changes
* Slow Queries

### N+1 Query Detection

N+1 is a classic performance problem in applications that access databases — especially systems using ORMs like Entity Framework, SQLAlchemy, or Sequelize. The name describes exactly what happens: instead of one optimized query, the application ends up running1 initial query + N additional queries.

Consider an e-commerce system that lists 20 orders and shows the email of each order's user. A naive approach would be:

SELECT
 
id
,
 
user_id
 
FROM
 
orders
 
LIMIT
 
:
n
;

SELECT
 
email
 
FROM
 
users
 
WHERE
 
id
 
=
 
:
uid
;

Enter fullscreen mode

Exit fullscreen mode

The first query fetches the orders. The second query then runs20 times— once per order. That's your N+1. The consequences at scale include multiplied latency, cache pollution, and unpredictable response times for users.

This can also appear in concurrent scenarios. Two threads both fetching user data simultaneously, each triggering their own cascade of lookups, can quickly multiply database load in ways that are hard to trace without instrumentation.

### Deadlock Simulation

Imagine two transactions happening concurrently:

Transaction A:

UPDATE
 
orders
 
SET
 
status
 
=
 
'pending'
 
WHERE
 
id
 
=
 
1
;

UPDATE
 
orders
 
SET
 
status
 
=
 
'paid'
 
WHERE
 
id
 
=
 
2
;

Enter fullscreen mode

Exit fullscreen mode

Transaction B (running simultaneously, in reverse order):

UPDATE
 
orders
 
SET
 
status
 
=
 
'paid'
 
WHERE
 
id
 
=
 
2
;

UPDATE
 
orders
 
SET
 
status
 
=
 
'pending'
 
WHERE
 
id
 
=
 
1
;

Enter fullscreen mode

Exit fullscreen mode

Each transaction holds a lock the other needs. The database detects the cycle and resolves it by rolling back one of the transactions — but that rollback has a cost. At scale, this kind of contention can cause noticeable latency spikes and, in the worst case, lock up parts of your application. The goal of the deadlock test isn't just to confirm that a deadlockcan*happen, but to measure *how the database recoversand what the timing impact looks like.

### Query Regression Tracking Across Schema Changes

This scenario focuses on measuring theimpact of schema changes— index creation, migrations, table alterations — on query execution plans and timings. It captures EXPLAIN ANALYZE output before and after a migration, then diffs the results.

This is especially useful for:

* Validating that an optimization actually improved things before merging
* Documenting schema versions and their performance characteristics over time
* Supporting production investigations when run periodically as a baseline

### Slow Queries

The slow query tests act as alatency gate— a set of critical queries that must stay under a defined threshold (configured inconfig.pyasSLOW_QUERY_THRESHOLD_MS). If any of these queries breach the threshold in CI, the pipeline fails.

Think of it as a performance budget for your most important database operations. In this project, five critical queries were monitored. Here are the results from a low-volume benchmark run:

Query

Avg (ms)

p95 (ms)

Max (ms)

user_lookup

0.20

0.29

0.35

order_history

0.31

0.43

0.75

inventory_search

0.24

0.32

0.62

All three passed the threshold comfortably. But the value here isn't just the green light — it's having ahistorical baseline. The next time someone adds a filter, changes a join, or drops an index, you'll know immediately if these numbers move.

## The solution structure

Here's how the project is organized:

.
├── config.py # DB_URL and SLOW_QUERY_THRESHOLD_MS
├── conftest.py # pytest fixtures: engine, instrumented_engine
├── pyproject.toml # pytest config and markers
├── requirements.txt
├── analysis/
│ ├── n_plus_one_detector.py # N+1 detection and simulation
│ ├── deadlock_simulator.py # Concurrent deadlock demo
│ └── explain_analyzer.py # EXPLAIN plan capture and diff
├── benchmarks/
│ ├── queries/ # Raw .sql files (12 queries)
│ ├── scenarios/
│ │ └── run_benchmark.py # Volume benchmark runner
│ ├── test_n_plus_one.py # N+1 detection tests
│ ├── test_deadlock.py # Deadlock tests
│ ├── test_explain.py # EXPLAIN ANALYZE plan tests
│ └── test_slow_queries.py # Latency threshold gate (5 critical queries)
├── data/
│ ├── seed.py
│ └── distributions.json
├── migrations/
│ ├── baseline/
│ │ └── 001_initial_schema.sql
│ └── v2_add_indexes/
│ └── 002_add_indexes.sql # Sample migration for regression demo
├── reports/
│ ├── query_regression_report.py # Delta reporter (also exports to Grafana)
│ ├── export_metrics.py # Writes results to benchmark_results table
│ ├── output/ # Timestamped benchmark JSON results
│ └── plans/ # Saved EXPLAIN plans
├── scripts/
│ └── setup_schema.py # Apply migration + snapshot schema
├── .github/
│ └── workflows/
│ └── performance-tests.yml # CI: schema → seed → pytest
└── docker/
 ├── docker-compose.yml # PostgreSQL + Grafana
 ├── init.sql
 └── grafana/
 ├── provisioning/
 └── dashboards/benchmark.json # Auto-provisioned dashboard

Enter fullscreen mode

Exit fullscreen mode

A few things worth highlighting in this structure:

analysis/is designed to be run independently.Each module — N+1 detection, deadlock simulation, EXPLAIN analysis — can be executed on its own. You don't have to run the full suite every time. This matters in practice: there are moments where you only care about regression tracking after a migration, and running deadlock simulation alongside it is just noise.

explain_analyzer.pycaptures and diffs EXPLAIN plans.This is what powers the query regression scenario — it saves plan snapshots before and after a schema change and computes the delta. The results are stored underreports/plans/as timestamped JSON files.

Grafana is provisioned automatically.Thebenchmark_resultstable gets populated byexport_metrics.pyafter each run, and the dashboard ingrafana/dashboards/benchmark.jsonis auto-loaded. No manual setup needed.

## What the data actually showed

The most interesting results came from thequery regression scenario. After adding a composite index (idx_orders_user_created) via migration002_add_indexes.sql, the EXPLAIN plans fororder_historychanged dramatically:

Before the index — Sequential Scan:

* Execution time:0.532ms
* The planner scanned the entireorderstable (touching 39 blocks) and filtered out2,497 rowsto find 3 matching records
* Total cost estimate:101.27

After the index — Bitmap Index Scan:

* Execution time:0.090ms
* The planner usedidx_orders_user_createddirectly, reading only 5 blocks
* Total cost estimate:10.92

That's an83% reduction in execution timeand a~10x drop in planner cost— from a full table scan touching 2,500 rows down to a targeted index lookup. Without the regression tracking in place, this kind of change would have been invisible unless someone happened to run EXPLAIN manually.

This is exactly the kind of validation that's worth having in CI: you add an index, run the suite, and get a clear before/after diff that confirms the optimization actually worked.

## On building with AI: the honest take

This is where I want to spend some real time, because the AI-assisted workflow was just as interesting to reflect on as the technical output itself.

What I actually didwas prompt the AI for a project idea, refine the scope, and then iteratively ask it to generate the solution — structure first, then individual modules, then the CI pipeline. I didn't write much code from scratch. What Ididwas spend a significant amount of time reading what it produced, questioning whether the test logic made sense, and validating that the scenarios matched the real-world problems they were meant to simulate.

What felt differentabout this workflow compared to writing everything myself:

* I spent more time thinking aboutwhetherthe tests were correct than abouthowto implement them. That's actually a good shift for a QA-focused project — but it felt unfamiliar.
* The AI was excellent at boilerplate and structure (docker-compose setup, pytest fixtures, file organization) and decent at logic, but it needed guidance on edge cases and test validity.
* I felt genuinely uncertain about "ownership" of the result. The code works, I understand it, and I made real decisions throughout — but I also couldn't have shipped it in two days without the AI. That's a strange feeling to sit with.

Where it genuinely helped:spinning up the Docker + Grafana integration was something I would have spent half a day on manually. The AI had a workingdocker-compose.ymlwith auto-provisioned dashboards in minutes. That alone was worth it for a POC.

Where it fell short:the AI tends to produce confident-looking code that needs careful review. A few of the generated SQL files had column names that didn't match the schema. The N+1 detection logic needed an extra pass to handle the concurrent case correctly. None of these were blockers, but they reinforced that the human-in-the-loop isn't optional — it's the job.

I'll keep experimenting with AI-assisted workflows, particularly for testing tooling and POCs. If you've built something similar or have thoughts on the approach, I'd love to hear it in the comments.You can check the full solutionhere.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse