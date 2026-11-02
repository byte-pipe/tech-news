---
title: 'GitHub - ivankovic/omnidiff: Fast, robust, accurate diffing · GitHub'
url: https://github.com/ivankovic/omnidiff
site_name: hackernews_api
content_file: hackernews_api-github-ivankovicomnidiff-fast-robust-accurate-diff
fetched_at: '2026-11-03T06:07:29.131055'
original_url: https://github.com/ivankovic/omnidiff
author: FabCH
date: '2026-11-02'
description: Fast, robust, accurate diffing . Contribute to ivankovic/omnidiff development by creating an account on GitHub.
tags:
- hackernews
- trending
---

main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

1,528 Commits
1,528 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.githooks
.githooks
 
 
.github
.github
 
 
assets
assets
 
 
packaging
packaging
 
 
research
research
 
 
scripts
scripts
 
 
src
src
 
 
tests
tests
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
LICENSE
LICENSE
 
 
LICENSE-COMMERCIAL
LICENSE-COMMERCIAL
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
REVIEW.md
REVIEW.md
 
 
THIRD-PARTY-NOTICES.md
THIRD-PARTY-NOTICES.md
 
 
flake.lock
flake.lock
 
 
flake.nix
flake.nix
 
 
list_of_repositories.csv
list_of_repositories.csv
 
 
list_of_repositories_100.csv
list_of_repositories_100.csv
 
 
list_of_repositories_tiny.csv
list_of_repositories_tiny.csv
 
 
ruff.toml
ruff.toml
 
 
View all files

## Repository files navigation

# OmniDiff

Fast, robust, accurate content-aware diffing.

* Robust:can diff 99.95% of code changes
* Content-aware:98.8% of changes diffed using content-specific algorithms

Content

Fast: under 100ms

Accurate: perfect

Accurate: near-perfect

Code

98%

70%

92%

Pictures

96%

69%

91%

Cursors

100%

85%

100%

Fonts

95%

82%

100%

Archives

88%

87%

87%

Message catalogs

100%

83%

83%

PDFs

57%

100%

100%

Speed measured on a T14s, Intel Core i7-1370P with 32 GB RAM (seeFast). PDFs
have fewer than ten judged test cases (seeAccurate).

See it in the browser: twenty real code
changes, recorded from the command-line tool and compared side by side in Unixdiffand in
OmniDiff, andcontent examples: an
OpenDocument file, a compiled translation catalog, and pictures, still and animated.

Various light and dark themes are available:

Files are diffed based on type. A PDF diagram with one box renamed, and a web font with twenty
icons redrawn:

# Installation

## From source

cargo install --locked omnidiff

This command builds OmniDiff from source, with the dependency versions it was tested with. You
need a C compiler onPATHand a Rust toolchain, rustc 1.92 or later. The build compiles every tree-sitter grammar from C.
The firstcargo installtakes a few minutes, because of this and thelto = "fat"release
profile.

## Prebuilt binaries

Prebuilt binaries for Linux, macOS (Intel and Apple Silicon), and Windows are attached to everyGitHub release.

## Homebrew

macOS and Linux:

brew install ivankovic/omnidiff/omnidiff

## Debian and Ubuntu

.debpackages for amd64 and arm64 are available in a signed apt repository:

sudo install -d -m 0755 /etc/apt/keyrings
curl -fsSL https://ivankovic.github.io/omnidiff/apt/omnidiff-archive-keyring.gpg \
 
|
 sudo tee /etc/apt/keyrings/omnidiff-archive-keyring.gpg 
>
 /dev/null

echo
 
"
deb [signed-by=/etc/apt/keyrings/omnidiff-archive-keyring.gpg] 
\

https://ivankovic.github.io/omnidiff/apt stable main
"
 \
 
|
 sudo tee /etc/apt/sources.list.d/omnidiff.list 
>
 /dev/null
sudo apt update 
&&
 sudo apt install omnidiff

## Nix and NixOS

On NixOS, or anywhere with Nix installed:

nix run github:ivankovic/omnidiff

