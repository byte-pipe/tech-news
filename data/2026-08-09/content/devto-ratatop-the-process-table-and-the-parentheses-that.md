---
title: 'ratatop: the process table, and the parentheses that ruin everything - DEV Community'
url: https://dev.to/lovestaco/ratatop-the-process-table-and-the-parentheses-that-ruin-everything-13fn
site_name: devto
content_file: devto-ratatop-the-process-table-and-the-parentheses-that
fetched_at: '2026-08-09T11:26:29.066661'
original_url: https://dev.to/lovestaco/ratatop-the-process-table-and-the-parentheses-that-ruin-everything-13fn
author: Athreya aka Maneshwar
date: '2026-08-07'
description: Hello, I'm Maneshwar. I'm building git-lrc, a Micro AI code reviewer that runs on every commit. It is... Tagged with rust, tui, cli, beginners.
tags: '#rust, #tui, #cli, #beginners'
---

Hello, I'm Maneshwar. I'm building git-lrc, a Micro AI code reviewer that runs on every commit. It is free and source-available on Github.Star git-lrcto help devs discover the project. Do give it a try and share your feedback.

CPU, memory, disks and network were all "read a file, do some arithmetic, draw it".

This one is different.

It reads about 400 directories every tick, and it is the first box you can actually interact with.

There is one bug in here that I would bet real money most/procparsers have shipped at some point. Let me start there.

## The parentheses that ruin everything

Here is a line from/proc/[pid]/stat:

125045 (cat) R 125025 125045 125025 0 -1 4194304 92 0 0 0 11 22 0 0 20 0 7 0 ...

Enter fullscreen mode

Exit fullscreen mode

Space separated.

Field 1 is the pid, field 2 is the process name in parentheses, field 14 is user time, field 15 is system time, field 20 is thread count, field 24 is resident memory.

So you split on whitespace and index into the result. Obvious. Works perfectly.

Until someone runs a process calledmy (weird) app.

42 (my (weird) app) S 1 42 1 0 -1 0 0 0 0 0 5 5 0 0 20 0 3 0 ...

Enter fullscreen mode

Exit fullscreen mode

That name is three whitespace-separated tokens, so every field after it shifts by two.

Your thread count is now reading someone's page fault counter.

Your memory is reading a scheduling priority.

Nothing crashes.

The numbers are just quietly, confidently wrong.

And the process name is fully user-controlled.

Anyone can rename a thread to whatever they like.

The fix is to not split the whole line at all.

