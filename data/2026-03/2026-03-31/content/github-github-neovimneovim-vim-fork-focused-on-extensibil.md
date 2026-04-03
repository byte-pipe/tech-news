---
title: 'GitHub - neovim/neovim: Vim-fork focused on extensibility and usability · GitHub'
url: https://github.com/neovim/neovim
site_name: github
content_file: github-github-neovimneovim-vim-fork-focused-on-extensibil
fetched_at: '2026-03-31T11:22:15.765937'
original_url: https://github.com/neovim/neovim
author: neovim
description: Vim-fork focused on extensibility and usability. Contribute to neovim/neovim development by creating an account on GitHub.
---

neovim

 

/

neovim

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork6.7k
* Star97.7k

 
 
 
 
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

35,956 Commits
35,956 Commits
.github
.github
 
 
cmake.config
cmake.config
 
 
cmake.deps
cmake.deps
 
 
cmake.packaging
cmake.packaging
 
 
cmake
cmake
 
 
contrib
contrib
 
 
deps
deps
 
 
runtime
runtime
 
 
scripts
scripts
 
 
src
src
 
 
test
test
 
 
.cirrus.yml
.cirrus.yml
 
 
.clang-format
.clang-format
 
 
.clang-tidy
.clang-tidy
 
 
.clangd
.clangd
 
 
.editorconfig
.editorconfig
 
 
.emmyrc.json
.emmyrc.json
 
 
.git-blame-ignore-revs
.git-blame-ignore-revs
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.luacheckrc
.luacheckrc
 
 
.luacov
.luacov
 
 
.luarc.json
.luarc.json
 
 
.mailmap
.mailmap
 
 
.stylua.toml
.stylua.toml
 
 
.stylua2.toml
.stylua2.toml
 
 
.styluaignore
.styluaignore
 
 
AGENTS.md
AGENTS.md
 
 
BSDmakefile
BSDmakefile
 
 
BUILD.md
BUILD.md
 
 
CMakeLists.txt
CMakeLists.txt
 
 
CMakePresets.json
CMakePresets.json
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
INSTALL.md
INSTALL.md
 
 
LICENSE.txt
LICENSE.txt
 
 
MAINTAIN.md
MAINTAIN.md
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
build.zig
build.zig
 
 
build.zig.zon
build.zig.zon
 
 
View all files

## Repository files navigation

# Documentation|Chat

Neovim is a project that seeks to aggressively refactorVimin order to:

* Simplify maintenance and encouragecontributions
* Split the work between multiple developers
* Enableadvanced UIswithout modifications to the core
* Maximizeextensibility

See theIntroductionwiki page andRoadmapfor more information.

## Features

* ModernGUIs
* API accessfrom any language including C/C++, C#, Clojure, D, Elixir, Go, Haskell, Java/Kotlin,
JavaScript/Node.js, Julia, Lisp, Lua, Perl, Python, Racket, Ruby, Rust
* Embedded, scriptableterminal emulator
* Asynchronousjob control
* Shared data (shada)among multiple editor instances
* XDG base directoriessupport
* Compatible with most Vim plugins, including Ruby and Python plugins

See:help nvim-featuresfor the full list, and:help newsfor noteworthy changes in the latest version!

## Install from package

Pre-built packages for Windows, macOS, and Linux are found on theReleasespage.

Managed packagesare inHomebrew,Debian,Ubuntu,Fedora,Arch Linux,Void Linux,Gentoo, and more!

## Install from source

SeeBUILD.mdandsupported platformsfor details.

The build is CMake-based, but a Makefile is provided as a convenience.
After installing the dependencies, run the following command.

make CMAKE_BUILD_TYPE=RelWithDebInfo
sudo make install

To install to a non-default location:

make CMAKE_BUILD_TYPE=RelWithDebInfo CMAKE_INSTALL_PREFIX=/full/path/
make install

CMake hints for inspecting the build:

* cmake --build build --target helplists all build targets.
* build/CMakeCache.txt(orcmake -LAH build/) contains the resolved values of all CMake variables.
* build/compile_commands.jsonshows the full compiler invocations for each translation unit.

## Transitioning from Vim

See:help nvim-from-vimfor instructions.

## Project layout

├─ cmake/ CMake utils
├─ cmake.config/ CMake defines
├─ cmake.deps/ subproject to fetch and build dependencies (optional)
├─ runtime/ plugins and docs
├─ src/nvim/ application source code (see src/nvim/README.md)
│ ├─ api/ API subsystem
│ ├─ eval/ Vimscript subsystem
│ ├─ event/ event-loop subsystem
│ ├─ generators/ code generation (pre-compilation)
│ ├─ lib/ generic data structures
│ ├─ lua/ Lua subsystem
│ ├─ msgpack_rpc/ RPC subsystem
│ ├─ os/ low-level platform code
│ └─ tui/ built-in UI
└─ test/ tests (see test/README.md)

## License

Neovim contributions sinceb17d96are licensed under the
Apache 2.0 license, except for contributions copied from Vim (identified by thevim-patchtoken). SeeLICENSE.txtfor details.

## About

Vim-fork focused on extensibility and usability

neovim.io

### Topics

 c

 vim

 api

 lua

 neovim

 nvim

 text-editor

### Resources

 Readme

 

### License

 View license
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

97.7k

 stars
 

### Watchers

966

 watching
 

### Forks

6.7k

 forks
 

 Report repository

 

## Releases50

Nvim 0.12.0

 Latest

 

Mar 29, 2026

 

+ 49 releases

## Sponsor this project

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 
* opencollective.com/neovim

Learn more about GitHub Sponsors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Vim Script40.6%
* Lua31.3%
* C27.3%
* CMake0.4%
* Zig0.2%
* Shell0.1%
* Other0.1%