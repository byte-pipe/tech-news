---
title: Good CTE, bad CTE | boringSQL
url: https://boringsql.com/posts/good-cte-bad-cte/
site_name: hnrss
content_file: hnrss-good-cte-bad-cte-boringsql
fetched_at: '2026-04-01T01:32:10.539135'
original_url: https://boringsql.com/posts/good-cte-bad-cte/
author: Radim Marek
date: '2026-03-30'
description: The planner treats CTEs very differently depending on how you write them. Here's what happens under the hood, version by version, through PostgreSQL 18.
tags:
- hackernews
- hnrss
---

Table of Contents

* Sample schema
* The optimization fence era (pre-PG 12)
* PostgreSQL 12: CTE inlining
* When does a CTE get materialized?Case 1: single reference, no side effects (INLINED)Case 2: multiple references (MATERIALIZED)Case 3: recursive CTE (ALWAYS MATERIALIZED)Case 4: data-modifying CTE (ALWAYS MATERIALIZED)Case 5: VOLATILE function (MATERIALIZED)Case 6: STABLE functions (INLINED)Case 7: forcing behaviour with hintsCase 8: FOR UPDATE / FOR SHARE (MATERIALIZED)Decision matrix
* Case 1: single reference, no side effects (INLINED)
* Case 2: multiple references (MATERIALIZED)
* Case 3: recursive CTE (ALWAYS MATERIALIZED)
* Case 4: data-modifying CTE (ALWAYS MATERIALIZED)
* Case 5: VOLATILE function (MATERIALIZED)
* Case 6: STABLE functions (INLINED)
* Case 7: forcing behaviour with hints
* Case 8: FOR UPDATE / FOR SHARE (MATERIALIZED)
* Decision matrix
* The statistics black holePG 17: Statistics propagation
* PG 17: Statistics propagation
* When materialization helps
* When inlining isn't enough
* Writable CTEs (the power and the traps)You cannot read what you just wroteTuple shuffling
* You cannot read what you just wrote
* Tuple shuffling
* Recursive CTEs are always materializedUNION vs UNION ALL
* UNION vs UNION ALL
* The exotic edge casesPartition pruning lostPrepared statements and plan cachingwork_mem spillingCTE and security barrier views
* Partition pruning lost
* Prepared statements and plan caching
* work_mem spilling
* CTE and security barrier views
* CTE vs. subquery vs. temporary table
* The PG 18 state of affairs

TheCommon Table Expression, or CTE, is often the first feature developers reach for beyond basic SQL, and often the only one. You write a subquery afterWITH, give it a name, and use it in the rest of your query. It only exists for the duration of that query.

But the popularity of CTEs usually has less to do with modernizing code and more to do with the promise of imperative logic. For many, CTE acts as an easy to understand remedy for 'scary queries' and way how to force execution order on the database. The way how many write queries is as if they tell optimizer "first do this, then do that".

This creates a problem. CTEs handle query decomposition, recursion and multi statement DDLs. Planner treats them differently depending how you write and use them though. For long time (prior PostgreSQL 12) CTEs acted as optimization fence. The planner couldn't push predicates into them, couldn't use indexes on the underlying tables. Couldn't do anything that materialize them and scan through the result.

PostgreSQL 12 changed this. CTEs now get inlined, materialized, or something in between, depending on how you write them.

## Sample schema

We will use the same schema as in the articlePostgreSQL Statistics: Why queries run slow.

CREATE TABLE
 customers
 (

 id 
integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY
,

 name text NOT NULL

);

CREATE TABLE
 orders
 (

 id 
integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY
,

 customer_id 
integer NOT NULL REFERENCES
 customers(id),

 amount 
numeric
(
10
,
2
)
 NOT NULL
,

 status text NOT NULL DEFAULT
 'pending'
,

 note 
text
,

 created_at 
date NOT NULL DEFAULT
 CURRENT_DATE

);

CREATE TABLE
 orders_archive
 (
LIKE
 orders INCLUDING ALL EXCLUDING 
IDENTITY
);

INSERT INTO
 customers (
name
)

SELECT
 'Customer '
 ||
 i

FROM
 generate_series
(
1
, 
2000
) 
AS
 i;

INSERT INTO
 orders (customer_id, amount, 
status
, note, created_at)

SELECT

 (random()
 *
 1999
 +
 1
)::
int
,

 (random()
 *
 500
 +
 5
)::
numeric
(
10
,
2
),

 (
ARRAY
['pending','shipped','delivered','cancelled'])[floor(random()*4+1)::int],

 CASE WHEN
 random()
 <
 0
.
3
 THEN
 'Some note text here for padding'
 ELSE NULL END
,

 '2022-01-01'
::
date +
 (random()
 *
 1095
)::
int

FROM
 generate_series
(
1
, 
100000
);

ANALYZE customers;

ANALYZE orders;

