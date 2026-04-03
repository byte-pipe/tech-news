---
title: 'GitHub - sherlock-project/sherlock: Hunt down social media accounts by username across social networks · GitHub'
url: https://github.com/sherlock-project/sherlock
site_name: github
content_file: github-github-sherlock-projectsherlock-hunt-down-social-m
fetched_at: '2026-03-30T11:25:57.498489'
original_url: https://github.com/sherlock-project/sherlock
author: sherlock-project
description: Hunt down social media accounts by username across social networks - sherlock-project/sherlock
---

sherlock-project

 

/

sherlock

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork8.8k
* Star74.3k

 
 
 
 
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

2,891 Commits
2,891 Commits
.actor
.actor
 
 
.github
.github
 
 
devel
devel
 
 
docs
docs
 
 
sherlock_project
sherlock_project
 
 
tests
tests
 
 
.dockerignore
.dockerignore
 
 
.editorconfig
.editorconfig
 
 
.gitignore
.gitignore
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
pyproject.toml
pyproject.toml
 
 
pytest.ini
pytest.ini
 
 
tox.ini
tox.ini
 
 
View all files

## Repository files navigation

Hunt down social media accounts by username across400+ social networks

Installation•Usage•Contributing

## Installation

Warning

Packages for ParrotOS and Ubuntu 24.04, maintained by a third party, appear to bebroken.Users of these systems should defer to pipx/pip or Docker.

Method

Notes

pipx install sherlock-project

pip
 may be used in place of 
pipx

docker run -it --rm sherlock/sherlock

dnf install sherlock-project

Community-maintained packages are available for Debian (>= 13), Ubuntu (>= 22.10), Homebrew, Kali, and BlackArch. These packages are not directly supported or maintained by the Sherlock Project.

See all alternative installation methodshere

## General usage

To search for only one user:

sherlock user123

To search for more than one user:

sherlock user1 user2 user3

Accounts found will be stored in an individual text file with the corresponding username (e.guser123.txt).

$ 
sherlock --help

usage: sherlock [-h] [--version] [--verbose] [--folderoutput FOLDEROUTPUT]

 [--output OUTPUT] [--tor] [--unique-tor] [--csv] [--xlsx]

 [--site SITE_NAME] [--proxy PROXY_URL] [--json JSON_FILE]

 [--timeout TIMEOUT] [--print-all] [--print-found] [--no-color]

 [--browse] [--local] [--nsfw]

 USERNAMES [USERNAMES ...]

Sherlock: Find Usernames Across Social Networks (Version 0.14.3)

positional arguments:

 USERNAMES One or more usernames to check with social networks.

 Check similar usernames using {?} (replace to '_', '-', '.').

optional arguments:

 -h, --help show this help message and exit

 --version Display version information and dependencies.

 --verbose, -v, -d, --debug

 Display extra debugging information and metrics.

 --folderoutput FOLDEROUTPUT, -fo FOLDEROUTPUT

 If using multiple usernames, the output of the results will be

 saved to this folder.

 --output OUTPUT, -o OUTPUT

 If using single username, the output of the result will be saved

 to this file.

 --tor, -t Make requests over Tor; increases runtime; requires Tor to be

 installed and in system path.

 --unique-tor, -u Make requests over Tor with new Tor circuit after each request;

 increases runtime; requires Tor to be installed and in system

 path.

 --csv Create Comma-Separated Values (CSV) File.

 --xlsx Create the standard file for the modern Microsoft Excel

 spreadsheet (xlsx).

 --site SITE_NAME Limit analysis to just the listed sites. Add multiple options to

 specify more than one site.

 --proxy PROXY_URL, -p PROXY_URL

 Make requests over a proxy. e.g. socks5://127.0.0.1:1080

 --json JSON_FILE, -j JSON_FILE

 Load data from a JSON file or an online, valid, JSON file.

 --timeout TIMEOUT Time (in seconds) to wait for response to requests (Default: 60)

 --print-all Output sites where the username was not found.

 --print-found Output sites where the username was found.

 --no-color Don't color terminal output

 --browse, -b Browse to all results on default browser.

 --local, -l Force the use of the local data.json file.

 --nsfw Include checking of NSFW sites from default list.

## Apify Actor Usage

You can run Sherlock in the cloud without installation using theSherlock ActoronApifyfree of charge.

$ 
echo
 
'
{"usernames":["user123"]}
'
 
|
 apify call -so netmilk/sherlock
[{
 
"
username
"
: 
"
user123
"
,
 
"
links
"
: [
 
"
https://www.1337x.to/user/user123/
"
,
 ...
 ]
}]

Read more about theSherlock Actor, including how to use it programmatically via the ApifyAPI,CLIandJS/TS and Python SDKs.

## Credits

Thank you to everyone who has contributed to Sherlock! ❤️

## Star History

## License

MIT © Sherlock ProjectOriginal Creator -Siddharth Dushantha

## About

Hunt down social media accounts by username across social networks

sherlockproject.xyz

### Topics

 python

 linux

 cli

 osint

 tools

 sherlock

 python3

 forensics

 cybersecurity

 infosec

 pentesting

 cti

 hacktoberfest

 information-gathering

 reconnaissance

 redteam

### Resources

 Readme

 

### License

 MIT license
 

### Code of conduct

 Code of conduct
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

74.3k

 stars
 

### Watchers

1.2k

 watching
 

### Forks

8.8k

 forks
 

 Report repository

 

## Releases2

Sherlock v0.16.0

 Latest

 

Sep 16, 2025

 

+ 1 release

## Sponsor this project

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

Learn more about GitHub Sponsors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python97.3%
* Dockerfile2.1%
* Shell0.6%