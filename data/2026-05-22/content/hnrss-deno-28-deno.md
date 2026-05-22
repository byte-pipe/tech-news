---
title: Deno 2.8 | Deno
url: https://deno.com/blog/v2.8
site_name: hnrss
content_file: hnrss-deno-28-deno
fetched_at: '2026-05-22T19:34:58.247896'
original_url: https://deno.com/blog/v2.8
date: '2026-05-22'
description: '`import defer`, six new subcommands (`deno transpile`, `deno pack`, `deno bump-version`, `deno ci`, `deno why`, `deno audit fix`), network debugging in Chrome DevTools, framework-aware `deno compile`, and 3.66x faster cold npm installs.'
tags:
- hackernews
- hnrss
---

# Deno 2.8

May 22, 2026

* Bartek Iwańczuk
* Product Update

Deno 2.8 is here. This is our biggest minor release to date and we’re excited to
share it with you.

To upgrade to Deno 2.8, run the following in your terminal:

deno upgrade

If Deno is not yet installed, run one of the following commands to install orlearn how to install it here.

# Using Shell (macOS and Linux):

curl
 
-fsSL
 https://deno.land/install.sh 
|
 
sh

# Using PowerShell (Windows):

iwr https://deno.land/install.ps1 
-useb
 
|
 iex

## New subcommands

### deno audit fix

