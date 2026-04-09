---
title: Doing My Day Job on Chimera Linux - Wesley Moore
url: https://www.wezm.net/v2/posts/2025/daily-driving-chimera-for-work/
site_name: lobsters
fetched_at: '2025-07-01T23:06:49.689480'
original_url: https://www.wezm.net/v2/posts/2025/daily-driving-chimera-for-work/
date: '2025-07-01'
tags: linux
---

## Doing My Day Job on Chimera Linux

29 June 2025

·
updated

30 June 2025

View of sugar cane fields from where I was working.

SinceI started running the first alpharelease ofChimera Linuxin
2023, my goal has been to eventually migrate to Chimera as my primary operating
system. This includes personal tinkering as well as for my job as a programmer.
A recent trip to Central Queensland afforded an opportunity to test the waters
of daily driving Chimera Linux for work. The trip spanned two weeks and involved
working remotely (as usual) during the week, and sightseeing on the weekends.

This post details some of the barriers that I encountered and how I worked
around them. While the post is focussed on Chimera Linux, the details probably
apply to most distributions usingmusl libc.

This is not the first time I’ve tried using a musl based distribution while on
a working holiday. I did the same withVoid Linux (musl) in 2019.
So, I’m not going into this 100% blind.

### Preparations

#### Hardware

The last time I did working travel like this I used Windows + WSL on myLenovo Yoga Slim 7x ARM laptop.
This worked pretty well, but since then Windows has become unstable on that machine.
Every few days it crashes and reboots with the error:

The system has rebooted without cleanly shutting down first. This error is
caused because the system stopped responding and the hardware watchdog
triggered a system reset.

Usually I don’t see the reboot. I just open it and it has restarted—
everything I had open is gone. ApparentlyI’m not the only one
experiencing the issue. I’ve tried various things to fix it, including a
clean reinstall, but the issue remains.

After the reinstall failed to fix WindowsI finally got around to installing
Chimera Linux on it. However, Linux support for Snapdragon X based laptops is
still a work in progress. The main issues are: the webcam doesn’t work, and the
battery drains pretty quickly while suspended. It is more stable than Windows though.

