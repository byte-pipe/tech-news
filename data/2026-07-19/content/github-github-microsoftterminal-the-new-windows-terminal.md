---
title: 'GitHub - microsoft/terminal: The new Windows Terminal and the original Windows console host, all in the same place! · GitHub'
url: https://github.com/microsoft/terminal
site_name: github
content_file: github-github-microsoftterminal-the-new-windows-terminal
fetched_at: '2026-07-19T11:27:26.153749'
original_url: https://github.com/microsoft/terminal
author: microsoft
description: The new Windows Terminal and the original Windows console host, all in the same place! - microsoft/terminal
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 microsoft

 

/

terminal

Public

* NotificationsYou must be signed in to change notification settings
* Fork9.4k
* Star104k

 
 
 
 
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

4,975 Commits
4,975 Commits
.config
.config
 
 
.github
.github
 
 
.nuget
.nuget
 
 
.vscode
.vscode
 
 
build
build
 
 
dep
dep
 
 
doc
doc
 
 
oss
oss
 
 
policies
policies
 
 
res
res
 
 
samples
samples
 
 
scratch/
ScratchIslandApp
scratch/
ScratchIslandApp
 
 
src
src
 
 
tools
tools
 
 
.clang-format
.clang-format
 
 
.editorconfig
.editorconfig
 
 
.git-blame-ignore-revs
.git-blame-ignore-revs
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.vsconfig
.vsconfig
 
 
.wt.json
.wt.json
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Directory.Build.props
Directory.Build.props
 
 
Directory.Build.targets
Directory.Build.targets
 
 
LICENSE
LICENSE
 
 
NOTICE.md
NOTICE.md
 
 
NuGet.Config
NuGet.Config
 
 
OpenConsole.slnx
OpenConsole.slnx
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
SUPPORT.md
SUPPORT.md
 
 
Scratch.sln
Scratch.sln
 
 
XamlStyler.json
XamlStyler.json
 
 
common.openconsole.props
common.openconsole.props
 
 
conhost.slnf
conhost.slnf
 
 
consolegit2gitfilters.json
consolegit2gitfilters.json
 
 
custom.props
custom.props
 
 
dirs
dirs
 
 
vcpkg.json
vcpkg.json
 
 
View all files

## Repository files navigation

# Welcome to the Windows Terminal, Console and Command-Line repo

Table of Contents

* Installing and running Windows TerminalMicrosoft Store [Recommended]Other install methodsVia GitHubVia Windows Package Manager CLI (aka winget)Via Chocolatey (unofficial)Via Scoop (unofficial)
* Microsoft Store [Recommended]
* Other install methodsVia GitHubVia Windows Package Manager CLI (aka winget)Via Chocolatey (unofficial)Via Scoop (unofficial)
* Via GitHub
* Via Windows Package Manager CLI (aka winget)
* Via Chocolatey (unofficial)
* Via Scoop (unofficial)
* Installing Windows Terminal Canary
* Terminal & Console OverviewWindows TerminalThe Windows Console HostShared ComponentsCreating the new Windows Terminal
* Windows Terminal
* The Windows Console Host
* Shared Components
* Creating the new Windows Terminal
* Resources
* FAQI built and ran the new Terminal, but it looks just like the old console
* I built and ran the new Terminal, but it looks just like the old console
* Documentation
* Contributing
* Communicating with the Team
* Developer Guidance
* Prerequisites
* Building the CodeBuilding in PowerShellBuilding in Cmd
* Building in PowerShell
* Building in Cmd
* Running & DebuggingCoding Guidance
* Coding Guidance
* Code of Conduct

This repository contains the source code for:

* Windows Terminal
* Windows Terminal Preview
* The Windows console host (conhost.exe)
* Components shared between the two projects
* ColorTool
* Sample projectsthat show how to consume the Windows Console APIs

Related repositories include:

* Windows Terminal Documentation(Repo: Contribute to the docs)
* Console API Documentation
* Cascadia Code Font

## Installing and running Windows Terminal

Note

Windows Terminal requires Windows 10 2004 (build 19041) or later

### Microsoft Store [Recommended]

Install theWindows Terminal from the Microsoft Store.
This allows you to always be on the latest version when we release new builds
with automatic upgrades.

This is our preferred method.

### Other install methods

#### Via GitHub

For users who are unable to install Windows Terminal from the Microsoft Store,
released builds can be manually downloaded from this repository'sReleases
page.

Download theMicrosoft.WindowsTerminal_<versionNumber>.msixbundlefile from
theAssetssection. To install the app, you can simply double-click on the.msixbundlefile, and the app installer should automatically run. If that
fails for any reason, you can try the following command at a PowerShell prompt:

#
 NOTE: If you are using PowerShell 7+, please run

#
 Import-Module Appx -UseWindowsPowerShell

#
 before using Add-AppxPackage.

Add-AppxPackage
 Microsoft.WindowsTerminal_
<
versionNumber
>
.msixbundle

Note

If you install Terminal manually:

* You may need to install theVC++ v14 Desktop Framework Package.
This should only be necessary on older builds of Windows 10 and only if you get an error about missing framework packages.
* Terminal will not auto-update when new builds are released so you will need
to regularly install the latest Terminal release to receive all the latest
fixes and improvements!

