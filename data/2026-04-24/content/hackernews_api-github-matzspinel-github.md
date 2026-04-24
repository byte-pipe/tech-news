---
title: GitHub - matz/spinel · GitHub
url: https://github.com/matz/spinel
site_name: hackernews_api
content_file: hackernews_api-github-matzspinel-github
fetched_at: '2026-04-24T19:51:18.152168'
original_url: https://github.com/matz/spinel
author: dluan
date: '2026-04-24'
description: Contribute to matz/spinel development by creating an account on GitHub.
tags:
- hackernews
- trending
---

matz

 

/

spinel

Public

* NotificationsYou must be signed in to change notification settings
* Fork11
* Star858

 
 
 
 
master
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

454 Commits
454 Commits
.claude
.claude
 
 
benchmark
benchmark
 
 
lib
lib
 
 
test
test
 
 
.gitignore
.gitignore
 
 
AUTHORS
AUTHORS
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
spinel
spinel
 
 
spinel_codegen.rb
spinel_codegen.rb
 
 
spinel_parse
spinel_parse
 
 
spinel_parse.c
spinel_parse.c
 
 
spinel_parse.rb
spinel_parse.rb
 
 
View all files

## Repository files navigation

# Spinel -- Ruby AOT Compiler

Spinel compiles Ruby source code into standalone native executables.
It performs whole-program type inference and generates optimized C code,
achieving significant speedups over CRuby.

Spinel isself-hosting: the compiler backend is written in Ruby and
compiles itself into a native binary.

## How It Works

Ruby (.rb)
 |
 v
spinel_parse Parse with Prism (libprism), serialize AST
 | (C binary, or CRuby + Prism gem as fallback)
 v
AST text file
 |
 v
spinel_codegen Type inference + C code generation
 | (self-hosted native binary)
 v
C source (.c)
 |
 v
cc -O2 -Ilib -lm Standard C compiler + runtime header
 |
 v
Native binary Standalone, no runtime dependencies

## Quick Start

#
 Fetch libprism sources (from the prism gem on rubygems.org):

make deps

#
 Build everything:

make

#
 Write a Ruby program:

cat 
>
 hello.rb 
<<
'
RUBY
'

def
 
fib
(
n
)

 
if
 n 
<
 
2

 n

 
else

 fib(n 
-
 
1
) 
+
 fib(n 
-
 
2
)

 
end

end

puts
 fib(
34
)

RUBY

#
 Compile and run:

./spinel hello.rb
./hello 
#
 prints 5702887 (instantly)

### Options

./spinel app.rb 
#
 compiles to ./app

./spinel app.rb -o myapp 
#
 compiles to ./myapp

./spinel app.rb -c 
#
 generates app.c only

./spinel app.rb -S 
#
 prints C to stdout

## Self-Hosting

Spinel compiles its own backend. The bootstrap chain:

CRuby + spinel_parse.rb → AST
CRuby + spinel_codegen.rb → gen1.c → bin1
bin1 + AST → gen2.c → bin2
bin2 + AST → gen3.c
gen2.c == gen3.c (bootstrap loop closed)

## Benchmarks

74 tests pass. 55 benchmarks pass.
Geometric mean:~11.6x fasterthan miniruby (Ruby 4.1.0dev) across
the 28 benchmarks below. Baseline is the latest CRubyminirubybuild
(without bundled gems), which is considerably faster than the systemruby(3.2.3); Spinel's advantage is correspondingly smaller but still
substantial on computation-heavy workloads.

### Computation

Benchmark

Spinel

miniruby

Speedup

