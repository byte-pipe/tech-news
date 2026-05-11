---
title: The cuda-oxide Book — cuda-oxide
url: https://nvlabs.github.io/cuda-oxide/index.html
site_name: hackernews_api
content_file: hackernews_api-the-cuda-oxide-book-cuda-oxide
fetched_at: '2026-05-12T06:00:17.381740'
original_url: https://nvlabs.github.io/cuda-oxide/index.html
author: adamnemecek
date: '2026-05-12'
description: 'CUDA-oxide: Nvidia''s official Rust to CUDA compiler'
tags:
- hackernews
- trending
---

# The cuda-oxide Book#

cuda-oxideis an experimental Rust-to-CUDA compiler that lets you write (SIMT) GPU kernels in safe(ish), idiomatic Rust. It compiles standard Rust code directly to PTX — no DSLs, no foreign language bindings, just Rust.

Note

This book assumes familiarity with the Rust programming language, including ownership, traits, and generics. Later chapters on async GPU programming also assume working knowledge ofasync/.awaitand runtimes like tokio.

For a refresher, seeThe Rust Programming Language,Rust by Example, or theAsync Book.

## Project Status#

The v0.1.0 release is an early-stage alpha:expect bugs, incomplete features, and API breakageas we work to improve it. We hope you’ll try it and help shape its direction by sharing feedback on your experience.

## 🚀 Quick start#

use
 
cuda_device
::{
cuda_module
,
 
kernel
,
 
thread
,
 
DisjointSlice
};

use
 
cuda_core
::{
CudaContext
,
 
DeviceBuffer
,
 
LaunchConfig
};

#[cuda_module]

mod
 
kernels
 
{

 
use
 
super
::
*
;

 
#[kernel]

 
fn
 
vecadd
(
a
:
 
&
[
f32
],
 
b
:
 
&
[
f32
],
 
mut
 
c
:
 
DisjointSlice
<
f32
>
)
 
{

 
let
 
idx
 
=
 
thread
::
index_1d
();

 
let
 
i
 
=
 
idx
.
get
();

 
if
 
let
 
Some
(
c_elem
)
 
=
 
c
.
get_mut
(
idx
)
 
{

 
*
c_elem
 
=
 
a
[
i
]
 
+
 
b
[
i
];

 
}

 
}

}

fn
 
main
()
 
{

 
let
 
ctx
 
=
 
CudaContext
::
new
(
0
).
unwrap
();

 
let
 
stream
 
=
 
ctx
.
default_stream
();

 
let
 
module
 
=
 
kernels
::
load
(
&
ctx
).
unwrap
();

 
let
 
a
 
=
 
DeviceBuffer
::
from_host
(
&
stream
,
 
&
[
1.0
f32
;
 
1024
]).
unwrap
();

 
let
 
b
 
=
 
DeviceBuffer
::
from_host
(
&
stream
,
 
&
[
2.0
f32
;
 
1024
]).
unwrap
();

 
let
 
mut
 
c
 
=
 
DeviceBuffer
::
<
f32
>
::
zeroed
(
&
stream
,
 
1024
).
unwrap
();

 
module

 
.
vecadd
(
&
stream
,
 
LaunchConfig
::
for_num_elems
(
1024
),
 
&
a
,
 
&
b
,
 
&
mut
 
c
)

 
.
unwrap
();

 
let
 
result
 
=
 
c
.
to_host_vec
(
&
stream
).
unwrap
();

 
assert_eq!
(
result
[
0
],
 
3.0
);

}

Build and run withcargooxiderunvecaddupon installing theprerequisites.

Note

#[cuda_module]embeds the generated device artifact into the host binary and
generates a typedkernels::loadfunction plus one launch method per kernel.
The lower-levelload_kernel_moduleandcuda_launch!APIs remain available
when you need to load a specific sidecar artifact or build custom launch code.

## Why cuda-oxide?#

🦀 Rust on the GPU

Write GPU kernels with Rust’s type system and ownership model.
Safety is a first-class goal, but GPUs have subtleties — read aboutthe safety model.

💎 A SIMT Compiler

Not a DSL. A custom rustc codegen backend that compiles
pure Rust to PTX.

⚡ Async Execution

Compose GPU work as lazyDeviceOperationgraphs.
Schedule across stream pools. Await results with.await.