---
title: macOS dotfiles should not go in ~/Library/Application Support @ rebecca®
url: https://becca.ooo/blog/macos-dotfiles/
site_name: lobsters
fetched_at: '2025-08-26T23:07:31.967843'
original_url: https://becca.ooo/blog/macos-dotfiles/
date: '2025-08-26'
description: A CLI tool is not an app, and none of you are reading the docs as carefully as you think you are
tags: mac, unix
---

# #macOS dotfiles should not go in~/Library/Application Support

One of my pet peeves is when command-line tools look for user configuration
files in~/Library/Application Supportwhen running on macOS. In addition to
offering poor ergonomics for users, I believe this behavior isincorrectaccording to the documentation which is cited to justify it. Instead,
command-line tools should implement theXDG Base Directory Specificationand look for configuration files in$XDG_CONFIG_HOME, which defaults to~/.config.

Usually, when a program looks for configuration files in~/Library/Application Support, it’s not because of an intentional design decision. Instead, the
author delegated that decision to a library, and several popular libraries for
determining platform-specific configuration directories use~/Library/Application Supportas the default configuration directory on
macOS, includingPython’splatformdirspackage(242
million downloads / month),JavaScript’senv-paths(95 million downloads / month),Rust’sdirscrate(4.8 million downloads / month), andGo’sadrg/xdgpackage(used in 913 packages). While~/Library/Application Supportmay be the correct configuration directory forGUI appswhich manage their
configuration files for the user automatically, the vast majority of
applications using these libraries are command-line utilities whose
configuration belongs in~/.config.

The main reason I dislike programs looking for dotfiles in~/Library/Application Supportis that it’sunexpected.AsAshlin Eldridge
explained on GitHub:

As a new user, it’s extremely surprising to me to that a modern tool likenuwould put config files under Application Support on macOS. It’s even
more surprising to see that some people areactivelyagainstadopting the XDG
standard.

The origins of XDG no longer matter at this point. No one really cares what
the X, D, and G stand for. The fact is thathundredsof tools
support it (including Git, Emacs, Neovim, Tmux) and users have come to expect
support for it. It’s the closest thing we have to a standard that allows
users to control the placement of their config files (which facilitates
users’ ability to source control their files) and it also includes support
for files that shouldn’t be source controlled such as cache and data files.

If a user explains that they found a program’s behavior surprising, many
engineers will respond by telling the user that their expectations were wrong.
However, I find that the reason users form an incorrect mental model of a
program’s behavior is usually because the program’s design violated an
established convention from some broader context. In accordance withthe
Principle of Least Astonishment, I prefer to change the program to
behave how users expect rather than futilely attempt to change what users
expect.

Users expect macOS CLI tools to look for configuration files in~/.configis
becausethat’s what almost every other program does.Your program should
probably not disagree with Bash and Vim and Git about where configuration files
are supposed to go!

These conventions help us explore unfamiliar systems by letting us apply
knowledge about one part of the system to other parts of the system.
Consistency is predictability. When every tool works the same except for a
small handful, users get justifiably annoyed at the exceptions for wasting
their time.

## #What do dotfile managers do?

Many engineers use (or maintain) some sort of dotfile manager to handle
tracking these configuration files. If configuration files are really supposed
to go in~/Library/Application Support, we would expect dotfile managers to
put configuration files there by default when running on macOS. After all, the
whole point of a dotfile manager is to simplify managing configuration files
across multiple machines and platforms. Let’s take a quick survey to see how
some popular dotfile managers behave on macOS:

* chezmoi(14.3k stars) makes no effort to link
configuration to~/Library/Application Support, despite includingdocumentation for using chezmoi on macOS
specifically.
* dotbot(7.3k stars) ignores~/Library/Application Support. Despite including macOS-specific
configuration files in the examples, the README shows a configuration for VS
Code that will be completely ignored on macOS.
* yadm(5.5k stars) makes no effort to
support~/Library/Application Support. The example configurations include
macOS-specific portions but also do not reference~/Library/Application Support.
* rcm(3.2k stars) makes no effort to
support~/Library/Application Support.
* GNU Stowmakes (unsurprisingly) no
effort to support~/Library/Application Support.

