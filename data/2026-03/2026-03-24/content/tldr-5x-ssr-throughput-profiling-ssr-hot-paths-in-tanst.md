---
title: '5x SSR Throughput: Profiling SSR Hot Paths in TanStack Start | TanStack Blog'
url: https://tanstack.com/blog/tanstack-start-5x-ssr-throughput
site_name: tldr
content_file: tldr-5x-ssr-throughput-profiling-ssr-hot-paths-in-tanst
fetched_at: '2026-03-24T19:28:04.007487'
original_url: https://tanstack.com/blog/tanstack-start-5x-ssr-throughput
author: co-authored by Manuel Schiller and Florian Pellet
date: '2026-03-24'
description: How profiling under sustained load uncovered SSR hot paths in TanStack Start and led to a 5.5x throughput gain by removing unnecessary server-side work.
tags:
- tldr
---

TanStack
New
TanStack Intent
Search...
 K
Auto
Log In
Start
RC
Start
RC
Router
Router
Query
Query
Table
Table
DB
beta
DB
beta
AI
alpha
AI
alpha
Form
new
Form
new
Virtual
Virtual
Pacer
beta
Pacer
beta
Hotkeys
alpha
Hotkeys
alpha
Store
alpha
Store
alpha
Devtools
alpha
Devtools
alpha
CLI
alpha
CLI
alpha
Intent
alpha
Intent
alpha
More Libraries
More Libraries
Builder
Alpha
Builder
Alpha
Blog
Blog
Maintainers
Maintainers
Partners
Partners
Showcase
Showcase
Learn
NEW
Learn
NEW
Stats
Stats
YouTube
YouTube
Discord
Discord
Merch
Merch
Support
Support
GitHub
GitHub
Ethos
Ethos
Tenets
Tenets
Brand Guide
Brand Guide
Blog
On this page

# 5x SSR Throughput: Profiling SSR Hot Paths in TanStack Start

Copy page

by Manuel Schiller and Florian Pellet on Mar 17, 2026.

## TL;DR

We improved TanStack Start's SSR performance dramatically. Under sustained load (using ourlinks-100stress benchmark with 100 concurrent connections, 30 seconds):

* Throughput: 427 req/s → 2357 req/s (5.5x)
* Average latency: 424ms → 43ms (9.9x faster)
* p99 latency: 6558ms → 928ms (7.1x faster)
* Success rate: 99.96% → 100% (the server stopped failing under load)

For SSR-heavy deployments, this translates directly to lower hosting costs, the ability to handle traffic spikes without scaling, and eliminating user-facing errors.

This work started afterv1.154.4and targets server-side rendering performance. The goal was to increase throughput and reduce server CPU time per request.

We did it with a repeatable process, not a single clever trick:

* Measure under load, not in microbenchmarks.
* UseCPU profilingto find the highest-impact work.
* Removeentire categories of costfrom the server hot path.

We highlight the highest-impact patterns below:

* avoidURLconstruction/parsing when it is not required
* avoid reactivity work during SSR (subscriptions, structural sharing, batching)
* add server-only fast paths behind a build-timeisServerflag
* avoiddeletein performance-sensitive code

## Methodology: feature-focused endpoints + flamegraphs

We are not claiming that any single line of code is "the" reason. This work spanned over20 PRs, with still more to come. Every change was validated by:

* a stable load test (same endpoint, same load)
* a before/after comparison on the same benchmark endpoint
* a CPU profile (flamegraph) that explains the delta

### Why feature-focused endpoints

We did not benchmark "a representative app page". We used endpoints that exaggerate a feature so the profile is unambiguous:

* links-100: renders ~100 links to stress link rendering and location building.
* layouts-26-with-params: deep nesting + params to stress matching and path/param work.
* empty: minimal route to establish a baseline for framework overhead.

This is transferable: isolate the subsystem you want to improve, and benchmark that.

### CPU profiling with@platformatic/flame

To capture a CPU profile of the server under load, we start the built server with@platformatic/flame:

sh
flame run ./dist/server.mjs

This produces:

* a CPU flamegraph
* a heap flamegraph
* and markdown summaries of the captured profile data

### Load generation withautocannon

While@platformatic/flameis running in one terminal, we usedautocannonin another terminal to generate a 30s sustained load. We tracked:

* requests per second (req/s)
* latency distribution (average, p95, p99)

Example command (adjust concurrency and route):

sh
autocannon -d 30 -c 100 --warmup [ -d 2 -c 20 ] http://localhost:3000/bench/links-100

### How to interpret the results

To improve SSR performance, we repeated the same loop:

* Focus onself timefirst. That is where the CPU is actually spent.
* Fix one hotspot, re-run the benchmark, and re-profile.
* Prefer changes that remove work in the steady state.

### Reproducing these benchmarks

