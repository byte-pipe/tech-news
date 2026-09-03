---
title: Porting my 1993 Amiga game to Godot, with an LLM reading the 68000 assembly — Babylonian Twins
url: https://babyloniantwins.com/blog/porting-a-1993-amiga-game-to-godot/
site_name: hnrss
content_file: hnrss-porting-my-1993-amiga-game-to-godot-with-an-llm-re
fetched_at: '2026-09-04T07:25:17.167151'
original_url: https://babyloniantwins.com/blog/porting-a-1993-amiga-game-to-godot/
date: '2026-09-03'
description: Babylonian Twins is an Amiga platformer I built in Baghdad in 1993, in 68000 assembly. This summer an LLM ported it to Godot, and this is what I found when I read back through what it did. The original disks are now free on itch.io.
tags:
- hackernews
- hnrss
---

← All posts
 
By Rabah Shihab · September 1, 2026
 

# Porting my 1993 Amiga game to Godot, with an LLM reading the 68000 assembly

 
 

In 1993, in Baghdad, I built a game called Babylonian Twins on an Amiga 500:
512KB of RAM, no hard drive, plugged into a TV. I was an engineering student in
my twenties. Pure 68000 assembly, every sprite and every scanline by hand.
Murtadha Salman drew the art and Mahir AlSalman composed the music. We were
under sanctions. No internet, no game development resources, just one copy of
the Amiga Hardware Reference Manual, which I used to program the hardware
directly, and electricity a few hours a day. The constant floppy disk swapping
(because of the small memory) and the 50°C summers killed my disk drive three
times.

Left: 1993, on the Amiga. Right: 2026, the same gateway.

On the Amiga, “by hand” means the game doesn’t ask the operating system for
anything while it runs. At startup it saves the interrupt vectors, switches the
OS interrupts off and takes the whole machine:

	move.l 	#$dff000,a0			
;Base for hardware registers

	lea
 	save(pc),a1			
;Get the system

	move.w 	#
$4000
,intena(A0)		
;from the AMIGA

“Get the system from the AMIGA” is my comment, from 1993. From that point on
the display is the game’s own copper list (the Amiga’s programmable video
coprocessor), rewritten on the fly for sprites and sky colours. Tiles move by
writing the blitter’s registers directly and waiting on its done flag. The
joystick is read straight from the hardware port, and the fire button is one
pin on a CIA chip. The OS comes back only between levels, to load the next
level’s files from the disk, and then it’s switched off again.

It was the first commercial game made in Iraq, and for a long time a game very
few people got to play. Commodore collapsed and sanctions scared off
publishers, so the finished game sat on a shelf. An Amiga forum found it in 2008 from my
brother’s YouTube uploads and hunted me down for the disks;the thread is still there.

The game has been ported once before, by hand, in 2010. The same team
rebuilt it for the iPhone on an engine written from scratch, about 34,000
lines of C++, over months of nights and weekends. Apple and Google featured
it, and it reached over two million downloads. That story ishere.

I didn’t do this port. I asked for it, played the result every night, said
what felt wrong, and made the few decisions that needed somebody who was
there in 1993. The file formats and the assembly reading were the AI’s work,
and so were the decisions about how to carry thirty-year-old code across, and
it went faster than I could follow. This post is what I found when I sat down
weeks later and read what had been done to my own game. Some of it was wrong,
and I didn’t notice for weeks.

## Why I tried again

I’d tried this before. About a year ago I gave an earlier model the same Amiga
material and asked it to make sense of my binary level maps. It got there in
the end, but it took several rounds and a lot of hints from me.

Then Claude Fable 5 shipped, and I gave it the same files.

The test was deliberate. My guess was that there is little Amiga assembly
code in LLM training sets. If the model was better at working things out
rather than recalling them, this is where it would show.

The July 4th weekend was coming up, so I planned three steps, each one
conditional on the previous working.

Step one, the safe ask: my own 2010 engine, the 34,000 lines of C++, moved
into Godot 4. This was the control.

Step two, the unfair ask: the original 72,758 lines of 68000 assembly, for a
machine that had gone out of production, with no comments to speak of and
nothing in common with the C++. Rebuild that in Godot too, at the Amiga’s
original 50 Hz.

Step three, the greedy ask: put the second one inside the first, so buying the
modern game gets you the 1993 original as a second thing you can launch.