Find thelastclosing parenthesis, take the name from between the first(and that, and only then split what remains:

fn
 
parse_stat
(
raw
:
 
&
str
)
 
->
 
Option
<
Stat
>
 
{

 
let
 
open
 
=
 
raw
.find
(
'('
)
?
;

 
let
 
close
 
=
 
raw
.rfind
(
')'
)
?
;

 
let
 
name
 
=
 
raw
.get
(
open
 
+
 
1
..
close
)
?
.to_string
();

 
// Fields resume at `state`, which is field 3 in the man page's numbering.

 
let
 
fields
:
 
Vec
<&
str
>
 
=
 
raw
.get
(
close
 
+
 
1
..
)
?
.split_whitespace
()
.collect
();

 
let
 
field
 
=
 
|
number
:
 
usize
|
 
->
 
u64
 
{

 
fields
.get
(
number
 
-
 
3
)
.and_then
(|
v
|
 
v
.parse
()
.ok
())
.unwrap_or
(
0
)

 
};

 
// ...

}

Enter fullscreen mode

Exit fullscreen mode

rfindinstead offind. That is the entire fix, and it is why the man page forprocexplicitly warns you about this field.

Thenumber - 3offset is worth a look too.

The man page numbers fields from 1, and the two we consumed manually were 1 and 2, so field 14 lives at index 11 of what is left.

I wrote it as a closure that takes the man page's number directly, so the code readsfield(14)and matches the documentation rather than making you do arithmetic while reviewing it.

## Percent of what, exactly?

Second decision that changes what the numbers mean.

A process's CPU time is in clock ticks. To turn that into a percentage you need a denominator, and there are two reasonable choices:

Percent of one core.A single-threaded process pinning a core shows 100%.

A process using four cores shows 400%. This is whathtopdoes by default.

Percent of the whole machine.That same core-pinning process shows 12.5% on my 8 core laptop, and the whole table sums to at most 100.

btop defaults to the second, so that is what I did. The denominator is the total tick delta across every core, which I already had from the CPU box:

let
 
total
 
=
 
cpu
::
sample
()
.total.total
;

let
 
elapsed
 
=
 
total
.saturating_sub
(
self
.previous_total
);

Enter fullscreen mode

Exit fullscreen mode

Neither is wrong. But you have to pick one and say so, because "4.9" means very different things under each, and a user comparing your tool to htop will notice the factor of eight immediately.

## The spike that isn't

Subtle one, and it took me a moment to reason about rather than observe.

CPU percentage is a delta between two samples.

A process that startedsincethe last sample has no previous sample to subtract from.

If you treat its absent baseline as zero, you compute its entire lifetime CPU time as if it were consumed in the last two seconds.

Every freshly spawned process would flash at some enormous number, immediately sort to the top, and then drop back to reality on the following tick.

// A process that appeared since the last sample has no baseline, and its

// lifetime total would read as a huge spike.

if
 
!
self
.previous
.contains_key
(
&
pid
)
 
{

 
return
 
0.0
;

}

Enter fullscreen mode

Exit fullscreen mode

Reporting zero for one tick is a small lie. Reporting 60% for a process that just started is a much larger one.

## Sorting floats is not sorting

Quick Rust one that catches everybody once.

Every other column sorts withsort_by_key:

SortBy
::
Memory
 
=>
 
self
.list
.sort_by_key
(|
p
|
 
p
.memory
),

Enter fullscreen mode

Exit fullscreen mode

CPU is anf64, and that does not compile.sort_by_keyrequiresOrd, and floats only implementPartialOrd, becauseNaNcompares false against everything including itself.

A type wherex == xcan be false cannot have a total order.

So the CPU column needs the explicit version:

SortBy
::
Cpu
 
=>
 
self
.list
.sort_by
(|
a
,
 
b
|
 
{

 
a
.cpu
.partial_cmp
(
&
b
.cpu
)
.unwrap_or
(
std
::
cmp
::
Ordering
::
Equal
)

}),

Enter fullscreen mode

Exit fullscreen mode

Treating an incomparable pair as equal is the pragmatic call here.

ANaNpercentage would be a bug upstream, and I would rather the row sit in an odd position than the whole table panic.

## A stock widget, finally

Four boxes in and I had not used a single ratatui widget that draws data. Everything wasBlock,Paragraph, and my own braille graph and meter.

The process table finally has a use for one:Scrollbar.

let
 
mut
 
state
 
=
 
ScrollbarState
::
new
(
total
.saturating_sub
(
visible
))
.position
(
offset
);

Scrollbar
::
new
(
ScrollbarOrientation
::
VerticalRight
)

 
.begin_symbol
(
Some
(
"↑"
))

 
.end_symbol
(
Some
(
"↓"
))

 
.thumb_style
(
Style
::
default
()
.fg
(
theme
::
HI_FG
))

 
.render
(
area
,
 
buf
,
 
&
mut
 
state
);

Enter fullscreen mode

Exit fullscreen mode

Note that this one is aStatefulWidget, not aWidget.

Different trait, and it will not compile until you import it.

The signature takes an extra&mut Stateargument:

fn
 
render
(
self
,
 
area
:
 
Rect
,
 
buf
:
 
&
mut
 
Buffer
,
 
state
:
 
&
mut
 
Self
::
State
);

Enter fullscreen mode

Exit fullscreen mode

That is ratatui's answer to a real problem with immediate mode.

Some widgets need to remember something between frames, and if everything is rebuilt every frame there is nowhere to put it.

StatefulWidgetmakes that state explicit and hands ownership to you, rather than hiding it inside the widget.

Which raises the obvious question about my scroll position.

## Scroll offset is derived, not stored

The tempting design is ascroll: usizefield that you bump on every key press.

I did not do that, and the reason is terminal resize.

If you store the offset and the user makes the window shorter, the stored value can now point past the end of a shorter list, and the selection can end up off screen with no key press to trigger a correction.

You end up writing clamping code that runs on resize, on list change, on selection change, and you will miss one.

Instead the offset is computed fresh every frame from the two things that are actually true:

fn
 
scroll_offset
(
selected
:
 
usize
,
 
visible
:
 
usize
,
 
total
:
 
usize
)
 
->
 
usize
 
{

 
if
 
visible
 
==
 
0
 
||
 
total
 
<=
 
visible
 
{

 
return
 
0
;

 
}

 
let
 
last_offset
 
=
 
total
 
-
 
visible
;

 
selected
.saturating_sub
(
visible
 
/
 
2
)
.min
(
last_offset
)

}

Enter fullscreen mode

Exit fullscreen mode

A pure function of selection, viewport height and list length.

Resize the terminal and it just produces the right answer, because it never had a stale answer to begin with.

This is immediate mode paying off, and it is a pattern I would not have reached for coming from a retained UI.

The selection index still has to be stored, and it still needs clamping, because processes exit constantly and the list genuinely shrinks under the cursor.

## Small things that add up

Kernel threads have an emptycmdline.

That is how you tell them apart from real processes.

btop shows theircommin brackets instead, so[kworker/4:0-events]is a rendering convention, not something the kernel gives you.

commis truncated to 15 bytes by the kernel.

That is whycodebase-memoryshows ascodebase-memorin the Program column.

Not my bug, and there is nothing to fix: the full name is in the Command column.

uid to username needs/etc/passwd./proc/[pid]gives you a numeric uid via the directory's owner.

I read the passwd file once at startup rather than per process, because 400 processes times one file read per tick is a lot of pointless syscalls for a mapping that does not change while the tool is open.

Everything can vanish mid-read.

Between listing/procand opening/proc/1234/stat, pid 1234 may well have exited. Every failure in that path just means "gone" and skips the entry.

No error, no log, no retry.

## What this cost

Worth being honest about the performance side.

The other four boxes read a handful of files per tick.

This one opens roughly 1200 files per tick:stat,cmdlineand ametadatacall for each of about 400 processes.

My test suite went from about one second to eleven, because several tests construct a fullAppand that now includes a complete process scan.

It is fine at a 2 second refresh.

It would not be fine at 100ms, which my+key allows.

btop solves this with the "lazy" mode you can see in my top-right corner, updating the expensive columns less often than the cheap ones.

I have the label but not yet the behaviour, which is a slightly embarrassing thing to leave in the UI.

That is on the list.

## All four boxes, done

Five days, four boxes, one Rust TUI that reads real system state:

## lovestaco/ratatop

### Keep an eye on what's cooking in your system

A reimplementation ofbtopin Rust, built onratatui.

The goal is a resource monitor that feels like btop: the four-box layout, braille
graphs with gradient fills, mouse-driven navigation, and a themable process
manager, but written as a modern Rust TUI.

## Status

The CPU box works.It samples real data and renders btop's layout:

Per-core braille history graphs, a gradient load bar with sub-cell resolution
frequency, package temperature, battery, and load averages.

Everything else, the memory, network, and process boxes, is still to come.

## Design notes

* Data source:/procand/syson Linux first, read directly rather than
shelling out. btop'ssrc/linux/btop_collect.cppis the reference for what to
read and how often; the BSD/macOS collectors are out of scope for v1.
* Graphs are the hard part.btop's look comes from braille sub-cell plotting
with a color gradient applied along the value axis, not from a stock chart
widget. Expect…

View on GitHub

From here it is polish rather than new territory.

Filtering the process list, killing and renicing, tree view, theme files, mouse support.

The thing I did not expect from this week is how much of the work wasreading kernel documentation carefullyrather than writing Rust.

The parentheses incomm, the 512 byte sectors,f_bavailversusf_bfree,MemAvailableversusMemFree, transmit bytes being field nine.

Every box had exactly one trap like that, and every one of them fails silently with a plausible looking number rather than an error.

Which is the actual lesson, I think.

When you are reading a kernel interface, a wrong answer looks exactly like a right answer.

The only defence is reading the docs properly and writing a test that encodes what you learned.

AI agents write code fast. They also silently remove logic, change behavior, and introduce bugs — without telling you. You often find out in production.

git-lrc fixes this. It hooks into git commit and reviews every diff before it lands. 60-second setup. Completely free.

Any feedback or contributors are welcome! It's online, source-available, and ready for anyone to use.

⭐ Star it on GitHub:

## HexmosTech/git-lrc

### Free, Micro AI Code Reviews That Run on Git Commit

|🇩🇰 Dansk|🇪🇸 Español|🇮🇷 Farsi|🇫🇮 Suomi|🇯🇵 日本語|🇳🇴 Norsk|🇵🇹 Português|🇷🇺 Русский|🇦🇱 Shqip|🇨🇳 中文|🇮🇳 हिन्दी|

# git-lrc

## Free, Micro AI Code Reviews That Run on Commit

 

 
 
 
 
 
 

GenAI today is arace car without brakes. It accelerates fast -- you describe something, and large blocks of code appear instantly. But AI agentssilently break things: they remove logic, relax constraints, introduce expensive cloud calls, leak credentials, and change behavior -- without telling you. You often find out in production.

git-lrcis your braking system.It hooks intogit commitand runs an AI review on every diffbeforeit lands. 60-second setup. Completely free.

In short, git-lrc helpsPrevent Outages, Breaches, and Technical Debt Before They Happen

At a glance:10 risk categories·100+ failure patterns tracked· every commit…

View on GitHub

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse