---
title: 'GitHub - Ataraxy-Labs/weave: Entity-level semantic merge driver for Git. Resolves conflicts that git can''t by understanding code structure via tree-sitter. 31/31 clean merges vs git''s 15/31. · GitHub'
url: https://github.com/Ataraxy-Labs/weave
site_name: hackernews_api
content_file: hackernews_api-github-ataraxy-labsweave-entity-level-semantic-mer
fetched_at: '2026-03-04T19:19:38.014068'
original_url: https://github.com/Ataraxy-Labs/weave
author: rs545837
date: '2026-03-04'
description: Entity-level semantic merge driver for Git. Resolves conflicts that git can't by understanding code structure via tree-sitter. 31/31 clean merges vs git's 15/31. - Ataraxy-Labs/weave
tags:
- hackernews
- trending
---

Ataraxy-Labs

 

/

weave

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork12
* Star415

 
 
 
 
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

85 Commits
85 Commits
.github
.github
 
 
Formula
Formula
 
 
assets
assets
 
 
benchmarks
benchmarks
 
 
crates
crates
 
 
docs
docs
 
 
site
site
 
 
.dockerignore
.dockerignore
 
 
.gitignore
.gitignore
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
LICENSE-APACHE
LICENSE-APACHE
 
 
LICENSE-MIT
LICENSE-MIT
 
 
README.md
README.md
 
 
fly.toml
fly.toml
 
 
View all files

## Repository files navigation

Resolves merge conflicts that Git can't by understanding code structure via tree-sitter.

## The Problem

Git merges by comparinglines. When two branches both add code to the same file — even to completely different functions — Git sees overlapping line ranges and declares a conflict:

<<<<<<< HEAD
export function validateToken(token: string): boolean {
 return token.length > 0 && token.startsWith("sk-");
}
=======
export function formatDate(date: Date): string {
 return date.toISOString().split('T')[0];
}
>>>>>>> feature-branch

These arecompletely independent changes. There's no real conflict. But someone has to manually resolve it anyway.

This happens constantly when multiple AI agents work on the same codebase. Agent A adds a function, Agent B adds a different function to the same file, and Git halts everything for a human to intervene.

## How Weave Fixes This

Weave replaces Git's line-based merge withentity-level merge. Instead of diffing lines, it:

1. Parses all three versions (base, ours, theirs) into semantic entities — functions, classes, JSON keys, etc. — usingtree-sitter
2. Matches entities across versions by identity (name + type + scope)
3. Merges at the entity level:* Different entities changed→ auto-resolved, no conflict
* Same entity changed by both→ attempts intra-entity merge, conflicts only if truly incompatible
* One side modifies, other deletes→ flags a meaningful conflict

The same scenario above? Weave merges it cleanly with zero conflicts — both functions end up in the output.

## Weave vs Git Merge

Scenario

Git (line-based)

Weave (entity-level)

Two agents add different functions to same file

CONFLICT

Auto-resolved

Agent A modifies 
foo()
, Agent B adds 
bar()

CONFLICT
 (adjacent lines)

Auto-resolved

Both agents modify the same function differently

CONFLICT

CONFLICT (with entity-level context)

One agent modifies, other deletes same function

CONFLICT (cryptic diff)

CONFLICT: 
function 'validateToken' (modified in ours, deleted in theirs)

Both agents add identical function

CONFLICT

Auto-resolved (identical content detected)

Different JSON keys modified

CONFLICT

Auto-resolved

The key difference: Git produces false conflicts onindependent changesbecause they happen to be in the same file. Weave only conflicts onactual semantic collisionswhen two branches change the same entity incompatibly.

## Real-World Benchmarks

Tested on real merge commits from major open-source repositories. For each merge commit, we replay the merge with both Git and Weave, then compare against the human-authored result.

* Wins: Merge commits where Git conflicted but Weave resolved cleanly
* Regressions: Cases where Weave introduced errors (0 across all repos)
* Human Match: How often Weave's output exactly matches what the human wrote
* Resolution Rate: Percentage of all merge commits Weave resolved vs total attempted

Repository

Language

Merge Commits

Wins

Regressions

Human Match

Resolution

git/git

C

1319

39

0

64%

13%

Flask

Python

56

14

0

57%

54%

CPython

C/Python

256

7

0

29%

13%

Go

Go

1247

19

0

58%

28%

TypeScript

TypeScript

2000

65

0

6%

23%

Zero regressions across all repositories. Every "win" is a place where a developer had to manually resolve a false conflict that Weave handles automatically.

## Conflict Markers

When a real conflict occurs, weave gives you context that Git doesn't:

<<<<<<< ours — function `process` (both modified)
export function process(data: any) {
 return JSON.stringify(data);
}
=======
export function process(data: any) {
 return data.toUpperCase();
}
>>>>>>> theirs — function `process` (both modified)

You immediately know: what entity conflicted, what type it is, and why it conflicted.

## Supported Languages

TypeScript, JavaScript, Python, Go, Rust, JSON, YAML, TOML, Markdown. Falls back to standard line-level merge for unsupported file types.

## Setup

#
 Build

cargo build --release

#
 In your repo:

./target/release/weave-cli setup

#
 Or manually:

git config merge.weave.name 
"
Entity-level semantic merge
"

git config merge.weave.driver 
"
/path/to/weave-driver %O %A %B %L %P
"

echo
 
"
*.ts *.tsx *.js *.py *.go *.rs *.json *.yaml *.toml *.md merge=weave
"
 
>>
 .gitattributes

Then use Git normally.git mergewill use weave automatically for configured file types.

## Preview

Dry-run a merge to see what weave would do:

weave-cli preview feature-branch

 src/utils.ts — auto-resolved
 unchanged: 2, added-ours: 1, added-theirs: 1
 src/api.ts — 1 conflict(s)
 ✗ function `process`: both modified

✓ Merge would be clean (1 file(s) auto-resolved by weave)

## Architecture

weave-core # Library: entity extraction, 3-way merge algorithm, reconstruction
weave-driver # Git merge driver binary (called by git via %O %A %B %L %P)
weave-cli # CLI: `weave setup` and `weave preview`

Usessem-corefor entity extraction via tree-sitter grammars.

## How It Works

 base
 / \
 ours theirs
 \ /
 weave merge

1. Parseall three versions into semantic entities via tree-sitter
2. Extract regions— alternating entity and interstitial (imports, whitespace) segments
3. Match entitiesacross versions by ID (file:type:name:parent)
4. Resolveeach entity: one-side-only changes win, both-changed attempts intra-entity 3-way merge
5. Reconstructfile from merged regions, preserving ours-side ordering
6. Fallbackto line-level merge for files >1MB, binary files, or unsupported types

## About

Entity-level semantic merge driver for Git. Resolves conflicts that git can't by understanding code structure via tree-sitter. 31/31 clean merges vs git's 15/31.

ataraxy-labs.github.io/weave/

### Topics

 git

 conflict-resolution

 rust

 tree-sitter

 mcp

 merge

 developer-tools

 ai-agents

 merge-driver

 semantic-merge

### Resources

 Readme

 

### License

 Apache-2.0, MIT licenses found
 

### Licenses found

Apache-2.0

LICENSE-APACHE

 

MIT

LICENSE-MIT

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

415

 stars
 

### Watchers

0

 watching
 

### Forks

12

 forks
 

 Report repository

 

## Releases11

v0.2.0

 Latest

 

Mar 4, 2026

 

+ 10 releases

## Sponsor this project

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Rust95.2%
* TypeScript4.2%
* Other0.6%