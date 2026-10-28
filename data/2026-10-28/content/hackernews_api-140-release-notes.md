---
title: 1.4.0 - Release Notes
url: https://ghostty.org/docs/install/release-notes/1-4-0
site_name: hackernews_api
content_file: hackernews_api-140-release-notes
fetched_at: '2026-10-28T12:07:59.336549'
original_url: https://ghostty.org/docs/install/release-notes/1-4-0
author: deaux
date: '2026-10-28'
description: Release notes for Ghostty 1.4.0, released on October 27, 2026.
tags:
- hackernews
- trending
---

* Ghostty Docs
* Install
* Release Notes
* 1.4.0

# Ghostty 1.4.0

Release notes for Ghostty 1.4.0, released on October 27, 2026.

Ghostty 1.4.0 is a major release that includes large performance and
memory improvements, a 100% complete Kitty graphics implementation including
animation and relative placements (the first non-Kitty terminal to do so),
SSH integration improvements, and hundreds more improvements and fixes
across all platforms.

This release features7 months of workwith changes from172 contributorsover2,889 commits. Thank you to all the contributors,
maintainers, community moderators, translators, packagers, and users
who each helped make this release possible.

These release notes are painstakingly and lovingly hand-crafted
by human Ghostty maintainers, including the full changelog. They take
a combined 16+ hours to write, so please enjoy. 🥰

Ghostty is non-profit! Please support development.
Almost all donations go directly to paying contributors. Learn more about how you can help.
Learn more →

## Security

* GHSA-4hwh-wx3w-3fqg.
Paste protection didn't treat carriage returns as line endings, so a
paste could run a command without confirmation in programs that don't
use bracketed paste. This requires user interaction (copy-paste) to
trigger.
* GHSA-mhff-mv4q-fp63.
Malicious Kitty graphics commands could crash or hang Ghostty, force
huge allocations, or in limited cases read or delete files outside the
allowed temporary directories. This only requires displaying malicious
output.
* GHSA-hcr9-7hcr-mjm8.
Malicious terminal output could crash Ghostty, closing every window,
via tmux control mode. tmux doesn't need to be installed. This affects
Ghostty 1.3.0 and 1.3.1.
* GHSA-hp9c-qp4q-cpw3.
The same impact as above, via a tmux control mode layout with a
zero-sized or oversized pane. This affects Ghostty 1.3.0 and 1.3.1.
* GHSA-w9q4-5jvv-mcv4.
Clearing the screen into scrollback could corrupt memory if it deleted
the scrollback page holding a styled or hyperlinked cursor. This only
requires displaying malicious output, but only with a smallscrollback-limitsuch as0. The default isn't known to be affected.
* GHSA-2r63-vmw6-3m3c.
A crafted directory name could make the zsh shell integration send
arbitrary escape sequences, such as silently replacing the clipboard via
OSC 52. bash was affected in a more limited way. This only requirescd-ing into a directory from untrusted content, such as a cloned
repository.
* macOS:GHSA-cw69-wm67-5pv8.
Cmd-clicking a crafted OSC 8 hyperlink could open unsafe local files or
custom URL schemes, leading to arbitrary command execution. Ghostty now
blocks unsafe targets and confirms custom URL schemes. This requires
user interaction (cmd-click) to trigger.
* macOS:GHSA-mfw9-xcr3-7gfp.
The same issue as above for links detected by thelinkconfiguration,
including the default URL matcher. This requires user interaction
(cmd-click) to trigger.
* macOS:GHSA-v8cw-fg4j-jcc4.
Drag-and-drop text skipped paste protection, with the same impact as
above. This requires user interaction (drag-and-drop) to trigger.
* macOS:GHSA-mxqx-236q-wrv7.
Opening a file whose name contains control characters could run a
different command than the one shown in the confirmation dialog. This
requires a crafted file on your system and confirming the dialog.

Note: I requested CVEs for the above advisories weeks ago, but GitHub
hasn't assigned them yet. If/when they're assigned, I will update the
above with proper CVE numbers.

## Highlights

### macOS 27 Support

PRs:#12999#13069#13393#14413#14414

Ghostty 1.4 supports macOS 27 (Golden Gate). Most of the work was
compatibility fixes:

* Tabs in the titlebar (macos-titlebar-style = tabs) lay out correctly
again.
* The native tab bar no longer draws as a solid gray bar on top of your
theme. It now lets the new glass style blend with your terminal
background.
* macos-titlebar-style = hiddenno longer covers the top lines of the
terminal when Reduce Transparency is on.
* The app icon no longer has a thin border.
* The Shortcuts "New Window" action no longer opens two windows when
Ghostty is running without any windows.

Ghostty 1.4 remains fully compatible with prior macOS versions back to
and including macOS 13 (Ventura). See thesystem requirementsfor more details.

Note

Ghostty 1.3.1 works on macOS 27, but it has some of the visual issues
listed above, such as the gray tab bar.

### Kitty Graphics Animation and Relative Placements

PRs:#13943#13939#13935#13934#13893#13933#13389#13270#13281

Ghostty now supports Kitty graphicsanimationandrelative placements.
These were the last major features of the Kitty graphics protocol that
Ghostty didn't support.

Programs that display animated images with the Kitty protocol, such as an
animated GIF shown withkitten icat, now animate in Ghostty instead of
showing a single still frame. Frame transmission, composition, and playback
control are all supported, and animations pause while the terminal isn't
visible. Relative placements let a program position one image relative to
another image's placement, so the child image moves along with its parent.