For recursive examples later on we'll also need anemployeestable with a self-referencing hierarchy:

CREATE TABLE
 employees
 (

 id 
integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY
,

 name text NOT NULL
,

 manager_id 
integer REFERENCES
 employees(id),

 department 
text NOT NULL

);

INSERT INTO
 employees (
name
, manager_id, department) 
VALUES

 (
'Alice'
, 
NULL
, 
'Engineering'
),

 (
'Bob'
, 
1
, 
'Engineering'
),

 (
'Charlie'
, 
1
, 
'Engineering'
),

 (
'Diana'
, 
2
, 
'Engineering'
),

 (
'Eve'
, 
2
, 
'Engineering'
),

 (
'Frank'
, 
3
, 
'Sales'
),

 (
'Grace'
, 
3
, 
'Sales'
),

 (
'Hank'
, 
6
, 
'Sales'
),

 (
'Ivy'
, 
6
, 
'Sales'
);

ANALYZE employees;

## The optimization fence era (pre-PG 12)

As we already covered before PostgreSQL 12, every CTE was materialized. No exceptions. The planner would compute the CTE result set in full, store it in a temporary tuplestore, and then scan that tuplestore whenever the main query referenced the CTE. This made CTEs anoptimization fencebecause the planner could not look through them.

Consider this simple query:

EXPLAIN 
WITH
 filtered 
AS
 (

 SELECT * FROM
 orders 
WHERE
 created_at 
>
 '2025-01-01'

)

SELECT * FROM
 filtered 
WHERE status =
 'pending'
;

On PostgreSQL 11 and earlier, theEXPLAINoutput would look something like this:

 QUERY PLAN

-------------------------------------------------------------------

 CTE Scan on filtered (cost=1840.00..2290.00 rows=2 width=58)

 Filter: (status = 'pending')

 CTE filtered

 -> Seq Scan on orders (cost=0.00..1840.00 rows=10000 width=58)

 Filter: (created_at > '2025-01-01'::date)

Notice what happens here. The CTE runs a sequential scan onorderswith the date filter. It materializes all matching rows. Then the outer query applies thestatus = 'pending'filteraftermaterialization. Even if a composite index on(created_at, status)existed, the planner couldn't use it as it can't see through the CTE boundary to combine the predicates.

Why was it designed this way? Two reasons. First, reason was snapshot isolation. Materializing the CTE guaranteed that the result set was computed once, from a single snapshot, regardless of how many times it was referenced. Second, as protection for side-effect edge cases. If a CTE contained a data-modifying statement (INSERT,UPDATE,DELETE), materialising ensured it executed exactly once.

The workaround was well-known in the community: rewrite CTEs as subqueries. Subqueries had always been subject to the planner's normal optimisation rules, including predicate pushdown and inlining. The same query written as 
SELECT * FROM (SELECT * FROM orders WHERE created_at > '2025-01-01') sub WHERE status = 'pending'
 would produce a much better plan.

This led to an entire workaround culture. Developers would write queries with CTEs for readability during development, then rewrite them as nested subqueries for production. The community had a saying:CTEs are optimization fences. It was repeated so often. Many developers still believe it today. But it hasn't been true since PostgreSQL 12.

## PostgreSQL 12: CTE inlining

PostgreSQL 12 introduced automatic CTE inlining. Non-recursive, side-effect-free, singly-referenced CTEs are now inlined by default. The planner started treating them as subqueries and applies all its normal optimisations. Predicate pushdown, index usage, join reordering apply exactly as if the CTE syntax never existed.

The same query from the previous section now produces a completely different plan:

EXPLAIN 
WITH
 filtered 
AS
 (

 SELECT * FROM
 orders 
WHERE
 created_at 
>
 '2025-01-01'

)

SELECT * FROM
 filtered 
WHERE status =
 'pending'
;
 QUERY PLAN

---------------------------------------------------------------------------

 Seq Scan on orders (cost=0.00..2355.00 rows=2 width=58)

 Filter: ((created_at > '2025-01-01'::date) AND (status = 'pending'::text))

The CTE is gone from the plan entirely. Both predicates are merged into a single scan onorders. If there's a suitable index, the planner can use it. The CTE syntax doesn't change the execution plan.

PostgreSQL 12 also introduced two new keywords that let you override the planner's decision:

* MATERIALIZED- forces the CTE to materialize, even when the planner would inline it
* NOT MATERIALIZED- forces inlining, even when the planner would materialize it

-- force materialization

EXPLAIN 
WITH
 filtered 
AS
 MATERIALIZED (

 SELECT * FROM
 orders 
WHERE
 created_at 
>
 '2025-01-01'

)

SELECT * FROM
 filtered 
WHERE status =
 'pending'
;

-- Force inlining

EXPLAIN 
WITH
 filtered 
