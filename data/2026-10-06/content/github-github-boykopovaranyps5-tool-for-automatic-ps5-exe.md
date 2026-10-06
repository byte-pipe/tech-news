---
title: 'GitHub - boykopovar/AnyPS5: Tool for automatic PS5 executables porting to Linux and Windows · GitHub'
url: https://github.com/boykopovar/AnyPS5
site_name: github
content_file: github-github-boykopovaranyps5-tool-for-automatic-ps5-exe
fetched_at: '2026-10-06T16:47:41.636626'
original_url: https://github.com/boykopovar/AnyPS5
author: boykopovar
description: Tool for automatic PS5 executables porting to Linux and Windows - boykopovar/AnyPS5
---

boykopovar

 

/

AnyPS5

Public

* NotificationsYou must be signed in to change notification settings
* Fork374
* Star5.1k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

1,997 Commits
1,997 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
3rdparty
3rdparty
 
 
core
core
 
 
docs
docs
 
 
tools
tools
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
CMakeLists.txt
CMakeLists.txt
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
View all files

## Repository files navigation

# About

Tool for automatic executables porting to Linux and Windows.

Includes arelinkerthat converts executable to the target system's native format and implementations ofsystem prx librariessuitable for dynamic linking. No emulation or separate runtime process.

Usage,Build instructions,Technical debt of the project,code style conventions,contributing

## Status

 

* System libraries: percentage of the functions known to the project so far (declared incore/libs/prx), not of every PS5 system function. The total grows as more functions are declared.

List of verified games

Dreaming Sarah (2D platformer) runs at a stable 60 fps on a GTX 1050 Ti / i5-7500 3.4GHz.

Unsupported or unexpected states strictly throwstd::runtime_error.what()is printed to stderr and the process terminates.

Theshader recompilersuccessfully produces SPIR-V (validated viaSpirv-Toolswhen built withANYPS5_ENABLE_SPIRV_TOOLS).

## Compatibility

See thegame compatibility listfor tested games and known issues.

## Input mapping

SDL-mapped game controllers are supported, including analog sticks and triggers. Keyboard and mouse controls can be configured with ananyps5-input.inifile. Seeinput mappingfor the supported devices and configuration format.

## Disclaimer

This project is intended for interoperability, research, preservation, and compatibility purposes. It does not include, distribute, or require copyrighted software, firmware, cryptographic keys, or proprietary libraries. Users are responsible for ensuring that any binaries used with this project are obtained and used in accordance with applicable laws and their respective license terms.

## License

This project is licensed under the GNU General Public License version 2 only.