life (Conway's GoL)

20 ms

1_733 ms

86.7x

ackermann

5 ms

374 ms

74.8x

mandelbrot

25 ms

1_453 ms

58.1x

fib (recursive)

17 ms

581 ms

34.2x

nqueens

10 ms

304 ms

30.4x

tarai

16 ms

461 ms

28.8x

tak

22 ms

532 ms

24.2x

matmul

13 ms

313 ms

24.1x

sudoku

6 ms

102 ms

17.0x

partial_sums

93 ms

1_498 ms

16.1x

fannkuch

2 ms

19 ms

9.5x

sieve

39 ms

332 ms

8.5x

fasta (DNA seq gen)

3 ms

21 ms

7.0x

### Data Structures & GC

Benchmark

Spinel

miniruby

Speedup

rbtree (red-black tree)

24 ms

543 ms

22.6x

splay tree

14 ms

195 ms

13.9x

huffman (encoding)

6 ms

59 ms

9.8x

so_lists

76 ms

410 ms

5.4x

binary_trees

11 ms

40 ms

3.6x

linked_list

136 ms

388 ms

2.9x

gcbench

1_845 ms

3_641 ms

2.0x

### Real-World Programs

Benchmark

Spinel

miniruby

Speedup

json_parse

39 ms

394 ms

10.1x

bigint_fib (1000 digits)

2 ms

16 ms

8.0x

ao_render (ray tracer)

417 ms

3_334 ms

8.0x

pidigits (bigint)

2 ms

13 ms

6.5x

str_concat

2 ms

13 ms

6.5x

template engine

152 ms

936 ms

6.2x

csv_process

234 ms

860 ms

3.7x

io_wordcount

33 ms

97 ms

2.9x

## Supported Ruby Features

Core: Classes, inheritance,super,include(mixin),attr_accessor,Struct.new,alias, module constants, open classes for built-in types.

Control Flow:if/elsif/else,unless,case/when,case/in(pattern matching),while,until,loop,for..in(range and array),break,next,return,catch/throw,&.(safe navigation).

Blocks:yield,block_given?,&block,proc {},Proc.new,
lambda-> x { },method(:name). Block methods:each,each_with_index,map,select,reject,reduce,sort_by,any?,all?,none?,times,upto,downto.

Exceptions:begin/rescue/ensure/retry,raise,
custom exception classes.

Types: Integer, Float, String (immutable + mutable), Array, Hash,
Range, Time, StringIO, File, Regexp, Bigint (auto-promoted), Fiber.
Polymorphic values via tagged unions. Nullable object types (T?)
for self-referential data structures (linked lists, trees).

Global Variables:$namecompiled to static C variables with
type-mismatch detection at compile time.

Strings:<<automatically promotes to mutable strings (sp_String)
for O(n) in-place append.+, interpolation,tr,ljust/rjust/center,
and all standard methods work on both. Character comparisons likes[i] == "c"are optimized to direct char array access (zero allocation).
Chained concatenation (a + b + c + d) collapses to a single malloc
viasp_str_concat4/sp_str_concat_arr-- N-1 fewer allocations.
Loop-localstr.split(sep)reuses the samesp_StrArrayacross
iterations (csv_process: 4 M allocations eliminated).

Regexp: Built-in NFA regexp engine (no external dependency).=~,$1-$9,match?,gsub(/re/, str),sub(/re/, str),scan(/re/),split(/re/).

Bigint: Arbitrary precision integers via mruby-bigint. Auto-promoted
from loop multiplication patterns (e.g.q = q * k). Linked as static
library -- only included when used.

Fiber: Cooperative concurrency viaucontext_t.Fiber.new,Fiber#resume,Fiber.yieldwith value passing. Captures free
variables via heap-promoted cells.

Memory: Mark-and-sweep GC with size-segregated free lists, non-recursive
marking, and sticky mark bits. Small classes (≤8 scalar fields, no
inheritance, no mutation through parameters) are automatically
stack-allocated asvalue types-- 1M allocations of a 5-field class
drop from 85 ms to 2 ms. Programs using only value types emit no GC
runtime at all.

Symbols: Separatesp_symtype, distinct from strings (:a != "a").
Symbol literals are interned at compile time (SPS_nameconstants);String#to_symuses a dynamic pool only when needed. Symbol-keyed
hashes ({a: 1}) use a dedicatedsp_SymIntHashthat storessp_sym(integer) keys directly rather than strings -- no strcmp, no
dynamic string allocation.

I/O:puts,print,printf,p,gets,ARGV,ENV[],File.read/write/open(with blocks),system(), backtick.

## Optimizations

Whole-program type inference drives several compile-time optimizations:

* Value-type promotion: small immutable classes (≤8 scalar fields)
become C structs on the stack, eliminating GC overhead entirely.
* Constant propagation: simple literal constants (N = 100) are
inlined at use sites instead of going throughcst_Nruntime lookup.
* Loop-invariant length hoisting:while i < arr.lengthevaluatesarr.lengthonce before the loop;while i < str.lengthhoistsstrlen. Mutation of the receiver inside the body (e.g.arr.push)
correctly disables the hoist.
* Method inlining: short methods (≤3 statements, non-recursive)
getstatic inlineso gcc can inline them at call sites.
* String concat chain flattening:a + b + c + dcompiles to a
singlesp_str_concat4/sp_str_concat_arrcall -- one malloc
instead of N-1 intermediate strings.
* Bigint auto-promotion: loops withx = x * yor fibonacci-stylec = a + bself-referential addition auto-promote to bigint.
* Bigintto_s: divide-and-conquer O(n log²n) via mruby-bigint'smpz_get_strinstead of naive O(n²).
* Static symbol interning:"literal".to_symresolves to a
compile-timeSPS_<name>constant; the runtime dynamic pool is
only emitted when dynamic interning is actually used.
* strlencaching in sub_range: when a string's length is
hoisted,str[i]accesses usesp_str_sub_range_lento skip the
internal strlen call.
* split reuse:fields = line.split(",")inside a loop reuses
the existingsp_StrArrayrather than allocating a new one.
* Dead-code elimination: compiled with-ffunction-sections -fdata-sectionsand linked with--gc-sections; each unused
runtime function is stripped from the final binary.
* Iterative inference early exit: the param/return/ivar fixed-point
loop stops as soon as a signature of the three refined arrays stops
changing. Most programs converge in 1-2 iterations instead of the
full 4, cutting bootstrap time by ~14%.
* parse_id_listbyte walk: the AST-field list parser (called
~120 K times during self-compile) walks bytes manually vias.bytes[i]instead ofs.split(","), dropping N+1 allocations
per call to 2.
* Warning-free build: generated C compiles cleanly at the default
warning level across every test and benchmark; the harness uses-Werrorso regressions surface immediately.

## Architecture

spinel One-command wrapper script (POSIX shell)
spinel_parse.c C frontend: libprism → text AST (1_061 lines)
spinel_codegen.rb Compiler backend: AST → C code (21_109 lines)
lib/sp_runtime.h Runtime library header (581 lines)
lib/sp_bigint.c Arbitrary precision integers (5_394 lines)
lib/regexp/ Built-in regexp engine (1_759 lines)
test/ 74 feature tests
benchmark/ 55 benchmarks
Makefile Build automation

The compiler backend (spinel_codegen.rb) is written in a Ruby subset
that Spinel itself can compile: classes,def,attr_accessor,if/case/while,each/map/select,yield,begin/rescue,
String/Array/Hash operations, File I/O.

No metaprogramming, noeval, norequirein the backend.

The runtime (lib/sp_runtime.h) contains GC, array/hash/string
implementations, and all runtime support as a single header file.
Generated C includes this header, and the linker pulls only the
needed parts fromlibspinel_rt.a(bigint + regexp engine).

The parser has two implementations:

* spinel_parse.clinks libprism directly (no CRuby needed)
* spinel_parse.rbuses the Prism gem (CRuby fallback)

Both produce identical AST output. Thespinelwrapper prefers the
C binary if available.require_relativeis resolved at parse time
by inlining the referenced file.

## Building

make deps 
#
 fetch libprism into vendor/prism (one-time)

make 
#
 build parser + regexp library + bootstrap compiler

make 
test
 
#
 run 74 feature tests (requires bootstrap)

make bench 
#
 run 55 benchmarks (requires bootstrap)

make bootstrap 
#
 rebuild compiler from source

sudo make install 
#
 install to /usr/local (spinel in PATH)

make clean 
#
 remove build artifacts

Override install prefix:make install PREFIX=$HOME/.local

Prismis the Ruby parser used byspinel_parse.make depsdownloads the prism gem tarball from
rubygems.org and extracts its C sources tovendor/prism. If you
already have the prism gem installed, the build auto-detects it; you
can also point at a custom location withPRISM_DIR=/path/to/prism.

CRuby is needed only for the initial bootstrap. Aftermake, the
entire pipeline runs without Ruby.

## Limitations

* No eval:eval,instance_eval,class_eval
* No metaprogramming:send,method_missing,define_method(dynamic)
* No threads:Thread,Mutex(Fiber is supported)
* No encoding: assumes UTF-8/ASCII
* No general lambda calculus: deeply nested-> x { }with[]calls

## Dependencies

* Build time:libprism(C library),
CRuby (bootstrap only)
* Run time: None. Generated binaries need only libc + libm.
* Regexp: Built-in engine, no external library needed.
* Bigint: Built-in (from mruby-bigint), linked only when used.

## History

Spinel was originally implemented in C (18K lines, branchc-version),
then rewritten in Ruby (branchruby-v1), and finally rewritten in a
self-hosting Ruby subset (currentmaster).

## License

MIT License. SeeLICENSE.

## About

 No description, website, or topics provided.
 

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

858

 stars
 

### Watchers

8

 watching
 

### Forks

11

 forks
 

 Report repository

 

## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Ruby70.5%
* C28.4%
* Other1.1%