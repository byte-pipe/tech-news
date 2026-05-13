---
title: 'GitHub - ArthurBrussee/brush: 3D Reconstruction for all · GitHub'
url: https://github.com/ArthurBrussee/brush
site_name: github
content_file: github-github-arthurbrusseebrush-3d-reconstruction-for-al
fetched_at: '2026-05-13T19:36:31.179854'
original_url: https://github.com/ArthurBrussee/brush
author: ArthurBrussee
description: 3D Reconstruction for all. Contribute to ArthurBrussee/brush development by creating an account on GitHub.
---

ArthurBrussee

 

/

brush

Public

* NotificationsYou must be signed in to change notification settings
* Fork231
* Star4.3k

 
 
 
 
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

1,155 Commits
1,155 Commits
.cargo
.cargo
 
 
.github
.github
 
 
.zed
.zed
 
 
apps
apps
 
 
crates
crates
 
 
.dockerignore
.dockerignore
 
 
.gitignore
.gitignore
 
 
CHANGELOG.md
CHANGELOG.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
_typos.toml
_typos.toml
 
 
brush_blueprint.rbl
brush_blueprint.rbl
 
 
deny.toml
deny.toml
 
 
dist-workspace.toml
dist-workspace.toml
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
View all files

## Repository files navigation

# Brush

BrushSizzleCompressedFrame.mp4

Massive thanks to@GradeEternafor the beautiful scenes

Brush is a 3D reconstruction engine usingGaussian splatting. It works on a wide range of systems:macOS/windows/linux,AMD/Nvidia/Intelcards,Android, and in abrowser. To achieve this, it uses WebGPU compatible tech and theBurnmachine learning framework.

Machine learning for real time rendering has tons of potential, but most ML tools don't work well with it: Rendering requires realtime interactivity, usually involve dynamic shapes & computations, don't run on most platforms, and it can be cumbersome to ship apps with large CUDA deps. Brush on the other hand produces simple dependency free binaries, runs on nearly all devices, without any setup.

Try the web demoNOTE: Only works on Chrome and Edge. Firefox and Safari are hopefully supported soon)

# Features

## Training

Brush takes in COLMAP data or datasets in the Nerfstudio format. Training is fully supported natively, on mobile, and in a browser. While training you can interact with the scene and see the training dynamics live, and compare the current rendering to input views as the training progresses.

It also supports masking images:

* Images with transparency. This will force the final splat to match the transparency of the input.
* A folder of images called 'masks'. This ignores parts of the image that are masked out.

## Viewer

Brush also works well as a splat viewer, including on the web. It can load .ply & .compressed.ply files. You can stream in data from a URL (for a web app, simply append?url=).

Brush also can load .zip of splat files to display them as an animation, or a special ply that includes delta frames (seecat-4DandCap4D!).

## CLI

Brush can be used as a CLI. Runbrush --helpto get an overview. Every CLI command can work with--with-viewerwhich also opens the UI, for easy debugging.

## Rerun

rerun_dash_compressed.mp4

While training, additional data can be visualized with the excellentrerun. To install rerun on your machine, please follow theirinstructions. Open the ./brush_blueprint.rbl in the viewer for best results.

## Building Brush

First install rust 1.88+. You can run tests withcargo test --all. Brush uses the wonderfulrerunfor additional visualizations while training, runcargo install rerun-cliif you want to use it.

### Windows/macOS/Linux

Usecargo run --releasefrom the workspace root to make an optimized build. Usecargo runto run a debug build.

### Web

Brush can be compiled to WASM. Runnpm run devto start the demo website using Next.js, see the web directory in app/brush-app/web.

Brush useswasm-packto build the WASM bundle. You can also use it without a bundler, seewasm-pack's documentation.

WebGPU is still an upcoming standard, and as such, only Chrome 134+ on Windows and macOS is currently supported.

### Android

As a one time setup, make sure you have the Android SDK & NDK installed.

* Check if ANDROID_NDK_HOME and ANDROID_HOME are set
* Add the Android target to rustrustup target add aarch64-linux-android
* Install cargo-ndk to manage building a libcargo install cargo-ndk

Each time you change the rust code, run

* cargo ndk -t arm64-v8a -o crates/brush-app/app/src/main/jniLibs/ build
* Nb: Nb, for best performance, build in release mode. This is separate
from the Android Studio app build configuration.
* cargo ndk -t arm64-v8a -o crates/brush-app/app/src/main/jniLibs/ build --release

You can now either run the project from Android Studio (Android Studio does NOT build the rust code), or run it from the command line:

./gradlew build
./gradlew installDebug
adb shell am start -n com.splats.app/.MainActivity

You can also open this folder as a project in Android Studio and run things from there. Nb: Running in Android Studio doesnotrebuild the rust code automatically.

## Benchmarks

Rendering and training are generally faster than gsplat. You can run benchmarks of some of the kernels usingcargo bench.

# Acknowledgements

gSplat, for their reference version of the kernels

Peter Hedman, George Kopanas & Bernhard Kerbl, for the many discussions & pointers.

The Burn team, for help & improvements to Burn along the way

Raph Levien, for theoriginal versionof the GPU radix sort.

GradeEterna, for feedback and their scenes.

# Disclaimer

This isnotan official Google product. This repository is a forked public version ofthe google-research repository

## About

3D Reconstruction for all

### Topics

 graphics

 reconstruction

 gaussian-splatting

### Resources

 Readme

 

### License

 Apache-2.0 license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

4.3k

 stars
 

### Watchers

66

 watching
 

### Forks

231

 forks
 

 Report repository

 

## Releases3

v0.3.0

 Latest

 

Sep 14, 2025

 

+ 2 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Rust94.6%
* TypeScript3.6%
* Python0.8%
* Java0.4%
* WGSL0.2%
* HTML0.2%
* Other0.2%