AS NOT
 MATERIALIZED (

 SELECT * FROM
 orders 
WHERE
 created_at 
>
 '2025-01-01'

)

SELECT * FROM
 filtered 
WHERE status =
 'pending'
;

This follows the same principle asVIEW inlining.

## When does a CTE get materialized?

### Case 1: single reference, no side effects (INLINED)

The simplest and most common case. If you reference the CTE exactly once and it contains no side effects, the planner inlines it.

EXPLAIN 
WITH
 recent 
AS
 (

 SELECT * FROM
 orders 
WHERE
 created_at 
>
 '2025-01-01'

)

SELECT * FROM
 recent 
WHERE status =
 'pending'
;
 QUERY PLAN

------------------------------------------------------------------------------

 Seq Scan on orders (cost=0.00..2355.00 rows=2 width=59)

 Filter: ((created_at > '2025-01-01'::date) AND (status = 'pending'::text))

(2 rows)

Both predicates are merged. The planner considers all access paths onordersdirectly.

### Case 2: multiple references (MATERIALIZED)

When a CTE is referenced more than once, the planner materializes it. This is actually a feature, CTE is computed once and reused. Therefore avoiding redundant work.

EXPLAIN 
WITH
 summary 
AS
 (

 SELECT status
, 
count
(
*
) 
AS
 cnt 
FROM
 orders 
GROUP BY status

)

SELECT
 a
.
status
, 
b
.
status

FROM
 summary a, summary b

WHERE
 a
.
cnt
 >
 b
.
cnt
;
 QUERY PLAN

----------------------------------------------------------------------------

 Nested Loop (cost=2355.04..2355.52 rows=5 width=64)

 Join Filter: (a.cnt > b.cnt)

 CTE summary

 -> HashAggregate (cost=2355.00..2355.04 rows=4 width=17)

 Group Key: orders.status

 -> Seq Scan on orders (cost=0.00..1855.00 rows=100000 width=9)

 -> CTE Scan on summary a (cost=0.00..0.08 rows=4 width=40)

 -> CTE Scan on summary b (cost=0.00..0.08 rows=4 width=40)

(8 rows)

TheCTE Scannodes appear twice, but theHashAggregateruns only once. For expensive computations referenced multiple times, this is exactly what you want.

### Case 3: recursive CTE (ALWAYS MATERIALIZED)

Recursive CTEs must maintain a working table between iterations. There's no way to inline them. We'll cover recursion in detail later in the article.

EXPLAIN 
WITH RECURSIVE
 subordinates 
AS
 (

 SELECT
 id, 
name
, manager_id 
FROM
 employees 
WHERE
 id 
=
 1

 UNION ALL

 SELECT
 e
.
id
, 
e
.
name
, 
e
.
manager_id

 FROM
 employees e

 JOIN
 subordinates s 
ON
 e
.
manager_id
 =
 s
.
id

)

SELECT * FROM
 subordinates;
 QUERY PLAN

-------------------------------------------------------------------------------

 CTE Scan on subordinates (cost=17.21..18.83 rows=81 width=40)

 CTE subordinates

 -> Recursive Union (cost=0.00..17.21 rows=81 width=13)

 -> Seq Scan on employees (cost=0.00..1.11 rows=1 width=13)

 Filter: (id = 1)

 -> Hash Join (cost=0.33..1.53 rows=8 width=13)

 Hash Cond: (e.manager_id = s.id)

 -> Seq Scan on employees e (cost=0.00..1.09 rows=9 width=13)

 -> Hash (cost=0.20..0.20 rows=10 width=4)

 -> WorkTable Scan on subordinates s (cost=0.00..0.20 rows=10 width=4)

(10 rows)

### Case 4: data-modifying CTE (ALWAYS MATERIALIZED)

CTEs that containINSERT,UPDATE, orDELETEare always materialized. The side effects must execute exactly once, in a predictable order.

EXPLAIN 
WITH
 deleted 
AS
 (

 DELETE FROM
 orders 
WHERE status =
 'cancelled'
 RETURNING 
*

)

SELECT
 count
(
*
) 
FROM
 deleted;
 QUERY PLAN

---------------------------------------------------------------------------

 Aggregate (cost=2670.13..2670.14 rows=1 width=8)

 CTE deleted

 -> Delete on orders (cost=0.00..2105.00 rows=25117 width=6)

 -> Seq Scan on orders (cost=0.00..2105.00 rows=25117 width=6)

 Filter: (status = 'cancelled'::text)

 -> CTE Scan on deleted (cost=0.00..502.34 rows=25117 width=0)

(6 rows)

TheCTE Scanis present because theDELETEmust be fully executed before thecount(*)can run.

### Case 5: VOLATILE function (MATERIALIZED)

If a CTE contains aVOLATILEfunction, the planner materializes it to prevent the function from being evaluated multiple times with potentially different results.

EXPLAIN 
WITH
 rand 
