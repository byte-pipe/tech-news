---
title: Codex Was Torching Your SSD and Nobody Noticed for Months - DEV Community
url: https://dev.to/varshithvhegde/codex-was-torching-your-ssd-and-nobody-noticed-for-months-4c5h
site_name: devto
content_file: devto-codex-was-torching-your-ssd-and-nobody-noticed-for
fetched_at: '2026-11-08T09:03:06.821791'
original_url: https://dev.to/varshithvhegde/codex-was-torching-your-ssd-and-nobody-noticed-for-months-4c5h
author: Varshith V Hegde
date: '2026-11-02'
description: Your Codex log file looked fine. Your SSD counters did not. The file was small. That was... Tagged with codex, security, devops, productivity.
tags: '#codex, #security, #devops, #productivity'
---

Small files mask massive flash wear

# Your Codex log file looked fine. Your SSD counters did not.

The file was small.

That was the trick.

If you opened~/.codex/, you could see a SQLite database calledlogs_2.sqlite. It was not huge. It was not swallowing the disk. Finder, Explorer,du, and every normal storage check had nothing dramatic to say.

Meanwhile, one developer's SSD recorded roughly37 TB of writes in 21 days.

That works out to about1.7 TB a day. If you stretch one heavy, continuous-use report across a full year, it becomes roughly640 TB.

The number is not a prediction for every Codex user. It came from one machine running for a long time. But it exposed a problem that is easy to miss with local developer tools:

a file can stay small while the storage device underneath it gets written to constantly.

This is the story of a noisy TRACE logging sink, a SQLite database doing exactly what it was told, and the SSD wear that nobody could see from file size alone.

## The quick version

* A user reported unusually high local disk writes and traced them to Codex CLI'slogs_2.sqlitedatabase and its WAL companion file.
* The reported machine accumulated about 37 TB of writes over 21 days of uptime.
* The file stayed bounded because new logs were inserted while older logs were deleted.
* The reported cause was an overly verbose TRACE logging path that did not fully respect the expectedRUST_LOGoverride.
* The supplied investigation says version0.142.0reduced the noisy writes substantially, with early testing reporting around85% fewer log writes.
* If you used an older build heavily, update first, then inspect real write activity and your SSD's lifetime-write counters.

## The number that made people look twice

37 TB in 21 days is not a normal “developer tool wrote some logs” story.

Measurement

Value

Reported writes

~37 TB

Reporting window

21 days

Approximate daily rate

~1.7 TB/day

Annualized at that rate

~640 TB/year

The annualized number needs context. It assumes the same workload every day for a year, which is rarely how people work. Someone running short sessions will produce far less. Someone leaving the tool open, working with long sessions, or using it in automation could produce much more than they expect.

The useful point is not “every SSD will die in a year.”

The useful point is that this level of write activity belongs in the category of things you should notice and control.

## Why the file size told you almost nothing

Most of us check disk problems like this:

du
 
-sh
 ~/.codex

ls
 
-lh
 ~/.codex/logs_2.sqlite
*

Enter fullscreen mode

Exit fullscreen mode

Those commands answer one question:

How much data is stored right now?

They do not answer this:

How much data has been written over time?

The Codex log database was designed to retain a bounded amount of diagnostic information. New rows were written, old rows were removed, and the database could remain roughly the same size.

So the folder looked calm while the disk was doing constant work.

Imagine a café with four tables. Looking through the window at noon, you see four people sitting down. Come back at 6 PM, still four people. The table count tells you nothing about whether eight customers visited or eight hundred.

The SQLite file was the same. Stable size, enormous turnover.

## What was generating all those writes?

The reported issue points to a logging path that defaulted toTRACE, the most detailed level in Rust's tracing ecosystem.

TRACE logging is useful when you are trying to understand a very specific failure. It can include low-level events that are normally too noisy for everyday use:

* file-open events
* raw network or WebSocket activity
* transport details
* telemetry plumbing
* dependency-library messages that get bridged into the application's tracing system

The supplied breakdown estimates that TRACE-level entries made up70.7%of the retained log-body size. The highest-volume targets included WebSocket handling, OpenTelemetry-related logs, a generic dependency log bridge, and client transport code.

That is diagnostic exhaust. A little of it is fine. A default stream of it, persisted locally in SQLite, is a different kind of workload.

## The three parts that stacked together

No single part of this design has to be bad on its own.

### 1. TRACE was active where it should have been opt-in

TRACE is not a normal default for a tool used for hours at a time. It is the level you turn on when you are actively debugging.

The reported behavior was that Codex initialized a feedback logging sink at TRACE. That turns every routine interaction into a lot of diagnostic detail.

