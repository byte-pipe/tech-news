---
title: Announcing Rust 1.99.0 | Rust Blog
url: https://blog.rust-lang.org/2026/10/01/Rust-1.99.0
site_name: tldr
content_file: tldr-announcing-rust-1990-rust-blog
fetched_at: '2026-10-02T16:31:18.461761'
original_url: https://blog.rust-lang.org/2026/10/01/Rust-1.99.0
date: '2026-10-02'
description: Empowering everyone to build reliable and efficient software.
tags:
- tldr
---

Oct. 1, 2026 · The Rust Release Team
 
 

The Rust team is happy to announce a new version of Rust, 1.99.0. Rust is a programming language empowering everyone to build reliable and efficient software.

If you have a previous version of Rust installed viarustup, you can get 1.99.0 with:

$
 rustup update stable

If you don't have it already, you can getrustupfrom the appropriate page on our website, and check out thedetailed release notes for 1.99.0.

If you'd like to help us out by testing future releases, you might consider updating locally to use the beta channel (rustup default beta) or the nightly channel (rustup default nightly). Pleasereportany bugs you might come across!

## What's in 1.99.0 stable

### extern "C" variadics

Rust 1.99.0 stabilizes defining C-ABI variadic functions with "C" and
"C-unwind" ABIs. Variadic functions defined this way use a variable argument
list (...) and accept an arbitrary number of arguments. Rust could already
call externally-defined variadic functions (e.g.,libc::printf). With Rust
1.99, these functions can now be written in Rust itself:

///
 SAFETY: must be called with (at least) 2 i32 arguments.

unsafe
 extern
 "
C
"
 fn
 sum
(
mut
 args
:
 ...
)
 ->
 i32
 {

 //
 SAFETY: guaranteed by the caller.

 let
 a
 =
 unsafe
 {
 args
.
next_arg
::
<
i32
>
(
)
 }
;

 let
 b
 =
 unsafe
 {
 args
.
next_arg
::
<
i32
>
(
)
 }
;

 a
 +
 b

}

fn
 foo
(
)
 ->
 i32
 {

 unsafe
 {
 sum
(
0
i32
,
 2
i32
)
 }

}

The type of...isVaList,
which is ABI-compatible with the Cva_listtype across targets. What types can be read from aVaListis guarded by theVaArgSafetrait.

For more details on c-variadic functions, see theReference.
This release also stabilizes support for defining naked variadic functions with
non-"C" ABIs, which must be written via inline assembly.

### Layout information from raw pointers

This release settles the safety requirements for retrieving the size and
alignment on raw pointers to bothSized(trivially safe, already possible on
stable) and non-Sizedtypes.

This is done by stabilizing three functions:

* Layout::for_value_raw
* mem::size_of_val_raw
* mem::align_of_val_raw

### Recommend against round-trip unleaking afterBox::leak

While there are no changes to the language semantics in Rust 1.99, we have
updated the documentation onBox::leakto recommend against patterns that
later deallocate that memory. This was done because such code was found to have
problematic interactions with current and future potential compiler optimizations,
and is especially problematic with the upcoming stabilization of custom allocators.
Instead,Box::into_non_nullorBox::into_rawshould be preferred.

This guidance also applies to otherleakfunctions in the standard library.

### Stabilized APIs

* IntoIteratorforBox<[T; N]>
* IntoIteratorfor&Box<[T; N]>
* IntoIteratorfor&mut Box<[T; N]>
* VecDeque::retain_back
* core::ffi::VaList
* Box::into_non_null
* Box::from_non_null
* Vec::into_parts
* Vec::from_parts
* core::mem::size_of_val_raw
* core::mem::align_of_val_raw
* core::alloc::Layout::for_value_raw
* String::from_utf8_lossy_owned
* string::FromUtf8Error::into_utf8_lossy
* FusedIterator for StepBy<I>
* std::fs::set_times
* std::fs::set_times_nofollow

### Other changes

Check out everything that changed inRust,Cargo, andClippy.

## Contributors to 1.99.0

Many people came together to create Rust 1.99.0. We couldn't have done it without all of you.Thanks!