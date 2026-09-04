---
title: 'A Query on a 3-Billion-Row Table Took 100 Minutes: One Added Line Made It 40ms'
url: https://explainanalyze.com/p/a-query-on-a-3-billion-row-table-took-100-minutes-one-added-line-made-it-40ms/
site_name: tldr
content_file: tldr-a-query-on-a-3-billion-row-table-took-100-minutes
fetched_at: '2026-09-04T21:14:47.657297'
original_url: https://explainanalyze.com/p/a-query-on-a-3-billion-row-table-took-100-minutes-one-added-line-made-it-40ms/
date: '2026-09-04'
published_date: '2026-09-03T00:00:00+00:00'
description: A derived table computes the latest stock count for 6.57 million stores so the outer query can keep 603 of them. The index it uses leads with the wrong column, so the optimizer walks 491 million index entries to get there. One added line fixes both.
tags:
- tldr
---

TL;DR
An 
EXPLAIN ANALYZE
 tree has one line that owns the time; find it before reading anything else, then diagnose two things separately: whether the query computes more than the question needs, and whether the filter matches an index’s leading columns. Worked through a real reporting query against a 3.2-billion-row table, rewritten from 1h43m to 40ms with no schema change. The rewrite only works because a small set exists to filter by; when there isn’t one, the fix is an index, and that is neither free nor reversible on a table that size.

The alert fires the way it always does: a statement crossed thirty minutes, the alerting job snapshotted everything running on the server, and the snapshot is attached to the ticket. In it, a reporting query againstinventory.stock_counts, a table whoseAUTO_INCREMENTcounter reads 3,252,568,638. Wall time at the moment of the snapshot: 1 hour 43 minutes, still running.

If the ticket didn’t have the snapshot,SHOW FULL PROCESSLIST;is where the SQL comes from.FULLmatters; without it the query text is cut at 100 characters, and the interesting part of this one is past character 100.

 1

 2

 3

 4

 5

 6

 7

 8

 9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

SELECT

 
cl
.
line_type
,

 
cl
.
resolution
,

 
COUNT
(
*
)
 
AS
 
row_count
,

 
SUM
(
EXISTS
 
(
 
-- [E] per-row check

 
SELECT
 
1
 
FROM
 
inventory
.
signoffs
 
s

 
WHERE
 
s
.
stock_count_id
 
=
 
sc
.
id

 
))
 
AS
 
counts_with_any_signoff

FROM
 
inventory
.
stock_counts
 
sc
 
-- [1] main table

JOIN
 
(
 
-- [2] derived table "latest"

 
SELECT
 
store_id
,
 
supplier_id
,
 
MAX
(
counted_at
)
 
AS
 
max_ts

 
FROM
 
inventory
.
stock_counts

 
WHERE
 
supplier_id
 
=
 
713

 
AND
 
store_id
 
IS
 
NOT
 
NULL

 
GROUP
 
BY
 
store_id
,
 
supplier_id

)
 
latest

 
ON
 
latest
.
store_id
 
=
 
sc
.
store_id

 
AND
 
latest
.
supplier_id
 
=
 
sc
.
supplier_id

 
AND
 
latest
.
max_ts
 
=
 
sc
.
counted_at

JOIN
 
retail
.
stores
 
st
 
-- [3] scope: whose stores?

 
ON
 
st
.
id
 
=
 
sc
.
store_id

JOIN
 
inventory
.
count_lines
 
cl
 
-- [4] the detail rows

 
ON
 
cl
.
stock_count_id
 
=
 
sc
.
id

WHERE
 
st
.
chain_id
 
=
 
2047
 
-- [3] scope, continued

 
AND
 
sc
.
supplier_id
 
=
 
713

GROUP
 
BY
 
cl
.
line_type
,
 
cl
.
resolution
 
-- [5] final rollup

ORDER
 
BY
 
cl
.
line_type
,
 
cl
.
resolution
;

The reflex is to paste this intoEXPLAIN ANALYZEand go looking for the red line. Hold that for a minute. The plan will tell you what the query costs. It cannot tell you what the answershouldcost, and without that yardstick every line in the plan looks equally suspicious. That yardstick comes from reading the query.