### 2. RUST_LOG=warn did not fully quiet it

Rust developers often reach for this first:

RUST_LOG
=
warn codex

Enter fullscreen mode

Exit fullscreen mode

That is supposed to turn down the volume. According to the issue analysis, it did not fully apply to the relevant sink. If a target did not have an explicit override, Codex's internal default still allowed noisy logging.

That is worse than an obvious missing setting. A user can think they reduced logging while the disk keeps receiving the same workload.

### 3. SQLite turned event noise into storage churn

SQLite is excellent. It is also not magic.

For small structured local data, a SQLite database is a good choice. For a constant stream of fine-grained TRACE events, inserts, deletes, indexes, and checkpoints, it can create a lot of writes even when the database never becomes large.

The problem was not “SQLite is bad.” The problem was using a write-heavy retention loop as a sink for a log level that should not have been permanently enabled.

## The part the operating system does not show you

There are two kinds of amplification in this story.

### SQLite write amplification

SQLite often uses WAL mode, short for write-ahead logging.

In simplified form:

1. A log event is appended to the WAL file.
2. SQLite later checkpoints that change into the main database.
3. Older rows are deleted to keep retained data bounded.
4. Indexes and database pages are updated along the way.

Enter fullscreen mode

Exit fullscreen mode

One logical log event can therefore create more than one write at the filesystem level.

The WAL is not wrong. Checkpoints are not wrong. The problem appears when that loop is fed relentlessly with small, noisy events.

### SSD write amplification

An SSD has its own internal life.

It writes data in small pages but erases much larger blocks. When a small part of a block changes, the SSD controller often writes the new data to a fresh location, marks old data stale, later moves still-valid pages, and erases the old block.

That movement is called garbage collection. Wear leveling moves writes around so one physical area does not wear out first.

Both are useful. Both mean the flash may receive more physical writes than the operating system asked for.

The ratio is called the write amplification factor. The exact number varies by drive, spare capacity, free space, workload, and controller. The supplied analysis does not measure the multiplier for the affected drive, so do not treat any guessed physical-wear number as a precise fact.

The direction is enough:

High-churn, small random writes are one of the workloads SSDs work hardest to manage.

## Is 640 TB actually dangerous?

It can be.

SSDs have an endurance rating usually expressed as TBW, or terabytes written. A typical 1 TB consumer SSD may be rated for a few hundred TBW. Enterprise drives may be rated much higher. The exact number depends on the model, capacity, NAND type, and warranty.

That does not mean a drive fails the moment it reaches its rated TBW. Ratings are warranty and endurance guidance, not a timer that hits zero at midnight. Plenty of drives outlive them.

But a background development tool potentially consuming hundreds of terabytes of writes is still worth taking seriously. It can eat through a meaningful part of the drive's expected write budget without filling the disk or showing a visible failure.

## How to check your own machine

The order matters.

Update first. Then look at real I/O. Then check what the drive itself says.

### Step 1: update Codex

The investigation supplied with this article identifies0.142.0as the version containing the logging reduction. Check the current release notes and your installed build, then update before you start measuring.

Also remember that Codex CLI, the desktop app, and editor integrations can ship or bundle components on different schedules. Updating one does not automatically prove every local Codex-related process is updated.

### Step 2: find the log files

On macOS and Linux:

ls
 
-la
 ~/.codex/logs_2.sqlite
*

Enter fullscreen mode

Exit fullscreen mode

On Windows PowerShell:

Get-Item
 
"
$
env
:
USERPROFILE
\.codex\logs_2.sqlite*"

Enter fullscreen mode

Exit fullscreen mode

You might see the database, a-walfile, and a-shmfile.

Do not stop after checking their size. A small database is the whole reason this incident was easy to miss.

### Step 3: watch actual writes

On Linux,pidstatcan show which process is writing:

pidstat 
-d
 5

Enter fullscreen mode

Exit fullscreen mode

To see whether a process has the database open:

sudo 
lsof ~/.codex/logs_2.sqlite

Enter fullscreen mode

Exit fullscreen mode

On macOS, openActivity Monitor, select theDisktab, and watch bytes written for Codex-related processes while you work.

On Windows, useResource Monitoror Task Manager's disk column. Look at sustained per-process writes, not just a brief spike during startup.

### Step 4: check the drive's own lifetime write counter

This is the closest thing to the truth you have.

On Linux or macOS with smartmontools installed, an NVMe drive can often be checked with:

sudo 
smartctl 
-a
 /dev/nvme0

Enter fullscreen mode

Exit fullscreen mode

Look for:

* Data Units Written
* Percentage Used
* warnings or critical health indicators

