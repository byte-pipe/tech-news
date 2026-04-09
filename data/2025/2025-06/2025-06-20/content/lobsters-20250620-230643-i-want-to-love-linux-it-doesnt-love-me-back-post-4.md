---
title: 'I Want to Love Linux. It Doesn’t Love Me Back: Post 4 – Wayland Is Growing Up. And Now We Don’t Have a Choice — fireborn'
url: https://fireborn.mataroa.blog/blog/i-want-to-love-linux-it-doesnt-love-me-back-post-4-wayland-is-growing-up-and-now-we-dont-have-a-choice/
site_name: lobsters
fetched_at: '2025-06-20T23:06:43.182641'
original_url: https://fireborn.mataroa.blog/blog/i-want-to-love-linux-it-doesnt-love-me-back-post-4-wayland-is-growing-up-and-now-we-dont-have-a-choice/
date: '2025-06-20'
tags: a11y, linux
---

fireborn

# I Want to Love Linux. It Doesn’t Love Me Back: Post 4 – Wayland Is Growing Up. And Now We Don’t Have a Choice


 Published on
June 19, 2025

## The future is Wayland. Let’s make sure we’re invited.

This post wasn’t supposed to exist — not yet. I meant to talk about bootloaders. About inaccessible USB installs. About the deafening silence between pressing the power button and hearing a screen reader. That post is still coming.

But something bigger is happening now.

Ubuntu is dropping GNOME on X11.GNOME itself is removing X11 code.And in Red Hat Enterprise Linux 10, Xorg is already gone.

Not just deprecated. Removed from the repositories entirely in the long-term.

Fedora hasn’t removed the GNOME on Xorg session yet, neither has Ubuntu. But they will. Everyone will. That’s where this is going. Other desktops will drop x11 support.

And for those of us who depend on accessibility, that shift is seismic.

### I Held Out. For Good Reasons.

Wayland used to mean losing access.

AT-SPI was fragile. Orca was inconsistent or silent. Flat review didn’t work. Login greeters didn’t speak. There were no logs, no fallbacks, no recovery paths.

X11 was ugly. But it waspredictable. I stuck with it because it let me work — not well, but reliably.

Then I triedGNOME on Wayland.

And… it works. Orca is responsive. Focus tracking behaves. That ancient modifier bug whereCaps Lock would stickafter Orca commands? Gone. That was an X problem — and Wayland fixes it.

It’s not perfect. But it’s progress I can feel.

### Xorg Is Going Away — Slowly, But For Real

The writing’s been on the wall for a while. But now it’s more than that.

Xorg isn’t just deprecated. It’s being removed.Red Hat made it official in RHEL 10 — gone from the repos. Not available. Not supported.

Other distros are following. First it disappears as the default. Then as an option. Then, eventually, as a package. Ubuntu is almost there. Fedora’s right behind. GNOME no longer wants to maintain X11 support.

Yes,Gentoo will be Gentoo.Yes,Debian will keep it until it won’t compile anymore.Yes, theAUR will archive its ghost for years.

But that’s not a fallback you can depend on. This won’t be a clean cut — it’ll be a long, messy decline.

And the longer we wait to make accessibility real on Wayland, the more people we leave behind.

### Developers Are Rising to the Challenge

Here’s the good news: I’ve talked to developers fromGNOME,KDE, andFedora.

They get it. And they’re taking it seriously.

* GNOME’s Wayland session is now stable and usable with Orca.
* KDE is catching up — and has alegally blind developerleading accessibility improvements.
* COSMIC is building Wayland from scratch with accessibility and global hotkey support in mind.
* For once, accessibility isn’t just a postscript. It’s in the room where design happens.

This transition is happening — but we’re not being ignored anymore.

### What We Gain From Wayland

This isn’t just a funeral for X. Some things in Wayland are genuinelybetter:

* Modifier key sanity.Caps Lock doesn’t stick. No weird leftover key states after Orca commands. That’s fixed.
* Clean focus behavior.Window focus events are less chaotic. Orca doesn’t get confused between apps the way it used to.
* Security that matters.Apps can’t spy on each other’s keystrokes or windows. That means your assistive tech is safer by default.
* A real foundation.X11 was a museum exhibit of patches and abandoned extensions. Wayland gives us something intentional. That alone opens doors tobuilding accessibility right, instead of constantly duct-taping it on.

### … But We’ve Lost a Lot, Too

