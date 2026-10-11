---
title: A versioned filesystem for disposable sandboxes
url: https://www.shayon.dev/post/2026/283/versioned-filesystem-for-disposable-sandboxes
site_name: tldr
content_file: tldr-a-versioned-filesystem-for-disposable-sandboxes
fetched_at: '2026-10-12T06:00:31.512823'
original_url: https://www.shayon.dev/post/2026/283/versioned-filesystem-for-disposable-sandboxes
date: '2026-10-12'
published_date: '2026-10-10'
description: How every 3B workflow step gets a durable, versioned filesystem, from a gVisor gofer that hands the sandbox a local file to a storage engine with snapshots, forks, an LSM index, and S3 as a cold tier.
tags:
- tldr
---

live
draft
sandbox 1
$ python sync_leads.py
sandbox 2
$ node enrich.js
sandbox 3, days later
$ python report.py
41
42
43
44
reads 43
branch/main
fork, nothing copied
branch/draft
a sandbox on the draft
$ python score_v2.py
Each sandbox commits a new snapshot to the volume, live keeps moving forward, and a draft forks off snapshot 43 without copying anything.

At Tines we built3Baround a simple idea, which is that every step in a workflow is a computer. A step’s code, whether a person or an agent wrote it, runs inside a fresh Linux sandbox that gets its credentials through a proxy, does its work, and then gets thrown away so no leftover state can cause security issues later.

But as you start doing more with these steps, you realize pretty quickly that you need somewhere to keep state, and that was clear to us from the start. Today, 3B customers clone repositories to run analysis, keep SQLite databases of their Salesforce leads, and store inbound webhooks in DuckDB so other workflows can search them later.

So every step gets a filesystem that outlives its sandbox, and we made that filesystem versioned, which turned out to matter a lot more than we expected. IOW, a sandbox run and the changes it makes to its files behave like a database transaction, where either all of it lands or none of it does. So you can build a workflow with an agent on a draft branch without touching the data live depends on, and nobody else sees a step’s changes until it finishes successfully.

In this post, step and sandbox mean the same thing, since every step runs in its own sandbox.

Before getting into it, it helps to know the three parts this post mentions often. The step’s code runs in the sandbox, and anything it does with files goes to Nest, a small gVisor gofer, which is the file server extension we wrote that sits just outside the sandbox. Underneath Nest is Spongeblob (aka Blobstore), the storage engine we wrote to hold every volume and, when S3 is available, copy it there for recovery and eviction.

sandbox
the program
inside gVisor
Nest
our gVisor gofer
pins one snapshot
copies open files
for this step only
Spongeblob
our storage engine
keeps every volume
on local disk
S3
recovery copy
and cold storage
LisaFS
fd
HTTP
later
A step’s code runs in the sandbox, Nest serves its files from just outside, and Spongeblob stores every volume and copies it to S3 in the background when S3 is available.

## The wish list

Before we wrote any code, we had a short list of things this system had to get right, and every decision later in this post traces back to one of them.

It had to behave like a real POSIX filesystem.Git, SQLite, compilers, andpipall expect a directory and lean onmmap,fsync, and renames, and none of them are going to adopt our SDK.

Nothing could live on the machine running the step,since the next step might run days later somewhere else.

The hot path had to be fast and local.We wanted a 128 KB write to be durable in 2–4 ms in the typical case, and since SQLite does a ton of small writes, putting a network round trip under each one, which is what a network filesystem on top of S3 would do, made that budget hard to hit.

Steps run in parallel,and two steps writing to the same volume should never corrupt it or quietly overwrite each other’s work.

It had to work without S3,because 3B also runs self-hosted, where S3 is not always available.

And it had to stay simple.Every extra moving part is one more thing to keep consistent after a crash, so we wanted one durable log, one owner per disk, and no separate database or consensus system to run, and we only added complexity where one of the requirements above forced it, because let’s admit it, there’s nothing simple about keeping data in sync, whether it’s a single writer, an LSM on S3, or, god forbid, a quorum-based system.

## What a step sees

