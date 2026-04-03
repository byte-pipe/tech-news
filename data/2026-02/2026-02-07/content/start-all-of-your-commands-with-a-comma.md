---
title: Start all of your commands with a comma
url: https://rhodesmill.org/brandon/2009/commands-with-comma/
site_name: hackernews
fetched_at: '2026-02-07T19:10:29.912362'
original_url: https://rhodesmill.org/brandon/2009/commands-with-comma/
author: theblazehen
date: '2026-02-07'
---

by Brandon Rhodes
 •Home

# Start all of your commands with a comma

Date:

18 August 2009

Tags:
computing

Like many Unix users,
 I long ago created a~/bin/directory in my home directory
 and added it to myPATHso that I could supplement
 the wonderfully rich set of basic Unix commands
 with some conveniences and shell scripts of my own devising.

The problem, of course, was the chance of collision.
 Because my shell script names
 tended to be short and pithy collections of lowercase characters,
 just like the default system commands,
 there was no telling when Linux would add a new command
 that would happen to have the same name as one of mine.
 This was actually not very likely on,
 say, a System V Revision 3 workstation in the 1980s,
 but the trouble became quite a bit more acute
 when I moved into the world of Debian.
 Red Hat never really worried me,
 because they packaged (comparatively) so little software.
 But Debian today supports a huge number of commands;
 my modest Ubuntu laptop shows several thousand available:

$

apt
-
file

search

-
x

'
^/
usr
/
bin
/
[
^/
]
*
$'

|

wc

-
l

21733

The solution was obviously to adjust my command names
 in such a way that they were still easy to type,
 but would never be chosen as system command names.
 For me, “easy to type” means not having to use the shift key,
 and very few characters turned out to be available,
 unshifted, on a modern keyboard.
 The lower-case letters
 are the very characters used in system commands;
 brackets, backslashes, the colon, the back-tick, and the single-tick
 all had a special meaning to the shell;
 and the slash and dot characters both mean something special
 in a filename.
 (The slash divides directory names from filenames,
 and thus cannot appear in a filename itself,
 while the dot means “hide this file from normal browsing”
 if it leads the name,
 and separates a file from its extension in many other cases.)

There was but one character left: the simple, modest comma.

A quick experiment revealed in a flash
 that the comma wasexactlythe character
 that I had been looking for!
 Every tool and shell that lay in arm's reach
 treated the comma as a perfectly normal
 and unobjectionable character in a filename.
 By simply prefixing each of my custom commands
 with a comma,
 they became completely distinct from system commands
 and thus free from any chance of a collision.

And, best of all,
 thanks to the magic of tab-completion,
 it became very easy to browse my entire collection of commands.
 When trying to remember which of my commands
 are available in my~/bin/directory on a given system,
 or when simply trying to remember what
 some of my commands are called,
 I simply type a comma followed bytaband my list of commands appears:

$ ,
«tab»

,complete-scp ,go-thpgp ,range
,complete-ssh ,gr ,svn-store-password
,coreoff ,hss ,umount
,coreon ,mount-thpgp
,find ,mount-twt

I heartily recommend this technique
 to anyone with their own~/bin/directory
 who wants their command names kept clean, tidy,
 and completely orthogonal
 to any commands that the future might bring to your system.
 The approach has worked for me for something like a decade,
 so you should find it immensely robust.
 And, finally, it's just plain fun.

©2021
