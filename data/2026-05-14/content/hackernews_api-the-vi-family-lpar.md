---
title: The vi family | LPAR
url: https://lpar.ATH0.com/posts/2026/05/the-vi-family/
site_name: hackernews_api
content_file: hackernews_api-the-vi-family-lpar
fetched_at: '2026-05-14T06:00:47.436871'
original_url: https://lpar.ATH0.com/posts/2026/05/the-vi-family/
date: '2026-05-06'
published_date: '2026-05-04T16:08:34-05:00'
description: The last text editor you’ll ever need to learn.
tags:
- hackernews
- trending
---

Polls of Linux users suggest thatvifamily editors are the most popular. Thevieditor is a terminal-based text editor which dates back to 1977. If you’re wondering why so many people would choose to use a fifty year old text editor with a notoriously steep initial learning curve, it’s because once you learn it, you can be ruthlessly efficient with your editing. There’s also the benefit that it’s basically everywhere, so you don’t have to keep re-learning how to edit — most IDEs havevikey bindings as an option, including VS Code, IntelliJ IDEA, and XCode.

Thevi2.0 release (1979) was a very large piece of software for the time, and in the 1980s it was only available to people with a commercial UNIX® license from AT&T. For this reason, multiple people created free clones ofvito run on 80s personal computers.

There are now manyviclones and derivatives to choose from, and I couldn’t find a good comprehensive list of all of them with links, so here’s mine. Dates are release dates, to the best of my ability to track them down. Some of the projects are no doubt defunct, but it can be hard to tell as they can also go years between releases.

I’m not going to list all the IDEs that havevikey bindings as an option, but other than that suggested additions are welcome.

## Original ex/vi (1977-2017?)#

https://github.com/n-t-roff/heirloom-ex-vi/

The original 2.11BSD vi, upgraded to support UTF-8, with fixes for POSIX compliance.

No major “quality of life” improvements, and it will fall over editing very large files.

## STevie (1987–1989)#

https://nosuch.com/tjt/STevie/

A clone for the Atari ST and Amiga. If you don’t have an ST or Amiga you don’t want this. If youdohave an ST or Amiga, you probably still don’t want this, as there are better options available to you. Vim (see below) descends from STevie.

## Elvis (1990–2024?)#

https://github.com/mbert/elvis

One of the earliestviclones, built to run on MS-DOS, Minix, and other systems of the early 1990s.

Elvis added improvementsincluding multiple edit buffers, multiple windows, and syntax coloring. Unlike STevie, it used a file buffer for editing, so it could deal with files larger than available memory. It was used for the 80386 port of BSD Unix.

## xvi (1992–2017?)#

https://martinwguy.github.io/xvi/

A STevie derivative which adds multiple windows and buffers. Probably the smallestviclone.

## Vile (1991–)#

https://invisible-island.net/vile/

Originally derived from Microemacs, givenvistyle editing, but withmoremodes. Adds infinite undo, UTF-8 support, syntax highlighting, and more.

## Vim (1991–)#

https://www.vim.org

Probably the most usedviclone. Derived from STevie. Adds windows, multiple buffers, assorted scripting options, and UTF-8 support. Handles very large files (GB in size).

Now incorporating LLM-generated code.

## nvi (1994–)#

https://repo.or.cz/nvi.git

Based on Elvis, a reimplementation ofviintended to be identical in core behavior to the original. Used for the 4BSD Unix release.

Adds support for additional scripting languages (Perl and Tcl). Introduced use of a database for storing file data. It’ll open files of about a GB in size but will complain about DB page sizes. Also unfortunately still doesn’t support UTF-8 text.

## OpenBSD vi / OpenVi (1994—)#

https://github.com/johnsonjh/OpenVi

A derivative ofnvi. Extensively cleaned up, but still doesn’t support UTF-8 text. Also missing macros, scripting, syntax highlighting.

## BusyBox vi (2001–)#

https://busybox.net

BusyBox includes a tiny incomplete (but usable) implementation ofvi. You’ll encounter it in Alpine Linux and embedded systems.

## IllumOS vi (2005–)#

https://github.com/illumos/illumos-gate/tree/master/usr/src/cmd/vi

AT&T UNIX®vifrom SVR4, open-sourced as part of OpenSolaris in 2005.

## nvi2 (2011–)#

https://github.com/lichray/nvi2

Adds UTF-8 support to nvi, as well as various CJK encodings.

## neovim (2014–)#

https://neovim.io

Cleans up Vim by removing support for ancient platforms. Adds LSP support, a built-in terminal emulator, Lua scripting to replace VimScript, and many other features.

Now incorporating LLM-generated code.

## EVi (2026–)#

https://codeberg.org/evi-editor/evi

A fork of Vim from before it began gaining LLM-generated code.

## Vim Classic (2026–)#

https://vim-classic.org

A fork of Vim from version 8.3 (pre LLM code), aiming for long term support by humans.

## ToyBox vi (2027?)#

https://codeberg.org/landley/toybox

ToyBox, the non-GPL BusyBox clone,may be getting its owntinyviimplementation.

Also, some things which aren’t really vi, but…

## Viper (1995–)#

https://www.gnu.org/software/emacs/manual/html_mono/viper.html

A set ofvikey bindings for Emacs.

## Kakoune (2012–)#

http://kakoune.org

A modal editor inspired byvi, but withslightly different key bindings. Designed to be minimal, calls external programs for some features.

## Evil (2013–)#

https://github.com/emacs-evil/evil

Another implementation ofvimodal editing on top of Emacs.

## vis (2015–)#

https://github.com/martanne/vis

Likevi, but with structural regular expressions and other features taken fromsam, the Plan 9 editor. (Sam is a graphical editor, so isn’t in this list.)

## Helix (2021–)#

https://github.com/helix-editor/helix

Another new modal editor, inspired by Kakoune and Vim. Again,key bindings are different.