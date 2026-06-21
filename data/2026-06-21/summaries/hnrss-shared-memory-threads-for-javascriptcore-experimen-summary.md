---
title: Shared-memory threads for JavaScriptCore (experimental, not working yet) by Jarred-Sumner · Pull Request #249 · oven-sh/WebKit · GitHub
url: https://github.com/oven-sh/WebKit/pull/249
date: 2026-06-20
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-06-21T11:07:23.828810
---

# Shared-memory threads for JavaScriptCore (experimental, not working yet) by Jarred-Sumner · Pull Request #249 · oven-sh/WebKit · GitHub

# Shared-memory threads for JavaScriptCore (experimental, not working yet)

## Overview
- Introduces a `Thread` class that runs a function on another core while sharing the same heap and objects.  
- No structured clone, no message passing, no reliance on `SharedArrayBuffer`.  
- Parallel JavaScript executes through all four JIT tiers without a global lock; the thread test suite now passes.  
- Still incomplete: thread‑sanitizer cleanup, fuzzing, one benchmark over budget, and extensive soak testing. The fallback locked mode and the threads‑disabled configuration remain unchanged. The PR may never be merged; it exists for design review.

## API Summary
- `new Thread(fn, ...args)` – creates a thread that calls `fn` with the supplied arguments.  
- `t.join()` – blocks the caller, returns the function’s value or rethrows its exception.  
- `await t.asyncJoin()` – returns a promise that resolves with the function’s result; never blocks.  
- `Thread.current` – reference to the current thread.  
- `t.id` – engine thread identifier (main thread is 0).

## Contrast with Web Workers
- Workers require stringifying source code, creating a blob URL, and using an `onmessage` protocol; the function cannot close over external variables.  
- `Thread` accepts a real closure, preserving imports, classes, and surrounding variables.  
- Exceptions propagate unchanged; workers deliver errors as `ErrorEvent`s.  
- No need for separate files, bundler configurations, or transferable objects.

## Example Patterns

### Parallel map without copying
```js
const items = loadItems();               // 100 k plain objects
const results = new Array(items.length);
const next = { i: 0 };
const workers = Array.from({ length: 8 }, () =>
  new Thread(() => {
    for (;;) {
      const i = Atomics.add(next, "i", 1);
      if (i >= items.length) return;
      results[i] = transform(items[i]);
    }
  })
);
workers.forEach(t => t.join());
// results now fully populated, never copied.
```

### Shared cache with a lock
```js
const cache = new Map();
const lock = new Lock();

function memoized(key) {
  let hit;
  lock.hold(() => { hit = cache.get(key); });
  if (hit) return hit;
  const value = compute(key);
  lock.hold(() => { cache.set(key, value); });
  return value;
}
```

### Simple cancellation flag
```js
const ctl = { stop: false };
const search = new Thread(() => {
  for (const candidate of space) {
    if (ctl.stop) return null;
    if (good(candidate)) {
      ctl.stop = true;
      return candidate;
    }
  }
});
ctl.stop = true;   // can be set from any thread
```

### Live progress reporting
```js
const progress = { done: 0, total: files.length };
const t = new Thread(() => {
  for (const f of files) {
    process(f);
    Atomics.add(progress, "done", 1);
  }
});
const ticker = setInterval(() => {
  render(`${progress.done}/${progress.total}`);
  if (progress.done === progress.total) clearInterval(ticker);
}, 100);
await t.asyncJoin();
```

### Blocking handoff with condition variable
```js
const lock = new Lock(), cond = new Condition();
const mailbox = { ready: false, payload: null };

const consumer = new Thread(() => {
  let received;
  lock.hold(() => {
    while (!mailbox.ready) cond.wait(lock);
    received = mailbox.payload;
  });
  return received.process();
});

lock.hold(() => {
  mailbox.payload = buildThing();
  mailbox.ready = true;
  cond.notify();
});
```

## Advantages
- All threads share a single global object (`globalThis`), prototype chain, and module graph; there is exactly one instance of each class and singleton.  
- No serialization or copying of objects; data structures are directly accessible from any thread.  
- Standard concurrency constructs (thread pools, fine‑grained locks, condition variables, lock‑free counters) map directly onto JavaScript code.  

## Remaining Work
- Clean up thread‑sanitizer warnings.  
- Add extensive fuzz testing.  
- Resolve the benchmark that exceeds the time budget.  
- Conduct long‑duration soak testing before considering production use.