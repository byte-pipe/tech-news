---
title: 'Nitpicking the shell history scene in ‘Tron: Legacy’'
url: https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/tron-legacy/
site_name: hnrss
content_file: hnrss-nitpicking-the-shell-history-scene-in-tron-legacy
fetched_at: '2026-05-29T12:07:06.079084'
original_url: https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/tron-legacy/
date: '2026-05-28'
description: 'Nitpicking the shell history scene in ''Tron: Legacy'''
tags:
- hackernews
- hnrss
---

# Nitpicking the shell history scene inTron: Legacy

[Simon Tatham, 2026-05-28]

* Introduction
* Spoilers
* The screenshotText transcript
* Text transcript
* What can we observe from this screenshot?
* Summary
* Addendum: thoughts from the Internet
* Footnote

## Introduction

In the 2010 filmTron: Legacy, there's a scene
 where the main character Sam Flynn sits down at a computer in
 his father’s study, and types some commands to try to figure out
 what Flynn senior had last been working on, before mysteriously
 disappearing.

When I first watched the film (conveniently, already on DVD), I
 paused it so that I could have a close look at the text on the
 computer screen. What can I say? I’m that kind of geek.

TheTronfilm series as a whole is based on
 somecompletelyludicrous premises about how computers
 work. So I wasn’t expecting realism; more likely I thought it
 would be hilarious fake-computerese nonsense made up entirely by
 movie people. In fact I saw analmostplausible Unix
 shell transcript, whose contents made sense in the context of
 the film plot – albeit with a couple of nits that jumped out at
 me immediately.

This year, I remembered that scene, and thought it might make a
 good learning exercise for a junior colleague: let’s look at
 that still image together and see how much we can understand
 about it. Can we find all the outright errors? Disregarding
 things we’ve definitely decided are errors, what can we infer
 from the rest of it about the computer system and what the
 Flynns (both of them) are doing with it?

I hoped this might be fun, interesting, and/or educational. It
 succeeded at all three, beyond my hopes! Instead of the half
 hour I’d guessed, we spent a whole day on it, on and off
 (exchanging Slack messages, in between other work), and squeezed
 a lot more juice out of it than I’d realised was there to be
 squozen. By the end of the exercise, I’d decided one of my own
 initial complaints was wrong (but found another to replace it),
 and I’d learned some new things myself. And I ended up more
 impressed than I’d started, with whoever constructed that
 screenshot.

So, since it ended up being that much fun, here’s a writeup, so
 that if you’re the same kind of geek as me, you can share the
 enjoyment!

## Spoilers

This article will include a minor spoiler for a thing that
 happens in the film. But it won’t be anything you couldn’t
 easily have guessed was going to appearsomewherein
 the film, just from having watched the original 1982 film that
 this is a sequel to,Tronitself. In any case,
 evenTron: Legacyis 16 years old by now and
 anotherTronfilm has come out since, so if you
 care about spoilers for it at all, you’ve probably already seen
 it.

More to the point, when I set this exercise to my colleague, it
 was intended as an educational puzzle – the point was
 towork outthe answers, not just hear them in the form
 of a lecture. So I’m going to take care not to spoil that
 puzzle. In this article I’ll present all the answers I have, but
 they’re below a<details>fold, so you can
 examine the transcript yourself before clicking through, and see
 how much you can get from it yourself.

## The screenshot

Of course I have to start by showing a still image from the
 film. My understanding (though I am not a lawyer) is that this
 should be justifiable under copyright law1I’m
 sitting in the UK as I write this. Under UK law, I believe this
 should constitute fair dealing: the purpose is quotation for
 criticism and review, and this single screen capture is in no
 way an alternative to paying to see the original film. The film
 comes from the USA, and under USA law I think it similarly
 constitutes fair use: it’s for non-profit educational purposes,
 the amount of the full work used is extremely small, and the
 effect on the value of the full work negligible.1.
 However, of course, I don’t have the resources to defend myself
 in a serious fight against Disney, so if they should demand that
 I take the image down, I’ll have no choice but to do so.

