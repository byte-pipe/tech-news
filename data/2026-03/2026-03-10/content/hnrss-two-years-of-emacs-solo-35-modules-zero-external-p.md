---
title: 'Two Years of Emacs Solo: 35 Modules, Zero External Packages, and a Full Refactor | Rahul''s Blog'
url: https://www.rahuljuliato.com/posts/emacs-solo-two-years
site_name: hnrss
content_file: hnrss-two-years-of-emacs-solo-35-modules-zero-external-p
fetched_at: '2026-03-10T11:15:52.510803'
original_url: https://www.rahuljuliato.com/posts/emacs-solo-two-years
date: '2026-03-10'
description: Rahul's Blog
tags:
- hackernews
- hnrss
---

## Rahul's Blog

light 
 dark

# Two Years of Emacs Solo: 35 Modules, Zero External Packages, and a Full Refactor

Rahul M. Juliato
Rahul M. Juliato
March	8, 2026
#
emacs
#
config
#
 elisp

I've been maintainingEmacs Solofor a while now, and I think it's time to talk about what happened in
this latest cycle as the project reaches its two-year mark.

For those who haven't seen it before, Emacs Solo is my daily-driver
Emacs configuration with one strict rule:no external packages.
Everything is either built into Emacs or written from scratch by me in
thelisp/directory. Nopackage-install, nostraight.el, nouse-package :ensure tpointing at ELPA or MELPA. Just Emacs and
Elisp. I'm keeping this post text only, but if you'd like to check howEmacs Sololooks and feels, the repository has screenshots and more
details.

Why? Partly because I wanted to understand what Emacsactuallygives
you out of the box. Partly because I wanted my config to survive
without breakage across Emacs releases. Partly because I was tired of
dealing with package repositories, mirrors going down in the middle of
the workday, native compilation hiccups, and the inevitable downtime
when something changed somewhere upstream and my job suddenly became
debugging my very long (at the time) config instead of doing actual
work. And partly, honestly, because it's a lot of fun!

This post covers the recent refactor, walks through every section of
the core config, introduces all 35 self-contained extra modules I've
written, and shares some thoughts on what I've learned.

Now, I'll be the first to admit: this config islong. But there's a
principle behind it. I only add features when they are not already in
Emacs core, and when I do, I try to build them myself. That means the
code is sketchy sometimes, sure, but it'sin my control. I wrote
it, I understand it, and when it breaks, I know exactly where to look.
The refactor I'm about to describe makes this distinction crystal
clear: what is "Emacs core being tweaked" versus what is "a really
hacky outsider I built in because I didn't want to live without it".

## The Refactor: Core vs. Extras

The single biggest change in this cycle wasarchitectural. Emacs
Solo used to be one biginit.elwith everything crammed
together. That worked, but it had problems:

— It was hard to navigate (even withoutline-mode)

— If someone wanted just one piece, say my Eshell config or my VC
extensions, they had to dig through thousands of lines

— It was difficult to tell where "configuring built-in Emacs" ended
and "my own hacky reimplementations" began

The solution was clean and simple:split the config into two layers.

### Layer 1:init.el(Emacs core configuration)

This file configuresonlybuilt-in Emacs packages and features. Everyuse-packageblock in here has:ensure nil, because it's pointing
at something that ships with Emacs. This is pure, standard Emacs
customization.

The idea is thatanyone can readinit.el, find a section they like, and
copy-paste it directly into their own config. No dependencies. No
setup. It just works, because it's configuring things Emacs already
has.

### Layer 2:lisp/(Self-contained extra modules)

These are my own implementations: replacements for popular external
packages, reimagined as small, focused Elisp files. Each one is a
properprovide/requiremodule. They live underlisp/and are
loaded at the bottom ofinit.elvia a simple block:

(
add-to-list
 
'load-path
 
(
expand-file-name
 
"lisp"
 user-emacs-directory
)
)

(
require
 
'emacs-solo-themes
)

(
require
 
'emacs-solo-movements
)

(
require
 
'emacs-solo-formatter
)

;; ... and so on

If you don't want one of them, just comment out therequireline.
If you want to use one in your own config, just copy the.elfile
into your ownlisp/directory andrequireit. That's it.

This separation made the whole project dramatically easier to
maintain, understand, and share.

## The Core: What init.el Configures

