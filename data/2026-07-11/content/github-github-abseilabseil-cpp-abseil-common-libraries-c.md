---
title: 'GitHub - abseil/abseil-cpp: Abseil Common Libraries (C++) · GitHub'
url: https://github.com/abseil/abseil-cpp
site_name: github
content_file: github-github-abseilabseil-cpp-abseil-common-libraries-c
fetched_at: '2026-07-11T01:36:51.574758'
original_url: https://github.com/abseil/abseil-cpp
author: abseil
description: Abseil Common Libraries (C++). Contribute to abseil/abseil-cpp development by creating an account on GitHub.
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 abseil

 

/

abseil-cpp

Public

* NotificationsYou must be signed in to change notification settings
* Fork3.2k
* Star17.5k

 
 
 
 
master
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

3,476 Commits
3,476 Commits
.github
.github
 
 
CMake
CMake
 
 
absl
absl
 
 
ci
ci
 
 
.clang-format
.clang-format
 
 
.gitignore
.gitignore
 
 
ABSEIL_ISSUE_TEMPLATE.md
ABSEIL_ISSUE_TEMPLATE.md
 
 
AUTHORS
AUTHORS
 
 
BUILD.bazel
BUILD.bazel
 
 
CMakeLists.txt
CMakeLists.txt
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
FAQ.md
FAQ.md
 
 
LICENSE
LICENSE
 
 
MODULE.bazel
MODULE.bazel
 
 
PrivacyInfo.xcprivacy
PrivacyInfo.xcprivacy
 
 
README.md
README.md
 
 
UPGRADES.md
UPGRADES.md
 
 
conanfile.py
conanfile.py
 
 
create_lts.py
create_lts.py
 
 
View all files

## Repository files navigation

# Abseil - C++ Common Libraries

The repository contains the Abseil C++ library code. Abseil is an open-source
collection of C++ code (compliant to C++17) designed to augment the C++
standard library.

## Table of Contents

* About Abseil
* Quickstart
* Building Abseil
* Support
* Codemap
* Releases
* License
* Links

## About Abseil

Abseil is an open-source collection of C++ library code designed to augment
the C++ standard library. The Abseil library code is collected from Google's
own C++ code base, has been extensively tested and used in production, and
is the same code we depend on in our daily coding lives.

In some cases, Abseil provides pieces missing from the C++ standard; in
others, Abseil provides alternatives to the standard for special needs
we've found through usage in the Google code base. We denote those cases
clearly within the library code we provide you.

Abseil is not meant to be a competitor to the standard library; we've
just found that many of these utilities serve a purpose within our code
base, and we now want to provide those resources to the C++ community as
a whole.

## Quickstart

If you want to just get started, make sure you at least run through theAbseil Quickstart. The Quickstart
contains information about setting up your development environment, downloading
the Abseil code, running tests, and getting a simple binary working.

## Building Abseil

BazelandCMakeare the official
build systems for Abseil.
See thequickstartfor more information
on building Abseil using the Bazel build system.
If you require CMake support, please check theCMake build
instructionsandCMake
Quickstart.

## Support

Abseil follows Google'sFoundational C++ Support
Policy. Seethis
tablefor a list of currently supported versions compilers, platforms, and build
tools.

## Codemap

Abseil contains the following C++ library components:

* baseThebaselibrary contains initialization code and other code which
all other Abseil code depends on. Code withinbasemay not depend on any
other code (other than the C++ standard library).
* algorithmThealgorithmlibrary contains additions to the C++<algorithm>library and container-based versions of such algorithms.
* cleanupThecleanuplibrary contains the control-flow-construct-like typeabsl::Cleanupwhich is used for executing a callback on scope exit.
* containerThecontainerlibrary contains additional STL-style containers,
including Abseil's unordered "Swiss table" containers.
* crcThecrclibrary contains code for
computing error-detecting cyclic redundancy checks on data.
* debuggingThedebugginglibrary contains code useful for enabling leak
checks, and stacktrace and symbolization utilities.
* flagsTheflagslibrary contains code for handling command line flags for
libraries and binaries built with Abseil.
* hashThehashlibrary contains the hashing framework and default hash
functor implementations for hashable types in Abseil.
* logTheloglibrary containsLOGandCHECKmacros and facilities
for writing logged messages out to disk,stderr, or user-extensible
destinations.
* memoryThememorylibrary contains memory management facilities that augment
C++'s<memory>library.
* metaThemetalibrary contains type checks
similar to those available in the C++<type_traits>library.
* numericThenumericlibrary contains 128-bit integer types as well as
implementations of C++20's bitwise math functions.
* profilingTheprofilinglibrary contains utility code for profiling C++
entities. It is currently a private dependency of other Abseil libraries.
* randomTherandomlibrary contains functions for generating pseudorandom
values.
* statusThestatuslibrary contains abstractions for error handling,
specificallyabsl::Statusandabsl::StatusOr<T>.
* stringsThestringslibrary contains a variety of strings routines and
utilities.
* synchronizationThesynchronizationlibrary contains concurrency primitives (Abseil'sabsl::Mutexclass, an alternative tostd::mutex) and a variety of
synchronization abstractions.
* timeThetimelibrary contains abstractions for computing with absolute
points in time, durations of time, and formatting and parsing time within
time zones.
* typesThetypeslibrary contains non-container utility types.
* utilityTheutilitylibrary contains utility and helper code.

## Releases

Abseil recommends users "live-at-head" (update to the latest commit from the
master branch as often as possible). However, we realize this philosophy doesn't
work for every project, so we also provideLong Term Support
Releasesto which we backport
fixes for severe bugs. See ourrelease
managementdocument for more details.

## License

The Abseil C++ library is licensed under the terms of the Apache
license. SeeLICENSEfor more information.

## Links

For more information about Abseil:

* Consult ourAbseil Introduction
* ReadWhy Adopt Abseilto understand our
design philosophy.
* Peruse ourAbseil Compatibility Guaranteesto
understand both what we promise to you, and what we expect of you in return.

## About

Abseil Common Libraries (C++)

abseil.io

### Resources

 Readme

 

### License

 Apache-2.0 license
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

17.5k

 stars
 

### Watchers

676

 watching
 

### Forks

3.2k

 forks
 

 Report repository

 

## Releases47

Abseil LTS branch, May 2026

 Latest

 

Jun 1, 2026

 

+ 46 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* C++91.9%
* Starlark2.5%
* CMake2.1%
* NASL2.0%
* C0.7%
* Shell0.5%
* Other0.3%