* Headless GUI workflows are broken.On X11, I usedxorg-video-dummywith a custom/etc/X11/xorg.conf.d/10-headless.confto create a virtual monitor. Electron apps ran fine. I usedocrdesktop. I could automate real tasks with no screen at all.Under Wayland? Nothing comparable exists. Electron apps lag or crash. The entire workflow? Gone.
* Desktop choice has collapsed — for now.My Linux journey started at theTTY, thenUnity, thenMATE— the desktop I came to rely on most.My first experience with a window manager wasi3, and later I forkedDWMto build something accessibility-first. I loved window managers: minimal, efficient, tailored to how I think.On Wayland? That kind of freedom is on hold. GNOME is the only working option for now.But KDE is moving. COSMIC is promising. Others will get there. I want that future back — not just for me, but for every user who deserves to choose how they compute.
* MATE isn’t on Wayland yet — and it matters.Let’s be real:MATE was the preferred desktopfor blind users under X11. Stable. Keyboard-accessible. No surprises.It doesn’t support Wayland yet. I hope it does. I hope it’s doneright— not half-baked, not bolted on. Because while I enjoy solving problems, not everyone wants to live in a constant battle. And they shouldn’t have to.
* We lost an ecosystem.xdotool,xclip,xwininfo,ocrdesktop, all the little tools that made scripting, testing, OCR, and interaction possible — broken or unported. Not impossible to rebuild. But we have to start over.

### Compositor Compatibility Is Still a Minefield

Let’s talk about something most people never notice:how your compositor handles input and permissions.

If you’re a sighted user, you can probably switch between Sway, Hyprland, and Wayfire without a second thought. But for those of us using screen readers, that freedom vanishes quickly.

* wlroots-based compositors— used by many lightweight Wayland setups — stilldon’t reliably support the D-Bus keybinding interfacesthat Orca depends on. I’ve heard of people getting them to work — sometimes — but oftennot on laptop keyboards, where modifier handling is especially flaky.

That means most tiling Wayland compositors are effectivelyinaccessible out of the box. Until they implement proper D-Bus-based keybinding forwarding, you either use GNOME or lose speech.

And then there’sXDG portals.

I agree: portals are the future. They're the right abstraction. Done well, they’ll let us build accessibility features, input emulation, screen capture, scripting, and more — without depending on insecure hacks.

But today? It’s chaos.

Each compositor can shipits own portal implementations. Some are incomplete. Some are buggy. Some are missing entirely. There's no consistent baseline. One portal might support accessibility events, another might break flat review, and a third might not support screen capture at all.

We’re supposed to be moving forward — but when every compositor speaks a different dialect, users fall through the cracks.

We need consistency.We need a minimum set of working portals and interfaces thatevery compositor supports— not just on paper, but in practice.

And to be clear:this isn’t GNOME’s fault.

I know hating on GNOME developers is popular. I’m not doing that today. GNOME is theonlyreason Wayland accessibility is usable right now. The work they’ve done is real, and it’s miles ahead of anyone else.

No one else is quite on GNOME’s level.KDE is trying — seriously trying. COSMIC too. I know that because I’ve spoken to the people behind them. They care. They’re listening. But GNOME is still the only desktop where accessibility isn’t a maybe — it’s a working reality.

That has to change.And it starts with every compositor agreeing on what “accessible” actually means.

### We Can Still Build Something Better

This isn’t just a painful transition. It’s a rare moment torethink everything.

* A modernocrdesktopusing PipeWire.
* Awaydotoolthat speaks AT-SPI and respects sandboxing.
* Headless GUI support that’s builton purpose, not hacked together.

The architecture is there. The interest is there. The people are listening.

Now’s the time.

### I Still Want to Love Linux

So I’m using Wayland now.Because Ihave to.Because X11 is heading toward the grave.Because I want to help shape what comes next — not just mourn what came before.

This is our moment to make sure accessibility doesn’t get erased in the name of “progress.”To build something better — not just shinier.

Wayland is growing up.Let’s make sure it doesn’t grow up without us.

And to the developers — the ones fixing bugs, wiring up events, untangling toolkit chaos, and answering hard questions with humility:

You are great people doing great things.Even when it’s frustrating. Even when it’s thankless.Thank you.You're the reason I haven’t given up yet.

Oh — and apparently,I’m a Wayland shill now.
Didn’t see that one coming either.
