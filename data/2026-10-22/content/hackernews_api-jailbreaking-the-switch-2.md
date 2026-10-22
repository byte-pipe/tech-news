---
title: Jailbreaking the Switch 2
url: https://pepsipu.com/blog/2026-10-switch2-jailbreak-ns2jb/
site_name: hackernews_api
content_file: hackernews_api-jailbreaking-the-switch-2
fetched_at: '2026-10-22T16:04:32.158570'
original_url: https://pepsipu.com/blog/2026-10-switch2-jailbreak-ns2jb/
author: ledoge
date: '2026-10-22'
description: Jailbreaking the Switch 2
tags:
- hackernews
- trending
---

jailbreaking the switch 2 
 
 ns2jb is a software-only jailbreak of the switch 2 for the current latest firmware 23.0.1 
 
 
 October 18, 2026 
 
 cs 
 
 
 
 

# Introduction

You can get a copy of the exploit from thens2jbrepository.

ns2jb is a software-only, tethered jailbreak for the Switch 2. It allows running arbitrary native code as any ordinary sysmodule, and as the built-infssysmodule. This lets us run homebrew, reverse engineer and mod Switch 2 games, back up save files off the Switch, and access most of the Switch 2’s peripherals through MMIO. To my knowledge, it’s the first such exploit for the Switch 2.

To demonstrate the capabilities of this jailbreak, Codex modded a Switch 2 exclusive, Mario Kart World. Thanks to my friends inDabney Housewho helped me choose characters to add and playtest the game.

 
 
 
 
 
Watch the first gameplay video
 
 
 
 
Watch the second gameplay video
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
▶ 0:09
 
 
 
▶ 0:05
 
 
 
 
 
 
 
cinnamoroll, red, and tole tole racing
 
 

first gameplay videosecond gameplay videofirst results photosecond results photo

 
 
 

# Setup

The very first thing I did was set up a harness around the Switch 1 and 2 so Codex could, ideally, jailbreak the Switch 2 without me:

“set a goal to jailbreak the switch 2. make no mistakes”

Edit: Many people have been asking me if I actually used this prompt. No, it’s just a silly caption. I set a /goal for userland code execution, but that didn’t succeed. The jailbreak itself took substantial effort for ~2 weeks. The Mario Kart World, however, was entirely vibecoded in a day, and was just for fun.

The JetKVMs allow Codex to send controller inputs to the Switches over USB and receive video output over HDMI. We also need a way to press the power button—when the Switch 2 crashes, it needs a button press to restart.

That’s what the Bluetooth light switch flicker from Amazon is for. When the lever comes down, it presses the power button. Once the power button is fully pressed, the rest of the lever’s torque lifts the mechanism.

watch the power button get pressed

# Getting code execution

WebKit is a popular target for console jailbreaks, so it’s unsurprising that Codex has picked it for initial code execution.

## Code execution through the browser

It claims to have “native control-flow hijack” by taking advantage of a WebKit n-day loaded via a custom Wi-Fi captive portal.

We’d like to get code execution in microkernel services (or “sysmodules” on the Switch), so we can run homebrew, mod games, download saves, etc.
Unfortunately, this approach of replacing one JavaScript function object with another doesn’t generalize beyond existing functions—we’d need a new way to make arbitrary IPC calls. That looks difficult.

Why?

* WebKit has execute-only memory, or XOM, so even with arbitrary memory RW, we don’t know where a gadget that could perform arbitrary IPC calls is.
* Even if we did, perhaps by parsing relocation data, it’s not clear how we’d construct a signed pointer for it because of PAC.
* And even if we could, with some signing gadget, it’s not clear how we’d call this pointer, since CFI type-checks most call sites.

Codex has reset the goal to complete these steps. It’s a side bet; it may succeed1, but let’s be real: the accessibility of WebKit and the Nintendo BBP reward have probably incentivized many before me to look here2.

While that runs, let’s explore other options.

## Code execution through smilehax2

My idea was to target Switch 1 games, for two reasons:

* They’re built by developers. It’s less likely we’ll need to deal with PAC and CFI, especially because the Switch 1does not support PAC.
* Since the Switch 1 root of trust is owned, we can decrypt the code and read it.

Maybe we can still get the upsides of the browser attack surface—orchestrating from JavaScript, using existing n-days, etc—while avoiding the downsides of WebKit mitigations by finding a Switch 1 game that embeds a browser? Something analogous to Electron, but for games, so we could pull off an exploit like thisDiscord RCE. I can’t disclose this approach’s findings publicly at the moment, but luckily, there are other Switch 1 games.

In particular, I’m interested inSmileBASIC. This is because it’s been pwned before, insmilehax, giving userspace code execution on the 3DS. It’s a giant C++ codebase; surely, if there was an exploitable memory corruption in the BASIC interpreter, there can be another.

