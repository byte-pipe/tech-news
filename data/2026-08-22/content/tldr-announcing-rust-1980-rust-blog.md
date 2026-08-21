---
title: Announcing Rust 1.98.0 | Rust Blog
url: https://blog.rust-lang.org/2026/08/20/Rust-1.98.0/
site_name: tldr
content_file: tldr-announcing-rust-1980-rust-blog
fetched_at: '2026-08-22T06:00:30.393108'
original_url: https://blog.rust-lang.org/2026/08/20/Rust-1.98.0/
date: '2026-08-22'
description: Empowering everyone to build reliable and efficient software.
tags:
- tldr
---

Aug. 20, 2026 · The Rust Release Team
 
 

The Rust team is happy to announce a new version of Rust, 1.98.0. Rust is a programming language empowering everyone to build reliable and efficient software.

If you have a previous version of Rust installed viarustup, you can get 1.98.0 with:

$
 rustup update stable

If you don't have it already, you can getrustupfrom the appropriate page on our website, and check out thedetailed release notes for 1.98.0.

If you'd like to help us out by testing future releases, you might consider updating locally to use the beta channel (rustup default beta) or the nightly channel (rustup default nightly). Pleasereportany bugs you might come across!

## What's in 1.98.0 stable

### Algebraic floating-point methods

The floating-point typesf32andf64now have "algebraic" methods for addition, subtraction, multiplication, division, and remainder. These allow optimizations on these operations using the algebraic properties of real numbers, even though these properties do not hold with the limitations of floating-point representations. The exact set of optimizations is not specified, but may be similar to the kind of optimization you would see with the-ffast-mathoption in other languages.

For example, floating-point addition isnot associative, so a sum likea + b + c + dmust be evaluated in the left-associative order in which it is parsed, like((a + b) + c) + d. If you write the same sum as a chain ofalgebraic_addcalls, then the compiler is free to reorder it, perhaps like(a + b) + (c + d)to evaluate the partial sums simultaneously. Broader loop-vectorization is often enabled by using these algebraic methods as well.

These methods are non-deterministic, since the compiler is free to choose different optimizations, but they never cause undefined behavior. See thelibrary documentationand the originalAPI change proposalfor more details.

### Buffered integer formatting

All of the primitive integer types now have aformat_intomethod that takes a&mut NumBuffer<Self>parameter, which is a buffer that is large enough to hold the decimal format of any value of that type. The buffer itself is opaque, but the method returns the formatted&strwith a lifetime borrowed from that buffer.

This method also bypasses much of the dynamic dispatch that you would get with bufferedwrite!formatting, which can be a boon to performance. Theitoa-benchmarkrepo now shows thatformat_intoperforms similarly toitoaitself, so this could serve as a standard replacement for that dependency and others like it.

### Fix interaction betweenManuallyDropandBox

Prior to Rust 1.96.0, there was a bug in the Rust compiler, which made the following code undefined behavior:

let
 mut
 x
 =
 ManuallyDrop
::
new
(
Box
::
new
(
1
)
)
;

unsafe
 {
 ManuallyDrop
::
drop
(
&
mut
 x
)
 }
;

let
 x
 =
 x
;
 //
 UB!

This is because the compiler considers it undefined behavior to move aBoxthat has been dropped (deallocated), andManuallyDropused to propagate that, such that movingManuallyDrop<Box<_>>where the box has been dropped would also be considered UB.

In Rust 1.96.0 we fixed this, so this code was no longer UB. In this release we have updated theManuallyDropdocumentation, providing a stable guarantee that this code will continue to not be UB in the future. SeeManuallyDropdocsand the relatedRFC 3336for more information.

### Stabilized APIs

* str::substr_range
* [T]::subslice_range
* core::fmt::NumBuffer
* <{integer}>::format_into
* Send/Sync for std::process::CommandArgs
* {fN}::algebraic_add
* {fN}::algebraic_sub
* {fN}::algebraic_mul
* {fN}::algebraic_div
* {fN}::algebraic_rem
* NonZero<{integer}>::from_str_radix
* String::from_utf16le
* String::from_utf16le_lossy
* String::from_utf16be
* String::from_utf16be_lossy
* [T]::strip_circumfix
* str::strip_circumfix
* Atomic<T>::from_mut
* Atomic<T>::get_mut_slice
* Atomic<T>::from_mut_slice
* std::range::legacy

### Other changes

Check out everything that changed inRust,Cargo, andClippy.

## Contributors to 1.98.0

Many people came together to create Rust 1.98.0. We couldn't have done it without all of you.Thanks!