The smears in front of the text, and the uneven background
 colour behind it, are because the screen is a reflective desk
 surface which had a thick layer of dust all over it until a
 moment ago; just before Sam sat down, we saw him wipe some of
 the dust off.

When Sam arrived, the main shell window on the right was empty.
 Everything shown in it here is commands he typed himself just
 now, and the computer’s responses to those commands.

### Text transcript

I’ve typed this out by hand so that you don’t have to: here’s a
 text transcript of the session in that main shell window.

$ whoami
flynn
$ uname -a
SolarOS 4.0.1 Generic_50203-02 sun4m i386
Unknown.Unknown
$ login -n root
Login incorrect
login: backdoor
No home directory specified in password file!
Logging in with home=/
# bin/history
 488 cd /opt/LLL/controller/laser/
 489 vi LLLSDLaserControl.c
 490 make
 491 make install
 492 ./sanity_check
 493 ./configure -o test.cfg
 494 vi test.cfg
 495 vi ~/last_will_and_testament.txt
 496 cat /proc/meminfo
 497 ps -a -x -u
 498 kill -9 2207
 499 kill 2208
 500 ps -a -x -u
 501 touch /opt/LLL/run/ok
 502 LLLSDLaserControl -ok 1
# 

## What can we observe from this screenshot?

If you’re up for trying this exercise yourself, have a good
 look at the image above, and see what you can see. When you’re
 ready, click through the cut below, and you’ll see a list of
 topics to think about. If those give you useful hints, you’ve
 got another chance to think harder about each one, before you
 open each topic in turn to see the thoughts we had about it.

Topic list

The command that prints the shell history

This was the very first thing that jumped out at me when
 I first watched this film and paused the DVD. Sam requests
 the shell history by runningbin/historyinstead of justhistory. Why?

I can’t see any possible way that makes sense on real
 Unix. Shell history is stored in data structures inside
 the shell process itself, so thehistorycommand must be a shell builtin, in order to read out
 those structures. Even if you only wanted to read out the
 version of the history stored in a disk file, the name and
 location of that file varies with the shell and its
 configuration, so an external command that
 didthatwould still be very difficult to get
 right.

My conclusion at the time – and it still seems fairly
 plausible to me now – is that this is revealing the
 technique the filmmakers used to present their fake
 plot-related shell history. (Like an accidental visible
 wire, in wire-fu.) I think this shell session was
 generated by typing commands into a real, carefully
 configured, Unix machine, andbin/historywas
 a simple shell script that printsthathistory in
 place of whatever more boring thing existed in the real
 shell.

(Note, in particular, that the history doesn’t end with
 the commandbin/history! When you run a real
 shell history command, generally the output ends with the
 veryhistorycommand you just typed, because
 it’s been inserted into the history list before the
 history list is read back out.)

Supposing I’m right, this could have been done better, by
 wrapping thehistoryshell builtin with an
 alias or function. Then the user could have typed
 plainhistory, and it still could have been
 made to produce this carefully constructed output.

(The same argument doesn’t apply to other commands Sam
 types in this session, likeuname, because
 those aren’t shell builtins: they’re found
 onPATH, so you can override them by putting
 your own directory earlier onPATH. So my
 guess is that whoever set up this scene knew how to do
 that, but didn’t know how to do aliases.)

The account setup on the computer

The first thing Sam sees is a shell prompt, not a login
 prompt: Flynn had left himself logged in. So he starts by
 runningwhoami, to determine who he was
 logged inas. The computer
 printsflynn, presumably an unprivileged user
 account. That’s no good – Sam knows he’s going to need to
 be root to investigate properly. He tries to log in
 asroot, but fails, so he
 triesbackdoorinstead, which succeeds.

