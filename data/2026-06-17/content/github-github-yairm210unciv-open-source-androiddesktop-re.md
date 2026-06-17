---
title: 'GitHub - yairm210/Unciv: Open-source Android/Desktop remake of Civ V · GitHub'
url: https://github.com/yairm210/Unciv
site_name: github
content_file: github-github-yairm210unciv-open-source-androiddesktop-re
fetched_at: '2026-06-17T12:27:13.396613'
original_url: https://github.com/yairm210/Unciv
author: yairm210
description: Open-source Android/Desktop remake of Civ V. Contribute to yairm210/Unciv development by creating an account on GitHub.
---

yairm210

 

/

Unciv

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.8k
* Star10.6k

 
 
 
 
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

12,999 Commits
12,999 Commits
.github
.github
 
 
.idea
.idea
 
 
.run
.run
 
 
android
android
 
 
buildSrc
buildSrc
 
 
core
core
 
 
desktop
desktop
 
 
docs
docs
 
 
extraImages
extraImages
 
 
fastlane/
metadata/
android
fastlane/
metadata/
android
 
 
gradle
gradle
 
 
server
server
 
 
tests
tests
 
 
.dockerignore
.dockerignore
 
 
.editorconfig
.editorconfig
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
build.gradle.kts
build.gradle.kts
 
 
changelog.md
changelog.md
 
 
docker-compose.yml
docker-compose.yml
 
 
gradle.properties
gradle.properties
 
 
gradlew
gradlew
 
 
gradlew.bat
gradlew.bat
 
 
keystore.jks
keystore.jks
 
 
mkdocs.yml
mkdocs.yml
 
 
settings.gradle.kts
settings.gradle.kts
 
 
View all files

## Repository files navigation

# Unciv - Civ V remake for Android & Desktop

## What is this?

An open source, moddability-focused Android and Desktop remake of Civ V, made with LibGDX.

## Is this any good?

Depends what you're looking for. If you're in the market for high-res graphics, amazing soundtracks, animations etc, I highly recommend Firaxis's Civ-V-like game, "Civilization V".

If you want a small, fast, moddable, FOSS, in-depth 4X that can still run on a potato, you've come to the right place :)

## How do I install?

* Android-Google PlayorF-droid
* Linux-itch.io, Flatpak viaFlathub, orAUR
* Windows-Grab the MSI, or get fromitch.io,Chocolatey, orScoop
* Raspberry Pi-Pi-apps
* MacOS- ViaBrew(brew update && brew install unciv) or installwith this guide
* Jars, APKs and Windows/Linux builds also available inReleases(run jar withjava -jar Unciv.jar) -not recommendedsince we update frequently and you will quickly become out-of-date
* Build from scratchif that's your thing

## What's the roadmap?

In this order:

* Polish!UI+UX improvements (suggestions welcome!)Better automation, AI etc. in-game
* UI+UX improvements (suggestions welcome!)
* Better automation, AI etc. in-game
* G&K mechanics - see#4697
* BNW mechanics - trade routes, world congress, etc.

## Contributing

Programmers starthere!

Translators starthere! Language completion statushere

Modders starthere!

You can join us in any of the open issues, or work on improving anything you want - once you're finished, issue a pull request and it'll go into the next version!

If not, you can help by spreading the word - vote for Unciv where you can, mention it on Reddit or Twitter etc, and help us with new ideas of how to get the word out!

## FAQ

### How about iOS?

I'm not planning on it. It means paying money to Apple, yet another release path, and since I don't have an iOS device it means I can't test it properly.

### Steam release?

Steam has decided that they don't want to host Unciv, they probably don't want to risk legal issues with Firaxis (although those should be non-existent, see below).

### Will you implement {feature}?

If it's in the original Civ V, then yes!

If not, then the feature won't be added to the base game - possibly it will be added as a way to mod the game, which is constantly expanding.

#### Why not? This is its own game, why not add features that weren't in Civ V?

Having a clear vision is important for actually getting things done.

Anyone can make a suggestion. Not all are good, viable, or simple. Not many can actually implement stuff.

As an open source project, this stuff is done in our spare time, of which there isn't much.

We need a clear-cut criteria to decide what to work on and what not to work on.

#### Will you implement Civ VI?

Considering how long it took to get this far, no.

### How can I learn to play? Where's the wiki?

All the tutorial information is available in-game at menu > civilopedia > tutorials

All the information is included in the amazingCiv V wiki

Since this is a Civ V clone, you can search Google for how to play Civ V and there are loads of answers =)

Alternatively, you couldjoin us on Discordand ask there =D

### Aren't you basically making a Civ V clone? Is that even legal?

According to theUS Copyright Office FL-108, intellectual property rightsdo notapply to mechanics - as I'm sure you know, there are a billion Flappy Bird knockoffs.

It is definitely illegal:

* To use any assets from the original game (images, sound etc) - they belong to Firaxis

It is probably illegal (no solid sources on this):

* To use the Civilization name
* To impersonate the Civ games (so calling yourself civi|zation with a similar logo, for instance)

Interestingly,Civilization is a registered trademark, but it looks like it's onlythat particular logowhich is trademarked, so technically you could make another game called "Civilization" and it'll stick. In any case we're not going there :)

## Run with Docker

If you have docker compose installed:

$ docker compose build && docker compose up

and then gotohttp://localhost:6901/vnc.html?password=headless

If just docker:

$ docker build . -t unciv && docker run -d -p 6901:6901 -p 5901:5901 unciv

Or just use our already built one:

$ docker run -d -p 6901:6901 -p 5901:5901 ghcr.io/yairm210/unciv

and then gotohttp://localhost:6901/vnc.html?password=headless

## Credits and 3rd parties

## About

Open-source Android/Desktop remake of Civ V

### Topics

 android

 game

 libgdx

 civilization

 strategy-game

 4x-strategy-game

 4x

 itch

 civilization-v

 civ

### Resources

 Readme

 

### License

 MPL-2.0 license
 

### Code of conduct

 Code of conduct
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

10.6k

 stars
 

### Watchers

109

 watching
 

### Forks

1.8k

 forks
 

 Report repository

 

## Releases940

4.20.14

 Latest

 

Jun 16, 2026

 

+ 939 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Kotlin99.5%
* Other0.5%