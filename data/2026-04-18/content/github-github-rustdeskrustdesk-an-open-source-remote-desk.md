---
title: 'GitHub - rustdesk/rustdesk: An open-source remote desktop application designed for self-hosting, as an alternative to TeamViewer. · GitHub'
url: https://github.com/rustdesk/rustdesk
site_name: github
content_file: github-github-rustdeskrustdesk-an-open-source-remote-desk
fetched_at: '2026-04-18T11:33:48.569221'
original_url: https://github.com/rustdesk/rustdesk
author: rustdesk
description: An open-source remote desktop application designed for self-hosting, as an alternative to TeamViewer. - rustdesk/rustdesk
---

rustdesk



/

rustdesk

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork16.7k
* Star112k




 
master
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

11,068 Commits
11,068 Commits
.cargo
.cargo
 
 
.github
.github
 
 
appimage
appimage
 
 
docs
docs
 
 
examples
examples
 
 
fastlane/
metadata/
android
fastlane/
metadata/
android
 
 
flatpak
flatpak
 
 
flutter
flutter
 
 
libs
libs
 
 
res
res
 
 
src
src
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
Dockerfile
Dockerfile
 
 
GEMINI.md
GEMINI.md
 
 
LICENCE
LICENCE
 
 
README.md
README.md
 
 
build.py
build.py
 
 
build.rs
build.rs
 
 
entrypoint.sh
entrypoint.sh
 
 
vcpkg.json
vcpkg.json
 
 
View all files

## Repository files navigation

Build•Docker•Structure•Snapshot[Українська] | [česky] | [中文] | [Magyar] | [Español] | [فارسی] | [Français] | [Deutsch] | [Polski] | [Indonesian] | [Suomi] | [മലയാളം] | [日本語] | [Nederlands] | [Italiano] | [Русский] | [Português (Brasil)] | [Esperanto] | [한국어] | [العربي] | [Tiếng Việt] | [Dansk] | [Ελληνικά] | [Türkçe] | [Norsk] | [Română]We need your help to translate this README,RustDesk UIandRustDesk Docto your native language

Caution

Misuse Disclaimer:The developers of RustDesk do not condone or support any unethical or illegal use of this software. Misuse, such as unauthorized access, control or invasion of privacy, is strictly against our guidelines. The authors are not responsible for any misuse of the application.

Chat with us:Discord|Twitter|Reddit|YouTube

Yet another remote desktop solution, written in Rust. Works out of the box with no configuration required. You have full control of your data, with no concerns about security. You can use our rendezvous/relay server,set up your own, orwrite your own rendezvous/relay server.

RustDesk welcomes contribution from everyone. SeeCONTRIBUTING.mdfor help getting started.

FAQ

BINARY DOWNLOAD

NIGHTLY BUILD

## Dependencies

Desktop versions use Flutter or Sciter (deprecated) for GUI, this tutorial is for Sciter only, since it is easier and more friendly to start. Check out ourCIfor building Flutter version.

Please download Sciter dynamic library yourself.

Windows|Linux|macOS

## Raw Steps to build

* Prepare your Rust development env and C++ build env
* Installvcpkg, and setVCPKG_ROOTenv variable correctlyWindows: vcpkg install libvpx:x64-windows-static libyuv:x64-windows-static opus:x64-windows-static aom:x64-windows-staticLinux/macOS: vcpkg install libvpx libyuv opus aom
* Windows: vcpkg install libvpx:x64-windows-static libyuv:x64-windows-static opus:x64-windows-static aom:x64-windows-static
* Linux/macOS: vcpkg install libvpx libyuv opus aom
* runcargo run

## Build

## How to Build on Linux

### Ubuntu 18 (Debian 10)

sudo apt install -y zip g++ gcc git curl wget nasm yasm libgtk-3-dev clang libxcb-randr0-dev libxdo-dev \
 libxfixes-dev libxcb-shape0-dev libxcb-xfixes0-dev libasound2-dev libpulse-dev cmake make \
 libclang-dev ninja-build libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libpam0g-dev

### openSUSE Tumbleweed

sudo zypper install gcc-c++ git curl wget nasm yasm gcc gtk3-devel clang libxcb-devel libXfixes-devel cmake alsa-lib-devel gstreamer-devel gstreamer-plugins-base-devel xdotool-devel pam-devel

### Fedora 28 (CentOS 8)

sudo yum -y install gcc-c++ git curl wget nasm yasm gcc gtk3-devel clang libxcb-devel libxdo-devel libXfixes-devel pulseaudio-libs-devel cmake alsa-lib-devel gstreamer1-devel gstreamer1-plugins-base-devel pam-devel

### Arch (Manjaro)