A natural question is: ifrootandbackdoorare separate accounts, isn’t he
 about to list the shell history from the wrong one? Surely
 Flynn was logged in asrootto do whatever he
 was doing.

But we can see that thebackdooraccount has
 user id 0, the same asroot, because after
 Sam successfully logs in asbackdoor, the
 shell prompt is a#instead of
 a$. That typically happens when the shell
 detects that it’s running as the root uid.
 Sobackdoorandrootshare a
 uid, and so it’s reasonable to guess that they share a
 home directory and shell history too.

We also see thatbackdoor’s home directory
 is taken byloginto be the VFS
 root,/, because nothing better is specified
 in/etc/passwd. So presumably the shell just
 read a history file from the VFS root: something like/.bash_history, or at
 least/.something_history(I don’t
 think there’s much evidence of exactly what shell this
 is). It’s fairly plausible thatrootalso has
 its home directory set to/; that’s not the
 default on Linux, which givesroota proper
 home directory of its own, but it was certainly pretty
 common on proprietary Unixes I used in the 1990s.

So that all hangs together: Flynn ran those commands
 asroot, and by a slightly roundabout route,
 Sam might indeed have logged in to an account that can
 list them in a natural way.

(I’m also a bit suspicious of the use
 ofloginto switch user from within an
 existing login session; one would expect
 perhapssu? To do this
 job,/bin/loginwould need to be setuid, and
 it certainly isn’t on Linux – it expects to be invoked by
 programs likegettyor
 (historically)telnetd, which are already
 root when they run it.PerhapsSolaris (or
 SolarOS) is different? But it seems unlikely.)

Finally, why is there abackdooraccount
 anyway? Normally you make one of those if you have access
 to a system but are worried that someone will try to take
 that access away from you (and are unscrupulous). A hacker
 worried their original entry route will be closed off, or
 one of the people with root on a system, worrying that the
 other(s) will take their access away. In this case, it’s
 Flynn’s own machine; who was he expecting to lock him out
 of it, to need a back door to get back in?

We could simply appeal to Scriptwriters’ Shortcuts:
 sometimes systems have back doors, so you can assume there
 is one if the plot requires it, and nobody needs to
 provide an in-world explanation. But we
 mostlyhaven’thad to use that kind of non-answer
 in this exercise, so I’d rather not. I think a perfectly
 good in-world explanation is thatSammade the
 back door, without his dad’s knowledge. Perhaps Flynn
 trusted his son with root on the same machine (plausible
 –mydad trusted me, when we shared a Linux
 system), but Sam had some reason to suspect that Flynn was
 becoming secretive and mysterious, and anticipated that
 Flynn might close off the root account to try to hide what
 he was up to. And it looks as if thatdidhappen,
 because we can see that Sam initiallyexpectedto
 be able to log in as properroot, and only
 used the back door once he found he couldn’t do that.
 Apparently he knew his father well, and was right to
 suspect!

What flavour of Unix is this, anyway?

Another initial investigatory command Sam runs
 isuname -a, to check exactly what kind of
 Unix system he’s looking at. You could imagine that that
 might change his choice of subsequent commands to type, if
 he’s enough of a Unix generalist to know which OSes spell
 which detailed things differently.

The operating system name printed byunameis “SolarOS”. That’s not a real OS name, but it looks a
 lot like a mixture ofSunOSandSolaris,
 two names for the range of proprietary Unixes from Sun
 Microsystems. I speculate that the very slight change of
 name might have been deliberate, to avoid a trademark
 quibble from Sun?

The appearance ofsun4mlater in
 theunameoutput supports this theory. And
 the overall format of theunamestring is
 pretty close to real Solaris examples I found on web pages
 (alas, I don’t have access to an actual Solaris machine to
 check with). I found this, for example, on one web page:

# uname -a
SunOS storage1 5.10 Generic_125101-09 i86pc i386 i86pc

