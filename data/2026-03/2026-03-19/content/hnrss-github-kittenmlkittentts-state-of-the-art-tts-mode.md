---
title: 'GitHub - KittenML/KittenTTS: State-of-the-art TTS model under 25MB 😻 · GitHub'
url: https://github.com/KittenML/KittenTTS
site_name: hnrss
content_file: hnrss-github-kittenmlkittentts-state-of-the-art-tts-mode
fetched_at: '2026-03-19T19:23:41.405870'
original_url: https://github.com/KittenML/KittenTTS
date: '2026-03-19'
description: State-of-the-art TTS model under 25MB 😻 . Contribute to KittenML/KittenTTS development by creating an account on GitHub.
tags:
- hackernews
- hnrss
---

KittenML

 

/

KittenTTS

Public

* NotificationsYou must be signed in to change notification settings
* Fork637
* Star11.5k

 
 
 
 
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

28 Commits
28 Commits
kittentts
kittentts
 
 
.gitignore
.gitignore
 
 
LICENSE
LICENSE
 
 
MANIFEST.in
MANIFEST.in
 
 
README.md
README.md
 
 
example.py
example.py
 
 
output.wav
output.wav
 
 
pyproject.toml
pyproject.toml
 
 
requirements.txt
requirements.txt
 
 
setup.py
setup.py
 
 
View all files

## Repository files navigation

# Kitten TTS

New:Kitten TTS v0.8 is out -- 15M, 40M, and 80M parameter models now available.

Kitten TTS is an open-source, lightweight text-to-speech library built on ONNX. With models ranging from 15M to 80M parameters (25-80 MB on disk), it delivers high-quality voice synthesis on CPU without requiring a GPU.

Status:Developer preview -- APIs may change between releases.

Commercial support is available.For integration assistance, custom voices, or enterprise licensing,contact us.

## Table of Contents

* Features
* Available Models
* Demo
* Quick Start
* API Reference
* System Requirements
* Roadmap
* Commercial Support
* Community and Support
* License

## Features

* Ultra-lightweight-- Model sizes from 25 MB (int8) to 80 MB, suitable for edge deployment
* CPU-optimized-- ONNX-based inference runs efficiently without a GPU
* 8 built-in voices-- Bella, Jasper, Luna, Bruno, Rosie, Hugo, Kiki, and Leo
* Adjustable speech speed-- Control playback rate via thespeedparameter
* Text preprocessing-- Built-in pipeline handles numbers, currencies, units, and more
* 24 kHz output-- High-quality audio at a standard sample rate

## Available Models

Model

Parameters

Size

Download

kitten-tts-mini

80M

80 MB

KittenML/kitten-tts-mini-0.8

kitten-tts-micro

40M

41 MB

KittenML/kitten-tts-micro-0.8

kitten-tts-nano

15M

56 MB

KittenML/kitten-tts-nano-0.8

kitten-tts-nano (int8)

15M

25 MB

KittenML/kitten-tts-nano-0.8-int8

Note:Some users have reported issues with thekitten-tts-nano-0.8-int8model. If you encounter problems, pleaseopen an issue.

## Demo

final_vid.mp4

### Try it online

Try Kitten TTS directly in your browser onHugging Face Spaces.

## Quick Start

### Prerequisites

* Python 3.8 or later
* pip

### Installation

pip install https://github.com/KittenML/KittenTTS/releases/download/0.8.1/kittentts-0.8.1-py3-none-any.whl

### Basic Usage

from
 
kittentts
 
import
 
KittenTTS

model
 
=
 
KittenTTS
(
"KittenML/kitten-tts-mini-0.8"
)

audio
 
=
 
model
.
generate
(
"This high-quality TTS model runs without a GPU."
, 
voice
=
"Jasper"
)

import
 
soundfile
 
as
 
sf

sf
.
write
(
"output.wav"
, 
audio
, 
24000
)

### Advanced Usage

# Adjust speech speed (default: 1.0)

audio
 
=
 
model
.
generate
(
"Hello, world."
, 
voice
=
"Luna"
, 
speed
=
1.2
)

# Save directly to a file

model
.
generate_to_file
(
"Hello, world."
, 
"output.wav"
, 
voice
=
"Bruno"
, 
speed
=
0.9
)

# List available voices

print
(
model
.
available_voices
)

# ['Bella', 'Jasper', 'Luna', 'Bruno', 'Rosie', 'Hugo', 'Kiki', 'Leo']

## API Reference

### KittenTTS(model_name, cache_dir=None)

Load a model from Hugging Face Hub.

Parameter

Type

Default

Description

model_name

str

"KittenML/kitten-tts-nano-0.8"

Hugging Face repository ID

cache_dir

str

None

Local directory for caching downloaded model files

### model.generate(text, voice, speed, clean_text)

Synthesize speech from text, returning a NumPy array of audio samples at 24 kHz.

Parameter

Type

Default

Description

text

str

--

Input text to synthesize

voice

str

"expr-voice-5-m"

Voice name (see available voices)

speed

float

1.0

Speech speed multiplier

clean_text

bool

False

Preprocess text (expand numbers, currencies, etc.)

### model.generate_to_file(text, output_path, voice, speed, sample_rate, clean_text)

Synthesize speech and write directly to an audio file.

Parameter

Type

Default

Description

text

str

--

Input text to synthesize

output_path

str

--

Path to save the audio file

voice

str

"expr-voice-5-m"

Voice name

speed

float

1.0

Speech speed multiplier

sample_rate

int

24000

Audio sample rate in Hz

clean_text

bool

True

Preprocess text (expand numbers, currencies, etc.)

### model.available_voices

Returns a list of available voice names:['Bella', 'Jasper', 'Luna', 'Bruno', 'Rosie', 'Hugo', 'Kiki', 'Leo']

## System Requirements

* Operating system:Linux, macOS, or Windows
* Python:3.8 or later
* Hardware:Runs on CPU; no GPU required
* Disk space:25-80 MB depending on model variant

A virtual environment (conda, venv, or similar) is recommended to avoid dependency conflicts.

## Roadmap

* Release optimized inference engine
* Release mobile SDK
* Release higher quality TTS models
* Release multilingual TTS
* Release KittenASR
* Need anything else?Let us know

## Commercial Support

We offer commercial support for teams integrating Kitten TTS into their products. This includes integration assistance, custom voice development, and enterprise licensing.

Contact usor emailinfo@stellonlabs.comto discuss your requirements.

## Community and Support

* Discord:Join the community
* Website:kittenml.com
* Custom support:Request form
* Email:info@stellonlabs.com
* Issues:GitHub Issues

## License

This project is licensed under theApache License 2.0.

## About

State-of-the-art TTS model under 25MB 😻

### Resources

 Readme

 

### License

 Apache-2.0 license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

11.5k

 stars
 

### Watchers

114

 watching
 

### Forks

637

 forks
 

 Report repository

 

## Releases3

0.8.1

 Latest

 

Feb 24, 2026

 

+ 2 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors3

* stellon-admin
* therealronRohan Joshi
* divamguptaDivam Gupta

## Languages

* Python100.0%