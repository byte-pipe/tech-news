---
title: 'GitHub - deepfakes/faceswap: Deepfakes Software For All · GitHub'
url: https://github.com/deepfakes/faceswap
site_name: github
content_file: github-github-deepfakesfaceswap-deepfakes-software-for-al
fetched_at: '2026-07-29T11:46:58.143441'
original_url: https://github.com/deepfakes/faceswap
author: deepfakes
description: Deepfakes Software For All. Contribute to deepfakes/faceswap development by creating an account on GitHub.
---

deepfakes

 

/

faceswap

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork13.4k
* Star56k

 
 
 
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

1,899 Commits
1,899 Commits
.fs_cache
.fs_cache
 
 
.github
.github
 
 
.install
.install
 
 
config
config
 
 
docs
docs
 
 
lib
lib
 
 
locales
locales
 
 
plugins
plugins
 
 
requirements
requirements
 
 
scripts
scripts
 
 
tests
tests
 
 
tools
tools
 
 
.gitignore
.gitignore
 
 
.readthedocs.yml
.readthedocs.yml
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
INSTALL.md
INSTALL.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
USAGE.md
USAGE.md
 
 
_config.yml
_config.yml
 
 
faceswap.py
faceswap.py
 
 
pyproject.toml
pyproject.toml
 
 
setup.py
setup.py
 
 
tools.py
tools.py
 
 
update_deps.py
update_deps.py
 
 
View all files

## Repository files navigation

# deepfakes_faceswap

### Important information forPatreonandPayPalsupporters. Please see this forum post:https://forum.faceswap.dev/viewtopic.php?f=14&t=3120

FaceSwap is a tool that utilizes deep learning to recognize and swap faces in pictures and videos.

    

Emma Stone/Scarlett Johansson FaceSwap using the Phaze-A model

Jennifer Lawrence/Steve Buscemi FaceSwap using the Villain model

 

Make sure you check outINSTALL.mdbefore getting started.

* deepfakes_faceswapImportant information forPatreonandPayPalsupporters. Please see this forum post: https://forum.faceswap.dev/viewtopic.php?f=14&t=3120
* Important information forPatreonandPayPalsupporters. Please see this forum post: https://forum.faceswap.dev/viewtopic.php?f=14&t=3120
* ManifestoFaceSwap has ethical uses.
* FaceSwap has ethical uses.
* How To setup and run the project
* OverviewExtractTrainConvertGUI
* Extract
* Train
* Convert
* GUI
* General notes:
* Help I need support!Discord ServerFaceSwap Forum
* Discord Server
* FaceSwap Forum
* DonatePatreonOne time Donations@torzdf@andenixa
* Patreon
* One time Donations@torzdf@andenixa
* @torzdf
* @andenixa
* How to contributeFor people interested in the generative modelsFor devsFor non-dev advanced usersFor end-users
* For people interested in the generative models
* For devs
* For non-dev advanced users
* For end-users
* About machine learningHow does a computer know how to recognize/shape faces? How does machine learning work? What is a neural network?
* How does a computer know how to recognize/shape faces? How does machine learning work? What is a neural network?

# Manifesto

## FaceSwap has ethical uses.

When faceswapping was first developed and published, the technology was groundbreaking, it was a huge step in AI development. It was also completely ignored outside of academia because the code was confusing and fragmentary. It required a thorough understanding of complicated AI techniques and took a lot of effort to figure it out. Until one individual brought it together into a single, cohesive collection. It ran, it worked, and as is so often the way with new technology emerging on the internet, it was immediately used to create inappropriate content. Despite the inappropriate uses the software was given originally, it was the first AI code that anyone could download, run and learn by experimentation without having a Ph.D. in math, computer theory, psychology, and more. Before "deepfakes" these techniques were like black magic, only practiced by those who could understand all of the inner workings as described in esoteric and endlessly complicated books and papers.

"Deepfakes" changed all that and anyone could participate in AI development. To us, developers, the release of this code opened up a fantastic learning opportunity. It allowed us to build on ideas developed by others, collaborate with a variety of skilled coders, experiment with AI whilst learning new skills and ultimately contribute towards an emerging technology which will only see more mainstream use as it progresses.

Are there some out there doing horrible things with similar software? Yes. And because of this, the developers have been following strict ethical standards. Many of us don't even use it to create videos, we just tinker with the code to see what it does. Sadly, the media concentrates only on the unethical uses of this software. That is, unfortunately, the nature of how it was first exposed to the public, but it is not representative of why it was created, how we use it now, or what we see in its future. Like any technology, it can be used for good or it can be abused. It is our intention to develop FaceSwap in a way that its potential for abuse is minimized whilst maximizing its potential as a tool for learning, experimenting and, yes, for legitimate faceswapping.

We are not trying to denigrate celebrities or to demean anyone. We are programmers, we are engineers, we are Hollywood VFX artists, we are activists, we are hobbyists, we are human beings. To this end, we feel that it's time to come out with a standard statement of what this software is and isn't as far as us developers are concerned.

