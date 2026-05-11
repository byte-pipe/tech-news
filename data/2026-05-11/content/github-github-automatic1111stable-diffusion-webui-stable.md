---
title: 'GitHub - AUTOMATIC1111/stable-diffusion-webui: Stable Diffusion web UI · GitHub'
url: https://github.com/AUTOMATIC1111/stable-diffusion-webui
site_name: github
content_file: github-github-automatic1111stable-diffusion-webui-stable
fetched_at: '2026-05-11T13:46:41.694683'
original_url: https://github.com/AUTOMATIC1111/stable-diffusion-webui
author: AUTOMATIC1111
description: Stable Diffusion web UI. Contribute to AUTOMATIC1111/stable-diffusion-webui development by creating an account on GitHub.
---

AUTOMATIC1111

 

/

stable-diffusion-webui

Public

* NotificationsYou must be signed in to change notification settings
* Fork30.3k
* Star163k

 
 
 
 
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

7,689 Commits
7,689 Commits
.github
.github
 
 
configs
configs
 
 
embeddings
embeddings
 
 
extensions-builtin
extensions-builtin
 
 
extensions
extensions
 
 
html
html
 
 
javascript
javascript
 
 
localizations
localizations
 
 
models
models
 
 
modules
modules
 
 
scripts
scripts
 
 
test
test
 
 
textual_inversion_templates
textual_inversion_templates
 
 
.eslintignore
.eslintignore
 
 
.eslintrc.js
.eslintrc.js
 
 
.git-blame-ignore-revs
.git-blame-ignore-revs
 
 
.gitignore
.gitignore
 
 
.pylintrc
.pylintrc
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CITATION.cff
CITATION.cff
 
 
CODEOWNERS
CODEOWNERS
 
 
LICENSE.txt
LICENSE.txt
 
 
README.md
README.md
 
 
_typos.toml
_typos.toml
 
 
environment-wsl2.yaml
environment-wsl2.yaml
 
 
launch.py
launch.py
 
 
package.json
package.json
 
 
pyproject.toml
pyproject.toml
 
 
requirements-test.txt
requirements-test.txt
 
 
requirements.txt
requirements.txt
 
 
requirements_npu.txt
requirements_npu.txt
 
 
requirements_versions.txt
requirements_versions.txt
 
 
screenshot.png
screenshot.png
 
 
script.js
script.js
 
 
style.css
style.css
 
 
webui-macos-env.sh
webui-macos-env.sh
 
 
webui-user.bat
webui-user.bat
 
 
webui-user.sh
webui-user.sh
 
 
webui.bat
webui.bat
 
 
webui.py
webui.py
 
 
webui.sh
webui.sh
 
 
View all files

## Repository files navigation

# Stable Diffusion web UI

A web interface for Stable Diffusion, implemented using Gradio library.

## Features

Detailed feature showcase with images:

* Original txt2img and img2img modes
* One click install and run script (but you still must install python and git)
* Outpainting
* Inpainting
* Color Sketch
* Prompt Matrix
* Stable Diffusion Upscale
* Attention, specify parts of text that the model should pay more attention toa man in a((tuxedo))- will pay more attention to tuxedoa man in a(tuxedo:1.21)- alternative syntaxselect text and pressCtrl+UporCtrl+Down(orCommand+UporCommand+Downif you're on a MacOS) to automatically adjust attention to selected text (code contributed by anonymous user)
* a man in a((tuxedo))- will pay more attention to tuxedo
* a man in a(tuxedo:1.21)- alternative syntax
* select text and pressCtrl+UporCtrl+Down(orCommand+UporCommand+Downif you're on a MacOS) to automatically adjust attention to selected text (code contributed by anonymous user)
* Loopback, run img2img processing multiple times
* X/Y/Z plot, a way to draw a 3 dimensional plot of images with different parameters
* Textual Inversionhave as many embeddings as you want and use any names you like for themuse multiple embeddings with different numbers of vectors per tokenworks with half precision floating point numberstrain embeddings on 8GB (also reports of 6GB working)
* have as many embeddings as you want and use any names you like for them
* use multiple embeddings with different numbers of vectors per token
* works with half precision floating point numbers
* train embeddings on 8GB (also reports of 6GB working)
* Extras tab with:GFPGAN, neural network that fixes facesCodeFormer, face restoration tool as an alternative to GFPGANRealESRGAN, neural network upscalerESRGAN, neural network upscaler with a lot of third party modelsSwinIR and Swin2SR (see here), neural network upscalersLDSR, Latent diffusion super resolution upscaling
* GFPGAN, neural network that fixes faces
* CodeFormer, face restoration tool as an alternative to GFPGAN
* RealESRGAN, neural network upscaler
* ESRGAN, neural network upscaler with a lot of third party models
* SwinIR and Swin2SR (see here), neural network upscalers
* LDSR, Latent diffusion super resolution upscaling
* Resizing aspect ratio options
* Sampling method selectionAdjust sampler eta values (noise multiplier)More advanced noise setting options
* Adjust sampler eta values (noise multiplier)
* More advanced noise setting options
* Interrupt processing at any time
* 4GB video card support (also reports of 2GB working)
* Correct seeds for batches
* Live prompt token length validation
* Generation parametersparameters you used to generate images are saved with that imagein PNG chunks for PNG, in EXIF for JPEGcan drag the image to PNG info tab to restore generation parameters and automatically copy them into UIcan be disabled in settingsdrag and drop an image/text-parameters to promptbox
* parameters you used to generate images are saved with that image
* in PNG chunks for PNG, in EXIF for JPEG
* can drag the image to PNG info tab to restore generation parameters and automatically copy them into UI
* can be disabled in settings
* drag and drop an image/text-parameters to promptbox
* Read Generation Parameters Button, loads parameters in promptbox to UI
* Settings page
* Running arbitrary python code from UI (must run with--allow-codeto enable)
* Mouseover hints for most UI elements
* Possible to change defaults/mix/max/step values for UI elements via text config
* Tiling support, a checkbox to create images that can be tiled like textures
* Progress bar and live image generation previewCan use a separate neural network to produce previews with almost none VRAM or compute requirement
* Can use a separate neural network to produce previews with almost none VRAM or compute requirement
* Negative prompt, an extra text field that allows you to list what you don't want to see in generated image
* Styles, a way to save part of prompt and easily apply them via dropdown later
* Variations, a way to generate same image but with tiny differences
* Seed resizing, a way to generate same image but at slightly different resolution
* CLIP interrogator, a button that tries to guess prompt from an image
* Prompt Editing, a way to change prompt mid-generation, say to start making a watermelon and switch to anime girl midway
* Batch Processing, process a group of files using img2img
* Img2img Alternative, reverse Euler method of cross attention control
* Highres Fix, a convenience option to produce high resolution pictures in one click without usual distortions
* Reloading checkpoints on the fly
* Checkpoint Merger, a tab that allows you to merge up to 3 checkpoints into one
* Custom scriptswith many extensions from community
* Composable-Diffusion, a way to use multiple prompts at onceseparate prompts using uppercaseANDalso supports weights for prompts:a cat :1.2 AND a dog AND a penguin :2.2
* separate prompts using uppercaseAND
* also supports weights for prompts:a cat :1.2 AND a dog AND a penguin :2.2
* No token limit for prompts (original stable diffusion lets you use up to 75 tokens)
* DeepDanbooru integration, creates danbooru style tags for anime prompts
* xformers, major speed increase for select cards: (add--xformersto commandline args)
* via extension:History tab: view, direct and delete images conveniently within the UI
* Generate forever option
* Training tabhypernetworks and embeddings optionsPreprocessing images: cropping, mirroring, autotagging using BLIP or deepdanbooru (for anime)
* hypernetworks and embeddings options
* Preprocessing images: cropping, mirroring, autotagging using BLIP or deepdanbooru (for anime)
* Clip skip
* Hypernetworks
* Loras (same as Hypernetworks but more pretty)
* A separate UI where you can choose, with preview, which embeddings, hypernetworks or Loras to add to your prompt
* Can select to load a different VAE from settings screen
* Estimated completion time in progress bar
* API
* Support for dedicatedinpainting modelby RunwayML
* via extension:Aesthetic Gradients, a way to generate images with a specific aesthetic by using clip images embeds (implementation ofhttps://github.com/vicgalle/stable-diffusion-aesthetic-gradients)
* Stable Diffusion 2.0support - seewikifor instructions
* Alt-Diffusionsupport - seewikifor instructions
* Now without any bad letters!
* Load checkpoints in safetensors format
* Eased resolution restriction: generated image's dimensions must be a multiple of 8 rather than 64
* Now with a license!
* Reorder elements in the UI from settings screen
* Segmind Stable Diffusionsupport

## Installation and Running

Make sure the requireddependenciesare met and follow the instructions available for:

* NVidia(recommended)
* AMDGPUs.
* Intel CPUs, Intel GPUs (both integrated and discrete)(external wiki page)
* Ascend NPUs(external wiki page)

Alternatively, use online services (like Google Colab):

* List of Online Services

### Installation on Windows 10/11 with NVidia-GPUs using release package

1. Downloadsd.webui.zipfromv1.0.0-preand extract its contents.
2. Runupdate.bat.
3. Runrun.bat.

For more details seeInstall-and-Run-on-NVidia-GPUs

### Automatic Installation on Windows

1. InstallPython 3.10.6(Newer version of Python does not support torch), checking "Add Python to PATH".
2. Installgit.
3. Download the stable-diffusion-webui repository, for example by runninggit clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git.
4. Runwebui-user.batfrom Windows Explorer as normal, non-administrator, user.

### Automatic Installation on Linux

1. Install the dependencies:

#
 Debian-based:

sudo apt install wget git python3 python3-venv libgl1 libglib2.0-0

#
 Red Hat-based:

sudo dnf install wget git python3 gperftools-libs libglvnd-glx

#
 openSUSE-based:

sudo zypper install wget git python3 libtcmalloc4 libglvnd

#
 Arch-based:

sudo pacman -S wget git python3

If your system is very new, you need to install python3.11 or python3.10:

#
 Ubuntu 24.04

sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.11

#
 Manjaro/Arch

sudo pacman -S yay
yay -S python311 
#
 do not confuse with python3.11 package

#
 Only for 3.11

#
 Then set up env variable in launch script

export
 python_cmd=
"
python3.11
"

#
 or in webui-user.sh

python_cmd=
"
python3.11
"

1. Navigate to the directory you would like the webui to be installed and execute the following command:

wget -q https://raw.githubusercontent.com/AUTOMATIC1111/stable-diffusion-webui/master/webui.sh

Or just clone the repo wherever you want:

git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui

1. Runwebui.sh.
2. Checkwebui-user.shfor options.

### Installation on Apple Silicon

Find the instructionshere.

## Contributing

Here's how to add code to this repo:Contributing

## Documentation

The documentation was moved from this README over to the project'swiki.

For the purposes of getting Google and other search engines to crawl the wiki, here's a link to the (not for humans)crawlable wiki.

## Credits

Licenses for borrowed code can be found inSettings -> Licensesscreen, and also inhtml/licenses.htmlfile.

* Stable Diffusion -https://github.com/Stability-AI/stablediffusion,https://github.com/CompVis/taming-transformers,https://github.com/mcmonkey4eva/sd3-ref
* k-diffusion -https://github.com/crowsonkb/k-diffusion.git
* Spandrel -https://github.com/chaiNNer-org/spandrelimplementingGFPGAN -https://github.com/TencentARC/GFPGAN.gitCodeFormer -https://github.com/sczhou/CodeFormerESRGAN -https://github.com/xinntao/ESRGANSwinIR -https://github.com/JingyunLiang/SwinIRSwin2SR -https://github.com/mv-lab/swin2sr
* GFPGAN -https://github.com/TencentARC/GFPGAN.git
* CodeFormer -https://github.com/sczhou/CodeFormer
* ESRGAN -https://github.com/xinntao/ESRGAN
* SwinIR -https://github.com/JingyunLiang/SwinIR
* Swin2SR -https://github.com/mv-lab/swin2sr
* LDSR -https://github.com/Hafiidz/latent-diffusion
* MiDaS -https://github.com/isl-org/MiDaS
* Ideas for optimizations -https://github.com/basujindal/stable-diffusion
* Cross Attention layer optimization - Doggettx -https://github.com/Doggettx/stable-diffusion, original idea for prompt editing.
* Cross Attention layer optimization - InvokeAI, lstein -https://github.com/invoke-ai/InvokeAI(originallyhttp://github.com/lstein/stable-diffusion)
* Sub-quadratic Cross Attention layer optimization - Alex Birch (Birch-san/diffusers#1), Amin Rezaei (https://github.com/AminRezaei0x443/memory-efficient-attention)
* Textual Inversion - Rinon Gal -https://github.com/rinongal/textual_inversion(we're not using his code, but we are using his ideas).
* Idea for SD upscale -https://github.com/jquesnelle/txt2imghd
* Noise generation for outpainting mk2 -https://github.com/parlance-zz/g-diffuser-bot
* CLIP interrogator idea and borrowing some code -https://github.com/pharmapsychotic/clip-interrogator
* Idea for Composable Diffusion -https://github.com/energy-based-model/Compositional-Visual-Generation-with-Composable-Diffusion-Models-PyTorch
* xformers -https://github.com/facebookresearch/xformers
* DeepDanbooru - interrogator for anime diffusershttps://github.com/KichangKim/DeepDanbooru
* Sampling in float32 precision from a float16 UNet - marunine for the idea, Birch-san for the example Diffusers implementation (https://github.com/Birch-san/diffusers-play/tree/92feee6)
* Instruct pix2pix - Tim Brooks (star), Aleksander Holynski (star), Alexei A. Efros (no star) -https://github.com/timothybrooks/instruct-pix2pix
* Security advice - RyotaK
* UniPC sampler - Wenliang Zhao -https://github.com/wl-zhao/UniPC
* TAESD - Ollin Boer Bohan -https://github.com/madebyollin/taesd
* LyCORIS - KohakuBlueleaf
* Restart sampling - lambertae -https://github.com/Newbeeer/diffusion_restart_sampling
* Hypertile - tfernd -https://github.com/tfernd/HyperTile
* Initial Gradio script - posted on 4chan by an Anonymous user. Thank you Anonymous user.
* (You)

## About

Stable Diffusion web UI

### Topics

 web

 ai

 deep-learning

 torch

 pytorch

 unstable

 image-generation

 gradio

 diffusion

 upscaling

 text2image

 image2image

 img2img

 ai-art

 txt2img

 stable-diffusion

### Resources

 Readme

 

### License

 AGPL-3.0 license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

163k

 stars
 

### Watchers

1.2k

 watching
 

### Forks

30.3k

 forks
 

 Report repository

 

## Releases27

1.10.1

 Latest

 

Feb 9, 2025

 

+ 26 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python87.5%
* JavaScript8.4%
* CSS2.1%
* HTML1.3%
* Other0.7%