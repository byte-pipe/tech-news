---
title: 'DXGI debugging: Microsoft put me on a list | PJB blog'
url: https://slugcat.systems/post/25-09-21-dxgi-debugging-microsoft-put-me-on-a-list/
site_name: hackernews_api
fetched_at: '2025-09-22T13:21:27.797698'
original_url: https://slugcat.systems/post/25-09-21-dxgi-debugging-microsoft-put-me-on-a-list/
author: todsacerdoti
date: '2025-09-21'
published_date: '2025-09-21T14:25:00+00:00'
description: 'DXGI debugging: Microsoft put me on a list'
tags:
- hackernews
- trending
---

# DXGI debugging: Microsoft put me on a list


				Sunday September 21, 2025


Why does Space Station 14 crash with ANGLE on ARM64? 6 hours later…

So. I’ve been continuing work on getting ARM64 builds out for Space Station 14. The thing I was working on yesterday were launcher builds, specifically asingledownload that supports both ARM64 and x64. I’d already gotten the game client itself running natively on ARM64, and it worked perfectly fine in my dev environment. I wrote all the new launcher code, am pretty sure I got it right. Zip it up, test it on ARM64, aaand…

The game client crashes on Windows ARM64. Both in my VM and on Julian’s real Snapdragon X laptop.

## Debugging: logs

The client logs are empty. They suspiciously cut out right after SDL is initialized.

Of course it isn’t that easy.

## Debugging: pulling WinDbg out of the shed

Given that there’s no logs, this has to be a native crash. That means it’s WinDbg time.

So at first I decided to startSpace Station 14 Launcher.exedirectly through WinDbg. This is annoying because I have to go into child processes (with.childdbg 1) twice, and for some reason there’s a lot of waiting, but it does work…

The game crashes inUSER32!GetDCon anillegal instruction, somewhere after SDL doessomething. I barely glanced at the disassembly but it made no sense to me, so I just assumed there’s some UB happening and didn’t think much of it. After all,why would the implementation ofGetDC()have broken assembly?

(3148.35e4): Illegal instruction - code c000001d (first chance)

(3148.35e4): Unknown exception - code c000041d (!!! second chance !!!)

*** WARNING: Unable to verify checksum for C:\Users\Luna\Downloads\SS14.Launcher_Windows\bin_arm64\loader\SDL3.DLL

USER32!GetDC+0x8:

00007ff9`f7be9548 ee8e1db0 ???

WinDbg was also unable to pull stack frames from C# code. It did, thankfully, clearly communicatewhythis was. Yep, it’s our friendmscordaccoreagain!

CLRDLL: Consider using ".cordll -lp <path>" command to specify .NET runtime directory.

CLRDLL: Consider using ".cordll -lp <path>" command to specify .NET runtime directory.

However, my attempts to actually follow said instructions were completely fruitless, giving this error:

0:027:ARM64EC> .cordll -lp C:\Users\Luna\Downloads\SS14.Launcher_Windows\dotnet_arm64\shared\Microsoft.NETCore.App\9.0.9

CLRDLL: Consider using ".cordll -lp <path>" command to specify .NET runtime directory.

CLR DLL status: ERROR: Unable to load DLL C:\Users\Luna\Downloads\SS14.Launcher_Windows\dotnet_arm64\shared\Microsoft.NETCore.App\9.0.9\mscordaccore_AMD64_arm64_9.0.925.41916.dll, Win32 error 0n87

Why is it trying to run anAMD64binary? Wait is WinDbg not natively compiled for ARM64?Sigh. Let’s just do it without C# debugging, I can probably manage based off the SDL stack trace. So I pullSDL3.pdbfrom our server, drop it next toSDL3.dll, and then use the UI to reload the symbols. And that gets us a bit further, we now have proper function names for SDL3!

So I double click one of the entries in the UI’s stack trace view. And the entire debugger breaks. Stack trace view goes empty. Every action I try to make causes more of these errors to be printed:

Machine is not a possible execution machine

Unable to get current machine context, HRESULT 0x8000FFFF

Machine is not a possible execution machine

Unable to get current machine context, HRESULT 0x8000FFFF

Machine is not a possible execution machine

Unable to get current machine context, HRESULT 0x8000FFFF

Machine is not a possible execution machine

Machine is not a possible execution machine

Now even WinDbg is broken??

Googling these errors gave nothing useful. One of them gavenot a single result. After just pondering the error for a moment, I thought “wait, why is the command prompt still sayingARM64EC>? ARM64EC is for emulation, but the active debugger processes (SS14.Launcher.exeandSS14.Loader.exe) are both native ARM64.

Turns out that it’s because I startedSpace Station 14 Launcher.exedirectly. You see, that executable is x64 native, and its only job is to set up the .NET environment and launch theactualARM64 executable. Something aboutstartingthe debugging session with that program causes WinDbg to get extremely confused when later looking at the child processes it spawns.

From this point on I just started launchingSS14.Launcher.exedirectly1. This means I wasn’t setting up the sameDOTNET_ROOT(because WinDbg can’t set environment variables when launching things… yes really), but this didn’t really matter. This fixed both the “Machine is not a possible execution machine” errorsandthe issues with showing C# stack traces. I guess WinDbg is compiled for ARM64 after all, and it just decided to run an x64 debug host when you start debugging an x64 application. Fair enough I guess?

## Debugging: what’s SDL doing?

After figuring out all of the above, we couldreallyget started. I also opted to swap outSDL3.dllwith a locally-built copy, so that the debugger could locate source files2. What SDL is doing is pretty straight forward: the first time the window is shown, it clears the background with GDI commands:

I mean… this is like, fine, right? I mean I don’t know much about this code, but why would this crash on ARM but not x64??? The window is valid.GetDC()is an extremely fundamental Win32 function call. If there was something broken with it, my OS would not be usable. What the fuck is going on?

Theif (ShouldClearWindowOnEraseBackground(data))allows it to be disabled via a hint, which can be specified by environment variable. This fixes the crash… until you open a second OS window, then SDL3 callsGetDC()once again andthatcrashes. Not a solution.

So I checked the actualUSER32!GetDCagain, and this time I actually paid attention to the disassembly code instead of glossing over it. What the fuck?pacibspis missing at the start. It’s loading an address for a jump that only jumps tothe next instruction, which isinvalid. In some runs, said instruction was instead a brokenx26-relativestrinstruction that AV’d because the register was all zeroes.

At this point let’s introduce the villain. You might have noticed it in the call stack:DXGI!My_GetDC.

Microsoft is detouring theirown code???

For those who aren’t well-versed in DirectX stuff:DXGIis a fundamental part of DirectX ever since DirectX 10 (Vista). For those who have never modded a game before: adetouris a hack that injects instructions into other functions at runtime, to do evil shit. Why thehellis Microsoft using this in DXGI?

## Debugging: DXGI despair

Through the debugging adventure, I ended up putting a breakpoint on every call toUSER32!GetDC. The first few calls are fine, but then thelastone, the one that crashes, is not.

At this point I got really desperate. “Asking in low-level programming Discords”-level desperate. I ended up asking for help in theDirectX Discord(yes, there’s an official DirectX Discord, and there’s many MS employees in there).

I would like to thank Jesse Natalia from the DirectX Discord for responding swiftly to my messages in there.

After some back and forth there, I wanted to catch DXGI in the act. Maybe that would tell me something, I don’t know. So with a simpleba w4 USER32!GetDC, I put a hardware breakpoint for whenever something wouldwritetoUSER32!GetDC. I did have to awkwardly “run the program for just a little bit” becauseUSER32.dllisn’t loaded immediately at program startup.3

While writing this blog post I realized thereisan intelligent way to do this. It’s calledsxe ld USER32.dll. I’ve literally written about itin this blog before. Oops.

Now this is very interesting. The bottom of the stack trace is quite expected: SDL creates a window, uses ANGLE’s EGL implementation for this, that does a bunch of stuff, and eventually creates a DXGI swapchain. But then what isUpgradeSwapEffect? And why is it installing a detour?

Ah, I already know what this is.

## Optimizing windowed games: flip model

Right. So. DirectX.

When you create a DirectX swapchain, you specify an “effect”, which falls into two categories: “bitblt” and “flip”. To make along story short: bitblt is the “original” one, while flip is the much more modern one added in Windows 84. It’s more efficient and performant, and all software should be using it. Furthermore, on modern versions of Windows and with a GPU supporting “Multiplane Overlays”, flip model actually enables windowed games to be displayed withzero additional latencyover “exclusive” fullscreen mode.

Of course, many games never get updated, or they’re stuck on an ancient version. And many of these games don’t care. So in Windows 11, Microsoft added “Optimizations for windowed games”, which forcibly enables flip model on games that are still using bitblt. Why does DXGI need to install detours for this? Probably some compatibility shit with the bitblt model. I don’t have any deep knowledge of how Win32 GDI stuff works, but it’s not hard for me to imagine there’s some interplay here they need to take care of. I can also confirm thatdisablingthe feature in Windows’ settings menu fixes the crash!

If you’re wondering why SS14 isn’t using flip model: it’s because we can’t. We’re not creating the swapchain directly,ANGLEis. And ANGLE is continuing to useSWAP_EFFECT_SEQUENTIAL. I actually onceexperimented with SS14 managing the swapchain, but this ran into some ANGLE limitations and I never got around to ironing out all the edge cases and crashes. I’d rather just spend the brain power on ditching OpenGL, rather than trying to continue working with this broken API.5.

So here we are. The entire debugging story so far, you’re like, “surely Microsoft didn’t break DXGI on ARM64, huh???” But now it’s becoming plausible. There’s barely any native ARM64 Windows games, and surely none that are using bitblt swapchains. And guess what, you don’t evenneedGetDC()for modern DirectX games. SDL does it because it’s heavily designed for OpenGL. Most games run in x64 emulation, and that presumably works fine. Everything adds up to it being possible this just genuinely fell under the radar at Microsoft.

This should be pretty easy to verify in a minimal example. I cloned anold DirectX SDK sample, updated it to be compiled for ARM64, added someGetDC()calls, aaand… nope, no crash. Then I spent quite a whiletrying various stuff: comparing the swapchain creation code with that of ANGLE, changing various parameters, verifying whether the detour was being installed (it wasn’t). But eventually, I did find it.

It’s the filename.

Of course it’s the goddamn filename.

## I’m on a list

It only happens when the program is calledSS14.Loader.exe.

The final piece of the puzzle. It didn’t happen in a dev environment because then the exe isn’t namedSS14.Loader.exe. Microsoft only enables “Optimizations for windowed games” on a specific list of games. And guess what,noneof those select games are on ARM64, at least until I was unfortunate enough to port mine. How did we get on the list? Who knows.

Microsoft put me on a list, that ships with every Windows install. And this list actually broke my game. Achievement unlocked!

## Addendum: why ANGLE, and about OpenGL on Windows ARM64

Traditionally, OpenGL on Windows has been implemented by the 3 IHVs (Nvidia, AMD, Intel). If they didn’t explicitly go out of their way to add it to their drivers, you’d have no OpenGL beyond 1.0. Those new Snapdragon X devices, however, use Microsoft’s new-ish “OpenGL on D3D12” driver. It’s actually part of Mesa!

The problem with Space Station 14 is that said driver is broken for us, causing severe graphical artifacts and flickering. I had been aware of this for years, because the same driver is used for the GPU acceleration of WSL2, but I never bothered to report it 😬. So for the purpose of porting SS14 to ARM64 Windows, I decided to just immediately force on ANGLE on Qualcomm devices, and call it a day.

What I didn’t know until yesterday is that the OpenGL on D3D12 driver does not ship with Qualcomm’s drivers!It’s on the Microsoft store!I can even install it in my VM and get it to emulate OpenGL on top of DirectX’s software renderer (WARP), just like I had been doing with ANGLE. I’ve finally bothered toreport the graphical issues, so hopefully it gets fixed eventually. If it does get fixed, Microsoft Store distribution means it shouldn’t take too long to trickle down to users, and then we can stop enforcing ANGLE on Qualcomm devices.

For Space Station 14, I will say that this means I’ll be postponing official Windows ARM64 supportfor now. At least until either bug (OpenGL on D3D12orARM64 DXGI detours) are fixed. Or when I finally rewrite the renderer to drop OpenGL, that’s also an option.

## Addendum: clarifications

(This bit added a few hours after publishing)

* “Why not just rename the.exeon ARM”: what I didn’t mention is that Steamworks does not support ARM64 Linux or Windows, at the moment. That means ARM64 builds will not be on Steam regardless, and I didn’t feel like going through even more the effort to addaworkaround, just to improve performance for that 0.001% of people playing the game on a Snapdragon X devicewhile also downloading from our website. And God forbid Microsoft updates the list later based on a bulk import of some random filenames and catches the new name too. The game already works when emulated, so I’m leaving it there until Windows is fixed.

1. DebuggingSS14.Loader.exedirectly would be a pain in the ass because it needs like a dozen arguments and environment variables configured by the launcher. I’d rather not.↩︎
2. Iassumethere’s a way to configure WinDbg to load these if the paths don’t line up properly… but I wouldn’t know how. Lol.↩︎
3. This is because, being a .NET app, most native libraries are dynamically loaded at runtime. Only libraries that are direct dependencies of the.exeare available in the “initial debugger break” period before the program really starts.↩︎
4. If you were one of those people that held onto Windows 7 for as long as possible, this is the kind of shit you were missing out on. Seriously, 8.1 was fine.↩︎
5. Fuck EGL especially.↩︎