* FaceSwap is not for creating inappropriate content.
* FaceSwap is not for changing faces without consent or with the intent of hiding its use.
* FaceSwap is not for any illicit, unethical, or questionable purposes.
* FaceSwap exists to experiment and discover AI techniques, for social or political commentary, for movies, and for any number of ethical and reasonable uses.

We are very troubled by the fact that FaceSwap can be used for unethical and disreputable things. However, we support the development of tools and techniques that can be used ethically as well as provide education and experience in AI for anyone who wants to learn it hands-on. We will take a zero tolerance approach to anyone using this software for any unethical purposes and will actively discourage any such uses.

# How To setup and run the project

FaceSwap is a Python program that will run on multiple Operating Systems including Windows, Linux, and MacOS.

SeeINSTALL.mdfor full installation instructions. You will need a modern GPU with CUDA support for best performance. Many AMD GPUs are supported through ROCm (Linux).

# Overview

The project has multiple entry points. You will have to:

* Gather photos and/or videos
* Extractfaces from your raw photos
* Traina model on the faces extracted from the photos/videos
* Convertyour sources with the model

Check outUSAGE.mdfor more detailed instructions.

## Extract

From your setup folder, runpython faceswap.py extract. This will take photos fromsrcfolder and extract faces intoextractfolder.

## Train

From your setup folder, runpython faceswap.py train. This will take photos from two folders containing pictures of both faces and train a model that will be saved inside themodelsfolder.

## Convert

From your setup folder, runpython faceswap.py convert. This will take photos fromoriginalfolder and apply new faces intomodifiedfolder.

## GUI

Alternatively, you can run the GUI by runningpython faceswap.py gui

# General notes:

* All of the scripts mentioned have-h/--helpoptions with arguments that they will accept. You're smart, you can figure out how this works, right?!

NB: there is a conversion tool for video. This can be accessed by runningpython tools.py effmpeg -h. Alternatively, you can useffmpegto convert video into photos, process images, and convert images back to the video.

Some tips:

Reusing existing models will train much faster than starting from nothing.
If there is not enough training data, start with someone who looks similar, then switch the data.

# Help I need support!

## Discord Server

Your best bet is to join theFaceSwap Discord serverwhere there are plenty of users willing to help. Please note that, like this repo, this is a SFW Server!

## FaceSwap Forum

Alternatively, you can post questions in theFaceSwap Forum. Please do not post general support questions in this repo as they are liable to be deleted without response.

# Donate

The developers work tirelessly to improve and develop FaceSwap. Many hours have been put in to provide the software as it is today, but this is an extremely time-consuming process with no financial reward. If you enjoy using the software, please consider donating to the devs, so they can spend more time implementing improvements.

## Patreon

The best way to support us is through our Patreon page:

## One time Donations

Alternatively you can give a one off donation to any of our Devs:

### @torzdf

There is very little FaceSwap code that hasn't been touched by torzdf. He is responsible for implementing the GUI, FAN aligner, MTCNN detector and porting the Villain, DFL-H128 and DFaker models to FaceSwap, as well as significantly improving many areas of the code.

Bitcoin:bc1qpm22suz59ylzk0j7qk5e4c7cnkjmve2rmtrnc6

Ethereum:0xd3e954dC241B87C4E8E1A801ada485DC1d530F01

Monero:45dLrtQZ2pkHizBpt3P3yyJKkhcFHnhfNYPMSnz3yVEbdWm3Hj6Kr5TgmGAn3Far8LVaQf1th2n3DJVTRkfeB5ZkHxWozSX

Paypal:

### @andenixa

Creator of the Unbalanced and OHR models, as well as expanding various capabilities within the training process. Andenixa is currently working on new models and will take requests for donations.

Paypal:

# How to contribute

## For people interested in the generative models

* Go to the 'faceswap-model' to discuss/suggest/commit alternatives to the current algorithm.

## For devs

* Read this README entirely
* Fork the repo
* Play with it
* Check issues with the 'dev' tag
* For devs more interested in computer vision and openCV, look at issues with the 'opencv' tag. Also feel free to add your own alternatives/improvements

## For non-dev advanced users

* Read this README entirely
* Clone the repo
* Play with it
* Check issues with the 'advuser' tag
* Also go to the 'faceswap Forum' and help others.

## For end-users

* Get the code here and play with it if you can
* You can also go to thefaceswap Forumand help or get help from others.
* Be patient. This is a relatively new technology for developers as well. Much effort is already being put into making this program easy to use for the average user. It just takes time!
* NoticeAny issue related to running the code has to be opened in thefaceswap Forum!

# About machine learning

## How does a computer know how to recognize/shape faces? How does machine learning work? What is a neural network?

It's complicated. Here's a good video that makes the process understandable:

Here's a slightly more in depth video that tries to explain the basic functioning of a neural network:

tl;dr: training data + trial and error