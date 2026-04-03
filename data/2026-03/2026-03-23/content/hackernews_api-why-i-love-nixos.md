---
title: Why I love NixOS
url: https://www.birkey.co/2026-03-22-why-i-love-nixos.html
site_name: hackernews_api
content_file: hackernews_api-why-i-love-nixos
fetched_at: '2026-03-23T19:49:09.207592'
original_url: https://www.birkey.co/2026-03-22-why-i-love-nixos.html
author: Kasim Tuman
date: '2026-03-22'
description: Why I love NixOS is really about the Nix package manager, reproducibility, and sane system management in the LLM coding era.
tags:
- hackernews
- trending
---

22 Mar 2026

# Why I love NixOS

What I love about NixOS has less to do with Linux and more to do
with theNix package manager1.

To me, NixOS is the operating system artifact of a much more important
idea: a deterministic and reproducible functional package
manager. That is the core of why I love NixOS. It is not distro
branding that I care about. It is the fact that I can construct a
whole operating system as a deterministic result of feeding Nix DSL to
Nix and then rebuild it, change it bit by bit, and roll it back if I
do not like the result.

I love NixOS because most operating systems slowly turn
into a pile of state. You install packages, tweak settings, try random
tools, remove some of them, upgrade over time and after a while you
have a machine that works but not in a way that you can confidently
explain from first principles. NixOS felt very different to me. I do
not have to trust a pile of state. I can define a system and build it.

I love NixOS because I can specify the whole OS
including the packages I need and the configuration in one
declarative setup. That one place aspect matters to
me more than it might sound at first. I do not have to chase package
choices in one place, desktop settings in another place and keyboard
behavior somewhere else. Below are a couple of small Nix DSL examples.

* GNOME extensions:

environment.systemPackages = with pkgs; [
 gnomeExtensions.dash-to-dock
 gnomeExtensions.unite
 gnomeExtensions.appindicator
 libappindicator
];

services.desktopManager.gnome.extraGSettingsOverrides = ''
 [org.gnome.shell]
 enabled-extensions=['dash-to-dock@gnome-shell-extensions.gcampax.github.com', 'unite@hardpixel.eu', 'appindicatorsupport@rgcjonas.gmail.com']

 [org.gnome.shell.extensions.dash-to-dock]
 dock-position='BOTTOM'
 autohide=true
 dock-fixed=false
 extend-height=false
 transparency-mode='FIX'
'';

* Key mapping per keyboard:

services.keyd = {
 enable = true;

 keyboards = {
 usb_keyboard = {
 ids = [ "usb:kb" ];
 settings.main = {
 leftcontrol = "leftmeta";
 leftmeta = "leftcontrol";
 rightalt = "rightmeta";
 rightmeta = "rightalt";
 };
 };

 laptop_keyboard = {
 ids = [ "laptop:kb" ];
 settings.main = swapLeftAltLeftControl;
 };
 };
};

Those are ordinary details of a working machine, but that is exactly
the point. I can describe them declaratively, rebuild the system and
keep moving. If I buy a new computer, I do not have to remember a long
chain of manual setup steps or half-baked scripts scattered all over. I
can rebuild the system from a single source of truth.

I love NixOS because it has been around for a long
time. In my experience, it has been very stable. It has a predictable release
cadence every six months. I can set it up to update automatically and
upgrade it without the usual fear that tends to come with operating
system upgrades. I do not have to think much about upgrade prompts,
desktop notifications or random system drift in the background. It
mostly stays out of my way. And if I want to be more adventurous, it
also has an unstable channel2that I can enable to experiment and get
newer software.

I love NixOS because it lets my laptop
be boring in the best possible sense. I recently bought an HP laptop3and NixOS worked beautifully on it out of the box. I did not have to
fight the hardware to get to a reasonable
baseline. That gave me exactly what I want from a personal computer: a
stable system that I can configure declaratively and then mostly
ignore while I focus on actual work.

I love NixOS because it makes experimentation cheap and safe. I
can try packages without mutating the base system. I can construct a
completely isolated package shell4for anything from a one-off script
to a full-blown project. If I want to harden it further, I can use the
Nix DSL to specify the dependencies, build steps and resulting
artifacts declaratively. That is a much better way to work than
slowly polluting my daily driver and hoping I can reconstruct what I did
later.