Theinit.elfile is organized into clearly labeled sections (using
outline-mode-friendly headers, so you can fold and navigate them
inside Emacs). Here's every built-in package and feature it touches,
andwhy.

### General Emacs Settings

Theemacsuse-package block is the largest single section. It sets
up sensible defaults that most people would want:

— Key rebindings:M-oforother-window,M-jforduplicate-dwim,C-x ;forcomment-line,C-x C-bforibuffer

— Window layout commands bound underC-x w(these are upcomingEmacs 31features:window-layout-transpose,window-layout-rotate-clockwise,window-layout-flip-leftright,window-layout-flip-topdown)

— Named frames:C-x 5 ltoselect-frame-by-name,C-x 5 stoset-frame-name, great for multi-frame workflows

— DisablingC-z(suspend) because accidentally suspending Emacs in
a terminal is never fun

— Sensible file handling: backups and auto-saves in acache/directory,recentffor recent files, clean buffer naming withuniquify

— Tree-sitter auto-install and auto-mode (treesit-auto-install-grammar tandtreesit-enabled-modes t, both Emacs 31)

—delete-pair-push-mark,kill-region-dwim,ibuffer-human-readable-size, all the small quality-of-life settings coming in Emacs 31

### Abbrev

A full abbrev-mode setup with a custom placeholder system. You
define abbreviations with###1###,###2###markers, and when the
abbreviation expands, it prompts you to fill in each placeholder
interactively. The###@###marker tells it where to leave point
after expansion. I wrote awhole article about it.

### Auth-Source

Configuresauth-sourceto use~/.authinfo.gpgfor credential
storage. Simple but essential if you use Gnus, ERC, or any
network-facing Emacs feature.

### Auto-Revert

Makes buffers automatically refresh when files change on disk.
Essential for any Git workflow.

### Conf / Compilation

Configuration file mode settings and acompilation-modesetup
with ANSI color support, so compiler output actually looks readable.

### Window

Custom window management beyond the defaults, because Emacs window
management out of the box ispowerfulbut needs a little nudging.

### Tab-Bar

Tab-bar configuration for workspace management. Emacs has had tabs
since version 27, and they're genuinely useful once you configure
them properly.

### RCIRC and ERC

Two IRC clients, both built into Emacs, both configured. ERC gets
the bigger treatment: logging, scrolltobottom, fill, match
highlighting, and even inline image support (via one of the extra
modules). The Emacs 31 cycle brought nice improvements here too,
including a fix for the scrolltobottom/fill-wrap dependency issue.

### Icomplete

This is where Emacs Solo's completion story lives. Instead of
reaching for Vertico, Consult, or Helm, I useicomplete-vertical-mode,
which is built into Emacs. With the right settings it's surprisingly
capable:

(
setq
 icomplete-delay-completions-threshold 
0
)

(
setq
 icomplete-compute-delay 
0
)

(
setq
 icomplete-show-matches-on-no-input 
t
)

(
setq
 icomplete-scroll 
t
)

I've also been contributing patches upstream to improve icomplete's
vertical rendering with prefix indicators. Some of those features
are already landing in Emacs 31, which means the polyfill code I
carry today will eventually become unnecessary.

### Dired

A heavily customized Dired setup. Custom listing switches, human
readable sizes, integration with system openers (openon macOS,xdg-openon Linux), and thedired-hide-details-hide-absolute-locationoption from Emacs 31.

### WDired

Writable Dired, so you can rename files by editing the buffer
directly.

### Eshell

This one I'm particularly proud of. Emacs Solo's Eshell
configuration includes:

—Shared history across all Eshell buffers: Every Eshell instance
reads from and writes to a merged history, so you never lose a
command just because you ran it in a different buffer

—Custom prompts: Multiple prompt styles you can toggle between
withC-c t(full vs. minimal) andC-c T(lighter vs. heavier
full prompt)

— A customwelcome bannerwith keybinding hints

— History size of 100,000 entries with deduplication

### Isearch

Enhanced incremental search with sensible defaults.

### VC (Version Control)

This is one of the largest sections and one I'm most invested in.
Emacs's built-invcis an incredible piece of software that most
people overlook in favor of Magit. I'm not saying it replaces Magit
entirely, but with the right configuration it covers 95% of daily
Git operations:

