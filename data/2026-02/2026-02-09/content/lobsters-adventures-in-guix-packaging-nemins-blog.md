---
title: Adventures in Guix Packaging - Nemin's Blog
url: https://nemin.hu/guix-packaging.html
site_name: lobsters
content_file: lobsters-adventures-in-guix-packaging-nemins-blog
fetched_at: '2026-02-09T06:00:28.993030'
original_url: https://nemin.hu/guix-packaging.html
date: '2026-02-09'
tags: lisp, nix
---

# Adventures in Guix Packaging

2026-02-01

Tags:programming, guix

## Table of Contents

* 1. Introduction
* 2. Baby steps
* 3. Enter WezTerm3.1. A mediocre first attempt3.2. A brief second attempt at packaging locally
* 3.1. A mediocre first attempt
* 3.2. A brief second attempt at packaging locally
* 4. Third time's the charm4.1. Setting things up4.2. Importing Cargo crates4.3. Patching Cargo.toml4.4. We have liftoff… Almost4.5. GPU maladies4.6. Finding fonts4.7. It's Vulkan, not Vulkan't4.8. A short aside: Committing is hard!
* 4.1. Setting things up
* 4.2. Importing Cargo crates
* 4.3. Patching Cargo.toml
* 4.4. We have liftoff… Almost
* 4.5. GPU maladies
* 4.6. Finding fonts
* 4.7. It's Vulkan, not Vulkan't
* 4.8. A short aside: Committing is hard!
* 5. And yet, some stuff is still better left to the Professionals
* 6. Conclusion

## 1.Introduction

Havingfreshly jumpedinto Guix System, it didn't take long for me to want to attempt packaging something for the distro.

Unlike the usual, "imperative" distributions, whose build scripts mostly interact with your system directly, Nix and Guix "recipes" provide a set of instructions for the build environment how it needs to compile your package's contents "from zero" and then where to place each of the resulting files.

My first choice wasGamescope, Valve's home-brewed compositor that enabled HDR gaming under Linux.1However, I quickly realized I bit bigger than I could chew. It took me less than an hour of trying to run into a wall that was (at least at that time) seemingly completely insurmountable.

The errors I received were somewhat vague, the system couldn't find the necessary dependencies, and I really wasn't sure what I was doing. In hindsight, it really wasn't the right approach and had I went about this project with more planning, it may have gone much better. Luckily dropping this thread allowed me to pick up a similarly interesting, but much more fruitful project, which I'd like to showcase to you in this article.

TL;DR:I spent about a week packagingWezTermand learning the ropes of being a Guix contributor along the way.

During the packaging process I stumble many times, only to stand back up and figure out a solution. I also explain some of my complaints about the peculiarities of the process, but also provide plenty of praise about of how much the system tries to enable you to do your job. Finally, I also touch on how positive the experience of the code review was.

If you just want to use WezTerm, do aguix pullandguix install wezterm.

## 2.Baby steps

Being somewhat disappointed in how quickly I failed with my initial attempt, I decided to instead start small and work my way up. To do this, I picked one of Gamescope's dependencies,OpenVR, andupdated its packageto its newest version.

This might sound impressive without context, but in reality it was little more than me just replacing a hash and a version number in a package definition someone else already wrote:

Listing 1:
My massive changes.
 diff --git a/gnu/packages/game-development.scm b/gnu/packages/game-development.scm

index 56f147f956..5cecbf6963 100644
---
a/gnu/packages/game-development.scm

+++
b/gnu/packages/game-development.scm