If flakes are not enabled in your Nix configuration, add--extra-experimental-features 'nix-command flakes'afternix.

## Arch and Gentoo

Recipes for Arch and Gentoo live inpackaging/: the PKGBUILD builds locally withmakepkg -si, and the Gentoo ebuild is ready for an overlay. The two distros are overwhelmed and
their repositories open and close to new packages sporadically.

## Editor integration

VS Code does not yet let an extension replace its built-in diff view. The API is implemented
upstream but unreleased; the extension will adopt it when it ships.

* VS Code-omnidiff-vscode. Search forOmniDiffin the Extensions view, orcode --install-extension ivankovic.omnidiff. Also onOpen VSXfor VSCodium, Cursor and Windsurf.
* Neovim-omnidiff.nvim.

# Using OmniDiff

## The interactive TUI

omnidiff # open an empty viewer; press o to pick each file
omnidiff BEFORE AFTER # open directly into the diff of two files

Press?in the viewer for the full list of keybindings.

The TUI uses 24-bit color when the terminal advertises it withCOLORTERM=truecolor, and the
nearest 256 colors otherwise (macOS Terminal.app, or most terminals over ssh, which does not
forwardCOLORTERM). If your terminal supports 24-bit color but does not advertise it, runexport COLORTERM=truecolor.

## In a browser

For reviewing changes in a browser, seecodereview.

Note: codereview is at v0.0.0; use it at your own risk.

## Headless / batch mode

omnidiff --headless BEFORE AFTER, or its synonym--batch, prints the diff as plain text, with
optional color, instead of opening the TUI. Use this for scripts or CI. Headless mode also starts
automatically whenever stdout is not a terminal, for example when piped intolessor redirected to
a file. Because of this,omnidiff BEFORE AFTER | lessworks without the flag.

OmniDiff collapses long runs of unchanged lines. It keeps 3 lines of context on each side of a
change (override with--context N), the same convention asdiff -u. OmniDiff also prefixes each
hunk with the nearest enclosing function, class, or struct line, when that line is not otherwise
visible. This shows the location of a change deep inside a large file.

Colors are on by default; pass--color never, or setNO_COLOR=1, to disable ANSI colors, for
example when you redirect output to a file ---color alwaysforces them even underNO_COLOR.

OmniDiff exits0on success and2on error. For scripting, pass--exit-codeto additionally
get1when the files differ. This follows thediff(1)convention.--exit-codeis opt-in rather
than the default for the same reasongit diffexits0even when files differ: OmniDiff's usual
non-interactive callers are version control systems driving it as a display tool, and they read a
non-zero exit as "the tool failed" -jjwarns on every file, andgit difftoolwithdifftool.trustExitCode=trueaborts the whole diff. (The 7-argumentGIT_EXTERNAL_DIFFform stays
at0even with--exit-code, since git treats a non-zero exit there as fatal.)

## JSON output

omnidiff --mode json BEFORE AFTERprints the diff as one JSON object. Its fields are described
insrc/tui/json_output.schema.json, a JSON Schema.

## Git integration

OmniDiff is agit difftoolbackend. Run the interactive setup wizard, which asks
whether to configure it globally or for the current repository only:

omnidiff git configure

### Configure by hand

git config difftool.omnidiff.cmd 'omnidiff "$LOCAL" "$REMOTE"'
git difftool --tool=omnidiff

Rungit config diff.tool omnidiffto make plaingit difftooluse OmniDiff by default, without
needing--tool. If you do not want git to ask "view diff ... [Y/n]?" before every file, rungit config difftool.prompt false.

### Usage

git difftoolopens the interactive TUI.git diffandgit log -pnever do.git diffpipes its output through git's pager, and a full-screen TUI cannot draw onto a pipe, so OmniDiff
always falls back to plain text there regardless of terminal orGIT_EXTERNAL_DIFFconfig (see
"Headless / batch mode" above). If you want the interactive viewer from git, usegit difftool,
notgit diff. Ifgit difftoolstill doesn't open interactively over SSH, reconnect withssh -t— the session needs an allocated pseudo-terminal; tmux panes always have one.

