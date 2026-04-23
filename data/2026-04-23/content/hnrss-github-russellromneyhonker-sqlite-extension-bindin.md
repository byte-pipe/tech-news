---
title: 'GitHub - russellromney/honker: SQLite extension + bindings for Postgres NOTIFY/LISTEN semantics with durable queues, streams, pub/sub, and scheduler · GitHub'
url: https://github.com/russellromney/honker
site_name: hnrss
content_file: hnrss-github-russellromneyhonker-sqlite-extension-bindin
fetched_at: '2026-04-23T20:06:05.668414'
original_url: https://github.com/russellromney/honker
date: '2026-04-23'
description: SQLite extension + bindings for Postgres NOTIFY/LISTEN semantics with durable queues, streams, pub/sub, and scheduler - russellromney/honker
tags:
- hackernews
- hnrss
---

russellromney

 

/

honker

Public

* NotificationsYou must be signed in to change notification settings
* Fork4
* Star236

 
 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

138 Commits
138 Commits
.github/
workflows
.github/
workflows
 
 
assets
assets
 
 
bench
bench
 
 
honker-core
honker-core
 
 
honker-extension
honker-extension
 
 
packages
packages
 
 
site @ 1220967
site @ 1220967
 
 
tests
tests
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
.python-version
.python-version
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
ROADMAP.md
ROADMAP.md
 
 
demo.py
demo.py
 
 
pyproject.toml
pyproject.toml
 
 
test_integration.py
test_integration.py
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

# honker

honkeris a SQLite extension + language bindings that add Postgres-styleNOTIFY/LISTENsemantics to SQLite, with built-in durable pub/sub, task queue, and event streams, without client polling or a daemon/broker. Any language that canSELECT load_extension('honker')gets the same features.

honker ships as aRust crate(honker, plushonker-core/honker-extension), aSQLite loadable extension, and language packages: Python (honker), Node (@russellthehippo/honker-node), Bun (@russellthehippo/honker-bun), Ruby (honker), Go, Elixir, C++. The on-disk layout is defined once in Rust; every binding is a thin wrapper around the loadable extension.

honkerworks by replacing a polling interval with event notifications on SQLite's WAL file, achieving push semantics and enabling cross-process notifications with single-digit millisecond delivery.

Experimental. API may change.

SQLite is increasingly the database for shipped projects. Those inevitably require pubsub and a task queue. The usual answer is "add Redis + Celery." That works, but it introduces a second datastore with its own backup story, a dual-write problem between your business table and the queue, and the operational overhead of running a broker.

honker takes the approach that if SQLite is the primary datastore, the queue should live in the same file. That meansINSERT INTO ordersandqueue.enqueue(...)commit in the same transaction. Rollback drops both. The queue is just rows in a table with a partial index.

