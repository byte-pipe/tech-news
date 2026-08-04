---
title: 'GitHub - denoland/deno: A modern runtime for JavaScript and TypeScript. · GitHub'
url: https://github.com/denoland/deno
site_name: github
content_file: github-github-denolanddeno-a-modern-runtime-for-javascrip
fetched_at: '2026-08-04T11:45:55.986435'
original_url: https://github.com/denoland/deno
author: denoland
description: A modern runtime for JavaScript and TypeScript. Contribute to denoland/deno development by creating an account on GitHub.
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 denoland

 

/

deno

Public

* NotificationsYou must be signed in to change notification settings
* Fork6.3k
* Star108k

 
 
 
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

17,204 Commits
17,204 Commits
.cargo
.cargo
 
 
.claude/
skills
.claude/
skills
 
 
.devcontainer
.devcontainer
 
 
.github
.github
 
 
cli
cli
 
 
doc
doc
 
 
ext
ext
 
 
libs
libs
 
 
runtime
runtime
 
 
tests
tests
 
 
tools
tools
 
 
.dprint.json
.dprint.json
 
 
.editorconfig
.editorconfig
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
.rustfmt.toml
.rustfmt.toml
 
 
CLAUDE.md
CLAUDE.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
LICENSE.md
LICENSE.md
 
 
README.md
README.md
 
 
Releases.md
Releases.md
 
 
flake.lock
flake.lock
 
 
flake.nix
flake.nix
 
 
import_map.json
import_map.json
 
 
rust-toolchain.toml
rust-toolchain.toml
 
 
x
x
 
 
View all files

## Repository files navigation

# Deno

 

 

Deno(/ˈdiːnoʊ/, pronounceddee-no) is a JavaScript, TypeScript, and WebAssembly runtime with secure
defaults and a great developer experience. It's built onV8,Rust, andTokio.

Learn more about the Deno runtimein the documentation.

## Installation

Install the Deno runtime on your system using one of the commands below. Note
that there are a number of ways to install Deno - a comprehensive list of
installation options can be foundhere.

Shell (Mac, Linux):

curl -fsSL https://deno.land/install.sh 
|
 sh

PowerShell (Windows):

irm https:
//
deno.land
/
install.ps1 
|
 iex

Homebrew(Mac):

brew install deno

Chocolatey(Windows):

choco install deno

WinGet(Windows):

winget install 
--
id
=
DenoLand.Deno

Scoop(Windows):

scoop install main
/
deno

### Build and install from source

Complete instructions for building Deno from source can be foundhere.

## Your first Deno program

Deno can be used for many different applications, but is most commonly used to
build web servers. Create a file calledserver.tsand include the following
TypeScript code:

Deno
.
serve
(
(
_req
: 
Request
)
 
=>
 
{

 
return
 
new
 
Response
(
"Hello, world!"
)
;

}
)
;

Run your server with the following command:

deno run --allow-net server.ts

This should start a local web server onhttp://localhost:8000.

Learn more about writing and running Deno programsin the docs.

## Additional resources

* Deno Docs: official guides and reference docs for
the Deno runtime,Deno Deploy, and beyond.
* Deno Standard Library: officially supported common
utilities for Deno programs.
* JSR: The open-source package registry for modern
JavaScript and TypeScript
* Developer Blog: Product updates, tutorials, and
more from the Deno team.

## Contributing

We appreciate your help! To contribute, please read ourcontributing instructions.