AS
 (

 SELECT
 id, random()
 AS
 r 
FROM
 orders

)

SELECT * FROM
 rand 
WHERE
 r 
<
 0
.
01
;
 QUERY PLAN

-----------------------------------------------------------------------

 CTE Scan on rand (cost=2105.00..4355.00 rows=33333 width=12)

 Filter: (r < '0.01'::double precision)

 CTE rand

 -> Seq Scan on orders (cost=0.00..2105.00 rows=100000 width=12)

(4 rows)

Even thoughrandis referenced only once, theCTE Scanis there.random()isVOLATILE, which forces materialization.

### Case 6: STABLE functions (INLINED)

STABLEfunctions likenow()donotprevent inlining. The reason is that the time is frozen at transaction start.

EXPLAIN 
WITH
 recent 
AS
 (

 SELECT * FROM
 orders

 WHERE
 created_at 
> now
()
 -
 interval 
'7 days'

)

SELECT * FROM
 recent 
WHERE status =
 'pending'
;
 QUERY PLAN

-------------------------------------------------------------------------------

 Seq Scan on orders (cost=0.00..2855.00 rows=2 width=59)

 Filter: ((status = 'pending'::text) AND (created_at > (now() - '7 days'::interval)))

(2 rows)

NoCTE Scan. The planner inlines the CTE and merges both predicates, just like Case 1.now()isSTABLEas it returns the same value within a transaction - and the planner's inlining check only looks forVOLATILEfunctions (viacontain_volatile_functions()).STABLEpasses that check.

Why do people thinkSTABLEblocks inlining? Because before PostgreSQL 12,allCTEs were materialized regardless of volatility. When PG 12 introduced inlining, the only function-level barrier wasVOLATILE. But the old "CTEs are optimization fences" mental model was so deeply ingrained that many developers assumedSTABLEwas also a problem. It isn't.

The function that actually blocks inlining:clock_timestamp(). Unlikenow(), it'sVOLATILEand returns a different value on every call. A CTE withclock_timestamp()will be materialized. Similarly,random()andnextval()areVOLATILEand force materialization (as shown in Case 5).

If you see a CTE withnow()being materialized, the cause is something else. Either multiple references, a data-modifying statement, or an explicitMATERIALIZEDhint. Don't blameSTABLE.

### Case 7: forcing behaviour with hints

You can always override the planner's decision.

-- force materialization on something that would normally be inlined

EXPLAIN 
WITH
 filtered 
AS
 MATERIALIZED (

 SELECT * FROM
 orders 
WHERE status =
 'pending'

)

SELECT * FROM
 filtered 
WHERE
 amount 
>
 400
;
 QUERY PLAN

----------------------------------------------------------------------

 CTE Scan on filtered (cost=2105.00..2670.58 rows=5290 width=92)

 Filter: (amount > '400'::numeric)

 CTE filtered

 -> Seq Scan on orders (cost=0.00..2105.00 rows=25137 width=59)

 Filter: (status = 'pending'::text)

(5 rows)
-- force inlining on something that would normally be materialized

EXPLAIN 
WITH
 filtered 
AS NOT
 MATERIALIZED (

 SELECT * FROM
 orders 
WHERE status =
 'pending'

)

SELECT * FROM
 filtered a

JOIN
 filtered b 
ON
 a
.
customer_id
 =
 b
.
customer_id
;
 QUERY PLAN

--------------------------------------------------------------------------------

 Hash Join (cost=2419.21..10686.65 rows=317742 width=118)

 Hash Cond: (orders.customer_id = orders_1.customer_id)

 -> Seq Scan on orders (cost=0.00..2105.00 rows=25137 width=59)

 Filter: (status = 'pending'::text)

 -> Hash (cost=2105.00..2105.00 rows=25137 width=59)

 -> Seq Scan on orders orders_1 (cost=0.00..2105.00 rows=25137 width=59)

 Filter: (status = 'pending'::text)

(7 rows) 

If the CTE were materialized, you would see a single scan of theorderstable, followed by two CTE Scans on the result. Instead, the planner has treated your query as if you had written a standard join between two subqueries.

Be careful withNOT MATERIALIZEDon multiply-referenced CTEs.When you force inlining, the subquery runs once for each reference. In the example above, theorderstable is scanned twice. Once foraand once forb. For small result sets this might be fine. For large ones, you're doing double the work. Measure before using.

### Case 8: FOR UPDATE / FOR SHARE (MATERIALIZED)

Row-locking clauses force materialization even on a singly-referenced, side-effect-free CTE. Internally, the planner'scontain_dml()check treatsFOR UPDATEandFOR SHAREthe same as data-modifying statements.

EXPLAIN 
WITH
 locked 
AS
 (

 SELECT * FROM
 orders 
WHERE status =
 'pending'
 FOR UPDATE

)

SELECT * FROM
 locked 
WHERE
 amount 
>
 400
