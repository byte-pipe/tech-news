---
title: Wayback 0.1 released!
url: https://wayback.freedesktop.org/news/2025/07/23/wayback-0.1-released/
site_name: lobsters
fetched_at: '2025-07-24T23:06:49.314717'
original_url: https://wayback.freedesktop.org/news/2025/07/23/wayback-0.1-released/
date: '2025-07-24'
tags: linux
---

News
×

# Wayback 0.1 released!

🕓 July 23, 2025

We are pleased to announce Wayback’s first preview release, version0.1, just
released!

Wayback is an X11 compatibility layer that allows for running full X11-only
desktop environments using Wayland. It is essentially an X11 server backed by
Wayland, leveragingwlrootsandXwayland. Our goal is for Wayback to eventually be a completely drop-in
replacement to theXorgbinary, thus reducing maintenance burden for distro
maintainers.

Ever since Wayback was announced onJune
28, we have been
making lots of progress to get it as stable and functional as possible, and while
this is a preview release it is already daily-driveable by users with simple
requirements, as long as they don’t mind bugs.

You can grab this new release fromthe git
repositoryor wait
for your distribution to pick it up!

## Status

While we hope they aren’t too many bugs, this is still considered alpha-quality
software and there are still features that are, as of now, unimplemented or
work-in-progress. To set expectations:

* There is no multi-monitor support at the moment (#8)
* DPMS controlling is not yet supported (#55)
* Many Xorg options are currently stubs (#14,#51)
* Some other things don’t work, e.g. mouse locking (very useful in first-person
shooters and used by XScreenSaver)

That being said, some of us are already daily-driving it to find bugs and fix
them as they appear. We highly encourage testing Wayback and reporting any bugs
you encounter, and we also welcome merge requests!

## Progress since June 28

Since the initial announcement a lot of progress has been made!

* We moved fromkaniini’s GitHub repo to a freedesktop.org GitLab
group.(ThanksConan_Kudo,mupuf, and the freedesktop.org
crew!):!40
* We now also have a Matrix bridge (#wayback:catircservices.org) to our IRC
channel at Libera.Chat(Thankswhitequark!)
* Split wayback into an X.org-like structure(Thanksaxtlos!):!27and!28wayback-compositoris the actual Wayland compositorXwaybackprovides anXorg-compatible command line interface for
launchingXwaylandandwayback-compositorwayback-sessionprovides astartx-compatible interface (note it is a
temporary measure, eventually we will make use of stockxinitfor that)
* wayback-compositoris the actual Wayland compositor
* Xwaybackprovides anXorg-compatible command line interface for
launchingXwaylandandwayback-compositor
* wayback-sessionprovides astartx-compatible interface (note it is a
temporary measure, eventually we will make use of stockxinitfor that)
* Introduced a more central logging mechanism(Thanksaxtlos!):!46
* We now have a properclang-formatand an established coding style(ThanksConan_Kudo!)
* Wayback got packaged in a number of distributions, including Alpine Linux,
Nix, Arch Linux (AUR), Fedora, and many others!
* A new option parser, similar togetopt, has been implemented. This is
necessary because Xorg supports options e.g.+optthat are not handled by
getopt(Thanksfunderscore!):!72
* A number of bugs have been fixed, and the overall code has been cleaned up.(Thanksaxtlos,Conan_Kudo,Consolatis,dramforever,funderscore,jmaselbas,kaniini,navi,fossdd,MonterraByte,Sertonix!)

### Logo and website

Some other exciting news: Wayback now finally has a logo! It is heavily
inspired by the X.org logo:

Alongside it, we also have a brand new website! It is powered byHugo.

Thanksjmaselbas,whitequark,funderscore!

## Remaining work

Many thanks to everybody who got involved in this first release.

Thanks to the thriving community we keep making lots of progress towards our goal.
If you are new to the project and would like to participate, hop in the#waybackIRC channel on Libera.Chat (#wayback:catircservices.orgon Matrix) to get started!

There is still a lot to be done before a stable release, so any and all help is
welcome, no matter how small.

## Git shortlog

Anna (navi) Figueiredo Gomes (7):

 wayback-session: properly handle XWAYBACK_PATH

 xwayback: remove unused variables

 xwayback: remove unsetenv check

 xwayback: use wl_display_connect_to_fd

 xwayback: unset WAYLAND_SOCKET as well

 xwayback: simplify argument relaying

 xwayback: use posix_spawn over fork+exec

Ariadne Conill (13):

 initial commit

 add wlr_viewporter

 implement session launching

 hackishly probe output geometry

 add LICENSE

 add README

 add code of conduct

 LICENSE: use MIT

 readme: note libera.chat discussion channel

 meson: add xwayback.c back

 fix sys/signal.h deprecation warnings on alpine

 protocol: meson: fix up deprecation warnings

 compositor: use traditional X killswitch combo instead of alt+esc

Consolatis (1):

 xwayback: allow nested startup on wayland

Ferass El Hafidi (29):

 xwayback: add handling of SIGSEGV

 xwayback: check if compositor/Xwayland path exists

 xwayback: ensure that xwayback->first_output is not NULL

 xwayback: run Xwayland with -terminate

 xwayback: prefix "passed descriptor" message

 xwayback: unset WAYLAND_DISPLAY

 xwayback: support setting XWAYLAND_PATH env var to an alternate path to Xwayland binary

 doc/Xwayback.scdoc: mention new XWAYLAND_PATH env var

 xwayback: actually use the XWAYLAND_PATH env var

 README.md: mention some distro packages

 .gitlab: add new issue templates

 doc: use tabs for indentation

 wayback-session: introduce XWAYBACK_PATH env var

 doc/wayback-session.scdoc: document supported environment variables

 xwayback: fix typo in 'Xwayland not found' error message

 xwayback: remove useless calls to strdup

 wayback-session,xwayback: remove useless F_OK

 wayback-session: actually initialise session_cmd

 Xwayback: use getopt_long_only instead of getopt_long

 wayback-session: only check access when the env var is set

 xwayback|wayback-session: print sterror-ified error message on exec failure

 wayback-session: also print sterror-ified message on session exec fail

 wayback-compositor: remove references to request_move/resize

 wayback-session: unset WAYLAND_DISPLAY before running session

 Xwayback: add timeout to `-terminate`

 reimplement option parsing

 Xwayback: do not hand over handled options to Xwayland

 Xwayback|wayback-compositor: replace remaining fprintf's with wayback_log

 Xwayback: add more options

Joaquim Monteiro (3):

 Set up GitHub CI

 meson: Set C standard to C11 with GNU extensions

 meson: Enable compiler warnings

Jules Maselbas (3):

 wayback-compositor: stop at the first handled key

 xwayback: make local symbols static

 xwayback: make env string pointer const

Michal Vanis (2):

 wayback-compositor: remove the viewporter protocol

 xwayback: remove the xwayland fullscreen flag

Neal Gompa (15):

 meson, wayback: Update to indicate code licensed under MIT license

 ci: Add Fedora Rawhide build testing

 meson, xwayback: Detect and use the Xwayland binary found at build time

 Add note of archival

 README: Drop GitHub archival note and update description to match fdo submission

 CI: Port over to GitLab CI leveraging gitlab.freedesktop.org instance runners

 Switch to the FreeDesktop Code of Conduct

 README: Fix formatting for GitLab

 doc: Add Wayback logo SVG

 doc: Update Wayback logo icon

 Add a clang-format definition and reformat codebase with clang-format

 CI: Run clang-format checks

 CI: Set clang-format to run only on merge requests and on the MR diff

 meson: Raise the C standard to C23 and bump minimum version to 1.4.0

 README: Point to the official Fedora Linux package

Sertonix (1):

 build: remove unused variable

axtlos (11):

 wayback-session/xwayback: properly quit with child

 Common: Add wayback logging functions

 Xwayback/wayback-session: Use new logging functions

 common: Use static library for common functions

 common: Respect NO_COLOR envvar for color logging

 common: Properly define includes as dependency

 Xwayback: use write to print error in case of segv

 Xwayback/wayback-compositor: Allow deciding which output to use

 Wayback: Remove uses of BUFSIZ

 Xwayback: Use X style arguments

 Xwayback: Pass unknown arguments to Xwayland

axtloss (23):

 Add installation instructions to README

 Use getopt for argument parsing

 Automatically exit with X11 Desktop/WM

 Set XDG_SESSION_TYPE to x11

 allow vt switching through alt+ctrl+Fn

 Split wayback in xorg like structure

 Add wayback-compositor

 Add xwayback to launch xwayland and wayback-compositor

 Add -displayfd option to Xwayback

 Add Xwayback(1) manpage

 wayback-compositor: Readd VT switching support

 Split wayback in xorg like structure

 Add wayback-session to to launch xwayback and the user session

 Use displayfd to get display in wayback-session

 wayback-session: improve get_xinitrc_path

 Add wayback-session(1) manpage

 Add meson build target for manpages

 wayback-session: Dont set WAYLAND_DISPLAY

 wayback-compositor: Properly bind ctrl+alt+backspace

 meson: Install wayback-compositor to libexec

 Properly concatenate path for wayback compositor

 meson: Allow wlroots-0.18

 xwayback: Allow overwriting wayback-compositor path

dramforever (2):

 wayback-compositor: Use common functions

 common: Add and use {asprintf,strdup}_or_exit

fossdd (2):

 build: install wayback

 build: generate Xwayback.1 manpage
