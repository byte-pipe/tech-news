---
title: 'Add DOS platform support (DJGPP) by AJenbo · Pull Request #15377 · libsdl-org/SDL · GitHub'
url: https://github.com/libsdl-org/SDL/pull/15377
site_name: hnrss
content_file: hnrss-add-dos-platform-support-djgpp-by-ajenbo-pull-requ
fetched_at: '2026-04-24T19:51:29.178984'
original_url: https://github.com/libsdl-org/SDL/pull/15377
date: '2026-04-24'
description: Simple DirectMedia Layer. Contribute to libsdl-org/SDL development by creating an account on GitHub.
tags:
- hackernews
- hnrss
---

libsdl-org

 

/

SDL

Public

* NotificationsYou must be signed in to change notification settings
* Fork2.7k
* Star15.4k

## Conversation

 

Contributor

### AJenbocommentedApr 13, 2026•edited

This is the combined work of@icculus@madebr@glebm@jayschwa@ccawley2011and me rounding it off with stability fixes and missing features, thanks to everyone for pitching in.

This is a fairly complete port to DOS with only minor features like audio recording missing. I have tested it extensively with DevilutionX in DOSBox. But no real hardware testing. The features I didn't add is mostly because I didn't have a good way to test that they worked correctly.

For threading I took some conceptual inspiration from the PS2 port.

## What's supported

* Video:VGA and VESA 1.2+ framebuffer, RGB, and 8-bit indexed color with VGA DAC palette programming, hardware page-flipping with vsync, VBE state save/restore on exit
* Audio:Sound Blaster 16 (16-bit stereo, up to 44.1 kHz), Sound Blaster Pro (8-bit stereo, up to 22 kHz), Sound Blaster 2.0/1.x (8-bit mono), all via IRQ-driven DMA with double-buffered auto-init
* Input:PS/2 keyboard with extended scancodes (0xE0 prefix), INT 33h mouse with queried sensitivity, gameport joystick via BIOS INT 15h with auto-calibration
* Threading:Cooperative scheduler usingsetjmp/longjmpwith stack patching. Real mutexes, semaphores, TLS, and condition variables (generic fallback). Yield points in the event pump and delay functions keep audio and other threads responsive.
* Timer:Native PIT-based timer using DJGPP'suclock()at ~1.19 MHz resolution
* Filesystem:GetBasePath/GetPrefPathvia DJGPP'ssearchpath(), POSIX filesystem ops fallback
* Build:CMake cross-compilation toolchain file, DJGPP CI job, preseed cache for faster configure

## What's NOT included

* Audio recordingplayback only
* SDL_TIMEnative implementationreuses Unixgettimeofdayvia DJGPP's POSIX layer (works fine)
* Shared libraryloading support (noSDL_LoadObject).

## How to build

cmake -S. -Bbuild-dos \
 -DCMAKE_TOOLCHAIN_FILE=build-scripts/i586-pc-msdosdjgpp.cmake \
 -DCMAKE_BUILD_TYPE=Release
cmake --build build-dos -j$(nproc)

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 
👍

6

 
arrowgent, lifning, gbraad, ancientstraits, pocketrice, and gresolio reacted with thumbs up emoji

 
🎉

40

 
madebr, foxtacles, glebm, natri0, Manawyrm, lessthen3, chkuendig, ccawley2011, ritalat, stianhoiland, and 30 more reacted with hooray emoji

 
❤️

41

 
jayschwa, madebr, qndel, foxtacles, glebm, yuripourre, ncake, Manawyrm, chkuendig, mmuman, and 31 more reacted with heart emoji

 
🚀

6

 
chrisnew, elf-alchemist, vlofgren, volkertb, lifning, and Skywalker13 reacted with rocket emoji

 
👀

2

 
jwt27 and TheBestTvarynka reacted with eyes emoji

 

All reactions

 
icculus

and others

 added 
30
 commits
 
April 13, 2026 08:50

 

 

 

 

dos: Some initial work.

b6c2f2f

 

 

 

 

dos: Turn off buffer on stdio SDL_IOStreams.

 …

 

8bf81e3

Seeking breaks otherwise. We might be able to just fflush() before or seeking
instead?

 

 

 

 

dos: Audio implementation using the Sound Blaster 16.

4c13af7

 

 

 

 

dos: remove audio Pump interface.

 …

 

d0868c7