## Read the query before the plan

SQL is not evaluated top to bottom. TheSELECTline runs almost last. The order isFROM,JOINs,WHERE,GROUP BY,SELECT,ORDER BY, with innermost self-contained subqueries evaluated before the query that wraps them. Read it in that order and the bracketed pieces above sort themselves out.

Start with the scope: scan theWHEREandONclauses for literal constants. They define the intended size of the answer. Piece [3] joinsretail.storesand filtersst.chain_id = 2047, restricting everything to one retail chain’s stores, andsc.supplier_id = 713restricts to one supplier. One chain is a few hundred stores. (stock_countshas its ownchain_idcolumn. Why the query scopes through another table instead is answered when we open the schema below.)

Next, the innermost self-contained piece: the derived table [2]. It has no references to the outside and could run on its own. For supplier 713, it computes the newestcounted_atfor every store. Measured against the scope from [3]: it knows nothing about any chain. It does this for virtually every store supplier 713 has ever delivered to, across every chain on the platform. TheIS NOT NULLfilter drops only the minority of rows with no store. Nothing narrows it to the few hundred stores the question is about.

Then [1] joined to [2]. Joininglatestback tostock_countson(store_id, supplier_id, max_ts = counted_at)is the standard “latest row per group” idiom: the subquery findswhenthe newest count happened per store, the join fetches the row from that moment. AMAX(...)subquery joined back on equality to the same table is this idiom every time you see it.

Piece [4] is the detail: each stock count has child rows ininventory.count_lines, one per SKU counted, and those carry theline_typeandresolutionbeing counted. Piece [E] asks, per stock count, whether at least one sign-off row exists.EXISTSreturns 1 or 0, soSUM(EXISTS ...)counts stock counts with any sign-off; a per-row lookup, cheap ifsignoffs.stock_count_idis indexed. Piece [5] groups the survivors by(line_type, resolution)and counts.

In one sentence: for chain 2047 and supplier 713, take each store’s most recent stock count and count its lines by variance type and resolution, noting which counts have been signed off.

That sentence already exposes the problem. The question is scoped to one chain, but piece [2] computes the latest timestamp for every store of supplier 713. The query as written relies on the optimizer to push the chain scoping into [2]. Whether it did is what the plan shows.

## Run EXPLAIN ANALYZE on a replica, then find the one line

EXPLAIN <query>prints the execution plan without running the query: driving table, index per join, join order. Every number in it is an estimate.rows=andcost=come from table statistics and can be off by orders of magnitude, so plainEXPLAINshows the intended shape of the plan, not where the time goes.EXPLAIN ANALYZE <query>executes the query and prints the same tree annotated with measurements:actual time=X..Yis milliseconds to first row and to last row,rows=is rows actually processed per loop,loops=is how many times the step ran. That turns “the query is slow” into “this specific line is slow.”Part II of the queries seriescovers the general reading; this post is one plan read all the way down.

Warning
EXPLAIN ANALYZE
 runs the query, so it takes as long as the query takes; the run below took 1h43m to produce. It is also all-or-nothing: killing it early returns an error, not a partial plan. Run it on a replica, never the primary, and know that a consistent-read snapshot held open for that long delays InnoDB purge on that replica for the duration. A timeout on the diagnostic run is pointless: the alert already established the query runs past thirty minutes, so any cap either kills the run (no output) or sits above the half-hour mark (no protection). Start with plain 
EXPLAIN
, and pay the full 
EXPLAIN ANALYZE
 cost once if the actuals are needed. The timeout belongs on the fix-validation runs later, where milliseconds are expected: 
SET max_execution_time = 60000;
 stops a wrong candidate from running another 1h43m. It governs plain 
SELECT
s and may not interrupt 
EXPLAIN ANALYZE
 itself, so keep 
KILL QUERY <id>
 ready from a second session.

The full output, produced in 1h 43m 29s:

 1

 2

 3

 4

 5

 6

 7

 8

 9

10

11

12

13

14

