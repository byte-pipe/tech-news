---
title: 'Excessive IO caused by systemd-journald · Issue #40262 · systemd/systemd · GitHub'
url: https://github.com/systemd/systemd/issues/40262
site_name: hnrss
content_file: hnrss-excessive-io-caused-by-systemd-journald-issue-4026
fetched_at: '2026-08-14T11:43:21.982813'
original_url: https://github.com/systemd/systemd/issues/40262
date: '2026-08-13'
description: systemd version the issue has been seen with 257.9 Used distribution Debian 13 Linux kernel version used 6.12.57+deb13-amd64 Component systemd-journald Expected behaviour you didn't see Log writes should be within order of magnitude of s...
tags:
- hackernews
- hnrss
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 systemd

 

/

systemd

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork4.6k
* Star16.6k

# Excessive IO caused by systemd-journald#40262

Open
Open
Excessive IO caused by systemd-journald
#40262
Labels
bug 🐛
Programming errors, that need preferential fixing
Programming errors, that need preferential fixing
journal

## Description

XANi
opened 
on Jan 3, 2026
Issue body actions

### systemd version the issue has been seen with

257.9

### Used distribution

Debian 13

### Linux kernel version used

6.12.57+deb13-amd64

### Component

systemd-journald

### Expected behaviour you didn't see

Log writes should be within order of magnitude of syslog

### Unexpected behaviour you saw

VM doing ~50 IOPS when writing 2 lines of log per second

### Steps to reproduce the problem

this is exactly same issue#15292that was closed without good reason

Step 1. Use journald in mode where it writes to hard drive. The FS is XFS

Step 2. have constant stream of log entries going on a VM

Jan 03 13:37:01 cthylla haproxy[727]: 192.168.1.1:48550 [03/Jan/2026:13:37:01.392] f_www b_icinga/web 0/0/0/6/6 302 153 - - ---- 2/2/0/0/0 0/0 "GET / HTTP/1.0"
Jan 03 13:37:03 cthylla haproxy[727]: 192.168.1.1:36892 [03/Jan/2026:13:37:03.403] f_www b_icinga/web 0/0/0/7/7 302 153 - - ---- 2/2/0/0/0 0/0 "GET / HTTP/1.0"
Jan 03 13:37:05 cthylla haproxy[727]: 192.168.1.1:36904 [03/Jan/2026:13:37:05.416] f_www b_icinga/web 0/0/0/6/6 302 153 - - ---- 2/2/0/0/0 0/0 "GET / HTTP/1.0"
Jan 03 13:37:07 cthylla haproxy[727]: 192.168.1.1:36906 [03/Jan/2026:13:37:07.427] f_www b_icinga/web 0/0/0/6/6 302 153 - - ---- 2/2/0/0/0 0/0 "GET / HTTP/1.0"
Jan 03 13:37:09 cthylla haproxy[727]: 192.168.1.1:36912 [03/Jan/2026:13:37:09.439] f_www b_icinga/web 0/0/0/7/8 302 153 - - ---- 2/2/0/0/0 0/0 "GET / HTTP/1.0"
Jan 03 13:37:11 cthylla haproxy[727]: 192.168.1.1:36918 [03/Jan/2026:13:37:11.454] f_www b_icinga/web 0/0/0/6/6 302 153 - - ---- 2/2/0/0/0 0/0 "GET / HTTP/1.0"
Jan 03 13:37:13 cthylla haproxy[727]: 192.168.1.1:45832 [03/Jan/2026:13:37:13.465] f_www b_icinga/web 0/0/0/7/7 302 153 - - ---- 2/2/0/0/0 0/0 "GET / HTTP/1.0"
Jan 03 13:37:15 cthylla haproxy[727]: 192.168.1.1:45848 [03/Jan/2026:13:37:15.476] f_www b_icinga/web 0/0/0/6/6 302 153 - - ---- 2/2/0/0/0 0/0 "GET / HTTP/1.0"
Jan 03 13:37:17 cthylla haproxy[727]: 192.168.1.1:45856 [03/Jan/2026:13:37:17.488] f_www b_icinga/web 0/0/0/6/6 302 153 - - ---- 2/2/0/0/0 0/0 "GET / HTTP/1.0"
Jan 03 13:37:19 cthylla haproxy[727]: 192.168.1.1:45862 [03/Jan/2026:13:37:19.500] f_www b_icinga/web 0/0/0/6/6 302 153 - - ---- 2/2/0/0/0 0/0 "GET / HTTP/1.0"

Step 3. Observe the VM IO traffic.

I used VM as example because the complaint in#15292was "iotop is not accurate" (I can believe that, it's before any OS write coaelscing) but this clearly shows traffic after every kernel mechanism was used. So no, it isn't "kernel making lotsa iops out of it", it's slow.

Journald just uses extremely inefficient format (also I've seen it corrupt on unclean reboot enough times to declare it's not even all that resilient) as files are also multiple times the size of what's actually written in them.

Reactions are currently unavailable

## Metadata

## Metadata