OmniDiff also works directly withgit diffandgit log -p, throughGIT_EXTERNAL_DIFF. This
path needs nodifftoolconfig:

GIT_EXTERNAL_DIFF=omnidiff git diff

Pictures, archives, fonts and the rest of thesupported contentget a short
report of what changed in them. Any other binary file gets a one-lineBinary file <path> differsnotice instead of a diff, the same stand-in git anddiff(1)print for them. Neither ever blocks
the rest of agit diff: an external diff that exits non-zero makes git abandon theentirerun,
so OmniDiff reports an unshowable file as a successful diff of nothing rather than as a failure.

## Jujutsu (jj) integration

jj does not read git'sdifftool/diff.externalsettings, even in a colocated repo, so it needs
its own configuration. Run the setup wizard:

omnidiff jj configure

### Configure by hand

jj config set --user merge-tools.omnidiff.program omnidiff
jj config set --user merge-tools.omnidiff.diff-args '["$left","$right"]'
jj config set --user merge-tools.omnidiff.diff-invocation-mode file-by-file

That registersjj diff --tool omnidiff. To make it the default for plainjj diffas well:

jj config set --user ui.diff-formatter omnidiff

Use--repoin place of--userto configure the current repository only.

diff-invocation-mode = "file-by-file"is required.jj's default hands a diff tool twodirectorytrees; OmniDiff diffs two files, so without this setting every invocation fails. With
it, jj passes one changed file pair at a time, keeping each file's real path and extension, so
language detection works exactly as it does under git.

### Usage

jj diffruns its formatter under a pager, so OmniDiff renders in its non-interactive text mode
there - the same outputgit diffgets. jj has no equivalent ofgit difftool's interactive
per-file viewer (its terminal-attached hook,ui.diff-editor, is forjj diffedit/jj split,
which edit the right-hand side and read it back - not something a read-only viewer should claim to
do), so for the full-screen TUI on a jj repo, runomnidiff BEFORE AFTERdirectly.

# Supported content

The language is detected from the file extension. A file with an unknown extension is diffed as
plain text, line by line, so nothing is refused.

25 languages are parsed with a tree-sitter grammar and diffed structurally:

Language

File extensions

C

.c
, 
.h

C#

.cs

C++

.cc
, 
.cpp
, 
.cxx
, 
.hpp
, 
.hh
, 
.hxx

CSS

.css
, 
.scss

Go

.go

HTML

.html
, 
.htm

Java

.java

JavaScript

.js
, 
.mjs
, 
.cjs
, 
.jsx

JSON

.json

Kotlin

.kt

Lua

.lua

Perl

.pl
, 
.pm

PHP

.php

Python

.py
, 
.pyi
, 
.pyw

R

.r

Ruby

.rb

Rust

.rs

Scala

.scala

Shell (Bash)

.bash
, 
.sh

Swift

.swift

TSX

.tsx

TypeScript

.ts
, 
.mts
, 
.cts

Vimscript

.vim

XML

.xml
, 
.xht
, 
.xhtml
, 
.svg
, 
.glif
, 
.plist
, 
.ui
, 
.qrc
, 
.glade
, 
.xib
, 
.storyboard
, 
.xaml
, 
.vcxproj
, 
.filters
, 
.csproj
, 
.fsproj
, 
.vbproj
, 
.props
, 
.targets
, 
.nuspec
, 
.resx
, 
.wxs
, 
.iml
, 
.manifest
, 
.config
, 
.policy
, 
.xsd
, 
.xsl
, 
.xslt
, 
.xlf
, 
.xliff
, 
.kml
, 
.gpx
, 
.rss
, 
.atom
, 
.graphml
, 
.dae

YAML

.yaml
, 
.yml

Recognised by extension but diffed as plain text, since no grammar is compiled in: Bazel (.bazel), Dart (.dart), Emacs Lisp (.el), Markdown (.md,.markdown), Protocol Buffers (.proto), SQL (.sql).

Files that are not text are recognised by their bytes, never by their names, and diffed by what
they hold:

Content

Formats

Diffed

Pictures

PNG, JPEG, GIF, WebP, BMP, ICO, TIFF

