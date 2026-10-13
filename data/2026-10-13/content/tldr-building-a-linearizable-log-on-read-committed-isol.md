---
title: Building a Linearizable Log on READ COMMITTED Isolation | Materialize
url: https://materialize.com/blog/building-a-linearizable-log-on-read-committed
site_name: tldr
content_file: tldr-building-a-linearizable-log-on-read-committed-isol
fetched_at: '2026-10-13T23:13:36.478435'
original_url: https://materialize.com/blog/building-a-linearizable-log-on-read-committed
date: '2026-10-13'
description: A linearizable metadata log for Materialize, built on PostgreSQL READ COMMITTED isolation, with 3x write throughput and a Lean 4 proof.
tags:
- tldr
---

Materialize's storage layer (persist) requires a metadata store where a small amount of state is maintained for each durable object. In June, a self-managed deployment with many such objects experienced a metastable failure where metadata operation latencies rose from a few milliseconds to thirty seconds, leading to an incident.

Self-managed deployments of Materialize use a PostgreSQL database as the metadata store, which during the incident had most of its connections in a waiting state. The number ofSIReadlocks had grown to hundreds of thousands, an indication that the cost of running queries underSERIALIZABLEisolation was the bottleneck.

This post is an account of how we reworked the implementation of thepersistmetadata store to be able to build a linearizable log with queries running underREAD COMMITTEDisolation. The new implementation was able to sustain three times the write throughput and gracefully degrade even as the load exceeded the capacity of the PostgreSQL database. Additionally, we describe how we gained confidence in its correctness by modeling PostgreSQL'sREAD COMMITTEDbehavior in Lean 4 and proving that the design is linearizable.

## Shards as logs of state diffs

Every durable object in Materialize (a table or a materialized view, for example) is stored bypersistin a unit called a shard. The bulk of a shard's data lives in object storage, while the metadata store holds the shard's state: which data files currently make up the shard, how far it has progressed in time, and which readers are holding on to old data.

The state of a shard can change for many reasons, including new data being committed, a reader advancing its read hold, and others. In a Materialize deployment there can be several independent processes all holding a shard handle for the same shard id. In order to make sure there is exactly one state history for any given shard we coordinate state-changing actions between processes in the usual way:

* For each shard, the metadata store maintains a versioned log of state diffs.
* Each process attempts to extend this log via a compare-and-set operation.
* Each version of the state is assigned a sequence number one higher than the previous one.
* Writers read the latest version, compute the next one, and request that the database append it on the condition that the version it read is still the latest, reading again and retrying if the condition fails.

We call the component that provides this "the consensus implementation", which on PostgreSQL is a single table:

1
 
CREATE
 
TABLE
 consensus (
 
2
 
 shard 
text
 
NOT
 
NULL
,
 
3
 
 sequence_number 
bigint
 
NOT
 
NULL
,
 
4
 
 data 
bytea
 
NOT
 
NULL
,
 
5
 
 
PRIMARY KEY
 (shard, sequence_number)
 
6
 
);
 
 
 Copy
 
sql

persistperforms four operations on it:

* head(shard)returns the row with the largest sequence number.
* scan(shard, from)returns all rows with sequence number at leastfrom, in order.
* compare_and_set(shard, seqno, state_diff)appendsstate_diffifseqnois exactly one past the current head, and returnsCommittedorExpectationMismatch. We abbreviate it as CaS, and refer toseqno - 1, the version the writer believes to be the head, asexpected. The first version of a shard has the sequence number 0 and thereforeexpectedis not defined. This case is covered separately below.
* truncate(shard, cut)deletes all rows with sequence number belowcut. It must not delete the head.

For this scheme to work, the log has to behave as if the operations happened one at a time, in some order consistent with when they were issued. It needs to be linearizable. Two writers must not both succeed at the same sequence number, and no writer may succeed at a sequence number that has already been truncated, since the state it writes there would be built on a version the rest of the system has discarded, and either outcome forks the shard.

## The cost of SERIALIZABLE

