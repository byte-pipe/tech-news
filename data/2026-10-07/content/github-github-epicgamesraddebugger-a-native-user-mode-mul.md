---
title: 'GitHub - EpicGames/raddebugger: A native, user-mode, multi-process, graphical debugger. · GitHub'
url: https://github.com/EpicGames/raddebugger
site_name: github
content_file: github-github-epicgamesraddebugger-a-native-user-mode-mul
fetched_at: '2026-10-07T17:42:29.281861'
original_url: https://github.com/EpicGames/raddebugger
author: EpicGames
description: A native, user-mode, multi-process, graphical debugger. - EpicGames/raddebugger
---

master
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

4,679 Commits
4,679 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github/
workflows
.github/
workflows
 
 
data
data
 
 
obsolete
obsolete
 
 
src
src
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
CHANGELOG.md
CHANGELOG.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
build.bat
build.bat
 
 
build.sh
build.sh
 
 
launch.vs.json
launch.vs.json
 
 
project.4coder
project.4coder
 
 
project.raddbg
project.raddbg
 
 
run_tests.bat
run_tests.bat
 
 
run_tests.sh
run_tests.sh
 
 
View all files

## Repository files navigation

# The RAD Debugger Project

NOTE:This README does not document usage instructions and tips for the
debugger itself, and is intended as a technical overview of the project. The
debugger's README, which includes usage instructions and tips, can be found
packaged along with debugger releases, or within thebuildfolder after a
local copy has been built. You can find pre-built release binarieshere.

The RAD Debugger is a native, user-mode, multi-process, graphical debugger. It
currently only supports local-machine Windows x64 debugging with PDBs, with
plans to expand and port in the future. In the future we'll expand to also
support native Linux debugging and DWARF debug info.

The debugger is currently inALPHA. In order to get the debugger
bullet-proof, it'd greatly help out if you submitted the issues you findhere, along with any
information you can gather, like dump files (along with the build you used),
instructions to reproduce, test executables, and so on.

In addition to the debugger, we aim to further improve the toolchain with two
additional related technologies:(1)the RAD Debug Info (RDI) format, and(2)the RAD Linker.

## The RAD Debug Info (RDI) Format

The RAD Debug Info (RDI) format is our custom debug information format, which
the debugger parses and uses, rather than the debug information natively
produced by toolchains, like PDB or DWARF. To work with these existing
toolchains, we convert PDB (and eventually PE/ELF files with embedded DWARF)
into the RDI format on-demand.

The RDI format is currently specified in code, in the files within thesrc/lib_rdifolder. Inrdi.handrdi.c, the types and functions which define the format
itself are specified. Inrdi_parse.handrdi_parse.c, helpers for parsing the format are
included.

We also have an in-progress library for constructing and serializing RDI data,
located within thesrc/lib_rdi_makefolder.

Ourradbinutility (accessible through the debugger too, via the--bincommand line argument) is capable of converting native debug information formats
to RDI, and of producing textual dumps of contents stored within RDI files.

## The RAD Linker

The RAD Linker is a new performance linker for generating x64 PE/COFF binaries.
It is designed to be very fast when creating gigantic executables. It generates
standard PDB files for debugging, but it can also (optionally) natively create
RAD Debug Info too, which is useful both to eliminate on-demand conversion time
when debugging, but also for huge executables that otherwise create broken
PDBs that overflow internal 32-bit tables.

The RAD Linker is primarily optimized to handle huge linking projects. In our
test cases (where debug info is multiple gigabytes), we see 50% faster link
times.

The command line syntax is fully compatible with MSVC; you can get a full list
of implemented switches from/help.

Our current designed-for use case for the linker is to help with the
compile-debug cycle of huge projects. We don't yet have support for
link-time-optimizations, but this feature is on the road map.

By default, the linker spawns as many threads as there are cores, so if you plan
to run multiple linkers in parallel, you can limit the number of thread workers
via/rad_workers.

We also have support for large memory pages, which, when enabled, reduce link
time by another 25%. To link with large pages, you need to explicitly request
them via/rad_large_pages. Large pages are off by default, since Windows
support for large pages is a bit buggy; we recommend they only be used in Docker
or VM images where the environment is reset after each link. In a standard
Windows environment, using large pages otherwise will fragment memory quickly,
forcing a reboot. We are working on a Linux port of the linker that will be able
to build with large pages robustly.

