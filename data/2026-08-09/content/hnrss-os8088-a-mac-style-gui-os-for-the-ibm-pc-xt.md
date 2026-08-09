---
title: os8088 -- a Mac-style GUI OS for the IBM PC XT
url: https://os8088.com/
site_name: hnrss
content_file: hnrss-os8088-a-mac-style-gui-os-for-the-ibm-pc-xt
fetched_at: '2026-08-09T11:26:34.748725'
original_url: https://os8088.com/
date: '2026-08-08'
description: A Macintosh System 1-style graphical OS for the Intel 8086/8088. Real-mode assembly, boots from floppy, runs in 256KB. Free to download.
tags:
- hackernews
- hnrss
---

os8088 1.0

# A graphical operating system for the IBM PC/XT

A Macintosh System 1-style desktop for the Intel 8086, written in real-mode
 assembly and booted from a floppy. Overlapping windows, pull-down menus, a serial mouse,
 loadable programs, and pre-emptive multitasking -- which the 1984 Macintosh did not have.

in VGA, 16 colors
640x480 

in Hercules, mono
720x348 

in CGA, mono
640x200 

of RAM
256K

byte kernel
78,950

pre-emption, 12 tasks
18.2Hz

Boot it in your browser

Download the floppies

Screenshots

os8088

Five programs running at once.A Note Pad loaded off the software floppy, a ticking Clock, a bouncing ball, the Control
 Panel and the Task Manager, each a separate instance with its own dock tile. The Task
 Manager reports the machine at 70% busy and 147K of RAM in use.

The desktop at rest, a few seconds after boot.The 512-byte boot sector has loaded the kernel and jumped to it. There is a floppy icon for
 each drive the machine reports through the BIOS, and the dock is empty because os8088
 launches nothing at startup.

A menu is open only while the button is held.Press in the menu bar, drag through the items, release on the one you want. There is no
 spare copy of the screen to restore from, so the pixels behind the pull-down are copied
 into a block claimed off the heap for exactly as long as the menu is up.

A title-bar drag, caught halfway through.The window has not moved yet. A hollow one-pixel outline tracks the pointer in XOR mode, so
 erasing it is the identical operation to drawing it -- you can watch it invert the Disk
 window's own title text where it crosses.

Several instances of the same program.A Disk window, two Clocks and two Bounces, each a separate record in the instance table,
 each cascaded sixteen pixels down and right from the previous copy of its kind. Every
 instance gets a dock tile, and the tile's position is its table slot.

Keystrokes reach the front window only.Two lines typed on the emulated keyboard, wrapped in the window's 258-pixel content area,
 with the caret after the last character. Each Note Pad instance gets its own 512-character
 buffer, and as many can be open at once as the heap has room for.

The About box reads live kernel state.The wordpre-emptiveon the third line is rendered from the kernel's scheduler
 byte every time the box paints, so the About box, the Control Panel and the Task Manager
 cannot disagree about which scheduler is running.

The Task Manager, with its history graph filled.One sample every nine ticks into a 160-column ring, so a full sweep across the window is
 about eighty seconds of history. Apps with no task of their own get their window callbacks
 timed at the dispatch site and billed to them, so the rows still add up to one total.

The scheduler setting, read straight from the kernel.The settings pane keeps no copy of the scheduler mode: it reads the kernel's mode byte every
 time it draws. Click Cooperative and the very next timer tick declines to switch tasks, with
 no restart and no handshake.

Two of these five programs are minimized.Clock and Bounce were sent to the dock with the minimize box in their title bars, and their
 tiles draw inverted so you can see at a glance what is hidden. Minimized is not stopped --
 the Clock is still counting, it only skips drawing.

The file manager, reading the software floppy.The software disk mounted on drive B:, with each file's name, size and its own icon. The
 icons come off the disk itself -- the browser peeks each file's first sector, where a
 package carries its own 16x16 bitmap -- so the list shows a real icon without loading it.

Two loaded programs, each in its own segment.MINES and HELLO came off the same floppy into separate regions claimed off the heap --
 2,048 bytes and 512 -- and each runs at offset zero inside its own, so nothing had to be
 patched on the way in.

Minesweeper: 1,510 bytes, loaded from the floppy.Double-clicking the MINES row read it into a segment of its own and opened its window; from
 then on its paint, key and click procs are plain near offsets the kernel calls exactly like
 a built-in's. This board is the only place in the system that uses more than two colors.

