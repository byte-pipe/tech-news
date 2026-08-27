---
title: 'GitHub - google/googletest: GoogleTest - Google Testing and Mocking Framework · GitHub'
url: https://github.com/google/googletest
site_name: github
content_file: github-github-googlegoogletest-googletest-google-testing
fetched_at: '2026-08-27T20:57:23.846348'
original_url: https://github.com/google/googletest
author: google
description: GoogleTest - Google Testing and Mocking Framework. Contribute to google/googletest development by creating an account on GitHub.
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 google

 

/

googletest

Public

* NotificationsYou must be signed in to change notification settings
* Fork10.9k
* Star39k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

4,667 Commits
4,667 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github/
ISSUE_TEMPLATE
.github/
ISSUE_TEMPLATE
 
 
ci
ci
 
 
docs
docs
 
 
googlemock
googlemock
 
 
googletest
googletest
 
 
.clang-format
.clang-format
 
 
.gitignore
.gitignore
 
 
BUILD.bazel
BUILD.bazel
 
 
CMakeLists.txt
CMakeLists.txt
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
CONTRIBUTORS
CONTRIBUTORS
 
 
LICENSE
LICENSE
 
 
MODULE.bazel
MODULE.bazel
 
 
README.md
README.md
 
 
WORKSPACE
WORKSPACE
 
 
WORKSPACE.bzlmod
WORKSPACE.bzlmod
 
 
fake_fuchsia_sdk.bzl
fake_fuchsia_sdk.bzl
 
 
googletest_deps.bzl
googletest_deps.bzl
 
 
View all files

## Repository files navigation

# GoogleTest

### Announcements

#### Documentation Updates

Our documentation is now live on GitHub Pages athttps://google.github.io/googletest/. We recommend browsing the documentation on
GitHub Pages rather than directly in the repository.

#### Release 1.18.0

Release 1.18.0is
now available.

The 1.18.x branchrequires at least C++17.

#### Continuous Integration

We use Google's internal systems for continuous integration.

#### Coming Soon

* We are planning to take a dependency onAbseil.

## Welcome toGoogleTest, Google's C++ test framework!

This repository is a merger of the formerly separate GoogleTest and GoogleMock
projects. These were so closely related that it makes sense to maintain and
release them together.

### Getting Started

See theGoogleTest User's Guidefor
documentation. We recommend starting with theGoogleTest Primer.

More information about building GoogleTest can be found atgoogletest/README.md.

## Features

* xUnit test framework:Googletest is based on thexUnittesting framework, a popular architecture for unit testing.
* Test discovery:Googletest automatically discovers and runs your tests, eliminating the need
to manually register your tests.
* Rich set of assertions:Googletest provides a variety of assertions, such as equality, inequality,
exceptions, and more, making it easy to test your code.
* User-defined assertions:You can define your own assertions with Googletest, making it simple to
write tests that are specific to your code.
* Death tests:Googletest supports death tests, which verify that your code exits in a
certain way, making it useful for testing error-handling code.
* Fatal and non-fatal failures:You can specify whether a test failure should be treated as fatal or
non-fatal with Googletest, allowing tests to continue running even if a
failure occurs.
* Value-parameterized tests:Googletest supports value-parameterized tests, which run multiple times with
different input values, making it useful for testing functions that take
different inputs.
* Type-parameterized tests:Googletest also supports type-parameterized tests, which run with different
data types, making it useful for testing functions that work with different
data types.
* Various options for running tests:Googletest provides many options for running tests including running
individual tests, running tests in a specific order and running tests in
parallel.

## Supported Platforms

GoogleTest follows Google'sFoundational C++ Support Policy.
Seethis tablefor a list of currently supported versions of compilers, platforms, and build
tools.

## Who Is Using GoogleTest?

In addition to many internal projects at Google, GoogleTest is also used by the
following notable projects:

* TheChromium projects(behind the Chrome
browser and Chrome OS).
* TheLLVMcompiler.
* Protocol Buffers, Google's data
interchange format.
* TheOpenCVcomputer vision library.

## Related Open Source Projects

GTest Runneris a Qt5 based
automated test-runner and Graphical User Interface with powerful features for
Windows and Linux platforms.

GoogleTest UIis a test runner that
runs your test binary, allows you to track its progress via a progress bar, and
displays a list of test failures. Clicking on one shows failure text. GoogleTest
UI is written in C#.

GTest TAP Listeneris an event
listener for GoogleTest that implements theTAP protocolfor test
result output. If your test runner understands TAP, you may find it useful.

gtest-parallelis a test runner that
runs tests from your binary in parallel to provide significant speed-up.

GoogleTest Adapteris a VS Code extension allowing to view GoogleTest in a tree view and run/debug
your tests.

C++ TestMateis a VS
Code extension allowing to view GoogleTest in a tree view and run/debug your
tests.

Cornichonis a small Gherkin DSL parser
that generates stub code for GoogleTest.

## Contributing Changes

Please readCONTRIBUTING.mdfor details on how to contribute to this project.

Happy testing!