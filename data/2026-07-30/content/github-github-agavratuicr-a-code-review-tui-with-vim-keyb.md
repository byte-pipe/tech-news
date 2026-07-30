---
title: 'GitHub - agavra/tuicr: a code review TUI with vim keybindings · GitHub'
url: https://github.com/agavra/tuicr
site_name: github
content_file: github-github-agavratuicr-a-code-review-tui-with-vim-keyb
fetched_at: '2026-07-30T11:39:28.149274'
original_url: https://github.com/agavra/tuicr
author: agavra
description: a code review TUI with vim keybindings. Contribute to agavra/tuicr development by creating an account on GitHub.
---

agavra

 

/

tuicr

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork151
* Star1.7k

 
 
 
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

348 Commits
348 Commits
.github
.github
 
 
docs
docs
 
 
examples
examples
 
 
public
public
 
 
scripts/
demo
scripts/
demo
 
 
skills/
tuicr
skills/
tuicr
 
 
src
src
 
 
tests/
fixtures/
pr_refresh
tests/
fixtures/
pr_refresh
 
 
.gitignore
.gitignore
 
 
.tuicrignore
.tuicrignore
 
 
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
 
 
PLAN.md
PLAN.md
 
 
README.md
README.md
 
 
RELEASE.md
RELEASE.md
 
 
cliff.toml
cliff.toml
 
 
flake.lock
flake.lock
 
 
flake.nix
flake.nix
 
 
View all files

## Repository files navigation

# tuicr

A code review TUI with vim keybindings. Export to GitHub, GitLab, or clipboard.

Tip

Pronounced "tweaker".

## What it does

* GitHub-style continuous diff in the terminal. Scroll through every changed file in one stream.
* PR-style comments at the line, range, file, and review level.
* Review tracking at file or hunk granularity, persisted across sessions.
* Three export targets: push a real review to GitHub or GitLab, copy structured markdown to your
clipboard, or pipe to stdout.
* Works with git, jj, and mercurial. Reviews uncommitted changes, commit ranges, or any GitHub PR
or GitLab MR.

## Install

curl -fsSL tuicr.dev/install.sh 
|
 sh

#
 or

brew install agavra/tap/tuicr

Other install methods (cargo, mise, nix, binaries, source)

#
 Cargo

cargo install tuicr

#
 Mise

mise use github:agavra/tuicr

#
 Nix

nix run github:agavra/tuicr

Pre-built binaries:GitHub Releases

From source:

git clone https://github.com/agavra/tuicr.git

cd
 tuicr
cargo install --path 
.

Update the active installation with one command:

tuicr update
tuicr update 0.18.0 
#
 Install a known-good version

tuicr updateuses Homebrew, Cargo, Mise, or a Nix profile when that manager owns the
executable. Install-script and manually downloaded binaries update in place from the matching
GitHub release asset after SHA-256 verification. Exact-version installs support Cargo and direct
binaries; use the package manager's pinning workflow for Homebrew, Mise, or Nix. Anix runinvocation is temporary rather than installed; rerun it to use the current flake, or usenix profile install github:agavra/tuicrfor an installation thattuicr updatecan upgrade.

## Quick start

tuicr 
#
 Pick from a commit selector

tuicr tui 
#
 Same TUI, explicit subcommand

tuicr -w 
#
 Uncommitted changes (skip selector)

tuicr -r main..HEAD 
#
 Commit range

tuicr pr 125 
#
 GitHub PR

tuicr mr 125 
#
 GitLab MR

tuicr tui pr 125 
#
 GitHub PR via explicit TUI subcommand

tuicr tui mr 125 
#
 GitLab MR via explicit TUI subcommand

tuicr --stdout 
#
 Pipe the review to stdout

tuicr review list 
#
 List saved local review sessions

tuicr update 
#
 Update the active installation

tuicr update 0.18.0 
#
 Install a known-good version

Inside tuicr, navigate withj/k, presscto comment, thenyto copy the review or:submitto push it to GitHub or GitLab. When opening a GitHub PR or GitLab MR you've reviewed
before, tuicr preselects commits newer than your latest submitted review when that metadata is
available; commits already covered by that review are marked with✓in the inline selector.
Auto-detects git, jj, or mercurial.

## How it compares

tuicr

hunk

lumen

gh pr review

git diff

TUI diff viewer

✅

✅

✅

❌

❌

Write comments in the TUI

✅

✅

✅

❌

❌

Vim keybindings

✅

❌

partial¹

❌

❌

Push inline review to GitHub

✅

❌

❌

partial²

❌

Push inline review to GitLab

✅

❌

❌

❌

❌

Agent-ready markdown export

✅

via CLI skill

❌

❌

❌

git

✅

✅

✅

❌

✅

jj

✅

✅

✅

❌

❌

Mercurial (hg)

✅

❌

❌

❌

❌

Single static binary

✅

(needs Node)

✅

✅

✅

¹ Lumen hasj/knavigation but no broader vim model (visual mode,{N}G,Ctrl-d/Ctrl-u,
etc.).

²gh pr reviewposts approve/comment/request-changes at the review level only. No inline line
comments.

## Export your review

When you're done reviewing, send your comments wherever the work continues.

### To GitHub

:submitopens a picker for Comment, Approve, Request changes, or Draft. Inline comments land
on the right lines as a real PR review. Review-level comments become the review summary.
Requiresghauthenticated to the repo.

### To GitLab