A step declares a volume with oneVOLUMEline in its Dockerfile, and the volume gets mounted into the sandbox as a directory at/storage/<name>. It can be read-only or read-write, scoped to a branch or a single run, and shared between concurrent writers or taken in turns. There’s nothing else to the interface, and when the step starts, it gets pinned to one version of the volume for the whole run.

## Opening a file

The sandbox isgVisor, which intercepts every system call, and anything that touches/storagegets handed to Nest. We could have run a FUSE filesystem instead, but gVisor already sends file operations to a gofer, so extending our own meant no extra layer in between, and it lets Nest hand the sandbox a real file descriptor so reads and writes hit a local file directly instead of going through a FUSE daemon on every call.

Laziness is a core property of the system (and of me, jk).

Opening a volume doesn’t download it, since Nest looks things up lazily as the program walks the tree. When the program opens a file, Nest copies it into a scratch file in memory on the host and hands the sandbox a file descriptor for it. From then on, reads, writes, andmmapall hit that local file at memory speed, and only control operations like open, rename, and list cross the sandbox boundary.

sandbox
the program
open("/storage/app/events.db")
local tmpfs file
reads, writes, and mmap stay here
Nest
when the program opens a file, Nest
1. finds it in the pinned snapshot
2. copies it into a tmpfs file
3. hands that file descriptor over
4. keeps track of what changes
Spongeblob
holds the committed
version of the file
LisaFS
fd
Opening a file goes over LisaFS to Nest, which copies the committed file into a local tmpfs file and hands back a file descriptor, so reads and writes stay local.

That does mean opening a file copies the whole thing. We tried fetching every file on demand instead, but the kernel’s page cache kept beating our proxy, because real programs reread the same pages constantly. So we’re now experimenting with a split, where small files still get copied in up front and keep the fast local path, while large files skip the copy and fetch only the blocks a program actually touches.

Nest also tracks what changed, including creates, renames, deletes, and the parts of each file that were written, and it fingerprints file chunks at open so it can catch changes made through a sharedmmap. Anfsyncinside a step only flushes the local copy, because durability comes when the step finishes. IOW, when a sandbox crashes, OOMs, or exits 1, its changes are thrown away and the volume doesn’t move. Throwing them away is the default today, and if we ever need it, we could add dedicated mounts that make a step’s changes visible while it’s still running.

sandbox
events.db
thrown away
reports/today.json
thrown away
exit 1
Spongeblob
42
branch/main
pinned to 42
pointer still at 42
A sandbox that crashes or exits 1 publishes nothing, so its local copies are thrown away and the branch still points at snapshot 42.

## Every step is a commit

A volume is a series of snapshots plus one small pointer that says which snapshot is current, and snapshots never change once they’re written. When a step succeeds, Nest uploads whatever changed, and Spongeblob builds a new snapshot on top of the current one and moves the pointer forward.

If you squint enough, it’s somewhat like Git, where a commit records the state of the whole tree, except every successful step makes one automatically. It also borrows from multiversion concurrency control, so if someone publishes snapshot 43 while you’re still reading 42, you keep reading 42, and readers and writers never wait on each other.

sandbox
events.db
changed locally
reports/today.json
changed locally
exit 0
Spongeblob
42
43
branch/main
pinned to 42
changed blocks
pointer 42 → 43
A successful step uploads its changed blocks, and Spongeblob builds snapshot 43 on top of 42 and moves the branch pointer in one swap.

Mooooo. I mean Hello COW.

Keeping every version around would be expensive if each snapshot were a full copy, so we use copy-on-write (COW, you get it). A new snapshot only rewrites the parts of the tree that changed, so updating one file in a huge volume writes a few small nodes and shares everything else.

snapshot 42
/src
/data
main.py
util.py
notes.md
events.db
snapshot 43
/data
events.db
written: 3 nodes, shared: 4 nodes
Changing events.db writes a new leaf, a new /data node, and a new root, and everything else is shared with snapshot 42.

## When two steps write at once

