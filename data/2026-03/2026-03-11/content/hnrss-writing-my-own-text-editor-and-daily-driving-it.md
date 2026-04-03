---
title: Writing my own text editor, and daily-driving it
url: https://blog.jsbarretto.com/post/text-editor
site_name: hnrss
content_file: hnrss-writing-my-own-text-editor-and-daily-driving-it
fetched_at: '2026-03-11T19:21:43.617470'
original_url: https://blog.jsbarretto.com/post/text-editor
date: '2026-03-11'
description: Writing my own text editor, and daily-driving it
tags:
- hackernews
- hnrss
---

# Writing my own text editor, and daily-driving it

A programmer's text editor is their castle

2026-03-10

 
 | 
↩️
 2

 │ 
🔄
 12

 │ 
⭐
 20

Toy softwareperforming a task when the stars align and the bytes hold their breath is one thing. Ingesting
whatever freakish data the real world has to offer and handling it gracefully is another.

For a while I’ve been dissatisfied with my text editor. I settled onHowlabout a decade ago; it’s lightweight
and efficient to use, but it falls down in a number of areas:

* Development has been dead for several years.I’ve been maintaining my own fork for a while, but the editor is written in
MoonScript and I don’t really care to learn the language and the codebase deeply enough to perform anything more than minor
tweaks to it.
* Howl chokes when doing project-wide file searches.It’s not awful, but it’s bad enough that it can pull me out of a flow
state and dissuades me from using it. I don’t like that: I am not in the habit of using an LSP, so grepping around for text is
something I lean on quite heavily to understand large codebases.
* Howl is a GUI editor.While it’s largely keyboard-oriented, I can’t easily run it over an SSH connection. Increasingly, a lot
of my time is spent logged into machines that sit on the other end of a network cable, and SFTP only gets you so far.
* It doesn’t have an integrated terminal.You can run external commands and see their output, but there’s no provision for
live interaction and the vast majority of ANSI escape codes are unsupported, so colour isn’t on the table.

For the past few years I’ve been shopping around for alternatives. Here follows an inexhaustive list of editors I’ve tried:

* Helix
* VS Code
* Sublime Text
* Vim
* Zed
* Neovim
* Emacs
* Geany (apparently it’s still alive!)
* Micro
* Lite XL
* Lapce
* GNOME Builder
* Kakoune

They’ve all got their own strengths, but none of them possess thefingerspitzengefühlI’m looking for. I stuck with Helix the longest, but
after a month of use I fell out of love with it. I don’t have any specific criticism of it, it’s a very good editor: it just
didn’t possess that ineffable quality that I care about.

And so, for the past 2 years, I’ve been working on my own. Here are a few reflections on different aspects of its development: feel
free to skip to whichever section personally interests you the most.

## Starting out

To begin with, I kept my scope small. Here are some things I kept off my feature list:

* Features for anybody that isn’t me: no toggle switches, all preferences are hard-coded into the editor.
* Performance:String-backed buffers are fine for the time being. I’ll fix performance when it becomes a problem.
* Proper support for unicode graphemes. I’m monolingual and I don’t use emoji much. Provided£occupies a single column, I don’t
really care.
* Syntax highlighting diversity: Most of what I do occurs in a fair small pool of languages. I’ll support those, and then fall back
to generic delimiter-based highlighting for anything more exotic.

Progress was slow at first. It’s really quite demotivating to stare at a blank screen while you’re hacking together basic terminal
rendering and I’d often go for weeks without working on it at all.

As it happens, this was my second shake at writing a text editor and I elected to build a simplistic if reasonably composable TUI
framework that simplified event and state logic. In hindsight, much of this early effort was overkill and I ended up incrementally
tearing it out as time went on in favour of a more literal, fine-grained approach.

## Eating the dogfood

At some point in time I finally reached a critical threshold: my editor wasjustfeatureful enough to open a single text file,
perform some simple work on it, then save the changes. I decided to start practicing three things that, in hindsight, have been
critical to the project not becoming another dead entry in my~/projectsdirectory:

1. My editor replacednano. Any time I needed to edit a system file or quickly make notes, I’d force myself to use it - no
matter how painful.
2. Every time I hit a missing feature, bug, weird behaviour, or limitation I would document it in the projectREADME.md, no
matter how small. Knowing what to hack on in my free time to make progress was essential.
3. If any issue bothered to me to the point of annoyance, I had to fix it: right there and then.

In combination, these practices pushed my work on the project from an hour a month to several hours a week. Almost all of the
~10k lines of code have appeared in the past 6 months alone.

## Cursor manipulation

Cursor manipulation is difficult! When you’re using a text input widget, much of the behaviour you expect as table-stakes isn’t
something you’re even conscious of. Exactly what happens when you hold a keybinding likectrl + shift + leftis probably muscle
memory but the logic required to getting it all playing together nicely isnot fun to write.

