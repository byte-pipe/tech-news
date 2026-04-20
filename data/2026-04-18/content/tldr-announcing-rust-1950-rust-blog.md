---
title: Announcing Rust 1.95.0 | Rust Blog
url: https://blog.rust-lang.org/2026/04/16/Rust-1.95.0/
site_name: tldr
content_file: tldr-announcing-rust-1950-rust-blog
fetched_at: '2026-04-18T11:33:58.586556'
original_url: https://blog.rust-lang.org/2026/04/16/Rust-1.95.0/
date: '2026-04-18'
description: Empowering everyone to build reliable and efficient software.
tags:
- tldr
---

Apr. 16, 2026 · The Rust Release Team



The Rust team is happy to announce a new version of Rust, 1.95.0. Rust is a programming language empowering everyone to build reliable and efficient software.

If you have a previous version of Rust installed viarustup, you can get 1.95.0 with:

$ rustup update stable

If you don't have it already, you cangetrustupfrom the appropriate page on our website, and check out thedetailed release notes for 1.95.0.

If you'd like to help us out by testing future releases, you might consider updating locally to use the beta channel (rustup default beta) or the nightly channel (rustup default nightly). Pleasereportany bugs you might come across!

## What's in 1.95.0 stable

### cfg_select!

Rust 1.95 introduces acfg_select!macro that acts roughly similar to a compile-timematchoncfgs. This
fulfills the same purpose as the popularcfg-ifcrate, although with a different
syntax.cfg_select!expands to the right-hand side of the first arm whose
configuration predicate evaluates totrue. Some examples:

cfg_select!

{

 unix
=>

{


fn

foo
(
)

{

/*
 unix specific functionality
*/

}


}

 target_pointer_width
=

"
32
"

=>

{


fn

foo
(
)

{

/*
 non-unix, 32-bit functionality
*/

}


}


_

=>

{


fn

foo
(
)

{

/*
 fallback implementation
*/

}


}

}

let
 is_windows_str
=

cfg_select!

{

 windows
=>

"
windows
"
,


_

=>

"
not windows
"
,

}
;

### if-let guards in matches

Rust 1.88 stabilizedlet chains. Rust
1.95 brings that capability into match expressions, allowing for conditionals
based on pattern matching.

match
 value
{


Some
(
x
)

if

let

Ok
(
y
)

=

compute
(
x
)

=>

{


//
 Both `x` and `y` are available here


println!
(
"
{}
,
{}
"
,
 x
,
 y
)
;


}


_

=>

{
}

}

Note that the compiler will not currently consider the patterns matched inif letguards as part of the exhaustiveness evaluation of the overall match, just
likeifguards.

### Stabilized APIs

* MaybeUninit<[T; N]>: From<[MaybeUninit<T>; N]>
* MaybeUninit<[T; N]>: AsRef<[MaybeUninit<T>; N]>
* MaybeUninit<[T; N]>: AsRef<[MaybeUninit<T>]>
* MaybeUninit<[T; N]>: AsMut<[MaybeUninit<T>; N]>
* MaybeUninit<[T; N]>: AsMut<[MaybeUninit<T>]>
* [MaybeUninit<T>; N]: From<MaybeUninit<[T; N]>>
* Cell<[T; N]>: AsRef<[Cell<T>; N]>
* Cell<[T; N]>: AsRef<[Cell<T>]>
* Cell<[T]>: AsRef<[Cell<T>]>
* bool: TryFrom<{integer}>
* AtomicPtr::update
* AtomicPtr::try_update
* AtomicBool::update
* AtomicBool::try_update
* AtomicIn::update
* AtomicIn::try_update
* AtomicUn::update
* AtomicUn::try_update
* cfg_select!
* mod core::range
* core::range::RangeInclusive
* core::range::RangeInclusiveIter
* core::hint::cold_path
* <*const T>::as_ref_unchecked
* <*mut T>::as_ref_unchecked
* <*mut T>::as_mut_unchecked
* Vec::push_mut
* Vec::insert_mut
* VecDeque::push_front_mut
* VecDeque::push_back_mut
* VecDeque::insert_mut
* LinkedList::push_front_mut
* LinkedList::push_back_mut
* Layout::dangling_ptr
* Layout::repeat
* Layout::repeat_packed
* Layout::extend_packed

These previously stable APIs are now stable in const contexts:

* fmt::from_fn
* ControlFlow::is_break
* ControlFlow::is_continue

### Destabilized JSON target specs

Rust 1.95 removes support on stable for passing a custom target specification
torustc. This shouldnotaffect any Rust users using a fully stable
toolchain, as building the standard library (including justcore) already
required using nightly-only features.

We're also gathering use cases for custom targets on thetracking issueas we consider whether some form of this feature should eventually be stabilized.

### Other changes

Check out everything that changed inRust,Cargo, andClippy.

## Contributors to 1.95.0

Many people came together to create Rust 1.95.0. We couldn't have done it without all of you.Thanks!
