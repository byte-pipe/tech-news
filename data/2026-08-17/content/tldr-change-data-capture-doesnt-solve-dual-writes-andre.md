---
title: Change-Data-Capture Doesn’t Solve Dual-Writes - Andreas Andreakis’ blog
url: https://aandreakis.com/posts/change-data-capture-doesnt-solve-dual-writes
site_name: tldr
content_file: tldr-change-data-capture-doesnt-solve-dual-writes-andre
fetched_at: '2026-08-17T19:26:06.815688'
original_url: https://aandreakis.com/posts/change-data-capture-doesnt-solve-dual-writes
date: '2026-08-17'
description: 'Backends typically grow into this pattern: one write happens in one datastore and additional writes are issued downstream. For example: a request arrives, the request handler commits a row to...'
tags:
- tldr
---

Backends typically grow into this pattern: one write happens in one datastore and additional writes are issued downstream. For example: a request arrives, the request handler commits a row to a database, and then updates a search index, refreshes a cache, and calls an external service such as an email provider. One logical change, four systems, four independent calls. The pattern has a name, thedual write, and a decade of literature with a simple message:don't do this.

The standard remedy is just as familiar: write once, to a database, and derive everything else from its transaction log, assuming the the database offers this capability. That is Change-Data-Capture (CDC). Over the last few years CDC has moved from niche to mainstream. Debezium ships connectors for several databases, Flink CDC is widely used, and cloud providers typically offer managed CDC services. At this point, one may have the impression thatdual writes are solved.

However,CDC does not solve dual writesand I just published anew paperthat discusses this.

What CDC actually does is that it moves additional writes one stage downstream and makes themretryable, though usually onlyfor some time. Those are genuinely valuable properties. They are not the same thing as solved, and the difference is where the incidents live.

## The Dual-Write everyone knows

One handler, four systems, no shared transaction. The database commit survives while the other work is never durably recorded as owed.

The naive version can fail in unspectacular ways. Assume the process dies after the database commit and before the index update: the order exists, but search cannot find it. The email call times-out after the commit: retry it and the customer may get two messages; skip it and they may get none. No transaction spans PostgreSQL, Elasticsearch, and an email provider, so all of these outcomes are reachable. The source database can be spotless while the damage sits in systems that do not know what they missed.

Two separate things make this hard. It pays to keep them apart, because CDC fixes one and not the other:

1. Nothing durable records what was supposed to happen.If the process dies halfway through the fan-out, no surviving system may hold a record that writes two through four are still owed. Recovery has nothing to read.
2. The receiving side may not tolerate redelivery.Repeating a version-aware upsert can be harmless. Sending the same email twice is not.

## The CDC answer

The application writes once, and everything else is derived from the transaction log. One arrow leaves the request path — the problem looks solved.

With CDC, the handler writes to the database and is done. The transaction log records committed changes durably and in order. A connector tails that log, and a pipeline later applies the changes to the index, the cache, and the email step.

This genuinely fixes the first problem. The fan-out now starts from a durable, ordered record. If the pipeline dies mid-flight, it can resume from that record. A downstream failure stops being silent divergence and becomeslag— a number you can graph, alert on, and reason about. Together with source ordering and replay, that is the honest core of CDC's value and why the architecture deserves its popularity.

On the whiteboard, the problem now looks gone: One writer, one arrow out of the application.

## Look one stage further

The same fan-out, one stage later. The relay writes a target and separately records its progress: two durable acts, no shared transaction. A dual-write with better tooling.

Follow a change past the log. It still has to land in the search index and still has to reach the email API. Those writes did not disappear. They happen later, issued by the pipeline instead of the request handler, against targets that can still be down and over calls that can still fail. The fan-out moved; it did not dissolve.

Now look closely at the process doing the delivery. For each event it performs two durable acts: it writes the target, and it records its own progress in an offset, checkpoint, or cursor. The target's acceptance and the relay's progress become durable under independent authorities, with no transaction spanning the pair. That is the definition we started with.The standard remedy for dual writes is itself implemented as a dual write.

And when putting checkpointing aside, writes still need to reach downstream systems. The difference is only which process issues the operations. After a write lands on the first database, without CDC: downstream writes are issued from the same process. With CDC: downstream writes happen asynchronously from another process and with added delay due to log propagation.

So, the multi-write has not gone away. It now sits one stage later, behind a replayable log and better operational tooling. Or in other words:dual writes, fundamentally, still occur under CDC.

## Side effects don't forgive

Here is the crash that makes the distinction concrete. The pipeline sends the confirmation email for order 41 and dies before committing the offset that would record it. On restart, the checkpoint still says 40. Should it send 41 again?

There are two possible worlds. In one, the provider accepted the first send before the crash, so re-sending duplicates it. In the other, the crash beat the send, so skipping abandons it. The uncomfortable part (this is a theorem in the paper) is that everything the crashed process can read locally can be identical in both worlds: the source database, the log, and the faithfully maintained checkpoint. The checkpoint is not buggy. It was asked to testify about an event it never observed: whether theother sideaccepted the effect. Only authoritative acceptance evidence at the receiver separates the worlds.

For a search index, the dilemma may be harmless. If delivery is a version-aware, idempotent upsert, redelivery writes the same document and the worlds converge. That is the second problem answered by the target. It is why at-least-once delivery plus idempotent writes works so well for indexes, caches, and replicas — and why CDC canfeelsolved when the whole fan-out has that shape.