I love NixOS because I can use the same package manager across macOS
and Linux. There is also community-maintained support for FreeBSD,
though I have not used it personally. That is a huge practical benefit
because my development tooling and dependency management can stay
mostly uniform across those systems. It means the value of Nix is not
tied only to NixOS. NixOS happens to be the most complete expression
of it, but the underlying model is useful to me across platforms.

I love NixOS because it fits especially well with the way I work in the
current LLM coding era.

Tools are changing very quickly. Coding agents often need very
specific versions of utilities, compilers and runtimes. They need to
install something, use it, throw it away, try another version and keep
going without turning my PC into a garbage dump of conflicting
state. Nix fits that model naturally. If I tell a coding agent that I
use Nix, it is usually clever enough to reach fornix shellornix developto bring the needed tool into an isolated environment
and execute it there. That is especially handy because Nix treats
tooling as a declared input instead of an accidental side effect on
the system.

A concrete example: I recently built a voice-to-text agent in
Rust5. I did not have the Rust toolchain installed on my system. I
simply told the coding agent that I use Nix, and it figured out how
to pull in the entire Rust toolchain through Nix, compile the project
inside an isolated shell and produce a working binary. My base system
was never touched. No~/.cargo, no~/.rustup, no mutated PATH
entries left behind. Without Nix, the agent would have reached forcurl | shto install rustup, quietly mutated my environment and
left my system slightly different forever. With Nix, none of that
happened.

This pattern generalizes. Every time an agent needs Python 3.11 vs
3.12, a specific version offfmpeg, an obscure CLI tool or a
particular compiler, Nix gives it a clean and reversible way to get
exactly what it needs. The agent does not have to guess whether a
tool is already installed or in the wrong version. It just declares
what it needs and Nix takes care of the rest in a sandboxed way.

The other thing I appreciate is that Nix turns an agent's
experiment into something you can actually commit and reproduce. Once
the agent has a working setup, you can capture the exact dependencies
in aflake.nixand runnix flake checkto verify it builds
cleanly from scratch. That transforms an ad hoc agent session into a
reproducible, verifiable artifact. That is a much stronger foundation
for delivering something that works reliably in production than hoping
the environment happens to be in the right shape on the next
machine.

I love NixOS because I like what Nix gives me in deployment too. I
have never been a big fan of Docker as the final answer to the "works
on my machine" problem. It solved important problems for the industry,
no doubt about that, but I always found the overall model less
satisfying than a truly deterministic one. Nix gives me a much better
story. I can usedockerTools.buildLayeredImageto build smaller Docker
images in a deterministic and layered approach. If I can build it on
one computer with the proper configuration, I can build the same
artifact on another one as long as Nix supports the architecture,
which in my experience has been very reliable.

That coherence is one of the things I value most about NixOS. The same
underlying model helps me with my laptop, my shell, my project
dependencies, my CI pipeline and my deployment artifact. It is one
way of thinking about software instead of a loose collection of
unrelated tools and habits.

So when I say I love NixOS, what I really mean is that I love what it
represents. I love a system that is declarative, reproducible,
reversible and stable. I love being able to experiment without fear
and upgrade without drama. I love that it helps me focus on building
and experimenting with fast-moving tools, including LLM coding
agents, without worrying about messing up my system in the process.

I love NixOS because it is the most complete everyday expression of
what I think software systems should be.

## Footnotes:

1
 

If you are new to Nix, I wrote a more practical
getting-started guide here:Nix: Better way for fun and profit.

2
 

By unstable channel I mean the official
`nixos-unstable` or `nixpkgs-unstable` channels. SeeChannel branchesandchannels.nixos.org.

3
 

HP EliteBook X G1a 14 inch Notebook with 64 GiB RAM and
AMD Ryzen AI 9 HX PRO 375.

4
 

For example,nix developdrops you into an interactive shell environment that is very close to
what Nix would use to build the current package or project.

5
 

A voice-to-text agent I built in Rust that replaced
Whisper and Willow Voice in my personal workflow. I wrote it first for
macOS and then ported it to Linux. I have been using it as a daily
driver for a couple of months now. I am considering open sourcing it
or releasing it as a standalone app.

Tags
: 
nix
 
ai