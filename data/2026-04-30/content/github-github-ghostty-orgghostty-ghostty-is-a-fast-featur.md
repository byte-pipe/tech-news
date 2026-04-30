---
title: 'GitHub - ghostty-org/ghostty: 👻 Ghostty is a fast, feature-rich, and cross-platform terminal emulator that uses platform-native UI and GPU acceleration. · GitHub'
url: https://github.com/ghostty-org/ghostty
site_name: github
content_file: github-github-ghostty-orgghostty-ghostty-is-a-fast-featur
fetched_at: '2026-04-30T12:14:30.591847'
original_url: https://github.com/ghostty-org/ghostty
author: ghostty-org
description: 👻 Ghostty is a fast, feature-rich, and cross-platform terminal emulator that uses platform-native UI and GPU acceleration. - ghostty-org/ghostty
---

ghostty-org

 

/

ghostty

Public

* NotificationsYou must be signed in to change notification settings
* Fork2.5k
* Star52.5k

 
 
 
 
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

16,077 Commits
16,077 Commits
.agents
.agents
 
 
.github
.github
 
 
dist
dist
 
 
example
example
 
 
flatpak
flatpak
 
 
images
images
 
 
include
include
 
 
macos
macos
 
 
nix
nix
 
 
pkg
pkg
 
 
po
po
 
 
snap
snap
 
 
src
src
 
 
test
test
 
 
vendor
vendor
 
 
.clang-format
.clang-format
 
 
.editorconfig
.editorconfig
 
 
.envrc
.envrc
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
.mailmap
.mailmap
 
 
.prettierignore
.prettierignore
 
 
.shellcheckrc
.shellcheckrc
 
 
.swiftlint.yml
.swiftlint.yml
 
 
AGENTS.md
AGENTS.md
 
 
AI_POLICY.md
AI_POLICY.md
 
 
CMakeLists.txt
CMakeLists.txt
 
 
CODEOWNERS
CODEOWNERS
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Doxyfile
Doxyfile
 
 
DoxygenLayout.xml
DoxygenLayout.xml
 
 
HACKING.md
HACKING.md
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
PACKAGING.md
PACKAGING.md
 
 
README.md
README.md
 
 
build.zig
build.zig
 
 
build.zig.zon
build.zig.zon
 
 
build.zig.zon.json
build.zig.zon.json
 
 
build.zig.zon.nix
build.zig.zon.nix
 
 
build.zig.zon.txt
build.zig.zon.txt
 
 
default.nix
default.nix
 
 
flake.lock
flake.lock
 
 
flake.nix
flake.nix
 
 
shell.nix
shell.nix
 
 
test_align
test_align
 
 
typos.toml
typos.toml
 
 
valgrind.supp
valgrind.supp
 
 
View all files

## Repository files navigation

# Ghostty

Fast, native, feature-rich terminal emulator pushing modern features.A native GUI or embeddable library vialibghostty.About·Download·Documentation·Contributing·Developing

## About

Ghostty is a terminal emulator that differentiates itself by being
fast, feature-rich, and native. While there are many excellent terminal
emulators available, they all force you to choose between speed,
features, or native UIs. Ghostty provides all three.

libghosttyis a cross-platform, zero-dependency C and Zig library
for building terminal emulators or utilizing terminal functionality
(such as style parsing). Anyone can uselibghosttyto build a terminal
emulator or embed a terminal into their own applications. SeeGhostlingfor a minimal complete project
example or theexamplesdirectoryfor smaller examples of usinglibghosttyin C and Zig.

For more details, seeAbout Ghostty.

## Download

See thedownload pageon the Ghostty website.

## Documentation

See thedocumentationon the Ghostty website.

## Contributing and Developing

If you have any ideas, issues, etc. regarding Ghostty, or would like to
contribute to Ghostty through pull requests, please check out our"Contributing to Ghostty"document. Those who would like
to get involved with Ghostty's development as well should also read the"Developing Ghostty"document for more technical details.

## Roadmap and Status

Ghostty is stable and in use by millions of people and machines daily.

The high-level ambitious plan for the project, in order:

#

Step

Status

1

Standards-compliant terminal emulation

✅

2

Competitive performance

✅

3

Rich windowing features -- multi-window, tabbing, panes

✅

4

Native Platform Experiences

✅

5

Cross-platform 
libghostty
 for Embeddable Terminals

✅

6

Ghostty-only Terminal Control Sequences

❌

Additional details for each step in the big roadmap below:

#### Standards-Compliant Terminal Emulation

Ghostty implements all of the regularly used control sequences and
can run every mainstream terminal program without issue. For legacy sequences,
we've done acomprehensive xterm auditcomparing Ghostty's behavior to xterm and building a set of conformance
test cases.

