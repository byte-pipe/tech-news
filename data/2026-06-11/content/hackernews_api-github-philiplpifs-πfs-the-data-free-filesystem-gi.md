---
title: 'GitHub - philipl/pifs: πfs - the data-free filesystem! · GitHub'
url: https://github.com/philipl/pifs
site_name: hackernews_api
content_file: hackernews_api-github-philiplpifs-πfs-the-data-free-filesystem-gi
fetched_at: '2026-06-11T12:23:34.557964'
original_url: https://github.com/philipl/pifs
author: helterskelter
date: '2026-06-10'
description: πfs - the data-free filesystem! Contribute to philipl/pifs development by creating an account on GitHub.
tags:
- hackernews
- trending
---

philipl

 

/

pifs

Public

* NotificationsYou must be signed in to change notification settings
* Fork294
* Star7.3k

 
 
 
 
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

22 Commits
22 Commits
src
src
 
 
.gitignore
.gitignore
 
 
AUTHORS
AUTHORS
 
 
COPYING
COPYING
 
 
ChangeLog
ChangeLog
 
 
INSTALL
INSTALL
 
 
Makefile.am
Makefile.am
 
 
NEWS
NEWS
 
 
README
README
 
 
README.md
README.md
 
 
autogen.sh
autogen.sh
 
 
configure.ac
configure.ac
 
 
View all files

## Repository files navigation

## Check outhttps://github.com/philipl/inferencefs/for the latest in data-free filesystems!

# πfs: Never worry about data again!

πfs is a revolutionary new file system that, instead of wasting space storing
your data on your hard drive, stores your data in π! You'll never run out of
space again - π holds every file that could possibly exist! They said 100%
compression was impossible? You're looking at it!

πfs is dead simple to build:

Firstly, you must install autoconf, automake, libfuse packages in your system.
For example, if you have Debian try:

sudo apt-get install autotools-dev
sudo apt-get install automake
sudo apt-get install libfuse-dev

./autogen.sh
./configure
make
make install

πfs is dead simple to use:

πfs -o mdd=
<
metadata directory
>
 
<
mountpoint
>

where themetadata directoryis where πfs should store its metadata (such
as filenames or the locations of your files in π) andmountpointis your
usual filesystem mountpoint.

## What does π have to do with my data?

π (or pi) is one of the most important constants in mathematics and has a
variety of interesting properties (which you can read about atwikipedia)

One of the properties that π is conjectured to have is that it isnormal,
which is to say that its digits are all distributed evenly, with the
implication that it is adisjunctive sequence, meaning that all possible
finite sequences of digits will be present somewhere in it. If we consider
π in base 16 (hexadecimal) , it is trivial to see that if this conjecture
is true, then all possible finite files must exist within π. The first
record of this observation dates back to2001.

From here, it is a small leap to see that if π contains all possible files,
why are we wasting exabytes of space storing those files, when we could just
look them up in π!

## Every file that could possibly exist?

That's right! Every file you've ever created, or anyone else has created or
will create! Copyright infringement? It's just a few digits of π! They were
always there!

## But how do I look up my data in π?

As long as you know the index into π of your file and its length, its a
simple task to extract the file using theBailey–Borwein–Plouffe formulaSimilarly, you can use the formula to initially find the index of your file

Now, we all know that it can take a while to find a long sequence of digits
in π, so for practical reasons, we should break the files up into smaller
chunks that can be more readily found.

In this implementation, to maximise performance, we consider each individual byte
of the file separately, and look it up in π.

## So I've looked up my bytes in π, but how do I remember where they are?

Well, you've obviously got to write them down somewhere; you could use a piece of
paper, but remember all that storage space we saved by moving our data into π? Why
don't we store our file locations there!?! Even better, the location of our files in
π is metadata and aswe all knowmetadata is becoming more and more important in everything we do. Doesn't it feel
great to have generated so much metadata? Why waste time with old fashioned data
when you can just deal with metadata, and lots of it!

## Yeah, but what happens if lose my file locations?

No problem, the locations are just metadata! Your files are still there, sitting
in π - they're never going away, are they?

## Why is this thing so slow? It took me five minutes to store a 400 line text file!

Well, this is just an initial prototype, and don't worry, there's always Moore's law!

## Where do we go from here?

There's lots of potential for the future!

* Variable run length search and lookup!
* Arithmetic Coding!
* Parallelizable lookup!
* Cloud based π lookup!
* πfs for Hadoop!

## About

πfs - the data-free filesystem!

### Resources

 Readme

 

### License

 GPL-3.0 license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

7.3k

 stars
 

### Watchers

188

 watching
 

### Forks

294

 forks
 

 Report repository

 

## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* C94.4%
* M43.3%
* Shell1.3%
* Makefile1.0%