All three worked. The level format that had taken several rounds and my
corrections a year earlier came out in a single pass, with no hints from me.

## How it was run

I ran it in Claude Code, so it had a terminal and my filesystem. It could edit files, run the assembler,
build the game, launch the game and read what came back. When I say below that
it rebuilt my 1993 binaries and checked them, it did that by running vasm and
diffing the output.

Early on it added a set of command-line flags to the game so it could play
without me:

--level=<name> load a level directly

--pose=<spec> put the twins at exact positions

--drive=<spec> press buttons on a script, frame by frame

--probe dump switch / gate / door / key state

--screenshot=<path> render a frame and quit

Which turns “does the jump feel right” into something a machine can read:

drive[btw_jump:2.2] pos=(25.44, 24.04) vel=(0.00, -14.51) ground=false apex_y=22.48

It also had two headless checks it could run before showing me anything: one
that compiles every script, and one that builds every level and reports
failures. On the Amiga side it drove the real toolchain, vasm to assemble and
FS-UAE to boot the result. What wasn’t automated: there was no image
comparison on the modern port (it took screenshots, I looked at them), and
nothing checked whether the game felt right.

## Step one: 34,000 lines of C++ in an evening

Wednesday night, the safe ask. Timestamps, unedited:

22:23 Godot 4 project scaffold, asset sync, TMX level pipeline

22:44 both twins playable — collision, physics, camera, switching

23:19 all 38 entity types ported — full object roster live

00:35 full screen flow — menus, map, story, save, game flows

02:15 exporting to macOS, iOS and Android

Twenty-one minutes from empty project to a playable character. Every line it
moved that night was a line I’d written, over months, in 2010. I went to bed
confused.

Getting it to feel right took about three days after that: jump arcs and
trampoline timing, and hit detection that rewards mashing, fixed in batches on
July 2nd, 3rd and 4th.

I wasn’t testing alone. My thirteen-year-old son played every build with me.
He’s always known I made this game, it’s a fact about his father he grew up
with, but he’d never seen me working on it. The testing turned into a
father-and-son thing I didn’t plan, and it’s one of my favourite parts of the
whole project.

### Same units, same tick

All the gameplay state lives in tile units (1.0 = one 48px tile), and the
update runs at a fixed 60 Hz, because the 2010 iOS build ran at 60 Hz. That
matters because the original applies drag multiplicatively, every frame:

static
 const
 float
 GROUND_DRAG_FACTOR 
=
 0.85
f
;

this
->velocity.x 
*=
 GROUND_DRAG_FACTOR;
 // every tick!

Multiply by 0.85 sixty times a second and you get one amount of friction;
multiply fifty times a second and you get another. Port it to a different tick
rate and every acceleration curve in the game changes. Nothing crashes, it
just feels wrong forever, and you won’t find it by reading the diff. At 60 Hz
the constant transplants verbatim. This is also why the 1993 rebuild runs at
50 Hz and the modern one at 60: two sets of hand-tuned numbers, each only
correct at its own tick. It kept both clocks. I’d have been tempted to tidy
them into one.

### It didn’t use CharacterBody2D

Godot shipsCharacterBody2Dandmove_and_slide(), and every tutorial tells
you to use them. The port used neither for the player. The original has its
own hand-written movement code, and rebuilding that on somebody else’s physics
would feel slightly wrong in ways that are miserable to track down. The player
is a plainNode2D, and the 150-line collision routine came across line for
line, including the fudge numbers I picked by feel fifteen years ago and the
comments I wrote to my future self:

# Add 0.5 because we want the character's feet to be in the middle of the tile.

var
 bottom 
:=
 pos.y 
+
 dim.y 
/
 2
 +
 0.5
 +
 i 
+
 fraction

if
 int
(bottom) 
==
 int
(pos.y 
+
 dim.y 
/
 2
 +
 0.49
):

 continue

var
 right 
:=
 pos.x

var
 left 
:=
 pos.x 
-
 dim.x 
/
 4
 # asymmetric probes!

Nothing tidied up the stray0.49. There are no tests and no docs; those
comments are the spec.

## Step two: the 68000 assembly

By Sunday afternoon, July 5th, I handed over the thing I actually wanted to
test. 72,758 lines across 26 files, written for a machine with 512 KB of
memory, by me, for me, with the commenting habits of somebody who never
expected another person to read it. No documentation. A 2008 transfer to
modern storage had shortened every long filename, so every include pointed at
names that no longer existed. One of the five level source files is cut off
partway through a data table. There’s no other copy.