Publishing is a compare-and-swap on the pointer, which roughly says “move it from 42 to 43, but only if it still says 42.” When someone else got there first, we compare what both steps changed. Changes to different files get replayed on top of the new snapshot, while changes to the same file fail with a conflict that names the paths. We’re still working out the right semantics for this, and there’s more to come soon.

42
43
44
step A
changes tests.json
step B
changes security.json
opens 42
opens 42
42 → 43, ok
expected 42, found 43
different file, so B
is replayed onto 43
branch/main
Both steps open 42, step A’s swap from 42 to 43 succeeds, and step B’s swap fails, so because B changed a different file it is replayed onto 43 to make 44.

## Does this mean you can fork a volume at will?

Pretty much. Since snapshots never change, a fork is just a second pointer aimed at the same snapshot, so a volume with gigabytes of data forks as fast as an empty one. Today a new draft branch can start empty or start from live, and very soon it’ll be able to fork from the branch it came from, and from then on the two pointers move on their own.

43
44
45
branch/main
branch/draft
A fork is a second pointer at snapshot 43, and from then on live and the draft publish independently.

We don’t merge files between branches, since each branch works on its own copy, and we didn’t want to invent three-way merges for a filesystem. The same pointers also make it easy to watch a branch’s files while workflows run on it, since the UI and the agent read whatever snapshot the branch points at and never see a half-written file.

running step
changed files
in local tmpfs copies
invisible to everyone else
until the step succeeds
43
44
branch/main
moves on publish
publish on success
readers
UI file browser
agent tools
API
other steps
read the current pointer
Readers follow the branch pointer to the last committed snapshot, while a running step’s changes stay in its local copies until it succeeds.

## Meet Spongeblob

Everything below Nest is Spongeblob, a storage engine we wrote in Rust. It’s split into an embedded database that only knows about immutable objects and versioned trees with pointers, and a service that turns those into product concepts like “this tree is a filesystem” and “these two writes conflict.”

Spongeblob process
HTTP routes
requests from Nest and the API
volume adapter
stores a filesystem as snapshots
execution adapter
stores step outputs and logs
embedded engine
knows nothing about volumes or workflows
objects
immutable values
snapshots
versioned trees with pointers
storage
packs, the index, S3 copies
Spongeblob is an embedded engine that only knows about objects and versioned trees, wrapped in a service that turns them into volumes and step outputs.

Spongeblob keeps everything on its own disk, and only one process owns that disk at a time, so there’s never any coordination between writers. We pay for that with a short handoff during deploys, where the old process steps aside and the new one reopens the same disk.

We also don’t run one giant Spongeblob. Each sharded 3B stack runs its own, with its own disk, so one busy workload can’t drag down everyone else’s reads and writes. In production today, a typical read takes about a millisecond and a typical write a little under two.

## How a write becomes durable

When Nest publishes a step’s changes, Spongeblob appends the new data to the end of a big file on its disk, which we call a pack, callsfsync, and the write is done. Writes from different steps that arrive around the same time share thatfsync, which is group commit, so the cost of durability follows time rather than the number of writes.

writes waiting
append
active pack
this turn: 32 writes, 1 fsync
so far: 192 writes, 6 fsyncs
Every write that arrives during a turn is appended to the active pack and covered by one fsync, so more writers make bigger batches rather than more syncs.

Updating the index, cleaning up old data, and uploading to S3 all happen async. There’s no separate journal file either. Each write lands in the pack as its data plus a small journal record, under the samefsync, so the packs are the log, and the bytes stay where they landed until cleanup copies the survivors out of a mostly dead pack.

## Where’s my data? Ask the index

Packs hold bytes but can’t answer questions like what the latest version of a file is or which pack it lives in, so Spongeblob keeps those answers in an index, and the index is an LSM tree. New entries go into a sorted table in memory, full tables get written out as sorted files that never change, and a background process merges those files over time.

We are standing on the shoulders of giants here. If you’ve worked with LSM trees or RocksDB, this will look familiar, and a lot of what we know came from RocksDB and the WiscKey paper. Like RocksDB’s blob files, we keep the big bytes out of the tree, so the index only holds small entries that point into the packs, and merging never moves file data.