A benchmark of the linker's performance is below:

# Project Development Setup / Local Build Instructions

The project is actively developed both onWindows x64andLinux x64development machines. Click on whichever you'd like to
use.

## Windows x64

### 1. Installing the Required Tools (MSVC & Windows SDK)

First, you'll need theMicrosoft C/C++ Build Tools v15 (2017) or later,
for the Windows SDK, and the MSVC compiler and linker.

If the Windows SDK is installed (e.g. via installation of the Microsoft C/C++
Build Tools), you may also build withClang.

### 2. Build Environment Setup

Building the codebase can be done in a terminal which is equipped with the
ability to call either MSVC or Clang from command line.

This is generally done by callingvcvarsall.bat x64, which is included in the
Microsoft C/C++ Build Tools. This script is automatically called by thex64 Native Tools Command Prompt for VS <year>variant of the vanillacmd.exe. If
you've installed the build tools, this command prompt may be easily located by
searching forNativefrom the Windows Start Menu search.

You can ensure that the MSVC compiler is accessible from your command line by
running:

cl

If everything is set up correctly, you should have output very similar to the
following:

Microsoft (R) C/C++ Optimizing Compiler Version 19.29.30151 for x64
Copyright (C) Microsoft Corporation. All rights reserved.

usage: cl [ option... ] filename... [ /link linkoption... ]

### 3. Building

Within this terminal,cdto the root directory of the codebase, and just run
thebuild.batscript:

build

You should see the following output:

[debug mode]
[msvc compile]
[default mode, assuming `raddbg` build]
metagen_main.c
searching C:\devel\raddebugger/src... 458 files found
parsing metadesk... 16 metadesk files parsed
gathering tables... 97 tables found
generating layer code...
raddbg_main.c

If everything worked correctly, there will be abuildfolder in the root
level of the codebase, and it will contain a freshly-builtraddbg.exe.

Thisraddbg.exewill have been built indebug mode, which is not built
with optimizations, and may perform worse. To produce arelease mode executable, runbuild.batwith areleaseargument:

build release

This build will take significantly longer.

By default,build.batonly builds the debugger if no arguments (or justrelease) are passed, but additional arguments can be passed to build the RAD
Linker, or theradbinCLI binary file utility:

build radlink release
build radbin release

## Linux x64

### 1. Installing the Required Tools (GCC or Clang, Libraries)

First, you'll need either GCC or Clang, if you don't already have them. They
can be obtained by running one of the following commands, depending on your
toolchain of choice and distribution:

#### GCC on Ubuntu / Debian / Mint

sudo apt update && sudo apt install build-essential

#### Clang on Ubuntu / Debian / Mint

sudo apt update && sudo apt install clang llvm

#### GCC on Arch / Manjaro

sudo pacman -S base-devel

#### Clang on Arch / Manjaro

sudo pacman -S clang llvm

If you've installed the Clang and LLVM tooling required, you can run:

clang --version && llvm-ar --version

You should see output similar to the following:

Ubuntu clang version 18.1.3 (1ubuntu1)
Target: x86_64-pc-linux-gnu
Thread model: posix
InstalledDir: /usr/bin
Ubuntu LLVM version 18.1.3
 Optimized build.

If you've installed the GCC tooling required, you can run:

gcc --version && gcc-ar --version

You should see output similar to the following:

gcc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0
Copyright (C) 2023 Free Software Foundation, Inc.
This is free software; see the source for copying conditions. There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

GNU ar (GNU Binutils for Ubuntu) 2.42
Copyright (C) 2024 Free Software Foundation, Inc.
This program is free software; you may redistribute it under the terms of
the GNU General Public License version 3 or (at your option) any later version.
This program has absolutely no warranty.

### 2. Installing Dependencies

The debugger project relies on a few dynamically linked libraries being present
on the system:

* libfreetype
* libx11
* libxext
* libxfixes
* libxrandr
* libgl
* libegl

You'll need the development packages for them in order to build. These can be
installed using one of the following commands, depending on your distribution:

#### Ubuntu / Debian / Mint

sudo apt install -y libfreetype6-dev libx11-dev libxext-dev libxfixes-dev libxrandr-dev libgl-dev libegl-dev

#### Arch / Manjaro

