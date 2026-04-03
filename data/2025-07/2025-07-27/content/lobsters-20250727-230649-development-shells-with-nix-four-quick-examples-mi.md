---
title: 'Development shells with Nix: four quick examples - Michael Stapelberg'
url: https://michael.stapelberg.ch/posts/2025-07-27-dev-shells-with-nix-4-quick-examples/
site_name: lobsters
fetched_at: '2025-07-27T23:06:49.502602'
original_url: https://michael.stapelberg.ch/posts/2025-07-27-dev-shells-with-nix-4-quick-examples/
author: Michael Stapelberg
date: '2025-07-27'
description: I wanted to use GoCV for one of my projects (to find and extract paper documents from within a larger scan), without permanently having OpenCV on my system. This seemed like a good example use-case to demonstrate a couple of Nix commands I like to use, covering quick interactive one-off dev shells to fully declarative, hermetic, reproducible, shareable dev shells.
tags: nix
---

# Development shells with Nix: four quick examples

published 2025-07-27


 in tag



nix

Table of contents

I wanted to useGoCVfor one of my projects (to find and
extract paper documents from within a larger scan), without permanently having
OpenCV on my system.

This seemed like a good example use-case to demonstrate a couple of Nix commands
I like to use, covering quick interactive one-off dev shells to fully
declarative, hermetic, reproducible, shareable dev shells.

Notably, you don’t need to use NixOS to run these commands! You caninstall and
use Nixon any
Linux system like Debian, Arch, etc., as long as you set a Nix path or use
Flakes (seesetup).

## For comparison: The Debian Way

Before we start looking at Nix, I will show how to get GoCV running on Debian.

Let’s create a minimal Go program which uses a GoCV function likegocv.NewMat(), just to verify that we can compile this program:

package
 main

import

"gocv.io/x/gocv"

func

main
() {

 gocv.
NewMat
()

}

If we try to build this on a Debian system, we get:

debian % mkdir -p /tmp/minimal
debian % cd /tmp/minimal

debian % cat > minimal.go <<'EOT'
package main
import "gocv.io/x/gocv"
func main() { gocv.NewMat(); }
EOT

debian % go mod init minimal
go: creating new go.mod: module minimal
go: to add module requirements and sums:
	go mod tidy

debian % go mod tidy
go: finding module for package gocv.io/x/gocv
go: downloading gocv.io/x/gocv v0.41.0
go: found gocv.io/x/gocv in gocv.io/x/gocv v0.41.0

