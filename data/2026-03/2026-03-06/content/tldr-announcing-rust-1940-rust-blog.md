---
title: Announcing Rust 1.94.0 | Rust Blog
url: https://blog.rust-lang.org/2026/03/05/Rust-1.94.0/
site_name: tldr
content_file: tldr-announcing-rust-1940-rust-blog
fetched_at: '2026-03-06T19:17:36.164216'
original_url: https://blog.rust-lang.org/2026/03/05/Rust-1.94.0/
date: '2026-03-06'
description: Empowering everyone to build reliable and efficient software.
tags:
- tldr
---

Mar. 5, 2026 · The Rust Release Team



The Rust team is happy to announce a new version of Rust, 1.94.0. Rust is a programming language empowering everyone to build reliable and efficient software.

If you have a previous version of Rust installed viarustup, you can get 1.94.0 with:

$ rustup update stable

If you don't have it already, you cangetrustupfrom the appropriate page on our website, and check out thedetailed release notes for 1.94.0.

If you'd like to help us out by testing future releases, you might consider updating locally to use the beta channel (rustup default beta) or the nightly channel (rustup default nightly). Pleasereportany bugs you might come across!

## What's in 1.94.0 stable

### Array windows

Rust 1.94 addsarray_windows, an iterating method for slices. It works just likewindowsbut with a constant length, so the iterator items are&[T; N]rather than dynamically-sized&[T]. In many cases, the window length may even be inferred by how the iterator is used!

For example, part of one2016 Advent of Code puzzleis looking for ABBA patterns: "two different characters followed by the reverse of that pair, such asxyyxorabba." If we assume only ASCII characters, that could be written by sweeping windows of the byte slice like this:

fn

has_abba
(
s
:

&
str
)

->

bool

{

 s
.
as_bytes
(
)


.
array_windows
(
)


.
any
(
|
[
a1
,

b1
,

b2
,
 a2
]
|

(
a1
!=
 b1
)

&&

(
a1
==
 a2
)

&&

(
b1
==
 b2
)
)

}

The destructuring argument pattern in that closure lets the compiler infer that we want windows of 4 here. If we had used the older.windows(4)iterator, then that argument would be a slice which we would have to index manually,hopingthat runtime bounds-checking will be optimized away.

### Cargo config inclusion

Cargo now supports theincludekey in configuration files (.cargo/config.toml), enabling better organization, sharing, and management of Cargo configurations across projects and environments. These include paths may also be markedoptionalif they might not be present in some circumstances, e.g. depending on local developer choices.

#
 array of paths

include

=

[


"
frodo.toml
"
,


"
samwise.toml
"
,

]

#
 inline tables for more control

include

=

[


{

path

=

"
required.toml
"

}
,


{

path

=

"
optional.toml
"
,

optional

=

true

}
,

]

See the fullincludedocumentationfor more details.

### TOML 1.1 support in Cargo

Cargo now parsesTOML v1.1for manifests and configuration files. See theTOML release notesfor detailed changes, including:

* Inline tables across multiple lines and with trailing commas
* \xHHand\estring escape characters
* Optional seconds in times (sets to 0)

For example, a dependency like this:

serde

=

{

version

=

"
1.0
"
,

features

=

[
"
derive
"
]

}

... can now be written like this:

serde = {

 version = "1.0",

 features = ["derive"],

}

Note that using these features inCargo.tomlwill raise your development MSRV (minimum supported Rust version) to require this new Cargo parser, and third-party tools that read the manifest may also need to update their parsers. However, Cargo automatically rewrites manifests on publish to remain compatible with older parsers, so it is still possible to support an earlier MSRV for your crate's users.

### Stabilized APIs

* <[T]>::array_windows
* <[T]>::element_offset
* LazyCell::get
* LazyCell::get_mut
* LazyCell::force_mut
* LazyLock::get
* LazyLock::get_mut
* LazyLock::force_mut
* impl TryFrom<char> for usize
* std::iter::Peekable::next_if_map
* std::iter::Peekable::next_if_map_mut
* x86avx512fp16intrinsics(excluding those that depend directly on the unstablef16type)
* AArch64 NEON fp16 intrinsics(excluding those that depend directly on the unstablef16type)
* f32::consts::EULER_GAMMA
* f64::consts::EULER_GAMMA
* f32::consts::GOLDEN_RATIO
* f64::consts::GOLDEN_RATIO

These previously stable APIs are now stable in const contexts:

* f32::mul_add
* f64::mul_add

### Other changes

Check out everything that changed inRust,Cargo, andClippy.

## Contributors to 1.94.0

Many people came together to create Rust 1.94.0. We couldn't have done it without all of you.Thanks!
