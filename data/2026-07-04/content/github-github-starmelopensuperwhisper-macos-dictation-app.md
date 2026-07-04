---
title: 'GitHub - Starmel/OpenSuperWhisper: macOS dictation app · GitHub'
url: https://github.com/Starmel/OpenSuperWhisper
site_name: github
content_file: github-github-starmelopensuperwhisper-macos-dictation-app
fetched_at: '2026-07-04T11:32:36.178268'
original_url: https://github.com/Starmel/OpenSuperWhisper
author: Starmel
description: macOS dictation app. Contribute to Starmel/OpenSuperWhisper development by creating an account on GitHub.
---

Starmel

 

/

OpenSuperWhisper

Public

* NotificationsYou must be signed in to change notification settings
* Fork144
* Star1.7k

 
 
 
 
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

185 Commits
185 Commits
.github
.github
 
 
.swiftpm/
xcode/
package.xcworkspace
.swiftpm/
xcode/
package.xcworkspace
 
 
OpenSuperWhisper.xcodeproj
OpenSuperWhisper.xcodeproj
 
 
OpenSuperWhisper
OpenSuperWhisper
 
 
OpenSuperWhisperTests
OpenSuperWhisperTests
 
 
OpenSuperWhisperUITests
OpenSuperWhisperUITests
 
 
Scripts
Scripts
 
 
asian-autocorrect @ 203fd5f
asian-autocorrect @ 203fd5f
 
 
docs
docs
 
 
libwhisper
libwhisper
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
Bridge.h
Bridge.h
 
 
Gemfile
Gemfile
 
 
Gemfile.lock
Gemfile.lock
 
 
LICENSE
LICENSE
 
 
Package.resolved
Package.resolved
 
 
Readme.md
Readme.md
 
 
ggml-tiny.en.bin
ggml-tiny.en.bin
 
 
jfk.wav
jfk.wav
 
 
make_release.sh
make_release.sh
 
 
notarize_app.sh
notarize_app.sh
 
 
run.sh
run.sh
 
 
View all files

## Repository files navigation

# OpenSuperWhisper

OpenSuperWhisper is a macOS application that provides real-time audio transcription using the Whisper model. It offers a seamless way to record and transcribe audio with customizable settings and keyboard shortcuts.

 

## Features

* 🎙️ Real-time audio recording and transcription
* 🧠 Two transcription engines:WhisperandParakeet— download models directly from the app
* ⌨️ Global keyboard shortcuts — key combination or single modifier key (e.g. Left ⌘, Right ⌥, Fn)
* ✊ Hold-to-record mode — hold the shortcut to record, release to stop
* 📁 Drag & drop audio files for transcription with queue processing
* 🎤 Microphone selection — switch between built-in, external, Bluetooth and iPhone (Apple Continuity) mics from the menu bar
* 🌍 Support for multiple languages with auto-detection
* 🇯🇵🇨🇳🇰🇷 Asian language autocorrect (autocorrect)

## Installation

brew update 
#
 Optional

brew install opensuperwhisper

Or fromGitHub releases page.

## Requirements

* macOS (Apple Silicon/ARM64)

## Support

If you encounter any issues or have questions, please:

1. Check the existing issues in the repository
2. Create a new issue with detailed information about your problem
3. Include system information and logs when reporting bugs

## Building locally

To build locally, you'll need:

git clone git@github.com:Starmel/OpenSuperWhisper.git
cd OpenSuperWhisper
git submodule update --init --recursive
brew install cmake libomp rust ruby
gem install xcpretty
./run.sh build

In case of problems, consult.github/workflows/build.ymlwhich is our CI workflow
where the app gets built automatically on GitHub's CI.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or create issues for bugs and feature requests.

### Contribution TODO list

* Streaming transcription
* Custom dictionary / keyword boosting (#19)
* Intel macOS compatibility (#15)
* Agent mode (#14)
* Background app (#8)
* Support long-press single key audio recording (#18)

## License

OpenSuperWhisper is licensed under the MIT License. See theLICENSEfile for details.

## Whisper Models

You can download Whisper model files (.bin) from theWhisper.cpp Hugging Face repository. Place the downloaded.binfiles in the app's models directory. On first launch, the app will attempt to copy a default model automatically, but you can add more models manually.

## About

macOS dictation app

### Topics

 macos

 dictation

 whisper

 parakeet

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

1.7k

 stars
 

### Watchers

10

 watching
 

### Forks

144

 forks
 

 Report repository

 

## Releases7

Release 0.1.0

 Latest

 

Mar 3, 2026

 

+ 6 releases

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Swift93.6%
* Shell6.2%
* Other0.2%