While usable, this felt a little too bleeding edge for a machine I’d need to
work from, so I picked up aLenovo Yoga 7 2-in-1 (14", Gen 10)laptop
with a decentEoFYdiscount. It’s
got a AMD Ryzen AI 7 350 CPU with 8 cores (4×Zen 5, 4×Zen 5c), 32 Gb RAM, and
1Tb NVMe. I was also curious to see what things were looking like on the x86
side of the fence (my last x86_64 laptop was from 2022).

Lenovo Yoga 7 2-in-1 (14" Gen 10)

#### Software

Installation of Chimera on the new laptop was straightforward:

1. Disable Secure Boot
2. Boot from live USB flash drive
3. Followinstallation instructions

fastfetch output on the Yoga 7 2-in-1.

The product I work on,Prince, is implemented in a mixture ofMercuryandRust.
I createdan apk package for the specific version of the Mercurycompiler we use.
The main issue I encountered here was Chimera’sfortify-headersdid not play nice
with the Mercury build, so I added apatch to disable it.

We also use a pinned version of Rust for building Prince, butrustuptoolchains
don’t work on Chimera—it’s only possible to run the packaged
version of Rust. Building Prince with this version of Rust was fine.

With Prince built, the next hurdle to jump over was passing the test suite. This
initially failed due to different output produced byzlib-ngused by Chimera,
compared tozlibused by other distros. This was easily fixed by telling our
build system to buildzlibwhen on Chimera Linux (like we already do for some
other systems).

Now most of the test suite passed, but there were still some failing tests. I
tracked this down to a difference in the regular expression syntax of GNUdiffand BSDdiff. We use the followingdiffinvocation to compare PDFs in our test
suite:

diff_pdf
() {

 (
[
!
-s
"$
1
"
]
&&
[
!
-s
"$
2
"
]
) ||

 $
DIFF -u -a
\

 --show-function-line
='
^[0-9][0-9]* 0 obj
'	\

 -I
'
^/FontName
' \

 -I
'
^/BaseFont
' \

 -I
'
^/MediaBox
' \

 -I
'
^/BleedBox
' \

 -I
'
^/TrimBox
' \

 -I
'
^<pdf:Producer
' \

 -I
'
^<xmp:CreateDate
' \

 -I
'
^<xmp:MetadataDate
' \

 -I
'
^<xmp:ModifyDate
' \

 -I
'
^<xmpMM:DocumentID
' \

 -I
'
^\(<<\)*/ModDate
' \

 -I
'
^\(<<\)*/CreationDate
' \

 -I
'
^\(<<\)*/Producer
' \

 -I
'
^[0-9]* 00000 n $
' \

 -I
'
^[1-9][0-9]*$
' \

 -I
'
^/ID \[<
' \

 "$
@
"

}

Notably, grouping in GNUdiffuses escaped parenthesis\(,\), which is
what our test harness uses. Whereas BSDdiffuses the more conventional
unescaped version(,). If I edited thediff_pdffunction to remove the
escaped parenthesis, then the test suite passed. I didn’t want to carry this change
specifically for my environment though. For various reasons I also didn’t come
up with a satisfying way to automatically switch syntax, so Ipackaged GNU
diffutils. Our test runner is already set up to prefer using agdiffbinary when present, so with mydiffutilspackage installed the test
suite passed without modification.

The last piece of the puzzle was a text editor. For work I use a mix ofZedandRust Rover(although now thatZed has debugger supportRust
Rover’s days may be numbered). I have previously got Rust Rover running on
Chimera, but when I tried again it failed to start with anIOException.

I turned my attention to Zed. Zed used to be packaged for Chimera, but it
started depending on thelivekitcrate, which downloads a pre-compiledlibwebrtc.soinbuild.rs. Unsurprisingly this pre-built library does not work
on Chimera, and theZed project are unwilling to make LiveKit
optional. The Zed project in general is extremelyfree-and-easy with
downloading pre-compiled binaries(that don’t run on Chimera),
and despite this being raised, acknowledged, and work started in October 2024
it remains unresolved as of 29 Jun 2025.

Fortunately Zed is open-source, and Chimera community memberpj has a
forkthat strips it down and makes it buildable on Chimera. He also
resurrected thecports package. I built this and my editor
situation was solved. I could also fall back to Neovim if needed too.

Four other programs that are important to my workflow are1Password,Obsidian,Signal, andBeyond Compare. 1Password, Obsidian, and Signal
were readily installed viaFlatpakpackages onFlathub. For Beyond Compare
I set up aDistroboxArch Linux container. This worked great, whenever I
needed to call upon Beyond Compare’s merge conflict resolution abilities I ran:distrobox enter arch -- git mergetool.

After confirming that the webcam worked in Signal (we do meetings in Signal) I
was good to travel!

### How did it go?

Totally fine. My preparations paid off and I didn’t encounter any blockers to
getting my work done. I did run into one tool that I use occasionally
that was not available for Chimera: theMuPDF tools. I briefly
considered packaging them, but after seeingthe Arch PKGBUILDI
promptly aborted that plan, and installed them in the Arch Distrobox container
withparu -S mupdf-toolsand carried on.

As a Rust developer (i.e. someone that primarily develops in Rust) one of the
main annoyances on Chimera is missing support forrustup. Being able to
install and switch to different Rust versions is nice at times, but the main
issue is being unable to install targets for cross-compiling. This is needed when
targeting microcontrollers, or say a Raspberry Pi Zero. I also can’t dorustup doc --stdto open an offline copy of the standard library documentation (it
seems therust-docpackage in Chimera only contains licences). I think the
solution to this will have to be Distrobox for now.

Having said that,rustupis fully statically linked anddoesrun on
Chimera. The issue is that the toolchains that it installs do not work. There
is a community project publishingbuilds of Rust nightly atmusl.rsthat are compatible with Chimera. This can come in handy
in the odd occasions where a nightly toolchain is needed.

To make it easier to switch between the system rust and nightly rust I installed rustup with:

RUSTUP_INIT_SKIP_PATH_CHECK=1 sh rustup-init --default-toolchain none

And then linked the local toolchains:

rustup toolchain link system /usr

rustup default system

rustup toolchain link musl-nightly ~/.local

This makes it easy to use the nightly version only when needed. For
example, I wanted to format the code in a doc-test, which is not stable yet. I
could do this with:

rustup musl-nightly cargo fmt -- --unstable-features --config format_code_in_doc_comments=true

(for some reason the usualcargo +musl-nightly fmt ...invocation did not work)

On Distrobox, I reached for an Arch Linux container as my fallback distro, but
Arch only officially supports x86_64. This poses a challenge if I am to
replicate this setup on the ARM-based Yoga Slim 7x. For this reason I think
I’ll switch to usingVoid Linuxas my Distrobox fallback in the future. (In
case it isn’t obvious I have no desire to use Debian/Ubuntu if I can avoid it).

### Thoughts on the laptop

As an aside, how did a current generation AMD laptop compare to the year old
ARM-based Yoga Slim 7x? Overall fine, although I still strongly prefer the 7x.
The 7x runs cooler, and is thinner and lighter, which makes it more pleasant to
move and hold. The AMD machine seemed to run hotter, and fire up the fan more.
In particular, the fan seemed to run whenever it was charging and being used at
the same time. Battery life seemed decent. I was able to do about 7 hours of
programming work on Prince, before it needed charging.

As in myoriginal review of the Yoga Slim 7xI used a clean build of theGleamcompiler to do some crude benchmarking:

git clone https://github.com/gleam-lang/gleam

cd gleam

git checkout v1.11.0

cargo fetch --locked

cargo clean && time cargo build --release --locked

Yoga Slim 7x specifications for reference:

fastfetch output on the Yoga 7x

I ran the Gleam build a couple of times on both laptops while plugged into power
using Rust 1.87.0. These were the results:

Device
CPU
Topology
Arch
Time

Yoga Slim 7x
Snapdragon X Elite
12c
ARM
0:49

Yoga 7 2-in-1
AMD Ryzen AI 7 350
8c/16t
x86_64
1:21

So, the 7x with its 4 additional cores is a good bit faster.

The 2-in-1 does have USB-A ports, which is nice. I didn’t make use of the
2-in-1 functionality, or the included stylus. It doesn’t seem like GNOME
detects the different lid configurations, and the on-screen keyboard didn’t
appear when the screen was flipped around (although this could be a setting I
missed).

In the end the 7x is cooler, faster, lighter, and thinner. I plan to sell the
2-in-1.

### Conclusion

The experiment was a success. This has given me more confidence to pursue
setting up my dev environment on my primary desktop computer, but there’s still
some things to address. Currently that machine runs theCOSMIC Desktop, which
is not packaged for Chimera, and doesn’t look like it would be a lot of fun to
implement.

The switch to COSMIC was prompted by X11 having unfixable tearing on my Intel
B580 GPU. Prior to that I ranAwesomeWMfor many years, and would like to
explorePinnacle(an Awesome-like Wayland compositor) as an alternative. It
is simpler to package than COSMIC, and I’ve alreadypartially completed
it. I shall continue to check things off the TODO list and
will get there eventually.

### Stay in touch!

Follow me on the⁂ Fediverse,subscribe to the feed,
 orsend me an email.
