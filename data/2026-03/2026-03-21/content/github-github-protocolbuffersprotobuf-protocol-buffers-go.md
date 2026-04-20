---
title: 'GitHub - protocolbuffers/protobuf: Protocol Buffers - Google''s data interchange format · GitHub'
url: https://github.com/protocolbuffers/protobuf
site_name: github
content_file: github-github-protocolbuffersprotobuf-protocol-buffers-go
fetched_at: '2026-03-21T11:08:53.825162'
original_url: https://github.com/protocolbuffers/protobuf
author: protocolbuffers
description: Protocol Buffers - Google's data interchange format - protocolbuffers/protobuf
---

protocolbuffers



/

protobuf

Public

* NotificationsYou must be signed in to change notification settings
* Fork16.1k
* Star70.9k




 
main
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

22,668 Commits
22,668 Commits
.bazelci
.bazelci
 
 
.bcr
.bcr
 
 
.github
.github
 
 
bazel
bazel
 
 
benchmarks
benchmarks
 
 
build_defs
build_defs
 
 
ci
ci
 
 
cmake
cmake
 
 
compatibility
compatibility
 
 
conformance
conformance
 
 
csharp
csharp
 
 
docs
docs
 
 
editions
editions
 
 
editors
editors
 
 
examples
examples
 
 
go
go
 
 
hpb
hpb
 
 
hpb_generator
hpb_generator
 
 
java
java
 
 
lua
lua
 
 
objectivec
objectivec
 
 
patches
patches
 
 
php
php
 
 
pkg
pkg
 
 
python
python
 
 
ruby
ruby
 
 
rust
rust
 
 
src
src
 
 
third_party
third_party
 
 
toolchain
toolchain
 
 
upb
upb
 
 
upb_generator
upb_generator
 
 
.bazelignore
.bazelignore
 
 
.bazeliskrc
.bazeliskrc
 
 
.bazelrc
.bazelrc
 
 
.clang-format
.clang-format
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
.readthedocs.yml
.readthedocs.yml
 
 
BUILD.bazel
BUILD.bazel
 
 
CMakeLists.txt
CMakeLists.txt
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
CONTRIBUTORS.txt
CONTRIBUTORS.txt
 
 
Disable_bundle_install.patch
Disable_bundle_install.patch
 
 
LICENSE
LICENSE
 
 
MODULE.bazel
MODULE.bazel
 
 
PrivacyInfo.xcprivacy
PrivacyInfo.xcprivacy
 
 
Protobuf.podspec
Protobuf.podspec
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
WORKSPACE
WORKSPACE
 
 
WORKSPACE.bzlmod
WORKSPACE.bzlmod
 
 
appveyor.bat
appveyor.bat
 
 
appveyor.yml
appveyor.yml
 
 
fix_permissions.sh
fix_permissions.sh
 
 
generate_descriptor_proto.sh
generate_descriptor_proto.sh
 
 
global.json
global.json
 
 
google3_export_generated_files.sh
google3_export_generated_files.sh
 
 
maven_dev_install.json
maven_dev_install.json
 
 
maven_install.json
maven_install.json
 
 
protobuf.bzl
protobuf.bzl
 
 
protobuf_deps.bzl
protobuf_deps.bzl
 
 
protobuf_release.bzl
protobuf_release.bzl
 
 
protobuf_version.bzl
protobuf_version.bzl
 
 
regenerate_stale_files.sh
regenerate_stale_files.sh
 
 
version.json
version.json
 
 
View all files

## Repository files navigation

# Protocol Buffers - Google's data interchange format

Copyright 2008 Google LLC

## Overview

Protocol Buffers (a.k.a., protobuf) are Google's language-neutral,
platform-neutral, extensible mechanism for serializing structured data. You
can learn more about it inprotobuf's documentation.

This README file contains protobuf installation instructions. To install
protobuf, you need to install the protocol compiler (used to compile .proto
files) and the protobuf runtime for your chosen programming language.

## Working With Protobuf Source Code