Until this work, the consensus queries ran underSERIALIZABLEisolation, which is the simplest way to obtain linearizability in PostgreSQL, since if every transaction is serializable then any interleaving of them behaves like some serial order and the SQL only has to be correct in a serial order. The CaS query we were using would read the current head row and insert the next one if the head matchedexpected. The very first write of a shard was anINSERTguarded by aNOT EXISTSclause asserting that the shard is empty. Both of those queries are correct when run one at a time.

When running underSERIALIZABLEisolation, PostgreSQL doesn't actually run transactions one by one. To increase performance it attempts to run transactions concurrently and detect serializability conflicts using Serializable Snapshot Isolation (SSI). The way this works is by recording every read of a transaction as anSIReadlock on the rows and index pages it visits, and having every write check theSIReadlocks held on the pages it touches to detect read-write conflicts between transactions.

These locks are retained from the time a transaction commits until every transaction that overlapped with it has also finished, because a conflict can still form with a transaction that is still running. On a small, hot table with thousands of concurrent writers, many shards share each index page, so each insert walks the locks of every transaction that recently read the same page.

These charts are from a reproduction on adb.r6g.2xlargeRDS instance, where the load is twenty Materialize clusters, each with six hundred trivial materialized views over an empty table, brought online gradually. What we can observe is that the database sustained the load up to about 4,300 CaS per second, but past that point transactions took long enough that the number of retainedSIReadlocks grew, which made the conflict check on every insert more expensive, which in turn made transactions slower still. Latency reached thirty seconds and throughput fell to a fraction of what the database had sustained moments before, and the system did not recover until we removed load.

This is the failure pattern that Bronson et al. call a metastable failure [1], where a system in a vulnerable state is pushed by a trigger into a bad state and a sustaining effect keeps it there after the trigger is gone, so that recovery requires reducing load well below the level that caused the failure.

The trigger in this case was a transient slowdown of transaction processing that led to the increase in the number ofSIReadlocks, which in turn increased the cost of every other write, turning the transient slowdown into a sustained effect. A transient slowdown can happen due to a transient spike in the load, the database starting concurrent table maintenance (vacuuming), a process pause, etc. TheSIReadlock count is what the paper calls a characteristic metric, a metric that rises with the trigger and does not return to normal until the failure is resolved, and the paper's recommendation is to treat the sustaining effect rather than the trigger, since many triggers lead to the same failure state. In our case a larger database instance or fewer shards would only move the trigger to a different threshold, whereas not relying onSERIALIZABLEeliminates the sustaining effect.

One way to avoidSIReadlocks is to run transactions underREAD COMMITTEDisolation. However, the existing queries were not correct in that mode. UnderREAD COMMITTEDeach statement sees a snapshot taken when it started, but the uniqueness check that anINSERTperforms against the primary key runs against the live index and sees rows committed or deleted after the snapshot, so a single statement can observe a state in itsWHEREclause that no longer holds when itsINSERTruns. As it turns out, it is possible to get a linearizable log behavior underREAD COMMITTEDby carefully adjusting the queries.

## The core shard log invariant

The new design relies on a property of the table that is maintained after every operation:

The sequence numbers present for a shard always form a contiguous interval 
[lo, head]
.

The two state-modifying operations are a compare-and-set and a truncate. A compare-and-set always extends the interval by one at the top. A truncation always removes a prefix, excluding the head. The consequence is that in a contiguous log the condition "expectedis present andexpected + 1is absent" is equivalent to the condition "expectedis the head", the latter being the condition required by the specification of CaS. Therefore under the assumption that the log is a contiguous log we can implement the condition of the specification using aSELECTand a primary key.

Figure 1. The contiguity invariant and the two local checks the CaS statement makes. The CTE checks thatexpectedis present; the primary key checks thatexpected + 1is absent. In a contiguous log the two together are equivalent to "expectedis the head", which is what the specification asks for. Rows belowlohave been truncated; the marker at −1 is never truncated.

This suggests the following CaS query:

1
 
WITH
 expected_row AS (
 
2
 
 
SELECT
 sequence_number FROM consensus
 
3
 
 
WHERE
 shard = $
1
 
AND
 sequence_number = $expected
 
4
 
 FOR KEY SHARE
 
5
 
)
 
