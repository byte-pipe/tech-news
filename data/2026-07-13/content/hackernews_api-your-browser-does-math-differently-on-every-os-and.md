---
title: Your Browser Does Math Differently on Every OS, and Anti-Bot Systems Read the Bits · scrapfly.dev
url: https://scrapfly.dev/posts/browser-math-os-fingerprint/
site_name: hackernews_api
content_file: hackernews_api-your-browser-does-math-differently-on-every-os-and
fetched_at: '2026-07-13T12:26:58.229586'
original_url: https://scrapfly.dev/posts/browser-math-os-fingerprint/
author: Scrapfly Engineering
date: '2026-07-13'
published_date: '2026-07-12T00:00:00Z'
description: Math.tanh, every CSS trig function, and the Web Audio compressor all route through the host libm, so the rounding of a cosine betrays the OS a browser actually …
tags:
- hackernews
- trending
---

← Back to all posts
Summarize this article with
Add as a preferred source
Share

Fingerprinting is usually about canvas, WebGL, fonts, audio. There is a quieter signal, and it lives in the last bits of a number.

Run this in any console:

Math
.
tanh
(
0.8
)

// 0.6640367702678491 genuine Linux Chrome (glibc)

// 0.664036770267849 genuine macOS Chrome (libsystem_m)

// 0.6640367702678489 genuine Windows Chrome (UCRT)

That output is an approximation, and its exact bits depend on the OS that computed it. A genuine Mac runsMath.tanhthrough Apple’s math library. Linux runs it through glibc1. The two disagree on about a quarter of all inputs, usually by one unit in the last place (1 ULP2). Windows, through the Universal C Runtime, disagrees with both on a few percent, and on the input above all three land on a different bit.

The same call, run on genuine Chrome 150 across three real machines:

Call
Linux (glibc)
macOS (
libsystem_m
)
Windows (UCRT)
Split
Math.tanh(0.5)
0.46211715726000974
0.46211715726000974
0.46211715726000974
all three agree
Math.tanh(0.7)
0.6043677771171636
0.6043677771171635
0.6043677771171635
Linux alone, 1 ULP
Math.tanh(0.8)
0.6640367702678491
0.664036770267849
0.6640367702678489
all three differ, 2 ULP spread
Math.tanh(0.9)
0.7162978701990245
0.7162978701990245
0.7162978701990244
Windows alone, 1 ULP

Measured over the DevTools protocol on Chrome 150: Linux (glibc), macOS 26 on Apple Silicon (libsystem_m), Windows 11 (ucrtbase.dll).tanh(0.5)is one of the roughly three-in-four inputs where everyone agrees, which is exactly why it makes a useless probe.tanh(0.8)is one that separates all three at once.

Onetanhcall on the right input is a per-OS signature. Claim macOS, return Linux math bits, and you have contradicted your own User-Agent.

This tell is recent. Until Chrome 148, V8 computedtanhitself with a bundled fdlibm3port, so it returned the same bits on every OS and leaked nothing. V8 commitc1486295ae5replaced it withstd::tanh, which reads the hostlibm. It first shipped in V8 14.8.57, which is Chrome 148. Chrome 147 and earlier do not leak here. Chrome 148, 149, and 150 do.

Scrapfly ships a browser that has to match a real one across hundreds of signals, and math is one of the harder ones.

## Why one function returns different bits

IEEE 7544defines how adoubleis stored. It does not requiresin,cos,tanh, orexpto be correctly rounded. Correct rounding is expensive, so every vendor ships alibm5that trades a fraction of a ULP for speed, with its own minimax6coefficients, lookup tables, and reduction constants.

The three implementations produce three sets of bits:

* Linux: glibc
* macOS: Applelibsystem_m
* Windows: UCRT7(ucrtbase.dll)

They agree almost everywhere and split just often enough to classify the OS. A detector needs no math, only a table: genuine macOS Chrome returns one pattern forcos(1), genuine Linux Chrome returns another, and a single comparison tells them apart.

## Four traps

“Just reimplement the Mac functions” breaks on contact, for four reasons.

