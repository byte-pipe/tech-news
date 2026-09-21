---
title: 'GitHub - mvt-project/mvt: MVT (Mobile Verification Toolkit) helps with conducting forensics of mobile devices in order to find signs of a potential compromise. · GitHub'
url: https://github.com/mvt-project/mvt
site_name: github
content_file: github-github-mvt-projectmvt-mvt-mobile-verification-tool
fetched_at: '2026-09-21T16:50:00.028299'
original_url: https://github.com/mvt-project/mvt
author: mvt-project
description: MVT (Mobile Verification Toolkit) helps with conducting forensics of mobile devices in order to find signs of a potential compromise. - mvt-project/mvt
---

mvt-project

 

/

mvt

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.3k
* Star13.4k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

1,305 Commits
1,305 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
docs
docs
 
 
src/
mvt
src/
mvt
 
 
tests
tests
 
 
.gitignore
.gitignore
 
 
.python-version
.python-version
 
 
.readthedocs.yaml
.readthedocs.yaml
 
 
.safety-policy.yml
.safety-policy.yml
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Dockerfile
Dockerfile
 
 
Dockerfile.android
Dockerfile.android
 
 
Dockerfile.ios
Dockerfile.ios
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
mkdocs.yml
mkdocs.yml
 
 
pyproject.toml
pyproject.toml
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

# Mobile Verification Toolkit

Important

We recently merged the "v3" branch. This introduced breaking changes. If you relied on mvt output in other scripts They might have broken. More details:#757

Mobile Verification Toolkit (MVT) is a collection of utilities to simplify and automate the process of gathering forensic traces helpful to identify a potential compromise of Android and iOS devices.

It has been developed and released by theAmnesty International Security Labin July 2021 in the context of thePegasus Projectalong witha technical forensic methodology. It continues to be maintained by Amnesty International and other contributors.

NoteMVT is a forensic research tool intended for technologists and investigators. It requires understanding digital forensics and using command-line tools. This is not intended for end-user self-assessment. If you are concerned with the security of your device please seek reputable expert assistance.

### Indicators of Compromise

MVT supports using publicindicators of compromise (IOCs)to scan mobile devices for potential traces of targeting or infection by known spyware campaigns. This includes IOCs published byAmnesty Internationaland other research groups.

WarningPublic indicators of compromise are insufficient to determine that a device is "clean", and not targeted with a particular spyware tool. Reliance on public indicators alone can miss recent forensic traces and give a false sense of security.

Reliable and comprehensive digital forensic support and triage requires access to non-public indicators, research and threat intelligence.

Such support is available to civil society throughAmnesty International's Security Labor through our forensic partnership withAccess Now’s Digital Security Helpline.

More information about using indicators of compromise with MVT is available in thedocumentation.

## Installation

MVT can be installed from sources or fromPyPI(you will need some dependencies, check thedocumentation):

pip3 install mvt

You can also install MVT from PyPI withuv. First, install uv:

curl -LsSf https://astral.sh/uv/install.sh 
|
 sh

Then install MVT as a command-line tool:

uv tool install mvt

For alternative installation options and known issues, please refer to thedocumentationas well asGitHub Issues.

## Usage

MVT provides three commands:mvt-iosandmvt-androidanalyse acquisitions from devices of that platform, andmvthosts what belongs to neither:version,completion,pluginsanddownload-iocs(versionanddownload-iocsremain available on the platform commands for now). Runningmvton its own shows the installed version, update notices and the available commands.Check out the documentation to learn how to use them!

Pass--verboseto any of the three commands, before the command name (mvt-ios --verbose check-backup ...), for debug output. The--verboseoption thecheck-*commands accept after their name still works but is kept for compatibility only and will be removed in a future release.

### Shell completion

MVT can generate a shell completion script for Bash, Zsh, and Fish which coversmvt,mvt-iosandmvt-android:

mvt completion

The command prints setup instructions by default. To generate the completion script directly, pass the shell name:

mvt completion bash

MVT only writes completion files or shell configuration when--installis passed. See thecommand completion documentationfor details.

Plugin packages extend MVT with additional forensic modules, which run inside
thecheck-*commands, and with top-level commands onmvt,mvt-iosandmvt-android. See thedevelopment documentationfor
writing and installing them, and thecustom CLI command documentationfor the entry points a package registers commands in.

## License

The purpose of MVT is to facilitate theconsensual forensic analysisof devices of those who might be targets of sophisticated mobile spyware attacks, especially members of civil society and marginalized communities. We do not want MVT to enable privacy violations of non-consenting individuals. In order to achieve this, MVT is released under its own license.Read more here.