-> Sort: inventory.cl.line_type, inventory.cl.resolution (actual time=6.21e+6..6.21e+6 rows=3 loops=1)

 -> Table scan on <temporary> (actual time=6.21e+6..6.21e+6 rows=3 loops=1)

 -> Aggregate using temporary table (actual time=6.21e+6..6.21e+6 rows=3 loops=1)

 -> Nested loop inner join (cost=8114 rows=3248) (actual time=6.21e+6..6.21e+6 rows=1823 loops=1)

 -> Nested loop inner join (cost=6173 rows=1627) (actual time=6.21e+6..6.21e+6 rows=552 loops=1)

 -> Nested loop inner join (cost=4951 rows=1397) (actual time=6.21e+6..6.21e+6 rows=552 loops=1)

 -> Covering index lookup on st using chain_id (chain_id=2047) (cost=62.3 rows=603) (actual time=0.0498..0.274 rows=603 loops=1)

 -> Filter: ((latest.supplier_id = 713) and (latest.max_ts is not null)) (cost=129e+6..5.79 rows=2.32) (actual time=10297..10297 rows=0.915 loops=603)

 -> Index lookup on latest using <auto_key2> (store_id=retail.st.id) (cost=228e+6..228e+6 rows=23.2) (actual time=10297..10297 rows=0.915 loops=603)

 -> Materialize (cost=228e+6..228e+6 rows=392e+6) (actual time=6.21e+6..6.21e+6 rows=6.57e+6 loops=1)

 -> Filter: ((inventory.stock_counts.supplier_id = 713) and (inventory.stock_counts.store_id is not null)) (cost=188e+6 rows=392e+6) (actual time=6.75..6.18e+6 rows=6.57e+6 loops=1)

 -> Covering index skip scan for grouping on stock_counts using store_supplier_counted_at over (NULL < store_id) (cost=188e+6 rows=392e+6) (actual time=0.0268..6.14e+6 rows=491e+6 loops=1)

 -> Covering index lookup on sc using store_supplier_counted_at (store_id=retail.st.id, supplier_id=713, counted_at=latest.max_ts) (cost=0.758 rows=1.16) (actual time=0.089..0.0898 rows=1 loops=552)

 -> Index lookup on cl using stock_count_id (stock_count_id=inventory.sc.id) (cost=0.994 rows=2) (actual time=0.246..0.249 rows=3.3 loops=552)

Indentation is nesting. Deeper lines execute first and feed results upward; the top line, theSort, happens last. Times are milliseconds, often in scientific notation:6.21e+6ms is 6,210,000 ms, about 1.7 hours. Don’t try to understand every line. Find the one with the largestactual timeand the largestrows. A parent’s time includes its children, which is whySort,Aggregate, and all three joins show6.21e+6; descend until the time originates.

It originates here:

1

2

-> Covering index skip scan for grouping on stock_counts using store_supplier_counted_at over (NULL < store_id)

 (cost=188e+6 rows=392e+6) (actual time=0.0268..6.14e+6 rows=491e+6 loops=1)

MySQL scanned thestore_supplier_counted_atindex onstock_counts, touched 491 million index entries, and spent 6.14e+6 ms on it, about 1.7 hours. The line sits underMaterialize: this branch is piece [2], the derived tablelatest, being built. It confirms the reading from the previous section. The optimizer did not push the chain scoping into [2]. It computed latest timestamps for 6.57 million stores (Materialize ... rows=6.57e+6) and then the outer join discarded all but 552 of them.

Two things worth noticing before moving on. The estimate on that line,rows=392e+6, was in the right ballpark of the actual 491 million, and the estimate is printed by plainEXPLAIN. The 1h43m diagnostic run bought certainty; a line estimating hundreds of millions of rows under aMaterializewas already visible for free. And the rest of the tree is healthy: thechain_idlookup found its 603 rows in 0.274 ms, and thescandcllookups take fractions of a millisecond per loop. One line owns the incident.

Why the optimizer couldn't rescue this one
MySQL 8.0.22 added 
derived condition pushdown
, which can move an outer 
WHERE
 condition into a derived table, including one with 
GROUP BY
, when the condition references only the derived table’s columns and constants. The chain scoping here is neither. It lives in a join condition to a different table (
latest.store_id = st.id
, with the constant on 
st.chain_id
), so there is nothing shaped like a pushable predicate. The optimizer did what the query said: build 
latest
 for the whole supplier, then join.

