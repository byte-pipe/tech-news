---
title: 'GitHub - openai/whisper: Robust Speech Recognition via Large-Scale Weak Supervision · GitHub'
url: https://github.com/openai/whisper
site_name: github
content_file: github-github-openaiwhisper-robust-speech-recognition-via
fetched_at: '2026-06-06T19:33:09.351264'
original_url: https://github.com/openai/whisper
author: openai
description: Robust Speech Recognition via Large-Scale Weak Supervision - openai/whisper
---

openai

 

/

whisper

Public

* NotificationsYou must be signed in to change notification settings
* Fork12.4k
* Star102k

 
 
 
 
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

168 Commits
168 Commits
.github
.github
 
 
data
data
 
 
notebooks
notebooks
 
 
tests
tests
 
 
whisper
whisper
 
 
.flake8
.flake8
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
CHANGELOG.md
CHANGELOG.md
 
 
LICENSE
LICENSE
 
 
MANIFEST.in
MANIFEST.in
 
 
README.md
README.md
 
 
approach.png
approach.png
 
 
language-breakdown.svg
language-breakdown.svg
 
 
model-card.md
model-card.md
 
 
pyproject.toml
pyproject.toml
 
 
requirements.txt
requirements.txt
 
 
View all files

## Repository files navigation

# Whisper

[Blog][Paper][Model card][Colab example]

Whisper is a general-purpose speech recognition model. It is trained on a large dataset of diverse audio and is also a multitasking model that can perform multilingual speech recognition, speech translation, and language identification.

## Approach

A Transformer sequence-to-sequence model is trained on various speech processing tasks, including multilingual speech recognition, speech translation, spoken language identification, and voice activity detection. These tasks are jointly represented as a sequence of tokens to be predicted by the decoder, allowing a single model to replace many stages of a traditional speech-processing pipeline. The multitask training format uses a set of special tokens that serve as task specifiers or classification targets.

## Setup

We used Python 3.9.9 andPyTorch1.10.1 to train and test our models, but the codebase is expected to be compatible with Python 3.8-3.11 and recent PyTorch versions. The codebase also depends on a few Python packages, most notablyOpenAI's tiktokenfor their fast tokenizer implementation. You can download and install (or update to) the latest release of Whisper with the following command:

pip install -U openai-whisper

Alternatively, the following command will pull and install the latest commit from this repository, along with its Python dependencies:

pip install git+https://github.com/openai/whisper.git 

To update the package to the latest version of this repository, please run:

pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git

It also requires the command-line toolffmpegto be installed on your system, which is available from most package managers:

#
 on Ubuntu or Debian

sudo apt update 
&&
 sudo apt install ffmpeg

#
 on Arch Linux

sudo pacman -S ffmpeg

