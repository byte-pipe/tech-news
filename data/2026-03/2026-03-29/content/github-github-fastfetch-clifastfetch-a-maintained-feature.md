---
title: 'GitHub - fastfetch-cli/fastfetch: A maintained, feature-rich and performance oriented, neofetch like system information tool. · GitHub'
url: https://github.com/fastfetch-cli/fastfetch
site_name: github
content_file: github-github-fastfetch-clifastfetch-a-maintained-feature
fetched_at: '2026-03-29T11:11:10.614451'
original_url: https://github.com/fastfetch-cli/fastfetch
author: fastfetch-cli
description: A maintained, feature-rich and performance oriented, neofetch like system information tool. - fastfetch-cli/fastfetch
---

fastfetch-cli



/

fastfetch

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork710
* Star21k




 
dev
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

7,034 Commits
7,034 Commits
.github
.github
 
 
completions
completions
 
 
debian
debian
 
 
doc
doc
 
 
presets
presets
 
 
screenshots
screenshots
 
 
scripts
scripts
 
 
src
src
 
 
tests
tests
 
 
.clang-format
.clang-format
 
 
.clang-format-ignore
.clang-format-ignore
 
 
.codespellrc
.codespellrc
 
 
.editorconfig
.editorconfig
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CMakeLists.txt
CMakeLists.txt
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
LICENSE
LICENSE
 
 
README-cn.md
README-cn.md
 
 
README.md
README.md
 
 
run.sh
run.sh
 
 
View all files

## Repository files navigation

# Fastfetch

Fastfetch is aneofetch-like tool for fetching system information and displaying it in a visually appealing way. It is written mainly in C, with a focus on performance and customizability. Currently, it supports Linux, macOS, Windows 8.1+, Android, FreeBSD, OpenBSD, NetBSD, DragonFly, Haiku and SunOS (illumos, Solaris).

Note: Fastfetch is only actively tested on x86-64 and aarch64 platforms. It may work on other platforms but is not guaranteed to do so.

According configuration files for examples are locatedhere.

There arescreenshots on different platforms.

## Installation

### Linux

Some distributions package outdated versions of fastfetch. Older versions receive no support, so please always try to use the latest version.

* Ubuntu:ppa:zhangsongcui3371/fastfetch(Ubuntu 22.04 or newer; latest version)
* Debian / Ubuntu:apt install fastfetch(Debian 13 or newer; Ubuntu 25.04 or newer)
* Debian / Ubuntu: Downloadfastfetch-linux-<proper architecture>.debfromGithub release pageand double-click it (for Ubuntu 20.04 or newer and Debian 11 or newer).
* Arch Linux:pacman -S fastfetch
* Fedora:dnf install fastfetch
* Gentoo:emerge --ask app-misc/fastfetch
* Alpine:apk add --upgrade fastfetch
* NixOS:nix-shell -p fastfetch
* openSUSE:zypper install fastfetch
* ALT Linux:apt-get install fastfetch
* Exherbo:cave resolve --execute app-misc/fastfetch
* Solus:eopkg install fastfetch
* Slackware:sbopkg -i fastfetch
* Void Linux:xbps-install fastfetch
* Venom Linux:scratch install fastfetch

You may needsudo,doas, orsupto run these commands.

If fastfetch is not packaged for your distribution or an outdated version is packaged,linuxbrewis a good alternative:brew install fastfetch

### macOS

* Homebrew:brew install fastfetch
* MacPorts:sudo port install fastfetch

### Windows

* scoop:scoop install fastfetch
* Chocolatey:choco install fastfetch
* winget:winget install fastfetch
* MSYS2 MinGW:pacman -S mingw-w64-<subsystem>-<arch>-fastfetch

You may also download the program directly fromthe GitHub releases pagein the form of an archive file.

### BSD systems

* FreeBSD:pkg install fastfetch
* NetBSD:pkgin in fastfetch
* OpenBSD:pkg_add fastfetch(Snapshots only)
* DragonFly BSD:pkg install fastfetch(Snapshots only)

### Android (Termux)

* pkg install fastfetch

### Nightly

https://nightly.link/fastfetch-cli/fastfetch/workflows/ci/dev?preview

## Build from source

See the Wiki:https://github.com/fastfetch-cli/fastfetch/wiki/Building

## Usage