;
 QUERY PLAN

----------------------------------------------------------------------------

 CTE Scan on locked (cost=2356.37..2921.95 rows=5290 width=92)

 Filter: (amount > '400'::numeric)

 CTE locked

 -> LockRows (cost=0.00..2356.37 rows=25137 width=65)

 -> Seq Scan on orders (cost=0.00..2105.00 rows=25137 width=65)

 Filter: (status = 'pending'::text)

(6 rows)

WithoutFOR UPDATE, this CTE would be inlined. TheLockRowsnode andCTE Scanconfirm materialization.

### Decision matrix

Here's the full picture across PostgreSQL versions:

Condition
PG ≤ 11
PG 12–16
PG 17–18

Single ref, pure SELECT
Materialized
Inlined
Inlined

Multiple refs, pure SELECT
Materialized
Materialized
Materialized (better stats)

VOLATILE function
Materialized
Materialized
Materialized

STABLE function
Materialized
Inlined
Inlined

Data-modifying (DML)
Materialized
Materialized
Materialized

FOR UPDATE / FOR SHARE
Materialized
Materialized
Materialized

Recursive
Materialized
Materialized
Materialized

Explicit 
MATERIALIZED
-
Materialized
Materialized

Explicit 
NOT MATERIALIZED
-
Inlined
Inlined

## The statistics black hole

As mentioned inPostgreSQL Statistics: Why queries run slow, materialized CTEs are one of the places "where no statistics go." This is arguably the biggest practical problem with CTE materialization.

When the planner materializes a CTE, the result set is stored in a temporary tuplestore. This tuplestore has nopg_statisticentries - no histograms, no MCVs, no correlation data. The planner has to estimate row counts and value distributions using hardcoded defaults.

Let's see this in action. Here's a CTE over 10,000 rows:

EXPLAIN 
WITH
 all_orders 
AS
 MATERIALIZED (

 SELECT * FROM
 orders

)

SELECT * FROM
 all_orders 
WHERE status =
 'pending'
 AND
 amount 
>
 400
;
 QUERY PLAN

-----------------------------------------------------------------------

 CTE Scan on all_orders (cost=1855.00..4355.00 rows=5290 width=92)

 Filter: ((amount > '400'::numeric) AND (status = 'pending'::text))

 CTE all_orders

 -> Seq Scan on orders (cost=0.00..1855.00 rows=100000 width=59)

(4 rows)

The planner estimated 5,290 rows. Where does that number come from? The planner has no MCV list forstatusinside the CTE, no histogram foramount. It falls back to default selectivities of0.3333for the range comparison onamountand a rough guess for the equality onstatus, and multiplies them against the 100,000 input rows.

If this CTE were inlined, the planner would read the actual statistics from 
pg_statistic
 for the 
orders
 table and produce estimates based on real data distribution, not defaults.

In a simple query this might not matter much. But when a materialized CTE feeds into a join, default-based estimates can cascade. The planner might choose a nested loop where a hash join would be better, or vice versa. It might underestimate memory needs and spill to disk unexpectedly.

### PG 17: Statistics propagation

PostgreSQL 17 brought two significant improvements to materialized CTEs:

Column statistics propagation.When the planner creates aCTE Scannode, it now propagates column statistics from the underlying query into the scan node. This meansn_distinct, MCV lists, and histograms from the source table can inform estimates on the CTE scan.

Path key propagation.Materialized CTEs now preserve sort order information. If the CTE's subquery produces sorted output, the planner knows about it and can skip redundant sorts downstream.

These improvements significantly reduce the estimation gap, but they don't eliminate it. Inlined CTEs are still strictly better for planning accuracy, because the planner works directly with the base table statistics rather than propagated copies. If your CTE doesn't need to be materialized, don't force it.

## When materialization helps

Materialization isn't always bad.

Multiple references.If the CTE result is used in multiple places, materialization computes it once. Without it, the subquery runs once per reference.

EXPLAIN 
WITH
 monthly_totals 
AS
 (

 SELECT
 date_trunc(
'month'
, created_at) 
AS month
,

 status
,

 sum
(amount) 
AS
 total

 FROM
 orders

 GROUP BY
 1
, 
2

)

SELECT
 cur
.
month
, 
cur
.
status
, 
cur
.
total
,

 prev
.
total
 AS
 prev_month_total,

 cur
.
total
 -
 prev
.
total
 AS
 delta

FROM
 monthly_totals cur

LEFT JOIN
 monthly_totals prev

 ON
 cur
.
month
 =
 prev
.
month
 +
 interval 
'1 month'

 AND
 cur
.
status
 =
 prev
.
status
; 
 QUERY PLAN