The best advice I can give is to try implementing high-level inputs in terms of more primitive ones. Want to implement word-wise
backspace? Implement it in terms of word-wise cursor movement, selection of the range between the start and end position, and then
deletion. When you get round to implementing undo/redo, you’ll have to ensure that these 3 actions get grouped together as one to
avoid an undo producing really unintuitive results. It’s not surprising that modal editors simply skip the middleman and just
expose these primitive operations directly to the user, allowing them to chain them together.

## File browser

There was one feature that kept me coming back to Howl, and it’s one that it does shockingly well: its file browser.

Howl’s file browser isn’t much to look at, but using it is joyous. It has an instantly-updating fuzzy filter for files, and the
filter isgood; it’s very common for it to get a positive hit on the file I’m looking for on the first keystroke or two, and
exceedingly rare that it doesn’t get it by the fourth or fifth. If a file doesn’t exist and you want to create it, you can do so
inline without needing to switch to another menu. Typing~/will automatically switch you to your home directory, no matter how
deep you are in another path. The main editing window displays a preview of the file you’re about to open.

Howl’s file browser does so many thingsrightand it confuses me deeply that so many other editors elect to have such lackluster
solutions to the problem ofopening files. A great number of editors in the list either force me to reach for the mouse, pull me
out of the editing experience by showing me GTK’sdefault opener dialogue, or ask me to guess the name of the file I want to
open instead of showing me which options are available.

Reimplementing it - with my own personalised quirks - wasn’t a particularly complex task. For the file filter, I briefly
considered doing something complex like using theLevenshtein distancebetween the filter and candidate entries, but a valuable lesson was realising that all of this effort is pointless overkill
because in practice only three things are required to provideexcellentpredictive search for a closed set of items:

1. Whether the entry starts with the filter phrase
2. Whether the entry contains the filter phrase
3. The time of the entry’s most recent modification/access

Rank your items by these criteria. Allow case-insensitive matches, but rank the entry a little higher if the case matches.

That’s it! Even when performing whole-project file searches in projects with tens of thousands of files, these criteria place the
file I’m looking for within 2 places of the top of the list after only 2 keystrokes in approximately 95% of cases.

## Regex

Regex support is used in a number of ways:

* Project-wide search
* Syntax highlighting
* In-buffer finding

All 3 require a reasonably performant implementation, but for the first two it is critical. I briefly considered integrating a
pre-built solution like theregex-automatacrate but one of my requirements is that
context-sensitive edge cases like Rust-style raw string syntax is handled correctly by the highlighter, something that vanilla
regex syntax can’t handle.

On top of that, the whole project is an exercise in building and understanding my own stack, so I elected to implement my own
regex engine, complete with extensions to support context sensitivity and arbitrary nesting of patterns for convenience.

My first attempts were, uh,not quick. I wrotea parserfor the regex syntax using my parsing crate,chumsky, andwalked the resulting ASTfor every character in the input to discover matches.

Over time I built several optimisations on top:

1. Asingle-pass optimiserthat walks the
AST, commuting common patterns that I’d keep see appearing again and again in flamegraphs. For example, a group of character
matches will be optimised into a singleStringnode which searches for an exact string, without any indirection.
2. Walk the AST in an attempt todiscover a common prefixshared by all matches. For example,hel[(lo)p]matches bothhelloandhelp, but both cases are always prefixed byhel-
so only perform matching on locations that start accordingly. This ended up being a huge win for project-wide search.
3. Reimplement the AST walker into a simplethreaded codeVM implemented via Rust
dynamic calls. You can find out more about this techniquehere.
4. Convertthe threaded code VM toCPSform, where each VM
instruction tail-calls its successor, allowing the compiler to optimise each one into a tail call.
5. Wrap Rust’s (slow) dynamic function callsin a manner that avoids needing to perform a vtable lookup on call. You can read more about this techniquehere. After doing this, codegen for many regex instructions was much improved, often no
more than a few machine instructions each.
6. Implement as many of the regex instructionsin terms of bytesrather than unicode codepoints as possible. One of the most brilliant things about the design of UTF-8 is that many of the
techniques that make manipulating ASCII strings fast still work just fine when the string contains multi-byte codepoints!

I did makean attemptat compiling regex to a
chain of jump LUTs, but I struggled to justify the added complexity after benchmarking it and finding it to only be about 20-30%
faster than the threaded code approach even in the best cases while severely hurting the flexibility of the implementation.

As a result of this work I found I was able to fully highlight the largest Rust (my editor’s most complex highlighting lang)
sample file I had (50,000 lines of autogenerated bindings) from a clean state in less than 10 milliseconds: faster than my screen
can refresh itself. I’m sure I could push beyond this with some more work, but I know only too well just how deep theoptimisation rabbit holegoes and have no desire to turn this into an exercise in
regex engine design.

## Highlighting

My initial approach was to rehighlight the file on every change. This does the job, but performance degredation becomes visible on
larger files.

To improve things, I wrotea cachethat highlights tokens on-demand in roughly equally sized chunks (very large tokens can sometimes cause chunks to be larger). When
a change (‘damage’) occurs to the buffer, all chunks that overlap or come after the damage location are invalidated.