Codex found a useful 32-bit integer overflow in the interpreter. When removing items from an array, the interpreter checkedposition + count <= array.length, but the sum could wrap and become negative. To fill the gap created by removing elements, it’s supposed to shift the remaining elements left, like so:

memmove
(

 backing 
+
 position 
*
 8
,
 // start of the gap

 backing 
+
 (position 
+
 count) 
*
 8
,
 // elements after the gap

 (length 
-
 position) 
*
 8
 // bytes to copy

);

Say we have a string arrayRof length 4, and we runREMOVE R,&H60000000,&H3FFFFFFF.position + countwraps to0x9fffffff. As a negative signed 32-bit integer, it’s less thanarray.length. The multiplications by 8 also wrap, so we end up performingmemmove(backing, backing - 8, 32), pulling the previous 8 bytes into the array. The command does report anOut of memoryerror, but it doesn’t matter, since the copy has happened already.

This is useful because the 8 bytes preceding any array in SmileBASIC contain a pointer to the array itself! After theREMOVE, operations onR[0]will treat the array backing as if it were a string.

Since a pointer occupies what would be the length field ofR[0], the string length is enormous, and we can perform reads and writes out of bounds. We read and write to memory by copying to and from substrings ofR[0].

This was a Switch 1 game, so the SmileBASIC agent could work on the exploit on my Switch 1, while the WebKit agent worked on the Switch 2. After some time, it got ROP.

# Getting sysmodule RW

Okay, now we need to compromise a more privileged process. We’re interested inordinary sysmodulesandbuilt-in sysmodules.

Which sysmodule should we pursue? We don’t have their code, so it’s unclear which sysmodules have which privileges.

I gave a few Codex instances the goal of getting sysmodule code execution. Most chose to focus onaudio and ldn. I think that’s because audio and ldn have had bugs on the Switch 2. Codex also looked at theNV service, probably because GPU drivers are generally fruitful?

## Thefssysmodule

In the meantime, I started looking at thebuilt-infssysmodule, because:

* The Switch 1 code shows that it’sable to serve decrypted code.
* There’s a lot of code.
* It’s probably similar to thefsmodule in the Switch 1, since the filesystem API didn’t change very much.

The first reason is the most attractive to me. Even if we can’t get a useful jailbreak fromfs, we can at least decrypt some of the other sysmodules so Codex can find bugs in them.
Other sysmodules likeldrandrolook enticing because they have permission to map executable memory3, but they don’t have large attack surfaces, especially from SmileBASIC. We’ll come back to them later.

### Buffer overflow with path normalization

AnIFileSystem handlehas an IPC command,GetEntryType. This takes a path string, normalized withPath::Normalize.

Paths containing a parent-directory component with a backslash, like/..\, call into a helper that allocates a temporary heap buffer of 0x301 bytes. Our path is copied in, but it can be larger than the buffer, causing a buffer overflow. lol

We’ll need a good victim allocation to overflow into. Codex found that theBufferedStorageobject allocates a cache entry for its files. If that entry has its dirty bit set, reads and writes to the file follow a pointer to cached data.
We can hijack that for arbitrary read/write4.

From here, I scanned through memory to find SmileBASIC’s connection object and set thesaved PID to 1.
Now, my process has “FullPermission”, meaning I can perform privileged filesystem actions. I dumped internal storage and all ordinary sysmodule code, so Codex could perform offline analysis and I could understand where to go next.

# Getting code execution as any ordinary sysmodule

Homebrew and modding typically rely on executing our own native code. Looking at the dumps, the only ordinary sysmodule with permission to map executable code isro. All these sysmodules have CFI, PAC, and XOM. Theinterfacefor the module seems pretty minimal too. It seemed more fruitful to pursue a logic bug than to look for memory corruption inrodirectly.

Let’s revisit that first point aboutfsserving decrypted code. This was useful for dumping the code for ordinary sysmodules. What’s the intended functionality of this interface? Loading programs?

Games and ordinary sysmodules are distributed asNintendo Content Archives, or NCAs, containing a filesystem image called ExeFS. This contains a file for the main executable,main, and program metadata,main.npdm.

To load a program, the built-inldrsysmoduleasksfsto open ExeFS, andfsreplies with an IPC handle to the filesystem.fsalso provides two pieces of cryptographic information about the NCA header: the header’s SHA-256 hash and the developer’s signature of that hash. The loader uses this information to perform two signature checks:

* Is Nintendo’s signature ofmain.npdm’s process permissions and the developer’s public key valid?
* Is the developer’s signature of the NCA header hash valid?

Seems cryptographically sound to me, because, in theory:

* the NPDM signature fixes the process permissions and developer key;
* the key fixes the NCA header’s signature;
* the signature fixes the NCA header’s hash;
* the hash fixes the NCA header’s contents, including its filesystem hashes;
* those hashes fix the executable content.

