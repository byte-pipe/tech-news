---
title: 'GitHub - nvm-sh/nvm: Node Version Manager - POSIX-compliant bash script to manage multiple active node.js versions · GitHub'
url: https://github.com/nvm-sh/nvm
site_name: github
content_file: github-github-nvm-shnvm-node-version-manager-posix-compli
fetched_at: '2026-08-11T11:42:48.140089'
original_url: https://github.com/nvm-sh/nvm
author: nvm-sh
description: Node Version Manager - POSIX-compliant bash script to manage multiple active node.js versions - nvm-sh/nvm
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 nvm-sh

 

/

nvm

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork10.3k
* Star94.4k

 
 
 
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

2,388 Commits
2,388 Commits
.github
.github
 
 
test
test
 
 
.dockerignore
.dockerignore
 
 
.editorconfig
.editorconfig
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
.mailmap
.mailmap
 
 
.npmrc
.npmrc
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Dockerfile
Dockerfile
 
 
GOVERNANCE.md
GOVERNANCE.md
 
 
LICENSE.md
LICENSE.md
 
 
Makefile
Makefile
 
 
PROJECT_CHARTER.md
PROJECT_CHARTER.md
 
 
README.md
README.md
 
 
ROADMAP.md
ROADMAP.md
 
 
bash_completion
bash_completion
 
 
install.sh
install.sh
 
 
nvm-exec
nvm-exec
 
 
nvm.sh
nvm.sh
 
 
package.json
package.json
 
 
rename_test.sh
rename_test.sh
 
 
update_test_mocks.sh
update_test_mocks.sh
 
 
View all files

## Repository files navigation

# Node Version Manager

## Table of Contents

* Intro
* About
* Installing and UpdatingInstall & Update ScriptAdditional NotesInstalling in DockerInstalling in Docker for CICD-JobsTroubleshooting on LinuxTroubleshooting on macOSAnsibleVerify InstallationImportant NotesGit InstallManual InstallManual Upgrade
* Install & Update ScriptAdditional NotesInstalling in DockerInstalling in Docker for CICD-JobsTroubleshooting on LinuxTroubleshooting on macOSAnsible
* Additional Notes
* Installing in DockerInstalling in Docker for CICD-Jobs
* Installing in Docker for CICD-Jobs
* Troubleshooting on Linux
* Troubleshooting on macOS
* Ansible
* Verify Installation
* Important Notes
* Git Install
* Manual Install
* Manual Upgrade
* UsageLong-term SupportMigrating Global Packages While InstallingMigrating Global Packages Between Installed VersionsOffline InstallDefault Global Packages From File While Installingio.jsSystem Version of NodeListing VersionsSetting Custom ColorsPersisting custom colorsSuppressing colorized outputRestoring PATHSet default node versionUse a mirror of node binariesPass Authorization header to mirror.nvmrcDeeper Shell IntegrationCallingnvm useautomatically in a directory with a.nvmrcfilebashzshfish
* Long-term Support
* Migrating Global Packages While Installing
* Migrating Global Packages Between Installed Versions
* Offline Install
* Default Global Packages From File While Installing
* io.js
* System Version of Node
* Listing Versions
* Setting Custom ColorsPersisting custom colorsSuppressing colorized output
* Persisting custom colors
* Suppressing colorized output
* Restoring PATH
* Set default node version
* Use a mirror of node binariesPass Authorization header to mirror
* Pass Authorization header to mirror
* .nvmrc
* Deeper Shell IntegrationCallingnvm useautomatically in a directory with a.nvmrcfilebashzshfish
* Callingnvm useautomatically in a directory with a.nvmrcfilebashzshfish
* bash
* zsh
* fish
* Running Tests
* Environment variables
* Bash CompletionUsage
* Usage
* Compatibility Issues
* Installing nvm on Alpine LinuxAlpine Linux 3.13+Alpine Linux 3.5 - 3.12
* Alpine Linux 3.13+
* Alpine Linux 3.5 - 3.12
* Uninstalling / RemovalManual Uninstall
* Manual Uninstall
* Docker For Development Environment
* Problems
* macOS Troubleshooting
* WSL Troubleshooting
* Maintainers
* Project Support
* Enterprise Support
* License
* Copyright notice

## Intro

nvmallows you to quickly install and use different versions ofnodevia the command line.

Example:

$ nvm install 24
Now using node v24.14.0 (npm v11.9.0)
$ node -v
v24.14.0
$ nvm use 22
Now using node v22.22.1 (npm v10.9.4)
$ node -v
v22.22.1
$ nvm use 20
Now using node v20.20.1 (npm v10.8.2)
$ node -v
v20.20.1

Simple as that!

## About

nvm is a version manager fornode.js, designed to be installed per-user, and invoked per-shell.nvmworks on any POSIX-compliant shell (sh,dash,ksh,zsh,bash), in particular on these platforms: unix,macOS, andWindows WSL.

## Installing and Updating

### Install & Update Script

Toinstallorupdatenvm, you should run theinstall script. To do that, you may either download and run the script manually, or use the followingcURLorWgetcommand:

curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.6/install.sh 
|
 bash

wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.6/install.sh 
|
 bash

Running either of the above commands downloads a script and runs it. The script clones the nvm repository to~/.nvm, and attempts to add the source lines from the snippet below to the correct profile file (~/.bashrc,~/.bash_profile,~/.zshrc, or~/.profile). If you find the install script is updating the wrong profile file, set the$PROFILEenv var to the profile file’s path, and then rerun the installation script.

export
 NVM_DIR=
"
$(
[ 
-z
 
"
${XDG_CONFIG_HOME-}
"
 ] 
&&
 
printf
 %s 
"
${HOME}
/.nvm
"
 
||
 
printf
 %s 
"
${XDG_CONFIG_HOME}
/nvm
"
)
"

[ 
-s
 
"
$NVM_DIR
/nvm.sh
"
 ] 
&&
 
\.
 
"
$NVM_DIR
/nvm.sh
"
 
#
 This loads nvm

#### Additional Notes

* If the environment variable$XDG_CONFIG_HOMEis present, it will place thenvmfiles there.
* You can add--no-useto the end of the above script to postpone usingnvmuntil you manuallyuseit:

export
 NVM_DIR=