ArtfulType, a Markdown writer.ActionRetro's writing app for classic 68k Macintoshes, rebuilt for the 8086. Full-screen
 Writer mode with its own menu bar, styling as you type, and plain Markdown files that open
 anywhere else.

Tracker, a four-channel MOD player.Load an Amiga.MODoff the floppy and play it: the pattern scrolls under the
 playing row, four channel meters move with the music, and the desktop stays usable while it
 plays.

Paint, a bitmap editor.Pencil, eraser, fill, shapes, selection, eyedropper and text, with a resizable canvas, undo,
 a clipboard and sixteen colors. Reads and writes BMP and GIF.

Fractal, a Mandelbrot explorer.Zoom in, pick a color scheme, and watch the picture sharpen through three passes. It draws
 in the background, so the rest of the desktop keeps working while it renders.

Piano, a two-octave keyboard.Play it with the mouse or the computer keys. Notes appear on the staff above as you play,
 and the staff plays back. Three built-in songs, and FM synthesis on a machine with a sound
 card.

Recorder, for sampled sound.Record, stop and play, with a waveform display and a built-in demo tone. It uses a Sound
 Blaster where the machine has one and the PC speaker where it does not; the status line says
 which.

Solitaire: Klondike.Deal from the stock, drag cards and runs between the seven columns, build the four
 foundations up from the aces. Cards drag with an outline, the same way windows do.

Arkanoid, a brick-breaker.Move the paddle with the arrow keys, clear six rows of bricks, keep the score across levels.
 The ball runs on its own timer, so it keeps a steady speed whatever else is happening.

Minesweeper, on a 9x9 board with ten mines.Click a cell to open it,Ffor flag mode,Nfor a new game. Empty
 regions open in one click, and the first click is always safe -- the mines are laid after
 you have chosen where to start.

Note Pad, a plain text editor.Word wrap, a caret, and Open, Save and Save As through the system file dialog. It writes
 ordinary files onto the FAT12 floppy, so a note written here opens on a modern computer.

Hello: a window with two lines of text.It does nothing else. It ships as the smallest working example for anyone writing a program
 of their own, and as the only package with no icon, which is why the Disk window draws it
 with the generic one.

Back

Pause

Next

## What it is

os8088 boots from the first sector of a floppy into a graphical desktop. There is no DOS
 underneath it and no command line anywhere in it -- the 512-byte boot sector loads a
 40KB kernel, the kernel works out which display adapter the machine has and switches it
 into graphics, borrows the video card's own 8x8 character set, and puts up a menu bar.

Everything after that is the interface you remember from a 1984 Macintosh: windows you
 drag by the title bar with a rubber-band outline, menus you pull down and drag through,
 a close box and a minimize box, icons for each floppy drive, and a dock along the bottom
 with one tile per running program. Programs load from a second floppy and run as
 first-class applications, several at a time.

The whole thing fits in 256K of RAM on an Intel 8086 or 8088 -- the processor in the
 original IBM PC and PC/XT. It is a hobby project, finished enough to use. The source is
 real-mode NASM assembly, written with AI, and it is on GitHub.

Video log

## Video log

os8088 gets recorded as it is built -- one video per step, from the
 first boot into a desktop to loadable packages. They are all onthe video log.

## By the numbers

Every figure below comes from the build.

Verified specifications of os8088

Kernel size
78,950 bytes
The scheduler, window manager, VGA driver, mouse driver, sound layer, file manager, loader, Task Manager and Control Panel, all of it.

Boot sector
512 bytes
LBA-to-CHS translation and retrying BIOS floppy reads. The build fails if it assembles to anything else.

Segment footprint
53,842 bytes
Code plus every buffer the kernel reaches through DS. It must fit the 64K segment -- currently 11,694 bytes of headroom. The task stacks, the disk buffers and every loaded program live outside the segment and are not counted here.

Source
real-mode assembly
NASM for the 8086, written with AI. No C, no linker, no runtime library.

Display
VGA, Hercules or CGA
Probed at boot. VGA mode 12h is 640x480 in 16 colors -- four 1-bit planes, 80 bytes per scanline; Hercules is 720x348 and CGA 640x200, both monochrome and banked. Drawn straight to the framebuffer on all three.

