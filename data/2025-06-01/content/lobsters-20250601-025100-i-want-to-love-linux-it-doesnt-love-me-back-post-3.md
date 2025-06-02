---
title: |
  I Want to Love Linux. It Doesn't Love Me Back: Post 3 – Speakup, BRLTTY, and the Forgotten Infrastructure of Console Access — fireborn
url: |
  https://fireborn.mataroa.blog/blog/i-want-to-love-linux-it-doesnt-love-me-back-post-3-speakup-brltty-and-the-forgotten-infrastructure-of-console-access/
site_name: lobsters
fetched_at: |
  2025-06-01T02:51:00.041572
original_url: |
  https://fireborn.mataroa.blog/blog/i-want-to-love-linux-it-doesnt-love-me-back-post-3-speakup-brltty-and-the-forgotten-infrastructure-of-console-access/
date: 2025-06-01
tags: a11y, linux
---



# I Want to Love Linux. It Doesn't Love Me Back: Post 3 – Speakup, BRLTTY, and the Forgotten Infrastructure of Console Access


            Published on
May 30, 2025

## The Console Is a Lie — Braille on Linux Is a Lovecraftian Joke

Welcome back to"I Want to Love Linux. It Doesn’t Love Me Back."In this post, we’re stepping into the part of Linux that everyone says “just works” — the console. The raw, text-only interface you drop into when X dies, the GUI fails, or you're installing a system from scratch.

Sighted users can rely on it without thinking. But if you’re blind? That safety net comes with holes, duct tape, and a list of arcane incantations.

This is aboutbraille,speech, and theillusionof accessibility in text mode. Not your GNOME terminal, not Konsole, but the real TTY — Ctrl+Alt+F2, system recovery shells, live install environments. The kind of places where graphical desktops are gone and the console is your last, best hope.

Linux claims to support blind users here. It even ships the tools. But using them? Getting speech or braille output when you need it most? That’s a punishing mess of driver quirks, missing defaults, audio stack failures, and layers of modern regression hidden under the surface.

### Speakup: The Crutch That's Always on Fire

Let’s talk aboutSpeakup, the kernel-space screen reader that ties into the virtual console. It’s been around forever. Itworks, or at leastcanwork — if everything is aligned, and you make the right sacrifices to the right deprecated mailing lists.

#### To Arch’s Credit...

Archdoesinclude Speakup in the install ISO. And it evenspeaks, provided you're:

That's a lot of caveats for what should be basic functionality. But I'll give Arch credit:it tries, and it's the only distro that lets me manually bash something together thatmostlyworks. Not by default, not out of the box, but at leastnot actively hostileto the idea.

#### Debian Tries Too… and Actually Remembers You Exist

Say what you will about Debian (and I have), butcredit where credit’s due: it’s one of thevery fewdistros that makes a serious, working effort to support blind users during installation —not just speech, but actual device selection.

Boot the installer, presss, and Speakup comes up. But here’s where Debian stands alone: if you’ve got multiple sound cards — including thoseHDMI audio trapsthat pretend to be speakers but don’t actually output anything —Debian asks you which one you want. And then itsaves that choice. That’s not just a quality-of-life feature. That’s a life-saving one.

It means I can say, with confidence:

“If I don’t hear anything, the system didn’t boot or this hardware’s unsupported.”

Debian treats the installer like it matters, because for a blind user, it does. It’s not a graphical toy that you’ll only run once. It’s thefirst timethe OS proves it knows you exist. And Debian actually shows up.

After installation? It still enables Speakup via a systemd service — and that’s more than most. But here’s whereDebian gets tripped up by the ecosystem: the moment you hit a login prompt, you enter a session withuser-locked audio. This isn’t Debian’s fault. It’s the fault ofPulseAudio,PipeWire, and theentire philosophy of session-bound audio daemonsthat don’t care what the kernel is doing.

So Speakup’s still running. It’s loaded. It’s waiting. But your login sessioncloses the doorand walks away with the audio keys. And now you’ve got a working screen readerscreaming silently into the void.

### BRLTTY: The Underrated Backbone — and a Source of Pain

Let’s talk aboutBRLTTY. It’s one of the most powerful accessibility tools on Linux, and somehow one of the least discussed. This is its first proper appearance in the series — and that’s a problem, because BRLTTY is essential.

