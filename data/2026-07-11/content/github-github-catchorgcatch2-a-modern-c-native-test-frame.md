---
title: 'GitHub - catchorg/Catch2: A modern, C++-native, test framework for unit-tests, TDD and BDD - using C++14, C++17 and later (C++11 support is in v2.x branch, and C++03 on the Catch1.x branch) · GitHub'
url: https://github.com/catchorg/Catch2
site_name: github
content_file: github-github-catchorgcatch2-a-modern-c-native-test-frame
fetched_at: '2026-07-11T01:36:50.834338'
original_url: https://github.com/catchorg/Catch2
author: catchorg
description: A modern, C++-native, test framework for unit-tests, TDD and BDD - using C++14, C++17 and later (C++11 support is in v2.x branch, and C++03 on the Catch1.x branch) - catchorg/Catch2
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 catchorg

 

/

Catch2

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork3.4k
* Star20.6k

 
 
 
 
devel
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

4,768 Commits
4,768 Commits
.conan
.conan
 
 
.github
.github
 
 
CMake
CMake
 
 
benchmarks
benchmarks
 
 
data/
artwork
data/
artwork
 
 
docs
docs
 
 
examples
examples
 
 
extras
extras
 
 
fuzzing
fuzzing
 
 
src
src
 
 
tests
tests
 
 
third_party
third_party
 
 
tools
tools
 
 
.bazelrc
.bazelrc
 
 
.clang-format
.clang-format
 
 
.clang-tidy
.clang-tidy
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
BUILD.bazel
BUILD.bazel
 
 
CMakeLists.txt
CMakeLists.txt
 
 
CMakePresets.json
CMakePresets.json
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
Doxyfile
Doxyfile
 
 
LICENSE.txt
LICENSE.txt
 
 
MAINTAINERS.md
MAINTAINERS.md
 
 
MODULE.bazel
MODULE.bazel
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
appveyor.yml
appveyor.yml
 
 
codecov.yml
codecov.yml
 
 
conanfile.py
conanfile.py
 
 
mdsnippets.json
mdsnippets.json
 
 
meson.build
meson.build
 
 
meson_options.txt
meson_options.txt
 
 
View all files

## Repository files navigation

## What is Catch2?

Catch2 is mainly a unit testing framework for C++, but it also
provides basic micro-benchmarking features, and simple BDD macros.

Catch2's main advantage is that using it is both simple and natural.
Test names do not have to be valid identifiers, assertions look like
normal C++ boolean expressions, and sections provide a nice and local way
to share set-up and tear-down code in tests.

Example unit test

#
include
 
<
catch2/catch_test_macros.hpp
>

#
include
 
<
cstdint
>

uint32_t
 
factorial
( 
uint32_t
 number ) {
 
return
 number <= 
1
 ? number : 
factorial
(number-
1
) * number;
}

TEST_CASE
( 
"
Factorials are computed
"
, 
"
[factorial]
"
 ) {
 
REQUIRE
( 
factorial
( 
1
) == 
1
 );
 
REQUIRE
( 
factorial
( 
2
) == 
2
 );
 
REQUIRE
( 
factorial
( 
3
) == 
6
 );
 
REQUIRE
( 
factorial
(
10
) == 
3'628'800
 );
}

Example microbenchmark

#
include
 
<
catch2/catch_test_macros.hpp
>

#
include
 
<
catch2/benchmark/catch_benchmark.hpp
>

#
include
 
<
cstdint
>

uint64_t
 
fibonacci
(
uint64_t
 number) {
 
return
 number < 
2
 ? number : 
fibonacci
(number - 
1
) + 
fibonacci
(number - 
2
);
}

TEST_CASE
(
"
Benchmark Fibonacci
"
, 
"
[!benchmark]
"
) {
 
REQUIRE
(
fibonacci
(
5
) == 
5
);

 
REQUIRE
(
fibonacci
(
20
) == 
6'765
);
 
BENCHMARK
(
"
fibonacci 20
"
) {
 
return
 
fibonacci
(
20
);
 };

 
REQUIRE
(
fibonacci
(
25
) == 
75'025
);
 
BENCHMARK
(
"
fibonacci 25
"
) {
 
return
 
fibonacci
(
25
);
 };
}

Note that benchmarks are not run by default, so you need to run it explicitly
with the[!benchmark]tag.

## Catch2 v3 has been released!

You are on thedevelbranch, where the v3 version is being developed.
v3 brings a bunch of significant changes, the big one being that Catch2
is no longer a single-header library. Catch2 now behaves as a normal
library, with multiple headers and separately compiled implementation.

The documentation is slowly being updated to take these changes into
account, but this work is currently still ongoing.

For migrating from the v2 releases to v3, you should look atour
documentation. It provides a simple
guidelines on getting started, and collects most common migration
problems.

For the previous major version of Catch2look into thev2.xbranch
here on GitHub.

## How to use it

This documentation comprises these three parts:

* Why do we need yet another C++ Test Framework?
* Tutorial- getting started
* Reference section- all the details

## More

* Issues and bugs can be raised on theIssue tracker on GitHub
* For discussion or questions please useour Discord
* See who else is using Catch2 inOpen Source Softwareorcommercially.

## About

A modern, C++-native, test framework for unit-tests, TDD and BDD - using C++14, C++17 and later (C++11 support is in v2.x branch, and C++03 on the Catch1.x branch)

discord.gg/4CWS9zD

### Topics

 testing

 framework

 tdd

 cpp

 bdd

 cpp14

 test-framework

 no-dependencies

### Resources

 Readme

 

### License

 BSL-1.0 license
 

### Code of conduct

 Code of conduct
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

20.6k

 stars
 

### Watchers

500

 watching
 

### Forks

3.4k

 forks
 

 Report repository

 

## Releases110

v3.15.2

 Latest

 

Jul 7, 2026

 

+ 109 releases

## Sponsor this project

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 
* https://www.paypal.me/horenmar

Learn more about GitHub Sponsors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* C++90.1%
* CMake5.5%
* Python3.3%
* Meson0.6%
* Starlark0.3%
* Batchfile0.1%
* Other0.1%