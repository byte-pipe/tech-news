---
title: Using fortune to reinforce habits
url: https://www.judy.co.uk/blog/using-fortune-to-reinforce-habits/
site_name: lobsters
fetched_at: '2025-07-26T23:06:42.397662'
original_url: https://www.judy.co.uk/blog/using-fortune-to-reinforce-habits/
date: '2025-07-26'
description: A tutorial showing how I use fortune to remind me what tools I have installed on my computer.
tags: practices
---

# Using fortune to reinforce habits

 July 23, 2025

 -


intermediate

cli

A while ago I installed a bunch of new command-line tools,
some of which replaced my existing tools, likeezainstead ofls.
Other tools improved the way that I work, such asLazyGit– the only interface to Git that I’ve found to be better that just usinggitcommands.

If you’re looking for some recommendations for a modern command-line,
I can highly recommendSupercharge your shellby Justin Mayer,
orOxidise your command linefrom the No Boilerplate YouTube channel.
Many of these tools are written in Rust,
which is a favourite language of mine,
but that shouldn’t make much difference to you!

I had two problems though.

## Problem 1: Forgetting to use the tools

One problem was that muscle-memory meant I kept using the old commands instead of the new ones.
I could fix this by creating aliases, likealias ls=eza.
That would mean that whenever I typedlsthe command thatactuallywas run would beeza.
That’s fine with commands which are backwards compatible.ezasupports all (or at least most!) of the flags thatlssupports.

The problem was with commands thataren’tcompatible.
For example, thedufcommand is much more powerful thanduwhich I used to use,
and isn’t a drop-in replacement.

## Problem 2: Forgetting I installed the tool

The other problem was that I kept forgetting that I had installed a tool,
or if I remembered,
then I couldn’t remember what the tool wascalled.

While I was working on this post,
I couldn’t remember the name of thexhtool.
It’s an HTTP client for the command line.
It’s a replacement for HTTPie which was a replacement for Curl!

## The Solution

I needed some constant reminders that these tools existed on my computer,
and a reminder of what each tool did.

What I imagined was that every time I opened a terminal window,
I would get a short message saying,
“Don’t forget you’ve installedxh– it’s a command-line HTTP client!”

Yes, I really write messages to myself in that chirpy style.

## In stepsfortune, fortunately

I nearly started coding something in Python.
I am a programmer after all.
Then I remembered…

There’s a tool for managing a database of short text snippets,
and selecting snippets at random.
It’s calledfortuneand it’s a proper old-school UNIX utility.

These days, fortune isn’t usually installed by default on Linux.
The following are the commands I know for installing fortune on different platforms:

# Debian etc.

apt
 install fortune-mod

# Fedora etc:

sudo
 dnf install fortune-mod

# Arch:

sudo
 pacman
 -S
 fortune-mod

# MacOS:

brew
 install fortune

Once it’s installed,
you can see a random snippet by running thefortunecommand with no parameters.
You’ll get a different snippet each time.

$
 fortune

"
Earth is a great, big funhouse without the fun.
"


--
 Jeff Berner

$
 fortune

Honesty
 pays, but it doesn'
t seem to pay enough to suit some people.

 -- F.M. Hubbard

I suspect that most people who install fortune just use the data files that come with fortune,
just like I did above.
They contain a bunch of jokes, quotes, technical and philosophical observations.

But you can also create yourowndata files for fortune.

## Create your own fortune file

I created a short text file called “habits”, and added some short snippets to it.
The format isn’t very complicated.
Each snippet is separated by the percent character (%) on its own line, like this:

Don't forget about hexyl! A handy binary file viewer.

%

Still using man? Try using *tldr* first!

%

Don't use *ps* - use *procs*!

Fortune can’t use this text file as it is.
First, it needs a data (or “dat”) file to be created.
The data file sits alongside the text file
and contains information that allows fortune to look up a random snippetreally quickly.
Fortunately the tool that does this processing is packaged withfortune,
and it’s calledstrfile.

