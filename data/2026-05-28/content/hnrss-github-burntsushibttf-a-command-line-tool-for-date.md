---
title: 'GitHub - BurntSushi/bttf: A command line tool for datetime arithmetic, parsing, formatting and more. · GitHub'
url: https://github.com/BurntSushi/bttf
site_name: hnrss
content_file: hnrss-github-burntsushibttf-a-command-line-tool-for-date
fetched_at: '2026-05-28T19:52:03.693623'
original_url: https://github.com/BurntSushi/bttf
date: '2026-05-28'
description: A command line tool for datetime arithmetic, parsing, formatting and more. - BurntSushi/bttf
tags:
- hackernews
- hnrss
---

BurntSushi

 

/

bttf

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork10
* Star514

 
 
 
 
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

37 Commits
37 Commits
.cargo
.cargo
 
 
.github
.github
 
 
ci
ci
 
 
pkg/
windows
pkg/
windows
 
 
src
src
 
 
tests
tests
 
 
.gitignore
.gitignore
 
 
.rgignore
.rgignore
 
 
COMPARISON.md
COMPARISON.md
 
 
COPYING
COPYING
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
GUIDE.md
GUIDE.md
 
 
LICENSE-MIT
LICENSE-MIT
 
 
README.md
README.md
 
 
UNLICENSE
UNLICENSE
 
 
build.rs
build.rs
 
 
rustfmt.toml
rustfmt.toml
 
 
View all files

## Repository files navigation

# bttf

A command line tool for datetime arithmetic, parsing, formatting and more.

Dual-licensed under MIT or theUNLICENSE.

### Documentation

Theuser guideshould be your first stop for understanding the high level
concepts that bttf deals with. Otherwise, consultbttf --helporbttf <sub-command> --helpfor more specific details.

Alternatively, there is acomparisonbetween other similar tools that might
give you a quick sense of what bttf is like.

### Brief Examples

Print the current time:

$ 
bttf

Sat, May 10, 2025, 8:02:04 AM EDT

Tip

If you get output like2025 M05 10, Mon 08:02:04instead, that's because
you likely don't havelocale supportsupport configured. That
requires settingBTTF_LOCALEand using a GitHub release binary or building
bttf with thelocalefeature enabled.

Print the current time in a format of your choosing:

$ 
bttf 
time
 fmt -f rfc3339 now

2025-05-10T08:08:30.101066734-04:00

$ 
bttf 
time
 fmt -f rfc9557 now

2025-05-10T08:08:33.420946447-04:00[America/New_York]

$ 
bttf 
time
 fmt -f 
'
%Y-%m-%d %H:%M:%S %Z
'
 now

2025-05-10 08:08:48 EDT

Print multiple relative times in one command:

$ 
bttf 
time
 fmt -f 
'
%c
'
 now -1d 
'
next sat
'
 
'
last monday
'
 
'
9pm last mon
'

Sat, May 10, 2025, 10:44:39 AM EDT

Fri, May 9, 2025, 10:44:39 AM EDT

Sat, May 17, 2025, 10:44:39 AM EDT

Mon, May 5, 2025, 10:44:39 AM EDT

Mon, May 5, 2025, 9:00:00 PM EDT

Print the current time in another time zone, and round it the nearest 15 minute
increment:

$ 
bttf 
time
 
in
 Asia/Bangkok now 
|
 bttf 
time
 round -i 15 -s minute

2025-05-10T19:15:00+07:00[Asia/Bangkok]

Add a duration to the current time:

$ 
bttf 
time
 add -1w now

2025-05-03T10:34:30.819577918-04:00[America/New_York]

$ 
bttf 
time
 add 
'
1 week, 12 hours ago
'
 now

2025-05-02T22:34:44.114109514-04:00[America/New_York]

$ 
bttf 
time
 add 6mo now

2025-11-10T10:34:49.023321635-05:00[America/New_York]

Find the duration since a date in the past and round it to the desired
precision:

$ 
bttf span since 2025-01-20T12:00

2636h 1m 21s 324ms 691µs 216ns

$ 
bttf span since 2025-01-20T12:00 -l year

3mo 20d 21h 1m 25s 171ms 886µs 534ns

$ 
bttf span since 2025-01-20T12:00 
|
 bttf span round -l year -s day

3mo 18d

