---
title: filesystems - What is the purpose of the lost+found folder in Linux and Unix? - Unix & Linux Stack Exchange
url: https://unix.stackexchange.com/questions/18154/what-is-the-purpose-of-the-lostfound-folder-in-linux-and-unix
date: 2026-06-05
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-06-08T11:01:54.588199
---

# filesystems - What is the purpose of the lost+found folder in Linux and Unix? - Unix & Linux Stack Exchange

# What is the purpose of the lost+found folder in Linux/Unix?

## Overview
- **lost+found** is a special directory created at the root of each filesystem.  
- It is used by the filesystem check utility **fsck** to store recovered file fragments when the filesystem becomes inconsistent.

## When and why files appear there
- **Unclean shutdown** (power loss, kernel panic) can leave files that were unlinked but still open; their data remains on disk but their name is lost.  
- **Filesystem corruption** caused by software or hardware bugs may leave orphaned inodes.  
- In both cases, fsck repairs the filesystem and places these orphaned files in **lost+found**.

## Characteristics of the recovered items
- Usually named by inode number, not by original filename.  
- May be complete, partial, or completely corrupted; usefulness varies.  
- Often they are sockets, broken symbolic links, or remnants of system/personal files.

## Interaction with the directory
- Normally the directory stays empty; users rarely need to touch it.  
- If files are present, you can inspect them and, if recognizable, move them back to their proper location.  
- Do **not** recreate the directory with `mkdir`; if it is accidentally removed, use `mklost+found` (when available) because the directory pre‑allocates space for fsck’s directory entries.

## Summary
- **lost+found** is a safety net for orphaned data recovered by **fsck** after crashes or corruption.  
- It allows the system to salvage potentially valuable data, though the recovered files may be incomplete or unusable.  
- Users generally ignore it unless they need to recover specific files after a filesystem repair.