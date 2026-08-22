---
title: Bun 1.4 | Bun Blog
url: https://bun.com/blog/bun-v1.4
site_name: tldr
content_file: tldr-bun-14-bun-blog
fetched_at: '2026-08-23T06:00:35.784510'
original_url: https://bun.com/blog/bun-v1.4
date: '2026-08-23'
published_date: '2026-08-20T00:53:44.000Z'
description: Bun 1.4 rewrites Bun in Rust, ships built-in headless browser automation (Bun.WebView), Bun.Image, Bun.markdown, JSON5, JSONL, Terminal and cron APIs, Node.js 26.3.0 compatibility with 1,517 newly passing tests, parallel test and run, Windows ARM64, and an opt-in global virtual store for up to 7× faster installs.
tags:
- tldr
---

Bun is the complete toolkit for building and testing full-stack JavaScript and TypeScript applications. If you're new to Bun, you can learn more from theBun 1.0blog post.

curl
powershell
npm
brew
docker

curl

curl -fsSL https://bun.sh/install 
|
 bash

powershell

powershell 
-c
 
"
irm bun.sh/install.ps1 | iex
"

npm

npm install -g bun

brew

brew install oven-sh/bun/bun

docker

docker pull oven/bun

Bun 1.4 adds +1,517 tests from the Node.js test suite - our biggest jump in Node.js compatibility since Bun 1.0. Bun v1.4 also fixes over 2,900 issues. It reduces idle CPU usage by 5x, reduces memory usage by up to 35%, and starts 50% faster on Linux. It addsBun.Image,Bun.WebView,Bun.markdown,Bun.cron(),Bun.Terminal,bun run --parallel,bun test --parallel,bun audit fix,bun dedupe, andbun prune. And it rewrites Bun from Zig to Rust.

This post covers everything we've shipped since Bun 1.3.0 (with new to Bun v1.4 tagged).

To upgrade:

bun upgrade

## Node.js compatibility#

Bun is designed to be a drop-in replacement for Node.js. We've added +1,517 tests from the Node.js test suite to run on every commit of Bun.

node:http,node:fs,node:cluster,node:timers,node:zlib,node:vm, andnode:streampass 97% of Node's own tests;node:quic99%;node:events,node:trace_events, andnode:sqlite100%.

Node.js v26.3.0
 test suite · passing on every commit
+
1,517
newly passing tests
▶ play
↻ replay
▶ play
quic
235
 / 
237
+
235
http
rewritten
403
 / 
415
+
193
fs
349
 / 
358
+
133
tls
191
 / 
224
+
106
http2
rewritten
261
 / 
280
+
102
repl
82
 / 
109
+
77
stream
254
 / 
262
+
61
worker
116
 / 
157
+
57
process
160
 / 
190
+
45
net
171
 / 
191
+
39
https
61
 / 
65
+
39
internal
68
 / 
108
+
35
cluster
85
 / 
88
+
31
trace_events
30
 / 
30
+
30
webcrypto
39
 / 
50
+
28
crypto
123
 / 
135
+
27
vm
98
 / 
101
+
25
webstreams
28
 / 
38
+
23
test_runner
28
 / 
81
+
21
module
68
 / 
93
+
19
diagnostics_channel
36
 / 
69
+
19
sqlite
18
 / 
18
+
18
child_process
105
 / 
116
+
15
inspector
22
 / 
110
+
14
Per-module pass counts from Bun’s vendored copy of Node’s
 
test/parallel
 suite, Bun 1.3 → 1.4. The tick marks the 1.3 baseline.

Bun is not 100% compatible with Node.js yet. In practice, much of the existing JavaScript ecosystem just works. You can more closelytrack Bun's Node.js test suite progress here.

### Playwrightv1.4.0#

Playwright now runs on Bun: drive a browser withconnectOverCDP(), run your suite withplaywright testand aplaywright.config.ts, open--ui, and launch Chromium on Windows.

### Next.js 16v1.3.2#

bun --bun next buildworks on Next.js 16.3 with Turbopack and the React Compiler.

### vitestv1.4.0#

vitest runs under Bun, including--coverage, with the threads and forks pools.

### OpenTelemetryv1.4.0#

OpenTelemetry's http and fs instrumentation export spans, andshimmerandrequire-in-the-middlepatch bundled code.

### dd-tracev1.4.0#

dd-tracetraces and@datadog/pprofprofiles continuously; the V8 C++ APIs they link against are implemented.

### Additional Node.js compatibility improvements#

Every day, Bun gets closer to 100% Node.js compatibility. More packages now work in Bun without changes:

* Nuxt:nuxt devconnects HMR and the Nuxt DevTools.
* testcontainersanddockerode:container.exec()works.
* https-proxy-agentandsocks-proxy-agent:http.request()tunnels through them.
* crawlee: crawls throughproxy-chain.
* @grpc/grpc-jsandConnectRPC: servers behind Envoy and clients behind AWS ALB work.
* amqplib: connects to RabbitMQ.
* @aws-sdk/client-s3: streaming uploads work.
* TypeORM: starts with the decorator settings in yourtsconfig.json.
* nock: interceptshttpandhttpsrequests.
* Fastifyinject()andlight-my-request: work.
* happy-dom: no longer breaksconsole.log.
* piscina: runs.

New Node.js APIs in Bun:

* worker_threads:resourceLimits,stdout,stderr, andevaloptions.
* ws:'upgrade'and'unexpected-response'events.
* socket.upgradeTLS({ isServer: true }): server-side STARTTLS.
* node:cluster: shares listening sockets between workers.
* node:repl,node:trace_events,node:domain: implemented.

## Production#

Bun v1.4 uses less memory, less CPU, and starts faster.

Until Bun v1.4, Bun used two memory allocators - JavaScriptCore's libpas allocator and mimalloc. JavaScriptCore in Bun now uses mimalloc (improving memory reclamation), and we've extended mimalloc with features like partial page clearing, a scavenger thread that frees memory while JavaScript idles, and improved lazy zeroing.

### CPU usage#

For Claude Code, a large long-running application built on Bun, production CPU usage dropped by 2×: p99 from 24% to 10%, p50 from 5.8% to 2.5%.

For a small "hello world" app, idle CPU usage drops by 5x.

We did this by optimizing when garbage collector timers request a GC, switching how JavaScriptCore visits Strong roots from a linked list to a linked list of segmented arrays, and reducing the number offutexcalls, along with the mimalloc changes mentioned earlier.

### Memory usage#

Applications using HTTP servers with Bun should see a 13% - 48% memory usage reduction.

Peak memory under load (1,000,000 requests with 64 connections; 100,000 for Next.js and Vite):

Server
Bun 1.4
Bun 1.3
Node.js 26
Δ vs Bun 1.3
fastify
120 MB
233 MB
156 MB
−48%
Express
92 MB
169 MB
145 MB
−46%
node:http
81 MB
135 MB
107 MB
−40%
Elysia
55 MB
91 MB
n/a
−40%
Next.js
285 MB
397 MB
342 MB
−28%
Bun.serve
36 MB
45 MB
n/a
−20%
Vite dev server
233 MB
268 MB
214 MB
−13%

Server-side rendering with Next.js gets a bigger reduction. On a common App Router pattern that grew without bound in 1.3 (React.cache+no-storefetch in a dynamic route), Bun 1.4 settles at 238 MB over 4,000 pages, under Node's 410 MB.

Next.js App Router SSR, 4,000 pages: Bun 1.4 settles at 238 MB, under Node's 410 MB.

### Startup#

On Windows, Bun starts 2.5× faster.

hello.js
 on Windows
Bun 1.4
Bun 1.3.14
Node.js 26
Startup time
15.5 ms
39.0 ms
40.1 ms
Peak memory
16.8 MB
46.5 MB
32.5 MB

On Linux, Bun starts 2× faster and uses less than half the memory.

hello.js
 on Linux
Bun 1.4
Bun 1.3
Node.js 26
Startup time
5.1 ms
10.9 ms
27.2 ms
Peak memory
14.6 MB
33.0 MB
44.5 MB

### Binary size#

On Linux and Windows, Bun gets up to 17% smaller.

Bun 1.4
Bun 1.3.14
Linux x64
77.0 MB
88.5 MB
Linux arm64
76.8 MB
87.6 MB
Windows x64
84.8 MB
93.9 MB
Windows arm64
75.1 MB
90.2 MB
macOS arm64
61.2 MB
60.2 MB
macOS x64
66.6 MB
66.0 MB

macOS binaries are about 1 MB larger.

### Observability#

The tools you already use work with Bun 1.4.

* bun --cpu-profwrites a.cpuprofile. Open it in Chrome DevTools or VS Code.
* bun --heap-profwrites a V8-compatible.heapsnapshot. Open it in Chrome DevTools.
* node:inspector: aSessioncan start and stop a CPU profile while the app runs, withProfiler.startandProfiler.stop.#25939
* Datadog:dd-tracetraces requests and@datadog/pprofprofiles CPU continuously.#36747
* OpenTelemetry: the@opentelemetry/instrumentation-httpand@opentelemetry/instrumentation-fspackages from npm work withnode:httpandnode:fsin Bun. Theshimmerandrequire-in-the-middlepackages they depend on can patch bundled code.
* Async stack traces: an error fromfs.promises,fetch(), S3, DNS, or crypto points at theawaitin your code, not at native frames.

Some of it is new in Bun.

#### --cpu-prof-md

--cpu-prof-mdwrites a CPU profile as Markdown, so you can find the hot function from a terminal: the top functions by self time, the call tree, and who calls whom. Read it over SSH,grepit, paste it into a bug report, or hand it to an LLM.

bun --cpu-prof-md ./app.ts
# CPU Profile

| Duration | Samples | Interval | Functions |

| -------- | ------- | -------- | --------- |

| 304.9ms | 279 | 1.0ms | 6 |

**Top 10:**
 
`tokenize`
 39.1%, 
`escapeHtml`
 25.6%, 
`escapeHtml`
 19.3%, 
`render`
 15.8%

## Hot Functions (Self Time)

| Self% | Self | Total% | Total | Function | Location |

| ----: | ------: | -----: | ------: | ------------ | ----------- |

| 39.1% | 119.4ms | 39.1% | 119.4ms | 
`tokenize`
 | 
`app.ts:14`
 |

| 25.6% | 78.1ms | 25.6% | 78.1ms | 
`escapeHtml`
 | 
`app.ts:5`
 |

| 19.3% | 58.9ms | 19.3% | 58.9ms | 
`escapeHtml`
 | 
`app.ts:4`
 |

| 15.8% | 48.3ms | 60.8% | 185.3ms | 
`render`
 | 
`app.ts:21`
 |

## Call Tree (Total Time)

| Total% | Total | Self% | Self | Function | Location |

| -----: | ------: | ----: | ------: | ------------ | ----------- |

| 60.8% | 185.3ms | 15.8% | 48.3ms | 
`render`
 | 
`app.ts:21`
 |

| 60.8% | 185.3ms | 0.0% | 0us | 
`(module)`
 | 
`app.ts:30`
 |

| 39.1% | 119.4ms | 39.1% | 119.4ms | 
`tokenize`
 | 
`app.ts:14`
 |

| 39.1% | 119.4ms | 0.0% | 0us | 
`(module)`
 | 
`app.ts:28`
 |

| 25.6% | 78.1ms | 25.6% | 78.1ms | 
`escapeHtml`
 | 
`app.ts:5`
 |

| 19.3% | 58.9ms | 19.3% | 58.9ms | 
`escapeHtml`
 | 
`app.ts:4`
 |

## Function Details

### 
`tokenize`

`app.ts:14`
 | Self: 39.1% (119.4ms) | Total: 39.1% (119.4ms) | Samples: 109

**Called by:**

- 
`(module)`
 (109)

### 
`escapeHtml`

`app.ts:5`
 | Self: 25.6% (78.1ms) | Total: 25.6% (78.1ms) | Samples: 72

**Called by:**

- 
`render`
 (72)

### 
`escapeHtml`

`app.ts:4`
 | Self: 19.3% (58.9ms) | Total: 19.3% (58.9ms) | Samples: 54

**Called by:**

- 
`render`
 (54)

### 
`render`

`app.ts:21`
 | Self: 15.8% (48.3ms) | Total: 60.8% (185.3ms) | Samples: 44

**Called by:**

- 
`(module)`
 (170)

**Calls:**

- 
`escapeHtml`
 (72)

- 
`escapeHtml`
 (54)

### 
`(module)`

`app.ts:28`
 | Self: 0.0% (0us) | Total: 39.1% (119.4ms) | Samples: 0
Expand

BUN_CPU_PROFILE=1turns on the CPU profiler for a process you cannot pass flags to, like a worker started by a framework.

#### --heap-prof-md

--heap-prof-mdwrites a heap profile as Markdown, so you can find what is holding memory from a terminal: total size, the types that retain the most, the largest objects, and the chains that keep them alive.

bun --heap-prof-md ./app.ts
# Bun Heap Profile

Generated by 
`bun --heap-prof-md`
. This profile contains complete heap data in markdown format.

**Quick Search Commands:**

```bash

grep 
'
| `Function`
'
 file.md 
# Find all Function objects

grep 
'
gcroot=1
'
 file.md 
# Find all GC roots

grep 
'
| 12345 |
'
 file.md 
# Find object #12345 or edges involving it

```

---

## Summary

| Metric | Value |

| --------------- | ---------------------: |

| Total Heap Size | 4.2 MB (4507930 bytes) |

| Total Objects | 121116 |

| Total Edges | 244084 |

| Unique Types | 67 |

| GC Roots | 427 |

## Top 50 Types by Retained Size

| Rank | Type | Count | Self Size | Retained Size | Largest Instance |

| ---: | ---------------------------- | -----: | --------: | ------------: | ---------------: |

| 1 | 
`<root>`
 | 1 | 0 B | 4.2 MB | 4.2 MB |

| 2 | 
`string`
 | 119883 | 4.1 MB | 4.1 MB | 67 B |

| 3 | 
`GlobalObject`
 | 1 | 10.3 KB | 83.1 KB | 83.1 KB |

| 4 | 
`Function`
 | 319 | 10.3 KB | 61.5 KB | 13.9 KB |

| 5 | 
`Structure`
 | 216 | 23.6 KB | 35.7 KB | 944 B |

| 6 | 
`FunctionExecutable`
 | 72 | 9.0 KB | 32.0 KB | 13.9 KB |

| 7 | 
`ModuleLoader`
 | 1 | 32 B | 20.1 KB | 20.1 KB |

| 8 | 
`ModuleRecord`
 | 2 | 3.0 KB | 19.4 KB | 15.3 KB |

| 9 | 
`NativeExecutable`
 | 228 | 17.8 KB | 17.8 KB | 80 B |

| 10 | 
`JSModuleEnvironment`
 | 2 | 128 B | 16.3 KB | 14.0 KB |

| 11 | 
`FunctionCodeBlock`
 | 5 | 12.3 KB | 12.3 KB | 4.1 KB |

| 12 | 
`ModuleProgramExecutable`
 | 2 | 224 B | 10.3 KB | 8.7 KB |

| 13 | 
`ModuleProgramCodeBlock`
 | 2 | 2.5 KB | 10.1 KB | 8.6 KB |

| 14 | 
`UnlinkedFunctionExecutable`
 | 69 | 6.4 KB | 6.4 KB | 96 B |

| 15 | 
`Array`
 | 61 | 1.0 KB | 6.1 KB | 5.1 KB |

| 16 | 
`console`
 | 1 | 48 B | 4.4 KB | 4.4 KB |

| 17 | 
`String`
 | 1 | 74 B | 4.3 KB | 4.3 KB |

| 18 | 
`Map`
 | 3 | 105 B | 4.2 KB | 2.6 KB |

| 19 | 
`GetterSetter`
 | 29 | 928 B | 3.7 KB | 256 B |

| 20 | 
`Iterator`
 | 2 | 54 B | 3.3 KB | 2.7 KB |
Expand

#### bun build --metafile-md

bun build --metafile-mdwrites the bundle analysis as Markdown, so you can see why a bundle is big: the largest modules, what each entry point loads, and the chain of imports that pulled each file in.

bun build ./src/index.ts --outdir ./dist --metafile-md=./dist/meta.md
# Bundle Analysis Report

This report helps identify bundle size issues, dependency bloat, and optimization opportunities.

## Table of Contents

- [
Quick Summary
](
#quick-summary
)

- [
Largest Modules by Output Contribution
](
#largest-modules-by-output-contribution
)

- [
Entry Point Analysis
](
#entry-point-analysis
)

- [
Dependency Chains
](
#dependency-chains
)

- [
Full Module Graph
](
#full-module-graph
)

- [
Raw Data for Searching
](
#raw-data-for-searching
)

---

## Quick Summary

| Metric | Value |

| ------------------------- | ------------------ |

| Total output size | 56.1 KB |

| Input modules | 4 |

| Entry points | 1 |

| node_modules contribution | 1 files (55.74 KB) |

| ESM modules | 4 |

## Largest Modules by Output Contribution

Modules sorted by bytes contributed to the output bundle. Large modules may indicate bloat.

| Output Bytes | % of Total | Module | Format |

| ------------ | ---------- | --------------------------------------- | ------ |

| 55.74 KB | 99.4% | 
`node_modules/marked/lib/marked.esm.js`
 | esm |

| 113 bytes | 0.2% | 
`src/escape.ts`
 | esm |

| 76 bytes | 0.1% | 
`src/render.ts`
 | esm |

| 52 bytes | 0.1% | 
`src/index.ts`
 | esm |

## Entry Point Analysis

Each entry point and the total code it loads (including shared chunks).

### Entry: 
`src/index.ts`

**Output file**
: 
`./index.js`

**Bundle size**
: 56.1 KB

**Exports**
: 
`main`

**Bundled modules**
 (sorted by contribution):

| Bytes | Module |

| --------- | --------------------------------------- |

| 55.74 KB | 
`node_modules/marked/lib/marked.esm.js`
 |

| 113 bytes | 
`src/escape.ts`
 |

| 76 bytes | 
`src/render.ts`
 |

| 52 bytes | 
`src/index.ts`
 |

## Dependency Chains

For each module, shows what files import it. Use this to understand why a module is included.

### Most Commonly Imported Modules

Modules imported by many files. Extracting these to shared chunks may help.

| Import Count | Module | Imported By |

| ------------ | ------ | ----------- |

## Full Module Graph

Complete dependency information for each module.

### 
`node_modules/marked/lib/marked.esm.js`

- 
**Output contribution**
: 55.74 KB

- 
**Format**
: esm

- 
**Imported by**
 (1 files): 
`src/index.ts`
Expand

#### process.on("memoryPressure")

When the operating system is running low on memory, it notifies Bun, and Bun emits"memoryPressure"onprocess. Use it to free memory before the OS kills your process: clear a cache, close idle connections, stop idle workers. It works on macOS, Linux, and Windows.

process.
on
(
"
memoryPressure
"
, (
level
) 
=>
 {

 cache.
clear
();

 pool.
drainIdle
();

});
* macOS:kqueuewithEVFILT_MEMORYSTATUS, the same event libdispatch uses forDISPATCH_SOURCE_TYPE_MEMORYPRESSURE.levelis"warning"or"critical".
* Linux: a PSI trigger written to/proc/pressure/memory(or the cgroup'smemory.pressure), watched withepollforEPOLLPRI.levelis"critical".
* Windows:CreateMemoryResourceNotification(LowMemoryResourceNotification), waited on withRegisterWaitForSingleObject.levelis"critical".

### Streams and bodies#

ReadableStream,WritableStream, andTransformStreamare now native. They use less memory, run faster, and pass 100% of the Web Platform Tests.

Four pipelines, each moving 64 MB in 4 KB chunks:

* Download:fetch()→DecompressionStream("gzip")→TextDecoderStream→for await
* Upload:fs.createReadStream()→CompressionStream("gzip")→fetch()POST body
* Transcode:fs.createReadStream()→TextDecoderStream→TextEncoderStream→fs.createWriteStream()
* Subprocess:fetch()body →catstdin, thencatstdout →for await

Throughput:

Pipeline
Bun 1.4
Bun 1.3
Node.js 26
Deno 2.9
Download
1,519 MB/s
n/a
204 MB/s
530 MB/s
Upload
179 MB/s
n/a
78 MB/s
137 MB/s
Transcode
132 MB/s
116 MB/s
52 MB/s
91 MB/s
Subprocess
751 MB/s
505 MB/s
256 MB/s
170 MB/s

Peak memory:

Pipeline
Bun 1.4
Bun 1.3
Node.js 26.7
Deno 2.9
Download
57 MB
n/a
86 MB
64 MB
Upload
60 MB
n/a
84 MB
61 MB
Transcode
62 MB
92 MB
72 MB
57 MB
Subprocess
65 MB
207 MB
106 MB
114 MB

All four runtimes run the same script. The file streams useReadable.toWeb()andWritable.toWeb()fromnode:stream. Bun 1.3 is missingCompressionStreamandDecompressionStream, so those rows are n/a.

Benchmark code: native-pipeline.mjs and serve-body.mjs
// End-to-end pipelines between native stream types (fetch body, DecompressionStream, TextDecoderStream,

// file streams via node:stream Readable/Writable.toWeb, child_process pipes). Portable: Bun, Node, Deno.

// Run: <runtime> native-pipeline.mjs --scenario=prep (writes the 64 MiB fixture files once)

// <runtime> native-pipeline.mjs --scenario=download-gunzip-decode --server=http://127.0.0.1:39872

// <runtime> native-pipeline.mjs --scenario=file-gzip-upload --server=http://127.0.0.1:39872

// <runtime> native-pipeline.mjs --scenario=file-decode-encode-file

// <runtime> native-pipeline.mjs --scenario=spawn-passthrough --server=http://127.0.0.1:39872

// Server: `bun run serve-body.mjs --gzip`. 64 MiB payloads/files, 4 KiB chunks end to end. Wrap in /usr/bin/time -v for peak RSS.

import
 fs 
from
 
"
node:fs
"
;

import
 { Readable, Writable } 
from
 
"
node:stream
"
;

import
 { spawn } 
from
 
"
node:child_process
"
;

const
 MB 
=
 
1024
 
*
 
1024
;

const
 CHUNK 
=
 
4096
;

const
 BYTES 
=
 
64
 
*
 MB;

const
 argv 
=
 globalThis.process?.argv 
??
 [];

const
 
arg
 
=
 (
k
, 
d
) 
=>

 argv.
find
((
a
) 
=>
 a.
startsWith
(
`--
${
k
}
=`
))?.
slice
(k.length 
+
 
3
) 
??
 d;

const
 scenario 
=
 
arg
(
"
scenario
"
, 
"
prep
"
);

const
 server 
=
 
arg
(
"
server
"
);

const
 dir 
=
 
arg
(
"
dir
"
, 
"
/tmp/native-pipeline
"
);

const
 JSON_FILE 
=
 
`
${
dir
}
/json-64mb.txt`
;

const
 UTF8_FILE 
=
 
`
${
dir
}
/utf8-64mb.txt`
;

const
 OUT_FILE 
=
 
`
${
dir
}
/out-
${
scenario
}
.txt`
;

const
 jsonTemplate 
=
 
new
 
TextEncoder
()

 .
encode
(

 
JSON
.
stringify
({

 messages
:
 
Array
.
from
({ length
:
 
700
 }, (
_
, 
i
) 
=>
 ({

 id
:
 i,

 role
:
 i 
%
 
2
 
?
 
"
assistant
"
 
:
 
"
user
"
,

 ts
:
 
1700000000
 
+
 i,

 body
:
 
"
the quick brown fox jumps over the lazy dog 
"
 
+
 i,

 })),

 }),

 )

 .
slice
(
0
, CHUNK);

const
 
utf8Text
 
=
 (

 
"
hello world 
\u{1F30A}
 stream ✨ café naïve 中文 
"
 
+
 
"
x
"
.
repeat
(
40
)

).
repeat
(
2000
);

const
 utf8Template 
=
 
new
 
TextEncoder
().
encode
(utf8Text).
slice
(
0
, CHUNK);

// Keep the UTF-8 fixture valid at 64 KiB chunk boundaries: cut the template at a char boundary.

const
 utf8Chunk 
=
 (() 
=>
 {

 
let
 end 
=
 utf8Template.byteLength;

 
while
 ((utf8Template[end 
-
 
1
] 
&
 
0xc0
) 
===
 
0x80
) end
--
;

 
if
 (end 
<
 utf8Template.byteLength) end
--
; 
// drop the lead byte of the truncated char too

 
return
 utf8Template.
slice
(
0
, end);

})();

const
 
countBytes
 
=
 
async
 (
rs
) 
=>
 {

 
let
 n 
=
 
0
;

 
for
 
await
 (
const
 v 
of
 rs)

 n 
+=
 
typeof
 v 
===
 
"
string
"
 
?
 v.length 
:
 v.byteLength;

 
return
 n;

};

async
 
function
 
prep
() {

 fs.
mkdirSync
(dir, { recursive
:
 
true
 });

 
const
 
write
 
=
 (
path
, 
template
, 
varyByte
) 
=>
 {

 
if
 (fs.
existsSync
(path) 
&&
 fs.
statSync
(path).size 
===
 BYTES) 
return
;

 
const
 fd 
=
 fs.
openSync
(path, 
"
w
"
);

 
let
 written 
=
 
0
,

 i 
=
 
0
;

 
const
 buf 
=
 
new
 
Uint8Array
(template.byteLength);

 
while
 (written 
<
 BYTES) {

 buf.
set
(template);

 
if
 (varyByte) buf[
0
] 
=
 
32
 
+
 (i
++
 
&
 
63
);

 fs.
writeSync
(fd, buf);

 written 
+=
 buf.byteLength;

 }

 fs.
closeSync
(fd);

 console.
log
(
`wrote 
${
path
}
 (
${
(written
 
/
 
MB).
toFixed
(
0
)
}
 MiB)`
);

 };

 
write
(JSON_FILE, jsonTemplate, 
true
);

 
write
(UTF8_FILE, utf8Chunk, 
false
);

}

const
 scenarios 
=
 {

 
// fetch(gzip body) -> DecompressionStream -> TextDecoderStream -> for await (count chars). MB/s over decompressed bytes.

 
"
download-gunzip-decode
"
:
 
async
 () 
=>
 {

 
const
 res 
=
 
await
 
fetch
(
`
${
server
}
/gzip`
);

 
const
 expected 
=
 
+
res.headers.
get
(
"
x-uncompressed-length
"
);

 
const
 chars 
=
 
await
 
countBytes
(

 res.body

 .
pipeThrough
(
new
 
DecompressionStream
(
"
gzip
"
))

 .
pipeThrough
(
new
 
TextDecoderStream
()),

 );

 
if
 (chars 
!==
 expected)

 
throw
 
new
 
Error
(

 
`decoded 
${
chars
}
 chars, expected 
${
expected
}
 (ASCII payload)`
,

 );

 
return
 expected;

 },

 
// fs.createReadStream(64 MiB, 4 KiB reads) -> CompressionStream -> fetch POST body; server returns bytes received. MB/s over input bytes.

 
"
file-gzip-upload
"
:
 
async
 () 
=>
 {

 
const
 body 
=
 Readable.
toWeb
(

 fs.
createReadStream
(JSON_FILE, { highWaterMark
:
 CHUNK }),

 ).
pipeThrough
(
new
 
CompressionStream
(
"
gzip
"
));

 
const
 res 
=
 
await
 
fetch
(
`
${
server
}
/upload`
, {

 method
:
 
"
POST
"
,

 body,

 duplex
:
 
"
half
"
,

 });

 
const
 received 
=
 
+
(
await
 res.
text
());

 
if
 (
!
(received 
>
 
0
 
&&
 received 
<
 BYTES))

 
throw
 
new
 
Error
(
`server received 
${
received
}
 bytes`
);

 
return
 fs.
statSync
(JSON_FILE).size;

 },

 
// fs.createReadStream(64 MiB utf-8, 4 KiB reads) -> TextDecoderStream -> TextEncoderStream -> fs.createWriteStream. MB/s over file bytes.

 
"
file-decode-encode-file
"
:
 
async
 () 
=>
 {

 
await
 Readable.
toWeb
(

 fs.
createReadStream
(UTF8_FILE, { highWaterMark
:
 CHUNK }),

 )

 .
pipeThrough
(
new
 
TextDecoderStream
())

 .
pipeThrough
(
new
 
TextEncoderStream
())

 .
pipeTo
(Writable.
toWeb
(fs.
createWriteStream
(OUT_FILE)));

 
const
 n 
=
 fs.
statSync
(OUT_FILE).size;

 
if
 (n 
!==
 fs.
statSync
(UTF8_FILE).size) 
throw
 
new
 
Error
(
`wrote 
${
n
}
 bytes`
);

 fs.
unlinkSync
(OUT_FILE);

 
return
 n;

 },

 
// fetch(64 MiB body in 4 KiB chunks).body -> cat stdin ; cat stdout -> for await. MB/s over body bytes.

 
"
spawn-passthrough
"
:
 
async
 () 
=>
 {

 
const
 child 
=
 
spawn
(
"
cat
"
, [], { stdio
:
 [
"
pipe
"
, 
"
pipe
"
, 
"
inherit
"
] });

 
const
 res 
=
 
await
 
fetch
(
`
${
server
}
/?bytes=
${
BYTES
}
&chunk=
${
CHUNK
}
`
);

 
const
 [, n] 
=
 
await
 
Promise
.
all
([

 res.body.
pipeTo
(Writable.
toWeb
(child.stdin)),

 
countBytes
(Readable.
toWeb
(child.stdout)),

 ]);

 
await
 
new
 
Promise
((
r
) 
=>
 child.
on
(
"
close
"
, r));

 
if
 (n 
!==
 BYTES) 
throw
 
new
 
Error
(
`got 
${
n
}
 bytes from cat`
);

 
return
 n;

 },

};

if
 (scenario 
===
 
"
prep
"
) {

 
await
 
prep
();

} 
else
 {

 
const
 fn 
=
 scenarios[scenario];

 
if
 (
!
fn)

 
throw
 
new
 
Error
(

 
`unknown --scenario=
${
scenario
}
; prep | 
${
Object
.
keys
(scenarios).
join
(

 
"
 | 
"
,

 
)
}
`
,

 );

 
if
 (scenario 
!==
 
"
file-decode-encode-file
"
 
&&
 
!
server)

 
throw
 
new
 
Error
(
"
--server=URL required (bun run serve-body.mjs --gzip)
"
);

 
const
 t0 
=
 performance.
now
();

 
const
 bytes 
=
 
await
 
fn
();

 
const
 ms 
=
 performance.
now
() 
-
 t0;

 console.
log
(

 
`
${
scenario.
padEnd
(
26
)
}
 
${
(bytes
 
/
 
MB
 
/
 
(ms
 
/
 
1000
))

 
.
toFixed
(
0
)

 
.
padStart
(
6
)
}
 MB/s 
${
ms.
toFixed
(
0
).
padStart
(
6
)
}
 ms 
${
(

 
bytes
 
/
 
MB

 
).
toFixed
(
0
)
}
 MiB`
,

 );

}
// Streaming-body server for streams-throughput.mjs --scenario=fetch and native-pipeline.mjs.

// Run: bun run serve-body.mjs [--gzip] (listens on 127.0.0.1:39872)

// GET /?bytes=N&chunk=C fresh C-byte chunks (default 65536), N bytes total

// GET /gzip 64 MiB of JSON-like text gzip-compressed once at startup (--gzip), served in 4 KiB chunks,

// no content-encoding header (the client decompresses explicitly)

// POST /upload drains the request body, responds with the byte count

const
 MB 
=
 
1024
 
*
 
1024
;

const
 CHUNK 
=
 
64
 
*
 
1024
;

const
 argv 
=
 process.argv;

const
 GZIP_BYTES 
=
 
64
 
*
 MB;

const
 GZIP_CHUNK 
=
 
4096
;

const
 jsonTemplate 
=
 
new
 
TextEncoder
()

 .
encode
(

 
JSON
.
stringify
({

 messages
:
 
Array
.
from
({ length
:
 
700
 }, (
_
, 
i
) 
=>
 ({

 id
:
 i,

 role
:
 i 
%
 
2
 
?
 
"
assistant
"
 
:
 
"
user
"
,

 ts
:
 
1700000000
 
+
 i,

 body
:
 
"
the quick brown fox jumps over the lazy dog 
"
 
+
 i,

 })),

 }),

 )

 .
slice
(
0
, CHUNK);

const
 
jsonSource
 
=
 (
total
) 
=>
 {

 
const
 count 
=
 
Math
.
ceil
(total 
/
 CHUNK);

 
let
 i 
=
 
0
;

 
return
 
new
 
ReadableStream
({

 
pull
(
c
) {

 
if
 (i 
<
 count) {

 
const
 b 
=
 
new
 
Uint8Array
(CHUNK);

 b.
set
(jsonTemplate);

 b[
0
] 
=
 
32
 
+
 (i
++
 
&
 
63
);

 c.
enqueue
(b);

 } 
else
 c.
close
();

 },

 });

};

let
 gzipped 
=
 
null
;

if
 (argv.
includes
(
"
--gzip
"
)) {

 
const
 t0 
=
 performance.
now
();

 gzipped 
=
 
new
 
Uint8Array
(

 
await
 
new
 
Response
(

 
jsonSource
(GZIP_BYTES).
pipeThrough
(
new
 
CompressionStream
(
"
gzip
"
)),

 ).
arrayBuffer
(),

 );

 console.
log
(

 
`pre-compressed 
${
GZIP_BYTES
 
/
 
MB
}
 MiB -> 
${
(

 
gzipped.byteLength
 
/
 
MB

 
).
toFixed
(
1
)
}
 MiB gzip in 
${
(performance.
now
()
 
-
 
t0).
toFixed
(
0
)
}
 ms`
,

 );

}

Bun.
serve
({

 port
:
 
39872
,

 hostname
:
 
"
127.0.0.1
"
,

 idleTimeout
:
 
255
,

 maxRequestBodySize
:
 
8
 
*
 
1024
 
*
 MB,

 
async
 
fetch
(
req
) {

 
const
 url 
=
 
new
 
URL
(req.url);

 
if
 (req.method 
===
 
"
POST
"
 
&&
 url.pathname 
===
 
"
/upload
"
) {

 
let
 n 
=
 
0
;

 
for
 
await
 (
const
 c 
of
 req.body) n 
+=
 c.byteLength;

 
return
 
new
 
Response
(
String
(n));

 }

 
if
 (url.pathname 
===
 
"
/gzip
"
) {

 
if
 (
!
gzipped) 
return
 
new
 
Response
(
"
start with --gzip
"
, { status
:
 
500
 });

 
let
 off 
=
 
0
;

 
const
 body 
=
 
new
 
ReadableStream
({

 
pull
(
c
) {

 
if
 (off 
<
 gzipped.byteLength) {

 c.
enqueue
(

 gzipped.
slice
(

 off,

 
Math
.
min
(off 
+
 GZIP_CHUNK, gzipped.byteLength),

 ),

 );

 off 
+=
 GZIP_CHUNK;

 } 
else
 c.
close
();

 },

 });

 
return
 
new
 
Response
(body, {

 headers
:
 {

 
"
content-type
"
:
 
"
application/gzip
"
,

 
"
x-uncompressed-length
"
:
 
String
(GZIP_BYTES),

 },

 });

 }

 
const
 total 
=
 
+
url.searchParams.
get
(
"
bytes
"
);

 
const
 chunk 
=
 
+
(url.searchParams.
get
(
"
chunk
"
) 
??
 CHUNK);

 
const
 count 
=
 
Math
.
ceil
(total 
/
 chunk);

 
let
 i 
=
 
0
;

 
const
 body 
=
 
new
 
ReadableStream
({

 
pull
(
c
) {

 
if
 (i 
<
 count) c.
enqueue
(
new
 
Uint8Array
(chunk).
fill
(i
++
 
&
 
0xff
));

 
else
 c.
close
();

 },

 });

 
return
 
new
 
Response
(body, { headers
:
 { 
"
content-length
"
:
 
String
(total) } });

 },

});

console.
log
(
"
listening on http://127.0.0.1:39872
"
);

Response.clone()andRequest.clone()no longer copy every chunk into the second branch. The clone shares the body's chunks with the original.

A 64 MB streaming body,res.clone(), then read both bodies:

Runtime
Peak memory
Time
Bun 1.4
220 MB
96 ms
Bun 1.3
311 MB
129 ms
Node.js 26
382 MB
230 ms
Deno 2.9
297 MB
134 ms

Reading only the clone, and never the original:

Runtime
Peak memory
Time
Bun 1.4
155 MB
63 ms
Bun 1.3
243 MB
98 ms
Node.js 26
318 MB
162 ms
Deno 2.9
233 MB
104 ms

The twoarrayBuffer()results account for 128 MB of the peak in the first table. Bun 1.4 saves one full copy of the body in both cases.

Benchmark code: response-clone.mjs
// Response.clone() and ReadableStream.tee() with fresh 64 KiB buffers. Peak RSS (via /usr/bin/time -v) is the point.

// Run: bun run response-clone.mjs --scenario=clone-both --bytes=67108864

// node response-clone.mjs --scenario=clone-chain --depth=100 --bytes=104857600

// deno run -A response-clone.mjs --scenario=tee --bytes=2147483648

// clone-both: res.clone(), then read both bodies concurrently.

// clone-only: res.clone(), read only the clone; the original is never read.

// clone-chain: clone a streaming Response N times, read only the last clone.

// tee: split a stream and drain both branches concurrently. MB/s is over the source bytes.

const
 MB 
=
 
1024
 
*
 
1024
;

const
 CHUNK 
=
 
64
 
*
 
1024
;

const
 argv 
=
 globalThis.process?.argv 
??
 [];

const
 
arg
 
=
 (
k
, 
d
) 
=>

 argv.
find
((
a
) 
=>
 a.
startsWith
(
`--
${
k
}
=`
))?.
slice
(k.length 
+
 
3
) 
??
 d;

const
 scenario 
=
 
arg
(
"
scenario
"
, 
"
clone-chain
"
);

const
 DEPTH 
=
 
+
arg
(
"
depth
"
, 
100
);

const
 BYTES 
=
 
+
arg
(

 
"
bytes
"
,

 { 
"
tee
"
:
 
2048
 
*
 MB, 
"
clone-chain
"
:
 
100
 
*
 MB }[scenario] 
??
 
1024
 
*
 MB,

);

const
 
freshSource
 
=
 (
total
) 
=>
 {

 
const
 count 
=
 
Math
.
ceil
(total 
/
 CHUNK);

 
let
 i 
=
 
0
;

 
return
 
new
 
ReadableStream
({

 
pull
(
c
) {

 
if
 (i 
<
 count) c.
enqueue
(
new
 
Uint8Array
(CHUNK).
fill
(i
++
 
&
 
0xff
));

 
else
 c.
close
();

 },

 });

};

const
 
drain
 
=
 
async
 (
rs
) 
=>
 {

 
const
 r 
=
 rs.
getReader
();

 
let
 n 
=
 
0
;

 
for
 (;;) {

 
const
 { done, value } 
=
 
await
 r.
read
();

 
if
 (done) 
return
 n;

 n 
+=
 value.byteLength;

 }

};

const
 scenarios 
=
 {

 
"
clone-both
"
:
 
async
 () 
=>
 {

 
const
 res 
=
 
new
 
Response
(
freshSource
(BYTES));

 
const
 c 
=
 res.
clone
();

 
const
 [a, b] 
=
 
await
 
Promise
.
all
([res.
arrayBuffer
(), c.
arrayBuffer
()]);

 
if
 (a.byteLength 
!==
 b.byteLength) 
throw
 
new
 
Error
(
"
clone mismatch
"
);

 
return
 a.byteLength;

 },

 
"
clone-only
"
:
 
async
 () 
=>
 {

 
const
 res 
=
 
new
 
Response
(
freshSource
(BYTES));

 
const
 c 
=
 res.
clone
();

 
return
 (
await
 c.
arrayBuffer
()).byteLength;

 },

 
"
clone-chain
"
:
 
async
 () 
=>
 {

 
let
 cur 
=
 
new
 
Response
(
freshSource
(BYTES));

 
const
 chain 
=
 [cur];

 
for
 (
let
 i 
=
 
0
; i 
<
 DEPTH; i
++
) chain.
push
((cur 
=
 cur.
clone
()));

 
return
 (
await
 chain.
at
(
-
1
).
arrayBuffer
()).byteLength;

 },

 
"
tee
"
:
 
async
 () 
=>
 {

 
const
 [a, b] 
=
 
freshSource
(BYTES).
tee
();

 
const
 [x, y] 
=
 
await
 
Promise
.
all
([
drain
(a), 
drain
(b)]);

 
if
 (x 
!==
 y) 
throw
 
new
 
Error
(
"
branch mismatch
"
);

 
return
 x;

 },

};

const
 fn 
=
 scenarios[scenario];

if
 (
!
fn)

 
throw
 
new
 
Error
(

 
`unknown --scenario=
${
scenario
}
; clone-both | clone-only | clone-chain | tee`
,

 );

const
 rss0 
=
 globalThis.process?.
memoryUsage
?.().rss 
??
 
0
;

const
 t0 
=
 performance.
now
();

const
 got 
=
 
await
 
fn
();

const
 ms 
=
 performance.
now
() 
-
 t0;

if
 (got 
!==
 BYTES)

 
throw
 
new
 
Error
(
`
${
scenario
}
: read 
${
got
}
 bytes, expected 
${
BYTES
}
`
);

const
 rssDelta 
=
 ((globalThis.process?.
memoryUsage
?.().rss 
??
 
0
) 
-
 rss0) 
/
 MB;

console.
log
(

 
`
${
scenario.
padEnd
(
12
)
}
 
${
(BYTES
 
/
 
MB
 
/
 
(ms
 
/
 
1000
))

 
.
toFixed
(
0
)

 
.
padStart
(
6
)
}
 MB/s 
${
ms.
toFixed
(
0
).
padStart
(
6
)
}
 ms 
${

 
BYTES
 
/
 
MB

 
}
 MiB rss +
${
rssDelta.
toFixed
(
0
)
}
 MB`
,

);

CompressionStream&DecompressionStreamare now implemented natively. Bun 1.3 did not have them.

1 GB of JSON text through a gzip stream, 64 KB chunks:

Stream
Bun 1.4
Node.js 26
Deno 2.9
CompressionStream
152 MB/s
135 MB/s
130 MB/s
DecompressionStream
2,291 MB/s
491 MB/s
679 MB/s

Compression is bound by zlib itself, so the runtimes are close. Decompression is where the native stream path shows.

Benchmark code: compression-stream.mjs
// CompressionStream / DecompressionStream throughput on JSON-like text, generated in fresh 64 KiB chunks.

// Run: bun run compression-stream.mjs --scenario=compress --format=gzip --bytes=1073741824

// node compression-stream.mjs --scenario=decompress --format=deflate

// deno run -A compression-stream.mjs --scenario=compress

// MB/s is over uncompressed bytes. `decompress` compresses the input first (untimed), then times the inflate.

const
 MB 
=
 
1024
 
*
 
1024
;

const
 CHUNK 
=
 
64
 
*
 
1024
;

const
 argv 
=
 globalThis.process?.argv 
??
 [];

const
 
arg
 
=
 (
k
, 
d
) 
=>

 argv.
find
((
a
) 
=>
 a.
startsWith
(
`--
${
k
}
=`
))?.
slice
(k.length 
+
 
3
) 
??
 d;

const
 scenario 
=
 
arg
(
"
scenario
"
, 
"
compress
"
);

const
 format 
=
 
arg
(
"
format
"
, 
"
gzip
"
);

const
 BYTES 
=
 
+
arg
(
"
bytes
"
, 
1024
 
*
 MB);

const
 template 
=
 
new
 
TextEncoder
()

 .
encode
(

 
JSON
.
stringify
({

 messages
:
 
Array
.
from
({ length
:
 
700
 }, (
_
, 
i
) 
=>
 ({

 id
:
 i,

 role
:
 i 
%
 
2
 
?
 
"
assistant
"
 
:
 
"
user
"
,

 ts
:
 
1700000000
 
+
 i,

 body
:
 
"
the quick brown fox jumps over the lazy dog 
"
 
+
 i,

 })),

 }),

 )

 .
slice
(
0
, CHUNK);

const
 
jsonSource
 
=
 (
total
) 
=>
 {

 
const
 count 
=
 
Math
.
ceil
(total 
/
 CHUNK);

 
let
 i 
=
 
0
;

 
return
 
new
 
ReadableStream
({

 
pull
(
c
) {

 
if
 (i 
<
 count) {

 
const
 b 
=
 
new
 
Uint8Array
(CHUNK);

 b.
set
(template);

 b[
0
] 
=
 
32
 
+
 (i
++
 
&
 
63
);

 c.
enqueue
(b);

 } 
else
 c.
close
();

 },

 });

};

const
 
drain
 
=
 
async
 (
rs
) 
=>
 {

 
const
 r 
=
 rs.
getReader
();

 
let
 n 
=
 
0
;

 
for
 (;;) {

 
const
 { done, value } 
=
 
await
 r.
read
();

 
if
 (done) 
return
 n;

 n 
+=
 value.byteLength;

 }

};

const
 
collect
 
=
 
async
 (
rs
) 
=>
 {

 
const
 parts 
=
 [];

 
const
 r 
=
 rs.
getReader
();

 
for
 (;;) {

 
const
 { done, value } 
=
 
await
 r.
read
();

 
if
 (done) 
break
;

 parts.
push
(value);

 }

 
const
 out 
=
 
new
 
Uint8Array
(parts.
reduce
((
n
, 
p
) 
=>
 n 
+
 p.byteLength, 
0
));

 
let
 off 
=
 
0
;

 
for
 (
const
 p 
of
 parts) out.
set
(p, off), (off 
+=
 p.byteLength);

 
return
 out;

};

const
 
chunked
 
=
 (
buf
) 
=>

 
new
 
ReadableStream
({

 
start
(
c
) {

 
for
 (
let
 i 
=
 
0
; i 
<
 buf.byteLength; i 
+=
 CHUNK)

 c.
enqueue
(buf.
subarray
(i, 
Math
.
min
(i 
+
 CHUNK, buf.byteLength)));

 c.
close
();

 },

 });

let
 run;

if
 (scenario 
===
 
"
compress
"
)

 
run
 
=
 () 
=>

 
drain
(
jsonSource
(BYTES).
pipeThrough
(
new
 
CompressionStream
(format)));

else
 
if
 (scenario 
===
 
"
decompress
"
) {

 
const
 compressed 
=
 
await
 
collect
(

 
jsonSource
(BYTES).
pipeThrough
(
new
 
CompressionStream
(format)),

 );

 
run
 
=
 () 
=>

 
drain
(
chunked
(compressed).
pipeThrough
(
new
 
DecompressionStream
(format)));

} 
else
 
throw
 
new
 
Error
(
`unknown --scenario=
${
scenario
}
; compress | decompress`
);

const
 t0 
=
 performance.
now
();

const
 got 
=
 
await
 
run
();

const
 ms 
=
 performance.
now
() 
-
 t0;

if
 (scenario 
===
 
"
decompress
"
 
&&
 got 
!==
 BYTES)

 
throw
 
new
 
Error
(
`inflated 
${
got
}
 bytes, expected 
${
BYTES
}
`
);

console.
log
(

 
`
${
scenario
}
 (
${
format
}
)`
.
padEnd
(
22
) 
+

 
` 
${
(BYTES
 
/
 
MB
 
/
 
(ms
 
/
 
1000
)).
toFixed
(
0
).
padStart
(
6
)
}
 MB/s 
${
ms

 
.
toFixed
(
0
)

 
.
padStart
(
6
)
}
 ms 
${
BYTES
 
/
 
MB
}
 MiB`
,

);

TextDecoderStream&TextEncoderStreamuse about half the memory of Bun 1.3.

Peak memory, 1 GB of mixed UTF-8 text, 64 KB chunks:

Stream
Bun 1.4
Bun 1.3
Node.js 26
Deno 2.9
TextEncoderStream
44 MB
110 MB
182 MB
52 MB
TextDecoderStream
56 MB
119 MB
68 MB
55 MB

Throughput, same run:

Stream
Bun 1.4
Bun 1.3
Node.js 26
Deno 2.9
TextEncoderStream
1,963 MB/s
1,881 MB/s
75 MB/s
612 MB/s
TextDecoderStream
1,489 MB/s
1,507 MB/s
1,540 MB/s
1,059 MB/s
Benchmark code: text-encoder-stream.mjs
// TextEncoderStream / TextDecoderStream throughput on mixed multi-byte UTF-8, fresh 64 KiB chunks.

// Run: bun run text-encoder-stream.mjs --scenario=encode --bytes=1073741824

// node text-encoder-stream.mjs --scenario=decode

// deno run -A text-encoder-stream.mjs --scenario=encode

// MB/s is over UTF-8 bytes (encoder output / decoder input).

const
 MB 
=
 
1024
 
*
 
1024
;

const
 CHUNK 
=
 
64
 
*
 
1024
;

const
 argv 
=
 globalThis.process?.argv 
??
 [];

const
 
arg
 
=
 (
k
, 
d
) 
=>

 argv.
find
((
a
) 
=>
 a.
startsWith
(
`--
${
k
}
=`
))?.
slice
(k.length 
+
 
3
) 
??
 d;

const
 scenario 
=
 
arg
(
"
scenario
"
, 
"
encode
"
);

const
 BYTES 
=
 
+
arg
(
"
bytes
"
, 
1024
 
*
 MB);

const
 
text
 
=
 (

 
"
hello world 
\u{1F30A}
 stream ✨ café naïve 中文 
"
 
+
 
"
x
"
.
repeat
(
40
)

).
repeat
(
2000
);

const
 utf8Template 
=
 
new
 
TextEncoder
().
encode
(text).
slice
(
0
, CHUNK);

const
 stringChunk 
=
 text.
slice
(
0
, CHUNK);

const
 stringChunkBytes 
=
 
new
 
TextEncoder
().
encode
(stringChunk).byteLength;

const
 
stringSource
 
=
 (
total
) 
=>
 {

 
const
 count 
=
 
Math
.
ceil
(total 
/
 stringChunkBytes);

 
let
 i 
=
 
0
;

 
return
 
new
 
ReadableStream
({

 
pull
(
c
) {

 
if
 (i 
<
 count)

 c.
enqueue
(
String
(i
++
 
&
 
0xffff
).
padStart
(
5
, 
"
0
"
) 
+
 stringChunk.
slice
(
5
));

 
else
 c.
close
();

 },

 });

};

const
 
bytesSource
 
=
 (
total
) 
=>
 {

 
const
 count 
=
 
Math
.
ceil
(total 
/
 CHUNK);

 
let
 i 
=
 
0
;

 
return
 
new
 
ReadableStream
({

 
pull
(
c
) {

 
if
 (i 
<
 count) {

 
const
 b 
=
 
new
 
Uint8Array
(CHUNK);

 b.
set
(utf8Template);

 b[
0
] 
=
 
32
 
+
 (i
++
 
&
 
63
);

 c.
enqueue
(b);

 } 
else
 c.
close
();

 },

 });

};

const
 
drain
 
=
 
async
 (
rs
) 
=>
 {

 
const
 r 
=
 rs.
getReader
();

 
let
 n 
=
 
0
;

 
for
 (;;) {

 
const
 { done, value } 
=
 
await
 r.
read
();

 
if
 (done) 
return
 n;

 n 
+=
 
typeof
 value 
===
 
"
string
"
 
?
 value.length 
:
 value.byteLength;

 }

};

let
 run, expected;

if
 (scenario 
===
 
"
encode
"
) {

 
const
 count 
=
 
Math
.
ceil
(BYTES 
/
 stringChunkBytes);

 expected 
=
 count 
*
 stringChunkBytes;

 
run
 
=
 () 
=>
 
drain
(
stringSource
(BYTES).
pipeThrough
(
new
 
TextEncoderStream
()));

} 
else
 
if
 (scenario 
===
 
"
decode
"
) {

 expected 
=
 
null
; 
// output is chars, not bytes

 
run
 
=
 () 
=>
 
drain
(
bytesSource
(BYTES).
pipeThrough
(
new
 
TextDecoderStream
()));

} 
else
 
throw
 
new
 
Error
(
`unknown --scenario=
${
scenario
}
; encode | decode`
);

const
 t0 
=
 performance.
now
();

const
 got 
=
 
await
 
run
();

const
 ms 
=
 performance.
now
() 
-
 t0;

if
 (expected 
!==
 
null
 
&&
 got 
!==
 expected)

 
throw
 
new
 
Error
(
`encoded 
${
got
}
 bytes, expected 
${
expected
}
`
);

const
 bytes 
=
 expected 
??
 
Math
.
ceil
(BYTES 
/
 CHUNK) 
*
 CHUNK;

console.
log
(

 
`
${
scenario.
padEnd
(
22
)
}
 
${
(bytes
 
/
 
MB
 
/
 
(ms
 
/
 
1000
))

 
.
toFixed
(
0
)

 
.
padStart
(
6
)
}
 MB/s 
${
ms.
toFixed
(
0
).
padStart
(
6
)
}
 ms 
${
(bytes
 
/
 
MB).
toFixed
(

 
0
,

 
)
}
 MiB`
,

);

All numbers: AMD EPYC 9R14, Linux x64. Bun 1.3.0, Bun 1.4.0, Node.js 26.7.0, Deno 2.9.5. Median of 3 runs, one process per run, peak RSS from/usr/bin/time -v.

### Backpressure#

Bun.serveautomatically pauses theReadableStreamrequest & response bodies when the connection can't accept more data, so a slow or stalled client holds at most one buffer's worth of server memory.

Bun.
serve
({

 routes
:
 {

 
"
/
"
:
 () 
=>
 {

 
return
 
new
 
Response
(

 
new
 
ReadableStream
({

 
// pauses when the socket's send buffer fills

 
pull
(
controller
) {

 controller.
enqueue
(
new
 
Uint8Array
(
65536
));

 },

 }),

 );

 },

 },

});

fetch()does the same on the receiving side. This also works withTransformStreamlikeCompressionStream&DecompressionStream, andHTMLRewriter.transform,child_process,Bun.spawn,Bun.file(path).stream(),Blob.stream()and more.

backpressure · Bun.serve ReadableStream
Bun
 
1.3
1.4
1.4
RSS
 
238 MB
▶ play
◼ playing…
▶ Bun 1.4: see the fix
↻ replay
▶ play
ReadableStream
pull(controller) 
{
 
controller.enqueue(…65536)
}
⏸ waiting for socket to drain
→
server heap
OOM
pause
💥 process killed (OOM)
→
slow client 🐌
for await (chunk of res.body)
reads every 
480
ms
The stream’s 
pull()
 outpaces a slow client 3:1. In Bun 1.3 the server buffered every unsent chunk on the heap until the process ran out of memory; in 1.4 
pull()
 pauses when the socket’s send buffer fills and resumes when it drains. Illustrative — each chip is a batch of 64 KB chunks; the ~1 GiB/s figure is from the
 
#
32553
 
repro.

## We rewrote Bun in Rust#

Bun is now written in Rust - and this is the first release (though Claude Code has been using Bun's Rust port for months now, and Prisma launchedPrisma Computeon it). Wewrote a blog postabout the Rust rewrite that goes into more detail.

## What's new#

This release makes Bun's builtin standard library bigger.

15
 dependencies · now built in
0
 
dependencies left
▶ play
↻ replay
◼ playing…
▶ play
package.json · dependencies
sharp
puppeteer
marked
node-cron
node-pty
concurrently
npm-run-all
serve-static
json5
fast-xml-parser
tar
string-width
slice-ansi
cli-truncate
wrap-ansi
built into Bun 1.4
✓
Bun.Image
image processing
✓
Bun.WebView
headless browser
✓
Bun.markdown
markdown rendering
✓
Bun.cron
scheduled jobs
✓
Bun.Terminal
native PTY
✓
bun run --parallel
parallel scripts
✓
bun run --parallel
parallel scripts
✓
Bun.serve routes
static files
✓
Bun.JSON5
JSON5 parsing
✓
Bun.XML
XML parsing
✓
Bun.Archive
tarballs
✓
Bun.stringWidth
terminal columns
✓
Bun.sliceAnsi
ANSI-aware slicing
✓
Bun.sliceAnsi
ANSI-aware truncation
✓
Bun.wrapAnsi
ANSI-aware wrapping
Every one of these ships in the Bun binary — no install step, no native build, no lockfile entry. Each is covered in its own section below.

### Bun.Imagev1.3.14#

Bun.Imageis a built-in image library.

await
 Bun.
file
(
"
photo.jpg
"
)

 .
image
()

 .
resize
(
1024
, 
1024
, { fit
:
 
"
inside
"
 })

 .
rotate
(
90
)

 .
webp
({ quality
:
 
85
 })

 .
write
(
"
thumb.webp
"
);

// Stream straight into a Response

return
 
new
 
Response
(
new
 Bun.
Image
(upload).
resize
(
200
).
jpeg
());

Decode, resize, rotate, and encode JPEG, PNG, WebP, GIF, and BMP. HEIC, AVIF, and TIFF work on macOS and Windows.

The API looks like sharp, and no native addon is needed. ICC color profiles like Display P3 survive transcoding.

On a 1080p PNG resized to a 400×400 JPEG, it's 1.38× faster than sharp. On JPEG to WebP, 1.19×.#30032

Bun.Image · decode → resize → rotate → encode
photo.jpg → thumb.webp
▶ play
◼ playing…
↻ replay
▶ play
await 
Bun
.
file
(
"photo.jpg"
)
 .
image
()
 .
resize
(
1024
, 
1024
, { 
fit
: 
"inside"
 })
 .
rotate
(
90
)
 .
webp
({ 
quality
: 
85
 })
 .
write
(
"thumb.webp"
);
JPEG
JPEG
WEBP
·
124 KB
✓ thumb.webp
zero 
npm install
 · 1.38× faster than sharp on decode→resize→encode ·
 
#30032

### Bun.WebViewv1.3.12v1.4.0#

Bun.WebViewis headless browser automation built into Bun, without Puppeteer or Playwright.

await
 using view 
=
 
new
 Bun.
WebView
({ width
:
 
800
, height
:
 
600
 });

await
 view.
navigate
(
"
https://bun.sh
"
);

await
 view.
click
(
"
a[href='/docs']
"
);

const
 title 
=
 
await
 view.
evaluate
(
"
document.title
"
);

await
 Bun.
write
(
"
page.png
"
, 
await
 view.
screenshot
());

Navigate, click, scroll, run JavaScript, and take screenshots. Clicks and scrolls are real user input.

On macOS it uses the system WebKit, with nothing to install. On macOS, Linux, and Windows it can also drive an installed Chrome, Chromium, or Edge.#39423

Bun.WebViewextendsEventTarget, returnsBlobscreenshots, and exposes a.cdp(method, params?)escape hatch for raw Chrome DevTools Protocol commands. See thedocsfor advanced usage.

Bun.WebView · headless browser in 5 lines
▶ play
◼ playing…
↻ replay
▶ play
await 
using 
view
 = 
new 
Bun.WebView
({ 
width
: 
800
, 
height
: 
600
 });
await 
view
.navigate
(
"https://bun.sh"
);
await 
view
.click
(
"a[href='/docs']"
);
const 
title
 = 
await 
view
.evaluate
(
"document.title"
);
await 
Bun
.write
(
"page.png"
, 
await 
view
.screenshot
());
https://bun.sh/docs
 
https://bun.sh
https://bun.sh/docs
Docs
Guides
Blog
Bun is a fast JavaScript
all-in-one toolkit
Documentation
title → 
"
Bun — Documentation
"
✓ page.png
No Puppeteer, no Playwright, no
 
npm install
 — a real browser (WebKit on macOS, or an installed Chrome/Edge via CDP) driven by five awaits. Clicks arrive as trusted input (
event.isTrusted === true
). Illustrative render — see the
 
docs
.

### Bun.markdownv1.3.8v1.4.0#

Bun.markdownis a Markdown parser built into Bun.

const
 html 
=
 Bun.markdown.
html
(
"
# Hello **world**
"
);

// "<h1>Hello <strong>world</strong></h1>\n"

// ANSI terminal output

const
 ansi 
=
 Bun.markdown.
render
(
"
# Hello
\n\n
**bold**
"
, {

 
heading
:
 (
children
) 
=>
 
`
\x1b
[1;4m
${
children
}\x1b
[0m
\n
`
,

 
paragraph
:
 (
children
) 
=>
 children 
+
 
"
\n
"
,

 
strong
:
 (
children
) 
=>
 
`
\x1b
[1m
${
children
}\x1b
[22m`
,

});

// React

export
 
default
 
function
 
Page
() {

 
return
 Bun.markdown.
react
(readme);

}

Bun.markdown.html()gives you an HTML string.Bun.markdown.react()gives you React elements, and you can swap in your own component for any tag.Bun.markdown.render()gives you a callback per element, for things like terminal output.

GFM tables, strikethrough, task lists, and autolinks are supported,.mdis a bundler loader, and the parser runs in linear time on adversarial input.

The HTML output is not sanitized: raw HTML, event-handler attributes, andjavascript:hrefs pass through verbatim.

### Bun.cron()v1.3.11v1.4.0#

Bun.cron()registers a scheduled job with the operating system: crontab on Linux, launchd on macOS, Task Scheduler on Windows.

Your script exports ascheduled(controller)handler, the same shape as Cloudflare Workers Cron Triggers.

Standard 5-field cron syntax works, including named days and@daily.#26999

// Register an OS-level cron job

await
 Bun.
cron
(
"
./worker.ts
"
, 
"
30 2 * * MON
"
, 
"
weekly-report
"
);

// Parse a cron expression → next matching UTC Date

const
 next 
=
 Bun.cron.
parse
(
"
*/15 * * * *
"
);

// worker.ts

export
 
default
 {

 
async
 
scheduled
(
controller
) {

 
// controller.cron === "30 2 * * 1"

 
// controller.scheduledTime === 1737340200000

 
await
 
doWork
();

 },

};

You can also pass a function instead of a file. Bun runs it on the event loop, with no system cron involved.

Jobs never overlap, andusingstops the job when it goes out of scope.

using job 
=
 Bun.
cron
(
"
*/5 * * * *
"
, 
async
 () 
=>
 {

 
await
 
cleanupTempFiles
();

});

job.cron; 
// "*/5 * * * *"

job.
unref
(); 
// allow process exit

job.
stop
(); 
// cancel (or let `using` dispose)

Bun.cronschedules run in local time by default, with a new{ tz }option for explicit timezones;parse()rejectsfromtimestamps outside the ECMAScriptDaterange.#35122#29282

### Bun.Terminalv1.3.5v1.4.0#

Bun.Terminalis a built-in pseudo-terminal, so you can drivebash,vim, orhtopfrom JavaScript without node-pty.

PassterminaltoBun.spawn, write input, resize, and read the colored output. It works on Linux, macOS, and Windows.#25415#29522

const
 proc 
=
 Bun.
spawn
([
"
bash
"
], {

 terminal
:
 {

 cols
:
 
80
,

 rows
:
 
24
,

 
data
(
term
, 
data
) {

 process.stdout.
write
(data);

 },

 },

});

proc.terminal.
write
(
"
echo Hello from PTY!
\n
"
);

### bun run --parallelv1.3.9v1.4.0#

bun run --parallelruns multiplepackage.jsonscripts concurrently with name-prefixed output. Glob-match script names, fan out across every workspace with--filter, and keep going past failures with--no-exit-on-error. This replaces tools like npm-run-all and concurrently.#26551

# Run "build" and "test" concurrently
bun run --parallel build 
test
# Glob-matched script names
bun run --parallel 
"
build:*
"
# Run "build" in every workspace package
bun run --parallel --filter 
'
*
'
 build
# Keep going even if one package fails
bun run --parallel --no-exit-on-error --filter 
'
*
'
 
test

Each line of output is prefixed with the script name (orpackage:scriptunder--filter), andprebuild/postbuildhooks are grouped with their main script so dependency order is preserved.--sequentialruns scripts one at a time with the same prefixed output and filtering.

❯
bun run --parallel "build:*"
↻ replay
build:client 
|
 
$ bun build src/client.ts --outdir=dist/client --minify
build:server 
|
 
$ bun build src/server.ts --outdir=dist/server --target=bun
build:worker 
|
 
$ bun build src/worker.ts --outdir=dist/worker --target=bun
build:styles 
|
 
$ bun run src/build-styles.ts
build:client 
|
 
Bundled 1 module in 4ms
build:server 
|
 
Bundled 1 module in 4ms
build:client 
|
 
 client.js 69 B (entry point)
build:worker 
|
 
Bundled 1 module in 3ms
build:server 
|
 
 server.js 153 B (entry point)
build:client 
|
 
Done in 25ms
build:worker 
|
 
 worker.js 98 B (entry point)
build:server 
|
 
Done in 32ms
build:worker 
|
 
Done in 34ms
build:styles 
|
 
compiled base.css
build:styles 
|
 
compiled components.css
build:styles 
|
 
compiled utilities.css
build:styles 
|
 
compiled theme.css
build:styles 
|
 
✓ 4 stylesheets → dist/styles.css
build:styles 
|
 
Done in 560ms

### 3x fasterbun:ffiv1.4.0#

bun:ffinow runs on FFI built into JavaScriptCore, replacing TinyCC. We added native support for FFI to JavaScriptCore.

Bun 1.3
Bun 1.4
no-op call
2.13 ns
0.70 ns
3.0×
new CString(ptr)
92.5 ns
24.1 ns
3.8×
opentui layout reads (1,000)
2.08×

The newbuffer_lengthargument type passes a TypedArray's length alongside its pointer, so the two can't disagree.

import
 { dlopen } 
from
 
"
bun:ffi
"
;

const
 { symbols } 
=
 
dlopen
(
"
libhash.so
"
, {

 hash
:
 { args
:
 [
"
buffer
"
, 
"
buffer_length
"
], returns
:
 
"
cstring
"
 },

});

const
 digest 
=
 symbols.
hash
(data, data);

typeof
 digest; 
// "string"

returns: "cstring"now gives you a plain string.NULLgives younull.

When a call site gets hot, the JIT compiles it into a direct call to the C function. It already knows the argument types from the signature, so it passes unboxed values in registers and skips the type checks and boxing a normal call would do.

bun:ffi gets up to 3x faster

### Dev toolingv1.3.2v1.4.0#

* --cpu-prof,--cpu-prof-md: A.cpuprofilefor Chrome DevTools, or the same profile as a Markdown report for pasting into a bug or an LLM;BUN_CPU_PROFILE=1for processes you can't pass flags to.#24112#26327
* --heap-prof,--heap-prof-md: A V8-compatible.heapsnapshot, or a Markdown report of the biggest types and objects.#26326
* Async stack traces: Errors from async native APIs (fs.promises,Bun.file(), S3, DNS, crypto,fetch) point back to theawaitin your code.#28652
* --no-orphans: Bun exits when its parent dies and SIGKILLs every descendant on exit, on Linux, macOS, and Windows.#29930
* --no-env-file: Skip automatic.envloading in production and CI (env = falseinbunfig.toml).#24767

### HTTP/3 inBun.serve()(experimental)v1.3.14v1.4.0#

Bun.serve()supports HTTP/3. Sethttp3: truenext totls, and Bun listens on UDP on the same port.

HTTP/1.1 keeps working over TCP, and responses advertise HTTP/3 with anAlt-Svcheader so browsers upgrade on their own.

On a static-route benchmark, HTTP/3 is 2.7× faster than HTTPS/1.1 on the same server.

Bun.
serve
({

 port
:
 
443
,

 tls
:
 { 
...
 },

 http3
:
 
true
, 
// also listen on UDP/443 for HTTP/3

 
// h1: false, // optional: serve HTTP/3 only

 
fetch
(
req
) {

 
return
 
new
 
Response
(
"
hi
"
);

 },

});

Experimental: zero-round-trip connection resumption is disabled,server.upgrade()returnsfalseover H3, andunix:sockets skip the H3 listener. Don't shiphttp3: trueto production yet.#29768

### HTTP/2 & HTTP/3 infetch()(experimental)v1.3.14v1.4.0#

fetch()now supports HTTP/2 and HTTP/3. Passprotocol: "http2"orprotocol: "http3".

const
 [a, b, c] 
=
 
await
 
Promise
.
all
([

 
fetch
(
"
https://api.example.com/a
"
, { protocol
:
 
"
http2
"
 }),

 
fetch
(
"
https://api.example.com/b
"
, { protocol
:
 
"
http2
"
 }),

 
fetch
(
"
https://api.example.com/c
"
, { protocol
:
 
"
http2
"
 }),

]);

const
 res 
=
 
await
 
fetch
(
"
https://example.com
"
, { protocol
:
 
"
http3
"
 });

Over HTTP/2, concurrent requests to the same origin share one connection. Redirects, decompression, and streaming work the same as they do over HTTP/1.1.

To turn them on everywhere, setBUN_FEATURE_FLAG_EXPERIMENTAL_HTTP2_CLIENT=1or pass--experimental-http3-fetch. With the HTTP/3 flag, Bun remembers which origins support it and uses it for later requests on its own.

### Serve files & foldersv1.4.0#

Bun.serve()routescan now serve a directory.

Files stream withsendfile.Content-Type,ETag,Last-Modified,304, andRangeare handled for you, andindex.htmlis served for directories.

This replacesexpress.static,serve-static, andsirv.#36156

Bun.
serve
({

 routes
:
 {

 
"
/static/*
"
:
 { dir
:
 
"
./public
"
 },

 },

});

When serving files from disk, paths are normalized before lookup and on Linux files are opened withopenat2withO_RESOLVE_BENEATH, so a symlink inside the directory can't reach above it.

### Range and conditional requestsv1.3.13v1.4.0#

Bun.servehonorsRangeheaders for file responses, so video seeking and resumable downloads work. Both static routes andBun.file()bodies return206 Partial Content.

Static routes andBun.file()responses also handle conditional requests.If-None-MatchandIf-Modified-Sinceget a304, andIf-MatchandIf-Unmodified-Sinceget a412when the precondition fails.

Bun.
serve
({

 routes
:
 {

 
"
/video.mp4
"
:
 
new
 
Response
(Bun.
file
(
"
./video.mp4
"
)),

 
"
/logo.png
"
:
 
new
 
Response
(Bun.
file
(
"
./logo.png
"
)),

 },

});
curl -H 
'
Range: bytes=0-1023
'
 localhost:3000/video.mp4
HTTP/1.1 206 Partial Content

Content-Range: bytes 0-1023/104857600
curl -H 
'
If-None-Match: "1a2b3c"
'
 localhost:3000/logo.png
HTTP/1.1 304 Not Modified

### HTML routes sourcemaps disabled in productionv1.4.0#

In production,Bun.serveno longer serves sourcemaps for HTML routes, so your original source stays on your server.

Development mode still serves them. Setsourcemapunder[serve.static]inbunfig.tomlto pick explicitly.#36982

[
serve
.
static
]

sourcemap
 
=
 
"
linked
"

### fetch()request compressionv1.4.0#

fetch()gains acompressoption. It compresses the request body before sending and sets theContent-Encodingheader automatically. It supportsgzip,deflate,br, andzstd, with an optional compression level. Buffered bodies (string,ArrayBuffer,TypedArray,Blob) are compressed, andContent-Lengthreflects the compressed size. Streaming bodies pass through unchanged.#32416

await
 
fetch
(url, {

 method
:
 
"
POST
"
,

 body
:
 largeJsonString,

 compress
:
 
"
gzip
"
, 
// or true, "deflate", "br", "zstd", { encoding, level }

});

### fetch()proxy headersv1.3.4#

fetch()'sproxyoption now also accepts an object withurlandheaders, letting you send custom headers (likeProxy-Authorization) directly to the proxy server, whether the destination is HTTPS or plain HTTP.#25090

await
 
fetch
(url, {

 proxy
:
 {

 url
:
 
"
http://proxy.example.com:8080
"
,

 headers
:
 { 
"
Proxy-Authorization
"
:
 
"
Bearer token
"
 },

 },

});

### TLS session resumptionv1.4.0#

A second cold connection to an originresumes at 1 RTT. A 32-entry LRU caches BoringSSL client sessions per origin, so reconnecting after the keep-alive pool evicts skips the full handshake and certificate-chain walk.

### Connection reusev1.3.10v1.4.0#

fetch()reuses connections through an HTTPS proxy, and reuses them for requests with custom TLS options like a client certificate or a custom CA.#28611#37715#27385

### Also built inv1.3.3v1.4.0#

* Bun.JSON5:Bun.JSON5.parse()/stringify(); import.json5files directly. Replaces json5.
* Bun.JSONL:parse()and streamingparseChunk()for newline-delimited JSON. Replaces ndjson.
* Bun.JSONC.parse(): JSON with comments and trailing commas, the parser behindtsconfig.json. Replaces jsonc-parser.
* Bun.XML: SIMD XML parser and serializer; import.xmlfiles directly. Replaces fast-xml-parser and xml2js.
* Bun.TOML: TOML v1.1.0, 708/708 oftoml-test; newstringify(). Replaces @iarna/toml.
* Bun.Archive: Create and extract tarballs off the main thread. Replaces tar.
* Bun.sliceAnsi(),Bun.wrapAnsi(),Bun.stringWidth(): Terminal-column-aware slicing, wrapping, and measurement, ANSI and grapheme aware. Replaces slice-ansi, cli-truncate, wrap-ansi, and string-width.
* URLPattern: The Web API, 408 WPT passing. Replaces path-to-regexp.
* CompressionStream/DecompressionStream: Web-standard streams forgzip,deflate,deflate-raw, plusbrotliandzstd.
* Response.textStream(): AReadableStream<string>of the body decoded as UTF-8.
* process.on("memoryPressure"): The OS's low-memory notification on macOS, Linux, and Windows.
* ML-DSA and ML-KEM: NIST post-quantum signatures and key encapsulation incrypto.subtleandnode:crypto.
* Bun.spawn({ cgroup }): Place a child in a cgroup before it starts, on Linux.
* bun repl: Native REPL: highlighting, history, tab completion,-e/-p.
* bun ./README.md: Renders Markdown to the terminal, no VM started. Replaces glow.

## bun install#

bun installis an npm-compatible package manager.

On a T3-stack Next.js app,bun installis many times faster than yarn, pnpm, and npm, and uses a fraction of the memory.

That holds for a first install, a fresh checkout, CI with and without a cache, and a no-op reinstall:

One app, six installs
T3-stack Next.js app, 25 direct dependencies, ~220 packages in the lockfile · install time and peak memory
source ↗
Scenario
bun
v1.4
npm
v12.0.2
pnpm
v11.21.0
yarn
v1.22.22
First install, ever
no cache · no lockfile · no node_modules
1.41s
15× faster
376 MB
18.1s
503 MB
13.5s
1.8 GB
20.5s
498 MB
Fresh checkout, warm cache
no lockfile yet · every package already in the cache
251ms
30× faster
52 MB
7.61s
798 MB
2.38s
1.1 GB
1.83s
204 MB
CI without a cache
lockfile committed · every tarball fetched from the registry
951ms
19× faster
214 MB
4.92s
455 MB
11.7s
2.7 GB
17.6s
323 MB
CI with a warm cache
lockfile committed · dependency cache restored · node_modules rebuilt
210ms
21× faster
12 MB
4.45s
698 MB
1.92s
1.4 GB
1.76s
205 MB
node_modules there, cache gone
already installed · only the dependency cache was cleared
12ms
33× faster
12 MB
384ms
129 MB
399ms
141 MB
212ms
107 MB
Everything already up to date
the reinstall after nothing changed
12ms
33× faster
12 MB
337ms
114 MB
400ms
141 MB
211ms
107 MB

Linux x64, EPYC 9R14 · bench/install in oven-sh/bun · each package manager with its own lockfile and node_modules, state prepared per scenario before every run, every package manager at defaults · medians of 3, peak memory is the largest of the 3 runs

### Global virtual store: up to 7x faster installsv1.3.14v1.4.0#

bun install --linker=isolatednow uses a shared global virtual store. Packages are extracted once into Bun's cache and symlinked into each project'snode_modules/.bun/store, instead of being copied intonode_moduleson every install.#29489

On a warm isolated install, copying packages intonode_modules(clonefileat()on macOS) was 95% of main-thread time, and macOS runs only one of those calls at a time.

Once a package exists anywhere on the machine, later installs do onesymlink()per package instead of oneclonefileat().

On the common CI path (lockfile present, cache warm,node_moduleswiped), a 1,400-package install is7x faster. The global store is opt-in: it applies when you select the isolated linker, which is not the default for existing projects.

# bunfig.toml

[
install
]

linker
 
=
 
"
isolated
"

### bun pm diffv1.4.0#

bun pm diffshows you what changed between two versions of a package.

It starts with a summary: which files changed, any new install scripts, and any new imports ofchild_process,fs,net, orvm. Then it shows the diff.

Minified files are un-minified before diffing, and formatting-only changes are skipped, so you see the lines that actually changed.#39229

bun pm diff react 
# the version in bun.lock → latest
bun pm diff react@18.2.0 19.0.0 
# two published versions
bun pm diff ./vendored-pkg pkg@2.1.0 
# a folder against a published version
bun pm diff react-dom@18.2.0 18.3.1 
'
*.min.js
'

### bun audit fixv1.4.0#

bun audit fixupgrades vulnerable packages to a safe version and installs.

If a fix needs a new major version, it tells you, and--latestlets it do that.--dry-runshows what it would change.#38333

bun audit fix
fixing:

 ms@0.7.0 → 0.7.1

 lodash@4.17.20 → 4.17.21

 package.json: 4.17.20 → 4.17.21

blocked by a dependent's range:

 minimatch@0.3.0 → 3.0.2

 express@3.21.2 depends on minimatch@0.3.0

Fixed 2 vulnerabilities in 2 packages

1 vulnerability remaining

### bun dedupev1.4.0#

bun deduperemoves duplicate versions of packages frombun.lock.

If you haveesbuild@0.15.10andesbuild@0.15.11and one version satisfies both, you end up with one. It never changespackage.json, and--checkfails CI if there are duplicates.#38333

bun dedupe
bun dedupe v1.4.0 (abc12345)

↳ esbuild 0.15.10 → 0.15.11

↳ react 18.2.0 → 18.3.1

2 duplicate versions removed, 3 packages installed (checked 5 packages) [12.00ms]

### bun prunev1.4.0#

bun prunedeletes packages fromnode_modulesthat aren't inbun.lockanymore.

bun prune --productionalso deletesdevDependencies, so you can build with them and ship without them.#38333

bun prune --production
bun prune v1.4.0 (abc12345)

- typescript@5.4.0

- @types/node@20.11.5

2 packages removed (checked 948) [22.00ms]
COPY package.json bun.lock ./

RUN bun install --frozen-lockfile

COPY . .

RUN bun run build

RUN bun prune --production

### bun pm licensesv1.4.0#

bun pm licenseslists your dependencies by license.

--jsongives you machine-readable output, and--prodskipsdevDependencies.#38333

bun pm licenses --prod --json 
>
 licenses.json

### bun updateupdates transitive dependenciesv1.4.0#

bun updatenow updates the dependencies of your dependencies too, not just the ones in yourpackage.json.

bun update
bun update zod
bun update 
'
@types/*
'
 --latest

bun update <name>updates that package everywhere it appears, andbun update '@types/*'takes a pattern.#38333

### bun add --filterv1.4.0#

bun add,bun remove, andbun updateaccept--filter, so you can add a package to one workspace from the root of your monorepo.

bun add zod --filter api
bun run --filter 
'
web...
'
 build

--filter 'web...'meansweband everything it depends on.--filter '...web'means everything that depends onweb.

### bun add --catalogv1.4.0#

bun add <pkg> --catalogadds the package to your root catalog and writes"catalog:"in the workspace'spackage.json.

bun add react --catalog

If the package is already in your default catalog, plainbun adduses it.

### Nested overridesv1.4.0#

You can now override a dependency's dependency without overriding it everywhere. npm's nested form, yarn'sa/b, and pnpm'sa>ball work, and an override can be scoped to a version range.

{

 
"
overrides
"
:
 {

 
"
express
"
:
 { 
"
qs
"
:
 
"
6.13.0
"
 },

 
"
lodash@<4.17.21
"
:
 
"
4.17.21
"

 }

}

### Lockfile integrity for GitHub and tarball dependenciesv1.3.10#

bun.locknow records a SHA-512 hash for GitHub and tarball dependencies, the same way it always has for npm packages. Existing lockfiles pick up the hashes on the next install.

[
"
pkg@github:user/repo#ref
"
, {}, 
"
resolved-commit
"
]

[
"
pkg@github:user/repo#ref
"
, {}, 
"
resolved-commit
"
, 
"
sha512-...
"
]

### trustedDependenciesonly auto-trusts the npm registryv1.3.5#

Bun's default trusted-dependencies list applies only to packages from the npm registry.

Afile:,link:,git:, orgithub:dependency named esbuild gets no trust from the real esbuild's entry. To run its lifecycle scripts, list it intrustedDependenciesyourself.

{

 
"
dependencies
"
:
 {

 
"
esbuild
"
:
 
"
github:some-fork/esbuild#main
"

 },

 
"
trustedDependencies
"
:
 [
"
esbuild
"
]

}

Trusted-dependency names,.npmrcscope names, and localfile:paths are compared by their full bytes rather than a hash, and registry credentials stay scoped to their configured host — never sent cross-origin, downgraded tohttp://, or printed in error or verbose output.

### nativeDependenciesandignoreScriptsv1.3.2#

For packages that ship prebuilt binaries as per-platformoptionalDependencies(esbuild and @esbuild/darwin-arm64), Bun links the right binary directly instead of runningpostinstall. List them innativeDependencies.

ignoreScriptsskips a package's lifecycle scripts entirely, even if it is also intrustedDependencies.#24283

Configure both inpackage.json, or disable native binary linking withBUN_FEATURE_FLAG_DISABLE_NATIVE_DEPENDENCY_LINKER=1and script skipping withBUN_FEATURE_FLAG_DISABLE_IGNORE_SCRIPTS=1.

{

 
"
nativeDependencies
"
:
 [
"
esbuild
"
, 
"
my-custom-package
"
],

 
"
ignoreScripts
"
:
 [
"
sharp
"
, 
"
another-package
"
]

}

## bun test#

bun test --parallelruns test files across worker processes.--shardsplits them across CI machines.--timingsbalances both by how long each file takes.--changedruns only the tests your diff touches.

bun 
test
 --changed=main 
# only what your branch touches
bun 
test
 --parallel --timings=timings.json --update-timings
bun 
test
 --parallel --shard=1/3 --timings=timings.json 
# in CI, per machine

### bun test --parallelv1.3.13v1.4.0#

bun test --parallel[=N]runs test files across N worker processes (defaulting to your CPU count). Files go to whichever worker frees up next.#29354

bun 
test
 --parallel
bun 
test
 --parallel=4 --isolate

Coverage and JUnit output are merged across workers.--bailstops every worker on the first failure.

--parallelimplies--isolate(below).--no-isolateturns that off, so each worker keeps one global and one module registry for every file it runs.

Each worker exposes its 1-indexed slot asJEST_WORKER_ID/BUN_TEST_WORKER_ID, so Jest setups that key databases or ports offJEST_WORKER_IDwork unchanged. Preload scripts with top-levelawaitcomplete before any worker starts running tests.

bun test --parallel · files go to whichever worker frees up
▶ play
↻ replay
▶ play
bun test
9.4s
bun test --parallel=
4
2.4s
3.9
× faster
✓ done · 
9.4s
w
1
w
2
w
3
w
4
✓ done · 
2.4s
 · workers idle
Same 24 test files, same durations, one wall-clock.
 
--parallel=
4
 hands each file to whichever worker’s queue is shortest — so the 1.8s 
sql/postgres.test.ts
 
outlier ties up one lane while the other three keep going, and all four finish within ~7% of each other. Durations illustrative.
 
#29354

### bun test --isolatev1.3.13v1.4.0#

bun test --isolateruns each test file in a fresh JavaScript global object, in the same process. This is how Jest and Vitest behave by default. It makes "passes alone, fails in the full suite" bugs go away.#29354

bun 
test
 --isolate

Between files, Bun:

* creates a newglobalThis, so properties a file put onglobalThis, patched built-ins, and module-level state are gone
* clears the ESM and CommonJS module registries, so every file re-evaluates its imports
* closes servers, sockets, file watchers, and subprocesses the file left open, cancels its timers, and restores fake timers
* re-runs--preloadscripts in the new global

Transpiled source and bytecode are cached at the process level and shared across globals. The second file to import a module skips reading, transpiling, and parsing it. Only the module's top-level code runs again.

Bun 1.4 fixes several stability problems from the first release of--isolate:

* Fake timers a file left installed no longer leak into the next file.#36385
* Subprocesses started at module scope are killed when the file ends, instead of outliving the run.#38750
* process.chdir()in one file no longer changes the working directory of the next file.#36175
* Servers, sockets, and other handles a file leaked no longer pin its global object in memory.#31793
* A--preloadscript with top-levelawaitfinishes before the first test runs.#30888
* Native addons (N-API) work across files, instead of pointing at the previous file's global.#30216
* Fixed a crash when garbage collection ran during the swap between two files.#29573
* The debugger resolves breakpoints in files loaded under--isolate.#37352

### bun test --shardv1.3.13v1.4.0#

bun test --shard=M/Nsplits your test files across multiple CI runners. Files are sorted deterministically and distributed round-robin so every machine sees the same partition, with 1-based indexing matching Jest, Vitest, and Playwright. Works alongside--changedand--randomize. An empty shard exits 0 instead of failing.#29366

# In a matrix of 3 jobs:
bun 
test
 --shard=1/3
bun 
test
 --shard=2/3
bun 
test
 --shard=3/3

### bun test --timingsv1.4.0#

--timings=<path>reads per-file durations from a previous run so--shardand--parallelbalance by wall time instead of file count.--update-timingsrecords the durations.#36814

bun 
test
 --timings=timings.json --update-timings 
# record per-file durations
bun 
test
 --shard=1/3 --timings=timings.json 
# cut shards by equal time
bun 
test
 --parallel --timings=timings.json 
# workers start slowest first

With timings, each shard gets about the same total time instead of the same number of files. Files that share imports stay together, so the module cache stays warm.

--parallelstarts each worker on its slowest file first. The timings file is written slowest-first, so it doubles as a slow-test report.

`bun test --timings` records how long each test file takes; `bun test --parallel --shard=i/N` uses timings to split CI shards via longest-processing-time-first scheduling, making large test suites run faster

### bun test --changedv1.3.13v1.4.0#

bun test --changedruns only the test files affected by your uncommitted changes, or by the diff against a branch or commit with--changed=main. The flag is vitest-compatible.#29262

bun 
test
 --changed 
# uncommitted (unstaged + staged + untracked)
bun 
test
 --changed=HEAD~1 
# diff against a commit / branch / tag
bun 
test
 --changed=main
bun 
test
 --changed --watch 
# re-filters on every restart

Bun scans every test file's imports, asks git which files changed, and walks the import graph backwards to find the tests that reach them.

tsconfigpathsaliases like@/*work. With--watch, editing any source file re-filters on restart.

bun test --changed
▶ next · edit cli.ts
▶ next · edit README.md
↻ replay
▶ next · edit cli.ts
1
 of 
3
 · you edit
 
src/lib/utils.ts
→ running
 
2
 of 3
 test files
TEST
date.test
TEST
auth.test
TEST
cli.test
date.ts
auth.ts
cli.ts
utils.ts
README.md
Same graph, three edits. Bun resolves the import graph once (skipping
 
node_modules
), then walks it backwards from whatever
 
git diff
 reports.

### bun test --retryv1.3.3v1.4.0#

test()accepts{ retry: n }to re-run a flaky test up tontimes, and{ repeats: n }to run itntimes and fail if any run fails.

bun test --retry <N>sets a default for the whole suite.#23713#26866

test
(

 
"
flaky network call
"
,

 
async
 () 
=>
 {

 
await
 
fetch
(
"
https://example.com
"
);

 },

 { retry
:
 
5
 },

);

test
(

 
"
stress
"
,

 () 
=>
 {

 
if
 (
Math
.
random
() 
<
 
0.1
) 
throw
 
new
 
Error
(
"
uh oh!
"
);

 },

 { repeats
:
 
20
 },

);

### jest.useFakeTimers()v1.3.4v1.4.0#

jest.useFakeTimers()lets you controlsetTimeout,setInterval, andDatefrom your tests.

@testing-library/react'swaitFordetects the fake timers and advances them instead of waiting in real time.#23764#25915

import
 { jest, test, expect } 
from
 
"
bun:test
"
;

test
(
"
debounce
"
, () 
=>
 {

 jest.
useFakeTimers
();

 
let
 called 
=
 
0
;

 
setTimeout
(() 
=>
 called
++
, 
1000
);

 jest.
advanceTimersByTime
(
1000
);

 
expect
(called).
toBe
(
1
);

 jest.
useRealTimers
();

});

jest.setSystemTime()works withadvanceTimersByTime(), andBun.cronschedules can be driven by the fake clock.#33623

## bun build#

### Built-in React Compilerv1.4.0#

bun build --react-compiler(orreactCompiler: trueinBun.build()) runs React's auto-memoization compiler on your components and hooks with no Babel or SWC in the loop. The compiler runs inside Bun's own parser, so there is no separate parse/print round-trip.

On a large React codebase (~860 components), enabling it adds 71 ms to the build (394 ms → 465 ms), about20× fasterthan the Babel plugin's 9.15 s on the same input. A full--compilebuild finishes in 3.62 s vs 13.04 s (3.6×).#32504

await
 Bun.
build
({

 entrypoints
:
 [
"
./src/index.tsx
"
],

 outdir
:
 
"
./dist
"
,

 reactCompiler
:
 
true
,

});
`bun build --react-compiler` runs the React Compiler in Rust. On a large React codebase, it's 19x faster than the Babel plugin

### Barrel import optimizationv1.3.10v1.4.0#

When you writeimport { Button } from "antd", Bun skips the hundreds of files behind the names you didn't import.

Packages that declare"sideEffects": falseget this automatically. For everything else, opt in withoptimizeImports.#26892

await
 Bun.
build
({

 entrypoints
:
 [
"
./src/index.tsx
"
],

 optimizeImports
:
 [
"
antd
"
, 
"
@mui/material
"
],

});
barrel import optimization · import 
{
 Button 
}
 from "antd"
Bun 1.3 · barrel not detected
Bun 1.4 · optimizeImports
Bun 1.4 · optimizeImports
modules parsed:
 
4
 · 
6
 
ms
▶ play
· playing ·
▶ with optimizeImports
↻ replay
▶ play
Affix
Alert
Anchor
App
AutoComplete
Avatar
BackTop
Badge
button/style
Button
_util/wave
config-provider
Carousel
Cascader
Checkbox
Col
Collapse
ColorPicker
ConfigProvider
DatePicker
Descriptions
Divider
Drawer
Dropdown
Empty
Flex
FloatButton
Form
Grid
Image
Input
InputNumber
Layout
List
Mentions
Menu
Modal
Pagination
Popconfirm
Popover
Progress
QRCode
Radio
Rate
Result
Row
Segmented
Select
Skeleton
Slider
Space
Spin
Statistic
Steps
Switch
Table
Tabs
Tag
Timeline
Tooltip
button/style
Button
_util/wave
config-provider
DatePicker
Form
Modal
Select
Table
import
 
{
 
Button
 
}
 
from
 
"antd"
antd/es/index.js
barrel · 
312
 re-exports
60
 of antd’s ~70 top-level exports shown. Module count and timing measured with Bun.build() on this exact import —
 
#
26892
.

### Compile-time feature flags withbun:bundlev1.3.5#

feature("FLAG")frombun:bundlebecomestrueorfalseat build time, and the dead branch is removed.

Set flags with--feature=FLAGorfeatures: [...]inBun.build(). They work inbun build,bun run, andbun test.#25462

import
 { feature } 
from
 
"
bun:bundle
"
;

if
 (
feature
(
"
SUPER_SECRET
"
)) {

 console.
log
(
"
Secret feature enabled!
"
);

}

// bun build --feature=SUPER_SECRET index.ts

### In-memory files inBun.build()v1.3.6#

Bun.build()accepts afilesoption: a map of paths to strings,Blobs, orTypedArrays. Use it to bundle entirely from memory or mix virtual modules with real files on disk — virtual paths take precedence. Handy for codegen, or for stubbing a module in tests without touching disk.#25852

await
 Bun.
build
({

 entrypoints
:
 [
"
/app/index.ts
"
],

 files
:
 {

 
"
/app/index.ts
"
:
 
`import { greet } from "./greet.ts"; console.log(greet("World"));`
,

 
"
/app/greet.ts
"
:
 
`export function greet(name: string) { return "Hello, " + name + "!"; }`
,

 },

});

### Single-file HTML with--compile --target=browserv1.3.10#

bun build --compile --target=browserproduces one HTML file with every script, stylesheet, and asset inlined.

You can double-click it and open it fromfile://, with no web server.#27056

bun build ./index.html --compile --target=browser --outdir=dist
# → dist/index.html (everything inlined, zero external requests)

### metafile: truev1.3.6v1.4.0#

Bun.build()supportsmetafile: true, returning build metadata in esbuild's metafile format: a full map of inputs, outputs, imports, exports, and byte sizes.result.metafileworks as-is with https://esbuild.github.io/analyze/ and anything else that reads esbuild's format.#25842

const
 result 
=
 
await
 Bun.
build
({

 entrypoints
:
 [
"
./index.js
"
],

 metafile
:
 
true
,

});

console.
log
(result.metafile.inputs);

console.
log
(result.metafile.outputs);

### --metafile-mdv1.3.8v1.4.0#

bun build --metafile-mdwrites the module graph as a Markdown report: a quick summary, the largest input files, per-entry-point breakdowns, dependency chains, and a grep-friendly raw section. The report is plain Markdown, so you can paste it into an LLM to ask why a bundle is large.#26441

bun build entry.js --metafile-md --outdir=dist
bun build entry.js --metafile-md=analysis.md --outdir=dist
bun build entry.js --metafile=meta.json --metafile-md=meta.md --outdir=dist

### Standard TC39 decoratorsv1.3.10v1.4.0#

You can now use standardTC39 decoratorsin Bun.

function
 
logged
(
value
, { 
kind
, 
name
 }) {

 
if
 (kind 
===
 
"
method
"
) {

 
return
 
function
 (
...
args
) {

 console.
log
(
`calling 
${
name
}
`
);

 
return
 value.
call
(
this
, 
...
args);

 };

 }

}

class
 
C
 {

 @
logged

 
greet
() {}

}

These are the decorators you get whenexperimentalDecoratorsis off intsconfig.json. They work on classes, methods, fields, accessors, and private members.

Bun passes theesbuild decorator test suite.

### --assetv1.4.0#

bun build --compile --asset <path>embeds a file or a whole directory into the executable, keeping the original filenames.

Use it for apublic/folder, templates, or a SvelteKitclient/build.path.join(import.meta.dir, ...)finds them the same way it does on disk.#36302

node:fsnow treats/$bunfs/as a real directory tree:existsSync,statSync,lstatSync,accessSync,readdirSync, andfs.promises.readdir(including{ withFileTypes: true }and{ recursive: true }) all work on embedded paths, so static-file servers that enumerate a directory at startup run unmodified inside a compiled binary.

bun build ./build/index.js --compile \
 --asset ./build/client --asset ./build/prerendered \

 --outfile server
./server 
# every route + static asset served from the binary

### Bytecode compilation for ES modulesv1.3.9v1.4.0#

--bytecodenow supports ES modules.--bytecode --format=esmrequires--compile, and enables top-level await,import.meta, dynamic imports, and code splitting in bytecode-compiled binaries; previously--bytecodeforced CommonJS output.#26402

### Code splitting on 20,000-module graphs is 14× fasterv1.4.0#

The code-splitting reachability walk is now BFS and O(V+E). A 20,000-module diamond-shaped DAG links in 320 ms, from 4.65 s. The tree-shaking liveness, TLA validation, CSS-order, and part-visitor passes run on explicit stacks. So linear import chains of thousands of modules link without stack growth.#35310#34554

## Faster#

Between Bun 1.3 and 1.4 we bumped our WebKit pin39 times, pulling in roughly eight months of upstream JavaScriptCore work; the regex engine, Promises, and most String/Array builtins moved from self-hosted JavaScript to C++, and Bun swapped in zlib-ng and SIMD kernels for its own hot paths.

### new URL()is up to 4.6× fasterv1.4.0#

Bun's URL parser was rewritten. WebKit's new parser does the parsing. On Bun's side,hrefreuses the input string, the last base URL is cached, and hosts that are already ASCII punycode skip ICU.

Operation
Bun 1.3
Bun 1.4
Node.js 26
new URL("http://localhost:3000/api/users/42")
349 ns
75 ns
232 ns
new URL("../x", base)
523 ns
168 ns
612 ns
url.href
16 ns
5 ns
8 ns

#39273#39368#39468

### Faster RegExpv1.4.0#

The RegExp performance gap between JavaScriptCore and V8 has been fixed.

marked.parse()gets 138× faster. On an 80 KB Markdown fixture, it runs in ~6 ms, from 912 ms.

isbotgets 200× faster. One call on a typical user agent takes 1.07 µs, from 218 µs in Bun 1.3. Node.js 26 takes 1.47 µs.

Benchmark code: isbot-bench.mjs
import
 { isbot } 
from
 
"
isbot
"
; 
// isbot@5.2.1

const
 uas 
=
 [

 
"
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36
"
,

 
"
Mozilla/5.0 (Macintosh; Intel Mac OS X 14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15
"
,

 
"
Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148
"
,

 
"
Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)
"
,

 
"
curl/8.7.1
"
,

 
"
Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36
"
,

 
"
Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0
"
,

 
"
Slackbot-LinkExpanding 1.0 (+https://api.slack.com/robots)
"
,

];

let
 hits 
=
 
0
;

for
 (
let
 i 
=
 
0
; i 
<
 
20_000
; i
++
)

 
for
 (
const
 ua 
of
 uas) hits 
+=
 
isbot
(ua) 
?
 
1
 
:
 
0
; 
// warm up

const
 N 
=
 
200_000
;

const
 t0 
=
 performance.
now
();

for
 (
let
 i 
=
 
0
; i 
<
 N; i
++
) 
for
 (
const
 ua 
of
 uas) hits 
+=
 
isbot
(ua) 
?
 
1
 
:
 
0
;

const
 ms 
=
 performance.
now
() 
-
 t0;

console.
log
(
`
${
((ms
 
*
 
1e6
)
 
/
 
(N
 
*
 
uas.length)).
toFixed
(
0
)
}
 ns/call`
, hits);

### node:zlibuses zlib-ngv1.3.13v1.4.0#

Bun now useszlib-ng, the same library Node.js 24 and Chromium use, fornode:zlib, gzippedfetch()responses, and everything else that compresses. It picks the fastest code path for your CPU at runtime.#29433

Time per call on 1 MB of JSON, default level:

Encoding
Operation
Bun 1.4
Bun 1.3
Node.js 26
Deno 2.9
gzip
gzipSync
9.36 ms
9.11 ms
10.27 ms
9.76 ms
gzip
gunzipSync
1.28 ms
1.56 ms
2.11 ms
2.06 ms
deflate
inflateSync
1.21 ms
1.54 ms
1.95 ms
2.07 ms
brotli
brotliDecompressSync
1.38 ms
1.40 ms
2.11 ms
2.39 ms
zstd
zstdCompressSync
2.09 ms
2.18 ms
2.09 ms
2.18 ms
zstd
zstdDecompressSync
0.81 ms
0.73 ms
1.57 ms
1.65 ms

Peak memory, same runs:

Encoding
Operation
Bun 1.4
Bun 1.3
Node.js 26
Deno 2.9
gzip
gzipSync
50 MB
74 MB
75 MB
69 MB
gzip
gunzipSync
62 MB
94 MB
125 MB
129 MB
deflate
inflateSync
63 MB
94 MB
126 MB
128 MB
brotli
brotliDecompressSync
73 MB
110 MB
129 MB
130 MB
zstd
zstdCompressSync
55 MB
79 MB
77 MB
71 MB
zstd
zstdDecompressSync
62 MB
95 MB
128 MB
136 MB

Compression speed depends on the input. On JSON, gzip compression is the same speed as Bun 1.3. On repetitive HTML,gzipSyncon 1 MB takes 3.9 ms instead of 5.75 ms. Decompression is about 20% faster on everything, and peak memory is 25–35 MB lower.

Benchmark code: zlib-bench.mjs
// node:zlib benchmark: compress/decompress a JSON-like text buffer, one scenario per process.

// Usage: <runtime> zlib-bench.mjs <gzip|deflate|brotli|zstd> <sync|async> <compress|decompress> [level] [--bytes=N] [--iters=N]

// e.g. bun zlib-bench.mjs gzip sync compress --bytes=1048576 --iters=50

// node zlib-bench.mjs brotli async compress

// deno run -A zlib-bench.mjs zstd sync decompress 3

// --bytes: input size (default 64 MiB). --iters: timed iterations (default 1); with >1, warms up

// 5 iterations and reports the median. Prints one JSON line: {encoding, api, op, level, ms, iters,

// inputBytes, compressedBytes}. Wrap with `/usr/bin/time -v` to get peak RSS.

import
 
*
 
as
 zlib 
from
 
"
node:zlib
"
;

const
 flags 
=
 
Object
.
fromEntries
(

 process.argv

 .
slice
(
2
)

 .
filter
((
a
) 
=>
 a.
startsWith
(
"
--
"
))

 .
map
((
a
) 
=>
 a.
slice
(
2
).
split
(
"
=
"
)),

);

const
 [encoding, api, op, levelArg] 
=
 process.argv

 .
slice
(
2
)

 .
filter
((
a
) 
=>
 
!
a.
startsWith
(
"
--
"
));

const
 level 
=
 levelArg 
===
 
undefined
 
?
 
undefined
 
:
 
Number
(levelArg);

const
 TARGET 
=
 
Number
(flags.bytes 
??
 
64
 
*
 
1024
 
*
 
1024
);

const
 ITERS 
=
 
Number
(flags.iters 
??
 
1
);

// Deterministic JSON-lines text; a few fields vary per record so it is not trivially repetitive.

function
 
makeInput
() {

 
let
 seed 
=
 
0x9e3779b9
;

 
const
 
rnd
 
=
 () 
=>
 (seed 
=
 (seed 
*
 
1103515245
 
+
 
12345
) 
>>>
 
0
) 
/
 
2
 
**
 
32
;

 
const
 cities 
=
 [

 
"
Berlin
"
,

 
"
Tokyo
"
,

 
"
Austin
"
,

 
"
Lagos
"
,

 
"
Lima
"
,

 
"
Oslo
"
,

 
"
Pune
"
,

 
"
Quito
"
,

 ];

 
const
 words 
=
 [

 
"
alpha
"
,

 
"
bravo
"
,

 
"
charlie
"
,

 
"
delta
"
,

 
"
echo
"
,

 
"
foxtrot
"
,

 
"
golf
"
,

 
"
hotel
"
,

 
"
india
"
,

 
"
juliet
"
,

 ];

 
const
 parts 
=
 [];

 
let
 size 
=
 
0
;

 
for
 (
let
 i 
=
 
0
; size 
<
 TARGET; i
++
) {

 
const
 tags 
=
 
Array
.
from
(

 { length
:
 
3
 },

 () 
=>
 words[(
rnd
() 
*
 words.length) 
|
 
0
],

 );

 
const
 rec 
=
 {

 id
:
 i,

 uuid
:
 
`
${
((
rnd
()
 
*
 
2
 
**
 
32
)
 
>>>
 
0
)

 
.
toString
(
16
)

 
.
padStart
(
8
, 
"
0
"
)
}
-4c1e-8a2b-
${
i.
toString
(
16
).
padStart
(
12
, 
"
0
"
)
}
`
,

 user
:
 
`user_
${
(
rnd
()
 
*
 
50000
)
 
|
 
0
}
`
,

 email
:
 
`person
${
(
rnd
()
 
*
 
1e6
)
 
|
 
0
}
@example.com`
,

 city
:
 cities[(
rnd
() 
*
 cities.length) 
|
 
0
],

 score
:
 
Math
.
round
(
rnd
() 
*
 
10000
) 
/
 
100
,

 active
:
 
rnd
() 
>
 
0.5
,

 tags,

 ts
:
 
1700000000000
 
+
 ((
rnd
() 
*
 
1e9
) 
|
 
0
),

 note
:

 
"
lorem ipsum dolor sit amet, consectetur adipiscing elit 
"
 
+

 words[i 
%
 words.length],

 };

 
const
 line 
=
 
JSON
.
stringify
(rec) 
+
 
"
\n
"
;

 parts.
push
(line);

 size 
+=
 line.length;

 }

 
return
 Buffer.
from
(parts.
join
(
""
), 
"
latin1
"
);

}

const
 fns 
=
 {

 gzip
:
 [zlib.gzipSync, zlib.gzip, zlib.gunzipSync, zlib.gunzip],

 deflate
:
 [zlib.deflateSync, zlib.deflate, zlib.inflateSync, zlib.inflate],

 brotli
:
 [

 zlib.brotliCompressSync,

 zlib.brotliCompress,

 zlib.brotliDecompressSync,

 zlib.brotliDecompress,

 ],

 zstd
:
 [

 zlib.zstdCompressSync,

 zlib.zstdCompress,

 zlib.zstdDecompressSync,

 zlib.zstdDecompress,

 ],

};

const
 [cSync, cAsync, dSync, dAsync] 
=
 fns[encoding];

if
 (
!
cSync) {

 console.
log
(
JSON
.
stringify
({ encoding, api, op, error
:
 
"
unsupported
"
 }));

 process.
exit
(
0
);

}

const
 opts 
=

 level 
===
 
undefined

 
?
 {}

 
:
 encoding 
===
 
"
brotli
"

 
?
 { params
:
 { [zlib.constants.
BROTLI_PARAM_QUALITY
]
:
 level } }

 
:
 { level };

const
 input 
=
 
makeInput
();

const
 compressed 
=
 op 
===
 
"
decompress
"
 
?
 
cSync
(input, opts) 
:
 
null
;

const
 [syncFn, asyncFn, data] 
=

 op 
===
 
"
decompress
"
 
?
 [dSync, dAsync, compressed] 
:
 [cSync, cAsync, input];

const
 
once
 
=
 () 
=>

 
new
 
Promise
((
resolve
, 
reject
) 
=>
 {

 
const
 t0 
=
 performance.
now
();

 
if
 (api 
===
 
"
sync
"
)

 
return
 
resolve
([
syncFn
(data, opts), performance.
now
() 
-
 t0]);

 
asyncFn
(data, opts, (
err
, 
out
) 
=>

 err 
?
 
reject
(err) 
:
 
resolve
([out, performance.
now
() 
-
 t0]),

 );

 });

let
 out,

 times 
=
 [];

if
 (ITERS 
>
 
1
) 
for
 (
let
 i 
=
 
0
; i 
<
 
5
; i
++
) 
await
 
once
();

for
 (
let
 i 
=
 
0
; i 
<
 ITERS; i
++
) {

 
const
 [o, ms] 
=
 
await
 
once
();

 out 
=
 o;

 times.
push
(ms);

}

times.
sort
((
a
, 
b
) 
=>
 a 
-
 b);

const
 ms 
=
 times[times.length 
>>
 
1
];

console.
log
(

 
JSON
.
stringify
({

 encoding,

 api,

 op,

 level
:
 level 
??
 
"
default
"
,

 ms
:
 
Math
.
round
(ms 
*
 
1000
) 
/
 
1000
,

 iters
:
 ITERS,

 inputBytes
:
 input.length,

 compressedBytes
:
 op 
===
 
"
decompress
"
 
?
 compressed.length 
:
 out.length,

 }),

);

### Buffer.from(str, "hex")is 8× faster and"base64url"46× fasterv1.4.0#

Buffer.from(str, "hex")andBuffer.from(str, "base64url")decode with SIMD.

Decoding 1 MiB:

Encoding
Bun 1.4
Bun 1.3
Node.js 26
Deno 2.9
hex
128 µs
1,035 µs
743 µs
3,863 µs
base64url
84 µs
3,897 µs
68 µs
104 µs

Decoding 128 KiB:

Encoding
Bun 1.4
Bun 1.3
Node.js 26
Deno 2.9
hex
15.1 µs
130.6 µs
102.7 µs
494.0 µs
base64url
11.6 µs
486.2 µs
17.0 µs
14.4 µs
Benchmark code: buffer-from-bench.mjs
import
 { Buffer } 
from
 
"
node:buffer
"
;

const
 sizes 
=
 [
1024
, 
128
 
*
 
1024
, 
1024
 
*
 
1024
];

const
 
raw
 
=
 (
n
) 
=>
 {

 
const
 b 
=
 Buffer.
alloc
(n);

 
for
 (
let
 i 
=
 
0
; i 
<
 n; i
++
) b[i] 
=
 (i 
*
 
2654435761
) 
>>>
 
24
;

 
return
 b;

};

for
 (
const
 enc 
of
 [
"
hex
"
, 
"
base64
"
, 
"
base64url
"
]) {

 
for
 (
const
 n 
of
 sizes) {

 
const
 str 
=
 
raw
(n).
toString
(enc);

 
let
 sink 
=
 
0
;

 
for
 (
let
 i 
=
 
0
; i 
<
 
200
; i
++
) sink 
+=
 Buffer.
from
(str, enc).length; 
// warm up

 
const
 iters 
=
 n 
>=
 
1024
 
*
 
1024
 
?
 
300
 
:
 n 
>=
 
128
 
*
 
1024
 
?
 
2000
 
:
 
100000
;

 
const
 times 
=
 [];

 
for
 (
let
 rep 
=
 
0
; rep 
<
 
5
; rep
++
) {

 
const
 t0 
=
 performance.
now
();

 
for
 (
let
 i 
=
 
0
; i 
<
 iters; i
++
) sink 
+=
 Buffer.
from
(str, enc).length;

 times.
push
(((performance.
now
() 
-
 t0) 
*
 
1000
) 
/
 iters);

 }

 times.
sort
((
a
, 
b
) 
=>
 a 
-
 b);

 console.
log
(enc, n 
/
 
1024
, 
"
KiB
"
, times[
2
].
toFixed
(
2
), 
"
µs/op
"
);

 }

}

### Source map decoding is 3.1× fasterv1.4.0#

Source map decoding uses SIMD.new SourceMap(json)on a 9.5 MB map takes 12 ms, 3.1× faster than before and 24× faster than Node.js.#32556

`new SourceMap(payload)` & sourcemap decoding gets up to 3x faster

### Promises are 1.5–2.4× fasterv1.4.0#

JavaScriptCore rewrote their Promise implementation to reduce overhead.

Time per operation, 2 million iterations:

Operation
Bun 1.4
Bun 1.3
Promise.race
 of 4 promises
142 ns
342 ns
Promise.all
 of 4 promises
207 ns
316 ns
Promise.allSettled
 of 4 promises
253 ns
411 ns
await
 a resolved promise
84 ns
143 ns
.then()
 chain of 4
172 ns
332 ns
async
 function with no 
await
37 ns
89 ns

Memory: 1,000,000 pending promises resolved at once.

Bun 1.4
Bun 1.3
Peak memory
251 MB
668 MB
Time to settle
12.5 ms
39.0 ms
Benchmark code: promise-bench.mjs and promise-rss.mjs
// Promise microbenchmarks. Prints ns/op per operation as JSON.

// Usage: bun promise-bench.mjs | node promise-bench.mjs | deno run -A promise-bench.mjs

const
 WARMUP 
=
 
1e5
;

const
 ITERS 
=
 
2e6
;

const
 p1 
=
 
Promise
.
resolve
(
1
),

 p2 
=
 
Promise
.
resolve
(
2
),

 p3 
=
 
Promise
.
resolve
(
3
),

 p4 
=
 
Promise
.
resolve
(
4
);

const
 arr 
=
 [p1, p2, p3, p4];

async
 
function
 
noAwait
(
x
) {

 
return
 x;

}

const
 benches 
=
 {

 
"
Promise.race (4 resolved)
"
:
 () 
=>
 
Promise
.
race
(arr),

 
"
Promise.all (4 resolved)
"
:
 () 
=>
 
Promise
.
all
(arr),

 
"
Promise.allSettled (4 resolved)
"
:
 () 
=>
 
Promise
.
allSettled
(arr),

 
"
await resolved promise
"
:
 
async
 () 
=>
 {

 
await
 p1;

 },

 
"
.then() chain of 4
"
:
 () 
=>

 p1

 .
then
((
x
) 
=>
 x)

 .
then
((
x
) 
=>
 x)

 .
then
((
x
) 
=>
 x)

 .
then
((
x
) 
=>
 x),

 
"
async fn, no await
"
:
 () 
=>
 
noAwait
(
1
),

};

async
 
function
 
time
(
fn
, 
n
) {

 
const
 t0 
=
 performance.
now
();

 
for
 (
let
 i 
=
 
0
; i 
<
 n; i
++
) 
await
 
fn
();

 
return
 ((performance.
now
() 
-
 t0) 
*
 
1e6
) 
/
 n;

}

const
 results 
=
 {};

for
 (
const
 [name, fn] 
of
 
Object
.
entries
(benches)) {

 
await
 
time
(fn, WARMUP);

 results[name] 
=
 
Math
.
round
((
await
 
time
(fn, ITERS)) 
*
 
10
) 
/
 
10
;

}

console.
log
(
JSON
.
stringify
(results));
// promise-rss.mjs: peak memory of 1,000,000 pending promises resolved at once

const
 N 
=
 
1_000_000
;

const
 resolvers 
=
 [];

const
 promises 
=
 
Array
.
from
(

 { length
:
 N },

 () 
=>
 
new
 
Promise
((
r
) 
=>
 resolvers.
push
(r)),

);

const
 all 
=
 
Promise
.
all
(promises);

for
 (
const
 r 
of
 resolvers) 
r
(
1
);

const
 t0 
=
 performance.
now
();

await
 all;

console.
log
(

 
`
${
N
}
 promises settled in 
${
(performance.
now
()
 
-
 
t0).
toFixed
(
1
)
}
 ms`
,

);

## Security#

Bun 1.4 includes a lot of security fixes. We recommend everyone update. Most of them change nothing you'd notice. They are listed underSecurity hardeningin the changelog. The handful below tighten a default, in most cases a TLS certificate check. That can turn a connection that worked on 1.3 into a verification error. Advisories will go up onGitHubonce people have had time to upgrade.

### checkServerIdentityruns beforefetch()sends the requestv1.4.0#

When you passtls: { checkServerIdentity }tofetch(), the callback runs after the TLS handshake and before any of the request is written, and again on each redirect hop. If it returns anError,fetch()rejects with that error and nothing is sent.

await
 
fetch
(
"
https://api.example.com/upload
"
, {

 method
:
 
"
POST
"
,

 body
:
 secretPayload,

 tls
:
 {

 
checkServerIdentity
(
hostname
, 
cert
) {

 
if
 (cert.fingerprint256 
!==
 PINNED) 
return
 
new
 
Error
(
"
pin mismatch
"
);

 },

 },

});

// nothing is sent until checkServerIdentity returns undefined

If you pin a certificate this way and the URL redirects through a host with a different one, the callback now sees that certificate too, so either accept every hop's certificate there or passredirect: "manual"and followLocationyourself.

### tls.connectnow useshostas the defaultservernamev1.3.13#

tls.connect({ host, port })without aservernamenow useshostfor both SNI and the certificate identity check. This matches Node.js. Connecting by IP address or tolocalhostnow fails withERR_TLS_CERT_ALTNAME_INVALIDwhen the certificate was issued for another name. This applies whether you calltls.connect()yourself or a driver likepgorioredisdoes. Pass the certificate's name asservername. Or passcheckServerIdentity: () => undefinedif you deliberately trust the server by its CA alone.

tls.
connect
({

 host
:
 
"
10.0.0.12
"
,

 port
:
 
5432
,

 ca,

 servername
:
 
"
db.internal
"
,

});

### Bun.connectandBun.listenenforcerejectUnauthorizedv1.4.0#

Bun.connect({ tls }),socket.upgradeTLS(), andBun.listen()withrequestCert: truenow default torejectUnauthorized: true, asnode:tlsandfetch()do. The usual case is aBun.connect()to a dev or staging server with a self-signed or private-CA certificate and noca. It does not throw. Thehandshakehandler runs withsocket.authorizedset tofalse. Writes return-1. The socket closes without delivering data. Pass the CA intls, or passrejectUnauthorized: false(NODE_TLS_REJECT_UNAUTHORIZED=0is honored here too).

### RedisClientenforces TLS hostname verificationv1.3.14#

Arediss://RedisClientchecks the server certificate against the host in the URL, as the Postgres and MySQL clients do, and rejects the first command withERR_TLS_CERT_ALTNAME_INVALIDon a mismatch. If you reach Redis by IP or through a port-forward tolocalhost, connect by the name on the certificate instead, or passtls: { rejectUnauthorized: false }.

### HTTP request parsing hardening inBun.servev1.3.4#

Bun.serve()answers400and closes the connection for more kinds of malformedContent-LengthandTransfer-Encodingheaders and chunked bodies. Browsers, curl,fetch()and reverse proxies send none of them. If a hand-written client starts getting400responses, look at its framing headers first; Bun does not call yourfetchhandler or log anything for most of these.

### Tarball extraction hardeningv1.3.6#

Tarball extraction forgithub:and URL dependencies andbun createtemplates skips entries that would land outside the package directory. If one of those is missing a file after the upgrade and you getCannot find modulefor it, look in its repo for a symlink that points outside the package, and replace it with the real file or a relative link.

## Platforms#

### Native FreeBSD buildsv1.3.14v1.4.0#

Bun now ships official FreeBSD binaries for x86_64 and aarch64. On FreeBSD 14.3+ the full runtime (Bun.serve(),fetch(),node:fs,node:os,Bun.spawn) works on a stock install with no extra system packages. This is a native port built against FreeBSD's own kernel APIs, not a Linux compatibility layer.#29676

curl -fsSL https://bun.sh/install 
|
 bash
uname -sm
FreeBSD amd64
bun --version
1.4.0

### Windows on ARM64v1.3.7v1.4.0#

Bun now builds natively for Windows on ARM64. Surface, Snapdragon X, and Ampere-based Windows machines run Bun natively.#26215

PS
>
 powershell -c 
"
irm bun.sh/install.ps1|iex
"

PS
>
 
$env
:PROCESSOR_ARCHITECTURE

ARM64

PS
>
 bun --version

1.4.0

### Experimental Android supportv1.4.0#

Bun ships experimental Android builds for aarch64 and x64 with every release.

### Linux glibc minimum drops to 2.17v1.3.13#

Bun's minimum glibc requirement on Linux drops from 2.26 to 2.17. Bun now runs on RHEL/CentOS 7, Amazon Linux 1, and ARM64 Linux distributions without needing a separate compatibility build.#29461

ldd --version
ldd (GNU libc) 2.17
bun --version
1.4.0

### Fallback for in-memory files on older Linux kernelsv1.3.13#

On Linux kernels older than 3.17, like RHEL 7, Bun detects thatmemfd_createis missing once and falls back. The documented minimum kernel is now 3.10.#29465

BUN_FEATURE_FLAG_DISABLE_MEMFD=1 bun run server.ts

### Ready for TypeScript 7#

bun initand the React templates ship atsconfig.jsonthat works with TypeScript 7, and@types/bunresolves cleanly against it.#28542#39341

{

 
"
compilerOptions
"
:
 {

 
"
types
"
:
 [
"
bun
"
]

 }

}

### Sub-15 ms timers on Windowsv1.4.0#

On Windows,setTimeout(fn, 1)fires in about 1.4 ms instead of 15.5 ms. Timers no longer round to the 15.6 ms system tick.#34834

Improved timer accuracy on Windows makes `Bun.sleep` faster

### Bun runs inside an AppContainerv1.4.0#

Bun runs inside a WindowsAppContainer, so embedders can sandbox it with a lowbox token.

bun install,bun run,Bun.spawn,child_process.fork, andBun.Terminalall work inside the container.

Bun also now works on read-only directories like Program Files and read-only network shares, and no longer fails when an ancestor directory isn't readable.

## Upgrading to 1.4#

Most code is unaffected. Five changes are the most likely to need a line in your project:

* Node.js 26:process.versions.modulesis now147. Packages that pick a prebuilt native addon byNODE_MODULE_VERSIONneed a build for147.res.writeHeader()is gone; useres.writeHead(). Paused-modereadable.read()returns one chunk.#31991
* New monorepos default to the isolated linker.bun.lockrecordsconfigVersion: 1. Existing lockfiles keep the hoisted linker. To opt out, pinlinker = "hoisted"inbunfig.toml.#24236
* Bun invoked asnode(bun --bun,bunx --bun, anodesymlink) does not load.envfiles. This matches Node. Pass--env-fileto keep them.#36610
* Bun.YAMLfollows YAML 1.2:yes/no/on/offare strings.on:in a GitHub Actions workflow parses as"on".#25537
* Bun.TOMLandbunfig.tomlare strict: unquoted strings, missing newlines between pairs, and integers pastNumber.MAX_SAFE_INTEGERareSyntaxErrors.#32953
Every behavior change in 1.4

### Node.js 26:NODE_MODULE_VERSION147,res.writeHeader()removed, pausedread()returns one chunkv1.4.0#

Bun now reportsNode.js 26. Three things change:

* process.versions.modulesis147. Packages that pick a prebuilt native addon byNODE_MODULE_VERSIONneed a build for147.
* res.writeHeader()innode:httpis removed. Callres.writeHead().
* In paused mode,readable.read()with no size returns one buffered chunk. Before, it returned the whole buffer. (setEncoding()keeps the old behavior.) Loop until it returnsnull.

#31991

res.
writeHeader
(
200
, { 
"
Content-Type
"
:
 
"
text/plain
"
 });

res.
writeHead
(
200
, { 
"
Content-Type
"
:
 
"
text/plain
"
 });

### x64 builds are now baseline-onlyv1.4.0#

x64 releases now ship only the baseline build. The separate build compiled with-march=haswellis gone. The-baselinedownload URLs and npm packages still exist and contain the same binary. Existing install scripts andbun upgradekeep working. TheCPU lacks AVX supportstartup warning is removed.#34782

### Temporalis now defined by default, andtoEqual()compares Temporal objects by valuev1.4.0#

TemporalandDate.prototype.toTemporalInstantare now defined. SetBUN_JSC_useTemporal=0to turn them off.Bun.deepEquals(),toEqual(),toStrictEqual(), andutil.isDeepStrictEqual()now compare Temporal objects by value. Before, any two instances of the same class were equal.#32978#37024

Bun.
deepEquals
(

 Temporal.PlainDate.
from
(
"
2020-01-01
"
),

 Temporal.PlainDate.
from
(
"
1999-12-31
"
),

); 
// false

### bun:ffi:cstringvalues are plain strings andCStringno longer has.ptrv1.4.0#

bun:ffiis nowengine-native. This changes four things:

* Areturns: "cstring"value or acstringcallback argument is a plain string. ANULLpointer isnull.
* new CString(ptr)returns a string with no.ptr,.byteLength, or.arrayBuffer. Keep the original pointer if you need to free it.
* napi_envandnapi_valueargument types throwTypeErroroutsidecc().
* dlopen()and the other entry points throwTypeErrorwhen the JIT is disabled.

#35246

const
 str 
=
 
new
 
CString
(ptr);

my_library_free
(str.ptr);

my_library_free
(ptr);

### bun build --compileno longer auto-loadstsconfig.jsonorpackage.jsonat runtimev1.3.4#

Standalone executables built withbun build --compileno longer auto-loadtsconfig.jsonorpackage.jsonfrom the runtime working directory. Before, a compiled binary could pick up unrelated config files from the directory it ran in. To opt back in, pass--compile-autoload-tsconfig/--compile-autoload-package-json(orcompile.autoloadTsconfig/compile.autoloadPackageJsoninBun.build())..envandbunfig.tomlstill auto-load by default. They keep their existing--compile-autoload-dotenv/--compile-autoload-bunfigflags.#25340

### bun installdefaults to the isolated linker for new monoreposv1.3.2#

New monorepos (projects with workspaces) now uselinker: "isolated". This is a symlinkednode_moduleslayout that prevents phantom dependencies.bun.lockrecords aconfigVersion. Existing lockfiles (config version 0) keep the hoisted linker they were created with. Yournode_moduleslayout does not change on upgrade.#24236

# bunfig.toml: pin the old behavior if you need it

[
install
]

linker
 
=
 
"
hoisted
"

### bun.lockis nowlockfileVersion: 2v1.4.0#

New lockfiles use version 2. Version 2 adds two stricter parse-time checks:

* npm packages resolved to a tarball outside your configured registry must carry an integrity hash.
* git dependency entries are validated to block path traversal (no/,\, or..).

Lockfiles written as v0/v1 keep loading without these checks. Existing projects do not break. Runbun installto migrate.

{

 
"
lockfileVersion
"
:
 
1
,

 
"
lockfileVersion
"
:
 
2
,

 
"
workspaces
"
:
 { 
...
 },

### Bun invoked asnodeno longer loads.envfilesv1.4.0#

When Bun runs asnode(underbun --bun,bunx --bun, or anodesymlink to Bun), it no longer loads.env,.env.local, or.env.{development,production,test}. This matches Node.js.bun file.jsstill loads them. Apackage.jsonscript that callsnodeunderbun --bun runnow sees those variables asundefined. To keep them, pass--env-filetonode.#36610

"
scripts
"
: {

 
"
check
"
:
 
"
node ./check.js
"

 
"
check
"
:
 
"
node --env-file=.env ./check.js
"

### Bun.YAMLnow parsesyes/no/on/offas strings, not booleansv1.3.5#

Bun.YAMLnow parses booleans per the YAML 1.2 spec.yes/no/on/off/y/Yare plain strings, not booleans. These are YAML 1.1 legacy values that the 1.2 spec dropped. Anon:key in a GitHub Actions workflow file now parses as the string"on", nottrue. Onlytrue/True/TRUEandfalse/False/FALSEresolve to booleans.#25537

Bun.
YAML
.
parse
(
"
on: push
"
);

// { on: "push" }

### Bun.TOML.parse()andbunfig.tomlare stricter and throwSyntaxErrorv1.4.0#

The rewrittenBun.TOMLparser throwsSyntaxErrorinstead ofBuildMessage. It rejects TOML that the old parser let through:

* unquoted string values
* missing newlines between key/value pairs
* integers outsideNumber.MAX_SAFE_INTEGER

Abunfig.tomlwith an unquoted value now fails at startup withTOML Parse error: Strings must be quoted. Quote the value.#32953

[
install
]

linker
 
=
 i
solated

linker
 
=
 
"
isolated
"

### .xmlimports now return the parsed document instead of the file pathv1.4.0#

importorrequire()of a.xmlfile now returns the same object asBun.XML.parse(). This applies at runtime and inbun build. Before, it returned the file's path. A file that does not parse throws at runtime and fails the build. To keep getting the path, pass--loader .xml:file.#37048

### import "."andimport ".."now resolve as directoriesv1.4.0#

"."and".."inimportandrequire()now resolve to the directory's index file orpackage.jsonmain. This matches Node.js. Before, they resolved to a sibling file with the directory's name. So"."insidelib/run.tsloadedlib.ts; it now loadslib/index.ts. To keep the sibling, name it.#36969

import
 { e } 
from
 
"
.
"
;

import
 { e } 
from
 
"
../lib
"
;

### .cssimports at runtime now export{}instead of the file pathv1.4.0#

At runtime, the default export of a.cssimport is now{}. This applies toimport,require(), dynamicimport(), and Workers. Before, it was the file's absolute path as a string.bun buildalready emitted{}..module.cssstill differs frombun build, which emits a class-name map.#35163

### "jsx": "react-jsx"intsconfig.jsonnow emitsjsxinstead ofjsxDEVv1.4.0#

With"jsx": "react-jsx",bun runandbun buildnow importjsxandjsxsfrom<pkg>/jsx-runtime. Before, both importedjsxDEVfrom<pkg>/jsx-dev-runtimeunlessNODE_ENV=productionor--productionwas set. An explicitNODE_ENVstill wins. To keep the development runtime, set"jsx": "react-jsxdev".#34422

{

 
"
compilerOptions
"
:
 {

 
"
jsx
"
:
 
"
react-jsx
"

 
"
jsx
"
:
 
"
react-jsxdev
"

 }

}

### useDefineForClassFields: falseintsconfig.jsonis now honoredv1.4.0#

WithuseDefineForClassFields: false, Bun now does what tsc does:

* Instance field initializers move into the constructor, after parameter-property assignments.
* Plain declaration-only fields are dropped.

Before, the option was ignored. An initializer that reads a parameter property now works instead of throwing. Private and decorated fields keep their declarations. Static fields and classes with a computed non-literal field key are left as they were. To keep the old output, remove the option.#36664

### Bun.Socket#setKeepAlive()now treatsinitialDelayas millisecondsv1.4.0#

setKeepAlive(true, delay)on aBun.Socketnow dividesdelayby 1000 before settingTCP_KEEPIDLE, as documented. Before, the raw value was used as seconds, so4000meant 4000 seconds. A value under 1000 now divides to0and leavesTCP_KEEPIDLEunchanged. Code that passed seconds should pass milliseconds.setKeepAlive(true)now returnstrueinstead offalse.net.Socket#setKeepAlive()still sets the same kernel value as before.#34269

socket.
setKeepAlive
(
true
, 
60
);

socket.
setKeepAlive
(
true
, 
60_000
);

### Bun.mmap({ offset })now starts the view atoffsetv1.4.0#

Bun.mmap(path, { offset })now returns a view whose index 0 is the byte atoffset. Before,offsetwas rounded down to a page boundary. The view started at that boundary, for reads and for writes through{ shared: true }. Remove anyoffset % pageSizeadjustment you added to compensate.#34120

const
 m 
=
 Bun.
mmap
(
"
data.bin
"
, { offset
:
 
100
 });

m[
0
]; 
// byte 0 of the file

m[
0
]; 
// byte 100 of the file

### Bun.cron.parse()and in-processBun.cron()now use local timev1.4.0#

Bun.cron.parse()and the in-processBun.cron(schedule, handler)overload now read schedules in the process's local time zone. Before, they used UTC. This matches the OS-registered overload."0 9 * * *"underTZ=America/Los_Angelesnow means 9:00 Pacific. To keep the old times, pass{ tz: "UTC" }. Both accept it as a new final argument.#35122

Bun.
cron
(
"
0 9 * * *
"
, handler);

Bun.
cron
(
"
0 9 * * *
"
, handler, { tz
:
 
"
UTC
"
 });

### Bun.$now globs only patterns written in the template itselfv1.4.0#

Glob characters that arrive through${...}, a shell variable, command substitution, or quoted text are now literal. Only*,**, and braces written directly in the template expand.?,[...], and a leading!are literal everywhere. Before,$`echo ${"**/"}*`matched recursively. It now fails withno matches found. Write the pattern in the template instead.#31220

await
 
$
`echo 
${
"
**/
"
}
*`
;

await
 
$
`echo **/*`
;

### fs.rmdirno longer accepts{ recursive: true }v1.4.0#

Passingrecursive: truetofs.rmdirnow throwsERR_INVALID_ARG_VALUE. This matches Node.js, which removed the option after a long deprecation. Usefs.rminstead.#31830

await
 fs.
rmdir
(
"
build
"
, { recursive
:
 
true
 });

await
 fs.
rm
(
"
build
"
, { recursive
:
 
true
, force
:
 
true
 });

### X509Certificateserial and modulus are now uppercase hexv1.4.0#

X509Certificate#serialNumber,.toLegacyObject().modulus, andtls.TLSSocket#getPeerCertificate()now return uppercase hex. This matches Node.js andopenssl x509 -serial. If you pin certificates against a lowercase serial string, normalize the case first.#31519

const
 { serialNumber } 
=
 
new
 
X509Certificate
(pem);

// "3b8e2a..."

// "3B8E2A..."

### tls.createServer({ requestCert: true })now rejects unverified client certificatesv1.4.0#

Anode:tlsserver withrequestCert: trueand no explicitrejectUnauthorizednow applies the default oftrue. A connection whose client certificate does not verify is destroyed, and the server emitstlsClientError. Before, it reached your handler withauthorized: false. To keep admitting those clients, passrejectUnauthorized: false.#31322

tls.
createServer
({

 ca,

 requestCert
:
 
true
,

 rejectUnauthorized
:
 
false
,

});

### dgram.Socketnow throws synchronously on a secondbind()and afterclose()v1.4.0#

Twonode:dgramchanges, both matching Node.js:

* bind()on a socket that is already bound throwsERR_SOCKET_ALREADY_BOUND. Before, it emitted anerrorevent.
* bind(),send(),address(),remoteAddress(), andclose()on a closed socket throwERR_SOCKET_DGRAM_NOT_RUNNING. Before, they threw an uncodedTypeError(or, forbind(), emitted anerrorevent).

Code that handled a secondbind()in anerrorlistener needs atry/catch.#33037#33024

### dns.lookup()now uses the system resolver on Linuxv1.4.0#

On Linux,dns.lookup(),dns.promises.lookup(), and hostname resolution innet.connect()now go throughgetaddrinfo(), as in Node.js. Before, they used c-ares. Names that onlysystemd-resolvedor a split-DNS VPN knows now resolve. Before, they failed withgetaddrinfo EREFUSED.dns.setServers()no longer affects these calls.dns.resolve*()andBun.dns.lookup()still use c-ares. If you need the old behavior for a lookup, pass{ backend: "c-ares" }toBun.dns.lookup().#37383

### Exceptions thrown innode:fs,node:dns, andcrypto.pbkdf2callbacks are nowuncaughtExceptionv1.4.0#

An exception thrown inside anode:fs,node:dns, orcrypto.pbkdf2()callback now reachesprocess.on("uncaughtException"), as in Node.js. Before, it surfaced as anunhandledRejection. A handler registered there no longer sees it. Move the handler.#34660

fs.
readFile
(
"
config.json
"
, () 
=>
 { 
throw
 
new
 
Error
(
"
bad config
"
); });

process.
on
(
"
unhandledRejection
"
, onError);

process.
on
(
"
uncaughtException
"
, onError);

### net.Serverandtls.Serverno longer auto-resume accepted sockets;tls.ServerchecksrequestCertandrejectUnauthorizedliterallyv1.4.0#

* Sockets accepted bynet.Serverortls.Serverare no longer resumed automatically. Bytes that arrive before a'data'listener is attached are buffered, as in Node.js.
* Only a literalrejectUnauthorized: falsedisables verification. This applies totls.connect()andtls.Server. Before,nulldid too.
* requestCertmust be literallytrue.
* Atls.Serverno longer readsNODE_TLS_REJECT_UNAUTHORIZEDfor its default.
* handshakeTimeoutnow also emits the socket's'timeout'event (after'tlsClientError'). It leaves the socket open instead of destroying it.
* An exception thrown in anonreadcallback or'secureConnection'listener is now an uncaught exception.

#32630#34598#35006

tls.
createServer
({

 key,

 cert,

 ca,

 requestCert
:
 
1
,

 rejectUnauthorized
:
 
null
,

 requestCert
:
 
true
,

 rejectUnauthorized
:
 
false
,

});

### fetch()responses andBun.serverequests now combine duplicate headers with,v1.4.0#

Duplicate headers on afetch()response or aBun.serverequest are now joined with,, per the Fetch spec. Before, only the last value was kept. Common headers were already combined. This change affects the rest, including every custom header.fetch()responses also keep empty values now. A header sent with no value reads""instead ofnull.Set-Cookiestill comes back as separate values fromgetSetCookie().#31734

// X-Dup: first

// X-Dup: second

res.headers.
get
(
"
x-dup
"
);

// "second"

// "first, second"

### Request#clone()andResponse#clone()now throw once the body has been readv1.4.0#

clone()on aRequestorResponsewhose body has been read, or whose stream is locked, now throwsTypeError: Body is disturbed or locked(ERR_BODY_ALREADY_USED). This is per the Fetch spec. It includes the request passed toBun.serveroute handlers. Before,clone()succeeded and the problem showed up later, as an empty body or an error when the clone was read. Callclone()before reading the body.#33129

const
 text 
=
 
await
 req.
text
();

const
 copy 
=
 req.
clone
();

const
 copy 
=
 req.
clone
();

const
 text 
=
 
await
 req.
text
();

### fetch()network errors are nowTypeError, and a failed body read setsbodyUsedv1.4.0#

fetch()and response body reads now reject a network error with aTypeError. Before, it was a plainError..code(for exampleECONNRESET) is still set. After a body read fails,bodyUsedistrue. A second read rejects withERR_BODY_ALREADY_USEDinstead of the socket error. Issue a newfetch()to retry.fetch(request)with a request whose stream body was already used now rejects with the sameTypeErrorbefore connecting.#35855#36499

const
 res 
=
 
await
 
fetch
(url); 
// connection drops mid-body

await
 res.
text
(); 
// rejects with Error, code "ECONNRESET"

await
 res.
text
(); 
// rejects with TypeError, code "ECONNRESET"

### Bun.serve({ inspector })has been removedv1.3.14#

The undocumentedinspector: trueoption is now silently ignored. It mounted a/bun:inspectdebugger WebSocket on your HTTP port. It predatedbun --inspectand was never in the public types. Use the--inspectflagto attach a debugger.#29613

Bun.
serve
({ inspector
:
 
true
, fetch });

Bun.
serve
({ fetch });
bun --inspect server.ts

### server.publish()andws.publish()now return0or-1under backpressurev1.4.0#

server.publish(),ws.publish(),ws.publishText(), andws.publishBinary()now return:

* 0if the message was dropped for any subscriber, or the topic had no subscribers
* -1if any subscriber has backpressure
* the byte count otherwise

Before, they returned the byte count whenever the topic had a subscriber, even when the data was discarded. Code that compares the return value against the byte count should treat0as dropped and-1as queued.#32889

### server.stop()now closes idle connections and waits for in-flight requestsv1.4.0#

server.stop()now closes idle keep-alive connections immediately. It closes busy ones once their response is sent. It resolves when the last connection has closed. Before, it closed only the listener and resolved while requests were still being served. It now stays pending on a connection that has sent part of a request and stopped.server.stop(true)closes such connections. It now works after a gracefulstop()too.#35130#37074

### WebSocket(global) no longer accepts anagentoptionv1.3.6#

The non-standardagentoption on the Web-standardWebSocketconstructor is removed. Node.js's globalWebSocketuses an undicidispatcher, not anhttp.Agent. The ws package'sWebSocket, which Bun polyfills natively, now acceptsagentinstead. This matches its documented API.#25935

const
 ws 
=
 
new
 
WebSocket
(url, { agent }); 
// global

import
 WebSocket 
from
 
"
ws
"
;

const
 ws 
=
 
new
 
WebSocket
(url, { agent }); 
// ws module

### WebSocket#close(),ping(), andpong()now validate their argumentsv1.4.0#

close()now throwsInvalidAccessErrorfor a code other than1000to1003,1007to1014, or3000to4999. It throwsSyntaxErrorfor a reason longer than 123 UTF-8 bytes. Before, an invalid code went out unchecked. With the default code, an over-long reason was silently sent as empty.ping()andpong()on theWebSocketclient,ServerWebSocket, and the ws package now throwRangeErrorfor a payload over 125 bytes. Before, they sent it. Shorten the reason or payload.#32820#35030

### WebSocketnow fails the handshake if a requested subprotocol is not negotiatedv1.4.0#

new WebSocket(url, protocols)now closes with code1002when the server's101response omitsSec-WebSocket-Protocol. This is per RFC 6455 and matches browsers. Before, it opened withws.protocol === "". Fix the server to echo a protocol, or stop passingprotocols. Connections that request no subprotocol are unaffected.#33072

### WebSocket#close()no longer firesclosebefore it returnsv1.4.0#

ws.close()andws.terminate()on aWebSocketclient now queue thecloseevent, as in Node.js and browsers. When the call returns,readyStateisCLOSINGandonclosehas not run yet. Code that readCLOSEDon the next line, or relied ononclosehaving run, should await thecloseevent instead.#27259

ws.
close
();

ws.readyState; 
// 3, CLOSED

ws.readyState; 
// 2, CLOSING

### jest.resetAllMocks()now drops mock implementationsv1.4.0#

jest.resetAllMocks()andvi.resetAllMocks()now reset every mock's implementation as well as its call history. This matches Jest. Before, they behaved likeclearAllMocks(). After the reset, ajest.fn(() => 42)returnsundefined. AspyOn()spy returnsundefineduntilmockRestore(). If you only want the call history cleared, callclearAllMocks().#33374

afterEach
(() 
=>
 {

 jest.
resetAllMocks
();

 jest.
clearAllMocks
();

});

### expect().toContain()now compares with===instead ofObject.isv1.4.0#

toContain()inbun:testnow compares array and iterable elements with===instead ofObject.is. This matches Jest.expect([-0]).toContain(0)passes andexpect([NaN]).toContain(NaN)fails.toBe()still usesObject.is.toContainEqual()still uses deep equality.#32950

expect
(values).
toContain
(
NaN
);

expect
([
...
values].
some
(
Number
.isNaN)).
toBe
(
true
);

### Bun.sqlnow decodes MySQLDATETIMEandTIMESTAMPas UTCv1.4.0#

MySQLDATETIMEandTIMESTAMPcolumns are now decoded as UTC. This matches howBun.sqlencodes them, so aDateround-trips unchanged. Before, it came back shifted by the machine's UTC offset on any host not running in UTC. Postgrestimestampread through.simple()is decoded as UTC too.timestamptzis unaffected. Remove any offset correction you added.#31212

await
 
sql
`INSERT INTO t (dt) VALUES (
${
new
 
Date
(
"
2024-06-15T12:00:00Z
"
)
}
)`
;

const
 [{ dt }] 
=
 
await
 
sql
`SELECT dt FROM t`
;

dt.
toISOString
(); 
// "2024-06-15T16:00:00.000Z" under TZ=America/New_York

dt.
toISOString
(); 
// "2024-06-15T12:00:00.000Z"

### Bun.sqlnow parses MariaDB 10.5+JSONcolumns instead of returning stringsv1.4.0#

On MariaDB 10.5 and later,Bun.sqlnow parsesJSONcolumns and JSON function results such asJSON_OBJECT()andJSON_EXTRACT(). Before, it returned the JSON text as a string. Ajsoncolumn holding{"b": 1}now reads as the object{ b: 1 }. Remove theJSON.parse().#37130

const
 [row] 
=
 
await
 
sql
`SELECT a FROM t`
;

const
 a 
=
 
JSON
.
parse
(row.a);

const
 a 
=
 row.a; 
// { b: 1 }

### Other behavior changesv1.4.0#

* Thebun feedbackcommand is removed.#38444
* Bun.password.hash()with argon2 now requiresmemoryCostof at least 8. Hashes made by Bun 1.3 with a lowermemoryCoststill verify.#39596
* bun updatenow moves transitive packages.bun update <name>errors (exit 1) on a name nothing depends on. Before, it added the package.--production/--prodonupdatemeans "only updatedependenciesandoptionalDependencies".-iupdates only the selection.#38333
* A project'sbunfig.tomlnow overrides any.npmrcfor the same key.#38333
* bun install <pkg> --filter xnow editsx, not the root.bun add y --filter xno longer installs a package namedx.add/remove --filter '*'no longer includes the root.#38333
* A plainbun add xin a workspace whose default catalog listsxnow writescatalog:.audit fixmay rewrite exact pins.--frozen-lockfile --lockfile-onlywrites nothing. Overrides/catalog changes fail frozen installs.#38333
* Projects withcatalog:peers or deadpkg@rangeoverride rows see one-time lockfile churn after upgrading. Lockfiles that use nested or version-scoped overrides arelockfileVersion: 3. Older Bun cannot read version 3. Turborepo and Nx changes to accept it are open upstream. Dependabot needs nothing.#38333
* bun initnow writes typescript^7. Before, it wrote^5, or nothing in the React templates. A fresh project installs TypeScript 7.#33265#39341
* bun initwith a non-TTY stdin (CI, a pipedspawn) now behaves asbun init -y. Before, it opened the template picker.#35165
* bun update -iwith a non-TTY stdin now exits with code1and an error. Before, it opened the picker. Usebun updateorbun outdated.#35165
* bun updatewith no package names now rewrites the rootcatalogandcatalogsentries (to the newest version with--latest). It leavescatalog:references in workspacepackage.jsonfiles in place. Before, it replaced them with^<version>. With--recursiveor--filter, it rewrites each selected workspace'spackage.json. It touches the root catalog only when the root is selected.#36304#36360#36379
* bun installandbun removenow drop a package frombun.lockwhen only an optional peer still points at it. A lockfile whose nested optional-peer placement differs from a fresh install may be rewritten once, on the first install after upgrading.#35681
* trustedDependenciesand--trustentries now match the exact package name. Before, they matched a truncated name hash. A package that only collides with an entry's hash no longer runs lifecycle scripts. If you meant to trust it, add the package's exact name. Entries loaded from a legacybun.lockbstill match by hash.#31218
* bun install --registry <url>no longer sends the configured registry's credentials to<url>when it is a different host, or when it downgrades fromhttps://tohttp://.#36165
* workspace:ranges are now honored only in the root and workspacepackage.jsonfiles. Inside a downloaded package, they fail to resolve like any other unknown range. Before, they created a workspace package.#37669
* Bun.JSONC.parse()now throwsSyntaxErroron invalid input. Before, it threw aBuildMessage.Bun.JSONC.parse("")also throwsSyntaxError. Before, it returned{}.#35066
* Wildcardexportsandimportstargets inpackage.jsonthat do not name an existing file are now retried with each known extension, or with.tsin place of.js. A subpath such as@modelcontextprotocol/sdk/server/stdionow resolves. Before, it failed withCannot find module.#36299
* bun buildnow bundles an unresolvablerequire(),require.resolve(), orawait import()insidecatchas a runtime throw. Before, it failed withCould not resolve.#35659
* Assigning to an imported binding is no longer a parse error at runtime. The module loads, and the assignment throwsTypeErrorwhen reached.bun buildstill reports it as an error.#36046
* bun build --target browsernow honors a package'sbrowserfield entry for a Node builtin ("crypto": falseor a remap). Before, it bundled the polyfill. It also resolvesrequire()of a package that hasjsnext:mainbut nomodulefield to itsmain, as it already did formodule.#35447#36597
* A bundledimport * as nsnamespace now enumerates its exports in sorted order. The spec requires this, and unbundled code already did it. Update snapshots that pinned the old order.#35957
* bun build --minifyno longer generates a bare$identifier. That identifier shadowed jQuery's$when a bundle was loaded as a classic script.#35668
* ESM imports of builtin modules (node:fs,node:process,node:module), andexport * from "bun"or a non-literalimport()of"bun", no longer evaluate every lazy export at import time. Each export is evaluated when something first binds to it. For"bun", a property that throws when constructed (Bun.rediswith an invalidREDIS_URL) now throws at the binding that uses it. Before, it failed the whole module.#37525#37714#37726
* bun build --metafilenow sets a bundled import'spathto the imported file'sinputskey (src/b/shared.js). Before, it was the raw specifier or an absolute path, sometafile.inputs[path]never matched.#34534
* Bun.randomUUIDv7()now throwsRangeErrorfor a timestamp of2**48or more. Before, values up to2**53 - 1were truncated to 48 bits. It also throws for aNaNtimestamp, an invalidDate, or aDatebefore 1970. Before, these were encoded as0.#34021
* Bun.udpSocket({ connect: { port } })now throws for a port outside1to65535. Before, it connected to port0and dropped every datagram.#34029
* Bun.YAML.parse()now throwsSyntaxErroron a NUL byte. Before, it silently stopped there. If you pad a buffer with zeros, pad with newlines instead.
* Bun.color()output changed for"ansi-16"(a real 16-color escape such as\x1b[91m),"hsl"and"lab"(valid CSS such ashsl(0, 100%, 50%)), and near-black"ansi-256"colors. A 24-bit number such as0xff0000is now opaque. Before, it had alpha0.#33328#33046
* Bun.Cookienow serializesExpireslikeDate#toUTCString(). Before, the weekday was one day off, the day was unpadded, and the zone was-0000instead ofGMT. Update tests that assert the old string.#32926
* structuredClone(),self.postMessage()inside a worker, andnew Worker(path, { transferList })now throwTypeErrorfor a transfer entry that is not an object, such asnull. Before, they skipped it.#32809
* bun:ffiviewSource()andnew JSCallback()now throw on invalid arguments. Before,viewSource()returned the error, andJSCallbackreturned an instance whoseptrwasundefined.#34396
* Bun.FileSystemRouter.match()now returnsnullfor a non-empty path string that does not start with/. Before,"Xtop"matched/top. Full URLs are unaffected.#34028
* Bun.Terminal#write()now returns the full input length, because the whole input is buffered. Before, it returned only the bytes flushed synchronously, and re-sending the rest duplicated input.drainnow fires on POSIX.#34289
* new Bun.RedisClient(url)now throwsInvalid database number in Redis URL: "notadb"when the URL path is not a database index, such asredis://host/notadb. Before, it connected to database0.#34039
* Bun.spawn()andBun.spawnSync()now throwERR_INVALID_ARG_VALUEfor a NUL byte inargv0orcwd. Before,argv0was silently cut at the NUL.
* Bun.$now fails withambiguous redirectwhen a redirect target such as> *.txtexpands to more than one word. Before, the words were joined into one path.#34324
* Nineinput validation hardeningrounds tightened input validation and bounds checks across the runtime. Each PR lists the subsystems it touched.
* Bun.spawn()andBun.spawnSync()now throwERR_OUT_OF_RANGEfortimeout: NaNandERR_UNKNOWN_SIGNALforkillSignal: 0. Before,timeout: NaNmeant no timeout, andkillSignal: 0sent a no-op signal. The child kept running either way.#35348
* Bun.spawn()andBun.spawnSync()now throwAbortError(withcauseset tosignal.reason) for asignalthat is already aborted. No process is created. Before,Bun.spawn()started the child and then killed it, andBun.spawnSync()ran it to completion.
* bun:sqlitedb.close()now finalizes everydb.query()statement, not only the cached ones.db.prepare()statements keep working until finalized.db.close(true)finalizes those too. Before, it threwdatabase is locked. A statement thatclose()finalized throws when used.#36573#36793
* bun:sqliterow objects andstmt.columnNamesnow keep a column aliasedAS "". Before, it was dropped, and a trailing one made.all()return a number.columnNamesnow throws afterfinalize().#34925
* Two robustness passes changed several edge cases.Bun.spawn({ stdout: typedArray })throws instead of aborting.FileSystemRouterno longer matches a URL shorter than the route pattern. CSS serialization escapes identifiers consistently. Workers readprocess.envat runtime instead of at transpile time. The PR bodies list the rest.
* S3Client.list()entries now exposechecksumAlgorithm. The misspelledchecksumAlgorithmestill works but is non-enumerable. It no longer appears inObject.keys()orJSON.stringify()output.#36502
* More inputs that were silently accepted now throw:odd-length hex passed toBun.CryptoHasher#update()a primitiveoptionsargument toTextDecoder#decode()invalid arguments tocrypto.createDiffieHellman()(before, returned as an error object)NaNorundefinedseconds inRedisClient#expire()(before, sentEXPIRE key 0)fractional or beyond-32-bit ports forBun.udpSocket(), andcost,timeCost, ormemoryCostvalues forBun.password(before, wrapped or truncated into range)Bun.openInEditor()with no editor found (before, returned silently)anfs.write()offsetpast the end of the buffer whenlengthis omitted (before, wrote 0 bytes)#35188#35189#36508#36835#36999#37210#37632
* odd-length hex passed toBun.CryptoHasher#update()
* a primitiveoptionsargument toTextDecoder#decode()
* invalid arguments tocrypto.createDiffieHellman()(before, returned as an error object)
* NaNorundefinedseconds inRedisClient#expire()(before, sentEXPIRE key 0)
* fractional or beyond-32-bit ports forBun.udpSocket(), andcost,timeCost, ormemoryCostvalues forBun.password(before, wrapped or truncated into range)
* Bun.openInEditor()with no editor found (before, returned silently)
* anfs.write()offsetpast the end of the buffer whenlengthis omitted (before, wrote 0 bytes)
* new URL(bad)now throws Node'sTypeError: Invalid URLwithcodeandinputset. It rejects an invalid punycodexn--host for special schemes.#34660
* assert.deepStrictEqual()andutil.isDeepStrictEqual()now compare prototypes, as in Node.js.Bun.deepEquals()andexpect()are unchanged.#34660
* child_process.spawn()now ignoresoptions.encoding, as Node does.stdoutandstderralways emitBufferchunks. Callchild.stdout.setEncoding()to get strings.#36050
* N-API status codes on validation and failure paths now match Node 26. For example,napi_wrap()on a non-object returnsnapi_invalid_arg.napi_reference_ref()returns0once the referent has been collected.napi_get_buffer_info()rejects a bareArrayBuffer. Addons that branch on a specific status see Node's values.#36805#36850
* fs.open()now throwsERR_INVALID_ARG_VALUEwhen an object is passed asflags. Before,{}opened the file read-only.#34505
* fs.rm()andfs.rmSync()now rejectrecursive,force,retryDelay, ormaxRetriesexplicitly set toundefined, as Node does. Omit the key instead.#34505
* On Windows,process.binding("uv")and everynode:fserror now use libuv's error numbers (-4058forENOENT). Before, the binding and some fs calls such asfs.access()reported CRT values like-2. POSIX is unchanged.#34505
* fs.write(),fs.writev(), andfs.readv()now operate at the current file offset whenpositionis not a safe integer (NaN,Infinity, a BigInt), as Node does.fs.createWriteStream()no longer overwrites the start of the file after a short write.#36135
* fs.appendFile()andfs.appendFileSync()with{ flag: "w" }now truncate the file, as the flag says. Before, they appended.#36553
* fs.watch()withrecursive: trueon Linux and FreeBSD now emits'error'(for exampleENOSPC, with the subdirectory'spath) for a subdirectory it cannot watch. It keeps watching the rest. Before, the subdirectory was skipped silently.#36415
* session.remoteSettingsinnode:http2is now{}while the session is connecting or destroyed, as in Node. Before, it wasnull. Reading a setting right afterconnect()now returnsundefinedinstead of throwing.session.localSettingsis{}at that point too. Before the peer's ACK, it shows only the defaults plus yourcustomSettings.#34358
* node:http2stream.end(chunk)now setsEND_STREAMon theDATAframe carryingchunk, as Node does. Before, it sent an empty frame after it.#34432
* node:http2pushStream()now reports invalid headers only through its callback, as Node does. The pushed stream no longer also emits'error'.#36551
* node:testsuites markedskipno longer run their callback. Before, the body ran and its tests were registered.{ skip: true, todo: true }now counts as a skip, not a todo.#34444
* process.execve()now throws an error carryingcode,syscall,errno, andpathwhen the exec fails. This matches Node 26. Before, it printed an error and aborted.
* process.titlenow defaults toargv[0]as invoked. Before, it was"bun".#31831
* require(),(await import()).default, andprocess.getBuiltinModule()now return the same object for a natively implemented builtin such asnode:buffer.module.builtinModulesno longer listsbun:wrap.#31831
* process.reallyExit()no longer emits'exit'before exiting. This matches Node. If you rely on'exit'listeners running, callprocess.exit().#34997
* util.styleText()now follows the Node 26 API. It returns plain text when the target stream (process.stdoutby default) is not a TTY. Pass{ validateStream: false }to always get escape codes.util.inspect()now bracketsArrayBufferinternals ([byteLength]: 4).util.format("%s", date)prints the ISO form.vmmodule namespaces have anullprototype.#34434
* Warnings are now printed as(node:PID) [CODE] Name: message. Adding a'warning'listener no longer replaces the default printer (seeprocess). Silence it withprocess.removeAllListeners("warning")or--no-warnings.#31831#37344
* crypto.subtleis now a getter onCrypto.prototype. It throwsERR_INVALID_THISwhen read off anything but aCrypto.subtle.importKey("jwk", ...)with a non-JWK object now rejects withDataError. Before, it threwTypeError. An unknown key format is reported asERR_INVALID_ARG_VALUE.#34838
* fetch()now returns a rejected promise when reading its options throws. Before, it threw synchronously. A synchronoustry/catcharound an unawaited call no longer catches it.#33649
* Response.redirect(url)now parses and re-serializes an absoluteurlbefore writingLocation.http://example.combecomeshttp://example.com/. A relativeurlis written as-is. A relativeurlcontaining a code point above U+00FF now throwsTypeError.#33126
* fetch()now rejects the body read when a compressed response with neitherContent-LengthnorTransfer-Encodingis cut off early. Before, it resolved with partial data.#34922
* fetch()now errors the response body when itssignalaborts, even if the whole body has already arrived. Pending and later reads reject withAbortError(or the abort reason). Before, they resolved with the buffered bytes. This matches Node.js.
* fetch()now parsesConnection,Transfer-Encoding,Content-Encoding, andUpgradeas token lists. Anyclosetoken disables connection reuse.Transfer-Encoding: gzip, chunkedis framed as chunked instead of rejected.identitycodings are ignored. A connection that carried an HTTP/1.0 response is reused only if the response saidConnection: keep-alive.#36777#37530
* fetch()now sends Latin-1 request header values byte-for-byte, per the Fetch spec. Before, it UTF-8 encoded them.cafégoes out as63 61 66 e9.#35338
* fetch()withredirect: "error"now rejects only on301,302,303,307, and308, per the Fetch spec. Other3xxsuch as304now resolve. Before, they rejected withUnexpectedRedirect.#36539
* fetch()now treats its idle timeout (still 300 seconds by default) as one deadline for receiving the whole response header block. A server that trickles header bytes now times out. Before, each byte reset the timer.#36145
* Bun.serve({ port })now throws aRangeErrorfor non-integer, negative, or out-of-range port values. Before, it silently clamped:port: 65536started a server on port 65535, andport: -1bound a random port. Numeric strings andnull/undefinedstill work.#34957
* Bun.servenow treats a returnedResponsewith a status outside100to999, such asResponse.error(), like a thrown error. It goes toerror()and answers500by default. Before, it wrote an invalid status line.#33400
* Bun.serveper-method route objects ({ GET: handler }) now answerHEADwith theGEThandler when noHEADkey is set. Before, the request fell through to the next route or404.#32822
* Bun.serveWebSocket connections now close with code1006and reasonReceived an incorrectly masked framewhen a client sends an unmasked frame, per RFC 6455. Before, the frame was parsed as if it were masked.#32820
* Bun.servenow answers413and closes the connection when a single chunk of a chunked request carries more than 16 KiB of chunk extensions. This matchesnode:http.#34504
* Bun.serveHTML routeswithdevelopment: falseno longer emitsourceMappingURLordebugIdcomments..mapURLs answer404.[serve.static] sourcemap = "linked"inbunfig.tomlrestores them.#36982
* Bun.serve({ tls: [...] })now enforcesrequestCertandrejectUnauthorizedset on a per-serverNameentry. Before, they were ignored. Clients of that name without an acceptable certificate are refused. Withhttp3: true, they are enforced over QUIC too.#36174#37669
* Bun.servenow answers400to a request whoseTransfer-Encodingnames anything besides a single finalchunked(gzip, chunked,chunked, chunked). Before, such requests got200with the body still encoded.node:httpstill acceptsgzip, chunkedbut now rejectschunked, chunked.#35295
* server.upgrade()now returnsfalseunless the request hasUpgrade: websocketand a well-formedSec-WebSocket-Key. It answers426whenSec-WebSocket-Versionis not13. Before, anyGETwith a 24-byte key was upgraded.#35298
* ws.subscribe()andws.unsubscribe()now returnfalseon a closedServerWebSocket(and are typedboolean).#35236
* ws.send()andpublish()of an in-memoryBlobnow send its bytes as a binary frame. Before, they sent the text[object Blob]. ABun.file()blob throws; read it first.#36032
* Bun.servestatic and file routes now evaluateIf-MatchandIf-Unmodified-SinceonGETandHEAD. They answer412when the precondition fails. Before, both headers were ignored.#35169
* new WebSocket(url, { proxy })now throwsSyntaxErrorat construction for a proxy scheme other thanhttporhttps. Before, it failed later withConnection ended.#35147
* Bun.deepEquals()now distinguishes boxed BigInts and Symbols with different contents (Object(1n)vsObject(2n)). In strict mode (toStrictEqual(),assert.deepStrictEqual()), it also distinguishes a boxed string or typed array that carries extra own properties. Before, all of these compared equal.#34434
* Bun.sql'sconnectionTimeoutnow bounds the whole handshake. Before, it restarted on every packet. A Postgres server that sends a second authentication request now fails the connection withERR_POSTGRES_UNEXPECTED_MESSAGE.#36308
* Bun.sqlnow honorsPGSSLMODEfrom the environment. A URL?sslmode=still wins.PGSSLMODE=requireagainst a server without TLS now fails. Before, it connected in plaintext.?ssl=and?ssl-mode=are accepted as spellings.tls: { caFile }enables verification likeca.#36840#37669
* Bun.sqlnow decodes a Postgresdate,timestamp, ortimestamptzofinfinityor-infinityas the numberInfinityor-Infinity. Before, it was an invalidDate. Check for it before callingDatemethods on the value.#35121
* On Linux, Bun no longer setsprctl(PR_SET_THP_DISABLE)at startup. That flag was inherited acrossexecve. It disabled transparent huge pages in every child process spawned viaBun.spawn,bun run, or lifecycle scripts. Bun's own allocations now opt out per-mapping viaMADV_NOHUGEPAGE. Child processes inherit the system THP setting.#36990

## Changelog#

Everything below is the long tail: smaller features, compatibility fixes, and bug fixes, grouped by area. See thefull changelogfor the complete list.

### Runtime#

#### ServerWebSocket.subscriptionsv1.3.2

A newsubscriptionsgetter returns an array of every topic the socket is currently subscribed to.#24299

#### bun replv1.3.10v1.4.0

bun replis now native. It is built directly into the Bun binary instead of lazily downloading a separate npm package on first run. It ships a full TUI:

* syntax highlighting
* the standard terminal line-editing shortcuts (Ctrl-A, Ctrl-E, Ctrl-K)
* persistent history (~/.bun_repl_history)
* tab completion
* multi-line input with automatic continuation detection
* the standard.help/.load/.save/.editorcommands

It supports top-levelawaitand the_/_errorspecial variables. Bare object literals work too:{ a: 1 }no longer needs to be wrapped in parens.#26304

❯
bun repl
↻ replay
 
Welcome to Bun v1.4.0
 
Type ".help" for more information.
 
> { a: 1 }
 
{ a: 1 }
 
> await fetch("https://bun.sh").then(r => r.status)
 
200
 
> _
 
200

bun replnow supports-e <script>to evaluate and-p <script>to evaluate and print, with full REPL semantics. Shell completions forreplship for bash, fish, and zsh, and there's a newREPL docs page.#27436

bun repl -e 
'
console.log(1 + 1)
'
2
bun repl -p 
'
{ a: 1, b: 2 }
'
{ a: 1, b: 2 }
bun repl -p 
'
await fetch("https://bun.sh").then(r => r.status)
'
200

#### bun ./README.mdv1.3.12

Bun pretty-prints Markdown files directly to your terminal: headings, tables, task lists, blockquotes, syntax-highlighted code blocks, and clickable hyperlinks, with correct alignment for emoji and Chinese/Japanese/Korean characters. No JavaScript VM is started.#28833

bun ./README.md
❯
bun ./README.md
project

═══════

│ 
Render Markdown to the terminal with 
bun ./README.md
.

┌───────────────┬──────────────────────────┐
│ 
Command
 │ 
What it does
 │
├───────────────┼──────────────────────────┤
│ 
bun run build
 │
 parallel 
build:*
 scripts │

│ 
bun profile
 │
 write a 
.cpuprofile
 │

└───────────────┴──────────────────────────┘

┌─ 
ts

│ Bun
.serve
({
│ fetch: () => 
new
 
Response
(
"hello"
),
│ });
└─
 
☒ 
tables
 
☒ 
task lists
 ☐ you, running 
bun ./README.md
 (https://bun.com)

#### Bun.JSON5v1.3.7v1.4.0

Bun ships a native JSON5 parser.Bun.JSON5.parse()andBun.JSON5.stringify()are built in, and.json5files can be imported directly in both the runtime and the bundler with no npm package needed. It passes the official JSON5 test suite.#26439

import
 config 
from
 
"
./config.json5
"
;

const
 data 
=
 Bun.
JSON5
.
parse
(
`{

 // comments work

 unquoted: 'single quotes',

 trailing: [1, 2, 3,],

}`
);

#### Bun.JSONLv1.3.7

Bun.JSONLis a built-in newline-delimited JSON parser. It is implemented in C++ on top of JavaScriptCore's optimized JSON parser.Bun.JSONL.parse()parses a complete JSONL string orUint8Arrayinto an array.Bun.JSONL.parseChunk()parses as many complete values as possible from streaming input. It returns{ values, read, done, error }, so you can resume where you left off without losing partial results. It parses ASCII input without an extra copy, skips UTF-8 BOMs automatically, and guards against inputs larger than 4 GB.#26356

const
 results 
=
 Bun.
JSONL
.
parse
(
'
{"a":1}
\n
{"b":2}
\n
'
);

// [{ a: 1 }, { b: 2 }]

const
 chunk 
=
 Bun.
JSONL
.
parseChunk
(
'
{"id":1}
\n
{"id":2}
\n
{"id":3
'
);

chunk.values; 
// [{ id: 1 }, { id: 2 }]

chunk.read; 
// 17

chunk.done; 
// false

#### Bun.JSONC.parse()v1.3.6v1.4.0

Bun.JSONC.parse()parses JSON with//and/* */comments and trailing commas. It's the same parser Bun uses internally to readtsconfig.json, exposed as a runtime API alongsideBun.YAMLandBun.TOML.#22115

const
 config 
=
 Bun.
JSONC
.
parse
(
`{

 // This is a comment

 "name": "my-app",

 "dependencies": {

 "react": "^18.0.0", // trailing comma allowed

 },

}`
);

#### Bun.XMLv1.4.0

Bun.XMLis a native XML parser.Bun.XML.parse()andBun.XML.stringify()are built in, and.xmlfiles can be imported directly in both the runtime and the bundler, alongsideBun.TOML,Bun.YAML, andBun.JSON5. Parsing is ~5× faster thanfast-xml-parserandxml2json ~200 KB feeds.#37048

import
 feed 
from
 
"
./atom.xml
"
;

Bun.
XML
.
parse
(
`<order id="A1"><item>Tea</item><item>Mug</item><paid/></order>`
);

// { order: { "@id": "A1", item: ["Tea", "Mug"], paid: "" } }

Bun.
XML
.
parse
(
`<p>Hi <b>you</b></p>`
, { compact
:
 
false
 });

// { name: "p", attributes: {}, children: ["Hi ", { name: "b", ... }] }

#### Bun.TOMLv1.4.0

Bun.TOMLwas rewritten for fullTOML v1.1.0conformance and now passes 708/708 cases in the officialtoml-testsuite.

const
 cfg 
=
 Bun.
TOML
.
parse
(
`

released = 2026-08-10T12:00:00Z

[package]

name = "app"

`
);

cfg.released; 
// "2026-08-10T12:00:00Z"

Bun.
TOML
.
stringify
({ name
:
 
"
app
"
, deps
:
 { bun
:
 
"
1.4.0
"
 } });

// name = "app"

//

// [deps]

// bun = "1.4.0"

#### Bun.Archivev1.3.6

Bun.Archiveis a new built-in for creating and extracting tarballs withoutnode-taror any other dependency.

const
 archive 
=
 Bun.Archive.
from
({

 
"
hello.txt
"
:
 
"
Hello, World!
"
,

 
"
data.json
"
:
 
JSON
.
stringify
({ foo
:
 
"
bar
"
 }),

});

await
 Bun.Archive.
write
(
"
archive.tar.gz
"
, archive, 
"
gzip
"
);

// Extract to a directory

await
 archive.
extract
(
"
./out
"
);

#### CompressionStreamandDecompressionStreamv1.3.3v1.4.0

Bun 1.3.3 added the Web-standardCompressionStreamandDecompressionStreamAPIs, supporting the spec formatsgzip,deflate, anddeflate-rawplusbrotliandzstdas Bun-specific extensions.

const
 stream 
=
 
new
 
Blob
([data])

 .
stream
()

 .
pipeThrough
(
new
 
CompressionStream
(
"
gzip
"
));

const
 compressed 
=
 
await
 
new
 
Response
(stream).
arrayBuffer
();

#### URLPatternv1.3.4

Bun now implements theURLPatternWeb API for declarative URL matching.

const
 pattern 
=
 
new
 
URLPattern
({ pathname
:
 
"
/users/:id
"
 });

pattern.
test
(
"
https://example.com/users/123
"
); 
// true

const
 result 
=
 pattern.
exec
(
"
https://example.com/users/123
"
);

console.
log
(result.pathname.groups.id); 
// "123"

#### ML-DSA and ML-KEM incrypto.subtlev1.4.0

crypto.subtlesupports the NIST post-quantum algorithms:

* ML-DSA (FIPS 204 signatures) at parameter sets 44/65/87, forsign/verify.
* ML-KEM (FIPS 203 key encapsulation) at 768/1024, via four newSubtleCryptomethods:encapsulateBits,encapsulateKey,decapsulateBits, anddecapsulateKey.

Keys import and export asspki,pkcs8,jwk,raw-public, andraw-seed. They survivestructuredClone.#34838

const
 { publicKey, privateKey } 
=
 
await
 crypto.subtle.
generateKey
(

 
"
ML-KEM-768
"
,

 
true
,

 [
"
encapsulateBits
"
, 
"
decapsulateBits
"
],

);

// Sender: derive a shared secret + ciphertext from the recipient's public key

const
 { sharedKey, ciphertext } 
=
 
await
 crypto.subtle.
encapsulateBits
(

 { name
:
 
"
ML-KEM-768
"
 },

 publicKey,

);

// Recipient: recover the same shared secret from the ciphertext

const
 secret 
=
 
await
 crypto.subtle.
decapsulateBits
(

 { name
:
 
"
ML-KEM-768
"
 },

 privateKey,

 ciphertext,

);

#### ML-DSA and ML-KEM innode:cryptov1.4.0

node:cryptonow supports the NIST post-quantum algorithms ML-DSA (FIPS 204 signatures) and ML-KEM (FIPS 203 key encapsulation).

* generateKeyPairacceptsml-dsa-44/-65/-87andml-kem-768/-1024.
* sign()andverify()work with ML-DSA keys.
* createPublicKey/createPrivateKeyimport PEM, DER, encrypted PKCS#8, and JWK (kty: "AKP").

Seven of Node v26.3.0's upstreamtest-crypto-pqc-*suites now pass byte-for-byte. ML-KEM-512 and SLH-DSA are not yet available, because BoringSSL does not expose them viaEVP_PKEY.crypto.encapsulate()/decapsulate()land in a later release.#34549

import
 { generateKeyPairSync, sign, verify } 
from
 
"
node:crypto
"
;

const
 { publicKey, privateKey } 
=
 
generateKeyPairSync
(
"
ml-dsa-65
"
);

const
 sig 
=
 
sign
(
undefined
, Buffer.
from
(
"
hello
"
), privateKey);

verify
(
undefined
, Buffer.
from
(
"
hello
"
), publicKey, sig); 
// true

publicKey.
export
({ format
:
 
"
jwk
"
 });

// { kty: "AKP", alg: "ML-DSA-65", pub: "..." }

#### Response.textStream()andRequest.textStream()v1.4.0

RequestandResponsenow implementtextStream(), returning aReadableStream<string>of the body decoded as UTF-8.

const
 res 
=
 
await
 
fetch
(
"
https://api.example.com/stream
"
);

for
 
await
 (
const
 chunk 
of
 res.
textStream
()) {

 process.stdout.
write
(chunk); 
// chunk is a string

}

Multi-byte characters split across chunk boundaries are reassembled, a leading BOM is stripped, and invalid sequences become U+FFFD. Bun decodes each body backing directly rather than piping bytes through aTextDecoderStream, so in-memory bodies emit a single string chunk andfetch()responses decode inline as bytes arrive.

#### process.on("memoryPressure")v1.4.0

A new"memoryPressure"event onprocessfires when the OS signals low available memory, so applications can drop caches or reap idle subprocesses instead of polling. On macOS, Linux, and Windows, Bun subscribes to the operating system's built-in low-memory notification. The listener does not keep the event loop alive.#32594

process.
on
(
"
memoryPressure
"
, (
level
:
 
"
warning
"
 
|
 
"
critical
"
) 
=>
 {

 cache.
clear
();

});
`process` emits a 'memoryPressure' event when the system runs low on memory (thanks @codebytere!)

#### Bun.sliceAnsi()v1.3.11v1.4.0

Bun.sliceAnsi()slices a string by terminal column width while preserving ANSI colors and terminal hyperlinks, without splitting emoji or other multi-codepoint characters. It replaces theslice-ansiandcli-truncatenpm packages, is faster than both, and returns the original string when nothing is cut.#26963

// slice-ansi replacement

Bun.
sliceAnsi
(
"
\x1b
[31mhello
\x1b
[39m
"
, 
1
, 
4
); 
// "\x1b[31mell\x1b[39m"

// cli-truncate replacement

Bun.
sliceAnsi
(
"
unicorn
"
, 
0
, 
4
, 
"
…
"
); 
// "uni…"

Bun.
sliceAnsi
(
"
unicorn
"
, 
-
4
, 
undefined
, 
"
…
"
); 
// "…orn"

#### Bun.wrapAnsi()v1.3.7v1.4.0

Bun.wrapAnsi()is a native, drop-in replacement for thewrap-ansinpm package. It word-wraps text to a column width with the same ANSI/hyperlink/Unicode handling as above, and is up to 88x faster than the JavaScript version.#26061

const
 wrapped 
=
 Bun.
wrapAnsi
(
"
\x1b
[31mThe quick brown fox
\x1b
[39m
"
, 
10
);

console.
log
(wrapped);

// \x1b[31mThe quick\x1b[39m

// \x1b[31mbrown fox\x1b[39m

#### Bun.stringWidth()v1.3.5v1.4.0

Bun.stringWidth()returns the number of terminal columns a string occupies, accounting for ANSI escape sequences, zero-width Unicode, and multi-codepoint emoji graphemes.

Bun.
stringWidth
(
"
hello
"
); 
// 5

Bun.
stringWidth
(
"
\x1b
[31mhello
\x1b
[0m
"
); 
// 5 (ANSI color)

Bun.
stringWidth
(
"
\x1b
[5A
"
); 
// 0 (cursor movement)

Bun.
stringWidth
(
"
👨‍👩‍👧
"
); 
// 2 (ZWJ sequence, one grapheme)

Bun.
stringWidth
(
"
🇺🇸
"
); 
// 2 (regional indicator pair)

Bun.
stringWidth
(
"
\x1b
]8;;https://bun.sh
\x07
Bun
\x1b
]8;;
\x07
"
); 
// 3 (terminal hyperlink)

It strips every kind of ANSI escape code (color, cursor movement, terminal hyperlinks). It also strips zero-width codepoints such as soft hyphen and combining marks. Emoji measure 2 columns each. That includes flag pairs, skin-tone modifiers, keycaps, and multi-part emoji like 👨‍👩‍👧.util.inspect,console.table, andreadlineuse the same implementation.#25447

Bun.stringWidth · terminal columns
example 1 of 5 · ascii
▶ play
↻ replay
◼ playing…
▶ next · ANSI color
▶ next · ZWJ family
▶ next · flag
▶ next · OSC 8 hyperlink
▶ play
Bun.stringWidth(
"hello"
)
// 
5
1
2
3
4
5
6
h
e
l
l
o
h
e
l
l
o
codepoints
codepoints:
5
·
bytes:
5
·
columns:
5
the easy case — one byte, one codepoint, one column each
Bun.stringWidth(
"\x1b[31mhello\x1b[0m"
)
// 
5
1
2
3
4
5
6
h
e
l
l
o
␛[31m
h
e
l
l
o
␛[0m
codepoints
codepoints:
14
·
bytes:
14
·
columns:
5
ANSI escapes are invisible in a terminal — stringWidth strips them
Bun.stringWidth(
"👨‍👩‍👧"
)
// 
2
1
2
3
4
5
6
👨‍👩‍👧
👨
ZWJ
👩
ZWJ
👧
codepoints
codepoints:
5
·
bytes:
18
·
columns:
2
zero-width joiners fuse three emoji into one grapheme — terminals give it 2 columns
Bun.stringWidth(
"🇺🇸"
)
// 
2
1
2
3
4
5
6
🇺🇸
🇺
🇸
codepoints
codepoints:
2
·
bytes:
8
·
columns:
2
regional indicators U + S pair into one flag — still 2 columns
Bun.stringWidth(
"\x1b]8;;https://bun.sh\x07Bun\x1b]8;;\x07"
)
// 
3
1
2
3
4
5
6
B
u
n
␛]8;…␇
B
u
n
␛]8;;␇
codepoints
codepoints:
29
·
bytes:
29
·
columns:
3
OSC 8 wraps a hyperlink around the text — only the anchor 'Bun' has width
One string, four sizes.
 
stringWidth
 
returns the last one — what a terminal actually draws. Same engine backs
 
Bun.sliceAnsi
,
 
Bun.wrapAnsi
,
 
console.table
, and
 
readline
.
 
#25447

Bun.stringWidth()is 7–56× faster on Chinese, Japanese, and Korean text.

Bun.stringWidth() 处理中文、日文、韩文字符的速度提升了 7~56 倍 Bun.stringWidth() が中国語・日本語・韓国語の文字で 7〜56 倍高速化されました Bun.stringWidth()가 중국어·일본어·한국어 문자에서 7~56배 빨라졌습니다

#### Bun.spawn({ cgroup })v1.4.0

On Linux,Bun.spawn()andBun.spawnSync()accept acgroupoption. It takes the path of an existing cgroup directory, or an open file descriptor for one. The child is placed in the cgroup before it starts running. So limits such asmemory.maxandpids.maxapply from its first instruction, and anything it forks stays inside. If the child exceeds its memory limit, the kernel kills it. The parent is unaffected. Bun only joins the cgroup. Create and configure it first (node:fsis enough), and remove it when you are done.

import
 { mkdirSync, writeFileSync } 
from
 
"
node:fs
"
;

const
 dir 
=
 
"
/sys/fs/cgroup/build-jobs
"
;

mkdirSync
(dir, { recursive
:
 
true
 });

writeFileSync
(
`
${
dir
}
/memory.max`
, 
String
(
2
 
*
 
1024
 
**
 
3
));

const
 proc 
=
 Bun.
spawn
({ cmd
:
 [
"
make
"
, 
"
-j8
"
], cgroup
:
 dir });

On cgroup v2 the child is created inside the cgroup withclone3(CLONE_INTO_CGROUP). Where that is unavailable, Bun writes the child intocgroup.procsbeforeexec. A missing directory fails the spawn with the errno and the path. A frozen cgroup is refused withEBUSY. Otherwise the child would freeze beforeexecand take the calling thread with it.node:child_processforwards the option. Other platforms ignore it.#37466

#### Async stack traces from native I/Ov1.3.12

Errors thrown from async native APIs likefs.promises,Bun.file(),Bun.S3Client, DNS, crypto, andfetchnow include async stack traces that point back to theawaitin your code. Previously these errors had empty stacks. There was no JavaScript on the call stack when the error was created in native code, so they were effectively impossible to trace.#28652

ENOENT: no such file or directory, open 
'
foo.txt
'

 at async 
foo
 (
/
path
/
to
/
app.js:
5
:
8
)

The stack is only captured when an error is constructed for rejection, so successful awaits are unaffected.

#### --cpu-profv1.3.2

Bun now ships a built-in CPU profiler. Pass--cpu-profto generate a.cpuprofilein the Chrome CPU Profiler format. It opens directly in Chrome DevTools or VS Code.--cpu-prof-mdwrites the same profile as a Markdown report: a summary table, top-10 hot functions, self-time and total-time tables, and a call tree. That is useful for pasting into a bug report or feeding to an LLM.--cpu-prof-name,--cpu-prof-dir, and--cpu-prof-intervalcustomize the output path and sampling interval.#24112#26327#26620

bun --cpu-prof ./app.ts
# Writes CPU.20260615.120000.12345.0.001.cpuprofile
bun --cpu-prof-md ./app.ts
A `bun --cpu-prof` profile opened in Chrome DevTools.

The CPU profiler can be enabled withBUN_CPU_PROFILE=1(plus optionalBUN_CPU_PROFILE_DIR/BUN_CPU_PROFILE_NAME) for processes you can't easily pass--cpu-profto.#26313

#### --heap-profv1.3.7

--heap-profgenerates a V8-compatible.heapsnapshotthat opens directly in Chrome DevTools, and--heap-prof-mdemits a grep-friendly Markdown report with total heap size, top types by retained size, and the largest individual objects.--heap-prof-nameand--heap-prof-dircontrol where the output lands.

# V8-compatible heap snapshot (opens in Chrome DevTools)
bun --heap-prof script.js
# Markdown heap profile for CLI analysis
bun --heap-prof-md script.js

#### --no-env-filev1.3.3

A new--no-env-fileflag (andenv = falseinbunfig.toml) disables Bun's automatic.envloading. This is useful in production and CI. There, environment variables are managed externally and stray.envfiles should be ignored. Explicit--env-filearguments are still honored.#24767

bun --no-env-file server.ts
# bunfig.toml

env
 
=
 
false

#### --no-orphansv1.3.14v1.4.0

A new--no-orphansflag (and[run] noOrphans = truein bunfig, orBUN_FEATURE_FLAG_NO_ORPHANS=1) makes Bun exit when its original parent process dies. It also recursively SIGKILLs all descendants on clean exit. So when your terminal dies, your dev servers die with it. It works on Linux and macOS with no extra thread or file descriptor. On Windows it uses a recursive kill-on-close Job Object plus a parent-process wait (#34768). It applies tobun run <script>,bunx, and--filter.#29930

bun --no-orphans run dev
`bun --no-orphans <file|script>` recursively terminates lingering processes on exit

#### Bun.TranspilerREPL modev1.3.7

A newreplModeoption transforms code for interactive REPL evaluation: it captures the last expression's value, hoists declarations so they persist across lines, convertsconsttoletfor re-declaration, and auto-detects bare object literals. Pair it withvm.runInContextto build a Node.js-compatible REPL on Bun's transpiler.#26246

#### Bun.YAMLpasses 402/402 of yaml-test-suitev1.4.0

Bun.YAMLnow passes 402/402 yaml-test-suite. This fixes spec-compliance bugs in:

* explicit?keys
* tab indentation
* {}-style mappings
* &anchors on empty values
* ---/...appearing mid-line
* the indent and newline-trim modifiers on|/>strings

YAML.stringify()also now correctly quotes number-like strings ("0e6836","0123"), strings ending in:, and strings starting with[/{. Cyclic anchors and aliases are supported inparse().#31527#37055

`Bun.YAML.parse` supports cyclic anchors & aliases

#### WebSocketproxies and Unix socketsv1.3.6v1.4.0

TheWebSocketclient now supports connecting through HTTP and HTTPS proxies via a newproxyoption. It supportsws://andwss://over both HTTP and HTTPS proxies, Basic auth via URL credentials, custom proxy headers, and full TLS configuration for the target connection. It also supports Unix domain sockets viaws+unix://andwss+unix://URL schemes. These use the same syntax as the npm ws package.#25614#29203

new
 
WebSocket
(
"
wss://example.com
"
, { proxy
:
 
"
http://user:pass@proxy:8080
"
 });

new
 
WebSocket
(
"
ws+unix:///tmp/app.sock:/api/stream?x=1
"
);

#### WebSocketURL credentialsv1.3.7v1.4.0

new WebSocket("ws://user:pass@host")now forwards URL-embedded credentials as a BasicAuthorizationheader. An explicitly providedAuthorizationheader still takes precedence.#26278

#### SHA-3 and X25519 in Web Cryptov1.3.13

SHA-3 lands in both Web Crypto andnode:crypto.crypto.subtle.digest()and HMACsign/verifynow acceptSHA3-256/SHA3-384/SHA3-512.createHash/createHmacaddsha3-224/256/384/512.crypto.subtle.deriveBitsnow supports X25519 as well, for deriving a shared secret between two key pairs. Small-order peer public keys are rejected, as RFC 7748 requires.#29323#29152

await
 crypto.subtle.
digest
(
"
SHA3-256
"
, 
new
 
TextEncoder
().
encode
(
"
hello
"
));

const
 bits 
=
 
await
 crypto.subtle.
deriveBits
(

 { name
:
 
"
X25519
"
, public
:
 bobPublicKey },

 alicePrivateKey,

 
256
,

);

#### structuredClonepreserves object identityv1.4.0

structuredClonepreserves object identity forDate,RegExp,Errorsubclasses,DOMException,CryptoKey,KeyObject,X509Certificate,Blob, andFile: the same instance referenced twice comes back as one object.#32796

#### Bun.CSRFsessionIdv1.4.0

Bun.CSRF.generate()andBun.CSRF.verify()accept a newsessionIdoption that binds a token to a specific principal via HMAC associated data. Tokens generated for one session won't verify under another, and verification fails closed ifsessionIdis supplied on only one side; tokens withoutsessionIdare unchanged.#31215

#### Bun.udpSocket()connection-refused errors and truncation flagsv1.3.12

On Linux, sending to a dead port now fires theerrorhandler withECONNREFUSEDinstead of silently timing out. Thedatacallback also gains a fifthflagsargument with{ truncated: boolean }to detect when a datagram exceeded the receive buffer.#28827

#### Grapheme clusters for Indic scriptsv1.3.7

We rewrote grapheme cluster segmentation with Indic Conjunct Break support. Devanagari and other Indic conjuncts now segment as single clusters.#26376

#### Bun.S3Clientv1.3.1v1.4.0

Bun.S3Clientnow supports AWS Requester Pays buckets. PassrequestPayer: trueon the client or per-operation to send thex-amz-request-payerheader on every request, including each part of a multipart upload.#25514

const
 s3 
=
 
new
 Bun.
S3Client
({

 bucket
:
 
"
hl-mainnet-evm-blocks
"
,

 requestPayer
:
 
true
,

});

const
 data 
=
 
await
 s3.
file
(
"
0/0/1.rmp.lz4
"
).
arrayBuffer
();

Other S3 fixes:

* write()andwriter()now acceptcontentDispositionandcontentEncoding.
* presign()honorscontentDispositionandtype.
* slice(0, N).stream()sends the correctRangeheader.
* queueSizeis respected instead of being silently overridden to 255.
* A memory leak inlist()has been fixed.

#25363#26149#25999#27273#29813#23880

#### Bun.sqlis more reliablev1.3.11v1.4.0

const
 sql 
=
 
new
 Bun.
SQL
({ prepare
:
 
false
 });

await
 
sql
`SELECT 1`
; 
// now safe behind PgBouncer transaction pooling
* PgBouncer transaction pooling: withprepare: false, Bun now sends each query in a single round-trip instead of two, so PgBouncer can no longer split it across Postgres connections and return the wrong query's results.#27952
* Docker startup windows: when a pooled connection is accepted then closed before the handshake completes (as happens with Docker while a containerized database is still starting), Bun now retries with exponential backoff untilconnectionTimeoutelapses instead of failing every waiting query.#32028

#### Named parameters inBun.sqlfor SQLitev1.4.0

sql.unsafe()andsql.file()accept an object of named parameters for:name,$name, and@nameplaceholders. Previously an object bound nothing, so aSELECTreturned no rows and no error. Keys keep their prefix ({ ":id": 1 }) unless the connection setsstrict: true.#37109

#### SQLite 3.53.0v1.3.14

bun:sqlite's bundled SQLite is upgraded to3.53.0;db.close(true)no longer throws "database is locked" afterdb.transaction(); non-UTF-8TEXTvalues under 64 bytes decode leniently to U+FFFD instead of returning"".#27912

#### Bun.isStandaloneExecutablev1.4.0

Bun.isStandaloneExecutableis a new read-only boolean,trueinside abun build --compilebinary; unlike checkingBun.embeddedFiles.length > 0, reading it allocates nothing.#32583

#### bun init --react=tanstackv1.3.4

bun init --react=tanstackis a new template that scaffolds a TanStack Start project with file-based routing, Vite, and Tailwind, running on Bun.#24648

### fetch()#

#### fetch()response backpressurev1.4.0

fetch()now applies backpressure when streaming a response body. Once a chunk is delivered to JavaScript and nothing has consumed it, the HTTP thread pauses reading from the socket instead of buffering the entire body in memory. Buffered consumers like.text(),.json(), and.arrayBuffer()opt out and still receive the body in one shot.#29831

const
 res 
=
 
await
 
fetch
(
"
https://example.com/large.bin
"
);

for
 
await
 (
const
 chunk 
of
 res.body) {

 
// The HTTP thread pauses reading while this loop is busy,

 
// instead of buffering the whole file in memory.

 
await
 
process
(chunk);

}

#### HTTPS proxies reuseCONNECTtunnelsv1.3.12v1.4.0

fetch()through an HTTPS proxy nowreuses CONNECT tunnels. The tunneled TLS session is pooled across sequential requests to the same target. Before, every request paid a fresh CONNECT + TLS handshake. The tunnel is also reused when the request passestlsoptions such asca,cert, orkey. Previously every such request opened a new connection to the proxy and redid theCONNECTand both TLS handshakes.#37715

#### Custom TLS options reuse keep-alive connectionsv1.3.10

fetch()with custom TLS options nowreuses keepalive connections. Identical SSL configs (client certificates, custom CA, mTLS) are interned with reference counting for O(1) pointer-equality matching, with an LRU-bounded context cache.

#### Header name casing is preserved on the wirev1.3.7

fetch()preserves header name casing on the wire instead of lowercasing it. Headers are case-insensitive per RFC 7230, but plenty of real-world servers rejectcontent-typewhile acceptingContent-Type.#26425

#### HTTP_PROXYis re-read at runtimev1.3.12

process.env.HTTP_PROXY/HTTPS_PROXY/NO_PROXYset at runtime now take effect on the nextfetch()call instead of only being read once at startup.#28614

### Test runner#

#### onTestFinished()v1.3.2

bun:testexportsonTestFinished(), a Vitest-compatible hook that registers a callback to run after the current test completes, after allafterEachhooks. It can only be called inside a test body, so you can clean up resources that were created during the test.#24038

import
 { test, onTestFinished } 
from
 
"
bun:test
"
;

test
(
"
uses a temp resource
"
, () 
=>
 {

 
const
 handle 
=
 
open
();

 
onTestFinished
(() 
=>
 handle.
close
());

 
// ...

});

#### bun test --only-failuresv1.3.1

bun test --only-failuressuppresses output for passing and skipped tests, printing only failures and the final summary.#23312

bun 
test
 --only-failures
test/example.test.ts:

(fail) failing test

error: expect(received).toBe(expected)

Expected: 3

Received: 2

5 pass

1 skip

1 fail

Ran 7 tests across 1 file.

#### bun test --path-ignore-patternsv1.3.11

bun test --path-ignore-patterns(andtest.pathIgnorePatternsin bunfig.toml) excludes test files by glob, so you can skip integration tests, generated fixtures, or whole directories without renaming files.#28089

#### bun test --pass-with-no-testsv1.3.1

bun test --pass-with-no-testsexits with code 0 when no tests match, matching Jest and Vitest. Useful in monorepos where a shared pattern runs across packages that may not all contain tests.#23424

#### bun test --grepv1.3.6

bun testnow accepts--grepas an alias for-t/--test-name-pattern, matching Mocha and Jest.#25788

#### using spy = spyOn(...)v1.3.9

spyOn()andmock()now implementSymbol.dispose, sousing spy = spyOn(obj, "method")automatically restores the original implementation when the spy goes out of scope. No manualmockRestore()orafterEachcleanup needed.#26692

#### Theviglobalv1.3.1v1.4.0

Theviglobal (Vitest compatibility alias) is now defined inbun test, so files that callvi.fn()orvi.mock()without importing run unmodified.#23674

#### Timeouts onbeforeAll/afterAllhooksv1.3.2v1.4.0

beforeAll,beforeEach,afterAll, andafterEachnow accept a numeric timeout or{ timeout }options object as the second argument instead of throwing.#24039

### Bundler#

#### Execute-only standalone binaries on Linuxv1.3.12

Standalone executables on Linux now embed the module graph in a segment the OS loads into memory with the rest of the binary. Before, they opened and read their own executable file at startup.bun build --compilebinaries start withzero file I/Oand run with execute-only permissions (chmod 111). This matches the existing behavior on macOS and Windows.#26923

bun build --compile ./app.ts --outfile=app
chmod 111 ./app
./app 
# works, no read permission needed

#### useDefineForClassFieldsand"jsx": "react-jsx"intsconfig.jsonv1.4.0

useDefineForClassFields: falseis honored. Instance field initializers move into the constructor after parameter-property assignments, as tsc does. And"jsx": "react-jsx"selects the production automatic runtime (jsx/jsxsfrom<pkg>/jsx-runtime)."react-jsxdev"selectsjsxDEV.#36664#34422

#### Nativeusingandawait usingfor--target=bunv1.3.14v1.4.0

usingandawait usingdeclarations are no longer lowered to helper functions when targeting Bun. JavaScriptCore supports explicit resource management natively, so the runtime transpiler,bun build --target=bun, and the REPL now emit them as-is. Browser and Node targets continue to lower as before.#29538

var
 
__using
 
=
 (
stack
, 
value
, 
async
) 
=>
 { 
/* ... */
 };

var
 
__callDispose
 
=
 (
stack
, 
error
, 
hasError
) 
=>
 { 
/* ... */
 };

let
 __stack 
=
 [];

try
 {

 
const
 x 
=
 
__using
(__stack, { [
Symbol
.dispose]() {} }, 
0
);

 console.
log
(
"
hi
"
);

} 
catch
 (_) { 
var
 _err 
=
 _, _hasErr 
=
 
1
; }

finally
 { 
__callDispose
(__stack, _err, _hasErr); }

using x 
=
 { [
Symbol
.dispose]() {} };

console.
log
(
"
hi
"
);

#### emitDecoratorMetadataimplies legacy decoratorsv1.3.11

SettingemitDecoratorMetadata: trueintsconfig.jsonnow implies legacy decorator semantics even whenexperimentalDecoratorsis omitted, fixing NestJS, TypeORM, and Angular projects that crashed withdescriptor.value is undefined.

#### --compile-executable-pathv1.3.6

bun build --compilegains--compile-executable-pathto point at a local Bun binary instead of downloading one when cross-compiling, and using an already-compiled standalone executable as that base no longer panics or produces a corrupt Mach-O binary.

#### reactFastRefreshandallowUnresolvedinBun.build()v1.3.6

Bun.build()gainsreactFastRefresh: true(works on all targets). It also gainsallowUnresolved: string[], which controls which dynamic-import glob shapes are permitted at bundle time. Other fixes:

* definevalues starting with*,?,(, or)are now correctly auto-quoted.
* CallingBun.build()from inside a macro throws a clear deadlock error instead of hanging.
* Repeated in-process builds no longer panic after ~2000 iterations.

#### browserfield remaps for Node builtinsv1.4.0

--target=browsernow applies package.json"browser"remaps to Node builtins before falling back to Bun's polyfills. It also applies them tomain/index resolutions written without an extension.jszipbundles at 149 KB instead of 459 KB. The legacyjsnext:mainfield gets the samemodule→mainfallback.#36597#36620#35447

#### Code splitting on 20,000-module graphs is 14× fasterv1.4.0

The code-splitting reachability walk is now BFS and O(V+E), taking a 20,000-module diamond-shaped DAG from 4.65 s to 320 ms. Separately, the tree-shaking liveness, TLA validation, CSS-order, and part-visitor passes moved from recursion to explicit stacks, so linear import chains of thousands of modules no longer stack-overflow.

### Node.js compatibility#

#### node:httpv1.3.4v1.4.0

Thenode:httpclient has beenrewritten as a direct port of Node's_http_client.js. It replaces the previousfetch()-based shim.http.ClientRequestnow runs onnet/tlssockets, Node's own HTTP parser, and anAgentsocket pool. So keep-alive reuse,Upgrade/CONNECT, 1xx'information'events, andcreateConnectionall behave exactly as they do in Node.

import
 http 
from
 
"
node:http
"
;

const
 agent 
=
 
new
 http.
Agent
({ keepAlive
:
 
true
, maxSockets
:
 
4
 });

const
 req 
=
 http.
request
({ host
:
 
"
example.com
"
, agent }, (
res
) 
=>
 {

 res.
on
(
"
data
"
, (
chunk
) 
=>
 process.stdout.
write
(chunk));

});

req.
on
(
"
information
"
, (
info
) 
=>
 console.
log
(
"
1xx:
"
, info.statusCode));

req.
end
();

Keep-alive agents reuse sockets exactly as in Node: subsequent requests through anhttp.AgentwithkeepAlive: trueare65.9% faster, with190% higheroverall throughput.#24351

On the server,headersTimeout,requestTimeout, andkeepAliveTimeoutfire with Node'sconnectionsCheckingIntervalsweep and raw408reply. Also:

* HTTP/1.1 pipelining is supported withmaxRequestsPerSocket.
* closeIdleConnections()andcloseAllConnections()count correctly.
* Connection sockets are realnet.Socketinstances with Node's'connection'/'clientError'/'close'lifecycle.
* Per-serverinsecureHTTPParserandmaxHeaderSizeare honored.
import
 http 
from
 
"
node:http
"
;

const
 server 
=
 http.
createServer
((
req
, 
res
) 
=>
 res.
end
(
"
ok
"
));

server.headersTimeout 
=
 
10_000
; 
// 408 if headers not complete in 10s

server.requestTimeout 
=
 
30_000
; 
// 408 if request not complete in 30s

server.keepAliveTimeout 
=
 
5_000
; 
// close idle keep-alive sockets after 5s

server.
listen
(
3000
);

#### node:http2v1.4.0

node:http2has a spec-compliant HTTP/2 parser. Server push works end to end viapushStream()andcreatePushResponse(), and Node API parity now covers raw headers, graceful connection shutdown, andrespondWithFD.93.2%of Node v26.3.0's byte-identical test suite passes.#31584

import
 http2 
from
 
"
node:http2
"
;

const
 server 
=
 http2.
createSecureServer
({ key, cert });

server.
on
(
"
stream
"
, (
stream
, 
headers
) 
=>
 {

 stream.
pushStream
({ 
"
:path
"
:
 
"
/app.css
"
 }, (
err
, 
push
) 
=>
 {

 push.
respondWithFile
(
"
./public/app.css
"
, { 
"
content-type
"
:
 
"
text/css
"
 });

 });

 stream.
respond
({ 
"
:status
"
:
 
200
, 
"
content-type
"
:
 
"
text/html
"
 });

 stream.
end
(
"
<link rel=stylesheet href=/app.css>
"
);

});

#### node:netandnode:tlsv1.4.0

socket.end()now half-closes the connection instead of full-closing it.resetAndDestroy(), write-after-end errors, andECONNRESETshapes are now correct.net.Socket#connect()andBun.connect()acceptlocalAddressandlocalPort. These bind outgoing sockets to a specific local interface. TLS gains:

* 'session'and'keylog'events
* structured OpenSSL errors (err.code/err.library/err.reason)
* SNICallback/ALPNCallback
* PFX support

#31155

import
 tls 
from
 
"
node:tls
"
;

import
 { appendFileSync } 
from
 
"
node:fs
"
;

const
 socket 
=
 tls.
connect
(
443
, 
"
example.com
"
, { servername
:
 
"
example.com
"
 });

socket.
on
(
"
keylog
"
, (
line
) 
=>
 
appendFileSync
(
"
keys.log
"
, line)); 
// for Wireshark decryption

socket.
on
(
"
session
"
, (
session
) 
=>
 {

 
// Session ticket for TLS resumption

});

#### node:worker_threadsv1.4.0

A worker with an unsettled top-levelawaitexits with code 13.process.abort()inside a worker ends only that worker.node:worker_threadsgains:

* postMessageToThread()and the'workerMessage'event
* markAsUntransferable/markAsUncloneable
* env: SHARE_ENV
* captured stdio ({ stdout: true })
* worker introspection (getHeapStatistics(),cpuUsage(),startCpuProfile())

MessagePort'sclose()callback timing,'close'event delivery to both ends of a channel, andDataCloneErrortransfer-list messages now pass Node's own suite. That suite is at73.9%overall, up from ~37% in Bun 1.3.

import
 { Worker, SHARE_ENV } 
from
 
"
node:worker_threads
"
;

const
 w 
=
 
new
 
Worker
(
"
./worker.js
"
, {

 env
:
 SHARE_ENV, 
// live, write-through process.env

 stdout
:
 
true
, 
// captured stdio

});

w.stdout.
pipe
(process.stdout);

const
 stats 
=
 
await
 w.
getHeapStatistics
();

#### node:fsv1.4.0

fs.cpandcpSyncget Node's fullERR_FS_CP_*error semantics,fs.watchgains theignoreoption, andfs.promises.watchgainsAbortSignalsupport.node:fsnow passes97.5%of Node v26.3.0's fs tests (99.1%excluding tests that require--expose-internals).

import
 { watch } 
from
 
"
node:fs/promises
"
;

const
 ac 
=
 
new
 
AbortController
();

for
 
await
 (
const
 { eventType, filename } 
of
 
watch
(
"
./src
"
, {

 recursive
:
 
true
,

 
ignore
:
 (
path
) 
=>
 path.
includes
(
"
node_modules
"
),

 signal
:
 ac.signal,

})) {

 console.
log
(eventType, filename);

}

#### node:streamv1.4.0

The experimentalstream/iterandzlib/iterAPIs land behind--experimental-stream-iter,readable.read()returns one buffered chunk at a time (Node 26's semver-major change), andpipeline()reports the real failure ahead of any internalAbortError.node:streampasses96.9%of Node v26.3.0's stream tests.

// bun --experimental-stream-iter app.js

import
 { map, filter } 
from
 
"
node:stream/iter
"
;

import
 { createReadStream } 
from
 
"
node:fs
"
;

const
 lines 
=
 
createReadStream
(
"
access.log
"
, 
"
utf8
"
);

for
 
await
 (
const
 hit 
of
 
filter
(

 
map
(lines, (
l
) 
=>
 l.
trim
()),

 (
l
) 
=>
 l.
includes
(
"
POST
"
),

)) {

 console.
log
(hit);

}

#### processv1.4.0

Settingprocess.env.TZnow updates existingDateinstances.process.envnow behaves like Node's: assigned values are coerced to strings, andstructuredClone(process.env)works.--no-warnings,--trace-warnings,--trace-deprecation,--redirect-warnings, and--disable-warningare all wired up.processjumps from 60.5% to84.2%on Node v26.3.0's tests.#31831

const
 now 
=
 
new
 
Date
();

process.env.
TZ
 
=
 
"
America/Los_Angeles
"
;

console.
log
(now.
toString
()); 
// existing Date reflects the new timezone

process.env.
PORT
 
=
 
3000
;

console.
log
(process.env.
PORT
); 
// "3000" (coerced to string)

#### AsyncLocalStoragev1.4.0

AsyncLocalStoragegains the Node 26defaultValue/nameconstructor options andAsyncLocalStorage.prototype.withScope().AsyncResource.bind()now preserves the original function's.lengthandthis. Coverage of Node'sasync_hookstestsdoubles to50%.#31825

import
 { AsyncLocalStorage } 
from
 
"
node:async_hooks
"
;

const
 requestId 
=
 
new
 
AsyncLocalStorage
({

 name
:
 
"
requestId
"
,

 defaultValue
:
 
"
-
"
,

});

{

 using scope 
=
 requestId.
withScope
(crypto.
randomUUID
());

 console.
log
(requestId.
getStore
()); 
// the UUID

}

console.
log
(requestId.
getStore
()); 
// "-"

#### node:vmv1.4.0

Top-levelawaitin aSourceTextModuleresumes after theawait, andnode:vmadds the v26 module-linking API (linkRequests(),instantiate(),moduleRequests,hasTopLevelAwait()) and implementsmicrotaskMode: 'afterEvaluate', taking Node v26.3.0's vm suite from 72% to97%.#32018

import
 vm 
from
 
"
node:vm
"
;

const
 ctx 
=
 vm.
createContext
({ console }, { microtaskMode
:
 
"
afterEvaluate
"
 });

const
 mod 
=
 
new
 vm.
SourceTextModule
(

 
`export const n = await Promise.resolve(42);`
,

 { context
:
 ctx },

);

await
 mod.
linkRequests
(() 
=>
 {});

mod.
instantiate
();

await
 mod.
evaluate
();

console.
log
(mod.namespace.n); 
// 42

#### node:clusterv1.4.0

node:clustershares sockets between workers. Bun 1.4 implements round-robin scheduling (the primary accepts connections and hands the file descriptors to workers over IPC),SCHED_NONEshared handles, UDP clustering, andworker.send(msg, socket)handle passing.#31829

import
 cluster 
from
 
"
node:cluster
"
;

import
 http 
from
 
"
node:http
"
;

import
 { availableParallelism } 
from
 
"
node:os
"
;

if
 (cluster.isPrimary) {

 
for
 (
let
 i 
=
 
0
; i 
<
 
availableParallelism
(); i
++
) cluster.
fork
();

} 
else
 {

 http

 .
createServer
((
req
, 
res
) 
=>
 res.
end
(
`hello from 
${
process.pid
}
`
))

 .
listen
(
3000
);

}

#### vitest --coveragev1.4.0

node:inspectornow implements the V8Profilercoverage methods, sovitest --coveragewith the default v8 provider works under Bun. Per-file statement, branch, function, and line percentages, and the uncovered-line report, match Node exactly on the same project.#32476

bun --bun vitest run --coverage
 % Coverage report from v8

-----------|---------|----------|---------|---------|-------------------

File | % Stmts | % Branch | % Funcs | % Lines | Uncovered Line #s

-----------|---------|----------|---------|---------|-------------------

All files | 87.43 | 76.19 | 88.88 | 87.43 |

#### chrome://inspectv1.4.0

inspector.open(),inspector.url(),inspector.close(), andinspector.waitForDebugger()are implemented. Bun starts a WebSocket server that speaks the Chrome DevTools Protocol. It serves the same discovery endpoints as Node and prints Node'sDebugger listening on ws://...line. Sochrome://inspectand VS Code's debugger discover and attach to a running Bun process.#32479

import
 inspector 
from
 
"
node:inspector
"
;

inspector.
open
(
9229
, 
"
127.0.0.1
"
);

console.
log
(inspector.
url
()); 
// ws://127.0.0.1:9229/...

inspector.
waitForDebugger
(); 
// blocks until DevTools attaches

#### node:testv1.4.0

Subtests work.t.test(),t.describe(), and top-leveltest()/describe()called inside a running test now execute inline instead of throwingNotImplementedError.node:testalso gains:

* t.plan()andt.waitFor()
* getTestContext()
* mock.timersandmock.property()
* runtimet.skip()/t.todo()
* test tags
* custom assertions viaassert.register()
* (t, done) => {}callback tests

t.mockis now a per-test tracker. It resets automatically when the test finishes.20of Node v26.3.0'stest_runnertests now pass, up from 7.#32631

import
 { test } 
from
 
"
node:test
"
;

test
(
"
parent
"
, 
async
 (
t
) 
=>
 {

 t.
plan
(
2
);

 
await
 t.
test
(
"
a
"
, () 
=>
 {});

 
await
 t.
test
(
"
b
"
, () 
=>
 {});

});

test
(
"
timers
"
, (
t
) 
=>
 {

 t.mock.timers.
enable
({ apis
:
 [
"
setTimeout
"
, 
"
Date
"
] });

 
let
 fired 
=
 
false
;

 
setTimeout
(() 
=>
 (fired 
=
 
true
), 
1000
);

 t.mock.timers.
tick
(
1000
);

 t.assert.
strictEqual
(fired, 
true
);

});

node:testgains the programmaticrun()API. Each file runs in its own child process. The returnedTestsStreamemits Node's event sequence (test:enqueue/dequeue,test:pass/fail, per-file and run-leveltest:summary) as both events and objectMode chunks. Node v26'sexpectFailureoption lands. A throwing body is the expected outcome. A passing one fails withfailureType: 'expectedFailure'. Two divergences reachable from plainbun testare also fixed. A skippeddescribeno longer runs its callback.{ skip: true, todo: true }is treated as a skip. Node v26.3.0'stest_runnersuite goes from 20 to26 of 81passing.#34444

import
 { run } 
from
 
"
node:test
"
;

const
 stream 
=
 
run
({ files
:
 [
"
./a.test.js
"
, 
"
./b.test.js
"
] });

stream.
on
(
"
test:fail
"
, ({ 
name
, 
details
 }) 
=>

 console.
error
(name, details.error.message),

);

#### node:quicv1.4.0

node:quicis now implemented. It is backed by lsquic, which Bun already vendors for HTTP/3. The full experimental Node v26 API is covered:

* listen()andconnect()
* bidirectional and unidirectional streams
* HTTP/3 and raw-QUIC applications
* datagrams
* 0-RTT session resumption
* path migration
* stateless resets
* per-SNI certificates
* qlog and keylog

All235vendored Node v26.3.0node:quictests pass on a release build.#32602

Bun-to-Bun runs at1.31×Node-to-Node throughput (64,591 vs 49,239 req/s, one HTTP/3 stream per request at concurrency 50, Linux x64). Node's published binaries compile QUIC out, so running the same code there requires a from-source--experimental-quicbuild.

import
 { listen } 
from
 
"
node:quic
"
;

const
 endpoint 
=
 
await
 
listen
(

 (
session
) 
=>
 {

 session.
onstream
 
=
 (
stream
) 
=>
 stream.closed.
catch
(() 
=>
 {});

 },

 {

 sni
:
 { 
"
*
"
:
 { keys
:
 [key], certs
:
 [cert] } },

 
onheaders
() {

 
this
.
sendHeaders
({ 
"
:status
"
:
 
"
200
"
 });

 
this
.writer.
endSync
();

 },

 },

);

#### node:sqlitev1.3.2v1.4.0

node:sqliteis now implemented. It passes all 18 of Node v26.3.0'stest-sqlite-*files (319 subtests, 0 failures, 4 skips, on Linux x64). macOS skips more, because Apple's system libsqlite3 omits some features. It is backed by the same bundled SQLite asbun:sqlite. Supported:

* DatabaseSyncandStatementSync
* backup()
* sessions and changesets
* user-defined scalar, aggregate, and window functions
* the authorizer callback
* process.versions.sqlite

#32498

import
 { DatabaseSync } 
from
 
"
node:sqlite
"
;

const
 db 
=
 
new
 
DatabaseSync
(
"
:memory:
"
);

db.
exec
(
`CREATE TABLE data(key INTEGER PRIMARY KEY, value TEXT) STRICT`
);

const
 insert 
=
 db.
prepare
(
"
INSERT INTO data (key, value) VALUES (?, ?)
"
);

insert.
run
(
1
, 
"
hello
"
);

insert.
run
(
2
, 
"
world
"
);

console.
log
(db.
prepare
(
"
SELECT * FROM data ORDER BY key
"
).
all
());

// [ { key: 1, value: 'hello' }, { key: 2, value: 'world' } ]
node:sqlite is fully implemented and passes 100% of Node.js’ test suite
* vm.Script,vm.SourceTextModule, andvm.compileFunctionrelease their results to GC; a GC-root cycle between the script and its fetcher retained every call forever, so after 500 iterations and a GC, retainedScriptobjects drop from +500 to +0.#28493
* fs.createReadStream().pipe(serverResponse)completes whenServerResponseis used standalone without an underlying socket;writableNeedDraindefaulted totrue, pausing piped streams, which broke Vite's static file serving and other connect-to-web middleware adapters.#24137
* Module._resolveFilenameforwardsoptions.pathsto overridden resolvers and honors custom paths when called directly, whichbun --bun next buildon Next.js 16 + React Compiler + Turbopack depends on.#24325

#### node:replv1.4.0

node:replis now a working port of Node v26.3.0's REPL. Before, it was a stub that threw on use. It passes75.2%of Node's repl tests. This includes line editing and keybindings, multi-line continuation (unfinished statements get a|prompt instead of a syntax error), top-levelawait, tab completion, and persistent history. A new--interactiveflag drops you straight into it. For interactive use, preferbun repl, which has Bun-specific features like syntax highlighting.--interactiveandnode:replare for tools that programmatically embed Node's REPL.#31827

bun --interactive
const res = await fetch(
"
https://bun.sh
"
)
res.status
200

#### node:trace_eventsv1.4.0

node:trace_eventsis now fully implemented. It passes100%of Node v26.3.0's trace tests. Bun supports--trace-events-enabled,--trace-event-categories, and--trace-event-file-pattern. It writesnode_trace.${rotation}.login Chrome trace format. It instruments timers, fs, and http with category-gated events that are zero-cost when tracing is off.#31824

bun --trace-events-enabled --trace-event-categories=node.fs.async,node.http app.js
ls node_trace.
*
.log
node_trace.1.log

#### node:domain

node:domainis now a real implementation instead of a ~70-line stub. It passes66.7%of Node's domain tests. Domains propagate via Bun'sAsyncLocalStoragemachinery. Uncaught exceptions route into the active domain before'uncaughtException'.EventEmitterintegrates with domains the same way it does in Node.#31828

import
 domain 
from
 
"
node:domain
"
;

const
 d 
=
 domain.
create
();

d.
on
(
"
error
"
, (
err
) 
=>
 console.
error
(
"
caught by domain:
"
, err.message));

d.
run
(() 
=>
 {

 
setTimeout
(() 
=>
 {

 
throw
 
new
 
Error
(
"
boom
"
);

 }, 
10
);

});

#### node:bufferv1.4.0

node:buffernow passes92.9%(65/70) of Node.js v26.3.0'stest-buffer*.jssuite.Buffer.indexOf/lastIndexOf/includesgain theendparameter.Buffer.concat/copyrange validation matches Node.ERR_INVALID_ARG_TYPE/ERR_OUT_OF_RANGEmessages are formatted identically to Node's, including grouped type lists and numeric separators for large values.#32626

Buffer.byteLength()no longer under-counts unpaired surrogates, so it agrees withBuffer.from(s).length, andlastIndexOfwithutf16leencoding no longer matches on odd byte offsets.#32784

const
 s 
=
 
"
\ud800
a
"
.
repeat
(
17
);

Buffer.
byteLength
(s, 
"
utf8
"
); 
// before: 51, after: 68

Buffer.
from
(s, 
"
utf8
"
).length; 
// 68 (now matches)

#### TextDecodersupports all WHATWG encodingsv1.4.0

TextDecodernow supports every encoding in the Encoding Standard. Sixteen previously-missing single-byte encodings (iso-8859-2,-5,-16,koi8-r,windows-1251, and others) are added, all 228 spec labels are recognized, and EUC-JP, Big5, ISO-2022-JP, and BOM handling during streaming decode now match the spec byte-for-byte.#32837

new
 
TextDecoder
(
"
iso-8859-5
"
); 
// no longer throws RangeError

new
 
TextDecoder
(
"
csisolatin5
"
); 
// label alias, also works

#### uidandgidfor child processesv1.4.0

Bun.spawn,Bun.spawnSync, andnode:child_processnow honor theuidandgidoptions. They change the child's user and group IDs before exec. Behavior matches Node/libuv:setgroupsthensetgidthensetuidon POSIX, andENOTSUPon Windows.EPERMis surfaced synchronously when the caller lacks permission.#33060

import
 { spawnSync } 
from
 
"
node:child_process
"
;

// as root:

spawnSync
(
"
id
"
, { uid
:
 
65534
, gid
:
 
65534
 });

// child reports uid=65534 gid=65534, supplementary groups dropped

#### NODE_COMPILE_CACHEv1.4.0

module.enableCompileCache()and theNODE_COMPILE_CACHEenvironment variable now persist bytecode to disk between runs.--cpu-profand--heap-profwrite V8-format profiles with Node's filename convention.--watch-kill-signaldelivers the configured signal to JS listeners before restarting. The Node 26Assertclassand a nativeassert.partialDeepStrictEqualare implemented. Throws insidefs/dns/pbkdf2callbacks now route to'uncaughtException'instead of'unhandledRejection'.node:urlreaches83.0%on Node's test suite.new URL(bad)throws Node's exactTypeError: Invalid URLshape.#34660

NODE_COMPILE_CACHE=
~
/.cache/bun bun app.js

#### Datadog continuous profiling worksv1.4.0

dd-tracewithprofiling: trueand@datadog/pprofnow load and profile in Bun.v8::CpuProfileris backed by JavaScriptCore's sampling profiler. The nanObjectWraptemplate pattern (FunctionTemplate::SetClassName,InstanceTemplate,PrototypeTemplate,Signature) is implemented. So are the rest of the 89 V8 and Node symbols pprof's prebuild links against. The returned profile correctly attributes wall-clock samples to the hot function with full stack depth.#36747

import
 { time } 
from
 
"
@datadog/pprof
"
;

time.
start
({ intervalMicros
:
 
1000
 });

// ... code to profile ...

const
 profile 
=
 
await
 time.
stop
(); 
// pprof-format profile

#### await worker.terminate()waits for the threadv1.4.0

Worker threads are joined by their parent.await worker.terminate()resolves with the exit code only once the thread is gone, and every worker it spawned too. Everything the worker posted before exiting is delivered before'exit'. A worker's "may run script" gate closes the moment its stop is requested. So no timer, socket callback, or thread-pool completion dispatches into a worker that is being stopped. Off-thread completions reach their VM through a handle that teardown closes. A late one is refused and released instead of touching freed memory.

import
 { Worker } 
from
 
"
node:worker_threads
"
;

const
 w 
=
 
new
 
Worker
(
"
./heavy.js
"
);

const
 code 
=
 
await
 w.
terminate
(); 
// resolves 1 for a running worker

// the thread and its nested workers are gone

This work landed in#38299,#38436,#38457, and#38660.

The event loop stays fair under a worker that posts faster than its parent can deserialize: message drains take a bounded budget per turn, so a message flood no longer starves timers, I/O, or the worker's own pending stop.

#### Node-API version 10v1.4.0

Bun now reports Node-API version 10, syncs the public headers from Node 26, and implements the fiveNAPI_EXPERIMENTALnode_api_*functions Node 26 added.#34146#36804#34147

#### N-API finalizers run in LIFO order at exitv1.3.13

napi_wrapfinalizers now run in LIFO order at process exit. This fixes shutdown segfaults in kuzu, duckdb, sqlite3, node-llama-cpp, and @napi-rs/canvas. Two crashes innapi_create_external_bufferand UTF-8 property-name handling were fixed. This unblocks napi-rs addons likeimpit.ThreadSafeFunctionfinalizer cleanup no longer crashes or hangs.napi_delete_referenceis now callable from inside a finalizer.napi_typeofcorrectly reports wrapped callbacks and boxed primitives.

#### tls.setDefaultCACertificates()andsecureContext.addCACert()v1.4.0

node:tlsgains per-contextsecureContext.addCACert()and process-widetls.setDefaultCACertificates().#31155

#### node:http2diagnostics_channel, AltSvc, extended CONNECT, andallowHTTP1v1.4.0

node:http2gainsdiagnostics_channelinstrumentation, AltSvc and Origin frames, extended CONNECT, andallowHTTP1fallback for the compatibility server.#31584

#### fs.mkdtempDisposable()andFileHandle#pull()/#writer()v1.4.0

fs.mkdtempDisposable()andFileHandle.prototype.pull()/.writer()are implemented, andfs.watchno longer drops events when two files change in the same millisecond.#31830

#### node:zlibbrotli and zstd dictionariesv1.4.0

node:zlibsupports brotli and zstd dictionaries,reset()is Node-compatible, asyncwrite()accepts growableSharedArrayBuffer, andzstdCompressaccepts explicitundefined/nulloptions. Node's zlib suite passes at96.8%.#34427#36555#36423

#### node:util:styleTexthex colors,getCallSites,tty.WriteStreamv1.4.0

styleTexthex colors,getCallSites, regexp highlighting, andtty.WriteStreamare now implemented.parseArgsmatches Node's property insertion order and treatsnullboolean flags as absent.MIMETypeerror messages matchERR_INVALID_MIME_SYNTAX.types.isBigIntObject/isSymbolObject/isBoxedPrimitivehandle modified boxed primitives.#34434#34601#33769#34611#34872

#### v8.GCProfilerv1.4.0

node:v8addsv8.GCProfiler(backed by JavaScriptCore'sHeapObserver) andv8.isStringOneByteRepresentation().

#### ws-compatible'upgrade'and'unexpected-response'eventsv1.4.0

Bun'sWebSocketclient emits'upgrade'and'unexpected-response'events, matching the ws package.#36272

#### dns.promises.getDefaultResultOrder()andgetServers()v1.3.12

node:dns/promisesnow exportsgetDefaultResultOrder()andgetServers(), fixing Vite 8 builds.#28949

#### SIGWINCHon Windowsv1.3.3

On Windows,SIGWINCHnow fires on terminal resize (unblocking TUI libraries like opentui and opencode), andSIGHUP/SIGBREAKfire on console close and Ctrl+Break.#24704

#### --use-system-careads Node's Windows certificate storesv1.3.14

--use-system-caon Windows now reads the same certificate stores Node.js does (ROOT,CA, andTrustedPeopleacross local-machine, current-user, group-policy, and enterprise locations), fixing intranet servers that omit their intermediate chain.#30408

### Package manager#

#### Lockfile migrationv1.4.0

bun install's npmpackage-lock.jsonmigrator now supports lockfileVersion 1 through 4, including bundled and nested dependencies,optionalPeers, andoverrides.

Migratingpnpm-lock.yamlv9 lockfiles now supportspatchedDependencies, snapshot aliases, catalogs, gitpath:, multi-document files,runtime:entries, and named registries.

A project'sbunfig.tomlnow takes precedence over any.npmrcfor the same key;.npmrc-only settings such as//host/:_authTokenstill attach to registries declared inbunfig.toml.

#### bun.lockversioningv1.3.2

bun.locknow records aconfigVersionalongside the existinglockfileVersion. So future Bun releases can change install defaults for new projects without affecting existing ones. New lockfiles getconfigVersion: 1and default to the isolated linker. Existing lockfiles without the field are treated asconfigVersion: 0and keep the hoisted default.#24236

{

 
"
lockfileVersion
"
:
 
2
,

 
"
configVersion
"
:
 
1
,

 
"
workspaces
"
:
 {

#### publicHoistPatternandhoistPatternv1.3.1

The isolated linker now readspublicHoistPatternandhoistPatternfrombunfig.tomland.npmrc.publicHoistPatternhoists matching transitive packages (like@types*or*eslint*) to the rootnode_modulesso every workspace can resolve them;hoistPatterncontrols what's hoisted intonode_modules/.bun/node_modules.#23567

[
install
]

publicHoistPattern
 
=
 [
"
@types*
"
, 
"
*eslint*
"
]

hoistPattern
 
=
 [
"
*
"
]

#### install.hoist = falsev1.4.0

install.hoist = falseinbunfig.toml(orhoist=falsein.npmrc) disables the isolated linker's hiddennode_modules/.bun/node_modulesfallback directory, so packages thatrequire()an undeclared dependency fail withMODULE_NOT_FOUNDinstead of resolving through the fallback, matching pnpm'shoistsetting.#36972

#### bun update --recursiveand--filterupdate every selected workspacev1.4.0

bun update --recursiveandbun update --filter <pattern>now update the dependencies of every workspace they select and write each workspace'spackage.json.--filtercan be repeated, and--filter '!name'excludes a workspace.bun outdatedaccepts the same repeated--filter. Previously two filters selected nothing. A dependency declared ascatalog:is left as written.#36360

bun update --recursive --latest

bun update --filter 
'
pkg-*
'
 --filter 
'
!pkg-c
'

#### bun update <name>updates every copyv1.4.0

bun update <name>now re-resolves every copy of<name>in the lockfile, including the copies other workspaces and your transitive dependencies depend on.#36360

#### Happy Eyeballs for registry connectionsv1.4.0

bun installnow correctly interleaves IPv6 and IPv4 addresses per RFC 8305 when connecting to the registry, so a blackholed IPv6 route (Starlink, some corporate networks, misconfigured Docker bridges) costs nothing per manifest fetch.#36295

#### Streaming tarball extractionv1.3.13

bun installnow decompresses and extracts packages while they download, with incremental integrity hashing computed on the fly.#29404

#### Peer dependency resolution is up to 8x fasterv1.3.13

bun install --linker=isolatedisup to 8x fasteron monorepos with heavy peer dependency graphs. The first resolution pass now deduplicates subtrees with the same resolved peer dependencies. Before, it expanded every position in the dependency tree. On one reported monorepo this cut the first-pass node count from millions to ~75K. The.bun/store layout is byte-identical.#29342

#### bun listv1.3.2

bun listis now a shorthand forbun pm ls, printing your dependency tree without the extrapmsubcommand.#24159

#### bun publishsends your READMEv1.3.14

bun publishnow sendsreadmeandreadmeFilenameto the registry, so packages published with Bun show their README on npmjs.com.#30257

#### Per-path.npmrcauth tokensv1.3.11v1.4.0

.npmrcauth tokens are now matched by hostandpath, so multiple registries on the same host (Azure Artifacts, JFrog) each get their own token instead of last-one-wins.#26351

#### bun updateupdates catalogsv1.4.0

bun updatenow updatescatalogversion definitions in non-interactive mode, and re-resolves catalog references when run from the workspace root.#36304#36379

#### patchedDependenciescache keyed by full patch hashv1.4.0

patchedDependenciescache entries are now keyed by a SHA-1 of the whole patch file. Previously the key was a Wyhash, and only the first 16 KiB of the file was hashed. So two projects sharing an install cache got each other's patched package if their patches collided or were identical for their first 16 KiB. Existingnode_modulesare re-patched once on the next install.#32749

#### bun pm ls --trustedv1.4.0

bun pm ls --trustedfilters the dependency tree to packages allowed to run lifecycle scripts, honoring bothtrustedDependenciesinpackage.jsonand Bun's default trusted list. Combines with--all.#32478

### Performance#

### JavaScriptCore#

#### Temporalv1.4.0

Temporal, the replacement forDate, is now enabled by default.

const
 departure 
=
 Temporal.ZonedDateTime.
from
(

 
"
2026-08-10T09:00[America/Los_Angeles]
"
,

);

departure.
add
({ hours
:
 
11
, minutes
:
 
5
 }).
withTimeZone
(
"
Asia/Tokyo
"
).
toString
();

// "2026-08-11T12:05:00+09:00[Asia/Tokyo]"

new
 
Date
().
toTemporalInstant
().
toZonedDateTimeISO
(Temporal.Now.
timeZoneId
());

#### WebAssemblyv1.4.0

* JSPI (JavaScript Promise Integration)is implemented and enabled by default (53e97afd3421,307705):WebAssembly.Suspending/WebAssembly.promisinglet Wasm suspend on JS Promises directly.
* Wasm SIMD now runs in the interpreter(300666, cec82daed8ab). SIMD instructions no longer require JIT compilation.
* Memory64 support (>4 GB Wasm heaps), the multi-memory proposal, and relaxed SIMD.
* WebAssembly.compileStreaming/instantiateStreamingacceptcompileOptions(4f51c89e3c77).
* The string size limit is removed (81ff731cd920).
const
 suspending 
=
 
new
 WebAssembly.
Suspending
(
async
 (
url
) 
=>
 {

 
const
 res 
=
 
await
 
fetch
(url);

 
return
 res.
arrayBuffer
();

});

const
 { instance } 
=
 
await
 WebAssembly.
instantiate
(
module
, {

 env
:
 { fetch
:
 suspending },

});

await
 WebAssembly.
promising
(instance.exports.run)();

Per-builtin speedups (String, Array, Map/Set, Object/JSON/Intl) are tabulated in thechangelog.

#### ES module loader rewritten in C++

JavaScriptCore's ES module loader has been rewritten (242740, 4a638109b905). The previous implementation was partly written in JavaScript, followed an outdated spec draft, and had long-standing bugs: assertion failures on valid ES modules, incorrect evaluation ordering with top-levelawait, and improperly cached resolution failures.

The new loader is pure C++ following the modern ECMAScript spec. Top-level-await evaluation order andimport()error propagation now match the spec exactly, which fixes several ESM/CJS interop bugs (require(ESM), dependency graphs with top-levelawait).#29393

#### Promises and async functions

JSC moved its Promise implementation from JavaScript builtins to C++, then layered allocation-elimination on top. This directly affects every async path in Bun (Bun.servehandlers,fetch, database drivers).

Moved to C++:Promise.all/allSettled/any/resolve/reject/prototype.finally(303603,303706,303732,300603,305030,300130) and the MicrotaskQueue code driving AsyncGenerator (304772).

Allocation elimination:

* Skip an internal allocation for the single-awaitcase (314637) and when an initialthenhas a single handler (314733).
* Inline async function bodies that contain noawaitand optimize the returned promise (304740,313029).
* Inline allocation forPromise.resolve(non-thenable)(314865).
* Skip the intermediate promise for non-thenable elements in combinators (315017,race 1.71× / all 1.47×), and avoid per-element context allocation (314861,314813).
* Scheduling a promise's.then/.catchcallback no longer allocates a separate microtask object (314788).
* promise.catch()now gets the same JIT optimization as.then()(f9d99657ac89,~1.22×).
* Queued microtasks take less memory and dispatch faster (2ff26dc8e6cc).
* Remove a redundant instruction fromawait/yieldbytecode (311239).
* Skip allocating the{value, done}result object on generator resume (0b65fe084bed).
* Shrink each generator object from 64 → 48 bytes in memory (e0704d3127d5).

#### String

Operation
Commit
Speedup
String#indexOf
 (1-char) on concatenated strings
3a21b7550526
44.98×
String#endsWith
 constant arg, inlined in the JIT
901865149859
up to 10.5×
String#includes
 in DFG/FTL (constant-folded)
cc5da5a661a3
9.76×
1-char 
startsWith
/
endsWith
 on concatenated strings
fa83cf53f871
9.35× / 8.65×
String 
===
 equality on Latin-1 strings in the JIT
2fc620c5697b
5.85×
startsWith
 in DFG/FTL (constant)
1f7d7d5a8c23
5.76×
isWellFormed
/
toWellFormed
 (SIMD)
e5f7abfaed5d
5.36× / 5.19×
String#indexOf
 1-char without rope resolve
8d918b4794c4
3.99×
startsWith
/
endsWith
 1–16B constant immediate
67969621f703
3.10× / 2.83×
replace
/
replaceAll
 in C++
2b37638c2082
up to 3.0×
String#includes
 1-char without rope resolve
dbe0b0a08f9a
2.73×
UTF-16↔UTF-8 conversion (SIMD)
fda0e1e0c823, 3fbc2eefcf86
2–5.5×
 (non-ASCII)
repeat
 in C++
2526a45e199d
up to 2.1×
padStart
/
padEnd
 in C++
62667c9f166e
up to 2.0×
String#indexOf
 strength reduction
81e56564a0b0
1.81×
toUpperCase
 DFG/FTL intrinsic
47263c1fcdf7
~1.4×
String#split
 in C++ + DFG node
1a0160315f98
~1.21–1.23×
String#concat
 in C++
fe7e0f57289e
String#replace
 (string arg) builds ropes
69162bbdb602
RegExp.prototype[Symbol.match]
 in C++
e922a2cecfac
String#matchAll
 in C++
31e38187aad2

#### Array

Operation
Commit
Speedup
indexOf
/
includes
 string compare, 8 bytes at a time
f9477aedc258
5.39× / 5.25×
Resizing arrays with 
arr.length = N
da43fc766f60
4.30×
Array.of
 compiled as an array literal in the JIT
445df9a64416
up to 3.2×
Array.prototype.flat
 in C++
546d47afe6bf
2.0–3.2×
Array.from(arguments)
 fast path
12bbbd4b4f3c
2.5–2.85×
lastIndexOf
 in the JIT
bc818abb8d4b
up to 2.57×
Array.from(map.keys()/values())
87d58dfdc60b
1.3–2.8×
Array.from(Set)
 fast path
ff70a7d00968
1.4–2.2×
FTL 
indexOf
/
includes
 string loop layout
6846e1b56c4b
1.68×
Array.of
 in C++
8d5b7e4c8f2e
1.43–1.55×
Array#sort
 on partially-sorted input
cd9b98604840
1.34×
Small-array sort inlined in DFG/FTL (≤16 elements)
cab7a45a413c
Dedicated 
Array#concat
 DFG/FTL nodes
94e35cf4d86c
unshift
 grow-and-shift fast path
dde627a1d427

#### Map / Set / WeakMap

Operation
Commit
Speedup
[...set]
 spread walks the hash table directly
38411ab91e01 + 4f4154bf1726
~6× total
[...map.keys()]
 / 
[...map.values()]
a82152a94870
~3.78×
Set#size
 / 
Map#size
 no longer a function call
2e2c23521a24
2.24× / 2.74×
Cloning large Maps/Sets (
new Map(map)
)
253bd0c20582
2.09× / 1.99×
Map/Set fast iteration (for-of)
433704897995
2.05× / 1.59×
Map/Set iterator 
.next()
 JIT-inlined
e4a0db79b3fb
new WeakMap()
 / 
new WeakSet()
 allocation JIT-inlined
d61d43e680e1, 8317f5c80ed4
Map/Set backing storage shrunk to actual usage
f72ea56abf5c
memory

#### Object, JSON, Intl, and JIT

Operation
Commit
Speedup
Intl.DurationFormat#format
 per-unit formatter cache
7e34b0157828
26.5×
Set class-field function names at parse time
b6a9b84dae1f
9.32×
Object.defineProperty
#31562
8.6×
Object.hasOwn
 JIT-inlined
aafd2ae78418
4.31×
JSON.stringify
 Int32-array fast path
2ec81a993d35
3.08×
Double 
%
 for positive integers
899d00c4aa72
2.84×
Math.hypot
 with 4+ args
60dfa5abdbb3
1.6–2.4×
JSON.parse
 short-string value cache
128591e63775
1.50×
Intl.Segmenter
 segment iteration
31d781e3386c
1.21×
Cached BigInt remainder (multiplicative inverse)
559de0581a46
Objects stay on JIT fast path up to 128 properties (was 64)
f6414a9cee54
Dedicated 
Array.isArray
 DFG/FTL node
b7c903516b25
for...of
 over arrays skips redundant bounds checks
2d4d8ad1273a
===
 between objects (reference equality)
8f52a29461ca
Error.isError
 in DFG/FTL
6c34b6a708cd
Eager AST build for IIFEs (skip syntax-only pass)
709e4e7e7ec7
cold start
Parser/Lexer memory-layout optimization
8243c6b69d66
JSON.parse
 numbers via fast_float
1625d084a7f4
JSON.stringify
 16-bit→8-bit characters
26ddd2802cf5
Intl.NumberFormat
 creation
367f77ea6640
toLocaleLowerCase
/
UpperCase
 root-locale fast path
e14189a28e4c

Plus more JIT compiler work landed across the pin bumps:

* faster comparison chains and SIMD constant loads on ARM64 (#26161)
* inlinedString#localeCompare(#29897)
* faster bit rotation
* faster module-loader star-export resolution
* a workaround for slow Date initialization on recent ICU (#30096)

### Other runtime fixes#

* Bun.RedisClient: a failed connection closes its socket,connect()settles once, andoncloseruns once. Before, a client that could not connect kept the process alive forever. Fixes#18895.#39511#39513
* Bun.RedisClient:close()andconnect()cancel the pending retry timer, so a closed client no longer keeps the process alive.#39546
* Bun.RedisClient:idleTimeoutcounts from connect and restarts on incoming data. Before, it behaved likeconnectionTimeout.#38281
* Bun.RedisClient:subscribe()on a failed client rejects instead of storing the listener and keeping the process alive.#39547
* Bun.RedisClient:close()on arediss://client no longer hangs when the TLS shutdown is deferred by a stuck peer.#39548
* Bun.RedisClient:duplicate()of a closed client starts with no close history and reconnects.#39575
* process.memoryUsage().heapUsednow updates after every collection, includingBun.gc(true). Before, it kept the value from the last allocation-driven collection.#39593
* console.write()inside abeforeExithandler no longer loops forever when stdout is a pipe.#38641
* Creating aShadowRealminside anode:vmcontext no longer crashes.#39529
* Bun.file(path).arrayBuffer()on a file over 4 GiB throwsRangeErrorinstead of returning a truncated buffer.#39558
* A source file of 2 GiB or more reports "File is too large to parse" instead of a garbled syntax error.#39095
* ICU, libuv, and BoringSSL allocate through mimalloc. This fixes an ICU "failed to initialize Segments" error on Windows.#39472
* require("ws")no longer loadsnode:httpup front, which saves about 10 ms.#39435
* f64/doublearguments preserveNaN,-0.0, and negative BigInts exactly.#33122
* toBufferleaves caller-owned memory alone when no finalizer is provided.#36521
* JSVALUE_TO_INT32handles double-encoded JSValues.#34653
* viewSourceandJSCallbackthrow validation errors.#34396
* TinyCC updated to latest upstream (macOS 15 compatibility, arm64 alignment fixes).#26210
* The built-in C compiler respectsC_INCLUDE_PATHandLIBRARY_PATH(so NixOS works).#26250
* dlopen()works on libraries embedded viabun build --compile.#30720
* new CString(ptr)is constructable.#25257
* Pointer values round-tripped throughNumber(String(ptr))no longer become18446744073709551615on the C side.#25045
* worker.terminate()is safe while the worker thread is inside aJSCallback.
* bun:ffierror messages now include the actualdlerror()message from the OS, telling you exactly which library failed to load and why, instead of a generic "Failed to open library".#23585
* Request.prototype.clone()andResponse.prototype.clone()now throwTypeErrorwhen the body has already been consumed or is locked, per the Fetch spec. Previously the clone succeeded silently and resolved to an empty body.#33129
* Response.redirect(url)now runs its argument through the WHATWG URL parser before writing theLocationheader, so spaces, non-ASCII characters, default ports, and dot segments are normalized per the Fetch spec.#33126
* Bun.readableStreamToArrayBufferand the otherreadableStreamTo*helpers now return a rejected promise instead of throwing synchronously when passed an already-errored stream; the same applies tonew Response(erroredStream).arrayBuffer().#33043
* HTMLRewriter.transform()now rejects when the upstream response body errors mid-stream instead of resolving with a silently truncated document.#32927
* structuredCloneon a detachedArrayBuffernow throws aDataCloneErrorDOMExceptioninstead of a plainTypeError, matching the HTML spec and Node.js.#32799
* structuredClone(Object.prototype)now returns{}instead of throwingDataCloneError, matching Node.js and the HTML spec.#32983
* FormDatamultipart serializationnormalizes lone CR and lone LF to CRLF in field names and string values per the WHATWG spec, so serialized bodies are byte-identical to Node.js and browsers.#32975
* URLSearchParamsandFormData.get(),.getAll(), and.has()now normalize malformed Unicode in the name argument the same way.set()and.append()do, so an entry stored under such a name is found by lookup, matching Node.js and browsers.#33398
* console.table()andBun.inspect.table()now invoke each cell's getter and custom-inspect hook exactly once instead of two or three times.#32924
* socket.setTypeOfService()onBun.connectsockets validates its argument, throwingERR_INVALID_ARG_TYPE/ERR_OUT_OF_RANGEfor non-numeric values.
* FormDatamultipart boundariesnow exactly match WebKit's----WebKitFormBoundary…format, fixing uploads to strict multipart parsers including OpenAI's file upload endpoint.#29631
* TextDecoderwith{ stream: true }no longer corrupts characters split across chunk boundaries forshift_jis,euc-jp,iso-2022-jp,gbk,gb18030,big5, andeuc-kr.#31438
* TextEncoder.encodeInto()now returns{ read: 0, written: 0 }and leaves the buffer untouched when a 4-byte character (like an emoji) doesn't fit, instead of writing the � replacement character, matching the WHATWG Encoding spec.#31532
* self.postMessage(msg, [transferable])inside aWorkernow actually transfersArrayBuffers andMessagePorts. Previously the positional-array overload was silently ignored and transferables were cloned instead of moved.#30068
* new Request()now stores and returns thecacheandmodeoptions instead of always reporting"default"and"navigate", and preserves them through.clone().#26099
* SlicedBlobsrespect their slice bounds when streamed or used as aResponsebody, and advertise the correctContent-Length.
* Response.clone()andRequest.clone()now tee the body when.bodywas accessed (but not read) before cloning. Previously the original's cached.bodystream was silently drained to zero bytes, breaking the commonres.clone()-then-new Response(res.body, res)cache-and-forward pattern.#33779
* new TextDecoder()and.decode()now throwTypeErrorwhen passed a primitive as the options argument and acceptnullas the default dictionary, per WebIDL.#35189
* new File()now normalizes thelastModifiedoption per WebIDL:NaNand unparseable strings become0, andnullis treated as present (yielding0) instead of falling through toDate.now().#33922
* .envparsinghandles UTF-8 correctly. A leading BOM no longer drops the first variable. Applies to auto-loaded.envfiles,--env-file, andutil.parseEnv.#34002
* .envparsing: Trailing junk after a closing quote no longer swallows the following lines into the value. Applies to auto-loaded.envfiles,--env-file, andutil.parseEnv.#34003
* .envparsing: Multibyte characters whose encoding ends in0xA0are no longer corrupted by whitespace trimming. Applies to auto-loaded.envfiles,--env-file, andutil.parseEnv.#34001
* Assigning to an ES module importis now a runtimeTypeErrorwhen the write is reached, per ECMA-262, instead of a parse-time error that made the module unloadable even when the assignment was in dead code or atry/catch.bun buildstill errors at bundle time.#36046
* require.extensionshooksregistered by an entry point of 4 KiB or more now work on every run. Previously they were ignored from the second run onwards, once the file came from the transpiler cache, and files with unknown extensions imported by that entry point were parsed as TSX instead of resolving to their paths.
* require.extensionshooksEntry points built withbun build --target=bun --format=cjshad the samerequire.extensionsbug on every run.#33371
* structuredClone(andpostMessage,Worker,MessageChannel) no longer silently resolves back-references to the wrong value when the graph contains aBigInt,CryptoKey, orX509Certificate. Previously a shared object appearing after a BigInt could come back as the BigInt itself, or deserialization could fail entirely.#32791
* db.close(true)finalizes all outstanding prepared statements.#36573#36793#37045#34925#34186#34962
* Bun.RedisClient:expire()rejectsNaN/undefinedseconds instead of silently sendingEXPIRE key 0
* Bun.RedisClient: the RESP line-length cap is raised from 512 KB to 512 MB for large replies
* Bun.RedisClient: a tornVerbatimString/BlobErrorbody is no longer treated as a fatal protocol error
* Bun.RedisClient: invalid database segments in the connection URL are rejected instead of silently ignored
* S3 simple requests handle close-delimited HTTP responses.
* Bun.write(): no longer over-copies or truncates when passed a caller-owned destination file descriptor.#36758
* Bun.write():Bun.write(file, file)no longer truncates on Linux when the source size is unknown (splice/sendfileloop to EOF).#36590
* Bun.YAML: input is validated for embedded NUL bytes before parsing.
* Bun.randomUUIDv7(): an explicit timestamp argument is honored verbatim.#34321
* Bun.randomUUIDv7(): monotonicity is preserved when the 12-bit counter rolls over within a millisecond.#34022
* Bun.randomUUIDv7(): timestamps ≥ 2^48 andNaNare rejected instead of silently truncated.#34021
* gzipSync/deflateSyncthrow a clear invalid-argument error for out-of-range libdeflate compression levels instead of a misleading "Out of memory".#34117#34114
* Bun.mmap()returns a view at the requestedoffsetinstead of the page-aligned offset.#34120
* Bun.mmap(): itsoffset/sizeoptions are now typed.#34573
* Bun.udpSocket:connect()rejects out-of-range ports instead of silently clamping to 0.#34029
* Bun.udpSocket: numeric options are range-checked instead of silently truncated (also applies toBun.password).#36999
* Bun.FileSystemRouter:match()returnsnullfor paths not starting with/instead of matching incorrectly.#34028
* Bun.FileSystemRouter: empty-key query pairs are skipped instead of terminating the query parse early.#34027
* Bun.color()clamps out-of-range object alpha instead of wrapping mod 256.#34020
* Bun.color()lists all accepted format strings in its invalid-format error.#34314
* Bun.CryptoHasher.update()rejects odd-length hex strings instead of silently truncating.#35188
* Bun.Socket.setKeepAlive()honors milliseconds as documented.#34269
* Bun.Socket.setKeepAlive():setKeepAlive(true)returnstrue.#34269
* Bun.Globpreserves a leading**as a globstar under!negation.#33759
* Bun.TranspilerthrowsTypeErrorfor non-transpilable loaders.
* Bun.openInEditor()throws when no editor is found instead of silently spawning an empty command.#37210
* Bun.RedisClient: calling.connect()after a disconnect properly resets the failed state instead of permanently rejecting every command withConnection has failed.#29927
* Bun.file():.stat()and.delete()no longer corrupt paths containing non-ASCII UTF-8 characters.#26646
* Bun.generateHeapSnapshot("v8", "arraybuffer")returns the snapshot as a UTF-8ArrayBuffer, which scales to very large heaps.
* RuntimeBun.plugin()onResolvehooks that return a filesystem path in the defaultfilenamespace now work. Previously the path came back asfile:/abs/path.jsand failed to load, breaking path aliases and virtual-to-real redirects for dynamicimport(), computedrequire(),Bun.resolveSync(), andimport.meta.resolve().#33409
* Bun.TOML.parse()throws on syntax errors like missing array commas instead of silently returning partial data.#31255
* Bun.TOML.stringify()no longer emits redundant headers for pass-through super-tables.#37009
* Added a socket syscall fault-injection layer for deterministic fuzzing ofnode:net,node:tls,node:http, HTTP/2,fetch, and WebSocket against partial reads/writes, mid-streamECONNRESET/EPIPE,EAGAINstorms, and backpressure races, and fixed several bugs it surfaced.
* Crashes inWorkerandworker_threadstermination have been fixed.
* A crash inBun.FileSystemRouter.match()has been fixed.
* A rare crash inconsole.logandBun.inspectformatting has been fixed.
* A crash instructuredClone()andpostMessage()serialization has been fixed.
* A crash in proxiedfetch()requests has been fixed.
* Fixed two GC bugs where anAbortSignalcould lose itsreasonor itsabortevent listeners.
* AbortSignal.any()keeps its source signals correctly rooted for GC.
* Errorfinalization crash is fixed.
* Stream error handling crash is fixed.
* Fixed a top-level await bug where a dynamicimport()from a module that was itself still awaiting would throwReferenceError: Cannot access '...' before initializationinstead of resolving.
* Workertermination is safe whilefs.watchFile()callbacks are pending.
* fs.readFile(path, "utf8"),Buffer.toString("utf8"), andStringDecoderreport allocation failure as anOutOfMemoryerror.
* Whole-file reads (the.envloader,bun pm pack,Bun.Image) report allocation failure asENOMEM.
* Bun.FileSystemRouter.reload()synchronizes access to the resolver's cached directory-entry map.
* Fixed a segfault running the linux-arm64 build under Termux on Android by issuingepoll_pwait2as a raw syscall and gating it off on Android, whose per-app seccomp policy blocks it.
* A crash in auto-install resolution has been fixed.
* require("./addon.node?v=1")loads the addon andimport("./addon.node?v=1")throws the intendedTypeError; query strings and custom extensions mapped to the napi loader are handled.
* The ini parser treats empty single-quoted values (key='orkey='') as empty strings, matching npm/ini.
* console.write.call(primitive)throwsERR_INVALID_THIS.
* Crash reports from baseline x86_64 builds now symbolicate correctly on bun.report; a deadcfg(feature)gate was tagging them with the non-baseline platform and resolving against the wrong debug artifact.
* Batched UDP receive (recvmsg_x/sendmsg_x) is gated to macOS 15.6+.
* Thebunnpm package's postinstall now tries the musl binary first on musl-based Linux (detected viaprocess.report, not just Alpine).#36283
* The generated@oven/bun-linux-*packages now carry alibcfield so npm skips downloading the wrong-ABI optional dependency.#36283
* bun --printwith top-levelawaitnow prints the module's final completion value instead of the first awaited value:bun -p '(await 1) + 1'prints2, not1.#30208
* The debugger no longer pegs a CPU core at 100% while paused at a breakpoint; Bun now sleeps instead of spinning in a loop while you step through code.#29438
* Breakpoints in files over 50KB now land on the right line when debugging from VS Code's debug terminal. The runtime transpiler cache is disabled whenever the inspector is active viaBUN_INSPECT, not just--inspect.#28189
* Loading a native addon known to require V8 C++ APIs Bun doesn't yet support (currentlybetter-sqlite3) now throws a clear error linking to the tracking issue and suggestingbun:sqlite, instead of a confusingdlopenfailure.#24384
* Runningbun file.css(or any file type Bun can't execute directly) now prints "Cannot run css files directly" instead of the misleading "File not found".#26126
* When thebunnpm package is installed with--ignore-scripts(or via pnpm, which skips postinstall by default), the placeholder binaries now print a clear error explaining how to fix it and exit non-zero, instead of silently doing nothing.#26259
* Fixed a--hotrace where an error thrown during module evaluation could be remapped against the wrong sourcemap if a file-watcher event fired before the error was printed.#29740
* @types/bunno longer depends on@types/react, so projects that don't use React no longer get React's global JSX types pulled in just by installing Bun's types.#24557
* @types/bunnow ships against@types/node@25.#25460
* Theexpect().toContainKey*matchers fall back toPropertyKeywhenkeyof unknownresolves tonever.#25460
* Bun's repo now ships a Nix flake, so contributors on NixOS can spin up a fully reproducible dev environment with LLVM 19, CMake, Rust, and Go with nosudorequired.#23406
* Download progress (likebun upgrade) now shows human-readable sizes (23.2MiB/100MiB) instead of raw byte counts.#24266
* CI environment detection now recognizes 40+ providers (auto-generated from theci-infodataset).#23708
* CI environment detection respectsCI=trueto force CI mode.#23708
* --no-clear-screenandBUN_CONFIG_NO_CLEAR_TERMINAL_ON_RELOADare now honored by the dev server whenhmr: true.#26184
* bun init --minimalno longer creates Cursor rules orCLAUDE.md; it now writes onlypackage.jsonandtsconfig.json, as intended.#26051
* bun init --reacttemplates now name the server entrypointindex.tsinstead ofindex.tsx.#23469
* The react-tailwind template'sbuild.tsnow type-checks under its own stricttsconfig.json.#26258
* bun publish --helpnow shows the correct description for--dry-run.#25137
* The VS Code extension's test explorer now recognizes Bun's newer test functions during static analysis, so code lenses and the sidebar pick them up.#25256
* Debugger CLI flags now propagate correctly to single-file executables built withbun build --compile.#25600
* Error carets for out-of-range\u{...}Unicode escapes now point exactly at the backslash instead of two columns to the left.#31138
* The dev server's inspector no longer emits duplicateBunFrontendDevServer.clientNavigatedevents on route navigation.#32081
* Type-definition fixes in@types/bun: addedServer.protocol,S3Options.contentEncoding, theseedparameter onBun.hash.crc32(), UDP socket methods,autoloadTsconfig/autoloadPackageJson, andBunLockFile.configVersiondocumentation.
* Socket.reload()correctly requires{ socket: handler }
* Bun.build()allowssplitting: truealongsidecompile
* TheBun.Buildtargettype includesbun-linux-x64-baseline,bun-linux-x64-modern, and other SIMD variants.
* The FFI type maps no longer triggerTS2300: Duplicate identifierunder thetsgonative preview..#25267

### Otherfetch()fixes#

* Cancelling afetch()response reader(reader.cancel()/res.body.cancel()) now aborts the underlying request and closes the connection instead of silently draining the remaining body, so servers observe the cancellation.
* DNS lookup failuresfromfetch()andBun.connect()now reportENOTFOUNDwithsyscall: "getaddrinfo"and the hostname instead of a misleadingConnectionRefused/ECONNREFUSED, so retry wrappers can distinguish "name does not resolve" from "host refused".#32990
* fetch()matchesContent-Encodingcase-insensitivelyper RFC 9110. Responses sent withGZIP,Gzip, or the legacyx-gzipalias are now decompressed instead of being handed to JavaScript still compressed.#31521
* fetch()with an authenticated proxynow encodesProxy-Authorization: Basicwith the standard base64 alphabet (with=padding) instead of base64url, fixing rejected credentials on strict proxies.#31782
* fetch()withredirect: "error"now only rejects the five WHATWG redirect statuses (301, 302, 303, 307, 308). Previously the whole 3xx range was treated as a redirect, so a304 Not Modifiedresponse rejected withUnexpectedRedirectinstead of being returned.#36539
* fetch(request)with an already-consumed stream bodynow throwsTypeErrorbefore any network I/O, instead of opening a connection, writing the request head, and then failing withERR_STREAM_CANNOT_PIPE.#36499
* fetch()with an already-abortedAbortSignalnow returns an already-rejected promise synchronously, per the Fetch spec, instead of a pending promise that settled after a round-trip to the HTTP thread.
* fetch()after a bodyless response(HEAD,204,304,Content-Length: 0, or a followed redirect) only returns the connection to the keep-alive pool when the response was framed cleanly.
* fetch()following a bodyless redirectnow reuses the keep-alive connection for the request to theLocationURL. Since 1.3.14 aGETanswered with a302, or a smallPOSTanswered with a303or307, closed the connection and opened a new one. A3xxwith a body orConnection: closestill closes it.#37451
* fetch()after an HTTP/1.0 responseno longer pools the connection unless the response saysConnection: keep-alive, per RFC 9112. Previously the next request went out on a socket the server had already closed; idempotent requests were retried, and aPOSTfailed withECONNRESET.#37530
* Fixedfetch()silently hanging against certain hosts (e.g.api.fortnox.se). Bun's TLS handshake was sending an optional probe extension that some strict servers reject.#29782
* Fixedfetch()through an HTTP CONNECT proxy leaking the proxy's200 Connection establishedline into the returned response when it arrived split across TCP reads.#30385
* Removed an unintended 1 GiB cap on decompressedfetch()response bodies that causedZlibErroron gzip/brotli/zstd responses whose decompressed size exceeded 1 GiB.#32366
* Fixedfetch()decoding only the first member of a multi-member gzip response body and silently dropping the rest.#33708
* fetch():response.body.cancel()on an unread body now aborts the underlying transfer.
* fetch(): aborting a streaming response frees the buffered body and errors the reader.
* fetch(): a fully-buffered response that is aborted now errors its body stream instead of resolving stale bytes.
* fetch():new Request(input, { signal: null })detaches frominput's abort signal per spec.
* fetch(): uploads of aBun.file().slice()now send the correctContent-Length.#36862
* fetch(): Latin-1 request header values are isomorphic-encoded on the wire per spec.#35338
* fetch(): sending a request body withOPTIONSis allowed.#34920
* fetch(): truncated compressed bodies on close-delimited responses are rejected instead of returning partial data.#34922
* fetch(): redirects are followed as soon as the 3xx headers arrive instead of waiting for the body.#33613
* fetch(): URL schemes are compared case-insensitively for proxies and redirectLocationheaders.#35144
* fetch():http_proxy/no_proxyare re-evaluated on each redirect hop.#33651
* fetch():Proxy-Authorizationis sent when the proxy URL has an empty username or password.#36041
* fetch()rejects (rather than throwing synchronously) when reading an option throws.#33647#36145#36309#33710#33649

### Other test runner fixes#

* Largeexpect()mismatches print a real diff. The old diff engine gave up after 1 s and printed both values whole; a 456 KB string pair now diffs in 4 ms instead of 74 ms.#39310
* Fixed the TypeScript types forvi.mockinbun:test. It was incorrectly typed asvi.module, causing "Property 'mock' does not exist" errors in editors.#24248
* The JUnit reporter now emits one<testcase>per retry attempt, so CI flaky-test dashboards get per-attempt timing.#26866
* bun test --bailnow flushes the JUnit--reporter-outfileon both bail paths (test failure and unhandled rejection), so CI always gets the XML even when bail triggers early.#26852
* toMatchSnapshot()now works correctly with--rerun-eachand test retries: the snapshot counter is reset between iterations instead of looking for<name> 2,<name> 3, etc.#29375
* Snapshot-creation errors in CI now include the snapshot name and the received value, so you can find which assertion tried to write a new snapshot.#23419
* Object diffs inexpect()failures andconsole.logno longer silently drop properties with empty-string keys.{ "": "value" }previously printed as{}.#27166
* IDE test integrations now receiveTestReporter.found/start/endevents even when the debugger attaches after tests were discovered (e.g. with--inspectinstead of--inspect-wait).#25986
* test.each()/describe.each()keep the table array alive until the test is registered.
* jest.mock()validates its source origin.
* expect.extend()validates that each matcher is an ordinary JavaScript function and throws aTypeErrorotherwise.
* expect.extend()handles matcher objects with numeric index keys.
* Custom matchers registered viaexpect.extend()throwTypeError: not a constructorwhen called withnew.
* Exceptions thrown inside custom asymmetric matchers registered viaexpect.extendnow propagate to JavaScript instead of triggering a debug assertion.#29199
* spyOn()supports indexed property keys.
* mock.module()validates that its first argument is a string.
* mock.module(specifier)/vi.mock(specifier)work without a factory callback when auto-install is triggered.
* bun testformats deeply nested objects safely.
* NegatedconcurrentTestGlobpatterns like"!**/sequential-*.test.ts"now correctly select non-matching files for concurrent execution.#35315
* bun testno longer parks in the event loop for ~100ms per file when a previous file left a long-running timer pending; in a debug build, a 21-file suite with a leakedsetTimeoutwent from 2.5s to 0.6s.#36453
* Bun.deepEquals()andexpect().toEqual()now compareTemporalobjects (Instant,PlainDate,ZonedDateTime,Duration, …) by value; previously any two instances of the same class were reported equal.#37024
* --reporter=junitnow emits well-formed XML: control characters in test names are dropped instead of producing invalid entities,classnameis no longer double-escaped, and<failure>elements include the error message.#34975
* --reporter=junitnow emits one<testcase>per test with its final outcome after retries, so CI dashboards no longer show a passing suite as failed because of intermediate retry attempts.#33967
* Fixed inspectorTestReportertest IDs colliding between the live and retroactive reporting paths, which caused inspector clients keying state by ID to conflate unrelated tests.#36522
* expect()failure messages no longer swallow<...>spans in Received/Expected values; comparing'<div class="a">Hello</div>'against'<div class="b">Hello</div>'previously printed both as"Hello".#34343
* toHaveReturned()and related matchers validate a mock's.mock.resultsarray before reading it.
* spyOn()supports spying on a function'sprototypeproperty.
* Formatting aFormDatavalue validates itstoJSONproperty.
* test.each()handles values that throw while being formatted into the test title.
* toBeArrayOfSize()andtoHaveBeenCalledTimes()handle arrays of any length.

### Other bundler fixes#

* Bun.build()waits only for its own work. A pendingfs.readFile()on a FIFO no longer blocks an unrelated build.#38604
* --splittingno longer emits a chunk for animport()that is only reachable from dead code, such as anif (FLAG)removed by--define.#39591
* In a--compileexecutable,require()of another embedded CommonJS entry point works instead of failing with "Failed to evaluate module".#38437
* Bun.build({ compile: true })now applies sourcemaps correctly, so stack traces from compiled binaries show your real source paths instead of/$bunfs/root/app.js.#23916
* Fixedunicode-rangein@font-facebeing mangled by the CSS parser (U+0000-00FF→U0-0FF), which caused browsers to drop the font.#27613
* Fixedimport.meta.urlin bundles built with--bytecode.#23803
* Fixed__toESMemission when bundling ESM input to CJS output; the default-export wrapper now matches Node.js semantics.#23803
* Fixedbun build --compilesilently producing a no-op executable when 8 or more files were embedded. A chunk-sorting bug was picking an asset wrapper as the entry point instead of your code.#25859
* Fixedbun build --compileproducing an all-zeros binary when the output directory lives on a different filesystem than the temp directory (common in Docker, Gitea runners, and other overlayfs setups).#26883
* Standalone executablesbuilt withbun build --compilenow applyBUN_OPTIONSasexecArgvinstead of leaking it intoprocess.argv.#26346
* CSS parsernow accepts class selectors in::view-transition-old(.foo), the.null-cell token ingrid-template-areas,@page :left/@page foo:firstpseudos, andmaskshorthandgeometry-boxvalues.
* CSS parser: Logicalborder-*-*-radiusproperties (including withvar()) are no longer dropped or mismapped.
* CSS@layer: top-level@layerordering declarations are preserved (fixes Tailwind CSS).
* CSS@layer:light-dark()fallback variables are now injected inside@layerblocks.
* CSS minifierbounds nested&expansion,light-dark()evaluation, angle values, and pseudo/at-rule nesting.
* CSS minifiermerges adjacent rules with identical selectors in linear time.
* JS minifiernow collapses(a) => { return x }into(a) => x.
* JS minifier: a batch of invalid-output edge cases are fixed:xinstanceof ytoken fusion at start-of-file, dangling{ ...a, x: }from simplified spreads,Promise.resolve().then(() => )from unused dynamic imports, emptyelse {}blocks, and numeric property keys that overflow toInfinity.
* Tree-shakingcorrectly handlessideEffects: falsebarrels that re-export namespace imports (import * as ns; export { ns }), object literals keyed by inlined enum members, andexport *across package boundaries, fixingundefinedexports from packages like@tanstack/react-query.#27524
* HTML bundlingMultiple HTML entrypoints sharing one CSS file all get the<link>tag.
* HTML bundlingCompiled HTML references chunks with root-relative paths so assets load from any route.
* HTML bundling--compile --target=browsernow emits sourcemaps for inlined scripts.#27821
* HTML bundling--compile --target=browsercorrectly inlines JS-imported assets asdata:URIs.#27821
* Dev server & HMR: rapid successive saves no longer throw "Unknown HMR script".
* Dev server & HMR: multipleimport {}statements from the same barrel no longer fail with "X is not a function".
* Dev server & HMR: CSS rebuilds and file-watching are hardened.
* Sourcemaps:--compile --sourcemap=externalnow writes.mapfiles to disk (one per chunk with--splitting).#27396
* Sourcemaps: comment statements now emit mappings for better debugger accuracy.#27396
* Sourcemaps: a memory leak inBun.build()withsourcemap: 'inline'and nooutdiris fixed.#27396
* Symbol renaming: a named function expression that shadowed an inlined import is now correctly renamed, fixing infinite recursion at runtime in Svelte 5 dev-mode apps.#26027
* Dynamicimport()with{ with: { type: 'text' } }now applies the requested loader during bundling.#28045
* Dynamicimport(): CommonJS chunks from dynamic imports are correctly wrapped with__toESMwhen code splitting is enabled.#26120
* Transpiler correctness: we fixed dozens of fuzzer-found invalid-output cases and hardened the parser. This includes:usingdeclarations insideswitchcasesdecorators on dropped TypeScript membersanonymous decoratedexport default classdeeply nested types and block statements (now throw a clean error)infer ... extendsparsingfor (async of …)reserved-word inferred namesnamespace/enum scope handlingmalformeddeclareblocks
* usingdeclarations insideswitchcases
* decorators on dropped TypeScript members
* anonymous decoratedexport default class
* deeply nested types and block statements (now throw a clean error)
* infer ... extendsparsing
* for (async of …)
* reserved-word inferred names
* namespace/enum scope handling
* malformeddeclareblocks
* Fixedbun build --compileproducing segfaulting Linux binaries when the basebunhad been run throughpatchelf(as NixOS'sautoPatchelfHookdoes): the writablePT_LOADsegment to extend is now selected by vaddr containment of the.bunsection, not table order.
* Fixedbun build --compilemangling..segments in embedded entrypoint paths to_.._, breakingnew Worker()targets that lived above the compile root.#32730
* Fixed non-deterministic output and silently dropped modules when code-splitting through chainedsideEffects: falsebarrel packages (@sentry/node-corere-exporting@sentry/core), which surfaced at runtime asExported binding 'X' needs to refer to a top-level declared variable.#36838
* Fixed HTML entry points writing a shared chunk into<script src>instead of the entry chunk when code splitting was enabled, leaving the page blank with no error.#34113
* An unresolvablerequire()inside acatchblock now emits a runtime throw instead of failing the build, matching the existing handling fortrybodies (fixes bundling packages that probe optional dependencies with try/catch fallbacks).#35659
* JS minifier[x][0]/{f:x}.ffolding no longer breaks optional-chain,this-binding, or assignment-target semantics.#36730
* JS minifierdeleteon constant-folded import identifiers no longer emits invalid output.#36740
* JS minifier!/typeoffolding on array/object/class literals keeps their side effects.#34254
* JS minifierNon-decimal BigInt literals (0xffn,0o7n,0b1n) are no longer constant-folded using their raw source text.#34823
* JS minifierNon-ASCII Unicode identifiers survive the bundler's renaming.#33863
* JS minifierBare$is never picked as a minified name to avoid colliding with jQuery-style globals.#35668
* Unused classes containing private fields/methods are now dropped.#36528#35472#35957
* Classes with side-effectful computed keys are no longer incorrectly tree-shaken.#36528#35472#35957
* TypeScript parserASI applies after contextual keywords before a newline.#34258
* TypeScript parserBlock-scopedenumlowers withletinstead ofvar#34249
* TypeScript parserenum/namespacebodies reject strayyield/await/this/return#34250
* TypeScript parserOptional tuple labels that are type-position keywords parse.#34248
* TypeScript parserasync as T/async satisfies Tparse as casts, not arrow functions.#34246
* TypeScript parserStandard decorator grammar accepts!,#private, andexport @decforms.#34245
* TypeScript parserType-argument lists in expression position require a bare>to close.#34224
* Printer & lexer:export {}is no longer emitted inside unbracedif/while/dobodies (a syntax error).
* Printer & lexer: the JSON printer emits valid escapes for the BEL and VT control characters (U+0007,U+000B).
* Printer & lexer: overflowing or unterminated\u{…}escapes are rejected at parse time.
* @supportsconditions containing newlines keep correct sourcemap line/column tracking.
* url()#fragmentsuffixes (and?queryon the file-loader path) survive asset rewriting.
* color-mix() rejects out-of-range percentages.
* The CSS tokenizer handles non-UTF-8 bytes.
* Minified token lists keep adjacent '/' and '*' delims separated.
* Fixed sourcemap column drift and unsortedmappingssegments on generated lines crossing two or more placeholder substitutions (multiple file-loader imports, or an entry chunk importing from multiple shared chunks).#33860
* Build pipeline:onBeforeParseplugin externals are GC-rooted for the lifetime of the build.
* Build pipeline:--no-macrospropagates to every parse task.
* Build pipeline: an unterminated[placeholderin--entry-naming/--chunk-namingreports an error.
* Build pipeline: a module that fails to print now fails the build instead of emitting truncated output.
* bun build --compile --target=bun-darwin-*validates that--compile-executable-pathpoints at a well-formed Mach-O binary and exits 1 withInvalidObjectotherwise, as malformed ELF and PE bases already did withInvalidElfFileandInvalidPEFile.
* Fixed--compile --bytecode --format=esm --splittingbuilds in which an import from another chunk resolved to a Node builtin instead of the chunk's export. It happened when arequire()d file in that chunk had a tree-shaken import with the same name as the export (import { rm } from "fs/promises"). Minified builds hit this whenever the minifier reused such a name.#37619
* Fixed--compile --bytecode --format=esmbinaries breaking on imports and re-exports of modules left outside the bundle. Examples:export * as ns from "node:fs"threwCannot access 'ns' before initialization;export { readFileSync as rfs } from "node:fs"leftrfsasundefined;import { join } from "node:path"in a file that also assignsmodule.exportsgavejoin is not defined. These builds now behave the same as without--bytecode.#37677
* --public-pathwas composing with the importer-relative chunk path instead of the outdir-relative one, so any chunk in a subdirectory emitted a URL likehttps://cdn.example/app/../../chunk.jsthat escapes the prefix. Code-split apps deployed under a CDN prefix now resolve their chunks and file-loader assets correctly.#33385
* Fixed concurrentbun buildprocesses (as spawned by concurrently or turbo) non-deterministically stalling for ~10 seconds instead of ~10 ms; a thread-pool shutdown race left a worker sleeping until its idle timeout.#32494
* bun build --splittingwith--format=cjsor--format=iifenow fails with a clear "only supported with esm" error instead of panicking;Bun.build()returns the same as a catchable build error.
* Bundled CommonJS dependencies that setmodule.exports = null(or any primitive) no longer crash at load time.
* Top-levelargumentsin bundled CommonJS resolves to the module wrapper's arguments instead of throwingReferenceErrorin ESM output.
* Fixed a local variable namedjsx,jsxDEV,jsxs,Fragment, orcreateElementin the same scope as the first JSX element aliasing the automatic JSX runtime import and causingTypeError: jsx is not a functionat runtime.#32593
* Fixed decorator lowering for class fields whose key is a string literal containing non-ASCII characters; the decorated field previously landed on a garbage property name at runtime.#32713
* CSS:calc()results of NaN serialize as0per CSS Values 4 instead of the invalid literalNaNpx.#33147
* CSS::nth-child(... of <list>)and:has()with an empty selector list are now rejected as invalid instead of emitted.#33151
* CSS: CSS-modulesanimation/animation-namenow scope the referenced@keyframesname to the same hash the definition receives.#33322
* Fixed repeated in-processBun.build()calls failing withEBADFwhen a package is reached through a symlinkednode_modulesentry; the parse task was closing a file descriptor it had borrowed from the resolver cache.#33102

### Other Node.js fixes#

* bun --bun jestruns.require("module").prototypeis non-enumerable, as in Node, so jest no longer fails with "Attempted to assign to readonly property".#39535
* A TCP peer reset behind unread data is reported asECONNRESET, not a cleanend.#39600
* On macOS, a peer reset on a paused socket is reported instead of leaving the socket open forever.#39610
* node:httpno longer writesConnection: closeinto the body onres.destroy().#39364
* node:httpno longer appendsContent-Length: 0to a close-delimited streamed response.#38701
* On Windows,fs.writeFile(path, data, { flag: "a+" })appends instead of overwriting from offset 0.#39355
* N-API: return status codes on error paths now align with Node across a set of entry points — NULL env/out-params returnnapi_invalid_arg, calls with a pending exception returnnapi_pending_exceptionon the entry points Node gates, andnapi_define_properties/freeze/seal/type_tag/element accessors coerce primitives viaToObjectlike Node.
* napi_get_all_property_namesnapi_key_*filters (own-only skip_strings/skip_symbols, and writable/configurable on Proxy and String wrappers) match Node.#34134#34129#34144#34143#34142#34126#34479
* napi_get_all_property_nameshandles accessor properties under everynapi_key_*filter.
* N-API: threadsafe functions stay alive after their env is torn down.
* N-API: threadsafe functions are finalized when the last ref is released after abort.
* N-API: threadsafe functions receiveNULLincall_jswhen no JS function was supplied.
* N-API: pending exceptions are cleared between finalizers during environment cleanup.
* N-API: Async cleanup hook handles stay alive until the addon removes them.
* V8 C++ API:ReturnValuecontents stay alive acrossHandleScopepops.#37159
* V8 C++ API:v8::Value::IsArraymatches V8'sJSArraytype check instead of the specIsArrayoperation, so Proxy-wrapped arrays are no longer treated as arrays and revoked proxies no longer throw.#34149
* node:http2: frame writing over JS-backed transport sockets, paddedDATAframes, re-entrantstreamStartcallbacks, and inboundHEADERSparsing are hardened.
* node:http2: corked frames stay scoped to their own session.
* Destroying a session during the writable flush loop is handled.
* node:http: chunked responses to HTTP/1.0 clients are well-formed.
* node:http: resizableArrayBuffers write correctly under backpressure.
* node:http:'error'ECONNRESETand'close'ordering on aborted request bodies matches Node.
* node:http:req.socketemits'pause'when the body buffer fills.
* node:http: request lines are validated strictly and rejected viaclientError.
* node:http: already-written response bytes are drained when the client half-closes.#35034
* node:http: Unread request body is drained afterres.socket.end().#34356
* node:http: Upgrade sockets emit'close'when the WebSocket peer disconnects.#32737
* node:http:process.binding('http_parser')exposes theM-SEARCHmethod token.#35277
* node:tls:getSession()/getTLSTicket()return the resumable ticket-bearing session on TLS 1.3.#36475#32630
* node:tls: error routing,manualStartreads, handshake timeout, andsetSecureContextedge cases are fixed.#35006#32630
* node:fs:WriteStreamno longer closes its fd before an in-flight write completes.#34803
* node:fs:WriteStream.write()afterdestroy()fails withERR_STREAM_DESTROYEDon the fast path.#34267
* node:fs:ReadStreamno longer leaks its fd on destroy with{ start, autoClose }.#30920
* node:fs:watchFileno longer fires queued callbacks after close.#36926
* node:fs: Recursivefs.watchinotify subtree failures surface as'error'events.#36415
* node:fs:fs.close(0/1/2)actually closes the standard descriptors.#33561
* node:fs:mkdtemp()honorsencoding.#33844
* node:fs:appendFilehonors explicitflag: 'w'.#36553
* node:fs: Non-bigintstatfsno longer truncates to i32.#36503
* node:fs:BigIntStatsreturns correct negative nanosecond values for pre-epoch times.#36187
* node:fs:utimeshandles negative fractional string timestamps.#34701
* node:fs:promises.glob()/promises.watch()validation and event prototypes match Node.#34196#34279
* Readable#pause()is a no-op on already-destroyed streams (matching Node's post-pipe flow state).#33467#34593#34025#34031#37183#32627
* node:events: single listeners are stored bare with copy-on-write arrays (matching Node's internal shape).
* node:events:addAbortListenerfires even when another listener callsstopImmediatePropagation.
* node:events:EventEmitter.listenerCount()validates its emitter argument.
* node:events: aReferenceErrorinlistenerCountis fixed.
* process:'beforeExit'no longer emits after a fatal uncaught exception.#34639
* process:reallyExit()no longer emits'exit'listeners.#34997
* process: Errors thrown inbeforeExit/exitlisteners route to'uncaughtException'.#33466
* process: Throwing'data'listeners on stdin no longer destroy stdin.#34019
* process: File-backed stdout/stderr can be written afterend().#33618
* process: Piped stdout/stderr correctly errors on write-after-end.#33557
* Module resolution: running Bun asnodeno longer auto-loads.envfiles.
* Module resolution: wildcardexports/importstargets auto-resolve extensions.
* Module resolution:"."and".."specifiers are treated as directories.
* Module resolution:Module._nodeModulePathsstrips trailing separators.
* Module resolution:module._resolveFilenamevalidates its argument.
* node:buffer:toString/writehandle buffers ofMAX_LENGTHbytes.
* node:buffer:indexOf/lastIndexOfwith a negative offset and a Buffer (not string) needle underucs2/utf16lewraps against the raw byte length as Node does.
* node:buffer: the internal<encoding>Slice/<encoding>Writebindings match Node's semantics.
* node:dns: pending queries always time out.
* node:dns:resolvethrowsERR_INVALID_ARG_TYPEfor undefinedrrtype.
* node:dns:Resolver/setServers/lookupServicevalidation matches Node.
* node:vm: property definition in sandboxed contexts crash is fixed.
* node:vm:createContextthrows when a context option getter throws.
* Error.captureStackTraceinstalls.stackas non-enumerable (matching V8).#34259
* Error.stackTraceLimitstays in sync with the limit actually used for captures.#34263
* assert.deepEqualthrowsTypeErroron detachedArrayBuffers.#34587
* node:worker_threads: workers no longer hang when captured stdout/stderr is never consumed.#34338
* node:perf_hooks: exports the realperformanceobject with correct entry prototypes.#34518
* node:tty: raw mode is tracked per-handle instead of per-process.#33527
* node:timers: timers reschedule when_idleStartis written, matching Node's internals.#36859
* node:string_decoder: state resets correctly after completing a buffered partial character.#33703
* node:os: fixed IPv6 address, netmask, and CIDR formatting inos.networkInterfaces().#32300
* node:dgram: compatibility improved to match Node v26.3.0 behavior.#32625
* createTagStore()capacity is now coerced like Node (double→int→size_t, so-1means unlimited and0caches nothing).#34454
* Explicit-undefinedoption rejection matches Node's arity-based validation.#34450
* node:http2:request()no longer sends headers out of order when an options getter callsrequest()again; options are now copied before encoding.#31323
* node:vmSyntheticModuleworks together withnode:async_hooks, fixingreact-email's preview server.
* node:httpsnow honorscaand other TLS options passed via theagent.#25937
* Passing a customlookupfunction tonode:http/node:httpsno longer breaks SNI and certificate validation, fixing axios with custom DNS resolution.#25937
* node:httpserver now delivers data pipelined immediately after a CONNECT request to the'connect'event'sheadparameter, fixing CONNECT tunneling from Cloudflare's workerd.#25938
* fs.staton Linux now works inside older Docker containers and locked-down sandboxes that previously blocked the underlying system call.#28825
* fs.cp/fs.cpSyncon Linux and FreeBSD now correctly preserve symlink targets instead of creating links pointing back at the source symlink's own path.#30073
* fs.statfs()on Intel macOS no longer returns field-shifted garbage (bsize: 0), fixing disk-space checks in tools like Unity Hub.#31139
* os.freemem()on Linux now reports the memory that is actually available, matching Node.js, instead of a much smaller number that ignored disk cache the kernel can free on demand.#29080
* process.ppidis now a live getter, so the orphan-detection patternif (process.ppid === 1) process.exit()works after the parent dies.#29171
* Unix domain socket binding now returnsEADDRINUSEinstead of silently unlinking an existing socket and stealing the address.#28798
* The Unix domain socket.sockfile is cleaned up onclose().#28798
* Buffer.copyBytesFrom(view)no longer returns wrong bytes (or throws a spurious out-of-memory error) when the view has a non-zerobyteOffset.#30132
* Dynamicimport()of unknownnode:modules inside CommonJS is now deferred to runtime instead of failing at transpile time, unblocking Next.js + turbopack + Better Auth probing fornode:sqlite.#26981
* node:crypto:createCipheriv()andcreateDecipheriv()reject a GCM IV longer than 128 bytes withERR_CRYPTO_INVALID_IV, as Node does, instead of producing ciphertext Node cannot decrypt.#34092
* node:fs:fs.mkdtemp("")in its sync, callback, and promise forms fails withEINVALlike Node instead of creating a six-character directory in the working directory.#34908
* node:fs:fs.createWriteStream()no longer overwrites the start of the file with the unwritten tail of a short write; it retries at the current offset, and a write that then fails (for exampleEFBIG) emits'error'instead of'finish'.#36135
* node:fs:fs.write,fs.writev, andfs.readvignore apositionthat is not a safe integer (NaN,Infinity,1.5, a BigInt) and use the current offset, matching Node.#36135
* node:fs:fs.writeandfs.writeSyncthrowERR_OUT_OF_RANGEfor anoffsetpast the end of the buffer when nolengthis passed, instead of writing 0 bytes.#37632
* node:dns: on Linux,dns.lookup()now uses the system resolver (getaddrinfo) like Node. Before, it used c-ares, the resolver library Bun bundles. c-ares reads/etc/resolv.confitself. So on hosts using systemd-resolved or a split-DNS VPN, names that Node resolved failed in Bun.dns.promises.lookup()andnet.connect()by hostname are covered.Bun.dns.lookup()still defaults to c-ares on Linux.#37383
* node:dns:dns.lookup()anddns.promises.lookup()treat anullhints,all, orverbatimoption as unset, as Node does, instead of throwingERR_INVALID_ARG_TYPE.#37319
* node:dns:dns.lookupService()resolves IPv4-mapped IPv6 addresses such as::ffff:127.0.0.1instead of failing withENOTFOUND.#37490
* process: the default'warning'printer is registered as a listener at startup, as in Node, soprocess.removeAllListeners("warning")silences it andprocess.emit("warning", err)prints.#37344
* node:http2:session.setNextStreamID(0.5)on a fresh client leaves the next stream ID at1, as in Node, instead of overflowing.
* node:http2:session.state.nextStreamIDno longer reports0when a server session reaches2 ** 32 - 1.
* node:http2: sessions now havegoawayCodeandgoawayLastStreamID, set from a receivedGOAWAYbefore'goaway'is emitted and kept after the session is destroyed. They wereundefined, so agoawayCode !== NGHTTP2_NO_ERRORcheck treated every session as errored.#37550
* node:http2:pushStream()now sends an array header value as one field per element. So"set-cookie": ["c1=1", "c2=2"]arrives as two cookies rather than one comma-joined value. An array (or a duplicate) for a single-value header such ascontent-typethrowsERR_HTTP2_HEADER_SINGLE_VALUE. Both match Node.#37579
* node:net: on Linux, anallowHalfOpensocket (which everynode:httpserver socket is) whoseAF_UNIXpeer closes first emits'end'and closes. A paused socket keeps the bytes it received before the peer closed untilresume(), then ends and closes.
* util.inspect.customon web classes: assigningSymbol.for("nodejs.util.inspect.custom")on aURLinstance in strict-mode code no longer throwsTypeError: Attempted to assign to readonly property. That broke SvelteKit SSR. The prototype property is now writable onURL,URLSearchParams,CryptoKey,BroadcastChannel, and the web stream classes. This matches Node.#38106
* node:worker_threads: a worker'sprocess.stdoutandprocess.stderroutput now all reaches the parent when the worker exits synchronously (process.exit(), an uncaught exception, or an unhandled rejection). Previously everything after the first write was dropped.worker.terminate()still does not flush, as in Node.#38229
* node:worker_threads:process.exitCodeset inside an'exit'listener is now honored, in workers and on the main thread.#38229
* node:net: asynchronousconnectfailures now carry Node's- Local (address:port)suffix when the local address is known, soconnect ECONNREFUSED 127.0.0.1:12399 - Local (127.0.0.1:12400)reads the same as in Node.#34523
* node:console:new Console({ inspectOptions })now honors aMapkeyed by stream, so stdout and stderr can be formatted differently; previously theMapwas treated as a plain options object and per-stream colors did nothing.#34523
* node:v8:v8.setFlagsFromString()now rejects a non-string argument withERR_INVALID_ARG_TYPE, as Node does, before throwingERR_NOT_IMPLEMENTED.#34523
* v8.startupSnapshot.isBuildingSnapshot()now returnsfalseinstead of throwing, unblocking bson (and therefore mongodb and @keyv/mongo) which calls it at import time.#32502
* process.stdinin paused mode no longer drops the final partial chunk at EOF:read(n)returns the buffered remainder once the stream ends, and a bareprocess.stdin.read()with no'readable'listener now delivers data.#33123
* tty.WriteStream#getColorDepth()no longer reports 256 colors for every terminal; TMUX andxterm-kittynow report 24-bit, GitHub Actions and CircleCI report truecolor, and emptyNO_COLORis ignored per no-color.org.#33124
* fs.readdir(path, { recursive: true })no longer silently drops entries whose relative path approachedMAX_PATH_BYTES(~1022 bytes on macOS, ~4094 on Linux); long paths now spill to a heap buffer.
* fs.promises.readdir(path, { recursive: true })completes when multiple per-directory subtasks fail.
* fs.open/openSync/readFile/writeFilenow accept a numericflagsargument that arrived as a double (e.g. read from aFloat64Array), fixing Go programs compiled withGOOS=js GOARCH=wasmwhose syscall bridge delivers every argument that way.#32506
* fs.open()now validates flag and mode strings strictly, rejecting uppercase flags like"W"and non-octal mode strings withERR_INVALID_ARG_VALUEinstead of silently opening the file.#32966
* node:fserrors now report Node's platform-independent operation name inerror.syscall("stat","lstat","utime") instead of the raw syscall Bun issued ("statx","utimensat"), so packages that branch onerr.syscallmatch correctly.#32964
* Abortednode:fsandnode:fs/promisesoperations now reject with anAbortErrorwhosecodeis'ABORT_ERR', matching Node.js.
* On Linux,fs.watch()now emits bothrenameevents with the correct basename when the watched path itself is deleted or moved, matching Node.js.#32962
* node:net'sautoSelectFamily(Happy Eyeballs) path no longer throws an uncaughtTypeError: null is not an objectwhenconnect()fails synchronously, common on macOS when DNS returns unroutable IPv6 addresses.#32660
* node:httptolerates clearedonwritable/ondata/onabortcallback slots on the socket.
* socket.connect()innode:neton a socket that already has a live native handle is handled.
* TLS handshake failures discovered from a write issued beforesecureConnect(ashttps.requestdoes) now report the handshake's own error code instead of being misreported asERR_TLS_CERT_ALTNAME_INVALID.#33390
* X509Certificate.checkHost()now returns the subject name that matched (e.g.*.wildcard.example.com) instead of echoing back the hostname you passed in.#33299
* crypto.createHash()andcrypto.hash()now accept the hyphenated and mixed-case algorithm aliases Node.js accepts ("shake-128","SHAKE256","BLAKE2s256").#32439
* crypto.subtle.wrapKey()withAES-KWand"jwk"format now pads the serialized JWK to a multiple of 8 bytes; previously it threwOperationErrorfor any key whose JWK wasn't already 8-byte-aligned (e.g. HMAC SHA-512).#32616
* cipher.setAAD()on a non-AEAD cipher such asaes-128-cbcthrowsERR_CRYPTO_INVALID_STATE.
* crypto.Hmac's nativeupdate()throwsERR_INVALID_THISwhen called with a wrong receiver.
* Bun'snode:cryptoimplementation now includes upstream correctness fixes from Node.js that tighten error handling in low-level cipher and memory-allocation code paths.#33202
* node:zlibnative handle lifecycle crash fixed, includingdictionaryvalidation inzlib.deflateSync.
* Readable.fromWeb()no longer reorders chunks when composed withReadable.toWeb(); concurrent pump loops on the same reader could interleave and permute the stream.#33300
* child.kill()now returnsfalsewhen the child has already exited, matching Node.js and makingkill(0)usable as a liveness probe.#32877
* process.execve()throws anErrnoExceptionwhen the underlying syscall fails (ENOENT,EACCES), and restores file-descriptor flags and the signal mask on failure.
* process.hrtime([a, b])coerces tuple elements withToNumberlike Node.js.
* dgram.Socketmethods called afterclose()now throwERR_SOCKET_DGRAM_NOT_RUNNINGinstead of an uncoded internalTypeError.#33024
* dgram.Socket[Symbol.asyncDispose]()on a closed socket resolves instead of rejecting.#33024
* dgram.Socket.prototype.bind()on an already-bound socket now throwsERR_SOCKET_ALREADY_BOUNDsynchronously instead of emitting an'error'event.#33037
* Buffer.alloc(n, pattern, enc)andbuf.fill(pattern, enc)now byte-truncate the pattern's encoding when it's longer than the destination.#33019
* Buffer.alloc(n, pattern, enc)andbuf.fill(pattern, enc): lone high surrogates encode as U+FFFD instead of throwing.#33019
* Buffer.prototype.fillnow matches Node's offset/end handling: string offsets on non-string values throwERR_INVALID_ARG_TYPE, an undefined offset ignores end, and a null or empty-string encoding is treated as utf8.#33033
* Buffer.from(arrayBuffer, byteOffset, length)now clamps negative and NaN lengths to 0 instead of throwing.#33036
* Buffer.from(arrayBuffer, byteOffset, length)honors an explicit length on resizable ArrayBuffers instead of always returning a length-tracking view.#33036
* structuredClone, workerpostMessage, and theWorkertransferListoption now validate the transfer list per WebIDL before serializing, throwingTypeErroron invalid entries instead of silently detaching the valid buffers.#32809
* path.normalize()andpath.join()now correctly handle a first segment ending in..(such as"bb../../x"), matching Node.js.#32783
* new StringDecoder(enc).encodingandReadable#readableEncodingnow normalize all UTF-16LE aliases (ucs2,ucs-2,utf-16le) to"utf16le".#33038
* napi_is_arraybuffernow returnsfalseforSharedArrayBuffer, matching Node.js.#32629
* navigator.userAgent,navigator.platform, andnavigator.hardwareConcurrencyare now read-only accessors instead of writable data properties, matching Node.js and browsers.#32440
* queueMicrotask.lengthnow reports 1 instead of 2, matching the HTML spec, browsers, and Node.js.#32419
* Callingsocket.destroySoon()orsocket.destroy()on a TLS socket after a large write could drop the tail of the stream while still signaling a clean close, so the receiver saw a short read with no error. Pending encrypted bytes are now flushed before the socket closes.#32719
* fs.write,fs.writeSync, andfilehandle.writenow apply the encoding argument when writing a string. Previously the encoding was parsed and then ignored, sofs.writeSync(fd, "abc", 0, "utf16le")silently wrote UTF-8 bytes.#32813
* fs.writeFileandfs.writeFileSyncno longer truncate files opened with a non-truncating flag (r+,rs+, or numericO_RDWR), which is the documented way to patch a region in place.#33355
* fs.writeFileandfs.writeFileSync: Also fixed:flag: "a"on Linux leaving a hole of zeroes before the appended data.#33355
* fs.writeFileandfs.writeFileSync: Also fixed: partial-write failures leaving the old file's stale tail behind the bytes that did land.#33355
* tls.connect({ socket })andnew TLSSocket(socket)work when both ends of an in-processduplexPair()are wrapped in TLS.
* socket.end()sendsclose_notifybefore FIN so the peer sees a clean shutdown.
* A handshake rejected by certificate verification fails closed on every code path.

### Other package manager fixes#

* bun outdatedandbun update -iexit 1 with the error when a manifest cannot be fetched, instead of printing an empty table and exit 0.#38809
* Credentials in a registry URL are sent asAuthorization, whether the URL comes from--registry,BUN_CONFIG_REGISTRY,npm_config_registry, or a bunfigregistry = { url }object. Bun 1.3 dropped them.#38796#38824
* A git dependency is cloned into a staging directory and moved into the cache only when the clone completes, so a killed install no longer leaves a half-cloned package that later resolves as valid.#38269
* bun patchworks for git and tarball dependencies.#38269
* bun pm packnow always includes files referenced by"bin"and"directories.bin"in the tarball even when they aren't listed in"files", matching npm.#23606
* bun pm packandbun publishnow re-readpackage.jsonafterprepublishOnly,prepack, andpreparerun, so version bumps made by lifecycle scripts land in the tarball filename and registry metadata.#26267
* .npmrcparsingnow expands environment variables inside quoted values.#25518
* .npmrcparsingsupports npm's${VAR?}optional modifier.#25518
* .npmrcparsingreads theemailfield for registries (like Sonatype Nexus) that require it.#25518
* --frozen-lockfilenow respects scope-specific registries frombunfig.tomlwhen the lockfile entry has an empty registry URL.#26047
* Optional peer dependenciesnow resolve to an installed package when one is available instead of being left unresolved, fixing duplicated packages undernode_modules/.bunin monorepos.#24272
* Lockfile migrationfrom npm/yarn/pnpm now creates the text-basedbun.lockinstead of the legacy binarybun.lockbwhen migration fails partway through.#24494
* Git dependenciesthat point to the same repository via different protocols (git+ssh://vsgit+https://) now resolve correctly.#24138
* Git dependencies: GitHub URLs with custom protocol prefixes take the faster tarball path instead of a full clone.#24138
* The security scannernow collects dependencies from all workspace packages, not just the root.#24942
* The security scanner: every scanner failure path now prints a diagnostic instead of exiting silently with code 1.#24942
* The isolated linkerfails fast on integrity-check failures and error tarball responses.
* The isolated linker: Cross-filesystem installs now fall back to copying instead of hardlinking.
* The isolated linker: workspace packages get their self-link when they depend on themselves.
* bunx @scope/namealways resolves the scoped package it names.
* Rare crashes inbun install,bun add,bun pm ls,bun pm patch, andbun update --interactiveare fixed, including registry request retries,.npmrccacert handling, local tarball resolution, git specifier parsing, package names, and lifecycle script filtering.
* Better error messageswhen afile:dependency points at a missing or stale path:bun installnow names the offending dependency instead of suggesting you runbun init.#26339
* bun initnow falls back to-ywhen stdin isn't a TTY.#35165
* bun update -inow errors out early (pointing tobun update/bun outdated) instead of hanging.#34858
* bun installnow falls back to copying when hardlinking from the cache fails withEACCES/EPERM.#36853
* postinstallnow runs when Bun auto-injectsnode-gyp rebuildfor a package with abinding.gypbut noinstallorpreinstallscript; previously the postinstall was silently dropped.
* bun.lockno longer keeps packages that are only reachable through an optional peer dependency's resolution slot.#35681
* bun patch --commitnow resolves paths correctly when run from inside a workspace package.#36290
* Isolated installs no longer re-apply the same patch once per peer-dependency variant.#33646
* --frozen-lockfileno longer spuriously rejects a lockfile whennpm:aliases place duplicate package names in one tree node.#36578
* npm:alias dependencieswhose registry target name collides with a same-named alias elsewhere in the tree now resolve to the package they name instead of being redirected to the alias — fixing Microsoft's recommended TypeScript 6/7 coexistence setup.#33835
* A tarball whose download already failed during resolution is no longer re-downloaded (and re-reported) during the install phase.#34861#34103
* Nestedbun run --bunno longer creates a self-referencingnodeshim symlink and fails withToo many levels of symbolic links.#30713
* Bun.semver.satisfies()no longer collapses^/~/x-range/hyphen ranges to an empty range when a version component isu64::MAX.#34600
* BUN_DISABLE_SLOW_FILESYSTEM_WARNING=1suppresses the "slow filesystem detected" notice.#37000
* Git,github:, and tarball dependencies:bun installfrom a lockfile with a cold cache now installs every git dependency that points at a different branch of the same repository (previously it installed one and exited 0).#35426
* Git,github:, and tarball dependencies: a git,github:, or tarball dependency that appears both directly and transitively no longer fails withfailed to resolve.#35426
* Git,github:, and tarball dependencies:git+file://dependencies install instead of failing withno commit matching.#35426
* $HOME/.npmrcis now read whenXDG_CONFIG_HOMEis set but$XDG_CONFIG_HOME/.npmrcdoes not exist, as on GitHub Actionsubuntu-latest. Previouslybun publishthere failed withmissing authenticationandbun installignored the registry configured in$HOME/.npmrc.#36289
* --frozen-lockfileno longer fails withlockfile had changeson an unchangedbun.lockwhen a root dependency satisfies a bundled package's optional peer (cdk8sbundlesfollow-redirects, whose optional peerdebugis also a root dependency).#37350
* Long version labels(a tarball orfile:spec, or a workspace's own version) are handled by the hoisted linker.
* Long version labels: apatchedDependenciesentry keyed by one is applied.
* Long version labels:bun patchandbun patch --commithandle long labels and report an error where the package cannot be patched.
* workspacesentrieswhose resolved path is longer than the platform path limit makebun installexit 1 withENAMETOOLONG; the same applies to a glob match whosepackage.jsonpath is too long. Over-long glob patterns match or are skipped like any other.

### Bun.serve()#

* Bun.serveHEAD and 204 responsesare framed per RFC 9110/9112: HEAD returns the same headers GET would, 204 responses no longer carryContent-Length: 0, and static routes with a null-body status no longer put body bytes on the wire.#32800
* Bun.serveper-method routes({ GET: handler }) now answer HEAD requests using the GET handler instead of falling through to the next route or returning 404.#32822
* Bun.serveHTML routes in productionnow inlineimport.meta.env.*(fixing a runtimeTypeErrorin the browser).#32854
* Bun.serveHTML routes in productionemit correctly quotedETagandCache-Controlheaders on bundled assets.#32854
* Bun.serveerror handlererror()is no longer re-invoked after the status line is committed.
* Bun.serveerror handlernullrejection reasons are passed through verbatim.
* Bun.serveerror handlerA streaming body returned fromerror()keeps the request alive.
* Bun.serveerror handlerHEAD requests on error paths no longer receive a body.
* Bun.serveerror handlerAborted uploads are handled cleanly while areq.body.tee()branch is being read.
* Bun.serveerror handlerA streamcancel()that throws when a peer aborts a streamingResponseno longer surfaces as an unhandled rejection.
* Bun.serveerror handlerThe development error page shows stack traces and source lines again.
* Bun.serve()server.stop()closes idle keep-alive connections.
* Bun.serve()A handler response withConnection: closecloses the connection.
* Bun.serve()req.url/req.headersremain populated afterserver.upgrade().
* Bun.serve()server.upgrade()now validates the WebSocket opening handshake before accepting.
* Bun.serve()ServerWebSocket.send(blob)sends the Blob's bytes instead of"[object Blob]"
* Bun.serve()TCP backpressure applies when a handler reads the request body slowly.
* Bun.serve()FIFO/pipe file bodies stream with chunked encoding instead ofContent-Length: 0
* Bun.serve()ReadableStreamresponse bodies are cancelled for HEAD requests.
* Bun.serve()Per-serverNameSNI TLS entries honorrequestCert/rejectUnauthorized
* Bun.serve()Routes set tofalsereturn 404 when nofetchhandler is configured.
* Bun.serve()Static routes no longer emit a duplicateDateheader.
* Bun.serve()HTTP/3 responses includeDate.
* Bun.serve()HTTP/3 responses sendCONNECTION_CLOSEwhen an idle connection is stopped abruptly.
* Bun.serve()Server callbacks are GC-traced instead of strongly rooted.
* Bun.serve(): returning aResponsewhose body was already used, or whose status is outside 100–999 (includingResponse.error()), now routes through theerror()handler instead of sending an empty 200 or a malformedHTTP/1.1 0status line.#33118#33400
* Bun.serve(): static routes keep theirContent-Typewhen the sameResponseis registered on multiple paths or afterreload().#33404
* Bun.servenow prints the "Expected a Response object, but received …" diagnostic when a synchronousfetchhandler returns a non-Response value, matching what the async path already did.#33120
* Bun.serve()andBun.listen()now throw whenepoll_ctl(EPOLL_CTL_ADD)fails (e.g.fs.epoll.max_user_watchesexhausted) instead of returning a server that silently never accepts connections.#32706
* Bun.serve()andBun.listen(): Accepted sockets that fail registration are now closed so peers see RST instead of a hung connection.#32706
* Bun.serve()on Linux: now setsTCP_DEFER_ACCEPT(andSO_ACCEPTFILTERon FreeBSD), letting the kernel hold new connections until data arrives. This collapses an extra epoll round-trip per accepted connection.
* Bun.servecaps chunk-extension bytes per chunk and responds413, matchingnode:httpand llhttp.
* Bun.serverejects aTransfer-Encodingheader naming any coding other than a single trailingchunkedwith400 Bad Request.
* Bun.serveanswers an HTTP/1.0 request that carries aTransfer-Encodingheader with400 Bad Request, per RFC 9112.node:httpstill accepts the request and then closes the connection, as Node does.
* Bun.serveWebSocketpublish()now delivers to subscribers when called from a socket that has never itself subscribed.#32879
* Bun.serveWebSocketpublish(): messages queued in the same tick are delivered before a subscriber's lastunsubscribe()frees it.#32852
* server.publish()andws.publish()now return0(dropped) or-1(backpressure) when subscribers are over their buffer limit, honoring the same contract asws.send().#32889
* ServerWebSocket.cork(callback)now passes the WebSocket as the callback's first argument, as documented; previously the argument wasundefined.#32438
* ServerWebSocketsubscribe()/unsubscribe()returnfalseon a closed socket instead oftrue.#36930#36790#35236#32746
* WebSocket#close()now throwsInvalidAccessErrorfor invalid close codes andSyntaxErrorfor reasons over 123 UTF-8 bytes.#32820
* Bun.serve's WebSocket server now closes the connection when a client sends unmasked data, which the WebSocket spec requires servers to reject.#32820
* Bun.serveno longer truncates responses from atype: "direct"ReadableStreamwhosepull()returns synchronously but writes more data later via a captured controller. Previously the response ended after the first synchronous flush. This fixes React 19'srenderToReadableStream(thereact-dom/server.bunbuild), which was closing after the shell and aborting the render.
* Bun.serve(): an over-long bracketed IPv6hostnamethrows a validation error.
* Bun.serveHTML routes: fixed a crash whenserver.stop()was called while a route was still bundling indevelopment: falsemode.stop()now waits for the build, which counts as one pending request.
* Bun.servehandles a client aborting a streamingResponsewhile the socket is under write backpressure.
* Bun.serve()GC pacing:the per-tick heap sampler is replaced with an idle-only timer. The old sampler self-perpetuated ~62 eden collections per second regardless of allocation rate; a 150 rps server with a 300 MB live heap was spending up to ~40% of wall time in GC.
* Bun.serve()backpressure drain: the uWSBackPressurebuffer is now a cursor-tracked slab soerase()is a pointer bump; a full drain no longermemmoves and reallocs the remaining bytes ~32 times.#34824
* Bun.serve(): fixed a per-request memory leak when returning a directReadableStreamthat drains synchronously.#29877
* Bun.serve(): passingBun.file()ascert/key/cano longer leaks one buffer per config parse.
* Fixedreq.text()inBun.serve()throwingTypeError: undefined is not a functionin certain cases.
* Fixed a file descriptor leak inBun.servestatic file routes.
* Bun.serve()WebSocket:perMessageDeflate: { decompress: "dedicated" }no longer drops browsers and ws clients after their second compressed message
* Bun.serve()WebSocket: a control or continuation frame with the compression flag set is now rejected
* Bun.servefile responses on macOS use the buffered read/write path instead ofsendfile(2), working around a Darwin XNU kernel bug.
* Bun.listen/Bun.connect: fixed callbacks being garbage-collected while the socket was still alive.
* Bun.listen/Bun.connect: fixed a crash when a socket close handler closes a sibling in the same group.
* Bun.listen/Bun.connect: sockets retry onENOBUFS/ENOMEMinstead of treating them as fatal.
* Bun.listen/Bun.connect: unhandled pending exceptions from connect-promise or TLS-session callbacks are now surfaced.
* Bun.serve()route objects accept aResponsedirectly under an HTTP-method key.
* Duplicate HTTP headersonfetch()responses andBun.serverequests are now combined with", "per the Fetch spec instead of silently keeping only the last value;Set-Cookiecontinues to return separate values.#31734
* HTML bundlingFavicons,<link rel="manifest">, and other URL-referenced assets now appear in the manifestfilesarray (no more 404s fromBun.serve())
* node:tls:socket.write()from inside a server'sALPNCallbackorSNICallbackno longer fails the handshake (the client sawTLSV1_ALERT_INTERNAL_ERROR); the bytes go out once the handshake completes. From insideBun.listen()'salpnCallbackandserverNamehooks, the same write returns0anddrainfires after the handshake, like any other write made before the handshake.#37675
* HTTPBun.serveandnode:httpapply stricter chunkedTransfer-Encodingparsing (HEXDIG-only sizes, 64-bit chunk sizes, a cap on chunk-extension bytes, and rejection of any coding besides a single trailingchunkedand ofTransfer-Encodingon HTTP/1.0 requests)

### Bun.$(shell)#

* Bun.$(shell)mvfalls back to copy+unlink across filesystems.
* Bun.$(shell)Barecdchanges to$HOME
* Bun.$(shell)Comma-less brace groups like{abc}are literals and nested groups keep trailing empty variants.
* Bun.$(shell)A redirect target that expands to multiple words is an error.
* Bun.$(shell)Redirects to FIFOs use the pollable writer path.
* Bun.$(shell)Redirecting an empty buffer to stdin delivers EOF instead of hanging.
* Bun.$(shell)rmno longer hangs on a lost wakeup between directory tasks.
* Bun.$(shell)new $.Shell()inherits env/cwd/throws defaults.
* Bun.$(shell)$.escapeno longer corrupts Latin-1 characters.#36338#34822#34856#34865#34324#34696#33994#34032#36409#32933
* Bun.$(shell)$.escapeno longer drops empty-string arguments.#36338#34822#34856#34865#34324#34696#33994#34032#36409#32933
* Bun.$builtins.quiet()accepts a boolean.
* Bun.$builtinsls -lprints a real long listing.
* Bun.$builtinsechosupports-e/-E
* Bun.$builtinsEmpty-string arguments are no longer dropped (sossh-keygen -N ""works)
* Bun.$builtins[[ -f ]]only matches regular files.
* Bun.$builtinsGlobbing into a nonexistent directory reportsno matches foundinstead of aborting the process..
* The buffered pipe writer used byBun.$andspawnstdin stays alive across async write completions on Windows.
* Bun Shell handlesepoll_ctlfailures during poll-driven pipe reads.
* Bun Shell handles synchronous redirect write failures such asENOSPCgracefully.
* Shell completions forbun runno longer hide standalone scripts whose names start withpreorpost, so prettier, postgres, postcss, andpreviewnow tab-complete correctly.#30088
* bun run --elide-linesis now a silent no-op when stdout isn't a TTY, so the same script works in both interactive shells and git hooks.#28977
* Fish shell completions now includebun updateand its flags.#25978
* Bun.spawn()andBun.$: fixed a leak of the writer that feeds aBufferorBlobstdinto the child when the child closed its stdin before the buffer had drained (typicallyEPIPE). This affected the shell's< ${buffer}redirect on every POSIX platform andBun.spawn()on macOS; on LinuxBun.spawn()passes the buffer as a memfd instead, so it only leaked where memfd was unavailable.#37774
* Windows dirfd-relative opens:~22 µs → 12–15 µs per callfor common path shapes (~17 µs for relatives that resolve above the directory handle; bare names stay a ~10 ns passthrough). TheNtCreateFileobject name is built from the NT device path directly, skipping the mount-manager IOCTL that drive-letter lookup costs. Applies to tarball extraction, dirfd-relativenode:fs, and shell file ops.
* Bun's crash handler now re-raises the original fault signal (SIGSEGV, SIGBUS, SIGFPE), or SIGABRT for panics, instead of always terminating with SIGILL, so shells and orchestrators see the real crash cause instead of "Illegal instruction".
* Injection:Bun.spawn(),Bun.spawnSync(), and Bun Shell reject NUL bytes in arguments, environment variables,argv0, andcwd.
* Injection:Bun.sqlrejects NUL bytes in connection parameters.
* Injection:Bun.s3rejects CR/LF incontentDisposition,contentEncoding, andtype.
* Injection:node:dnsrejects hostnames with embedded NUL bytes.
* Injection: Bun Shell treats glob metacharacters arriving through interpolation as literals and keeps its internal delimiter out of reach of interpolated strings.
* Injection:vm.createContext(DONT_CONTEXTIFY)sandboxes get their ownObject.prototype.
* File handles that Bun duplicates internally (forBun.file(fd).stream(), afetch()body made fromBun.file(fd), aFileSinkon an fd, andBun.$subshells and pipelines) are created non-inheritable on Windows, as they already were on POSIX viaF_DUPFD_CLOEXEC.
* Bun.$: pipeline write failures other thanEPIPEare handled.
* Bun.$:rmno longer leaks when the directory-read loop aborts with child tasks already queued.
* Bun.$: spawn-time pipe failures are handled.
* Bun.$: multiple parse errors inShellError.messageare separated by newlines.
* Bun.$: the interpreter no longer leaks when finalized with subprocesses still running.
* Bun.$:ls -a -Arespects flag order (last one wins).
* Bun.$: theyesbuiltin works when its stdout is captured.

### Bun.sql#

* Bun.sql: a result column named""(for exampleselect ''on MySQL or MariaDB) no longer crashes the process.#38143
* Bun.sql(MySQL): JSON columns from MariaDB parse into objects via extended-type-info negotiation.#37130
* Bun.sql(MySQL): column-count and structure mismatches are asserted instead of silently dropping values.#36554
* Bun.sql(MySQL): prepared statements assignedstatement_id0 by the server are rejected instead of silently misbehaving.#33238
* Bun.sql(Postgres): fixed memory leaks in array-typed columns and failed connections.
* Bun.sql(Postgres): binaryNUMERICvalues smaller than 1e-8 decode correctly.
* Bun.sql(Postgres): queries exceeding the 65,535-parameter wire limit throwERR_POSTGRES_TOO_MANY_PARAMETERS.
* Bun.sql(Postgres): multi-statement simple queries return the correct column names per result set.
* Bun.sql(MySQL)SELECTno longer silently returns zero rows against StarRocks, TiDB, and SingleStore.
* Bun.sql(MySQL)Memory usage stays flat across thousands of queries (column-name and prepared-statement buffers are now freed)
* Bun.sql(MySQL)DATETIME/TIMESTAMPround-trip as UTC.
* Bun.sql(MySQL)YEARand computedDECIMALcolumns decode correctly.
* Bun.sql(MySQL)BINARY/VARBINARY/BLOB returnBufferwhile binary-collated VARCHAR returnsstring
* Bun.sql(MySQL).raw()no longer includes stray protocol bytes at the start of each value.
* Bun.sql(MySQL)A hang involving stored procedures and multi-statement queries has been fixed.
* Bun.sql(MySQL)Idle connections no longer hold the event loop open or spike CPU to 100% over TLS..#28005#28633#31212
* Bun.sql(pool & helpers)Thesql({...})INSERT helper omitsundefinedso columns fall back to theirDEFAULT
* Bun.sql(pool & helpers)Throwing insideonconnect/oncloseno longer hangs the pool.
* Bun.sql(pool & helpers)sql.close({ timeout: 0 })resolves during a half-open handshake.
* Bun.sql(pool & helpers)NewERR_*_CONNECTION_FAILEDcodes distinguish "never connected" from "connection dropped"..#25830
* Bun.sql(Postgres) could silently deliver one query's rows to a different query when a simple-protocol query ran concurrently with a not-yet-prepared parameterized query on the same connection. Simple-protocol queries include.simple(), parameter-lesssql.unsafe(), and theBEGIN/COMMIT/ROLLBACKthatsql.begin()issues. Bun was sending a redundant protocol message that pushed its reply queue out of step with the server.#32772
* JSON serialization:~3x fasteracross IPC,console.log('%j'), PostgreSQL/MySQL JSON columns, and Jest format specifiers. These paths now hit JavaScriptCore's SIMD-optimized FastStringifier instead of the slow path.
* TLSHostname matching is one implementation acrossfetch(),WebSocket,Bun.connect,Bun.sql, andX509Certificate#checkHost, aligned withtls.checkServerIdentity
* Native memory: edge cases involving bounds and lifetime checks inBuffer(concat,compare,indexOf/lastIndexOf/includes),crypto.randomFill,TextDecoder.decode,Bun.udpSocketsend/sendMany,node:zlib, structured-clone deserialization (bun:jsc,node:v8, advanced IPC),node:fspath handling and Windows path normalization, generated native-class setters called with a foreign receiver, the.npmrcINI parser, and the Postgres and MySQL wire parsers have been fixed
* Bun.sql(Postgres): connection parameters are validated and reject null bytes withERR_INVALID_ARG_TYPE.
* Bun.sql(Postgres): a synchronous validation error on an idle pooled connection no longer wedges the event loop keep-alive and prevents exit.
* Bun.sql(Postgres): backend message framing is validated.
* Bun.sql(Postgres): connection-failure messages are handled regardless of how they arrive across TCP reads.
* Bun.sql(MySQL):caching_sha2_passwordfast authentication against MySQL 8 now works instead of falling back to full authentication on every connect.#33179
* Bun.sql(MySQL): binary-protocolNULLon digit-named columns lands at the column's numeric name instead of index0.#32367
* Bun.sql(Postgres):'infinity'::date/timestampvalues decode to±Infinityinstead of invalid dates.#35121
* Bun.sql(Postgres):DateStyle=ISOis pinned on connect so a server default can't corrupt date parsing.#35112
* Bun.sql(Postgres): the wire-protocol parser enforces message-length frame boundaries and boundsDataRow/RowDescriptionreads.#35114#34436
* Bun.sql(Postgres): out-of-range digit words are rejected when decoding binaryNUMERIC.#34429

### Bun.spawn()#

* AbortSignal.timeout()now fires even if nothing is observing the signal when the deadline arrives, as in Node and browsers. Previously, removing the last abort listener, clearingonabort, closing anfs.watch()watcher the signal was passed to, or aBun.spawn()child exiting cancelled the timer, soabortedstayedfalseand listeners attached later never fired.
* Bun.spawn(): relative$PATHentries are resolved against thecwdoption.
* Bun.spawn(): the parent's cwd is inherited when nocwdis given.
* Bun.spawn(): an already-abortedsignalthrowsAbortErrorimmediately instead of spawning.
* Bun.spawn():timeout: NaNandkillSignal: 0are rejected with a validation error.
* Bun.spawn(): extra stdio file descriptors exposed via.stdioare no longer double-closed.
* Bun.spawn(): caller-supplied file descriptors are returned fromproc.stdio[N]instead ofnull.#29629
* Bun.spawnkeeps the subprocessstdout/stderrreader alive while its pipe poll is armed.
* ABun.spawnstdout/stderrstream reader can be cancelled from inside its own read callback.
* Bun.spawn({ stdin: readableStream })no longer surfaces an unhandledEPIPErejection when the child exits while the internal stdin pump still has a write in flight.#33021
* node:child_process: stdinEPIPEemits'error'and destroys the stream.
* node:child_process: the abort listener onoptions.signalis no longer leaked when spawn fails.
* node:child_process:stdio: 'overlapped'string shorthand is accepted.
* node:child_process:spawn()ignoresoptions.encoding.
* node:child_process:subprocess.stdinstaysnullafter exit when stdio wasn't piped.
* child_processmaxBuffernow stops reading and closes the pipe when the limit is hit instead of continuing to drain everything the child writes before it dies; stdout/stderr overshoot is bounded to at most 64 KB past the limit, matching Node.js.#33309#33330
* spawnSync()now forwards thedetachedoption, so the child gets its own process group as documented.#32874
* spawn()withstdio: 'ignore'at fd ≥ 3 now leaves that descriptor closed in the child instead of opening/dev/null, matching Node.js.#32892
* node:child_process: pipedstdout/stderrnow apply kernel backpressure instead of buffering unbounded in memory.#34971
* node:child_process:child.stdout.pause()is honored after the stream has started flowing.#36035
* node:child_process:spawnSyncdrains piped stdio to EOF after the child exits.#33832
* Fixed Python asyncio-based subprocesses (including all Python MCP servers) breaking underBun.spawn: Bun was prematurely signaling end-of-stream on the child's stdio pipes, which asyncio read as "connection closed".#27435
* A rare bug causing silent data loss when reading subprocess pipes on Windows is fixed.
* FixedBun.spawnSync({ timeout })on Windows firing the timeout immediately if its isolated event loop had been idle longer than the timeout value; libuv's cached loop clock is now refreshed before arming the timer.#33935
* A failedBun.spawn()(e.g.ENOENT) on Windows leaves later spawn calls unaffected.
* Pausing and resuming a pipe from inside its own read callback (the pathchild_processstdio backpressure takes) is safe on Windows, via a libuv upgrade.
* Bun.spawn():Bun.file(path)andBun.file(fd)work atstdio[3]and higher.
* Bun.spawn(): on Windows, an async-iterablestdincompletes after the child exits.
* Bun.spawn():maxBufferstays enforced after the.stdout/.stderrstream getters are accessed.#34349
* Bun.spawn(): stdout/stderr pipes are closed after a timeout kill so buffered reads don't hang.#35012
* Bun.spawn(): Windows child processes can now setCREATE_BREAKAWAY_FROM_JOBunder Bun's no-orphans job object.#36414

### Web Streams#

* Response.clone()andRequest.clone()no longer lock the original body'sReadableStreamwhen.bodywas accessed before cloning. Both the original and the clone remain independently readable, per the Fetch spec.#25484
* type: "direct"ReadableStreamsnow deliver bytes written after aflush()insidepull()topipeTo(),pipeThrough(),tee(),for await, andResponse#textStream(); previously those consumers stopped at the flush, whiletext()and a plain reader were unaffected.#37692
* type: "direct"ReadableStreams: apull()that throws synchronously no longer also reports a strayunhandledRejection.#37692
* ReadableStream({ type: "direct" })serializespull()calls on the JS reader path.#33782
* FileSink.write()under backpressure resolves to the correct byte count for that chunk.#33538
* FileSinkteardown in Windows standalone executables no longer captures diagnostic backtraces, which had also taken a process-wide dbghelp lock on everyFileSinkdestruction.
* console.log(ReadableStream)and other Web/DOM constructors now print[class ReadableStream]instead of[class Function].#29229
* FileSink.write()now returnsnumber | Promise<number>
* Removed the non-existent.formData()/.arrayBuffer()methods fromReadableStream
* fetch()with a streamed request body frames empty chunks correctly on the wire.
* fetch()with a streamed request body keeps the connection out of the keep-alive pool until the upload has finished.
* fetch()with a streamed request body completes uploads sent with an explicitContent-Lengththat yield empty chunks.
* FixedBuildArtifact.prototype.stream()returning the artifact's.kindstring instead of aReadableStreamafter any cached getter was read, a regression from December 2023.#33144
* Readable.fromWeb()now propagates the underlying web stream's error to the Readable's'error'event instead of surfacing an unhandled rejection.#32863
* stream.finished()accepts WHATWGReadableStreamandWritableStream.#32863
* Cancelled streamingfetch()bodiesnever freed theReadableStream, its Promises, andUint8Arraybuffers, leaking~260 KB per cancelled request. Cancel now propagates back to the underlying HTTP request and releases the stream immediately.#27191
* NativeReadableStreamsourcesreuse the same buffer across reads until it actually fills, instead of allocating a fresh one on every pull; this sharply reduces memory commit on Windows.
* ReadableStreamnative sinks: long-lived closures stored on native sinks and controllers are now bound top-level helpers, so they no longer keep their parent function's entire lexical environment alive.#32656
* Fixednew TransformStream()never being garbage-collected unless explicitly closed;for (;;) new TransformStream()would OOM.#29891
* An error thrown inside aReadableStreamused as aResponsebody is reported and the connection is aborted. A stream that errors mid-body force-closes the socket instead of ending the response cleanly.
* ReadableStream.pipeTo(): drains already-queued chunks in place when the destination has capacity, making pipes to aWritableStreamwithhighWaterMark > 1up to 12% faster and avoiding a promise allocation per chunk.#33329
* FileSink: pendingwrite()promises are settled on every synchronousclose()/end()path.#35365
* FileSink: pendingwrite()promises are rejected when a deferred auto-flush hitsEPIPE.#35278
* FileSink: pendingwrite()promises are rejected (not double-reported) whenend()fails.#35344
* FileSink: buffered writes are flushed whenprocess.exit()is called in the same tick.#36250
* Web Streams:.bytes()/.arrayBuffer()on a single-chunk stream return a copy.
* Web Streams: direct-controllerwrite()/close()no-op instead of throwing after the stream is closed.
* Web Streams: the direct controller marks closed on cancel.
* Web Streams:Response.textStream()over a native fetch body decodes multi-byte characters split across any number of chunks.
* Web Streams: aReadableStream's underlying source is released to GC as soon as the stream reaches a terminal state.#36666
* Web Streams:Request/Response.bodyno longer holds a strong GC reference to the stream after the wrapper owns it.#36624
* Web Streams: body-producer hooks are freed once the body is realized as a stream.#36809
* Web Streams: native sinks release their backing buffer onclose().#36785
* @types/bunnow includes thewait?: booleanparameter onReadableStreamDirectController.flush(), and thetype: "direct"backpressure contract is documented:write()returns a negative number under backpressure, andawait flush(true)waits for the sink to drain.#32640

### WebSocketclient#

* The WebSocket clientnow closes with a protocol error when the server sets the permessage-deflate compression flag mid-message, instead of silently delivering the malformed data, matching browsers and Node's ws.#33395
* WebSocketclose eventsnow report the correctCloseEvent.codeandwasClean: a bodyless server close reports1005(not1000), a received1001is no longer remapped, andwasCleanistruefor clean server-initiated closes.#31518
* new WebSocket("wss://...", { proxy }): large bursts of incoming frames are processed correctly while a write happens concurrently (an automatic pong, orsend()fromonmessage). The bug showed up on busy long-lived connections. The same fix stopstls.connect({ socket })from firing the next'data'event from inside a'data'handler that callswrite().#37467
* wss://through an HTTPCONNECTproxyno longer loses the connection when theopenhandler spins the event loop (for exampleexpect(...).resolvesinbun:test). Previously the socket stayedOPENforever without ever firingmessageorclose.#37610
* WebSocket#terminate()on awss://connectionwhose peer has stopped responding now firesclosewith code1006. Previously the socket stayed inCLOSINGforever, waiting for a TLSclose_notifythe peer never sent, while the same call onws://closed immediately.close()still sends the Close frame before tearing down the connection.#38243
* fetch()andWebSocketaccept aURLinstance for theproxyoption andproxy.url.#33648#33641
* Fixed a re-entrancy bug in WebSocket client when calling certain functions inside amessagehandler during a multi-frame read
* Fixed the WebSocket client dropping and reallocating its receive buffer after every fragmented message, and a related head-offset bug that could truncate a later payload; the 2 KB preallocation is now retained across messages as in 1.3.#32356
* Parsers and decoders: the JSON/JSONC parser and CSS minifier are bounded on deeply nested or fan-out-heavy input and raise a catchable error.
* Parsers and decoders: the WebSocket client enforces a maximum decompressed message size forpermessage-deflate.
* Parsers and decoders: the WebSocket client verifiesSec-WebSocket-Accept.
* Parsers and decoders: the Redis/Valkey RESP parser caps aggregate nesting depth.
* Fixed the WebSocket client rejecting the upgrade withInvalid responsewhen a server pipelined a large (>16 KB) initial frame in the same TCP segment as the tail of the101response.#32394
* WebSocketclient:Sec-WebSocket-Keyis now 16 spec-compliant random bytes instead of a v4 UUID.#36496
* WebSocketclient: the opening-handshake timeout is re-armed after TCP connect so a slow upgrade times out.#35167
* WebSocketclient: unsupported proxy protocols are rejected with a clear error instead of misusing HTTP CONNECT.#35147
* WebSocketclient:ping()/pong()reject payloads over 125 bytes per RFC 6455.#35030
* WebSocketclient: thecloseevent is dispatched as a queued task per spec, not synchronously.#27259
* WebSocketclient: fixed permessage-deflate decompression failing afterZ_STREAM_ENDwith context takeover enabled.#34105

### Windows#

* bun:ffinow works on Windows ARM64, after fixing a TinyCC arm64 codegen bug where LLP64's 32-bitlongtruncated an immediate-operand mask and corrupted every double and pointer crossing the FFI boundary.#33696
* dlopen()accepts non-ASCII library paths on Windows, so DLLs under a profile directory with a non-English username load.#33712
* On Windows,bun ./dist/**/*.htmlnow registers subdirectory routes with forward slashes; previously/components/buttons404'd because the route was stored as/components\buttons.#36532
* TheResponse(Bun.file(path))streaming path on Windows closes its file descriptor exactly once.
* fs.rm(..., { recursive: true })on Windows handles readonly files and files held by antivirus or cloud-sync software.
* Unrecognized Windows error codes now map to the same errno values Node.js returns.
* The Windowsbun run/bunxfast path now heap-allocates its environment block instead of using a fixed 32,767-character buffer, so it no longer bails to the slow path when the process environment exceeds 32 KB (common in CI).
* bun getcompletesnow works on Windows, so tab completion can be installed on every platform.#24620
* --compileon Windows: the emitted.exenow carries a valid PEOptionalHeader.CheckSum.
* --compileon Windows: the emitted.exeis truncated to the correct length (orphaned Authenticode bytes from the base binary were being left past the last section).
* Fixedbun build --compiledropping the[dir]prefix fromBun.embeddedFiles[].nameunder a path-preserving asset naming pattern.#31576
* Fixed ENOENT reading nested embedded assets on Windows.#31576
* Sourcemaps: original columns are no longer off by one on lines containing a non-ASCII character.
* Sourcemaps:sourcespaths on Windows use forward slashes so DevTools resolves them.
* Sourcemaps: source files ending in an incomplete multi-byte UTF-8 sequence are handled.
* node:net: sockets no longer close before buffered inbound data is read.#36332
* node:net:SO_REUSEADDRis set when bindinglocalPorton outgoing connections on non-Windows platforms.#33886
* node:net:server.unref()releases Windows named-pipe listeners.#37079
* node:net: aReferenceErrorin the happy-eyeballs path withlocalPortset is fixed.#30699
* node:fs: coverage of Node's suite reaches97.5%withUtf8Streamsupport and unified Windows errno mapping.#34505
* node:fs: Leakedfs.promisesFileHandledescriptors are closed on GC withERR_INVALID_STATE.#33693
* node:fs:fs.writev/readvchunk more thanIOV_MAXbuffers.#33695
* node:fs: paths of exactlyMAX_PATH_BYTESare rejected withENAMETOOLONG.#34091
* node:path:path.win32.resolvefixed for drive-relative paths on Windows.
* node:path:path.win32.relative()handles slash-rooted prefix inputs.
* fs.watchnow emits('change', null)to every live watcher when the kernel's event queue overflows on Linux or Windows, instead of silently dropping the loss signal.
* bunxon Windowsnow correctly handles empty-string arguments, quoted arguments containing spaces, and package names containing multi-byte UTF-8 characters.
* Windows ARM64: thenode_modules/.binshim executable is now compiled natively for aarch64, so package binaries no longer launch through x64 emulation.#27448
* Native-binary postinstall skippingnow applies to nested copies of anativeDependenciespackage (a second esbuild pinned underdrizzle-kit/node_modules/), not just the hoisted one.#36495
* Native-binary postinstall skipping: Windows now takes the same.bin→ platform-binary redirect path as POSIX.#36856
* Isolated store directory namesnow sanitize?in tarball URLs, so a package installed from a URL with a query string can be imported (and installs on Windows, where?is an invalid filename character).#36989
* BoringSSL on macOS and Windows:now allocates through mimalloc. TheOPENSSL_memory_*override hooks were compiled out on non-ELF targets, so every TLS record read hit the system allocator.
* Startup memory on Windows: JavaScriptCore's 128MB compact-heap reservation is nowlazily committed, so only the ~3–8MB actually used counts toward committed memory.
* node:httpOn Windows, the server now stops reading the socket while a request body is paused (req.pause(), or a handler that never readsreq), applying backpressure to the client.
* Fixed a memory leak on Windows (oneStaticPipeWriterper spawn) when a bufferstdinfinishes writing.#35297#35150#35107
* Fixed a crash at thread teardown or infreeon Linux and Windows for threads that had used a private mimalloc heap, which includesWorkerthreads; fixed by resyncing Bun's mimalloc fork with upstream.
* fs.watch()on Windows cleans up its internal path map when a watch fails, so retrying the same path (as Vite, NestJS CLI, chokidar, and watchpack do) works.
* Buffer.indexOf/lastIndexOf:worst case is now O(n+m). A rare-byte two-anchor SIMD prefilter backed by a Two-Way fallback replaces the first-byte-only scan; alastIndexOfover a 4 MBaaa…haystack with a 4000-byte adversarial needle drops from 7.4 s to under 1 ms (Node: 19 ms). About 250 byte- and substring-search sites in the runtime nowcall the Highway kernel directly, including onWindows.
* Bun.Globon Windows: up to2.39x fasterfor non-**patterns. The current pattern component is passed as a kernel-sideFileNamefilter toNtQueryDirectoryFile, so non-matching entries never reach userspace.
* Internal rough-tick clock: sub-µs everywhere, backed by the CPU timestamp counter on x64 and ARM64. The old ~15.6 msGetTickCount64floor on Windows is gone.#29806
* Linux and Windows builds now bundle ICU 78.3 (up from 75.1 and 73.2), soIntluses newer locale data.
* On Windows,bun run --filternow kills the full descendant process tree on Ctrl+C, so grandchild dev servers spawned through.cmdshims orcmd.exeno longer survive with their ports still bound.#36291
* On Windows,net.connect()failures now surface the real error code (EADDRINUSE,ECONNRESET) instead of reportingECONNREFUSED(orENOENTfor a path connect) for every failure.#36786
* On Windows,fs.mkdir(dir, { recursive: true })no longer throwsEEXISTwhen the directory already exists with the ReadOnly attribute set, which OneDrive applies to synced folders.#34416
* Fixed a hang whereawait proc.exitedafterproc.unref()(or anAbortSignal.timeout()underbun test) busy-spun forever because libuv'suv_run(UV_RUN_NOWAIT)skipped its IOCP poll with only unref'd handles alive.
* Fixed a CRT fd leak infstat/futimensonNtCreateFile-backed handles (Bun.Image(path),bun pm pack,bun create) that drifted long-running processes intoEMFILEafter ~8,189 calls.#33713
* FixedNtCreateFileopens withO_NOFOLLOWdroppingFILE_SYNCHRONOUS_IO_NONALERT, a latent bug with no JS-reachable path today.#36193
* Reading and writing files larger than 4GB works on Windows.
* Reparse points are classified by tag so only name surrogates are followed as symlinks
* Opening files withO_TRUNCtruncates correctly regardless of access mode
* process.dlopenreturns an error for over-length paths
* Bun.write()reports an error when the source file does not exist
* Socket polling setup handlesuv_poll_init_socketfailure
* Native addons using SEH no longer have first-chance exceptions hijacked by Bun's crash handler
* --linker=isolatedon Windowsnow falls back to junctions when symlink creation fails with an unrecognized Windows error (typically from security software or certain filesystems), instead of silently succeeding with missing package links.#32643
* bun pm pack --quietno longer prints a leading newline before the tarball name, so$(bun pm pack --quiet)captures a clean filename.#32751
* bun pm pack--destinationon Windows no longer prints a mixed-separator path.#32751

### Memory and reliability#

* node:zlibBrotli/Zstdreset()uses~50x less memory. It was allocating a new encoder/decoder on every reset without freeing the previous one.#25592
* tls.connect({ socket })upgradesleaked one raw socket wrapper per upgrade, causing unbounded growth with the MongoDB Node.js driver (whose connection-monitoring heartbeats cycle TLS upgrades every ~10s) and the mysql2 TLS path.#26766
* Mongoose + MongoDB over TLS: a longstanding issue causing excessive peak memory usage is fixed.
* Response.clone()chain memory:flat across depth. Tee'd chunks are shared by reference instead of structured-cloned into each branch; a 100-deep clone chain of a 10 MB streaming body now costs ~20 MB RSS instead of ~1050 MB. Node.js 26.7 and Deno 2.9 both use ~1050 MB for the same chain.
* Startup symbol ordering:Linuxbun -eRSS drops another ~9 MB. Function-entry tracing (replacing page-fault tracing) lists only the ~14k functions that actually run at startup instead of the ~38k that share a page with one, and macOS arm64 now gets startup ordering too.
* Bundled startup heap:11% fewer objectsand 4 MB less memory on a large React bundle.__toESMcaches its wrapper objects in aWeakMap, and getter/setter closures are replaced with.bind().
* Runtime source maps:~8x smaller in memory. A bit-packed binary format read in place shrinks mappings from 20 bytes each to ~2.4 bytes; on TypeScript's compiler that's ~11.3 MB → 1.3 MB resident, andbun build --compilebinaries get several MB smaller.
* bun build --compilestartup:zero-copy module strings. ASCII bundle source is wrapped directly from the kernel-mmapped.bunsection instead of heap-copied; on a 40 MB bundle that's one 40 MB allocation gone at startup.
* Bun.RedisClientbuffer replies:~10% less CPU and 25–33% less peak RSSfor 1MBgetBuffercalls. The parser's allocation is adopted directly as the Buffer backing store instead of copied.
* bun build --compileresident memory: standalone executables nowmadvise(MADV_DONTNEED)the embedded source sectiononce the entrypoint is parsed, releasing bundled JS source pages back to the kernel.
* Bundler memory: boolean flags inImportRecord,Chunk,Location, and resolverResultare nowpacked into bitfields, saving an estimated 200KB–1.5MB per large build.
* Transpiler comma-expression simplification: runs in linear memory withtarget: "bun"; at n=4000 operands the RSS delta drops from ~370 MB to ~4 MB.
* Boolean flags across stream/controller/tee/pipe classes are packed into bitfields.#33817#33833
* fetch()response body memory:await res.arrayBuffer()peaks at ~1× the payloadinstead of 2–3×. The buffered path reservesContent-Lengthupfront, and decoded body bytes are delivered as a borrowed slice instead of copied through an intermediate; a 129 MB body drops from 377 MB to 139 MB over baseline.
* fetch()streaming: response-body buffers are nowreleased eagerly as chunks are consumedduring long-running downloads and proxy passthroughs, instead of being held for the lifetime of the stream.
* file:tarball dependenciesat or above the 64 MB libdeflate threshold are now streamed through libarchive instead of being decompressed into memory first, removing the 2 GiB decompressed-size cap and the intermediate buffer.#36541
* node:cryptowrapper classes (KeyObject,Hash,Hmac,Cipher,Sign,Verify,ECDH) now report their native OpenSSL memory to the garbage collector, so tight loops that allocate large keys or XOF digests no longer grow the native heap unbounded.
* node:httpA paused upload no longer buffers in memory on Windows.
* node:httpA client that finishes uploading and half-closes while the request is paused now gets its response onresume(), as it already did on Linux and macOS, instead of an aborted request.
* node:httpres.write()under backpressure:large payloads are held by referenceinstead of copied into the uWSstd::stringbackpressure buffer. The caller's Buffer is pinned and resumed from an offset on drain, matching Node.
* Async operations free their context before invoking the callback (preventing a leak when the callback exits the process).#36986#35948#37057#37017
* HTMLRewriter: fixed a memory leak where handler exceptions were over-protected in the rejection slot.#36511
* HTMLRewriter: handlers registered via.on()/.onDocument()no longer leak memory when the rewriter is garbage-collected.#29879
* Fixed a memory leak where partially-readBlob.stream()andfetch()response bodies were never collected if the reader was released without cancelling.#32582
* Fixed per-call string leaks infetch(): theproxyoption URL, and the response URL forfile://andblob:fetches, were leaked on every request.#32329
* AbortSignal.timeout()used withutil.aborted()no longer leaks memory.
* Fixed a memory leak inrequire('module')._nodeModulePaths()where each call leaked one string ref for the input and one per returned path; a 30,000-call loop now grows RSS by ~8 MB instead of ~76 MB.#32337
* Fixed a leak where droppedAbortSignal.timeout()signals kept their native timer alive until the deadline even after the JS wrapper was collected.
* Fixed a shutdown leak where JSC deferred-work tasks scheduled after the last event-loop tick were never dropped.#34293#32703#33131
* bun info,bun audit,bun publish,bun upgrade,bun create: fixed a small memory leak of the response metadata on every request these commands make.#36335
* Environment variables that contain bytes that aren't valid UTF-8 are read correctly throughprocess.env(closes eight reported issues).
* Fixed a data corruption bug inBun.write()where files larger than 2 GB would silently skip chunks, producing truncated or interleaved output.#25720
* A hypothetical race condition in the thread pool on aarch64 could leave a scheduled task with no thread awake to run it, causingfs.promises,Bun.file(),Bun.write(),crypto.subtle, andbun installto hang forever. This is fixed. Intel and AMD (x86_64) machines were never affected.
* Separately, a crashing Bun process on aarch64 could spin forever at 100% CPU instead of terminating whenever a JSSIGTRAPlistener was registered, which thesignal-exitnpm package (a transitive dep of most CLI tools) does by default. The crash handler now restores the defaultSIGTRAPhandler, and the process terminates instead of spinning.
* Illegal instruction(SIGILL) crashes on ARMv8.0 hardware (Raspberry Pi 4, Cortex-A53, AWS a1 instances) are fixed. The memory allocator was being compiled with CPU instructions these chips don't support; it now targets the baseline ARM instruction set, and CI emulates this hardware to catch regressions.
* MessagePortandBroadcastChannelwere rewritten to be thread-safe.
* socket.upgradeTLS()can be called synchronously from inside that socket's ownopenordatahandler. This is the native code path taken by Node'stls.connect({ socket }), which is how database drivers upgrade an existing TCP connection to TLS after a plaintext protocol handshake.
* realpathSyncno longer hangs when called on a FIFO — the internalopen()now passesO_NONBLOCK

### Other performance improvements#

* macOS DNS:dns.lookup()no longer parks one thread per in-flight query. Rewritten onDNSServiceGetAddrInfoover a shared connection to mDNSResponder; 500 concurrent lookups stay at ~9 threads instead of spiking to 513.
* fs.copyFile/Bun.write(file, file)read/write fallback: whenclonefile/copy_file_range/sendfilearen't available, the source is hintedPOSIX_FADV_SEQUENTIALso the kernel doubles its readahead: up to 1.39× faster on the 32 KiB inner loop from a cold cache (~1.2× end-to-end for small files); the >1 MiB slab path is unchanged.#34825
* url.searchParams.append(): fixed an O(N²) reserialize-on-every-mutation; 4000 appends took 2–5 s before and now take under 1 ms, within noise of a detachedURLSearchParams. The URL's href is now rebuilt lazily on the next read.#35080
* Timer GC sweep: fixed an O(n²) ordered-map remove when many timers had their numeric id read (+t,`${t}`); sweeping 30,000 such timers drops from seconds to ~2 ms.#35077
* bun install --minimum-release-age/bun outdated: npm-manifesttimeentries are indexed in one O(V) pass instead of an O(V²) linear scan per version; packages with thousands of versions like typescript no longer pay millions of comparisons per cold resolve.#34543
* bun buildcross-chunk export aliasing: fixed an O(N²) restart-from-1 probe loop; a shared chunk with 20,000 same-name exports builds in 424 ms instead of 17.3 s.#34529
* Bun.Globbrace groups: skipping to the end of a group is now O(1) via a cached close-}index; a ~300 KB{*,*,…,*}bpattern that took ~5 s permatch()now completes instantly.#36407
* Response.json():~3.5x faster. Bun was accidentally passing0instead ofundefinedfor the indent argument, knocking JavaScriptCore out of its SIMD-accelerated FastStringifier path.
* Buffer.toString("hex"):up to ~1.8x fasterthan Bun 1.3.14 (1.2–1.5x on 64 KB–1 MB buffers), now backed by a Highway SIMD kernel instead of a scalar table loop.
* Buffer.toString("base64")/"base64url"on 32–128 KB buffers are ~20–30% faster now that the output string is allocated through a cheaper path.
* path.parse():~2.2–2.8x fasterfor typical paths and ~7x faster for empty strings. Bun caches a pre-built Structure for{root, dir, base, ext, name}and writes property values by offset instead of triggering five shape transitions per call.
* Bun.hash.xxHash3:~2.5x fasteron AVX-512 hardware for the-baselinebuild, ~1.2x for the AVX2 build — the stripe loop now runtime-dispatches to the widest SIMD available.
* TextEncoder.encode: up to~1.6x fasteron ASCII strings of a few hundred bytes and up. The leading ASCII run is now scanned and copied in a single SIMD pass, and a redundant 2 KB stack zero-fill on every call is gone.
* Buffer.slice()/Buffer.subarray():~1.5–1.7x fasteracross all cases. Moved from a JS builtin to native C++ with an int32 fast path that skipstoNumber()coercion.
* bun buildon 2-core machines:~1.3–1.4x faster. A CAS bug inThreadPool.warm()meant worker threads were never actually pre-spawned, so the bundler ran with one fewer real thread than configured.
* expect().toContain():~2x faster,toBeOneOf()~1.3x faster.JSArrayIteratorreads directly from contiguous array storage instead of callinggetIndex()per element.
* ESM module loading:~12% faster. A one-character fix in the parser stops copying an 8 KB allocator struct on every AST node creation;_platform_memmovedropped from 7.5% to 2.9% of self time.
* Async HTTP handlers that interleave:stay on the corked fast path. Bun keeps two independent cork buffers per event loop, so a resumed handler can batch its writes even when another request is mid-flight.
* structuredClone()of dense arrays:memcpyfast path. Int32 and Double arrays clone with a singlememcpyof their backing storage, and contiguous arrays of primitives skip the byte-stream serializer entirely.
* structuredClone()of arrays of flat objects:Structure-cache fast path. The shape of the first element is reused for every subsequent same-shaped element, skipping all property transitions during deserialization.
* Bun.Glob.scan()with multiple**:visits each directory once. Patterns like**/node_modules/**/\*.jsno longer fork the traversal at every\*\*/Xboundary; the walker carries an NFA state set instead.
* Bun.stringWidth:SIMD throughout. We scan ASCII runs 64 bytes at a time and skip ANSI escape sequences (terminal hyperlinks, colors) vector-wide instead of byte by byte.
* Bun.escapeHTML:zero-allocation when nothing to escape. Rewritten as a Highway SIMD binding that returns the inputJSStringunchanged when clean, and computes exact output length in one pass before a single table-driven fill.
* Compile-time string maps:no runtime hashing. Static string lookups throughout the runtime use length-dispatched jump tables and constant word-sized compares; lexer keywords and HTTP method names resolve without a hash round.
* Bun.hash.crc32():20–100x fasteron 1MB inputs (2.3 ms → 18 µs on an AVX-512 x64 machine). Now uses zlib's hardware-accelerated implementation (PCLMULQDQ on x86, CRC32 instructions on ARM) instead of a software-only loop.
* Buffer.from(array):up to ~2x fasterfor small plain JS arrays. SkipsJSC::construct()overhead and hits JavaScriptCore's bulk-copy fast path for Int32/Double-shaped arrays.
* JSON-mode IPC: fixed anO(n²) hot loopwhen large messages arrive in chunks. Each byte is now scanned exactly once; a 100 MB message from anodechild arrives in 0.5 s instead of 1.2 s.
* tls.getCACertificates('system')on macOS:~10s → ~50mson managed Macs. No longer triggers per-certificate OCSP/CRL network fetches when enumerating the keychain.
* setImmediateon Linux/macOS:no longer writes to the eventfd on every iteration. strace shows ~44k eventfd writes for a 5ssetImmediateloop dropping to 0.
* Event loop on Linux: now usesedge-triggered epoll for eventfd wakeups, eliminating an unnecessaryread()syscall on every loop tick.
* Event loop under load: nowdrains epoll/kqueue in a tight loopwhen more than 1024 fds become ready at once, so one tick can service the whole backlog instead of one 1024-event batch.
* Module resolver:caches not-found resultsto skip repeatedstat/openatsyscalls for the same missing path during import resolution (part 2).
* Enum-string getters:request.cache,response.type,ws.binaryType,socket.localFamily, and friends nowreturn cached atom-backed stringsinstead of allocating on every access.
* bun build --compile: embedded.nodeaddons areextracted once to a content-hashed filein the temp dir and reused acrossdlopen()calls, Workers, and restarts, instead of writing a new copy per load.
* Incremental GC: ~60 generated JS classes (Request,Response,Stats,Dirent,Subprocess, …)no longer enroll in JSC's output-constraint GC pass. Every edge they expose already fires a write barrier, so the per-mutator-yield rescan was pure overhead.
* structuredClone(): the dense-number-array fast pathno longer zero-fills the destinationbefore copying into it.
* AbortSignal.abort():~6% fasterwhen no listeners are registered. Skips allocating and dispatching the Event entirely.
* Removed anunnecessarygetcwd()syscallfromfs.watch().
* Fixed anoperator-precedence bugin the native-readable stream'sgetRemainingChunkthat was triggering an unnecessaryBuffer.allocon nearly every chunk.
* Dozens of hot-path micro-optimizations across the runtime: redundant allocations and copies removed fromresponse.statusText,hash.digest('base64'),server.fetch(url),fetch()with a customHostheader,package.json"exports"resolution, and the runtime transpiler cache (#31054,#31064).
* Rejected-promise drain: draining the rejected-promise list at each macrotask checkpoint is now O(n) instead of O(n²); rejecting 20,000 promises in one tick drops from 19.13 ms to 0.88 ms.#32554
* Bun.indexOfLine(): fixed an O(n²) scan when the buffer contained any non-ASCII byte; a 60 KB buffer with a singleébefore the newline now scans in ~0.01 ms instead of ~15 ms.#32732
* Recursivefs.cpon macOS: once again uses a single whole-treeclonefile()when the source contains only regular files and directories and the destination doesn't exist, restoring the fast path lost when Node's relative-symlink rewriting was ported.#32503
* FileSystemRouterURL joins: skip zero-filling two 2 KB stack scratch buffers per join, saving 4 KB of memset per emitted URL in the router and dev server.#32393
* bun installnow explains that an unsupportedbun.lockversion was likely written by a newer Bun and suggests runningbun upgrade, instead of a bare "Unknown lockfile version" error.#32465
* Error messages forbun install --linker,bun build --format/--loader/--define,bun patchwith no argument, andbun run --filteron an unreadable workspacepackage.jsonnow echo the offending value and/or show a correct example.#32470
* bun initnow scaffolds every template (blank, library, and all React variants) with TypeScript 7.#33265
* Thebun inittemplate lockfiles have been regenerated sobun install --frozen-lockfilepasses out of the box.#33265
* ESM imports of builtins:importofnode:fs,node:tls,node:http,node:timers, and the other builtins with lazily computed exports no longer computes those exports at import time; each is computed when something first binds to it. Plain data exports are still snapshotted at import.import "node:fs"was pulling in the wholenode:streamstack forReadStreamandWriteStream, taking 13.3 ms whererequire("node:fs")took 7.8 ms.#37525
* export * from "bun": re-exporting thebunmodule, or loading it throughimport()with a computed specifier, no longer constructs all 115Bun.*properties up front; each is constructed when first bound. One consequence: an invalidREDIS_URLnow throws when theredisexport is first used, and the rest of the module loads.#37714
* node:processandnode:module: both now construct only the exports a file imports.import process from "node:process"no longer buildsstdout,stderr, andstdinor loadsnode:ttyandnode:streamfor them, which was adding 10–18 ms to the startup of an otherwise empty file;import { createRequire } from "node:module"constructs onlycreateRequire.#37726

### Other JavaScriptCore changes#

* Iterator.prototype.includes()is enabled by default (319f94b3db4a).#36794
* CyclicArray#join/toStringnow throwsRangeErrorper spec instead of returning""(f2f2c2ddf637).#36794
* The debugger now resolves breakpoints in ES modules loaded bybun test --isolateor--paralleland inbun build --compileexecutables (oven-sh/WebKit#405). PreviouslyDebugger.setBreakpointreplied "Could not resolve breakpoint" andDebugger.setBreakpointByUrlreturned no locations.#37352
* Thearlocale, for example, now formats numbers with Latin digits.
* new URL()andurl.domainToASCII()now take their Unicode 16 hostname mappings (ẞtoß) from ICU instead of a table in Bun.
* Math.roundreturned the wrong result via thefloor(x+0.5)JIT fast path for0.49999999999999994(312687).
* JIT miscompiled self-comparisons likex === x(306820).
* JIT miscompiled%results that should be-0(308016).
* JIT miscompiled guards that a value matches a known constant (311779).
* ArrayToPrimitivefast path ignoredvalueOfoverrides (312672,314582).
* String#splitRegExp fast path missed side effects (316508).
* matchAllfast path ignoredSymbol.specieson RegExp subclasses afterRegExp.prototypewas modified (316047).
* Map/Set iteration fast path skippedIteratorClosewhen the callback threw (316495,315979).
* Array#concatfast path could return wrong results when concatenating arrays with mixed element kinds (314015).
* String#searchJIT fast path mishandledlastIndexfor global/sticky regexes (313139).
* RegExp engine: named groups dropped fromindices.groupson backtrack with/d(e1cdfab158f3).
* RegExp engine:/^(?:c||b)/mid-empty alternatives gave wrong JIT result (e6d0f57f8d04).
* RegExp engine:/iASCII ranges didn't matchſ(U+017F) andK(U+212A) (faf717c136d1).
* RegExp engine: greedy backtracking didn't try up to max count (316378).
* Promise.resolvereturned a base Promise even for subclasses (309472).
* Promise.prototype.finallythrow timing inSpeciesConstructor(312466).
* Promise jobs ran with the realm of a cross-realm settle site (316187).
* Deferred module namespace's"then"leaked intoObject.keys(316610).
* Intl spec conformance:Intl.NumberFormat(303270),Intl.Locale.prototype.getWeekInfo(302587),Intl.SegmenterisWordLikeoff-by-one (312596),Intl.Localecanonicalization before language override (312693),Intl.DateTimeFormatlegacy[[TimeZone]](312841) andRangeErrorfor legacy non-IANA timezones (296248),String.prototype.substringusesToIntegerOrInfinity(300578).
* A crash inWebAssemblyresizable memory buffers is fixed.
* Deep import graphs of modules using top-levelawaitload safely.
* A GC bug inevalhas been fixed.
* Garbage-collector heap cleanup is synchronized with background scanning threads.
* The JIT rechecks the prototype chain when optimizing prototype property accesses.
* Wasm interpreter miscomputedmemory.atomic.*/memory.growresults (316507).
* Better error messages: calling a class constructor withoutnewnow names the class (dabbab2ba61e).
* Better error messages: a non-object return from a derived constructor now names the constructor (e2c7e56a9516).

### Security hardening#

* TLStls.Serverapplies its defaultrejectUnauthorized: trueto incoming connections and gates peer-certificate verification onrequestCert, matching Node.
* TLSWildcard certificates no longer match across multiple labels.
* TLSfetch()supports mTLS: passcertandkeyintlsand each request uses its own client certificate.
* TLSLongtls.passphrasevalues are handled safely.
* HTTPres.statusMessageandwriteEarlyHintsvalidate against CRLF.
* HTTPfetch()drops caller-suppliedTransfer-Encodingfor fixed-size bodies.
* HTTPfetch()caps user-supplied header count.
* HTTPnode:http2zero-fills DATA-frame padding.
* HTTPnode:http2validates padding lengths.
* HTTPnode:http2rejects malformed request pseudo-header blocks.
* HTTPThe HTTP/3 server enforces the same header-byte and client-certificate rules as TCP.
* bun installand registry authPackage folder names are validated before extraction.
* bun installand registry authOff-registry tarballs migrated frompackage-lock.jsonrequire integrity.
* bun installand registry authTransitivefile:targets are constrained.
* bun installand registry authBin links that escape the package directory are rejected.
* bun installand registry authSymlink entries in git/GitHub tarballs are created after every file and directory entry.
* bun installand registry authTrusted-dependency names,.npmrcscope names, and localfile:paths are compared by their full bytes rather than a hash.
* bun installand registry authRegistry tokens stay scoped to their configured host and are never sent cross-origin or downgraded tohttp://
* bun installand registry authCredentials are redacted from error and verbose output and from publisheddist.tarballURLs.
* bun installand registry authBuild artifacts are created with owner-only permissions.
* bun installand registry authNODE_COMPILE_CACHEfiles are0600
* bun installand registry authThe install-time security scanner receives package data over a pipe instead of process arguments.
* Crypto: PostgreSQL SCRAM-SHA-256 server-signature verification is constant-time.
* Crypto: WebCrypto pads the JWK"d"field to the correct length for EC private keys.
* Crypto:crypto.subtle.deriveBitshandleslength: 0, omitted, and non-multiple-of-8 lengths per spec.
* Crypto:crypto.subtle.importKeyrejects Ed25519 keys whose public half does not match.
* Crypto:crypto.getCiphers()/getHashes()return lowercase names.
* Crypto:node:cryptorandom functions draw from BoringSSL's DRBG again.
* Dependencies: BoringSSL updated to upstream606d3a344(post-quantum algorithms, plus upstream fixes to RC2 and TLS handshake handling).
* Dependencies: bundled root certificates updated to NSS 3.124 (the store shipping in Firefox 152), removing 25 expired or distrusted roots.

### Platform#

* Sockets are now created withWSA_FLAG_NO_HANDLE_INHERIT, so a detached child spawned while a server is listening no longer inherits the listen socket and holds the port open after the parent exits.#36938

### Bug fixes#

We fixed over 2,900 issues since Bun 1.3. Many were found through continuous fuzzing of runtime APIs with Fuzzilli, coverage-guided fuzzing of system calls and parsers, AddressSanitizer in CI, LeakSanitizer in CI, and a continuously-running Claude Code session fuzzing Bun canary's outputs against Bun v1.3.14 and Node.js.

* bun build --compile: Linux standalone executables run on WSL1. The.bunpayload is now embedded inside an existing segment of the binary instead of adding a new one, a layout WSL1's program loader rejects.#29967
* path.resolve,path.relative, andpath.toNamespacedPathhandle arbitrarily long paths.
* The timer behindAtomics.waitAsyncis thread-safe.
* Async zstd compression,crypto.scrypt, andBun.Transpilerkeep their input buffers alive for the duration of the operation.
* FixedRequest.formData()truncating small binary file uploads at the first null byte, so a 4-byte gzip header would come back as 3 bytes.
* Fixedprocess.envbeing completely empty when the current working directory lacks read permission (common in locked-down containers).#28785
* Bun now starts on older Linux kernels (< 3.17, e.g. Synology NAS) that lack thegetrandom()syscall.#27282
* Bun no longer returnsEINVALon socket reads under gVisor (Google Cloud Run).#27390
* Fixed piping Bun's output intoless,fzf, andfx. Bun was clobbering the downstream program's raw mode at exit, leaving it unresponsive to keypresses.#29593
* FixedBun.Globandfs.readdir({ recursive: true })silently skipping files on bind mounts, FUSE, NFS, and similar filesystems.#25838
* The Linux file watcher handles large batches of inotify events.
* Fixedbun --hoton macOS losing track of files after editors performed atomic write-then-rename saves, causing the module graph to flip between old and new code.#29529
* Bun's HTTP server handles absolute-form request URLs on keep-alive connections.
* Fixed Bun's DNS cache never expiring stale entries while any in-flight request to that host held a reference, so DNS results never refreshed under sustained traffic.#28271
* Fixedrequire()of an ES module deadlocking when the module graph contained a diamond dependency through a barrel file.#30527
* Deeply nested expressions and JSX throw a catchable error inbun buildand the dev server.
* Bun.S3Client: fixed a leak when a download stream is cancelled while the socket is idle.#32608
* Bun.S3Client: aContent-Length: 0+Connection: closeresponse (the shape of every S3 PUT/DELETE) is no longer misreported asConnectionClosed, fixing spurious retries through connection-recycling proxies.#33292
* Bun.Glob: explicitly-named dotfile segments match withoutdot: true, matching bash and fast-glob.
* Bun.Glob: literal segments resolve through symlinked directories withoutfollowSymlinks: true, matching bash and fast-glob.
* Bun.Glob:absolute: truereportsENAMETOOLONGfor over-long paths.
* Bun.Glob: deeply nested braces are handled.
* Bun.color(): 24-bitnumberinputs like0xff0000are treated as opaque instead of alpha 0.
* Bun.color():ansi-16output emits the color number as decimal digits instead of a raw control byte.
* Bun.color():ansi-256no longer underflows the grey ramp.
* Bun.color():hsl/laboutput is parseable.
* Bun.color():lab()/oklab()on the sRGB gamut boundary no longer desaturate in their sRGB fallback.
* Bun.Cookie:Expiresserializes as a valid RFC 6265 date (previously every date had the wrong weekday, an unpadded day, and-0000instead ofGMT).#32926
* Bun.Cookie:parse()records bothExpiresandMax-Ageregardless of order.#33393
* Bun.Cookie:isExpired()applies the RFC 6265 precedence rule.#33393
* Bun.YAML:parse()combines\uD8xx\uDCxxsurrogate-pair escapes so JSON documents containing emoji parse correctly.#32731
* Bun.YAML:stringify()no longer emits\L/\Pfor U+00A8/U+00A9.#32718
* HTMLRewriter:element.getAttribute()returns""for present-but-empty attributes (including boolean attributes likedisabled) instead ofnull.#32840
* HTMLRewriter:setAttribute/removeAttributethrow on invalid arguments instead of returning anErrorobject.#32840
* bun:sqlite: generic errors (syntax errors, unknown tables, unknown columns) seterror.codeto"SQLITE_ERROR"instead ofundefined, matching better-sqlite3.#33397
* Bun.stringWidth(): bidi controls (U+202A–U+202E, U+2066–U+2069, U+061C) and Mongolian variation selectors are now zero-width, matchingwcwidth(3)and thestring-widthpackage.#33049
* Bun.JSON5.parse,Bun.JSONC.parse,Bun.TOML.parse,Bun.YAML.parse, and theBun.markdownrenderers throwERR_OUT_OF_RANGEon oversized inputs.
* Sockets with pending writes are torn down cleanly on peer reset on macOS.
* Fixedfetch()hanging at 100% CPU when anode:streamReadablewhose_read()pushes synchronously was passed as the request body.#36087
* Fixednode:httpsserver truncating large response bodies when the client half-closed the connection before Bun had finished flushing its buffered TLS writes.#35109
* Fixedprocess.setuid(),process.seteuid(), and related identity calls deadlocking on Linux.#33565
* Fixed nestedbun runexiting before its child on Ctrl-C — the signal-forwarding handler now stays installed across deliveries, sobun runwaits for the script's cleanup to finish.#36711
* The epoll_pwait fallback no longer busy-spins on sub-millisecond timers.#34779#34780
* epoll/kqueue waits now subtract elapsed time when retrying after EINTR instead of over-waiting.#34779#34780
* Loading a glibc-linked native addon on musl-based Linux now throwsERR_DLOPEN_FAILEDinstead of segfaulting.
* Restored the Izenpe.com root CA to the bundled certificate store; a bug in the cert-bundling script had accidentally dropped it.#31612
* Fixed a crash when aborting afetch()after its response body stream had been garbage collected.
* Comma-separatedConnection,Transfer-Encoding,Content-Encoding, andUpgradeheaders are now parsed as token lists.#36777#36370#34425#36588
* File-response streams tear down cleanly on read errors.
* Sockets: TLS sockets now FIN the TCP write side afterSSL_shutdowncompletes on half-open connections.
* Sockets: UDP sockets stop dispatching batched packets onceclose()is called from a data handler.
* Sockets: connecting to over-long Unix socket paths on Linux returns an error.
* DNS:dns.Resolverno longer keeps the event loop alive for an extra retransmit interval after its last query completes via c-ares timeout.#36192
* DNS: fixed aFilePollslot leak per distinct-hostname libinfo lookup (fetch,Bun.connect, WebSocket, QUIC) on macOS.#34423
* DNS: fixed a memory leak of pending-lookup hostnames when the resolver pool is dropped.#33901
* Workertermination: fixed several crashes whenworker.terminate()ran while sockets, WebSockets, CJSrequire,process.emit,fs.readFile, or DNS lookups were in flight.
* Bun.file(): fixed an fd leak on POSIX when an abandoned.stream()reader is garbage-collected.#35211
* Module resolver: fixed a bug intsconfigpathswildcard resolution when the pattern's prefix and suffix overlap.
* Module loading: importing a longdata:URL no longer fails withENAMETOOLONG.#37157
* Module loading: CSS imports at runtime now default-export{}, matchingbun buildbehavior.#35163
* Parser: JS, TS, and TOML error columns now count UTF-16 code units, so editors jump to the right column.#34720
* Parser: error locations are correct for rest-with-default and parenthesized destructuring pattern syntax errors.#35970
* ResolveMessage.message,.specifier, and.referrerrender non-ASCII paths correctly.#34096
* Parser: deeply nested TOML throwsRangeError.
* Parser: the sourcemap parser rejects malformed VLQ fields with a proper error.
* Parser: the CSS parser reports custom at-rule block parse errors.
* structuredClone: malformedSet,Map, andRegExppayloads are rejected.
* Duplex-wrap origin/listeners are now GC-rooted via the JS wrapper instead of Strong handles (rooting-model cleanup, not a leak).#34672
* HTMLRewriter: abandoned transforms are collected safely.
* Process exit and worker termination are safe while an off-thread transform is in flight.
* bun build --compile: inject temp files use random names to avoid cross-process collisions.
* bun build --compile: single-file executables validate the Mach-O__BUNsegment size.
* Bun.plugin: an object-loaderexportsgetter that throws is handled.
* WebAssembly.instantiateStreamingacceptsapplication/wasmregardless ofContent-Typeletter case.#33229
* multipart/form-dataparsing matchesform-datacase-insensitively and accepts HTAB whitespace.#34362
* Oversized strings throwERR_STRING_TOO_LONG.
* --cpu-prof-dirand--heap-prof-dirreport an error on over-long paths.
* Bun.JSONC.parsethrowsSyntaxErroron invalid input instead of aBuildMessage.
* bunfig.toml type-mismatch errors print human-readable type names.
* Error.stackcomputation,Blobcontent-type handling, and deserializedBloblastModifiedare hardened.
* node:vmlink(),Workername, and FFI threadsafe callbacks are hardened.
* SlicedBun.file()reads respect the slice bounds.
* process.stdinno longer ignoreshighWaterMarkbackpressure when reading from a pipe.
* The file watcher returns an error when its thread fails to spawn.
* Nested${...}inside${VAR:-default}in.envfiles parses correctly.
* NativeSIGABRTandSIGTRAPcrashes now produce Bun crash reports.
* Heap snapshots reportmodule.childrenandmodule._compilefor better memory debugging.
* bun createno longer busy-waits on git operations.
* Bun.sliceAnsireturns the ellipsis when a start-cut range contains only zero-width clusters.
* TLS sockets: the handshake idles correctly while waiting on the peer.
* Module resolver: over-longpackage.jsonbrowsermap keys are handled; the package loads and the other entries in the map still apply.
* file:../paths inoverridesandresolutionsare no longer rejected with "unsafe folder path"; paths declared in the rootpackage.jsonare trusted the same as direct dependencies.#32452
* Transitivefile:dependenciesof a localfile:package are now linked intonode_modulesunder the hoisted linker, fixingCannot find moduleat runtime for the nested package.#33159
* Lockfile migrationfrompackage-lock.jsonandpnpm-lock.yamlno longer silently dropsfile:dependencies whoseos/cpufields don't match the host.#33155
* The isolated linkerno longer leavesnode_modules/.bunsymlinked to the shared global store afterinstall.globalStoreis disabled.#32182
* The isolated linker: ranged peer dependencies loaded frombun.locknow resolve to the same version on the second install as the first.#32182
* bun pm pkg setno longer writes a garbage property key intopackage.jsonwhen the key path contains a bracketed index likecontributors[0]=alice.#33186
* Registry request retriesfollow 3xx redirects to the correct URL.
* Registry request retries: a retry after a cross-origin redirect keeps itsAuthorizationheader.
* patchedDependenciesentries with malformed hunks are handled bybun install.
* Error message formatting: severalbun installerror paths no longer leak raw markup tags (Integrity check failed<r> for tarball) into terminal output.#33245
* A crash in the HTTP client in request-failure handling has been fixed.
* Bun.YAML.stringify(),Bun.TOML.stringify(),Bun.JSON5.stringify(): a boxedStringorNumberwhoseSymbol.toPrimitive,valueOf, ortoStringthrows now surfaces that exception; previously it was dropped (and tripped an assertion in debug builds).#37025
* Bun.inspect()andBun.deepEquals(): objects mutated by a custom inspect hook or getter during formatting or comparison are handled safely.
* GitHub Actions error annotations no longer drop non-ASCII bytes from the title and body, so a test throwing"hello é world"shows the full message instead of a truncated fragment.#32736
* expect.any(Object)now matchesnulland rejects functions, matching Jest'stypeof === "object"semantics.#32922
* expect().toContain()now compares array and iterable elements with===instead ofObject.is, matching Jest.expect([-0]).toContain(0)now passes andexpect([NaN]).toContain(NaN)now fails.#32950
* jest.resetAllMocks()andvi.resetAllMocks()now reset mock implementations and return values, not just call history. Previously both were bound to the same function asclearAllMocks().#33374
* Fixed theoven/bunDebian and Debian-slim Docker images failingapt-getover HTTPS withcertificate verify failed;ca-certificatesis now installed in the final stage.#33136

## Thank you!#

Bun is free, open source, and MIT-licensed. We receive a lot of contributions from the community, and we'd like to thank everyone who fixed a bug or contributed a feature in this release.

* @190n
* @alanstott
* @alii
* @alinalihassan
* @amdad121
* @ant-kurt
* @anthonybaldwin
* @avarayr
* @baboon-king
* @billywhizz
* @bmwalters
* @Boshen
* @braden-w
* @c-stoeckl
* @carlsmedstad
* @chrislloyd
* @cirospaciari
* @coleleavitt
* @connerlphillippi
* @crishoj
* @csvlad
* @d4mr
* @darwin808
* @ddmoney420
* @dioro
* @djs5008
* @dylan-conway
* @Elfayer
* @emwadde
* @eroderust
* @fraidev
* @franklinfollis
* @gameroman
* @gaowhen
* @halil-pan
* @hamidrezahanafi
* @HK-SHAO
* @Hona
* @hoXyy
* @ig-ant
* @igorkofman
* @jackkleeman
* @Jarred-Sumner
* @jsparkdev
* @kirillmarkelov
* @kjanat
* @km-anthropic
* @kylekz
* @ldkhang1201
* @Lillious
* @lydiahallie
* @makuko
* @mariusz4044
* @markovejnovic
* @martinamps
* @mattermoran
* @MiniGod
* @mippbipp
* @mmitchellg5
* @nathanosoares
* @nektro
* @nfreya
* @NicoCevallos
* @nkxxll
* @ocodista
* @paperclover
* @pfgithub
* @prekucki
* @rekram1-node
* @remorses
* @RiskyMH
* @robjtede
* @RyanGst
* @shendongming
* @ShlomoCode
* @sosukesuzuki
* @sqdshguy
* @ssing2
* @Tamicktom
* @taylordotfish
* @vadim-anthropic
* @veggiesaurus
* @WhiteMinds
* @xingxingmofashu
* @yinheli
* @zackradisic
* @brunorodmoreira
* @pxseu