Prior art:pg_notify(fast triggers, no retry/visibility),Huey(SQLite-backed Python),pg-bossandOban(the Postgres-side gold standards we're chasing on SQLite). If you already run Postgres, use those, as they are excellent.

## At a glance

import
 
honker

db
 
=
 
honker
.
open
(
"app.db"
)

emails
 
=
 
db
.
queue
(
"emails"
)

# Enqueue

emails
.
enqueue
({
"to"
: 
"alice@example.com"
})

# Consume (worker process)

async
 
for
 
job
 
in
 
emails
.
claim
(
"worker-1"
):
 
send
(
job
.
payload
)
 
job
.
ack
()

Any enqueue can be atomic with a business write. Rollback drops both.

with
 
db
.
transaction
() 
as
 
tx
:
 
tx
.
execute
(
"INSERT INTO orders (user_id) VALUES (?)"
, [
42
])
 
emails
.
enqueue
({
"to"
: 
"alice@example.com"
}, 
tx
=
tx
)

## Features

Today:

* Notify/listen across processes on one.dbfile
* Work queues with retries, priority, delayed jobs, and a dead-letter table
* Any send can be atomic with your business write (commit together or roll back together)
* Single-digit millisecond cross-process reaction time, no polling
* Handler timeouts, declarative retries with exponential backoff
* Delayed jobs, task expiration, named locks, rate-limiting
* Crontab-style periodic tasks with a leader-elected scheduler
* Opt-in task result storage (enqueuereturns an id, worker persists the
return value, caller awaitsqueue.wait_result(id))
* Durable streams with per-consumer offsets and configurable flush interval
* SQLite loadable extension so any SQLite client can read the same tables
* Bindings: Python, Node.js, Rust, Go, Ruby, Bun, Elixir

Deliberately not built: task pipelines/chains/groups/chords, multi-writer replication, workflow orchestration with DAGs.

## Quick start

### Python: queue (durable at-least-once work)

pip install honker

import
 
honker

db
 
=
 
honker
.
open
(
"app.db"
)

emails
 
=
 
db
.
queue
(
"emails"
)

with
 
db
.
transaction
() 
as
 
tx
:
 
tx
.
execute
(
"INSERT INTO orders (user_id) VALUES (?)"
, [
42
])
 
emails
.
enqueue
({
"to"
: 
"alice@example.com"
}, 
tx
=
tx
) 
# atomic with order

# Then in a worker, do: 

async
 
for
 
job
 
in
 
emails
.
claim
(
"worker-1"
): 
# wakes on any WAL commit

 
try
:
 
send
(
job
.
payload
); 
job
.
ack
()
 
except
 
Exception
 
as
 
e
:
 
job
.
retry
(
delay_s
=
60
, 
error
=
str
(
e
))

claim()is an async iterator. Each iteration is oneclaim_batch(worker_id, 1). Wakes on any WAL commit, falls back to a 5 s paranoia poll only if the WAL watcher can't fire. For batched work, callclaim_batch(worker_id, n)explicitly and ack withqueue.ack_batch(ids, worker_id). Defaults: visibility 300 s.

### Python: tasks (Huey-style decorators)

If you want a function call to turn into an enqueued job without wrappingqueue.enqueueby hand:

@
emails
.
task
(
retries
=
3
, 
timeout_s
=
30
)

def
 
send_email
(
to
: 
str
, 
subject
: 
str
) 
->
 
dict
:
 ...
 
return
 {
"sent_at"
: 
time
.
time
()}

# Caller

r
 
=
 
send_email
(
"alice@example.com"
, 
"Hi"
) 
# enqueues, returns a TaskResult

print
(
r
.
get
(
timeout
=
10
)) 
# blocks until worker runs it

Worker side, either in-process or as its own process:

python -m honker worker myapp.tasks:db --queue=emails --concurrency=4

Auto-name is{module}.{qualname}(Huey/Celery convention). Explicit names with@emails.task(name="...")are recommended in prod so renames don't orphan pending jobs. Periodic tasks use@emails.periodic_task(crontab("0 3 * * *")). Full details inpackages/honker/examples/tasks.py.

### Python: stream (durable pub/sub)

stream
 
=
 
db
.
stream
(
"user-events"
)

with
 
db
.
transaction
() 
as
 
tx
:
 
tx
.
execute
(
"UPDATE users SET name=? WHERE id=?"
, [
name
, 
uid
])
 
stream
.
publish
({
"user_id"
: 
uid
, 
"change"
: 
"name"
}, 
tx
=
tx
)

async
 
for
 
event
 
in
 
stream
.
subscribe
(
consumer
=
"dashboard"
):
 
await
 
push_to_browser
(
event
)

Each named consumer tracks its own offset in the_honker_stream_consumerstable.subscribereplays rows past the saved offset, then transitions to live delivery on WAL wake. The iterator auto-saves offset at most every 1000 events or every 1 second (whichever first) so a high-throughput stream doesn't hammer the single-writer slot. Override withsave_every_n=/save_every_s=, or set both to 0 to disable auto-save and callstream.save_offset(consumer, offset, tx=tx)yourself (atomic with whatever you just did in that tx). At-least-once: a crash re-delivers in-flight events up to the last flushed offset.

### Python: notify (ephemeral pub/sub)

async
 
for
 
n
 
in
 
db
.
listen
(
"orders"
):
 
print
(
n
.
channel
, 
n
.
payload
)

with
 
db
.
transaction
() 
as
 
tx
:
 
tx
.
execute
(
"INSERT INTO orders (id, total) VALUES (?, ?)"
, [
42
, 
99.99
])
 
tx
.
notify
(
"orders"
, {
"id"
: 
42
})

Listeners attach at currentMAX(id); history is not replayed. Usedb.stream()if you need durable replay. The notifications table is not auto-pruned. Calldb.prune_notifications(older_than_s=…, max_keep=…)from a scheduled task. Task payloads have to be valid JSON so a Python writer and Node reader can share a channel.

### Node.js

const
 
{
 open 
}
 
=
 
require
(
'@russellthehippo/honker-node'
)
;

const
 
db
 
=
 
open
(
'app.db'
)
;

// Atomic: business write + notify commit together

const
 
tx
 
=
 
db
.
transaction
(
)
;

tx
.
execute
(
'INSERT INTO orders (id) VALUES (?)'
,
 
[
42
]
)
;

tx
.
notify
(
'orders'
,
 
{
 
id
: 
42
 
}
)
;

tx
.
commit
(
)
;

// Listen wakes on WAL commits, filters by channel

for
 
await
 
(
const
 
n
 
of
 
db
.
listen
(
'orders'
)
)
 
{

 
handle
(
n
.
payload
)
;

}

### SQLite extension (any SQLite 3.9+ client)

.load .
/
libhonker_ext

SELECT
 honker_bootstrap();

INSERT INTO
 _honker_live (queue, payload) 
VALUES
 (
'
emails
'
, 
'
{"to":"alice"}
'
);

SELECT
 honker_claim_batch(
'
emails
'
, 
'
worker-1
'
, 
32
, 
300
); 
--
 JSON array

SELECT
 honker_ack_batch(
'
[1,2,3]
'
, 
'
worker-1
'
); 
--
 DELETEs; returns count

SELECT
 honker_sweep_expired(
'
emails
'
); 
--
 count moved to dead

SELECT
 honker_lock_acquire(
'
backup
'
, 
'
me
'
, 
60
); 
--
 1 = got it, 0 = held

SELECT
 honker_lock_release(
'
backup
'
, 
'
me
'
); 
--
 1 = released

SELECT
 honker_rate_limit_try(
'
api
'
, 
10
, 
60
); 
--
 1 = under, 0 = at limit

SELECT
 honker_rate_limit_sweep(
3600
); 
--
 drop windows >1h old

SELECT
 honker_cron_next_after(
'
0 3 * * *
'
, unixepoch()); 
--
 unix ts of next fire

SELECT
 honker_scheduler_register(
'
nightly
'
, 
'
backups
'
,
 
'
0 3 * * *
'
, 
'
"go"
'
, 
0
, 
NULL
); 
--
 register periodic task

SELECT
 honker_scheduler_tick(unixepoch()); 
--
 JSON: fires due

SELECT
 honker_scheduler_soonest(); 
--
 min next_fire_at

SELECT
 honker_scheduler_unregister(
'
nightly
'
); 
--
 1 = deleted

SELECT
 honker_stream_publish(
'
orders
'
, 
'
k
'
, 
'
{"id":42}
'
); 
--
 returns offset

SELECT
 honker_stream_read_since(
'
orders
'
, 
0
, 
1000
); 
--
 JSON array

SELECT
 honker_stream_save_offset(
'
worker
'
, 
'
orders
'
, 
42
); 
--
 monotonic upsert

SELECT
 honker_stream_get_offset(
'
worker
'
, 
'
orders
'
); 
--
 offset or 0

SELECT
 honker_result_save(
42
, 
'
{"ok":true}
'
, 
3600
); 
--
 save w/ 1h TTL

SELECT
 honker_result_get(
42
); 
--
 value or NULL

SELECT
 honker_result_sweep(); 
--
 prune expired

SELECT
 notify(
'
orders
'
, 
'
{"id":42}
'
);

The extension shares_honker_live,_honker_dead, and_honker_notificationswith the Python binding, so a Python worker can claim jobs any other language pushed via the extension. Schema compatibility is pinned bytests/test_extension_interop.py.

## Design

This repo includes thehonkerSQLite loadable extension and bindings for Python, Node, Rust, Go, Ruby, Bun, and Elixir.

For most applications,SQLite alone is sufficient. There are already great libraries that leverage SQLite for durable messaging.Hueyis the one honker draws the most from. This project is inspired by it and seeks to do something similar across languages and frameworks by moving package logic into a SQLite extension.

For Postgres-backed apps,pg_notify+pg-bossorObanis the equivalent. This library is for apps where SQLite is the primary datastore.

The extension has three primitives that tie it together: ephemeral pub/sub (notify()), durable pub/sub with per-consumer offsets (stream()), at-least-once work queue (queue()). All three are INSERTs inside your transaction, which lets a task "send" be atomic with your business write, and rollback drops everything.

The explicit goal is to doNOTIFY/LISTENsemantics without constant polling, to achieve single-digit ms reaction time. If you use your app's existing SQLite file containing business logic, it will notify workers on every WAL commit. This means that most triggers will not result in anything happening: instead, workers just read the message/queue with no result. This "overtriggering" is on purpose and is the tradeoff for push semantics and fast reaction time.

### WAL-only by design

honker requiresjournal_mode = WALon every database it manages.honker_bootstrap()refuses to run on a file-backed DB that isn't in WAL mode, and the language bindings setPRAGMA journal_mode = WALin their default open path.

* Workers hold open read views (WAL subscription channels, listener iterators) for their whole lifetime. In DELETE / TRUNCATE modes, writers take an EXCLUSIVE lock; every active reader blocks until release. A single worker actively claiming would serialize everyenqueue()/notify()in the system behind it. WAL lets readers and writers coexist.
* The.db-walsidecar grows on every commit and only shrinks at checkpoint. Stat-polling it gives a monotonic, unambiguous change signal. The rollback-journal sidecar (.db-journal) in DELETE mode appears mid-transaction and vanishes on commit, making it a poor stat-poll target.
* Withwal_autocheckpoint = 10000, WAL performs one fsync per 10k pages instead of per-commit. Most of the throughput win comes from that.

If you need a SQLite database that never enters WAL mode (e.g. for a backup target, or to avoid the.db-wal/.db-shmsidecars in a shared filesystem), honker is not the right tool. Use plain SQLite and live without the NOTIFY/LISTEN semantics.

The library/extension is a small coordination layer built on the properties of SQLite and single-server architecture.

* One.db+ one.db-walis the entire system. You get every benefit of SQLite (embedded, local, durable, snapshot-able) that your app already uses.
* WAL mode gives one writer and concurrent readers. Claim is oneUPDATE … RETURNINGvia a partial index, ack is oneDELETE.
* The WAL file grows on every commit, so(size, mtime)is the cross-process commit signal.
* SQLite has no wire protocol. Consumers must initiate reads; server-push is impossible. Wake signal = file change →SELECT.
* Transactions are cheap, so jobs, events, and notifications are rows in the caller's openwith db.transaction()block in an "outbox"-type pattern.
* We usestat(2)cross-platform instead of the technically betterFSEvents/inotify/kqueue. FSEvents drops same-process writes on macOS, meaning a listener and enqueuer in the same Python process would never see each other.stat(2)works identically on Linux/macOS/Windows at ~1 ms granularity for negligible CPU. Cost: ~0.5 ms of latency vs kernel notifications.
* Single machine, single writer. SQLite's locking is designed for a single host. Two servers writing one.dbover NFS will corrupt it. Shard by file, or switch to Postgres.

## Architecture

### Wake path

* Onestat(2)thread perDatabase, polls.db-walevery 1 ms
* (size, mtime)change → fan out a tick to each subscriber's bounded channel
* Each subscriber runsSELECT … WHERE id > last_seenagainst a partial index, yields rows, returns to wait
* 100 subscribers = 1 stat thread
* Idle listeners run zero SQL queries

Idle cost is a singlestat(2)per millisecond per database. Listener count scales for free because the wake signal is a file stat instead of a polling query.

SharedWalWatcher(inhonker-core) owns the poll thread and fans out to N subscribers via boundedSyncSender<()>channels keyed by subscriber id. Eachdb.wal_events()call registers a subscriber and returns a handle whoseDropauto-unsubscribes, so a dropped listener causes the bridge thread'srx.recv() -> Errand exits cleanly.

### Queue schema

* _honker_live: pending + processing rows
* Partial index:(queue, priority DESC, run_at, id) WHERE state IN ('pending','processing')
* Claim = oneUPDATE … RETURNINGvia that index
* Ack = oneDELETE
* Retry-exhausted →_honker_dead(never scanned by claim path)

Partial-index on state means the claim hot path is bounded by theworking-setsize rather than thehistorysize. A queue with 100k dead rows claims as fast as a queue with zero.

### Claim iterator

* async for job in q.claim(id)yields one job at a time viaclaim_batch(id, 1)
* Job.ack()is oneDELETEin its own transaction. Return is an honest bool:Trueiff the claim was still valid,Falseif the visibility window elapsed and another worker reclaimed.
* Wakes on WAL commit from any process; a 5 s paranoia poll is the only fallback.

For batched work, callclaim_batch(worker_id, n)directly and ack withqueue.ack_batch(ids, worker_id). The library doesn't hide batching behind the iterator. The per-tx cost and the at-most-once visibility semantics are easier to reason about when the API doesn't try to be clever.

### Transactional coupling

* notify()is a SQL scalar function registered on the writer connection
* INSERTs into_honker_notificationsunder the caller's open tx
* queue.enqueue(…, tx=tx)andstream.publish(…, tx=tx)do the same
* Rollback drops the job/event/notification with the rest of the tx

This is the transactional outbox pattern, by default, without a library to install. Business write and side-effect enqueue commit or roll back together. There is no separate dispatch table and no separate dispatcher process: the side-effect rowisthe committed row, and any process watching the WAL picks it up within ~1 ms.

### Over-triggering quickly is better than over-triggering from polling

* A WAL change wakeseverysubscriber on thatDatabase, not just the ones whose channel committed
* Each wasted wake = one indexed SELECT (microseconds)
* A missed wake = a silent correctness bug

The library prefers waking ten listeners that don't care over missing one that does. Channel filtering happens in theSELECTpath instead of the trigger notification.Many small queries are efficient in SQLite.

### Retention

* Queue jobs persist until ack; retry-exhausted rows move to_honker_dead
* Stream events persist; each named consumer tracks its own offset
* Notify is fire-and-forget and not auto-pruned

The caller chooses retention per primitive.db.prune_notifications(older_than_s=…, max_keep=…)is a tool you invoke. This keeps retention policy visible in the caller's code instead of inherited from a library default.

## Crash recovery

* Rollback drops jobs/events/notifications with your business write (SQLite ACID).
* SIGKILL mid-tx is safe. WAL rollback on next open leaves no stale state. Verified intests/test_crash_recovery.py(subprocess killed pre-COMMIT,PRAGMA integrity_check == 'ok', fresh notifies still flow).
* If a worker crashes mid-job, the claim expires aftervisibility_timeout_s(default 300 s) and another worker reclaims.attemptsincrements. Aftermax_attempts(default 3), the row moves to_honker_dead.
* Listeners offline during a prune miss the pruned events. For durable replay, usedb.stream(), which tracks per-consumer offsets.

## Wiring into your web framework

Honker ships no framework plugins. API is small and the integration is a few lines of glue:

# FastAPI: enqueue in a request, run workers via lifespan.

@
app
.
on_event
(
"startup"
)

async
 
def
 
_start_workers
():
 
async
 
def
 
worker_loop
():
 
async
 
for
 
job
 
in
 
db
.
queue
(
"emails"
).
claim
(
"worker"
):
 
await
 
honker
.
_worker
.
run_task
(
 
job
, 
send_email
, 
timeout
=
30
, 
retries
=
3
, 
backoff
=
2.0

 )
 
app
.
state
.
_worker
 
=
 
asyncio
.
create_task
(
worker_loop
())

@
app
.
post
(
"/orders"
)

async
 
def
 
create_order
(
order
: 
dict
):
 
with
 
db
.
transaction
() 
as
 
tx
:
 
tx
.
execute
(
"INSERT INTO orders (user_id) VALUES (?)"
, [
order
[
"user_id"
]])
 
db
.
queue
(
"emails"
).
enqueue
({
"to"
: 
order
[
"email"
]}, 
tx
=
tx
)
 
return
 {
"ok"
: 
True
}

SSE endpoints are ~30 lines ofasync def stream(...): yield f"data: ...\n\n"overdb.listen(channel)ordb.stream(name).subscribe(...). For Django/Flask, run the worker as a dedicated CLI process (same pattern as Celery/RQ).

## Performance

Handles thousands of messages per second on a modern laptop, with cross-process wake latency bounded by the 1 ms stat-poll cadence (~1–2 ms median on M-series). Runbench/wake_latency_bench.pyandbench/real_bench.pyto measure on your hardware.

## Development

Layout:

honker-core/ # Rust rlib shared across all bindings (in-tree, published on crates.io)
honker-extension/ # SQLite loadable extension (cdylib, published on crates.io)
packages/
 honker/ # Python package (PyO3 cdylib + Queue/Stream/Outbox/Scheduler)
 honker-node/ # napi-rs Node.js binding [git submodule]
 honker-rs/ # ergonomic Rust wrapper [git submodule]
 honker-go/ # Go binding [git submodule]
 honker-ruby/ # Ruby binding [git submodule]
 honker-bun/ # Bun binding [git submodule]
 honker-ex/ # Elixir binding [git submodule]
 honker-cpp/ # C++ binding [git submodule]
tests/ # integration tests (cross-package)
bench/ # benches
site/ # honker.dev (Astro) [git submodule]

Each binding repo is published independently (PyPI / npm / crates.io / Hex / RubyGems) and pinned here as a git submodule;honker-core+honker-extensionlive in-tree since they're the shared foundation every binding depends on. Clone withgit clone --recursiveor rungit submodule update --init --recursiveafter a normal clone.

make 
test
 
#
 default: rust + python + node (fast, ~10s)

make test-python-slow 
#
 soak + real-time cron tests (~2 min)

make test-all 
#
 everything including slow marks

make build 
#
 PyO3 maturin develop + loadable extension

python bench/wake_latency_bench.py --samples 500
python bench/real_bench.py --workers 4 --enqueuers 2 --seconds 15
python bench/ext_bench.py

### Coverage

One-time:make install-coverage-deps(installscoverage.py+cargo-llvm-cov).

make coverage 
#
 both HTML reports into coverage/

make coverage-python 
#
 honker python paths

make coverage-rust 
#
 honker-core Rust unit tests

Python coverage reflects the full honker test suite (~92% ofpackages/honker/). Rust coverage reflects onlycargo test. Manyhonker_ops.rspaths (honker_enqueue,honker_claim_batch, etc.) are only exercised via the Python test suite and won't show up in the Rust report. Combined cross-language coverage is non-trivial (LLVM profile-data merging across PyO3 boundaries) and is deferred.

## License

Apache 2.0. SeeLICENSE.

## About

SQLite extension + bindings for Postgres NOTIFY/LISTEN semantics with durable queues, streams, pub/sub, and scheduler

honker.dev

### Resources

 Readme

 

### License

 Apache-2.0 license
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

236

 stars
 

### Watchers

0

 watching
 

### Forks

4

 forks
 

 Report repository

 

## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python71.0%
* Rust27.9%
* Makefile1.1%