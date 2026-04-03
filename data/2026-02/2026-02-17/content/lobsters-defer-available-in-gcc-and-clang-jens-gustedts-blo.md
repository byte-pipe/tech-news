---
title: Defer available in gcc and clang – Jens Gustedt's Blog
url: https://gustedt.wordpress.com/2026/02/15/defer-available-in-gcc-and-clang/
site_name: lobsters
content_file: lobsters-defer-available-in-gcc-and-clang-jens-gustedts-blo
fetched_at: '2026-02-17T06:00:38.551575'
original_url: https://gustedt.wordpress.com/2026/02/15/defer-available-in-gcc-and-clang/
date: '2026-02-17'
published_date: '2026-02-15T10:58:11+00:00'
description: 'About a year ago I posted about defer and that it would be available for everyone using gcc and/or clang soon. So it is probably time for an update. Two things have happened in the mean time: A technical specification (TS 25755) edited by JeanHeyd Meneide is now complete and moves through ISO''s complicated publication…'
tags: c
---

February 15, 2026

## Defer available in gcc and clang

About a year ago Iposted aboutdeferand that it would be available for everyone using gcc and/or clang soon. So it is probably time for an update.

Two things have happened in the mean time:

* Atechnical specification (TS 25755)edited by JeanHeyd Meneide is now complete and moves through ISO’s complicated publication procedures.
* Both gcc and clang communities have worked on integrating this feature into their C implementations.

I have not yet got my hands on the gcc implementation (but this is also less urgent, see below), but I have been able to use clang’s which is available starting with clang-22.

I think that with this in mind everybody developing in C could and should now seriously consider switching todeferfor their cleanup handling:

* no more resource leakage or blocked mutexes on rarely used code paths,
* no more spaghetti code just to cover all possibilities for preliminary exits from functions.

I am not sure if the compiler people are also planning back ports of these features, but with some simple work around and slightly reduced grammar for thedeferfeature this works for me from gcc-9 onward and for clang-22 onward:

#if __has_include(<stddefer.h>)
# include <stddefer.h>
# if defined(__clang__)
# if __is_identifier(_Defer)
# error "clang may need the option -fdefer-ts for the _Defer feature"
# endif
# endif
#elif __GNUC__ > 8
# define defer _Defer
# define _Defer _Defer_A(__COUNTER__)
# define _Defer_A(N) _Defer_B(N)
# define _Defer_B(N) _Defer_C(_Defer_func_ ## N, _Defer_var_ ## N)
# define _Defer_C(F, V) \
 auto void F(int*); \
 __attribute__((__cleanup__(F), __deprecated__, __unused__)) \
 int V; \
 __attribute__((__always_inline__, __deprecated__, __unused__)) \
 inline auto void F(__attribute__((__unused__)) int*V)
#else
# error "The _Defer feature seems not available"
#endif

So this is already a large panel of compilers. Obviously it depends on your admissible compile platforms whether or not these are sufficient for you. In any case, with these you may compile for a very wide set of installs sincedeferdoes not need any specific software infrastructure or library once the code is compiled.

As already discussed many times, the gcc fallback uses the so-called “nested function” feature which is always subject of intense debate and even flame wars. Don’t worry, the implementation as presented here, even when compiled with no optimization at all, does not produce any hidden function in the executable, and in particular there is no “trampoline” or whatever that would put your execution at risk of a stack exploit.

You may also notice that there is no fallback for older clang version. This is because their so-called “blocks” extension cannot easily be used as a drop-in to replace nested function: their semantics to access variables from the surrounding scope are different and not compatible with thedeferfeature as defined by TS 25755.

So for example if you are scared of using big VLA on the stack, you may use the above code in headers and something like

double* BigArray
 = malloc(sizeof(double[aLot]));
if (!BigArray {
 exit(EXIT_FALURE);
}
defer {
 free(BigArray);
}

to have an implementation of a big array with a failure mode for the allocation.

Or if you want to be sure that all your mutexes are unlocked when you leave a critical section, use and idiom as here

{
 if (mtx_lock(&mtx) != thrd_success) {
 exit(EXIT_FAILURE);
 }
 defer {
 mtx_unlock(&mtx);
 }

 ... do something complicated ...

 if (rareCondition) {
 return 42;
 }

 ... do something even more complicated ...
}

Just notice, that you’d always have to use thedeferfeature with curly braces to ensure that the gcc fallback works smoothly.

### Share this:

* Share
* Email a link to a friend (Opens in new window)Email
* Print (Opens in new window)Print
* Share on Facebook (Opens in new window)Facebook
* Share on X (Opens in new window)X

###### Fediverse Reactions



			4 reposts

			5 likes

			1 quote

C11
,
C17
,
C23
,
C2x
,
C2y
,
Modern C

Posted by:

Jens Gustedt