#
 on MacOS using Homebrew (https://brew.sh/)

brew install ffmpeg

#
 on Windows using Chocolatey (https://chocolatey.org/)

choco install ffmpeg

#
 on Windows using Scoop (https://scoop.sh/)

scoop install ffmpeg

You may needrustinstalled as well, in casetiktokendoes not provide a pre-built wheel for your platform. If you see installation errors during thepip installcommand above, please follow theGetting started pageto install Rust development environment. Additionally, you may need to configure thePATHenvironment variable, e.g.export PATH="$HOME/.cargo/bin:$PATH". If the installation fails withNo module named 'setuptools_rust', you need to installsetuptools_rust, e.g. by running:

pip install setuptools-rust

## Available models and languages

There are six model sizes, four with English-only versions, offering speed and accuracy tradeoffs.
Below are the names of the available models and their approximate memory requirements and inference speed relative to the large model.
The relative speeds below are measured by transcribing English speech on a A100, and the real-world speed may vary significantly depending on many factors including the language, the speaking speed, and the available hardware.

Size

Parameters

English-only model

Multilingual model

Required VRAM

Relative speed

tiny

39 M

tiny.en

tiny

~1 GB

~10x

base

74 M

base.en

base

~1 GB

~7x

small

244 M

small.en

small

~2 GB

~4x

medium

769 M

medium.en

medium

~5 GB

~2x

large

1550 M

N/A

large

~10 GB

1x

turbo

809 M

N/A

turbo

~6 GB

~8x

The.enmodels for English-only applications tend to perform better, especially for thetiny.enandbase.enmodels. We observed that the difference becomes less significant for thesmall.enandmedium.enmodels.
Additionally, theturbomodel is an optimized version oflarge-v3that offers faster transcription speed with a minimal degradation in accuracy.

Whisper's performance varies widely depending on the language. The figure below shows a performance breakdown oflarge-v3andlarge-v2models by language, using WERs (word error rates) or CER (character error rates, shown inItalic) evaluated on the Common Voice 15 and Fleurs datasets. Additional WER/CER metrics corresponding to the other models and datasets can be found in Appendix D.1, D.2, and D.4 ofthe paper, as well as the BLEU (Bilingual Evaluation Understudy) scores for translation in Appendix D.3.

## Command-line usage

The following command will transcribe speech in audio files, using theturbomodel:

whisper audio.flac audio.mp3 audio.wav --model turbo

The default setting (which selects theturbomodel) works well for transcribing English. However,theturbomodel is not trained for translation tasks. If you need totranslate non-English speech into English, use one of themultilingual models(tiny,base,small,medium,large) instead ofturbo.

For example, to transcribe an audio file containing non-English speech, you can specify the language:

whisper japanese.wav --language Japanese

Totranslatespeech into English, use:

whisper japanese.wav --model medium --language Japanese --task translate

Note:Theturbomodel will return the original language even if--task translateis specified. Usemediumorlargefor the best translation results.

Run the following to view all available options:

whisper --help

Seetokenizer.pyfor the list of all available languages.

## Python usage

Transcription can also be performed within Python:

import
 
whisper

model
 
=
 
whisper
.
load_model
(
"turbo"
)

result
 
=
 
model
.
transcribe
(
"audio.mp3"
)

print
(
result
[
"text"
])

Internally, thetranscribe()method reads the entire file and processes the audio with a sliding 30-second window, performing autoregressive sequence-to-sequence predictions on each window.

Below is an example usage ofwhisper.detect_language()andwhisper.decode()which provide lower-level access to the model.

import
 
whisper

model
 
=
 
whisper
.
load_model
(
"turbo"
)

# load audio and pad/trim it to fit 30 seconds

audio
 
=
 
whisper
.
load_audio
(
"audio.mp3"
)

audio
 
=
 
whisper
.
pad_or_trim
(
audio
)

# make log-Mel spectrogram and move to the same device as the model

mel
 
=
 
whisper
.
log_mel_spectrogram
(
audio
, 
n_mels
=
model
.
dims
.
n_mels
).
to
(
model
.
device
)

# detect the spoken language

_
, 
probs
 
=
 
model
.
detect_language
(
mel
)

print
(
f"Detected language: 
{
max
(
probs
, 
key
=
probs
.
get
)
}
"
)

# decode the audio

options
 
=
 
whisper
.
DecodingOptions
()

result
 
=
 
whisper
.
decode
(
model
, 
mel
, 
options
)

# print the recognized text

print
(
result
.
text
)

## More examples

Please use the🙌 Show and tellcategory in Discussions for sharing more example usages of Whisper and third-party extensions such as web demos, integrations with other tools, ports for different platforms, etc.

## License

Whisper's code and model weights are released under the MIT License. SeeLICENSEfor further details.

## About

Robust Speech Recognition via Large-Scale Weak Supervision

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

102k

 stars
 

### Watchers

745

 watching
 

### Forks

12.4k

 forks
 

 Report repository

 

## Releases13

v20250625

 Latest

 

Jun 26, 2025

 

+ 12 releases

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python100.0%