To create a file called “habits.dat” from the file “habits”,
I ranstrfile habits habits.dat.
This created “habits.dat” in my current directory.
Now I can runfortuneand point it at my text file.
It will find the dat file automatically:

# Check that both habits and habits.dat are in the right place:

$
 ls
 -1

habits

habits.dat

$
 fortune habits

Still
 using man? Try using *tldr* first!

$
 fortune habits

Don
'
t forget about hexyl! A handy binary file viewer.

## Make it easy to update the habits file

I often forget how to update the data file when I’ve updated my fortune text file.
(I had actually forgotten when I started to write this post.)
I created a Makefile to make it easier to update the data file.
Makefiles are also pretty old-school,
but they’re also the perfect tool for this job!

# Makefile

habits.dat
:
habits


@
strfile
 habits habits.dat

Just make sure your text editor isn’t going to replace the indent with spaces
– it’s important that it remains a tab character.

I have to admit thatmyMakefile is slightly more complex than this,
but I’m a nerd. The Makefile above is fine.

After writing this, I can now just runmake,
and it will update “habits.dat” if the “habits” file has changed.

At this point,
I filled out my “habits” file with details of all the commands I’d installed.
I stole some content fromtldr,
which is super-helpful for learning the basics for a new tool.

$
 tldr duf

-
 List accessible devices:


duf

-
 List everything (such as pseudo, duplicate or inaccessible file systems)
:


duf --all

-
 Only show specified devices or mount points:


duf
 path/to/directory1 path/to/directory2 ...

-
 Sort the output by a specified criteria:


duf --sort
 size|
used
|
avail
|
usage


...

## Automatic reminders

Do you remember that I wanted to print out these snippets every time I opened a terminal window?
How you do that depends on the shell you’re running.

First, I moved the directory containing “habits”, “habits.dat”, and my “Makefile” into an appropriate directory.
I chose “~/.local/habits”.
Afterwards, I could do this:

$
 ls
~
/.local/habits

habits
 habits.dat Makefile

If you use bash or zsh you can add the following to the end of “~/.bashrc” or “~/.zshrc”:

# ~/.bashrc or ~/.zshrc

# ... existing content goes here ...

fortune ~
/.local/habits

If you’re onfish shell, it’s a bit different.
(You should try fish shell, I absolutely love it!)
In this case, you need to add the above command to a function calledfish_greeting.

# ~/.config/fish/functions/fish_greeting.fish

function
fish_greeting


fortune
~/.local/habits

end

However you configure it,
once you’ve made the necessary edits open a new terminal window and you should see a handy reminder!

## Bonus points

The code above is pretty useful,
but the text doesn’t stand out very much in the console.
I found it was a little too easy to ignore it.

There are a few neat tools for the command line that can format text in interesting ways,
for example, by drawing ascii-art frames around the text.
Two popular ones arecowsayandboxes.

I changed thefortunecall so that it pipes the output throughboxes.
My command looks like this:

fortune ~
/.local/habits |
boxes -d
 parchment

… and the end result looks like this:

## Summary

Building my own habit reminder as I’ve described above was something that I’ve found surprisingly useful.
I had never really thought of usingfortunein this way,
but it’s proven to be quick to set up,
didn’t require any coding,
and it’s helped me to improve how I use the command-line!

## Update

This post has done some numbers, and apparently inspired some people!
I love that the phrase “habits file” is being used by others as a shorthand for this idea.

If you’d like to configurechezmoito synchronise your habits files across the different machines you use,
do check out Chris’ post,Habits in the Shell, shared.
Chezmoi is a tool that I also use,
to share config between my computers.
It’s an awesome piece of software,
with a bit of a learning curve.

If you found this tutorial useful, let me know onMastodonorBluesky!

This is the blog of Judy2k.You can follow him onMastodon(if you like).© 2025 Mark Smith, All Rights Reserved
