---
title: My Backup Infrastructure, 2025 Edition
url: |
  https://borretti.me/article/my-backup-infrastructure-2025-edition
site_name: lobsters
fetched_at: |
  2025-06-01T23:46:32.834316
original_url: |
  https://borretti.me/article/my-backup-infrastructure-2025-edition
author: Fernando Borretti
date: 2025-06-01
description: How I back up my personal data.
tags: practices
---

tl;dr two portable SSDs, synced withrsync; and aBackblazebucket synced withrestic:

I’m finally satisfied with my infrastructure for backups, so I’m writing it up so others can benefit from it.

# Criteria

My requirements for backup infrastructure are:

The one non-criterion is portability. Because I only use macOS, I don’t need a solution where I can restore the backups from different operating systems.

# Local Backups

I have two portable SSDs, Chiron and Nessus, with encryptedAPFS. The filesystem itself being encrypted is extremely convenient: I just plug them in, and themacOS keychainhas the keys. There’s no possibility of accidentally leaking cleartext into the disk because the encryption is transparent.

I use rsync to synchronize the laptop to the disks. The specific incantation is:

rsync
--progress

--archive

--human-readable

--delete

\

      ~/Root/ /Volumes/Chiron/Root

Which recursively copies the contents of~/Rootinto/Volumes/Chiron/Root, preserving permissions/times/the executable flag, using checksums rather than heuristics to see which files have changed, and deleting files that exist in the target but not the source.

Note that in rsync, trailing slashes matter!rsync -a source targetcreates asourcedirectory insidetarget, whilersync -a source/ targetsyncs the contents ofsourceinsidetarget.

Why two disks? No reason.Why have one when you can have two for twice the price?

# Remote Backups

Continuing with the centaur naming convention, I have a Backblaze bucket named Pholus, and I use restic to take snapshots of the laptop and upload them to the bucket.

Why Backblaze? Because it’s cheaper thanS3, and less involved than S3 (no IAM/roles/policies/etc.), and it does one thing and does it well. I would use S3 if I already had other personal infrastructure on AWS, and latency was a problem (I’m in Australia, and Backblaze is not; with AWS I could have an S3 bucket with ~6ms latency to my home).

Why restic? Because everything else is worse.Duplicityrequires usingGnuPGfor key management, which is like if to start a car you had to stab yourself with your keys.Borgis written in Python, which is usually a bad sign for performance and user experience.Rclone, by default, is just cloud rsync, it doesn’t encrypt anything, you have to use a two-level configuration, where acryptbackend acts as a proxy to the real storage backend. So if you misconfigure things, you could end up writing cleartext to the cloud.

restic is easy to learn. The ontology is: you have a thing called arepository, which could be a local directory or a remote object store, identified by a path and locked with a password. A repository has a list of snapshots, which are like Git commits: a snapshot of a directory at a point in time. You canlsthe contents of snapshotsand evenrestore specific files, which is useful for checking that a snapshot has the data you want without restoring the whole thing.

I recommend trying out the commands usinglocalrepositories, where the data is stored in a directory. That lets you get a hang of the ontology and the commands. Then you can create a repository backed by cloud storage.

restic supports Backblaze directly, but the documentationrecommendsusing Backblaze’s S3-compatible API. To do this, when creating a bucket key you have to tick “Allow List All Bucket Names”, you will also have to know how to map the Backblaze key properties to the AWS environment variables. This is the only difficulty.

Taking a snapshot is just:

export
AWS_ACCESS_KEY_ID
=[
Backblaze keyID]

export
AWS_SECRET_ACCESS_KEY
=[
Backblaze applicationKey]

export
RESTIC_REPOSITORY
=
"s3:[bucket endpoint hostname]/[bucket name]"

restic backup ~/Root

You will then be asked to enter the repository password. For added peace of mind, you canlsthe snapshot and dump the contents of a few representative files.

# Frequency

I have a recurring task on mytodo listwhereby, once a week, I plug in the external drives, run the backup script, and also take a restic snapshot.

I could leave the drives plugged in all the time, and runrsyncautomatically every day, but my MacBook Air doesn’t have enough ports for that and, also, this risks propagating data loss to the backups, which defeats the purpose. My doing manual backups, if I lose data unintentionally, I have up to a week to notice and restore it from the SSD.