ThatGeneric_125101-09is a pretty close
 match to theGeneric_50203-02in the film;
 I’d guess it’s something like the kernel version number.
 The rest is fairly close too (although the host name
 fieldstorage1in the real output seems to
 have no analogue in the film version). So it looks as if
 this issupposedto be a depiction of a
 (prudently renamed) Solaris.

However, the shell windows on the left make this look
 like a superficial imitation! The top left shell window is
 showing the output oftopin exactly the
 Linux style, and not only that, the list of process names
 down the right-hand column is characteristically Linuxish.
 Even though we can only see the first four letters of each
 process, we can see things that look suspiciously
 likekthreadd,scsi_eh_something,migration,ksoftirqd,
 andwatchdogd. All of those are process names
 internal to the Linux kernel. Meanwhile, the bottom left
 window is showing what looks like the output
 ofiostat, and again, it looks much more like
 the Linux style ofiostatthan the Solaris
 style.

So I think this issupposedto be a Solaris
 machine, within the story – but the actor playing the part
 is a Linux machine, and the costume and makeup department
 missed a few bits.

Also, I think the appearance
 ofbothsun4mandi386in theunameoutput is another goof. Solaris
 does run on x86 hardware, butsun4mis a
 class of SPARC-based hardware. The real
 Solarisunameoutput I show above prints the
 identifieri86pcin the ‘platform name’ slot
 where the film hadsun4m.

Another hint of Linux is thecat
 /proc/meminfoin the shell history on the right. As
 far as I can tell from Solaris man pages on the web,
 Solaris doeshavea/procspecial
 filesystem, but it’s not exactly like Linux’s, and in
 particular, doesn’t havememinfoor anything
 like it. (In fact, from the man pages I found,
 theonlythings that live in
 Solaris/procare numbered directories
 corresponding to running processes, and
 theselfsymlink.)

The ‘configure’ command in the shell history

When I paused the DVD while watching the film, I
 immediately noticed that there were three
 commandsmake,make install, and
 (after one intervening command)./configure.
 “Hang on,” I thought, “those are in the wrong order!
 Everyone knows that./configurecomes
 first,beforemake.”

But I was wrong! I hadn’t looked closely enough, and I’m
 glad that this year’s exercise made me spot my hasty
 misjudgment.

The sequence
 “./configure,make,make
 install” is correctifthe configure
 script was generated by Autoconf, because if so, then its
 job is to create theMakefilewhich the
 subsequentmakecommand will read. But in
 this case, it’s clear that that’s not what this script is
 doing. It’s being run with the arguments-o
 test.cfg. Autoconf-generated configure scripts
 don’t have a-ooption at all – so this isn’t
 an Autoconf-generated script. It’s some completely
 different thing, which shares a name with Autoconf’s
 output by pure coincidence.

In fact, it looks to me as ifthisconfigure
 script is part of the ‘laser controller’ software package
 that Flynn was working with. It’s plausible for a software
 package that requires a complicated configuration file to
 provide a script that generates one automatically, perhaps
 intended as a starting point for user editing. Here, we
 see Flynn running such a script to generate a starting
 filetest.cfg, and indeed immediately editing
 it withvito adjust whatever parts of it the
 automatic configurer got wrong.

On the other hand, it’s not clearwhyFlynn did
 this, because I highly doubt that the ‘live’ run of the
 laser controller at the end of the shell history was using
 that configuration file. It’s in the source code
 directory, and Flynn called ittest.cfg,
 which doesn’t sound like a file name or path that the real
 software would read by default. After editing it, he
 didn’t copy it to any more official location (like
 maybe/opt/LLL/etc?), and he didn’t run the
 final laser command with any option pointing at it by
 pathname.

I think that’s an error: surely, if Flynn went to the
 trouble of making and editing a shiny new config file, he
 should have finished up by telling the program to actually
 use it. On the other hand, maybe this isn’t an error on the
 part of thefilmmakers; maybe they’re
 intentionally depicting a shell history in which Flynn was
 a bit distracted, or rushed, and didn’t quite do everything
 right!Realusers’ shell histories are full of
 errors, after all.

