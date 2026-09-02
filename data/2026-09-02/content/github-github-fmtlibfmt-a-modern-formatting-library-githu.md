---
title: 'GitHub - fmtlib/fmt: A modern formatting library · GitHub'
url: https://github.com/fmtlib/fmt
site_name: github
content_file: github-github-fmtlibfmt-a-modern-formatting-library-githu
fetched_at: '2026-09-02T14:58:50.216639'
original_url: https://github.com/fmtlib/fmt
author: fmtlib
description: A modern formatting library. Contribute to fmtlib/fmt development by creating an account on GitHub.
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 fmtlib

 

/

fmt

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork3k
* Star23.9k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

7,961 Commits
7,961 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
doc
doc
 
 
include/
fmt
include/
fmt
 
 
src
src
 
 
support
support
 
 
test
test
 
 
.clang-format
.clang-format
 
 
.clang-tidy
.clang-tidy
 
 
.cmake-format
.cmake-format
 
 
.gitignore
.gitignore
 
 
CMakeLists.txt
CMakeLists.txt
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
ChangeLog.md
ChangeLog.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
View all files

## Repository files navigation

{fmt}is an open-source formatting library providing a fast and safe
alternative to C stdio and C++ iostreams.

Documentation

Cheat Sheets

Q&A: ask questions onStackOverflow with the tag
fmt.

Try {fmt} inCompiler Explorer.

# Features

* Simpleformat APIwith positional
arguments for localization
* Implementation ofC++20
std::formatandC++23 std::print
* Format string syntaxsimilar
to Python'sformat
* Fast IEEE 754 floating-point formatter with correct rounding,
shortness and round-trip guarantees using theDragonboxalgorithm
* Portable Unicode support
* Safeprintf
implementationincluding the POSIX extension for positional arguments
* Extensibility:support for user-defined
types
* High performance: faster than common standard library
implementations of(s)printf, iostreams,to_stringandto_chars, seeSpeed testsandConverting a
hundred million integers to strings per
second
* Small code size both in terms of source code with the minimum
configuration consisting of just three files,base.h,format.handformat-inl.h, and compiled code; seeCompile time and code
bloat
* Reliability: the library has an extensive set oftestsand iscontinuously fuzzed
* Safety: the library is fully type-safe, errors in format strings can
be reported at compile time, automatic memory management prevents
buffer overflow errors
* Ease of use: small self-contained code base, no external
dependencies, permissive MITlicense
* Portabilitywith
consistent output across platforms and support for older compilers
* Clean warning-free codebase even on high warning levels such as-Wall -Wextra -pedantic
* Locale independence by default
* Optional header-only configuration enabled with theFMT_HEADER_ONLYmacro

See thedocumentationfor more details.

# Examples

Print to stdout(run)

#
include
 
<
fmt/base.h
>

int
 
main
() {
 
fmt::print
(
"
Hello, world!
\n
"
);
}

Format a string(run)

std::string s = fmt::format(
"
The answer is {}.
"
, 
42
);

//
 s == "The answer is 42."

Format a string using positional arguments(run)

std::string s = fmt::format(
"
I'd rather be {1} than {0}.
"
, 
"
right
"
, 
"
happy
"
);

//
 s == "I'd rather be happy than right."

Print dates and times(run)

#
include
 
<
fmt/chrono.h
>

int
 
main
() {
 
auto
 now = 
std::chrono::system_clock::now
();
 
fmt::print
(
"
Date and time: {}
\n
"
, now);
 
fmt::print
(
"
Time: {:%H:%M}
\n
"
, now);
}

Output:

Date and time: 2023-12-26 19:10:31.557195597
Time: 19:10

Print a container(run)

#
include
 
<
vector
>

#
include
 
<
fmt/ranges.h
>

int
 
main
() {
 std::vector<
int
> v = {
1
, 
2
, 
3
};
 
fmt::print
(
"
{}
\n
"
, v);
}

Output:

[1, 2, 3]

Check a format string at compile time

std::string s = fmt::format(
"
{:d}
"
, 
"
I am not a number
"
);

This gives a compile-time error in C++20 becausedis an invalid
format specifier for a string.

Write a file from a single thread

#
include
 
<
fmt/os.h
>

int
 
main
() {
 
auto
 out = 
fmt::output_file
(
"
guide.txt
"
);
 out.
print
(
"
Don't {}
"
, 
"
Panic
"
);
}

This can beup to 9 times faster thanfprintf.

Print with colors and text styles

#
include
 
<
fmt/color.h
>

int
 
main
() {
 
fmt::print
(
fg
(fmt::color::crimson) | fmt::emphasis::bold,
 
"
Hello, {}!
\n
"
, 
"
world
"
);
 
fmt::print
(
fg
(fmt::color::floral_white) | 
bg
(fmt::color::slate_gray) |
 fmt::emphasis::underline, 
"
Olá, {}!
\n
"
, 
"
Mundo
"
);
 
fmt::print
(
fg
(fmt::color::steel_blue) | fmt::emphasis::italic,
 
"
你好{}！
\n
"
, 
"
世界
"
);
}

Output on a modern terminal with Unicode support:

# Benchmarks

## Speed tests

Library

Method

Run Time, s

libc

printf

0.66

libc++

std::ostream

1.63

{fmt} 12.1

fmt::print

0.44

Boost Format 1.88

boost::format

3.89

Folly Format

folly::format

1.28

{fmt} is the fastest of the benchmarked methods, ~50% faster thanprintf.

