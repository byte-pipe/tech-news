---
title: 'GitHub - jellyfin/jellyfin: The Free Software Media System - Server Backend & API · GitHub'
url: https://github.com/jellyfin/jellyfin
site_name: github
content_file: github-github-jellyfinjellyfin-the-free-software-media-sy
fetched_at: '2026-05-04T12:21:12.054636'
original_url: https://github.com/jellyfin/jellyfin
author: jellyfin
description: The Free Software Media System - Server Backend & API - jellyfin/jellyfin
---

jellyfin

 

/

jellyfin

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork4.7k
* Star51k

 
 
 
 
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

28,690 Commits
28,690 Commits
.config
.config
 
 
.devcontainer
.devcontainer
 
 
.github
.github
 
 
.vscode
.vscode
 
 
Emby.Naming
Emby.Naming
 
 
Emby.Photos
Emby.Photos
 
 
Emby.Server.Implementations
Emby.Server.Implementations
 
 
Jellyfin.Api
Jellyfin.Api
 
 
Jellyfin.Data
Jellyfin.Data
 
 
Jellyfin.Server.Implementations
Jellyfin.Server.Implementations
 
 
Jellyfin.Server
Jellyfin.Server
 
 
MediaBrowser.Common
MediaBrowser.Common
 
 
MediaBrowser.Controller
MediaBrowser.Controller
 
 
MediaBrowser.LocalMetadata
MediaBrowser.LocalMetadata
 
 
MediaBrowser.MediaEncoding
MediaBrowser.MediaEncoding
 
 
MediaBrowser.Model
MediaBrowser.Model
 
 
MediaBrowser.Providers
MediaBrowser.Providers
 
 
MediaBrowser.XbmcMetadata
MediaBrowser.XbmcMetadata
 
 
deployment/
unraid/
docker-templates
deployment/
unraid/
docker-templates
 
 
fuzz
fuzz
 
 
src
src
 
 
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
 
 
BannedSymbols.txt
BannedSymbols.txt
 
 
CONTRIBUTORS.md
CONTRIBUTORS.md
 
 
Directory.Build.props
Directory.Build.props
 
 
Directory.Packages.props
Directory.Packages.props
 
 
Jellyfin.sln
Jellyfin.sln
 
 
Jellyfin.sln.DotSettings
Jellyfin.sln.DotSettings
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SharedVersion.cs
SharedVersion.cs
 
 
bump_version
bump_version
 
 
global.json
global.json
 
 
jellyfin.code-workspace
jellyfin.code-workspace
 
 
nuget.config
nuget.config
 
 
stylecop.json
stylecop.json
 
 
View all files

## Repository files navigation

# Jellyfin

### The Free Software Media System

Jellyfin is a Free Software Media System that puts you in control of managing and streaming your media. It is an alternative to the proprietary Emby and Plex, to provide media from a dedicated server to end-user devices via multiple apps. Jellyfin is descended from Emby's 3.5.2 release and ported to the .NET platform to enable full cross-platform support.

There are no strings attached, no premium licenses or features, and no hidden agendas: just a team that wants to build something better and work together to achieve it. We welcome anyone who is interested in joining us in our quest!

For further details, please seeour documentation page. To receive the latest updates, get help with Jellyfin, and join the community, please visitone of our communication channels. For more information about the project, please see ourabout page.

Want to get started?Check out ourdownloads pageor ourinstallation guide, then see ourquick start guide. You can alsobuild from source.

Something not working right?Open anIssueon GitHub.

Want to contribute?Check out ourcontributing choose-your-own-adventureto see where you can help, then see ourcontributing guideand ourcommunity standards.

New idea or improvement?Check out ourfeature request hub.

Don't see Jellyfin in your language?Check out ourWeblate instanceto help translate Jellyfin and its subprojects.

## Jellyfin Server

This repository contains the code for Jellyfin's backend server. Note that this is only one of many projects under the Jellyfin GitHuborganizationon GitHub. If you want to contribute, you can start by checking out ourdocumentationto see what to work on.

## Server Development

These instructions will help you get set up with a local development environment in order to contribute to this repository. Before you start, please be sure to completely read ourguidelines on development contributions. Note that this project is supported on all major operating systems except FreeBSD, which is still incompatible.

### Prerequisites

Before the project can be built, you must first install the.NET 9.0 SDKon your system.

Instructions to run this project from the command line are included here, but you will also need to install an IDE if you want to debug the server while it is running. Any IDE that supports .NET 6 development will work, but two options are recent versions ofVisual Studio(at least 2022) andVisual Studio Code.

ffmpegwill also need to be installed.

### Cloning the Repository

After dependencies have been installed you will need to clone a local copy of this repository. If you just want to run the server from source you can clone this repository directly, but if you are intending to contribute code changes to the project, you shouldset up your own forkof the repository. The following example shows how you can clone the repository directly over HTTPS.

git clone https://github.com/jellyfin/jellyfin.git

### Installing the Web Client

The server is configured to host the static files required for theweb clientin addition to serving the backend by default. Before you can run the server, you will need to get a copy of the web client since they are not included in this repository directly.

Note that it is recommended for development tohost the web client separatelyfrom the web server with some additional configuration, in which case you can skip this step.