debian % go build
# gocv.io/x/gocv
# [pkg-config --cflags -- opencv4]
Package opencv4 was not found in the pkg-config search path.
Perhaps you should add the directory containing `opencv4.pc'
to the PKG_CONFIG_PATH environment variable
Package 'opencv4', required by 'virtual:world', not found

On Debian, we can install OpenCV as follows:

debian % sudo apt install libopencv-dev

[…]

Summary:
 Upgrading: 7, Installing: 512, Removing: 0, Not Upgrading: 27
 Download size: 367 MB
 Space needed: 1590 MB / 281 GB available

Continue? [Y/n]

Saying “yes” to this prompt downloads and installs over 500 packages (takes a
few minutes).

Now the build works:

debian % go build
debian % file minimal
minimal: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), […]

…but we have over 500 extra packages on our system that will now need to be
updated in all eternity, therefore I would like to separate this one-off
experiment from my usual system.

We could use Docker to start a Debian container and work inside that container,
but, depending on the task, this can be cumbersome precisely because it’s a
separate environment. For this example, I would need to specify a volume mount
to make my input files available to the Docker container, and I would need to
set up environment variables before programs inside the Docker container can
open graphical windows on the host…

Let’s look at how we can use Nix to help us with that!

## Setup: Nix-on-Debian (or Nix-on-Arch, or…)

Users of NixOS can skip this section, as NixOS systems include a ready-to-use
Nix.

Before you can try the examples on your own computer, you need to complete these
three steps:

1. Install Nix
2. Enable Flakes
3. Set a Nix path

### Step 1: Install Nix

Users of Debian, Arch, Fedora, or other Linux systems first need to install
Nix. Luckily, Nix is available for many popular Linux distributions:

* Debian shipsnix-setup-systemd
* Arch Linux packagesnixand provides documentationon the Nix Arch Wiki
page. In practice, I installed the
package andconfigured a couple ofnixbldusers.
* More generally, there are Nix builds (rpm, deb, pacman) available for a number
of distributions:https://github.com/nix-community/nix-installers

### Step 2: Enable Flakes

Nix flakes are“a generic way to package Nix
artifacts”.

Examples 3 and 4 use Nix flakes to pin dependencies, so we need toenable Nix
flakes.

### Step 3: Set a Nix path

For example 1 and 2, we want to use the Nix expressionimport <nixpkgs>.

On NixOS, this expression will follow the system version, meaning if you useimport <nixpkgs>on a NixOS 25.05 installation, that will referencenixpkgs
in version nixos-25.05.

On other Linux systems, you’ll see an error message like this:

debian-server % nix-shell -p pkg-config opencv
error: file 'nixpkgs' was not found in the Nix search path (add it using $NIX_PATH or -I)

 at «string»:1:25:

 1| {...}@args: with import <nixpkgs> args; (pkgs.runCommandCC or pkgs.runCommand) "shell" { buildInputs = [ (pkg-config) (opencv) ]; } ""
 | ^
(use '--show-trace' to show detailed location information)

We need to tell Nix which version ofnixpkgsto use by setting theNix search
path:

debian-server % export NIX_PATH=nixpkgs=channel:nixos-25.05
debian-server % nix-shell -p pkg-config opencv
[nix-shell:/tmp/opencv]#

Alright! Now we are set up. Let’s jump into the first example!

## Example 1: Interactive one-offs: nix-shell

Nix provides a middle-ground between installing OpenCV on your system (apt installlike in the example above) and installing OpenCV in a separate Docker
container: Nix can make available OpenCV without permanently installing it.

We can runnix-shell(1)to start a bash shell in
which the specified packages are available. To successfully build Go code that
uses GoCV, we need to have OpenCV available:

% nix-shell -p pkg-config opencv
these 194 paths will be fetched (175.80 MiB download, 764.10 MiB unpacked):
 /nix/store/ig2nk0hsha9xaailhaj69yv677nv95q4-abseil-cpp-20210324.2
 /nix/store/yw5xqn8lqinrifm9ij80nrmf0i6fdcbx-alsa-lib-1.2.13
[…]

[nix-shell:/tmp/opencv]$ pkg-config --cflags opencv4
-I/nix/store/mh5b1dx2ifv4jkp9a8lgssxwhzxssb96-opencv-4.11.0/include/opencv4

In case you were wondering: Yes, we do need to specifypkg-configin thisnix-shellcommand explicitly, otherwise runningpkg-configwill run the host
version (outside the dev shell), which cannot findopencv4.pc.

## Example 2: nix-shell config file: shell.nix

Once we have a combination of packages that work for our project (in our
example, justpkg-configandopencv), we can create ashell.nix(in any
directory, but usually in the root of a project) whichnix-shell(without the-pflag) will read:

{

 pkgs
?

import

<nixpkgs>
 { }
,

}:

pkgs
.
mkShell {

 packages
=

with
 pkgs; [


# Explicitly list pkg-config so that mkShell will arrange


# for the PKG_CONFIG_PATH to find the .pc files.

 pkg-config

 opencv

 ];

}

…and then, we just runnix-shell:

% nix-shell
[nix-shell:/tmp/opencv]$ pkg-config --cflags opencv4
-I/nix/store/mh5b1dx2ifv4jkp9a8lgssxwhzxssb96-opencv-4.11.0/include/opencv4

If you’re curious, here are a couple of documentation pointers regarding the
boilerplate around the list of packages:

* Line 1 to 3declare a
functionwith an argument set — this is the required structure fornix-shellto be
able to call yourshell.nixfile.
* pkgs.mkShellis
a convenience helper for use withnix-shell.
* Thewith pkgs;part allows us to writeopencvinstead ofpkgs.opencv.

By the way: With thenixd language
server, editors withLSP
supportcan show the
versions that packages resolve to, point out your spelling mistakes, or provide
features like “jump to definition”.

For example, in this screenshot, I was editingshell.nixin Emacs and was
curious how the Nix source of theopencvpackage looked like. By pressingM-.(xref-find-definitions) with“point”overopencv, I got toopencv/4.x.nixin my local Nix store:

## Example 3: Hermetic, pinned devShells: Nix Flakes

The previous examples used nixpkgs from your system (or Nix path), which means
you don’t need to change the.nixfile when you upgrade your system —
depending on the use-case, I see this behavior as either convenient or
terrifying.

For use-cases where it is important that the.nixfile is built exactly the
same way, no matter what version the surrounding OS uses, we can useNix
Flakesto build in a hermetic way, with
dependency versions pinned in theflake.lockfile.

Aflake.nixcontains the samemkShellexpression as above, but declares
structure around it: ThemkShellexpression goes into theoutputs.devShells.x86_64-linux.defaultattribute and theinputsattribute
containsFlake
referencesthat are available to this build:

{

 inputs
.
nixpkgs
.
url
=

"github:NixOS/nixpkgs/nixos-25.05"
;

 outputs
=

 { self
,
 nixpkgs }:

 {

 devShells
.
x86_64-linux
.
default
=


let

 pkgs
=
 nixpkgs
.
legacyPackages
.
x86_64-linux;


in

 pkgs
.
mkShell {

 packages
=

with
 pkgs; [


# Explicitly list pkg-config so that mkShell will arrange


# for the PKG_CONFIG_PATH to find the .pc files.

 pkg-config

 opencv

 ];

 };

 };

}

By the way: Despite the name, it is a best practice to usenixpkgs.legacyPackages, which conceptually provides a singleimport nixpkgsresult (for
efficiency).

Now, I can usenix developto get a shell with OpenCV:

% nix develop
michael@midna$ pkg-config --cflags opencv4
-I/nix/store/mh5b1dx2ifv4jkp9a8lgssxwhzxssb96-opencv-4.11.0/include/opencv4

The firstnix developrun creates aflake.lockfile, so runningnix developlater will get us exactly the same environment. To update to newer
versions, usenix flake update.

Tip:Instead of a shell,nix develop --command=emacsis also a useful variant.

## Example 4: Making the Flake system-independent

Unfortunately, the aboveflake.nixhard-codesx86_64-linux, so it will not
be usable on, say, anaarch64-linux(ARM) computer, or on ax86_64-darwin(Mac).

Having to explicitly specify thesystemby default is a long-standing
criticism of Nix Flakes.

There are a number of workarounds. For example, we can usenumtide/flake-utilsand refactor ourflake.nixto use itseachDefaultSystemconvenience function:

{

 inputs
=
 {

 nixpkgs
.
url
=

"github:nixos/nixpkgs/nixos-25.05"
;

 flake-utils
.
url
=

"github:numtide/flake-utils"
;

 };

 outputs
=

 {

 self
,

 nixpkgs
,

 flake-utils
,

 }:

 flake-utils
.
lib
.
eachDefaultSystem (

 system:


let

 pkgs
=
 nixpkgs
.
legacyPackages
.
${
system
}
;


in

 {

 formatter
=
 pkgs
.
nixfmt-tree;

 devShells
.
default
=
 pkgs
.
mkShell {

 packages
=

with
 pkgs; [


# Explicitly list pkg-config so that mkShell will arrange


# for the PKG_CONFIG_PATH to find the .pc files.

 pkg-config

 opencv

 ];

 };

 }

 );

}

Or we could usenumtide/blueprint,
its spiritual successor.

LucPerkins’s dev-templateshave effectively
inlineda
version of this technique.

For a solution that isn’t part of Nix, but Nix-adjacent:devenvis a separate tool that is built on Nix (no longer
using the CppNix implementation, buttvix
actually),
but with its own .nix files.

## Tip: Keeping packages around

If you notice thatnix developor similar commands fetch packages despite theflake.locknot having changed, you can install the Flake into your profile todeclare it as a gcroot to
Nix:

% nix profile install .#devShells.x86_64-linux.default

But wait, isn’t that getting us into the same state aswith The Debian
Way? No! While OpenCV will remain available indefinitely if you
install the flake into your profile, there still is a layer of separation:
Within your system, OpenCV isn’t available, only when you start a development
shell withnix-shellornix develop.

## Conclusion

How do the four examples above compare? Here’s an overview:

Example

Boilerplate

Pinned?

System-dependent?

Ex 1
:
nix-shell -p …

😊

no

no

Ex 2
:
shell.nix

🙂

no

no

Ex 3
:
flake.nix

😲

yes

yes

Ex 4
: system-independent
flake.nix

🤨

yes

no

For personal one-off experiments, I usenix-shell.

Once the experiment works, I typically want to pin the dependencies, so I use aflake.nix.

If this is software that isn’t just versioned, but also published (or worked on
with multiple people/systems), I go through the effort of making it a
system-independentflake.nix.

I hope in the future, it will become easier to write a system-independent flake.

Despite the rough edges, I appreciate the reproducibility and control that Nix
gives me!

Did you like this
 post?Subscribe to this
 blog’s RSS feedto not miss any new posts!

I run a blog since 2005, spreading knowledge and experience for over 20 years! :)

If you want to support my work, you
 canbuy me a coffee.

Thank you for your support! ❤️

Table Of Contents
