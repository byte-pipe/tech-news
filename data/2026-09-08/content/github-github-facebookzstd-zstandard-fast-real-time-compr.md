---
title: 'GitHub - facebook/zstd: Zstandard - Fast real-time compression algorithm · GitHub'
url: https://github.com/facebook/zstd
site_name: github
content_file: github-github-facebookzstd-zstandard-fast-real-time-compr
fetched_at: '2026-09-08T14:53:44.587401'
original_url: https://github.com/facebook/zstd
author: facebook
description: Zstandard - Fast real-time compression algorithm. Contribute to facebook/zstd development by creating an account on GitHub.
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 facebook

 

/

zstd

Public

* NotificationsYou must be signed in to change notification settings
* Fork2.6k
* Star27.7k

 
 
 
dev
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

11,495 Commits
11,495 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
build
build
 
 
contrib
contrib
 
 
doc
doc
 
 
examples
examples
 
 
lib
lib
 
 
programs
programs
 
 
tests
tests
 
 
zlibWrapper
zlibWrapper
 
 
.buckconfig
.buckconfig
 
 
.buckversion
.buckversion
 
 
.cirrus.yml
.cirrus.yml
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
CHANGELOG
CHANGELOG
 
 
CMakeLists.txt
CMakeLists.txt
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
COPYING
COPYING
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
Package.swift
Package.swift
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
TESTING.md
TESTING.md
 
 
View all files

## Repository files navigation

Zstandard, orzstdas short version, is a fast lossless compression algorithm,
targeting real-time compression scenarios at zlib-level and better compression ratios.
It's backed by a very fast entropy stage, provided byHuff0 and FSE library.

Zstandard's format is stable and documented inRFC8878. Multiple independent implementations are already available.
This repository represents the reference implementation, provided as an open-source dualBSDORGPLv2licensedClibrary,
and a command line utility producing and decoding.zst,.gz,.xzand.lz4files.
Should your project require another programming language,
a list of known ports and bindings is provided onZstandard homepage.

Development branch status:

## Benchmarks

For reference, several fast compression algorithms were tested and compared
on a desktop featuring a Core i7-9700K CPU @ 4.9GHz
and running Ubuntu 24.04 (Linux 6.8.0-53-generic),
usinglzbench, an open-source in-memory benchmark by @inikep
compiled withgcc14.2.0,
on theSilesia compression corpus.

Compressor name

Ratio

Compression

Decompress.

zstd 1.5.7 -1

2.896

510 MB/s

1550 MB/s

brotli 1.1.0 -1

2.883

290 MB/s

425 MB/s

zlib
 1.3.1 -1

2.743

105 MB/s

390 MB/s

zstd 1.5.7 --fast=1

2.439

545 MB/s

1850 MB/s

quicklz 1.5.0 -1

2.238

520 MB/s

750 MB/s

zstd 1.5.7 --fast=4

2.146

665 MB/s

2050 MB/s

lzo1x 2.10 -1

2.106

650 MB/s

780 MB/s

lz4
 1.10.0

2.101

675 MB/s

3850 MB/s

snappy 1.2.1

2.089

520 MB/s

1500 MB/s

lzf 3.6 -1

2.077

410 MB/s

820 MB/s

The negative compression levels, specified with--fast=#,
offer faster compression and decompression speed
at the cost of compression ratio.

Zstd can also offer stronger compression ratios at the cost of compression speed.
Speed vs Compression trade-off is configurable by small increments.
Decompression speed is preserved and remains roughly the same at all settings,
a property shared by most LZ compression algorithms, such aszlibor lzma.

The following tests were run
on a server running Linux Debian (Linux version 4.14.0-3-amd64)
with a Core i7-6700K CPU @ 4.0GHz,
usinglzbench, an open-source in-memory benchmark by @inikep
compiled withgcc7.3.0,
on theSilesia compression corpus.

Compression Speed vs Ratio

Decompression Speed

A few other algorithms can produce higher compression ratios at slower speeds, falling outside of the graph.
For a larger picture including slow modes,click on this link.

## The case for Small Data compression

Previous charts provide results applicable to typical file and stream scenarios (several MB). Small data comes with different perspectives.

The smaller the amount of data to compress, the more difficult it is to compress. This problem is common to all compression algorithms, and reason is, compression algorithms learn from past data how to compress future data. But at the beginning of a new data set, there is no "past" to build upon.

To solve this situation, Zstd offers atraining mode, which can be used to tune the algorithm for a selected type of data.
Training Zstandard is achieved by providing it with a few samples (one file per sample). The result of this training is stored in a file called "dictionary", which must be loaded before compression and decompression.
Using this dictionary, the compression ratio achievable on small data improves dramatically.

The following example uses thegithub-userssample set, created fromgithub public API.
It consists of roughly 10K records weighing about 1KB each.

Compression Ratio

Compression Speed

Decompression Speed

These compression gains are achieved while simultaneously providingfastercompression and decompression speeds.