It’s the tool that makes braille work. It supports dozens of braille displays over USB, Bluetooth, and serial connections. It can drive displays directly from the TTY, pipe input through speech, integrate with graphical screen readers like Orca, and even act as a bridge between user-space applications and low-level terminal buffers. BRLTTY is the thing that lets blind and deafblind users actuallyusea Linux system — not just when it’s booted, but when it’s broken, when it’s offline, when the network’s down and your last hope is a blinking cursor in a recovery shell.

Especially fordeafblindusers, BRLTTY isn't a luxury — it's the entire UI. When speech fails, you can fall back to braille. When graphics fail, you can fall back to the console. But whenbraillefails, and you can't hear output, and you can't see the screen, you're done. There is no fallback. There is no workaround. If BRLTTY doesn't come up clean, or it binds the wrong port, or it races with udev and loses — that's it. You're locked out.

And it does fail:
- On non-English locales, BRLTTY will frequently misrender or drop characters outright.
- When switching to a graphical session, it often says "screen not in text mode" — which is accurate, but not helpful.
- Sometimes it just gives up and says "no screen." No diagnostic. No explanation. Just that.
- Integration with Orca can break silently. No crash, no error message, just a display that doesn’t update.

I’ve debugged BRLTTY systems for other blind users before. In one case, a deafblind person was completely locked out of their system after a routine upgrade. BRLTTY was running — sort of. The daemon was active, but the display was frozen. No output. They couldn’t read logs, couldn’t even tell if the system had booted. They had to get another blind user to SSH in, trace the USB detection, discover thatmodemmanagerhad eaten the braille port, and rip it out manually. That's the kind of debugging you can't do if you're the one who needs the accessibility support.

And then there’s BRLTTY’s habit ofeating serial and USB ports. Plug in an audio interface or communication device, and it might not appear at all — because BRLTTY bound to the port first. The solution? According to some documentation and forum threads:just disable BRLTTY. Right. Turn off the screen reader for your only input/output device. Perfect.

Want BRLTTY to work reliably at boot? You need to:

This isn’t optional extra functionality. This iscore accessibility infrastructure. And yet Linux treats it like an afterthought — something for edge cases, or niche embedded setups. There's no standard distro integration. There's no fallback detection. There's no sanity checking if the configured device fails. Just silence.

BRLTTY is powerful. It has scripting, speech integration, braille table customization, and the ability to control the system at a level most sighted users never touch. It deserves full-time support, upstream coordination, and testing pipelines. Instead, it gets relegated to a handful of package maintainers and bug reporters in the dark.

## Linux doesn’t support braille.It ships BRLTTY and prays it starts.

### Fenrir: Surprisingly Capable — If You Survive the Kernel Bugs

EnterFenrir, the Python-based userland console screen reader that was supposed to be the modern alternative to Speakup.

And you know what?It’s actually pretty great.- It supports scripting.
- It works with BRLTTY for braille output.
- It’s easy to configure once installed.
- And unlike Speakup, it lives entirely in user space, so you don’t need to mess with kernel modules.

If —and this is a big if— it’s included in your distro’s repositories andyour kernel upgrades don’t suddenly lock up your keyboard when it’s active, then Fenrir can deliver a genuinely usable console experience. That’s not theoretical. That’s from daily use.

But here’s the problem:you still can’t use it to install a distro, or boot into a live ISO, or rescue a broken system. Because:

So even though it’s modern, modular, and capable, it’s still gated behind a successful install — which, for a blind user, is the part we need help with themost.

Fenrir deserves praise for being actively maintained, scriptable, and clean. But like every other tool in this space,it suffers from the absence of upstream integration and predictable defaults.It’s the best tool we have — and it still requires more bootstrapping than most people realize.

### The Console Can Be the Whole System

This is true whether you're using Speakup or Fenrir. Once you're past the installation and configuration barriers, the Linux console can become far more than a fallback. It can be acomplete and powerful daily environmentfor blind users — and for me,it was. For years.

This isn’t just theoretical. The console was my entire system. Not a backup. Not a novelty. Areal workspace— fast, reliable, and built for speech.

The TTY is efficient and free from the visual clutter and accessibility regressions that plague modern desktops. Eventually, I moved away from the console — not because it failed me, but because I wanted to try something more modern: a full desktop with graphical applications, real-time collaboration tools, and the kind of integrated software that still doesn't exist in TTY land. But I left the console behind reluctantly. It had been my whole world, and itworked.It’s not some legacy curiosity. It’s a platform thatshouldbe first-class for blind users. And it nearly was.

