---
title: 'GitHub - actions/runner-images: GitHub Actions runner images · GitHub'
url: https://github.com/actions/runner-images
site_name: github
content_file: github-github-actionsrunner-images-github-actions-runner
fetched_at: '2026-09-26T14:54:04.516906'
original_url: https://github.com/actions/runner-images
author: actions
description: GitHub Actions runner images. Contribute to actions/runner-images development by creating an account on GitHub.
---

actions

 

/

runner-images

Public

* NotificationsYou must be signed in to change notification settings
* Fork3.9k
* Star13.2k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

7,297 Commits
7,297 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
.vscode
.vscode
 
 
docs
docs
 
 
helpers
helpers
 
 
images.CI
images.CI
 
 
images
images
 
 
schemas
schemas
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
View all files

## Repository files navigation

# GitHub Actions Runner Images

Table of Contents

* About
* Available Images
* Announcements
* Image Definitions
* Image Releases
* Software and Image Support
* How to Interact with the Repo
* FAQs

## About

This repository contains the source code used to create the VM images forGitHub-hosted runnersused for Actions, as well as forMicrosoft-hosted agentsused for Azure Pipelines.
To build a VM machine from this repo's source, see theinstructions.

## Available Images

Image

Architecture

YAML Label

Included Software

Ubuntu 26.04

x64

ubuntu-26.04

ubuntu-26.04

Ubuntu 26.04 Arm64

arm64

ubuntu-26.04-arm

ubuntu-26.04-arm64

Ubuntu 24.04

x64

ubuntu-latest
 or 
ubuntu-24.04

ubuntu-24.04

Ubuntu 24.04 Arm64

arm64

ubuntu-24.04-arm

ubuntu-24.04-arm64

Ubuntu 22.04

x64

ubuntu-22.04

ubuntu-22.04

Ubuntu 22.04 Arm64

arm64

ubuntu-22.04-arm

ubuntu-22.04-arm64

Ubuntu Slim

x64

ubuntu-slim

ubuntu-slim

Xcode 27 

arm64

xcode-27
 or 
xcode-27-xlarge

xcode-27

macOS 26

x64

macos-latest-large
, 
macos-26-intel
, 
macos-26-large

macOS-26

macOS 26 Arm64

arm64

macos-latest
, 
macos-26
 or 
macos-26-xlarge

macOS-26-arm64

macOS 15

x64

macos-15-large
, or 
macos-15-intel

macOS-15

macOS 15 Arm64

arm64

macos-15
, or 
macos-15-xlarge

macOS-15-arm64

macOS 14 

x64

macos-14-large

macOS-14

macOS 14 Arm64 

arm64

macos-14
 or 
macos-14-xlarge

macOS-14-arm64

Windows Server 2025

x64

windows-latest
, 
windows-2025
, or 
windows-2025-vs2026

windows-2025-vs2026

Windows Server 2022

x64

windows-2022

windows-2022

Windows 11 Arm64

arm64

windows-11-arm

windows-11-arm64

Windows 11 Arm64 with Visual Studio 2026

arm64

windows-11-vs2026-arm

windows-11-vs2026-arm64

### Label scheme

* In general the-latestlabel is used for the latest OS image version that is GA.
* Before moving the-latestlabel to a new OS version we will announce the change and give sufficient lead time for users to update their workflows.
* The-xlargeand-largesuffixes are unique to macOS images and are only available for GitHub Actions. Learn more aboutGitHub Actions larger runners.

## Announcements

See notable upcoming changes by viewing issues with theAnnouncementlabel.

## Image Definitions

### Beta

The purpose of a Beta is to collect feedback on an image before it is released to GA. The goal of a Beta is to identify and fix any potential issues that exist on that
image. Images are updated on a weekly cadence. Any workflows that run on a beta image do not fall under the customerSLAin place for Actions.
Customers choosing to use Beta images are encouraged to provide feedback in the runner-images repo by creating an issue. A Beta may take on different availability, i.e. public vs private.

### GA

A GA (General Availability) image has been through a Beta period and is deemed ready for general use. Images are updated on a weekly cadence. In order to be moved to
GA the image must meet the following criteria:

1. Has been through a Beta period (public or private)
2. Most major software we install on the image has a compatible
version for the underlying OS and
3. All major bugs reported during the Beta period have been addressed.

This image type falls under the customerSLAfor actions. GA images are eventually deprecated according to our guidelines as we only support the
latest 2 versions of an OS.

#### Latest Migration Process

GitHub Actions and Azure DevOps use the-latestYAML label (ex:ubuntu-latest,windows-latest, andmacos-latest). These labels point towards the newest stable OS version available.

The-latestmigration process is gradual and happens over 1-2 months in order to allow customers to adapt their workflows to the newest OS version. During this process, any workflow using the-latestlabel, may see changes in the OS version in their workflows or pipelines. To avoid unwanted migration, users can specify a specific OS version in the yaml file (ex: macos-14, windows-2022, ubuntu-22.04).

## Image Releases

How to best follow along with changes

1. Find the latest releases for this repositoryhere.
2. Subscribe to the releases coming out of this repository, instructionshere.
3. Upcoming changes: A pre-release is created when the deployment of an image has started. As soon as the deployment is finished, the pre-release is converted to a release. If you have subscribed to releases, you will get notified of pre-releases as well.* You can also track upcoming changes using theawaiting-deploymentlabel.
4. For high impact changes, we will post these in advance to the GitHub Changelog on ourblogand onX.* Ex: breaking changes, GA or deprecation of images

Cadence