Killing some processes to free up memory

Apparently the laser control software needs a lot of free
 memory, because in commands 496–500, it looks as if Flynn
 is freeing some up. First he checks how much free memory
 there is usingcat /proc/meminfo(although
 see above for another note about that command); apparently
 he didn’t like what he saw, because the next thing he does
 is to runpsto list the processes, and then
 issue a couple ofkillcommands. Presumably
 he got those pids out of thepslisting, and
 presumably they corresponded to processes he thought were
 likely to be memory hogs. Finally, he
 runspsagain, to check the
 processes he killed are really gone.

I think if I’d been in his position, my final command
 would have been anothercat /proc/meminfo,
 instead of (or maybe as well as) anotherps.
 The ultimate aim of this activity isn’t to kill processes;
 it’s to free up memory. If the laser program needs memory,
 make sure the memoryreally hasbeen freed up
 before you run it!

But, as in a previous section, I think this can
 reasonably be imagined as an in-universe mistake – a piece
 of carelessness onFlynn’spart, faithfully
 depicted by the filmmakers, and not an error on the part
 of the filmmakers themselves. He’s certainly nervous, and
 quite possibly rushed, or distracted, or excited.

Double safety-catch on the laser-control software

Before he runs the laser program, Flynn
 runstouchon a
 file/opt/LLL/run/ok. The nominal purpose
 oftouchis to update a file’s timestamp, but
 if you run it on a file that doesn’t exist already, a side
 effect is to create that file. Presumably, this
 file/opt/LLL/run/okdidn’texist
 already, and Flynn’s purpose here is to create it. Also
 presumably, he’s creating it because the laser control
 software will refuse to actually control the laser if that
 file doesn’t exist. It’s a safety catch, to make it less
 likely that the laser is activated by accident.

In addition to this safety catch, there’s a second one:
 when Flynn runs the laser controller in his final command,
 healsohas to give the option-ok
 1. This laser program demandstwodifferent ways of saying “yes, I really mean it” before it
 will do anything.

Both of these safety-catch techniques are seen in real
 Unix software. Git, in particular, uses both, in different
 parts of its sprawling feature
 set.git-daemonwon’t serve a Git repository
 over HTTP unless there’s a
 filegit-daemon-export-okin the repository
 directory;git-clean, which deletes files,
 won’t delete them for real unless you give it
 the-foption on the command line.

Even with both of these safety catches, I don’t know if
 this laser software would meet the requirements of serious
 safety standards such as ISO 26262. You can certainly see
 things that might still manage to go wrong. Once you’ve
 used a command-line “yes I mean it” option, it’s in your
 shell history (as we see here!), so that recalling and
 re-running the same command doesn’t need repeated
 confirmation. And once you’ve made that file in the
 program’srundirectory, it stays there.

(Or does it? You might imagine that the laser
 softwaredeletes/opt/LLL/run/ok, as
 a side effect of actually activating the laser. Then
 youwouldneed at least one repeated confirmation
 – you’d have to re-create theokfile every
 time you used the laser. But in fact the next thing Sam
 does, after this shot, is to re-run the final command
 ‘LLLSDLaserControl -ok 1’ to see what it does
 – and it turns out that itdoesstill activate
 the laser, without him having had to recreate
 theokfile.)

But then, we shouldn’t expect this software to be safe by
 Serious Business standards. It’s not clear whether Flynn
 wrote it himself or got someone else to help, but he did
 all of this in secret, so it’s definitely ‘one or two
 people coding in a basement’ style software. Nobody is
 insisting that it be certified to industry-standard levels
 of safety. Flynn is only trying to satisfy
 hisownstandards of caution, which don’t look
 all that cautious.

Last will and testament