packs
append-only files on Spongeblob’s disk
pack 7
sealed
pack 8
sealed
pack 9
active
LSM index
small rows that point at the data
object a1f3… → pack 7, 256 KiB
object 9c02… → pack 9, 64 KiB
volume logs, main → snapshot 43
snapshot 43 root → node 8e1…
object 77be… → deleted
File data lives in append-only packs, and the LSM index holds small rows that point into them.

Where we drew the line matters too, and it isn’t free on either side. On the read side, a file is an index lookup plus range reads into whichever packs hold its blocks, and since a step’s changed blocks get stored together while untouched blocks stay where they were, a file that’s been updated many times ends up spread across more packs and takes more reads to copy in. On the write side, separating them moves some of the write cost rather than removing it, into copying survivors out of mostly dead packs, and because we only relocate a pack once at least half of it is dead, file data ends up written at most about twice over its life.

So why not just embed RocksDB? It probably could have worked, and ideas like compaction filters and a shared write-buffer budget are a big part of what we learned from. We wrote a small engine of our own because we wanted it shaped around our data, with formats we read in place and one process budgeting its journal, index, and background work together. Even with RocksDB or a similar system underneath, we’d still have built the snapshot trees, primitives that power forks, leases, conflict checks, and image chunk storage ourselves, since no key-value store hands you those. We also didn’t want a separate database cluster like FoundationDB holding the metadata, since that puts a network hop under every file lookup and gives every stack, and every self-hosted install, one more system to run and keep in agreement with the packs.

## Hot data on disk, cold data in S3

Most of what steps read is generally recent. A workflow tends to reopen the files it wrote in its last few runs, while old snapshots and files nobody has touched in weeks mostly sit there. So Spongeblob treats its own disk as the place for hot, durable data and S3 as the cold tier when it’s available.

A pack takes appends until it’s full or 30 seconds old (configurable if you want a tighter recovery point), then it gets sealed and never changes again. When S3 is configured, sealed packs get uploaded in the background and recorded in a recovery checkpoint, which has everything we’d need to rebuild the store. Once a pack is safely in S3, it becomes eligible for eviction, so when the disk starts filling up, past a high-water mark Spongeblob drops the local copies of packs nobody has read in a while. If someone does read an evicted pack later, Spongeblob fetches it back from S3 on demand, checks it, and serves the read, so cold data costs a trip to S3 the first time it’s read again and stays local while it’s in use.

active
appending, one
fsync per group
sealed
after 30 seconds
or when full
in S3
uploaded and
verified
covered
named by a
recovery checkpoint
evicted
local copy dropped
when the disk fills
a cold read fetches it back
relocate
at half live or less, copy
the live data to a new pack
reclaim
at zero live, once recovery
no longer needs the pack
A pack is sealed after 30 seconds or when full, uploaded to S3 and named by a checkpoint, evicted when the disk fills, and fetched back on a cold read, while mostly dead packs are relocated and empty ones are reclaimed.

Packs also fill up with dead data as files get overwritten and old snapshots expire. Mostly dead packs get their survivors copied into a fresh pack, and fully dead ones get deleted once no checkpoint needs them. On a self-hosted install without S3 there’s nowhere to evict to, so every pack stays on the disk. Reclaiming dead packs keeps it from filling up, and we resize the disk when that isn’t enough.

## Why not write straight to S3?

You might be wondering why we don’t write straight to S3, like a lot of the newer LSM-on-S3 systems. Part of it is the self-hosted requirement, and part is latency. Nest absorbs a step’s page-level reads and writes, so Spongeblob mostly sees a file read in at open and one publish at the end, and both come off its disk in a millisecond or two, while AWS’s own guidance puts small S3 requests in the tens of milliseconds, well past the budget we set for a write. The rest is cost, since sending every write through S3, even batched, would cost a couple of times more than we spend on S3 requests today and grow with traffic. None of these is a dealbreaker alone, but together they made local disk first and S3 second the better fit. The underlying design doesn’t lock us into that choice, though, and moving the end of the log to S3 Express One Zone is something we’re actively considering, which we’ll get to below.