Turns out DosBox-X was having trouble with the Sound Blaster or something;
standard DosBox works correctly directly from the interrupt handler, and
without doubling the buffer size.

 

 

 

 

dos: just dump and restore the stdio buffer when seeking.

 …

 

dcc721c

This is MUCH faster than just leaving buffering disabled, and also works
around getting bogus reads after an fseek. SDL_LoadWAV on test/sample.wav
no longer takes several seconds to finish, and comes up with the correct
data.

I wonder if we're triggering this in LoadWAV because we're malloc'ing data
between seeks/reads, and it's causing the djgpp transfer buffer to change. Or
maybe the Fat DS trick is confusing it? I don't know, I haven't had time to
debug it, it might just be a legit libc bug in djgpp too, for all I know.

 

 

 

 

dos: Protect audio device "thread" iterations when streams are locked.

 …

 

23ecf0d

This uses an old trick we used in SDL 1.2 for MacOS Classic, which did its
audio callback in a hardware interrupt. If the audio is locked when the
interrupt fires, make a note of it and return immediately. When the lock is
released, if the interrupt has been fired, run the audio device iteration
right then.

Since there isn't a big device lock in SDL3 (available to the app, at least),
this keeps a counter of when any SDL_AudioStream is locked, which is probably
good enough.

 

 

 

 

dos: Implemented initial video subsystem.

 …

 

62726d7

This uses VESA interfaces to manage the display and works with the software
renderer.

Events aren't hooked up yet, so prepare to close DosBox on each run. :)

 

 

 

 

dos: Whoops, forgot to add these to revision control. Core and Main s…

 …

 

ccffbee

…upport.

 

 

 

 

dos: Wired up basic filesystem support.

 …

 

fac1d20

This gets most of the rendering examples, which use SDL_GetBasePath() to
find textures to load, working.

 

 

 

 

dos: Fixed compiler warning.

fcdcad5

 

 

 

 

dos: Initial mouse support!

3028098

 

 

 

 

dos: Move interrupt hooking code into core/dos.

c86a2e3

 

 

 

 

dos: Initial keyboard support!

4b80172

 

 

 

 

dos: Use a simple ring buffer for keyboard events.

 …

 

5fa9dbb

Of course Quake 1 solved this better, haha. It's smart: less memory, dirt
simple, and you don't even have to worry about synchronizing with the
interrupt handler, because it's safe for both sides no matter when an
interrupt fires.

 

 

 

 

ci: add djgpp job

 …

 

1164f40

[sdl-ci-filter djgpp]
[sdl-ci-artifacts]

 

 

 

dos: Fix build issues after rebase onto current main

 …

 

3423584

- SDL_runapp.c: Add SDL_PLATFORM_DOS to the exclusion list so the
 generic
 SDL_RunApp() is disabled when the DOS-specific one is compiled.
- SDL.c: Exclude SDL_Gtk_Quit() on DOS. DJGPP defines __unix__ which
 sets
 SDL_PLATFORM_UNIX, but DOS has no GTK/display server. The GTK source
 is not compiled (CMake UNIX is false for DOS) so this was a link
 error.
- sdlplatform.cmake: Add DOS case to SDL_DetectCMakePlatform so the
 platform is properly detected from CMAKE_SYSTEM_NAME=DOS.
- i586-pc-msdosdjgpp.cmake: Add i386-pc-msdosdjgpp-gcc as a fallback
 compiler name, since some DJGPP toolchain builds use the i386 prefix.

 

 

 

Add 8-bit palette support to DOS VESA driver

4a76c43

 

 

 

Add VBE page-flipping, state restore, and robust keyboard handling

 …

 

750f61a

- Implement double-buffered page-flipping for VBE modes with >1 image
 page
- Save and restore full VBE state on video init/quit for clean mode
 switching
- Improve DOS keyboard handling: support extended scancodes and Pause
 key
- Lock ISR code/data to prevent page faults during interrupts
- Always vsync when blitting in single-buffered modes to reduce tearing

 

 

 

Refactor Sound Blaster audio mixing to main loop

 …

 

8c07e7d

Move audio mixing out of IRQ handler to main loop for improved
stability and to avoid reentrancy issues. Add SDL_DOS_PumpAudio
function, update DMA buffer handling, and adjust sample rate to 22050
Hz.
Silence stale DMA buffer halves to prevent stutter during load.

 

 

 

Add DOS timer support and update build config

998baf8

 

 

 

Add support for pre-SB16 8-bit mono Sound Blaster audio

 …

 