### What I Gained — and What I Lost

Switching to a graphical desktop gave me things I couldn’t easily replicate on the console:
- Real-time collaboration through web apps and chat clients.
- Full-featured graphical browsers that could handle modern, JavaScript-heavy websites.
- A larger ecosystem of mainstream software, from productivity suites to communication tools.

That’s what I gained: access to the same digital world as everyone else.

But I lost things, too:

Most of all, I lostconfidence. On the console, I knew every part of the stack. I could trust it. With a desktop, I’m always watching out for the next GNOME regression, the next broken AT-SPI hook, the next time a browser update silently kills accessibility.

Modern Linux desktops offer a broader world — but the console, when it works, offerscontrol. And no blind user should be forced to choose between the two.

This is the tension at the heart of blind accessibility on Linux: the GUI is advancing in features, while the TTY is decaying from neglect. And yet the console remains the most stable, most direct, most reliable interface —when it’s allowed to work. That’s what makes all of this so heartbreaking.

We don’t need miracles. We just need the console — the one place Linux has always claimed to be universal — to actually include us.

This isn’t just about accessibility. This is aboutpower and independence— being able to administer servers, work offline, or troubleshoot real-world problemswith tools that speak to you on your terms. And it’s infuriating that we are stillthis closeto having that experience work out of the box, but only if we fight for it, patch it, and guard it from every system update like it’s a fragile shrine.

### The Chicken-and-Egg Hell

Let’s say you’re blind, you want to install Linux, and you want bothspeech and brailleat boot. Here’s what you have to do:

All just to get a text prompt you canhear or feel.

And every part of that pipeline is fragile, undocumented, and increasingly incompatible with “modern Linux.” There are no presets. No safe defaults. And absolutelyno respectfor the fact that blind users might need to use the TTYwhen their desktop breaks.

### SIDEBAR: Why Session-Locked Audio Screws Blind Users (Even When It Can Be Fixed)

Modern Linux audio —PulseAudio, and nowPipeWire— isn’t just “sandboxed” in the Flatpak sense. It’ssession-locked by design. Only processes running inside the currently active user session are allowed to produce audio output. That’s fine for desktop apps. It’s a disaster forkernel-level screen readerslike Speakup.

#### Speakup vs. the Session Wall

When you boot, Speakup runs outside your user session. It tries to speak usingespeakup, which outputs through ALSA. But once PulseAudio or PipeWire grabs the audio stack, only the current user's session is allowed to use it — and Speakup isn't in that session. Result: silence.

#### The PipeWire Fix (Yes, It Works)

PipeWire is actually flexible enough to fix this. TheFenrir screen reader projectprovides a script that:

Run it once as your user and once as root. Done. You now have working audio forboththe console and graphical environment — simultaneously.

I didn’t learn this from upstream docs. I learned it from areader of my first blog postwho figured it out and shared it. That’s the story of Linux accessibility in a nutshell.

#### The PulseAudio Maybe-Fix

Fenrir also includes a similar script for PulseAudio. It does the same dual-socket trick: one config for the user to serve the audio, and one for root to connect to it. It might work. I haven’t tested it deeply — and honestly, Pulse is older, more fragile, and less predictable.

Still: someone in the community thought to do this. Upstream didn’t.

#### The Real Problem

None of this should be necessary. There isno standard wayto say:

“This process is accessibility-critical. Let it speak.”

No XDG spec. No PipeWire setting. No distro guideline. Nothing.

So when a blind user logs in, modern Linux says:

"Welcome, human! You may now hear sound."

And to Speakup, the one thing that’s been speaking this whole time:

"Shut up. You're not part of the session."

Blind users? Accessibility? System-wide speech?Still treated asnoise.

### The Brutal Truth

If you're blind, here's what Linux offers you in 2025:
-Speech output in the console,maybe, on some distros, under strict conditions.
-Braille output at boot,if you manually configure it in the initramfs.
-User sessions that break accessibility by default.-Screen readers that only work after install, when it's already too late.- And an entire ecosystem that pretends this isn’t a problem.

Console accessibility isn’t a solved problem. It’s a decaying pile of partial solutions that only work if younever make a mistake, never change hardware, and never let your audio stack change.

I want to love Linux. I want to trust it to recover a broken boot, install a headless server, or drop into a rescue shell when everything else fails. But unless I build it all myself — and know every damned quirk of every component —Linux will leave me blind and locked out of the very tools it pretends are accessible.
