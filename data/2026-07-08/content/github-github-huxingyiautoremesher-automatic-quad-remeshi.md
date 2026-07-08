---
title: 'GitHub - huxingyi/autoremesher: Automatic quad remeshing tool · GitHub'
url: https://github.com/huxingyi/autoremesher
site_name: github
content_file: github-github-huxingyiautoremesher-automatic-quad-remeshi
fetched_at: '2026-07-08T19:33:31.700489'
original_url: https://github.com/huxingyi/autoremesher
author: huxingyi
description: Automatic quad remeshing tool. Contribute to huxingyi/autoremesher development by creating an account on GitHub.
---

huxingyi

 

/

autoremesher

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork146
* Star1.9k

 
 
 
 
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

100 Commits
100 Commits
.github
.github
 
 
ci
ci
 
 
include/
AutoRemesher
include/
AutoRemesher
 
 
resources
resources
 
 
shaders
shaders
 
 
src
src
 
 
thirdparty
thirdparty
 
 
.clang-format
.clang-format
 
 
.gitignore
.gitignore
 
 
ACKNOWLEDGEMENTS.html
ACKNOWLEDGEMENTS.html
 
 
AUTHORS
AUTHORS
 
 
CHANGELOGS.md
CHANGELOGS.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SUPPORTERS
SUPPORTERS
 
 
autoremesher.icns
autoremesher.icns
 
 
autoremesher.pro
autoremesher.pro
 
 
autoremesher.rc
autoremesher.rc
 
 
favicon.ico
favicon.ico
 
 
resources.qrc
resources.qrc
 
 
View all files

## Repository files navigation

# AutoRemesher

AutoRemesher is a cross-platform automatic quad remeshing tool that converts high-polygon meshes into clean quad-based topology. It is built on top of libraries:Geogram,libigl,isotropicremesherandothers.

Buy me a coffee for staying up late coding :-)

## Getting Started

These instructions will get you a copy ofAutoRemesherup and running on your local machine for development.

### Prerequisites

* C++ compiler with C++14 support (GCC, Clang, or MSVC)
* Qt 5.15.2
* TBB (Intel Threading Building Blocks)
* CMake 3.12 or later (only needed on Windows to build TBB from source)

### Building

#### Linux (Ubuntu/Debian)

#
 Install Qt and build tools

sudo apt install build-essential qt5-qmake qtbase5-dev qttools5-dev-tools libqt5svg5-dev libqt5multimedia5-dev

#
 Install TBB and OpenGL

sudo apt install libtbb-dev libgl1-mesa-dev

#
 Clone and build

git clone https://github.com/huxingyi/autoremesher.git

cd
 autoremesher
qmake
make -j
$(
nproc
)

Fedora:sudo dnf install gcc-c++ qt5-qtbase-devel qt5-qttools-devel tbb-devel mesa-libGL-devel

#### Windows (Visual Studio 2022)

1. InstallVisual Studio 2022withDesktop development with C++workload.
2. InstallCMake(required to build TBB from source).
3. Install Qt 5.15.2 with theonline installer— select themsvc2019_64archive.
4. Open ax64 Native Tools Command Prompt for VS 2022and run:

::
 Build TBB from the bundled third-party source

cd
 thirdparty\tbb
cmake -B build2 
^

 -DTBB_BUILD_SHARED=ON 
^

 -DTBB_BUILD_STATIC=OFF 
^

 -DTBB_BUILD_TBBMALLOC=OFF 
^

 -DTBB_BUILD_TBBMALLOC_PROXY=OFF 
^

 -DTBB_BUILD_TESTS=OFF
cmake --build build2 --config Release

cd
 ..\..

::
 Build AutoRemesher

qmake -spec win32-msvc

set
 
CL
=
/MP
nmake -f Makefile.Release

The release binary will be atrelease\autoremesher.exe.

#### macOS

#
 Install Xcode Command Line Tools

xcode-select --install

#
 Install dependencies via Homebrew

brew install qt@5 tbb cmake

#
 Build

export
 PATH=
"
/usr/local/opt/qt@5/bin:
$PATH
"

git clone https://github.com/huxingyi/autoremesher.git

cd
 autoremesher
qmake CONFIG+=sdk_no_version_check
make -j
$(
sysctl -n hw.logicalcpu
)

### Running a quick test

AutoRemesher has a CLI mode for headless processing. Try it with one of thecommon-3d-test-models:

./autoremesher \
 --input armadillo.obj \
 --output remeshed.obj \
 --report remeshed_report.txt \
 --target-quads 50000 \
 --edge-scaling 1.0 \
 --sharp-edge 90.0 \
 --smooth-normal 0.0 \
 --adaptivity 1.0

### Quick Start

#### Windows

Downloadautoremesher-<version>-win32-x86_64.zipfromreleases, extract it and runautoremesher.exe.

#### macOS

Downloadautoremesher-<version>.dmgfromreleases.

For the first time, Apple will reject to run and popup something like "can't be opened because its integrity cannot be verified". Go to System Preferences > Security & Privacy > General and under "Allow apps downloaded from" click the button to allow it.

#### Linux

Downloadautoremesher-<version>.AppImagefromreleases.

$ chmod a+x ./autoremesher-<version>.AppImage
$ ./autoremesher-<version>.AppImage

### Links

* Check out open-source auto-retopology tool AutoRemeshercgchannel.com
* A New Open-Source Auto-Retopology Tool80.lv
* [Non-Blender] Autoremesher auto-retopology tool releasedblendernation.com
* オープンソースの新しいオートリメッシュツール Auto Remeshercginterest.com
* AutoRemesher 1.0.0-alpha - 超高速で高品質のクワッドポリゴン生成！Dust3D開発者によるオープンソースの自動リメッシュツール！3dnchu.com
* Open Source AutoRemesher releasedcgpress.org
* 「autoremesher」多角形を自動でリトポしてれる無料トポロジーツールmodelinghappy.com
* Open Source Auto Remesherblender-addons.org
* AutoRemesher | Auto-Retopology-Tooldigitalproduction.com
* Autoremesher open source auto-retopology toolblenderartists.org

## License

AutoRemesher is licensed under the MIT License - see theLICENSEfile for details.

## Acknowledgements

See the fullACKNOWLEDGEMENTSfor a list of libraries and resources used in this project.

## About

Automatic quad remeshing tool

autoremesher.dust3d.org

### Topics

 retopology

 quadremesh

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

1.9k

 stars
 

### Watchers

69

 watching
 

### Forks

146

 forks
 

 Report repository

 

## Releases7

1.0.0

 Latest

 

Jul 6, 2026

 

+ 6 releases

## Sponsor this project

 

 

 Sponsor

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

Learn more about GitHub Sponsors

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* C++65.6%
* HTML27.3%
* QMake3.8%
* GLSL2.3%
* Other1.0%