Before firing the laser, Flynn edits a file
 called~/last_will_and_testament.txt. Even if
 you knew nothing about the film other than this
 screenshot, that would suggest that whatever he’s about to
 do with the laser is dangerous to him personally.

In fact (and this is where knowledge of the rest of the
 film comes in) he’s going to fire the laserat
 himself, disappearing his physical body completely
 and digitising it into a piece of sentient computer
 software, in the same way that it was done to him in the
 originalTron. This time he’s doing it of his
 own free will, instead of the hostile Master Control
 Program doing it to him nonconsensually, so he has time to
 prepare. Probably there’s a risk that the digitisation
 fails, leaving him simply dead; anddefinitelythere’s a risk that he might successfully enter the
 software world but find it hard to get out again. (It was
 hard to get out in the first film, after all.) Either way,
 he’s prudently putting his IRL affairs in order.

But I’m not sure he’s thinking all that clearly. Surely a
 will needs to be signed, witnessed, and
 leftsomewherethat people can actually find it
 after your death? I certainly wouldn’t want to entrust my
 own affairs to the offchance that someone going through my
 computer after my death might find a file called ‘will’ in
 my home directory. If nothing else, wouldn’t they need my
 will to get probate in order tosearchmy home
 directory in the first place?

(Also, this isn’t evenflynn’s home
 directory; it’sroot’s home directory, and by
 the analysis in a previous section, it seems likely that
 that’s/. Not the most obvious place to look
 for a will, evenafteryou’ve got access to the
 deceased’s machine.)

On the other hand, Sam is quite likely Flynn’s executor,
 and as we see here, hehasfound the will. Even
 so, good luck persuading anyone that it’s valid without
 signature or witnesses!

(On theotherother hand, he only found it by
 using thebackdooraccount, and – again by
 analysis in a previous section – it’s possible that Flynn
 didn’t know Sam could do that. So it doesn’t seem too
 plausible that that was the method by which
 FlynnintendedSam to find his will.)

But – yet again – all of this could quite plausibly be
 legitimate in-universe mistakes by Flynn himself, and need
 not be an error by the filmmakers. I expect if I were
 about to perform a life-threatening and untested procedure
 on myself and not even tell anyone in advance, I wouldn’t
 be thinking all that clearly either!

Text rendering in the terminal windows

Everything up to here has been focusing onwhatthe text says. But there’s one last oddity:howit says it.

In a typical terminal window, text is in a fixed-width
 font. But in the main terminal window in our screenshot
 here, the text is in a variable-pitch font. You can see
 that most clearly in the lines “Login incorrect” followed
 by “login: backdoor”. In a fixed-pitch font, the “ogin” of
 “login” would line up vertically between the two lines.
 But here, they’re offset from each other, because the
 capital and lowercase L are different widths:

Also, the text has been word-wrapped, which isn’t usual.
 In normal terminals, if a simple command-line program
 writes a line of text straight tostdoutwhich exceeds the terminal width, the terminal will either
 (occasionally) overprint all the excess characters on top
 of each other in the right margin, or (more usually) wrap
 to the next line atexactlythe right margin,
 without concern for word boundaries – a long word will be
 split across lines wherever it meets the margin, without
 even the dignity of a hyphen.

uname -anormally produces all its output on
 a single line, so the ‘Unknown.Unknown’ was
 probably meant to be on the same line as the rest of it.
 (Indeed, we can see another copy of that same text in the
 bottom left terminal window, and there itisall
 on one line, since that window is wider.) But that final
 word has been moved to the next lineas a whole,
 even though there’s plenty of space left before the right
 margin.

I havenoidea what’s going on here. What
 behaves enough like a Unix terminal program that you can
 run a shell session in it, but uses a proportional font
 and automatically word-wraps? I suppose it’s possible that
 EmacsM-x shellcould be reconfigured into
 that mode via a lot of work with custom face
 configurations andvisual-line-mode– but
 there’s no emacs status bar here, so it can’t
 beexactlythat.

