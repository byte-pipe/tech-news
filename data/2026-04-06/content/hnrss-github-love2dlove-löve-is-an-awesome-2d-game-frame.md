---
title: 'GitHub - love2d/love: LÖVE is an awesome 2D game framework for Lua. · GitHub'
url: https://github.com/love2d/love
site_name: hnrss
content_file: hnrss-github-love2dlove-löve-is-an-awesome-2d-game-frame
fetched_at: '2026-04-06T11:21:56.299045'
original_url: https://github.com/love2d/love
date: '2026-04-04'
description: LÖVE is an awesome 2D game framework for Lua. Contribute to love2d/love development by creating an account on GitHub.
tags:
- hackernews
- hnrss
---

love2d



/

love

Public

* NotificationsYou must be signed in to change notification settings
* Fork573
* Star8.1k




 
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

5,620 Commits
5,620 Commits
.github/
workflows
.github/
workflows
 
 
extra
extra
 
 
platform
platform
 
 
src
src
 
 
testing
testing
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
CMakeLists.txt
CMakeLists.txt
 
 
changes.txt
changes.txt
 
 
license.txt
license.txt
 
 
readme-iOS.rtf
readme-iOS.rtf
 
 
readme.md
readme.md
 
 
View all files

## Repository files navigation

LÖVE is anawesomeframework you can use to make 2D games in Lua. It's free, open-source, and works on Windows, macOS, Linux, Android, and iOS.

## Documentation

We use ourwikifor documentation.
If you need further help, feel free to ask on ourforums, ourDiscord server, or oursubreddit.

## Repository

We use the 'main' branch for development of the next major release, and therefore it should not be considered stable.

There are also branches for currently released major versions, which may have fixes and changes meant for upcoming patch releases within that major version.

We tag all our releases (since we started using mercurial and git), and have binary downloads available for them.

Experimental changes are sometimes developed in a separatelove-experimentsrepository.

## Builds

Files for releases are in thereleasessection on GitHub.The sitehas links to files and additional platform content for the latest release.

There are also unstable/nightly builds:

* Builds for some platforms are automatically created after each commit and are available through GitHub's CI interfaces.
* For ubuntu linux they are inppa:bartbes/love-unstable
* For arch linux there'slove-gitin the AUR.

## Test Suite

The test suite intesting/covers all the LÖVE APIs, and tests them the same way developers use them. You can view current test coverage from anyaction.You can run the suite locally like you would run a normal LÖVE project, e.g.:love testing

See thereadmein the testing folder for more info.

## Contributing

The best places to contribute are through the issue tracker and the official Discord server or IRC channel.

For code contributions, pull requests and patches are welcome. Be sure to read thesource code style guide.
Changes and new features typically get discussed in the issue tracker or on Discord or the forums before a pull request is made.

Note

Pull requests, bug reports, and other contributions made with LLM / generative AI technology will not be accepted.

## Compilation

### Windows

Follow the instructions at themegasourcerepository page.

### *nix

Because in-tree builds are not allowed, the Makefiles needs to be generated in a separate build directory. In this example, folder namedbuildis used:

$ cmake -B build -S. --install-prefix $PWD/prefix # this will create the directory `build/`.
$ cmake --build build --target install -j$(nproc) # this will build with all cores and put the files in `prefix/`.

Note

CMake 3.15 and earlier doesn't support--install-prefix. In that case, use-DCMAKE_INSTALL_PREFIX=instead.

### macOS

Download or clonethis repositoryand copy, move, or symlink themacOS/Frameworkssubfolder into love'splatform/xcode/macosxfolder and thesharedsubfolder into love'splatform/xcodefolder.

Then use the Xcode project found atplatform/xcode/love.xcodeprojto build thelove-macosxtarget.

### iOS

Building for iOS requires macOS and Xcode.

Download thelove-apple-dependencieszip file corresponding to the LÖVE version being used from theReleases page,
unzip it, and place theiOS/librariessubfolder into love'splatform/xcode/iosfolder and thesharedsubfolder into love'splatform/xcodefolder.

Or, download or clonethis repositoryand copy, move, or symlink theiOS/librariessubfolder into love'splatform/xcode/iosfolder and thesharedsubfolder into love'splatform/xcodefolder.

Then use the Xcode project found atplatform/xcode/love.xcodeprojto build thelove-iostarget.

Seereadme-iOS.rtffor more information.

### Android

Visit theAndroid build repositoryfor build instructions.

## Dependencies

* SDL3
* OpenGL 3.3+ / OpenGL ES 3.0+ / Vulkan / Metal
* OpenAL
* Lua / LuaJIT / LLVM-lua
* FreeType
* harfbuzz
* ModPlug
* Vorbisfile
* Theora

## About

LÖVE is an awesome 2D game framework for Lua.

love2d.org

### Topics

 gamedev

 lua

 game-development

 luajit

 love2d

### Resources

 Readme



### License

 View license


### Uh oh!

There was an error while loading.Please reload this page.





Activity


Custom properties


### Stars

8.1k

 stars


### Watchers

92

 watching


### Forks

573

 forks


 Report repository



## Releases17

LÖVE 11.5 [Mysterious Mysteries]

 Latest



Dec 3, 2023



+ 16 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.





### Uh oh!

There was an error while loading.Please reload this page.





## Contributors

### Uh oh!

There was an error while loading.Please reload this page.





## Languages

* C++83.5%
* C13.9%
* Lua1.8%
* Objective-C++0.4%
* CMake0.2%
* HTML0.1%
* Other0.1%
