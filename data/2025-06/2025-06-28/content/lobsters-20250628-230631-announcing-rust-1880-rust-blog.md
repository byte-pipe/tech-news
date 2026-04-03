---
title: Announcing Rust 1.88.0 | Rust Blog
url: https://blog.rust-lang.org/2025/06/26/Rust-1.88.0/
site_name: lobsters
fetched_at: '2025-06-28T23:06:31.893394'
original_url: https://blog.rust-lang.org/2025/06/26/Rust-1.88.0/
date: '2025-06-28'
description: Empowering everyone to build reliable and efficient software.
tags: rust
---

June 26, 2025 · The Rust Release Team



The Rust team is happy to announce a new version of Rust, 1.88.0. Rust is a programming language empowering everyone to build reliable and efficient software.

If you have a previous version of Rust installed viarustup, you can get 1.88.0 with:

$ rustup update stable

If you don't have it already, you cangetrustupfrom the appropriate page on our website, and check out thedetailed release notes for 1.88.0.

If you'd like to help us out by testing future releases, you might consider updating locally to use the beta channel (rustup default beta) or the nightly channel (rustup default nightly). Pleasereportany bugs you might come across!

## What's in 1.88.0 stable

### Let chains

This feature allows&&-chainingletstatements insideifandwhileconditions, even intermingling with boolean expressions, so there is less distinction betweenif/if letandwhile/while let. The patterns inside theletsub-expressions can be irrefutable or refutable, and bindings are usable in later parts of the chain as well as the body.

For example, this snippet combines multiple conditions which would have required nestingif letandifblocks before:

if

let

Channel
::
Stable
(
v
)

=

release_info
(
)


&&

let
 Semver
{
 major
,
 minor
,

..

}

=
 v


&&
 major
==

1


&&
 minor
==

88

{


println!
(
"
`let_chains` was stabilized in this version
"
)
;

}

Let chains are only available in the Rust 2024 edition, as this feature depends on theif lettemporary scopechange for more consistent drop order.

Earlier efforts tried to work with all editions, but some difficult edge cases threatened the integrity of the implementation. 2024 made it feasible, so please upgrade your crate's edition if you'd like to use this feature!

### Naked functions

Rust now supports writing naked functions with no compiler-generated epilogue and prologue, allowing full control over the generated assembly for a particular function. This is a more ergonomic alternative to defining functions in aglobal_asm!block. A naked function is marked with the#[unsafe(naked)]attribute, and its body consists of a singlenaked_asm!call.

For example:

#
[
unsafe
(
naked
)
]

pub

unsafe

extern

"
sysv64
"

fn

wrapping_add
(
a
:

u64
,
b
:

u64
)

->

u64

{


//
 Equivalent to `a.wrapping_add(b)`.


core
::
arch
::
naked_asm
!
(


"
lea rax, [rdi + rsi]
"
,


"
ret
"


)
;

}

The handwritten assembly block defines theentirefunction body: unlike non-naked functions, the compiler does not add any special handling for arguments or return values. Naked functions are used in low-level settings like Rust'scompiler-builtins, operating systems, and embedded applications.

Look for a more detailed post on this soon!

### Boolean configuration

Thecfgpredicate language now supports boolean literals,trueandfalse, acting as a configuration that is always enabled or disabled, respectively. This works in Rustconditional compilationwithcfgandcfg_attrattributes and the built-incfg!macro, and also in Cargo[target]tables in bothconfigurationandmanifests.

Previously, empty predicate lists could be used for unconditional configuration, likecfg(all())for enabled andcfg(any())for disabled, but this meaning is rather implicit and easy to get backwards.cfg(true)andcfg(false)offer a more direct way to say what you mean.

SeeRFC 3695for more background!

### Cargo automatic cache cleaning

Starting in 1.88.0, Cargo will automatically run garbage collection on the cache in its home directory!

When building, Cargo downloads and caches crates needed as dependencies. Historically, these downloaded files would never be cleaned up, leading to an unbounded amount of disk usage in Cargo's home directory. In this version, Cargo introduces a garbage collection mechanism to automatically clean up old files (e.g..cratefiles). Cargo will remove files downloaded from the network if not accessed in 3 months, and files obtained from the local system if not accessed in 1 month. Note that this automatic garbage collection will not take place if running offline (using--offlineor--frozen).

Cargo 1.78 and newer track the access information needed for this garbage collection. This was introduced well before the actual cleanup that's starting now, in order to reduce cache churn for those that still use prior versions. If you regularly use versions of Cargo even older than 1.78, in addition to running current versions of Cargo, and you expect to have some crates accessed exclusively by the older versions of Cargo and don't want to re-download those crates every ~3 months, you may wish to setcache.auto-clean-frequency = "never"in the Cargo configuration, as described in thedocs.

For more information, see the originalunstable announcementof this feature. Some parts of that design remain unstable, like thegcsubcommand tracked incargo#13060, so there's still more to look forward to!

### Stabilized APIs

* Cell::update
* impl Default for *const T
* impl Default for *mut T
* mod ffi::c_str
* HashMap::extract_if
* HashSet::extract_if
* hint::select_unpredictable
* proc_macro::Span::line
* proc_macro::Span::column
* proc_macro::Span::start
* proc_macro::Span::end
* proc_macro::Span::file
* proc_macro::Span::local_file
* <[T]>::as_chunks
* <[T]>::as_rchunks
* <[T]>::as_chunks_unchecked
* <[T]>::as_chunks_mut
* <[T]>::as_rchunks_mut
* <[T]>::as_chunks_unchecked_mut

These previously stable APIs are now stable in const contexts:

* NonNull<T>::replace
* <*mut T>::replace
* std::ptr::swap_nonoverlapping
* Cell::replace
* Cell::get
* Cell::get_mut
* Cell::from_mut
* Cell::as_slice_of_cells

### Other changes

Thei686-pc-windows-gnutarget has been demoted to Tier 2, as mentioned in anearlier post. This won't have any immediate effect for users, since both the compiler and standard library tools will still be distributed byrustupfor this target. However, with less testing than it had at Tier 1, it has more chance of accumulating bugs in the future.

Check out everything that changed inRust,Cargo, andClippy.

## Contributors to 1.88.0

Many people came together to create Rust 1.88.0. We couldn't have done it without all of you.Thanks!
