---
title: 'GitHub - sliverarmory/beignet: MacOS Shared Library to Shellcode Loader · GitHub'
url: https://github.com/sliverarmory/beignet
site_name: tldr
content_file: tldr-github-sliverarmorybeignet-macos-shared-library-to
fetched_at: '2026-08-07T11:44:10.277793'
original_url: https://github.com/sliverarmory/beignet
date: '2026-08-07'
description: MacOS Shared Library to Shellcode Loader. Contribute to sliverarmory/beignet development by creating an account on GitHub.
tags:
- tldr
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 sliverarmory

 

/

beignet

Public

* NotificationsYou must be signed in to change notification settings
* Fork6
* Star89

 
 
 
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

19 Commits
19 Commits
.github/
workflows
.github/
workflows
 
 
cli
cli
 
 
internal
internal
 
 
testdata
testdata
 
 
.gitignore
.gitignore
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
amd64_bootstrap.go
amd64_bootstrap.go
 
 
amd64_bootstrap_test.go
amd64_bootstrap_test.go
 
 
arm64_bootstrap.go
arm64_bootstrap.go
 
 
arm64_bootstrap_test.go
arm64_bootstrap_test.go
 
 
go.mod
go.mod
 
 
go.sum
go.sum
 
 
loader_source.go
loader_source.go
 
 
shellcode.go
shellcode.go
 
 
shellcode_test.go
shellcode_test.go
 
 
View all files

## Repository files navigation

# Beignet

Donutfor MacOS, convertsdarwin/arm64anddarwin/amd64.dylibfiles into MacOS PIC shellcode, can be used as a CLI or imported as a golang library.

### CLI

Convert a dylib to a raw shellcode buffer:

./beignet --out payload.bin ./payload.dylib

Optionally compress the staged dylib with aPLib (AP32):

./beignet --compress --out payload.bin ./payload.dylib

### Comple from Source

make

### Regenerating the embedded loader (darwin/arm64 + darwin/amd64)

go generate ./internal/stager