Before porting anything, it made the 1993 sources assemble again, using vasm
on an Apple Silicon Mac, and kept going until the output was byte-identical
to the binaries that shipped.

14:34 import the Amiga sources, assets, references

14:49 vasm toolchain reproduces the shipped binaries byte-identically

15:20 disk images rebuilt

15:42 the rebuilt demo boots and plays in FS-UAE

Fifteen minutes from a folder of files to the first rebuild that matched the
shipped bytes. I wrote these in ASM-One, whose dialect differs from vasm’s in ways that change the bytes:
ASM-One encodescmp #4,d0as CMPI, vasm picks a different, equally valid
encoding, so telling it not to optimise is necessary and not sufficient.
Rather than edit my sources it wrote a preprocessing pass that bridges five
such differences, and rebuilt the broken filename mapping file by file.

The expensive one wasorg. With no linker and no relocation, the level
source lays out the Amiga’s memory by hand, address by address:

org 
$6a000
				; this section lives at address $6a000

Mapadd:

	incbin
"
btwins:
binary/L1/Map1.b"	
;Game Map

	org mapadd+
73
*
1024
		; skip to 73 KB past the map's start

GLBtable:

	dc.w 
$3333
,
50
,
20
,
100
		; one object record begins

	dc.w SahamR-grb,
26
		;Routine,Length

	...

org glbtable+
2
*
1024
			; the object table gets exactly 2 KB

The level-one map uses 74,400 of those 74,752 bytes, a margin of 352, and
nothing checked it except me, in 1993. (SahamR-grbattaches an object’s
behaviour as a named offset; saham is Arabic for arrow.) ASM-One’sorgcan also move the location counter backwards, which vasm can’t. The
first workaround got one case wrong: ads.b 800inside a rewound block,
which ASM-One treats as “skip 800 bytes”, was written out as 800 bytes of
zeros. Everything after that point in the file, the copper list included, sat
944 bytes away from where the shipped binary had it. The game assembled and
booted, and drew the wrong thing.

Even after that, some chunks still wouldn’t match, by about 108 bytes
scattered through the variable area. Those bytes explained where the shipped
files came from. ASM-One assembles into memory, and the game got onto disk by
saving that memory out, after the game had been run. So the shipped files are
a snapshot of a game that had already been running, not clean assembler
output. A fresh assembly has zeros in those variables, because nothing has set
them yet; the shipped disk has whatever they held on the machine when it was
saved. The code writes them before it reads them, so the zeros are harmless.

At the time I read that line, moved on, and waited for the actual game. It
took me weeks to see that this was the most important thing in the project,
and that nobody had asked for it. From then on, every claim about this game
could be settled by comparing bytes. I wouldn’t have done it myself. I
already had the binaries, and in eighteen years rebuilding them from source
never seemed worth an afternoon.

## The formats

For every format it went to the code that reads the bytes and worked
backwards from that. The level loader is 1,652 lines of uncommented 68000,
which is why I’d always reached for a hex editor instead.

### The levels

A level is a grid of tiles: a long list of numbers, where each number means
“put picture 47 here”, in my own private 1993 layout. This is the format the
older model and I had ground through a year earlier.

Here is the full set of tiles a level is built from, 256 of them, 16×16
pixels each, for level one:

And a slice of level one, assembled from those tiles:

The input is a list of numbers with no header and no dimensions, inside a
compressed chunk. This time I didn’t explain anything.
It found the drawing routine, read how the grid was walked, worked out the
width and height from constants elsewhere in the file, and produced correct
maps for all five levels on the first attempt.

Then it re-rendered each level from its own extracted data and compared the
result, pixel by pixel, against full-level captures I had made in 2020. Where
they didn’t match, it went looking for the cause and found two copper
effects: the sky gradient and the water colour cycle. With those two accounted
for: five full-level images, zero differing
pixels. Level one alone is 600 tiles wide, 9,600 pixels.

### Map cell properties

Drawing the level is only half of what a map cell does. Each cell is one
16-bit word, and the picture is the smaller part of it:

one map cell, 16 bits:

 bits 15..10 the property: what this square DOES (6 bits)

 bit 8 which of the two tile banks to use (1 bit)

 bits 7..0 which of the 256 tile pictures to draw (8 bits)