sudo pacman -S --needed freetype2 libx11 libxext libxfixes libxrandr libglvnd

### 3. Building

To build,cdto the root directory of the codebase, and run thebuild.shscript:

./build.sh

You should see something similar to the following output:

[clang compile]
[debug mode]
[building metagen]
searching /mnt/c/devel/raddebugger/src... 562 files found
parsing metadesk... 23 metadesk files parsed
gathering tables... 138 tables found
generating layer code...

If everything worked correctly, there will be abuildfolder in the root
level of the codebase, and it will contain a freshly-builtraddbgbinary.

Thisraddbgwill have been built indebug mode, which is not built with
optimizations, and may perform worse. To produce arelease mode executable,
runbuild.shwith areleaseargument:

./build.sh release

This build will take significantly longer.

By default,build.shonly builds the debugger if no arguments (or justrelease) are passed, but additional arguments can be passed to build the RAD
Linker, or theradbinCLI binary file utility:

./build.sh radlink release
./build.sh radbin release

# Project Roadmap

### The Initial Alpha Battle-Testing Phase

The first priority for the project is to ensure that the most crucial components
are functioning extremely reliably for local, x64, Windows development.
For the debugger, this would include parts like debug info conversion, debug
info loading, process control, stepping, evaluation (correct usage of both
location info and type info), and a robust frontend which ensures the lower
level parts are usable. For the linker, this is a matter of reliability and
convergence with existing linker behavior.

We feel that we've already come a long way in all of these respects, but given
the massive set of possible combinations of languages, build settings,
toolchains, used language features, and patterns of generated code, we still
expect some issues, and are prioritizing these issues being resolved first.

We also hope to continue to improve performance in this phase. For the debugger,
this primarily includes frontend performance, introducing caches when economical
to do so, and tightening existing systems up. For the linker, it has been mostly
tuned thus far for giant projects, and so we'd like to improve linking speed for
small-to-mid sized projects as well.

