---
title: 'GitHub - yorukot/superfile: Pretty fancy and modern terminal file manager · GitHub'
url: https://github.com/yorukot/superfile
site_name: github
content_file: github-github-yorukotsuperfile-pretty-fancy-and-modern-te
fetched_at: '2026-07-24T11:34:53.372202'
original_url: https://github.com/yorukot/superfile
author: yorukot
description: Pretty fancy and modern terminal file manager. Contribute to yorukot/superfile development by creating an account on GitHub.
---

yorukot

 

/

superfile

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork587
* Star19.1k

 
 
 
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

2,264 Commits
2,264 Commits
.github
.github
 
 
asset
asset
 
 
cd_on_quit
cd_on_quit
 
 
release
release
 
 
scripts
scripts
 
 
src
src
 
 
testsuite
testsuite
 
 
vhs
vhs
 
 
website
website
 
 
.envrc
.envrc
 
 
.gitignore
.gitignore
 
 
.golangci.yaml
.golangci.yaml
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
NOTICE.md
NOTICE.md
 
 
README.md
README.md
 
 
build.sh
build.sh
 
 
dev.sh
dev.sh
 
 
flake.lock
flake.lock
 
 
flake.nix
flake.nix
 
 
go.mod
go.mod
 
 
go.sum
go.sum
 
 
gomod2nix.toml
gomod2nix.toml
 
 
main.go
main.go
 
 
notice.tmpl
notice.tmpl
 
 
View all files

## Repository files navigation

#### superfile is supported by the community.

 
 
 
 
 

## Demo

Perform common operations

## Content

* Demo
* Content
* InstallationmacOS and LinuxWindowsPowershellWingetScoopMore installation methods
* macOS and Linux
* WindowsPowershellWingetScoop
* Powershell
* Winget
* Scoop
* More installation methods
* BuildFor macOS/LinuxFor Windows
* For macOS/Linux
* For Windows
* Start superfile
* Supported Systems
* Tutorial
* Plugins
* Themes
* Hotkeys
* Notes
* Troubleshooting
* UninstallingmacOS and LinuxWindows
* macOS and Linux
* Windows
* Contributing
* ThanksSupportCore maintainerContributorsPowered byStar History
* Support
* Core maintainer
* Contributors
* Powered by
* Star History
* ༼ つ ◕_◕ ༽つ Please share.

## Installation

### macOS and Linux

bash -c 
"
$(
curl -sLo- https://superfile.dev/install.sh
)
"

If you want to inspect the script, see :install.sh

### Windows

#### Powershell

powershell 
-
ExecutionPolicy Bypass 
-
Command 
"
Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://superfile.dev/install.ps1'))
"

If you want to inspect the script, see :install.ps1

#### Winget

winget install 
--
id yorukot.superfile

#### Scoop

scoop install superfile

### More installation methods

Click me to check on how to install

## Build

You can build the source code yourself by using these steps:

Requirements

* golang

Build Steps

Clone this repository using the following command:

git clone https://github.com/yorukot/superfile.git --depth=1

Enter the downloaded directory:

cd
 superfile

### For macOS/Linux

Run thebuild.shfile:

./build.sh

Add the binary file to your $PATH, e.g., in/usr/local/bin:

sudo mv ./bin/spf /usr/local/bin

### For Windows

go build -o bin/spf.exe

Edit System Environment Variables and add superfile repo'sbindirectory to your PATH

## Start superfile

spf

## Supported Systems

* Linux
* macOS
* Windows (Not fully supported yet)

## Tutorial

After you install superfile, you can gohereto briefly understand how to use superfile!

## Plugins

Click me to the plugins wiki

## Themes

Click me to the theme wiki

## Hotkeys

[!WARNING] If you are vim/nvim user please change your default hotkeys config to vim version!

Click me to see the hotkey wiki

## Notes

We have an auto update functionality, that fetches superfile's latest released version from github (if last timestamp of last version check was less than 24 hours) and prints a prompt to user, if there is a newer version available.

You can turn this off, by settingauto_check_updateto false in superfile config.Click me to see the config wiki

## Troubleshooting

Click me to see common problem fix

## Uninstalling

### macOS and Linux

bash -c 
"
$(
curl -sLo- https://superfile.dev/uninstall.sh
)
"

If you want to inspect the script, see :uninstall.sh

### Windows

To uninstall superfile on Windows, use this powershell script.

powershell 
-
ExecutionPolicy Bypass 
-
Command 
"
Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://superfile.dev/uninstall.ps1'))
"

## Contributing

If you want to contribute please follow thecontribution guide

Click me to see changelog

## Thanks

### Support

* a Star on my GitHub repository would be nice 🌟
* You can buy a coffee for me 💖

### Core maintainer

We welcome anyone who wants to become a core maintainer. Feel free to reach out!

* @yorukot- Original author and maintainer
* @lazysegtree- Core maintainer

### Contributors

Thanks to all the contributors for making this project even greater!

### Powered by

Thanks to JetBrains team for providing open-source licenses to support the maintenance of superfile.

### Star History

THANKS FOR All OF YOUR STARS!Your stars are my motivation to keep updating!

## ༼ つ ◕_◕ ༽つ Please share.