In addition to legacy sequences (what you'd call real "terminal" emulation),
Ghostty also supports more modern sequences than almost any other terminal
emulator. These features include things like the Kitty graphics protocol,
Kitty image protocol, clipboard sequences, synchronized rendering,
light/dark mode notifications, and many, many more.

We believe Ghostty is one of the most compliant and feature-rich terminal
emulators available.

Terminal behavior is partially a de jure standard
(i.e.ECMA-48)
but mostly a de facto standard as defined by popular terminal emulators
worldwide. Ghostty takes the approach that our behavior is defined by
(1) standards, if available, (2) xterm, if the feature exists, (3)
other popular terminals, in that order. This defines what the Ghostty project
views as a "standard."

#### Competitive Performance

Ghostty is generally in the same performance category as the other highest
performing terminal emulators.

"The same performance category" means that Ghostty is much faster than
traditional or "slow" terminals and is within an unnoticeable margin of the
well-known "fast" terminals. For example, Ghostty and Alacritty are usually within
a few percentage points of each other on various benchmarks, but are both
something like 100x faster than Terminal.app and iTerm. However, Ghostty
is much more feature rich than Alacritty and has a much more native app
experience.

This performance is achieved through high-level architectural decisions and
low-level optimizations. At a high-level, Ghostty has a multi-threaded
architecture with a dedicated read thread, write thread, and render thread
per terminal. Our renderer uses OpenGL on Linux and Metal on macOS.
Our read thread has a heavily optimized terminal parser that leverages
CPU-specific SIMD instructions. Etc.

#### Rich Windowing Features

The Mac and Linux (build with GTK) apps support multi-window, tabbing, and
splits with additional features such as tab renaming, coloring, etc. These
features allow for a higher degree of organization and customization than
single-window terminals.

#### Native Platform Experiences

Ghostty is a cross-platform terminal emulator but we don't aim for a
least-common-denominator experience. There is a large, shared core written
in Zig but we do a lot of platform-native things:

* The macOS app is a true SwiftUI-based application with all the things you
would expect such as real windowing, menu bars, a settings GUI, etc.
* macOS uses a true Metal renderer with CoreText for font discovery.
* macOS supports AppleScript, Apple Shortcuts (AppIntents), etc.
* The Linux app is built with GTK.
* The Linux app integrates deeply with systemd if available for things
like always-on, new windows in a single instance, cgroup isolation, etc.

Our goal with Ghostty is for users of whatever platform they run Ghostty
on to think that Ghostty was built for their platform first and maybe even
exclusively. We want Ghostty to feel like a native app on every platform,
for the best definition of "native" on each platform.

#### Cross-platformlibghosttyfor Embeddable Terminals

In addition to being a standalone terminal emulator, Ghostty is a
C-compatible library for embedding a fast, feature-rich terminal emulator
in any 3rd party project. This library is calledlibghostty.

Due to the scope of this project, we're breaking libghostty down into
separate libraries, starting withlibghostty-vt. The goal of
this project is to focus on parsing terminal sequences and maintaining
terminal state. This is covered in more detail in thisblog post.

libghostty-vtis already available and usable today for Zig and C and
is compatible for macOS, Linux, Windows, and WebAssembly. The functionality
is extremely stable (since its been proven in Ghostty GUI for a long time),
but the API signatures are still in flux.

libghosttyis already heavily in use. Seeexamplesfor small examples of usinglibghosttyin C and Zig or theGhostlingproject for a
complete example. Seeawesome-libghosttyfor a list of projects and resources related tolibghostty.

We haven't tagged libghostty with a version yet and we're still working
on a better docs experience, but ourDoxygen websiteis a good resource for the C API.

#### Ghostty-only Terminal Control Sequences

We want and believe that terminal applications can and should be able
to do so much more. We've worked hard to support a wide variety of modern
sequences created by other terminal emulators towards this end, but we also
want to fill the gaps by creating our own sequences.

We've been hesitant to do this up until now because we don't want to create
more fragmentation in the terminal ecosystem by creating sequences that only
work in Ghostty. But, we do want to balance that with the desire to push the
terminal forward with stagnant standards and the slow pace of change in the
terminal ecosystem.

We haven't done any of this yet.

## Crash Reports

Ghostty has a built-in crash reporter that will generate and save crash
reports to disk. The crash reports are saved to the$XDG_STATE_HOME/ghostty/crashdirectory. If$XDG_STATE_HOMEis not set, the default is~/.local/state.Crash reports arenotautomatically sent anywhere off your machine.

Crash reports are only generated the next time Ghostty is started after a
crash. If Ghostty crashes and you want to generate a crash report, you must
restart Ghostty at least once. You should see a message in the log that a
crash report was generated.

Note

Use theghostty +crash-reportCLI command to get a list of available crash
reports. A future version of Ghostty will make the contents of the crash
reports more easily viewable through the CLI and GUI.

Crash reports end in the.ghosttycrashextension. The crash reports are inSentry envelope format. You can
upload these to your own Sentry account to view their contents, but the format
is also publicly documented so any other available tools can also be used.
Theghostty +crash-reportCLI command can be used to list any crash reports.
A future version of Ghostty will show you the contents of the crash report
directly in the terminal.

To send the crash report to the Ghostty project, you can use the following
CLI command using theSentry CLI:

SENTRY_DSN=https://e914ee84fd895c4fe324afa3e53dac76@o4507352570920960.ingest.us.sentry.io/4507850923638784 sentry-cli send-envelope --raw <path to ghostty crash>

Warning

The crash report can contain sensitive information. The report doesn't
purposely contain sensitive information, but it does contain the full
stack memory of each thread at the time of the crash. This information
is used to rebuild the stack trace but can also contain sensitive data
depending on when the crash occurred.

## About

👻 Ghostty is a fast, feature-rich, and cross-platform terminal emulator that uses platform-native UI and GPU acceleration.

ghostty.org

### Resources

 Readme

 

### License

 MIT license
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

52.5k

 stars
 

### Watchers

197

 watching
 

### Forks

2.5k

 forks
 

 Report repository

 

## Releases

13

tags

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Zig78.7%
* Swift11.6%
* C4.2%
* C++2.9%
* Shell0.6%
* HTML0.6%
* Other1.4%