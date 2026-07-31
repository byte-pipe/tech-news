---
title: 'GitHub - erincatto/box3d: Box3D is a 3D physics engine for games · GitHub'
url: https://github.com/erincatto/box3d
site_name: github
content_file: github-github-erincattobox3d-box3d-is-a-3d-physics-engine
fetched_at: '2026-07-31T11:44:06.805585'
original_url: https://github.com/erincatto/box3d
author: erincatto
description: Box3D is a 3D physics engine for games. Contribute to erincatto/box3d development by creating an account on GitHub.
---

erincatto

 

/

box3d

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork281
* Star5.7k

 
 
 
main
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

38 Commits
38 Commits
.github
.github
 
 
benchmark
benchmark
 
 
data
data
 
 
docs
docs
 
 
extern/
sokol
extern/
sokol
 
 
include/
box3d
include/
box3d
 
 
samples
samples
 
 
shared
shared
 
 
src
src
 
 
test
test
 
 
.clang-format
.clang-format
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
CMakeLists.txt
CMakeLists.txt
 
 
CMakePresets.json
CMakePresets.json
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
build.sh
build.sh
 
 
build_vs2022.bat
build_vs2022.bat
 
 
build_vs2026.bat
build_vs2026.bat
 
 
deploy_docs.sh
deploy_docs.sh
 
 
View all files

## Repository files navigation

# Box3D

Box3D is a 3D physics engine for games.

## Features

### Collision

* Continuous collision detection
* Contact events
* Convex hulls, capsules, spheres, triangle meshes, and height fields
* Multiple shapes per body
* Collision filtering
* Ray casts, shape casts, and overlap queries
* Sensor system
* Character mover

### Physics

* RobustSoft Steprigid body solver
* Continuous physics for fast translations and rotations
* Island based sleep
* Revolute, prismatic, distance, motor, weld, and wheel joints
* Joint limits, motors, springs, and friction
* Joint and contact forces
* Body movement events and sleep notification

### System

* Data-oriented design
* Written in portable C17
* Extensive multithreading and SIMD
* Optimized for large piles of bodies
* Cross platform determinism
* Recording and replay

### Samples

* Uses sokol to run with D3D11 on Windows, Metal on macOS, and OpenGL 4.5 on Linux.
* Graphical user interface with imgui.
* Many samples to demonstrate features and performance.

## Building all platforms

* InstallCMake
* Installgit
* Ensure these run from the command line

## Building with CMake presets (recommended)

This uses the presets inCMakePresets.json.

* Windows:cmake --preset windowsthencmake --build --preset windows-release
* Linux:cmake --preset linux-releasethencmake --build --preset linux-release
* macOS:cmake --preset macosthencmake --build --preset macos-release
* Windows MinGW:cmake --preset mingw-releasethencmake --build --preset mingw-release

Run the samples app (must be in the Box3D directory).

* Windows:.\build\bin\Release\samples.exe
* Linux:./build/bin/samples
* macOS:./build/bin/Release/samples

## Building for Visual Studio

* InstallVisual Studio
* Runbuild_vs2026.bat
* Open and buildbuild/box3d.slnx

## Building for Linux

* Runbuild.shfrom a bash shell
* Results are in the build sub-folder

## Building for Xcode

* mkdir build
* cd build
* cmake -G Xcode ..
* Openbox3d.xcodeproj
* Select the samples scheme
* Build and run the samples

## Building for Web

* Emscripten SDK
* emcmake cmake -B build -DBOX3D_SAMPLES=OFF
* cmake --build build

Box3D uses SSE2 with WebAssembly. DefineBOX3D_DISABLE_SIMDto disable SSE2.

## Building and installing

* mkdir build
* cd build
* cmake ..
* cmake --build . --config Release
* cmake --install . (might need sudo)

## Using Box3D in your project

The core library has no dependencies beyond the C runtime (andlibmon Unix). Linking it
gives you thebox3d::box3dtarget.

I recommend to use FetchContent:

include
(
FetchContent
)

FetchContent_Declare
(box3d
 
GIT_REPOSITORY
 https://github.com/erincatto/box3d.git
 
GIT_TAG
 v0.1.0)

FetchContent_MakeAvailable
(box3d)

target_link_libraries
(
my_app
 
PRIVATE
 
box3d::box3d
)

For a vendored copy or git submodule, pointadd_subdirectoryat it:

add_subdirectory
(
extern/box3d
)

target_link_libraries
(
my_app
 
PRIVATE
 
box3d::box3d
)

To use a copy installed withcmake --install, find the package:

find_package
(
box3d
 
0.1
 
REQUIRED
)

target_link_libraries
(
my_app
 
PRIVATE
 
box3d::box3d
)

Seedocs/hello.mdfor a minimal first program.

## Compatibility

The Box3D library and samples build and run on Windows, Linux, and Mac.

You will need a compiler that supports C17 to build the Box3D library.

You will need a compiler that supports C++20 to build the samples.

Box3D uses SSE2 and Neon SIMD math to improve performance. SIMD can be disabled by definingBOX3D_DISABLE_SIMD.

## Documentation

The user manual lives indocs/and is built with Doxygen. Enable theBOX3D_DOCSCMake option and build thedoctarget.

## Community

* Discord

## Contributing

Pull requests are currently disabled. Instead, please file an issue for bugs or feature requests. For support, please visit the Discord server.

## Giving feedback

Please file an issue or start a chat on discord. You can also useGitHub Discussions.

## License

Box3D is developed by Erin Catto and uses theMIT license.

## Sponsorship

Support development of Box3D throughGithub Sponsors.

Please consider starring this repository and subscribing to myYouTube channel.

## LLM Usage

LLMs are used in the following areas:

* unit tests
* samples app
* migrating code between Box2D and Box3D
* build configuration
* code reviews
* benchmarking

Elsewhere all code is developed and written by me. I take responsibility for every line of code in Box2D/3D.