-------------------------------------------------------------------------------

 Merge Left Join (cost=3887.46..3990.90 rows=4384 width=136)

 Merge Cond: ((cur.month = ((prev.month + '1 mon'::interval))) AND (cur.status = prev.status))

 CTE monthly_totals

 -> HashAggregate (cost=3105.00..3181.72 rows=4384 width=49)

 Group Key: date_trunc('month'::text, (orders.created_at)::timestamp with time zone), orders.status

 -> Seq Scan on orders (cost=0.00..2355.00 rows=100000 width=23)

 -> Sort (cost=352.87..363.83 rows=4384 width=72)

 Sort Key: cur.month, cur.status

 -> CTE Scan on monthly_totals cur (cost=0.00..87.68 rows=4384 width=72)

 -> Sort (cost=352.87..363.83 rows=4384 width=72)

 Sort Key: ((prev.month + '1 mon'::interval)), prev.status

 -> CTE Scan on monthly_totals prev (cost=0.00..87.68 rows=4384 width=72)

(12 rows)

The aggregation runs once. Bothcurandprevread from the materialized result. Without materialization, the entire aggregation would run twice.

Expensive VOLATILE expressions.If a CTE contains calls to volatile functions or expensive computations, materialization ensures they execute exactly once.

Data-modifying operations.The whole point of writable CTEs is that the side effects happen once and theRETURNINGdata is available downstream. Materialization is not optional here.

## When inlining isn't enough

The imperative mindset from the introduction, "first do this, then do that", doesn't go away just because the planner inlines your CTEs. And this one is my personal favourite, and source that never stop delivering query refactoring.

Developers still structure queries as sequential pipelines, and that structure itself can create performance problems that have nothing to do with materialization.

A common pattern is building queries as an assembly line: one CTE filters rows, the next LEFT JOINs related tables and aggregates metadata withGROUP BY, the next filters on the aggregated results. It reads like a clean pipeline, but theGROUP BYin the middle creates a wall the planner can't optimize past.

WITH
 recent_orders 
AS
 (

 SELECT * FROM
 orders 
WHERE
 created_at 
>
 '2024-01-01'

),

order_metadata 
AS
 (

 SELECT

 o
.
id
,

 bool_or(
oa
.
id
 IS NOT NULL
) 
AS
 was_archived,

 count
(
o2
.
id
) 
AS
 related_count

 FROM
 recent_orders o

 LEFT JOIN
 orders_archive oa 
ON
 o
.
id
 =
 oa
.
id

 LEFT JOIN
 orders o2 
ON
 o
.
customer_id
 =
 o2
.
customer_id
 AND
 o2
.
id
 !=
 o
.
id

 GROUP BY
 o
.
id

)

SELECT
 o.
*
, 
m
.
was_archived
, 
m
.
related_count

FROM
 recent_orders o

JOIN
 order_metadata m 
ON
 o
.
id
 =
 m
.
id

WHERE
 m
.
was_archived
 =
 false

 AND
 m
.
related_count
 >
 0
;

Each CTE here is referenced once, so they all get inlined. No materialization, no optimization fence. The planner sees the full query. So what's the problem?

TheGROUP BYinorder_metadata. Even after inlining, the planner cannot push thewas_archived = falsepredicate past the aggregation. It must first LEFT JOIN every filtered order againstorders_archiveand self-joinorders, compute the aggregates for all of them, and only then discard the rows that don't match. Ifrecent_ordersreturns 50,000 rows but only 200 were ever archived, you're joining and aggregating 49,800 rows for nothing.

The fix is to replace the aggregation-then-filter pattern with correlatedEXISTSsubqueries:

SELECT
 o.
*

FROM
 orders o

WHERE
 o
.
created_at
 >
 '2024-01-01'

 AND NOT EXISTS
 (

 SELECT
 1
 FROM
 orders_archive oa 
WHERE
 oa
.
id
 =
 o
.
id

 )

 AND EXISTS
 (

 SELECT
 1
 FROM
 orders o2

 WHERE
 o2
.
customer_id
 =
 o
.
customer_id
 AND
 o2
.
id
 !=
 o
.
id

 );

EXISTSshort-circuits after finding the first matching row. The planner can pushcreated_at > '2024-01-01'all the way down to an index scan onorders, then probe each related table per result. No aggregation, no wasted work.

The rule of thumb:if your CTE contains aGROUP BYor aLEFT JOINjust to compute a boolean ("does this row have related data?"), you've built a wall the planner can't see past. A correlatedEXISTSlets the planner push filters down and stop scanning early. This applies whether the CTE is materialized or inlined.

## Writable CTEs (the power and the traps)

Data-modifying CTEs let youINSERT,UPDATE, orDELETEinside aWITHclause and use theRETURNINGdata in subsequent CTEs or the main query.

EXPLAIN 
WITH
 deleted 
AS
 (

 DELETE FROM
 orders

 WHERE status =
 'cancelled'

 AND
 created_at 
<
 '2023-01-01'

 RETURNING 
*

),

