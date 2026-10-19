---
title: The 7.3 kernel has been released [LWN.net]
url: https://lwn.net/Articles/1101143/
site_name: hackernews_api
content_file: hackernews_api-the-73-kernel-has-been-released-lwnnet
fetched_at: '2026-10-19T17:20:36.094315'
original_url: https://lwn.net/Articles/1101143/
author: cjd8
date: '2026-10-19'
description: Linux 7.3
tags:
- hackernews
- trending
---

Linus Torvalds has 
released
 the 7.3
kernel, as expected.

It's Sunday afternoon, and this week I somehow kept my wits
	together long enough to keep track of the day of the week, so the
	release isn't randomly delayed. Will wonders never cease?Anyway, nothing very special seems to have happened this last week,
	so as expected the final 7.3 is out, and thus tomorrow the merge
	window for 7.4 opens. Except I'm on my annual family vacation, so
	instead of merging anything first thing in the morning, I'll spend
	most of the day on a boat and under water. I'll get back to merging
	in the afternoon, but I expect my schedule to be a bit unusual for
	a while.This release is a record-breaker on all fronts; it brought in 18,765
non-merge commits from 3,021 developers, 807 of whom were first-time kernel
developers.Significant changes in this release include somesignificant binfmt_misc extensions, somegroup-scheduling workaimed at improving performance on large systems, the newfailfsfilesystem that fails all operations, thefchroot()system call,
global per-CPU data for BPF programs, thecompletionofthe sched_ext subscheduler feature,working-set trackingfor virtual
machines,alternative
data-stream supportin the ntfs3 filesystem,
along
list of SMB server improvements,
and much more. See the LWN merge-window summaries 
(part 1,part 2) andthe KernelNewbies 7.3 pagefor details.to post comments### yay!Posted Oct 18, 2026 23:52 UTC (Sun)
 byjpeisach(subscriber, #181966)
 [Link]looking forward to the final dev stats!### Recent documentation / introductory books for newcomersPosted Oct 19, 2026 2:57 UTC (Mon)
 byswilmet(subscriber, #98424)
 [Link] (3 responses)For consuming kernel features from userspace, there is theThe Linux Programming Interface(thick) book, but the latest edition dates back from 2010; thankfully there is apage listing what's newsince then.For an introductory book/documentation about Linux kernel development itself, what would you recommend nowadays? I know there isLinux Device Drivers, but it becomes a bit old I suppose.What resources would you recommend nowadays?(It's just for my own curiosity, but answering the question could help other readers).### Recent documentation / introductory books for newcomersPosted Oct 19, 2026 10:19 UTC (Mon)
 byeru(subscriber, #2753)
 [Link]I believe one recommended stating point ishttps://kernelnewbies.org/.### Recent documentation / introductory books for newcomersPosted Oct 19, 2026 15:16 UTC (Mon)
 byDragoonAethis(guest, #187211)
 [Link]Unfortunately, TLPI's What's New seems to be updated only with new release numbers at this point :(### Recent documentation / introductory books for newcomersPosted Oct 19, 2026 15:19 UTC (Mon)
 bycorbet(editor, #1)
 [Link]The kernel'sdevelopment-process documentationis a bit better maintained than much of the rest, and has a lot of necessary reading for new developers.### Submerge before mergePosted Oct 19, 2026 9:53 UTC (Mon)
 byteknohog(subscriber, #70891)
 [Link] (1 responses)> I'll spend most of the day on a boat and under water. I'll get back to merging in the afternoonSo before the Linux merge window, there's the Linus submerge window. (I'll get my coat!)### Submerge before mergePosted Oct 19, 2026 10:30 UTC (Mon)
 byzdzichu(subscriber, #17118)
 [Link]Quote of the week material.