deno audit(shipped in 2.6)
reports vulnerabilities in npm packages in your dependency tree. The newdeno audit fixsubcommand goes one step further and automatically upgrades
affected packages to the nearest patched version that still satisfies your
version constraints (#32909,#34273). The same behavior is
also available as a--fixflag ondeno audit:

$ deno audit fix
╭ body-parser vulnerable to denial of 
service
 when url encoding is enabled
│ Severity: high
│ Package: body-parser
│ Vulnerable: 
<
1.20
.3
╰ Info: https://github.com/advisories/GHSA-qwcr-r2fm-qrc7

╭ Express.js Open Redirect 
in
 malformed URLs
│ Severity: moderate
│ Package: express
│ Vulnerable: 
<
4.19
.2
╰ Info: https://github.com/advisories/GHSA-rv95-896h-c2vc

Found 
2
 vulnerabilities
Severity: 
0
 low, 
1
 moderate, 
1
 high, 
0
 critical

Fixed 
1
 vulnerability:
 body-parser 
1.19
.0 -
>
 
1.20
.3

1
 vulnerability could not be fixed automatically:
 express 
(
major upgrade to 
5.0
.0
)

Anything that needs a major-version bump is listed separately, so you can decide
whether to relax the constraint.Learn more aboutdeno audit fix.

### deno bump-version

deno bump-versionupdates the version field in yourdeno.jsonorpackage.json(#30562):

$ deno bump-version patch 
# 1.4.6 -> 1.4.7

$ deno bump-version minor 
# 1.4.6 -> 1.5.0

$ deno bump-version major 
# 1.4.6 -> 2.0.0

$ deno bump-version prerelease 
# 1.4.7-0 -> 1.4.7-1

In a workspace it does more. Run it at the workspace root and the same increment
is applied to every member package, with matchingjsr:version constraints in
the root config and import map rewritten in place so cross-package references
stay in sync (#33689):

$ deno bump-version patch 
# bumps every workspace member

Without an increment argument, workspace mode switches to deriving per-package
bumps fromConventional Commitsbetween
a base ref and the current branch. It honors scoped commits, wildcard*scopes,BREAKING/!for major bumps, prerelease increments, and 0.x.y
semver semantics, and treats any manual version edits since the base ref as
authoritative.

$ deno bump-version 
--base
=
main --dry-run

--dry-runprints the planned changes without writing anything, and--start/--baselet you pin the comparison range when the default “current branch since
the latest tag” isn’t what you want.

Learn more aboutdeno bump-version.

### deno ci

CI scripts and Dockerfiles want one thing from an install: “give me exactly what
the lockfile says, and fail loudly if anything is off.” Until now that meant
remembering the right combination of flags ondeno install. Deno 2.8 adds a
dedicateddeno cisubcommand (#34235):

$ deno ci

It errors ifdeno.lockis missing, removes any existingnode_modulesdirectory, and then runs the install with--frozenso the lockfile must match
the config file exactly. Drop it into your CI step orDockerfileand you get
an obvious, greppable signal of “reproducible install” without having to think
about flags.--prodand--skip-typeswork the same way they do ondeno install.

### deno pack

deno packis closer totsc+npm packcombined than tonpm packalone:
it builds a Deno or JSR project into an npm-publishable tarball in one shot
(#32139). Given adeno.jsonlike:

deno.json
{

 
"name"
:
 
"@scope/my-lib"
,

 
"version"
:
 
"1.0.0"
,

 
"exports"
:
 
"./mod.ts"

}

…runningdeno packproduces ascope-my-lib-1.0.0.tgzthat’s ready fornpm publish. The tarball contains:

* A generatedpackage.jsonwithtype: "module", conditionalexports(types/import/default), and the extracted runtime dependencies.
* Your TypeScript transpiled to JavaScript.
* .d.tsdeclaration files extracted via the same fast-check pipelinedeno publishuses (pass--allow-slow-typesto skip).
* READMEandLICENSEfiles if present in the project root.

Along the waydeno packrewrites specifiers so the published package works
inside the npm ecosystem:jsr:@std/pathbecomes@jsr/std__path,npm:express@4becomesexpress, relative./utils.tsimports become./utils.js, andnode:builtins are left alone. If your code callsDeno.*APIs, the package automatically picks up@deno/shim-denoas a dependency so it
runs on Node too (opt out with--no-deno-shim).

File selection is graph-based: only modules reachable from your declaredexportsare bundled, not whatever sits in the directory. Tarballs are
deterministic (sorted entries, fixed timestamps and permissions), which matters
for reproducible builds and content-addressed registries.

$ deno pack 
# build the tarball

$ deno pack --dry-run 
# preview the file list

$ deno pack --set-version 
2.0
.0 
# override version without editing deno.json

$ deno pack 
--output
 my-package.tgz 
# write to a specific path

$ deno pack 
--ignore
=
tests/ 
# exclude test files

$ deno pack --allow-dirty 
# pack with uncommitted changes

Learn more aboutdeno pack.

### deno transpile

A new subcommand strips types from TypeScript, JSX, and TSX and writes plain
JavaScript to disk. No bundling, no module rewriting, no config. Just the emit
step.

greeter.ts
interface
 
User
 
{

 name
:
 
string
;

 balance
:
 
number
;

}

export
 
function
 
greet
(
user
:
 
User
)
:
 
string
 
{

 
return
 
`
Hello 
${
user
.
name
}
, you have $
${
user
.
balance
.
toFixed
(
2
)
}
`
;

}
$ deno transpile greeter.ts 
-o
 greeter.js
greeter.js
export
 
function
 
greet
(
user
)
 
{

 
return
 
`
Hello 
${
user
.
name
}
, you have $
${
user
.
balance
.
toFixed
(
2
)
}
`
;

}

deno transpileaccepts multiple files,--outdirfor batch output,--source-map separate|inline, and--declarationto emit.d.tsalongside
the JS. Useful when you need to publish a JS-only artifact or pre-build TS for a
runtime that doesn’t speak it natively.

Learn more aboutdeno transpile.

### deno why

deno why <package>explains why a package is installed by walking from your
direct dependencies down to the package in question
(#32908). It’s the equivalent ofnpm explain/pnpm why/yarn why. It works with both npm and JSR
dependencies (#34227).

Given a project that mixes both registries:

deno.json
{

 
"imports"
:
 
{

 
"express"
:
 
"npm:express@^4"
,

 
"dax"
:
 
"jsr:@david/dax@^0.43"

 
}

}

deno whytraces an npm transitive back to its npm entry point:

$ deno why qs
qs@6.14.2
 npm:express@4 
>
 qs@6.14.2

qs@6.15.1
 npm:express@4 
>
 body-parser@1.20.5 
>
 qs@6.15.1

…and a JSR transitive back to its JSR entry point, with each path through the
tree listed separately:

$ deno why @std/path
@std/path@1.1.4
 jsr:@david/dax@0.43 
>
 @std/path@1.1.4
 jsr:@david/dax@0.43 
>
 @david/path@0.2.0 
>
 @std/path@1.1.4
 jsr:@david/dax@0.43 
>
 @std/fs@1.0.23 
>
 @std/path@1.1.4
 jsr:@david/dax@0.43 
>
 @david/path@0.2.0 
>
 @std/fs@1.0.23 
>
 @std/path@1.1.4

Pin to a specific version withdeno why qs@6.15.1ordeno why @std/path@1.1.4when you only care about one branch of the tree.Learn more aboutdeno why.

## Deno now defaults tonpm:

Deno 2.8 drops thenpm:prefix requirement at the CLI:deno addanddeno installnow treat unprefixed names as npm packages by default
(#33246), so the command you type
matches what every Node developer already types out of muscle memory.

# Before 2.8

$ deno 
add
 express
error: express is missing a prefix. Did you mean 
`
deno 
install
 npm:express
`
?

# 2.8

$ deno 
add
 express
Add npm:express@5.2.1

Dependencies:
+ npm:express@5.2.1

Thenpm:prefix still works (and is still required inimportspecifiers),
but you don’t have to type it at the CLI. JSR packages keep thejsr:prefix so
the two registries stay unambiguous.

With this changedeno installbecomes a drop-in fornpm install,yarn, orpnpm installin an existing Node project. It readspackage.json, writes a
compatiblenode_moduleslayout, andinstalls3.66xfaster than 2.7 on a cold cache; warm installs
are faster still thanks to Deno’s shared global cache across projects. Reach for
Deno as your package manager and keep running everything else on Node.Learn more aboutdeno install.

## Node.js API compatibility

Node.js compatibility has been an important focus for us in the past couple
years. And we’re happy to announce that we made a huge leap forward in Deno 2.8:
pass rate against Node’s own test suite jumped from roughly42% in Deno 2.7 to
76.4% in Deno 2.8(3,405 of 4,457 tests passing); 500 commits landed since
Deno 2.7, touching nearly everynode:module.

We keep close track of this percentage atnode-test-viewer.deno.dev:

Don’t mind that 100% blip in January 😅

Head-to-head against Bun 1.3.14 on the same suite:

Node.js test suite pass rate (4,457 tests)

Deno v2.8

76.4% 
(3,405)

Bun 1.3.14

40.6% 
(1,810)

Excluding tests that bail out early: 
Deno 2.8 72.4%
 (3,229 / 4,457) vs 
Bun 1.3.14 36.4%
 (1,623 / 4,457).

Deno 2.8 also makes Node compatibility cheaper in real projects: many Node
built-in modules are now lazy-loaded, so programs that don’t touch them start
faster (importing one of those modules later pays a small deferred load cost).
Severalnode:*hot paths also picked up dedicated optimizations; see thePerformance sectionbelow for benchmark numbers.

## Performance

Deno 2.8 ships meaningful speedups across the package manager,node:*compatibility, HTTP serving, and the Web platform. Measured on Linux against
Deno 2.7.1:

Deno 2.7 (gray) vs 2.8 (blue)

Cold npm install
lower is better

v2.7
3,319 ms

v2.8
906 ms

3.66x faster

node:buffer
 base64
lower is better

v2.7
2,594 ms

v2.8
844 ms

3.07x faster

node:http
 throughput
higher is better

v2.7
8,339 req/s

v2.8
18,431 req/s

2.21x faster

node:crypto
 scrypt
lower is better

v2.7
1,533 ms

v2.8
724 ms

2.12x faster

node:http
 p99 latency
lower is better

v2.7
20.86 ms

v2.8
11.89 ms

1.75x faster

node:http
 chunked writes
higher is better

v2.7
6,635 req/s

v2.8
11,521 req/s

1.74x faster

Chunked writes p99
lower is better

v2.7
25.39 ms

v2.8
15.68 ms

1.62x faster

node:fs
 recursive 
cpSync
lower is better

v2.7
432 ms

v2.8
290 ms

1.49x faster

Worker 
MessagePort
 ping-pong
lower is better

v2.7
1,678 ms

v2.8
1,270 ms

1.32x faster

Bars share a scale per order of magnitude. Process benchmarks: 30 
hyperfine
 samples. HTTP benchmarks: 10 samples of 30-second 
oha
 runs.

Cold npm installs.An entrypoint importing React, Vite, Babel parser, and
ESLint installs3.66xfasterin Deno 2.8,3,319msdown to906ms, on a
freshDENO_DIR. Across 30 samples, the bootstrap 95% confidence interval for
the speedup was3.53xto3.75x. A few of the changes that fed into that
number:

* Abbreviated packuments(#32364). The npm registry
exposes a smaller “abbreviated” metadata document
(application/vnd.npm.install-v1+json) that includes only the fields a
resolver needs; Deno now uses this smaller document for resolution and only
fetches the full packument if it needs to.
* Parallel npm resolution(#32416). The resolver used to
walk parent nodes one at a time. Deno 2.8 fans out across parent nodes too, so
independent branches of the dependency tree no longer wait on each other.
* Decompression off the async event loop(#32400). Large packument gzip
decompression could stall other HTTP/2 streams sharing the same connection.
Deno 2.8 routes registry-body decompression through a blocking thread pool,
freeing the event loop for more concurrent requests.
* Tarball extraction split into CPU and I/O phases(#32408). Tarball extract used
to be a single tight loop. It now splits into a CPU-bound decompression phase
and an I/O-bound filesystem write phase. Pairs withlibdeflater + a
preallocated buffer(#32511)
(a faster gzip decoder than the stockflate2) andfewer syscalls during
tarball extraction(#32541).

node:http.Hello-worldnode:httpmore than doubles throughput (2.21x)
and cuts p99 latency by roughly 40%; chunked responses see comparable gains
(1.74xthroughput,1.62xtail latency).

base64 across the board.A single change, switchingbase64encode/decode
tosimdutf(#32743), drives3.07xfasternode:bufferbase64(2,594msdown to844ms) and the same kind of speedup
foratob/btoaand every Web API path that touches base64.

Othernode:*hot paths.scryptSyncfromnode:cryptois now2.12xfaster, Rust-backed recursivenode:fscpSyncgets1.49xfaster, and
exchanging messages overMessagePortbetween Workers is now1.32xfaster.

Deno.serve.NativeDeno.servegot a direct dispatch into the JS handler,
a fast path for fully-buffered response bodies, and lighterVaryhandling
(#33845,#33844,#33892). A hello-world benchmark
sees1.13xincrease in throughput and1.20xlower median p99 latency.

Other optimizations.A pile of smaller wins that show up everywhere:

* TextEncoder/TextDecoderfast paths for ASCII / Latin-1 / short strings
(#32735,#33674,#33675,#34055).
* Linear-timeset/deleteonFormData,URLSearchParams, andHeaders(#33961), no more quadratic
blowups on large header sets.
* URLPatternops drop serde overhead and GC pressure
(#32766), so middleware that
matches every request gets cheaper.
* Zero-copy V8-to-Rust string conversion in op slow-paths
(#32688) and a SIMD ASCII fast
path forop_decode(#33720),
whichResponse.text(),File.text(), and FormData parsing all ride on.
* V8 thread pool capped at 4 threads
(#33697), trimming ~1 MB RSS on
a typical desktop.
* malloc_trimafter module loading
(#32662) and on Worker
termination (#32617), fixing
3–5x RSS bloat on Linux when loading large TypeScript codebases.

## import defer

Deno now supports theTC39 import defer proposal:
a module can be loaded and parsed without running its top-level code. The module
is then only evaluated the first time you touch one of its exports
(#32360).

This feature is useful for trimming startup time when a module is expensive to
evaluate but rarely used on a given codepath.

deferred.js
console
.
log
(
"deferred module evaluated"
)
;

export
 
const
 value 
=
 
42
;
main.js
import
 defer 
*
 
as
 deferred 
from
 
"./deferred.js"
;

console
.
log
(
"before access"
)
;

console
.
log
(
`
value: 
${
deferred
.
value
}
`
)
;

console
.
log
(
"after first access"
)
;
$ deno run main.js
before access
deferred module evaluated
value: 
42

after first access

Thedeferred module evaluatedline lands betweenbefore accessand the
property read. Module evaluation is delayed until something actually needs it.

The same semantics are available withimport.defer()for dynamic imports. A
common pattern: pre-load both branches of a decision, but only evaluate the one
you actually pick.

png-decoder.js
console
.
log
(
"PNG decoder evaluated"
)
;

export
 
function
 
decode
(
bytes
)
 
{
/* ... */
}
jpeg-decoder.js
console
.
log
(
"JPEG decoder evaluated"
)
;

export
 
function
 
decode
(
bytes
)
 
{
/* ... */
}
main.js
const
 png 
=
 
await
 
import
.
defer
(
"./png-decoder.js"
)
;

const
 jpeg 
=
 
await
 
import
.
defer
(
"./jpeg-decoder.js"
)
;

const
 format 
=
 
Deno
.
args
[
0
]
;
 
// "png" or "jpeg"

const
 decoder 
=
 format 
===
 
"png"
 
?
 png 
:
 jpeg
;

const
 bytes 
=
 
Deno
.
readFileSync
(
`
input.
${
format
}
`
)
;

console
.
log
(
decoder
.
decode
(
bytes
)
)
;
$ deno run 
-R
 main.js png
PNG decoder evaluated

Both modules are fetched and parsed up front, but only the selected one is
evaluated.

import deferWorks in.tsand.tsxfiles with no extra setup.deno checkand the LSP both understand the syntax:

main.ts
import
 defer 
*
 
as
 deferred 
from
 
"./deferred.ts"
;

const
 n
:
 
number
 
=
 deferred
.
value
;

Learn more aboutimport defer.

## TypeScript 6.0.3

The bundled TypeScript compiler is updated to 6.0.3
(#32944). 6.0 is a transition
release the TypeScript team uses to land breaking changes and deprecations
before the native-port 7.0 ships; see Microsoft’sAnnouncing TypeScript 6.0post for the full list.

deno check,deno bundle, the LSP, anddeno compileall use the new version
automatically. No flag, no config change.

## lib.nodeincluded by default

deno checkand the LSP now includelib.nodein every type-check by default
(#33823). Before 2.8 you had to
add"node"tocompilerOptions.libindeno.json(or sprinkle/// <reference types="node" />across files) to getNodeJS.*,Buffer,process, and the rest of Node’s ambient types to resolve. Now they’re just
there:

node_globals.ts
// 2.8: type-checks with no `compilerOptions.lib` configuration

const
 buf
:
 
Buffer
 
=
 
Buffer
.
from
(
"hello"
)
;

const
 t
:
 
NodeJS
.
Timeout
 
=
 
setTimeout
(
(
)
 
=>
 
{
}
,
 
0
)
;

console
.
log
(
process
.
versions
.
node
)
;

lib.nodeis implemented on top of@types/node, and Deno pulls that package
from npm whose major version matches the Node release Deno reports inprocess.versions.node. Today that’s the Node 24.x types, in line with the
version returned by:

node_version.ts
console
.
log
(
process
.
versions
.
node
)
;
 
// e.g. 24.2.0

If you’d rather pin a different version of@types/node(for example because
your project standardizes on Node 22, or because you need a newer patch), just
declare it as a dependency and Deno will use yours instead of the bundled copy:

package.json
{

 
"devDependencies"
:
 
{

 
"@types/node"
:
 
"^22.10.0"

 
}

}
deno.json
{

 
"imports"
:
 
{

 
"@types/node"
:
 
"npm:@types/node@^22.10.0"

 
}

}

In practice the default behavior means npm packages with Node-typed APIs (i.e.
nearly all of them) type-check cleanly when imported vianpm:, and library
authors writing for both runtimes can rely onNodeJS.Timeout,Buffer, and
friends without telling Deno consumers to configure their TypeScript.

The trade-off is that Node-only globals likeprocessandBufferare now in
scope at the type level even when you don’t want them, which can quietly
encourage code that won’t run in the browser. Theno-process-globalandno-node-globalslint rules
used to be on by default to catch this; in 2.8 they are off by default but still
available (#33247). Re-enable
them indeno.jsonif your project targets multiple runtimes:

deno.json
{

 
"lint"
:
 
{

 
"rules"
:
 
{

 
"include"
:
 
[
"no-process-global"
,
 
"no-node-globals"
]

 
}

 
}

}

The runtime globals themselves are unchanged. This is purely a type-level
addition.Learn more about including Node types.

## Debugging

A major addition to debugging capabilities in 2.8 is thatChrome DevTools can
now inspect Deno’s network traffic. Run your program with--inspect-wait(or--inspect/--inspect-brk), openchrome://inspectin Chromium, clickInspecton the Deno target, and the DevToolsNetworktab now shows everyfetch(),node:http/node:httpsclient request, andWebSocketyour
program makes (including server-side WebSockets opened viaDeno.upgradeWebSocket()), with request and response headers, status codes,
bodies, and timing, exactly the way you’d see network traffic in a browser tab.

server.ts
const
 res 
=
 
await
 
fetch
(
"https://api.github.com/repos/denoland/deno"
)
;

console
.
log
(
res
.
status
,
 
(
await
 res
.
json
(
)
)
.
stargazers_count
)
;
$ deno run --inspect-wait --allow-net server.ts
Debugger listening on ws://127.0.0.1:9229/
..
.
Visit chrome://inspect to connect to the debugger.
Deno is waiting 
for
 debugger to connect.

Under the hood this required implementing theNetwork CDP domainon the inspector side and wiringfetch(),node:http, andWebSocketinto it
on the runtime side:

The same events also surface throughnode:inspectorfor programmatic clients
and through any other CDP frontend (VS Code’s JavaScript debugger, the
standalonechrome-devtools-frontend, etc.), so tooling that already speaks CDP
against Node can attach to Deno without changes.Learn more about inspecting network traffic.

### CPU profiling

Deno 2.8 ships a built-in CPU profiler that matches Node’s--cpu-profflag, plus a few
extras. Start the profiler with--cpu-profand Deno writes a V8 CPU profile to
disk when the program exits
(#31909):

$ deno run --cpu-prof main.ts
$ 
ls

CPU.20260519.022823.34721.0.001.cpuprofile main.ts

The.cpuprofilefile opens directly in Chrome DevTools (Performancepanel,
thenLoad profile) or any tool that speaks the V8 profile format (eg.V8’sprofview). For times when
you don’t want to load a profile into a UI, two new output formats land
alongside it:

* --cpu-prof-flamegraphwrites a self-contained, interactive SVG you can open
in any browser, no extra tooling required
(#32572).
* --cpu-prof-mdwrites a human-readable Markdown report with the hottest
functions, the call tree, and per-function details.

Combine them in a single run:

$ deno run --cpu-prof --cpu-prof-flamegraph --cpu-prof-md main.ts
$ 
ls

CPU.20260519.022823.34721.0.001.cpuprofile
CPU.20260519.022823.34721.0.001.svg
CPU.20260519.022823.34721.0.001.md

The Markdown report is the fastest way to triage a slow run from a terminal:

#
 CPU Profile

|
 Duration 
|
 Samples 
|
 Interval 
|
 Functions 
|

|
 
-------:
 
|
 
------:
 
|
 
-------:
 
|
 
--------:
 
|

|
 187.81ms 
|
 74 
|
 1000us 
|
 34 
|

**
Top 10:
**
 
`fib`
 100.0%

##
 Hot Functions (Self Time)

|
 Self% 
|
 Self 
|
 Total% 
|
 Total 
|
 Function 
|
 Location 
|

|
 
-----:
 
|
 
------:
 
|
 
-----:
 
|
 
------:
 
|
 
--------
 
|
 
---------
 
|

|
 100.0% 
|
 72.00ms 
|
 100.0% 
|
 72.00ms 
|
 
`fib`
 
|
 main.ts:1 
|

The SVG flamegraph is interactive. Click any frame to zoom, hover to see exact
timings:

Learn more about CPU profiling in Deno.

## Package and workspace management

### catalog:protocol

Monorepos that share dependency versions across packages used to require manual
coordination: every member’spackage.jsonhad to be updated in lockstep when a
shared dep was bumped. Deno 2.8 adopts pnpm’scatalog:protocol, letting you declare versions
once in the workspace root and reference them by name from each member
(#32947).

Declare a default catalog in the workspace root:

deno.json
{

 
"workspace"
:
 
[
"./packages/api"
,
 
"./packages/web"
]
,

 
"catalog"
:
 
{

 
"hono"
:
 
"^4.6.0"
,

 
"zod"
:
 
"^3.23.0"

 
}

}

Then reference it from any member with the barecatalog:specifier:

packages/api/package.json
{

 
"name"
:
 
"api"
,

 
"dependencies"
:
 
{

 
"hono"
:
 
"catalog:"
,

 
"zod"
:
 
"catalog:"

 
}

}

For projects that need multiple catalogs (e.g. one for production, one for build
tooling), use named catalogs under the pluralcatalogsfield:

deno.json
{

 
"workspace"
:
 
[
"./packages/api"
]
,

 
"catalogs"
:
 
{

 
"runtime"
:
 
{
 
"hono"
:
 
"^4.6.0"
 
}
,

 
"tools"
:
 
{
 
"typescript"
:
 
"^6.0.0"
 
}

 
}

}
packages/api/package.json
{

 
"dependencies"
:
 
{
 
"hono"
:
 
"catalog:runtime"
 
}
,

 
"devDependencies"
:
 
{
 
"typescript"
:
 
"catalog:tools"
 
}

}

catalog:also resolves correctly insidepackage.jsonoverrides
(#33799) and inside workspaces
declared in the object form
(#33816), so the protocol works
the same way no matter where you reach for it.Learn more about thecatalog:protocol.

### Cross-platform npm installs

A lot of popular npm packages ship platform-specific native binaries viaoptionalDependencies: esbuild, sharp, rollup, the SWC family, and so on. Deno
reads theosandcpufields declared on each optional dependency, compares
them to the host platform, and only fetches the binary you can actually run.
Installs stay small, fast, and free of untrusted binaries from platforms you
don’t ship to.

The trade-off shows up when you do want a different platform: building a Linux
ARM64 Docker image from a macOS dev laptop, prepping a CI artifact for Windows,
or pre-populating a cache for a deploy target. The new--osand--archflags
ondeno installtell the resolver to pretend it’s on a different host,
mirroringnpm install --os --cpu(#32785):

$ deno 
install
 
--os
=
linux 
--arch
=
arm64

Supported--osvalues:aix,android,darwin,freebsd,linux,openbsd,sunos,win32. Supported--archvalues:arm,arm64,ia32,mips,mipsel,ppc,ppc64,s390,s390x,x64.Learn more about cross-platform installs.

### --prodflag

Production deploys rarely needdevDependenciesor@types/*packages. Until
nowdeno installalways pulled them in anyway, padding the install size and
adding npm packages you don’t actually ship. The new--prodflag skips both
(#33248):

$ deno 
install
 
--prod

Drop it into yourDockerfileor CI release step and your production image gets
only the dependencies it needs to run.Learn more about--prod.

### Hoistednode_modules

Deno’s defaultnode_moduleslayout is isolated: each package gets its own
symlink-resolved tree, so it can only see the dependencies it explicitly
declared. That’s the right default for new projects, but some legacy npm tooling
assumes the flat, hoisted layout thatnpm installproduces, where every
package lives at the top level ofnode_modulesand canrequire()anything it
finds.

deno.jsongets a newnodeModulesLinkerfield for those cases
(#32788):

deno.json
{

 
"nodeModulesDir"
:
 
"manual"
,

 
"nodeModulesLinker"
:
 
"hoisted"

}

Valid values are"isolated"(the default) and"hoisted". Use the latter when
porting an existing Node project that relies on the npm-style layout.Learn more about isolated vs. hoistednode_modules.

### .npmrcsupport

Several gaps in Deno’s.npmrchandling were closed this release.

min-release-ageis the headline addition. The feature itselfshipped in 2.6:
Deno refuses to install a package version younger than the configured age, which
catches the vast majority of npm supply-chain attacks before they land in your
tree (malicious versions are typically detected and yanked within a few days of
publishing). In 2.8 you can also configure it from.npmrc, matching the npm
convention so existing tooling keeps working
(#33983):

.npmrc
min-release-age
=
72h

The remaining improvements unblock common authentication and configuration
scenarios with private registries:

* certfileandkeyfilefor mutual-TLS authentication
(#32655)
* emailfield on_authentries, used by some legacy on-prem registries
(#32616)
* NPM_CONFIG_REGISTRYcorrectly overrides the registry declared in.npmrc(#32394)

Learn more about.npmrcconfiguration.

### file:andlink:dependencies in npm packages

file:andlink:specifiers point at a local path on the publisher’s machine
and only make sense during development. Plenty of published npm packages still
ship with one accidentally left in theirpackage.json:

some-published-package/package.json
{

 
"name"
:
 
"some-package"
,

 
"version"
:
 
"1.2.3"
,

 
"dependencies"
:
 
{

 
"lodash"
:
 
"^4.17.0"
,

 
"local-helpers"
:
 
"file:../local-helpers"

 
}

}

That strayfile:entry used to break Deno with a cryptic error during
resolution:

$ deno 
install

error: Invalid version requirement. Unexpected character.
 some-package@1.2.3 -
>
 local-helpers

In 2.8,file:andlink:specifiers are silently skipped while parsing
registry metadata, so packages that carry stray local-path deps install cleanly
(#32876). The actual code those
deps reference is bundled into the published tarball anyway, so nothing’s lost
by ignoring them.Learn more aboutfile:andlink:dependencies.

### --package-jsonflag

Projects migrating from Node often end up with both apackage.jsonand adeno.json. By default,deno add,deno install,deno remove, anddeno uninstallmodifydeno.jsonbecause that’s where Deno-native projects
keep their dependencies. The new--package-jsonflag forces those subcommands
to targetpackage.jsoninstead, useful when you want the npm-style manifest to
remain the source of truth for your team’s tooling
(#33199):

$ deno 
add
 --package-json express
$ deno 
install
 --package-json
$ deno remove --package-json lodash

Learn more about--package-json.

### Bug fixes

Deno’s package management code is a moving target. Every release brings a lot of
small correctness fixes, and 2.8 is no exception: 35 of them landed. A few worth
calling out explicitly:

* Peer dependency resolutiongot two meaningful improvements: a fix for
cases where a peer dep ended up installed in multiple conflicting versions and
caused hangs (#32358), and
memoization of peer-cache hit checks that previously blew up combinatorially
on large workspaces (#32609).
* Aliasedpackage.jsondependencies("my-name": "npm:foo@1") are now all
linked intonode_modules, not just the canonical one
(#33068).
* Global installsregenerate their lockfile correctly when you pass--force(#33970).
* deno update --lockfile-onlyno longer rewrites your config file
alongside the lockfile, restoring the contract of the--lockfile-onlyname
(#33746).

## deno compileupdates

deno compilekeeps moving toward “point it at a project, get a binary back” as
the default workflow. Two new features cover most of that ground in 2.8, plus a
batch of fixes for binaries that re-launch themselves the way many npm published
CLIs do.

### Framework detection

Runningdeno compile .(ordeno compile ./myapp) now auto-detects the web
framework you’re using, runsdeno task buildto produce build output, and
generates the right entrypoint for it
(#33164). The supported list
covers most of the popular options: Next.js, Astro, Fresh, Remix, SvelteKit,
Nuxt, SolidStart, TanStack Start, and Vite SSR.

$ deno compile 
.

Compile file:///project/main.ts to file:///project/myapp
Detected Vite SSR project
Running deno task build
..
.

..
.

Entrypoints useimport.meta.dirnameso paths resolve against the virtual
filesystem inside the compiled binary, which means a Next.js or Astro build
shipped as a single executable now works without a separate runtime wrapper.Learn more about framework detection.

### Other improvements

For projects with large npm dependency treesdeno compileused to go silent
for tens of seconds. It now reports progress through each phase
(#33874): an animated progress
bar in an interactive terminal, or per-phase log lines in CI and piped output.
Operations that finish in under 120ms render nothing, so fast paths stay quiet.

A batch of fixes targets compiled npm CLIs that re-launch themselves (e.g.@google/gemini-cli).child_process.spawnandchild_process.forkskip the
Node-to-Deno CLI argument translation when running inside a standalone binary
(#32980), the duplicate exe path
is stripped fromargvwhen a standalone binary relaunches itself
(#33016), andprocess.argv[1]now resolves toDeno.execPath()in compiled binaries instead of the entrypoint
URL (#32990). The self-extracting
cache directory also moves to a hidden directory next to the executable
(#32329) so it no longer clutters
the binary’s parent directory.

A few smaller fixes round out the section:--env-fileresolves
parent-directory paths again and a missing env file no longer abortsdeno compile(#32686); bundling
CSS treats same-document fragment URLs as external
(#33492); andDeno.bundlereports a clearer error when called from inside a compiled binary
(#33503).

## OpenTelemetry

Deno’s built-in OpenTelemetry integration gets two new exporters and a way to
route permission audits straight into your OTel pipeline.

### Console exporter

SetOTEL_EXPORTER_OTLP_PROTOCOL=consoleto print spans, logs, and metrics to
stderr in a human-readable format. No collector required. Handy when you’re
debugging instrumentation locally
(#32717).

$ 
OTEL_DENO
=
true 
OTEL_EXPORTER_OTLP_PROTOCOL
=
console deno run 
-A
 main.ts
SPAN outer span 
[
00000000000000000000000000000001/0000000000000001
]
 Internal 1ms
 scope: example-tracer
SPAN inner span 
[
00000000000000000000000000000001/0000000000000002
]
 Internal 0ms
 parent: 0000000000000001
 scope: example-tracer
 key: value
LOG 
[
INFO
]
 
"hello from inner"

 scope: deno
 trace: 00000000000000000000000000000001/0000000000000002

### gRPC OTLP exporter

The OTLP exporter now speaks gRPC alongside the existing HTTP/protobuf
transport. Point it at your collector’s gRPC port and you’re done
(#30365).

$ 
OTEL_DENO
=
true 
\

 
OTEL_EXPORTER_OTLP_PROTOCOL
=
grpc 
\

 
OTEL_EXPORTER_OTLP_ENDPOINT
=
https://otel.example.com:4317 
\

 deno run 
-A
 main.ts

### Permission audits as OTel logs

The permission audit log (introduced in 2.5) can now be fed straight into your
OTel exporter. SetDENO_AUDIT_PERMISSIONS=oteland every permission check
becomes an OTel log event correlated with the surrounding span, so you can alert
on unexpected file or network access across your fleet without scraping JSONL
files (#32501).

$ 
OTEL_DENO
=
true 
DENO_AUDIT_PERMISSIONS
=
otel deno run 
-A
 main.ts

Learn more about OpenTelemetry in Deno.

### Other improvements

* Span attributes copied from HTTP requests onto per-route metrics
(#32720)
* Array values supported in OTel attribute maps
(#32748)
* Server spans for 4xx responses no longer marked as errors
(#32722)
* log.iostreamattribute added to console logs
(#32723)
* exception.*attributes added to OTel log records
(#32726)

## Testing and coverage

Deno’s built-in test runner and coverage tool both pick up a few useful
improvements this release.

### Sanitizers off by default

ThesanitizeOpsandsanitizeResourcesoptions onDeno.test()now default
tofalseinstead oftrue(#33250). These sanitizers fail a
test when async ops or resources outlive it, and in practice they have been a
frequent source of confusing failures, especially for code that usessetTimeout,node:http, or other APIs whose cleanup is loosely scoped. The
new default matches what most people expect: tests pass when their assertions
pass, and you opt back into the stricter behavior when you actually want it.

You can re-enable sanitizers for a single test:

leak_test.ts
Deno
.
test
(

 
"leaks a timer"
,

 
{
 sanitizeOps
:
 
true
,
 sanitizeResources
:
 
true
 
}
,

 
(
)
 
=>
 
{

 
setTimeout
(
(
)
 
=>
 
{
}
,
 
1000
)
;

 
}
,

)
;

…for every test in a file via the new module-level API:

strict_test.ts
// Apply to every Deno.test() in this file.

Deno
.
test
.
sanitizer
(
{
 ops
:
 
true
,
 resources
:
 
true
 
}
)
;

Deno
.
test
(
"leaks a timer"
,
 
(
)
 
=>
 
{

 
setTimeout
(
(
)
 
=>
 
{
}
,
 
1000
)
;

}
)
;

…or globally indeno.json:

{
 "test": {
 "sanitizeOps": true,
 "sanitizeResources": true
 }
}

Learn more about test sanitizers.

### Per-test timeouts

Deno.test()now accepts atimeoutoption (in milliseconds) that fails a test
if it runs longer than expected, instead of hanging your CI run
(#33815):

slow_test.ts
Deno
.
test
(
"slow operation"
,
 
{
 timeout
:
 
100
 
}
,
 
async
 
(
)
 
=>
 
{

 
await
 
new
 
Promise
(
(
r
)
 
=>
 
setTimeout
(
r
,
 
500
)
)
;

}
)
;
$ deno 
test

slow operation 
..
. FAILED 
(
102ms
)

 ERRORS

slow operation 
=
>
 ./server_test.ts:5:6
error: Test timed out after 100ms.

The timeout is per-test, so a slow test no longer drags down everything else in
the suite. Pair it with--parallelto keep total wall-clock time predictable.Learn more about test timeouts.

### Function coverage

deno coveragenow reports per-function coverage alongside line and branch
coverage in both the text summary and the HTML report
(#32507). Useful when a file has
high line coverage but most of its API surface is untested:

$ deno 
test
 
--coverage
=
cov
$ deno coverage cov

|
 File 
|
 Branch % 
|
 Function % 
|
 Line % 
|

|
 --------- 
|
 -------- 
|
 ---------- 
|
 ------ 
|

|
 math.ts 
|
 
100.0
 
|
 
66.7
 
|
 
66.7
 
|

|
 All files 
|
 
100.0
 
|
 
66.7
 
|
 
66.7
 
|

In this example two of three exported functions inmath.tsare tested: line
and function coverage agree here, but the new column makes it obvious at a
glance which functions are missing tests. Line percentage alone can hide that
when a file has a few large untested functions.Learn more about function coverage.

### Other fixes

* deno testdedupes test modules discovered through multiple workspace members
so each test only runs once
(#32380)
* deno test --watchrestarts the suite when an--env-filechanges, matching
the watch behavior for source edits
(#32461)
* Coverage line and branch counts are now correct in edge cases involving
partially overlapping zero-count ranges
(#32312)
* deno coveragewarns instead of erroring out when a source file referenced by
the profile is missing, so a stale data file doesn’t kill the whole report
(#32398)

## Web APIs

Deno 2.8 keeps closing the gap with the browser platform, with two new APIs,
expanded Web Crypto coverage, and a long tail of fixes and perf wins acrossfetch, streams,TextEncoder/TextDecoder, and friends.

### Canvas and geometry primitives

Two browser-platform APIs that server-side code has long been asking for:OffscreenCanvas(#29357) lands
as a stable global, and theGeometry Interfaces Module Level 1spec is
implemented behind--unstable-webgpu(#27527).

OffscreenCanvasis the same API the browser exposes for off-thread canvas
work: create a canvas without a DOM, get a rendering context, and transfer it
between workers viapostMessage. Deno’s implementation supports the"bitmaprenderer"and"webgpu"contexts (the"2d"and WebGL contexts are
not implemented andgetContextreturnsnullfor them). A common pattern is
to decode an image, place the resultingImageBitmapon the canvas, and encode
the canvas back out viaconvertToBlob:

thumb.ts
const
 res 
=
 
await
 
fetch
(

 
"https://images.unsplash.com/photo-1469474968028-56623f02e42e?w=480"
,

)
;

const
 bitmap 
=
 
await
 
createImageBitmap
(
await
 res
.
blob
(
)
)
;

const
 
{
 width
,
 height 
}
 
=
 bitmap
;

const
 canvas 
=
 
new
 
OffscreenCanvas
(
width
,
 height
)
;

const
 ctx 
=
 canvas
.
getContext
(
"bitmaprenderer"
)
!
;

ctx
.
transferFromImageBitmap
(
bitmap
)
;
 
// consumes the bitmap

const
 out 
=
 
await
 canvas
.
convertToBlob
(
{
 type
:
 
"image/png"
 
}
)
;

await
 
Deno
.
writeFile
(
"out.png"
,
 
new
 
Uint8Array
(
await
 out
.
arrayBuffer
(
)
)
)
;
$ deno run --allow-net --allow-write
=
. thumb.ts

That covers headless format conversion, thumbnail generation, and social-card
rendering without a headless browser. Pair it with the"webgpu"context for
off-window GPU-rendered targets.

The geometry interfaces addDOMPoint,DOMRect,DOMQuad, andDOMMatrix(plus theirReadonlyvariants). These are the same matrix and rectangle types
the browser uses for transforms and hit-testing, and they’re the missing
primitive for code that wants to share geometry math between the browser and
Deno:

geometry.ts
const
 m 
=
 
new
 
DOMMatrix
(
)

 
.
translate
(
100
,
 
50
)

 
.
rotate
(
30
)

 
.
scale
(
2
)
;

const
 p 
=
 
new
 
DOMPoint
(
10
,
 
0
)
.
matrixTransform
(
m
)
;

console
.
log
(
p
.
x
,
 p
.
y
)
;
 
// 117.32050807568878 60

const
 r 
=
 
new
 
DOMRect
(
0
,
 
0
,
 
100
,
 
50
)
;

console
.
log
(
r
.
right
,
 r
.
bottom
)
;
 
// 100, 50
$ deno run --unstable-webgpu geometry.ts

Learn more about OffscreenCanvasandGeometry Interfaces.

### Cloneable and transferable values

The web platform draws a careful line between two ways of moving JavaScript
values across realm and worker boundaries:serializable objectscan be deep-copied withstructuredClone,
andtransferable objectscan have their ownership moved with zero copy. Deno 2.8 closes long-standing
gaps in both, so you can finally write efficient multi-threaded programs without
serializing state to JSON by hand.

The headline fix is that non-serializable Web types are finally transferable
when correctly listed in thetransferarray ofstructuredCloneorpostMessage(#33491):

transfer.js
const
 stream 
=
 
new
 
ReadableStream
(
{

 
start
(
c
)
 
{

 c
.
enqueue
(
"hello"
)
;

 c
.
close
(
)
;

 
}
,

}
)
;

// Before 2.8: threw DataCloneError.

// 2.8: ownership of `stream` moves into the cloned value.

const
 cloned 
=
 
structuredClone
(
{
 stream 
}
,
 
{
 
transfer
:
 
[
stream
]
 
}
)
;

worker
.
postMessage
(
{
 
stream
:
 cloned
.
stream
 
}
,
 
[
cloned
.
stream
]
)
;

The full set of types Deno can now transfer isHeaders,Request,Response,ReadableStream,WritableStream,
andTransformStream.
The full set of types Deno can now serialize (deep-copy) isBlob,File,CryptoKey,DOMException,X509Certificate,EventLoopDelayHistogram,
andRecordableHistogram.

Learn more aboutstructuredCloneand transferable objects.

### Other fixes

* crypto.subtle.digestaccepts"SHA3-256","SHA3-384", and"SHA3-512"(#32342).
* P-521 (the largest NIST curve) gains first-class support across sign, verify,
and ECDH derive (#32602), with
EC key export fixed for all formats
(#32412,#34087). Importing X25519,
X448, and Ed25519 raw keys also validates their length now instead of silently
accepting any byte string
(#33944).
* CacheStorage.keys()andCache.keys()are implemented
(#33275), filling in the
iteration entry points on the Cache API.
* AbortSignal.any()no longer leaks memory when wrapping long-lived signals
(#32916).
* subtle.importKeyno longer panics on a wrong algorithm name
(#32410); it throws as
specified.
* getRandomValuesthrowsTypeMismatchErrorfor non-TypedArrayinputs
(#33470).
* fetchretries on stale pooled HTTP/1.1 connections
(#32566) and stops mutating the
caller’s options inDeno.createHttpClient(#33497). The response resource
is closed cleanly when an abort races op completion
(#33928), and NodeReadablerequest bodies stream through a byteReadableStream(#33432).
* Deno.listenDatagramdefaults its hostname to0.0.0.0(#33496), matchingDeno.listen.
* HTTP upgrade handlers can now reject with non-101 status codes
(#32615), an emptyHostheader is treated as missing
(#33234), and a WebSocket H2
stream reset no longer panics
(#33982).
* MessageEventports convert via the WebIDL sequence iteration protocol
(#33652), andsourceis now
retained fromMessageEventInit(#33500).
* A few Node-aligned error code touch-ups:ERR_MISSING_ARGSonURL.revokeObjectURL()(#33471),ERR_ILLEGAL_CONSTRUCTOR(#33535) andERR_INVALID_THIS(#33467) on the correspondingTypeErrors, andAbortSignal.timeout’s error message matches Node’s
(#33460).
* console.logsupports the%jJSON format specifier
(#32684), andconsole.dirxmlnow routes through the log printer
(#33443).
* QuotaExceededErroris upgraded to aDOMException-derived interface
(#32244),removeEventListenerhandles anulloptions argument
(#32605), andEvent.returnValuerespects thecancelableandpassiveflags
(#33651).
* ReadableStreamBYOBRequest.viewis narrowed toUint8Array(#33477), a late write racing
withTransformStream.cancelno longer hangs
(#33478), and aWebTransportdatagram-overflow infinite loop is fixed
(#33075).
* GPUQueue.writeBuffer()accepts plainArrayBufferdata sources
(#33152).
* WebSocket response headers handle non-ASCII bytes correctly
(#32594).

## Task runner

deno taskgot a small quality-of-life improvement that matters once you start
running tasks in parallel: every output line is now prefixed with the task name
that produced it, so interleaved stdout from concurrent tasks no longer reads as
one tangled stream (#33805).
Given a config that fans out to two builds:

deno.json
{

 
"tasks"
:
 
{

 
"client"
:
 
"echo building client && sleep 1 && echo client ready"
,

 
"server"
:
 
"echo building server && sleep 1 && echo server ready"
,

 
"dev"
:
 
{
 
"dependencies"
:
 
[
"client"
,
 
"server"
]
 
}

 
}

}

…runningdeno task devinterleaves the two scripts cleanly:

$ deno task dev
Task client 
echo
 building client 
&&
 
sleep
 
1
 
&&
 
echo
 client ready

[
client
]
 building client
Task server 
echo
 building server 
&&
 
sleep
 
1
 
&&
 
echo
 server ready

[
server
]
 building server

[
client
]
 client ready

[
server
]
 server ready

deno task
 fanning out to three child tasks in parallel, with each output line prefixed and color-coded by task name.

The prefixes are color-coded per task and stay attached even when a task forks
subprocesses, so a parallelbuild+test+lintworkflow stays legible
without piping everything through a separate multiplexer.

The task shell itself also picks up a couple of POSIX features:set -e/set -o errexit(andset +eto turn it back off) aborts the surrounding
sequential list on the first non-zero exit, and the POSIX null command:is
now a builtin. Both make it easier to port shell scripts intotasksblocks
without resorting to a separatebash -cwrapper.

The rest of the changes are workspace fixes that make--filterand recursive
task discovery match user expectations:

* --filternow matches a workspace member by directory name as well as package
name (#33499), and falls back
to the directory name only when an explicit workspace root check passes
(#33540)
* Recursive task name completion works inside workspaces, so shell
tab-completion sees tasks declared in any member
(#32422)
* Backticks in arguments forwarded to a task are escaped correctly instead of
being re-evaluated by the task shell
(#34151)

Learn more about task dependencies and parallel output.

## deno upgradechanges

Two improvements todeno upgradeworth flagging: it’s a lot smaller over the
wire now, and you can use it to grab a Deno build straight from a PR.

### Delta updates

deno upgradenow downloads a binary diff between your current version and the
target instead of the full release archive, when one is available
(#33274). A typical patch-level
upgrade goes from a roughly 48 MB download to 3-6 MB, an 87-93% bandwidth
reduction. Useful for everyone, but especially for CI runners and ephemeral
environments that pull Deno on every job.

The implementation chains up to threebsdiffpatches to reach the target (e.g.
2.7.14 to 2.8.0 to 2.8.1 to 2.8.2). Every patch and every intermediate binary is
SHA-256-checked against the published checksums, so a bad delta can’t quietly
corrupt your install. If any step fails (missing delta asset, checksum mismatch,
patch error), Deno transparently falls back to a full download. The--no-deltaflag forces the full path if you ever want to bypass deltas entirely.Learn more about delta updates.

### Install from a PR

deno upgrade pr <number>downloads the binary that CI built for a given pull
request and replaces your localdenowith it, so you can try a fix or new
feature without building from source
(#33252). It uses theghCLI under the hood, so you need it installed and
authenticated:

# Try the binary CI built for PR #34227

$ deno upgrade 
pr
 
34227

# Save to a path instead of replacing your current install

$ deno upgrade 
--output
 ./deno-pr 
pr
 
34227

# See what would happen without doing it

$ deno upgrade --dry-run 
pr
 
34227

Under the hooddeno upgradequeriesgh pr view, walks the PR’s CI runs to
find the right artifact for your platform (preferring release over debug),
downloads it, sanity-checks it withdeno -V, then swaps it in. Faster than agit clone && cargo buildround-trip when you just want to verify a fix.Learn more about installing a build from a PR.

## Module loader hooks

Technically a piece of Node.js API compatibility, but big enough to deserve its
own section: Deno 2.8 implements Node’smodule.registerHooks()API (#34081). Loader hooks let
you customize module loading at runtime: intercept resolution, transform source,
redirect specifiers, mock dependencies for tests, or add instrumentation, all
without rebuilding Deno or running a separate build step.

As a concrete example, here’s a 14-line loader that teaches Deno how toimporta.cssfile as the stylesheet text:

css-loader.ts
import
 
module
 
from
 
"node:module"
;

module
.
registerHooks
(
{

 
load
(
url
,
 context
,
 nextLoad
)
 
{

 
if
 
(
!
url
.
endsWith
(
".css"
)
)
 
{

 
return
 
nextLoad
(
url
,
 context
)
;

 
}

 
const
 css 
=
 
Deno
.
readTextFileSync
(
new
 
URL
(
url
)
)
;

 
return
 
{

 format
:
 
"module"
,

 source
:
 
`
export default 
${
JSON
.
stringify
(
css
)
}
;
`
,

 shortCircuit
:
 
true
,

 
}
;

 
}
,

}
)
;
button.css
.button
 
{

 
padding
:
 
8
px
 
16
px
;

 
border-radius
:
 
4
px
;

 
background
:
 
#66c2ff
;

}

Pre-load the hooks with--importso they register before user code runs:

main.ts
import
 
buttonCss
 
from
 
"./button.css"
;

console
.
log
(
buttonCss
)
;
$ deno run --allow-read 
--import
 ./css-loader.ts main.ts
.button 
{

 padding: 8px 16px
;

 border-radius: 4px
;

 background: 
#66c2ff;

}

You could also get a CSS file as text via the standardimport attributesproposal
(import css from "./button.css" with { type: "text" }) thatwe shipped back in Deno v2.4. The point of the example above isn’t.cssspecifically; it’s showing the
mechanics of writing a custom loader for arbitrary file types or
transformations.

Loader hooks also work inside binaries produced bydeno compile, which makes
them useful for distributing self-contained CLIs that ship with custom
resolution baked in. Here’s a virtual-module loader that exposes avirtual:greetingspecifier from inside the compiled binary:

greeter.ts
import
 
module
 
from
 
"node:module"
;

module
.
registerHooks
(
{

 
resolve
(
specifier
,
 context
,
 nextResolve
)
 
{

 
if
 
(
specifier 
!==
 
"virtual:greeting"
)
 
{

 
return
 
nextResolve
(
specifier
,
 context
)
;

 
}

 
return
 
{
 url
:
 
"virtual:greeting"
,
 shortCircuit
:
 
true
 
}
;

 
}
,

 
load
(
url
,
 context
,
 nextLoad
)
 
{

 
if
 
(
url 
!==
 
"virtual:greeting"
)
 
return
 
nextLoad
(
url
,
 context
)
;

 
return
 
{

 format
:
 
"module"
,

 source
:
 
`
export default "Hello from a virtual module!";
`
,

 shortCircuit
:
 
true
,

 
}
;

 
}
,

}
)
;

const
 
{
 
default
:
 greeting 
}
 
=
 
await
 
import
(
"virtual:greeting"
)
;

console
.
log
(
greeting
)
;
$ deno compile 
-A
 
--output
 greeter greeter.ts
$ ./greeter
Hello from a virtual module
!

We chose not to implement themodule.register()API, since Node has deprecated it and plans to remove it.

Learn more about module loader hooks in Deno.

## setTimeoutandsetInterval

A change we’ve been planning for a long timefinally lands in 2.8:setTimeoutandsetIntervalnow return Node’sTimeoutobject instead of an opaque number, matchingnode:timersbehavior at the
global scope (#33249).

This is technically a breaking change, but in practice it should affect very few
programs. The common case keeps working untouched:

timer.ts
const
 t 
=
 
setTimeout
(
(
)
 
=>
 
console
.
log
(
"hi"
)
,
 
1000
)
;

clearTimeout
(
t
)
;

The only code that breaks is code that relied on the return value being anumber, e.g. storing it in anumber-typed field, doing arithmetic on it, or
runtime-checking its type:

timer_id.ts
// Before 2.8: id was a number

const
 id
:
 
number
 
=
 
setTimeout
(
fn
,
 
0
)
;

// 2.8: assign to NodeJS.Timeout instead

const
 id
:
 
NodeJS
.
Timeout
 
=
 
setTimeout
(
fn
,
 
0
)
;
timer_check.ts
// Before 2.8: timer was a number, this branch ran

if
 
(
typeof
 timer 
===
 
"number"
)
 
{

 
clearTimeout
(
timer
)
;

}

// 2.8: timer is a NodeJS.Timeout object, branch never runs.

// Just clear unconditionally:

clearTimeout
(
timer
)
;

Why is it worth even this small amount of churn? Three reasons:

1. Performance.The compatibility shim we used to wrap web-stylesetTimeoutaroundnode:timerssat on a hot event-loop path. Removing it
cuts overhead on every timer call.
2. Tech debt.Maintaining two parallel timer implementations (web and Node)
plus a global proxy that converted between them was a constant source of
subtle bugs.
3. Simpler mental model.There is now one globalsetTimeoutin Deno, it
behaves the waynode:timersdoes, and the sameTimeoutobject flows
through both styles of code. The global proxy that used to intercept these
calls is gone.

TheNodeJS.Timeouttype used above resolves out of the box, thanks tolib.nodenow being included by default.

## Miscellaneous

A few smaller changes worth flagging that don’t fit neatly under any of the
sections above:

* TheNODE_EXTRA_CA_CERTSenvironment variable is now honored at the root
certificate store level
(#33148), so extra CA
certificates apply to every TLS code path:fetch(),Deno.connectTls(),node:https, andnode:tls. Useful behind corporate MITM proxies or when you
need to trust an internal CA across a whole script.
* Linux release builds run again on systems with glibc older than 2.27
(#33259), restoring
compatibility with a long tail of older distros and CI images.
* deno compileconfiguration growsincludeandexcludefields, so you can
declare bundled data files indeno.jsoninstead of repeating--includeflags on every invocation
(#33024,docs).
* Several additional Unix-style signals (SIGUSR1,SIGUSR2, and others) are
now usable on Windows for Node compatibility
(#32689).
* deno xaccepts a--package/-pflag for the case where the package name
differs from the binary name (e.g. runningtscfromnpm:typescript)
(#32855).
* deno evalauto-detects CommonJS vs ES module syntax in the input snippet, so
quick one-liners work without picking a flag
(#32472).
* Deno.upgradeWebSocketnow wires up cleanly tonode:httpupgrade events, so
Node-style servers can hand off WebSocket connections to Deno’s native
implementation (#33342).
* Deno.watchFspaths are normalized so events no longer carry leading./segments that broke string-equality checks against the watched paths
(#33490).
* FFI calls hold onto their argument backing stores for the duration of the
call, preventing a use-after-free when async FFI work outlives the caller’s
stack frame (#32775).
* The event loop now wakes correctly when V8 posts foreground tasks from
background threads, fixing a class of subtle hangs around async module
evaluation (#32450).
* deno_graphis bumped to 0.108.2 for proper handling of WebAssembly
multi-value return types
(#34070).
* deno doclearns to render npm packages
(#32435), with follow-up fixes
for npm entrypoints that ship without types
(#34147). The HTML output also
picks up Prism highlighting for JSX/TSX code blocks
(#33255) and cleaner operator
rendering in dark mode
(#33267).
* --watchrestarts now sendSIGTERMand dispatchunload/process.exitbefore tearing the process down, so cleanup handlers actually run
(#32564,#32664). The grace period
before the hard kill drops from 5 seconds to 500 milliseconds
(#33099), and--watch-excludepatterns are now respected for every file change event, not just the initial
scan (#33854).
* Text imports (with { type: "text" }) are stable and no longer require--unstable-raw-imports(#34238,introduced in 2.4). Bytes imports
(with { type: "bytes" }) remain behind the flag.Learn more about import attributes.
* deno publishno longer panics during provenance generation when run on CI
providers other than GitHub
(#33802).
* Vite’simport.meta.hotreferences now type-check correctly
(#32127).

## V8 14.9

Deno 2.8 upgrades the V8 engine from 14.6 to14.9(#34226).

## Acknowledgments

We couldn’t build Deno without the help of our community! Whether by answering
questions in our communityDiscord serverorreporting bugs, we are incredibly
grateful for your support. In particular, we’d like to thank the following
people for their contributions to Deno 2.8: Amol Yadav, Ashwin Naren, Avocet,
BitToby, Dan Dascalescu, Daniel Osvaldo Rahmanto, Daniil Sivak, David Sherret,
em, Felipe Cardozo, Fibi, Hajime-san, Hunnyboy1217, Janosh Riebesell, Jean
Ibarz, Jimmy, John L. Carveth, Josh Fleming, kaju, Kenta Moriuchi, Kit Dallege,
KnorpelSenf, KT, Kyle Kelley, Lach, Leo Zaki, lif, Luca Barbato, Luna, Marvin
Hagemeister, Michael Horstmann, Nayeem Rahman, Nik B, Olivér Falvai, Pietro
Marchini, r3wretrhy, Rano | Ranadeep, Rohan Santhosh Kumar, RoomWithOutRoof,
Shivam Tiwari, tmimmanuel, Varun Chawla, and web-dev0521.

Would you like to join the ranks of Deno contributors?Check out our contribution docs here,
and we’ll see you on the list next time.

Believe it or not, the changes listed above still don’t tell you everything that
got better in 2.8. You can view thefull list of pull requests merged in Deno 2.8 on GitHub.

That’s all for 2.8, thanks for reading and see you in the next release.