#### Via Windows Package Manager CLI (aka winget)

wingetusers can download and install
the latest Terminal release by installing theMicrosoft.WindowsTerminalpackage:

winget install 
--
id Microsoft.WindowsTerminal 
-
e

Note

Dependency support is available in WinGet version1.6.2631 or later. To install the Terminal stable release 1.18 or later, please make sure you have the updated version of the WinGet client.

#### Via Chocolatey (unofficial)

Chocolateyusers can download and install the latest
Terminal release by installing themicrosoft-windows-terminalpackage:

choco install microsoft
-
windows
-
terminal

To upgrade Windows Terminal using Chocolatey, run the following:

choco upgrade microsoft
-
windows
-
terminal

If you have any issues when installing/upgrading the package please go to theWindows Terminal package
pageand follow theChocolatey triage process

#### Via Scoop (unofficial)

Scoopusers can download and install the latest Terminal
release by installing thewindows-terminalpackage:

scoop bucket add extras
scoop install windows
-
terminal

To update Windows Terminal using Scoop, run the following:

scoop update windows
-
terminal

If you have any issues when installing/updating the package, please search for
or report the same on theissues
pageof Scoop Extras bucket
repository.

## Installing Windows Terminal Canary

Windows Terminal Canary is a nightly build of Windows Terminal. This build has the latest code from ourmainbranch, giving you an opportunity to try features before they make it to Windows Terminal Preview.

Windows Terminal Canary is our least stable offering, so you may discover bugs before we have had a chance to find them.

Windows Terminal Canary is available as an App Installer distribution and a Portable ZIP distribution.

The App Installer distribution supports automatic updates. Due to platform limitations, this installer only works on Windows 11.

The Portable ZIP distribution is a portable application. It will not automatically update and will not automatically check for updates. This portable ZIP distribution works on Windows 10 (19041+) and Windows 11.

Distribution

Architecture

Link

App Installer

x64, arm64, x86

Download

Portable ZIP

x64

Download

Portable ZIP

ARM64

Download

Portable ZIP

x86

Download

Learn more about thetypes of Windows Terminal distributions.

## Terminal & Console Overview

Please take a few minutes to review the overview below before diving into the
code:

### Windows Terminal

Windows Terminal is a new, modern, feature-rich, productive terminal application
for command-line users. It includes many of the features most frequently
requested by the Windows command-line community including support for tabs, rich
text, globalization, configurability, theming & styling, and more.

The Terminal will also need to meet our goals and measures to ensure it remains
fast and efficient, and doesn't consume vast amounts of memory or power.

### The Windows Console Host

The Windows Console host,conhost.exe, is Windows' original command-line user
experience. It also hosts Windows' command-line infrastructure and the Windows
Console API server, input engine, rendering engine, user preferences, etc. The
console host code in this repository is the actual source from which theconhost.exein Windows itself is built.

Since taking ownership of the Windows command-line in 2014, the team added
several new features to the Console, including background transparency,
line-based selection, support forANSI / Virtual Terminal
sequences,24-bit
color,
aPseudoconsole
("ConPTY"),
and more.

However, because Windows Console's primary goal is to maintain backward
compatibility, we have been unable to add many of the features the community
(and the team) have been wanting for the last several years including tabs,
unicode text, and emoji.

These limitations led us to create the new Windows Terminal.

You can read more about the evolution of the command-line in general, and the
Windows command-line specifically inthis accompanying series of blog
postson the Command-Line team's blog.

### Shared Components

While overhauling Windows Console, we modernized its codebase considerably,
cleanly separating logical entities into modules and classes, introduced some
key extensibility points, replaced several old, home-grown collections and
containers with safer, more efficientSTL
containers,
and made the code simpler and safer by using Microsoft'sWindows Implementation
Libraries - WIL.

This overhaul resulted in several of Console's key components being available
for re-use in any terminal implementation on Windows. These components include a
new DirectWrite-based text layout and rendering engine, a text buffer capable of
storing both UTF-16 and UTF-8, a VT parser/emitter, and more.

### Creating the new Windows Terminal

When we started planning the new Windows Terminal application, we explored and
evaluated several approaches and technology stacks. We ultimately decided that
our goals would be best met by continuing our investment in our C++ codebase,
which would allow us to reuse several of the aforementioned modernized
components in both the existing Console and the new Terminal. Further, we
realized that this would allow us to build much of the Terminal's core itself as
a reusable UI control that others can incorporate into their own applications.

The result of this work is contained within this repo and delivered as the
Windows Terminal application you can download from the Microsoft Store, ordirectly from this repo's
releases.

## Resources

For more information about Windows Terminal, you may find some of these
resources useful and interesting:

* Command-Line Blog
* Command-Line Backgrounder Blog
Series
* Windows Terminal Launch:Terminal "Sizzle
Video"
* Windows Terminal Launch:Build 2019
Session
* Run As Radio:Show 645 - Windows Terminal with Richard
Turner
* Azure DevOps Podcast:Episode 54 - Kayla Cinnamon and Rich Turner on DevOps
on the Windows
Terminal
* Microsoft Ignite 2019 Session:The Modern Windows Command Line: Windows
Terminal -
BRK3321