Training works if there is some correlation in a family of small data samples. The more data-specific a dictionary is, the more efficient it is (there is nouniversal dictionary).
Hence, deploying one dictionary per type of data will provide the greatest benefits.
Dictionary gains are mostly effective in the first few KB. Then, the compression algorithm will gradually use previously decoded content to better compress the rest of the file.

### Dictionary compression How To:

1. Create the dictionaryzstd --train FullPathToTrainingSet/* -o dictionaryName
2. Compress with dictionaryzstd -D dictionaryName FILE
3. Decompress with dictionaryzstd -D dictionaryName --decompress FILE.zst

## Build instructions

makeis the main build system of this project.
It is the reference, and other build systems are periodically updated to stay compatible.
However, small drifts and feature differences can be present, since perfect synchronization is difficult.
For this reason, when your build system allows it, prefer employingmake.

### Makefile

Assuming your system supports standardmake(orgmake),
just invokingmakein root directory generateszstdcli at root,
and also generateslibzstdintolib/.

Other standard targets include:

* make install: install zstd cli, library and man pages
* make check: runzstd, test its essential behavior on local platform

TheMakefilefollows theGNU Standard Makefile conventions,
allowing staged install, standard compilation flags, directory variables and command variables.

For advanced use cases, specialized flags which control binary generation and installation paths are documented
inlib/README.mdfor thelibzstdlibrary
and inprograms/README.mdfor thezstdCLI.

### cmake

Acmakeproject generator is available for generating Makefiles or other build scripts
to create thezstdbinary as well aslibzstddynamic and static libraries.
The repository root now contains a minimalCMakeLists.txtthat forwards tobuild/cmake,
so you can configure the project with a standardcmake -S .invocation,
while the historicalcmake -S build/cmakeentry point remains fully supported.

cmake -S 
.
 -B build-cmake
cmake --build build-cmake

By default,CMAKE_BUILD_TYPEis set toRelease.

#### Support for Fat (Universal2) Output

zstdcan be built and installed with support for both Apple Silicon (M1/M2) as well as Intel by using CMake's Universal2 support.
To perform a Fat/Universal2 build and install use the following commands:

cmake -S 
.
 -B build-cmake-debug -G Ninja -DCMAKE_OSX_ARCHITECTURES=
"
x86_64;x86_64h;arm64
"

cd
 build-cmake-debug
ninja
sudo ninja install

### Meson

A Meson project is provided withinbuild/meson. Follow
build instructions in that directory.

You can also take a look at.travis.ymlfile for an
example about how Meson is used to build this project.

Note that default build type isrelease.

### VCPKG

You can build and install zstdvcpkgdependency manager:

git clone https://github.com/Microsoft/vcpkg.git
cd vcpkg
./bootstrap-vcpkg.sh
./vcpkg integrate install
./vcpkg install zstd

The zstd port in vcpkg is kept up to date by Microsoft team members and community contributors.
If the version is out of date, pleasecreate an issue or pull requeston the vcpkg repository.

### Conan

You can install pre-built binaries for zstd or build it from source usingConan. Use the following command:

conan install --requires=
"
zstd/[*]
"
 --build=missing

The zstd Conan recipe is kept up to date by Conan maintainers and community contributors.
If the version is out of date, pleasecreate an issue or pull requeston the ConanCenterIndex repository.

### Visual Studio (Windows)

Going intobuilddirectory, you will find additional possibilities:

* Projects for Visual Studio 2008 and 2010.VS2010 project is compatible with VS2012, VS2013, VS2015 and VS2017.
* VS2010 project is compatible with VS2012, VS2013, VS2015 and VS2017.
* Automated build scripts for Visual compiler by@KrzysFR, inbuild/VS_scripts,
which will buildzstdcli andlibzstdlibrary without any need to open Visual Studio solution.
* It is now recommended to generate Visual Studio solutions fromcmake

### Buck

You can build the zstd binary via buck by executing:buck build programs:zstdfrom the root of the repo.
The output binary will be inbuck-out/gen/programs/.

### Bazel

You can integrate zstd into your Bazel project by using the module hosted on theBazel Central Repository.

## Testing

You can run quick local smoke tests by runningmake check.
If you can't usemake, execute theplayTest.shscript from thesrc/testsdirectory.
Two env variables$ZSTD_BINand$DATAGEN_BINare needed for the test script to locate thezstdanddatagenbinary.
For information on CI testing, please refer toTESTING.md.

## Status

Zstandard is deployed within Meta and many other large cloud infrastructures,
to compress humongous amounts of data in various formats and use cases.
It is also continuously fuzzed for security issues by Google'soss-fuzzprogram.

## License

Zstandard is dual-licensed underBSDORGPLv2.

## Contributing

Thedevbranch is the one where all contributions are merged before reachingrelease.
Direct commit toreleaseare not permitted.
For more information, please readCONTRIBUTING.