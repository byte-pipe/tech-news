---
title: Rust running on every GPU | Rust GPU
url: https://rust-gpu.github.io/blog/2025/07/25/rust-on-every-gpu/
site_name: hackernews_api
fetched_at: '2025-07-27T10:22:43.116756'
original_url: https://rust-gpu.github.io/blog/2025/07/25/rust-on-every-gpu/
author: littlestymaar
date: '2025-07-26'
published_date: '2025-07-25T00:00:00.000Z'
description: I've built a demo of a single
tags:
- hackernews
- trending
---

I've built ademoof a single
shared Rust codebase that runs on every major GPU platform:

* CUDAfor NVIDIA GPUs
* SPIR-Vfor Vulkan-compatible GPUs from AMD, Intel, NVIDIA, and Android devices
* Metalfor Apple devices
* DirectX 12for Windows
* WebGPUfor browsers
* CPUfallback for non-GPU systems

The same compute logic runs on all targets, written entirely in regular Rust. No shader
or kernel languages are used.

The code is available onGitHub.

## Background​

GPUs are typically programmed using specialized languages likeWGSL,GLSL,MSL,HLSL,Slang, orTriton. These languages are GPU-specific and
separate from the host application's language and tooling, increasing complexity and
duplicating logic across CPU and GPU code.

Some of us in the Rust community are taking a different approach and want to program
GPUs by compiling standard Rust code directly to GPU targets. Three main projects make
this possible1:

1. Rust GPU:Compiles Rust code toSPIR-V, the binary format used byVulkanand other modern GPU APIs. This allows GPU code to
be written entirely in Rust and used in any Vulkan-compatible workflow.
2. Rust CUDA:Compiles Rust code toNVVM
IR, enabling execution on
NVIDIA GPUs through the CUDA runtime.
3. Naga:A GPU language translation layer
developed by thewgputeam. It provides a common
intermediate representation and supports translating between WGSL, SPIR-V, GLSL, MSL,
and HLSL. Naga focuses on portability and is used to bridge different graphics
backends.

Previously, these projects were siloed as they were started by different people at
different times with different goals. As a maintainer of Rust GPU and Rust CUDA and a
contributor tonaga, I have been working to bring them closer together.

Thisdemois the first time all
major GPU backends run from a single Rust codebase without a ton of hacks. It's the
culmination of hard work from many contributors and shows that cross-platform GPU
compute in Rust is now possible.

There are still many rough edges and a lot of work to do, but this is an exciting
milestone!

## How it works​

The demo implements a simplebitonic
sort. The compute logic is fully generic
and shared across all targets, running the same code on both CPU and GPU.

GPU terminology is a bit of a mess and it is easy to get turned around. To avoid
confusion, this is how I will refer to different parts of the system:

* Host: The Rust code running on the CPU that launches GPU work.
* Device: The GPU or CPU where the compute kernel runs.
* Driver API: The low-level interface used to communicate with the device (e.g.,CUDA,Vulkan,Metal,DirectX 12).
* Backend: The Rust-side abstraction layer or library used to target a driver API
(e.g.,cust,ash,wgpu).

### Backend selection​

Backends and driver APIs are selected using a combination of Rust feature flags and compilation targets.

* cargo build --features wgpuuseswgpu, which selects the system default driver API.
* cargo build --features wgpu,vulkanforceswgputo use Vulkan, even on platforms where it isn’t the default (for example, to useMoltenVKon macOS).
* cargo build --features ashenables a Vulkan-only backend using theashcrate. This is useful when you want direct control over Vulkan without the overhead or abstraction ofwgpu, and demonstrates that the project is not tied to a single graphics abstraction.
* cargo build --features cudaenables the NVIDIA-specific CUDA backend. This uses thecustcrate internally, but support could be added forcudarcas well.

Though this demo doesn't do so, multiple backends could be compiled into a single binary
and platform-specific code paths could then be selected at runtime. This would allow a
single Rust binary to dynamically choose the best GPU technology for a user's device.

There is a huge matrix of supported hosts, driver APIs, and backends. For the full list,
see theREADME.

