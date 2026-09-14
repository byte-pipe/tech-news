---
title: Principles for fast Tokio applications
url: https://dial9-rs.github.io/blog/principles-for-fast-tokio-applications/
date: 2026-09-14
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-09-15T07:39:12.259428
---

# Principles for fast Tokio applications

# Principles for fast Tokio applications

## General principles

### First, determine whether you have a problem
- Look for long polls (time between `.await` points) that exceed the 10‑100 µs range suggested by Alice Ryhl.  
- Use a real metric (e.g., latency percentile) as the driver; long polls are not always harmful.  
- Most performance issues stem from application logic, not Tokio itself.  
- Tokio’s *schedule latency* histogram (time from task becoming ready to being polled) is the most useful metric for spotting problems.

### Split for latency, batch for throughput
#### Yield more frequently to optimize for latency
- Fairness between connections is essential for low latency.  
- In pipelined protocols (e.g., Redis), reading many frames without yielding creates long polls and unfairness.  
- Inserting `tokio::task::yield_now().await` after each request—or after a few consecutive ready reads—can reduce latency by an order of magnitude.  
- Signs you have this issue: high P99 vs. P50 latency, polls longer than the work they contain, many spans inside a single poll.

#### Batch work to amortize overhead
- Reduce the number of runtime events (task switches, queue insertions) by grouping work.  
- `tokio::fs` operations run on the blocking pool; spawning many small `spawn_blocking` calls adds noticeable overhead.  
- Batch filesystem or other blocking operations into larger units, or use a dedicated OS thread when appropriate.  
- Spawning thousands of tiny tasks is inefficient; consider the work size before creating a new task.  
- Indicators: `spawn_blocking` shows up prominently in flamegraphs, tight loops with many tiny operations, throughput improves when work is grouped.

### Beware global resources
- The blocking pool is a global queue; high submission rates (e.g., ~50 k blocking tasks/s on a 32‑core machine) can become a bottleneck.  
- `spawn_blocking` is not a universal remedy; short bounded work may be better handled by regular workers with work‑stealing.

### Be extremely careful with mutexes
- Global mutexes can serialize work and increase poll times; prefer lock‑free designs or fine‑grained locking.

### Constrain parallelism — usually
- Limit the amount of concurrent work to what the runtime can handle efficiently; oversubscription leads to contention and higher latency.

### Isolate Tokio workers from other threads
- Keep Tokio worker threads separate from non‑async threads to avoid interference and preserve scheduling predictability.

## Tricks for when you know better
- **Blocking the executor can be fine—sometimes**: occasional blocking may be acceptable if it does not dominate the runtime.  
- **Use multiple runtimes to isolate workloads by priority**: run high‑priority tasks on a dedicated runtime to prevent them from being delayed by lower‑priority work.  
- **Spin to keep control**: in very low‑latency scenarios, a short spin loop can be used instead of yielding, but it should be bounded.

## Appendix: A mental model for Tokio in four bullet points
- Tokio runs a work‑stealing pool of worker threads that poll ready futures.  
- *Schedule latency* measures the delay between a task becoming ready and being polled.  
- Global resources (blocking pool, mutexes) can become bottlenecks under high load.  
- Fairness (yielding) versus batching is a trade‑off: yield often for low latency, batch for higher throughput.