---
title: 'GitHub - plbrault/youre-the-os: A game where you are a computer''s OS and you have to manage processes, memory and I/O events. · GitHub'
url: https://github.com/plbrault/youre-the-os
site_name: hackernews_api
content_file: hackernews_api-github-plbraultyoure-the-os-a-game-where-you-are-a
fetched_at: '2026-06-26T19:36:10.942208'
original_url: https://github.com/plbrault/youre-the-os
author: exploraz
date: '2026-06-23'
description: A game where you are a computer's OS and you have to manage processes, memory and I/O events. - plbrault/youre-the-os
tags:
- hackernews
- trending
---

plbrault

 

/

youre-the-os

Public

* NotificationsYou must be signed in to change notification settings
* Fork83
* Star2.3k

 
 
 
 
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

226 Commits
226 Commits
.github/
workflows
.github/
workflows
 
 
automation
automation
 
 
readme-assets
readme-assets
 
 
src
src
 
 
.gitignore
.gitignore
 
 
.pylintrc
.pylintrc
 
 
.python-version
.python-version
 
 
AGENTS.md
AGENTS.md
 
 
LICENSE.txt
LICENSE.txt
 
 
Pipfile
Pipfile
 
 
Pipfile.lock
Pipfile.lock
 
 
README.md
README.md
 
 
favicon.png
favicon.png
 
 
run-auto.py
run-auto.py
 
 
run-desktop.py
run-desktop.py
 
 
run-sandbox.py
run-sandbox.py
 
 
run-web.py
run-web.py
 
 
View all files

## Repository files navigation

# You're the OS!

This is a game where you are the operating system of a computer.
As such, you have to manage processes, memory and I/O events.
Make sure not to leave processes idling for too long, or the user will get really impatient and reboot you!

You can play the game here:https://plbrault.github.io/youre-the-os

Also available onitch.io.

## Prerequisites

* Python 3.14The project is not guaranteed to work with other versions.If needed, usepyenvto install the required version without impacting your system globally.
* The project is not guaranteed to work with other versions.
* If needed, usepyenvto install the required version without impacting your system globally.
* pipenv
* An empty.venvdirectory at the root of the project

## Usage

The main branch can be unstable. For a stable version, checkout a release tag.

Install dependencies:

pipenv sync --dev

Run as a desktop app:

pipenv run desktop

Run web version:

pipenv run web

Run sandbox mode

The sandbox mode allows you to skip the menu and immediately run a custom stage. It is provided for development purposes.

First, you need to create a sandbox configuration file. An example is provided insrc/sandbox/sample.py. It is recommended to store your configuration file in that samesrc/sandboxdirectory. Files added to that directory will be ignored by Git.

Next, run the following command, replacingsandbox.sampleby the Python module path fromsrcto your own configuration file (for instance, if your file issrc/sandbox/myConfig.py, the module path will besandbox.myConfig):

pipenv run sandbox sandbox.sample

Run with an automated script:

(Original implementation by@Wiguwbe)

WARNING:Running automation scripts (including the provided example) may cause rapidly changing colors on the screen.

pipenv run auto 
<
script.py
>
 [args]

#
 to get all the available options

pipenv run auto --help

Seeautomation/skeleton.pyfor information on how to write your script.

Build web version without running:

pipenv run web build

Createweb.ziparchive for itch.io:

pipenv run web archive

Run linter:

pipenv run pylint

Run unit tests:

pipenv run pytest

## Contributing

Pull requests that address open issues labeledbugorhelp wantedare welcome.

If you use AI, please ensure your agent follows all instructions inAGENTS.md.

If you have an idea for an improvement to this game, please share it in theDiscussionstab.

## License

Copyright © 2023-present Pier-Luc Braultpier-luc@brault.me

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, seehttps://www.gnu.org/licenses/.

## Asset Licenses

* The game icon/logo is a modified version of an image byMuhammat Sukirmanpublished under theCreative Commons Attribution License 3.0.
* Emojis used in the game are fromOpenMoji. They are published under theCreative Commons Attribution-ShareAlike License 4.0.
* The image used in the Game Over screen is byAleksandar Cvetanović. It was published on Pixabay prior to January 2019, and as such, is available under theCreative Commons Zero (CC0) Licenseaccording to Pixabay's Terms of Service.
* The primary font used in the game is namedVT323, and was designed by Peter Hull. The secondary font is namedVictor Monoand was designed by Rune Bjørnerås. Both are published under theOpen Font License.

## About

A game where you are a computer's OS and you have to manage processes, memory and I/O events.

plbrault.github.io/youre-the-os/

### Topics

 game

 python

 os

 webassembly

 pygame

### Resources

 Readme

 

### License

 GPL-3.0 license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

2.3k

 stars
 

### Watchers

9

 watching
 

### Forks

83

 forks
 

 Report repository

 

## Releases16

v1.11.0

 Latest

 

Apr 11, 2026

 

+ 15 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python100.0%