## Open the table and diagnose two things separately

The slow line names its table and index. Pull the definition:

1

SHOW
 
CREATE
 
TABLE
 
inventory
.
stock_counts
\
G

 1

 2

 3

 4

 5

 6

 7

 8

 9

10

11

CREATE
 
TABLE
 
stock_counts
 
(

 
id
 
bigint
 
NOT
 
NULL
 
AUTO_INCREMENT
,

 
counted_at
 
bigint
 
NOT
 
NULL
,

 
chain_id
 
bigint
 
DEFAULT
 
NULL
,

 
store_id
 
bigint
 
DEFAULT
 
NULL
,

 
supplier_id
 
bigint
 
NOT
 
NULL
,

 
...

 
PRIMARY
 
KEY
 
(
id
),

 
KEY
 
store_supplier_counted_at
 
(
store_id
,
 
supplier_id
,
 
counted_at
),

 
KEY
 
chain_supplier_counted_at
 
(
chain_id
,
 
supplier_id
,
 
counted_at
)

)
 
ENGINE
=
InnoDB
 
AUTO_INCREMENT
=
3252568638
 
...

AUTO_INCREMENT=3252568638: the table has seen roughly 3.2 billion rows. The scale is why the mistake costs hours rather than seconds.

chain_supplier_counted_aton(chain_id, supplier_id, counted_at)looks purpose-built for this question, which raises the obvious objection: why doesn’t the query filterWHERE sc.chain_id = 2047and skip thestoresjoin entirely? Becausechain_idonstock_countsis not populated. It isDEFAULT NULL, and rows do not reliably carry it, so filtering on it returns wrong (empty) results. The query scopes throughretail.storesbecause that table is the source of truth for which chain owns a store. That resolves the question parked earlier, and it is verified empirically in the next section, where the wrong candidate gets tested anyway.

Before building a fix around a promising index, check that the column has data:

1

2

3

4

SELECT
 
COUNT
(
*
)
 
AS
 
total
,
 
COUNT
(
chain_id
)
 
AS
 
with_chain

FROM
 
inventory
.
stock_counts

WHERE
 
supplier_id
 
=
 
713
;

-- COUNT(col) skips NULLs; if with_chain is ~0, the index is unusable

A decoy like this deserves a follow-up outside the incident. The column and its index are not neutral. The index takes disk and write overhead on every insert while being unusable for reads, and it invites wrong queries; the wrong candidate below is exactly that. The resolution is either to backfillchain_idso the index becomes trustworthy, or, more likely, to drop the index (fast) and then the column, after auditing for remaining readers and writers.

Now compare the usable index against the piece of the query that produced the slow line, the derived table [2]:

1

2

WHERE
 
supplier_id
 
=
 
713
 
AND
 
store_id
 
IS
 
NOT
 
NULL

GROUP
 
BY
 
store_id
,
 
supplier_id

The relevant concept is the leftmost-prefix rule. A composite index is ordered like a phone book sorted by (last name, first name): lookups by last name, or last name plus first name, are fast, and a lookup by first name alone gets no help from the sort order.store_supplier_counted_atleads withstore_id, but piece [2] only constrainssupplier_id, the second column. MySQL could not seek directly to supplier 713’s rows. Instead it did what the plan line says, a skip scan for grouping (the tree-format name for theloose index scanMySQL uses forGROUP BY): walk every distinctstore_idin the index, and probe each one for supplier 713. That is the 491 million entries and the 1.7 hours.

The diagnosis is two independent problems, and they have separate fixes:

1. Logical waste, visible from reading the query: piece [2] computes latest timestamps for 6.57 million stores when the question needs 603.
2. Physical mismatch, confirmed from the schema: the filter columnsupplier_iddoes not lead any trustworthy index, so the wasteful computation was also executed in the worst available way.

## Fix the logical waste first

The principle: compute the small set first and hand it to the big table, so the index’s leading column is constrained. The chain has 603 stores, and the usable index leads withstore_id; feeding the store ids in turns every lookup into an index seek. Three versions of the same idea, from most manual to ready-to-run.

V1 is two steps, fully manual, and fine for a one-off investigation because each step is verifiable on its own:

