---
title: Lean proved this program was correct; then I found a bug.
url: https://kirancodes.me/posts/log-who-watches-the-watchers.html
site_name: hnrss
content_file: hnrss-lean-proved-this-program-was-correct-then-i-found
fetched_at: '2026-04-14T11:57:26.761007'
original_url: https://kirancodes.me/posts/log-who-watches-the-watchers.html
author: Kiran Gopinathan
date: '2026-04-14'
description: Lean proved this program correct; then I found a bug
tags:
- hackernews
- hnrss
---

## Lean proved this program was correct; then I found a bug.13 Apr, 2026leanformal_verificationsecurityfuzzing

I fuzzed a verified implementation of zlib and found a buffer overflow in the Lean runtime.

AI agents are gettingvery goodat finding vulnerabilities in
large-scale software systems.

Anthropic, was apparently so spooked by the vulnerability-discovery
capabilities of Mythos, they decided not to release it as it was "too
dangerous" (lol). Whether you believe the hype about these latest
models or not, it seems undeniable that the writing is on the wall:

The cost of
discovering security bugs is collapsing, and the vast majority of
software running today was never built to withstand that kind of
scrutiny.We are facing a looming software crisis.

In the face of this oncoming tsunami, recently there has been
increasing interest informal verificationas a solution. If we state
and prove properties about our code using a mechanical tool, can we
build robust, secure and stable software that can overcome this
oncoming barrage of attacks?

One recent development in the Lean ecosystem has taken steps towards
this question. 10 agents autonomously built and proved an
implementation of zlib,lean-zip, an impressive landmark result.
Quoting fromLeo De Moura, the chief architect of the Lean FRO
(here):

With apologies for the AI-slop (Leo has a penchant for it, it seems),
the key result is thatlean-zipis not just another implementation of
zlib. It is an implementation that has been verified as correct end to
end, guaranteed by Lean to be entirely free of implementation bugs.

What does "verified as correct" actually look like? Here is one of the
main theorems (github):

theorem

zlib_decompressSingle_compress

(
data : ByteArray
)

(
level : UInt8
)


(
hsize : data.size
<

1024

*

1024

*

1024
)
 :
 ZlibDecode.decompressSingle

(
ZlibEncode.compress data level
)

=
 .ok data

Foranybyte array less than 1 gigabyte, callingZlibDecode.decompressSingleon the output ofZlibEncode.compressproduces the original data. The decompress function is exactly the
inverse of compression. This pair of functions isentirelycorrect.

Or is it?

I pointed a Claude agent atlean-zipover a weekend, armed with AFL++,
AddressSanitizer, Valgrind, and UBSan. Over105 million fuzzing
executions, it found:

* Zero memory vulnerabilitiesin the verified Lean application code.
* A heap buffer overflowin the Lean 4 runtime (lean_alloc_sarray), affecting every version of Lean to date. (bug report,pending fix)
* A denial-of-serviceinlean-zip's archive parser, which was never verified.

### The setup

The setup for the experiment was quite simple. I took thelean-zip
codebaseand produced astripped down versionand pointed Claude at
it.

In particular, as part of the setup: (1) I dropped all theorems and
 specifications, (2) removed all markdown documentation, and (3)
 stripped outlean-zip's C FFI bindings to zlib which it provided as
 an alternative to its native implementation. What remained was
 purely the verified code: the native Lean definitions for DEFLATE,
 gzip, ZIP archive handling, and tar. Any bug found in this would
 correspond to an error in the verified code.

The idea with dropping theorems and documentation was to avoid biasing
the Claude agent by revealing that the code was actually verified – I
figured if it knew the code "had no bugs" then it might pre-emptively
give up, while operating in the blind might let it work through the
software without bias.

With the lean implementation accessible through a CLI, I then spun up
a server for the fuzzing experiments, pointed Claude at it, and let it
go wild.

### Results

Over thecourse of a night, Claude launched 16 parallel fuzzers across
the 6 attack surfaces of the library: ZIP extract, gzip decompress,
raw DEFLATE inflate, tar extract, tar.gz, and compression. It built
separate binaries with AddressSanitizer and
UndefinedBehaviorSanitizer, ran Valgrind memcheck, used cppcheck and
flawfinder for static analysis, crafted 48 hand-written exploit files
targeting known zlib CVE patterns.

Overall, this resulted in105,823,818 fuzzing executions. 359 seed
files. 16 fuzzers running for approximately 19 hoursuncovering 4
crashing inputs, and 1 memory vulnerability in the code.

#### Bug 1: Heap buffer overflow in the Lean runtime

The most substantial finding wasa heap buffer overflow!but, not inlean-zip's code, but in the Lean runtime itself.

The vulnerable function islean_alloc_sarray, which allocates all
scalar arrays (ByteArray,FloatArray, etc.) in Lean 4:

lean_obj_res

lean_alloc_sarray
(


unsigned

elem_size
,
size_t

size
,
size_t

capacity

)