6
 
INSERT 
INTO
 consensus (shard, sequence_number, 
data
)
 
7
 
SELECT
 $
1
, $expected + 
1
, $data
 
8
 
FROM expected_row;
 
 
 Copy
 
sql

Theexpected_rowCTE (Common Table Expression) checks that the row the writer intends to build on is present and takes a shared lock on it, and theINSERTaddsexpected + 1if the primary key allows it, so the statement inserts a row in one case only: the predecessor is present and its successor is absent, which by the invariant meansexpectedwas the head. If the CTE finds nothing, theINSERTaffects zero rows, and if the successor is already there the primary key rejects it. Both outcomes are reported asExpectationMismatch.

Concurrent CaS operations fence each other through the primary key alone. Several clients can run the statement for the sameexpectedat once, in which case all of them seeexpected + 1absent in their snapshot and all of them attempt the sameINSERT. The primary key admits one, and the others receive a unique violation, by which time the head has moved andExpectationMismatchis the correct answer for them. TheFOR KEY SHARElock plays no part in this, since it is a shared lock and concurrent CaS operations on the same predecessor all acquire it without blocking one another. Its purpose is to order CaS operations with respect to truncation, which is dealt with later in the post.

The other operations are single statements.headandscanare oneSELECTeach:

1
 
-- head
 
2
 
SELECT
 sequence_number, data 
FROM
 consensus
 
3
 
WHERE
 shard = $
1
 
4
 
ORDER
 
BY
 sequence_number 
DESC
 
LIMIT
 
1
;
 
5
 

 
6
 
-- scan
 
7
 
SELECT
 sequence_number, data 
FROM
 consensus
 
8
 
WHERE
 shard = $
1
 
AND
 sequence_number >= $
from
 
9
 
ORDER
 
BY
 sequence_number 
ASC
 
LIMIT
 $
limit
;
 
 
 Copy
 
sql

A single statement sees one snapshot, so each of them observes the log at one instant.

Finally,truncateis oneDELETEwith anEXISTSguard:

1
 
-- truncate
 
2
 
DELETE
 
FROM
 consensus
 
3
 
WHERE
 shard 
=
 $
1
 
AND
 sequence_number 
>=
 
0
 
AND
 sequence_number 
<
 $cut
 
4
 
 
AND
 
EXISTS
 (
 
5
 
 
SELECT
 
*
 
FROM
 consensus 
WHERE
 shard 
=
 $
1
 
AND
 sequence_number 
>=
 $cut
 
6
 
 );
 
 
 Copy
 
sql

The guard requires a row at or abovecutto survive, so the statement never deletes the head, and deleting a prefix of an interval leaves an interval. Thesequence_number >= 0clause protects a marker row at sequence number-1which is something the first write relies on and is described below.

## Proving linearizability

Changing such a correctness-critical component requires having extremely high confidence that the linearizability guarantees are met. For this reason, we employed formal methods to gain additional confidence in the design by modeling the system underREAD COMMITTEDisolation in Lean 4 and proving that any execution is equivalent to a linearizable one.

The technique we used is called refinement, in which we relate the execution traces of two systems. In this context a system is described by some state and a set of actions that can be performed at any given point. We can then define the set of execution traces of a system as all possible sequences of actions starting from some initial set of states. The goal of refinement is to say that for all execution traces of system A there exists some execution trace of system B that is equivalent in some way. The two systems in our case are an idealized abstract system and the concrete implementation underREAD COMMITTED. Since different shards are completely independent and the linearizability requirements exist only within the sequence of a single shard, we model the two systems as managing a single shard.

The abstract system captures the desired behavior by being as simple as possible. Its state is a map from sequence number to data and the set of actions corresponds directly to the four operations expected by the consensus implementation, performed atomically. Specifically,compare_and_set(seqno, state_diff)succeeds if and only ifseqno - 1is the largest key in the map, or the map is empty andseqnois 0, andtruncate(cut)removes every key belowcut.