1. Only some math leaks.V88ships its own math and links it statically:Math.exp,Math.pow,Math.atan, and most of the rest come from bundled llvm-libc9, andMath.sin/Math.cosfrom a bundled glibc-deriveddbl-64routine. All of them are identical on every OS, so spoofing them creates an inconsistency. The exception isMath.tanh: since Chrome 148 V8 computes it with the platformstd::tanhinstead of the bundled routine it used before, so it now reads the hostlibm. It is the onlyMath.*that leaks the OS, and that asymmetry is itself checkable.

2. JavaScript math and CSS math are different code paths.CSSsin(),cos(), andatan2()do not share code withMath.sin. The layout engine reduces the angle in degrees, then calls platformstd::sinon the reduced value. That gives a different result than a direct radiansin(), and it hits the hostlibm, so all seven CSS trig functions leak. We reproduced the degree reduction and the radians-to-degrees step bit-for-bit, not just the leaf function.

3. macOS has two math libraries that disagree.Apple Silicon carries scalarlibsystem_mand the Accelerate framework10’s vector routines (vvsin,vvtanh). They are different code. Across a million inputs they diverge on 10 to 89 percent, depending on the function. Takecos(0): scalar returns exactly1.0, Accelerate returns0.9999999999999999. So “reproduce Apple’s math” is undefined until you know which library the browser calls, at which site. We resolved it by driving real Chrome on a real Mac over the debugging protocol and reading the exact double. Answer: scalarlibsystem_mbacksMath.tanh, CSS trig, and the audio compressor’s per-sample transcendentals. Accelerate backs Chrome’s Web Audio DSP on Mac, the FFT, the vector math, and the biquad filters (fft_frame_mac.cc,vector_math_mac.h,biquad.cc, allBUILDFLAG(IS_MAC)). Pick the wrong library for a given call site and you land 1 ULP off on most inputs, worse than not spoofing.

4. Architecture leaks.ARM and x86 differ on fused-multiply-add and on NaN sign propagation. A reproduction that is correct on paper drifts if the compiler fuses a multiply-add on one target and not the other.

## The map: what leaks where

Put the routing on one page.Boldis the hostlibm(glibc, Applelibsystem_m, or UCRT), the code that leaks the OS. Everything else is identical on every machine and safe to leave alone.

Operation
V8 
Math.*
 (JS)
CSS 
calc()
Web Audio
sin
 
cos
 
tan
V8 bundled
host libm
Accelerate
 (osc FFT), 
sin
 scalar in the compressor
asin
 
acos
 
atan
 
atan2
V8 bundled
host libm
not used
tanh
host libm
none
not used
exp
V8 bundled
host libm
scalar in the compressor
log
 
log2
 
log10
 
pow
V8 bundled
host libm
scalar 
log10f
 / 
powf
 in the compressor
vector add/mul/scale, FFT
n/a
n/a
Accelerate
 (
vDSP
) on Mac
sqrt
 
abs
 
+
 
-
 
*
 
/
hardware
hardware
hardware

V8 bundled= statically linked and identical on every OS: llvm-libc for most functions, a glibc-deriveddbl-64routine forsin/cos.host libm= the platform library that leaks the OS (libsystem_mon Mac, glibc on Linux, UCRT on Windows).Accelerate= Apple’svDSP, which Chrome uses for the Mac Web Audio DSP.

V8 routes almost everything through its own bundled math, so JavaScriptMathis a tell in exactly one place,Math.tanh. CSS is a tell everywhere, because Blink calls the hostlibmdirectly for every trig function. Web Audio on Mac runs on Accelerate for the FFT and the vector stages, while the DynamicsCompressor’s per-sample transcendentals stay scalarlibsystem_m, so one audio graph touches three separate libraries.

WASM is not in the table because it has no transcendental opcodes.sinand friends come from whateverlibmthe module bundled, and its arithmetic (f64.sqrt,f64.mul) is hardware, so WASM math is identical on every OS. Its only fingerprint axis is the ARM-versus-x86 split in NaN canonicalization and a few SIMD roundings.

The tells cluster in three surfaces:Math.tanh, every CSS trig function, and Web Audio, where the Accelerate FFT carries the CPU architecture and the compressor’s scalarlibsystem_mcarries the OS.

## How to close it

No noise.Perturbing the output fails twice. A reference comparison sees a value that matches no real OS, and per-call randomness breaks determinism, which is its own tell. The target is a value identical to the OS you claim, which noise cannot produce.