Our benchmarks were stable enough to produce very similar results on a range of setups. However, here are the exact environment details we used to run most of the benchmarks:

* Node.js: v24.12.0
* Hardware: MacBook Pro (M3 Max)
* OS: macOS 15.7

The exact benchmark code is available inour repository.

## Finding 1:URLis expensive in server hot paths

### The mechanism

In our SSR profiles,URLconstruction/parsing showed up as significant self-time in the hot path on link-heavy endpoints. The cost comes from doing real work (parsing/normalization) and allocating objects. When you do it once, it does not matter. When you do it per link, per request, it dominates.

### The transferable pattern

Use cheap predicates first, then fall back to heavyweight parsing only when needed.

* If a value is clearly internal (e.g. starts with/but not//, or starts with.), don't try to parse it as an absolute URL.
* If a feature is only needed in edge cases (e.g. rewrite logic), keep it off the default path.

### What we changed

typescript
// Before: always parse
const url = new URL(to, base)

// After: check first, parse only if needed
if (isSafeInternal(to)) {
 // fast path: internal navigation, no parsing needed
} else {
 const url = new URL(to, base)
 // ...external URL handling
}

TheisSafeInternalcheck can be orders of magnitude cheaper than constructing aURLobject1. It's meant to be a cheap predicate, so it is okay if some URLs thatwouldbe internal are classified as external and go through the slower path.

See:#6442,#6447,#6516

### Measuring the improvements

Like every PR in this series, this change was validated by profiling the impacted method before and after. For example we can see in the example below that thebuildLocationmethod went from being one of the major bottlenecks of a navigation to being a very small part of the overall cost:

Before:
 The
RouterCore.buildLocation
 (red arrow) method was creating a
new URL
 every time (purple blocks), and then updating its search which re-triggers an expensive parsing step.

After:
 The
isSafeInternal
 check is able to fully skip the
URL
.
RouterCore.buildLocation
 becomes an almost insignificant part of the overall cost.

## Finding 2: SSR does not need reactivity

### The mechanism

SSR renders once per request.2There is no ongoing UI to reactively update, so on the server:

* store subscriptions add overhead but provide no benefit
* structural sharing3reduces re-renders, but SSR does not re-render
* batching reactive updates is irrelevant if nothing is subscribed

### The transferable pattern

If your code supports both client reactivity and SSR, gate the reactive machinery so the server can skip it entirely:

* on the server: return state directly, no subscriptions, reduce immutability overhead
* on the client: subscribe normally

This is the difference between "server = a function" and "client = a reactive system".

### What we changed

typescript
// Before: same code path for client and server
function useRouterState() {
 return useStore(router, { ... }) // unnecessary subscription on the server
}

// After: server gets a simple snapshot
function useRouterState() {
 if (isServer) return router.store // no subscriptions on the server
 return useStore(router, { ... }) // regular behavior on the client
}

See:#6497,#6482

Note

isServeris a build-time constant. This means that the above code is not violating the rules of hooks in React. At runtime, the code will always execute the same branch.

### Measuring the improvements

Taking the example of theuseRouterStatehook, we can see that most of the client-only work was removed from the SSR pass, leading to a ~2x improvement in the total CPU time of this hook.

Before:
 The
useRouterState
 hook was subscribing to the router store, which triggers many sync and memoization calls before calling the
select
 callback.

After:
 The
isServer
 check is able to skip directly to the
select
 callback.

## Finding 3: server-only fast paths are worth it (when gated correctly)

### The mechanism

As a general rule, client code cares about bundle size, while server code cares about CPU time per request. Those constraints are different.

If you can guard a branch with abuild-time constantlikeisServer, you can:

* add server-only fast paths for common cases
* keep the general algorithm for correctness and edge cases
* allow bundlers to delete the server-only branch from client builds

In TanStack Start,isServeris provided via build-time resolution of export conditions4(client:false, server:true, dev/test:undefinedwith fallback). Modern bundlers like Vite, Rollup, and esbuild perform dead code elimination (DCE)5, removing unreachable branches when the condition is a compile-time constant.

### The transferable pattern

Write two implementations:

* fast pathfor the common case
* general pathfor correctness

And gate them behind a build-time constant so you don't inflate the bundle size for clients.

### What we changed

typescript
// isServer is resolved at build time:
// - Vite/bundler replaces it with `true` (server) or `false` (client)
// - Dead code elimination removes the unused branch

if (isServer) {
 // server-only fast path (removed from client bundle)
 if (isCommonCase(input)) {
 return fastServerPath(input)
 }
}
// general algorithm that handles all cases
return generalPath(input)

See:#4648,#6505,#6506

### Measuring the improvements

Taking the example of thematchRoutesInternalmethod, we can see that its children's total CPU time was reduced by ~25%.

Before:
 The
interpolatePath
 function spends >1s using the generic
parseSegment
 function.

After:
 The
interpolatePath
 function now uses the server-only fast path, skipping
parseSegment
 entirely.

## Finding 4:deletecan be expensive

### The mechanism

Modern engines optimize property access using object "shapes" (e.g. V8 HiddenClasses6/ JSC Structures7) and inline caches.deletechanges an object's shape and can force a slower internal representation (e.g. dictionary/slow properties), which can disable or degrade those optimizations and deopt optimized code.

### The transferable pattern

Avoiddeletein hot paths. Prefer patterns that don't mutate object shapes in-place:

* set a property toundefined(when semantics allow)
* create a new object without the key (object rest destructuring) when you need a "key removed" shape

### What we changed

typescript
// Before: mutates shape
delete this.shouldViewTransition

// After: set to undefined
this.shouldViewTransition = undefined

See:#6456,#6515

### Measuring the improvements

Taking the example of thestartViewTransitionmethod, we can see that the total CPU time of this method was reduced by >50%.

Before:
 The
startViewTransition
 function (red arrow) has ~400ms of self-time in the hot path (i.e. not including the time spent in its children).

After:
 Removing the
delete
 statement almost completely removes the self-time of this function.

## Results

### Independent benchmark

Matteo Collina independently benchmarked Start's SSR performance as part of hisarticle investigating SSR performance across React meta-frameworksand observed significant improvements after our optimizations. The following table summarizes the before/after results under sustained load:

Metric
Before
After
Improvement
Success rate
75.52%
100%
does not fail under load
Throughput
477 req/s
1041 req/s
+118% (2.2x)
Average latency
3,171ms
13.7ms
231x faster
p90 latency
10,001ms
23.0ms
435x faster
p95 latency
10,001ms
28.1ms
370x faster

The "before" numbers show a server under severe stress: 25% of requests failed (likely timeouts), and p90/p95 hit the 10s timeout ceiling. After the optimizations, the server handles the same load comfortably with sub-30ms tail latency and zero failures.

To be clear: TanStack Start was not broken before these changes. Under normal traffic, SSR worked fine. These numbers reflect behavior undersustained heavy load(the kind you see during traffic spikes or load testing). The optimizations increase headroom. At this same load, the server no longer drops requests, and it only starts failing at substantially higher load than before.

### Event-loop utilization

The following graphs show event-loop utilization8against throughput for each feature-focused endpoint, before and after the optimizations. Lower utilization at the same req/s means more headroom; higher req/s at the same utilization means more capacity.

For reference, the machine on which these were measured reaches 100% event-loop utilization at 100k req/s on an empty Node HTTP server9.

#### 100 links per page

#### Deeply nested layout routes

#### Minimal route (baseline)

## Conclusion

The biggest gains came from removing whole categories of work from the server hot path. Throughput improves when you eliminate repeated work, allocations, and unnecessary generality in the steady state.

There were many other improvements (client and server) not covered here. SSR performance work is ongoing.

## References

## Footnotes

1. The WHATWG URL Standard requires significant parsing work: scheme detection, authority parsing, path normalization, query string handling, and percent-encoding. See theURL parsing algorithmfor the full state machine.↩
2. With streaming SSR and Suspense, the server may render multiple chunks, but each chunk is still a single-pass render with no reactive updates. SeerenderToPipeableStreamin the React documentation.↩
3. Structural sharing is a pattern from immutable data libraries (Immer, React Query, TanStack Store) where unchanged portions of data structures are reused by reference to enable cheap equality checks. SeeStructural Sharingin the TanStack Query documentation.↩
4. Conditional exports are a Node.js feature that allows packages to define different entry points based on environment or import method. SeeConditional exportsin the Node.js documentation.↩
5. Dead code elimination is a standard compiler optimization. See esbuild's documentation ontree shaking, Rollup'stree-shaking guideand Rich Harris's article ondead code elimination.↩
6. V8 team,Fast properties in V8. Great article, but 9 years old so things might have changed.↩
7. WebKit,A Tour of Inline Caching with Delete↩
8. Event-loop utilization is the percentage of time the event loop is busy utilizing the CPU. See thisnodesource blog postfor more details.↩
9. To get a reference for the values we were measuring, we ran a similarautocannonbenchmark on the smallest possible Node HTTP server:require('http').createServer((q,s)=>s.end()).listen(3000). This tells us thetheoreticalmaximum throughput of the machine and test setup.↩

Edit on GitHub
Partners
Libraries
Start
Router
Query
Table
Form
DB
AI
Intent

Latest Posts
We Removed 3rd Party Ads from TanStack.com
Mar 24, 2026
5x SSR Throughput: Profiling SSR Hot Paths in TanStack Start
Mar 17, 2026
Lazy Tool Discovery: Scaling AI Tool Systems Without Drowning in Tokens
Mar 12, 2026
