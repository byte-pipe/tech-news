---
title: "Zig's Io.Threaded is Neat"
url: https://matklad.github.io/2026/08/06/neat-io-threaded.html
date: 2026-08-22
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-08-23T06:01:09.461960
---

# Zig's Io.Threaded is Neat

# Zig's Io.Threaded is Neat

## Overview
- std.Io.Threaded is an implementation of Zig’s new I/O interface that runs on ordinary OS threads.
- It uses blocking syscalls but adds full support for cancellation, achieving a feature the author has wanted for a long time.

## Concurrency vs Parallelism
- **Concurrency**: handling asynchronous, nondeterministic events; often requires the ability to cancel work.
- **Parallelism**: using hardware resources to perform work simultaneously; typically deterministic and declarative.
- Example of parallelism with Rayon shows splitting work into independent partitions that the platform executes.
- Concurrency inevitably involves cancelation: when one async computation determines another is no longer needed, it must be stopped promptly.

## Problems with Plain Threads
- Spawning many threads may need system‑wide configuration changes, which is impractical for many applications.
- Without a cancellation mechanism, a thread blocked inside a syscall cannot be unblocked by ordinary checks (e.g., `is_canceled()` loops).
- Standard language APIs do not provide a way to interrupt a blocked syscall.

## Zig’s Solution (SIGIO)
- On POSIX, a blocked syscall can be interrupted by delivering a signal, causing it to return `EINTR`.
- Zig combines this with a shared‑memory flag protocol:
  1. Canceling thread sets a flag and repeatedly signals the target thread.
  2. The target thread, upon receiving `EINTR`, checks the flag.
  3. If cancellation is requested, it returns `error.Canceled` and begins unwinding; otherwise it retries the syscall.
- On Windows, the more direct `NtCancelSynchronousIo` is used.
- This approach allows standard OS threads and blocking APIs to be canceled reliably without needing newer mechanisms like `io_uring`.

## Prior Art Comparison
- **Java**: thread interruption exists but cannot cancel syscalls; `IOException` and `InterruptedException` are unrelated.
- **pthread_cancel**: uses a similar signal‑plus‑flag technique but lacks integration with language‑level cancellation (`try`, `defer`) and tears down the whole thread, which is costly.
- Zig’s I/O separates “may run concurrently” from “must run concurrently”, employs a thread pool, and spawns new threads only when the pool is exhausted.
- This design yields clearer signatures (`concurrent` is always fallible, `async` never is) and better expresses the programmer’s intent.

## Takeaway
- Zig’s `std.Io.Threaded` provides a practical way to use ordinary OS threads with reliable cancellation, avoiding the need for specialized kernel interfaces.
- It improves the ergonomics of concurrency in Zig compared to existing mechanisms in other languages and operating systems.