—Git add/reset from vc-dir:Sto stage,Uto unstage,
directly in thevc-dirbuffer. Admittedly, I almost never use this
because I'm now used to the Emacs-style VC workflow:C-x v DorC-x v =, then killing what I don’t want, splitting what isn’t ready yet,
and finishing withC-c C-c. Amending withC-c C-eis
awesome. Still useful once or twice a semester.

—Git reflog viewer: A customemacs-solo/vc-git-reflogcommand
with ANSI color rendering and navigation keybindings

—Browse remote:C-x v Bopens your repository on GitHub/GitLab
in a browser; with a prefix argument it jumps to the current
file and line

—Jump to current hunk:C-x v =opens the diff buffer scrolled
to the hunk containing your current line

—Switch between modified files:C-x C-glets youcompleting-readthrough all modified/untracked files in the
current repo

—Pull current branch: A dedicated command forgit pull origin <current-branch>

— Emacs 31 settings:vc-auto-revert-mode,vc-allow-rewriting-published-history,vc-dir-hide-up-to-date-on-revert

### Smerge / Diff / Ediff

Merge conflict resolution and diff viewing. Ediff configured to
split windows sanely (side by side, not in a new frame).

### Eldoc

Documentation at point, witheldoc-help-at-pt(Emacs 31) for
showing docs automatically.

### Eglot

The LSP client that ships with Emacs. Configured with:

— Auto-shutdown of unused servers

— No event buffer logging (for performance)

— Custom server programs, includingrassumfrassumfor
multiplexing TypeScript + ESLint + Tailwind (I wrotea whole post
about that)

— Keybindings underC-c lfor code actions, rename, format, and
inlay hints

— Automatic enabling for allprog-modebuffers exceptemacs-lisp-modeandlisp-mode

### Flymake / Flyspell / Whitespace

Diagnostics, spell checking, and whitespace visualization. All
built-in, all configured.

### Gnus

The Emacs newsreader and email client. Configured for IMAP/SMTP
usage.

### Man

Manual page viewer settings.

### Minibuffer

Fine-tuned minibuffer behavior, includingcompletion-eager-updatefrom Emacs 31 for faster feedback during completion.

### Newsticker

RSS/Atom feed reader built into Emacs. Customized with some extras I
build my self for dealing with youtube feeds: thumbnail, transcripts,
sending to AI for a quick summary, and so on.

### Electric-Pair / Paren

Auto-closing brackets and parenthesis highlighting.

### Proced

Process manager (liketop, but inside Emacs).

### Org

Org-mode configuration, because of course.

### Speedbar

File tree navigation in a side window. With Emacs 31, speedbar
gainedspeedbar-windowsupport, so it can live inside your
existing frame instead of spawning a new one.

### Time

World clock with multiple time zones, sorted by ISO timestamp
(Emacs 31).

### Uniquify

Buffer name disambiguation when you have multiple files with the
same name open.

### Which-Key

Key discovery. Built into Emacs since version 30.

### Webjump

Quick web searches from the minibuffer. Configured with useful
search engines.

### Language Modes

Specific configurations for every language I work with, organized
into three areas:

Common Lisp:inferior-lispandlisp-modewith custom REPL
interaction, evaluation commands, and a poor man's SLIME/SLY setup
that actually works quite well for basic Common Lisp development.

Non-Tree-sitter:sass-modefor when tree-sitter grammars
aren't available.

Tree-sitter modes:ruby-ts-mode,js-ts-mode,json-ts-mode,typescript-ts-mode,bash-ts-mode,rust-ts-mode,toml-ts-mode,markdown-ts-mode(Emacs 31),yaml-ts-mode,dockerfile-ts-mode,go-ts-mode. Each one
configured with tree-sitter grammar sources (which Emacs 31 is
starting to define internally, so those definitions will eventually
become unnecessary).

## The Extras: 35 Self-Contained Modules

This is where the fun really is. Each of these is a complete,
standalone Elisp file that reimplements functionality you'd
normally get from an external package. They're all inlisp/and
can be used independently.

I call them "hacky reimplementations" in the spirit of Emacs Solo:
they're not trying to be feature-complete replacements for their
MELPA counterparts. They're trying to besmall, understandable,
and good enoughfor daily use while keeping the config
self-contained.

### emacs-solo-themes