The property is the level’s invisible physics. 1 is solid ground. 2 and 3 can
be climbed. 10 to 13 all mean “this hurts”, four codes because knockback needs
a direction. 14 kills outright. 63 is a door. None of this is written down
anywhere. It was recovered because two routines read the same word and each
one reveals its own half: the draw loop masks off the low byte, and the
collision check does the opposite:

	move.w	(a1),d6			
; the same cell

	and
.w	#$fc00,d6		
; keep the top 6 bits

	lsr.w	#
2
,d6

	lsr.w	#
8
,d6			
; d6 = the property, 0..63

	bsr
	cbCheck			
; 2 or 3? you can climb this

	bsr
	Checkrmh		
; 10..13? this hurts, and from which side

Checkrmhhands the painful cases to a label calledrmhEnjury, which is
1993 me spelling “injury”.

Those bits were painted in an editor. Before the game could be built I had to
build the tool that builds it:MEDITOR.S, 1,254 lines of assembly, dated by
its own header, in my 1993 English:

; ***********************************************************************

; *		This Program was written in four days			*

; * 			1993-2-8/7/6/5					*

; * I made it to help me to make a map to my first serious		*

; *				Game 					*

; ***********************************************************************

Four days in February 1993. Paint tiles with the mouse, pick a property number
on the panel’s CURRENT FLAG counter, stamp it onto cells with PUT FLAG, and a
flag view marks every cell carrying the selected number. While writing this
post, I asked the model to run the map editor and get a screenshot. It
assembled the 1993 source with a modern assembler, laid the shipped Level 2
data out in memory where the editor expects it, and booted the result in an
emulator.

My own tool at thirty-three years old, editing the real Level 2, flag view on.
CURRENT FLAG reads 0001, solid, and the ground you can stand on is marked
while the decoration you walk through isn’t. The panel says 1994: the panel
artwork is a separate bitmap file the editor loads, and the copy that survived
is a later one than the February 1993 code.

The other name on the panel, Udai, was my partner in Mesopotamia Software,
which is what we called ourselves. He was building a game of his own at the
time. I wrote the editor, for both of us, but its design was worked out
between us so one tool could serve both games. His game was never finished.

### Object tables

Enemies aren’t in the map. The world is stored one screen at a time, 25 tiles by 20, and every screen has a
small table of the objects on it. My 1993 comments explain the markers:

;	$1111=this is a Screen but it contain nothing or(End of Screen)

;	$2222=this is an object but do not draw it (dead)go to next

;	other=this is an object,draw it and go to the next

Scr0:
	dc.w 
$3333
,
50
,
23
,
17
		; a live object: frame, then x, y

	dc.w hiddenwallR-lrb,
20
		; its behaviour: a routine, as an offset

	dc.w 
0

	dc.w 
0

	dc.w 
7

	dc.w 
10
				; parameters only that routine understands

	dc.w 
$3333
,
50
,
12
,
14

	dc.w GreatTR-LRb,
16
,GkeyT-GTT,
1

	dc.w 
$1111
			; end of this screen

An enemy is a row of words: a marker, a frame, a position inside its screen,
then its behaviour.hiddenwallR-lrbis the crumbling-wall routine, attached
as an offset from a base label, the same trick as the arrow thrower earlier.
The words after it are parameters that mean whatever that routine wants them
to mean. Nothing in the file says which word is which, so it found the routine
that walks these tables every frame and let it name the fields, then converted
every object in all five levels to world coordinates and checked them against
the rendered maps.

### GAME.S

Most of the data files scramble their 16-byte headers with a key stored inside
the file, a 1993 trick to keep disk editors out. The retail loader,GAME.S,
has no unscrambling step at all. It read that as a clue:GAME.Swas
written before the scrambling was added,
so it is an older file. That clue is what later let it recover the lost
two-disk retail set, from a sector map inside that same file.

### The doors aren’t in the map

I was sure they were.

Load a level’s tile map and there are holes where every door should be, with
no door tile in them, open or closed. An 18-byte object record stamps them onto
the map at runtime, a 1×4 tile column, from a table:

closed $528 $53C $550 $564 ; solid, blocks the way

open $129 $13D $151 $165 ; passable — exactly one sheet-column right