@@ -3294,7 +3294,7 @@
 (define-public instead

 (define-public openvr
 (package
 (name "openvr")

-
 (version "
1
.
26
.
7
")

+
 (version "
2
.
12
.
14
")

 (home-page "https://github.com/ValveSoftware/openvr/")
 (source
 (origin

@@ -3304,7 +3304,7 @@
 (define-public openvr

 (commit (string-append "v" version))))
 (file-name (git-file-name name version))
 (sha256

-
 (base32 "
09rvrja3pz6ggs41ra71p4dwjl4n
0
rpqrqw
8
jiy92xl33hhxbsmx
"))))

+
 (base32 "0
i85awq7w669j0x091chma
8
rcx1zqwn1j4v0d42bcjcvhqa6iv0v
"))))

 (build-system cmake-build-system)
 (arguments

 ;; No tests.

Even though the changes I made are trivial, to get here, I had to set up the development environment, I had to set up a fork of the repository, learn about the project's committing rules, how opening PR-s for Guix works, and how I could test my changes locally. (I'm only making a tally here, all of these will be elaborated on in more detail in the rest of the article.)

I'd really encourage anyone interested in how the packaging process works to seek out similar low hanging fruits to get down the basics in an environment where you have basically no chance of failing.

You walk away with knowledge and a basis to build more involved stuff and in turn some members of the community might just get an update to a package they've been waiting for or someone might get inspired to add yet another package that they couldn't until now.

## 3.Enter WezTerm

WezTermis one of the many GPU-accelerated terminal emulators out there, distinguishing itself with a fairly broad Lua-based configuration API and having tabs as a built-in feature among other things.

I admit, I haven't really used or interacted much with it previously. If I remember correctly, I tried it years ago before quickly moving on to other applications for my terminal needs, which begs the question:Why even bother to spend quite a few days on packaging it?

Well, I've basically been nerd-sniped into it. While I was still figuring out my own woes with Guix System's installation, I was frequently reading r/Guix in hopes of getting a bit further. And it just so happened that one of the posts on the front page at the time wasa pleafrom a prospective Guix user for a native WezTerm package for Guix. What I quickly discovered is that there was none. I couldn't even really find discussions about it. This felt like acall.

Note from the future:Along the post, you'll occasionally see little boxes like this one. While the main body of the article documents my thinking and justifications during development, in these I'll bring attention to parts where I've either did things in a not entirely idiomatic way or where there's a much better / easier solution.

The point of this post is less "How to write a 100% correct package definition that will get immediately merged into Guix" and more "What sort of journey would someone face, who hassomedeclarative packaging and Scheme knowledge, but is still quite new to the whole topic".

While the final code is indubitably much better than what I started with, I believe there is more merit in showcasing my iterative process instead of simply going through the merged package, as it doesn't really give any insight into how one would go about packaging something from zero.

### 3.1.A mediocre first attempt

To start out, I wanted to try to compile WezTerm in an ad-hoc environment to get an idea what it'd need. I cloned it usinggit clone https://github.com/wezterm/weztermand created a new shell environment usingguix shell rust cargo… Except this didn't actually work, as Guix immediately spit the following error:guix shell: error: cargo: unknown package.

Oh, right. With a cursory read of the Rust package, it quickly turned out Cargo isn't a separate package, but rather anoutputof Rust. Outputs in Guix are basically separate "sub-packages" of packages, that maintainers can use to group related artifacts together, without all of them having to be installed at the same time in case the user doesn't need them.

For instance most packaged libraries include both dynamic variants underout(which is the default output) and statically-linked ones understatic. With Rust, we have the following options (you can find these usingguix search):

name: rust
version: 1.85.1
outputs:
 + rust-src: [description missing]
 + tools: [description missing]
 + cargo: [description missing]
 + out: everything else

For our purposes, we needout, which contains the Rust compilerrustc, and we also needcargo. To instruct the shell to load both, the command we actually need isguix shell rust rust:cargo. We could have also explicitly usedrust:outforrustc, but if we leave it out, the shell uses it by default anyway.

Armed with the right toolchain, I issued a naivecargo buildand for a while things seemed to be in order, only to suddenly come to a crashing halt with the following error:

error occurred in cc-rs: failed to find tool "cc":
No such file or directory (os error 2)

It might come as a surprise, but due to the expectation that most things will be handled using declarative configuration, Guix System doesn't set theCCenvironment variable (norCXX, though we won't be using that in this project).

In fact, there isn't even any C compiler toolchain installed by default. This causes any programs that expect Autoconf/Makefile-like conventions to not be able to compile stuff. We can really easily solve it by addinggcc-toolchainto our shell and settingCCtogcc:

guix shell rust rust:cargo gcc-toolchain

export

CC
=gcc
cargo build

Moments later we experience a new error (which, just like before, I'll abridge by a lot, because it's several pages long):

Could not find openssl via pkg-config:
Could not run `PKG_CONFIG_ALLOW_SYSTEM_CFLAGS=1 pkg-config --libs --cflags openssl`
The pkg-config command could not be found.

The issue here is twofold, though both come from the same source. The compiler is looking for OpenSSL usingpkg-config, but our environment doesn't contain either. While we could do what we previously did and exit the shell, addpkg-configandopenssl, go back, call Cargo, and fail again at the next missing dependency, there is a slightly better way.

Note from the future:Look, I'll be honest, the first time I did this process, I was actually doing this completely "manually" as described above. That is to say, I tried compiling and when it eventually failed with an error about a missing dependency, I just added it to the list, rinse and repeat.

It's a horribly inefficient method and I didn't want to drag this post down by emulating it.

Though WezTerm has no Guix package (we're working on it right now!), it does come with aNix flakeand, though Nix and Guix have diverged quite a bit, it's still very helpful to see the list of packages spelled out for us by someone else:

nativeBuildInputs
 =

with
 pkgs;
 [
 installShellFiles
 ncurses
# tic for terminfo

 pkg-config
 python3
 ]
 ++ lib.optional stdenv.isDarwin perl;

buildInputs
 =

with
 pkgs;
 [
 fontconfig
 openssl
 zlib
 ]
 ++ lib.optionals stdenv.isLinux [
 libxkbcommon
 wayland

 xorg.libX11
 xorg.libxcb
 xorg.xcbutil
 xorg.xcbutilimage
 xorg.xcbutilkeysyms
 xorg.xcbutilwm
# contains xcb-ewmh among others

 ]
 ++ lib.optionals stdenv.isDarwin ([
 libiconv
 ]);

Obviously we cannot use this 1:1 as the two systems have different packaging conventions, but we can at least extract a good first approximation of the dependency list:

guix shell rust rust:cargo gcc-toolchain pkg-config openssl wayland libx11
\

 libxcb xcb-util libxkbcommon xcb-util-image freetype fontconfig

export

CC
=gcc
cargo build --bin wezterm

And, guess what, the application builds. Victory! Or so we think until we actually try to run it usingcargo run --bin wezterm:

ERROR wezterm_gui::frontend > Failed to create window: with_egl_lib failed:
libEGL.so.1: libEGL.so.1: cannot open shared object file: No such file or directory,
libEGL.so: libEGL.so: cannot open shared object file: No such file or directory,
libEGL.so.1: libEGL.so.1: cannot open shared object file: No such file or directory,
libEGL.so: libEGL.so: cannot open shared object file: No such file or directory

Bummer. WezTerm is a GPU-accelerated terminal emulator, so it (unsurprisingly) needs to communicate with our GPU. Under NVIDIA , this happens with the help of a library calledlibEGL2, which our binary cannot locate without some additional help. The reason for this is that Guix isn't using the standardLinux filesystem hierarchy, solibEGLis nowhere to be found on the list of places the library loader checks by default.

The "fix" I used to circumvent this is really ugly, but for a quick attempt it sufficed. Firstly, I needed to figure out wherelibEGL.soeven is. Thankfully all this took was a simpleguix locate libEGL.so(this command is case-sensitive, I learned it the hard way), which spits out a list such as this:

fhs-union-32@0.0 /gnu/store/wr6kq2ixxcnh4nidg64ivsns19k7ynnn-fhs-union-32-0.0/lib/libEGL.so
fhs-union-64@0.0 /gnu/store/9jn31ksjz3frkhwdk5f72s65lrn3gbs7-fhs-union-64-0.0/lib/libEGL.so
mesa@25.2.3 /gnu/store/4kp4rn5vnnaj57464k72wqpg45k45x56-nvda-580.12/lib/libEGL.so
nvda@580.12 /gnu/store/d7vln3cxysi04wf7p8nzwgwabjysznjd-nvda-580.12/lib/libEGL.so
libglvnd@1.7.0 /gnu/store/qhc0y0xzmdmh38bpr9yv2il8alrv5l4g-libglvnd-1.7.0/lib/libEGL.so
mesa@21.3.8 /gnu/store/7rn2s4ip6926sdn8h23qbdyhsr4lj4xk-mesa-21.3.8/lib/libEGL.so

As you can see, due to the way Guix works, multiple versions of the library can coexist without conflicting with each other. As I'm running an NVIDIA card, I picked the line fornvda. Next, I had to set the special environment variableLD_PRELOADto this file's path and then callwezterm. What this does is instruct the dynamic library loader to add the contents of the environment variable to its load path3and thus the library is finally visible to the application.

LD_PRELOAD
=/gnu/store/d7vln3cxysi04wf7p8nzwgwabjysznjd-nvda-580.12/lib/libEGL.so
\

 ./target/debug/wezterm

Et voila,we have WezTerm running. Reddit threadsolved. Well, kind of. Our victory is a bit of a hollow one. While we did compel Cargo to build the terminal and it technically works, we have not made a package. Guix isn't aware of WezTerm and anyone else who wants to build the application has to follow these haphazard steps, including overriding a "potentially dangerous" environment variable.

### 3.2.A brief second attempt at packaging locally

To turn our fickle experiment into a proper package, we need to create a build recipe, which we can later integrate into theguix/guixCodeberg repository. The customary filename for such recipes in Guix is, perhaps unsurprisingly,guix.scm. Inside this file you're expected to return a(package ...)form as your final value, which Guix can then process and turn into a derivation4for you.

 1:
(
define-module
 (
wezterm
))

 2:

 3:
(
use-modules
 (guix git)

 4:
 (guix git-download)

 5:
 (guix packages)

 6:
 ((guix licenses)
#:prefix
 license:)

 7:
 (guix build-system cargo)

 8:
 (gnu packages)

 9:
 (gnu packages commencement)

10:
 (gnu packages tls)

11:
 (gnu packages freedesktop)

12:
 (gnu packages xorg)

13:
 (gnu packages xdisorg)

14:
 (gnu packages fontutils)

15:
 (gnu packages autotools)

16:
 (gnu packages guile)

17:
 (gnu packages pkg-config)

18:
 (gnu packages sdl)

19:
 (gnu packages texinfo))

20:

21:
(package

22:
 (name
"wezterm"
)

23:
 (version
"05343b3"
)

24:
 (home-page
"https://wezterm.org/"
)

25:
 (synopsis
"TODO"
)

26:
 (description
"TODO"
)

27:
 (license license:expat)

28:
 (source (git-checkout (url
"https://github.com/wezterm/wezterm"
)

29:
 (commit version)))

30:
 (inputs (append (list gcc-toolchain pkg-config openssl wayland

31:
 libx11 libxcb xcb-util libxkbcommon xcb-util-image

32:
 freetype fontconfig)))

33:
 (build-system cargo-build-system))

Let's go through our code, section by section. We begin by declaring a module for our package. This is not strictly necessary, but it's common practice with Guile code and (as you'll soon see) it won't really matter in the long run anyway. Next we import a bunch of utilities and packages. A common rule of thumb is that packages underguixare utilities, whilegnu packagesare packages.

We import stuff like methods for importing from a Git repository, definitions of software licenses (more on that below), and Guix's Cargo-based builder preset. The observant might notice that wedon'tpull inrust,rust:cargo, andgcc-toolchain. All of these are handled by the preset.

Next comes the main package definition. We declare some static metadata, such as the name of the package, its version number (I'm using the current commit of the repository, as WezTerm hasn't had a release since 2024), the project's website, and we leave the synopsis and description empty for now, as I'd rather first have the package working before wasting time on bookkeeping busywork.

Finally we set the package's license. In Guix (and Nix too), licenses aren't simple text fields, so we can't simply say"MIT"and move on with our lives. Rather they are objects of their own. This both allows recording any necessary to fully specify the license and also removes a lot of guesswork from the packagers' workflow such as:

* "Do I specify 'MIT'? Or 'Expat'? Or 'MIT/Expat'?"
* "Is the field case sensitive?"
* "Is it 'GPL-3' or 'GPL3' or maybe 'GPLv3'?"
* And so on and so forth.

To access these license objects, we need to pull in the(guix licenses)module and specify from it the exact variant we need. In our case this islicense:expat, the MIT license's other name. As you can see, in the imports section I specifiedlicense:as the license module's prefix. This means all the identifiers exported from this module are automatically renamed to containlicense:in the front. This is done to prevent overshadowing unrelated names and prefixing licenses this way is an idiomatic practice in Guix.

This is followed by the actually interesting stuff. First we declare the source of our package's code. This can be many things, an archive downloaded from the Internet, a Git repository like we see in this case, or even a local folder as seen in thisexcellent tutorial. We declare our commit to be the same as what we set for our version, i.e. the Git commit with the (short) ID05343b3.

Next we declare our "inputs", these are all the packages that we either need to use to build our package or we need at runtime. Note the vagueness of the word "use" here: Inputs may not just be source code dependencies. For instance, as with the manual method,pkg-configis used to find other sources' locations and won't actually be part of the final executable. But we might also include tools that generate files. Or we might request assets, like fonts. It's best to think of inputs as not just the ingredients, but the entire kitchen supply.

After that comes the build system. Just like our source, this too can bemany thingsand it is what primarily decides what our build process is going to look like. Since we're trying to make a Rust package, we usecargo-build-system, which itself is based on thegnu-build-system(which is a smarter codification of the good old./configure,make,make installritual), except with all the GNU-specific build tools replaced with calls to Cargo.

Well, let's give it a shot. Surely, things cannot be much more complex than this.

Listing 2:
Crash and burn…
error: failed to get `finl_unicode` as a dependency of package `termwiz v0.24.0 (/tmp/guix-build-wezterm-05343b3.drv-0/source/termwiz)`

Caused by:
 failed to load source for dependency `finl_unicode`

Caused by:
 Unable to update https://github.com/wez/finl_unicode.git?branch=no_std

Caused by:
 can't checkout from 'https://github.com/wez/finl_unicode.git': you are in the offline mode (--offline)
error: in phase 'build': uncaught exception:
%exception #<&invoke-error program: "cargo" arguments: ("build" "--offline" "-j" "24" "--release" "-p" "wezterm-gui" "--features" "distro-defaults") exit-status: 101 term-signal: #f stop-signal: #f>
phase `build' failed after 0.0 seconds
command "cargo" "build" "--offline" "-j" "24" "--release" "-p" "wezterm-gui" "--features" "distro-defaults" failed with status 101
build process 18 exited with status 256
builder for `/gnu/store/nllax38xh9v0hcsc3g9vviw5mqnrj5x0-wezterm-05343b3.drv' failed with exit code 1
build of /gnu/store/nllax38xh9v0hcsc3g9vviw5mqnrj5x0-wezterm-05343b3.drv failed

Things can't be as simple as we'd like, huh?

## 4.Third time's the charm

The main reason we failed is because Guix is very particular about the way it allows source code to be fetched5and, though Cargo has an ecosystem of its own, Guix wants to have the final say. If packages, such as the previously seenfinl_unicodearen't known by Guix, then even though Cargo could fetch it for us, the build system will refuse to proceed.

The good news is that Guix has built in features to allow mass-importing crates, so we don't have to manually go through every single of WezTerm's dozen crates. The bad news is that, for this to work, you need to be working inside Guix's primary repository or else you're unleashing an unreasonable amount of extra work on yourself. Since our end goal is to upstream the package definition anyway, it really is the right choice to just bite the bullet and do it properly.

So, back totabula rasa, let's create a package inside the actual Guix package repository.

### 4.1.Setting things up

I'm going to assume at least a bit of Git knowledge, as this post will be long enough as-is without starting from the very basics. Due to my previous tiny contribution with OpenVR, I already had a fork repository ofguix/guix, so that's one hurdle down. Next, we do the usual, update themaster6branch, create a new branch, switch to it, then prepare our working environment:

git pull
git switch --create add-wezterm
guix shell -D guix -CPWN
make

The first twogitcommands are fairly trivial, but the third command is worth talking about a little. The interesting thing about Guix development is that it happens 90% inside Guix itself! Isn't that cool? By issuingguix shell -D guix -CPWN, we are:

* -C: are transported into a container, a fully isolated environment, in which only the source tree is available,
* -D guix: with the development inputs of theguixpacakge included,
* -P: with the profile initialized to the source tree's environment,
* -W: with theguixexecutable available,
* -N: and finally we request network access.

But, before we can throw ourselves into writing our package with wild abandon, we have one more preliminary thing to take care of first. By issuingmake7, the development environment does several things at once:

* Itcompilesall existing Scheme files into.gofiles, which aren'tGolangsource files, but rather Guile byte-code. This speeds up execution as instead of interpreting source code, Guile can work based on pre-chewed binary data,
* It compiles all documentation. To our purposes this isn't hugely relevant, but it's a one-time cost, so there's not much point in figuring out elaborate ways to avoid it,
* Finally, and most importantly, it places a new script into our workspace namedpre-inst-env. The name stands for "[run with] pre-installation environment" and it is the primary driver of our Code->Compile->Test loop.By prepending all ourguixinvocations with./pre-inst-env, we can instruct Guix to use the workspace package registry as its source and thus we can build and test our package without the horribly slow process of manually doingguix pullon our work directory andguix build <package>.What's even better is that this works even outside the container, so we can use all our usual tools while testing or build in the restricted environment to make sure we're not introducing any external dependencies.

After a couple minutes of wait, our workspace is finally ready for action. Now we can finally handle the actual Guix stuff. First order of business is figuring out where even our package should go. The Guix repository's folder structure is logical, but it is still occasionally non-trivial to figure out where some packages might be located.

A good rule of thumb is that usually things go into general categories (e.g.emulators.scm), but if a set of packages only make sense together (an example beingdjango.scmfor all the PythonDjangostuff out there), it can go into a category, and thus, a new file of its own. For us, there are two possible candidates:

* rust-apps, whose purpose I'm still not 100% sure about, since the only thing that connects the stuff inside it seems to be that it's all Rust-based applications,
* andterminals.scm, which is for terminal emulators. This is the one I ultimately went with, as it already hadAlacrittyinside, which is also a Rust-based terminal emulator, just like WezTerm.

So, let's just plop our previous package definition (extended a little bit) into this file and give it a whirl.

(
define-public

wezterm

 (package
 (name
"wezterm"
)
 (version
"05343b387085842b434d267f91b6b0ec157e4331"
)
 (source
 (origin
 (method git-fetch)
 (file-name
"wezterm"
)
 (uri (git-reference
 (url
"https://github.com/wezterm/wezterm"
)
 (recursive? #t)
 (commit version)))
 (sha256
 (base32
"0q3f1y3bx3g2k21yzp6wkws6kyxsmk4pscmvd8gqmjbbss8az9ap"
))))
 (native-inputs (list pkg-config))
 (inputs (append (cargo-inputs 'wezterm)
 (list openssl wayland libx11
 libxcb xcb-util xcb-imdkit
 libxkbcommon xcb-util-image
 freetype fontconfig libssh2
 libgit2 sqlite `(,zstd
"lib"
)
 mesa)))
 (build-system cargo-build-system)
 (home-page
"https://wezterm.org/"
)
 (synopsis
"Powerful cross-platform terminal emulator and multiplexer"
)
 (description

"A GPU-accelerated cross-platform terminal emulator and
multiplexer written by wez and implemented in Rust. Features:

@itemize
@item Runs on Linux, macOS, Windows 10, FreeBSD and NetBSD,
@item Multiplex terminal panes, tabs and windows on local and
remote hosts, with native mouse and scrollback,
@item Ligatures, Color Emoji and font fallback, with true color
and dynamic color schemes,
@item Hyperlinks.
@end itemize
"
)
 (license license:expat)))

There's only really three things of note:

* Instead of simply doing a "bare"packageform, we wrap our package definition into adefine-publicform. This is how we ensure that multiple package definitions can coexist in a single file.
* Secondly, the package source form was rewritten to useorigininstead, which allows for a lot more flexibility in how we download stuff from the net.Among other things, it allows us to rewrite parts of the source, delete unnecessary files, create wholly new files, and (as can be seen here) it also allows us to cryptographically check whether the source files we get really are what we expect them to be. Packages meant for the main Guix repo all must have their hash checked, so adding it wasn't merely my frivolousness.Note from the future:As it turns out, as helpful as this step was during development, it is entirely possible to make WezTerm work without recursive cloning and, in fact, this option is only allowed in extraordinary cases.I also enabled recursive cloning of the repo as there are some submodules involved and once we're past the source-fetching stage, the network is disabled and we wouldn't be able to download them anymore.
* Thirdly you may wonder about the weird`(,zstd "lib")form in our inputs. As inputs are actual other packages, not strings-based specifications, we can no longer do the previous "package:output" way of referring to alternative outputs.For that, we need to create a two-element list, where the first is the dependency and the second is the textual name of the output. So, really, this is just the packaging way of sayingzstd:lib.

### 4.2.Importing Cargo crates

Still, with all this work, if we run this using./pre-inst-env guix build wezterm, we will be met with the previous error about Cargo not being able to fetchfinl_unicode. Which shouldn't be surprising, sinceas mentionedearlier we haven't imported our Cargo dependencies into Guix yet.

To do this, we will need to issueguix importin our previously checked out WezTerm Git repository in the following way:

guix import -i <path to Guix repo>/gnu/packages/rust-crates.scm
\

 crate -f <path to Git repo>/Cargo.lock
\

 wezterm

What this does is go through every individual Cargo dependency in theCargo.lockfile and compares it to the list found inrust-crates.scm. If a matching entry is found, nothing is done, if not, the importer adds a new entry to the file. If a crate has a matching crates.io page, an entry such as this is generated:

(
define

rust-libssh-rs-0.3.6

 (crate-source
"libssh-rs"

"0.3.6"


"11f6fj59dqpy7n0g74s7vnnyrbpxbrcyxhnrvfnsb5dvsq8f2rih"
))

If not, however, then we get a slightly bigger variant:

(
define

rust-finl-unicode-1.3.0.a1892f2


;;
TODO REVIEW: Define standalone package if this is a workspace.

 (origin
 (method git-fetch)
 (uri (git-reference (url
"https://github.com/wez/finl_unicode.git"
)
 (commit
"a1892f26245529f2ef3877a9ebd610c96cec07a6"
)))
 (file-name (git-file-name
"rust-finl-unicode"

"1.3.0.a1892f2"
))
 (sha256 (base32
"0g9lqwrzm7ca54vlq8sgix3wvbsxwp7glkx3dzjdd591grfbmi6z"
))))

It bears resemblance to our own package'soriginfield and it also has a foreboding comment about how we need to review this generated package to check if it's a "workspace". Elaborating onwhat a workspace isin Rust is beyond the scope of this article, but the long story short is that a single Cargo project may contain multiple, related subprojects and the importer is not able to untangle these by itself.

If you're packaging something that depends on such a project, you must manually make sure every single subproject gets its own definition, which call back to the main workspace.finl_unicodeisn't such a project, however, so we can safely ignore the warning for now.

Where we cannot ignore the comment, however, is with the bindings for OpenSSL,rust-openssl-sys-0.9.111. If we were to leave things as-is, we'd soon find that our project does not build due to not findingopenssl-src.

Thankfully, we don't have to figure it out how to fix this issue ourselves, as the package already has several other versions in the Guix repo. We simply have to copy someone else's solution and we're one step closer to making WezTerm build:

diff --git a/gnu/packages/rust-crates.scm b/gnu/packages/rust-crates.scm
index 74fba63cd8..213882b4a2 100644
---
a/gnu/packages/rust-crates.scm

+++
b/gnu/packages/rust-crates.scm

@@ -13605,9 +13605,19 @@
 (define rust-openssl-sys-0.9.110

 (copy-file "Cargo.toml.orig" "Cargo.toml"))))

 (define rust-openssl-sys-0.9.111

-
 ;; TODO REVIEW: Check bundled sources.

 (crate-source "openssl-sys" "0.9.111"

-
 "08f3mpsabivfi3fd0qv9231qidqy68lr8a4qi32y6xda43av5jl2"))

+
 "08f3mpsabivfi3fd0qv9231qidqy68lr8a4qi32y6xda43av5jl2"

+
 #:snippet

+
 #~(begin

+
 ;; Remove dependency on boringssl and vendor openssl source.

+
 (substitute* "Cargo.toml.orig"

+
 (("vendored = .*") "vendored = []\n")

+
 ((".*bssl.*") "")

+
 ((".*openssl-src.*") "")

+
 ;; Allow any version of bindgen.

+
 (("(bindgen = \\{ version =) \".*\"," _ bindgen)

+
 (string-append bindgen "\"*\",")))

+ (copy-file "Cargo.toml.orig" "Cargo.toml"))))

Once the importer has gone through every dependency, it also generates a lookup table entry inrust-crates.scmin the form ofpackage-name => (list <list-of-dependencies>). This is ultimately the mechanism that pairs user defined Rust Guix packages to their Cargo defined dependencies. For instance, since we enteredwezterm8in ourcargo importquery, we get the following list:

(wezterm =>
 (list rust-addr2line-0.25.1
 rust-adler-1.0.2
 rust-adler2-2.0.1
 rust-adler32-1.2.0
 rust-ahash-0.8.12
 rust-aho-corasick-1.1.4
 rust-aligned-vec-0.6.4
 ... and like 600 more crates ...
 ))

And somewhere in this list,finl_unicodecan also be found. Finally, we are able to provide all our dependencies to the build system:

Listing 3:
The build system has access to all the crates that we automagically imported from the Cargo lockfile.
;;
cons* takes an arbitrary amount of elements and a list and prepends the former to the latter.

;;
E.g. (cons* 'a 'b 'c '(d e)) => (a b c d e)

(inputs (cons*
 openssl
 wayland
 libx11
 ... our previous list of packages ...
 (cargo-inputs 'wezterm)))

We issue./pre-inst-env guix build wezterm… and run into the same error. What gives?

### 4.3.Patching Cargo.toml

Though the code itself is fairly trivial, understanding the solution to this issue was perhaps the most difficult part of the entire process to me. Largely because there is almost zero indication what and how you need to do, and the docsbarely touch uponthe existence of this issue and its fix either. I had to resort to reading other packages' definitions, which worked, but definitely wasn't the smooth-sailing as things had been up to this point.

To finally reveal this hidden menace that has been keeping us from compiling this poor application till now, let's take a look at two different dependencies from WezTerm'sCargo.toml:

finl_unicode
 = { version =
"1.3"
, git=
"https://github.com/wez/finl_unicode.git"
, branch=
"no_std"
 , default-features=
false
, features=[
"categories"
,
"grapheme_clusters"
]}

fixed
 =
"1.23"

For dependencies likefixed, there is no issue, the build system can match them with their imported package no-problem. However, for some reason that I still don't quite understand, if there is agitfield in the dependency list, then that completely breaks the proces, as Cargo will always try to download it from the internet, which then fails due to the build environment not having network access.

The solution?

finl_unicode
 = { version =
"1.3"
, default-features=
false
, features=[
"categories"
,
"grapheme_clusters"
]}

Yep. That's it. We just have to instruct Guix to rewrite this one line (well, actually two, because there's two such dependencies in the project, but I'll not bore you with the exact same process) and everything else will magically work.

To do this, we introduce a new section to our package definition,arguments. The role of this field is to override certain aspects of the build system preset, such as the build flags or what so-called "build phases" we wish to execute on the code.

A build phase can be practically anything from setting environment variables, to compiling code, to editing files. We would like to do the last one, so let's introduce a new build phase:

(arguments
 (list

#:phases

 #~(modify-phases %standard-phases
 (add-after 'unpack 'use-guix-vendored-dependencies
 (
lambda
 _
 (substitute*
"Cargo.toml"

 ((
", git.*default-features"
)

", default-features"
)
 ((
", git.*, rev.*}"
)

;;
This is added to ensure a different dependency


;;
uses libraries provided by the inputs instead


;;
of relying on bundled files.


", features=[\"use-system-lib\"]}"
)))))))

This code adds a new phase afterunpack(which is the phase responsible for extracting the actually usable files and folders from ourorigin) nameduse-guix-vendored-dependencies. The name of the phase that we're adding is arbitrary, but you're expected to pick something informative and truthful, so please don't trydo-stufforthing.

The magic happens insidesubstitute*, which takes a filename and a list ofregexp => replacementpairs, and then executes the replacements. It's kind of like having a lispysedin your arsenal.

Careful readers may have noticed the weird#~symbol in front of themodify-phasesfunction call. This is a Guix-exclusive extension to Scheme's syntax, calledG-expressions(abbreviated as "gexp").

Their job is to facilitate working with files as data, therefore whenever we need to directly affect our source code (be that creation, deletion, or modification) or call out into the operating system, we need to do so inside a gexp. This isn't the only place where we'll need to do so, so I'll call into attention when it happens.

In more important news, if we were to issue./pre-inst-env guix build weztermnow, we'd find that the package actually builds… before failing again:

error: crates-io is replaced with non-remote-registry source dir /tmp/guix-build-wezterm-05343b387085842b434d267f91b6b0ec157e4331.drv-0/source/guix-vendor;
include `--registry crates-io` to use crates.io
error: in phase 'package': uncaught exception:
%exception #<&invoke-error program: "cargo" arguments: ("package" "--offline" "--no-metadata" "--no-verify") exit-status: 101 term-signal: #f stop-signal: #f>
phase `package' failed after 0.1 seconds
command "cargo" "package" "--offline" "--no-metadata" "--no-verify" failed with status 101
build process 18 exited with status 256

The actual error is a little vague, but the gist is that by default thecargo-build-systemattemptsto install the sources of all the dependencies we used. For us, this is neither desirable, nor does it actually allow the build to finish, so by adding the following to our arguments, we disable it (along with tests9):

diff --git a/gnu/packages/terminals.scm b/gnu/packages/terminals.scm
index 476e2b743e..84f52b24f8 100644
---
a/gnu/packages/terminals.scm

+++
b/gnu/packages/terminals.scm

@@ -1702,6 +1702,8 @@
 (define-public wezterm

 (build-system cargo-build-system)
 (arguments
 (list

+
 #:install-source? #f

+
 #:tests? #f

 #:phases
 #~(modify-phases %standard-phases

 (add-after 'unpack 'use-guix-vendored-dependencies

Call build again, and…

### 4.4.We have liftoff… Almost

No errors. Our build was successful.

successfully built /gnu/store/h8d2igkg4vlg687ixgj6hizyd4gbzl64-wezterm-05343b387085842b434d267f91b6b0ec157e4331.drv
/gnu/store/h99jlsdism6jxn3x02fv7jig61r6ydv2-wezterm-05343b387085842b434d267f91b6b0ec157e4331

Let's celebrate by starting a shell that contains our newly built terminal in it and start it up:

guix shell wezterm -- wezterm
guix shell: error: wezterm: command not found

Sadly we're still no quite there, but there is only one step separating us from the same spot as we were with the original "ad-hoc" implementation. If we list the files in our built derivation, we would find that it doesn't contain anything useful:

/gnu/store/h99jlsdism6jxn3x02fv7jig61r6ydv2-wezterm-05343b387085842b434d267f91b6b0ec157e4331
└── share
 └── doc
 └── wezterm-05343b387085842b434d267f91b6b0ec157e4331
 ├── ANGLE.md
 ├── LICENSE.md
 └── README.md

What happened? Simply put, we only told Guix to build our executables, not that we actuallyneedthem. The built package contains several different binaries, of which we're primarily interested in one:wezterm-gui.

To access it, we will a phase calledinstallwhich is supposed to put everything in its rightful place. Let's modifyargumentsand override it to install our file:

diff --git a/gnu/packages/terminals.scm b/gnu/packages/terminals.scm
index 84f52b24f8..8f54a79dbe 100644
---
a/gnu/packages/terminals.scm

+++
b/gnu/packages/terminals.scm

@@ -1712,7 +1712,16 @@
 (define-public wezterm

 ((", git.*default-features")
 ", default-features")
 ((", git.*, rev.*}")

-
 ", features=[\"use-system-lib\"]}")))))))

+
 ", features=[\"use-system-lib\"]}"))))

+
 (replace 'install

+
 (lambda* (#:key inputs native-inputs #:allow-other-keys)

+
 ;; Binaries

+
 (with-directory-excursion "target/release"

+
 (for-each

+
 (lambda (name) (install-file name (string-append #$output "/bin")))

+
 '("wezterm" "wezterm-gui"

+
 "wezterm-mux-server"

+
 "strip-ansi-escapes"))))))))

 (home-page "https://wezterm.org/")

Note from the future:Binaries aren't the only thing that need to be installed for a package like this. You also need to copy over stuff like icons,.desktopfiles, and any other various assets a package might need.

I abridged the package definition here quite a bit, because much of the process is just more of the same and I see very little educational value in repeating 95% the same code.

This snippet of code enters./target/release, which is the folder where Cargo places our compiled binaries, walks through our supplied list of executable names and copies each to#$output/bin. In Bash terms, you could think of this ascp ./target/release/wezterm $OUTPUT/bin/.

You may wonder what#$outputeven is. It's actually two separate things combined:

#$is a so-calledreader extensionspecific to Guix. Reader extensions are a user-defined extension to the usual syntax extensions, which are in turn special characters that affect the behavior of Lispy languages and are mostly used because spelling out the entire form they shorten would be quite unwieldy.

Listing 4:
Some examples of common syntax extensions to all Lispy languages.
(+ 1 2)
;;
=> 3 (Form is evaluated as usual)

'(+ 1 2)
;;
=> (+ 1 2) (Form is "quoted" and returned as-is)

`(+ 1 2)
;;
=> (+ 1 2) (Form is "quasiquoted" and returned as-is)

`(+ 1 ,(+ 1 1))
;;
=> (+ 1 2) (Form is "quasiquoted", the third element is "unquoted")

In our case#$is a lot like,(also known asunquote), which is used in conjunction with`(quasiquote). It allows us to "unquote" (i.e. execute) code inside agexp, which itself acts as sort of a quasiquote (i.e. a form that isn't evaluated by default, only the parts that are explicitly unquoted). For more information about the concept, Guile has anentire pagededicated to it.

Meanwhile,outputis simply a variable provided implicitly in our install phase, that points to the directory where our derivation will be built into. This folder acts similarly to a filesystem root folder (what you may know as/), but it only contains files that either we explicitly placed into it or are automatically copied by the build phases.

When we install a package, the files from its output are made available in our general environment. You can see this by callingls /run/current-system/profile/bin, which will list out most10of the binaries available to you in the current environment. One thing of note is that none of these files here are the actual executables, but rather symlinks to binaries found in the Guix store, which is the organized collection of all built derivations.

Circling back to our package, now that our executables are copied over to the output's bin folder, they will be available to use if we were to install the package. Let's do so:

guix shell wezterm
wezterm

This time the terminal runs, but then immediately crashes…

### 4.5.GPU maladies

Note from the future:The method shown below might be a viable path for some particularly stubborn libraries, however, it isnota good first approach. As it turns out in this case we can get rid of this entire build phase by simply instructing Cargo to linklibEGLusing theRUSTFLAGSenvironment variable.

If you're thinking of making your own package, please be sure to check whether you can simply instruct your linker before you attempt to hack apart the code you're working on.

21:59:33.533 ERROR wezterm_gui::frontend > Failed to create window: with_egl_lib failed:
libEGL.so.1: libEGL.so.1: cannot open shared object file: No such file or directory,
libEGL.so: libEGL.so: cannot open shared object file: No such file or directory,
libEGL.so.1: libEGL.so.1: cannot open shared object file: No such file or directory,
libEGL.so: libEGL.so: cannot open shared object file: No such file or directory

You might remember, that we'veseenthis error already. This time, however, we'll do it right and instead of relying on a random build string extracted from a command, we'll rely on our build inputs.

To figure out what we're supposed to do, let'sgrepforlibEGL.soto find all the places the library is used. There are some irrelevant results, but there is some promising code under./window/src/egl.rs. The definition of the function namedwith_egl_libreveals how exactly we're trying to load the library:

fn

with_egl_lib
<
F
:
FnMut
(
EglWrapper
) ->
anyhow
::
Result
<
Self
>>(

mut

func
:
F
,
) ->
anyhow
::
Result
<
Self
> {

let

mut

paths
:
Vec
<
std
::
path
::
PathBuf
> =
vec!
[

#[cfg(target_os =
"windows"
)]


"libEGL.dll"
.into(),

#[cfg(target_os =
"windows"
)]


"atioglxx.dll"
.into(),

#[cfg(all(not(target_os =
"macos"
), not(target_os =
"windows"
)))]


"libEGL.so.1"
.into(),

#[cfg(all(not(target_os =
"macos"
), not(target_os =
"windows"
)))]


"libEGL.so"
.into(),
 ];

This piece of code tries to simply look forlibEGL.sowithout any path associated with it. Therefore the dynamic library loader will try all known search places. However, since Guix doesn't put libraries in the normal search paths, this will fail.

So, what if we were to replace this string by an exact path to the library provided by one of our inputs? Turns out that's exactly what we need to do.

As you might have guessed, we need yet another phase:

diff --git a/gnu/packages/terminals.scm b/gnu/packages/terminals.scm
index f7eb633624..34758f238e 100644
---
a/gnu/packages/terminals.scm

+++
b/gnu/packages/terminals.scm

@@ -1713,6 +1713,10 @@
 (define-public wezterm

 ", default-features")
 ((", git.*, rev.*}")
 ", features=[\"use-system-lib\"]}"))))

+
 (add-after 'unpack 'fix-libegl-so

+
 (lambda _

+
 (substitute* "./window/src/egl.rs"

+
 (("libEGL.so") (string-append #$mesa "/lib/libEGL.so")))))

 (replace 'install
 (lambda* (#:key inputs native-inputs #:allow-other-keys)

 ;; Binaries

Let's rebuild and run our package again.

Success! Well, mostly. If we really wanted to, we could stop here. Our package technically "works" and can be installed. However, in its current state, it'd never be accepted into the registry for two main reasons (and a myriad of small ones, see thefinal partof this story).

### 4.6.Finding fonts

Note from the future:WezTerm actually bundlesfour different fonts. During the development of the package I only packaged JetBrains Mono and Roboto, because those two are considered vital for the terminal to function.

However, by the time the package was merged, one of the contributors added the other two fonts too and replaced this entire phase with much more elegant code.

Of these two big issues, one is that we are still relying on fonts bundled by the source repository. This is a no-go, especially since most of the fonts we wish to use are already packaged in Guix.

By looking into the source files, we find that WezTerm's font-loading code is found inwezterm-font/src/parser.rs:

/// In case the user has a broken configuration, or no configuration,
/// we bundle JetBrains Mono and Noto Color Emoji to act as reasonably
/// sane fallback fonts.
/// This function loads those.

pub
(
crate
)
fn

load_built_in_fonts
(
font_info
:
&
mut

Vec
<
ParsedFont
>) ->
anyhow
::
Result
<()> {

#[allow(unused_macros)]


macro_rules!
 font {
 (
$font
:literal) => {
 (
include_bytes!
($font)
as

&
'
static
 [
u8
], $font)
 };
 }

let

lib
 =
crate
::
ftwrap
::
Library
::new()
?
;


let

built_ins
:
&
[
&
[(
&
[
u8
],
&
str
)]] =
&
[

#[cfg(any(test, feature =
"vendor-jetbrains"
))]


&
[

font!
(
"../../assets/fonts/JetBrainsMono-BoldItalic.ttf"
),

font!
(
"../../assets/fonts/JetBrainsMono-Bold.ttf"
),

font!
(
"../../assets/fonts/JetBrainsMono-ExtraBoldItalic.ttf"
),

font!
(
"../../assets/fonts/JetBrainsMono-ExtraBold.ttf"
),

font!
(
"../../assets/fonts/JetBrainsMono-ExtraLightItalic.ttf"
),

font!
(
"../../assets/fonts/JetBrainsMono-ExtraLight.ttf"
),

font!
(
"../../assets/fonts/JetBrainsMono-Italic.ttf"
),

font!
(
"../../assets/fonts/JetBrainsMono-LightItalic.ttf"
),

font!
(
"../../assets/fonts/JetBrainsMono-Light.ttf"
),

font!
(
"../../assets/fonts/JetBrainsMono-MediumItalic.ttf"
),

font!
(
"../../assets/fonts/JetBrainsMono-Medium.ttf"
),

font!
(
"../../assets/fonts/JetBrainsMono-Regular.ttf"
),

font!
(
"../../assets/fonts/JetBrainsMono-SemiBoldItalic.ttf"
),

font!
(
"../../assets/fonts/JetBrainsMono-SemiBold.ttf"
),

font!
(
"../../assets/fonts/JetBrainsMono-ThinItalic.ttf"
),

font!
(
"../../assets/fonts/JetBrainsMono-Thin.ttf"
),
 ],

As you guessed, we need yet another phase, this time to replace all instances of../../assets/fontsto the font package's own path:

diff --git a/gnu/packages/terminals.scm b/gnu/packages/terminals.scm
index 13e690e11f..a2a5a71a07 100644
---
a/gnu/packages/terminals.scm

+++
b/gnu/packages/terminals.scm

@@ -67,6 +67,7 @@
 (define-module (gnu packages terminals)

 #:use-module (gnu packages sqlite)
 #:use-module (gnu packages elf)
 #:use-module (gnu packages vulkan)

+
 #:use-module (gnu packages fonts)

 #:use-module ((guix licenses) #:prefix license:)
 #:use-module (guix build-system cargo)
 #:use-module (guix build-system cmake)

@@ -1702,7 +1703,9 @@
 (define-public wezterm

 patchelf
 vulkan-loader
 `(,zstd "lib")

-
 mesa)))

+
 mesa

+
 font-jetbrains-mono

+
 font-google-roboto
)))

 (build-system cargo-build-system)
 (arguments
 (list

@@ -1721,6 +1724,17 @@
 (define-public wezterm

 (lambda _
 (substitute* "./window/src/egl.rs"
 (("libEGL.so") (string-append #$mesa "/lib/libEGL.so")))))

+
 (add-after 'unpack 'fix-font-load-path

+
 (lambda* (#:key inputs #:allow-other-keys)

+
 (substitute* "wezterm-font/src/parser.rs"

+
 (("../../assets/fonts/JetBrains")

+
 (string-append

+
 #$font-jetbrains-mono

+
 "/share/fonts/truetype/JetBrains"))

+
 (("../../assets/fonts/Roboto")

+
 (string-append

+
 #$font-google-roboto

+ "/share/fonts/truetype/Roboto")))))

A rebuild confirms that the terminal still launches as before, only this time it's using fonts from Guix, not the ones bundled in the repository.

### 4.7.It's Vulkan, not Vulkan't

Note from the future:Just like withlibEGL, this isn't the best way to ensure WezTerm (or any other Rust-based package) can see Vulkan and is only shown because this is what I stumbled upon while reading others' code and what any other complete beginner might reasonably reach out for without knowing better.

In this case too, you can simply just instruct the linker, which both helps us get rid ofpatchelfand any manual mucking with the load paths and is a lot more idiomatic.

While the terminal is functional at this point, if we were to inspect the parent terminal where we startedwezterm, we might notice a suspicious error message:

libEGL warning: pci id for fd 20: 10de:2f04, driver (null)

pci id for fd 21: 10de:2f04, driver (null)
kmsro: driver missing
libEGL warning: egl: failed to create dri2 screen
pci id for fd 21: 10de:2f04, driver (null)
kmsro: driver missing
libEGL warning: egl: failed to create dri2 screen

This is in fact the other big issue foreshadowed two sections ago. While we have fixed the situation withlibEGL, there is another library we need to really get WezTerm working. This library islibvulkan, also known asVulkan, OpenGL's successor. WezTerm uses it to enable GPU hardware acceleration and, without it, we're left with an embarrassingly slow CPU-accelerated rendering pipeline, that even stuff as old as the originalxtermbeat by magnitudes of speed.11

However, this time around, unlike with EGL, there is no hard-coded filename to patch, no matter how hard we're looking. So the usual trick of rewriting won't work here. Instead, we are going to addlibvulkan.soto the library loader's search path in another way. Enterpatchelf, a handy tool that can manipulate theELF headerof a binary.

ELF or"Executable and Loadable Format"is the Unix solution to storing the metadata of executables. It is a small header that defines (among many other things, this is just a taste) what sort of machine this code is expected to run on (32-bit or 64-bit, x86 or ARM, etc.), what memory location our program code starts at, and most importantly for our purposes, the libraries linked to the executable.

By changing this header table, we are able to slip in a reference tolibvulkan.so, without it ever being mentioned directly in the code:

diff --git a/gnu/packages/terminals.scm b/gnu/packages/terminals.scm
index 34758f238e..13e690e11f 100644
---
a/gnu/packages/terminals.scm

+++
b/gnu/packages/terminals.scm

@@ -65,6 +65,8 @@
 (define-module (gnu packages terminals)

 #:use-module (gnu packages fcitx5)
 #:use-module (gnu packages version-control)
 #:use-module (gnu packages sqlite)

+
 #:use-module (gnu packages elf)

+
 #:use-module (gnu packages vulkan)

 #:use-module ((guix licenses) #:prefix license:)
 #:use-module (guix build-system cargo)
 #:use-module (guix build-system cmake)

@@ -1697,6 +1699,8 @@
 (define-public wezterm

 libssh2
 libgit2
 sqlite

+
 patchelf

+
 vulkan-loader

 `(,zstd "lib")
 mesa)))
 (build-system cargo-build-system)

@@ -1717,6 +1721,12 @@
 (define-public wezterm

 (lambda _
 (substitute* "./window/src/egl.rs"
 (("libEGL.so") (string-append #$mesa "/lib/libEGL.so")))))

+
 (add-before 'install 'patch-libvulkan-so

+
 (lambda* (#:key inputs #:allow-other-keys)

+
 (invoke "patchelf"

+
 "--add-needed"

+
 (string-append #$vulkan-loader "/lib/libvulkan.so")

+
 "./target/release/wezterm-gui")))

 (replace 'install
 (lambda* (#:key inputs native-inputs #:allow-other-keys)

 ;; Binaries

invokeas the name suggests is Guix's mechanism to call out into a different application during build time. Because we're inside a gexp, our code is ensured to only be actually executed when we're done with the building and just before the installation is attempted. Since we addedpatchelfto our inputs, we don't have to worry about finding it,invokewill sort it out for us.

Another minor, yet important thing to note is that this time we usedadd-beforeinstead ofadd-after. We don't really care when exactlypatchelfruns, only that it happens before the installation process is finished, as we'd first like to change the ELF header.

With this step done,libvulkan.sois finally visible to the library loader and the system can start using Vulkan to drive its graphics pipeline:

Figure 1:The different GPUs (real or emulated) WezTerm sees, now that Vulkan is enabled.

### 4.8.A short aside: Committing is hard!

Listing 5:
An example of the "ChangeLog" format.
gnu: Add wezterm.

* gnu/packages/terminal.scm: (wezterm): New variable.
* gnu/packages/rust-crates.scm (lookup-cargo-inputs) [
wezterm
]: New entry.

This was a topic I wanted to mention, but couldn't really find a better place for, so I'll just stick it here before the epilogue.

Guix, like most other GNU projects, follows the so-called "ChangeLog" style of commit messages. The idea is to have all contributors provide mostly consistent descriptions to their commits, based on a set of rules that makes understanding what exactly changed easier and in a sense "algorithmic".

You can basically go through a list of possible commit message formats and figure out what the current change fits most. Was it an addition, a modification, a deletion, a fix? After you nailed down the action, you can extract the exact file, section, and sometimes even subsection that was modified. And then there's still the "free form" part of the commit message, that elaborates on exactly what happened.

Thing is, while this sounds excellent on paper, I found it really difficult to properly follow this style. With every commit I was double guessing myself whether what I'm writing is succinct enough and fits the style, or if I'm making subtle errors and just think it's correct because it looksmostlyfine.

Unlike most other things in this article, I have no "and then it all clicked" moment to share here. I basically limped to the finish line, stealing turns of phrases from other contributors and then most of my commit messages disappeared when my submission was overhauled (see below). The rest that remained are such simple messages, that they don't really contain any of the actually iffy stuff, that confused me.

Don't get me wrong, this is still better than total anarchy and I imagine with time you get a "feel" for how to do it right, but it sure as hell didn't inspire much confidence in me while I was working on this project.

## 5.And yet, some stuff is still better left to the Professionals

So, at this point we have a pretty well-functioning package. In fact, what you're seeing above is 90% the same as what I'vesubmitted to guix/guix, with the high hopes, that the contributors there would accept it and I'd have a proper foot in the ecosystem.

The reality is both a little disappointing and, in a sense, very reassuring. As it turned out, my package definition was lacking in quite a few things:

* Instead of handling all dependencies correctly, I relied on(recurisve? #t), which is considered ananti-pattern. Instead, I should have unbundled all dependencies properly.
* I missed some bundled files that could've been deleted from the source folder, as they're completely unused during the compilation process.
* Myinstallphase didn't quite install all the files necessary. I accidentally left out stuff like shell completions and integrations.
* I didn't install theTerminfofiles for WezTerm. This caused a lot of subtle errors with command line applications, that rely on these files to know how to manipulate the state of the terminal.
* The version string I came up with was incorrect both per the Guix rules andWezTerm's own. The final version conforms to both.
* Turns out WezTerm reads a file called.tagto figure its own version out. I didn't include this in my initial submission.
* The way I patchedlibEGLandlibvulkanare considered unidiomatic and can be replaced with a much simpler snippet, which just instructs Cargo to link these libraries as you'd usually do:(setenv"RUSTFLAGS"(string-join
 '("-C""link-arg=-lEGL""-C""link-arg=-lvulkan")" "))
* The description I came up with was not quite up to snuff either, due to some sensationalized words that I didn't manage to cut.
* And I had quite a few stylistic gaffes that weren't strictly wrong, but could be expressed much better. For a couple of examples:I usedstring-appendto concatenate folders, even though Guile has a dedicated function for it calledin-vicinity.12I kept referencing packages directly in places wheresearch-input-filewould have sufficed.I destructured lists usingcarandcdr, whenmatch-lambdaworks much nicer for these purposes.
* I usedstring-appendto concatenate folders, even though Guile has a dedicated function for it calledin-vicinity.12
* I kept referencing packages directly in places wheresearch-input-filewould have sufficed.
* I destructured lists usingcarandcdr, whenmatch-lambdaworks much nicer for these purposes.

Yet, the story doesn't end on a sour note. I had three different contributors jump in and offer help and feedback, turning my package into one that truly deserves to be in the repository.

Of these three people, I'd like to specifically call out and thankhako, who also happens to be the person running and developing "Guix Moe", a project which includes a powerful build farm / mirror, and a hand-crafted, Nonguix-enabledLiveCD, which allows for much easier installation of Guix System.

Hako jumped in fairly early after I opened the PR and practically revamped my code from the ground up. Obviously much of the code remains mine, but the remaining extensions and refactors made the whole thing a lot more readable and correct and, without their help, I don't think my package would have made it in or at least not nearly as easily. They also went the extra mile to include all of the recommended fonts for WezTerm, which further fixed some failing test-cases and issues.

Being a software developer, I was already familiar with the experience of facing a code review, so having my PR thrown back for several days didn't feel too daunting. On the contrary, it was actually quite great to see the amount of care put into and attention given to my work. That's the beauty of free software and people acting out of genuine enthusiasm and willingness to help.

I hope my experience might assuage some worries of potential packagers:Your code doesn't have to be perfect!As long as you're willing to communicate and address change requests, you'll be fine and if things really are above your level, there will be others who will bear that load for you.

## 6.Conclusion

So ends about a week of coding around and finding out. As I happen to havesomeNix experience, the process wasn't nearly as harrowing as it might seem from a first glance, but Guix definitely has a couple of rough edges.

One thing that I found a bit frustrating for example was how the manual can occasionally be outdated, causing people (like myself) who aren't "in the know" to commit mistakes that could've been easily avoided otherwise. For instance,it stipulatesthat you should useguix styleto provide a consistent styling to your code. I've been following this advice and religiously formatting my code with each commit, only to betold by hako, that I actually shouldn't use the formatter at all, because it cannot cope with complex code.

Still, despite all this and even if Guix isn't quite as powerful from an infrastructure-perspective as, say, Nix, I believe the enthusiasm of its community still carries the experience hard and because of that, I came away from the experience with quite a positive impression while Guix came away with a working WezTerm package.

If you're reading this, you're only aguix pullaway from being able to addweztermto your manifest orguix installit and have it available on your system. If you happen to be a WezTerm user, I hope my package will serve you well.

Thank you for sticking with me in this quite long post! Till next time!

## Footnotes:

1


I was trying to playPortal RTXand I was a bit annoyed that even though both that and KDE support HDR, I still cannot make the two work due to Gamescope not being present on Guix System.

2


I'm being intentionally vague here. The actual trip graphical data takes to your monitor is convoluted and varies by several factors including driver, manufacturer, whether you're using Xorg or Wayland, etc. Because of that I'm not very comfortable talking about it in any authoritative way and so I won't. It doesn't really matter in the context of this blogpost anyway.

3


SpecificallyLD_PRELOADadds libraries to thefrontof the search path. This can be used to override libraries which can be used for things like injecting debug messages, using alternative memory allocation, etc.

It's an extremely powerful tool and a great attack vector if you happen to load in a tainted library. Since we're working with Guix-packaged stuff, we're fine, but it's not something to use without care and good reason.

4


In case you're unused to declarative lingo, you can think of a "derivation" as a deterministic result from a build script. Usually this is a software package (like WezTerm's in this particular instance), but the system is flexible enough to be utilized for basically anything that results in files.

For instance, the Guix home manager allows you to manage your dotfiles in a declarative way. The contents of the derivations built by Guix home are the files that are placed into your home folder including configuration files, scripts, and whatever else you may need.

5


Specifically what this means is that by the time the build system is engaged, you're only allowed to access data you've specified either in your inputs or thesourceof your package. The actual build itself happens inside a sealed off container without even network access. This is both for security reasons (a malicious package has a far smaller attack surface if it cannot talk to the cloud, nor even see your files) and to ensure reproducibility.

While Guix is primarily known for its FSF/GNU affiliation, one of their major goals is to provide a system that can be bootstrapped from the ground up using nothing more than a tiny binary seed and a long-long chain of programs of increasing complexity. It is an utterly fascinating topic and if you find it as fascinating as I do, I really suggest givingthis websitea read.

6


It's completely unrelated to the packaging journey in the post, but I found it really interesting, that Guix had aconsensus voteabout doing away with therecently controversial"master" name for the base branch.

It was nice to see the kind of pragmatism and forward thinking involved in this process: The maintainers weighed how much effort it'd take to update everyone from one branch to another, how difficult it'd be to undo, what other possible actions they could take, etc. Ultimately, the vote fell through in its infancy, due to not achieving majority support and master was kept.

Whether or not you agree with the outcome, I hope you're similarly pleased to see that this project takes its democratic values seriously. If I happen to stick with Guix for a longer while, I hope to one day join the decision making myself, even if only as a minor voice in the choir.

7


If you happen to be following along or thinking of writing your own package, please don't forget about the-jflag. It allows multiple parallel jobs to run and Guix's source is very well decoupled from each other. I have a 24-core Ryzen processor and it's a joy to see how fastmake -j24chews through the build process compared to the utter sluggishness of a single-core run.

8


It is worth noting that you have to get the package name right. When I first tried importing my crates, I didn't realize I had to use the final package's name and just enteredfinl_unicode, since I assumed I have to provide the name of the crate I wanted to import.

This ultimately sent me down a painful side-track that led nowhere until I finally read the docs better and realized I actually need to usewezterm. Learn by my mistake!

9


I'm actually not quite sure what's Guix's policy regarding tests. Some packages have them disabled, some enabled, some selectively disable some tests. In my variant of the package, I disabled them following other packages' example, but in the final variant, that other contributors helped out with, the tests are once again enabled.

10


There's also your personal profile'sbinandsbinfolders,current-system'ssbinfolder, stuff managed byguix home, etc.

11


I'm not 100% sure if Vulkan is needed on AMD hardware. I have a sneaking suspicion that the error is at least partly caused by the fact that on Guix System NVIDIA hardware requires a smallmagic incantationto work with most packages. Still, whether the error is caused by the lack of Vulkan or not doesn't really matter, as the library is still a needed dependency of WezTerm, so adding it wasn't just for kicks.

12


In my defensein-vicinityis a fairly horrible name for a function that joins paths. I mean, yeah, sure, it technically means what it does, but surelypath-appendorconstruct-pathwould've worked a lot better.
