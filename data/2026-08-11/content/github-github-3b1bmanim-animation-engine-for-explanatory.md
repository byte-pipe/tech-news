---
title: 'GitHub - 3b1b/manim: Animation engine for explanatory math videos · GitHub'
url: https://github.com/3b1b/manim
site_name: github
content_file: github-github-3b1bmanim-animation-engine-for-explanatory
fetched_at: '2026-08-11T11:42:48.867237'
original_url: https://github.com/3b1b/manim
author: 3b1b
description: Animation engine for explanatory math videos. Contribute to 3b1b/manim development by creating an account on GitHub.
---

3b1b

 

/

manim

Public

* NotificationsYou must be signed in to change notification settings
* Fork7.5k
* Star89.9k

 
 
 
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

6,459 Commits
6,459 Commits
.github
.github
 
 
docs
docs
 
 
logo
logo
 
 
manimlib
manimlib
 
 
tests
tests
 
 
.gitignore
.gitignore
 
 
LICENSE.md
LICENSE.md
 
 
MANIFEST.in
MANIFEST.in
 
 
README.md
README.md
 
 
example_scenes.py
example_scenes.py
 
 
pyproject.toml
pyproject.toml
 
 
requirements.txt
requirements.txt
 
 
setup.cfg
setup.cfg
 
 
setup.py
setup.py
 
 
View all files

## Repository files navigation

Manim is an engine for precise programmatic animations, designed for creating explanatory math videos.

Note, there are two versions of manim. This repository began as a personal project by the author of3Blue1Brownfor the purpose of animating those videos, with video-specific code availablehere. In 2020 a group of developers forked it into what is now thecommunity edition, with a goal of being more stable, better tested, quicker to respond to community contributions, and all around friendlier to get started with. Seethis pagefor more details.

## Installation

Warning

WARNING:These instructions are for ManimGLonly. Trying to use these instructions to installManim Community/manimor instructions there to install this version will cause problems. You should first decide which version you wish to install, then only follow the instructions for your desired version.

Note

Note: To install manim directly through pip, please pay attention to the name of the installed package. This repository is ManimGL of 3b1b. The package name ismanimglinstead ofmanimormanimlib. Please usepip install manimglto install the version in this repository.

Manim runs on Python 3.10 or higher.

System requirements areFFmpeg,OpenGLandLaTeX(optional, if you want to use LaTeX).
For Linux,Pangoalong with its development headers are required. See instructionhere.

### Directly

#
 Install manimgl

pip install manimgl

#
 Try it out

manimgl

For more options, take a look at theUsing manimsections further below.

If you want to hack on manimlib itself, clone this repository and in that directory execute:

#
 Install manimgl

pip install -e 
.

#
 Try it out

manimgl example_scenes.py OpeningManimExample

#
 or

manim-render example_scenes.py OpeningManimExample

### Linux (Ubuntu/Debian)

1. Install system dependencies.

sudo apt update

sudo apt install ffmpeg
sudo apt install python3-pip
sudo apt install libpango1.0-dev

1. Install a lightweight LaTeX distribution (optional, for LaTeX rendering).

sudo apt install texlive-science texlive-fonts-extra texlive-latex-extra

This lightweight setup is significantly smaller than installingtexlive-fullwhile still supporting most Manim projects.

1. Clone and install ManimGL.

git clone https://github.com/3b1b/manim.git

cd
 manim

python3 -m pip install -e 
.

manimgl example_scenes.py OpeningManimExample

💡 Optional: Using a virtual environment (venv)

It is recommended to use a virtual environment to avoid conflicts with system packages.

sudo apt install python3-venv

python3 -m venv venv

source
 venv/bin/activate

python3 -m pip install -e 
.

Ifpython3-venvis unavailable on your system, try installing the version-specific package instead:

sudo apt install python3.12-venv

### Directly (Windows)

1. Install FFmpeg.
2. Install a LaTeX distribution.MiKTeXis recommended.
3. Install the remaining Python packages.git clone https://github.com/3b1b/manim.gitcdmanim
pip install -e.manimgl example_scenes.py OpeningManimExample

### Mac OSX

1. Install FFmpeg, LaTeX in terminal using homebrew.brew install ffmpeg mactex💡 An alternative to heavyweight MacTeX bundle.To avoid installing the full MacTeX bundle, which is ~6GB, you can alternatively install the
lightweightBasicTeXand then gradually add
only the LaTeX packages you actually need. A list of packages sufficient to run examples can
be foundhere.
For an overview of the MacTeX installer bundles, seehttps://www.tug.org/mactex/.
2. If you are using an ARM-based processor, install Cairo.arch -arm64 brew install pkg-config cairo
3. Install latest version of manim using these command.git clone https://github.com/3b1b/manim.gitcdmanim
pip install -e.manimgl example_scenes.py OpeningManimExample (make sure to add manimgl to path first.)

## Anaconda Install

1. Install LaTeX as above.
2. Create a conda environment usingconda create -n manim python=3.10.
3. Activate the environment usingconda activate manim.
4. Install manimgl usingpip install -e ..

## Using manim

Try running the following:

manimgl example_scenes.py OpeningManimExample

This should pop up a window playing a simple scene.

Look through theexample scenesto see examples of the library's syntax, animation types and object types. In the3b1b/videosrepo, you can see all the code for 3blue1brown videos, though code from older videos may not be compatible with the most recent version of manim. The readme of that repo also outlines some details for how to set up a more interactive workflow, as shown inthis manim demo videofor example.

When running in the CLI, some useful flags include:

* -wto write the scene to a file
* -oto write the scene to a file and open the result
* -sto skip to the end and just show the final frame.-sowill save the final frame to an image and show it
* -sowill save the final frame to an image and show it
* -n <number>to skip ahead to then'th animation of a scene.
* -fto make the playback window fullscreen

Take a look at custom_config.yml for further configuration. To add your customization, you can either edit this file, or add another file by the same name "custom_config.yml" to whatever directory you are running manim from. For examplethis is the onefor 3blue1brown videos. There you can specify where videos should be output to, where manim should look for image files and sounds you want to read in, and other defaults regarding style and video quality.

### Documentation

Documentation is in progress at3b1b.github.io/manim. And there is also a Chinese version maintained by@manim-kindergarten:docs.manim.org.cn(in Chinese).

manim-kindergartenwrote and collected some useful extra classes and some codes of videos inmanim_sandbox repo.

## Contributing

Is always welcome. As mentioned above, thecommunity editionhas the most active ecosystem for contributions, with testing and continuous integration, but pull requests are welcome here too. Please explain the motivation for a given change and examples of its effect.

## License

This project falls under the MIT license.