:submitoffers Comment, Approve, or Request changes on a GitLab MR. Inline comments post as
discussion notes. Review-level comments become the summary. Requiresglabauthenticated to the
host. Request changes needs your account to be an assigned reviewer. Only Draft is GitHub-only
here. Seedocs/GITLAB.mdfor setup, self-hosted instances, and troubleshooting.

### To your coding agent

yor:clipcopies a structured markdown block to your clipboard. Each comment has a number
and a file/line anchor:

I reviewed your code and have the following comments. Please address them.

1
.
 
`
src/auth.rs
`
 - Consider adding unit tests

2
.
 
`
src/auth.rs:42
`
 - Magic number should be a named constant

3
.
 
`
src/auth.rs:50-55
`
 - This block could be refactored

Paste it back to any coding agent (Claude, Codex, Cursor, etc).

For an agent-driven workflow where your agent opens tuicr in a tmux, Zellij, or Herdr
split pane, seeskills/tuicr/SKILL.md.

### To stdout

Run with--stdoutto pipe the markdown to another process:

tuicr --stdout 
>
 review.md
tuicr --stdout 
|
 pbcopy

## Review session CLI

tuicr reviewexposes saved sessions without opening the TUI. It can list
sessions, add comments, and print stored comments for agent and script
integrations. Seedocs/REVIEW_CLI.md.

The TUI creates a persisted session file when a review target becomes active,
so collaborative tools can add comments immediately. Empty auto-created session
files are removed when the TUI exits.tuicr review listmarks currently open
TUI sessions with"active": true.

## Library API

tuicr also exposes a Rust library API for tools that want to build on top of its
persisted review sessions.ReviewStorecan list sessions for a checkout, load a
session, and add review, file, line, or range comments using the same insertion
primitive as the TUI.

use
 tuicr
::
{
AddCommentRequest
,
 
CommentTarget
,
 
CommentType
,
 
LineSide
,
 
ReviewStore
}
;

let
 store = 
ReviewStore
::
new
(
)
;

let
 sessions = store
.
list_sessions_for_repo
(
"/path/to/repo"
)
?
;

let
 session = 
&
sessions
[
0
]
.
session_ref
;

store
.
add_comment
(

 session
,

 
AddCommentRequest
 
{

 
target
:
 
CommentTarget
::
Line
 
{

 
path
:
 
"src/main.rs"
.
into
(
)
,

 
line
:
 
42
,

 
side
:
 
LineSide
::
New
,

 
}
,

 
content
:
 
"Handle the empty case here."
.
into
(
)
,

 
comment_type
:
 
CommentType
::
from_id
(
"issue"
)
,

 
}
,

)
?
;

## Configuration

Path:~/.config/tuicr/config.tomlon Linux/macOS,%APPDATA%\tuicr\config.tomlon Windows.

theme
 = 
"
catppuccin-mocha
"

diff_view
 = 
"
side-by-side
"
 
#
 or "unified"

ignore_whitespace
 = 
false
 
#
 ignore all whitespace in local VCS diffs

appearance
 = 
"
system
"
 
#
 or "dark" / "light"

mouse
 = 
true

leader
 = 
"
;
"
 
#
 configurable prefix for leader shortcuts

comment_vim
 = 
false
 
#
 vim modal editing in the review comment box

review_watch_interval_ms
 = 
1000
 
#
 set to 0 to disable persisted-review polling

[[
comment_types
]]

id
 = 
"
issue
"

color
 = 
"
red
"

definition
 = 
"
must fix before merge
"

Bundled themes:dark,light,ayu-light,ayu-mirage,onedark,github-light,github-dark,catppuccin-latte,catppuccin-frappe,catppuccin-macchiato,catppuccin-mocha,everforest-dark,everforest-light,gruvbox-dark,gruvbox-light,nord-dark,nord-light,nord-dark-high-contrast,nord-light-high-contrast,solarized-light,solarized-dark,tokyo-night-storm,tokyo-night-day.

Local themes: settheme = "my-theme"or runtuicr --theme my-theme, then create~/.config/tuicr/themes/my-theme.tomlon Linux/macOS or%APPDATA%\tuicr\themes\my-theme.tomlon Windows. Local themes may reference a localsyntax_theme = "my-syntax.tmTheme"file for
syntax highlighting. A ready-to-copy example lives atexamples/tuicr-teal.tomlwith its matchingexamples/tuicr-teal-syntax.tmThemesyntax theme.

Full options, theme resolution precedence,comment_typessemantics, and.tuicrignorerules indocs/CONFIG.md.

## Keybindings

A first-session cheatsheet. Press?inside tuicr for the full reference.

Key

Action

j
 / 
k

Down / up

Ctrl-d
 / 
Ctrl-u

Half-page down / up

g
 / 
G

Top / bottom

{
 / 
}

Previous / next file

[
 / 
]

Previous / next hunk

m
 / 
M

Next / previous comment

/

Search the diff, or search help while help is open (case-insensitive)

c
 / 
C

Add line / file comment

v
 / 
V

Visual mode (range comment)

r

Toggle file reviewed

R

Toggle hunk reviewed

e

Open focused file in 
$EDITOR

y

Copy review to clipboard

:edit

Open focused file in 
$EDITOR

:submit

Push review to GitHub or GitLab

Tab
 in 
:
 prompt

Complete or cycle commands

?

Toggle full help

Full reference indocs/KEYBINDINGS.md.

## Sponsors

Thanks to the folks below for keeping tuicr development going, it means a lot to have the
work I'm doing here appreciated!

## License

MIT licensed. Contribution notes inCONTRIBUTING.md.