The above results were generated by buildingtinyformat_test.cppon
macOS 15.6.1 withclang++ -O3 -DNDEBUG -DSPEED_TEST -DHAVE_FORMAT, and
taking the best of three runs. In the test, the format string"%0.10f:%04d:%+g:%s:%p:%c:%%\n"or equivalent is filled 2,000,000
times with output sent to/dev/null; for further details refer to thesource.

{fmt} is up to 20-30x faster thanstd::ostringstreamandsprintfon
IEEE754floatanddoubleformatting
(dtoa-benchmark) and faster
thandouble-conversionandryu:

## Compile time and code bloat

The scriptbloat-test.pyfromformat-benchmarktests compile
time and code bloat for nontrivial projects. It generates 100 translation units
and usesprintf()or its alternative five times in each to simulate a
medium-sized project. The resulting executable size and compile time (Apple
clang version 15.0.0 (clang-1500.1.0.2.5), macOS Sonoma, best of three) is shown
in the following tables.

Optimized build (-O3)

Method

Compile Time, s

Executable size, KiB

Stripped size, KiB

printf

1.6

54

50

IOStreams

28.4

98

84

{fmt} 
1122268

5.0

54

50

tinyformat

32.6

164

136

Boost Format

55.0

530

317

{fmt} is fast to compile and is comparable toprintfin terms of per-call
binary size (within a rounding error on this system).

Non-optimized build

Method

Compile Time, s

Executable size, KiB

Stripped size, KiB

printf

1.4

54

50

IOStreams

27.0

88

68

{fmt} 
1122268

4.7

87

84

tinyformat

28.1

185

145

Boost Format

38.9

678

381

libc,lib(std)c++, andlibfmtare all linked as shared libraries
to compare formatting function overhead only. Boost Format is a
header-only library so it doesn't provide any linkage options.

## Running the tests

Please refer toBuilding the
libraryfor
instructions on how to build the library and run the unit tests.

Benchmarks reside in a separate repository,format-benchmark, so to
run the benchmarks you first need to clone this repository and generate
Makefiles with CMake:

$ git clone --recursive https://github.com/fmtlib/format-benchmark.git
$ cd format-benchmark
$ cmake .

Then you can run the speed test:

$ make speed-test

or the bloat test:

$ make bloat-test

# Migrating code

clang-tidyv18 provides themodernize-use-std-printcheck that is capable of converting occurrences ofprintfandfprintftofmt::printif configured to do so. (By default it
converts tostd::print.)

# Notable projects using this library

* 0 A.D.: a free, open-source, cross-platform
real-time strategy game
* AMPL/MP: an open-source library for
mathematical programming
* Apple's FoundationDB: an open-source,
distributed, transactional key-value store
* Aseprite: animated sprite
editor & pixel art tool
* AvioBook: a comprehensive aircraft
operations suite
* Blizzard Battle.net: an online gaming
platform
* Celestia: real-time 3D visualization of
space
* Ceph: a scalable distributed storage system
* ccache: a compiler cache
* ClickHouse: an
analytical database management system
* ContextVision: medical imaging software
* Contour: a modern
terminal emulator
* CUAUV: Cornell University's autonomous
underwater vehicle
* Drake: a planning, control, and analysis
toolbox for nonlinear dynamical systems (MIT)
* Envoy: C++ L7 proxy and
communication bus (Lyft)
* FiveM: a modification framework for GTA V
* fmtlog: a performant
fmtlib-style logging library with latency in nanoseconds
* Folly: Facebook open-source
library
* GemRB: a portable open-source implementation
of Bioware's Infinity Engine
* Grand Mountain
Adventure:
a beautiful open-world ski & snowboarding game
* HarpyWar/pvpgn: Player vs
Player Gaming Network with tweaks
* KBEngine: an open-source
MMOG server engine
* Keypirinha: a semantic launcher for
Windows
* Kodi(formerly xbmc): home theater software
* Knuth: high-performance Bitcoin full-node
* libunicode: a
modern C++17 Unicode library
* MariaDB: relational database management
system
* Microsoft Verona: research
programming language for concurrent ownership
* MongoDB: distributed document database
* MongoDB Smasher: a small
tool to generate randomized datasets
* OpenSpace: an open-source
astrovisualization framework
* PenUltima Online (POL): an MMO server,
compatible with most Ultima Online clients
* PyTorch: an open-source
machine learning library
* quasardb: a distributed,
high-performance, associative database
* Quill: asynchronous low-latency
logging library
* QKW: generalizing aliasing to
simplify navigation, and execute complex multi-line terminal
command sequences
* redis-cerberus: a Redis
cluster proxy
* redpanda: a 10x faster Kafka®
replacement for mission-critical systems written in C++
* rpclib: a modern C++ msgpack-RPC server and
client library
* Salesforce Analytics
Cloud:
business intelligence software
* Scylla: a Cassandra-compatible NoSQL
data store that can handle 1 million transactions per second on a
single server
* Seastar: an advanced, open-source
C++ framework for high-performance server applications on modern
hardware
* spdlog: super fast C++ logging
library
* Stellar: financial platform
* Touch Surgery: surgery simulator
* TrinityCore:
open-source MMORPG framework
* 🐙 userver framework: open-source
asynchronous framework with a rich set of abstractions and database
drivers
* Windows Terminal: the new
Windows terminal

More...

If you are aware of other projects using this library, please let me
know byemailor by submitting anissue.

# Maintainers

The {fmt} library is maintained by Victor Zverovich
(vitaut) with contributions from many other
people. SeeContributorsandReleasesfor some of the
names. Let us know if your contribution is not listed or mentioned
incorrectly and we'll make it right.