ed6adf2

Detect SB version and select 8-bit mono or 16-bit stereo mode.
Handle DMA and DSP setup for both SB16 and pre-SB16 hardware.
Add FORCE_SB_8BIT option for testing in DOSBox.

 

 

 

Add SB Pro stereo support and simplify IRQ handler

cf1e599

 

 

 

Add DOS joystick driver support

d3b2510

 

 

 

Improve DOS hardware handling and clarify memory allocation

 …

 

8565d56

- Poll Sound Blaster DSP status instead of fixed delay after speaker-on
- Clarify DPMI conventional memory is always locked; update comments
- Document and justify DMA memory allocation strategy
- Free IRET wrapper after restoring interrupt vector to avoid leaks
- Throttle joystick axis polling to ~60 Hz to reduce BIOS timing loop
 cost
- Always poll joystick buttons directly for responsiveness

 

 

 

Query and use mouse sensitivity from INT 33h function 0x1B

d9a7438

 

 

 

Add support for VESA banked framebuffer modes

 …

 

9d631c4

Implement banked framebuffer access for VBE 1.2+ modes without LFB.
Detect and initialize banked modes, copy framebuffer data using bank
switching, and blank the framebuffer on mode set. Page-flipping is
disabled in banked mode.

 

 

 

Add optional vsync to page flipping in DOS VESA driver

6a29b3b

 

 

 

Add cooperative threading support for DOS platform

9cce6b1

 

 

 

Move SoundBlaster audio mixing to SDL audio thread

738fa40

 

 

 

Fix DOS platform comments and workarounds for DJGPP support

1abf5d8

 

 127 hidden items
 

 Load more…
 

 

 
AJenbo

 

 added 
4
 commits
 
April 23, 2026 03:02

 

 

 

DOS: Cap mouse range

e1d21fd

 

 

 

DOS: Map test resources to 8.3 names

4c8867c

 

 

 

DOS: Skip unsupported WM color modes

e277825

 

 

 

Fix "windowed" resolution selection

479a6b4

 

 

Contributor

Author

### AJenbocommentedApr 23, 2026•edited

Done:

(and Quake still works)

There are a couple of issues with some standard formatting functions that makes it unable to finish the automation tests, I patched around it and got the test to complete, there where still some failing cases that I haven't looked in to and I don't feel confident enough about how to correctly patch the failing formatting functions to include them either, most demos works as one would reasonably expect I think.

@sloukenif it was up to me I would probably squash merge this PR, GitHub will still provide a reference from the resulting commit to the PR where all the steps can be viewed.

This would also give you a chance to add propper attributions to@glebmand@jayschwawho also contributed significant code.@ccawley2011's 1.2 port was mostly used for comparison, but they did significant testing and reviewing so I think it would be fair to include them as well.So add this on top of what GitHub suggests:

Co-authored-by: Gleb Mazovetskiy <glex.spb@gmail.com>
Co-authored-by: Jay Petacat <jay@jayschwa.net>
Tested-by: Cameron Cawley <ccawley2011@gmail.com>

 

All reactions

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

 

madebr

 reviewed

 

Apr 23, 2026

 

View reviewed changes

 

 

Comment thread

test/CMakeLists.txt

endif()

if(DOS)

 set(NAME83_LONG "unifont-15.1.05.hex;unifont-15.1.05-license.txt;physaudiodev.png;logaudiodev.png;audiofile.png;soundboard.png;soundboard_levels.png;trashcan.png;msdf_font.png;msdf_font.csv;gamepad_front.png;gamepad_back.png;gamepad_face_abxy.png;gamepad_face_axby.png;gamepad_face_bayx.png;gamepad_face_sony.png;gamepad_battery.png;gamepad_battery_unknown.png;gamepad_battery_wired.png;gamepad_touchpad.png;gamepad_button.png;gamepad_button_small.png;gamepad_button_background.png;gamepad_axis.png;gamepad_axis_arrow.png;gamepad_wired.png;gamepad_wireless.png;sdl-test_round.png")

 

 

Contributor

### sulixcommentedApr 23, 2026

The latest version is working well here for non-fullscreen windows (in both the test programs and my own code). Fullscreen is giving an empty black screen at the moment, though (e.g.draw.exe --fullscreen).

Still, this is definitely usable for me, on both DOSBox and DOS 6.22 on a Vortex86 board (albeit slowly). I'll try it out on a more extensive set of systems sometime in the next ~week, too.