$ 
bttf span since 2025-01-20T12:00 
|
 bttf span round -l day -s day

110d

Find timestamps in a log file and reformat them into your local time in place:

$ 
head -n3 /tmp/access.log

2025-04-30T05:25:14Z INFO http.log.access.log0 handled request

2025-04-30T05:25:17Z INFO http.log.access.log0 handled request

2025-04-30T05:25:18Z INFO http.log.access.log0 handled request

$ 
bttf tag lines /tmp/access.log 
|
 bttf 
time
 
in
 system 
|
 bttf 
time
 fmt -f 
'
%c
'
 
|
 head -n3 
|
 bttf untag -s

Wed, Apr 30, 2025, 1:25:14 AM EDT INFO http.log.access.log0 handled request

Wed, Apr 30, 2025, 1:25:17 AM EDT INFO http.log.access.log0 handled request

Wed, Apr 30, 2025, 1:25:18 AM EDT INFO http.log.access.log0 handled request

Generate a sequence of the next 5 days that are Monday, Wednesday or Friday
at a specific time, and then format them in your locale:

$ 
bttf 
time
 seq day today -c5 -H 9 -w mon,wed,fri 
|
 bttf 
time
 fmt -f 
'
%c
'

Mon, May 12, 2025, 9:00:00 AM EDT

Wed, May 14, 2025, 9:00:00 AM EDT

Fri, May 16, 2025, 9:00:00 AM EDT

Mon, May 19, 2025, 9:00:00 AM EDT

Wed, May 21, 2025, 9:00:00 AM EDT

Print every day remaining in the current month:

$ 
bttf 
time
 seq daily --until 
$(
bttf 
time
 end-of month now
)
 today

2025-05-10T00:00:00-04:00[America/New_York]

2025-05-11T00:00:00-04:00[America/New_York]

2025-05-12T00:00:00-04:00[America/New_York]

2025-05-13T00:00:00-04:00[America/New_York]

[.. snip ..]

Find the last weekday in each of the next 12 months and print them in a
succinct format:

$ 
bttf 
time
 seq -c12 monthly -w mon,tue,wed,thu,fri --set-position -1 
|
 bttf 
time
 fmt -f 
'
%a, %Y-%m-%d
'

Fri, 2025-05-30

Mon, 2025-06-30

Thu, 2025-07-31

Fri, 2025-08-29

Tue, 2025-09-30

Fri, 2025-10-31

Fri, 2025-11-28

Wed, 2025-12-31

Fri, 2026-01-30

Fri, 2026-02-27

Tue, 2026-03-31

Thu, 2026-04-30

Or print the second Tuesday of each month until the end of the year:

$ 
bttf 
time
 seq monthly -w 2-tue --until 
$(
bttf 
time
 end-of year now
)
 
|
 bttf 
time
 fmt -f 
'
%a, %F
'

Tue, 2025-05-13

Tue, 2025-06-10

Tue, 2025-07-08

Tue, 2025-08-12

Tue, 2025-09-09

Tue, 2025-10-14

Tue, 2025-11-11

Tue, 2025-12-09

Finally, this command will get the last commit date on each file in a git
repository, sort them in ascending order, format the datetime to a fixed-width
format and then print the data in a tabular format:

$ 
git ls-files \

 | bttf tag exec git log -n1 --format='%aI' \

 | bttf time sort \

 | bttf time fmt -f '%Y-%m-%d %H:%M:%S %z' \

 | bttf untag -f '{tag}\t{data}'

[.. snip ..]

2025-05-05 21:54:09 -0400 src/tz/timezone.rs

2025-05-05 21:54:09 -0400 src/tz/tzif.rs

2025-05-05 22:06:38 -0400 Cargo.toml

2025-05-05 22:06:38 -0400 crates/jiff-static/Cargo.toml

2025-05-07 18:55:23 -0400 scripts/test-various-feature-combos

2025-05-07 18:55:23 -0400 src/error.rs

2025-05-08 08:38:22 -0400 src/tz/system/mod.rs

2025-05-08 16:52:55 -0400 crates/jiff-icu/Cargo.toml

2025-05-08 16:52:55 -0400 crates/jiff-icu/src/lib.rs

To see more examples, check out theuser guideor thecomparisonbetween
bttf and other datetime command line tools.