"
$(
[ 
-z
 
"
${XDG_CONFIG_HOME-}
"
 ] 
&&
 
printf
 %s 
"
${HOME}
/.nvm
"
 
||
 
printf
 %s 
"
${XDG_CONFIG_HOME}
/nvm
"
)
"

[ 
-s
 
"
$NVM_DIR
/nvm.sh
"
 ] 
&&
 
\.
 
"
$NVM_DIR
/nvm.sh
"
 --no-use 
#
 This loads nvm, without auto-using the default version

* You can customize the install source, directory, profile, and version using theNVM_SOURCE,NVM_DIR,PROFILE, andNODE_VERSIONvariables.
Eg:curl ... | NVM_DIR="path/to/nvm". Ensure that theNVM_DIRdoes not contain a trailing slash.
* The installer can usegit,curl, orwgetto downloadnvm, whichever is available.
* You can instruct the installer to not edit your shell config (for example if you already get completions via azsh nvm plugin) by settingPROFILE=/dev/nullbefore running theinstall.shscript. Here's an example one-line command to do that:PROFILE=/dev/null bash -c 'curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.6/install.sh | bash'

#### Installing in Docker

When invoking bash as a non-interactive shell, like in aDockercontainer, none of the regular profile files are sourced. In order to usenvm,node, andnpmlike normal, you can instead specify the specialBASH_ENVvariable, which bash sources when invoked non-interactively.

#
 Use bash for the shell

SHELL
 [
"/bin/bash"
, 
"-o"
, 
"pipefail"
, 
"-c"
]

#
 Create a script file sourced by both interactive and non-interactive bash shells

ENV
 BASH_ENV 
"${HOME}/.bash_env"

RUN
 touch 
"${BASH_ENV}"

RUN
 echo 
'. "${BASH_ENV}"'
 >> ~/.bashrc

#
 Download and install nvm

RUN
 curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.6/install.sh | PROFILE=
"${BASH_ENV}"
 bash

RUN
 echo node > .nvmrc

RUN
 nvm install

##### Installing in Docker for CICD-Jobs

More robust, works in CI/CD-Jobs. Can be run in interactive and non-interactive containers.
See#3531.

FROM
 ubuntu:latest

ARG
 NODE_VERSION=20

#
 install curl

RUN
 apt update && apt install curl -y

#
 install nvm

RUN
 curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.6/install.sh | bash

#
 set env

ENV
 NVM_DIR=/root/.nvm

#
 install node

RUN
 bash -c 
"source $NVM_DIR/nvm.sh && nvm install $NODE_VERSION"

#
 set ENTRYPOINT for reloading nvm-environment

ENTRYPOINT
 [
"bash"
, 
"-c"
, 
"source $NVM_DIR/nvm.sh && exec 
\"
$@
\"
"
, 
"--"
]

#
 set cmd to bash

CMD
 [
"/bin/bash"
]

This example defaults to installation of nodejs version 20.x.y. Optionally you can easily override the version with docker build args like:

docker build -t nvmimage --build-arg NODE_VERSION=19 .

After creation of the image you can start container interactively and run commands, for example:

docker run --rm -it nvmimage

root@0a6b5a237c14:/# nvm -v
0.40.6

root@0a6b5a237c14:/# node -v
v19.9.0

root@0a6b5a237c14:/# npm -v
9.6.3

Noninteractive example:

user@host:/tmp/test $ docker run --rm -it nvmimage node -v
v19.9.0
user@host:/tmp/test $ docker run --rm -it nvmimage npm -v
9.6.3

#### Troubleshooting on Linux

OnLinux, after running the install script, if you getnvm: command not foundor see no feedback from your terminal after you typecommand -v nvm, simply close your current terminal, open a new terminal, and try verifying again.
Alternatively, you can run the following commands for the different shells on the command line:

bash:source ~/.bashrc

zsh:source ~/.zshrc

ksh:. ~/.profile

These should pick up thenvmcommand.

#### Troubleshooting on macOS