Thanks very much!

 
👍

1

 
evktalo reacted with thumbs up emoji

 

All reactions

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

 

 

DOS: Hide INDEX8 modes behind SDL_DOS_ALLOW_INDEX8_MODES

16b180a

 

 

Contributor

Author

### AJenbocommentedApr 23, 2026•edited

The issue wasSDL_GetClosestFullscreenDisplayMode()dropping the mode to INDEX8 and the application not knowing how to render at INDEX8.

The way I hangled this in the internal equivalent was that I only considered INDEX8 modes if the user had already set an INDEX8 fullscreen mode, for SDL to generally support INDEX8 as a display modeSDL_GetClosestFullscreenDisplayMode()should probably be changed to do something similar, it would probably be good to make it more explicit about how it chooses between bpp in general, right now it will probably give you a random bpp based on what order the driver lists modes in and not what bests matchs your current pixel format.

For now I have guarding INDEX8 behindSDL_HINT_DOS_ALLOW_INDEX8_MODESso that applications have to explicitly opts into it when they are able to handle it properly.

 

All reactions

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

 

Collaborator

### sloukencommentedApr 23, 2026

The issue wasSDL_GetClosestFullscreenDisplayMode()dropping the mode to INDEX8 and the application not knowing how to render at INDEX8.

This might actually be fixed if you rebase against main. We just changed it so we take the highest bit depth (first mode in the list) rather than the lowest (last in the list). I'd prefer that if it works rather than adding another hint.

 
😄

1

 
AJenbo reacted with laugh emoji

 

All reactions

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

 

Contributor

Author

### AJenbocommentedApr 23, 2026•edited

This might actually be fixed if you rebase against main. We just changed it so we take the highest bit depth (first mode in the list) rather than the lowest (last in the list). I'd prefer that if it works rather than adding another hint.

That does solve the bpp issue ... but now I get 1024x768 when asking for best fit for 640x480. This wasn't the case previously so it sems it's part fix part breakage.

Should I just rebase and then you guys can fixSDL_GetClosestFullscreenDisplayMode()separately?

 

All reactions

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

 

Collaborator

### sloukencommentedApr 23, 2026

This might actually be fixed if you rebase against main. We just changed it so we take the highest bit depth (first mode in the list) rather than the lowest (last in the list). I'd prefer that if it works rather than adding another hint.

That does solve the bpp issue ... but now I get 1024x768 when asking for best fit for 640x480. This wasn't the case previously so it sems it's part fix part breakage.

Should I just rebase and then you guys can fixSDL_GetClosestFullscreenDisplayMode()separately?

I reverted the change. I don't have time to look into it right now, so if you want to investigate and provide a separate PR for a better fix, I can include that.

 
👍

1

 
AJenbo reacted with thumbs up emoji

 

All reactions

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

 

 

Remove SDL_HINT_DOS_ALLOW_INDEX8_MODES and order modes logically

74ea44f

 

 

Contributor

Author

### AJenbocommentedApr 23, 2026•edited

@sloukenI removed theSDL_HINT_DOS_ALLOW_INDEX8_MODES, if you can merge#15442then it should allow automatic mode selection to work correctly for applications that don't set a palette and don't pick there full screen mode them selfs, so I think it's ready to merge as well. I would really prefer not to end up in a rabbit hole of fixing existing issues in SDL here.

P.s. I'm happy to help with fixes, testing and improvements as follow ups.

 

All reactions

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

 

Collaborator

### icculuscommentedApr 23, 2026

Let's merge both these things and call this good to go!

I'll do so shortly if there are no objections.

 

All reactions

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

 

Contributor

### madebrcommentedApr 23, 2026

Doessprite.exework for you? It closes immediately for me on DOSBox.wm.exeanddraw.exerender nothing (but close on pressing ESC).Running testpalette segfaults.

 

All reactions

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

 

Contributor

Author

### AJenbocommentedApr 23, 2026•edited

Doessprite.exework for you? It closes immediately for me on DOSBox.wm.exeanddraw.exerender nothing (but close on pressing ESC). Running testpalette segfaults.

@madebrthis PR currently depends onthe other PRfor demos to render anything other then black becauseSDL_GetClosestFullscreenDisplayMode()currently prefer the lowest color depth, which for this port is INDEX8 and so would requires the application to set a palette. sprinte.exe doesn't crash for me either way, you would have to get theSDL_Log()or the DJGPP crash dump for me to know what that's about.

 