{


lean_sarray_object
 *
o
 =

(
lean_sarray_object
*
)
lean_alloc_object
(


sizeof
(
lean_sarray_object
)
 + elem_size * capacity

)
;

//
...

}

For aByteArrayof capacityn, the allocation size is24 + n.
Whennis close toSIZE_MAX(2^{64} - 1on 64-bit systems), the
addition wraps around to a small number. The runtime allocates a tiny
buffer of around 23 bytes, but the caller proceeds to readnbytes
into it.

The overflow can be triggered throughlean_io_prim_handle_read, the C
function backingIO.FS.Handle.read:

obj_res

lean_io_prim_handle_read
(


b_obj_arg

h
,
usize

nbytes

)

{


FILE
 *
fp
 = io_get_handle
(
h
)
;

obj_res

res
 =
 lean_alloc_sarray
(
1, 0, nbytes
)
;
//
overflows here


//
...


usize

n
 = std::fread
(

 lean_sarray_cptr
(
res
)
, 1, nbytes, fp

)
;

//
^^^ 23-byte buffer ^^^ SIZE_MAX count

A 156-byte crafted ZIP file with a ZIP64compressedSizeof0xFFFFFFFFFFFFFFFFis sufficient to trigger it. The same pattern
exists inlean_io_get_random_bytes. The bug affects every version of
Lean 4 up to and including the latest nightly
(v4.31.0-nightly-2026-04-11). The minimal reproducer is 5 simple lines:

def

main
 : IO Unit
:=

do

 IO.FS.writeFile
"test.bin"

"hello"


let
 h ← IO.FS.Handle.mk
"test.bin"
 .read

let
 n : USize
:=

(
0
 : USize
)

-

(
1
 : USize
)

--
SIZE_MAX


let

_
 ← h.read n
--
overflows in lean_alloc_sarray

Edit: there is apending PRto lean to fix this.

#### Bug 2: Denial-of-service in the archive parser

AFL also found a denial-of-service in lean-zip's own code. ThereadExactfunction inArchive.leanpasses thecompressedSizefield from the ZIP central directory straight toh.readwithout
validating it against the actual file size:

def

readExact

(
h : IO.FS.Handle
)

(
n : Nat
)
 ...
:=

do


--
...

 while buf.size
<
 n
do


let
 remaining
:=
 n
-
 buf.size

let
 chunk ← h.read remaining.toUSize

--
n comes from the ZIP header


--
...

A 156-byte ZIP claiming acompressedSizeof several exabytes causes
the process to panic withINTERNAL PANIC: out of memory, ash.readallocates more memory than available. This is indeed a bug: the systemunziphandles this gracefully, validating header sizes against the
file before allocating, whilelean-zipdoes not and crashes with an
OOM.

### Why verification didn't catch these bugs

The OOM denial-of-service is straightforward: the archive parser was
never verified.lean-zip's proofs cover the compression and
decompression pipeline (DEFLATE, Huffman, CRC32, roundtrip
correctness), butArchive.lean, the module that reads ZIP headers and
extracts files, has zero theorems even in the original unstripped
codebase. ThecompressedSizefield is read from an untrusted header
and passed directly to an allocation without validation. The situation
is reminiscent ofYang et al.'s CSmith work(PLDI 2011), which found
that CompCert'sverifiedoptimisation passes had zero bugs while itsunverifiedfront-end did. Verification works where it is applied. The
archive parser was wherelean-zipwas not verified.

The heap buffer overflow is more fundamental.lean_alloc_sarrayis a
C++ function in the Lean runtime, part of thetrusted computing
base. Every Lean proof assumes the runtime is correct. A bug here
does not just affect lean-zip. It affects every Lean 4 program that
allocates aByteArray.

### Conclusion

The positive result here is actually the remarkable one. Across 105
million executions, theapplication code(that is, excluding the
runtime) had zero heap buffer overflows, zero use-after-free, zero
stack buffer overflows, zero undefined behaviour (UBSan clean), and
zero out-of-bounds array reads in the Lean-generated C code. To quote
Claude's own assessment of the codebase (without knowing it was
verified):

This isgenuinelyone of the most memory-safe codebases I've
analyzed. The Lean type system with dependent types and well-founded
recursion has eliminated entire classes of bugs that plague C/C++ zip
implementations. The CVE classes that have plagued zlib for decades
are structurally impossible in this codebase.

The two bugs that were found both sat outside the boundary of what the
proofs cover. The denial-of-service was a missing specification. The
heap overflow was a deeper issue in the trusted computing base, the
C++ runtime that the entire proof edifice assumes is correct (andnow
has a PR addressing).

Overall verification resulted in a remarkably robust and rigorous
codebase. AFL and Claude had a really hard time finding errors. But
they did still find issues. Verification is only as strong as the
questions you think to ask and the foundations you choose to trust.

Quis custodiet ipsos custodes?

### Links

* lean-zip on GitHub
* Lean 4 bug report