Back buffer
optional, off by default
An off-screen copy of the screen is 153,600 bytes, more than half the machine's memory, so a 256K machine always draws straight to the display, as the 1984 Macintosh did. At 500K or more the Control Panel can switch one on.

Tasks
12 slots, 1,536-byte stacks
Each Clock and each Bounce window is its own pre-empted task.

Context switch rate
18.2065 Hz
The PC's stock timer rate. Every tick the handler saves nine registers, swaps the stack pointer and returns into a different program.

Loadable programs
a segment each
Packages loaded from a second floppy into their own regions of conventional memory -- about 107K of arena on a 512K machine, 233K at 640K -- several resident at once, each freeing its memory when closed.

Mouse
1200 baud, 7N1
A Microsoft serial mouse on COM1, three bytes per report, decoded in an interrupt handler that also draws the cursor.

Target hardware
IBM PC/XT, 8088 at 4.77MHz
256K of RAM, a serial mouse, and any of a VGA, Hercules or CGA card. Repaints are slow enough to watch happen.

Instruction set
8086 only, enforced
cpu 8086
 plus 
-w+error
, so anything newer is a build failure. A 1978 instruction set, mechanically guaranteed.

## What it does

Four things it does. There are more on thescreenshots page.

Pre-emptive multitasking

No program has to cooperate.

 Two clocks keep time and two balls keep moving while you type into something else. The
 timer interrupt fires 18.2 times a second, saves whichever task was running, swaps the
 stack pointer and returns into the next one -- about thirty instructions. The Macintosh
 of the period did not do this: System 1 ran one application at a time, and MultiFinder,
 which arrived in 1987, was cooperative.

Rubber-band dragging

The window does not move until you let go.

 A one-pixel XOR outline follows the pointer and the window is redrawn once, at the
 release. Repainting a whole window on every mouse report is not affordable at 4.77MHz,
 which is why the 1984 Macintosh did the same thing.

Loadable software

Programs come off a second floppy.

 Double-click a file in the Disk window and it loads into a segment of its own and runs as
 a real application. Minesweeper is 1,510 bytes including its icon. Several packages -- or
 several copies of one -- can be resident at the same time.

Task Manager

The system reports on itself.

 A live CPU meter with a scrolling history graph, a RAM readout, and one row per running
 program. Apps without their own task get their window callbacks timed at the dispatch
 site and billed to them, so the rows still add up to one total.

All the screenshots

## On real hardware

Everything above was captured in an emulator. In August 2026 the disk images were written
 onto real floppies and booted on three period machines -- a 1981 IBM 5150, a Toshiba T1100
 Plus and a 286 -- and photographed.

IBM 5150, 8088 at 4.77MHz

Six programs at once on a 1981 IBM PC.

 A 5150 driving a Hercules card at 720x348, booted off a 360K floppy, with the machine's own
 card list typed into a Note Pad loaded from that same disk. Photographed by
 
Elendilon
, who reported no
 noticeable speed difference against the same system under emulation.

os8088 on real hardware

## Some history

In February 1985 Digital Research shipped GEM 1.0 for the IBM PC: a Macintosh-style
 desktop with overlapping windows and icons, running on stock XT hardware. Apple sued.
 The settlement led to GEM Desktop 2.0 in 1986, which removed overlapping windows and
 desktop icons on the PC -- while the Atari ST version, not covered by the agreement,
 kept them.

So the PC briefly had this and then did not. os8088 is a rebuild of roughly that idea,
 from scratch, forty years later, on the same class of machine, plus the pre-emptive
 multitasking neither GEM nor the Macintosh of the period offered.

## What it is not

* It is not DOS and it does not run DOS programs. There is no DOS underneath it; it owns
 the machine from the boot sector up.
* It has no memory protection. The 8086 has none to offer -- every program shares one
 64K segment with the kernel, which is what makes a context switch cheap enough to be worth
 doing.
* There are no file handles and no seeking. The disk API moves whole files at a time:
 write, read, delete, rename.
* There is no networking.
* It is a hobby project, not a product, though it is complete enough to sit down and
 use.

## Try it

The browser demo boots the floppy image in an emulated PC -- the same bytes you would
 write to a disk. To run it yourself, the download page has 360K images for period hardware
 and 86Box, and 1.44MB images for QEMU.

Boot it in your browser

Download

How it works