1

2

3

4

5

6

7

8

9

-- Step 1: get the small set

SELECT
 
id
 
FROM
 
retail
.
stores
 
WHERE
 
chain_id
 
=
 
2047
;

-- Step 2: paste the ids into the original query's subquery

...

 
WHERE
 
supplier_id
 
=
 
713

 
AND
 
store_id
 
IN
 
(
1001
,
 
1002
,
 
...)
 
-- the 603 ids

 
GROUP
 
BY
 
store_id
,
 
supplier_id

...

V2 keeps the shape of the original and adds one line. Minimal diff, easy to review, and the version that gets validated below:

1

2

3

4

5

6

7

8

JOIN
 
(

 
SELECT
 
store_id
,
 
supplier_id
,
 
MAX
(
counted_at
)
 
AS
 
max_ts

 
FROM
 
inventory
.
stock_counts

 
WHERE
 
supplier_id
 
=
 
713

 
AND
 
store_id
 
IN
 
(
SELECT
 
id
 
FROM
 
retail
.
stores
 
WHERE
 
chain_id
 
=
 
2047
)
 
-- <-- the fix

 
GROUP
 
BY
 
store_id
,
 
supplier_id

)
 
latest

...

V3 is V2 spelled out end to end. Everything is the original except the one added line:

 1

 2

 3

 4

 5

 6

 7

 8

 9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

SELECT

 
cl
.
line_type
,

 
cl
.
resolution
,

 
COUNT
(
*
)
 
AS
 
row_count
,

 
SUM
(
EXISTS
 
(

 
SELECT
 
1
 
FROM
 
inventory
.
signoffs
 
s

 
WHERE
 
s
.
stock_count_id
 
=
 
sc
.
id

 
))
 
AS
 
counts_with_any_signoff

FROM
 
inventory
.
stock_counts
 
sc

JOIN
 
(

 
SELECT
 
store_id
,
 
supplier_id
,
 
MAX
(
counted_at
)
 
AS
 
max_ts

 
FROM
 
inventory
.
stock_counts

 
WHERE
 
supplier_id
 
=
 
713

 
AND
 
store_id
 
IN
 
(
SELECT
 
id
 
FROM
 
retail
.
stores
 
WHERE
 
chain_id
 
=
 
2047
)
 
-- <-- the fix

 
GROUP
 
BY
 
store_id
,
 
supplier_id

)
 
latest

 
ON
 
latest
.
store_id
 
=
 
sc
.
store_id

 
AND
 
latest
.
supplier_id
 
=
 
sc
.
supplier_id

 
AND
 
latest
.
max_ts
 
=
 
sc
.
counted_at

JOIN
 
retail
.
stores
 
st

 
ON
 
st
.
id
 
=
 
sc
.
store_id

JOIN
 
inventory
.
count_lines
 
cl

 
ON
 
cl
.
stock_count_id
 
=
 
sc
.
id

WHERE
 
st
.
chain_id
 
=
 
2047

 
AND
 
sc
.
supplier_id
 
=
 
713

GROUP
 
BY
 
cl
.
line_type
,
 
cl
.
resolution

ORDER
 
BY
 
cl
.
line_type
,
 
cl
.
resolution
;

All three work the same way underneath.store_id, the index’s leading column, is now constrained to 603 values, so the subquery becomes roughly 603 index seeks instead of a 491-million-entry skip scan. Seconds instead of hours, no schema change, reversible. Results are identical as long as “latest per store” does not depend on rows outside the chain, and here it does not: the join back toscwas already store-scoped, and a store belongs to one chain.

A further form replaces the derived table with a correlated subquery. It plans cleaner, with noMaterializestep at all, and it is the version that shipped, shown at the end.

The rewrite works because a small set exists:retail.storessupplies one chain’s worth of store ids. If that scoping were unavailable (a genuinely per-supplier question: latest stock count for every store supplier 713 delivers to), there is nothing to filter first and the fix has to be physical. The filter is onsupplier_id, sosupplier_idhas to lead the index:

1

KEY
 
supplier_store_counted_at
 
(
supplier_id
,
 
store_id
,
 
counted_at
)

