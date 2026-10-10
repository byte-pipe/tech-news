---
title: Bun v1.4.3 | Bun Blog
url: https://bun.com/blog/bun-v1.4.3
site_name: tldr
content_file: tldr-bun-v143-bun-blog
fetched_at: '2026-10-10T16:08:00.375171'
original_url: https://bun.com/blog/bun-v1.4.3
date: '2026-10-10'
published_date: '2026-10-10T03:18:05.517Z'
description: Fixes 166 issues, addressing 122 👍. bun check, a TypeScript type checker built into Bun that is 3x to 6.4x faster than tsc 7, --check for bun run, bun build and bun test, 67–89% less idle CPU, Bun.FetchSession, experimental Bun.ModuleGraph, --disallow-code-generation-from-strings, up to 2.7x faster large node:http responses, a JavaScriptCore upgrade with faster JSON.parse, faster rejected-promise handling, CompressionStream compression levels, If-Range support in Bun.serve, bun install skips tarballs it won't install, lower bun build memory with many entry points, [hashN] output names, profile-guided bytecode layout and faster startup for --compile --bytecode, and many bugfixes and Node.js compatibility improvements.
tags:
- tldr
---

#### To install Bun

curl
npm
powershell
scoop
brew
docker

curl

curl -fsSL https://bun.sh/install 
|
 bash

npm

npm install -g bun

powershell

powershell -c 
"
irm bun.sh/install.ps1|iex
"

scoop

scoop install bun

brew

brew tap oven-sh/bun
brew install bun

docker

docker pull oven/bun
docker run --rm --init --ulimit memlock=-1:-1 oven/bun

#### To upgrade Bun

bun upgrade

## bun check: a TypeScript type checker built into Bun#

bun checkis an incredibly fast TypeScript type checker that passes 100% of TypeScript 7.0.2's conformance test suite.

bun check
1 | 
import
 { greet } 
from
 
"
./user
"
;

2 |

3 | 
const
 message 
=
 
greet
({ id
:
 
"
1
"
, name
:
 
"
Ada
"
 });

 
^

error
: 
TS2322: Type 'string' is not assignable to type 'number'.

 at 
src/index.ts
:
3
:
25

Found 1 error
 in 1 file
, checked 2 files [14.00ms]

It's 3x to 6.4x faster thantsc7.0.2, on a 16-core Apple silicon Mac:

Project
Files
bun check
tsc
 7.0.2
Faster
VS Code 
src
9,795
1.24 s
5.98 s
4.8x
mikro-orm
2,883
1.20 s
5.97 s
5.0x
Next.js 
packages/next
2,881
0.28 s
1.82 s
6.4x
Next.js, root
3,547
0.42 s
1.28 s
3.1x
Storybook 
scripts
1,039
0.27 s
0.96 s
3.5x
Nuxt
839
0.27 s
0.80 s
3.0x
Playwright
706
0.15 s
0.64 s
4.2x
lit 
packages/react
6
0.46 s
2.12 s
4.6x

And it uses 2.2x to 4.9x less memory:

Project
Files
bun check
tsc
 7.0.2
Less
VS Code 
src
9,795
2.14 GB
7.97 GB
3.7x
mikro-orm
2,883
1.35 GB
6.67 GB
4.9x
Next.js 
packages/next
2,881
0.71 GB
1.81 GB
2.5x
Next.js, root
3,547
0.55 GB
1.33 GB
2.4x
Storybook 
scripts
1,039
0.56 GB
1.39 GB
2.5x
Nuxt
839
0.51 GB
1.14 GB
2.2x
Playwright
706
0.46 GB
1.06 GB
2.3x
lit 
packages/react
6
0.24 GB
0.63 GB
2.6x

It's a port oftypescript-go. It reads yourtsconfig.json, reports the same errors astsc, and uses every CPU core. You don't need thetypescriptpackage installed.

It only type checks. It doesn't emit JavaScript or.d.tsfiles, and there's no language server, so your editor keeps using TypeScript.

### bun run --check#

Type check, then run. If there's a type error, your code doesn't run.

bun run --check src/index.ts
1 | 
import
 { greet } 
from
 
"
./user
"
;

2 |

3 | 
console.
log
(
greet
({ id
:
 
"
1
"
, name
:
 
"
Ada
"
 }));

 
^

error
: 
TS2322: Type 'string' is not assignable to type 'number'.

 at 
src/index.ts
:
3
:
21

2 | 
 id: number;

 
^

note
: 
The expected type comes from property 'id' which is declared here on type 'User'

 at 
src/user.ts
:
2
:
3

Found 1 error
 in 1 file
, checked 2 files [24.00ms]

It also works withpackage.jsonscripts (bun run --check dev) and with--watch, which checks again before every restart.

### bun test --check#

Type check the test files and everything they import, then run the tests. If there's a type error, no tests run.

bun 
test
 --check
bun test 
v1.4.3