The map data says there’s no door. The level code says there is. For
thirty-three years I’d have told you the map is the source of truth and doors
are map data, and I’d never have looked. It held both facts, found the routine
that reconciles them, and came back with the design: doors are drawn by code
at runtime; they were never painted into the map in the editor. That’s why
the obvious port of the level data produces a tower with doorways full of
sky.

### The copper sky

In every level, colour index 31 is the sky, and nothing in the tile art ever
paints it. The tile atlas renders it transparent, and behind it the copper
repaints the background colour on chosen scanlines to make a vertical
gradient. The gradient sits in the level source as a plain list of colours.
This is the entire sky of the second level:

backgndcol:

col1:
 dc.w 
$09FF
,
$09FF
,
$09FF
,
$09FF
,
$09EF
,
$09EF
,
$0ADF
,
$0ADF

 dc.w 
$0ACF
,
$0ACF
,
$0ABF
,
$0BBF
,
$0BBF
,
$0CBF
,
$0CBF
,
$0DCF

 dc.w 
$0DCF
,
$0ECF
,
$0DCF
,
$0DCF
,
$0CCF
,
$0CCF
,
$0CDF
,
$0CDF

Read down the list and the sky goes from pale blue to warm near the horizon.

The same 24 words, rendered. Left is the top of the screen.

The first rebuild missed it, and the levels looked fine. Flat, in a way I
couldn’t name. The pixel comparison refused to go green, and the gradient went
back in.

The diff that would not go green: white is every pixel the first rebuild got wrong, the copper's sky and water.

### Sprite sheet ambiguity

Amiga sprite sheets are planar (five separate 1-bit bitplanes in plane-major
strips, plus a transparency mask), and all of that was worked out from the
draw routines and theorgarithmetic. Sheet sizes of the formframes * width * height * 2 * 5are
ambiguous: that2could mean double-width frames, or two stacked rows, one
per facing direction. Both readings fit every byte in the file. It’s two
facing rows; that was my choice in 1993.

Two stacked rows, one per facing direction, drawn frame by frame, not mirrored.

It flagged the ambiguity and asked.

The same twin, the same six frames: 1993 above, 2026 below.

That was the last format. From there the 1993 game went into Godot the same
way the C++ had, behaviour rewritten in GDScript at the original 50 Hz.

## Step three: the old game inside the new one

The greedy ask took one evening, 21:58 to 23:43. The retro game runs as a
guest, with its own namespace and scene host, and the engine switches to
50 Hz on the way in and back to 60 on the way out. It’s fiddly, and it was
done in one sitting. I’d assumed the feature would eat a week and get cut.
It’s the reason the Steam version ships with the 1993 game inside
it.

The same doorway in both games, running in the same program. Left: 1993. Right: 2026.

The game you download contains no Amiga code. The data, the packed chunks and planar graphics
and the music, was decoded once, on my machine, by Python scripts, into
ordinary PNG, WAV and JSON. The behaviour (how a guard patrols, when a door
opens) was rewritten in the engine’s own language. If you want the real
thing, that’s the free disk image at the end of this post and
an emulator.

## Where it was wrong

### The guard bug

In level 2 you walk along a corridor. Waterfall to your left, stone pillar
ahead. No enemy on the screen, nothing approaching, and you take a hit. What
hit you was a spear-carrying soldier standing thirteen tiles above you, on a
grass ledge next to a palm tree, with solid rock in between.

He’s a doorman. He shoves whoever stands at his feet. In the original that
check is fenced on both sides:

 sub
.w d1,d4 
; d4 = vertical distance to the kid

 cmp
.w #
4
,d4

 bpl
 Sg.
Far
 ; 4 or more rows below? not my problem

 cmp
.w #-
2
,d4

 bmi SG.
far
 ; too far above? also not my problem

The port kept the lower bound and dropped the upper one. A shove meant to
cover the guard’s own three rows now ran the whole height of the map column
beneath him, through the floor, into a corridor he doesn’t appear in.

The doorman himself, from the 1993 sheet.

Smaller ones: every level has a second tile layer the original never
renders; it’s the hidden artwork revealed when a door opens or a fake wall
crumbles. Render it “faithfully” and every secret passage stands open from
the start. Move enemies before players instead of after, and a trampoline jump
gets counted twice, twenty tiles into the air. A door listed"p1,p2,p3,p4",
meaning all four palms, was read as a single key with a strange name, and the
tutorial exit never opened. A sound-loop length computed as stereo when the
effects are mono cut every sound off halfway and restarted it.

