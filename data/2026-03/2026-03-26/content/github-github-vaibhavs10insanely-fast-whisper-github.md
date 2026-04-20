---
title: GitHub - Vaibhavs10/insanely-fast-whisper · GitHub
url: https://github.com/Vaibhavs10/insanely-fast-whisper
site_name: github
content_file: github-github-vaibhavs10insanely-fast-whisper-github
fetched_at: '2026-03-26T11:22:34.928626'
original_url: https://github.com/Vaibhavs10/insanely-fast-whisper
author: Vaibhavs10
description: Contribute to Vaibhavs10/insanely-fast-whisper development by creating an account on GitHub.
---

Vaibhavs10



/

insanely-fast-whisper

Public

* NotificationsYou must be signed in to change notification settings
* Fork775
* Star10.6k




 
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

180 Commits
180 Commits
notebooks
notebooks
 
 
src/
insanely_fast_whisper
src/
insanely_fast_whisper
 
 
tests
tests
 
 
.gitignore
.gitignore
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
convert_output.py
convert_output.py
 
 
insanely_fast_whisper_colab.ipynb
insanely_fast_whisper_colab.ipynb
 
 
pdm.lock
pdm.lock
 
 
pyproject.toml
pyproject.toml
 
 
View all files

## Repository files navigation

# Insanely Fast Whisper

An opinionated CLI to transcribe Audio files w/ Whisper on-device! Powered by 🤗Transformers,Optimum&flash-attn

TL;DR- Transcribe150minutes (2.5 hours) of audio in less than98seconds - withOpenAI's Whisper Large v3. Blazingly fast transcription is now a reality!⚡️

pipx install insanely-fast-whisper==0.0.15 --force

Not convinced? Here are some benchmarks we ran on a Nvidia A100 - 80GB 👇

Optimisation type

Time to Transcribe (150 mins of Audio)

large-v3 (Transformers) (
fp32
)

~31 (
31 min 1 sec
)

large-v3 (Transformers) (
fp16
 +
batching [24]
 +
bettertransformer
)

~5 (
5 min 2 sec
)

large-v3 (Transformers) (
fp16
 +
batching [24]
 +
Flash Attention 2
)

~2 (
1 min 38 sec
)

distil-large-v2 (Transformers) (
fp16
 +
batching [24]
 +
bettertransformer
)

~3 (
3 min 16 sec
)

distil-large-v2 (Transformers) (
fp16
 +
batching [24]
 +
Flash Attention 2
)

~1 (
1 min 18 sec
)

large-v2 (Faster Whisper) (
fp16
 +
beam_size [1]
)

~9.23 (
9 min 23 sec
)

large-v2 (Faster Whisper) (
8-bit
 +
beam_size [1]
)

~8 (
8 min 15 sec
)

P.S. We also ran the benchmarks on aGoogle Colab T4 GPUinstance too!

P.P.S. This project originally started as a way to showcase benchmarks for Transformers, but has since evolved into a lightweight CLI for people to use. This is purely community driven. We add whatever community seems to have a strong demand for!

## 🆕 Blazingly fast transcriptions via your terminal! ⚡️

We've added a CLI to enable fast transcriptions. Here's how you can use it:

Installinsanely-fast-whisperwithpipx(pip install pipxorbrew install pipx):

pipx install insanely-fast-whisper

⚠️If you have python 3.11.XX installed,pipxmay parse the version incorrectly and install a very old version ofinsanely-fast-whisperwithout telling you (version0.0.8, which won't work anymore with the currentBetterTransformers). In that case, you can install the latest version by passing--ignore-requires-pythontopip:

pipx install insanely-fast-whisper --force --pip-args=
"
--ignore-requires-python
"

If you're installing withpip, you can pass the argument directly:pip install insanely-fast-whisper --ignore-requires-python.

Run inference from any path on your computer:

insanely-fast-whisper --file-name
<
filename or URL
>

Note: if you are running on macOS, you also need to add--device-id mpsflag.

🔥 You can runWhisper-large-v3w/Flash Attention 2from this CLI too:

insanely-fast-whisper --file-name
<
filename or URL
>
 --flash True

🌟 You can rundistil-whisperdirectly from this CLI too:

insanely-fast-whisper --model-name distil-whisper/large-v2 --file-name
<
filename or URL
>


Don't want to installinsanely-fast-whisper? Just usepipx run:

pipx run insanely-fast-whisper --file-name
<
filename or URL
>

Note

The CLI is highly opinionated and only works on NVIDIA GPUs & Mac. Make sure to check out the defaults and the list of options you can play around with to maximise your transcription throughput. Runinsanely-fast-whisper --helporpipx run insanely-fast-whisper --helpto get all the CLI arguments along with their defaults.

## CLI Options

Theinsanely-fast-whisperrepo provides an all round support for running Whisper in various settings. Note that as of today 26th Nov,insanely-fast-whisperworks on both CUDA and mps (mac) enabled devices.

 -h, --help show this help message and exit
 --file-name FILE_NAME
 Path or URL to the audio file to be transcribed.
 --device-id DEVICE_ID
 Device ID for your GPU. Just pass the device number when using CUDA, or "mps" for Macs with Apple Silicon. (default: "0")
 --transcript-path TRANSCRIPT_PATH
 Path to save the transcription output. (default: output.json)
 --model-name MODEL_NAME
 Name of the pretrained model/ checkpoint to perform ASR. (default: openai/whisper-large-v3)
 --task {transcribe,translate}
 Task to perform: transcribe or translate to another language. (default: transcribe)
 --language LANGUAGE
 Language of the input audio. (default: "None" (Whisper auto-detects the language))
 --batch-size BATCH_SIZE
 Number of parallel batches you want to compute. Reduce if you face OOMs. (default: 24)
 --flash FLASH
 Use Flash Attention 2. Read the FAQs to see how to install FA2 correctly. (default: False)
 --timestamp {chunk,word}
 Whisper supports both chunked as well as word level timestamps. (default: chunk)
 --hf-token HF_TOKEN
 Provide a hf.co/settings/token for Pyannote.audio to diarise the audio clips
 --diarization_model DIARIZATION_MODEL
 Name of the pretrained model/ checkpoint to perform diarization. (default: pyannote/speaker-diarization)
 --num-speakers NUM_SPEAKERS
 Specifies the exact number of speakers present in the audio file. Useful when the exact number of participants in the conversation is known. Must be at least 1. Cannot be used together with --min-speakers or --max-speakers. (default: None)
 --min-speakers MIN_SPEAKERS
 Sets the minimum number of speakers that the system should consider during diarization. Must be at least 1. Cannot be used together with --num-speakers. Must be less than or equal to --max-speakers if both are specified. (default: None)
 --max-speakers MAX_SPEAKERS
 Defines the maximum number of speakers that the system should consider in diarization. Must be at least 1. Cannot be used together with --num-speakers. Must be greater than or equal to --min-speakers if both are specified. (default: None)

## Frequently Asked Questions

How to correctly install flash-attn to make it work withinsanely-fast-whisper?

Make sure to install it viapipx runpip insanely-fast-whisper install flash-attn --no-build-isolation. Massive kudos to @li-yifei for helping with this.

How to solve anAssertionError: Torch not compiled with CUDA enablederror on Windows?

The root cause of this problem is still unknown, however, you can resolve this by manually installing torch in the virtualenv likepython -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121. Thanks to @pto2k for all tdebugging this.

How to avoid Out-Of-Memory (OOM) exceptions on Mac?

Thempsbackend isn't as optimised as CUDA, hence is way more memory hungry. Typically you can run with--batch-size 4without any issues (should use roughly 12GB GPU VRAM). Don't forget to set--device-id mps.

## How to use Whisper without a CLI?

All you need to run is the below snippet:

pip install --upgrade transformers optimum accelerate

import

torch

from

transformers

import

pipeline

from

transformers
.
utils

import

is_flash_attn_2_available

pipe

=

pipeline
(

"automatic-speech-recognition"
,

model
=
"openai/whisper-large-v3"
,
# select checkpoint from https://huggingface.co/openai/whisper-large-v3#model-details


torch_dtype
=
torch
.
float16
,

device
=
"cuda:0"
,
# or mps for Mac devices


model_kwargs
=
{
"attn_implementation"
:
"flash_attention_2"
}
if

is_flash_attn_2_available
()
else
 {
"attn_implementation"
:
"sdpa"
},
)

outputs

=

pipe
(

"<FILE_NAME>"
,

chunk_length_s
=
30
,

batch_size
=
24
,

return_timestamps
=
True
,
)

outputs

## Acknowledgements

1. OpenAI Whisperteam for open sourcing such a brilliant check point.
2. Hugging Face Transformers team, specificallyArthur,Patrick,Sanchit&Yoach(alphabetical order) for continuing to maintain Whisper in Transformers.
3. Hugging FaceOptimumteam for making the BetterTransformer API so easily accessible.
4. Patrick Arminiofor helping me tremendously to put together this CLI.

## Community showcase

1. @ochen1 created a brilliant MVP for a CLI here:https://github.com/ochen1/insanely-fast-whisper-cli(Try it out now!)
2. @arihanv created an app (Shush) using NextJS (Frontend) & Modal (Backend):https://github.com/arihanv/Shush(Check it outtt!)
3. @kadirnar created a python package on top of the transformers with optimisations:https://github.com/kadirnar/whisper-plus(Go go go!!!)

## About

 No description, website, or topics provided.


### Resources

 Readme



### License

 Apache-2.0 license


### Uh oh!

There was an error while loading.Please reload this page.





Activity


### Stars

10.6k

 stars


### Watchers

79

 watching


### Forks

775

 forks


 Report repository



## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.





### Uh oh!

There was an error while loading.Please reload this page.





## Contributors

### Uh oh!

There was an error while loading.Please reload this page.





## Languages

* Jupyter Notebook98.4%
* Python1.6%