Reproduce the algorithm exactly.Recover the target’s minimax coefficients, exponent tables, and reduction constants from itslibm, and transcribe them to portable C. Match every bit, including the inputs where the target rounds the wrong way. Here is Apple’ssinpolynomial, coefficients pulled straight out oflibsystem_m:

// Every fused multiply-add Apple emits is written as an explicit fma(). The

// bit pattern of each coefficient is copied verbatim; a decimal transcription

// would round differently.

static
 
const
 
double
 
P
[
6
]
 
=
 
{

 
0x1
.5
d8fd1fd19ccdp
-
33
,
 
-
0x1
.
ae5e5a9291f5dp
-
26
,
 
0x1
.71
de3567d48a1p
-
19
,

 
-
0x1
.
a01a019bfdf03p
-
13
,
 
0x1
.111111110f
7
d0p
-
7
,
 
-
0x1
.5555555555548
p
-
3
,

};

static
 
double
 
sin_poly
(
double
 
x2
)
 
{

 
double
 
p
 
=
 
fma
(
x2
,
 
P
[
0
],
 
P
[
1
]);

 
p
 
=
 
fma
(
x2
,
 
p
,
 
P
[
2
]);

 
p
 
=
 
fma
(
x2
,
 
p
,
 
P
[
3
]);

 
p
 
=
 
fma
(
x2
,
 
p
,
 
P
[
4
]);

 
p
 
=
 
fma
(
x2
,
 
p
,
 
P
[
5
]);

 
return
 
x2
 
*
 
p
;
 
// caller finishes: sin(x) = fma(x, x2*p, x)

}

Make it deterministic.That explicitfma()matters. Compile with FMA contraction off (-ffp-contract=off) so the compiler never invents or drops a fusion of its own. Now the fused ops are exactly the ones Apple fuses, and the result is identical on FMA11and non-FMA CPUs, and identical between the ARM machine you imitate and the x86 fleet you run on. Hardware FMA and correctly-rounded software FMA return the same bits.

When reproduction is not worth it, lift the original.Windows UCRT is x86-64, the same ISA as a Linux server, and position-independent. Map the genuineucrtbase.dllinto memory at runtime and call its exports directly. The bits are genuine because the code is genuine, no reverse-engineering required.

Calling into Windows code from a Linux binary hits the ABI boundary. UCRT is compiled for the Windows x64 convention: the callee owns 32 bytes of shadow space above the return address, and the callee-saved register set differs from System V. Declare the function pointersms_abior clang’s frame layout gets corrupted by the callee’s shadow-space writes, and the indirect call jumps into garbage.

// Windows x64 ABI, not System V. Without ms_abi the call crashes.

typedef
 
double
(
__attribute__
((
ms_abi
))
 
*
 
D1
)(
double
);
 
// tanh, sin, ...

typedef
 
double
(
__attribute__
((
ms_abi
))
 
*
 
D2
)(
double
,
 
double
);
 
// atan2

// The mapped DLL code is not a CFI-registered indirect-call target, so

// -fsanitize=cfi-icall (on in production) #UD-traps every call -> SIGILL at

// startup. Opt the wrappers that call through the pointers out of that check.

[[
clang
::
no_sanitize
(
"cfi-icall"
)]]

double
 
ucrt_tanh
(
double
 
x
)
 
{

 
return
 
ucrt
.
loaded
 
?
 
ucrt
.
tanh
(
x
)
 
:
 
std
::
tanh
(
x
);

}

One more detail decides correctness. Every UCRT math function starts withmov eax, [rip+disp32], reading a CPU-dispatch flag that selects the scalar or the FMA/AVX2 code path. A fresh mapping leaves it at zero, so you get the slow path, whose bits differ from what a modern Windows box produces. Extract the flag’s address from thetanhprologue and force it to the FMA path before the first call, and the lifted library matches a real Windows machine bit-for-bit.

Patch the chokepoint, gate it.Hook the single function that owns the value, where the engine callslibm. Gate on the claimed OS: Linux keeps glibc, Mac gets the reproduction.

