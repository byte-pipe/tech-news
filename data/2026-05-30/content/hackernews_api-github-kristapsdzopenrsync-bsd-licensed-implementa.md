---
title: 'GitHub - kristapsdz/openrsync: BSD-licensed implementation of rsync · GitHub'
url: https://github.com/kristapsdz/openrsync
site_name: hackernews_api
content_file: hackernews_api-github-kristapsdzopenrsync-bsd-licensed-implementa
fetched_at: '2026-05-30T19:34:01.868740'
original_url: https://github.com/kristapsdz/openrsync
author: sph
date: '2026-05-30'
description: BSD-licensed implementation of rsync. Contribute to kristapsdz/openrsync development by creating an account on GitHub.
tags:
- hackernews
- trending
---

kristapsdz

 

/

openrsync

Public

* NotificationsYou must be signed in to change notification settings
* Fork32
* Star623

 
 
 
 
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

419 Commits
419 Commits
.github/
workflows
.github/
workflows
 
 
.gitignore
.gitignore
 
 
LICENSE.md
LICENSE.md
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
TODO.md
TODO.md
 
 
blocks.c
blocks.c
 
 
charclass.h
charclass.h
 
 
client.c
client.c
 
 
compats.c
compats.c
 
 
configure
configure
 
 
copy.c
copy.c
 
 
downloader.c
downloader.c
 
 
extern.h
extern.h
 
 
fargs.c
fargs.c
 
 
flist.c
flist.c
 
 
hash.c
hash.c
 
 
ids.c
ids.c
 
 
io.c
io.c
 
 
log.c
log.c
 
 
main.c
main.c
 
 
md4.c
md4.c
 
 
md4.h
md4.h
 
 
misc.c
misc.c
 
 
mkpath.c
mkpath.c
 
 
mktemp.c
mktemp.c
 
 
openrsync.1
openrsync.1
 
 
receiver.c
receiver.c
 
 
rmatch.c
rmatch.c
 
 
rsync.5
rsync.5
 
 
rsyncd.5
rsyncd.5
 
 
rules.c
rules.c
 
 
sender.c
sender.c
 
 
server.c
server.c
 
 
session.c
session.c
 
 
socket.c
socket.c
 
 
symlinks.c
symlinks.c
 
 
tests.c
tests.c
 
 
uploader.c
uploader.c
 
 
View all files

## Repository files navigation

# Introduction

This system has been merged into OpenBSD base. If you'd like to
contribute to openrsync, please mail your patches totech@openbsd.org.
This repository is simply the OpenBSD version plus some glue for
portability.

This is an implementation ofrsyncwith a
BSD (ISC) license. It's compatible with a modern rsync (3.1.3 is used
for testing, but any supporting protocol 27 will do), but accepts only a
subset of rsync's command-line arguments.

Its officially-supported operating system is OpenBSD, but it will
compile and run on other UNIX systems. SeePortabilityfor details.

The canonical documentation for openrsync is its manual pages. Seersync(5)andrsyncd(5)for protocol details or utility documentation inopenrsync(1).
If you'd like to write your own rsync implementation, the protocol
manpages should have all the information required.

TheArchitectureandAlgorithmsections
on this page serve to introduce developers to the source code. They are
non-canonical.

## Project background

openrsync is written as part of therpki-client(1)project, anRPKIvalidator for OpenBSD. openrsync was funded byNetNod,IIS.SE,SUNETand6connect.

# Installation

On an up-to-date UNIX system, simply download and run:

% ./configure
% make
# make install

This will install the openrsync utility and manual pages.
It's ok to have an installation of rsync at the same time: the two will
not collide in any way.

If you upgrade your sources and want to re-install, just run the same.
If you'd like to uninstall the sources:

# make uninstall

If you'd like to interact with the openrsync as a server, you can run
the following:

