---
title: The Optimization Ladder - Cemrehan Çavdar
url: https://cemrehancavdar.com/2026/03/10/optimization-ladder/
site_name: hnrss
content_file: hnrss-the-optimization-ladder-cemrehan-çavdar
fetched_at: '2026-03-15T06:00:52.582733'
original_url: https://cemrehancavdar.com/2026/03/10/optimization-ladder/
author: Cemrehan Çavdar
date: '2026-03-10'
description: Python loses every public benchmark by 21-875x. I took the exact problems people use to dunk on Python and climbed every rung of the optimization ladder -- from CPython version upgrades to Rust. Real numbers, real code, real effort costs.
tags:
- hackernews
- hnrss
---

Every year, someone posts a benchmark showing Python is 100x slower than C. The same argument plays out: one side says "benchmarks don't matter, real apps are I/O bound," the other says "just use a real language." Both are wrong.

I took two of the most-citedBenchmarks Gameproblems --n-bodyandspectral-norm-- reproduced them on my machine, and ran every optimization tool I could find. Then I added a third benchmark -- a JSON event pipeline -- to test something closer to real-world code.

Same problems, same Apple M4 Pro, real numbers. This is one developer's journey up the ladder -- not a definitive ranking. A dedicated expert could squeeze more out of any of these tools. The full code is atfaster-python-bench.

Here's the starting point -- CPython 3.13 on the official Benchmarks Game run:

Benchmark

C gcc

CPython 3.13

Ratio

n-body (50M)

2.1s

372s

177x

spectral-norm (5500)

0.4s

350s

875x

fannkuch-redux (12)

2.1s

311s

145x

mandelbrot (16000)

1.3s

183s

142x

binary-trees (21)

1.6s

33s

21x

The question isn't whether Python is slow at computation. It is. The question is how much effort each fix costs and how far it gets you. That's the ladder.

## Why Python Is Slow

The usual suspects are the GIL, interpretation, and dynamic typing. All three matter, but none of them is the real story. The real story is that Python is designed to bemaximally dynamic-- you can monkey-patch methods at runtime, replace builtins, change a class's inheritance chain while instances exist -- and that design makes itfundamentally hard to optimize.

A C compiler seesa + bbetween two integers and emits one CPU instruction. The Python VM seesa + band has to ask: what isa? What isb? Doesa.__add__exist? Has it been replaced since the last call? Isaactually a subclass ofintthat overrides__add__? Every operation goes through this dispatch because the languageguaranteesyou can change anything at any time.

The object overhead is where this shows up concretely. In C, an integer is 4 bytes on the stack. In Python:

C
 
int
:
 
[
 
4
 
bytes
 
]

Python
 
int
:
 
[
 
ob_refcnt
 
8
B
 
]
 
reference
 
count

 
[
 
ob_type
 
8
B
 
]
 
pointer
 
to
 
type
 
object

 
[
 
ob_size
 
8
B
 
]
 
number
 
of
 
digits

 
[
 
ob_digit
 
4
B
 
]
 
the
 
actual
 
value

 
─────────────────

 
=
 
28
 
bytes
 
minimum

(Simplified -- CPython 3.12+ replacedob_sizewithlv_tagin a restructured int layout. Total is still 28 bytes. Seelongintrepr.h.)

4 bytes of number, 24 bytes of machinery to support dynamism.a + bmeans: dereference two heap pointers, look up type slots, dispatch toint.__add__, allocate a newPyObjectfor the result (unless it hits the small-integer cache), update reference counts. CPython 3.11+ mitigates this withadaptive specialization-- hot bytecodes likeBINARY_OP_ADD_INTskip the dispatch for known types -- but the overhead is still there for the general case. One number isn't slow. Millions in a loop are.