archived 
AS
 (

 INSERT INTO
 orders_archive

 SELECT * FROM
 deleted

 RETURNING id

)

SELECT
 count
(
*
) 
FROM
 archived;
 QUERY PLAN

----------------------------------------------------------------------------------------------

 Aggregate (cost=2709.19..2709.20 rows=1 width=8)

 CTE deleted

 -> Delete on orders (cost=0.00..2355.00 rows=8334 width=6)

 -> Seq Scan on orders (cost=0.00..2355.00 rows=8334 width=6)

 Filter: ((created_at < '2023-01-01'::date) AND (status = 'cancelled'::text))

 CTE archived

 -> Insert on orders_archive (cost=0.00..166.68 rows=8334 width=92)

 -> CTE Scan on deleted (cost=0.00..166.68 rows=8334 width=92)

 -> CTE Scan on archived (cost=0.00..166.68 rows=8334 width=0)

(9 rows) 

This deletes old cancelled orders, moves them to an archive table, and counts how many were archived - all in a single atomic statement, no application-level coordination needed.

But there are sharp edges.

### You cannot read what you just wrote

All sub-statements in a data-modifying CTE see the same snapshot. This means the effects of one CTE arenot visibleto other CTEs or the main query when they read thetarget table. Only theRETURNINGclause communicates data between CTE steps.

SELECT
 count
(
1
) 
FROM
 orders 
WHERE
 customer_id 
=
 1
;
 count

-------

 31

(1 row)
WITH
 ins 
AS
 (

 INSERT INTO
 orders (customer_id, amount, 
status
, created_at)

 VALUES
 (
1
, 
100
.
00
, 
'pending'
, CURRENT_DATE)

 RETURNING id

)

-- this does NOT see the row we just inserted

SELECT
 count
(
1
) 
FROM
 orders 
WHERE
 customer_id 
=
 1
;
 count

-------

 31

(1 row)

Thecount(1)query sees the pre-insert snapshot. If you need the inserted data, you must use theRETURNINGclause from theinsCTE, not re-read the table.

### Tuple shuffling

A common pattern is using writable CTEs to move rows between tables atomically:

WITH
 moved 
AS
 (

 DELETE FROM
 orders_staging

 RETURNING 
*

)

INSERT INTO
 orders

SELECT * FROM
 moved;

This deletes all rows from the staging table and inserts them into the production table in a single atomic operation. No window where data exists in both or neither table.

Data-modifying CTEs disable parallel query for the entire statement. If you have a complex query that mixes reads and writes, the write CTE prevents parallelism even for the read-only parts.

## Recursive CTEs are always materialized

Recursive CTEs use an iterative working-table mechanism. Despite the name, they aren't truly recursive. PostgreSQL doesn't "call itself" by creating a nested stack of unfinished queries. Instead, it operates in loops.

1. Execute the non-recursive term (the "seed"). Put results in the working table.
2. Execute the recursive term using the working table as input. New rows become thenextworking table.
3. Repeat until the recursive term returns no new rows.
4. Return the union of all iterations.

WITH RECURSIVE
 org_chart 
AS
 (

 -- Seed: start from the CEO

 SELECT
 id, 
name
, manager_id, 
1
 AS
 depth

 FROM
 employees

 WHERE
 manager_id 
IS NULL

 UNION ALL

 -- Recursive term: find direct reports

 SELECT
 e
.
id
, 
e
.
name
, 
e
.
manager_id
, 
oc
.
depth
 +
 1

 FROM
 employees e

 JOIN
 org_chart oc 
ON
 e
.
manager_id
 =
 oc
.
id

)

SELECT * FROM
 org_chart 
ORDER BY
 depth, 
name
;
 id | name | manager_id | depth

----+---------+------------+-------

 1 | Alice | | 1

 2 | Bob | 1 | 2

 3 | Charlie | 1 | 2

 4 | Diana | 2 | 3

 5 | Eve | 2 | 3

 6 | Frank | 3 | 3

 7 | Grace | 3 | 3

 8 | Hank | 6 | 4

 9 | Ivy | 6 | 4

(9 rows)

### UNION vs UNION ALL

The choice betweenUNIONandUNION ALLin recursive CTEs matters more than in regular queries.

UNION ALLkeeps all rows, including duplicates. This is faster but dangerous: if your graph has cycles, the recursion never terminates. PostgreSQL will run until you cancel the query or memory is exhausted.

UNIONdeduplicates at each iteration. This prevents infinite loops in cyclic graphs but adds the cost of hashing and comparing rows at every step.

PostgreSQL 14 added SQL-standardSEARCHandCYCLEclauses that replace the manual patterns for controlling traversal order (breadth-first vs. depth-first) and detecting cycles.SEARCH BREADTH FIRST BY/SEARCH DEPTH FIRST BYcontrol the order, whileCYCLEautomatically detects and marks cycles, which is far cleaner than the old pattern of accumulating an array of visited IDs.