* We typically deploy weekly updates to the software on the runner images.

## Software and Image Support

### Support Policy

* Tools and versions will typically be removed 6 months after they are deprecated or have reached end-of-life
* We support (at maximum) 2 GA images and 1 beta image at a time. We begin the deprecation process of the oldest image label once the newest OS image label has been released to GA.
* The images generally contain the latest versions of packages installed except for Ubuntu LTS where we mostly rely on the Canonical-provided repositories.
* Popular tools can have several versions installed side-by-side with the following strategy:

Tool name

Installation strategy

Docker images

not more than 3 latest LTS OS\tool versions. New images or new versions of current images are added using the standard tool request process

Java

all LTS versions

Node.js

3 latest LTS versions

Go

3 latest minor versions

Python 
 Ruby

5 most popular 
major.minor
 versions

PyPy

3 most popular 
major.minor
 versions

.NET Core

2 latest LTS versions and 1 latest version. For each feature version only latest patch is installed. Note for 
Ubuntu images see details.

GCC 
 GNU Fortran 
 Clang 
 GNU C++

3 latest major versions

Android NDK

1 latest non-LTS, 2 latest LTS versions

Xcode

- only one major version of Xcode will be supported per macOS version 
 - all minor versions of the supported major version will be available 
 - beta and RC versions will be provided "as-is" in the latest available macOS image only no matter of beta/GA status of the image 
 - when a new patch version is released, the previous patch version will be replaced

Xcode Platforms

- only three major.minor versions of platform tools and simulator runtimes will be available for installed Xcode, including beta/RC versions

### Package managers usage

We use third-party package managers to install software during the image generation process. The table below lists the package managers and the software installed.

Note

Third-party repositories are re-evaluated every year to identify if they are still useful and secure.

Operating system

Package manager

Third-party repos and packages

Ubuntu

APT

docker
 
 
Eclipse-Temurin (Adoptium)
 
 
Erlang
 
 
Firefox
 
 
git-lfs
 
 
git
 
 
Google Cloud CLI
 
 
Heroku
 
 
HHvm
 
 
MongoDB
 
 
Mono
 
 
MS Edge
 
 
PostgreSQL
 
 
R

pipx

ansible-core 
yamllint

Windows

Chocolatey

No third-party repos installed

macOS

Homebrew

aws-cli v2
 
 
azure/bicep
 
 
mongodb/brew

pipx

yamllint

### Image Deprecation Policy

* Images begin the deprecation process of the oldest image label once a new GA OS version has been released.
* Deprecation process begins with an announcement that sets a date for deprecation.
* As it gets closer to the date, GitHub begins doing scheduled brownouts of the image.
* During this time there will be an Announcement pinned in the repo to remind users of the deprecation.
* Finally, GitHub will deprecate the image and it will no longer be available.

### Preinstallation Policy

In general, these are the guidelines we follow when deciding what to pre-install on our images:

* Popularity: widely-used tools and ecosystems will be given priority.
* Latest Technology: recent versions of tools will be given priority.
* Deprecation: end-of-life tools and versions will not be added.
* Licensing: MIT, Apache, or GNU licenses are allowed.
* Time & Space on the Image: we will evaluate how much time is saved and how much space is used by having the tool pre-installed.
* Support: If a tool requires the support of more than one version, we will consider the cost of this maintenance.

### Default Version Update Policy

* In general, once a new version is installed on the image, we announce the default version update 2 weeks prior to deploying it.
* For potentially dangerous updates, we may extend the timeline up to 1 month between the announcement and deployment.

## How to Interact with the Repo

* Issues: To file a bug report, or request tools to be added/updated, pleaseopen an issue using the appropriate template
* Discussions: If you want to share your thoughts about image configuration, installed software, or bring a new idea, please create anew discussion. Before making a new discussion, please make sure no similar topics were created earlier in theactions category.
* For general questions about using the runner images or writing your Actions workflow, please open requests in theGitHub Community discussion Actions category.

## FAQs

What images are available for GitHub Actions and Azure DevOps?

The availability of images for GitHub Actions and Azure DevOps is the same. However, deprecation policies may differ. See documentation for more details:

* GitHub Actions
* Azure DevOps

What image version is used in my build?

Usually, image deployment takes 2-3 days, and documentation in themainbranch is only updated when deployment is finished. To find out which image version and what software versions are used in a specific build, seeSet up job(GitHub Actions) orInitialize job(Azure DevOps) step log.

Looking for other Linux distributions?

We do not plan to offer other Linux distributions. We recommend using Docker if you'd like to build using other distributions with the hosted runner images. Alternatively, you can leverageself-hosted runnersand fully customize your VM image to your needs.

How do I contribute to the macOS source?

macOS source lives in this repository and is available for everyone. However, macOS image-generation CI doesn't support external contributions yet so we are not able to accept pull-requests for now.

We are in the process of preparing macOS CI to accept contributions. Until then, we appreciate your patience and ask you to continue to make tool requests by filing issues.

How does GitHub determine what tools are installed on the images?

For some tools, we always install the latest at the time of the deployment; for others, we pin the tool to specific version(s). For more details please see thePreinstallation Policy

How do I request that a new tool be pre-installed on the image?

Please create an issue and get an approval from us to add this tool to the image before creating the pull request.

What branch should I use to build custom image?

We strongly encourage customers to build their own images using the main branch.
This repository contains multiple branches and releases that serve as document milestones to reflect what software is installed in the images at certain point of time. Current builds are not idempotent and if one tries to build a runner image using the specific tag it is not guaranteed that the build will succeed.