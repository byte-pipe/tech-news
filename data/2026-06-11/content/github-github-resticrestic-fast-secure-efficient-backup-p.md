---
title: 'GitHub - restic/restic: Fast, secure, efficient backup program · GitHub'
url: https://github.com/restic/restic
site_name: github
content_file: github-github-resticrestic-fast-secure-efficient-backup-p
fetched_at: '2026-06-11T12:23:31.935536'
original_url: https://github.com/restic/restic
author: restic
description: Fast, secure, efficient backup program. Contribute to restic/restic development by creating an account on GitHub.
---

restic

 

/

restic

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.8k
* Star34k

 
 
 
 
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

9,658 Commits
9,658 Commits
.github
.github
 
 
changelog
changelog
 
 
cmd/
restic
cmd/
restic
 
 
contrib
contrib
 
 
doc
doc
 
 
docker
docker
 
 
helpers
helpers
 
 
internal
internal
 
 
.codespellrc
.codespellrc
 
 
.dockerignore
.dockerignore
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.golangci.yml
.golangci.yml
 
 
.readthedocs.yaml
.readthedocs.yaml
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
GOVERNANCE.md
GOVERNANCE.md
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
VERSION
VERSION
 
 
build.go
build.go
 
 
doc.go
doc.go
 
 
go.mod
go.mod
 
 
go.sum
go.sum
 
 
View all files

## Repository files navigation

# Introduction

restic is a backup program that is fast, efficient and secure. It supports the three major operating systems (Linux, macOS, Windows) and a few smaller ones (FreeBSD, OpenBSD).

For detailed usage and installation instructions check out thedocumentation.

You can ask questions in ourDiscourse forum.

## Quick start

Once you'veinstalledrestic, start
off with creating a repository for your backups:

$ restic init --repo /tmp/backup
enter password for new backend:
enter password again:
created restic backend 085b3c76b9 at /tmp/backup
Please note that knowledge of your password is required to access the repository.
Losing your password means that your data is irrecoverably lost.

and add some data:

$ restic --repo /tmp/backup backup ~/work
enter password for repository:
scan [/home/user/work]
scanned 764 directories, 1816 files in 0:00
[0:29] 100.00% 54.732 MiB/s 1.582 GiB / 1.582 GiB 2580 / 2580 items 0 errors ETA 0:00
duration: 0:29, 54.47MiB/s
snapshot 40dc1520 saved

Next you can either userestic restoreto restore files or userestic mountto mount the repository via fuse and browse the files from previous
snapshots.

For more options check out theonline documentation.

# Backends

Saving a backup on the same machine is nice but not a real backup strategy.
Therefore, restic supports the following backends for storing backups natively:

* Local directory
* sftp server (via SSH)
* HTTP REST server(protocol,rest-server)
* Amazon S3(either from Amazon or using theMinioserver)
* OpenStack Swift
* BackBlaze B2
* Microsoft Azure Blob Storage
* Google Cloud Storage
* And many other services via thercloneBackend

# Design Principles

Restic is a program that does backups right and was designed with the
following principles in mind:

* Easy: Doing backups should be a frictionless process, otherwise
you might be tempted to skip it. Restic should be easy to configure
and use, so that, in the event of a data loss, you can just restore
it. Likewise, restoring data should not be complicated.
* Fast: Backing up your data with restic should only be limited by
your network or hard disk bandwidth so that you can backup your files
every day. Nobody does backups if it takes too much time. Restoring
backups should only transfer data that is needed for the files that
are to be restored, so that this process is also fast.
* Verifiable: Much more important than backup is restore, so restic
enables you to easily verify that all data can be restored.
* Secure: Restic uses cryptography to guarantee confidentiality and
integrity of your data. The location the backup data is stored is
assumed not to be a trusted environment (e.g. a shared space where
others like system administrators are able to access your backups).
Restic is built to secure your data against such attackers.
* Efficient: With the growth of data, additional snapshots should
only take the storage of the actual increment. Even more, duplicate
data should be de-duplicated before it is actually written to the
storage back end to save precious backup space.

# Reproducible Builds

The binaries released with each restic version starting at 0.6.1 arereproducible, which means that you can
reproduce a byte identical version from the source code for that
release. Instructions on how to do that are contained in thebuilder repository.

## News

You can follow the restic project on Mastodon@resticbackupor subscribe to
theproject blog.

## License

Restic is licensed underBSD 2-Clause License. You can find the
complete text inLICENSE.

## Sponsorship

Backend integration tests for Google Cloud Storage and Microsoft Azure Blob
Storage are sponsored byAppsCode!

## About

Fast, secure, efficient backup program

restic.net

### Topics

 go

 backup

 dedupe

 secure-by-default

 restic

 deduplication

### Resources

 Readme

 

### License

 BSD-2-Clause license
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

34k

 stars
 

### Watchers

228

 watching
 

### Forks

1.8k

 forks
 

 Report repository

 

## Releases50

restic 0.19.0

 Latest

 

Jun 9, 2026

 

+ 49 releases

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Go99.8%
* Other0.2%