Of course, this is an imitation of a Unix system in a
 film. So there’s no requirement for it to behave exactly
 like real Unix systems. But on the other hand, in a
 previous section I spotted at least one clue in this
 screenshot that suggests theremighthave been a
 real Unix system involved here, used as the easiest way to
 make all these commands deliver the right responses. So
 maybe there really is a weird proportional-width
 word-wrapping terminal program that I’ve never
 encountered?

But if so … it’s not being usedconsistentlywithin this screenshot. The topleftterminal
 window, showing the output oftop, is in what
 looks like a very similar font, but itisfixed-pitch. You can see that the four visible characters
 of each process name line up in nice columns, whether or
 not they’re narrow letters likeiorl– in this window, those letters have
 plenty of blank space around them, unlike in the main
 window. Compare the ‘in’ ofinithere with
 the ‘in’ of “login” above:

So the three windows aren’t all behaving the same
 way as each other!

## Summary

There was a lot to see in this transcript! And quite a lot of
 it had good explanations, within the film’s universe. There are
 a few things I’d class as outright errors by the filmmakers, but
 a lot more things that make perfect sense. And, somewhere in
 between, some things thatcouldbe filmmaker mistakes,
 but are also quite plausible as errors on Flynn’s part.

Apart from a lot of specific knowledge about Unix, the other
 main thing I think this exercise was good for is: reading a
 thing in detail, and avoiding the temptation to skip over things
 thatlook plausiblebut you’re not sure they’re right.
 In this screenshot, there are definitely some things
 thataren’tright – but also, if you examine the whole
 thing in the level of detail that catches those, you find a lot
 of other things thatareright, but weren’t obvious.

I’ll finish up by summarising which things I think are which.
 Of course, this section contains spoilers forallof
 the above.

What’s an error and what’s not

Mistakes by the filmmakers: I stand by my
 original judgment, from the first time I saw this scene,
 thatbin/historyisjust wrong. I’m
 suspicious of/bin/loginworking in this
 situation. I’m very dubious aboutunamereporting bothsun4mandi386on
 the same machine. And finally, it seems clear that
 they’vetriedto make the OS look like Solaris (or
 its fictional renaming SolarOS), because theuname
 -aoutput is not like any real Unix and must have
 been deliberately made up; but in that case, having so many
 Linuxisms all over the rest of the screen seems like an
 avoidable mistake.

Mistakes by Flynn(plausibly): I think he
 should have re-checked/proc/meminfoafter
 killing processes (even though that file doesn’t really
 exist on Solaris). He surely should have done something
 more sensible with his last will and testament. And I think
 he accidentally ran the laser control software with its
 default configuration and not the one he’d carefully created
 just beforehand (but, luckily, apparently that didn’t cause
 a problem). But I’m prepared to accept all of those as
 consequences of a highly distracted state of mind!

No idea at all: I don’t have any good
 answer to the inconsistently proportional font in the
 terminal windows. I can’t think of a way (or a reason)
 someone might have done that on purpose,ora way
 it might have happened by accident. It baffles me.

Perfectly sensible: pretty much everything
 else! It makes sense that Sam had that back door account but
 only tried it once realrootdidn’t let him in.
 Some serious thought was put into the shell history,
 including little details like needing to free up some
 memory, the ‘write a configuration file and then edit it’
 operation, and the dangerous laser software having a double
 safety catch.

None of those fine details isnecessaryto the
 thing that’s happening in the plot. All that’s really needed
 is that Sam found his dad had run a mysterious command with
 ‘laser’ in the name, and ran it again to see what would
 happen. All of this is bonus extra content just for people
 like me who pause to examine it in detail. And mostly,
 pretty well done!