That reads supplier 713’s contiguous slice of the index, already sorted by store with timestamps sorted within each, and drops reads from roughly 491 million to roughly 6.6 million: minutes instead of hours. For the per-supplier question all 6.57 million groups are genuinely needed, so that is the floor.

It is not needed here, and it is not free. Hours of online DDL (gh-ost or pt-online-schema-change) on a 3.2-billion-row table, tens of gigabytes of disk, write overhead on every future insert, replica-lag risk during the build. It is also net-new, because the existingstore_supplier_counted_atstill serves “history of one store” lookups and can’t be swapped out. The shape that holds up is to propose it only if per-supplier queries become a recurring pattern, sized against write volume. Query rewrites are free and reversible;indexes on billion-row tables are neither. A third, long-term option is backfillingchain_idsochain_supplier_counted_atbecomes usable, and that is a data-quality project rather than a query fix.

## Verify correctness before speed

Verification is two questions, in order: is it still correct, then is it actually fast. Two candidate fixes were tested. Each fails a different one of the two checks, which is why both checks are needed. The baseline comes from the original 1h43m run: 3 groups, 1,823 rows, 552 stock counts. Capture that before touching anything; a fix without a baseline can’t be verified, only admired.

The first candidate filters onsc.chain_iddirectly, the one the decoy index suggests. It runs in 0.08 ms and is wrong:

1

2

-> Index lookup on stock_counts using chain_supplier_counted_at (chain_id=2047, supplier_id=713)

 (actual time=0.0212..0.0212 rows=0 loops=1)

rows=0: no stock count carries thischain_id, because the column is unpopulated. Every later join in the plan readsnever executed, since the driving table was empty, which is why the query finished in a tenth of a millisecond. Fast does not imply correct. Compare row counts against the baseline every time. Andnever executedin a plan means something upstream short-circuited; find the deepest line withrows=0to see where the data ran out.

The second candidate is V2, the subquery filtered to the chain’s stores. Correct, and 79 ms against 1h 43m:

Original
chain_id
 filter
store filter (V2)
Time
1h 43m
0.08 ms
79 ms
Rows read to build 
latest
491,000,000
0
12,500
Result correct?
baseline
wrong (empty)
matches baseline

Generalized, the checklist is short. PlainEXPLAINfirst: confirm the expected index appears and no line estimates millions of rows.EXPLAIN ANALYZEwithmax_execution_timeset: confirm where the time actually goes. Compare results to the known-good baseline, row counts at minimum. A fix that changes the answer is not a fix.

The version that shipped is the correlated form. Same idea as the one-line fix, constrain everything to the chain’s stores, expressed directly: drive fromretail.storesand compute each store’s latest timestamp on demand, with no derived table at all.

 1

 2

 3

 4

 5

 6

 7

 8

 9

10

11

12

13

14

15

16

17

18

SELECT

 
cl
.
line_type
,

 
cl
.
resolution
,

 
COUNT
(
*
)
 
AS
 
row_count
,

 
SUM
(
EXISTS
 
(
SELECT
 
1
 
FROM
 
inventory
.
signoffs
 
s
 
WHERE
 
s
.
stock_count_id
 
=
 
sc
.
id
))
 
AS
 
counts_with_any_signoff

FROM
 
retail
.
stores
 
st

JOIN
 
inventory
.
stock_counts
 
sc

 
ON
 
sc
.
store_id
 
=
 
st
.
id

 
AND
 
sc
.
supplier_id
 
=
 
713

 
AND
 
sc
.
counted_at
 
=
 
(
SELECT
 
MAX
(
sc2
.
counted_at
)

 
FROM
 
inventory
.
stock_counts
 
sc2

 
WHERE
 
sc2
.
store_id
 
=
 
st
.
id

 
AND
 
sc2
.
supplier_id
 
=
 
713
)

JOIN
 
inventory
.
count_lines
 
cl

 
ON
 
cl
.
stock_count_id
 
=
 
sc
.
id

WHERE
 
st
.
chain_id
 
=
 
2047

GROUP
 
BY
 
cl
.
line_type
,
 
cl
.
resolution

ORDER
 
BY
 
cl
.
line_type
,
 
cl
.
resolution
;