For the linker, there are also a number of features to come, like
dead-code-elimination (/opt:ref), and link-time-optimizations with the help
ofclang(we won't support LTCG from MSVC, since it is undocumented).

### Local x64 Linux Debugging Phase

The next priority for the project is to take the rock solid x64 Windows
debugging experience, and port all of the relevant pieces to support local x64
Linux debugging also.

The debugger has been written to abstract over the parts that need to differ on
either Linux or Windows, and this is mainly going to be a task in building out
different backends for those abstraction layers.

The major parts of this phase are:

* Porting thesrc/demonlayer to implement the Demon local process control
abstraction API.
* Implementing an x64 ELF Linux unwinder in thesrc/ctrllayer.
* Creating a DWARF-to-RDI converter (in the same way that we've built a
PDB-to-RDI converter). A partial implementation of this is insrc/rdi_from_dwarf.
* Porting thesrc/renderlayer to implement all of the rendering features the
frontend needs on a Linux-compatible API (the backend used on Windows is D3D11).
* Porting thesrc/font_providerlayer to a Linux-compatible font
rasterization backend, like FreeType (the backend used on Windows is
DirectWrite).
* Porting thesrc/oslayers to Linux. This includes core operating system
abstraction (virtual memory allocation, threading and synchronization
primitives, and so on), and graphical operating system abstraction (windows,
input events, and so on).

Once the above list is complete, and once every part is rock solid, the Windows
debugging experience we'll have worked diligently to create will also be
available natively on Linux machines.

### And Beyond!

There are several directions we might take after these two major phases,
like remote debugging, porting to different architectures, further improving
the debugger's features (like improving the visualization engine), and so on.
But for now, we're mostly focused on those first two phases.

# Codebase Introduction

## Top-Level Directory Descriptions

* data: Small binary files which are used when building, either to embed
within build artifacts, or to package with them.
* src: All source code.

After setting up the codebase and building, the following directories will
also exist:

* build: All build artifacts. Not checked in to version control.
* local: Local files, used for local build configuration input files. Not
checked in to version control.

## Layer Descriptions

The codebase is organized intolayers. Layers are separated either to isolate
certain problems, and to allow inclusion into various builds without needing to
pull everything in the codebase into a build. Layers correspond with folders
inside of thesrcdirectory. Sometimes, one folder inside of thesrcdirectory will include multiple sub-layers, but the structure is intended to be
fairly flat.

Layers correspond roughly 1-to-1 withnamespaces. The term "namespaces" in
this context does not refer to specific namespace language features, but rather
a naming convention for C-style namespaces, which are written in the codebase as
a short prefix, usually 1-3 characters, followed by an underscore. These
namespaces are used such that the layer to which certain code belongs may be
quickly understood by glancing at code. The namespaces are generally quite short
to ensure that they aren't much of a hassle to write. Sometimes, multiple sub-
layers will share a namespace. A few layers do not have a namespace, but most
do. Namespaces are either all-caps or lowercase depending on the context in
which they're used. For types, enum values, and some macros, they are
capitalized. For functions and global variables, they are lowercase.

Layers depend on other layers, but circular dependencies would break the
separability and isolation utility of layers (in effect, forming one big layer),
so in other words, layers are arranged into a directed acyclic graph.

A few layers are built to be used completely independently from the rest of the
codebase, as libraries in other codebases and projects. As such, these layers do
not depend on any other layers in the codebase. The folders which contain these
layers are prefixed withlib_, likelib_rdi.

A list of the layers in the codebase and their associated namespaces is below:

* artifact_cache(AC_): Implements an asynchronously-filled cache of
computation artifacts, which are automatically evicted when not accessed. Used
for asynchronously streaming and caching process memory and file system
contents, as well as asynchronously preparing visualizer data.
* base(no namespace): Universal, codebase-wide constructs. Strings, math,
memory allocators, helper macros, command-line parsing, and so on. Requires
no other codebase layers.
* codeview(CV_): Code for parsing and writing the CodeView format.
* coff(COFF_): Code for parsing and writing the COFF (Common Object File
Format) file format.
* content(C_): Implements a cache for general data blobs, keyed by a
128-bit hash of the data. Also implements a keying system on top, where keys
refer to a unique identity which corresponds to a history of 128-bit hashes.
Used as a general data store by other layers.
* ctrl(CTRL_): The debugger's "control system" layer. Implements
asynchronous process control, stepping, and breakpoints for all attached
processes. Runs in lockstep with attached processes. When it runs, attached
processes are halted. When attached processes are running, it is halted.
Driven by a debugger frontend on another thread.
* dbg_engine(D_): Implements the core debugger system, without any
graphical components. This contains top-level logic for things like stepping,
launching, freezing threads, mid-run breakpoint addition, some caches, and so
on.
* dbg_info(DI_): Implements asynchronous debug info conversion and loading.
Maintains a cache for loaded debug info. Loads RAD Debug Info (RDI) files.
Launches separate processes for on-demand conversion to the RDI format if
necessary. Also provides various asynchronous operations for using debug info,
like fuzzy searching across all records in loaded debug info.
* demon(DMN_): An abstraction layer for local-machine, low-level process
control. The abstraction is used to provide a common interface for process
control on target platforms. Used to implement part ofctrl.
* disasm(DASM_): Implements disassembly generation, including exposing the
ability to compute and cache disassembly asynchronously.
* draw(DR_): Implements a high-level graphics drawing API for the
debugger's purposes, using the underlyingrenderabstraction layer. Provides
high-level APIs for various draw commands, but takes care of batching them,
and so on.
* dwarf(DW_): Code for parsing the DWARF format.
* eh(EH_): Code for parsing the EH frame format.
* elf(ELF_): Code for parsing the ELF format.
* eval(E_): A compiler for an expression language, built for evaluation of
variables, registers, types, and more, from debugger-attached processes,
debug info, debugger state, and files. Broken into several phases mostly
corresponding to traditional compiler phases: lexer, parser, type-checker, IR
generation, and IR evaluation.
* eval_visualization(EV_): Implements the core non-graphical evaluation
visualization engine, which can be used to visualize evaluations (provided by
theevallayer) in a number of ways. Implements core data structures and
transforms for watch tables.
* file_stream(FS_): Implements asynchronous file streaming, storing the
artifacts inside of the cache implemented by thecontentandartifact_cachelayers, hot-reloading the contents of files when they change.
Allows callers to map file paths to data hashes, which can then be used to
obtain the file's data.
* font_cache(FNT_): Implements a cache of rasterized font data, both in
CPU-side data for text shaping, and in GPU texture atlases for rasterized
glyphs. All cache information is sourced from thefont_providerabstraction
layer.
* font_provider(FP_): An abstraction layer for various font file decoding
and font rasterization backends.
* lib_raddbg_markup(RADDBG_): Standalone library for marking up user
programs to work with various features in the debugger. Does not depend onbase, and can be independently relocated to other codebases.
* lib_rdi(RDI_): Standalone library which defines the core RDI types
and helper functions for reading and writing the RDI debug info file format.
Does not depend onbase, and can be independently relocated to other
codebases.
* lib_rdi_make(RDIM_): Standalone library for constructing RDI debug info
data. Does not depend onbase, and can be independently relocated
to other codebases.
* linker(LNK_): The layer which implements the RAD Linker executable
itself.
* mdesk(MD_): Code for parsing Metadesk files (stored as.mdesk), which
is the JSON-like (technically a JSON superset) text format used for the
debugger's user and project configuration files and metacode, which is parsed
and used to generate code with themetagenlayer.
* metagen(MG_): A metaprogram which is used to generate primarily code and
data tables. Consumes Metadesk files, stored with the extension.mdesk, and
generates C code which is then included by hand-written C code. Currently, it
does not analyze the codebase's hand-written C code, but in principle this is
possible. This allows easier & less-error-prone management of large data
tables, which are then used to produce e.g. Cenums and a number of
associated data tables. There are also a number of other generation features,
like embedding binary files or complex multi-line strings into source code.
* msf(MSF_): Code for parsing and writing the MSF file format.
* msvc_crt(MSCRT_): Code for parsing that's specific to the MSVC CRT.
* mule(no namespace): Test executables for battle testing debugger
functionality.
* mutable_text(MTX_): Implements an asynchronously-filled-and-mutated
cache for text buffers which are mutated across time. In the debugger, this is
used to implement theOutputlog.
* natvis(no namespace): NatVis files for type visualization of the codebase's
types in other debuggers.
* os/core(OS_): An abstraction layer providing core, non-graphical
functionality from the operating system under an abstract API, which is
implemented per-target-operating-system.
* os/gfx(OS_): An abstraction layer, building onos/core, providing
graphical operating system features under an abstract API, which is
implemented per-target-operating-system.
* pdb(PDB_): Code for parsing and writing the PDB file format.
* pe(PE_): Code for parsing and writing the PE (Portable Executable) file
format.
* radbin(RB_): The layer implementing theradbinbinary utility
executable.
* raddbg(RD_): The layer which ties everything together for the main
graphical debugger executable. Implements the debugger's graphical frontend,
all of the debugger-specific UI, the debugger executable's command line
interface, and all of the built-in visualizers.
* rdi(RDI_): A layer which includes thelib_rdilayer and bundles it with
codebase-specific helpers, to easily include the library in codebase programs,
and have it be integrated with codebase constructs.
* rdi_from_coff(C2R_): Code for converting information in COFF files to the
equivalent RDI data.
* rdi_from_dwarf(D2R_): In-progress code for converting DWARF to the
equivalent RDI data.
* rdi_from_elf(E2R_)): Code for converting ELF data to the equivalent RDI
data.
* rdi_from_pdb(P2R_): Code for converting PDB data to the equivalent RDI
data.
* rdi_make(RDIM_): A layer which includes thelib_rdi_makelayer and
bundles it with codebase-specific helpers, to easily include the library in
codebase programs, and have it be integrated with codebase constructs.
* regs(REGS_): Types, helper functions, and metadata for registers on
supported architectures. Used in reading/writing registers indemon, or in
looking up register metadata.
* render(R_): An abstraction layer providing an abstract API for rendering
using various GPU APIs under a common interface. Does not implement a high
level drawing API - this layer is strictly for minimally abstracting on an
as-needed basis. Higher level drawing features are implemented in thedrawlayer.
* scratch(no namespace): Scratch space for small and transient test programs.
* tester(no namespace): A program used for automated testing.
* text(TXT_): Implements text processing functions, like parsing line
breaks, and lexing and parsing source code. Also offers an API to do this
asynchronously.
* third_party(no namespace): External code from other projects, which some
layers in the codebase depend on. All external code is included and built
directly within the codebase.
* ui(UI_): Machinery for building graphical user interfaces. Provides a
core immediate mode hierarchical user interface data structure building
API, and has helper layers for building some higher-level widgets.