Custom color themes based on Modus.Provides several theme
variants: Catppuccin Mocha, Crafters (the default), Matrix, and
GITS. All built on top of Emacs's built-in Modus themes by overriding
faces, so you get the accessibility and completeness of Modus with
different aesthetics.

### emacs-solo-mode-line

Custom mode-line format and configuration.A hand-crafted
mode-line that shows exactly what I want: buffer state indicators,
file name, major mode, Git branch, line/column, and nothing else.
Nodoom-modeline, notelephone-line, just format strings and
faces.

### emacs-solo-movements

Enhanced navigation and window movement commands.Extra
commands for moving between windows, resizing splits, and
navigating buffers more efficiently.

### emacs-solo-formatter

Configurable format-on-save with a formatter registry.You
register formatters by file extension (e.g.,prettierfor.tsx,blackfor.py), and the module automatically hooks intoafter-save-hookto format the buffer. All controllable via adefcustom, so you can toggle it on and off globally.

### emacs-solo-transparency

Frame transparency for GUI and terminal.Toggle transparency on
your Emacs frame. Works on both graphical and terminal Emacs, using
the appropriate mechanism for each.

### emacs-solo-exec-path-from-shell

Sync shell PATH into Emacs.The classic macOS problem: GUI Emacs
doesn't inherit your shell'sPATH. This module solves it the same
wayexec-path-from-shelldoes, but in about 20 lines instead of a
full package.

### emacs-solo-rainbow-delimiters

Rainbow coloring for matching delimiters.Colorizes nested
parentheses, brackets, and braces in different colors so you can
visually match nesting levels. Essential for any Lisp, and helpful
everywhere else.

### emacs-solo-project-select

Interactive project finder and switcher.Acompleting-readinterface for finding and switching between projects, building on
Emacs's built-inproject.el.

### emacs-solo-viper-extensions

Vim-like keybindings and text objects for Viper.If you use
Emacs's built-inviper-mode(the Vim emulation layer), this
extends it with text objects and additional Vim-like commands. No
Evil needed.

### emacs-solo-highlight-keywords

Highlight TODO and similar keywords in comments.MakesTODO,FIXME,HACK,NOTE, and similar keywords stand out in source
code comments with distinctive faces. A small thing that makes a
big difference.

### emacs-solo-gutter

Git diff gutter indicators in buffers.Shows added, modified,
and deleted line indicators in the margin, likediff-hlorgit-gutter. Pure Elisp, usingvc-gitunder the hood.

### emacs-solo-ace-window

Quick window switching with labels.When you have three or more
windows, this overlays single-character labels on each window so
you can jump to any one with a single keystroke. A minimal
reimplementation of the popularace-windowpackage.

### emacs-solo-olivetti

Centered document layout mode.Centers your text in the window
with wide margins, likeolivetti-mode. Great for prose writing,
Org documents, or any time you want a distraction-free centered
layout.

### emacs-solo-0x0

Upload text and files to 0x0.st.Select a region or a file and
upload it to the0x0.stpaste service. The URL
is copied to your kill ring. Quick and useful for sharing snippets.

### emacs-solo-sudo-edit

Edit files as root via TRAMP.Reopen the current file with root
privileges using TRAMP's/sudo::prefix. A reimplementation of thesudo-editpackage.

### emacs-solo-replace-as-diff

Multi-file regexp replace with diff preview.Perform a
search-and-replace across multiple files and see the changes as a
diff before applying them. This one turned out to be more useful
than I expected.

### emacs-solo-weather

Weather forecast from wttr.in.Fetches weather data fromwttr.inand displays it in an Emacs buffer.
Because checking the weather shouldn't require leaving Emacs.

### emacs-solo-rate

Cryptocurrency and fiat exchange rate viewer.Query exchange
rates and display them inside Emacs. For when you need to know how
much a bitcoin is worth but refuse to open a browser tab.

### emacs-solo-how-in

Query cheat.sh for programming answers.Ask "how do I do X in
language Y?" and get an answer fromcheat.shdisplayed right in Emacs. Likehowdoibut simpler.

### emacs-solo-ai

AI assistant integration (Ollama, Gemini, Claude).Send prompts
to AI models directly from Emacs. Supports multiple backends:
local Ollama, Google Gemini, and Anthropic Claude. The response
streams into a buffer. Nogptel, noellama, justurl-retrieveand some JSON parsing.

### emacs-solo-dired-gutter