The results, 0.22 s from a cold cache:

line_type
resolution
row_count
counts_with_any_signoff
Variance
None
1
1
Variance
Reorder
551
311
Variance
WriteOff
36
36
Reconciled
None
1236
1236

ItsEXPLAIN ANALYZE, complete, at 40 ms warm:

 1

 2

 3

 4

 5

 6

 7

 8

 9

10

11

12

-> Sort: inventory.cl.line_type, inventory.cl.resolution (actual time=40.1..40.1 rows=4 loops=1)

 -> Table scan on <temporary> (actual time=40.1..40.1 rows=4 loops=1)

 -> Aggregate using temporary table (actual time=40.1..40.1 rows=4 loops=1)

 -> Nested loop inner join (cost=991 rows=1192) (actual time=0.118..29.7 rows=1824 loops=1)

 -> Nested loop inner join (cost=273 rows=603) (actual time=0.104..25.3 rows=552 loops=1)

 -> Covering index lookup on st using chain_id (chain_id=2047) (cost=62.2 rows=603) (actual time=0.0429..0.191 rows=603 loops=1)

 -> Filter: (inventory.sc.counted_at = (select #3)) (cost=0.25 rows=1) (actual time=0.041..0.0415 rows=0.915 loops=603)

 -> Covering index lookup on sc using store_supplier_counted_at (store_id=retail.st.id, supplier_id=713, counted_at=(select #3)) (cost=0.25 rows=1) (actual time=0.0292..0.0296 rows=0.915 loops=603)

 -> Select #3 (subquery in condition; dependent)

 -> Aggregate: max(inventory.sc2.counted_at) (cost=0.895 rows=1) (actual time=0.013..0.013 rows=1 loops=1707)

 -> Covering index lookup on sc2 using store_supplier_counted_at (store_id=retail.st.id, supplier_id=713) (cost=0.574 rows=3.21) (actual time=0.00462..0.0114 rows=22 loops=1707)

 -> Index lookup on cl using stock_count_id (stock_count_id=inventory.sc.id) (cost=0.993 rows=1.98) (actual time=0.00626..0.00769 rows=3.3 loops=552)

The whole plan drives from the small set.stores using chain_idfinds 603 rows in 0.19 ms, and every other line is a per-store index seek. The derived table is gone: noMaterialize, no skip scan, no 6.57-million-row temp table. TheSelect #3 (dependent)branch computes each store’sMAX(counted_at)on demand, about 22 index entries per evaluation at roughly 0.01 ms each. On the order of 38,000 index entries read instead of 491,000,000. Check timings against a cold run, since warm-cache numbers flatter any fix; here it is 40 ms warm and 0.22 s cold.

The baseline check, per the previous section:loops=552, the same 552 stock counts. The rollup shows 4 groups and 1,824 rows against the baseline’s 3 and 1,823, and a delta like that has to be explained before shipping, not waved through because the direction is right. It is stable across reruns, and the new group is a single row (Variance/None,row_count=1): one count line landed between the baseline run and this one. The data moved, not the semantics.

## Red flags, for the next plan

What you see
What it means
actual time
 in 
e+6
 ms on one line
The bottleneck (1e+6 ms is about 17 minutes)
rows
 read far above rows kept by the parent line
No usable index for that filter; rows are discarded during the scan
Table scan on <big table>
No index used at all
Materialize ... rows=<millions>
A subquery built a huge temp table before outer filters could apply
skip scan
The index’s leading column is not filtered (leftmost-prefix mismatch)
Estimated 
rows=
 vs actual off by 100x or more
Stale statistics; plain 
EXPLAIN
 estimates are unreliable here
An index that fits the query but is unused or returns 0 rows
Check the column data; an unpopulated column makes the index unusable
never executed
 on join branches
The plan short-circuited; find the deepest line with 
rows=0

The method, compressed: understand what the query is asking and how big the answer should be; runEXPLAIN ANALYZEon a replica; find the one line that owns the time; openSHOW CREATE TABLEand diagnose two things separately, whether the query computes more than it needs (fix: filter the small set first) and whether the filter matches an index’s leading columns (fix: reorder or add an index); then verify correctness against a known-good baseline before trusting the speed.