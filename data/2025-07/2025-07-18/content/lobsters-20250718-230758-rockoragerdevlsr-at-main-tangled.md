---
title: '@rockorager.dev/lsr at main · tangled'
url: https://tangled.sh/@rockorager.dev/lsr
site_name: lobsters
fetched_at: '2025-07-18T23:07:58.263591'
original_url: https://tangled.sh/@rockorager.dev/lsr
date: '2025-07-18'
tags: performance, zig
---

@rockorager.dev

/

lsr

 34


 fork



 ls but with io_uring




 main


 v1.0.0


 v0.2.0


 v0.1.0


 70


 1


 3


 docs


2 months ago

 nix


1 week ago

 src


20 hours ago

.gitignore


2 months ago

LICENSE


2 months ago

README.md


2 months ago

build.zig


4 weeks ago

build.zig.zon


1 week ago

flake.lock


2 months ago

flake.nix


4 weeks ago

screenshot.png


2 months ago

 commits


 view 70 commits

feature: support listing multiple directories

meow

 429eaeff



 theMackabu


8 hours ago

 main


fmt: user symlink_dir in short mode too

 82fe0382



 @rockorager.dev


8 hours ago

icons: prioritize entry kind vs extension

 ac72b537



 @rockorager.dev


1 week ago

 branches


 view 1 branches

 main


8 hours ago

default

 tags


 view 3 tags

 v1.0.0


4 weeks ago

latest

# lsr

ls(1)but with io_uring

## Installation

lsruses the zig build system. To install, you will need zig 0.14.0. To
install for the local user (assuming$HOME/.local/binis in$PATH), run:

zig build -Doptimize=ReleaseSmall --prefix $HOME/.local

which will installlsrand the associated manpage appropriately. Replace$HOME/.localwith your preferred installation directory.

## Usage

lsr [options] [path]

 --help Print this message and exit
 --version Print the version string

DISPLAY OPTIONS
 -1, --oneline Print entries one per line
 -a, --all Show files that start with a dot (ASCII 0x2E)
 -A, --almost-all Like --all, but skips implicit "." and ".." directories
 -C, --columns Print the output in columns
 --color=WHEN When to use colors (always, auto, never)
 --group-directories-first Print all directories before printing regular files
 --hyperlinks=WHEN When to use OSC 8 hyperlinks (always, auto, never)
 --icons=WHEN When to display icons (always, auto, never)
 -l, --long Display extended file metadata
 -r, --reverse Reverse the sort order
 -t, --time Sort the entries by modification time, most recent first

## Benchmarks

Benchmarks were all gathered on the same set of directories, using the latest
releases of each program (versions are shown below). All benchmarks run on Linux
(because io_uring).lsrdoes work on macOS/BSD as well, but will not see the
syscall batching benefits that are available with io_uring.

Program

Version

lsr

0.1.0

ls

9.7

eza

0.21.3

lsd

1.1.5

uutils

0.0.30

busybox

1.36.1

### Time

Data gathered withhyperfineon a directory ofnplain files.

Program

n=10

n=100

n=1,000

n=10,000

lsr -al

372.6 µs

634.3 µs

2.7 ms

22.1 ms

busybox ls -al

403.8 µs

1.1 ms

3.5 ms

32.5 ms

ls -al

1.4 ms

1.7 ms

4.7 ms

38.0 ms

eza -al

2.9 ms

3.3 ms

6.6 ms

40.2 ms

lsd -al

2.1 ms

3.5 ms

17.0 ms

153.4 ms

uutils ls -al

2.9 ms

3.6 ms

11.3 ms

89.6 ms

### Syscalls

Data gathered withstrace -con a directory ofnplain files. (Lower is better)

Program

n=10

n=100

n=1,000

n=10,000

lsr -al

20

28

105

848

busybox ls -al

84

410

2,128

20,383

ls -al

405

675

3,377

30,396

eza -al

319

411

1,320

10,364

lsd -al

508

1,408

10,423

100,512

uutils ls -al

445

986

6,397

10,005

push

git remote add origin
 git@tangled.sh:rockorager.dev/lsr

clone

HTTP

git clone
 https://tangled.sh/@rockorager.dev/lsr

SSH

git clone
 git@tangled.sh:rockorager.dev/lsr

Note that for self-hosted knots, clone URLs may be different based
 on your setup.