The concrete system captures the intricacies that arise by running underREAD COMMITTED. The state of the concrete system is a table of rows and a set of statements in flight. The actions of this system correspond to the actions PostgreSQL can take, like starting a statement by taking a snapshot, performing a write against the live index, consulting row locks, etc.

The main modeling decision is that a CaS statement is no longer one atomic step but two, a step that evaluates the CTE against a snapshot and a later step that performs theINSERTagainst the live index. The model allows for other clients to take any number of steps between these two.

### Relating execution traces

The first step to relating the execution traces is to establish what it means for a pair of states of the two systems to be equivalent. As shown above, the concrete system carries much more detail in its state than the idealized system, like the currently locked rows, so the two states are not directly comparable. We define equivalence through the use of an abstraction functionα, which can transform an instance of the concrete PostgreSQL state to an instance of the idealized system. This function answers the question "What is the abstract state of the shard given this concrete state of the database?". For our case the functionαis simply returning the set of active rows of the table, ignoring all other implementation details like the set of active locks or current set of active transactions.

With this at hand we now have to prove a forward simulation: for every step the concrete system can take, from any reachable state, either the abstract system can take a matching step with the same result, or the concrete step changes nothing observable and the abstract system stays where it is. Taking a snapshot is a step of the second kind, and performing theINSERTis a step of the first kind, being the point at which the CaS takes effect, so the obligation is that it inserts a row when and only when the abstractcompare_and_setwould have succeeded, and inserts nothing when and only when it would have failed.

Figure 2. Forward simulation. Every step of the concrete system either matches an abstract step with the same operation and result, or changes nothing the abstraction functionαcan see. Taking theFOR KEY SHARElock is a stutter; theINSERTis the point at which the CaS takes effect. Client C's CaS withexpected = 2finds no row to lock after the truncation and maps to an abstractcas(3)that returnsMismatch. The locked row is part of the concrete state but not of the abstract one.

If the obligation holds for every step, every concurrent execution of the concrete system corresponds to some sequential execution of the abstract one with the same operations returning the same results, which is the definition of linearizability. The proof quantifies over all clients and all sequence numbers, so there are no bounds on the number of writers or the length of the log.

A key part for successfully proving the simulation is invariants. Since the simulation for theINSERTstep needs to know that "predecessor present, successor absent" implies "predecessor is the head", which is only true if the log is contiguous, contiguity has to be proven as an invariant. After that the invariant is available as a hypothesis in every other proof obligation. Most of the work in a proof of this kind is finding the invariants that discharge the individual steps, and most of the bugs it finds appear as invariants that cannot be preserved.

### Linearizing CaS against truncations

Simulating concurrent CaS operations alone is straightforward. Contiguity is trivially preserved because the only modification is an append athead + 1, which extends the contiguous region. Additionally, theINSERTstep's obligation (i.e., thatexpectedis the head) follows from contiguity and the primary key. Therefore concurrent CaS operations for the sameexpectedall map to a sequence of abstract CaS operations, one that returnsCommittedand the rest returningExpectationMismatch, in the order their inserts reach the index. Note that this argument does not depend at all on the existence of theFOR KEY SHARElock, which never causes CaS queries to wait for one another.

The lock matters oncetruncateis in the model as a step that removes every row belowcutprovided a row at or abovecutexists. Without the shared lock it is possible for a concurrent execution of CaS and truncate operations to produce a non-contiguous shard, breaking the invariant. The failure corresponds to this execution:

1. Client A starts a CaS withexpected = 4. Its snapshot shows row 4 present and row 5 absent, so the CTE produces a row.
2. Before A'sINSERTruns, client B appends 5, 6 and 7.
3. Atruncatewithcut = 7deletes rows 4, 5 and 6.
4. A'sINSERTchecks the live index for row 5, finds nothing, and inserts it.

The table now holds rows 5 and 7, contiguity is broken, and A believes it advanced the head when it wrote a version below one that the rest of the system had already moved past. The primary key behaved correctly, since at the instant of the insert row 5 did not exist. What we would like to be true is that once anexpected_rowis observed it is not deleted until the subsequentINSERThas been executed.