The one that cost the most was a feature I asked for in the 1993 build: let
the twins swap places at any distance. The proximity check came out, and the
statues started corrupting. It went back into the routine and came out with the real
answer, which wasn’t what I expected: that check was never a distance
limit. The idle twin is stamped into the map itself as a statue, and
two statues stamped on top of each other eat each other’s tiles. The guard
went back in, and I killed the feature on the 1993 build.

I made the same kind of mistake myself in 2010, slowly, over months.

## Then it shipped it

Then it did the release work: screenshots at five pixel sizes in eleven
languages, a preview video, store text, icons in six shapes, uploaded to three
stores that disagree about everything. I’ve shipped this game before, so I
know how many evenings that part costs.

The screenshots come out of the game itself. It launches the real game at each
store’s pixel size, in the language it needs, walks the character to a chosen
spot, takes the shot, then draws the caption band with the game’s own fonts.
AI never renders the text in a store image. The captions are real fonts and
real translated strings, or the image doesn’t ship. Once it did break, and the
Russian and Korean captions came out as rows of empty boxes, which I saw in
the output folder before uploading.

My complaint about Steam is that it has many fields in its forms, many more
than the Apple App Store and the Google Play Console. In addition, it doesn’t
have an API to make the process of metadata updates easy. For iOS and Android
there are proper APIs and it used them. Steam has a web dashboard, so it drove
the browser: store page fields, achievements, the demo checklist, artwork
uploads, clicking through Steamworks. I do the login, and I
press anything that submits, publishes, prices or releases. It fills in the
forms.

It reads my reviews too. The official Google Play API only gives you the last
seven days, which is useless for a game with fifteen years of reviews, so it
pulls the rest with the public scraper, one language at a time. Then it read all of them and listed which ones
described real defects. I approved the list.

One of them was a one-star review on Google Play, bad spelling, the kind you
scroll past:

“cant get through door on level one. opens but level dowsnt end”

Read literally, it’s a bug report, and it was right. In my game, opening
the exit and walking through it are two separate actions, and the prompt that
says so exists in all eleven languages, placed in exactly two of my eighteen
levels. One of the levels missing it was the last free one. So the player
deciding whether this game is worth paying for was standing in front of an
open door with no way to know what to do, and concluded the game was broken.

I never found that in fifteen years, and neither did my testers or two
rebuilds. It took a stranger’s one-star review. The fix went out as 2.0.3 on both
stores. I keep that review.

## The trampoline bug

“The trampoline feels too high.” That was the whole report, from me, playing
the build at night. The
constants checked out: a twenty-line simulation of the original’s integrator
predicted 19.1 tiles, and the build measured 19.5. The physics was right.

It was input semantics. The 2010 build was event-driven, and because of a
workaround for a tvOS quirk we shipped years ago, a held jump button read as
released until you physically pressed again. Godot polls input, and kept
reporting the hold. Reproducing that accident is what makes the high bounce
need a fresh, well-timed press, which is how the game played on a phone, and
what my hands were expecting.

The 2010 source doesn’t record this, because from the source’s point of view
nothing unusual is happening. You’d have to have been
there, holding the phone, working around a bug in a television.

## The original, released

After thirty-three years, the full original is out, free onitch.io. Boot it in FS-UAE,
WinUAE, or on real hardware. The Definitive Edition is on iOS and Android now,
has a free demo on Steam, and the full Steam release (Windows, Mac, Linux)
lands this fall, with the 1993 game inside it as a second launch option.

The port was Claude Fable 5 running in Claude Code; I asked, played, and
decided. This post went the same way. I gave it my notes from the port, what
I remember about the key parts of the old game (the map encoding, the object
tables), and the repos for both the Amiga version and the port, and it wrote
a first draft. I spent a week editing it line by line. The code, timestamps
and screenshots are real. The part I’m least sure of is the 108 bytes: the
model told me the shipped files were a memory snapshot saved after a run, and
that the code writes those variables before it reads them. I read that, moved
on, and have never checked it myself.

One slice from each of the five levels, rendered from the extracted map data.

Babylonian Twins: Definitive Edition comes to Steam this fall —wishlist it here.Free demo available now · live today on iOS and Android · the original 1993
ADF isfree on itch.

 
 
 
Play Babylonian Twins →