### Kernel compilation​

Kernels are compiled to the appropriate device format for the given Rust features,
target OS, and driver API. These compiled kernels are embedded into the binary at build
time. While this demo does not support runtime loading, the underlying tools and
ecosystem do.

The demo uses a single compute kernel and entry point for simplicity. The underlying
tools and ecosystem support multiple kernels and multiple entry points if your use case
requires it.

## A look under the hood​

There are many pieces that are working together behind the scenes to enable such a
simple developer experience. Here is roughly what happens for a given command:

* cargo run --release:During the build,rustccompiles both the host code and the compute kernel to
native CPU code.No external toolchains or code generation steps are involved.The kernel runs directly on the CPU as standard Rust code.
* cargo run --features wgpu:During the build,build.rsusesrustc_codegen_spirvto compile the GPU kernel to SPIR-V.The resulting SPIR-V is embedded into the CPU binary as static data.The host code is compiled normally.At runtime, the CPU loads the embedded SPIR-V and passes it tonaga, which translates it to the
shading language required by the platform.wgputhen forwards the translated code to the appropriate driver API to execute the
kernel on the GPU:macOS:SPIR-V is translated to MSLMSL is passed to MetalMetal executes the kernel on the GPUWindows:SPIR-V is translated to HLSLHLSL is passed to DirectX 12DX12 executes the kernel on the GPULinux / Android:SPIR-V is used directlySPIR-V is passed to VulkanVulkan executes the kernel on the GPU
* macOS:SPIR-V is translated to MSLMSL is passed to MetalMetal executes the kernel on the GPU
* SPIR-V is translated to MSL
* MSL is passed to Metal
* Metal executes the kernel on the GPU
* Windows:SPIR-V is translated to HLSLHLSL is passed to DirectX 12DX12 executes the kernel on the GPU
* SPIR-V is translated to HLSL
* HLSL is passed to DirectX 12
* DX12 executes the kernel on the GPU
* Linux / Android:SPIR-V is used directlySPIR-V is passed to VulkanVulkan executes the kernel on the GPU
* SPIR-V is used directly
* SPIR-V is passed to Vulkan
* Vulkan executes the kernel on the GPU
* cargo run --features cuda:During the build,build.rsusesrustc_codegen_nvvmto compile the GPU
kernel to PTX.The resulting PTX is embedded into the CPU binary as static data.The host code is compiled normally.At runtime, the CPU loads the embedded PTX and passes it to the CUDA driver via thecustcrate.CUDA compiles the PTX to SASS (GPU machine code), uploads it to the GPU, and executes the kernel.

## A Rust-native GPU project​

In previous demos, we simply ported GLSLshadertoysandVulkan
examplesto Rust as-is.
This project instead focuses on demonstrating some of Rust's strengths for GPU
programming directly.

### no_stdsupport​

Code that runs on the GPU uses#![no_std],
as the standard library isn't available on GPUs:

#![cfg_attr(target_arch =
"spirv"
, no_std)]
#![cfg_attr(target_os =
"cuda"
, no_std)]

Rust'sno_stdecosystem was designed from day one to support embedded, firmware, and
kernel development. These environments, like GPUs, lack operating system services. This
first-class support creates a clear separation betweencore(always available) andstd(needs an OS), with compiler-enforced boundaries
that guarantee if your code compiles, it will link.

Existingno_std+ noalloccrates written for
other purposes can generally run on the GPU without modification.no_stdis not an
afterthought or a special "GPU mode", it's how Rust was designed to work.

### Conditional compilation​

The project uses sophisticatedconditional compilationpatterns:

// Platform-specific type availability
#[cfg(any(target_arch =
"spirv"
, target_os =
"cuda"
))]
use

shared
::
BitonicParams
;
// Conditional trait implementations
#[cfg(feature =
"cuda"
)]
unsafe

impl

DeviceCopy

for

BitonicParams

{
}
// Platform-specific constants with unified naming
// CUDA terminology alias only appears when using CUDA.
pub

const

WORKGROUP_SIZE
:

u32

=

256
;
#[cfg(feature =
"cuda"
)]
pub

const

BLOCK_SIZE
:

u32

=

WORKGROUP_SIZE
;

Rust's conditional compilation is a first-class language feature that keeps platform
code in one place while maintaining clarity. The compiler understands all code paths and
provides full IDE support across all configurations. This is in stark contrast to traditional GPU tooling.

### Newtypes​

There is extensive use ofnewtypesto prevent
logical errors at compile time:

#[derive(Copy, Clone, Debug)]
pub

struct

ThreadId
(
u32
)
;
#[derive(Copy, Clone, Debug)]
pub

struct

ComparisonDistance
(
u32
)
;
#[derive(Copy, Clone, Debug, PartialEq, Eq, Pod, Zeroable)]
#[repr(transparent)]

// Same memory layout as u32
pub

struct

Stage
(
u32
)
;

Newtypes turn runtime errors into compile-time errors by making domain concepts part of
the type system. With#[repr(transparent)],
these abstractions have zero runtime cost—they compile to identical machine code as raw
integers. The result is self-documenting APIs that prevent logical errors using the same
patterns Rust developers use daily on the CPU. Newtypes are especially valuable for GPU
programming, where debugging is difficult and errors can manifest as silent corruption.

### Enums​

Enumsreplace magic numbers with compile-time checked values:

#[derive(Copy, Clone, Debug, PartialEq)]
#[repr(u32)]

// Guaranteed memory layout for GPU
pub

enum

SortOrder

{

Ascending

=

0
,

Descending

=

1
,
}

Enums provide type-safe configuration that can compile to raw integers. With#[repr(u32)], you get predictable layout across platforms, while pattern matching
ensures exhaustive handling of all cases. The result is self-documenting code that reads
naturally while eliminating entire classes of bugs.

warning

Care must still be taken when passing enumsbetweenthe CPU host and GPU kernel code. Even with a fixed layout using#[repr(u32)], Rust does not guarantee that every possibleu32value is a valid instance of the enum.With the above enum, if the host or kernel writes the value "3" into a buffer shared across the device boundary and the other side interprets it asSortOrder, this results in undefined behavior. Rust assumes that all enum values are valid according to their discriminant, and violating this assumption can break pattern matching, control flow, and optimization correctness.We hope to improve the safety of this boundary in the future by making Rust more "GPU
aware", but there is language design work to do.

### Traits​

Traitsenable generic algorithms
that work across types without runtime dispatch:

pub

trait

SortableKey
:

Copy

+

Pod

+

Zeroable

+

PartialOrd

{

fn

to_sortable_u32
(
&
self
)

->

u32
;

fn

from_sortable_u32
(
val
:

u32
)

->

Self
;

fn

should_swap
(
&
self
,
 other
:

&
Self
,
 order
:

SortOrder
)

->

bool
;

fn

max_value
(
)

->

Self
;

fn

min_value
(
)

->

Self
;
}
// Implementations handle type-specific details
impl

SortableKey

for

f32

{

fn

to_sortable_u32
(
&
self
)

->

u32

{

let
 bits
=

self
.
to_bits
(
)
;

// Bit manipulation to handle IEEE 754 float ordering correctly

if
 bits
&

(
1

<<

31
)

!=

0

{

!
bits
// Negative floats: flip all bits

}

else

{
 bits
|

(
1

<<

31
)

// Positive floats: flip sign bit

}

}
}

Traits provide zero-cost abstraction for generic GPU algorithms. You write once and use
with any type that meets the requirements, with trait bounds documenting exactly what
the GPU needs from a type. Monomorphization generates specialized code with the same
performance as hand-written versions, while complex type-specific logic stays
encapsulated in implementations.

This ecosystem composability is extremely valuable and unmatched. Any Rust crate can
implement your traits for its types, enabling third-party numeric types to work
seamlessly with your GPU kernels while maintaining clear contracts between GPU code and
data types.

### Inline​

The project uses#[inline]to ensure abstractions disappear at compile time:

impl

ComparisonDistance

{

#[inline]

fn

from_stage_pass
(
stage
:

Stage
,
 pass
:

Pass
)

->

Self

{

Self
(
1u32

<<

(
stage
.
as_u32
(
)

-
 pass
.
as_u32
(
)
)
)

}

#[inline]

fn

find_partner
(
&
self
,
 thread_id
:

ThreadId
)

->

ThreadId

{

ThreadId
::
new
(
thread_id
.
as_u32
(
)

^

self
.
0
)

}
}

This matters for GPUs because function calls are expensive due to register pressure and
the lack of a traditional stack. These example methods compile to single instructions,
and bit manipulation operations likeXORandshiftmap directly to GPU hardware
instructions. The same zero-cost principle that makes Rust suitable for systems
programming makes it perfect for GPUs.

### Struct composition​

Complex programs usually benefit fromsemantic
grouping:

/// Represents a comparison pair in the bitonic network
#[derive(Copy, Clone, Debug)]
pub

struct

ComparisonPair

{
 lower
:

ThreadId
,
 upper
:

ThreadId
,
}
impl

ComparisonPair

{

#[inline]

fn

try_new
(
thread_id
:

ThreadId
,
 partner
:

ThreadId
)

->

(
bool
,

Self
)

{

let
 is_valid
=
 partner
.
as_u32
(
)

>
 thread_id
.
as_u32
(
)
;

let
 pair
=

Self

{
 lower
:
 thread_id
,
 upper
:
 partner
,

}
;

(
is_valid
,
 pair
)

}

#[inline]

fn

is_in_bounds
(
&
self
,
 num_elements
:

u32
)

->

bool

{

self
.
upper
.
as_u32
(
)

<
 num_elements

}
}

Traditional GPU kernels often suffer from parameter explosion, with 10 or more arguments
passed to a single function. Rust's struct composition provides a cleaner approach. This
snippet shows:

* Semantic grouping:The two thread IDs that form a comparison pair live together as a
logical unit.
* Encapsulation:Private fields ensure lower and upper maintain their relationship.
* Smart constructors:try_new()returns both validity and the pair, preventing
invalid states.

Standard Rust practices transform what would be error-prone index manipulations into
type-safe, self-documenting GPU code.

### Memory layout control​

Rust provides fine-grainedrepresentation control, defining explicit and verifiable memory layouts essential for GPU interoperability.

#[repr(C)]

// C-compatible layout, field order preserved
#[derive(Copy, Clone, Debug, Pod, Zeroable)]
pub

struct

BitonicParams

{

pub
 num_elements
:

u32
,

pub
 stage
:

Stage
,

// Newtypes with #[repr(transparent)]

pub
 pass_of_stage
:

Pass
,

// Compiles to u32 in memory

pub
 sort_order
:

u32
,
}

The#[repr(C)]attribute provides the layout guarantees required for GPU data transfer.

warning

Care must still be taken to ensure data is padded correctly. We hope in the future we
can better integrate the padding requirements for each GPU target into Rust, but for now
you must do so manually.

### Pattern matching​

Pattern matchingprovides exhaustive case handling and clear intent:

/// Compare two values for sorting
fn

should_swap
(
&
self
,
 other
:

&
Self
,
 order
:

SortOrder
)

->

bool

{

match
 order
{

SortOrder
::
Ascending

=>

self

>
 other
,

SortOrder
::
Descending

=>

self

<
 other
,

}
}

Pattern matching is particularly valuable for GPU programming. It makes all code paths
explicit, helping the compiler generate efficient code. When dealing with
platform-specific values or error conditions, pattern matching provides clear, type-safe
handling that prevents invalid states from reaching GPU kernels.

### Generics​

Generic functionsare leveraged to
reuse the same logic for multiple types:

#[inline]
fn

compare_and_swap
<
T
>
(
data
:

&
mut

[
T
]
,
 pair
:

ComparisonPair
,
 direction
:

BitonicDirection
)
where

T
:

Copy

+

PartialOrd
,