Most of these tools areableto link configuration files to~/Library/Application Supportif you ask them to explicitly (although macOS
will regularly replace your symlinks with copies of the destination files), but
the fact that they don’t bother to do so by default is revealing. Users only
want this behavior for specific misbehaving programs.

## #An appeal to logic

Perhaps “consistency” isn’t a good enough reason for you to place your
program’s configuration files in~/.configlike everybody else. Maybe you
think that programs should follow the platform guidelines, even if they don’t
match developer expectations.@soc on GitHubphrases it like this:

As a general advice for macOS devs: If you are developing on their platform,
do what the platform owners tell you. They are the lords, you are the
share-croppers.

Elsewhere,Reilly Wood rebukesa user asking if there would “be any
downside to just not usingApplication Supportever” by saying that “[Nushell
would] no longer be following themacOS Standard Directories
guidelines.”

We’ll read through those guidelines in a minute, but it’s not entirely clear to
me that they’re relevant in the first place. TheXDG Base Directory
Specificationmentions Unix a few times but lists no carveouts for macOS
or any other operating system. If~/.configis accepted as the standard
location for configuration files on Unix-like operating systems, then surely it
would be the standard location on macOS as well, given that macOS is a Unix by
way of BSD.

But suppose we accept that the XDG specification only applies tosomeUnix
operating systems, despite making no mention of this. ThemacOS Standard
Directoriesdocumentation starts by stating that
“[w]hether provided by the system or created by your app, every file has its
place in macOS”, and honestly we could stop reading right there, becausea
command-line tool is not the system or an app.

While this might seem like a pedantic nitpick, in reality it’scriticalto
correctly interpreting this documentation! I suspect that many of the
developers who cite these guidelines do not know very much about macOS and
think that “app” is just what macOS calls executables, but that’s not true. A
couple screens down, the same page says that/bin“[c]ontains essential
command-line binaries”, so we can be sure the authors aren’t conflating apps
and command-line tools. Apps on macOS are installed in/Applicationsand are
subject toa number of additional requirements, from a bundle ID
(a unique reverse-DNS identifier for an app, likecom.apple.PreviewforPreview.app) to application icons, launch screens, code signing,
notarization, app sandboxing, and runtime hardening. Needless to say, none of
the developers shipping command-line utilities are following any oftheseguidelines.

Moving on,the documentation for~/Library/Application Supportsays that it:

Contains all app-specific data and support files. These are the files that
your app creates and manages on behalf of the user and can include files that
contain user data.

Again, command-line tools do not haveanyapp-specific data because they are
not apps. Further, dotfiles are usually written by hand and not managedon
behalf ofthe user.

The next paragraph makes it very clear that~/Library/Application Supportis
for apps only:

By convention, all of these items should be put in a subdirectory whose name
matches the bundle identifier of the app. For example, if your app is namedMyAppand has the bundle identifiercom.example.MyApp, you would put your
app’s user-specific data files and resources in the~/Library/Application Support/com.example.MyApp/directory. Your app is responsible for creating
this directory as needed.

Command-line tools do not have a bundle identifier, including many command-line
tools shipped with macOS by Apple (such aslsorvim). And even thoughApple feels very comfortable shipping command-line tools that behave in a
subtly different manner from their equivalents on other modern Unix-descendent
operating systems,the macOS variants ofbash,zsh,git, andvimall look for their configuration files in the same place:~/.config.
Unless your tool is installed in/Applications, there’s no reason for its
configuration to live in~/Library/Application Support.

## #Whenshouldyou use~/Library/Application Support

With the guidelines and conventions listed above in mind, your application
should store its configuration files in~/Library/Application Supportinstead
of$XDG_CONFIG_HOMEif both of the following conditions apply:

1. It is a GUI application installed in/Applicationsor~/Applications.
2. It manages its configuration files automatically on behalf of the user,
rather than expecting the user to write their configuration in a text file
themself.

## #TL;DR

Users do not expect command-line tools to look for configuration files in~/Library/Application Supporton macOS. Dotfile managers do not place
configuration files in~/Library/Application Supporton macOS. The most
commonly-cited justifications for placing configuration files in~/Library/Application Supportare not meant to apply to command-line tools at
all. Even command-line tools likebashandgitshipped by Apple look for
their configuration files in~/.config.

Please, please,pleasejust use theXDG Base Directory Specification.
