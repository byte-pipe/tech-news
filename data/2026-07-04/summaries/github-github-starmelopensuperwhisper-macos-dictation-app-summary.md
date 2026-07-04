---
title: GitHub - Starmel/OpenSuperWhisper: macOS dictation app · GitHub
url: https://github.com/Starmel/OpenSuperWhisper
date: 
site: github
model: llama3.2:1b
summarized_at: 2026-07-04T11:44:20.102198
---

# GitHub - Starmel/OpenSuperWhisper: macOS dictation app · GitHub

**Starmel/OpenSuperWhisper: macOS Dictation App**
=================================================

**Overview**
------------

OpenSuperWhisper is a macOS application that provides real-time audio transcription using the Whisper model. It offers a seamless way to record and transcribe audio with customizable settings and keyboard shortcuts.

**Key Features**
----------------

* Real-time audio recording and transcription
* Two transcription engines: Whisper and Parakeet ( downloadable models directly from the app)
* Global keyboard shortcuts:
 + Hold-to-record mode: holds the shortcut to record, releases to stop
 + Drag & drop audio files for transcription with queue processing
 + Switch between built-in, external, Bluetooth, and iPhone microphone connections from the menu bar

**Installation**
---------------

* `brew update` optional
* `brew install opensuperwhisper` (optional)

**Requirements**
----------------

* macOS (Apple Silicon/ARM64)

**Support**
------------

* Check existing issues in the repository [1]
* Create a new issue with detailed information about your problem [2]
* Include system information and logs when reporting bugs

**Building Locally**
--------------------

To build locally, you'll need:

```bash
git clone git@github.com:Starmel/OpenSuperWhisper.git
cd OpenSuperWhisper
git submodule update --init --recursive
brew install cmake libomp rust ruby
gem install xcpretty
./run.sh build
```

**Contributing**
----------------

Contributions are welcome! Please feel free to submit pull requests or create issues for bugs and feature requests.

**TODO List**

* Streaming transcription [3]
* Custom dictionary / keyword boost [4]

### TODO Notes:

[1] Repository issues page -> Search for "OpenSuperWhisper"

[2] GitHub repository URL -> "Issues" tab for reporting problems