pixel by pixel, as the eye compares them: how much changed and where; animations frame by frame

Archives

zip (and so jar, Office documents, EPUB), tar, gzip, xz, bzip2

file by file, each by what it is, archives inside archives included; Java class files as a listing of their fields and methods

Fonts

TrueType, OpenType, WOFF, WOFF2, EOT

glyph by glyph, each drawn, and the font's names and metrics

Cursors

Windows 
.cur
 and 
.ani
, X cursors, Hyprland 
.hlc

size by size and frame by frame

Message catalogs

gettext 
.mo
, Qt 
.qm

message by message

Documents

PDF

page by page, each page drawn

Text in other encodings

UTF-16 and UTF-32 with a byte order mark

as text, like any other file

Only the members that changed are opened, so a font with two edited glyphs shows two glyphs. Each
change is also named by how much of it a reader would see: invisible (only the bytes differ),
imperceptible, artifacts (what compression or resampling leaves behind), edited, redrawn or
replaced - for text, whitespace, formatting and rewritten stand in for the second, third and
fifth.

The TUI shows pictures as pictures: in the terminal's own graphics where it speaks the kitty,
sixel or iTerm2 protocol, and in Unicode half blocks everywhere else.bswitches to half blocks
and back, andOMNIDIFF_GRAPHICS=halfblocks(orkitty,sixel,iterm2) overrides the
detection; inside tmux, the terminal in front of the pane decides. An archive, a font or any other
container lists its changed members beside the one selected,gshows every changed glyph or
picture at once, andEnteropens a text member in the full diff view.

Anything else binary gets the one-lineBinary file <path> differsnotice.

# License

Copyright (C) 2026 Marko Ivankovic

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, version 3 of the License.

See the LICENSE file for the full text of the License.

## Cannot use AGPL software?

A commercial license is available as a monthly subscription throughGitHub Sponsors. It covers internal use of omnidiff
by your organisation without the source-disclosure obligations of the AGPL. The terms are inLICENSE-COMMERCIAL. Pick the tier that names the commercial license as a
benefit. For invoicing or other arrangements, contact me atmarko@ivankovic.me.

# Guiding principles

## Fast

OmniDiff's goal is:

* A median diff in 100ms or less.
* A 99th-percentile diff in 1000ms or less.

Both are met. Over the 2,302 fixtures insrc/test/data/diffs/, measured 2026-10-31 on a laptop,
an Intel Core i7-1370P (6 performance and 8 efficiency cores, 20 threads) with 32 GB RAM:p50
4.2ms, p90 35.1ms, p99 177ms, slowest 482ms.100ms is the 97.6th percentile— 55 fixtures
take longer than that, and none takes longer than a second.

Times belong to the machine that measured them, so each machine keeps its own (seeresearch/data/machines.csv): the Intel Xeon E3-1275 v5 server that measured the research
figures takes about 2.5 times as long per fixture. Runtime is reported, never gated:make check-qualityprints this distribution against the machine's own committed baseline on every
push, and warns when the runtime is more than twice the baseline's.

Other content is timed over pairs sampled from the same corpus, decoding included - unpacking an
archive, drawing a font's glyphs or a PDF's pages - measured 2026-10-17 on the same laptop:

Content

Pairs

p50

p90

p99

Under 100ms

Pictures

230

1.8ms

41ms

526ms

96.1%

Cursors

22

0.6ms

1.3ms

15ms

100%

Fonts

100

6.4ms

57ms

826ms

95%

Archives

100

2.6ms

156ms

1,938ms

88%

Message catalogs

81

0.4ms

1.9ms

4.7ms

100%

PDFs

100

69ms

310ms

985ms

57%

Archives miss the 99th-percentile goal: the slowest hold thousands of changed members. PDFs meet
both goals, but only 57% of them take under 100ms, since a PDF draws every changed page.make benchmark-contentmeasures this and writesresearch/data/performance/content_speed/<machine>.csv.

## Robust

OmniDiff's goal is to process 100% of all commits.