All reactions

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

 

Collaborator

### icculuscommentedApr 23, 2026

Other PR is merged. Last call on DOS pull request!

 

All reactions

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

 

Contributor

### madebrcommentedApr 23, 2026

@madebrthis PR currently depends on#15442for demos to render anything other then black because SDL_GetClosestFullscreenDisplayMode() currently prefer the lowest color depth, which for this port is INDEX8 and so would requires the application to set a palette

That was it. Merging that pr locally got everything working :)

Only thing is the cursor not being transparent.

 

All reactions

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

 

 

Don't convert cursor if dest is not INDEX8

3a8a287

 

 

Contributor

Author

### AJenbocommentedApr 23, 2026

Only thing is the cursor not being transparent.

Fixed

 

All reactions

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

 

Collaborator

### icculuscommentedApr 23, 2026

Worry about cursor later?

 

All reactions

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

 

Contributor

Author

### AJenbocommentedApr 23, 2026•edited

Worry about cursor later?

To late I already fixed it :D

(I fixed it by using an unoptimized, version for RGB modes, and yeah lets worry about optimizing that til later. It should be correct in both RGB and INDEX8 (what@ccawley2011had issues with originally) now, slightly better performance on XRGB1555 and RGB565 is very minor I think)

 
🚀

2

 
madebr and icculus reacted with rocket emoji

 

All reactions

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

 

madebr

 approved these changes

 

Apr 23, 2026

 

View reviewed changes

 

 

### palxexcommentedApr 23, 2026

A question: due tohttps://www.vogons.org/viewtopic.php?f=63&t=57420, some Nvidia GPUs' 4f07(SetDisplayStart) not works well, though it reports. In my test the range maybe even bigger, up to 3060, down to 9300(not be complete, as we can only test on owed GPUs）. In test I also observed the display problem in our project. But disabling features based on GPU vendor in SDL seems unwise; maybe we need a new hint to let users control page_flip_available directly?

 

All reactions

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

 

Collaborator

### icculuscommentedApr 23, 2026

We can add that later (unless@AJenbohas already pushed it while I'm typing this, haha).

 

All reactions

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

 
Hide details

View details

icculus

 merged commit 
a8ecd67

 into

 

libsdl-org
:
main

Apr 23, 2026

 46 checks passed
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

 

Collaborator

### icculuscommentedApr 23, 2026•edited

Too late, it is merged! :)

Excellent work,@AJenbo. You went above-and-beyond on this work.

(Thank you to everyone else, too!)

I'm considering this a 3.6.0 feature, so let's not cherry-pick it to 3.4.x.

 
🎉

7

 
madebr, glebm, otonoton, AJenbo, foxtacles, ccawley2011, and DaMan69 reacted with hooray emoji

 
🚀

2

 
madebr and glebm reacted with rocket emoji

 

All reactions

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

 

AJenbo

 
 deleted the
 

 sdl3-dos

 

 branch

 
April 24, 2026 01:23

 

Contributor

Author

### AJenbocommentedApr 24, 2026

A question: due tohttps://www.vogons.org/viewtopic.php?f=63&t=57420, some Nvidia GPUs' 4f07(SetDisplayStart) not works well, though it reports. In my test the range maybe even bigger, up to 3060, down to 9300(not be complete, as we can only test on owed GPUs）. In test I also observed the display problem in our project. But disabling features based on GPU vendor in SDL seems unwise; maybe we need a new hint to let users control page_flip_available directly?

If you enableSDL_HINT_DOS_ALLOW_DIRECT_FRAMEBUFFERthat probably isn't relevant.

 

All reactions

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

 

Sign up for free

to join this conversation on GitHub
.
 Already have an account?
 
Sign in to comment

Add this suggestion to a batch that can be applied as a single commit.
This suggestion is invalid because no changes were made to the code.
Suggestions cannot be applied while the pull request is closed.
Suggestions cannot be applied while viewing a subset of changes.
Only one suggestion per line can be applied in a batch.
Add this suggestion to a batch that can be applied as a single commit.
Applying suggestions on deleted lines is not supported.
You must change the existing code in this line in order to create a valid suggestion.
Outdated suggestions cannot be applied.
This suggestion has been applied or marked resolved.
Suggestions cannot be applied from pending reviews.
Suggestions cannot be applied on multi-line comments.
Suggestions cannot be applied while the pull request is queued to merge.
Suggestion cannot be applied right now. Please check back later.