The GIL (Global Interpreter Lock) gets blamed a lot, but it hasno impact on single-threaded performance-- it only matters when multiple CPU-bound threads compete for the interpreter. For the benchmarks in this post, the GIL is irrelevant. CPython 3.13 shipped experimental free-threaded mode (--disable-gil) -- still experimental in 3.14 -- but as we'll see, it actually makes single-threaded codeslowerbecause removing the GIL adds overhead to every reference count operation.

The interpretation overhead is real but is being actively addressed. CPython 3.11'sFaster CPythonproject added adaptive specialization -- the VM detects "hot" bytecodes and replaces them with type-specialized versions, skipping some of the dispatch. It helped (~1.4x). CPython 3.13 went further with an experimentalcopy-and-patch JIT compiler-- a lightweight JIT that stitches together pre-compiled machine code templates instead of generating code from scratch. It's not a full optimizing JIT like V8's TurboFan or a tracing JIT like PyPy's; it's designed to be small and fast to start, avoiding the heavyweight JIT startup cost that has historically kept CPython from going this route. Early results in 3.13 show no improvement on most benchmarks, but the infrastructure is now in place for more aggressive optimizations in future releases. JavaScript's V8 achieves much better JIT results, but V8 also had a large dedicated team and a single-threaded JavaScript execution model that makes speculative optimization easier. (For more on the "why doesn't CPython JIT" question, see Anthony Shaw's"Why is Python so slow?".)

So the picture is:Python is slow because its dynamic design requires runtime dispatch on every operation.The GIL, the interpreter, the object model -- these are all consequences of that design choice. Each rung of the ladder removes some of this dispatch. The higher you climb, the more you bypass -- and the more effort it costs.

## Rung 0: Upgrade CPython

Cost: changing your base image. Reward: up to 1.4x.

Version

N-body

vs 3.14

Spectral-norm

vs 3.14

CPython 3.10

1,663ms

0.75x

16,826ms

0.83x

CPython 3.11

1,200ms

1.04x

13,430ms

1.05x

CPython 3.13

1,134ms

1.10x

13,637ms

1.03x

CPython 3.14

1,242ms

1.0x

14,046ms

1.0x

CPython 3.14t (free-threaded)

1,513ms

0.82x

14,551ms

0.97x

The story is3.10 to 3.11: a 1.39x speedup on n-body, for free. That's theFaster CPythonproject -- adaptive specialization of bytecodes, inline caching, zero-cost exceptions. 3.13 squeezed out a bit more. 3.14 gave some of it back -- a minor regression on these benchmarks.

Free-threaded Python (3.14t) issloweron single-threaded code. The GIL removal adds overhead to every reference count operation. Worth it only if you have genuinely parallel CPU-bound threads. (Full version comparison)

This rung costs nothing. If you're still on 3.10, upgrade.

## Rung 1: Alternative Runtimes (PyPy, GraalPy)

Cost: switching interpreters. Reward: 6-66x.

N-body

Spectral-norm

CPython 3.14

1,242ms

14,046ms

GraalPy

211ms (
5.9x
)

212ms (
66x
)

PyPy

98ms (
13x
)

1,065ms (
13x
)

Both are JIT-compiled runtimes that generate native machine code from your unmodified Python. Zero code changes. Just a different interpreter.

PyPy uses a tracing JIT -- it records hot loops and compiles them. GraalPy runs on GraalVM's Truffle framework with a method-based JIT. PyPy wins on n-body (13x vs 5.9x), but GraalPy dominates spectral-norm (66x vs 13x) -- the matrix-heavy inner loop plays to GraalVM's strengths. GraalPy also offers Java interop and is actively developed by Oracle.

The catch: ecosystem compatibility. Both support major packages, but C extensions run through compatibility layers that can be slower than on CPython. GraalPy is on Python 3.12 (no 3.14 yet) and has slow startup -- it's JVM-based, so the JIT needs warmup before reaching peak performance. For pure Python code with long-running hot loops -- these are free speed.

## Rung 2: Mypyc

Cost: type annotations you probably already have. Reward: 2.4-14x.

N-body

Spectral-norm

CPython 3.14

1,242ms

14,046ms

Mypyc

518ms (
2.4x
)

990ms (
14x
)

Mypyc compiles type-annotated Python to C extensions using the same type analysis as mypy. No new syntax, no new language -- just your existing typed Python, compiled ahead of time.

# Already valid typed Python -- mypyc compiles this to C

def
 
advance
(
dt
:
 
float
,
 
n
:
 
int
,
 
bodies
:
 
list
[
Body
],
 
pairs
:
 
list
[
BodyPair
])
 
->
 
None
:

 
dx
:
 
float

 
dy
:
 
float

 
dz
:
 
float

 
dist_sq
:
 
float

 
dist
:
 
float

 
mag
:
 
float

 
for
 
_
 
in
 
range
(
n
):

 
for
 
(
r1
,
 
v1
,
 
m1
),
 
(
r2
,
 
v2
,
 
m2
)
 
in
 
pairs
:

 
dx
 
=
 
r1
[
0
]
 
-
 
r2
[
0
]

 
dy
 
=
 
r1
[
1
]
 
-
 
r2
[
1
]

 
dz
 
=
 
r1
[
2
]
 
-
 
r2
[
2
]

 
dist_sq
 
=
 
dx
 
*
 
dx
 
+
 
dy
 
*
 
dy
 
+
 
dz
 
*
 
dz

 
dist
 
=
 
math
.
sqrt
(
dist_sq
)

 
mag
 
=
 
dt
 
/
 
(
dist_sq
 
*
 
dist
)

 
# ...

The difference from the baseline: explicit type declarations on every local variable so mypyc can use C primitives instead of Python objects, and decomposing** (-1.5)intosqrt()+ arithmetic to avoid slow power dispatch. That's it -- no special decorators, no new build system beyondmypycify().

The mypy project itself -- ~100k+ lines of Python -- achieved a4x end-to-end speedupby compiling with mypyc. The official docs say "1.5x to 5x" for existing annotated code, "5x to 10x" for code tuned for compilation. The spectral-norm result (14x) lands above that range because the inner loop is pure arithmetic that mypyc compiles directly to C. On our dict-heavy JSON pipeline, mypyc hit 2.3x on pre-parsed dicts -- closer to the expected floor.

The constraint: mypyc supports a subset of Python. Dynamic patterns like**kwargs,getattrtricks, and heavily duck-typed code will compile but won't be optimized -- they fall back to slow generic paths. But if your code already passes mypy strict mode, mypyc is the lowest-effort compilation rung on the ladder.

## Rung 3: NumPy

Cost: knowing NumPy. Reward: up to 520x.

Spectral-norm

CPython 3.14

14,046ms

NumPy

27ms (
520x
)

520x. Faster than our single-threaded Rust at 154x on the same problem -- though NumPy delegates to BLAS, which uses multiple cores.

Spectral-norm is matrix-vector multiplication. NumPy pre-computes the matrix once and delegates to BLAS (Apple Accelerate on macOS):

a
 
=
 
build_matrix
(
n
)

for
 
_
 
in
 
range
(
10
):

 
v
 
=
 
a
.
T
 
@
 
(
a
 
@
 
u
)

 
u
 
=
 
a
.
T
 
@
 
(
a
 
@
 
v
)

Each@is a single call to hand-optimized BLAS with SIMD and multithreading. NumPy trades O(N) memory for O(N^2) memory -- it stores the full 2000x2000 matrix (30MB) -- but the computation is done in compiled C/C++ (Apple Accelerate on macOS, OpenBLAS or MKL on Linux), not Python.

This is the lesson people miss when they say "Python is slow." Python the loop runner is slow. Python the orchestrator of compiled libraries is as fast as anything.

The constraint: your problem must fit vectorized operations. Element-wise math, matrix algebra, reductions, conditionals (np.wherecomputes both branches and masks the result -- redundant work, but still faster than a Python loop on large arrays) -- NumPy handles all of these. What it can't help with: sequential dependencies where each step feeds the next, recursive structures, and small arrays where NumPy's per-call overhead costs more than the computation itself.

## Interlude: JAX

Cost: rewriting loops asjax.lax.fori_loop+ array operations. Reward: 12-1,633x.

A Reddit commenter (justneurostuff) suggested testingJAX-- an array computing library that uses XLA JIT compilation. I expected it to land somewhere near NumPy. I was wrong.

N-body

Spectral-norm

CPython 3.14

1,242ms

14,046ms

NumPy

--

27ms (
520x
)

JAX JIT

100ms (
12.2x
)

8.6ms (
1,633x
)

8.6ms on spectral-norm. That's 3x faster than NumPy and the fastest result in this entire post. On n-body, 12.2x -- between Mypyc and Numba. Both results match the CPython baseline to 9 decimal places. This is single-threaded -- forcing one thread gave 9.1ms vs 8.6ms on spectral-norm.

I don't know JAX well enough to explain exactly why it's 3x faster than NumPy on the same matrix multiplications. Both call BLAS under the hood. My best guess is that JAX's@jitcompiles the entire function -- matrix build, loop, dot products -- so Python is never involved between operations, while NumPy returns to Python between each@call. But I haven't verified that in detail. Might be time to learn.

The catch: JAX is a different programming model. Python loops becomelax.fori_loop. Conditionals becomelax.cond. You're writing functional array programs that happen to use Python syntax -- closer to a domain-specific language than a drop-in optimizer. But if your problem fits, the numbers speak for themselves. JAX isn't the only library that compiles array code -- PyTorch hastorch.compile, for example. I only tested JAX, so I can't say whether others would produce similar results on these benchmarks.

## Rung 4: Numba

Cost:@njit+ restructuring data into NumPy arrays. Reward: 56-135x.

N-body

Spectral-norm

CPython 3.14

1,242ms

14,046ms

Numba @njit

22ms (
56x
)

104ms (
135x
)

Numba JIT-compiles decorated functions to machine code via LLVM:

@njit
(
cache
=
True
)

def
 
advance
(
dt
,
 
n
,
 
pos
,
 
vel
,
 
mass
):

 
for
 
i
 
in
 
range
(
n
):

 
for
 
j
 
in
 
range
(
i
 
+
 
1
,
 
n
):

 
dx
 
=
 
pos
[
i
,
 
0
]
 
-
 
pos
[
j
,
 
0
]

 
dy
 
=
 
pos
[
i
,
 
1
]
 
-
 
pos
[
j
,
 
1
]

 
dz
 
=
 
pos
[
i
,
 
2
]
 
-
 
pos
[
j
,
 
2
]

 
dist
 
=
 
sqrt
(
dx
 
*
 
dx
 
+
 
dy
 
*
 
dy
 
+
 
dz
 
*
 
dz
)

 
mag
 
=
 
dt
 
/
 
(
dist
 
*
 
dist
 
*
 
dist
)

 
vel
[
i
,
 
0
]
 
-=
 
dx
 
*
 
mag
 
*
 
mass
[
j
]

 
# ...

One decorator. Restructure data into NumPy arrays. The constraint: Numba works best with NumPy arrays and numeric types. It has limited support for typed dicts, typed lists, and@jitclass, but strings and general Python objects are largely out of reach. It's a scalpel, not a saw.

## Rung 5: Cython

Cost: learning C's mental model, expressed in Python syntax. Reward: 99-124x.

N-body

Spectral-norm

CPython 3.14

1,242ms

14,046ms

Cython

10ms (
124x
)

142ms (
99x
)

124x on n-body. Within 10% of Rust. But here's the thing about this rung:

My first Cython n-body got 10.5x.Same Cython, same compiler. The final version got 124x. The difference was three landmines, none of which produced warnings:

* Cython's**operator with float exponents. Even with typed doubles and-ffast-math,x ** 0.5is 40x slower thansqrt(x)in Cython -- the operator goes through a slow dispatch path instead of compiling to C'ssqrt(). The n-body baseline uses** (-1.5), which can't be replaced with a singlesqrt()call -- it required decomposing the formula intosqrt()+ arithmetic.7x penalty on the overall benchmark.
* Precomputed pair index arrays prevent the C compiler from unrolling the nested loop.2x penalty.The "clever" version is slower.
* Missing@cython.cdivision(True)inserts a zero-division check before every floating-point divide in the inner loop. Millions of branches that are never taken.

Cython's promise is that it "makes writing C extensions for Python as easy as Python itself." In practice that means: learn C's mental model, express it in Python syntax, and use the annotation report (cython -a) to verify the compiler did what you think. The full story is inThe Cython Minefield.

The reward is real -- 99-124x, matching compiled languages. But the failure mode is silent. All three landmines cost you silently, and the annotation report is the only way to catch them.

## Rung 6: The New Wave

Cost: new toolchains, rough edges, ecosystem gaps. Reward: 26-198x.

Three tools promise to compile Python (or Python-like code) to native machine code. I tested all three.

N-body

Speedup

Spectral-norm

Speedup

The catch

Codon 0.19

47ms

26x

99ms

142x

Own runtime, limited stdlib, limited CPython interop

Mojo nightly

16ms

78x

118ms

119x

New language (pre-1.0), full rewrite required

Taichi 1.7

16ms

78x

71ms

198x

Python 3.13 only (no 3.14 wheels)

The numbers are real. The developer experience is rough. Codon can't import your existing code. Mojo is a new language wearing Python's clothes. Taichi has the best spectral-norm result (198x) butdoesn't ship wheels for Python 3.14-- its numbers above were benchmarked on a separate Python 3.13 environment. That's the compromise with these tools: if your runtime doesn't keep up with CPython releases, you're stuck on an old version or juggling multiple environments. (Full deep dive with code and DX verdicts)

None are drop-in. All are worth watching.

## Rung 7: Rust via PyO3

Cost: learning Rust. Reward: 113-154x.

N-body

Spectral-norm

CPython 3.14

1,242ms

14,046ms

Rust (PyO3)

11ms (
113x
)

91ms (
154x
)

The top of the ladder. But notice: on n-body, Cython at 10ms vs Rust at 11ms -- they're essentially tied. Both compiled to native machine code. The remaining difference is noise, not a fundamental language gap.

The real Rust advantage isn't raw speed -- it'spipeline ownership. When Rust parses JSON directly with serde into typed structs, it never creates a Python dict. It bypasses the Python object system entirely. That matters more on the next benchmark.

## The Ceiling

The Benchmarks Game problems are pure compute: tight loops, no I/O, no data structures beyond arrays. Most Python code looks nothing like that. So I built a third benchmark: load 100K JSON events, filter, transform, aggregate per user. Dicts, strings, datetime parsing -- the kind of code that makes Numba useless and makes Cython fight the Python object system.

First, every tool starts from pre-parsed Python dicts -- same input, same work:

Approach

Time

Speedup

What it costs you

CPython 3.14

48ms

1.0x

Nothing

Mypyc

21ms

2.3x

Type annotations

Cython (dict optimized)

12ms

4.1x

Days of annotation work

4.1x. Not 50x. The bottleneck isPython dict access. Even Cython's fully optimized version --@cython.cclass, C arrays for counters, direct CPython C-API calls (PyList_GET_ITEM,PyDict_GetItemwith borrowed refs) -- still reads input dicts through the Python C API.

But wait -- why are we feeding Cython Python dicts at all?json.loads()takes ~57ms to create those dicts. That's more than the entire baseline pipeline. What if Cython reads the raw bytes itself?

I wrote a second Cython pipeline that callsyyjson-- a general-purpose C JSON parser, comparable to Rust's serde_json. Both are schema-agnostic: they parse any valid JSON, not just our event format. Cython walks the parsed tree with C pointers, filters and aggregates into C structs, and builds Python dicts only for the final output. For Rust, idiomatic serde with zero-copy deserialization. Both own the data end-to-end:

Approach

Time

Speedup

What it costs you

CPython 3.14 (json.loads + pipeline)

105ms

1.0x

Nothing

Mypyc (json.loads + pipeline)

77ms

1.4x

Type annotations

Cython (json.loads + pipeline)

67ms

1.6x

C-API dict access

Rust (serde, from bytes)

21ms

5.0x

New language + bindings

Cython (yyjson, from bytes)

17ms

6.3x

C library + Cython declarations

6.3x for Cython, 5.0x for Rust.The ceiling was never the pipeline code -- it wasjson.loads(). Both approaches use general-purpose JSON parsers -- yyjson on the Cython side, serde on the Rust side -- and both avoid Python objects entirely in the hot loop: Cython walks yyjson's C tree into C structs, Rust deserializes into native structs via serde.

I'm not claiming Cython is faster than Rust or vice versa. A sufficiently motivated person could make either one faster -- swap parsers, tune allocators, restructure the pipeline. The point isn't which tool wins this specific benchmark. The point ishow many rungs you're willing to climb. Both land in the same neighborhood once you bypassjson.loads(). The code is atfaster-python-bench.

## The Full Report Card

### N-body (500K iterations, tight floating-point loops)

Approach

Time

Speedup

What it costs you

CPython 3.10

1,663ms

0.75x

Old version

CPython 3.14

1,242ms

1.0x

Nothing

CPython 3.14t

1,513ms

0.82x

GIL-free but slower single-thread

Mypyc

518ms

2.4x

Type annotations

GraalPy

211ms

5.9x

Python 3.12 only, ecosystem compatibility

JAX JIT

100ms

12.2x

Rewrite loops as 
lax.fori_loop

PyPy

98ms

13x

Ecosystem compatibility

Codon

47ms

26x

Separate runtime, limited stdlib

Numba

22ms

56x

@njit
 + NumPy arrays

Taichi

16ms

78x

Python 3.13 only (no 3.14 wheels)

Mojo

16ms

78x

New language + toolchain

Cython

10ms

124x

C knowledge + landmines

Rust (PyO3)

11ms

113x

Learning Rust

### Spectral-norm (N=2000, matrix-vector multiply)

Approach

Time

Speedup

What it costs you

CPython 3.10

16,826ms

0.83x

Old version

CPython 3.14

14,046ms

1.0x

Nothing

CPython 3.14t

14,551ms

0.97x

GIL-free but slower single-thread

Mypyc

990ms

14x

Type annotations

GraalPy

212ms

66x

Python 3.12 only, ecosystem compatibility

PyPy

1,065ms

13x

Ecosystem compatibility

Codon

99ms

142x

Separate runtime, limited stdlib

Numba

104ms

135x

@njit
 + NumPy arrays

Mojo

118ms

119x

New language + toolchain

Rust (PyO3)

91ms

154x

Learning Rust

Cython

142ms

99x

C knowledge + landmines

Taichi

71ms

198x

Python 3.13 only (no 3.14 wheels)

NumPy

27ms

520x

Knowing NumPy + O(N^2) memory

JAX JIT

8.6ms

1,633x

Rewrite loops as 
lax.fori_loop

### JSON pipeline (100K events, end-to-end from raw bytes)

Approach

Time

Speedup

What it costs you

CPython 3.14 (json.loads + pipeline)

105ms

1.0x

Nothing

Mypyc (json.loads + pipeline)

77ms

1.4x

Type annotations

Cython (json.loads + pipeline)

67ms

1.6x

C-API dict access

Rust (serde, from bytes)

21ms

5.0x

New language + bindings

Cython (yyjson, from bytes)

17ms

6.3x

C library + Cython declarations

## When to Stop Climbing

The effort curve is exponential. Mypyc (2.4-14x) costs type annotations. PyPy/GraalPy (6-66x) costs a binary swap. Numba (56-135x) costs a decorator and data restructuring. JAX (12-1,633x) costs rewriting your code functionally. Cython (99-124x) costs days and C knowledge. Rust (113-154x) costs learning a new language.

Upgrade first.3.10 to 3.11 gives you 1.4x for free.

Mypyc for typed codebases.If your code already passes mypy strict, compile it. 2.4x on n-body, 14x on spectral-norm, for almost no work.

NumPy for vectorizable math.If your problem is matrix algebra or element-wise operations, NumPy gets you 520x with code you already know.

JAX if you can express it functionally.Same array paradigm as NumPy, but XLA whole-graph compilation took spectral-norm to 1,633x -- 3x faster than NumPy. The cost is rewriting loops aslax.fori_loopand conditionals aslax.cond. On problems that don't vectorize well (n-body with 5 bodies), JAX is 12x -- good but not exceptional.

Numba for numeric loops.@njitgives you 56-135x with one decorator and honest error messages.

Cython if you know C.99-124x is real, but the failure mode is silent slowness.

Rust for pipeline ownership.On pure compute, Cython and Rust are neck and neck. The real advantage is when Rust owns the data flow end-to-end.

PyPy or GraalPy for pure Python.6-66x for zero code changes is remarkable, if your dependencies support it. GraalPy's spectral-norm result (66x) rivals compiled solutions.

Most code doesn't need any of this.The pipeline benchmark -- the most realistic of the three -- topped out at 4.1x when starting from Python dicts. 6.3x when Cython called yyjson and owned the bytes. If your hot path isdict[str, Any], the answer might be "stop creating dicts," not "change the language." And if your code is I/O bound, none of this matters at all.

Profile before you optimize.cProfileto find the function.line_profilerto find the line. Then pick the right rung.

Not covered:Nuitka(Python-to-C compiler, mostly used for packaging -- speedups are in the Mypyc range),Pythran(NumPy-focused AOT compiler, niche),SPy(Antonio Cuni's static Python dialect -- not ready yet but worth watching), andCinderX(Meta's performance-oriented CPython fork -- not ready yet).

Found an error?Open a PR.

## Edits

2026-03-10:Rewrote the NumPy constraints paragraph. The original listed"irregular access patterns, conditionals per element, recursive structures"as things NumPy can't handle. Two of those were wrong: NumPy fancy indexing handles irregular access fine (22x faster than Python on random gather), andnp.wherehandles conditionals (2.8-15.5x faster on 1M elements, even though it computes both branches). Replaced with things NumPy actually can't help with: sequential dependencies (n-body with 5 bodies is 2.3x slower with NumPy), recursive structures, and small arrays (NumPy loses below ~50 elements due to per-call overhead).

2026-03-10:The original text said"Early results are modest (single-digit percent improvements)"-- implying the 3.13 JIT was already delivering gains. Changed to"Early results in 3.13 show no improvement on most benchmarks."Bad wording on my part -- 3.13 JIT shows no speedup (and can be slightly slower). The speedups are coming in 3.15:Savannah Ostrowski's preliminary FastAPI benchmarksshow ~8% improvement on 3.15 (see alsodoesjitgobrrr.com). Thanks toFidget-Spinner(CPython core developer working on the JIT) for thecorrection.

2026-03-11:Added JAX JIT benchmarks aftera Reddit commentfrom justneurostuff suggested testing it. Results: 1,633x on spectral-norm (fastest in the post -- 3x faster than NumPy), 12.2x on n-body. Both match baseline to 9 decimal places. Added as an interlude between NumPy and Numba sections, and to both report card tables.