Git status indicators in Dired buffers.Shows Git status
(modified, added, untracked) next to file names in Dired, using
colored indicators in the margin. Thinkdiff-hl-dired-modebut
self-contained.

### emacs-solo-dired-mpv

Audio player for Dired using mpv.Mark audio files in Dired,
hitC-c m, and play them through mpv. You get a persistent mpv
session you can control from anywhere withC-c m. A mini music
player that lives inside your file manager.

### emacs-solo-icons

File type icon definitions for Emacs Solo.The icon registry
that maps file extensions and major modes to Unicode/Nerd Font
icons. This is the foundation that the next three modules build on.

### emacs-solo-icons-dired

File type icons for Dired buffers.Displays file type icons
next to file names in Dired. Uses Nerd Font glyphs.

### emacs-solo-icons-eshell

File type icons for Eshell listings.Same as above but for
Eshell'slsoutput.

### emacs-solo-icons-ibuffer

File type icons for ibuffer.And again for the buffer list.

### emacs-solo-container

Container management UI for Docker and Podman.A fulltabulated-list-modeinterface for managing containers: list,
start, stop, restart, remove, inspect, view logs, open a shell.
Works with both Docker and Podman. This one started small and grew
into a genuinely useful tool.

### emacs-solo-m3u

M3U playlist viewer and online radio player.Open.m3uplaylist files, browse the entries, and play them with mpv.RETto
play,xto stop. Great for online radio streams.

### emacs-solo-clipboard

System clipboard integration for terminals.Makes copy/paste
work correctly between Emacs running in a terminal and the system
clipboard. Solves the eternal terminal Emacs clipboard problem.

### emacs-solo-eldoc-box

Eldoc documentation in a child frame.Shows eldoc
documentation in a floating child frame near point instead of the
echo area. A reimplementation of theeldoc-boxpackage.

### emacs-solo-khard

Khard contacts browser.Browse and search yourkhardaddress book from inside
Emacs. Niche, but if you use khard for contact management, this
is handy.

### emacs-solo-flymake-eslint

Flymake backend for ESLint.Runs ESLint as a Flymake checker
for JavaScript/TypeScript files. Disabled by default now that LSP
servers handle ESLint natively, but still available if you prefer
the standalone approach.

### emacs-solo-erc-image

Inline images in ERC chat buffers.When someone posts an image
URL in IRC, this fetches and displays the image inline in the ERC
buffer. A small luxury that makes IRC feel more modern.

### emacs-solo-yt

YouTube search and playback with yt-dlp and mpv.Search
YouTube from Emacs, browse results, and play videos (or just
audio) through mpv. Because sometimes you need background music
and YouTube is right there.

### emacs-solo-gh

GitHub CLI interface with transient menu.A transient-based
menu for theghCLI tool. Browse issues, pull requests, run
actions, all from a structured Emacs interface without memorizingghsubcommands.

## Emacs 31: Looking Forward

Throughout the config you'll see comments tagged; EMACS-31marking features that are coming (or already available on the
development branch). Some highlights:

—Window layout commands:window-layout-transpose,window-layout-rotate-clockwise, and flip commands. Finally,
first-class support for rearranging window layouts

—Tree-sitter grammar sources defined in modes: No more
manually specifyingtreesit-language-source-alistentries for
every language

—markdown-ts-mode: Tree-sitter powered Markdown, built-in

—Icomplete improvements: In-buffer adjustment, prefix
indicators, and better vertical rendering

—Speedbar in-frame:speedbar-windowlets the speedbar live
inside your frame as a normal window

—VC enhancements:vc-dir-hide-up-to-date-on-revert,vc-auto-revert-mode,vc-allow-rewriting-published-history

—ERC fixes: The scrolltobottom/fill-wrap dependency is finally
resolved

—native-comp-async-on-battery-power: Don't waste battery
on native compilation

—kill-region-dwim: Smart kill-region behavior

—delete-pair-push-mark: Better delete-pair with mark
pushing

—World clock sorting:world-clock-sort-orderfor sensible
timezone display

I tag these not just for my own reference, but so that anyone
reading the config can see exactly which parts will become cleaner
or unnecessary as Emacs 31 stabilizes. Some of the polyfill code
I carry today, particularly around icomplete, exists specifically
because those features haven't landed in a stable release yet.

## What I've Learned

This latest cycle of working on Emacs Solo taught me a few things
worth sharing.