4 | 
test
(
"
greet
"
, () 
=>
 {

5 | 
 
expect
(
greet
({ id
:
 
"
1
"
, name
:
 
"
Ada
"
 })).
toBe
(
"
hello Ada
"
);

 
^

error
: 
TS2322: Type 'string' is not assignable to type 'number'.

 at 
src/user.test.ts
:
5
:
18

2 | 
 id: number;

 
^

note
: 
The expected type comes from property 'id' which is declared here on type 'User'

 at 
src/user.ts
:
2
:
3

Found 1 error
 in 1 file
, checked 2 files [23.94ms]

### bun build --check#

Type check, then bundle. A type error fails the build like any other build error, and nothing is written.

bun build --check ./src/index.ts --outdir out
3 | 
console.
log
(
greet
({ id
:
 
"
1
"
, name
:
 
"
Ada
"
 }));

 
^

error
: 
TS2322: Type 'string' is not assignable to type 'number'.

 at 
/app/src/index.ts
:
3
:
21

2 | 
 id: number;

 
^

note
: 
TS6500: The expected type comes from property 'id' which is declared here on type 'User'

 at 
/app/src/user.ts
:
2
:
3

Bun.buildtakescheck: true.

### Testingbun check#

Every commit of Bun runs TypeScript 7.0.2's complete conformance test suite (and we will continue to keep it up-to-date as TypeScript itself updates).

Baseline
What it checks
Tests
Passing
Errors
Every error
13,101
13,101
Types
The type of every expression
12,463
12,463
Symbols
The symbol behind every name
12,463
12,463
Declarations
Emitted 
.d.ts
 files
13,032
13,032
Module resolution
How every import resolves
151
151
Total
51,210
51,210

#### 72 misconfigured open-source projects

For a project as complex as a TypeScript type checker, conformance tests aren't enough, so we deliberately misconfigured 72 popular open-source repositories and comparedbun check's output withtsc's output.

Missingnode_modules, mismatched TypeScript versions, no build step. Every error has to match: same file, line, column and error code.

Project
Configs
Identical
Errors
Mismatches
anthropics/anthropic-sdk-typescript
16
16
596
0
apollographql/apollo-client
7
7
559
0
arktypeio/arktype
5
5
389
0
axios/axios
1
1
105
0
colinhacks/zod
10
10
191
0
date-fns/date-fns
3
3
1
0
discordjs/discord.js
2
2
3
0
drizzle-team/drizzle-orm
3
3
10,786
0
Effect-TS/effect
10
10
2
0
elysiajs/elysia
4
4
53
0
excalidraw/excalidraw
7
7
11,048
0
fabian-hiller/valibot
2
2
1
0
fastify/fastify
1
1
0
0
gcanti/fp-ts
2
2
3
0
gcanti/io-ts
2
2
3
0
graphql/graphql-js
3
3
24
0
gvergnaud/ts-pattern
2
2
2
0
honojs/hono
6
6
14,239
0
immerjs/immer
1
1
5
0
jquense/yup
1
1
1
0
kysely-org/kysely
6
6
1,185
0
langchain-ai/langchainjs
41
41
5,273
0
lit/lit
34
34
2,588
0
microsoft/playwright
4
4
22
0
microsoft/TypeScript
4
4
613
0
microsoft/vscode
, its own build
1
1
0
0
microsoft/vscode, extensions and tests
105
105
5,685
0
mikro-orm/mikro-orm
17
17
87,981
0
millsp/ts-toolbelt
1
1
3
0
mobxjs/mobx
3
3
186
0
mswjs/msw
10
10
5,878
0
nestjs/nest
30
30
27,345
0
nuxt/nuxt
3
3
11
0
openai/openai-node
4
4
6
0
pmndrs/jotai
2
2
7
0
pmndrs/valtio
1
1
0
0
pmndrs/zustand
1
1
0
0
preactjs/preact
1
1
1
0
prisma/prisma
44
44
24,201
0
puppeteer/puppeteer
10
10
2,701
0
react-hook-form/react-hook-form
2
2
3
0
ReactiveX/rxjs
10
10
22,271
0
reduxjs/redux
1
1
0
0
reduxjs/redux-toolkit
8
8
142
0
remeda/remeda
7
7
13
0
remix-run/react-router
14
14
6,735
0
rollup/rollup
9
9
107
0
sequelize/sequelize
16
16
6,768
0
sindresorhus/got
1
1
2
0
sindresorhus/ky
2
2
52
0
sindresorhus/type-fest
2
2
0
0
solidjs/solid
7
7
740
0
statelyai/xstate
8
8
545
0
storybookjs/storybook
19
19
1,401
0
stripe/stripe-node
4
4
42
0
sveltejs/svelte
5
5
186
0
TanStack/form
13
13
124
0
TanStack/query
15
15
686
0
TanStack/router
29
29
4,853
0
TanStack/table
20
20
574
0
tldraw/tldraw
4
4
0
0
total-typescript/ts-reset
2
2
4
0
typeorm/typeorm
4
4
959
0
typescript-eslint/typescript-eslint
35
35
18,392
0
unjs/h3
1
1
0
0
unjs/nitro
5
5
742
0
urql-graphql/urql
2
2
17
0
vercel/ai
52
52
9,742
0
vercel/next.js
356
356
3,690
0
vercel/swr
4
4
314
0
vitest-dev/vitest
18
18
2,111
0
vuejs/core
6
5
1,359
1
withastro/astro
12
12
1,996
0
All 72
1,103
1,102
286,267
1

The one mismatch is in vuejs/core.tsconly reports that error whenglobal.tscomes beforemodel.tsinfiles.

We ran 69 of them again under 11 other sets of compiler options:

Compiler options
Projects
Identical
Errors
Mismatches
Every strictness flag on
69
69
100,756
0
strict
 off
69
68
76,960
12
skipLibCheck
 off
69
69
90,609
0
checkJs
69
69
84,122
0
declaration
69
69
80,495
0
isolatedModules
 + 
verbatimModuleSyntax
69
69
80,622
0
isolatedDeclarations
62
62
34,982
0
erasableSyntaxOnly
 + legacy decorators
69
69
71,577
0
nodenext
69
69
85,238
0
"types": []
69
69
105,818
0
"lib": ["es5"]
69
69
83,872
0
All 11
752
751
895,051
12

#### Fuzzing & mutation testing

Each fuzzer generates every combination of a set of language features, runstscandbun checkon the result, and diffs the output.

Fuzzer
Functions
Mismatches
Control flow narrowing
46,080
0
Variables with no type annotation
29,484
0
Variables reassigned inside 12 kinds of loop
20,304
0
Callbacks and contextual typing
9,984
0
Circular references
9,196
0
Interfaces that extend a mapped type of themselves
8,424
0
Index signatures
5,770
0
Circular references next to overloaded calls
3,888
0
Boolean assignability
1,664
0
8 smaller fuzzers
1,441
0
Total
136,235
0

Those run on every commit. These are larger runs we did offline:

Fuzzer
Programs
Mismatches
Overloads, inference and variance
1,300,000
0
Where long types get cut off in error messages
1,060,000
0
Classes: access, overrides, initialization, 
super
290,000
0
Duplicate declarations of a variable or property
123,891
0
JSDoc in type-checked JavaScript
68,334
0
JSX: tags, attributes and children
63,770
0
Annotations that refer to what's being declared
50,688
95
Class expressions that refer to what holds them
40,128
21
Immediately invoked functions
19,200
21
Symbols that 
tsc
 creates lazily
15,444
25
Infinitely recursive type aliases
517
28
Module augmentation through re-exports
210
1
Total
3,032,182
191

162 of the 191 mismatches are in code that refers to itself while it's being declared, likeclass A { x = { a: null! as { p: A["x"] } } }.

For mutation testing, we brokeEffect's source 913 times (swapped arguments, dropped type arguments, deleted overloads) and compared every error.

Mutations
Errors in 
tsc
Missing in 
bun check
Only in 
bun check
913
2,925
0
0
Also on every commit
Count
Fuzzer-generated functions, diffed against 
tsc
136,235
Edge cases found by reading typescript-go next to the port, diffed against 
tsc
2,362
Corrupted source files that still have to report an error
1,893
Generated projects: file name casing, malformed 
tsconfig.json
, 
references
656
Regression tests
576

#### Try it on your project

bunx -p typescript@7.0.2 tsc --noEmit --pretty 
false
 
>
 tsc.txt

bun check --no-pretty 
>
 bun.txt

diff tsc.txt bun.txt

If there's a difference, that's a bug in Bun. Pleaseopen an issue.

Read thebun checkdocs.

## New in the runtime#

### 67–89% less CPU while your server sleeps#

### Bun.FetchSession#

Bun.FetchSessiongives a group of requests their own TLS, proxy, and keep-alive settings and their own connection pool. Sessions never share connections with each other or with plainfetch().

const
 session 
=
 
new
 Bun.
FetchSession
({

 tls
:
 { ca
:
 
await
 Bun.
file
(
"
corp-ca.pem
"
).
text
() },

 proxy
:
 { url
:
 
"
http://proxy.internal:8080
"
 },

 keepAlive
:
 { idleTimeout
:
 
30
, maxIdleSockets
:
 
8
 },

});

const
 client 
=
 
new
 
SomeClient
({ fetch
:
 session.fetch });

await
 
fetch
(
"
https://example.com
"
, { session }); 
// same thing
* session.fetchis bound, so any client that accepts afetchfunction can use it.
* Options on the request override the session's.
* session.close()(orusing) closes idle connections.
* A session'stls.checkServerIdentityruns once per connection. Requests that reuse the connection skip it.

### Better proxy environment support infetch()#

NO_PROXYaccepts wildcards, CIDR blocks, bare IPv6 addresses, andhost:port.

NO_PROXY=
"
*.internal.example.com, 10.0.0.0/8, fd00::/8, localhost:3000
"

ALL_PROXYis used whenHTTP_PROXY/HTTPS_PROXYis unset.proxy: falseignores the proxy environment for one request.

await
 
fetch
(
"
https://example.com
"
, { proxy
:
 
false
 });

When a proxy refusesCONNECTwith a non-2xx status,fetch()rejects withERR_PROXY_TUNNEL. The error carries the proxy'sstatusandheaders. Before,fetch()resolved with the proxy's reply as if it came from the origin.

### Experimental:Bun.ModuleGraph#

Run many instances of one app in a single process. Each graph gets fresh module state, its ownrequire.cache, and its own timers and I/O. Parsed code and bytecode are shared between graphs.

const
 graph 
=
 
new
 Bun.
ModuleGraph
({

 globals
:
 { process
:
 tenantProcess },

 
onError
:
 (
error
, 
kind
) 
=>
 console.
error
(kind, error),

});

const
 app 
=
 
await
 graph.
import
(
"
./app.ts
"
);

await
 graph.
run
(() 
=>
 app.
handle
(request));

graph.
dispose
(); 
// closes the graph's servers, sockets, timers, child processes
* graph.run(fn, ...args)callsfnin the graph's context, so what it opens belongs to the graph.
* graph.dispose()(orusing) behaves likeworker.terminate(). It is not a security sandbox.
* Bun.ModuleGraph.currentis the graph whose context the caller is in.

### --disallow-code-generation-from-stringsblockseval()andnew Function()#

With Node's--disallow-code-generation-from-stringsflag,eval()andnew Function()throw. It covers the whole process, including everyWorker. Bun used to accept the flag and ignore it.

new
 
Function
(
"
return 1 + 1
"
);

// EvalError: Code generation from strings disallowed for this context

=strictis Bun-only. It also blocks every other way a string becomes code:node:vm,import()of adata:URL,new Worker(code, { eval: true }),module._compile(), plugins that return source text,napi_run_script()and the inspector.

A flag embedded in a compiled executable always applies.BUN_OPTIONScan raise the level but not lower it.

bun build --compile ./server.ts --outfile server \
 --compile-exec-argv="--disallow-code-generation-from-strings=strict"

### Up to 2.7x faster large responses innode:http#

A response over 16 KB now goes out in one write per tick instead of up to 16. It applies tonode:httpandBun.serve, over HTTP and HTTPS.

Requests per second from anode:httpserver:

Response
After
Before
Node.js 26.3
4 × 
res.write(16 KB)
19,160
6,983
17,735
4 × 
res.write(16 KB)
, HTTPS
15,510
6,110
11,720
40 × 
res.write(2 KB)
14,980
6,140
9,879
res.end(64 KB)
19,889
16,528
18,535

node:httpwas slower than Node in six of eight large-response benchmarks. Now it's faster in all eight. ABun.servedirect stream writing 4 × 16 KB is 83% faster. Small responses are unchanged.

### JavaScriptCore upgrade#

Bun's JavaScriptCore engine picks up upstream WebKit performance work and spec fixes.

Operation
Change
JSON.parse()
 on npm registry manifests
1.2x–1.5x faster
JSON.parse()
 on 1,000 objects with the same keys
1.5x faster
/^\/users\/(\d+)$/.test(path)
 in a router benchmark
~5x faster
Object.values(obj)
 with 9+ properties
2.3x–3.2x faster
arr.copyWithin(0, 1)
~2x faster, ~45x with holes
arr.includes(x)
 on long number arrays
2.4x–3.3x faster
arr.splice(2, 1, x)
new fast path
for (const x of arr)
, and the same for strings
no iterator object allocated
const [a, b] = arr
no iterator object allocated

TheJSON.parsenumbers are against Bun v1.4.2 on an Apple silicon Mac, with manifests from 331 KB to 8 MB. Thefor...ofand destructuring change helps code that hasn't reached the top JIT tier yet.

* WebAssembly wide arithmetic (i64.add128,i64.mul_wide_uand friends) is on by default.
* RegExp.escape()no longer escapes supplementary code points like U+2002A.
* Atomics.isLockFree(4294967297)returnsfalseinstead of wrapping to1.
* A strict-mode async generator that doesreturn someCall()awaits the returned promise.
* ++arr.lengthin a loop no longer slows down quadratically past 100,000 elements.
* BigInt("-"),BigInt("+")andBigInt("0x")throwSyntaxErrorinstead of returning0n.
* (a?.b)(x)throws aTypeErrorwhenaisnullorundefined. Before, it returnedundefined, as if the parentheses weren't there.
* super.tag`x`callstagwith the currentthis.
* Error.stackTraceLimitis read from theErrorconstructor when a stack is captured, like V8.node:vmcontexts start at 10, matching Node.
* JIT-optimized code with many live floating-point values no longer turns one intoNaNafter readingarr[i]. This could happen ifarrwas sometimes aFloat32ArrayorFloat64Arrayand sometimes another kind of object.
* Intl.DurationFormatkeeps the minus sign of a duration between -1 and 0. Withseconds: "numeric",{ milliseconds: -500 }formats as-0.5instead of0.5.
* Intl.Segmenter'scontaining(index)returns the right segment whenindexis the first half of a surrogate pair, like the start of an emoji.
* On Windows, WebAssembly fast memory is enabled again. Growing a WebAssembly memory or a resizableArrayBufferat the system commit limit throws instead of crashing.
* --bytecodeoutput is 3–6% smaller.

### Faster handling of many rejected promises#

Promise.allSettledover thousands of throwing async calls no longer stalls. Attaching handlers to many promises that reject in the same turn took quadratic time. It is linear now.

await
 
Promise
.
allSettled
(

 
Array
.
from
({ length
:
 
100_000
 }, 
async
 () 
=>
 {

 
throw
 
new
 
Error
(
"
nope
"
);

 }),

);
Time
After
148 ms
Before
24 s
Node.js
475 ms

Attaching.catch()to 160,000 already-rejected promises went from 83 s to 24 ms.

### CompressionStreamaccepts a compression level#

Pass aleveloption toCompressionStreamto trade ratio for speed. Brotli previously always ran at quality 11, which is very slow for large, dynamic responses.

const
 stream 
=
 
new
 
CompressionStream
(
"
brotli
"
, { level
:
 
4
 });
* gzip,deflate,deflate-raw: 0-9
* brotli: 0-11
* zstd: 1-22

Out-of-range values throw aRangeError. Omittinglevelkeeps each format's current default.

### Bun.servesupportsIf-Range#

Clients can safely resume a download fromBun.serve. ARangerequest withIf-Rangegets the range only if the file hasn't changed. Otherwise it gets the full body.

await
 
fetch
(
"
http://localhost:3000/big.bin
"
, {

 headers
:
 {

 Range
:
 
"
bytes=1000-
"
,

 
"
If-Range
"
:
 lastModified, 
// from the first response

 },

});

// 206 if the file is unchanged, 200 with the full body if it changed

It works forBun.fileresponses and{ dir }routes.

## New inbun install#

### bun installskips tarballs it won't install#

Without a lockfile,bun installandbun addno longer download tarballs for packages that never land innode_modules: bundled dependencies, packages for other platforms, and groups turned off by--productionor--omit.

Tarballs downloaded with a cold cache and no lockfile:

Install
After
Before
npm@10.9.2
1
196
express
 + dev deps, 
--production
69
403

## New inbun build#

### Lower memory usage inbun buildwith many entry points#

Builds with many entry points or chunks use much less memory.

Peak RSS, 800 entry points
After
Before
Each imports one export from a file with 200,000 exports, 
--splitting
276 MB
2,121 MB
13 modules each, with or without 
--splitting
200 MB
405 MB

This fixes a regression from Bun v1.4.1 wherebun build --splittingwith ~800 chunks peaked at 7.7 GB instead of 6.2 GB. On Windows, it could abort withmemory allocation of N bytes failed.

### Bun.buildsupports[hashN]in output names#

Large--splittingbuilds no longer fail with "Multiple files share the same output path". Before, two chunks with different contents could get the same 8-character[hash]name. Now both names get extra hash characters until they differ.

Use[hash9]through[hash13]to set a wider minimum hash.[hash13]is the full 64-bit hash.

await
 Bun.
build
({

 entrypoints
:
 [
"
./src/index.ts
"
],

 outdir
:
 
"
./dist
"
,

 splitting
:
 
true
,

 naming
:
 { chunk
:
 
"
chunk-[hash13].[ext]
"
 },

});

### Metafile names the input file behind a splitimport()#

With--splitting, each dynamicimport()inmetafile.inputshas anentryPointfield naming the input file it loads, so tools that build a module graph no longer have to join throughoutputs. Metafile byte counts and--metafile-mdoutput are now accurate too.

meta.json

{

 
"
path
"
:
 
"
./chunk-abc123.js
"
,

 
"
kind
"
:
 
"
dynamic-import
"
,

 
"
original
"
:
 
"
./lazy.js
"
,

 
"
entryPoint
"
:
 
"
lazy.js
"
,

 
"
external
"
:
 
true

}
* entryPointis a key ofinputs. Arequire()of an ES module with--target=bungets one too. True externals likeimport("node:fs")don't.

## New inbun build --compile#

### bun build --compilesupports profile-guided bytecode layout#

--bytecode-orderlays out a--compile --bytecodeexecutable from a profile of a real run. The bytecode that run used goes together at the front of the file.

In one large CLI app, cold start went from 1.01s to 0.53s. Resident bytecode memory at its prompt went from 59.5 MB to 20.5 MB.

bun build --compile --bytecode ./cli.ts --outfile myapp

# Run it the way your users do. The profile is written on exit.

BUN_BYTECODE_ORDER_OUT=myapp.order ./myapp --help

bun build --compile --bytecode --bytecode-order=myapp.order ./cli.ts --outfile myapp
* Functions are matched by a hash of their syntax, so a profile from an older build still applies.
* --bytecode-order=a.order,b.ordertakes several profiles, most common first.
* Bun.buildusescompile: { bytecodeOrder: "./myapp.order" }.
* bytecodeOrderStats()frombun:jscreports how many loaded functions the profile covered.

### Faster startup for--compile --bytecodeexecutables#

Executables built withbun build --compile --bytecodestart faster. ESM executables embed a pre-resolved module graph and optimized bytecode and load every bundled module in one pass, and JavaScriptCore does less work to decode embedded bytecode and link compiled functions.

On a ~2,300-module CLI app, time to the first interactive prompt went from 698 ms to 579 ms (−17%). On a ~2,000-module CLI, the bytecode decode changes alone cut 6.3% of instructions to its first prompt.

bun build ./app.ts --compile --bytecode --format=esm --outfile myapp

The new--compile-jit-policy <n>flag (compile: { jitPolicy: n }inBun.build) scales JIT tier-up thresholds. Run-once startup code stays in the interpreter longer. CallBun.unsafe.setJITPolicy(1)once your app is interactive:

await
 
renderFirstScreen
();

Bun.unsafe.
setJITPolicy
(
1
); 
// back to the normal JIT policy
* --no-optimize-bytecode/optimize: { bytecode: false }skips the build-time bytecode optimizer.

## Other improvements#

* Fixed:crypto.randomInt()was about 20x slower per call since Bun 1.4.0. It takes 34 ns instead of 760 ns, on par with Node.js.
* Fixed: small zstd calls were up to 3.7x slower in x64 virtual machines since Bun v1.4.0.Bun.zstdDecompressSyncon a 1 KB input takes 1.38 µs instead of 5.11 µs.
* Fixed:node:zlibcalls on small inputs were slower since Bun v1.4.0.gunzipSyncwith a 1 KB result takes 2.97 µs instead of 4.99 µs, and 64 MB through gzip streams takes 131 ms instead of 166 ms.
* Fixed:Bun.color()got slower in Bun v1.4.0, and this recovers most of that. A call takes 208 ns instead of 692 ns, and 432 ns instead of 17,793 ns when 8 Workers call it at once.
* Improved: a shorttranspiler.transformSync()call takes 550 ns instead of 1,236 ns, and 2,290 ns instead of 15,246 ns when 8 Workers call it at once.
* Improved:vm.runInContext()andvm.runInNewContext()are about 30% faster per call (2.5 µs to 1.7 µs).new vm.Script(src, {})is about 2x faster. This recovers most of a 1.4.0 regression.
* Improved:Bun.serveanswers pipelined HTTP/1.1 requests with onesend()for the whole batch instead of about 14 syscalls per response. This fixes a regression from Bun v1.2.6.
* Improved:Object.keys(require.cache)andkey in require.cacheno longer leak a namespace object per loaded ES module. Listing 2,000 modules dropped from 38 ms to 2.6 ms.
* Improved:Bun.markdown.render()no longer takes quadratic time on deeply nested lists or emphasis when no callback is registered for the nested element. In Bun v1.4.2, 300 KB of nested lists took 99.5 s.
* Improved:Bun.gc(true)andgc()return freed memory to the OS before returning, so RSS drops right away instead of after a delay. This holds even when a background purge is in progress, and memory freed during a purge no longer stays resident until the event loop goes idle.
* Improved: Bun's mimalloc fork is now slightly smarter about when to give freed memory back to the operating system. Echoing a 512 KiB JSON body, Elysia takes 388 page faults per request instead of 574, and Express 523 instead of 762.
* Improved: threads that are idle afterWebAssembly.compile(), or blocked inAtomics.wait()orBun.sleepSync(), give freed memory back to the OS after about 100 ms. A thread blocked for one second after freeing most of its heap held 115 MB instead of 424 MB.
* Improved: on macOS,process.memoryUsage().rssnow reports the physical memory footprint that Activity Monitor shows, andprocess.resourceUsage().maxRSSreports its peak.
* Improved: long-runningbun build --compileapps on Linux keep less of Bun's own code resident in memory. Bun's linker order file now also traces app-shaped workloads.
* Improved: on Windows,Bun.secrets.set()takespersist: "local"to keep a credential on the current computer. By default ("enterprise") it roams with the user's account.
* Improved: updated SQLite to 3.53.4, libarchive to 3.8.9, brotli to 1.2.0, lsquic to 4.9.4 and libjpeg-turbo to 3.2.0. Chunked HTTP bodies with bare-LF chunk line endings are now rejected, as in llhttp.
* Improved: updated the bundled root certificates to NSS 3.128 (Firefox 156). This adds SECOM and Telia TLS roots and removes Entrust Root Certification Authority, ePKI, Atos TrustedRoot 2011, and SecureSign Root CA12.
* Improved: theoven/bun:alpineDocker image is now based on Alpine 3.24, matching the libstdc++ the musl build links against.
* Improved:bun test --coverage-reporter=lcovnow implies--coverage. Before, it ran the tests and wrote no report.

## Bugfixes#

### Security#

* Hardened:fetch,WebSocket,Bun.connect,Bun.RedisClientandBun.SQLverify the server during the TLS handshake instead of after it, like curl and Go. Error codes are unchanged.
* Hardened: TLS certificate name matching intls.connect,tls.checkServerIdentity,https,fetchandBun.connectonly accepts valid host names and canonical IP addresses (CVE-2026-48618).
* Hardened: certificate verification innode:tlsandBun.listenwhen a connection closes during the TLS handshake.
* Hardened: certificate checks innode:tls,https.Agentandfetch()when a TLS session or pooled connection is reused.fetch()rejects atls.checkServerIdentitythat isn't a function or that returns a truthy value, as in Node.
* Hardened:Bun.SQLtreatstls: Bun.file("ca.pem")(orssl:) liketls: { ca: Bun.file("ca.pem") }and usesverify-full.
* Hardened:node:http2servers rate-limit stream resets (CVE-2023-44487, CVE-2025-8671).streamResetBurstandstreamResetRatetake effect, matching Node.
* Hardened:Bun.servefollows RFC 9112 more strictly afterConnection: close.
* Hardened: rare scenario when precise conditions are met that can causereq.urlandreq.headersto return incorrect values on aborted requests inBun.serve().
* Hardened: TLSBun.serve()servers apply the idle timeout to connections that never finish the handshake.
* Hardened:fetch()validates chunked transfer encoding in responses more strictly, like Node.
* Hardened:fetch("file://host/path")rejects withERR_INVALID_FILE_URL_HOSTunless the host is empty orlocalhost.
* Hardened:fetch()rejects when your code passes aContent-Lengthheader that doesn't match theReadableStreambody it sends.
* Hardened:fetch()andnode:httpagents terminate an idle keep-alive connection that received unexpected data, matching Node.js.
* Hardened:fetch()against servers that close or reset a TLS connection at unexpected times. This fixes three rare crashes.
* Hardened:bun installparses registry and tarball URLs more strictly before attaching credentials.
* Hardened:bun installagainst malformedbinfields in apackage.jsonor registry manifest.
* Hardened:Bun.Archive#extract(),bun createandbun installofgithub:dependencies against malformed tar archives.
* Hardened:v8.deserialize()and IPC withserialization: "advanced"against crafted records.
* Hardened: UDP socketaddMembership(),dropMembership()and their source-specific variants against arguments with side effects.

### Node.js compatibility improvements#

#### node:http

* Fixed: afterreq.pause()in anode:httpserver, a small body was not received untilreq.resume(), soreq.completestayedfalseandreq.readableLengthstayed0while paused.
* Fixed: in anode:httpserver,res.end()before the request body had arrived madereqemit'end'at once and dropped the rest of the body. A handler that read the body first was unaffected.
* Fixed: in anode:httpserver, a synchronousres.destroy()in the'request'listener or a'data'listener, while the request body was still arriving, madereqemit'end'withreq.complete === trueinstead of'aborted'andECONNRESET.
* Fixed:'finish'and theres.end()callback on anode:httpresponse fired before the last bytes left the socket. This needed a response too large for the kernel's socket buffer and a client that was slow to read it.
* Fixed: anode:httpresponse never emitted'drain'whenres.write()had returnedfalseand other code, such as a heartbeat timer, calledres.write()again just as the client caught up. Astream.pipe(res)on that response then hung.
* Fixed: anode:httpserver never answered a pipelined request when part of its body arrived after the previous response had ended.
* Fixed:server.close()on anode:httpserver called back once in-flight responses finished, while their keep-alive connections were still open and serving requests.closeAllConnections()afterclose()did nothing, so an open connection kept the process alive.
* Fixed:server.closeAllConnections()also stopped the listener and destroyed tunnels and WebSockets.
* Fixed: writes to anode:http'upgrade'or'connect'socket stayed buffered untilsocket.end()when the same keep-alive connection had already served a request. The npmwspackage stalled this way. Fresh connections were unaffected.
* Fixed: CONNECT and Upgrade tunnel sockets kept reading while paused.
* Fixed: anode:http'connect'or'upgrade'listener that calledsocket.end()missed part of the data the client had sent right behind the request. This needed request headers that arrived in more than one read, with more than 17 KB of data behind them.
* Fixed: anode:httpserver dropped the body of a HEAD or TRACE request that declared one withContent-Length.
* Fixed:Proxy-Connection: closenow closes the connection, likeConnection: close.
* Fixed: HTTP/1.0 requests with anExpectheader get a plain'request', not100 Continue.
* Fixed: servers fed a socket throughserver.emit("connection", duplex)or http2'sallowHTTP1fallback threwERR_HTTP_SOCKET_ASSIGNEDon pipelined or fast keep-alive requests.
* Fixed:req.setTimeout()never fired when a pipelined request's body stalled behind a pending response. The server closed the socket instead.
* Fixed:node:httpserver.close()never called back when a request body finished arriving while theIncomingMessagewas paused, the response ended later, and the same keep-alive connection then served another request.
* Fixed: callinglisten()on anode:httpserver that was already listening leaked the first listener and kept the process alive afterclose(). It now throwsERR_SERVER_ALREADY_LISTEN, like Node.
* Fixed:node:httpservers emitted'clientError'repeatedly for the same stalled request (eventually triggeringMaxListenersExceededWarning) when the listener didn't destroy the socket after aheadersTimeoutorrequestTimeout.
* Fixed: innode:httpservers,req.socketemitted only'close'when the client closed the connection, never'end'for a FIN or'error'(ECONNRESET) for a reset.
* Fixed:req.socket.setKeepAlive()andreq.socket.resetAndDestroy()in anode:httpserver returnedundefinedinstead of the socket, so chaining threw.
* Fixed: anode:httpserver that calledres.detachSocket()on an unfinished response could, in rare cases, crash on a later use of that response, or never exit, after the client disconnected. Regression since v1.4.0.
* Fixed:node:httpandnode:httpsproxy errors (ERR_PROXY_TUNNEL,ERR_PROXY_INVALID_CONFIG) included the username and password from the proxy URL.
* Fixed: a proxiednode:httpsrequest (new https.Agent({ proxyEnv }),NODE_USE_ENV_PROXY=1) emitted'close'but never'error'(ECONNRESET) when the connection ended after the proxy acceptedCONNECTbut before the TLS handshake finished.

#### node:http2

* Fixed: on Linux,http2.connect()to a closed port reportedECONNRESETinstead ofECONNREFUSED. With no'error'listener, the failure was silently swallowed. Regression since v1.4.0.
* Fixed: anode:http2request with[http2.sensitiveHeaders]also sent a literalnodejs.http2.sensitiveheadersheader that listed those header names.Bun.spawnenv and macros also turned Symbol keys into string keys.
* Fixed:node:http2ALTSVC and ORIGIN frames used UTF-8 instead of latin-1, so a value containing bytes 0x80 to 0xFF read differently on a Node.js peer. ASCII values were unaffected.
* Fixed:http2.connect(),createServer()andcreateSecureServer()accepted invalid options that Node rejects, such as a non-booleanstrictSingleValueFields.
* Fixed:ClientHttp2Stream.close(code)emittederrorforNGHTTP2_CANCEL, andendbeforeerrorfor other error codes.
* Fixed:session.originSetthrew afterdestroy()on a TLS session that had never read it. It now returnsundefined, like Node.

#### node:tls

* Fixed:tls.Server#setSecureContext()had no effect on a server that was already listening.
* Fixed:tls.Server#addContext()andBun.serve({ tls: [{ serverName }] })served the default certificate for a hostname with an unusually large number of labels. AnaddContext()wildcard also did not cover the hostname passed tolisten().
* Fixed: client-sidenew tls.TLSSocket(socket)(STARTTLS) never started a handshake.write()threw aTypeErrorand_start()threwERR_MISSING_ARGS. Themysqlpackage connects this way whensslis set.
* Fixed: aftertls.connect({ socket }),'data'listeners left on the plain socket kept firing with the encrypted bytes. A STARTTLS listener that calledtls.connect({ socket })on every chunk gotInvalid socketfrom the second call.
* Fixed: a TLS socket that wraps anet.Socketignored the wrapped socket'sallowHalfOpen. A STARTTLS server created withnet.createServer({ allowHalfOpen: true })could not reply after the client ended its side.
* Fixed: anet.Socketwrapped bynew tls.TLSSocket(socket)ortls.connect({ socket })emitted its own'error'on a peer reset, and'end'and'finish'ontlsSocket.destroy(err), on top of the TLS socket's events. Node emits only'close'on the wrapped socket.
* Fixed: destroying atls.connect({ socket })client in the same tick it was created left the wrappednet.Socketopen, with no FIN sent, if that socket still had unflushed writes.
* Fixed: when anode:tlssocket ran over a plainstream.Duplex(not anet.Socket), destroying theDuplexwith an error threw an uncaught exception instead of emitting'error'on the TLS socket. Anhttps.requestover such a socket exited the process.
* Fixed: a server-sidetls.TLSSocketover aDuplexemittedECONNRESETand no'close'when theDuplexwas destroyed before the handshake finished. If it was destroyed in the same tick as the wrap, the TLS socket emitted nothing.
* Fixed: in an uncommon configuration, anode:tlsserver over aDuplexwhoseALPNCallbackwrites to the socket, the server could crash during the handshake.
* Fixed:end()on anode:tlssocket over aDuplexnever ended theDuplex(the peer saw no FIN) if the peer stalled mid-handshake or never answered the TLS close.
* Fixed:tls.TLSSocketend()anddestroySoon()sent no FIN when the peer never answered the TLS handshake, so the socket never emitted'close'.
* Fixed: an acceptednode:tlssocket whose peer reset the connection during a large write could emit only'end', never'error'or'close', soserver.close()never completed. This was seen on Linux and depended on timing.
* Fixed: atls.connect()ornode:httpsclient that wrote before a TLS 1.3 handshake finished could getECONNRESETinstead of the reply. This needed a server withoutnoDelaythat reset the connection a few milliseconds after replying.

#### node:netandnode:dns

* Fixed: anode:netsocket could drop or resend bytes after a partialwritev(). This needed a peer that had stopped reading, data already buffered for it, and a new write that the kernel accepted only part of.
* Fixed:net.Socket#write()returnedtruewhen the send failed immediately (ECONNRESET,EPIPE, or a closed handle). It now returnsfalseand setssocket.errored, matching Node.
* Fixed:node:netrouted an exception thrown in a socket'data'or server'connection'listener to the socket's'error'event and closed the socket, instead ofuncaughtExceptionlike Node.
* Fixed: anode:netornode:tlssocket was never garbage collected if it was destroyed before its connection attempt started (in the same tick asconnect(), or during the DNS lookup), or if its DNS lookup failed.
* Fixed:new net.Socket({ fd, readable: false, writable: true })ended and closed the fd one tick after construction, so later writes failed withEPIPE.
* Fixed:fetch(),Bun.connect()anddns.lookup()(on macOS and Windows, or with thesystem/libcbackend) reported a temporary DNS failure (SERVFAIL or every nameserver timing out) asETIMEOUTinstead ofEAI_AGAIN, so retry logic keyed onEAI_AGAINnever fired.

#### node:child_process

* Fixed: on Linux and macOS, withchild_process.spawn()and an"ipc"stdio slot, a non-JS child (e.g. Python) that wrote a message larger than the socket buffer in onewrite()got a short write, and the message never arrived.
* Fixed:child_process.spawnSync()of a command that can't be spawned returnedstatus: undefined,pid: undefinedandoutput: [null, null, null]. It now returnsstatus: null,pid: 0andoutput: null, like Node.
* Fixed:child.stdin.end(cb)andtty.WriteStream#end()called with no data firedcband'finish'while earlier writes still waited on a full pipe. A parent that exited incbtruncated the child's input.end(chunk, cb)was not affected.
* Fixed:child_process.spawn()now throwsERR_INVALID_ARG_VALUEwhenstdioholds atls.TLSSocket, like Node.js.
* Fixed: callingdestroy()inside a'data'listener onchild.stdout,child.stderr, or aReadable.fromWeb()stream emitted one more'data'(and sometimes'end').exec()withmaxBuffercould overshoot the limit by a chunk. Regression in v1.4.0.

#### node:module

* Fixed:require()andrequire.resolve()crashed whenModule._resolveFilenamewas set to a non-function. They now throw aTypeError, like Node.
* Fixed:require()of an ES module crashed when code had replacedModule._resolveFilenamewith its own function, and that function returned a path that was not normalized (a symlink, or one containing/./,/../or//).
* Fixed: the secondrequire()of an ES module threw if aModule._extensionshandler had called the original loader and caught the module's error. The module was dropped fromrequire.cache.
* Fixed: Bun crashed when a preload setModule.runMainto a non-function such as{}or a string. An override that threw printed onlyError occurred loading entry point: JSError, without the error.

#### node:vm

* Fixed: when the host passed itsFileorfs.Statsclass into anode:vmcontext,class Upload extends File {}there crashed onnew Upload(...). A hostPerformanceObserverwhose callback was created in a context crashed when it delivered entries.
* Fixed:vm.runInContext(),vm.runInNewContext()and the matchingvm.Scriptmethods crashed instead of throwing aTypeErrorwhen an option such asdisplayErrorswas given a null-prototype object that had a customutil.inspectfunction.
* Fixed:node:vmaborted the process, even insidetry/catch, when text it built from JS, such ascompileFunction()parameters or a thrown error'sstack, passed the maximum string length of 2^31 - 1 characters.
* Fixed: avm.Script,vm.compileFunctionorvm.SourceTextModulekept its context alive for the life of the process when itsimportModuleDynamicallycallback could reach that context (such as a closure over the sandbox) and the code left a function on it.
* Fixed: in anode:vmcontext, theTypeErrorthrown whenObject.definePropertyon the global failed was created in the host realm instead of the context's realm.

#### node:fs

* Fixed: on Linux and macOS,node:fsopened files withoutO_CLOEXEC. Child processes forked by native code, such asnode-ptyor an addon callingsystem(), inherited those descriptors. Children ofBun.spawnandnode:child_processdid not.
* Fixed: inside anode:fscallback, a microtask the callback queued ran before aprocess.nextTick()it queued. The order now matches Node.
* Fixed:fs.readSync()andfs.read()threwERR_OUT_OF_RANGEinstead of Node'sERR_INVALID_ARG_TYPEwhenbufferwas not a buffer andoffsetwas invalid.

#### node:util

* Fixed:util.format('%s', value)printed theutil.inspect()output (such as<Buffer 61 62>) forBuffer,URL, andURLSearchParams. It now prints theirtoString()result, as Node does.
* Fixed: every garbage-collectedMIMETypefromnode:utilleaked itstypeandsubtypestrings. That was about 57 bytes per instance for atext/htmltype with acharsetparameter.
* Fixed:util.aborted()invoked a user-replacedFunction.prototype.bindon its internal abort listener.
* Fixed: after a few hundredutil.promisify()calls,util.promisify(setTimeout)could return the promise version ofsetImmediateorsetIntervalif that timer was promisified first, soawait sleep(300)resolved at once. Regression in v1.4.1.

#### node:crypto

* Fixed: innode:crypto,hash.update()afterhash.end(), which throws in Node.js, hung forever onsha3-*hashes.hash.end()afterdigest(), as whenpipe()ends a hash whosedigest()was already called, emittedERR_CRYPTO_HASH_FINALIZEDinstead of the digest.
* Fixed:crypto.hkdfSync()andcrypto.hkdf()returned an emptyArrayBufferfor akeylenof 0 instead of failing with "HKDF derivation failed", as Node.js does.

#### node:buffer

* Fixed:buffer.transcode()aborted the process, even insidetry/catch, when its output needed 2 GiB or more.
* Fixed:buf.utf8Write(123),buf.hexWrite(123)and the other per-encodingBufferwrite methods wrote the string form of a non-string value. They now throwERR_INVALID_ARG_TYPE, like Node.js.

#### Native addons

* Fixed: when the main thread or a Worker exited naturally, a native addon's N-API finalizers and cleanup hooks could still call into JavaScript, and that JavaScript could call a second addon that was already torn down. These calls now returnnapi_cannot_run_js, like Node.js.
* Fixed: native addons that callv8::Function::GetScriptOrigin(), such as@newrelic/fn-inspect, failed to load on Linux and crashed on macOS.

#### Other modules

* Fixed:node:wasipoll_oneoffthrewTypeError: Invalid mix of BigInt and other type in subtractionon any clock wait with a positive timeout, so a WASIsleep()failed.
* Fixed:node:wasifd_preadreported twice the bytes read whenever a read filled its buffer.
* Fixed:require("cluster")threwcluster._setupWorker is not a functionwhen a script setprocess.env.NODE_UNIQUE_IDitself afternode:nethad loaded.
* Fixed:node:dnsandAsyncLocalStorage.bind()argument errors readThe "undefined" argument must be of type ...instead of naming the argument.
* Fixed: response bodies from an installed copy of Undici could stay pending instead of rejecting after a forced socket close, becausenode:stream'sisReadable()returnednullfor webReadableStreams.
* Fixed:for await (const line of rl)overnode:readlinethrewERR_USE_AFTER_CLOSEand dropped the last line when the input ended with a single chunk of 1,026 or more lines. This hitReadable.from([text])and HTTP responses, not files, stdin or child process output. Regression in v1.4.0.
* Fixed: innode:quic,sendHeaders()on a stream opened before the handshake finished was not sent until the client wrote a body or ended the stream.
* Fixed:url.parse()andurl.resolve()crashed instead of rethrowing when they were passed an object instead of a string and a getter on that object (likeconstructor) threw a primitive value.
* Fixed:class Sub extends StringDecoder {}returned the class itself fromnew Sub()instead of an instance, sowrite()was undefined.
* Fixed:process.exit()called a replacedprocess.reallyExitwith the wrongthis(nowprocess). It also threw aTypeErrorwith an empty message whenprocess.reallyExitwas not a function.
* Fixed: seven Node.js error codes had a wrong.messagethat now matches Node.js. For example,ERR_HTTP_TRAILER_INVALIDreadundefinedandERR_INVALID_URL_SCHEMEreadfile.
* Fixed:node-fetch'sfetch(url, { body })never settled when an old-styleStreambody that isn't aReadable(such asform-data) emitted"error"before"end". It now rejects with that error.
* Fixed:node-fetch'snew Response(stream)threw for an old-styleStreamthat isn't aReadable. This brokenode-fetch-cache.

### Bun APIs#

* Fixed:Bun.servedropped WebSocket frames that a client sent without waiting for the101response, when they arrived in the same TCP read as the upgrade request. Browsers wait for the101, so they were not affected.
* Fixed: on Linux, aBun.serveresponse serving a file of 1 MB or more could send file bytes before the end of its headers. This needed response headers too large for the kernel's send buffer (the repro used a 16 MB header).
* Fixed: in aBun.serveserver withhttp2: trueorhttp3: true, some requests with a streamed response body were never released, sopendingRequestsstayed above zero and a gracefulserver.stop()never resolved. Both options are off by default.
* Fixed: inBun.servewithhttp3: true, callingserver.stop()from inside a request handler spun at 100% CPU if that connection had already served a request. Callingstop(true)from a handler left clients waiting 10 to 30 seconds for their idle timeout.
* Fixed: inBun.servewithhttp2: true, the tail of a streamed body under 256 bytes was sent twice when the client's flow-control window cut it off more than once, causingPROTOCOL_ERROR.
* Fixed: inBun.serve({ http3: true }), a request header value that a client sent with leading or trailing whitespace reached the handler untrimmed.req.headers.get()returned" v\t"where HTTP/1.1 gave"v".
* Fixed: withBun.serve({ tls }),ws.terminate()waited for the peer's TLS shutdown reply instead of closing at once. If the peer had stopped reading, theclosehandler did not run until the idle timeout, andmessage()could still fire.
* Fixed:Bun.servecrashed with a stack overflow when a handler calledresponse.text()on afetch()Response without awaiting it, then returned that Response before its body arrived. It now responds with a 500 viaerror().
* Fixed:Bun.serve()responded200with an empty body when a secondResponsereused aReadableStreaman earlier response already sent. It now errors.
* Fixed:Response.clone()on a body from an unreadBun.file().stream()dropped the MIME type, soBun.servesent noContent-Typefor the clone.
* Fixed: aBun.servehandler that calledreq.clone()on a request with a body and then read neither copy leaked about 7 KB of memory per request.
* Fixed: aBun.serveresponse with atype: "direct"stream sent an empty body whenpull()wrote and then calledcontroller.close()in the same tick.cancel()also ran after every completed response.
* Fixed: in aBun.servedirect stream, a synchronouspull()that ended a chunked response (for exampleflush()thenend()) and then threw in the same call wrote the last chunk twice. Strict clients then failed to parse the next keep-alive response.
* Fixed: in aBun.servedirect stream, an asyncpull()that calledend()after anawaitand then never returned kept its request pending, so a gracefulserver.stop()never resolved.
* Fixed: in aBun.servedirect stream, aflush(true)promise never settled (and leaked) ifend()was called while the socket was still backpressured.
* Fixed: callingserver.ref()afterawait server.stop()completed kept the process alive forever.
* Fixed:Bun.spawn,Bun.spawnSyncandnode:child_processreturned truncated data with no error when the kernel failed a read or write on a stdio pipe with an errno likeEIOorENOBUFS. They now report the error. Found by fault injection.
* Fixed: on macOS and Linux,spawnSyncorexecFileSynccould spin at 100% CPU and never return after a garbage collection during an earlierBun.spawnSyncfreed a stream such as a previous test file'sprocess.stderr. Users hit this in largebun test --isolatesuites.
* Fixed: after user code closed fd 0, 1 or 2 (e.g.fs.closeSync(1)),Bun.spawncould reuse that number for its own pipes.proc.stdout.text()then hung if fds 0 and 1 were both closed, and on Linux a child withstdout: "inherit"could overwrite aBlobof 8 MiB or more.
* Fixed: on macOS,subprocess.signalCodeandsubprocess.kill()used Linux signal numbers, so a child killed by SIGBUS reported"SIGUSR1"andkill("SIGUSR1")sent SIGBUS. Signals numbered the same on both systems, like SIGTERM, SIGKILL and SIGINT, were not affected.
* Fixed: on Linux, when the process hit its open file limit right after starting a child,Bun.spawnandchild_process.spawnblocked until that child exited. A child waiting on a stdin pipe never did, which froze the process. They now fail withEMFILE.
* Fixed:Bun.spawnSynccrashed the process when it ran out of file descriptors (handles on Windows) while creating its event loop on the first call. It now throwsEMFILE.
* Fixed: on macOS and Linux, when aBun.spawn({ terminal })child exited withterminal.write()input still queued, theBun.Terminaland its three pty file descriptors were never released and the process used CPU while idle. This was a regression in v1.4.0.
* Fixed: on Windows, callingterminal.write()after the child exited leaked theBun.Terminaland its callbacks, a regression in v1.4.0.
* Fixed: on Linux and macOS, the process never exited when code held a reader onBun.spawnstdout orBun.stdin.stream(), stopped callingread()while more than 16 KB of output was still unread, and the other end then closed.
* Fixed: a pipe-backedFileSink(Bun.stdout.writer(),Bun.spawnstdin) lost buffered data when a write was larger than the pipe could accept at once andend()was then called without a top-levelawait. The process exited before the reader drained the pipe.
* Fixed:Bun.file().stream()hung instead of erroring when the underlyingread()failed with an error likeEIO, for example on/proc/self/mem. After such an error on a pty or non-blocking pipe, the process never exited.
* Fixed: on macOS,await Bun.write(dest, Bun.file(src))resolved to0instead of the byte count whendestalready existed or was on another volume. The file itself was copied in full.
* Fixed:Bun.file(path).exists()kept returningfalseafter the file was created, if an earlierexists()orsizeon the sameBun.file()had found no file.
* Fixed: anHTMLRewriterwas never garbage collected when one of its handlers referenced the rewriter or the transformedResponse.
* Fixed:HTMLRewriterleaked the outputResponsewhen anelement.onEndTag()callback referenced it and a handler threw or the output was cancelled before that end tag.
* Fixed: whenHTMLRewriter.transform()read atype: "direct"stream body and a handler threw, the output was cancelled, or the client disconnected, the stream'scancel()receivedundefinedand its nextwrite()threw.cancel()now receives the reason andwrite()returns0.
* Fixed:Bun.ImagethrewERR_IMAGE_DECODE_FAILEDfor slightly damaged JPEGs (stray bytes, a missing end marker, truncated data) that libjpeg-turbo can decode with only a warning.
* Fixed: inBun.markdownwithwikiLinks: true, a*,_or~inside a[[target|label]]target paired with one outside the link, leaving an unclosed<em>,<strong>or<del>.
* Fixed: inBun.markdown, a*inside a reference link's label could leave an unclosed<em>when the link was followed by(<with no closing>, as in*[a*](<bwith[a*]: /urldefined.
* Fixed: inBun.markdown, a backslash before a space, tab or line ending in a link destination was treated as an escape, so[a](te\ st)rendered as a link instead of literal text.
* Fixed:YAML.stringify()with an indent argument left a trailing space after keys, put empty[]and{}on their own line, and misaligned nested sequences at indent widths other than 2.
* Fixed:YAML.stringify()could write a*aliasin place of an unrelated object or array. This needed getters or Proxy traps that returned a new object on each read, and a garbage collection during the call.
* Fixed: in aWorker,Bun.TOML.stringify()crashed instead of throwingRangeError: Maximum call stack size exceededon an object nested about 9,500 levels deep, just under the depth limit. Deeper objects already threw.
* Fixed:Bun.wrapAnsi()aborted the process instead of throwing aRangeErrorwhen an input line wrapped into tens of millions of rows or one row approached 2 GB.
* Fixed:Bun.stripANSI()aborted the process on a non-Latin-1 string of 2^30 or more characters that contained an escape sequence, as didBun.sliceAnsi()on about 78 million escape sequences in a row.
* Fixed:Bun.indexOfLine()could miss a line break in input that is not valid UTF-8, sofor await (const line of console)merged two lines.
* Fixed: on Linux,Bun.Globscans with*,?or[...]could miss file names that are not valid UTF-8, such as names from a Latin-1 archive.bun pm packcould also pack such a file that.npmignoreexcludes.
* Fixed:new Bun.FileSystemRouter()panicked or returned truncated route names for nested files whendirwas an absolute path containing.., such asimport.meta.dir + "/../pages".
* Fixed:cc()frombun:fficould crash or hang when several Workers made their firstcc()call at the same time.
* Fixed: subclassingBun.Cookie,Bun.CookieMap,crypto.ECDH,crypto.DiffieHellman,dns.Resolveror$.Shellreturned an instance of the base class, soinstanceofand subclass methods broke.
* Fixed:X509Certificate,crypto.hkdf,bun:sqlite, andBun.CookieMapaborted the process when given a non-ASCII string of 2^30 or more characters. They now throw aRangeErroror report no match.

### Web APIs#

#### fetch

* Fixed: on macOS,fetch(), sockets anddns.lookup()failed withENOTFOUNDfor split-DNS names, like a host only a VPN's resolver knows while iCloud Private Relay is on.
* Fixed: afetch()body stream (res.body) ors3file.stream()that code created, never read and dropped kept its connection if the server stopped sending mid-body. With 256 of these open at once, laterfetch()calls stayed pending.
* Fixed: a regression in 1.4.1 where, after more than 64 concurrentfetch()requests to one keep-alive origin finished, the surplus idle connections were closed with an RST, so servers loggedECONNRESET. The responses themselves were not affected.
* Fixed: a regression in 1.4.0 wherefetch()leaked an ASCII stringbodywhen it rejected before sending, such as on an invalid header name or aGETwith a body.
* Fixed:fetch()sent the URL fragment to the server in the request line when the fragment contained a?and no query string came before the#, as in/#/users?id=1.
* Fixed:delete process.env.HTTPS_PROXY(or reassigning it after a delete) had no effect on laterfetch()calls.
* Fixed:fetch(url, { unix })sent a proxy-form request down the Unix socket whenHTTP_PROXYwas set.
* Fixed: a streamedfetch()response withContent-Encoding: brorzstddelivered only the first 4096 bytes of a larger flushed chunk, holding the rest until the next compressed chunk arrived.
* Fixed: a compressedfetch()body read through a stream reader over HTTP/1.1 was decompressed as fast as it arrived, not as fast as it was read. With a slow reader and an unusually compressible body, memory could grow by hundreds of MB.
* Fixed:fetch()rejected a validContent-Encoding: deflateresponse withZlibErrorwhen the server compressed with a zlib window smaller than 32 KB, or when the first read held only one byte of the body.
* Fixed: after afetch()was aborted mid-body, native readers ofres.bodysuch asnew Response(res.body).text()orBun.write()got a genericAbortErroror an empty body instead ofsignal.reason.
* Fixed: a stream taken from afetch()body,req.body,S3File.stream()orHTMLRewriteroutput while the transfer was running, but first read after it had failed, ended cleanly with 0 bytes instead of rejecting. In rare cases since 1.4.0, a partly read stream crashed.
* Fixed: a memory leak where afetch()Responseand itsAbortSignalwere never garbage collected if anabortlistener on the signal referenced the response.
* Fixed: afterreq.clone()inBun.serveorres.clone()on afetch()response, a reader on the original'sbodystream ended withdone: trueinstead of rejecting when the body failed mid-stream.text()and the clone already rejected.
* Fixed:arrayBuffer()andbytes()on afetch()response orResponsewhose body exceeded 4 GiB aborted the process instead of rejecting withRangeError: Out of memory.
* Fixed: over HTTP/2 and HTTP/3,fetch()kept leading and trailing whitespace on a response header value when the server sent it, which the HTTP/2 spec forbids. A paddedLocationheader failed to redirect.
* Fixed:fetch()withprotocol: "http3"crashed when the QUIC connection closed before the response headers arrived and the automatic retry could not open a new connection at all, such as when no address for the host was reachable.
* Fixed: aborting an HTTP/3fetch()upload made the server treat the truncated body as complete. If the request declared acontent-length, the server closed the connection and the next upload to that origin could reject withHTTP3StreamReset.
* Fixed: HTTP/3fetch()andBun.serve({ http3: true })spun at 100% CPU when the kernel kept refusing UDP sends, such as under a firewall DROP rule or a low egress MTU.

#### WebSocket

* Fixed: theWebSocketclient reported close code1005or a1002protocol error when the server's Close frame was split across two TCP reads within its first three bytes.
* Fixed: awss://WebSocket through an HTTP CONNECT proxy reported close code 1006 "Failed to write" instead of the server's close code when the server ended TLS right behind its Close frame, asws.close()inBun.servedoes.
* Fixed: awss://WebSocket to an IP address such as127.0.0.1, or through an HTTPS proxy at an IP address, closed with code 1006 when a TLS 1.2 server renegotiated (regression in 1.4.1).

#### Streams

* Fixed:controller.write()in atype: "direct"ReadableStreamnever waited for a slow reader usinggetReader(),for awaitorpipeTo(). Once unread bytes reachhighWaterMark(64 KiB by default), it now returns a promise that resolves on the next read.
* Fixed: a direct stream'scancel(reason)was never called onreader.cancel(),stream.cancel(), or abreakout offor await.
* Fixed: in a direct stream, awrite()made afterend()orclose()insidepull()was still delivered to the reader.
* Fixed:bytes()andarrayBuffer()hung on a direct stream whose asyncpull()calledcontroller.end()and never returned.
* Fixed:Duplex.fromWebdropped the last chunk of atype: "direct"ReadableStreamwhenpull()calledcontroller.error()or threw right after flushing that chunk. Only theerrorevent was emitted.
* Fixed: an async-iterable body (new Response(asyncGen()), afetchupload, aBun.serveresponse) was silently truncated or hung when the generator threw an error with codeERR_INVALID_THIS, instead of failing the stream.
* Fixed:new Response(asyncIterable)kept pulling the iterator after its consumer had stopped early, throughreader.cancel(), abreakout offor await, a failedpipeTo(), or aBun.write()that hitENOSPC. It now calls the iterator'sreturn(), sofinallyblocks run.
* Fixed:finished(stream)fromnode:stream/promisesnever settled for afetch()body orBun.file()stream consumed natively (byBun.write(), afetch()request body,Bun.serve(), spawn stdin, or S3). The stream stayedreadable.
* Fixed: for aResponsebody backed by a string,Blob, typed array or file, readingres.bodyand then callingarrayBuffer(),bytes(),blob(),json()orformData()left the streamreadable, sofinished(body)fromnode:stream/promisesnever settled.
* Fixed: ares.bodystream taken beforeawait res.text()(orjson(),blob(), etc.) was left unlocked afterwards andgetReader()still worked, unlike undici and browsers.
* Fixed: readingblob.slice(start, end).stream()with.text(),.bytes(),.json()orBun.readableStreamToText()returned the whole parentBlobif the parent and the slice had already been garbage-collected.
* Fixed:ReadableStreamcancel(),pipeTo()andpipeThrough()on a locked stream threw aTypeErrorwithoutcode: "ERR_INVALID_STATE", a regression from 1.3.
* Fixed: web streams aborted the process instead of throwingRangeError: Out of memorywhen a queue or buffer hit its size limit, such as 67 million chunks queued and not yet read, or a single 2 GiB chunk (since 1.4.0).

#### Other

* Fixed:postMessage()detached theArrayBuffers in its transfer list even when it threwDataCloneErrorbecause a getter in the message closed a transferredMessagePort.

### TLS#

* Fixed:fetch(),WebSocket, andBun.SQLwithsslmode=verify-fullfailed certificate verification when connecting to an IPv6 literal likehttps://[::1]:3000, even when the cert had a matching IP SAN.fetch()rejected withERR_TLS_CERT_ALTNAME_INVALID.
* Fixed: aBun.connectTLS socket that calledshutdown()mid-handshake never firedcloseafterend()while the peer stayed connected. The next socket to do the same never got itshandshakecallback.
* Fixed: on aBun.listen()TLS server,socket.pause()did not hold for a connection whose handshake was queued because many handshakes arrived at once.handshakeanddatastill fired on it.

### Runtime#

* Fixed: on Linux and macOS, after a script accessed a pipedprocess.stdoutorprocess.stderr, a full pipe madeconsole.log()andconsole.error()silently drop the rest of their output, and made writes instdio: "inherit"children fail withEAGAIN.
* Fixed: on Linux and macOS, an un-awaitedBun.write(Bun.stdout, new Response(stream))to a full pipe truncated the output and exited with code 0 when nothing else kept the event loop alive.
* Fixed: on Linux and macOS, a read fromprocess.stdinor a child process'sstdoutthat failed right after returning data (for exampleECONNRESET) could end the stream with'end'instead of'error'.
* Fixed: a promise thatfetch(),Bun.write(),server.fetch()orBun.resolve()returned already rejected (for examplefetch("http://[bad")) never emittedunhandledRejectionwhen nothing awaited or caught it, so the process exited 0.
* Fixed: promise callbacks queued from abeforeExitlistener (for example the code after anawait) never ran beforeexit. This needed a script that had not yet usedprocess.nextTickor loadednode:stream.
* Fixed:drainMicrotasks()frombun:jscalso ran queued I/O andpostMessagecallbacks, nesting them inside the calling callback. It now drains only microtasks andprocess.nextTick.
* Fixed: in JIT-optimized functions, ausingdispose method that threw after the block body threw reported its own error instead of aSuppressedErrorcarrying both.
* Fixed:error.stackcould showErrorwithout the name and message, and dropnewfrom constructor frames, if garbage collection ran before the stack was first read. It was reported for errors thrown by an async function and caught afterawait.
* Fixed: calling the defaultError.prepareStackTracefrom a custom one (as source-map-support and depd do) headed every stack withErrorinstead of the error's name, likeTypeError.
* Fixed: in non-strict CommonJS code, calling the function thatCallSite.getFunction()gave a customError.prepareStackTracecrashed for an async function frame afterawaitor a generator frame afternext(). It now returnsundefinedfor internal frames.
* Fixed: the first read oferror.stackcrashed when a customError.prepareStackTraceran a synchronous GC (Bun.gc(true), a heap snapshot) and the strict-mode function that created the error was already unreachable. Fuzzing found it, and no user reported it.
* Fixed: an error message that embedded a string near the maximum string length, as inBuffer.from("x", "q".repeat(2 ** 31 - 10)), aborted the process. It now throws a catchableRangeError..stackon an error with a message that long now returnsname: messagewithout the frames.
* Fixed: printing an error whosecodewas aStringobject with a throwingtoStringor no prototype crashed with "Bun has run out of memory".
* Fixed: a crash when remapping a stack trace if a runtime transpiler cache file had been damaged on disk (by another process or a torn write) and its sourcemap header was invalid. Bun now discards and regenerates the bad entry.
* Fixed:console.logandBun.inspectignored the depth limit for nestedMap,Set,Arrayand Errorcausechains and printed every level. A 1000-deepMapprinted 2 MB, and nesting thousands of levels deep threwRangeError.
* Fixed: a rare crash when garbage collection ran while a module that threw during evaluation (e.g. viaimport()) or a failedBun.resolve()was being rejected.
* Fixed:delete require.cache[path]of an ES module that was still loading, followed byimport()orrequire()of it, crashed or evaluated the module twice. This needed a CommonJS dependency of that module to delete and re-import it while it loaded.
* Fixed:import()crashed ifmock.module(), a plugin'sbuild.module(), or abun --hotreload had replaced the module while an earlierimport()of it was still loading dependencies.
* Fixed: a runtime plugin'sonResolvecould run up to three times for oneimportorrequire(), the extra times on its own answer. It now runs once, when that line executes.
* Fixed:require()of a path that a plugin'sonResolveput in a namespace failed withCannot find package. It now loads through the plugin'sonLoad, likeimport.
* Fixed: a plugin whoseonResolvemapsatobandbtocloadedcfora. It now loadsb.
* Fixed: arequire()in a branch that never ran still called a plugin'sonResolve.
* Fixed: a plugin'sonResolvethat threw failed the whole file. It can now be caught by atryaround therequire().
* Fixed:import()resolved a relativepathfrom a plugin'sonResolveagainst the working directory instead of the importing module.
* Fixed: each garbage-collected module leaked the string that held itsimport.metaURL. Re-importing afterdelete require.cache[...], hot reloading, or terminating Workers leaked one such string per module.
* Fixed: on Linux,process.on("memoryPressure")emitted a falsecriticalevent shortly after a listener was added, with no real memory pressure. Hosts running a privileged PSI watcher such assystemd-oomddid not see it.
* Fixed: on Linux withoutpidfd_open(an old kernel, or a seccomp filter that blocks it), a child process exiting could interrupt a system call on the main thread withEINTR. A native addon orbun:fficall that doesn't retry could see a failedread().
* Fixed: Bun crashed at startup when the working directory, a--configpath, or$XDG_CONFIG_HOME/$HOMEwas so long that addingbunfig.tomlpassed the maximum path length (4096 bytes on Linux, 1024 on macOS).
* Fixed: on macOS,bun --watchleaked one file descriptor for the project directory on every reload.
* Fixed:bun --watchandbun --hotkept a file descriptor open for every directory the resolver read, reaching thousands innode_modules-heavy monorepos.
* Fixed: after a reload followed by a garbage collection,bun --hotcould crash, stop reloading on save, or report an already-handled rejection as the entry point's error. Which one, if any, depended on what the program allocated next.
* Fixed: on Linux, a seccomp profile that failsfaccessat2withEPERMorEINVALmade a hoistedbun installfrom a warm cache fail with "package was not found in the cache". Regression in Bun v1.4.0.
* Fixed: on Linux, a seccomp profile that deniesprlimit64madebun install,bun buildandbun run <script>panic. Regression in Bun v1.4.0.

### Transpiler#

* Fixed: in a class with standard decorators, a field initializer that read a decorated field, like@dec a = 1; b = this.a, sawundefined.
* Fixed:static { this.#m }in a class with anaccessorfield was aSyntaxError.
* Fixed: two classes with standard decorators oraccessorfields in the same scope could get each other's field initial values or throw "Cannot add the same private member more than once".
* Fixed: inbun run, astatic accessorinitializer that read aletorconstdeclared above the class threw aReferenceError. This needed a top-level class statement with no other side effects.
* Fixed: after a process transpiled about 2 GiB of modules at runtime (for example arequire.cache-clearing loop), valid files could fail with aSyntaxErrorbecause keywords lost their trailing space.
* Fixed: the JavaScript parser crashed on animport { ... }clause with more than 65535 names, affectingbun run,bun build, andBun.Transpiler.
* Fixed:Bun.buildused quadratic memory on files that declare the same TypeScriptenummany times. 8,192 declarations dropped from 8.6 GB to 1.1 GB.
* Fixed: a+chain that repeated an inlined TypeScript stringenummember thousands of times used quadratic memory. 8,192 terms took 1.4 GB inbun run.
* Fixed: a TypeScript stringenummember whose value was itself a concatenation, likeB = "1" + "2", printed the wrong value after it was used in a template literal. A second use crashed the transpiler.
* Fixed: a non-binding parameter in a TypeScript type literal signature, liketype T = { foo(1): void }, reportederror: Backtrackwith no location instead ofUnexpected 1.

### bun install#

* Fixed:bun installdid not apply--cafile,--caor the bunfigcafile/casettings when it reached an https registry throughHTTPS_PROXY, so a registry with a self-signed certificate failed withDEPTH_ZERO_SELF_SIGNED_CERT. Certificates were still verified.
* Fixed: on Windows,bun installhung at 100% CPU and never saved the lockfile when the package it replaced held the last hard link of a running executable, as after--backend copyfileor a deleted--cache-dir.opencode upgradehit this.
* Fixed:bun installfrom an existingbun.lockinto a newnode_modulesreinstalled an npm package's bundledfile:dependency as self-referencing symlinks, so importing the package failed withCannot find module.@fly/spriteswas affected.
* Fixed: a regression in Bun v1.4.0 wherebun installrejected a rootfile:package's own relativefile:dependencies that point outside the project.
* Fixed:bun update <name>exited 0 and rewrotepackage.jsonwhen<name>was an optional dependency that resolved through annpm:alias and its download failed.
* Fixed:bun update <dep> <peer>failed witherror: <dep> failed to resolvewhen<peer>was an auto-installed peer dependency that nothing else depends on. Updating either name alone worked.
* Fixed:bun installandbun pm migratepanicked migrating ayarn.lockwhoseresolvedtarball URL had/-/right after the host, such as the tarball of the npm package named-.
* Fixed:bun infoandbun pm viewpanicked when the registry returned a version entry that is not an object. They now print a parse error.
* Fixed:bun pm ls --allandbun list --allpanicked withbuffer too smallwhen a dependency's resolved spec, such as a tarball URL, was longer than 512 bytes.
* Fixed: a regression in Bun v1.4.0 wherebun pm packandbun publishpanicked withint castwhen a write to the tarball failed, for example on a full disk. They now print the error, such asENOSPC, and exit 1.

### JavaScript bundler#

* Fixed: a regression in 1.4.1 where a bundledconst { v } = require("./b.js")of an ES module saw a later value ofv. This needed therequire()to run whileb.jswas still initializing, through an import cycle or a callback.
* Fixed: in bundled output,Object.defineProperty,delete, andObject.freezeon the default import of a CommonJS module did not affect later property reads (regression in 1.4.1).
* Fixed: a regression in 1.4.1 where, with--splitting, a lazy chunk could import an entry without[hash]in its name, so loading that entry with a query string (index.js?v=1) ran it twice.
* Fixed: with--splittingand--target=bun, arequire()of an ES module that imports back into its caller could read a binding before it was initialized, when small chunks were merged.
* Fixed: with--splitting, a chunk shared by several entry points could print an import cycle in the wrong order, so a hoistedvarread asundefinedat runtime. opencode hit this when built with Bun 1.4.1 or 1.4.2.
* Fixed: inbun buildoutput, a barrel file'sexport * as ns from "./b"wasundefinedwhen a file the barrel re-exported earlier importednsback from the barrel and used it at load time.
* Fixed: without--splitting,bun buildemitted__INVALID__REF__for animport()ed module whose only top-level code, besides function declarations and constants, was a deadawait(likefalse && await 0) or, with--target=bun, ausingwith a constant initializer (likeawait using x = null).
* Fixed:bun buildloaded a file's type-only and macro imports when another module imported that file withimport * asorexport * from. The build failed only if one of them could not be bundled, like a macro module importingbununder--target=browser.
* Fixed: tsconfigjsxImportSource: "solid-js"emittedReact.createElementcalls instead of using the automatic runtime.jsx = "solid"and--jsx-runtime=solidare now errors.
* Fixed:Bun.build({ tsconfig: "./custom.json" })ignored the option and used thetsconfig.jsonthat Bun found by itself.
* Fixed:bun buildandbun runprintedInternal error: directory mismatch for directorywhenever--tsconfig-overridewas passed. The override still applied and the command still succeeded.
* Fixed: in a non-minified bundle, a binding namedNaN,Infinity, orundefinedcould capture an inlined constant such as a macro returningNaN, changing its value.
* Fixed: afterBun.buildfinished, all but one bundler worker thread kept its memory (about 100 MB extra after bundling a 2.5 MB file) until its next task.
* Fixed:outputs[..].bytesfrombun build --metafileandBun.build({ metafile: true })undercounted chunks that import other outputs, have a source map comment, or are HTML.
* Fixed: with--splitting,--metafile-mdreported animport()of a bundled file as an external import and counted it under "External imports".
* Fixed:Bun.build({ files })crashed when an in-memory file contained an import orurl()specifier longer than the OS path limit, such as an inlinedata:image over 4 KB in CSS.
* Fixed:bun buildcrashed on a malformed data URL with no comma, such asurl(data:)in CSS,href="data:"in HTML, orimport "data:".
* Fixed:bun buildwith the default--target=browserpanicked when a relative import such asimport "../.."resolved to the filesystem root.
* Fixed:bun build --sourcemapsometimes crashed when linking failed, for example onNo matching export. It now prints the error.Bun.build()was not affected.
* Fixed:Bun.Transpilerandbun build --no-bundlecrashed with identifier minification on an empty file or a JSON, TOML, YAML or text loader input.
* Fixed:Bun.Transpilerandbun build --no-bundleprinted a leading space when output began with++xor+x. They also wrapped a leadinglet;in parentheses.
* Fixed: the dev server andbun build --react-fast-refreshcrashed on a.tsxfile where a class method, accessor or constructor calls anything named like a hook, such asapp.useGlobalPipes().
* Fixed: with React Fast Refresh, a component kept its state after an edit renamed the variables a hook is assigned to, such asconst [a, setA] = useState(0)toconst [b, setB] = useState(0). The state now resets, matchingreact-refresh/babel.
* Fixed: the dev server could crash when a client sent an HMR WebSocket message that only Bun's own test suite uses. The HMR client that runs in the browser never sends it.
* Fixed: the dev server panicked on an HTML route's first bundle when two files imported a file that itself had an unresolved import, such as a package that isn't installed.

#### bun build --react-compiler

* Fixed: with--target=browser, the build crashed on a component where a closure read aletthat was declared below the closure and reassigned later. With some closure bodies the component was left unmemoized instead.
* Fixed: the build crashed on a component containing an object literal with a method shorthand like{ m() {} }. This needed--target=bun,--target=node, or ssr output mode.
* Fixed: with--target=browser, the build panicked with "Expected a node for all scopes" when a ternary's test assigned a call result, like(m = f()) ? 1 : 0, andmwas later put in an array or object literal. That function is now left uncompiled.
* Fixed: build memory grew quadratically with the size of one component. A 100-term||chain used 80 MB, 400 terms about 1 GB, and 800 terms was OOM-killed at 3 GB. 800 terms now uses 78 MB.
* Fixed: build memory doubled with each statement likeif (a) { log() } else if (b) { v = 1 }that reassigned the same local in one component. 16 of them cost 4 MB, 22 cost 1 GB, and more than 24 aborted.
* Fixed: compile time doubled with each level of function expressions nested inside one component. 20 levels took 0.18 s, 25 took 5.3 s, and 30 never finished.
* Fixed: a member assignment whose right-hand side reassigns a variable used in its target, liketail.next = tail = nodeorarr[i] = i++, could throw aTypeErroror store to the wrong object or index.
* Fixed: a compound assignment to a local inside a larger expression ran before that expression's earlier reads of the local, soo["k" + i] = i += 2wrote the wrong key.i += 2as its own statement was not affected.
* Fixed: two assignments of constants to the same variable inside one expression could be reordered when one value was constant-folded, so[(x = 5), -(x = 10), x++]returned wrong values.
* Fixed: a component or hook that calledrequire()orimport()inside its own body and kept the result in a local, likeconst { a } = require("./x"), threwTypeErrororReferenceErrorwhen it ran (regression in 1.4.1). A module-levelrequire()was not affected.
* Fixed: without--minify-identifiers, a compiled component's local shadowed a bundled module's export of the same name that it read through an alias or namespace.import { theme as defaultTheme }thenconst theme = custom ?? defaultThemethrewReferenceError.
* Fixed: assigning a value from props to aletvariable inside a JSX prop or call argument, likev={(x = props.n)}, threwReferenceError: t0 is not definedwhen the component readxafterwards.
* Fixed: a never-read local assigned at the end of severalcatchhandlers lost itslet, causingReferenceError: v is not defined.
* Fixed: with the classic JSX runtime, the output calledjsxDEV()without importing it, so it threwReferenceError: jsxDEV is not definedon first render.
* Fixed: JSX tags starting with_or$(such as the_Transbinding from Lingui's<Trans>macro) compiled to string tags, so the component never rendered.
* Fixed: achildrenattribute alongside JSX children (<div children="x">y</div>) was merged into an array instead of being overridden.

### bun build --compile#

* Fixed: on Linux,bun build --compilerun from inside a compiled executable (BUN_BE_BUN=1orBun.build({ compile })) wrote an executable that crashed at startup, a regression since v1.3.14.
* Fixed:bun build --compile --bytecode --format=esm --splittingwrote an executable that differed by a few bytes on every run from the same inputs, breaking reproducible builds. The executables ran the same.
* Fixed: withbytecode: true,Bun.buildreturned anundefinedoutput and dropped the last asset when a chunk could not be compiled to bytecode, such as one with an invalid\p{...}regex.
* Fixed: a--compile --bytecodeexecutable that had calledinspector.open()crashed when a debugger client connected.

### JavaScript minifier#

* Fixed: a Bun v1.4.1 regression wherebun build --minify-syntax(or--minify) output threwReferenceError: m is not defined. It neededconst m = await import("./x")inside a function, and a next statement that usedmitself once before readingm.n, likereturn [m, m.n].
* Fixed: the minifier rewrotenew Array(n, ...rest)to[n, ...rest], so an emptyrestgave[n]instead ofnempty slots (also underbun run).
* Fixed: with--minify-whitespace, a keyword directly beforerequire()lost its space (return__toCommonJS(...),returnglobalThis.Bun), so the bundle threwReferenceErroror failed to parse. It neededrequire("bun")with--target=bun, or a bundled ES module whose top level held only functions, classes and primitive constants.
* Fixed: with--minify-syntax, a computed template tag likens["tag"]`x`on a CommonJS export lost itsthis, throwingTypeErrorwhen the tag usedthis.
* Fixed:bun build --no-bundleandBun.Transpilerwith identifier minification could rename a parameter, local or import to the name of an export when that name was short (such ast), so the output threwTypeErroror failed to parse. Bundled output was not affected.

### CSS Parser#

* Fixed: the CSS parser rejected a::view-transition-*name plus classes or a chain of classes, like::view-transition-group(hero.big)or::view-transition-new(.a.b), withUnexpected token: .
* Fixed:::view-transition-group-children()printed an "Unsupported pseudo-element" warning, and in CSS modules its name or class argument was not scoped.
* Fixed: in CSS modules, classes inside::view-transition-group(),::view-transition-old(),::view-transition-new()and::view-transition-image-pair()were hashed but missing from the exports object.
* Fixed:bun builddropped an explicitborder-boxclip from the CSSbackgroundshorthand when the origin wascontent-box, turningred content-box border-boxintored content-box.
* Fixed:bun buildcould drop a CSS rule that had nested rules. This needed the same selector four times in one file: two plain rules that merged into the rule before them, the rule with nesting, then a plain rule repeating its properties.

### bun test#

* Fixed:mock.module()spun at 100% CPU forever when its factory returned a pending promise for a module that was already imported, as in the vitest partial-mock pattern.
* Fixed: withjest.useFakeTimers(),advanceTimersByTime()andrunOnlyPendingTimers()never returned when anabortlistener armed a newAbortSignal.timeout(0)every time it fired, or when code polled withwhile (!done) await Bun.sleep(0).
* Fixed: withbun test --isolateor--parallel, a promise or callback that a finished test file left in flight could run during the next file and leak its timers, servers, orprocess.chdir()into it.
* Fixed: withbun test --isolate, aFinalizationRegistrycallback from a finished file could run during a later file if a garbage collection landed just as the first file ended. If that callback threw, the later file lost its remaining tests.
* Fixed: withbun test --isolateor--parallel, a staticimportthat a runtime plugin'sonResolveput in anamespacenever reached the plugin'sonLoad. This happened when the resolved path alone no longer matched theonResolvefilter, as with./data.bar?customorvirt:thing.
* Fixed:bun test --parallelexited 130 on SIGTERM instead of 143, and a worker that crashed mid-file left processes its test spawned running after the run.
* Fixed: a crash when anode:vmcontext, or a finished test file's global underbun test --isolateor--parallel, was garbage collected while one of itsFinalizationRegistrycallbacks was still queued.
* Fixed: a crash inbun test --isolateand--parallelwhen a finished test file left aBun.SQLorBun.RedisClientopen and retried from its rejected query oronclosehandler, once the retry'sconnectionTimeoutfired.
* Fixed:bun testcould crash withNAPI FATAL ERRORafter all tests passed when a native addon such assqlite3still had work in flight.
* Fixed:bun test --coveragecounted only the last load of a file loaded more than once, such asimport("./lib.ts?a")then?b, so lines only an earlier load ran showed as uncovered. Two overlappingimport()s of one file dropped it from the report.
* Fixed:spyOn(obj, 0)on a non-function indexed property returned the mock on reads instead of the value and crashed on the next write.
* Fixed: inbun test, an assertion that compared an asymmetric matcher likeexpect.any(String)orexpect.stringContaining()with an array hole crashed instead of failing. Insideexpect.arrayContaining(), so did a matcher at an index past the end of the actual array.
* Fixed:expect.not.any(),expect.resolvesTo.any()andexpect.rejectsTo.any()gave the wrong verdict for primitive values, soexpect(5).toEqual(expect.not.any(Number))passed.
* Fixed: inbun test, a snapshot matcher or a failingtoEqual()crashed when it had to print a value nested many thousands of levels deep. It now throws aRangeError.

### Bun Shell#

* Fixed: in Bun Shell, a pipeline command that failed with a JavaScript error before it started, such as a redirect into aResponse(cmd | cat > ${new Response("r")}), left the other commands running and the process never exited.
* Fixed: a Bun Shell command with< ${buffer}stdin never finished when the buffer was larger than the pipe buffer, the command exited without reading it, and a background process it had started still held stdin open.
* Fixed: Bun Shell's.then()and.catch()threw synchronously instead of returning a rejected promise when the shell failed to start, such as.cwd()to a missing directory. Code that usedawaitsaw an ordinary rejection either way.

### SQL / SQLite / S3 clients#

* Fixed: inBun.SQL(Postgres), binding anumber[], a plain object or aDateto abyteaparameter silently stored an emptybytea. Strings, Buffers and TypedArrays were stored correctly. It now rejects with aTypeError.
* Fixed: inBun.SQL(Postgres), a parameter that threw while it was encoded, such as an object whosetoString()throws or{ a: 1n }bound tojsonb, closed the connection, failing its pipelined queries and open transaction. Now only that query rejects.
* Fixed: inBun.SQL(Postgres), a result value the client could not decode, such as a multidimensional array, closed the connection and rejected every other pipelined query on it. Now only that query rejects.
* Fixed: inBun.SQLwith MySQL, a query that failed client-side (e.g. a bad parameter) while it waited in a connection's queue never settled, and the next query queued on that connection resolved with another query's rows.
* Fixed: inBun.SQL(Postgres), right after a pipelined query failed, a statement new to that connection and the query issued with it could resolve with each other's rows. This depended on timing, except behind pgdog, where a syntax error triggered it every time.
* Fixed: inBun.SQL(Postgres),sql.begin()resolved even though the server rolled the transaction back, when the callback swallowed a failed query's error. It now rejects withERR_POSTGRES_COMMIT_ROLLED_BACK.
* Fixed: inBun.SQL(MariaDB), aJSONcolumn holding text that MariaDB accepts butJSON.parserefuses closed the connection and rejected every queued query. Now only the query that read it rejects.
* Fixed:Bun.SQL(Postgres) returned a zero from anumeric(p, s)column as"0"instead of"0.0000"when the query used the binary protocol (prepared statements).
* Fixed:bun:sqlitestatements with more than 65535 parameters threw a wrong "expected N values" error, which broke largeBun.SQLsqlite bulk inserts (one report: 7389 rows of 11 columns). With an object of named parameters, the extra ones were silently bound asNULL.
* Fixed:bun:sqlitebound a TypedArray with a detached ArrayBuffer asNULLinstead of an empty BLOB.
* Fixed:bun:sqlitebound a 2 GiBUint8Arrayas empty text instead of throwingSQLITE_TOOBIG.
* Fixed:Database.deserialize()inbun:sqlitethrew for anArrayBuffer, which its types and docs accept.
* Fixed:Database.setCustomSQLite()threwSQLite already loadedin a Worker when called with the same path the process had already loaded.
* Fixed:Bun.write(s3file, Bun.file(path))ands3file.writer()held the entire payload in memory during a multipart upload, so a 500 MB upload raised peak RSS by about 850 MB.
* Fixed: anS3File.writer()garbage-collected withoutend()leaked its buffered bytes, left the multipart upload open, and kept the process from exiting.

### TypeScript types#

* Fixed: theTextEncoder.encodeInto()types marked both arguments optional, so calls missing an argument type-checked but threw at runtime.
* Fixed:@types/bunrejected code that runs fine, includingtest.todo("label")with no callback,test("label", { retry: 1 }, fn),expect(await sql`select 1`).toEqual(rows),Bun.YAML.parse(buffer), andnew Blob().slice()withoutlib.dom.
* Fixed:@types/bunfailed to type check in projects installed withlinker = "isolated"andglobalStore = true.tscreportedTS2307: Cannot find module 'undici-types'whenskipLibCheckwas off.

### Windows#

* Fixed: on Windows 10 and 11,process.report.getReport().header.osReleaseread6.1instead of10.0.
* Fixed: on Windows,Bun.connect()to a named pipe leaked a small amount of memory each time the connect failed synchronously, such as with an invalidtlscertificate.