This is what theFOR KEY SHARElock on the predecessor in the CaS query is for. ADELETEtakes aFOR UPDATEstrength lock on each row it removes, which conflicts withFOR KEY SHARE, so atruncatethat would remove the predecessor of an in-flight CaS blocks until that CaS has finished, and at the instant theINSERTruns the predecessor is guaranteed to be present.FOR KEY SHAREis the weakest lock mode that conflicts with aDELETE, and since it is a shared lock, concurrent CaS operations on the same predecessor do not block each other. Serialization of writers remains the job of the primary key; the lock only prevents a truncation from running in the gap thatREAD COMMITTEDisolation allows.

In the model the lock is a set of(client, sequence number)pairs, added when the snapshot step runs and removed when theINSERTstep runs. We then add a precondition to thetruncatestep thatcutmust be at or below every locked sequence number, which is the model's transcription of the lock conflict. With it in place the predecessor's presence at insert time follows directly and the simulation for theINSERTstep holds in the presence of concurrent truncations.

### Linearizing the first write

The CaS query above assumes a predecessor row exists to be checked and locked. The first version of a shard has sequence number 0 and so there is no predecessor, so it needs its own query, and this is the operation that took the most iterations to get right.

The query used underSERIALIZABLEwas:

1
 
INSERT
 
INTO
 consensus 
SELECT
 $
1
, 
0
, $data
 
2
 
WHERE
 
NOT
 
EXISTS
 (
SELECT
 * 
FROM
 consensus 
WHERE
 shard = $
1
)
 
3
 
ON
 CONFLICT 
DO
 NOTHING;
 
 
 Copy
 
sql

The specification says the first write succeeds if and only if the shard is empty, which underSERIALIZABLEtheNOT EXISTSguard implements directly. However, underREAD COMMITTEDthe guard is evaluated against a snapshot, and theINSERTagainst the live index, allowing other steps to run in between. Under this model, this query is incorrect as the following execution is possible:

1. Client A starts the first write for a new shard. Its snapshot is empty, soNOT EXISTSholds.
2. Before A'sINSERTruns, client B performs its own first write for the same shard and commits sequence number 0.
3. Client B appends 1, 2 and 3.
4. Atruncatewithcut = 3deletes rows 0, 1 and 2.
5. A'sINSERTchecks the live index for row 0, finds nothing, and inserts it.

The table now holds rows 0 and 3, and both A and B believe they created the shard. This is the truncation problem from the previous section again, but the previous fix does not apply, since there is no predecessor row for A to lock, and there is nothing else in the table for A to lock either, because at the time of A's snapshot the shard did not exist.

In order to prevent this we need a row to collide with that is never removed by truncation. We take advantage of the fact that PostgreSQL uses signed integers and use the sequence number-1with no data as a marker for "the shard is initialized". We then arrange for the first initialization of a shard to insert both the marker row and the intended first version, which can only succeed once. Additionally, we know truncate will only ever delete non-negative sequence numbers, leaving the marker intact. This gives rise to the following query for the first write:

1
 
INSERT
 INTO consensus (shard, sequence_number, data)
 
2
 
VALUES (
$1
, -
1
, 
''
), (
$1
, 
0
, 
$data
);
 
 
 Copy
 
sql

A stale first writer now always collides with the marker in the live index, no matter what truncation did to sequence number 0 in the meantime, so the resurrection above is no longer possible. This query is correct in a system where every client runs the new set of queries, and is refined once more in the next section, where we consider what happens during an upgrade.

## Reasoning about rollouts

### During the rollout

So far we have only reasoned about the correctness of a system where every client performs the new set of queries. However, that assumption leaves a correctness hole for the real system, since these queries need to be released as a version upgrade of an existing Materialize installation. During that time the old version of Materialize will have to co-exist with the new version to perform a zero-downtime upgrade, and during that window the combination of the two sets of queries needs to be linearizable as well.

Unfortunately, the combination of the old set of queries underSERIALIZABLEwith the new set of queries underREAD COMMITTEDdoes not result in a linearizable system, since SSI only tracks conflicts betweenSERIALIZABLEtransactions and the old first write'sNOT EXISTSguard is blind to aREAD COMMITTEDcreator. To make matters worse, even if both sets of queries run inSERIALIZABLEmode they can still lead to a linearizability violation.