In practice, however, I’m doubtful of that last claim, because it’s the responsibility of thefsmodule to ensure the served filesystem matches the NCA header’s filesystem hash, and we have ARW in it.

## Arbitrary r/w to native code execution

Indeed, with ARW, we can replace the ExeFS object behind the loader’s IPC handle with our own temporary filesystem. This filesystem still needs to serve a valid developermain.npdmfor the loader’s first check, but the executablemainitself can be arbitrary.
The second check will pass because, by the time the loader opens the filesystem,fshas already submitted the valid NCA header hash and signature for the original filesystem.

There are two writes we perform:

* The first puts a temporary filesystem object we’ve made into the domain-table entry for the loader’s ExeFS. This temporary filesystem contains the originalmain.npdmand our replacementmain.
* The second puts the loader’s ExeFS object into the domain-table entry for our temporary filesystem. It’s just to keep refcounts consistent and preventfsfrom crashing.

These writes must happen after the loader requests the ExeFS filesystem but beforefsprocesses the subsequent file requests. How do we ensure this?

Thefsprocess maintains a list of its IPC connections. When a connection has a new IPC message,fsprocesses it.
Using our arbitrary read/write, we can replace the handlefswaits on for the loader’s IPC connection with an event handle we control from SmileBASIC. That lets us control whenfsprocesses a loader message.

With this, we can execute arbitrary code as any program we have amain.npdmfor!

## Getting built-in sysmodule native code execution

Whatmain.npdms do we have? Well, all of them. With ARW, we can use to the loader’sfsp-srvconnection to copy the NPDM of any ordinary sysmodule or game.

We’ll use this capability to launch our own code usingro’s NPDM. As mentioned earlier,ro’s NPDM gives it permission to invoke kernel SVCs likeSetProcessMemoryPermission,MapProcessCodeMemory, andMapProcessMemory. In this case, we’ll useMapProcessMemoryto create a writeable view offs’s existing code. We can also dumpfs’s code by reading this view.

These calls, however, require aKProcesshandle to the process. To get a handle tofs, we’ll use our ARW to overwriteIEventNotifier’s 4-byte handle with0xffff8001and then callGetEventHandlefrom SmileBASIC. The kernel interprets this value to mean “the current process’s handle”, so SmileBASIC getsfs’sKProcesshandle.

We can then send this handle to our customroprocess, who patchesfs’s code.

# Conclusion

Arbitrary code execution with any ordinary sysmodule’s permissions seems really powerful. We can investigate hardware without first exploiting each device’s driver. I’m hopeful this will help the homebrew community make progress toward CFW.

In the short term, there are a few next steps I think would be interesting:

* Porting thefssysmodule exploit to WebKit. Now that we know what bug we want to exploit, being able to perform arbitrary IPC calls is not as valuable. We might be able to trigger ARW infsby changing the data used by WebKit’s existing filesystem code.
* This jailbreak is tethered, and we don’t currently have a way to compromise built-in sysmodules other thanfs.fsis a built-in sysmodule, so SM skips service ACL checks fromfs, providing the same capabilities assmhax. I wonder if we can find bugs in other built-in modules?
* With native code execution infs, we can orchestrate its crypto hardware directly. For example, it’s used for NCA4 decryption.
* The exploit has also been tested on the Switch 1, but I haven’t gotten around to packaging it yet. It wouldn’t provide the capabilities of a modchip, but it wouldn’t require any external hardware.

For now, I’m excited to see all the upcoming Switch 2 homebrew, emulation, and modding.

## Footnotes

1. It did not succeed.↩
2. It’s not inherently bad to attempt a WebKit exploit. Once we have a bug in a sysmodule we know to be valuable, it might make sense to go back and try to exploit it in WebKit with a data-only attack. This is because WebKit is accessible offline, meaning Nintendo can’t withdraw it like an eShop title. However, at this stage of our research, it’s not worth the cost to our iteration speed.↩
3. I wonder if one day Nintendo will map ordinary sysmodules and even game code via encrypted blobs only the kernel or secure monitor can decrypt. Then, no userspace process could observe any code on the system—there can never be RX mappings in userspace.
Even the loader module, which starts new processes, would ask a higher exception level to load encrypted blobs it supplies. There’d be tradeoffs, like games being unable to read their own code at runtime. However, Nintendo has already started removing dynamic code features, like the JIT sysmodule. I wonder if this is the direction the Switch is headed. Luckily, that day is not today.↩
4. Initially, Codex’s read/write primitive repeated the buffer overflow on the cache object each time it wanted to change the backing buffer pointer. This hurts stability, especially when following many pointers consecutively, since each change is a chance to crash the system. We can use a similar trick to the onehere. We can use some overflows to point the first cache entry’s backing buffer pointer at another cache entry’s metadata. Then we can replace the second cache entry’s pointer without risking more overflows.↩

 
 
 

Subscribe