Since OS X 10.9,/usr/bin/githas been preset byXcodecommand line tools, which means we can't properly detect if Git is installed or not. You need to manually install the Xcode command line tools before running the install script, otherwise, it'll fail. (see#1782)

If you getnvm: command not foundafter running the install script, one of the following might be the reason:

* Since macOS 10.15, the default shell iszshand nvm will look for.zshrcto update, none is installed by default. Create one withtouch ~/.zshrcand run the install script again.
* If you use bash, the previous default shell, your system may not have.bash_profileor.bashrcfiles where the command is set up. Create one of them withtouch ~/.bash_profileortouch ~/.bashrcand run the install script again. Then, run. ~/.bash_profileor. ~/.bashrcto pick up thenvmcommand.
* You have previously usedbash, but you havezshinstalled. You need to manually addthese linesto~/.zshrcand run. ~/.zshrc.
* You might need to restart your terminal instance or run. ~/.nvm/nvm.sh. Restarting your terminal/opening a new tab/window, or running the source command will load the command and the new configuration.
* If the above didn't help, you might need to restart your terminal instance. Try opening a new tab/window in your terminal and retry.

If the above doesn't fix the problem, you may try the following:

* If you use bash, it may be that your.bash_profile(or~/.profile) does not source your~/.bashrcproperly. You could fix this by addingsource ~/<your_profile_file>to it or following the next step below.
* Try addingthe snippet from the install section, that finds the correct nvm directory and loads nvm, to your usual profile (~/.bash_profile,~/.zshrc,~/.profile, or~/.bashrc).
* For more information about this issue and possible workarounds, pleaserefer here

NoteFor Macs with the Apple Silicon chip, node started offeringarm64arch Darwin packages since v16.0.0 and experimentalarm64support when compiling from source since v14.17.0. If you are facing issues installing node usingnvm, you may want to update to one of those versions or later.

#### Ansible

You can use a task:

- 
name
: 
Install nvm

 
ansible.builtin.shell
: 
>

 curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.6/install.sh | bash

 
args
:
 
creates
: 
"
{{ ansible_env.HOME }}/.nvm/nvm.sh
"

### Verify Installation

To verify that nvm has been installed, do:

command
 -v nvm

which should outputnvmif the installation was successful. Please note thatwhich nvmwill not work, sincenvmis a sourced shell function, not an executable binary.

Note:On Linux, after running the install script, if you getnvm: command not foundor see no feedback from your terminal after you typecommand -v nvm, simply close your current terminal, open a new terminal, and try verifying again.

### Important Notes

If you're running a system without prepackaged binary available, which means you're going to install node orio.jsfrom its source code, you need to make sure your system has a C++ compiler. For OS X, Xcode will work, forDebian/Ubuntubased GNU/Linux, thebuild-essentialandlibssl-devpackages work.

Note:nvmalso supports Windows in some cases. It should work through WSL (Windows Subsystem for Linux) depending on the version of WSL. It should also work withGit Bash(MSYS) orCygwin. Otherwise, for Windows, a few alternatives exist, which are neither supported nor developed by us:

* nvm-windows
* nodist
* nvs

Note:nvmdoes not supportFisheither (see#303). Alternatives exist, which are neither supported nor developed by us:

* bassallows you to use utilities written for Bash in fish shell
* fast-nvm-fishonly works with version numbers (not aliases) but doesn't significantly slow your shell startup
* plugin-nvmplugin forOh My Fish, which makes nvm and its completions available in fish shell
* nvm.fish- The Node.js version manager you'll adore, crafted just for Fish
* fish-nvm- Wrapper around nvm for fish, delays sourcing nvm until it's actually used.

Note:We still have some problems withFreeBSD, because there is no official pre-built binary for FreeBSD, and building from source may needpatches; see the issue ticket:

* [#900] [Bug] node on FreeBSD may need to be patched
* nodejs/node#3716

Note:On OS X, if you do not have Xcode installed and you do not wish to download the ~4.3GB file, you can install theCommand Line Tools. You can check out this blog post on how to just that:

* How to Install Command Line Tools in OS X Mavericks & Yosemite (Without Xcode)

Note:On OS X, if you have/had a "system" node installed and want to install modules globally, keep in mind that:

* When usingnvmyou do not needsudoto globally install a module withnpm -g, so instead of doingsudo npm install -g grunt, do insteadnpm install -g grunt
* If you have an~/.npmrcfile, make sure it does not contain anyprefixsettings (which is not compatible withnvm)
* You can (but should not?) keep your previous "system" node install, butnvmwill only be available to your user account (the one used to install nvm). This might cause version mismatches, as other users will be using/usr/local/lib/node_modules/*VS your user account using~/.nvm/versions/node/vX.X.X/lib/node_modules/*

Homebrewinstallation is not supported. If you have issues with homebrew-installednvm, pleasebrew uninstallit, and install it using the instructions below, before filing an issue.

Note:If you're usingzshyou can easily installnvmas a zsh plugin. Installzsh-nvmand runnvm upgradeto upgrade (you can setNVM_AUTO_USE=trueto have it automatically detect and use.nvmrcfiles).

Note:Git versions before v1.7 may face a problem of cloningnvmsource fromGitHubvia https protocol, and there is also different behavior of git before v1.6, and git prior tov1.17.10can not clone tags, so the minimum required git version is v1.7.10. If you are interested in the problem we mentioned here, please refer to GitHub'sHTTPS cloning errorsarticle.

### Git Install

If you havegitinstalled (requires git v1.7.10+):

1. clone this repo in the root of your user profile* cd ~/from anywhere thengit clone https://github.com/nvm-sh/nvm.git .nvm
2. cd ~/.nvmand check out the latest version withgit checkout v0.40.6
3. activatenvmby sourcing it from your shell:. ./nvm.sh

Now add these lines to your~/.bashrc,~/.profile, or~/.zshrcfile to have it automatically sourced upon login:
(you may have to add to more than one of the above files)

export
 NVM_DIR=
"
$HOME
/.nvm
"

[ 
-s
 
"
$NVM_DIR
/nvm.sh
"
 ] 
&&
 
\.
 
"
$NVM_DIR
/nvm.sh
"
 
#
 This loads nvm

[ 
-s
 
"
$NVM_DIR
/bash_completion
"
 ] 
&&
 
\.
 
"
$NVM_DIR
/bash_completion
"
 
#
 This loads nvm bash_completion

### Manual Install

For a fully manual install, execute the following lines to first clone thenvmrepository into$HOME/.nvm, and then loadnvm:

export
 NVM_DIR=
"
$HOME
/.nvm
"
 
&&
 (
 git clone https://github.com/nvm-sh/nvm.git 
"
$NVM_DIR
"

 
cd
 
"
$NVM_DIR
"

 git checkout 
`
git describe --abbrev=0 --tags --match 
"
v[0-9]*
"
 
$(
git rev-list --tags --max-count=1
)
`

) 
&&
 
\.
 
"
$NVM_DIR
/nvm.sh
"

Now add these lines to your~/.bashrc,~/.profile, or~/.zshrcfile to have it automatically sourced upon login:
(you may have to add to more than one of the above files)

export
 NVM_DIR=
"
$HOME
/.nvm
"

[ 
-s
 
"
$NVM_DIR
/nvm.sh
"
 ] 
&&
 
\.
 
"
$NVM_DIR
/nvm.sh
"
 
#
 This loads nvm

[ 
-s
 
"
$NVM_DIR
/bash_completion
"
 ] 
&&
 
\.
 
"
$NVM_DIR
/bash_completion
"
 
#
 This loads nvm bash_completion

### Manual Upgrade

For manual upgrade withgit(requires git v1.7.10+):

1. change to the$NVM_DIR
2. pull down the latest changes
3. check out the latest version
4. activate the new version

(
 
cd
 
"
$NVM_DIR
"

 git fetch --tags origin
 git checkout 
`
git describe --abbrev=0 --tags --match 
"
v[0-9]*
"
 
$(
git rev-list --tags --max-count=1
)
`

) 
&&
 
\.
 
"
$NVM_DIR
/nvm.sh
"

## Usage

To download, compile, and install the latest release of node, do this:

nvm install node 
#
 "node" is an alias for the latest version

To install a specific version of node:

nvm install 14.7.0 
#
 or 16.3.0, 12.22.1, etc

To set an alias:

nvm 
alias
 my_alias v14.4.0

Make sure that your alias does not contain any spaces or slashes.

The first version installed becomes the default. New shells will start with the default version of node (e.g.,nvm alias default).

You can list available versions usingls-remote:

nvm ls-remote

And then in any new shell just use the installed version:

nvm use node

Or you can just run it:

nvm run node --version

Or, you can run any arbitrary command in a subshell with the desired version of node:

nvm 
exec
 4.2 node --version

You can also get the path to the executable to where it was installed:

nvm which 12.22

In place of a version pointer like "14.7" or "16.3" or "12.22.1", you can use the following special default aliases withnvm install,nvm use,nvm run,nvm exec,nvm which, etc:

* node: this installs the latest version ofnode
* iojs: this installs the latest version ofio.js
* stable: this alias is deprecated, and only truly applies tonodev0.12and earlier. Currently, this is an alias fornode.
* unstable: this alias points tonodev0.11- the last "unstable" node release, since post-1.0, all node versions are stable. (inSemVer, versions communicate breakage, not stability).
* current: the version currently active in this shell (i.e. whatnoderesolves to via$PATH). It isnotaffected by.nvmrc. Useful when you want to refer to the active version explicitly — e.g.nvm which currentalways prints the path to the activenode, regardless of whether an.nvmrcfile is present.

### Long-term Support

Node has aschedulefor long-term support (LTS) You can reference LTS versions in aliases and.nvmrcfiles with the notationlts/*for the latest LTS, andlts/argonfor LTS releases from the "argon" line, for example. In addition, the following commands support LTS arguments:

* nvm install --lts/nvm install --lts=argon/nvm install 'lts/*'/nvm install lts/argon
* nvm uninstall --lts/nvm uninstall --lts=argon/nvm uninstall 'lts/*'/nvm uninstall lts/argon
* nvm use --lts/nvm use --lts=argon/nvm use 'lts/*'/nvm use lts/argon
* nvm exec --lts/nvm exec --lts=argon/nvm exec 'lts/*'/nvm exec lts/argon
* nvm run --lts/nvm run --lts=argon/nvm run 'lts/*'/nvm run lts/argon
* nvm ls-remote --lts/nvm ls-remote --lts=argonnvm ls-remote 'lts/*'/nvm ls-remote lts/argon
* nvm version-remote --lts/nvm version-remote --lts=argon/nvm version-remote 'lts/*'/nvm version-remote lts/argon

Any time your local copy ofnvmconnects tohttps://nodejs.org, it will re-create the appropriate local aliases for all available LTS lines. These aliases (stored under$NVM_DIR/alias/lts), are managed bynvm, and you should not modify, remove, or create these files - expect your changes to be undone, and expect meddling with these files to cause bugs that will likely not be supported.

To get the latest LTS version of node and migrate your existing installed packages, use:

nvm install --reinstall-packages-from=current 
'
lts/*
'

### Migrating Global Packages While Installing

If you want to install a new version of Node.js and migrate npm packages from a previous version:

nvm install --reinstall-packages-from=node node

This will first use "nvm version node" to identify the current version you're migrating packages from. Then it resolves the new version to install from the remote server and installs it. Lastly, it runs "nvm reinstall-packages" to reinstall the npm packages from your prior version of Node to the new one.

You can also install and migrate npm packages from specific versions of Node like this:

nvm install --reinstall-packages-from=5 6
nvm install --reinstall-packages-from=iojs v4.2

Note that reinstalling packagesexplicitly does not update the npm version— this is to ensure that npm isn't accidentally upgraded to a broken version for the new node version.

To update npm at the same time add the--latest-npmflag, like this:

nvm install --reinstall-packages-from=default --latest-npm 
'
lts/*
'

or, you can at any time run the following command to get the latest supported npm version on the current node version:

nvm install-latest-npm

If you've already gotten an error to the effect of "npm does not support Node.js", you'll need to (1) revert to a previous node version (nvm ls&nvm use <your latest _working_ version from the ls>), (2) delete the newly created node version (nvm uninstall <your _broken_ version of node from the ls>), then (3) rerun yournvm installwith the--latest-npmflag.

### Migrating Global Packages Between Installed Versions

--reinstall-packages-fromis tied tonvm install. To migrate global npm packages between versions youalreadyhave installed, without (re)installing anything,nvm usethe destination and runnvm reinstall-packagesas a standalone command, pointing at the version you want to copyfrom:

nvm use 22.22.2
nvm reinstall-packages 22.20.0

This reinstalls all global packages from22.20.0into the currently-active version (22.22.2). As with--reinstall-packages-from, the npm version itself is not changed.

### Offline Install

If you've previously downloaded a node version (or it's still in the cache), you can install it without any network access using the--offlineflag:

nvm install --offline 14.7.0

This resolves versions using only locally installed versions and cached downloads. It will not attempt to download anything. This is useful in air-gapped environments, on planes, or when you want to avoid network latency.

You can combine--offlinewith--ltsto install the latest cached LTS version (as long as LTS aliases have been populated by a priornvm ls-remote --lts):

nvm install --offline --lts

### Default Global Packages From File While Installing

If you have a list of default packages you want installed every time you install a new version, we support that too -- just add the package names, one per line, to the file$NVM_DIR/default-packages. You can add anything npm would accept as a package argument on the command line.

#
 $NVM_DIR/default-packages

rimraf
object-inspect@1.0.2
stevemao/left-pad

### io.js

Warning

io.js was afork of Node.js, created in 2014 and merged back in 2015. io.js shipped v1, v2, and v3 release lines; post-merge, node.js began releasing with v4.

If you want to install io.js:

nvm install iojs

If you want to install a new version of io.js and migrate npm packages from a previous version:

nvm install --reinstall-packages-from=iojs iojs

The same guidelines mentioned for migrating npm packages in node are applicable to io.js.

### System Version of Node

If you want to use the system-installed version of node, you can use the special default alias "system":

nvm use system
nvm run system --version

### Listing Versions

If you want to see what versions are installed:

nvm ls

If you want to see what versions are available to install:

nvm ls-remote

### Setting Custom Colors

You can set five colors that will be used to display version and alias information. These colors replace the default colors.
Initial colors are: g b y r e

Color codes:

r/R = red / bold red

g/G = green / bold green

b/B = blue / bold blue

c/C = cyan / bold cyan

m/M = magenta / bold magenta

y/Y = yellow / bold yellow

k/K = black / bold black

e/W = light grey / white

nvm set-colors rgBcm

#### Persisting custom colors

If you want the custom colors to persist after terminating the shell, export theNVM_COLORSvariable in your shell profile. For example, if you want to use cyan, magenta, green, bold red and bold yellow, add the following line:

export
 NVM_COLORS=
'
cmgRY
'

#### Suppressing colorized output

nvm help (or -h or --help),nvm ls,nvm ls-remoteandnvm aliasusually produce colorized output. You can disable colors with the--no-colorsoption (or by setting the environment variableTERM=dumb):

nvm ls --no-colors
nvm 
help
 --no-colors
TERM=dumb nvm ls

### Restoring PATH

To restore your PATH, you can deactivate it:

nvm deactivate

### Set default node version

To set a default Node version to be used in any new shell, use the alias 'default':

nvm 
alias
 default node 
#
 this refers to the latest installed version of node

nvm 
alias
 default 18 
#
 this refers to the latest installed v18.x version of node

nvm 
alias
 default 18.12 
#
 this refers to the latest installed v18.12.x version of node

### Use a mirror of node binaries

To use a mirror of the node binaries, set$NVM_NODEJS_ORG_MIRROR:

export
 NVM_NODEJS_ORG_MIRROR=https://nodejs.org/dist
nvm install node

NVM_NODEJS_ORG_MIRROR=https://nodejs.org/dist nvm install 4.2

To use a mirror of the io.js binaries, set$NVM_IOJS_ORG_MIRROR:

export
 NVM_IOJS_ORG_MIRROR=https://iojs.org/dist
nvm install iojs-v1.0.3

NVM_IOJS_ORG_MIRROR=https://iojs.org/dist nvm install iojs-v1.0.3

nvm usewill not, by default, create a "current" symlink. Set$NVM_SYMLINK_CURRENTto "true" to enable this behavior, which is sometimes useful for IDEs. Note that usingnvmin multiple shell tabs with this environment variable enabled can cause race conditions.

#### Pass Authorization header to mirror

To pass an Authorization header through to the mirror url, set$NVM_AUTH_HEADER

NVM_AUTH_HEADER=
"
Bearer secret-token
"
 nvm install node

### .nvmrc

You can create a.nvmrcfile containing a node version number (or any other string thatnvmunderstands; seenvm --helpfor details) in the project root directory (or any parent directory).
Afterwards,nvm use,nvm install, andnvm whichwill use the version specified in the.nvmrcfile if no version is supplied on the command line; if no.nvmrcis found either, they exit with status127. (nvm execandnvm runfollow the same.nvmrclookup, but currently fall back to the active node if neither resolves — treat that fallback as undefined behavior; pass an explicit version if you need predictable scripting.) If you want the currently active version, passcurrentexplicitly (e.g.nvm which current) —currentis not affected by.nvmrc.

For example, to make nvm default to the latest 5.9 release, the latest LTS version, or the latest node version for the current directory:

$ 
echo
 
"
5.9
"
 
>
 .nvmrc

$ 
echo
 
"
lts/*
"
 
>
 .nvmrc 
#
 to default to the latest LTS version

$ 
echo
 
"
node
"
 
>
 .nvmrc 
#
 to default to the latest version

[NB these examples assume a POSIX-compliant shell version ofecho. If you use a Windowscmddevelopment environment, eg the.nvmrcfile is used to configure a remote Linux deployment, then keep in mind the"s will be copied leading to an invalid file. Remove them.]

Then when you run nvm use:

$ nvm use
Found 
'
/path/to/project/.nvmrc
'
 with version 
<
5.
9>

Now using node v5.9.1 (npm v3.7.3)

Running nvm install will also switch over to the correct version, but if the correct node version isn't already installed, it will install it for you.

$ nvm install
Found 
'
/path/to/project/.nvmrc
'
 with version 
<
5.
9>

Downloading and installing node v5.9.1...
Downloading https://nodejs.org/dist/v5.9.1/node-v5.9.1-linux-x64.tar.xz...

#
################################################################################### 100.0%

Computing checksum with sha256sum
Checksums matched
!

Now using node v5.9.1 (npm v3.7.3)

nvm useet. al. will traverse directory structure upwards from the current directory looking for the.nvmrcfile. In other words, runningnvm useet. al. in any subdirectory of a directory with an.nvmrcwill result in that.nvmrcbeing utilized.

The contents of a.nvmrcfilemustcontain precisely one<version>(as described bynvm --help) followed by a newline..nvmrcfiles may also have comments. The comment delimiter is#, and it and any text after it, as well as blank lines, and leading and trailing white space, will be ignored when parsing.

Key/value pairs using=are also allowed and ignored, but are reserved for future use, and may cause validation errors in the future.

Runnpx nvmrcto validate an.nvmrcfile. If that tool’s results do not agree with nvm, one or the other has a bug - please file an issue.

### Deeper Shell Integration

You can usenvshimto shim thenode,npm, andnpxbins to automatically use thenvmconfig in the current directory.nvshimisnotsupported by thenvmmaintainers. Pleasereport issues to thenvshimteam.

If you prefer a lighter-weight solution, the recipes below have been contributed bynvmusers. They arenotsupported by thenvmmaintainers. We are, however, accepting pull requests for more examples.

#### Callingnvm useautomatically in a directory with a.nvmrcfile

In your profile (~/.bash_profile,~/.zshrc,~/.profile, or~/.bashrc), add the following tonvm usewhenever you enter a new directory:

##### bash

Put the following at the end of your$HOME/.bashrc:

cdnvm
() {
 
command
 
cd
 
"
$@
"
 
||
 
return
 
$?

 nvm_path=
"
$(
nvm_find_up .nvmrc 
|
 
command
 tr -d 
'
\n
'
)
"

 
#
 If there are no .nvmrc file, use the default nvm version

 
if
 [[ 
!
 
$nvm_path
 
=
 
*
[^[:space:]]
*
 ]]
;
 
then

 
declare
 default_version
 default_version
=
"
$(
nvm version default
)
"

 
#
 If there is no default version, set it to `node`

 
#
 This will use the latest version on your machine

 
if
 [ 
$default_version
 
=
 
'
N/A
'
 ]
;
 
then

 nvm 
alias
 default node
 default_version=
$(
nvm version default
)

 
fi

 
#
 If the current version is not the default version, set it to use the default version

 
if
 [ 
"
$(
nvm current
)
"
 
!=
 
"
${default_version}
"
 ]
;
 
then

 nvm use default
 
fi

 
elif
 [[ 
-s
 
"
${nvm_path}
/.nvmrc
"
 
&&
 
-r
 
"
${nvm_path}
/.nvmrc
"
 ]]
;
 
then

 
declare
 nvm_version
 nvm_version
=
$(
<
"
${nvm_path}
"
/.nvmrc
)

 
declare
 locally_resolved_nvm_version
 
#
 `nvm ls` will check all locally-available versions

 
#
 If there are multiple matching versions, take the latest one

 
#
 Remove the `->` and `*` characters and spaces

 
#
 `locally_resolved_nvm_version` will be `N/A` if no local versions are found

 locally_resolved_nvm_version
=
$(
nvm ls --no-colors 
"
${nvm_version}
"
 
|
 
command
 tail -1 
|
 
command
 tr -d 
'
\->*
'
 
|
 
command
 tr -d 
'
[:space:]
'
)

 
#
 If it is not already installed, install it

 
#
 `nvm install` will implicitly use the newly-installed version

 
if
 [ 
"
${locally_resolved_nvm_version}
"
 
=
 
'
N/A
'
 ]
;
 
then

 nvm install 
"
${nvm_version}
"
;

 
elif
 [ 
"
$(
nvm current
)
"
 
!=
 
"
${locally_resolved_nvm_version}
"
 ]
;
 
then

 nvm use 
"
${nvm_version}
"
;

 
fi

 
fi

}

alias
 cd
=
'
cdnvm
'

cdnvm 
"
$PWD
"
 
||
 
exit

This alias would search 'up' from your current directory in order to detect a.nvmrcfile. If it finds it, it will switch to that version; if not, it will use the default version.

##### zsh

This shell function will install (if needed) andnvm usethe specified Node version when an.nvmrcis found, andnvm use defaultotherwise.

Put this into your$HOME/.zshrcto callnvm useautomatically whenever you enter a directory that contains an.nvmrcfile with a string telling nvm which node touse:

#
 place this after nvm initialization!

autoload -U add-zsh-hook

load-nvmrc
() {
 
local
 nvmrc_path
 nvmrc_path=
"
$(
nvm_find_nvmrc
)
"

 
if
 [ 
-n
 
"
$nvmrc_path
"
 ]
;
 
then

 
local
 nvmrc_node_version
 nvmrc_node_version=
$(
nvm version 
"
$(
cat 
"
${nvmrc_path}
"
)
"
)

 
if
 [ 
"
$nvmrc_node_version
"
 
=
 
"
N/A
"
 ]
;
 
then

 nvm install
 
elif
 [ 
"
$nvmrc_node_version
"
 
!=
 
"
$(
nvm version
)
"
 ]
;
 
then

 nvm use
 
fi

 
elif
 [ 
-n
 
"
$(
PWD=
$OLDPWD
 nvm_find_nvmrc
)
"
 ] 
&&
 [ 
"
$(
nvm version
)
"
 
!=
 
"
$(
nvm version default
)
"
 ]
;
 
then

 
echo
 
"
Reverting to nvm default version
"

 nvm use default
 
fi

}

add-zsh-hook chpwd load-nvmrc
load-nvmrc

After saving the file, runsource ~/.zshrcto reload the configuration with the latest changes made.

##### fish

This requires that you havebassinstalled.

#
 ~/.config/fish/functions/nvm.fish

function
 nvm
 bass source ~/.nvm/nvm.
sh
 
--no-use
 
'
;
'
 nvm 
$argv

end

#
 ~/.config/fish/functions/nvm_find_nvmrc.fish

function
 nvm_find_nvmrc
 bass source ~/.nvm/nvm.
sh
 
--no-use
 
'
;
'
 nvm_find_nvmrc

end

#
 ~/.config/fish/functions/load_nvm.fish

function
 load_nvm 
--on-variable
=
"
PWD
"

 
set
 
-l
 default_node_version (nvm version default)
 
set
 
-l
 node_version (nvm version)
 
set
 
-l
 nvmrc_path (nvm_find_nvmrc)
 
if
 
test
 
-n
 
"
$nvmrc_path
"

 
set
 
-l
 nvmrc_node_version (nvm version (
cat
 
$nvmrc_path
))
 
if
 
test
 
"
$nvmrc_node_version
"
 = 
"
N/A
"

 nvm install (
cat
 
$nvmrc_path
)
 
else
 
if
 
test
 
"
$nvmrc_node_version
"
 != 
"
$node_version
"

 nvm use 
$nvmrc_node_version

 
end

 
else
 
if
 
test
 
"
$node_version
"
 != 
"
$default_node_version
"

 
echo
 
"
Reverting to default Node version
"

 nvm use default
 
end

end

#
 ~/.config/fish/config.fish

#
 You must call it on initialization or listening to directory switching won't work

load_nvm 
>
 /dev/stderr

## Running Tests

Tests are written inUrchin. Install Urchin (and other dependencies) like so:

npm install

There are slow tests and fast tests. The slow tests do things like install node
and check that the right versions are used. The fast tests fake this to test
things like aliases and uninstalling. From the root of the nvm git repository,
run the fast tests like this:

npm run test/fast

Run the slow tests like this:

npm run test/slow

Run all of the tests like this:

npm test

Nota bene: Avoid running nvm while the tests are running.

## Environment variables

nvm exposes the following environment variables:

* NVM_DIR- nvm's installation directory.
* NVM_BIN- where node, npm, and global packages for the active version of node are installed.
* NVM_INC- node's include file directory (useful for building C/C++ addons for node).
* NVM_CD_FLAGS- used to maintain compatibility with zsh.
* NVM_RC_VERSION- version from .nvmrc file if being used.

Additionally, nvm modifiesPATH, and, if present,MANPATHandNODE_PATHwhen changing versions.

The following environment variables can be set to configurenvm install:

* NVM_NO_SOURCE_FALLBACK- when1, a failed binary download aborts instead of silently falling back to a (much slower) from-source compile; the persistent equivalent of the-bflag, and mutually exclusive with-s.
* NVM_INSTALL_LOCK_TIMEOUT- seconds to wait for a concurrent install of the same version to finish before giving up (default600). On timeout, nvm prints the lock path so a lock left behind by a killed install can be removed.
* NVM_INSTALL_LOCK_STALE- minutes after which an install lock is assumed abandoned and stolen automatically;0(the default) never steals.

nvm install <version>takes a per-version advisory lock (a directory under$NVM_DIR/.cache/locks), so two shells installing the same version at once cannot corrupt its version directory; installs ofdifferentversions never block each other.

## Bash Completion

To activate, you need to sourcebash_completion:

[[ 
-r
 
$NVM_DIR
/bash_completion ]] 
&&
 
\.
 
$NVM_DIR
/bash_completion

Put the above sourcing line just below the sourcing line for nvm in your profile (.bashrc,.bash_profile).

### Usage

nvm:

$ nvmTab

alias
 deactivate install list-remote reinstall-packages uninstall version
cache 
exec
 install-latest-npm ls run unload version-remote
current 
help
 list ls-remote 
unalias
 use which

nvm alias:

$ nvm aliasTab

default iojs lts/
*
 lts/argon lts/boron lts/carbon lts/dubnium lts/erbium node stable unstable

$ nvm alias my_aliasTab

v10.22.0 v12.18.3 v14.8.0

nvm use:

$ nvm useTab

my_alias default v10.22.0 v12.18.3 v14.8.0

nvm uninstall:

$ nvm uninstallTab

my_alias default v10.22.0 v12.18.3 v14.8.0

## Compatibility Issues

nvmwill encounter some issues if you have some non-default settings set. (see#606)
The following are known to cause issues:

Inside~/.npmrc:

prefix=
'
some/path
'

Environment Variables:

$NPM_CONFIG_PREFIX

$PREFIX

Shell settings:

set
 -e

## Installing nvm on Alpine Linux

In order to provide the best performance (and other optimizations), nvm will download and install pre-compiled binaries for Node (and npm) when you runnvm install X. The Node project compiles, tests and hosts/provides these pre-compiled binaries which are built for mainstream/traditional Linux distributions (such as Debian, Ubuntu,CentOS,RedHatet al).

Alpine Linux, unlike mainstream/traditional Linux distributions, is based onBusyBox, a very compact (~5MB) Linux distribution. BusyBox (and thus Alpine Linux) uses a different C/C++ stack to most mainstream/traditional Linux distributions -musl. This makes binary programs built for such mainstream/traditional incompatible with Alpine Linux, thus we cannot simplynvm install Xon Alpine Linux and expect the downloaded binary to run correctly - you'll likely see "...does not exist" errors if you try that.

There is a-sflag fornvm installwhich requests nvm download Node source and compile it locally.

If installing nvm on Alpine Linuxisstill what you want or need to do, you should be able to achieve this by running the following from your Alpine Linux shell, depending on which version you are using:

### Alpine Linux 3.13+

apk add -U curl bash ca-certificates openssl ncurses coreutils python3 make gcc g++ libgcc linux-headers grep util-linux binutils findutils
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.6/install.sh 
|
 bash

### Alpine Linux 3.5 - 3.12

apk add -U curl bash ca-certificates openssl ncurses coreutils python2 make gcc g++ libgcc linux-headers grep util-linux binutils findutils
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.6/install.sh 
|
 bash

Note: Alpine 3.5 can only install NodeJS versions up to v6.9.5, Alpine 3.6 can only install versions up to v6.10.3, Alpine 3.7 installs versions up to v8.9.3, Alpine 3.8 installs versions up to v8.14.0, Alpine 3.9 installs versions up to v10.19.0, Alpine 3.10 installs versions up to v10.24.1, Alpine 3.11 installs versions up to v12.22.6, Alpine 3.12 installs versions up to v12.22.12, Alpine 3.13 & 3.14 install versions up to v14.20.0, Alpine 3.15 & 3.16 install versions up to v16.16.0 (These are all versions on the main branch). Alpine 3.5 - 3.12 required the packagepython2to build NodeJS, as they are older versions to build. Alpine 3.13+ requirespython3to successfully build newer NodeJS versions, but you can usepython2with Alpine 3.13+ if you need to build versions of node supported in Alpine 3.5 - 3.15, you just need to specify what version of NodeJS you need to install in the package install script.

The Node project has some desire but no concrete plans (due to the overheads of building, testing and support) to offer Alpine-compatible binaries.

As a potential alternative,@mhart(a Node contributor) has someDocker images for Alpine Linux with Node and optionally, npm, pre-installed.

## Uninstalling / Removal

### Manual Uninstall

To removenvmmanually, execute the following:

First, usenvm unloadto remove the nvm command from your terminal session and delete the installation directory:

$ nvm_dir=
"
${NVM_DIR
:-
~
/
.nvm}
"

$ nvm unload
$ rm -rf 
"
$nvm_dir
"

Edit~/.bashrc(or other shell resource config) and remove the lines below:

export
 NVM_DIR=
"
$HOME
/.nvm
"

[ 
-s
 
"
$NVM_DIR
/nvm.sh
"
 ] 
&&
 
\.
 
"
$NVM_DIR
/nvm.sh
"
 
#
 This loads nvm

[[ 
-r
 
$NVM_DIR
/bash_completion ]] 
&&
 
\.
 
$NVM_DIR
/bash_completion

## Docker For Development Environment

To make development and testing work easier we supply a Dockerfile for development usage. It's based on an Ubuntu base image prepared with essential and useful tools fornvmdevelopment. To build the docker image of the environment, do a Docker build at the root ofnvmrepository:

$ docker build -t nvm-dev 
.

This will package your current nvm working copy with our pre-defined development environment into a Docker image namednvm-dev. After the build you should see it appear in the list of images:

$ docker images

REPOSITORY TAG IMAGE ID CREATED SIZE
nvm-dev latest 9ca4c57a97d8 7 days ago 650 MB

To start and enter a container based on this image:

$ docker run -h nvm-dev -it nvm-dev

nvm@nvm-dev:
~
/.nvm$

It takes several minutes to build the image and the image size is about 650MB, so it's not suitable for production usage.

For more information and documentation about Docker, please refer to itsofficial websiteanddocumentation:

## Problems

* If you try to install a node version and the installation fails, be sure to runnvm cache clearto delete cached node downloads, or you might get an error like the following:curl: (33) HTTP server doesn't seem to support byte ranges. Cannot resume.
* Where's mysudo node? Check out#43
* After the v0.8.6 release of node, nvm tries to install from binary packages. But in some systems, the official binary packages don't work due to incompatibility of shared libs. In such cases, use-soption to force install from source:

nvm install -s 0.8.6

* If setting thedefaultalias does not establish the node version in new shells (i.e.nvm currentyieldssystem), ensure that the system's nodePATHis set before thenvm.shsource line in your shell profile (see#658)

## macOS Troubleshooting

nvm node version not found invimshell

If you set node version to a version other than your system node versionnvm use 6.2.1and open vim and run:!node -vyou should seev6.2.1if you see your system versionv0.12.7. You need to run:

sudo chmod ugo-x /usr/libexec/path_helper

More on this issue indotphiles/dotzsh.

nvm is not compatible with the npm config "prefix" option

Some solutions for this issue can be foundhere

There is one more edge case causing this issue, and that's amismatch between the$HOMEpath and the user's home directory's actual name.

You have to make sure that the user directory name in$HOMEand the user directory name you'd see from runningls /Users/are capitalized the same way(See this issue).

To change the user directory and/or account name follow the instructionshere

Homebrew makes zsh directories insecure

zsh compinit: insecure directories, run compaudit 
for
 list.
Ignore insecure directories and 
continue
 [y] or abort compinit [n]
?
 y

Homebrew causes insecure directories like/usr/local/share/zsh/site-functionsand/usr/local/share/zsh. This isnotannvmproblem - it is a homebrew problem. Referherefor some solutions related to the issue.

Macs with Apple Silicon chips

Experimental support for the Apple Silicon chip architecture was added in node.js v15.3 and full support was added in v16.0.
Because of this, if you try to install older versions of node as usual, you will probably experience either compilation errors when installing node or out-of-memory errors while running your code.

So, if you want to run a version prior to v16.0 on an Apple Silicon Mac, it may be best to compile node targeting thex86_64Intel architecture so thatRosetta 2can translate thex86_64processor instructions to ARM-based Apple Silicon instructions.
Here's what you will need to do:

* Install Rosetta, if you haven't already done so$ softwareupdate --install-rosettaYou might wonder, "how will my Apple Silicon Mac know to use Rosetta for a version of node compiled for an Intel chip?".
If an executable contains only Intel instructions, macOS will automatically use Rosetta to translate the instructions.
* Open a shell that's running using Rosetta$ arch -x86_64 zshNote: This same thing can also be accomplished by finding the Terminal oriTermApp in Finder, right clicking, selecting "Get Info", and then checking the box labeled "Open using Rosetta".Note: This terminal session is now running inzsh.
Ifzshis not the shell you typically use,nvmmay not besource'd automatically like it probably is for your usual shell through your dotfiles.
If that's the case, make sure to sourcenvm.$source"${NVM_DIR}/nvm.sh"
* Install whatever older version of node you are interested in. Let's use 12.22.1 as an example.
This will fetch the node source code and compile it, which will take several minutes.$ nvm install v12.22.1 --shared-zlibNote: You're probably curious why--shared-zlibis included.
There's a bug in recent versions of Apple's systemclangcompiler.
If one of these broken versions is installed on your system, the above step will likely still succeed even if you didn't include the--shared-zlibflag.
However, later, when you attempt tonpm installsomething using your old version of node.js, you will seeincorrect data checkerrors.
If you want to avoid the possible hassle of dealing with this, include that flag.
For more details, seethis issueandthis comment
* Exit back to your native shell.$exit$ arch
arm64Note: If you selected the box labeled "Open using Rosetta" rather than running the CLI command in the second step, you will seei386here.
Unless you have another reason to have that box selected, you can deselect it now.
* Check to make sure the architecture is correct.x64is the abbreviation forx86_64, which is what you want to see.$ node -p process.arch
x64

Now you should be able to use node as usual.

## WSL Troubleshooting

If you've encountered this error on WSL-2:

curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.6/install.sh 
|
 bash
% Total % Received % Xferd Average Speed Time Time Time Current
 Dload Upload Total Spent Left Speed
0 0 0 0 0 0 0 0 --:--:-- 0:00:09 --:--:-- 0curl: (6) Could not resolve host: raw.githubusercontent.com

It may be due to your antivirus, VPN, or other reasons.

Where you canping 8.8.8.8while you can'tping google.com

This could simply be solved by running this in your root directory:

sudo rm /etc/resolv.conf
sudo bash -c 
'
echo "nameserver 8.8.8.8" > /etc/resolv.conf
'

sudo bash -c 
'
echo "[network]" > /etc/wsl.conf
'

sudo bash -c 
'
echo "generateResolvConf = false" >> /etc/wsl.conf
'

sudo chattr +i /etc/resolv.conf

This deletes yourresolv.conffile that is automatically generated when you run WSL, creates a new file and putsnameserver 8.8.8.8, then creates awsl.conffile and adds[network]andgenerateResolveConf = falseto prevent auto-generation of that file.

You can check the contents of the file by running:

cat /etc/resolv.conf

## Maintainers

Currently, the sole maintainer is@ljharb- more maintainers are quite welcome, and we hope to add folks to the team over time.Governancewill be re-evaluated as the project evolves.

## Project Support

Only the latest version (v0.40.6 at this time) is supported.

## Enterprise Support

If you are unable to update to the latest version ofnvm, ourpartnersprovide commercial security fixes for all unsupported versions:

* HeroDevs Never-Ending Support

## License

SeeLICENSE.md.

## Copyright notice

CopyrightOpenJS Foundationandnvmcontributors. All rights reserved. TheOpenJS Foundationhas registered trademarks and uses trademarks. For a list of trademarks of theOpenJS Foundation, please see ourTrademark PolicyandTrademark List. Trademarks and logos not indicated on thelist of OpenJS Foundation trademarksare trademarks™ or registered® trademarks of their respective holders. Use of them does not imply any affiliation with or endorsement by them.The OpenJS Foundation|Terms of Use|Privacy Policy|Bylaws|Code of Conduct|Trademark Policy|Trademark List|Cookie Policy