## FAQ

### I built and ran the new Terminal, but it looks just like the old console

Cause: You're launching the incorrect solution in Visual Studio.

Solution: Make sure you're building & deploying theCascadiaPackageproject in
Visual Studio.

Note

OpenConsole.exeis just a locally-builtconhost.exe, the classic
Windows Console that hosts Windows' command-line infrastructure. OpenConsole
is used by Windows Terminal to connect to and communicate with command-line
applications (viaConPty).

## Documentation

All project documentation is located ataka.ms/terminal-docs. If you would like
to contribute to the documentation, please submit a pull request on theWindows
Terminal Documentation repo.

## Contributing

We are excited to work alongside you, our amazing community, to build and
enhance Windows Terminal!

BEFORE you start work on a feature/fix, please read & follow ourContributor's
Guideto
help avoid any wasted or duplicate effort.

## Communicating with the Team

The easiest way to communicate with the team is via GitHub issues.

Please file new issues, feature requests and suggestions, butDO search for
similar open/closed preexisting issues before creating a new issue.

If you would like to ask a question that you feel doesn't warrant an issue
(yet), please reach out to us via Twitter:

* Christopher Nguyen, Product Manager:@nguyen_dows
* Dustin Howett, Engineering Lead:@dhowett
* Mike Griese, Senior Developer:@zadjii@mastodon.social
* Carlos Zamora, Developer:@cazamor_msft
* Pankaj Bhojwani, Developer
* Leonard Hecker, Developer:@LeonardHecker

## Developer Guidance

## Prerequisites

You can configure your environment to build Terminal in one of two ways:

### Using WinGet configuration file

After cloning the repository, you can use aWinGet configuration fileto set up your environment. Thedefault configuration fileinstalls Visual Studio 2026 Community & rest of the required tools. There are two other variants of the configuration file available in the.configdirectory for Enterprise & Professional editions of Visual Studio 2026. To run the default configuration file, you can either double-click the file from explorer or run the following command:

winget configure .config\configuration.winget

### Manual configuration

* You must be running Windows 10 2004 (build >= 10.0.19041.0) or later to run
Windows Terminal
* You mustenable Developer Mode in the Windows Settings
appto locally install and run Windows Terminal
* You must havePowerShell 7 or laterinstalled
* You must have theWindows 11 (10.0.26100) SDKinstalled at version 10.0.26100.8249 or greater.
* You must have at leastVS 2026version 18.6 installed
* You must install the following Workloads via the VS Installer. Note: Opening
the solution willprompt you to install missing components automatically:Desktop Development with C++WinUI application development
* Desktop Development with C++
* WinUI application development
* You must install the.NET Framework 4.7.2 Targeting Packto build test projects

## Building the Code

OpenConsole.slnx may be built from within Visual Studio or from the command-line
using a set of convenience scripts & tools in the/toolsdirectory:

### Building in PowerShell

Import-Module
 .\tools\OpenConsole.psm1

Set-MsBuildDevEnvironment

Invoke-OpenConsoleBuild

### Building in Cmd

.
\t
ools
\r
azzle.cmd
bcz

## Running & Debugging

To debug the Windows Terminal in VS, right click onCascadiaPackage(in the
Solution Explorer) and go to properties. In the Debug menu, change "Application
process" and "Background task process" to "Native Only".

You should then be able to build & debug the Terminal project by hittingF5. Make sure to select either the "x64" or the "x86" platform - the
Terminal doesn't build for "Any Cpu" (because the Terminal is a C++ application,
not a C# one).

👉 You willnotbe able to launch the Terminal directly by running the
WindowsTerminal.exe. For more details on why, see#926,#4043

### Coding Guidance

Please review these brief docs below about our coding practices.

👉 If you find something missing from these docs, feel free to contribute to
any of our documentation files anywhere in the repository (or write some new
ones!)

This is a work in progress as we learn what we'll need to provide people in
order to be effective contributors to our project.

* Coding Style
* Code Organization
* Exceptions in our legacy codebase
* Helpful smart pointers and macros for interfacing with Windows in WIL

## Code of Conduct

This project has adopted theMicrosoft Open Source Code of
Conduct. For more information see theCode of Conduct
FAQor contactopencode@microsoft.comwith any
additional questions or comments.

## About

The new Windows Terminal and the original Windows console host, all in the same place!

### Topics

 windows

 console

 terminal

 command-line

 wsl

 cmd

 hacktoberfest

 contributions-welcome

 windows-console

 good-first-issue

 windows-terminal

### Resources

 Readme

 

### License

 MIT license
 

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

104k

 stars
 

### Watchers

1.4k

 watching
 

### Forks

9.4k

 forks
 

 Report repository

 

## Releases156

Windows Terminal v1.24.11911.0

 Latest

 

Jul 16, 2026

 

+ 155 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* C++92.4%
* C#3.9%
* C1.8%
* PowerShell1.0%
* Batchfile0.5%
* HLSL0.2%
* Other0.2%