% rsync --rsync-path=openrsync src/* dst
% openrsync --rsync-path=openrsync src/* dst

If you'd like openrsync and rsync to interact, it's important to use
command-line flags available on both.
Seeopenrsync(1)for a listing.

# Algorithm

For a robust description of the rsync algorithm, see "The rsync
algorithm", by Andrew Tridgell
and Paul Mackerras.
Andrew Tridgell's PhD thesis, "Efficient Algorithms for Sorting and
Synchronization", covers the
topics in more detail.
This gives a description suitable for delving into the source code.

The rsync algorithm has two components: thesenderand thereceiver.
The sender manages source files; the receiver manages the destination.
In the following invocation, first the sender is hostremoteand the
receiver is the localhost, then the opposite.

% openrsync -lrtp remote:foo/bar ~/baz/xyzzy
% openrsync -lrtp ~/foo/bar remote:baz/xyzzy

The algorithm hinges upon a file list of names and metadata (e.g., mode,
mtime, etc.) shared between components.
The file list describes all source files of the update and is generated
by the sender.
The sharing is implemented inflist.c.

After sharing this list, both the receiver and sender independently sort
the entries by the filenames' lexicographical order.
This allows the file list to be sent and received out of order.
The ordering preserves a directory-first order, so directories are
processed before their contained files.
Moreover, once sorted, both sender and receiver may refer to file
entries by their position in the sorted array.

After the receiver reads the list, it iterates through each file in
the list, passing information to the sender so that the sender may send
back instructions to update the file.
This is called the "block exchange" and is the maintstay of the rsync
algorithm.
During the block exchange, the sender waits to receive a request for
update or end of sequence message; once a request is received, it scans
for new blocks to send to the receiver.

Once the block exchange is complete, the files are all up to date.

The receiver is implemented inreceiver.c;
the sender, insender.c.
A great deal of the block exchange happens inblocks.c.

## Block exchange

The block exchange sequence is different for whether the file is a
directory, symbolic link, or regular file.

For symbolic links, the information required by the receiver is already
encoded in the file list metadata.
The symbolic link is updated to point to the correct target.
No update is requested from the sender.

For directories, the directory is created if it does not already exist.
No update is requested from the sender.

Regular files are handled as follows.
First, the file is checked to see if it's up to date.
This happens if the file size and last modification time are the same.
If so, no update is requested from the sender.

Otherwise, the receiver examines each file in blocks of a fixed size.
SeeBlock sizesfor details.
(The terminal block may be smaller if the file size is not divisible by
the block size.)
If the file is empty or does not exist, it will have zero blocks.
Each block is hashed twice: first, with a fast Adler-32 type 4-byte
hash; second, with a slower MD4 16-byte hash.
These hashes are implemented inhash.c.
The receiver sends the file's block hashes to the sender.

Once accepted, the sender examines the corresponding file with the given
blocks.
For each byte in the source file, the sender computes a fast hash given
the block size.
It then looks for matching fast hashes in the sent block information.
If it finds a match, it then computes and checks the slow hash.
If no match is found, it continues to the next byte.
The matching (and indeed all block operation) is implemented inblock.c.

When a match is found, the data prior to the match is first sent as a
stream of bytes to the receiver.
This is followed by an identifier for the found block, or zero if no
more data is forthcoming.

The receiver writes the stream of bytes first, then copies the data in
the identified block if one has been specified.
This continues until the end of file, at which point the file has been
fully reconstituted.

If the file does not exist on the receiver side---the basis case---the
entire file is sent as a stream of bytes.

Following this, the whole file is hashed using an MD4 hash.
These hashes are then compared; and on success, the algorithm continues
to the next file.

## Block sizes

The block size algorithm plays a crucial role in the protocol
efficiency.
In general, the block size is the rounded square root of the total file
size.
The minimum block size, however, is 700 B.
Otherwise, the square root computation is simplysqrt(3)followed byceil(3)

For reasons unknown, the square root result is rounded up to the nearest
multiple of eight.

# Architecture

Each openrsync session is divided into a runningserverandclientprocess.
The client openrsync process is executed by the user.

% openrsync -rlpt host:path/to/source dest

The server openrsync is executed on a remote host either on-demand overssh(1)or as a persistent network
daemon.
If executed overssh(1), the server
openrsync is distinguished from a client (user-started) openrsync by the--serverflag.

Once the client or server openrsync process starts, it examines the
command-line arguments to determine whether it's inreceiverorsendermode.
(The daemon is sent the command-line arguments in a protocol-specific
way described inrsyncd(5),
but otherwise does the same thing.)
The receiver is the destination for files; the sender is the origin.
There is always one receiver and one sender.

The server process is explicitly instructed that it is a sender with the--sendercommand-line flag, otherwise it is a receiver.
The client process implicitly determines its status by looking at the
files passed on the command line for whether they are local or remote.

openrsync path/to/source host:destination
openrsync host:source path/to/destination

In the first example, the client is the sender: itsendsdata from
itself to the server.
In the second, the opposite is true in that itreceivesdata.

The client's command-line files may have any of the following host
specifications that determine locality.

* local:../path/to/source ../another
* remote server:host:path/to/source :path/to/another
* remote daemon:rsync://host/module/path ::another

Host specifications must be consistent: sources must all be local or all
be remote on the same host. Both may not be remote. (Aside: it's
technically possible to do this. I'm not sure why the GPL rsync is
limited to one or the other.)

If the source or destination is on a remote server, the client thenfork(2)s and starts the server
openrsync on the remote host overssh(1).
The client and the server subsequently communicate oversocketpair(2)pipes.
If on a remote daemon, the client doesnotfork, but instead connects
to the standalone server with a networksocket(2).

The server's command-line, whether passed to an openrsync spawned on-demand
over anssh(1)session or passed to the daemon,
differs from the client's.

openrsync --server [--sender] . files...

The files given are either the single destination directory when in receiver
mode, or the list of sources when in sender mode.
The standalone full-stop is a mystery to me.

Locality detection and routing to client and server run-times are
handled inmain.c.
The client for a server is implemented inclient.cand the server inserver.c.
The client for a network daemon is insocket.c.
Invocation of the remote server openrsync is managed inchild.c.

Once the client and server begin, they start to negotiate the transfer
of files over the connected socket.
The protocol used is specified inrsync(5).
For daemon connections, thersyncd(5)protocol is also used for handshaking.

The receiver side is managed inreceiver.cand the sender insender.c.

The receiver side technically has two functions: not only must it upload
block metadata to the sender, it must also handle data writes as they
are sent by the sender.
The rsync protocol is designed so that the sender receives block
requests and continuously sends data to the receiver.

To accomplish this, the receiver multitasks as theuploaderanddownloader. These roles are implemented inuploader.c.
anddownloader.c,
respectively.
The multitasking takes place by a finite state machine driven by data
coming from the sender and files on disc are they are ready to be
checksummed and uploaded.

The uploader scans through the list of files and asynchronously opens
files to process blocks.
While it waits for the files to open, it relinquishes control to the
event loop.
When files are available, it hashes and checksums blocks and uploads to
the sender.

The downloader waits on data from the sender.
When data is ready (and prefixed by the file it will update), the
downloader asynchronously opens the existing file to perform any block
copying.
When the file is available for reading, it then continues to read data
from the sender and copy from the existing file.

## Differences from rsync

The design of rsync involves another mode running alongside the
receiver: the generator.
This is implemented as another processfork(2)ed from the receiver, and
communicating with the receiver and sender.

In openrsync, the generator and receiver are one process, and an event
loop is used for speedy responses to read and write requests.

# Security

Besides the usual defensive programming, openrsync makes significant use
of native security features.

The system operations available to executing code are foremost limited
by OpenBSD'spledge(2). The pledges
given depend upon the operating mode. For example, the receiver needs
write access to the disc---but only when not in dry-run mode (-n).
The daemon client needs DNS and network access, but only to a point.pledge(2)allows available resources
to be limited over the course of operation.

The second tool is OpenBSD'sunveil(2), which limits access to
the file-system. This protects against rogue attempts to "break out" of
the destination. It's an attractive alternative tochroot(2)because it doesn't require
root permissions to execute.

On the receiver side, the file-system isunveil(2)ed at and beneath the
destination directory.
After the creation of the destination directory, only targets within
that directory may be accessed or modified.

Lastly, the MD4 hashs are seeded witharc4random(3)instead of withtime(3). This is only applicable when
running openrsync in server mode, as the server generates the seed.

# Portability

Many have asked about portability.

The only officially-supported operating system is OpenBSD, as this has
considerable security features. openrsync does, however, useoconfigurefor compilation
on non-OpenBSD systems. This is to encourage porting.

It currently is portable across Linux (glibc and musl), FreeBSD, NetBSD,
Mac OS X, and OmniOS. This is enforced by the GitHub CI mechanism,
which tests on this systems. Architectures tested for include x86_64,
aarch64, and s390x.

The actual work of porting is matching the security features provided by
OpenBSD'spledge(2)andunveil(2). These are critical
elements to the functionality of the system. Without them, your system
accepts arbitrary data from the public network.

This is possible (I think?) with FreeBSD'sCapsicum, but Linux's security
facilities are a mess, and will take an expert hand to properly secure.

rsync has specific running modes for the super-user.
It also pumps arbitrary data from the network onto your file-system.
openrsync is about 10 000 lines of C code: do you trust me not to make
mistakes?

## About

BSD-licensed implementation of rsync

### Topics

 rsync

### Resources

 Readme

 

### License

 ISC license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

623

 stars
 

### Watchers

18

 watching
 

### Forks

32

 forks
 

 Report repository

 

## Releases

6

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

* C94.0%
* Roff5.7%
* Makefile0.3%