* Run with default configuration:fastfetch
* Run withall supported modulesto find what interests you:fastfetch -c all.jsonc
* View all data that fastfetch detects:fastfetch -s <module1>[:<module2>][:<module3>] --format json
* Display help messages:fastfetch --help
* Generate a minimal config file:fastfetch [-s <module1>[:<module2>]] --gen-config [</path/to/config.jsonc>]Use:--gen-config-fullto generate a full config file with all optional options
* Use:--gen-config-fullto generate a full config file with all optional options

## Customization

Fastfetch uses JSONC (JSON with comments) for configuration.See the Wiki for details. There are some premade config files in thepresetsdirectory, including those used for the screenshots above. You can load them using-c <filename>. These files can serve as examples of the configuration syntax.

Logos can also be heavily customized; see thelogo documentationfor more information.

### WARNING

Fastfetch supports aCommandmodule that can run arbitrary shell commands. If you copy-paste a config file from an untrusted source, it may contain malicious commands that can harm your system or compromise your privacy. Please always review the config file before using it.

## FAQ

### Q: Neofetch is good enough. Why do I need fastfetch?

1. Fastfetch is actively maintained.
2. Fastfetch is faster, as the name suggests.
3. Fastfetch has a greater number of features, though by default it only has a few modules enabled; usefastfetch -c allto discover what you want.
4. Fastfetch is more configurable. You can find more information in the Wiki:https://github.com/fastfetch-cli/fastfetch/wiki/Configuration.
5. Fastfetch is more polished. For example, neofetch prints555 MiBin the Memory module and23 Gin the Disk module, whereas fastfetch prints555.00 MiBand22.97 GiBrespectively.
6. Fastfetch is more accurate. For example,neofetch never actually supports the Wayland protocol.

### Q: Fastfetch shows my local IP address. Does it leak my privacy?

A local IP address (10.x.x.x, 172.x.x.x, 192.168.x.x) has nothing to do with privacy. It only has meaning if you are on the same network, for example, if you connect to the same Wi-Fi network.

Actually, theLocal IPmodule is the most useful module for me personally. I (@CarterLi) have several VMs installed to test fastfetch and often need to SSH into them. With fastfetch running on shell startup, I never need to typeip addrmanually.

If you really don't like it, you can disable theLocal IPmodule inconfig.jsonc.

### Q: Where is the config file? I can't find it.

Fastfetch does not generate a config file automatically. You can usefastfetch --gen-configto generate one. The config file will be saved in~/.config/fastfetch/config.jsoncby default. See theWiki for details.

### Q: The configuration is so complex. Where is the documentation?

Fastfetch uses JSON (with comments) for configuration. I suggest using an IDE with JSON schema support (like VSCode) to edit it.

Alternatively, you can refer to the presets in thepresetsdirectory.

Thecorrectway to edit the configuration:

This is an example thatchanges size prefix from MiB / GiB to MB / GB. Editor used:helix

### Q: I WANT THE DOCUMENTATION!

Here is the documentation. It is generated from theJSON schema, but you might not find it very user-friendly.

### Q: How can I customize the module output?

Fastfetch usesformatto generate output. For example, to make theGPUmodule show only the GPU name (leaving other information undisplayed), you can use:

...which is equivalent tofastfetch -s gpu --gpu-format '{name}'

Seefastfetch -h formatfor information on basic usage. For module-specific formatting, seefastfetch -h <module>-format

### Q: I have my own ASCII art / image file. How can I show it with fastfetch?

Tryfastfetch -l /path/to/logo. See thelogo documentationfor details.

If you just want to display the distro name inFIGlet text:

#
 install pyfiglet and jq first

pyfiglet -s -f small_slant
$(
fastfetch -s os --format json
|
 jq -r
'
.[0].result.name
'
)

&&
 fastfetch -l none

### Q: My image logo behaves strangely. How can I fix it?

See the troubleshooting section:https://github.com/fastfetch-cli/fastfetch/wiki/Logo-options#troubleshooting

### Q: Fastfetch runs in black and white on shell startup. Why?

This issue usually occurs when using fastfetch withp10k. There are known incompatibilities between fastfetch and p10k instant prompt.
The p10k documentation clearly states that you should NOT print anything to stdout afterp10k-instant-promptis initialized. You should putfastfetchbefore the initialization ofp10k-instant-prompt(recommended).

You can always usefastfetch --pipe falseto force fastfetch to run in colorful mode.

### Q: Why do fastfetch and neofetch show different memory usage results?

See#1096.

### Q: Fastfetch shows fewer dpkg packages than neofetch. Is it a bug?