Most users will find working fromsupported releasesto be
the easiest path.

If you choose to work from the head revision of the main branch your build will
occasionally be broken by source-incompatible changes and insufficiently-tested
(and therefore broken) behavior.

If you are using C++ or otherwise need to build protobuf from source as a part
of your project, you should pin to a release commit on a release branch.

This is because even release branches can experience some instability in between
release commits.

### Bazel with Bzlmod

Protobuf supportsBzlmodwith Bazel 8 +.
Users should specify a dependency on protobuf in their MODULE.bazel file as
follows.

bazel_dep(name = "protobuf", version = <VERSION>)

Users can optionally override the repo name, such as for compatibility with
WORKSPACE.

bazel_dep(name = "protobuf", version = <VERSION>, repo_name = "com_google_protobuf")

### Bazel with WORKSPACE

Users can also add the following to their legacyWORKSPACEfile.

Note that with the release of 30.x there are a few more load statements to
properly set up rules_java and rules_python.

http_archive(
 name = "com_google_protobuf",
 strip_prefix = "protobuf-VERSION",
 sha256 = ...,
 url = ...,
)

load("@com_google_protobuf//:protobuf_deps.bzl", "protobuf_deps")

protobuf_deps()

load("@rules_java//java:rules_java_deps.bzl", "rules_java_dependencies")

rules_java_dependencies()

load("@rules_java//java:repositories.bzl", "rules_java_toolchains")

rules_java_toolchains()

load("@rules_python//python:repositories.bzl", "py_repositories")

py_repositories()

## Protobuf Compiler Installation

The protobuf compiler is written in C++. If you are using C++, please follow
theC++ Installation Instructionsto install protoc along
with the C++ runtime.

For non-C++ users, the simplest way to install the protocol compiler is to
download a pre-built binary from ourGitHub release page.

In the downloads section of each release, you can find pre-built binaries in
zip packages:protoc-$VERSION-$PLATFORM.zip. It contains the protoc binary
as well as a set of standard.protofiles distributed along with protobuf.

If you are looking for an old version that is not available in the release
page, check out theMaven repository.

These pre-built binaries are only provided for released versions. If you want
to use the github main version at HEAD, or you need to modify protobuf code,
or you are using C++, it's recommended to build your own protoc binary from
source.

If you would like to build protoc binary from source, see theC++ Installation Instructions.

## Protobuf Runtime Installation

Protobuf supports several different programming languages. For each programming
language, you can find instructions in the corresponding source directory about
how to install protobuf runtime for that specific language:

Language

Source

C++ (include C++ runtime and protoc)

src

Java

java

Python

python

Objective-C

objectivec

C#

csharp

Ruby

ruby

Go

protocolbuffers/protobuf-go

PHP

php

Dart

dart-lang/protobuf

JavaScript

protocolbuffers/protobuf-javascript

## Quick Start

The best way to learn how to use protobuf is to follow thetutorials in our
developer guide.

If you want to learn from code examples, take a look at the examples in theexamplesdirectory.

## Documentation

The complete documentation is available at theProtocol Buffers doc site.

## Support Policy

Read about ourversion support policyto stay current on support timeframes for the language libraries.

## Developer Community

To be alerted to upcoming changes in Protocol Buffers and connect with protobuf developers and users,join the Google Group.

## About

Protocol Buffers - Google's data interchange format

protobuf.dev

### Topics

 serialization

 protobuf

 protocol-buffers

 marshalling

 rpc

 protoc

 protocol-compiler

 protobuf-runtime

### Resources

 Readme



### License

 View license


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

70.9k

 stars


### Watchers

2k

 watching


### Forks

16.1k

 forks


 Report repository



## Releases210

Protocol Buffers v34.1

 Latest



Mar 19, 2026



+ 209 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.





## Used by965k

 + 964,732


## Contributors1,170

+ 1,156 contributors

## Languages

* C++37.5%
* C#20.0%
* Java12.0%
* C11.6%
* Objective-C7.6%
* Python3.7%
* Other7.6%
