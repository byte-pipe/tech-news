---
title: filesystems - What is the purpose of the lost+found folder in Linux and Unix? - Unix & Linux Stack Exchange
url: https://unix.stackexchange.com/questions/18154/what-is-the-purpose-of-the-lostfound-folder-in-linux-and-unix
site_name: hnrss
content_file: hnrss-filesystems-what-is-the-purpose-of-the-lostfound-f
fetched_at: '2026-06-08T11:00:27.484466'
original_url: https://unix.stackexchange.com/questions/18154/what-is-the-purpose-of-the-lostfound-folder-in-linux-and-unix
date: '2026-06-05'
description: What is the purpose of the lost+found folder in Linux and Unix? (2014)
tags:
- hackernews
- hnrss
---

828 

There is a folder at the root of Linux and Unix operating systems called/lost+found/

What is it for? Under what circumstances would I interact with it? How would I interact with it?

* filesystems
* directory-structure
* lost-found

edited 
May 28, 2012 at 1:41

Gilles 'SO- stop being evil'

870k
207
207 gold badges
1.8k
1.8k silver badges
2.3k
2.3k bronze badges

 asked 
Aug 5, 2011 at 20:49

Wesley

15k
12
12 gold badges
39
39 silver badges
49
49 bronze badges

4

## 3 Answers3

 Sorted by:
 

 Reset to default
 

 Highest score (default)
 

 Date modified (newest first)
 

 Date created (oldest first)
 

715 

If you runfsck, the filesystem check and repair command, it might find data fragments that are not referenced anywhere in the filesystem. In particular,fsckmight find data that looks like a complete file but doesn't have a name on the system — aninodewith no corresponding file name. This data is still using up space, but it isn't accessible by any normal means.

If you tellfsckto repair the filesystem, it will turn these almost-deleted files back into files. The thing is, the file had a name and location once, but that information is no longer available. Sofsckdeposits the file in a specific directory, calledlost+found(afterlost and foundproperty).

Files that appear inlost+foundare typically files that were already unlinked (i.e. their name had been erased) but still opened by some process (so the data wasn't erased yet) when the system halted suddenly (kernel panic or power failure). If that's all that happened, these files were slated for deletion anyway, you don't need to care about them.

Files can also appear inlost+foundbecause the filesystem was in an inconsistent state due to a software or hardware bug. If that's the case, it's a way for you to find files that were lost but that the system repair managed to salvage. The files may or may not contain useful data, and even if they do they may be incomplete or out of date; it all depends how bad the filesystem damage was.

On many filesystems, thelost+founddirectory is a bit special because it preallocates a bit of space forfsckto deposit files there. (The space isn't for the file data, whichfsckleaves in place; it's for the directory entries whichfsckhas to make up.) If you accidentally deletelost+found, don't re-create it withmkdir, usemklost+foundif available.

edited 
Jun 21, 2014 at 19:51

Cristian Ciupitu

2,560
1
1 gold badge
23
23 silver badges
31
31 bronze badges

 answered 
Aug 5, 2011 at 21:23

Gilles 'SO- stop being evil'

870k
207
207 gold badges
1.8k
1.8k silver badges
2.3k
2.3k bronze badges

15

78 

Thelost+founddirectory (not Lost+Found) is a construct used byfsckwhen there is damage to the filesystem (not to the hardware device, but to the fs). Files that would normally be lost because of directory corruption would be linked in that filesystem'slost+founddirectory by inode number. Some of these might be lost directories or lost files or even lost devices. Each filesystem should have its ownlost+founddirectory, but you might be looking at a system with only one filesystem. In general, you should hope that the directory is empty; but if there is corruption, be thankful that in many conditions files can be recovered afterfsckplaces them here.

edited 
Feb 5, 2014 at 21:03

erch

5,260
17
17 gold badges
54
54 silver badges
86
86 bronze badges

 answered 
Aug 5, 2011 at 21:21

Arcege

23k
5
5 gold badges
59
59 silver badges
66
66 bronze badges

5

45 

From "Linux Filesystem Hierarchy", section/lost+found":

As was explained earlier during the overview of the FSSTND, Linux
 should always go through a proper shutdown. Sometimes your system
 might crash or a power failure might take the machine down. Either
 way, at the next boot, a lengthy filesystem check using fsck will be
 done. Fsck will go through the system and try to recover any corrupt
 files that it finds. The result of this recovery operation will be
 placed in this directory. The files recovered are not likely to be
 complete or make much sense but there always is a chance that
 something worthwhile is recovered. Each partition has its own
 lost+found directory. If you find files in there, try to move them
 back to their original location. If you find something like a broken
 symbolic link to 'file', you have to reinstall the file/s from the
 corresponding RPM, since your file system got damaged so badly that
 the files were mutilated beyond recognition. Below is an example of a
 /lost+found directory. As you can see, the vast majority of files
 contained here are in actual fact sockets. As for the rest of the
 other files they were found to be damaged system files and personal
 files. These files were not able to be recovered.

edited 
Jun 21, 2014 at 20:06

Cristian Ciupitu

2,560
1
1 gold badge
23
23 silver badges
31
31 bronze badges

 answered 
Aug 23, 2012 at 8:19

bhupal

451
4
4 silver badges
2
2 bronze badges

## You mustlog into answer this question.

Start asking to get answers

Find the answer to your question by asking.

Ask question

Explore related questions

* filesystems
* directory-structure
* lost-found

See similar questions with these tags.