The issue stems from the fact that the new shard initialization is a blind write and so even underSERIALIZABLEit takes noSIReadlocks. The fix is twofold. First we must ensure that during the rollout from the old set of queries to the new set, both clients run underSERIALIZABLE. Secondly, we must ensure that the new initialization query properly participates in the serialization detection by not being a blind write.

To address the first issue, we released the new set of queries with a configuration variable that controls the isolation level in which they run. Since this variable was new and only present in the just-released version, there was no way for users to set it while still running the old environment. This restriction ensured that during the rollout window, both sets of queries would be running underSERIALIZABLEand therefore correctly linearize.

To address the second issue, we had to combine the blind write query with the emptiness check present in the old initial write query, leading to the following query:

1
 
INSERT
 
INTO
 consensus (shard, sequence_number, data)
 
2
 
SELECT
 v.shard, v.sequence_number, v.data
 
3
 
FROM
 (
VALUES
 
 
4
 
 (
$1
::
text
, 
-1
::
bigint
, 
''
::
bytea
), 
 
5
 
 (
$1
::
text
, 
$2
::
bigint
, 
$3
::
bytea
)
 
6
 
) 
AS
 v (shard, sequence_number, data)
 
7
 
WHERE
 
NOT
 
EXISTS
 (
SELECT
 * 
FROM
 consensus 
WHERE
 shard = 
$1
)
 
 
 Copy
 
sql

During the overlap theWHERE NOT EXISTSclause ensures a stale initialization attempt is either rejected by the guard or, if it raced the creation, detected and aborted by PostgreSQL, since the guard is a read that SSI tracks.

### After the rollout

After the rollout is over, we know that the old environment is fenced out, but we're still running underSERIALIZABLEmode until the new feature flag is flipped. Once the operator flips the flag we have a new overlapping period to worry about, since the new setting does not reach every process at the same instant. We must reason about whether new queries underSERIALIZABLEmixed with new queries underREAD COMMITTEDlinearize correctly. Additionally, the database will contain shards that were initialized with the old initialization query. Those shards lack the initialization marker, and so theWHERE NOT EXISTSguard should remain in the query even after everyone has upgraded. Fortunately, the combination of isolation modes in the new queries correctly linearizes and so flipping the flag is safe.

## Results

After rerunning the same benchmark on the same database instance with the new queries, the database sustained the load to the end of the run, reaching about 13,000 CaS per second. We ran out of clusters to add before the database ran out of capacity, so the actual limit is higher. The difference in behavior at the limit is that under the new queries, the cost of an insert does not depend on how many other transactions are in flight or recently finished, so there is no sustaining effect, and when the database reaches its capacity, latency rises with load and falls again when load falls. In the paper's terms, the vulnerable state no longer exists for this failure mode.

## Afterthoughts

The design came down to one invariant: once the sequence numbers are known to be contiguous, a primary key check is sufficient to decide whether a write is at the head, andSERIALIZABLEis no longer needed. The one lock in the design is there for truncation and has no effect on writers. Every operation, including the first write, is a single statement.

Modeling the queries and proving them linearizable gave us a profound level of understanding of and confidence in the design. We were able to quickly test query variations and discover problematic interleavings when proofs failed to go through.

For self-managed deployments of Materialize running against PostgreSQL, the flag ispersist_pg_consensus_read_committed. It defaults to off, and we recommend turning it on once the deployment has finished upgrading to v26.33 or later.

## References

[1] Nathan Bronson, Abutalib Aghayev, Aleksey Charapko, and Timothy Zhu. Metastable Failures in Distributed Systems. InWorkshop on Hot Topics in Operating Systems (HotOS '21), 2021.https://doi.org/10.1145/3458336.3465286

Header photo by Karl Fredrickson onUnsplash.

 
 

Petros Angelatos

 

Member of Technical Staff,Materialize

 

Petros was the former CTO and co-founder of balena.io where he led the engineering team and raised multiple rounds of investment.

 
linkedin
 
x
 
github