We also did a full conformance pass against the specification and Kitty
itself, fixing dozens of behavioral differences. For example, images now
scroll with text inside scroll regions (#4323), retransmitting an image
ID replaces the old image (#6711), and invalid image data now gets an
error response instead of silence, which could leave clients hanging. The
full list is in theterminal capabilitiessection.

Kitty graphics are faster, too. Image payloads are now parsed in bulk
with SIMD instead of one byte at a time, making large image transfersabout 16x fasterto parse in our benchmarks (64 MiB of image data,
x86_64 Linux), and drawing images costs much less per frame.

Our Kitty graphics implementation now covers 100% of the published
specification, making Ghostty (and libghostty) the first terminal
to do this outside of Kitty itself.

### Scrollback Compression and Lower Memory Usage

PRs:#13264#13473#13240#13245#14130#14137#14138#14017

Ghostty now transparently compresses scrollback that isn't visible,
reducing the physical memory those pages use by70% to 90%for typical
text-heavy history. Compression only runs while the terminal is idle and
pages are decompressed on demand when you scroll back or search, so it
has no measurable impact on I/O throughput.

Thanks to compression,the default scrollback limit has been raised from
10 MB to 50 MBper terminal. On platforms that support compression, a
full scrollback still generally uses less physical memory than the old
10 MB limit did.

Note

Compression lowersresident(physical) memory, notvirtualmemory, so
look at resident memory when measuring it. It is currently available on
macOS and 64-bit Linux.

Beyond scrollback, memory usage is lower in many places:

* A new, empty terminal now uses about16 KiBof terminal page memory
on macOS, down from 128 KiB in Ghostty 1.3.1.
* On macOS and Linux, memory freed by clearing or trimming scrollback is
now returned to the OS instead of being held until the terminal closes.
* Hidden tabs release their GPU resources. On macOS, with one visible tab
and 20 hidden tabs, GPU memory dropped from about 385 MiB to 18 MiB.
Rebuilding them when a tab becomes visible again takes under a
millisecond.

### Performance Improvements

PRs:#13209#13220#13226#13227#13537#13827#13587#14011#13722#14035#12760

There are performance improvements across the board in Ghostty 1.4
that yield significant gains compared to prior Ghostty versions.

The biggest win came from a surprising discovery: on macOS, the kernel
caps every read from a pty at about 1 KiB no matter how large the read
buffer is. Previously, Ghostty processed each read as it arrived, so per-read
overhead was paid every kilobyte, and the program writing output sat
blocked while we parsed. Ghostty now drains the pty on one thread while
parsing on another, raising end-to-end I/O throughput by25% to 55%on macOS (M4 Max, plain and Unicode text) over Ghostty 1.3.x.

VT processing itself is also much faster. In parser benchmarks, plain
ASCII text went from 128 MB/s to 725 MB/s (5.7x), CJK text got 3.4x
faster, and a 2.6 GB dataset of real-world terminal recordings
fromasciinemais processed about 25% faster.
Together, these changes tookcat-ing a 150 MB text file on macOS from
1.5 seconds to 566 milliseconds.

Other notable improvements:

* Resize:resizing a terminal with a large scrollback is about6x
faster(120x80 with 10,000 lines of scrollback), and 3x to 5x faster
with history full of CJK text or emoji.
* Rendering:the renderer holds the terminal lock2.7x to 11xless per frame, leaving more time for the I/O thread during heavy
output.
* Copy and search:formatting terminal contents as plain text, HTML,
or VT, which backs clipboard copy,write_screen_file, and scrollback
search, is 1.5x to 8x faster.
* Launch (macOS):about 15% faster from launch to visible window, and
27% faster to the first rendered frame.
* Idle energy:on macOS, the renderer's display link now sleeps when
there's nothing to draw. On GTK, hidden tabs stop rendering, matching
macOS.
* Large OSC sequences:OSC 52 clipboard payloads parse about30x
faster, and even short sequences like title changes are about 6x
faster.

### New OpenGL Renderer (Linux, FreeBSD)

PRs:#14052#14269

The GTK app has a new rendering pipeline. It no longer usesGtkGLArea.
Instead, the renderer draws with EGL on its own thread, exports each frame
as a DMABUF, and hands it to GTK to display. Rendering is now
triple-buffered, which should greatly reduce tearing, and no OpenGL calls
run on the main thread anymore, which let us remove a number of
workarounds.

The most visible result is crisp text under fractional scaling. Text and
box-drawing characters are no longer blurry with fractional display
scaling such as 125% or 150% (#1938). We fixed this once before, but it
came back after upstream GTK changes. Ghostty now renders at the window's
true fractional scale, so every rendered pixel maps to exactly one pixel
on screen.

The new render surface needs a system EGL library (seeChanges for Package Maintainers).
On GPU drivers that can't export DMABUFs, Ghostty falls back to copying
frames through the CPU, which is slower but works.

### Kitty Clipboard Protocol

PRs:#13962#13993#13995#13998#14002#14061

Ghostty now implements theKitty clipboard protocol(OSC 5522) on both macOS and GTK. Ghostty 1.3 could parse the protocol
but didn't implement it.

OSC 52 can only read and write plain text. The Kitty clipboard protocol
lets programs running in the terminal read and write any kind of clipboard
data, such as images or HTML, and lets them pick among the formats on the
clipboard. Programs can also enable paste events (mode 5522), which tell
the program what formats a paste contains so it can read the one it
wants. This is how a terminal program can accept a pasted image, for
example.

Clipboard access follows the existingclipboard-readandclipboard-writeconfigurations. By default, reads prompt for permission
and writes are allowed. The permission prompt shows a preview of the
clipboard contents, including images. Programs that send a password can
have your answer remembered for the rest of that terminal session. A newclipboard-write-limit-bytesconfiguration limits the size of a single
write (default 64 MiB). A write over the limit fails and leaves the
clipboard untouched.

### Split Drag and Drop (GTK)

PRs:#10423#13706

You can now rearrange splits on GTK by dragging them, matching the macOS
feature introduced in Ghostty 1.3. When a tab has two or more splits, each
split shows a drag handle at the top. Grab the handle and drop the split
onto any other split, including splits in other tabs and windows. An
overlay shows which side of the target split it will land on. The terminal
contents, working directory, and running processes all move with it.

A newdrag-handleconfiguration controls when drag handles are shown on
both macOS and GTK:auto(default),always, ornever. Withnever,
splits can't be rearranged with the mouse. Hiding the handles was a
common request from users who found them in the way.

On GTK, splits can only be dropped onto other splits. Dragging a split out
to create a new tab or window is macOS-only.

### Terminal Emulation Accuracy

PRs:#14454#13494#14483#14538#14673#14375#14144

Ghostty 1.4 includes dozens of improvements to core terminal emulation. We
now runesctest, Thomas Dickey's
terminal conformance suite, against Ghostty's terminal core in CI.
Alongside that, we fixed many differences from xterm in cursor movement
within margins, tab stops, character sets, mode reports, and more. You
can find the full list of related changes in theterminal capabilitiessection.

Ghostty also supports several new sequences, including soft terminal reset
(DECSTR), extended cursor position reports (DECXCPR), backarrow key mode
(DECBKM), and screen size reports in characters (CSI 19 t). Programs can
also now ask whether the terminal is visible usingvisibility reports(mode 2033), so they can stop rendering while hidden.

Keyboard encoding also matches xterm more closely, with fixes formodifyOtherKeysmode 2 and legacy Alt-as-Escape encoding of non-ASCII
keys.

Two new sequences are disabled by default because they can be abused by
untrusted programs, including ones running on a remote machine:

# Allow programs to resize the window (CSI 8 t)
vt-window-resize-allowed = true

# Allow programs to request screen checksums (DECRQCRA)
vt-xt-checksum-report = true

### SSH Integration withghostty +ssh

PRs:#12582#12814#13533#13844#14472#14854

Ghostty 1.2 introducedSSH shell integration featuresas a work in progress. In Ghostty 1.4, they're backed by a newghostty +sshCLI action: a drop-insshwrapper that prepares the
remote session for Ghostty and then runs the realsshwith your
arguments forwarded unchanged.

ghostty +ssh user@example.com

# Or alias it so every ssh invocation goes through it

alias
 ssh=
'ghostty +ssh --'

Before connecting,+sshinstalls Ghostty's terminfo on the remote host
so the properxterm-ghosttyTERMvalue can be used, and forwardsCOLORTERM,TERM_PROGRAM, andTERM_PROGRAM_VERSION. If the terminfo
install fails (for example,ticisn't available on the remote), it falls
back toTERM=xterm-256color. Flags such as--terminfo=false,--forward-env=false, and--verbosecontrol each step.

Thessh-envandssh-terminfoshell integration features (still opt-in)
now call+sshtoo. Previously, each shell integration carried its own copy
of this logic, which made up roughly a third of our shell integration
scripts. Now bash, zsh, fish, elvish, and Nushell all behave identically,
and you can get the same behavior from scripts or anywhere else by callingghostty +sshdirectly.

The terminfo install itself is also more reliable. Ghostty now always
installs its own bundled terminfo rather than accepting whateverxterm-ghosttyentry the remote already has, and it reinstalls
automatically when a Ghostty update changes the terminfo. It also no longer
needsinfocmpor Ghostty's terminfo on the local machine. Installs are
cached per hostandport, so two machines behind one address no longer
share a cache entry. Andssh-envno longer silently overridesSetEnventries in your~/.ssh/config(#11518).

The+ssh-cachecommand that manages this cache now takes positional
destinations (ghostty +ssh-cache user@example.com) and has a new--prune=30dflag. See thebreaking changesif you
script against+ssh-cache.

## System Requirements

macOS:The minimum required macOS version for Ghostty 1.4 remains
unchanged (macOS 13 Ventura). Ghostty is now compatible with macOS 27.

GTK:Ghostty 1.4 requiresGTK 4.18andlibadwaita 1.7, up from
GTK 4.14 and libadwaita 1.5 in Ghostty 1.3. This aligns with ourGTK/Adwaita version policy.
Notably, Ubuntu 24.04 LTS doesn't meet this requirement. Systems with
older GTK or Adwaita versions can work around this requirement by using an
older version of Ghostty or the Flatpak package.#14330

OpenGL (GTK):The minimum required OpenGL version remains 4.3, but
Ghostty now renders through EGL instead of GTK's OpenGL widget. This
should be invisible for nearly everyone, but if Ghostty fails to start
with an EGL error, please make sure your GPU driver provides a working
EGL implementation.

Important

We previously announced that Ghostty 1.4 would require macOS 14.
Nothing forced our hand to do this in this release, so we kept macOS
13 support.We still plan to drop macOS 13 in a future release.Apple
dropped security support for macOS 13 in the fall of 2025, so we
recommend upgrading regardless.

## Breaking Changes

The following behaviors have changed in 1.4.0:

* copy-on-selecthas been reworked and now acceptsnone,primary,clipboard, orboth.The meaning ofclipboardhas changed:it
previously copied to both the selection clipboard and the system
clipboard, and now copies only to the system clipboard. If you setcopy-on-select = clipboardand want the old behavior, change it toboth.#12600#12604
* macOS:copy-on-selectnow defaults tonone(previouslytrue), so
selecting text no longer copies it anywhere and middle-click paste of the
selection no longer works by default. To restore the 1.3 behavior, setcopy-on-select = primary. Note that an explicitcopy-on-select = trueon macOS now copies selections to the system clipboard, which is
different from 1.3.#12600#12604
* macOS:cmd+arrow_upandcmd+arrow_downnow runjump_to_promptagain,
matching Terminal.app and Ghostty 1.2. In 1.3, these keys were hardcoded
to scroll to the top and bottom and couldn't be rebound. To keep the 1.3
behavior, setkeybind = cmd+arrow_up=scroll_to_topandkeybind = cmd+arrow_down=scroll_to_bottom.#12245
* GTK: The defaultctrl+shift+page_upandctrl+shift+page_downkeybinds
now move the current tab left and right (move_tab), matching Firefox,
GNOME Terminal, and VS Code.jump_to_promptmoved toctrl+shift+arrow_upandctrl+shift+arrow_down, so programs running in
the terminal no longer receive those keys. If a program you use needs
them, unbind them withkeybind = ctrl+shift+arrow_up=unbindandkeybind = ctrl+shift+arrow_down=unbind.#4998#12458

### Deprecations

The list below contains deprecations that remain compatible today through
a compatibility layer, but may break in a future release if they are
ignored:

* scrollback-limithas been renamed toscrollback-limit-bytes, to make
room for the newscrollback-limit-lines.#13473
* copy-on-select = trueis replaced withcopy-on-select = primaryon
Linux and FreeBSD, orcopy-on-select = clipboardon macOS.copy-on-select = falseis replaced withcopy-on-select = none.#12600#12604

There is no set timeline to remove these deprecations, but we recommend
adapting to the new configurations sooner rather than later to avoid
any possible disruptions in the future.

## Full Changelog

* Scrollback history is now transparently compressed while the terminal
is idle, reducing the physical memory used by compressed scrollback by
70% to 90% for typical text. Compression is available on macOS and 64-bit
Linux and can be disabled with the newscrollback-compressionconfiguration. Because of this, the default scrollback limit has been
raised from 10 MB to 50 MB, which on average still uses less memory than
a full scrollback did previously.#13264
* A new configurationscrollback-limit-lineslimits scrollback by number
of lines instead of bytes. The existingscrollback-limitconfiguration
has been renamed toscrollback-limit-bytes(the old name continues to
work). If both are set, the first limit reached applies, and both acceptunlimited.#13473
* copy-on-selectnow acceptsnone,primary,clipboard, andbothand no longer affects middle-click paste (seemiddle-click-action).clipboardnow copies only to the system clipboard, so usebothfor the
previous behavior. The default on macOS is nownone. See thebreaking changesfor migration details.#12600
* A new configurationmiddle-click-actionconfigures the behavior of
middle-clicking:primary-paste(default) pastes from the selection
clipboard,clipboard-pastepastes from the system clipboard, andignoredoes nothing.#12478
* A new binding actionmove_tab_to_new_windowmoves the current tab into
a new window of its own. It is also available in the command palette.#2630
* A new CLI command+explain-configprints the documentation for a
configuration option or binding action, e.g.ghostty +explain-config font-size.#11546
* The+explain-configand+show-configCLI commands now page their
output through$GHOSTTY_PAGERor$PAGER(falling back toless) when
run interactively. Paging can be disabled with--no-pageror by setting
the pager to an empty value.#11940
* A new configurationdrag-handlecontrols when the split drag handles
are shown:auto(default),always, ornever.#13706#13709
* Scrollback search now wraps around when navigating past the first or
last match.#11449
* A new configurationlink-osc8(defaulttrue) can be set tofalseto
disable OSC 8 hyperlinks entirely. Disabled OSC 8 hyperlinks are not
highlighted, previewed, copied, or opened.#13634
* Processes running in Ghostty now receive aGHOSTTY_SURFACE_IDenvironment variable that uniquely identifies the terminal they are
running in.#12027
* The right-click context menu now has a "Close Split" item.#11173#11174
* Upgrade to Unicode 18.#14293
* I/O throughput is 25% to 55% higher on macOS by reading from the pty
concurrently with parsing previously read output.#13209
* VT processing is significantly faster across the board. Plain text is up
to ~6x faster, real-world output (measured against a large asciinema
dataset) is ~24% faster, grapheme-heavy output is ~3x faster, and DEC
special graphics (line drawing), repeated characters (REP),
hyperlink-heavy output, and scroll regions are all faster.#13220#13226#13231#13294#13625#13826#14356
* Large OSC sequences, such as OSC 52 clipboard writes, are parsed ~30x
faster and small OSC sequences, such as title changes, ~6x faster.#14011#13565
* Resizing with reflow is ~6x faster with large scrollback and 3x to 5x
faster with scrollback heavy in wide characters such as CJK or emoji.#13537#13827
* Terminals use significantly less memory. A new terminal now uses ~16 KiB
of physical memory for its screen instead of 128 KiB on macOS, every
terminal page uses 30% less memory, and memory freed from scrollback
(such as by clearing it) is now returned to the operating system.#13240#13245#14130#14137#14138
* Kitty graphics are faster. Large image transfers are parsed in bulk using
SIMD, zlib-compressed images decompress ~17% faster, pixel format
conversion avoids an extra copy, and the per-frame cost of drawing images
is much lower, especially with Unicode placeholder images on screen or
long scrollback.#13270#13281#13987#14422#14780#14789
* Formatting terminal contents is 1.5x to 8x faster, which speeds up
clipboard copy (plain, HTML, and VT),write_screen_fileand related
actions, and scrollback search.#13587
* The renderer holds the terminal lock 2.7x to 11x less time per frame,
and glyph and font lookups are faster.#13227#14300#14301#14420#14406#13258
* command-palette-entry = clearremoves all command palette entries,
including the default entries.#12682
* window-padding-balancehas a new valueequalthat balances padding
equally on all four sides without capping the top padding.#11491
* themenow expands~to the home directory in theme file paths,
including in separate light and dark themes.#13840
* +list-themesnow supportsgandGto jump to the first and
last theme, andctrl+dandctrl+uto page down and up.#13681#14607
* The terminal inspector can now copy terminal I/O events or export them
to a file.#13519
* Bundled themes updated torelease-20261019-151001-86a776d.
This adds 356 new themes and renames or removes none. The colors of 10
existing themes changed upstream: Adwaita, Adwaita Dark, Atom One Light,
Catppuccin Frappe, Catppuccin Latte, Catppuccin Macchiato, Catppuccin
Mocha, Cursor Dark, Dark Modern, and Electron Highlighter.
* Fix configuration parsing silently ignoring all settings after a comment
or blank line that happened to end at an internal buffer boundary. This
typically only affected long configuration files.#13638
* Fix a performance degradation where, after a long uptime, the renderer
rebuilt its full terminal state on every frame.#13585
* Fix the automatically created configuration file being empty instead of
containing the configuration template.#13774
* +edit-configworks when$EDITORor$VISUALcontains arguments,
such aszed --new.#11897
* adjust-cursor-heightworks again.#13225
* Mouse selection improvements: dragging after actrl/cmdtriple-click
output selection now extends the selection by command output, autoscroll
stops when the screen switches (e.g. to the alternate screen), a force
touch on macOS selects the word at the press location without starting a
drag, and releasing a drag no longer activates a link or prompt click.#12830
* Double-click word selection no longer continues across hard line breaks,
and double-clicking either half of a wide character (such as CJK) selects
the whole word.#14354#14391
* Wide characters at the edges of a selection are now consistently rendered
as selected and included when copying, including when the wide character
wraps onto a new internal page.#14632#14651
* Triple-click line selection no longer pulls in neighboring prompt text
when clicking blank cells between OSC 133 prompt boundaries.#14553
* Link detection and double-click selection no longer merge prompt text
with the command text next to it when shell integration is active.#12435
* File paths opened withcmd/ctrl-click no longer include trailing
spaces, which broke opening paths printed by some TUIs.#13505
* Mouse releases are now reported to the program that received the mouse
press when clicking at a shell prompt with click-to-move enabled. This
fixes double-click selection in programs like fzf'sctrl+rhistory
search.#14710
* Shell redraws after a resize are no longer processed at the old terminal
size. This fixes one cause of duplicated or misplaced prompts after
resizing.#14706
* Scrolling, such as clicking in the scrollbar, now works with very large
scrollback (millions of lines).#13048
* Customcommand-palette-entryactions with string parameters, such asset_tab_title, no longer have their parameters escaped when run from
the command palette.#13609
* HTML clipboard copies no longer include a superfluous trailing newline.#13543
* Copying as VT (copy_to_clipboard:vt) and VT screen files now preserve
OSC 8 hyperlinks, empty gaps between text, and cells that only have
a background color, such as colored status bars. VT screen files also
keep trailing blank rows.#14711#14725#14766
* The mouse pointer now restores the shape set by the running program
(OSC 22) after releasing modifier keys instead of resetting to the
default.#14128
* Custom shaders no longer receive swapped selection foreground and
background color uniforms.#14460
* Ghostty no longer floods the logs with "adjusting page capacity"
messages during output with many styles, graphemes, or hyperlinks.#14631
* Fix stale wrap and prompt state on rows reused after scrolling or
erasing, which could cause incorrect copy, search, selection, and reflow
results.#14010
* Fix stale rendering of the previous row after erasing or deleting a
wrapped wide character.#14054
* Fix a freeze when reloading the configuration while a program is flooding
the terminal with queries, such as color queries.#14833
* +list-themesno longer crashes on some keys when the search
matches no themes, and the keypad down key now moves one row instead of
21.#14612#14605
* Fix crashes in scrollback search after clearing the scrollback, resizing,
or erasing history.#11957#13274#13282
* Fix crashes and viewport corruption when resizing with scrolled-back
history or with the cursor near the bottom of the screen.#12300#12907#12935
* Fix a use-after-free crash when clicking or selecting text during heavy
output.#12463
* Fix a possible crash when reflowing hyperlinks during a resize.#13524
* Fix possible crashes or memory corruption when scrolling or erasing rows
across a page boundary that needed more capacity.#13394#13397
* Fix possible crashes and memory corruption found via fuzzing when
printing causes a page to grow, or after clearing the screen into
scrollback.#11261#13997
* Fix many latent crashes and undefined behavior in selection, pins,
search, title and working directory updates, and resize error handling.#12894#13275#13278#13367
* Fix a possible crash or corrupted input when many pty writes are queued,
such as during large pastes.#13659
* Fix an out-of-bounds access when IME preedit text with wide characters
is composed between existing wide characters, such as with Korean input.#12479
* Fix a crash when pressing or releasing mouse button 11.#14759
* Fix thewrite_screen_file,write_scrollback_file, andwrite_selection_fileactions leaking two file descriptors on each use,
which could eventually prevent opening new terminals.#13644
* Fix memory and file descriptor leaks in terminal I/O, including for writes
in read-only mode and files read via theinputconfiguration.#13574#13579#13931

### Terminal Capabilities

* vt: Kitty graphics animation is now fully supported: frame transmission,
composition, animation control, and rendering.#5255#13943
* vt: Kitty graphics relative placements (P=,Q=,H=,V=) are now
supported, allowing images to be positioned relative to other images.#13939
* vt: Support the Kitty graphics transient image usage hint. Transient
images are evicted first when image storage is full.#13389
* vt: The Kitty clipboard protocol (OSC 5522) is now implemented on macOS
and GTK, including paste events (mode 5522). Reads and writes followclipboard-readandclipboard-write, and a newclipboard-write-limit-bytesconfiguration limits the size of a single
write.#10549#13962#13993#13995#13998#14002#14061
* vt: Support visibility reports (mode 2033 andCSI ? 998 n), which tell
programs when the terminal is not visible, such as in a background tab
or on another workspace, so they can stop rendering.#13494
* vt: Programs can resize the window with the xtermCSI 8 ; rows ; cols tsequence if the newvt-window-resize-allowedconfiguration is enabled
(default off). The request is ignored in splits, windows with multiple
tabs, the quick terminal, and fullscreen, maximized, or tiled windows.#1115#14375
* vt: Support OSC 133click_events=2, which reports prompt clicks with
row coordinates relative to the prompt.#10865#12953
* vt: Support soft terminal reset (DECSTR,CSI ! p), which resets
modes, margins, and text attributes without clearing the screen.#14538
* vt: Support backarrow key mode (DECBKM, mode 67), which lets programs
choose whether backspace sendsDEL(0x7f, the default) orBS(0x08).#12226
* vt: Support the DECRQCRA and XTCHECKSUM screen checksum reports, which
are mostly used by terminal test suites. Because a program can use these
to read the screen contents, they are disabled unless the newvt-xt-checksum-reportconfiguration is enabled. The newvt-xt-checksum-extensionconfiguration controls how the checksum is
calculated.#14483
* vt: Respond toCSI 19 t(report screen size in characters) and to
DECXCPR (CSI ? 6 n) extended cursor position requests.#14633#14673
* vt: DECRQM now answers ANSI mode queries (CSI Ps $ p), reports DECECM
and other unimplemented ANSI modes as permanently reset like xterm, and
no longer truncates mode numbers above 32767 in its reply.#12505#14236#14237#14672
* vt: Ghostty terminfo now advertises overline support (Smol/Rmol),
which lets tmux pass overlines through. DECRQSS SGR replies now include
overline and curly, double, dotted, and dashed underline styles.#13649#13653#13470
* vt: The terminfoSecapability now resets the cursor to the configuredcursor-styleinstead of a steady block. This fixes programs like Neovim
leaving a block cursor behind on exit.#12482
* vt: OSC payloads are now limited to 8 MiB, Kitty graphics payloads to
65 MiB, and each cell to 64 combining codepoints, so terminal output
can't easily exhaust memory. This also fixes a memory leak on invalid
Kitty graphics data.#12349#13633
* vt: Experimental support for theGlyph Protocol(APC25a1), which lets programs register custom glyphs. Ghostty parses
and answers requests but doesn't render registered glyphs yet.#12352#12930#12937
* vt: Parse the new program status protocol (OSC 7501), which lets programs
report whether they are idle, working, done, blocked, or failed. This is
the first terminal specification pioneered by the Ghostty project.
libghostty can parse it all, but the Ghostty GUI ignores it for now.#14560
* vt: Parse (but do not implement) the Kitty desktop notification protocol
(OSC 99).#10467
* vt: Parse (but do not implement) the Kitty drag and drop protocol
(OSC 72).#13029
* vt: More tmux control mode fixes, including crashes that runningtmux -CCcould trigger. tmux control mode is still not hooked up to
the GUI.#11395#11935#14262#14680
* vt: Clearing the screen at a prompt (e.g.ctrl+lin bash or zsh) now
moves prior output into scrollback even when the prompt is not on the
last row. Previously, the output was erased.#14660#14668
* vt: Kitty graphics: transmitting an image with an existing ID now
replaces the image and removes its old placements, as the spec requires.
Interrupted or failed retransmissions no longer leave stale images on
screen.#6711#13723#13893
* vt: Kitty graphics: images now move with the text when a program scrolls
withCSI S,CSI T, or scroll margins, and are clipped to the scroll
region.#4323#13935
* vt: Kitty graphics: automatically assigned image IDs no longer collide
with IDs chosen by the program.#2197#13934
* vt: Kitty graphics: delete commands now match the spec and Kitty. Point
deletes (d=p,d=c) only remove placements at that cell,d=aonly
removes placements on the visible screen, range deletes accept empty
ranges, and deleting a missing placement no longer frees the image.#13652#13895#13898#13932
* vt: Kitty graphics: command validation and responses now match Kitty.
This fixes missing responses for invalid image data that could hang
clients, false positive query replies, lost IDs in chunked transfer
replies, file transfers with an exactSsize, and loads interrupted by
a non-chunk transmission.#13889#13892#13896#13897#13933#14811
* vt: Kitty graphics: cropped source rectangles are no longer stretched,
andX/Yoffsets are kept within the first cell.#13890#13891
* vt: Kitty graphics: the cursor moves after tall images like Kitty does,
so consecutive images no longer overlap.#13887
* vt: Full reset (RIS) no longer resetsimage-storage-limitto the
default.#13951
* vt: OSC and APC sequences (such as Kitty graphics commands) canceled by
CAN or SUB, or aborted by another control character, are now discarded
instead of executed, matching xterm.#14453#14812
* vt: With modifyOtherKeys level 2, control keys, keypad keys, andalt+escapenow encode like xterm. F13 to F25, Help, and Menu now send
xterm's function key sequences in all legacy encoding modes.#14144#14145
* vt: Legacy alt-as-escape encoding now sends the full UTF-8 sequence for
non-ASCII keys.#14146
* vt: Kitty keyboard protocol release events no longer repeat the typed
text for dead keys or level 5 keys on GTK, which caused duplicated
characters in programs like Neovim.#13861
* vt:ctrl+alt+shift+backspacenow sendsESC BSin legacy key encoding,
matching xterm.#14508
* vt: UTF-8 mouse mode (1005) now encodes the button correctly, fixing
invalid reports for the back and forward mouse buttons.#14532
* vt: Foreground, background, and cursor colors reset with OSC 110, 111,
or 112 now follow later configuration changes, such as a light/dark
theme switch.#13650
* vt: Full reset (RIS) now restores palette colors changed with OSC 4.#14480
* vt: An empty OSC 22 now resets the mouse pointer shape to the default.#14495
* vt: Long desktop notifications (OSC 9 and OSC 777) with multibyte UTF-8
text are no longer dropped or shown as invalid UTF-8 when truncated.#13795#13811
* vt: DCS strings now carry UTF-8 data. Previously, some UTF-8 bytes were
dropped, ended the string early, or started a new control sequence.#14016
* vt: C0 controls0x10to0x1Fare now executed instead of printed
as text, and UTF-8 encoded C1 controls are ignored, matching xterm.#14022#14023
* vt: Erasing a full line (CSI 2 K) now clears its soft-wrap state, so
erased rows no longer join together when the window is resized.#13637
* vt: The cursor and saved cursor keep the correct position when a resize
reflows text, fixing an extra line wrap or overwritten text after
resizing.#12598#14458#14478
* vt: Variation selectors (VS15/VS16) now apply to the preceding codepoint,
fixing the rendering of some ZWJ emoji such as the pirate flag.#12596
* vt: Combining marks printed after a character in the last column now
attach to that character.#12581
* vt: Characters above U+00FF, such as emoji, now print as-is instead of as
a blank while a non-UTF-8 character set such as DEC line drawing is
active.#14554
* vt: Single shifts (SS2/SS3) now apply only to the next printed character.#14576
* vt: Tab clear (TBC) fixes:CSI 0 gno longer sets a tab stop where
there wasn't one, andCSI gwith no parameter clears the tab stop at
the cursor.#13900#14644
* vt: Printing with autowrap (DECAWM) disabled clears the pending wrap, so
re-enabling autowrap doesn't cause a spurious line wrap.#14652
* vt: With reverse wrap enabled, moving left after restoring a cursor with
a pending wrap no longer jumps the cursor.#14390
* vt: Cursor movement respects margins and origin mode: CUB and backspace
stop at the left margin, and CHA, HPA, VPA, HPR, and VPR no longer apply
the margin offset twice in origin mode.#14761#14762
* vt: Fix a crash when VS15 narrows a wide character under the cursor.#13631
* vt: Fix a crash or memory corruption after narrowing the terminal cuts a
wide character in half on the alternate screen or with wraparound
disabled.#14509
* vt: Fix a crash when a grapheme cluster widens in the last column and
wraps inside or below a scroll region with grapheme clustering (mode
2027) enabled.#14552
* vt: Fix a slow memory and performance leak in graphics-heavy sessions
where evicted Kitty images left their placements' tracked positions
behind.#13656
* vt: Fix a memory leak when an OSC color sequence contains more than two
requests.#13239

### Shell Integration

* A newghostty +sshCLI action wrapssshand sets up Ghostty on remote
hosts: it forwards Ghostty's environment and installs Ghostty's terminfo
on the first connection to each host, caching successful installs. It can
be used directly (ghostty +ssh user@example.com) or as an alias
(alias ssh='ghostty +ssh --') without shell integration. Thessh-envandssh-terminfoshell integration features now use it for every
shell.#12582
* ssh-terminfonow always installs Ghostty's bundled terminfo on remote
hosts instead of keeping an existing, possibly outdated,xterm-ghosttyentry, and reinstalls it when a newer Ghostty changes its terminfo.#13844
* ghostty +ssh-cachehas been reworked with positional destinations, a
new--pruneoption, consistent output and exit codes, and error
messages that name the cache file. See thebreaking changesabove.#12814#13533
* ssh-terminfonow tells apart the same host on different ports, so
terminfo is installed on each of them.ghostty +ssh-cacheacceptshost:portdestinations.#14472
* ssh-envno longer overridesSetEnventries in your~/.ssh/config.#11518#14854
* bash: Failed commands now report their real exit status on Bash 4.4+,
so command finished notifications no longer report every command as
successful.#14247#14250
* nu: Tab completion forsshandsudonow works with external
completers such as carapace.#13310
* bash: The bundled bash-preexec, used only for Bash versions older than
4.4 such as macOS's/bin/bash, has been updated to 0.7.0.#14120
* zsh: Fix a stray{in the prompt and broken prompt marking whenPS1orPS2ends with a bare%.#11832
* bash: Fix "command not found" errors in subshells that inheritPROMPT_COMMAND.#11690
* bash: Fix a syntax error when an existingPROMPT_COMMANDends with a
newline.#11621
* bash: Fix extra blank lines at the prompt when using ble.sh.#11644
* bash: Fix the shell integration hook being added twice when it is
sourced again with an arrayPROMPT_COMMAND.#14266

### macOS

* macOS: Support macOS 27. This fixes the layout and background color of
titlebar tabs, a thin border around the app icon, hidden titlebars
covering the top lines of the terminal with Reduce Transparency enabled,
and the Shortcuts "New Window" action opening two windows.#13001#13390#14107#14411#12999#13069
* macOS: When a terminal's process exits, a native bar now appears at the
bottom of the terminal instead of text being written into the terminal.
Commands that fail or exit faster thanabnormal-command-exit-runtimeare highlighted in red.#7649#12251
* macOS: Quitting, or closing a window, when multiple windows or tabs have
running processes now offers "Review Windows...", which steps through
each one so you can decide what to close.#12742#14062
* macOS: The command palette now highlights matching text, matches
initials, searches action descriptions, and ranks results by where they
matched.#12264#13610#13624
* macOS: The search bar now remembers the last search and shares it with
other apps through the system find pasteboard, like Safari and
Terminal.app.#12516#12712
* macOS: Screen readers such as VoiceOver are now notified when the
selection changes instead of reading a stale selection.#12902
* macOS: The AppleScriptterminalclass and the Shortcuts terminal entity
now exposepid(of the foreground process) andtty.#11592#10756#11922
* macOS: AppleScript tabs and terminals have a new read-writename overrideproperty to set or clear a custom title.#12048#14733
* macOS: Middle-clicking a tab closes it withmacos-titlebar-style = tabs.#11962#11963
* macOS: The version in the About window now links to the release notes
for that version.#11964
* macOS: Updates that are downloaded and installed automatically no longer
prompt you to restart. Checking for updates manually still offers to
restart.#13623
* macOS:toggle_background_opacitynow applies to every tab in the
window, and new windows inherit the current state.#11583
* macOS:cmd+arrow_upandcmd+arrow_downnow run their configured
keybinds, which default tojump_to_prompt. Ghostty 1.3 always scrolled
to the top or bottom of the scrollback instead, ignoring the
configuration. To scroll to the top or bottom, usecmd+homeandcmd+end.#12245
* macOS: In the configuration errors window, Return reloads the
configuration and Escape ignores the errors.#12601
* macOS: Ghostty launches about 15% faster to a visible window and draws
its first frame about 27% sooner.#13722
* macOS: Terminals that aren't visible, such as background tabs, now
release their GPU resources and rebuild them when shown again. With 20
background tabs, GPU memory drops from about 385 MiB to 18 MiB. Metal
buffers also no longer over-allocate when they grow.#14017#13490
* macOS: Lower idle CPU and energy use. The display link now pauses when
there is nothing to draw, and unfocused terminals that are animating
draw at most once per display refresh instead of once per write.#14035#14068
* macOS: Update Sparkle to 2.9.6, which fixes several security advisories
in Sparkle, including CVE-2026-47121 and CVE-2026-47122.#14072#14082
* macOS: Global keybinds no longer stop working after macOS disables
Ghostty's event tap.#12294#12714
* macOS: Fix IME composition issues. Korean text being composed is now
committed instead of lost when pressing an arrow key, and control-key
IME shortcuts such as Japanese input'sctrl+jno longer send control
characters to the terminal.#11461#12447#12518#12547
* macOS: Text from input methods, dictation, and the emoji picker is now
sent as typed input instead of pasted text. Programs no longer treat
dictation as a paste, and switching input sources mid-composition sends
the pending text as keys, matching Terminal.app.#13195#13222#13817
* macOS: Unicode Hex Input can now enter characters outside the Basic
Multilingual Plane, such as emoji, typed as surrogate pairs.#13733#13737
* macOS:font-thickennow also applies to IME preedit text.#14230
* macOS:option+backspaceand other modified Backspace keys now report
their modifiers with the Kitty keyboard protocol instead of sending a
bare DEL.#13871
* macOS: Pasting and dropping text now prefer plain text over URLs, so a
path copied from apps like Transmit pastes as a path instead of ansftp://URL.#13152#13170#13212
* macOS: The search bar keeps focus when you click in it or on the
next/previous buttons, and the terminal's focus state is now correct
while search is open.#11872#11978
* macOS: The Find Next and Find Previous menu items and thenavigate_searchandend_searchkeybinds now work correctly,
including while the search field is focused.#12070#12492
* macOS: Pressing Enter in the search bar no longer blocks confirming an
IME candidate.#12781
* macOS: Clicking a command palette entry with the mouse now runs it
instead of closing the palette.#11665
* macOS: The command palette now gets focus and paste when opened from the
inline tab title editor.#12524
* macOS: Holdingcmd+tto create many tabs now leaves the newest tab
focused.#13725#13985
* macOS: Fix an empty "ghost" tab or window that could appear when a tab
was closed right after it was opened.#12119
* macOS: Titlebar tabs no longer disappear after creating a tab from
"Show All Tabs".#12949#13017
* macOS: Double-clicking the window title now zooms the window withmacos-titlebar-style = tabs.#12219
* macOS: Moving a tab withmacos-titlebar-style = tabson macOS 26 no
longer briefly shows the neighboring tab.#14847
* macOS: The inline tab title editor stays in place while the window is
resized.#12220
* macOS: Fix tabs flashing when switching tabs after a program changed the
background color with OSC 11, and the window chrome keeping the old
color after a light/dark theme switch.#12825#12828#12822
* macOS: Themacos-glass-regularandmacos-glass-clearoptions forbackground-blurnow layer the glass over the background color, and
focused windows are no longer less transparent than unfocused ones.#13914#13928
* macOS: The native titlebar no longer cuts off the end of the title when
using a customwindow-title-font-family.#14135#14217
* macOS: Fix terminals rendering at a stale size under heavy system load or
during rapid resizes from window managers.#12143
* macOS: Splits dragged into another tab or window now render immediately,
and the source window keeps keyboard focus.#12343#12338
* macOS: The split zoom indicator no longer stays visible after the other
splits of a zoomed split are closed, such as with AppleScript.#14703
* macOS: The split divider now uses the standard row and column resize
pointers.#13433
* macOS:window-save-state = nevernow also stops macOS from taking
window restoration snapshots, which could stall focus changes between
windows.#14506
* macOS: Window state saved by Ghostty 1.2 or later is now migrated, so
windows and tabs are restored after updating Ghostty.#12461
* macOS: Tabs created while the screen is locked now initialize correctly.#13639
* macOS: Quitting now asks for confirmation when windows with running
processes are minimized or the quick terminal is hidden.#13686
* macOS: OSC 52 clipboard read confirmations no longer steal focus. If the
terminal is unfocused, Ghostty rings the bell and shows the prompt when
you return to it.#13744
* macOS: Splits in the quick terminal now also setGHOSTTY_QUICK_TERMINAL=1.#12895#12896
* macOS: The quick terminal no longer reopens at a stale size after a
display is reconnected at a different resolution.#13250
* macOS: The "New Ghostty Tab Here" and "New Ghostty Window Here" services
now open the correct directory when given a plain-text path.#12727#12731
* macOS: Working directories passed from Services, Shortcuts, and
AppleScript are now normalized, fixing Nushell and zsh%1~prompts.#12614#14051
* macOS:ghostty -eno longer opens the command's file arguments as
extra terminals, e.g.ghostty -e vim file.txt.#13748
* macOS: Opening a.commandfile from Finder no longer corrupts
non-ASCII characters in its path.#13862
* macOS: The Shortcuts terminal entity now reports the correct kind,
title, working directory, and screenshot for new terminals.#13007
* macOS: The Shortcuts "New Terminal" action now works with commands that
have arguments and with a command field that was cleared.#12391#12392
* macOS: AppleScriptsend keynow works for character keys, not only
special keys likeenter, and respectsmacos-option-as-alt.#13205
* macOS: Update pill fixes: update errors are now shown, "Install and
Relaunch" no longer asks for confirmation, and the cancel option is
hidden once an update can no longer be canceled.#13540#13562#13612
* macOS: The default app icon follows the system icon style again after
changing it in System Settings, and custom icons now apply to the app in
Finder.#12180#12344
* macOS: The dock icon bell badge now appears when notification permission
was granted earlier without badge permission.#12133
* macOS: The Copy menu item is disabled when nothing is selected.#12521
* macOS: Menu items now show the correct shortcut for keybinds on physical
keys (e.g.super+backquote), uppercase letters, forward delete, and
thescroll_to_selectionandsearch_selectionactions.#13888#12039#12011#12281
* macOS: The secure input indicator's popover arrow now points at the
icon.#12249
* macOS: Fix a rare permanent freeze after waking from sleep or changing
displays. macOS did not mark the app as "Not Responding", so it could
only be killed.#14691
* macOS: Fix a crash when closing a tab, most easily triggered withundo-timeout = 0.#13359#13364
* macOS: Fix a crash when opening a new tab from a native fullscreen
window.#13636
* macOS: Fix a crash caused by a data race when reading cached terminal
contents.#13646
* macOS: Fix a crash when OSC 52 clipboard confirmation prompts overlap.#13648
* macOS: Fix crashes when CoreText returns null, such as for fonts without
a display name or under severe memory pressure.#13642#13679
* macOS: Fix closed windows leaking with transparent titlebars (the
default), which made Ghostty and WindowServer use more CPU and memory
over time.#13601
* macOS: Fix a memory leak each time Ghostty reads terminal text, such as
for copy, Quick Look, or accessibility.#12020#12025
* macOS: Fix an IOSurface memory leak when scripts rapidly create and close
terminals.#13640
* macOS: Fix a Mach port leak, and a gradual slowdown, while global
keybinds wait for Accessibility permission.#13590

### GTK (Linux, FreeBSD)

* GTK: Splits can now be rearranged with drag and drop, matching macOS.
Drag a split by its handle and drop it onto another split, including
splits in other tabs and windows.#10224#10423
* GTK: Ghostty now renders at the true fractional scale (e.g. 125% or
150%), so text and box-drawing characters are sharp instead of blurry
under fractional scaling.#1938#14269
* GTK: The renderer no longer usesGtkGLArea. Ghostty now renders with
EGL entirely on the render thread and hands finished frames to GTK as
DMABUFs, so the main thread no longer does any OpenGL work.#14052#14636
* GTK: Windows can now be renamed using the menu, command palette, or the
newprompt_window_titleandset_window_titlebinding actions.#10469#10999
* GTK: A new+new-tabCLI command opens a new tab in a running Ghostty
instance. When run from inside Ghostty, the tab opens in the same
window. It accepts the same-e,--working-directory, and--titleflags as+new-window.#11762
* GTK: A new+toggle-quick-terminalCLI command toggles the quick
terminal of a running Ghostty instance, useful for binding in window
managers without global shortcut support.#12661
* GTK: Global keybinds now use thevicinae-hotkey-v1Wayland protocol
when the compositor supports it (e.g. Hyprland 0.56+), falling back to
the XDG desktop portal otherwise. Ghostty shows a desktop notification if
a global keybind can't be registered.#13464
* GTK:quick-terminal-screenis now supported on Wayland. The default,main, places the quick terminal on the compositor's primary output
(or the first monitor if the compositor doesn't report one). Set it tomouseto let the compositor choose, which was the previous behavior.#11117
* GTK: On Wayland,background-blurnow uses the compositor-agnosticext-background-effect-v1protocol instead of KDE's blur protocol,
enabling blur on compositors such as Niri. The blur region also no longer
covers the window's client-side shadows.#10721#10720#10727
* GTK: On GTK 4.23.3 and newer,background-bluruses GTK's built-in
background blur, which covers the window more accurately.#13581#13586
* GTK: Theopen_configbinding action now acceptsnew_windowto
edit the configuration in$VISUALor$EDITORin a new Ghostty
window. The default,os_open, keeps the previous behavior.#11905
* GTK: A new configurationgtk-horizontal-tab-scroll(defaulttrue)
can be set tofalseto stop two-finger horizontal scrolling from
switching tabs, passing the scroll to the terminal application instead.#12659
* GTK: A new configurationgtk-tabs-invertedmoves the close button to
the start of each tab, in both the tab bar and the tab overview.#14657
* GTK: The default command palette entries are now translatable.#11641
* GTK: The embedded Noto emoji fonts were updated, so newer emoji and ZWJ
sequences such as the head-shaking faces render as one glyph instead of
overlapping neighboring cells.#14047
* GTK:ctrl+shift+page_upandctrl+shift+page_downnow move the current
tab left and right (move_tab), matching Firefox, GNOME Terminal, and
VS Code.jump_to_promptmoved toctrl+shift+arrow_upandctrl+shift+arrow_down.#4998#12458
* GTK: URLs now open through the XDG desktop portal, falling back toxdg-openif the portal is unavailable. Ghostty passes an activation
token so the opened application, such as your browser, can come to the
front on compositors that require one.#5991#11754#14785#14787
* GTK: Desktop notifications are now withdrawn when their terminal is
focused or closed, and repeated notifications with the same text
replace each other, matching macOS.#14108
* GTK: Tabs that aren't visible no longer render, saving CPU and GPU.
This matches macOS.#12760
* GTK: The Dolphin "Open Ghostty Here" action now opens a new window in
the running Ghostty instance instead of launching a separate one.#11614
* GTK: Fix Ghostty sometimes failing to launch with systemd 262, which
refused to start the service because Ghostty reported readiness before
it could handle reload signals.#14398#14399
* GTK: Fix deeply nested splits sometimes becoming invisible or losing
focus.#11193#12698
* GTK: Resizing splits, especially withresize_splitkeybinds, no
longer flickers.#13414
* GTK:resize_spliton nested splits no longer causes large jumps in
size.#12699
* GTK: Splits can no longer be resized smaller than one cell, by dragging
the divider or withresize_split.#14476
* GTK: High-resolution scroll wheels no longer scroll much faster than
standard scroll wheels.#12483
* GTK: Disable unwanted kinetic scrolling on trackpads with GTK versions
older than 4.20.1.#11793
* GTK: Middle clicks are once again sent to terminal applications using
mouse reporting whengtk-enable-primary-pasteis disabled in
GSettings.#12940#13108
* GTK: The quick terminal no longer breaks when toggled off manually
whilequick-terminal-autohideis enabled.#11679#12471
* GTK: Opening the right-click context menu no longer hides the quick
terminal whenquick-terminal-autohideis enabled.#12843
* GTK: The resize overlay no longer keeps reappearing when the scrollbar
is visible and no longer blocks mouse input while shown.#11970#11972
* GTK: The maximum window size is now based on the monitor the window is
currently on, not the monitor it was opened on.#13171
* GTK:+new-window -enow works whenshell-integrationis set to a
specific shell.+new-windowand+new-tabalso accept a new--shell-integrationflag.#12378#13741
* GTK: Keys remapped to modifiers with XKB (e.g. Delete remapped toISO_Level3_Shift) no longer also send the original key.#13967
* GTK: On Wayland, the IME candidate window now follows the cursor while
composing and no longer covers the line being edited.#14729
* GTK: Splits in a tab that was moved to another window now act on the
new window (e.g.toggle_fullscreen).#14474
* GTK: The mouse cursor keeps its text shape while selecting text.#14558
* GTK: The command palette now uses the terminal colors whenwindow-theme = ghostty.#14662
* GTK: Opening URLs no longer fails when the fallback opener (xdg-open)
produces large output.#12797
* GTK: Clicking a desktop notification no longer focuses the wrong
terminal when the one that sent it has since been closed.#12028
* GTK: A bell in the focused terminal no longer leaves the bell
indicator set.#13597
* GTK: Fix the window continuously redrawing in the background after an
indeterminate progress bar (OSC 9;4) was removed.#14704#14738
* GTK: Log missing or invalidgtk-xft-dpivalues once instead of
repeatedly.#14410#14085#14434
* GTK: Fix a crash when closing tabs or splits on GTK 4.20 (GNOME 49).#12426
* GTK: Fix a crash with global keybinds or on configuration reload when
no D-Bus connection is available.#13101
* GTK: Fix a possible crash when Fontconfig reports a font's language as a
plain string instead of a language set.#14853
* GTK: Fix a leak where every audio bell started a new GStreamer pipeline
and threads that were never cleaned up, slowly raising CPU usage.#13647#12815#13657
* Snap: Link the system FreeType, Fontconfig, HarfBuzz, libpng, and zlib
instead of bundled copies, fixing frequent crashes caused by two copies
of the same library in one process.#14392#14682
* Snap: The snap's own GIO modules and XDG data directories now take
priority over the host's.#12045
* Snap: Programs running inside Ghostty, such asclear, now find thexterm-ghosttyterminfo entry.#12662
* Flatpak: Commands started by Ghostty on the host are now terminated if
Ghostty crashes.#12427

### Localization

Ghostty 1.4 introduces full localization for the command palette and adds
support for4 new languages:

* Basque
* Belarusian
* Danish
* Serbian (Cyrillic and Latin scripts)

Localization is maintained by volunteer contributors. If you want to
help localize Ghostty in your language, please open a discussion on the
GitHub repo. Thank you to all the volunteers who contributed to Ghostty's
localization!

### Changes for Package Maintainers

* Ghostty now requires Zig 0.17 to build.#14518#14519
* GTK builds now requireGTK 4.18andlibadwaita 1.7, up from
GTK 4.14 and libadwaita 1.5. Builds against older headers fail at
compile time, and Ghostty exits at startup if older libraries are
loaded at runtime.#14330
* GTK builds now link the system EGL library (pkg-configegl, usually
provided by libglvnd or Mesa) for the new renderer. At runtime, Ghostty
uses GTK's EGL display when it can, and otherwise needs an EGL driver
that supports the surfaceless platform.#14052#14636
* A new-Dinstalled-exe-pathbuild option sets the absolute executable
path written into the desktop file, D-Bus services, and systemd user
service. Previously this path came from the install prefix. Without the
option, these files now nameghosttyalone, which systemd only finds in/usr/binor/usr/local/bin, so set it for any other prefix.#14805#14806
* When linking the system gtk4-layer-shell (-fsys=gtk4-layer-shell),
version 1.0.4 or newer is now required. Ghostty no longer disables the
quick terminal on older versions, which can crash on some compositors.#11559

## Libghostty

As with 1.3, libghostty isn't directly part of the Ghostty 1.4 release.
But a large part of the 1.4 development cycle went into libghostty, so
here's an update.

Over the past 6 months, the C API for libghostty-vt has grown from a
parser and a few encoders into a complete terminal emulator API, adopted
by dozens of free and commercial terminal emulators used by millions of
people. It's hard to quantify exactly, but the number of people using a
libghostty-based terminal is confidently several times the number of
people using the Ghostty GUI.

libghostty-vt now builds for macOS, Linux, Windows (MSVC and GNU), FreeBSD,
Android, iOS, and WebAssembly, and CI continuously verifies every one of
these targets. The goal is for libghostty-vt to be generally usable everywhere,
within reason, so if you want more target support, let us know!

It's also easier to integrate libghostty-vt into existing build systems.
There's CMake support, Nix packaging, an xcframework, and a source
tarball, in addition to the existing pkg-config file.libghostty-vt no
longer needs libc++, and it can build freestanding.

The API is still marked as a work in progress and broke compatibility
several times during this cycle, so expect more breaking changes before
a tagged release. TheAPI documentationand theZig, C, C++, Swift, and WebAssembly examples(now over 30) are kept up to date withmain.

We're going to do a final pass over the C API, break ABI one more time,
and then likely tag a libghostty 1.0 release very soon.

## Financial Update

Ghostty is anon-profit project, fiscally sponsored
byHack Club.
All of our finances arepublic on HCB,
so you can see exactly where every dollar goes.

During the 1.4 cycle, we paid$41,820to contributors under contract and
spent about$1,260on infrastructure such as website hosting.

I'm happy to share that we've now signed our first two12-month contracts,
which give contributors stable, long-term paid work on Ghostty and help
ensure the ongoing stability and sustainability of the project:

* @trag1cis Ghostty's head of operations.
He manages the community on GitHub and Discord, coordinates our
volunteer translators, and maintains various other important project
systems.
* @vanclueverworks on various Ghostty
subsystems. In this cycle, he led the upgrade to Zig 0.16, moved the
build off Zig's deprecated@cImport, updated the bundled Fontconfig,
and more. He's also the author ofz2d, the 2D graphics library Ghostty
uses to draw box-drawing characters and other sprite glyphs.

If you'd like to support Ghostty, please visit oursponsorship page.

## Roadmap

The primary focus of the roadmap continues to be libghostty functionality,
stability, and portability. During the last release cycle, I said I aimed to
tag a libghostty release. We haven't done that yet, but I'm confident we will
do so before Ghostty 1.5.

libghostty is a project that continues to be the tide that lifts all boats.
libghostty improvements tie directly to Ghostty GUI improvements as well as
dozens of other large projects in the ecosystem. As more large projects adopt
libghostty, libghostty tends to get more testing and attention, and this
creates a cycle that yields the most gain for terminal emulators everywhere.

macOS and GTK builds of Ghostty have talented, capable maintainer teams that
are continuing to improve them, so they're not neglected by any means!
As a project, we've decided to drop any roadmap for Windows support in the
Ghostty GUI. libghostty fully supports Windows (and we test it in CI), and the
official stance now is that downstream projects should use that.

Our release cycle remains 6 months. This release was delayed by one month,
but Ghostty 1.5 is planned for March 2027. libghostty will have a separate
release cycle.

Edit on GitHub 
* Security
* Highlights
* macOS 27 Support
* Kitty Graphics Animation and Relative Placements
* Scrollback Compression and Lower Memory Usage
* Performance Improvements
* New OpenGL Renderer (Linux, FreeBSD)
* Kitty Clipboard Protocol
* Split Drag and Drop (GTK)
* Terminal Emulation Accuracy
* SSH Integration with ghostty +ssh
* System Requirements
* Breaking Changes
* Deprecations
* Full Changelog
* Terminal Capabilities
* Shell Integration
* macOS
* GTK (Linux, FreeBSD)
* Localization
* Changes for Package Maintainers
* Libghostty
* Financial Update
* Roadmap