One last thing: if the laser command run
 as root causes the laser behind the computer chair to fire
 and digitise the person sitting in it, how come the
 computerwasn’tleft logged in
 asroot, with the shell history already visible
 on the screen, and no need to runhistoryto
 find it out? How come Sam only found a clear terminal window
 logged in as a mere unprivileged user account? Of course
 thiscouldbe just another mistake … but perhaps
 the answer is that that window doesn’t contain
 thesameterminal session that Flynn ran the real
 command in. Perhaps there’s a cunning system that times out
 unattended root logins after a while?

Finally: there’s a lot of analysis here, but I’m not
 overconfident enough to imagine that I’vedefinitelygot all of it. Maybe someone else will be able to find something
 we still missed!

## Addendum: thoughts from the Internet

Discussion after I published this article did indeed suggest a
 few more points that my colleague and I didn’t think of.

Just so nobody feels a need to tell me thesameextra thoughts again, I’ll list them here, under another cut.
 But I haven’t edited any of the textabovethis
 appendix: mistakes in my own analysis are still there, and I
 won’t try to pretend I never made them.

Things other people pointed out to me

Saving and printing
 withinvi. It didn’t occur to us that
 when you edit a file usingvi, you can issue
 commandswithinthe editor that save it to a
 different pathname, or pipe it to an external command.
 Operations within the editor like that wouldn’t show up in
 the shell history, but it doesn’t mean they didn’t happen.
 So maybe Flynnwasusing his newly created laser
 configuration file after all – maybe he ran something like:w /opt/LLL/etc/laser.cfgwithinvito save it to the right location.
 Similarly, maybe he did do the right thing with his will –
 he could have piped it straight to a printing tool
 likelprfrom within the editor, and then done
 something sensible with the paper copy.

logincanbe setuid.
 My own Linux prejudice was showing./bin/loginisn’t setuid on Linux, but it is on other Unixes, including
 FreeBSD and NetBSD.

An article by theTron: Legacyvisual
 effects artist Josh Nimoyexists!Link
 to article. Alas, it doesn’t directly
 discussthisscene, but it’s still interesting. In
 particular, it mentions the use of emacs and
 itseshellmode to create recordings of shell
 sessions.

Stop-motion replay?That article by Josh
 Nimoy mentionsrecordingshell sessions for use in
 the scenes being filmed. I received a suggestion (from
 someone who had apparently read another article I haven’t
 seen) that those recordings might have been manually
 replayed one frame at a time by someone else – the digital
 analogue of stop-motion animation, where you carefully
 position everything for the next frame and then take the
 picture. So maybe the text in this scenedoescome
 from a real shell session (making my speculation
 aboutbin/historystill reasonable), but it
 might have been recorded in advance, and replayed by pasting
 it a bit at a time into some application more like a text
 editor. That would explain the word-wrapping and
 proportional font. (And the window showingtopis different on purpose, becausetop’s output
 is in columns and they needed it to line up.)

However, as another responder points out, the menu bar
 along the top of the shell window looks like one from a
 terminal application, not a text editor. In fact, it’s
 exactly the same sequence of menu names (“File”, “Edit”,
 “View”, “Terminal”, “Tabs”, “Help”) seen
 inxfce4-terminal.
 Butxfce4-terminalis a perfectly normal
 terminal application which doesn’t let you use a
 proportional font. So perhaps the recording is being
 replayed in aslightly customisedtext editor with
 the menu bar tweaked for realism!

LLL easter egg. Parts of the
 originalTronwere shot in Lawrence Livermore
 Laboratory. In-story, it was representing a corporate
 facility owned by the fictional ENCOM corporation, but
 really it was LLL. The lettersLLLin the name
 of the laser control software are surely a shoutout to
 that.

## Footnote

1.I’m
 sitting in the UK as I write this. Under UK law, I believe this
 should constitute fair dealing: the purpose is quotation for
 criticism and review, and this single screen capture is in no
 way an alternative to paying to see the original film. The film
 comes from the USA, and under USA law I think it similarly
 constitutes fair use: it’s for non-profit educational purposes,
 the amount of the full work used is extremely small, and the
 effect on the value of the full work negligible.