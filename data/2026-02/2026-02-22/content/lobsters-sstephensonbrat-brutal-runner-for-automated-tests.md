---
title: 'sstephenson/brat: Brutal Runner for Automated Tests, a parallel TAP testing harness for the POSIX shell - Codeberg.org'
url: https://codeberg.org/sstephenson/brat
site_name: lobsters
content_file: lobsters-sstephensonbrat-brutal-runner-for-automated-tests
fetched_at: '2026-02-22T06:00:36.745804'
original_url: https://codeberg.org/sstephenson/brat
author: sstephenson
date: '2026-02-22'
description: brat - Brutal Runner for Automated Tests, a parallel TAP testing harness for the POSIX shell
tags: unix
---

sstephenson
/
brat

Watch

			1


Star

			14


Fork

				You've already forked brat


			0


Brutal Runner for Automated Tests, a parallel TAP testing harness for the POSIX shell

posix-shell

tap

unit-testing

unix

* Shell77.5%
* Awk22.5%

main

Find a file

		HTTPS


Sam Stephenson

94e95bcb9e


			All checks were successful





Brat CI / macOS (push)
Successful in 6s

Details

Brat CI / Linux (alpine) (push)
Successful in 8s

Details

Brat CI / Linux (debian) (push)
Successful in 22s

Details

Brat CI / Linux (fedora) (push)
Successful in 28s

Details

Brat CI / FreeBSD (push)
Successful in 1m1s

Details

Fix per-user installation instructions

2026-02-20 12:47:31 -06:00

.forgejo
/workflows



Move CI runner into a top-level
script/test

2026-02-18 13:57:51 -06:00

bin



brut: Pass original arguments to
_unhandled.sh

2026-02-06 13:21:22 -06:00

lib
/brat



Brat 0.9.0

2026-02-19 12:48:02 -06:00

libexec



Escape
#
 and
\
 in test names, per the TAP spec

2026-02-13 18:38:36 -06:00

script



Test suite defaults
BRAT_JOBS
 to the number of CPUs

2026-02-18 15:50:04 -06:00

test



Extract
script/loc

2026-02-18 13:59:25 -06:00

.gitattributes

Mark
wcwidth.awk
 as vendored

2026-02-01 22:13:52 -06:00

CHANGELOG.md

Brat 0.9.0

2026-02-19 12:48:02 -06:00

LICENSE.md

Initial commit

2026-01-22 11:17:18 -06:00

README.md

Fix per-user installation instructions

2026-02-20 12:47:31 -06:00

#### README.md

# Brat

Brat is theBrutal Runner for Automated Tests, a parallel TAP testing harness for the POSIX shell.

Brutal as in architecture.Brat is true to the “materials” it is built with: shell, awk, and the Unix pipeline. It reveals its internal plumbing in the same way a brutalist building might expose its ductwork. Some will find it ugly; others (maybe you?) will appreciate its didactic honesty.

POSIX as in zero dependencies.Brat targets the POSIX.1-2024 specification. Practically speaking, it is designed to run on the minimum common subset of contemporary Unix OSes, with no other dependencies or specific implementation requirements. Wetest Bratunder continuous integration against a variety of platforms.

Intentionally small.Brat is designed to be embedded directly into your project. It has no build step and nothing to configure. At just under a thousand lines of shell and awk, you can read and understand the codebase in an afternoon.

Jump to:Installation|Writing Tests|Running Tests|Implementation Notes|Contributing|License

## Overview

With Brat, you write tests for Unix programs using a special shell syntax:

# test/backup.brat

setup
()

{


cd

"
$DIR
/.."

}

@test
"prints usage when run without arguments"

{

 run bin/backup.sh

[

$status
 -eq
1

]

 match
"
$stderr
"

'usage:'

}

@test
"errors when source directory does not exist"

{

 run bin/backup.sh /nonexistent
"
$TEST_TMP
.tar.gz"


[

$status
 -eq
1

]

 match
"
$stderr
"

'not found'

}

@test
"creates backup archive"

{

 run bin/backup.sh
"
$DIR
/fixtures/testdata"

"
$TEST_TMP
.tar.gz"


[

$status
 -eq
0

]

 tar tf
"
$TEST_TMP
.tar.gz"

}

A preprocessor transforms these test cases into shell functions which run withset -eu(exit on error, error when referencing undefined variables). In this way, every line of a test case acts as an assertion.

When you run your tests, Brat displays the results in a streaming TAP format:

$ brat test/*.brat
TAP version 14
1..3

ok 1 - backup.brat:7: prints usage when run without arguments
ok 2 - backup.brat:13: errors when source directory does not exist
ok 3 - backup.brat:19: creates backup archive

# ✓ 3 tests (3 passed, 0 failed, 0 skipped)

If any line of a test fails, Brat shows the shell’sxtrace(set -x) output up to that point, along with anything written to stdout or stderr:

$ brat test/backup.brat:19
TAP version 14
1..1

not ok 1 - backup.brat:19: creates backup archive
# + setup
# + cd $DIR/..
# + run bin/backup.sh $DIR/fixtures/testdata $TEST_TMP.tar.gz
# + '[' 0 -eq 0 ']'
# + tar tf $TEST_TMP.tar.gz
# tar: Error opening archive: Unrecognized archive format
# (test failed with status 1)

# ✘ 1 test (0 passed, 1 failed, 0 skipped)

Bratformats its TAP streamwith color when connected to a terminal. In particular, failing tests are highlighted in red.

### Parallel Execution

Tests run sequentially by default, but Brat has built-in support for parallel test execution. Use-jor set$BRAT_JOBSto run tests in parallel. For example, to run up to 8 tests concurrently:

$ brat -j 8 test/*.brat

Brat spawns each test in a background process, streaming results as they complete, potentially out of order. Thepretty formatterbuffers and sorts them live for display.

### Comparison with Bats

Brat is a spiritual successor toBats, the Bash Automated Testing System. If you’ve used Bats, Brat will feel familiar, but more spartan.

Bats

Brat

Shell

Requires Bash

Works with any POSIX shell

Parallel execution

Requires GNU parallel

Built-in support, using a FIFO

Output

TAP or a proprietary pretty format

TAP always; pretty format is highlighted and sorted TAP

Output capture

$output
,
$lines[]
 (in-memory strings)

$stdout
,
$stderr
 (file paths)

Built-in helpers

Rich standard library and ecosystem

Minimal

Lifecycle hooks

Per-test and per-module setup and teardown

Per-test setup and teardown only

One important difference is that Brat’srunhelper captures output to separate files and exposes their paths to you, avoiding the runtime overhead of reading large outputs into strings and arrays.

### Portability

Brat is written entirely in POSIX shell and awk, targeting thePOSIX.1-2024 standardwith no other dependencies. It is architecture-independent and does not require a C compiler.

We test Brat,using Brat, with continuous integration on the following platforms:

sh

awk

Alpine Linux

busybox ash

busybox awk

Debian Linux

dash

mawk

Fedora Linux

Bash

gawk

FreeBSD

FreeBSD ash

nawk

macOS

Bash (3.2)

nawk

## Installation

Brat has no build step and no dependencies to install.

### Installing Brat Globally

Download and extract thelatest release archiveand symlinkbin/bratinto your PATH. For example, to install Brat in/usr/local:

# curl -sL https://codeberg.org/sstephenson/brat/archive/latest.tar.gz | tar -C /usr/local -xf -
# ln -s /usr/local/brat/bin/brat /usr/local/bin/brat

Or if you prefer a per-user installation (assuming$HOME/.local/binis in your PATH):

$ curl -sL https://codeberg.org/sstephenson/brat/archive/latest.tar.gz | tar -C ~/.local -xf -
$ ln -s ~/.local/brat/bin/brat ~/.local/bin/brat

### Embedding Brat in Your Project

Clone Brat into your project and run it directly:

$ git clone https://codeberg.org/sstephenson/brat.git vendor/brat
$ vendor/brat/bin/brat test/*.brat

## Writing Tests

Test files use the.bratextension by convention. Each file is a shell script containing one or more test definitions:

@test
"description of what this tests"

{


# Commands here run with errexit enabled; any


# command that exits nonzero fails the test


[

1
 -eq
1

]

}

It’s a good idea to add a standard#!/bin/shshebang to the top of each test file so that your editor or code forge applies proper syntax highlighting. Note, however, that Brat test files cannot be executed directly by the shell.

### About the Test Environment

Brat automatically sets the following variables before each test run:

* $FILE— the path to the test file
* $DIR— the directory containing the test file
* $TEST_TMP— a unique temporary path prefix for the current test

Use the$DIRvariable to source test helper scripts or load fixture data relative to the location of the test file.

You can use the$TEST_TMPvariable as a prefix for temporary files or directories you create during a test. Filenames matching$TEST_TMP.*are automatically deleted after each test run.

### Running Commands with therunHelper

Userunto execute a command and capture its output and status code:

@test
"captures exit status and output"

{

 run ls /nonexistent

[

$status
 -eq
1

]

 match
"
$stderr
"

'No such file'

}

Afterrun, three variables are available:

* $status— the command’s exit code
* $stdout— the path to a file containing standard output
* $stderr— the path to a file containing standard error

### Matching Output with thematchHelper

Usematchto assert that a file contains a string or pattern:

match
"
$stdout
"

'hello world'

# exact substring

match
"
$stdout
"

'/^hello .+$/'

# ERE pattern

If the second argument begins and ends with a/, thematchhelper treats it as anextended regular expression (ERE) pattern. Otherwise, it is treated as an exact substring to match.

### Comparing Files with thecompareHelper

Usecompareto assert that two files have identical contents:

run my_formatter <input.txt
compare
"
$stdout
"

"
$DIR
/fixtures/expected-output.txt"

compareuses the POSIXcksumutility to calculate a 32-bit CRC of both files and compare them, along with the files’ lengths, to determine equivalence.Do notuse this helper if you need cryptographic integrity when comparing files. It is provided as an approximate replacement forcmpon systems where that command is not included by default.

### Skipping Tests

Use@skipto mark tests that shouldn’t run:

@skip
"not yet implemented"

{


# This test body is not executed


false

}

Brat treats a@skiptest like a passing test. It will appear with a# SKIPdirective following its name in the TAP output.

### Marking Works in Progress

Use@todoto mark tests you expect to fail:

@todo
"waiting on upstream fix"

{


# Runs, but records as passing even when it fails

 run buggy_command

[

$status
 -eq
0

]

}

If a@todotest fails, Brat will display its xtrace output but otherwise treat it as a passing test. It will appear with a# TODOdirective following its name in the TAP output.

### Lifecycle Hooks

You can definesetupandteardownfunctions to run code before and after each test case:

setup
()

{


TMPFILE
=
"
$(
mktemp
)
"

}

teardown
()

{

 rm -f
"
$TMPFILE
"

}

@test
"uses the temp file"

{


echo
 data >
"
$TMPFILE
"


[
 -s
"
$TMPFILE
"

]

}

teardownruns even when a test fails, so it’s safe to use for cleanup.

### Top-Level Code

Code outside of@test,@skip, and@todoblocks runs twice: once when Brat scans the file to discover tests and their names, and again before each test runs.

# Runs during both planning and test execution

cd

"
$DIR
/.."

setup
()

{


# Only called during test execution

}

@test
"example"

{


# ...

}

Keep this in mind if your top-level code has side effects. In practice, most test files only define functions (likesetup) at the top level, which is harmless during planning.

## Running Tests

To…

Run…

Run all tests in a directory

brat test/*.brat

Run a specific test file

brat test/backup.brat

Run a specific test by line number

brat test/backup.brat:19

Run tests in parallel (8 concurrent jobs)

brat -j 8 test/*.brat

Filter tests by exact name match

brat -n "creates backup archive" test/*.brat

Filter tests by extended regular expression (ERE)

brat -n "/backup/" test/*.brat

Exclude tests by exact name or ERE

brat -e "/usage/" test/*.brat

### Working with Subcommands

Brat exposes the subcommands that make up its internal pipeline. When you runbrat test/*.brat, Brat orchestrates the following:

1. For each test file,test-planextracts test metadata (file, line, kind, name) into a tab-delimited plan.
2. plan-buildaggregates these plans, sorts the tests by filename and line number, and applies any-n/-efilters.
3. plan-runexecutes tests from the plan, invokingtest-runin parallel and printing the results as TAP.

You can work with this plumbing directly:

Subcommand

Description

brat plan-run

The main entry point: build a plan, run tests, format output

brat plan-build

Build a test plan from files, applying
-n
/
-e
 filters

brat test-plan

Extract test metadata from a single file

brat test-run

Run a single test by file and line number

The subcommands are composable. For example, you can build a plan once and pipe it tobrat plan-run -:

$ brat plan-build test/*.brat | grep backup | sort -r >plan.txt
$ brat plan-run - <plan.txt

### Formatting Output

Brat outputsTAP version 14. When connected to a terminal, the TAP stream passes through a pretty formatter that live-sorts results and applies syntax highlighting. When stdout is not a terminal, or when$CIis set, Brat outputs unadorned TAP.

You can force raw TAP output by settingBRAT_FORMAT=plain.

## Implementation Notes

Brat is built on a small command dispatcher called Brut, theBrutal Router for Unix Tools, which discovers and delegates tosubcommand executables in thelibexec/directory. Brut is entirely self-contained in thebin/bratscript.

### Dispatch Behavior

Before parsing any arguments,bin/bratsourceslib/brat/_init.sh, which forks a copy of itself to continue subcommand execution, waits on the forked process to exit, and deletes any temporary files it created. This automatic garbage collection removes the need for bookkeeping in subcommands.

After scanning arguments, ifbin/bratdoes not find a matching subcommand, it sourceslib/brat/_unhandled.sh, which attempts to rewrite the arguments into abrat plan-runpipeline. SeeWorking with Subcommandsfor details on the default pipeline.

### Subcommand Interaction

Brat locates itself in the filesystem and adds itslibexec/andlib/brat/directories to the front of the PATH. Subcommands invoke each other directly (e.g.brat-plan-build,brat-test-run) without going through the dispatcher. Subcommands with--in the name (e.g.brat--tap-format) are “private” and cannot be invoked as arguments tobin/brat.

### Shell Functions

Shared shell functions live inlib/brat/. Because this directory is first in the PATH, its files can be sourced directly by subcommands (e.g.. brat.sh).

* lib/brat/brat.sh— caching, preprocessing, EXIT trap chaining; sourced by convention at the top of every subcommand script
* lib/brat/eval.sh— test environment and lifecycle functions; sourced bybrat-test-planandbrat-test-run
* lib/brat/test.sh— therun,match, andcomparehelpers; sourced bybrat-test-run

### Awk Filters

Brat’s many awk filters also live inlib/brat/.

* lib/brat/match.awk— used by thematchhelper to test file contents
* lib/brat/plan-lines.awk— used bybrat-plan-buildto parsefile:linearguments
* lib/brat/plan-names.awk— filters a plan by-n(include) and-e(exclude) patterns
* lib/brat/preprocess.awk— preprocesses Brat test directives into shell functions
* lib/brat/rewrite-paths.awk— rewrites internal pathnames in test output
* lib/brat/tap-format-plain.awk— passes TAP through unchanged, appending a summary line
* lib/brat/tap-format-pretty.awk— live-sorts TAP results with color highlighting and a status line
* lib/brat/tap-status.awk— parses TAP to track test counts and generate summaries
* lib/brat/terminal.awk— provides functions for ANSI escape sequences and terminal dimensions

### Tracing Execution

You can setBRAT_DEBUG=1to follow the execution of a Brat run. When this variable is set, thelib/brat/_init.shscript enables xtrace output to stderr withset -x. Note that this does not include the trace output for tests themselves, which is redirected to disk by Brat.

## Contributing

Brat is hosted on Codeberg:https://codeberg.org/sstephenson/brat

We welcome issues and tested pull requests from human contributors. However, before submitting a large pull request, or one that changes behavior that is not a bug, we ask that you please open an issue first so we can discuss whether it is a good fit for the project.

### About the Test Suite

Brat’s tests live in thetest/directory; thetest/*.bratfiles together comprise itstest suite. The tests in these files primarily invoke Brat on another tree of test files rooted intest/fixtures/.

Use thescript/testcommand to run the test suite. This script first performs a series of “sentinel” checks to verify that Brat actually runs tests and propagates their exit statuses. Then it runsbin/brat test/*.bratin parallel, with a job count equal to the number of CPUs on the host system.

### Reporting Issues

Brat is portable software and compatibility is a moving target. When reporting issues, please be sure to include information about your operating system, including its release version, and the versions and lineage of thesh,awk, andsedcommands.

### Code Conventions

When contributing changes to Brat, please respect the conventions of existing code inlib/brat/andlibexec/.

Shell should be written withset -euand careful consideration of what is specified by POSIX. See theShell Command Language specificationfor more details.

Similarly, awk code should be written in thesubset specified by POSIX. Be sure to declare local variables in awk functions at the end of the parameter list. By convention, Brat separates “real” parameters from local variables with an unused parameter named__.

## License

Brat is free software, distributable under the terms of the MIT + Trans Rights License. SeeLICENSE.mdfor details.

Brat includes a copy ofwcwidth.awkby Eric Pruitt, released under the 2-Clause BSD license.

© 2026Sam Stephenson. Handwritten in Mexico City.