sudo pacman -Syu --needed unzip git cmake gcc curl wget yasm nasm zip make pkg-config clang gtk3 xdotool libxcb libxfixes alsa-lib pipewire

### Install vcpkg

git clone https://github.com/microsoft/vcpkg

cd
 vcpkg
git checkout 2023.04.15

cd
 ..
vcpkg/bootstrap-vcpkg.sh

export
 VCPKG_ROOT=
$HOME
/vcpkg
vcpkg/vcpkg install libvpx libyuv opus aom

### Fix libvpx (For Fedora)

cd
 vcpkg/buildtrees/libvpx/src

cd

*

./configure
sed -i
'
s/CFLAGS+=-I/CFLAGS+=-fPIC -I/g
'
 Makefile
sed -i
'
s/CXXFLAGS+=-I/CXXFLAGS+=-fPIC -I/g
'
 Makefile
make
cp libvpx.a
$HOME
/vcpkg/installed/x64-linux/lib/

cd

### Build

curl --proto
'
=https
'
 --tlsv1.2 -sSf https://sh.rustup.rs
|
 sh

source

$HOME
/.cargo/env
git clone --recurse-submodules https://github.com/rustdesk/rustdesk

cd
 rustdesk
mkdir -p target/debug
wget https://raw.githubusercontent.com/c-smile/sciter-sdk/master/bin.lnx/x64/libsciter-gtk.so
mv libsciter-gtk.so target/debug
VCPKG_ROOT=
$HOME
/vcpkg cargo run

## How to build with Docker

Begin by cloning the repository and building the Docker container:

git clone https://github.com/rustdesk/rustdesk

cd
 rustdesk
git submodule update --init --recursive
docker build -t
"
rustdesk-builder
"

.

Then, each time you need to build the application, run the following command:

docker run --rm -it -v
$PWD
:/home/user/rustdesk -v rustdesk-git-cache:/home/user/.cargo/git -v rustdesk-registry-cache:/home/user/.cargo/registry -e PUID=
"
$(
id -u
)
"
 -e PGID=
"
$(
id -g
)
"
 rustdesk-builder

Note that the first build may take longer before dependencies are cached, subsequent builds will be faster. Additionally, if you need to specify different arguments to the build command, you may do so at the end of the command in the<OPTIONAL-ARGS>position. For instance, if you wanted to build an optimized release version, you would run the command above followed by--release. The resulting executable will be available in the target folder on your system, and can be run with:

target/debug/rustdesk

Or, if you're running a release executable:

target/release/rustdesk

Please ensure that you run these commands from the root of the RustDesk repository, or the application may not find the required resources. Also note that other cargo subcommands such asinstallorrunare not currently supported via this method as they would install or run the program inside the container instead of the host.

## File Structure

* libs/hbb_common: video codec, config, tcp/udp wrapper, protobuf, fs functions for file transfer, and some other utility functions
* libs/scrap: screen capture
* libs/enigo: platform specific keyboard/mouse control
* libs/clipboard: file copy and paste implementation for Windows, Linux, macOS.
* src/ui: obsolete Sciter UI (deprecated)
* src/server: audio/clipboard/input/video services, and network connections
* src/client.rs: start a peer connection
* src/rendezvous_mediator.rs: Communicate withrustdesk-server, wait for remote direct (TCP hole punching) or relayed connection
* src/platform: platform specific code
* flutter: Flutter code for desktop and mobile
* flutter/web/js: JavaScript for Flutter web client

## Screenshots

## About

An open-source remote desktop application designed for self-hosting, as an alternative to TeamViewer.

rustdesk.com

### Topics

 android

 windows

 macos

 linux

 dart

 rust

 ios

 remote-control

 p2p

 teamviewer

 rust-lang

 rdp

 remote-desktop

 vnc

 flutter

 flatpak

 wayland

 flutter-apps

 anydesk

### Resources

 Readme



### License

 AGPL-3.0 license


### Code of conduct

 Code of conduct


### Contributing

 Contributing


### Security policy

 Security policy


### Uh oh!

There was an error while loading.Please reload this page.





Activity


### Stars

112k

 stars


### Watchers

577

 watching


### Forks

16.7k

 forks


 Report repository



## Releases36

1.4.6

 Latest



Mar 5, 2026



+ 35 releases

## Sponsor this project

### Uh oh!

There was an error while loading.Please reload this page.






* ko-fi.com/rustdesk

Learn more about GitHub Sponsors

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.





## Contributors

### Uh oh!

There was an error while loading.Please reload this page.





## Languages

* Rust65.3%
* Dart25.6%
* C++2.0%
* Python1.8%
* C1.5%
* Kotlin1.4%
* Other2.4%
