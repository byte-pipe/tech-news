---
title: 'GitHub - jqlang/jq: Command-line JSON processor · GitHub'
url: https://github.com/jqlang/jq
site_name: github
content_file: github-github-jqlangjq-command-line-json-processor-github
fetched_at: '2026-04-10T11:21:46.209260'
original_url: https://github.com/jqlang/jq
author: jqlang
description: Command-line JSON processor. Contribute to jqlang/jq development by creating an account on GitHub.
---

jqlang

 

/

jq

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.8k
* Star34.1k

 
 
 
 
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

1,897 Commits
1,897 Commits
.github
.github
 
 
build
build
 
 
config
config
 
 
docs
docs
 
 
m4
m4
 
 
scripts
scripts
 
 
sig
sig
 
 
src
src
 
 
tests
tests
 
 
vendor
vendor
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
AUTHORS
AUTHORS
 
 
COPYING
COPYING
 
 
ChangeLog
ChangeLog
 
 
Dockerfile
Dockerfile
 
 
KEYS
KEYS
 
 
Makefile.am
Makefile.am
 
 
NEWS.md
NEWS.md
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
compile-ios.sh
compile-ios.sh
 
 
configure.ac
configure.ac
 
 
jq.1.prebuilt
jq.1.prebuilt
 
 
jq.spec
jq.spec
 
 
libjq.pc.in
libjq.pc.in
 
 
View all files

## Repository files navigation

# jq

jqis a lightweight and flexible command-line JSON processor akin tosed,awk,grep, and friends for JSON data. It's written in portable C and has zero runtime dependencies, allowing you to easily slice, filter, map, and transform structured data.

## Documentation

* Official Documentation:jqlang.org
* Try jq Online:play.jqlang.org

## Installation

### Prebuilt Binaries

Download the latest releases from theGitHub release page.

### Docker Image

Pull thejq imageto start quickly with Docker.

#### Run with Docker

##### Example: Extracting the version from apackage.jsonfile

docker run --rm -i ghcr.io/jqlang/jq:latest 
<
 package.json 
'
.version
'

##### Example: Extracting the version from apackage.jsonfile with a mounted volume

docker run --rm -i -v 
"
$PWD
:
$PWD
"
 -w 
"
$PWD
"
 ghcr.io/jqlang/jq:latest 
'
.version
'
 package.json

### Building from source

#### Dependencies

* libtool
* make
* automake
* autoconf

#### Instructions

git submodule update --init # if building from git to get oniguruma

autoreconf -i # if building from git

./configure --with-oniguruma=builtin

make clean # if upgrading from a version previously built from source

make -j8

make check

sudo make install

Build a statically linked version:

make LDFLAGS=-all-static

If you're not using the latest git version but instead building a released tarball (available on the release page), skip theautoreconfstep, and flex or bison won't be needed.

##### Cross-Compilation

For details on cross-compilation, check out theGitHub Actions fileand thecross-compilation wiki page.

## Community & Support

* Questions & Help:Stack Overflow (jq tag)
* Chat & Community:Join us on Discord
* Wiki & Advanced Topics:Explore the Wiki

## License

jqis released under theMIT License.jq's documentation is
licensed under theCreative Commons CC BY 3.0.jquses parts of the open source C library "decNumber", which is distributed
underICU License

## About

Command-line JSON processor

jqlang.org

### Topics

 jq

### Resources

 Readme

 

### License

 View license
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

34.1k

 stars
 

### Watchers

344

 watching
 

### Forks

1.8k

 forks
 

 Report repository

 

## Releases15

jq 1.8.1

 Latest

 

Jul 1, 2025

 

+ 14 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* C79.0%
* M46.7%
* Shell5.3%
* Yacc3.5%
* jq1.6%
* C++1.5%
* Other2.4%