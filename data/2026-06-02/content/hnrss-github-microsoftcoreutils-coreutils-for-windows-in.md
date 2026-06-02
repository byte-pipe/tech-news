---
title: 'GitHub - microsoft/coreutils: Coreutils for Windows: Installer & Packaging · GitHub'
url: https://github.com/microsoft/coreutils
site_name: hnrss
content_file: hnrss-github-microsoftcoreutils-coreutils-for-windows-in
fetched_at: '2026-06-02T20:05:34.789286'
original_url: https://github.com/microsoft/coreutils
date: '2026-06-02'
description: 'Coreutils for Windows: Installer & Packaging. Contribute to microsoft/coreutils development by creating an account on GitHub.'
tags:
- hackernews
- hnrss
---

microsoft

 

/

coreutils

Public

* NotificationsYou must be signed in to change notification settings
* Fork4
* Star289

 
 
 
 
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

2 Commits
2 Commits
.cargo
.cargo
 
 
.pipelines
.pipelines
 
 
deps
deps
 
 
src
src
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
LICENSE
LICENSE
 
 
NOTICE.md
NOTICE.md
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
build.ps1
build.ps1
 
 
build.rs
build.rs
 
 
coreutils.iss
coreutils.iss
 
 
View all files

## Repository files navigation

# Coreutils for Windows

UNIX-style core utilities for Windows. The same commands and pipelines you use on Linux, macOS, and WSL - natively.

### Install·Shell conflicts·Windows caveats·Contributing

A Microsoft-maintained build ofuutils/coreutils,findutils, and a GNU-compatiblegreppackaged as a
single multi-call binary for Windows. The goal is to make moving between Linux, macOS, WSL,
containers, and Windows frictionless: the same commands, flags, and pipelines work the same
way, so existing scripts carry over without translation.

Each command supports the standard--helpflag for full syntax and options.

This project is in preview.

## Install

Install Coreutils for Windows with WinGet:

winget install Microsoft.Coreutils

Or grab the latest build from ourRelease Page.

## Shell conflicts

Note

Any command not mention is included in this suite. The following only lists conflicts.

Warning

PowerShell 7.4 or newer is required. Older PowerShell versions aren't supported.

Several commands share names with built-ins in CMD and PowerShell. Whether the Coreutils
version runs depends on the shell, the PATH order, and (for PowerShell) the alias table.

Legend: ✅ ships and works ·⚠️ships but conflicts with a built-in · 🛑 not shipped

Command

CMD

PowerShell 7.4+

Notes

cat

✅

⚠️

cp

✅

⚠️

date

⚠️

⚠️

dir

🛑

🛑

Conflicts with the built-in DOS command

echo

⚠️

⚠️

expand

🛑

🛑

Conflicts with the built-in DOS command

find

✅

✅

Integrated port of the original DOS command

hostname

✅

✅

Superset of the Windows built-in

kill

🛑

🛑

Unavailable due to lack of signals on Windows; Implementing a form of SIGTERM/SIGKILL may be possible in the future however

ls

✅

⚠️

mkdir

⚠️

⚠️

more

🛑

🛑

Conflicts with the built-in DOS command (consider 
edit
 as an alternative)

mv

✅

⚠️

paste

🛑

🛑

Conflicts with the built-in DOS command

pwd

✅

⚠️

rm

✅

⚠️

rmdir

⚠️

⚠️

sleep

✅

⚠️

sort

✅

✅

Integrated port of the original DOS command

tee

✅

⚠️

timeout

🛑

🛑

Relies on 
kill
's functionality

uptime

✅

⚠️

whoami

🛑

🛑

Conflicts with the built-in Windows command

## Windows caveats

Difference

Detail

CRLF line endings

Windows text files often use CRLF (
\r\n
). Most utilities handle this transparently, but pattern matching with 
$
 and exact byte counts can be affected.

No 
/dev/null

Use 
NUL
 instead, for example 
find . -name "*.log" > NUL

No POSIX signals

Signals such as 
SIGHUP
, 
SIGPIPE
, and 
SIGUSR
 aren't available. 
Ctrl+C
 (
SIGINT
) works as expected.

Path separators

Both 
/
 and 
\
 are accepted. Some utilities produce 
\
-separated output, which can affect downstream piping.

File permissions

Windows uses ACLs, not POSIX permission bits. Permission-based predicates (for example 
find -perm
) may behave differently or be unavailable.

Symbolic links

Reading existing symbolic links works without elevation. Creating new symbolic links requires Developer Mode (
Settings > System > Advanced
) or an elevated terminal.

### Intentionally dropped

Commands that exist upstream but aren't shipped here because they rely on POSIX-only concepts, would break existing Windows scripts, or simply aren't useful on Windows.

* dd: Perhaps useful in the future.
* dircolors,shred,sync,uname: Not particularly useful on Windows.
* chcon,chgrp,chmod,chown,chroot,groups,hostid,id,install,logname,mkfifo,mknod,nice,nohup,pathchk,pinky,runcon,stdbuf,stty,tty,users,who: POSIX-only concepts unavailable on Windows.

## Contributing

Bug reports and pull requests are welcome. SeeCONTRIBUTING.mdfor details on the repo layout and how changes flow between this repo and the upstream uutils projects.

## About

Coreutils for Windows: Installer & Packaging

### Topics

 command-line-tool

 coreutils

 gnu-coreutils

### Resources

 Readme

 

### License

 MIT license
 

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

289

 stars
 

### Watchers

2

 watching
 

### Forks

4

 forks
 

 Report repository

 

## Releases1

Our first release of Coreutils for Windows

 Latest

 

Jun 2, 2026

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Rust39.4%
* PowerShell34.9%
* Inno Setup25.7%