On Windows, CrystalDiskInfo exposesTotal Host Writesand health information. PowerShell can also show some device health data:

Get-PhysicalDisk
 
|
 
Get-StorageReliabilityCounter
 
|

 
Select-Object
 
DeviceId
,
 
Wear
,
 
Temperature

Enter fullscreen mode

Exit fullscreen mode

Compare lifetime writes with the TBW rating for your exact drive model. Do not compare against a random SSD number from a search result.

## What if I used an older version for months?

First, do not panic and do not guess from file size.

Check the drive counters. If the drive has low percentage used and reasonable total writes for its age and workload, update and move on. If the drive has unusually high wear, warnings, or a large write count compared with its TBW rating, back up your important data and plan for a replacement before failure forces the schedule.

This is a good backup reminder even if your drive looks healthy. SSDs usually fail without much theatre.

## Workarounds if you cannot update immediately

Updating is the right fix. These are temporary ways to reduce persistent write pressure while you arrange that update.

### Put throwaway logs on ephemeral storage

For CI jobs and containers, the cleanest option is usually to run with a temporary home directory or mount the relevant config directory on ephemeral storage.

Example for a disposable CI environment:

export 
HOME
=
"
$(
mktemp
 
-d
)
"

Enter fullscreen mode

Exit fullscreen mode

For a container workload, mount a tmpfs at the appropriate Codex state directory if the environment can tolerate losing local diagnostics when the job exits.

This is especially useful for build runners that create and destroy their environment anyway.

### Be careful with /tmp

Moving a log file to/tmpis only useful if/tmpis actually memory-backed in your environment. On many Linux systems it may be tmpfs. On macOS,/tmpis not automatically a RAM disk by default.

Check the mount before assuming the write load vanished:

mount | 
grep
 
' /tmp '

Enter fullscreen mode

Exit fullscreen mode

Then verify with a real I/O monitor. Never trust a workaround because it sounded plausible in a comment thread.

### Avoid unsupported database surgery unless you really need it

Some community workarounds modify the SQLite log database so inserts are ignored. That can be useful in an emergency, but it is an unsupported change to an internal application file.

Future versions may change the schema or assume the database behaves normally. If you choose that route, stop Codex first, make a copy of the database, document what you changed, and remove the workaround once you are on a fixed release.

## The bigger lesson for tool builders

This bug is bigger than one CLI.

### Measure bytes written, not just disk space used

Every local persistence feature should have an I/O budget under realistic usage. Test bytes written per hour, per session, and per day. File size is not a sufficient metric for databases, caches, indexes, or log rotation systems.

### TRACE must be an intentional decision

Verbose logging needs an explicit opt-in and a clear way back out. Shipping it by default turns every user into a debugging environment.

### Standard controls have to work end to end

If your ecosystem has a standard logging override, honour it for every sink. A partial override is dangerous because it gives experienced users false confidence.

### Structured logs have storage costs

SQLite, RocksDB, local search indexes, and caches are all good tools. High-frequency writes have a cost. The design needs backpressure, batching, rate limits, retention rules, and test coverage for pathological verbosity.

### Privacy and wear are connected

The more raw operational detail a tool records, the more it writes and the more sensitive local data it can retain. Logging file paths, raw transport frames, and low-level event payloads should be a deliberate debugging choice, not background noise.

## The bigger lesson for users

There is a simple habit worth keeping:

When you install a new long-running developer tool, look at its write rate once.

Two minutes in Activity Monitor, Resource Monitor, orpidstatcan catch a surprising amount.

Check lifetime SSD writes occasionally. Keep your tools updated. Treat a stable file size as a storage number, not an I/O number.

The log file was small. The work it made the SSD do was not.

## What is confirmed and what is still uncertain

The supplied investigation is clear about its limits, and those limits matter:

* The 37 TB measurement came from one heavy user's machine. It is a data point, not a universal rate.
* Reports disagree about when the highest logging verbosity began. The exact start date is uncertain.
* The annualized 640 TB figure is arithmetic based on the reported 21-day sample, not a forecast.
* SSD write amplification is real, but the exact physical NAND multiplier was not measured for this incident.
* The reported 85% reduction after version 0.142.0 is an early observed result, not a guarantee for every platform or workload.

That uncertainty does not weaken the main finding. The correct response is still simple: update, measure the process, and inspect the drive counter.

## Sources and further reading

* GitHub issue #28224 in openai/codex
* Official OpenAI Codex documentation
* The public reporting and technical analysis supplied for this article, including Notebookcheck, Windows Report, Lilting.ch, yage.ai, and Daniel Vaughan's write-up

Submit

Preview

Dismiss

 View full discussion (38 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.