For pure hierarchical data (trees without cycles), consider theltreeextension as an alternative to recursive CTEs. It stores the full path as a label tree and supports efficient ancestor/descendant queries with GiST indexes. The trade-off is denormalized storage vs. on-the-fly recursion.

## The exotic edge cases

### Partition pruning lost

When you materialize a CTE over a partitioned table, partition pruning cannot happen on the CTE scan side. The materialized result is a flat tuplestore disconnected from the partition metadata.

-- assume orders is range-partitioned by created_at

WITH
 recent 
AS
 MATERIALIZED (

 SELECT * FROM
 orders

)

SELECT * FROM
 recent 
WHERE
 created_at 
>
 '2025-06-01'
;

Thecreated_at > '2025-06-01'predicate is appliedaftermaterialization. All partitions are scanned to build the CTE, even though only one or two would be needed. UseNOT MATERIALIZED(or simply let the planner inline it) to preserve partition pruning.

### Prepared statements and plan caching

PostgreSQL generates custom plans for the first 5 executions of a prepared statement. After that, it may switch to a generic plan. CTE inlining decisions can differ between custom and generic plans, because generic plans don't know the actual parameter values.

This means a CTE that gets inlined during your first 5 calls might start materializing on the 6th or vice versa. If you see sudden plan changes with prepared statements, check whether the CTE inlining behaviour has shifted.

### work_mem spilling

Materialized CTEs store their results in memory, bounded bywork_mem. When the result set exceeds this limit, it silently spills to disk as a temporary file. This is not an error - it just gets slower.

Monitor withlog_temp_files = 0(logs all temp files) or checkEXPLAIN (ANALYZE, BUFFERS)for temp read/write counts.

PostgreSQL 18: EXPLAIN now shows memory/disk usageStarting with PostgreSQL 18,EXPLAIN ANALYZEreports memory and disk usage for Material nodes, including CTE materialization. You can see exactly how much memory a materialized CTE consumed and whether it spilled to disk.

### CTE and security barrier views

A `security_barrier` view is a "black box" that forces the database to fully resolve the view's internal logic before any outer filters are applied.

Security-barrier views already prevent subquery flattening as a security measure (to stop user-defined functions from seeing rows they shouldn't). When you combine a security-barrier view with a CTE, you compound the optimisation barriers. The planner can neither inline the view nor the CTE. If performance matters in this scenario, consider materializing the security-sensitive filtering into a temporary table first.

## CTE vs. subquery vs. temporary table

CTE, referenced oncethe planner inlines it on PG 12+, so it doesn't affect the execution plan. This is the default choice for breaking up complex queries.

CTE, referenced multiple times (small result)represents acceptable cost. Materialization means the subquery runs once. For aggregations or filtered subsets that produce a few hundred rows, the overhead is minimal.

As 
Henrietta Dombrovskaya
 emphasizes, "The best temporary table is the one you didn't create". Always exhaust your indexing and query-rewriting options before reaching for a temp table, as the DDL overhead often outweighs the execution gains.

**CTE, referenced multiple times (large result)** ss case when you might consider a temporary table instead. A materialized CTE has no indexes and no statistics. A temporary table can have both, and as covered in [Introduction to Buffers](/posts/introduction-to-buffers/), temporary tables use local buffers with simpler locking and no WAL overhead. If you're joining against 100k+ rows from a CTE, create a temp table, add an index, and `ANALYZE` it.

Data-modifying operationswith writable CTE. No alternative gives you the atomic, single-statement behavior.

Recursive CTEs. There's no alternative in pure SQL.

Large intermediate results needing indexes/statistics. If you really need them use temporary table. As discussed inReading Buffer statistics, temporary tables offer full planner support - indexes, statistics, and buffer management - that materialized CTEs simply don't have.

Scenario
Recommendation

Readability, single reference
CTE (inlined, free)

Compute once, use many times (small)
CTE (materialized)

Compute once, use many times (large)
Temporary table

Atomic data modification
Writable CTE

Hierarchy / graph traversal
Recursive CTE

Need indexes on intermediate data
Temporary table

## The PG 18 state of affairs

PostgreSQL 18 continues to refine CTE handling without any revolutionary changes:

* EXPLAIN shows memory/disk usagefor CTE materialization nodes. You can finally see whether your CTE fit inwork_memor spilled to disk.
* Better query plans for CTEs on the same table.The planner is smarter about eliminating redundant scans when multiple CTEs reference the same underlying table.
* Data-modifying CTE fix for updatable views with rules.An edge case where writable CTEs interacted incorrectly with views defined using rules has been resolved.
* CTE inlining is mature.The core inlining logic hasn't changed since PG 12. What has improved is everything around it - better statistics propagation (PG 17), better materialisation diagnostics (PG 18), better cost estimation.

CTEs are a good tool. Just know when you're holding the sharp end.