The full test dataset holds the git commit history of about 7,500 open-source git repositories,
as available on the main branch. This list of repositories comes from the Gentoo Linux
distribution. Find it inlist_of_repositories.csv.

Measured over every modified code file in the most recent 50 commits of each of those
repositories - 442,530 readable before/after pairs in 25 languages, diffed with no size cap under
a 120-second budget and a 6 GB memory cap per process -442,322 (99.95%) completed
successfully.96 pairs ran past the budget and 112 past the memory cap; the latter are twenty
files, nineteen of them generated or embedded - tree-sitter parser tables, codegen, minified
bundles, a PNG as a C array - and one commit of a 40,000-line single-header C++ library. Given
24 GB and 300 s, 11 of the 28 files that first hit the cap complete. The run, its harness and every pair that did not complete are documented inresearch/data/performance/PROVENANCE.md.

Beyond code, over every file changed in the same window - 2,018,010 changes in 7,352
repositories, pictures, fonts and archives included -98.8% are diffed as text or by their
content(98.2% counting each repository at most 1,000 times, so that a few giant ones do not
decide it; 6,481 repositories entirely). What is left is mostly text in legacy encodings, compiled
objects, audio, and EOT fonts compressed with MicroType Express. The census is documented inresearch/data/corpus_stats/PROVENANCE.md.

## Accurate

OmniDiff must match a human's own reading of a change, measured against the hand-authored
ground-truth mappings insrc/test/data/diffs/:

* 90% of test cases with zero mismatched bytes.
* 99% of test cases with at most 1% of bytes mismatched.

Neither is met yet. 1,419 of the 2,302 fixtures carry a hand-painted ground truth - every byte of
both files labelled with what a human says happened to it - and OmniDiff's own highlighting is
compared against it byte by byte, under each of its two highlighting presets (--full, which keeps
brackets, separators and leading whitespace, and--minimal, which drops them):

preset

zero mismatched bytes

at most 1% mismatched

mismatched bytes, whole corpus

--full

851 (60.0%)

1,241 (87.5%)

99,157 of 73.3M (0.14%)

--minimal

987 (69.6%)

1,299 (91.5%)

51,740 of 73.3M (0.07%)

The whole-corpus rate is far below 1% because most of each file is unchanged and nobody gets that
wrong; the per-test-case numbers are the ones that count, since a reader meets the mistakes one
diff at a time. Most of what is left is not in the matching: rendering the human's own node
mapping still disagrees with the painting on 91% of the--fullbytes and 91% of the--minimalones, so the highlighting rules own the gap more than the matcher does.

make update-painting-attributionmeasures this and writes one row per fixture and preset toresearch/data/quality/painting_attribution.csv, which the table is counted from;make check-painting-attributionfails if any fixture gets worse.

Other content is judged rather than painted: a human names how much each change is (invisible,
imperceptible, artifacts, edited, redrawn or replaced, seesupported content)
and OmniDiff's verdict is compared with theirs. A test case is perfect when every verdict matches,
and near-perfect when every one is at most one level off:

Content

Judged

Perfect

Near-perfect

Pictures

130

90 (69%)

118 (91%)

Cursors

13

11 (85%)

13 (100%)

Fonts

11

9 (82%)

11 (100%)

Archives

23

20 (87%)

20 (87%)

Message catalogs

12

10 (83%)

10 (83%)

PDFs

4

4 (100%)

4 (100%)

make benchmark-contentcounts these too.

# AI policy

This project uses substantial AI assistance, currently Claude Code. Most commits disclose this
with aCo-Authored-Bytrailer and a link to the session that produced them. This project does not
hide that fact. This project does not treat AI assistance as a lesser way to write software.

Contributions are not accepted at this time, to keep the development speed high (seeCONTRIBUTING.md). When that changes, AI-assisted contributions will be as
welcome as any other, disclosed the same way: whoever submits the work is responsible for
understanding it and standing behind it.

# For Developers, human or otherwise

SeeCONTRIBUTING.mdfor the technology overview, code-quality and testing
expectations, project structure, and what CI checks on every push and PR.AGENTS.mdhas
additional AI-agent-specific conventions.