An email API absorbs nothing by itself. Neither does a payment capture, a push notification, or any endpoint whose writeisan action. For those targets, the pipeline faces the same choice as the naive handler: retry and risk a duplicate, or skip and risk an omission. If the receiver supports stable idempotency keys, or exposes an authoritative record of accepted requests, redelivery can be made safe under that contract. If it exposes neither, more bookkeeping on the source side cannot manufacture the missing fact. The design has to choose which failure it prefers and document that choice before the incident.

CDC moved the crash window downstream and placed replayable history behind it. For side effects, the decision inside that window remains.

## Retries borrow time from the log

So what did the log actually buy?Time.When the index is down for an hour, events wait, the pipeline retries, and the systems converge. In the naive design, the same failure may create permanent divergence that nobody notices. In the CDC design it creates lag. In production, that difference is enormous.

But the time is borrowed. Transaction logs are operational artifacts with retention policies, not archives. PostgreSQL replication slots may retain WAL indefinitely by default until consumed. MySQL binlogs expire on a configured timer. MongoDB's oplog is capped. SQL Server CDC tables have a cleanup policy. Kafka topics have their own settings so entries may or may not be retained. None of this is negligence. Unbounded retention can threaten the primary system itself, as anyone whose disk filled behind a stalled consumer can confirm. Give a sufficiently high write pressure and a system is eventually forced to evict log entries.

Retries reach only what retention kept. When lag crosses the eviction horizon, events still owed are no longer replayable — and sink-side deduplication evidence can expire in the same way.

This gives retry a horizon. A broken connector over a long weekend, a sink rebuild that takes a week, or a paused pipeline someone forgot can outlive it. Once every replayable copy of an owed event is gone, the connector's cursor may survive, but a cursor only tells you where you stopped; it does not contain the work that used to be there. You are back to missing secondary work with no content from which to reconstruct it, now at pipeline scale.

The paper formalizes this endgame as theTruncation Dilemma. On its constructed states, once retained history hides the old content, recovery cannot always distinguish fabricating work from abandoning work. The important distinction is content versus position: remembering how far the history once extended is not the same as retaining what it contained.

The practical fallback is often a backfill: derive the secondary again from the current table. But a backfill rebuilds state, not history. It can tell a search index that an order is now shipped; it cannot tell you whether the email provider accepted the shipping email last Tuesday. Re-deriving a live table without stopping writes is its own problem, the one myprevious postand the DBLog papers are about.

Evidence can expire on the receiving side too. Idempotency keys and accepted-request records are usually retained for finite periods;Stripe’s API, for example, uses a 24-hour idempotent replay window. A retry that arrives after the receiver has forgotten the key can be accepted as new work. Log retention on the left, deduplication memory on the right: the usable recovery guarantee lasts no longer than the shorter of the two.

## What CDC actually buys

None of this is an argument against CDC. CDC ismy corner.This is an argument against assuming that dual writes are fixed. The honest accounting looks like this:

* The application-tier dual write is genuinely gone: one writer, one commit, with downstream work derived from committed history.
* Downstream failure becomes lag: visible, measurable, and alertable instead of silent divergence.
* Redelivery is absorbable where the target contract makes repeat writes idempotent.
* Side-effecting deliveries retain the dual-write decision unless the receiver cooperates through idempotency or authoritative acceptance evidence.
* Every replay and deduplication guarantee holds within an evidence window.

In one sentence:CDC converts an atomicity problem you cannot solve into a delivery problem you can operate.

## If you have Dual-Writes (with or without CDC)

1. Sort targets into stores and actions.Stores hold state you can overwrite: indexes, caches, replicas. Actions create effects you cannot un-perform: emails, charges, webhooks. The original ambiguity is sharpest at the actions.
2. Make store writes idempotent and version-aware.Upsert by stable key, carry the source coordinate (LSN, GTID, offset), and reject stale applications. Derive event identity once at the source; content-derived keys can merge two legitimately identical events.
3. For actions, negotiate with the receiver — or choose your failure.Use stable idempotency keys or queryable acceptance records where available. Otherwise decide whether that endpoint prefers duplicates or omissions, and write the decision down.
4. Treat lag versus retention as an SLO.Alert on headroom — the time before retention reaches the oldest undelivered event — not just on current lag. Size both replay and deduplication windows for the longest outage you promise to survive.
5. Have a backfill plan for the day history is gone.Know which targets can be rebuilt from current source state without stopping traffic, and which historical effects cannot.
6. Watch the quiet half.Duplicates are loud; omissions are silent. Track committed-but-unaccepted work per target. “No pipeline errors” is not the same as “nothing was lost.”

## The Paper

Most of the advice above is folklore — good folklore, a decade old, and largely correct. What has been missing is precision about when it works: which recovery decisions are impossible from which evidence, which escapes work under which premises, what can make a correct answer stale, and how the guarantee expires when its evidence does. That is what the new paper supplies:Machine-Checked Dual-Write Recovery from a Committed Log.

The paper proves the two-world checkpoint argument for a deterministic deliver-then-checkpoint protocol, gives the conditional escape through the sink's durable accepted record, and studies two additional races: old requests that remain in flight and overlapping recoverers. It states the corresponding fencing obligations and their cost. It also makes precise when at-least-once delivery plus an absorbing deduplicating view yields payload-counted exactly-once, and how bounded deduplication memory or truncated source history ends that guarantee. The theory is machine-checked in Isabelle/HOL, with the premises stated rather than smuggled in, and the practitioner section turns the results into questions you can use in a design review.

The mental model to keep is small. A dual write is not solved until the destination can safely absorb or reject a redelivery, and the evidence needed for that decision survives long enough. CDC gives you committed history, ordering, retries, observable lag, and time. The last step — making the destination safe to write twice — was always yours.