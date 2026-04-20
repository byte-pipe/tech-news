---
title: Good CTE, bad CTE | boringSQL
url: https://boringsql.com/posts/good-cte-bad-cte/
date: 2026-03-30
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-04-01T01:33:29.957110
---

# Good CTE, bad CTE | boringSQL

# Good CTE, bad CTE | boringSQL

## Sample schema
- Defines three tables (`customers`, `orders`, `orders_archive`) and an `employees` hierarchy used for examples.
- Populates tables with synthetic data and runs `ANALYZE` to collect statistics.

## The optimization‑fence era (pre‑PG 12)
- Every CTE was **materialized**: result stored in a temporary tuplestore and scanned repeatedly.
- Materialization prevented predicate push‑down and index usage, turning CTEs into optimizer fences.
- Reasoned by snapshot isolation (single snapshot for all references) and safety for side‑effect statements.
- Common workaround: rewrite CTEs as subqueries to regain optimizer freedom.

## PostgreSQL 12: CTE inlining
- Introduced automatic inlining for **non‑recursive, side‑effect‑free, singly‑referenced** CTEs.
- Planner now treats such CTEs like subqueries: predicates are merged, indexes can be used, join reordering applies.
- Example query shows the CTE disappearing from the plan and both filters applied in a single scan.

## When does a CTE get materialized? (Cases)
| Case | Condition | Behaviour |
|------|-----------|-----------|
| 1 | Single reference, no side effects | **INLINED** |
| 2 | Multiple references | **MATERIALIZED** |
| 3 | Recursive CTE | **ALWAYS MATERIALIZED** |
| 4 | Data‑modifying CTE (`INSERT/UPDATE/DELETE`) | **ALWAYS MATERIALIZED** |
| 5 | Contains a `VOLATILE` function | **MATERIALIZED** |
| 6 | Contains only `STABLE` functions | **INLINED** |
| 7 | Explicit hints (`MATERIALIZED` / `NOT MATERIALIZED`) | Forces chosen behaviour |
| 8 | `FOR UPDATE` / `FOR SHARE` clauses | **MATERIALIZED** |

## Decision matrix
- Summarises the above cases, showing which combination of references, recursion, side effects, and volatility leads to inlining vs. materialization.

## The statistics black hole (PG 17)
- PostgreSQL 17 adds **statistics propagation** through inlined CTEs, allowing better row‑count estimates.
- Previously, materialized CTEs hid statistics from the outer query, causing sub‑optimal plans.

## When materialization helps
- Guarantees a single evaluation (useful for expensive functions or when a stable snapshot is required).
- Prevents repeated work when the CTE is referenced many times.

## When inlining isn’t enough
- Complex queries with volatile functions, recursion, or data‑modifying statements still need materialization.
- Inlining may produce plans that exceed `work_mem` or cause excessive spilling.

## Writable CTEs (the power and the traps)
- **Writable CTEs** execute DML and can be referenced later, but you cannot read rows that were just written within the same CTE.
- Leads to “tuple shuffling” issues where the planner may reorder operations incorrectly.

## UNION vs UNION ALL
- `UNION` forces a distinct sort, often materializing intermediate results.
- `UNION ALL` streams rows, avoiding unnecessary materialization.

## Exotic edge cases
- **Partition pruning loss**: materialized CTEs can hide partition keys, preventing pruning.
- **Prepared statements & plan caching**: CTE inlining decisions are made at plan time; changes in parameter values may not re‑trigger optimal re‑planning.
- **`work_mem` spilling**: large materialized CTEs can exceed memory limits, causing disk spill.
- **Security‑barrier views**: CTEs inside such views retain their barrier properties.

## CTE vs. subquery vs. temporary table
- **Subquery**: always inlined, full optimizer freedom.
- **CTE**: may be inlined or materialized depending on the cases above.
- **Temporary table**: materialized explicitly, useful for very large intermediate results or when you need to reference the data multiple times with stable snapshots.

## The PG 18 state of affairs
- Continues the trend of smarter inlining and better statistics handling.
- Provides more fine‑grained control via planner hints and improved handling of edge cases.
