---
title: "Let's compile Quake like it's 1997!"
url: https://fabiensanglard.net/compile_like_1997/
date: 2026-05-29
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-05-30T06:02:31.402585
---

# Let's compile Quake like it's 1997!

# Let's compile Quake like it's 1997!

## Historical context
- Early Quake binaries (quake.exe, vquake.exe) were cross‑compiled on HP 712‑60/NeXT and a DEC Alpha server.
- In June 1996 id Software moved development to Intergraph hardware running Windows NT after the initial release.
- Subsequent Windows binaries (winquake.exe, glquake.exe, QuakeWorld tools) were built with Visual C++ 4.x.

## Required environments
- Authentic options: Intergraph RealizM Dual P6‑200 MHz workstation, dual‑Pentium Pro machine, a typical late‑90s “Quake PC”, or a VirtualBox VM.
- The author tested the procedure on both a real Quake PC and a VM running Windows 98 SE or Windows NT 4.0.

## Installing Windows NT 4
- Use the bootable CD; installation takes about 30 minutes.
- NT 4 shows CPU count and RAM at startup; it does not auto‑detect a second CPU—re‑install is needed for SMP support.
- UI theme matches Windows 9x; earlier NT 3 resembled Windows 3.1.

## Installing Visual C++ 6
- Original Quake win32 code was written for Visual C++ 4.x; by 1999 the project migrated to VC++ 6.
- The IDE can be obtained from Internet Archive or winworldpc.com; it includes the “Visual Studio” suite.
- Run at 640×480 or 800×600 for proper layout; high resolutions look mis‑aligned.

## Obtaining the source code
- Do **not** download from GitHub or FTP; the workspace file (.dsw) will break.
- Download `q1source.zip` from the Quake Official Archive (maintained by Jason Brownless).
- Transfer files via VM drag‑and‑drop or a simple FTP server; extract with WinRAR 2.50.

## Building the project
- Open `WinQuake.dsw` in VC++ 6 (workspace → projects).
- First “Rebuild All” fails because hand‑optimized `.s` files need the `ml.exe` assembler.
- Install Visual Studio 6 Service Pack 5 (requires MDAC 2.5; run `mdac_typ.exe` from the extracted folder, then `setupsp5.exe`).
- Install VC++ 6 Processor Pack to obtain the assembler.
- After adding the processor pack, run “Rebuild All” again; the build succeeds.
- Copy `PmProXX.dll`, `WdirXX.dll`, and `id1` to the game directory; the executable runs, including QuakeWorld with QSpy.

## Remarks on the IDE
- VC++ 6 offered “Go to definition”, breakpoints, stack traces, and variable inspection, though no IntelliSense.
- The author notes the experience feels like navigating a 1990s development environment.

## References
- Conversation with John Carmack.  
- Quake Official Archive.