It turns out that this approach isvery fastin practice. The most pessimistic case is that you’re editing text right in the
middle of a very large file. In this case, you get to keep all of the highlighting state that comes before the damage area, and
the editor simply doesn’t bother to highlight anything that comes much after the bottom of the screen: because highlighting
information is never requested for it! Because the approach isdemand-driven, it works even when multiple panes are focussed on
different parts of the same buffer.

## Project search

There’s nothing much to say here: when searching a project, I:

1. Walk back from the current directory until I find a.git/directory, indicating the project root
2. Recursively walk all directories in the project root, matching the search needle regex pattern against file contents
3. Extract a file snippet from each positive match and syntax-highlight it for the results preview
4. Rank the results according to their traversal distance from the current path (nearby files are more likely to be relevant)

There are some basic filtering rules to avoid traversing things like build directories.

One slightly interesting detail is that this process is multi-threaded, and work is allocated between threads using a basic
work-stealing approach. An interesting problem I faced was determining when all threads had stopped generating new work (every
thread is both a consumer and a producer of work, which is unusual for work-stealing). I settled on a design where threads waiting
for work would enter a critical section in which they’d increment an atomic counter and sleep for a short time in a loop. If the
atomic counter ever reaches a value equal to the number of worker threads and the work queue is empty, that means that all workers
have finished producing work and all of them can stop.

In practice I’ve found that the regex optimisations I mentioned above, combined with the speed of a modern SSD, mean that full
project searches for trivial patterns resolve almost instantly, even on fairly large codebases likeVeloren. Flamegraphs tend to show that I’m at least mostly IO-bound, although I’m sure
there are cleverer approaches to batching file access that would improve things further.

I can’t express how much of a win this is for my productivity: being able to search a large codebase for answers to a question,
within the editor, at the speed of thought and as those questions pop into my head, is a lovely feeling and it’s something I’d
not previously experienced with any editor I actually enjoyed using.

## Terminal emulator buffers

My editor is pane-based and supports many buffers open next to one-another. It quickly became clear that the convenience of
having a pane be a terminal window was enormous, as opposed to relying on my terminal emulator to provide this functionality (and
hence, using a different set of keybindings to manage both).

I briefly looked into implementing an ANSI parser by hand, but supporting newer terminal rendering features like OSC52, Kitty
keyboard extensions, etc. quickly become an overwhelming (and, more to the point, not especially interesting) mountain that I had
no desire to climb, so I opted to built on top of thealacritty_terminalcrate,
which implements the core escape sequence parser and terminal state management logic for the Alacritty terminal emulator project.
As a result, implementing this feature proved to be fairly trivial, although I don’t have much to say about it owing to my use of
third-party libraries.

My text editor is now perfectly usable as a replacement for the core functionality ofscreen/tmux, with richer escape sequence
support to boot, so that’s nice.

## Rendering

My editor is TUI-based, but just because it’s using a terminal doesn’t make it automatically fast! I still care about bandwidth
when using the editor remotely over a mobile connection, and scrolling through a large file can still present a significant
problem.

To minimise this, my editor has a double-buffered internal copy of the terminal screen. When a redraw occurs it compares the new
frame to the previous one and only emits ANSI escape sequences for cells that have been damaged, and only emits things like cursor
movement, style mode changes, etc. sequences when it actually needs to do so.

The result is that on the vast majority of terminal emulators (excluding perhaps Ghostty) it’s actually faster to open my editor
into a terminal pane,cata large file, then close my editor than it is tocatthe file in the host terminal since my editor
shields the host terminal emulator from the cost of processing all of those extra stdout bytes (thanks,alacritty_terminal!).

## Conclusion

Common knowledge (and perhapscommon sense) would have you believe that writing your own editor / tools is an exercise in
pointless pain. After giving it a go, I firmly disagree: for the motivated engineer, there are a lot of advantages:

* Fits like a glove: my editor does exactly what I want it to do; no more, no less.
* Learned a lot of things: Building my editor required building up a deep understanding of severalgenerally usefultechnologies I only had partial knowledge of previously: regex, ANSI, pseudoterminals (ptys), TUI design, the nitty-gritty of
UTF-8, etc.
* Greater long-term productivity: Knowing your own tool back to front and explicitly building in features for your personal
workflow means you spend less time fighting with your tool (eventually!) and more time enjoying the act of programming. It
shifts the dial of software development away from ‘clerical chores’ and toward ‘thinking work’.
* It’s just damn fun: There’s nothing like solving a lot of neat, self-contained problems and then seeing - no -feelingthe product of your labour in your fingers. It’s reignited some of the love for programming that I’ve been struggling to keep
hold of in recent months, and a lot of that passion has spilled over into open-source, my day job, and my personal life. I have
found myselfgrinning manicallyandchuckling to myselfwhile programming, which is something I’ve not done for many years.
I can only hope this is a good sign, but the jury is out for now.

So: go make your own tools! It needn’t be a text editor. And, for god’s sake,enjoy the challengeand resist the urge to push
the difficult bits off to a box of statistics. There is joy in struggle.

Enter the tarpit 🤖

If you notice accessibility issues with this site, please 
let me know
!

© Joshua Barretto