Watch the clock.A perfect reproduction that runs slow is still a tell. Our first build lowered everyfma()to a software call, because the default x86 baseline predates hardware FMA. That ran 2.5 to 6 times slower than native. A loop timingMath.tanhagainstMath.sinwould show a ratio no real browser has. Turning on hardware FMA cut each fused op to one instruction: about 6 times faster, faster than glibc, and bit-identical.

## Validation

None of this ships without proof. Our harness runs 871,000 inputs per release across every branch and domain: dense grids, interval boundaries, subnormals, signed zeros, infinities, NaNs. Two ground truths back it:

1. A genuine-device oracle: a real Mac computing both scalar and Accelerate results for every input, so we know exactly where the two disagree.
2. A genuine-browser anchor: real Chrome on a real Mac over the debugging protocol, computingMath.tanhand every CSS trig function at full precision. This is the surface a fingerprinter reads.

We ship at bit-for-bit parity with genuine Mac Chrome onMath.tanhand on CSSsin,cos,tan,asin,acos,atan, andatan2, with the reproduction verified identical to the machine code in the shipped binary. Domain edges get checked too:asin(2)on a real Mac resolves to0(out of domain is NaN, and CSS clamps NaN to zero), not the 90 degrees a naive reproduction returns.

## Why it matters

Math is deterministic, cheap to probe, hard to fake, and almost never on a spoofing stack’s radar. That makes it a strong signal for a defender and a liability for a scraper. Getting it right takes reverse-engineering vendorlibminternals, mapping how three engines route math per call site, matching algorithms to the last bit, holding determinism across architectures, and proving it against real hardware.

Scrapfly’s browser carries all of it. Send a request through our API and ask to present as macOS, and the identity holds down to the rounding of a cosine.

Scrapiumis Scrapfly’s scraping browser, built to stay indistinguishable from real traffic. Our engineering blog goes deep on the rest of the stack.

1. glibc: the GNU C Library, the standard C library andlibmon most Linux systems. Reference:gnu.org/software/libc.↩︎
2. ULP (unit in the last place): the gap between two consecutive representable floating-point numbers at a given magnitude. “1 ULP off” is the smallest difference adoublecan express. Reference:Wikipedia.↩︎
3. fdlibm: Sun Microsystems’ “Freely Distributable libm”, the portable reference implementation of the C math functions. V8 carried a port of it and computedMath.tanhwith it until Chrome 148, returning identical bits on every OS. Reference:netlib fdlibm.↩︎
4. IEEE 754: the floating-point standard. It fixes how adoubleis stored but does not require transcendental functions to be correctly rounded, which is the room every vendor’slibmfills differently. Reference:Wikipedia.↩︎
5. libm: the C standard library’s math module (sin,cos,exp,tanh, and so on). Each OS ships its own build, which is why the same call returns different bits: glibc on Linux, Applelibsystem_mon macOS, UCRT on Windows. Reference:C mathematical functions.↩︎
6. minimax polynomial: the approximating polynomial that minimizes worst-case error. Eachlibmpicks its own coefficients, and that choice is where the differing bits originate. Reference:Wikipedia.↩︎
7. UCRT (Universal C Runtime): Microsoft’s C runtime (ucrtbase.dll) and its math functions. Being x86-64 and position-independent lets it be mapped into a Linux process and called directly. Reference:Microsoft Learn.↩︎
8. V8 / Blink: Chrome’s JavaScript engine (routesMath.*through llvm-libc) and Chromium’s rendering engine (owns CSScalc()trig, which calls the hostlibmdirectly). References:v8.dev,chromium.org/blink.↩︎
9. llvm-libc: LLVM’s C library. V8 statically links its math routines, soMath.sin,cos,exp, andpoware identical on every OS, which is why onlyMath.tanhleaks. Reference:libc.llvm.org.↩︎
10. Accelerate framework: Apple’s vector and DSP library (vvsin,vvtanh,vDSP). It backs only the Web Audio FFT, not the scalarMath.*calls, which is why the scalar and vector results disagree. Reference:Apple Developer.↩︎
11. FMA (fused multiply-add): a single instruction computinga*b+cwith one rounding instead of two. Compiling-ffp-contract=offstops the compiler adding or dropping fusions, which is what makes the reproduction bit-stable across CPUs. Reference:Wikipedia.↩︎
← All posts

scrapfly.io
 ·

RSS