// Constraints are explicit
{

let
 val_i
=
 data
[
pair
.
lower
.
as_usize
(
)
]
;

let
 val_j
=
 data
[
pair
.
upper
.
as_usize
(
)
]
;

if
 direction
.
should_swap
(
val_i
,
 val_j
)

{
 data
.
swap
(
pair
.
lower
.
as_usize
(
)
,
 pair
.
upper
.
as_usize
(
)
)
;

}
}

Rust enables generic programming with clear constraints and (mostly) excellent error
messages.Trait
boundsexplicitly state what operations are needed, and error messages point to your code
rather than expanded template instantiations.Monomorphizationgenerates optimal code for each type, and the same generic algorithms work seamlessly on
both CPU and GPU. This makes it practical to write complex generic GPU algorithms that
are both reusable and maintainable.

### Derive macros​

Derive macrosare used to automatically implement traits:

#[derive(Copy, Clone, Debug, PartialEq, Eq, Pod, Zeroable)]
#[repr(transparent)]
pub

struct

Stage
(
pub

u32
)
;

Each derive provides specific guarantees:Copyenables bitwise copying (required for GPU types),Cloneprovides explicit cloning support,Debugmakes types printable for CPU-side debugging,PartialEqandEqenable comparison operators,Pod("Plain Old Data") ensures the type is safe to transmit to GPU memory, andZeroableconfirms it's safe to zero-initialize. One line of derive macros generates all the boilerplate that GPU programming traditionally requires you to write manually, with the compiler verifying these traits are actually valid for your type (unless you useunsafe).

### Module system​

Rust'smodule
systemkeeps the code organized. GPU projects quickly become complex with host-side setup code,
multiple kernels, shared type definitions, and platform-specific implementations. This
complexity is organized using the same patterns developers use for any large CPU-based
Rust project.

### Workspaces and workspace dependencies​

The project usesCargo
workspacesto organize
code. For large GPU projects with multiple kernels and utilities, workspaces make it
easy to share common code while maintaining clear boundaries between components.

Workspace
dependenciesensure consistency in dependencies across crates:

[dependencies]
# Platform-specific dependency inherited from workspace
[target.'cfg(target_arch = "spirv")'.dependencies]
spirv-std.workspace = true
# Inherit workspace lints
[lints]
workspace = true

### Formatting​

Rust GPU code is formatted withrustfmt, following the same standards as all Rust
code. This not only ensures my GPU code looks identical to my CPU code, it makes my GPU
code consistent with theentire Rust ecosystem. Leveraging standard tools likerustfmtminimizes cognitive overhead and avoids the hassle of configuring third-party
formatters of varying quality.

### Lint​

Linting GPU code in Rust works the same way as for CPU code. Runningcargo clippyhighlighted issues and enforced consistent code quality. As shown above, custom lint
configurations are applied to Rust GPU kernels as well and interact as you would expect
with workspaces.

### Documentation​

Writing doc comments and runningcargo docgenerates documentation for GPU kernels,
exactly how it happens in regular Rust. The code in doc comments are only run on the CPU
though.

While some ecosystems offer similar tools, Rust's integration is built-in and works
seamlessly for both CPU and GPU code. There's no special setup required.

### Build scripts​

The project uses a Cargobuild
scriptto compile and
embed GPU kernels as part of the normalcargo buildprocess:

// build.rs
fn

main
(
)

{

#[cfg(any(feature =
"vulkan"
, feature =
"wgpu"
))]

build_spirv_kernel
(
)
;

#[cfg(feature =
"cuda"
)]

build_cuda_kernel
(
)
;
}

The build script provides seamless integration and good DX by invoking specialized
compilers (rustc_codegen_nvvm,rustc_codegen_spirv) to generate GPU binaries duringcargo build. This leverages Rust's dependency resolution and caching while keeping
everything in the normal Rust ecosystem. The same kernel source code is compiled to
different targets based on feature flags with no manual build steps or shell scripts
required.

### Unit tests​

One of the most powerful aspects of using Rust is that GPU kernel code can be tested
on the CPU using standard Rust testing tools:

#[cfg(test)]
mod

tests

{

#[test]

fn

test_bitonic_sort_correctness
(
)

{

let

mut
 data
=

vec!
[
5
,

2
,

8
,

1
,

9
]
;

// Test the algorithm logic without GPU complexity

sort_on_cpu
(
&
mut
 data
)
;

assert_eq!
(
data
,

vec!
[
1
,

2
,

5
,

8
,

9
]
)
;

}
}

warning

Care must still be taken to run the kernel code on the CPU in a way that matches its GPU
behavior.The same invariants—such as workgroup size, memory access patterns, and
synchronization—must be upheld to ensure correctness across backends.We hope in the future to have built-in simulators or libraries that handle this for you,
but they do not exist yet.

CPU testing capability transforms GPU development. You can use standard debugging tools
likegdborlldbto
step through your kernel logic. Print debugging withprintln!works during development.
Property-based testing with crates likeproptestcan verify algorithm correctness.
Code coverage tools likecargo-llvm-covshow which paths your tests exercise.

The development cycle becomes: write the algorithm, test it thoroughly on CPU with
familiar tools, then run it on GPU knowing the logic is likely correct. This eliminates
much of the painful "compile, upload, run, crash, guess why" cycle that plagues GPU
development. When something goes wrong on the GPU, you can usually reproduce it on the
CPU and debug it properly. Open source projects likerenderlinguse this testing capability for great
effect.

Furthermore, because the kernel code is standard Rust, no GPU hardware is needed in CI
to test the logic. This is important for open source projects as theGitHub Actions
runnersdo not have GPUs. One can even test the Vulkan kernel code using a software driver likeSwiftShaderorlavapipeand get some signal that the
bulk of CUDA logic is correct (modulo any platform-gated logic). This has the potential
to save on expensive NVIDIA GPU time.

## Rough edges​

This demo shows that Rust can target all major GPU platforms, but the developer
experience is still pretty rough and bolted together.

First, the compiler backends are not integrated intorustc. To build GPU code,
developers must userustc_codegen_spirvorrustc_codegen_nvvmdirectly. Helper
crates likespirv_builderandcuda_builderhide some complexity but it's still more involved than using standard Rust. Furthermore,
a very specific version of nightly Rust is necessary for everything to work. Ideally
these backends would be built into the main compiler and work with things like standardrustuptooling. There is no timeline for this, but it is a goal.

Rust CUDA also depends on NVIDIA's toolchain, which is effectively tied to LLVM 7.1.
Most modern Linux distributions no longer provide packages for this version so it must
be built manually. This is a significant burden. The project maintainsDocker
imageswith the full
toolchain but ideally those should only be needed by compiler developers and not end
users like they are now.

Debugging the compilation process is also difficult. Tracing Rust code through the
various layers and toolchains is challenging. Some parts support debug info, others do
not. This often leads to opaque errors with no clear indication of which code caused the
failure. Improving the debugging experience is a high priority and clearly needed.

Finally, Rust GPU and Rust CUDA evolved independently and diverged in their APIs. For
example, accessing thread indices is done through a function call in Rust CUDA
(thread::thread_idx_x()), while in Rust GPU it requires annotating entrypoint
arguments. Even the standard library names differ (cuda_stdvsspirv_std) and thuscfg()directives are required in GPU-aware code even if the APIs are the same. These
inconsistencies make the user experience harder than it should be and unifying the APIs
where possible is an obvious next step. Unifying the codebases might make sense too.

## Come join us!​

We can finally write GPU code in Rust and run it on all major platforms across all major
GPUs. The next step is to improve the experience. We need to add support for more Rust
language constructs and APIs. Everything needs to be made more ergonomic, more
consistent, and fully integrated into the Rust ecosystem. Plus, we haven't even really
started optimizing performance either. Come help, we're eager to add more users and
contributors!

To follow along or get involved, check out therust-gpurepo on
GitHubor therust-cudarepo on
GitHub.

## Footnotes​

1. There are other projects and approaches, check out theGPU ecosystem in Rust
overview page.↩