### Installation

The binary name for bttf isbttf. It is also oncrates.io under the namebttf.

Archives of precompiled binaries for bttf are available for Windows,
macOS and Linux.Linux and
Windows binaries are static executables.

Alternatively, if you're aRust programmer, bttf can be installed withcargo. Note that the binary may be bigger than expected because it contains
debug symbols. This is intentional. To remove debug symbols and therefore
reduce the file size, runstripon the binary.

cargo install bttf

Or, if you wantlocale support(which is enabled in the
binaries distributed on GitHub), then install with thelocalefeature
enabled:

cargo install bttf --features locale

### bttf as a library

There is relatively little datetime logic inside of bttf proper.
(Except for its RFC 5545 implementation, which may eventually move
out to a library.) Most of the datetime logic is instead provided byJiff. Additionally, localization is
provided byICU4Xand integrated with Jiff viajiff-icu.

### WARNING

I may ship arbitrary and capricious breaking changes at this point. You have
been warned.

Also, no compatibility withdateis intended. This is not a drop-in
replacement. It is not intended to be. It never will be. And it doesn't give
a hoot about POSIX (other than theTZenvironment variable). If you need adatecompatible program, then go use an implementation of POSIXdate.
With that said, bttf'sbttf time fmtcommand generally supports astrftimesyntax that has a large amount of compatibility with GNUdate.

If you have use cases serviced bydatethat aren't possible with bttf, I'd
like to hear about them.

### Motivation

I built this tool primarily as a way to expose some of the library
functionality offered byJiffon the
command line. I was after a succinct way to format datetimes or do arithmetic.
So I built this tool.

dateis one of those commands that I use infrequently enough, and its flags
and behavior is weird enough, that I constantly have to re-read its manual in
order to use it effectively. So perhaps there is room for improvement there.

As I progressed in constructing this tool, I quickly found it somewhat limited
by the fact that theonlydata it could process was datetimes. To make bttf
much more versatile, I added abttf tagcommand that looks for datetimes in
arbitrary data and wraps them up into a JSON lines format. It's unclear to me
how broadly useful folks will find this functionality, but other datetime
utilities don't seem to have it.

I also wanted to use Jiff in "anger," and in particular, as part of confidently
getting it to a 1.0 state. Is its performance acceptable? Are there APIs
missing that are needed for real world programs? And so on. For example,
because of my development on bttf, I added a way to hook ICU4X localization
into Jiff'sjiff::fmt::strtimeAPIs.

### Building

bttf is written in Rust, so you'll need to grab aRust installationin order to compile it.

To build bttf:

git clone https://github.com/BurntSushi/bttf

cd bttf

cargo build --release

./target/release/bttf --version

Additionally, optional locale support can be built with bttf by enabling thelocalefeature:

cargo build --release --features locale

bttf can be built with the musl target on Linux by first installing the musl
library on your system (consult your friendly neighborhood package manager).
Then you just need to add musl support to your Rust toolchain and rebuild
bttf, which yields a fully static executable:

rustup target add x86_64-unknown-linux-musl

cargo build --release --target x86_64-unknown-linux-musl

Applying the--features localeflag from above should also work.

### Running tests

To run both unit tests and integration tests, use:

cargo test

from the repository root. If you're hacking on bttf and need to change or
add tests, bttf makes heavy use ofcargo instafor snapshot testing. For
example, to run tests with Insta, use:

cargo insta test

And if there are any snapshots to review, you can review them via:

cargo insta review

## About

A command line tool for datetime arithmetic, parsing, formatting and more.

### Topics

 rust

 cli

 time

 command-line

 datetime

 date

 timezone

 zone

 iana

 strftime

 time-zone

 rfc-5545

 strptime

 jiff

 recurrence-rule

### Resources

 Readme

 

### License

 Unlicense and 2 other licenses found
 

### Licenses found

Unlicense

UNLICENSE

 

Unknown

COPYING

 

MIT

LICENSE-MIT

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

514

 stars
 

### Watchers

1

 watching
 

### Forks

10

 forks
 

 Report repository

 

## Releases4

0.1.4

 Latest

 

May 28, 2026

 

+ 3 releases

## Sponsor this project

 

 

 Sponsor

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

Learn more about GitHub Sponsors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Rust99.9%
* Shell0.1%