There are two options to get the files for the web client.

1. Build them from source following the instructions on thejellyfin-web repository
2. Get the pre-built files from an existing installation of the server. For example, with a Windows server installation the client files are located atC:\Program Files\Jellyfin\Server\jellyfin-web

### Running The Server

The following instructions will help you get the project up and running via the command line, or your preferred IDE.

#### Running With Visual Studio

To run the project with Visual Studio you can open the Solution (.sln) file and then pressF5to run the server.

#### Running With Visual Studio Code

To run the project with Visual Studio Code you will first need to open the repository directory with Visual Studio Code using theOpen Folder...option.

Second, you need toinstall the recommended extensions for the workspace. Note that extension recommendations are classified as either "Workspace Recommendations" or "Other Recommendations", but only the "Workspace Recommendations" are required.

After the required extensions are installed, you can run the server by pressingF5.

#### Running From the Command Line

To run the server from the command line you can use thedotnet runcommand. The example below shows how to do this if you have cloned the repository into a directory namedjellyfin(the default directory name) and should work on all operating systems.

cd
 jellyfin 
#
 Move into the repository directory

dotnet run --project Jellyfin.Server --webdir /absolute/path/to/jellyfin-web/dist 
#
 Run the server startup project

A second option is to build the project and then run the resulting executable file directly. When running the executable directly you can easily add command line options. Add the--helpflag to list details on all the supported command line options.

1. Build the project

dotnet build 
#
 Build the project

cd
 Jellyfin.Server/bin/Debug/net10.0 
#
 Change into the build output directory

1. Execute the build output. On Linux, Mac, etc. use./jellyfinand on Windows usejellyfin.exe.

#### Accessing the Hosted Web Client

If the Server is configured to host the Web Client, and the Server is running, the Web Client can be accessed athttp://localhost:8096by default.

API documentation can be viewed athttp://localhost:8096/api-docs/swagger/index.html

### Running from GitHub Codespaces

As Jellyfin will run on a container on a GitHub hosted server, JF needs to handle some things differently.

NOTE:Depending on the selected configuration (if you just click 'create codespace' it will create a default configuration one) it might take 20-30 seconds to load all extensions and prepare the environment while VS Code is already open. Just give it some time and wait until you seeDownloading .NET version(s) 7.0.15~x64 ...... Done!in the output tab.

NOTE:If you want to access the JF instance from outside, like with a WebClient on another PC, remember to set the "ports" in the lower VS Code window to public.

NOTE:When first opening the server instance with any WebUI, you will be sent to the login instead of the setup page. Refresh the login page once and you should be redirected to the Setup.

There are two configurations for you to choose from.

#### Default - Development Jellyfin Server

This creates a container that has everything to run and debug the Jellyfin Media server but does not setup anything else. Each time you create a new container you have to run through the whole setup again. There is also no ffmpeg, webclient or media preloaded. Use the.NET Launch (nowebclient)launch config to start the server.

Keep in mind that as this has no web client you have to connect to it via an external client. This can be just another codespace container running the WebUI. vuejs does not work from the get-go as it does not support the setup steps.

#### Development Jellyfin Server ffmpeg

this extends the default server with a default installation of ffmpeg6 though the means described here:https://jellyfin.org/docs/general/installation/linux#repository-manualIf you want to install a specific ffmpeg version, follow the comments embedded in the.devcontainer/Dev - Server Ffmpeg/install.ffmpeg.shfile.

Use theghcs .NET Launch (nowebclient, ffmpeg)launch config to run with the jellyfin-ffmpeg enabled.

### Running The Tests

This repository also includes unit tests that are used to validate functionality as part of a CI pipeline on Azure. There are several ways to run these tests.

1. Run tests from the command line usingdotnet test
2. Run tests in Visual Studio using theTest Explorer
3. Run individual tests in Visual Studio Code using the associatedCodeLens annotation

### Advanced Configuration

The following sections describe some more advanced scenarios for running the server from source that build upon the standard instructions above.

#### Hosting The Web Client Separately

It is not necessary to host the frontend web client as part of the backend server. Hosting these two components separately may be useful for frontend developers who would prefer to host the client in a separate webpack development server for a tighter development loop. See thejellyfin-webrepo for instructions on how to do this.

To instruct the server not to host the web content, there is anowebclientconfiguration flag that must be set. This can be specified using the command line
switch--nowebclientor the environment variableJELLYFIN_NOWEBCONTENT=true.

Since this is a common scenario, there is also a separate launch profile defined for Visual Studio calledJellyfin.Server (nowebcontent)that can be selected from the 'Start Debugging' dropdown in the main toolbar.

NOTE:The setup wizard cannot be run if the web client is hosted separately.

This project is supported by:

## About

The Free Software Media System - Server Backend & API

jellyfin.org

### Topics

 csharp

 dotnet

 hacktoberfest

 jellyfin

### Resources

 Readme

 

### License

 GPL-2.0 license
 

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

51k

 stars
 

### Watchers

353

 watching
 

### Forks

4.7k

 forks
 

 Report repository

 

## Releases104

10.11.8

 Latest

 

Apr 5, 2026

 

+ 103 releases

## Sponsor this project

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 
* opencollective.com/jellyfin

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* C#99.7%
* Other0.3%