## Durability, consistency, and availability

Putting it all together, Spongeblob makes three promises today, and like any storage system, each one comes with trade-offs.

Durability.A write is durable once its group’sfsyncto Spongeblob’s disk returns. In our cloud that disk is an EBS volume, which AWS already replicates within an availability zone, so a crash, a restart, or a deploy never loses an acknowledged write. Losing the volume itself is the one case EBS doesn’t cover, and S3 is our backstop for it. Sealed packs and recovery checkpoints get copied there in the background, so if a volume were ever lost, we’d rebuild from the last checkpoint, which we keep within about a minute of the latest write. On a self-hosted install without S3, durability is what the disk provides.

Consistency.Every step reads one snapshot from start to finish, no matter what gets published in the meantime. Publishes are ordered, because one process owns each disk and every publish is a compare-and-swap on the pointer, so anyone reading a branch, whether that’s another step, the UI, or an agent, sees a step’s whole change or none of it, and never a half-written file.

Availability.Having one process own each disk keeps things simple, since writers never have to coordinate and everything is served straight from local disk, with cold data faulted back in from S3. The one moment it shows is a deploy, when the old process drains and hands the disk to the new one, which usually takes a second or two. A small router in front of Spongeblob does its due diligence on which process owns the disk, so traffic moves over as soon as the new one is ready, and anything that lands in the gap gets a quick response telling the client to retry in a second.

Both of those windows are small today, and the loss window in particular comes from keeping the end of the log on one disk, which is also the easiest part of the design to change. The journal is the only thing that decides whether a write happened, and everything above it, including the index, snapshots, and forks, is derived from it, so we can move where the end of the log lives without redesigning the rest. Writing just that tail synchronously to S3 Express One Zone would cost around 7–10 ms per commit, which is outside our write budget but nowhere near as far as S3 Standard, and in return it would close the window for losing the volume and stop a new owner from depending on the old disk, while the data itself stays on local disk. S3 Express lives in a single availability zone, though, so like EBS it wouldn’t cover losing the zone itself. That’s still a long way from putting the whole store on object storage, since reads, packs, the index, and snapshots would all stay local, and only the end of the log would move. We’re weighing that against building a quorum-based log across a few machines, which would keep commits fast but means running a consensus system of our own (who wants to manage that?!).

## Where this leaves us

We feel good about where this landed, and most of that comes down to a handful of primitives underneath. Snapshots never change, a pointer only moves through a compare-and-swap, a fork costs one pointer, and data is named by its contents, all sitting on a single durable log. A lot of product features fell out of those without us building them one by one. A draft can’t touch live because it’s a different pointer, and a step either commits or leaves nothing behind because publishing is one swap at the end. Two steps can’t clobber each other because that same swap catches it, and you can watch a branch’s files while workflows run because readers just follow the pointer.

Forking is the one I’m most excited about. Since a fork is just a pointer, a working branch can get its own full copy of the entire volume and everything inside it, whether that’s a SQLite file, JSONL, a DuckDB file, or something else, without copying a single byte.

The same design is turning out to be useful outside of volumes, too. A sandbox’s base image, its root filesystem, can be backed by Spongeblob as well, which gives us fast boots and lets images share chunks, and we’ll have more to share on that later.

Looking back, the simple choices did most of the work. One owner per disk means writers never coordinate, the packs doubling as the log means there’s one durability story, and not merging branches means no merge logic to get wrong. We took on complexity only where the requirements pushed us, like writing our own engine instead of bending another LSM store to fit, moving packs between disk and S3, and replaying non-conflicting writes on top of each other.

The places where we still pay for keeping it simple are the ones we’re working on next. We want to settle which files get copied at open and which get fetched on demand, so even big files are cheap to open. We also want index merges to do less work for the same amount of change, since they’re our biggest background cost. And for v2, we’re deciding whether the end of the log should live in S3 Express or on a quorum of machines, so losing a disk no longer loses recent writes and a new owner no longer needs the old disk during a handoff.