Neofetch incorrectly countsrcpackages (packages that have been removed but still have configuration files remaining). See bug:dylanaraps/neofetch#2278

### Q: I use Debian / Ubuntu / Debian-derived distro. My GPU is detected asXXXX Device XXXX (VGA compatible). Is this a bug?

Try upgradingpci.ids: Downloadhttps://pci-ids.ucw.cz/v2.2/pci.idsand overwrite the file/usr/share/hwdata/pci.ids. For AMD GPUs, you should also upgradeamdgpu.ids: Downloadhttps://gitlab.freedesktop.org/mesa/drm/-/raw/main/data/amdgpu.idsand overwrite the file/usr/share/libdrm/amdgpu.ids

Alternatively, you may try usingfastfetch --gpu-driver-specific, which will make fastfetch attempt to ask the driver for the GPU name if supported.

### Q: I get the errorAuthorization required, but no authorization protocol specifiedwhen running fastfetch as root

Tryexport XAUTHORITY=$HOME/.Xauthority

### Q: Fastfetch cannot detect my awesome 3rd-party macOS window manager!

Tryfastfetch --wm-detect-plugin. See also#984

### Q: How can I change the colors of my ASCII logo?

Tryfastfetch --logo-color-[1-9] <color>, where[1-9]is the index of color placeholders.

For example:fastfetch --logo-color-1 red --logo-color-2 green.

In JSONC, you can use:

### Q: How do I hide a key?

Set the key to a white space.

### Q: How can I display images on Windows?

As of April 2025:

#### mintty and Wezterm

mintty (used by Bash on Windows and MSYS2) and Wezterm (nightly build only) support the iTerm image protocol on Windows.

Inconfig.jsonc:

{

"logo"
: {

"type"
:
"
iterm
"
,

"source"
:
"
C:/path/to/image.png
"
,

"width"
:
<num-in-chars>

 }
}

#### Windows Terminal

Windows Terminal supports the sixel image protocol only.

* If you installed fastfetch through MSYS2:Install imagemagick:pacman -S mingw-w64-<subsystem>-x86_64-imagemagickInconfig.jsonc:
* Install imagemagick:pacman -S mingw-w64-<subsystem>-x86_64-imagemagick
* Inconfig.jsonc:

* If you installed fastfetch via scoop or downloaded the binary directly from the GitHub Releases page:Convert your image manually to sixel format usingany online image conversion serviceInconfig.jsonc:
* Convert your image manually to sixel format usingany online image conversion service
* Inconfig.jsonc:

### Q: I want feature A / B / C. Will fastfetch support it?

Fastfetch is a system information tool. We only accept hardware or system-level software feature requests. For most personal uses, I recommend using theCommandmodule to implement custom functionality, which can be used to grab output from a custom shell script:

Otherwise, please open a feature request inGitHub Issues.

### Q: I have questions. Where can I get help?

* For usage questions, please start a discussion inGitHub Discussions.
* For possible bugs, please open an issue inGitHub Issues. Be sure to fill out the bug report template carefully to help developers investigate.

## Donate

If you find Fastfetch useful, please consider donating.

* Current maintainer:@CarterLi
* Original author:@LinusDierheimer

## Code signing

* Free code signing provided bySignPath.io, certificate bySignPath Foundation
* This program will not transfer any information to other networked systems unless specifically requested by the user or the person installing or operating it

## Star History

Give us a star to show your support!

## About

A maintained, feature-rich and performance oriented, neofetch like system information tool.

### Topics

 fetch

 terminal

 command-line

 neofetch

 hacktoberfest

 winfetch

 fastfetch

 flashfetch

 macfetch

 bsdfetch

### Resources

 Readme



### License

 MIT license


### Code of conduct

 Code of conduct


### Uh oh!

There was an error while loading.Please reload this page.





Activity


Custom properties


### Stars

21k

 stars


### Watchers

54

 watching


### Forks

710

 forks


 Report repository



## Releases170

2.61.0

 Latest



Mar 28, 2026



+ 169 releases

## Sponsor this project

### Uh oh!

There was an error while loading.Please reload this page.






* ko-fi.com/carterli
* https://paypal.me/zhangsongcui

Learn more about GitHub Sponsors

### Uh oh!

There was an error while loading.Please reload this page.





## Contributors

### Uh oh!

There was an error while loading.Please reload this page.





## Languages

* C93.4%
* CMake2.5%
* C++1.8%
* Objective-C1.6%
* Other0.7%
