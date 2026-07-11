---
title: 'GitHub - nasa/fprime: F´ - A flight software and embedded systems framework · GitHub'
url: https://github.com/nasa/fprime
site_name: github
content_file: github-github-nasafprime-f-a-flight-software-and-embedded
fetched_at: '2026-07-11T11:24:39.565536'
original_url: https://github.com/nasa/fprime
author: nasa
description: F´ - A flight software and embedded systems framework - nasa/fprime
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 nasa

 

/

fprime

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.7k
* Star11.4k

 
 
 
 
devel
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

6,080 Commits
6,080 Commits
.github
.github
 
 
CFDP
CFDP
 
 
Drv
Drv
 
 
Fpp
Fpp
 
 
FppTestProject
FppTestProject
 
 
Fw
Fw
 
 
Os
Os
 
 
STest
STest
 
 
Svc
Svc
 
 
TestDeploymentsProject
TestDeploymentsProject
 
 
TestUtils
TestUtils
 
 
Utils
Utils
 
 
ci
ci
 
 
cmake
cmake
 
 
default
default
 
 
docs
docs
 
 
googletest @ 58d77fa
googletest @ 58d77fa
 
 
.clang-format
.clang-format
 
 
.clang-tidy
.clang-tidy
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
.nav.yml
.nav.yml
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
AI_POLICY.md
AI_POLICY.md
 
 
CITATION.cff
CITATION.cff
 
 
CMakeLists.txt
CMakeLists.txt
 
 
CMakePresets.json
CMakePresets.json
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
CONTRIBUTORS.md
CONTRIBUTORS.md
 
 
GOVERNANCE.md
GOVERNANCE.md
 
 
LICENSE.txt
LICENSE.txt
 
 
NOTICE.txt
NOTICE.txt
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
release.clang-tidy
release.clang-tidy
 
 
requirements.txt
requirements.txt
 
 
settings.ini
settings.ini
 
 
View all files

## Repository files navigation

## A Flight-Proven, Multi-Platform, Open-Source Flight Software Framework

F´ (F Prime) is a component-driven framework that enables rapid development and deployment of spaceflight and other embedded software applications. Originally developed at theJet Propulsion Laboratory, F´ has been successfully deployed onseveral space applications. It is tailored but not limited to small-scale spaceflight systems such as CubeSats, SmallSats, and instruments.

Please Visit the F´ Website:https://fprime.jpl.nasa.govfor more information.

## What does F´ provide

* An architecture that decomposes flight software into discrete components with well-defined interfaces
* A C++ framework that provides core capabilities such as message queues and threads
* Modeling tools for specifying components and connections and automatically generating code
* A growing collection of ready-to-use components
* Testing tools for testing flight software at the unit and integration levels.

Learn more aboutF´ key features.

## System Requirements

The following system requirements apply to your workstation for developing F´ applications. To see the list of supported platforms on which F´ applications can run on, seeSupported Platforms.

1. Linux, Windows with WSL, or macOS operating system
2. git
3. Python 3.10+,virtual environments, andPIP
4. ClangorGNU C and C++ compilers(e.g. gcc and g++)

Click to Expand: How to Verify System Requirements

1. git --version
2. python --versionandpython -m venv -h. Your system might use an alternate likepython3orpython3.13. For pip:pip --version. On your system it might bepip3orpipx.
3. g++ --versionand then create, build, and run a test program. For example, create a file namedhello.cppwith contents:#include<iostream>intmain(void){
 std::cout <<"Hello, World!"<< std::endl;
}then build and run it, for example like:% g++ -o hi hello.cpp
% ./hi
Hello, World!

## Getting Started

To get started with F´, install the F´ bootstrapping tool with:

pip install fprime-bootstrap

Then, create a new project with:

fprime-bootstrap project

See theHelloWorld Tutorialto guide you through all the steps of developing an F´ project.

New users are encouraged to read through theUser Manualand explore theother tutorials.

## Getting Help

### Discussions

To ask questions, discuss improvements, and ask for help please use the project'sGitHub Discussions.

### Bug reports

To report bugs and issues,open an issue here.

### Community

TheF´ CommunityGitHub Organization contains third party contributions, more documentation of flight software development, and additional resources.

## Resources

* User Manual
* Tutorials
* Discussions
* Submit an Issue
* F´ Community

## Meet the Team

The following roles are members of the CCB and per ourgovernancedocument have decision making power within the framework.

Role

Team Member

Community Manager

@LeStarch

Community Manager

@thomas-bc

Community Manager

@kevin-f-ortega

Security Overseer

@bitWarrior

CCB Member

@bocchino

CCB Member

@kevin-f-ortega

CCB Member

@SterlingPeet

CCB Member

@timcanham

CCB Member

@zimri-leisher

Each product has a set of Maintainers who are charged with the day-to-day implementation of the CCB's direction as realized in a by product.

Product

Core Maintainer(s)

F Prime

@LeStarch, @thomas-bc

F Prime (v3.6.x Maintenance)

@SterlingPeet

fprime-tools

@thomas-bc, @LeStarch

fprime-gds

@thomas-bc, @LeStarch

fpp

@bocchino, @Kronos3

F Prime Platforms

@kevin-f-ortega, @LeStarch

Security

@bitWarrior

## Release Notes

The version history and artifacts associated with the project can be found atReleases.

## About

F´ - A flight software and embedded systems framework

fprime.jpl.nasa.gov

### Topics

 raspberry-pi

 components

 real-time

 framework

 embedded

 cpp

 nasa

 embedded-systems

 flight

 spaceflight

 object-oriented-programming

 flight-software

 fprime

### Resources

 Readme

 

### License

 Apache-2.0 license
 

### Code of conduct

 Code of conduct
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

11.4k

 stars
 

### Watchers

321

 watching
 

### Forks

1.7k

 forks
 

 Report repository

 

## Releases42

v4.2.2

 Latest

 

Apr 24, 2026

 

+ 41 releases

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* C++86.3%
* CMake5.8%
* Fortran5.1%
* Python1.8%
* C1.0%
* Shell0.0%