Emacs gives you more than you think.Every time I set out to
"reimplement" something, I discovered that Emacs already had 70% of
it built in.vcis far more capable than most people realize.icomplete-vertical-modeis genuinely good.tab-bar-modeis a
real workspace manager.procedis a real process manager. The gap
between "built-in Emacs" and "Emacs with 50 packages" is smaller
than the community often assumes.

Writing your own packages is the best way to learn Elisp.I
learned more about Emacs Lisp writingemacs-solo-gutterandemacs-solo-containerthan I did in years of tweaking other
people's configs. When you have to implement something from
scratch, you're forced to understandoverlays,process filters,tabulated-list-mode,transient,child frames,
and all the machinery that packages usually hide from you.

Small is beautiful.Most of the modules inlisp/are under
200 lines. Some are under 50. They don't try to handle every edge
case. They handlemyedge cases, and that's enough. If someone
else needs something different, the code is simple enough to fork
and modify.

Contributing upstream is worth it.Some of the things I
built as workarounds (like the icomplete vertical prefix indicators)
turned into upstream patches. When you're deep enough in a feature
to build a workaround, you're deep enough to propose a fix.

## Conclusion

Emacs Solo started as a personal challenge: can I have a productive,
modern Emacs setup without installing a single external package?

The answer, after this cycle, is a definitiveyes.

Is it for everyone? Absolutely not. If you're happy with Doom Emacs or
Spacemacs or your own carefully curated package list, that's
great. Those are excellent choices.

But if you're curious about what Emacs can do on its own, if
you want a config where you understand every line, if you want
something you can hand to someone and say "just drop this into~/.emacs.d/and it works", then maybe Emacs Solo is worth a
look.

The repository is here:https://github.com/LionyxML/emacs-solo

It's been a lot of fun. I learned more in this cycle than in any
previous one. And if anyone out there finds even a single module or
config snippet useful, I'd be happy.

That's the whole point, really. Sharing what works.

## Acknowledgements

None of this exists in a vacuum, and I want to give proper thanks.

First and foremost, to theEmacs core team. The people who
maintain and develop GNU Emacs are doing extraordinary work, often
quietly, often thanklessly. Every built-in feature I configure ininit.elis the result of decades of careful engineering. The fact
that Emacs 31 keeps making thingsbetterin ways that matter
(tree-sitter integration, icomplete improvements, VC enhancements,
window layout commands) is a testament to how alive this project
is.

While working on Emacs Solo I also had the opportunity to contribute
directly to Emacs itself. I originally wrotemarkdown-ts-mode,
which was later improved and integrated with the help and review of
Emacs maintainers. I also contributed changes such as aligningicompletecandidates with point in the buffer (similar to Corfu or
Company) and a few fixes tonewsticker.

I'm very grateful for the help, reviews, patience, and guidance from
people likeEli Zaretskii,Yuan Fu,Stéphane Marks,João
Távora, and others on the mailing lists.

To theauthors of every package that inspired a module inlisp/. Even though Emacs Solo doesn't install external
packages, it is deeply influenced by them.diff-hl,ace-window,olivetti,doom-modeline,exec-path-from-shell,eldoc-box,rainbow-delimiters,sudo-edit, and many others showed me what
was possible and set the bar for what a good Emacs experience looks
like. Where specific credit is due, it's noted in the source code
itself.

A special thanks toDavid Wilson (daviwil) and the System Crafters
community. David's streams and videos were foundational for me in
understanding how to build an Emacs config from scratch, and the
System Crafters community has been an incredibly welcoming and
knowledgeable group of people. The "Crafters" theme variant in
Emacs Solo exists as a direct nod to that influence.

ToProtesilaos Stavrou (Prot), whose work on Modus themes, Denote,
and his thoughtful writing about Emacs philosophy has shaped how I
think about software defaults, accessibility, and keeping things
simple. The fact that Emacs Solo's themes are built on top of Modus
is no coincidence.

And toGopar (goparism), whose Emacs content and enthusiasm for
exploring Emacs from the ground up resonated deeply with the spirit
of this project. It's encouraging to see others who believe in
understanding the tools we use.

To everyone who I probably forgot to mention, who has opened issues,
suggested features, or just tried Emacs Solo and told me about it:
thank you. Open source is a conversation, and every bit of feedback
makes the project better.