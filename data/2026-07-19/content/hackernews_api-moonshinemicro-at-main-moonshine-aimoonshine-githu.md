---
title: moonshine/micro at main · moonshine-ai/moonshine · GitHub
url: https://github.com/moonshine-ai/moonshine/tree/main/micro
site_name: hackernews_api
content_file: hackernews_api-moonshinemicro-at-main-moonshine-aimoonshine-githu
fetched_at: '2026-07-19T11:27:29.648483'
original_url: https://github.com/moonshine-ai/moonshine/tree/main/micro
author: petewarden
date: '2026-07-14'
description: Very low latency speech to text, intent recognition, and text to speech, for building voice agents and interfaces - moonshine/micro at main · moonshine-ai/moonshine
tags:
- hackernews
- trending
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 moonshine-ai

 

/

moonshine

Public

* NotificationsYou must be signed in to change notification settings
* Fork491
* Star9.1k

 
 
 

## FilesExpand file tree

 
main
/

# micro

/
Copy path

## Directory actions

## More options

More options

## Directory actions

## More options

More options

## Latest commit

 

## History

History
History
 
main
/

# micro

/
Copy path
Top

## Folders and files

Name
Name
Last commit message
Last commit date

### parent directory

..
cmake
cmake
 
 
examples/
rp2350
examples/
rp2350
 
 
feature-generation
feature-generation
 
 
g2p
g2p
 
 
images
images
 
 
klatt-tts
klatt-tts
 
 
models
models
 
 
neural-tts
neural-tts
 
 
stt-training
stt-training
 
 
stt
stt
 
 
test-support
test-support
 
 
third-party
third-party
 
 
vad
vad
 
 
CMakeLists.txt
CMakeLists.txt
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
pico_sdk_import.cmake
pico_sdk_import.cmake
 
 
video-thumbnail.gif
video-thumbnail.gif
 
 
View all files

## README.md

Outline

# Moonshine Micro — Voice Interfaces for Microcontrollers

Moonshine Voiceis an open source AI toolkit for developers building real-time voice agents and applications. Moonshine Micro is a version designed specifically for embedded system processors like microcontrollers and DSPs, and uses the Raspberry Pi RP2350, which retails for just 80 cents, as its reference platform. It includesvoice-activity detection,command recognition, andneural speech synthesisand can run in as little as 470 KB of RAM.

You can see a full walkthrough in the video below:

The memory and compute requirements are designed to fit resource-constrained
systems. Figures below are forthe RP2350 demo; the
detailedmemory budgetbreaks each one down:

Component

Flash

SRAM (arena peak)

Compute

VAD (Voice Activity Detection)

~89 KiB

~36 KiB

~0.8 MMAC/frame (~25 MMAC/s)

STT (SpellingCNN Speech-to-Text)

~1.3 MiB

~346 KiB

~36 MMAC/s

TTS (neural diphone synth @ 16 kHz)

~1.8 MiB voice pack

~340 KiB

~37 MMAC typical reply (~65 MMAC/s out)

TOTAL (Demo pipeline)

~3.6 MiB

~468 KiB provisioned*

classify + speak ~0.7–1.0 s

Notes:

* Flash is.text+.rodatameasured witharm-none-eabi-sizeon the defaultmoonshine_micro_echofirmware (includes the embedded neural voice pack); SRAM is.bss+ heap + stacks.
* *VAD, STT, and neural TTS run sequentially and time-share one ~384 KiB TFLM arena, so SRAM is not additive — ~468 KiB is the total RAM provisioned on the 520 KiB RP2350 (wifi_hardware~491 KiB).
* A MAC is one multiply-accumulate; MMAC/s = millions per second during the active (non-idle) stage.

The code is released underthe permissive MIT License, suitable for commercial applications.

There's acomplete end-to-end exampleshowing how to set up a wifi connection on a microcontroller using voice on an RP2350 MCU.

The VAD, STT, and TTS libraries can be used independently of each other, relying on the includedTensorFlow Lite Microlibrary for the neural computations.

## Documentation

* Voice Activity Detection
* Speech to Text
* Custom Word Recognition
* Neural Text to Speech
* Wifi Setup Example

## License

This code, apart from the source inthird-party/, is licensed under the MIT
License — seeLICENSEin this directory (also at the repository root).

The SpellingCNN and TinyVadCNN models inmodels/are released under
the MIT License.

The code inthird-party/is licensed according to the terms of the open
source projects it originates from, with details in a LICENSE file in each
subfolder.