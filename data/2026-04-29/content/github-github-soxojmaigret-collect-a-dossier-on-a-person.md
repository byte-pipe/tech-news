---
title: 'GitHub - soxoj/maigret: 🕵️‍♂️ Collect a dossier on a person by username from 3000+ sites · GitHub'
url: https://github.com/soxoj/maigret
site_name: github
content_file: github-github-soxojmaigret-collect-a-dossier-on-a-person
fetched_at: '2026-04-29T12:16:34.098446'
original_url: https://github.com/soxoj/maigret
author: soxoj
description: 🕵️‍♂️ Collect a dossier on a person by username from 3000+ sites - soxoj/maigret
---

soxoj

 

/

maigret

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork1.4k
* Star19.8k

 
 
 
 
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

1,278 Commits
1,278 Commits
.githooks
.githooks
 
 
.github
.github
 
 
docs
docs
 
 
maigret
maigret
 
 
pyinstaller
pyinstaller
 
 
static
static
 
 
tests
tests
 
 
utils
utils
 
 
.dockerignore
.dockerignore
 
 
.gitignore
.gitignore
 
 
.readthedocs.yaml
.readthedocs.yaml
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Dockerfile
Dockerfile
 
 
Installer.bat
Installer.bat
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
TROUBLESHOOTING.md
TROUBLESHOOTING.md
 
 
cloudshell-tutorial.md
cloudshell-tutorial.md
 
 
cookies.txt
cookies.txt
 
 
example.ipynb
example.ipynb
 
 
opensuse.txt
opensuse.txt
 
 
poetry.lock
poetry.lock
 
 
pyproject.toml
pyproject.toml
 
 
pytest.ini
pytest.ini
 
 
sites.md
sites.md
 
 
snapcraft.yaml
snapcraft.yaml
 
 
wizard.py
wizard.py
 
 
View all files

## Repository files navigation

# Maigret

Maigretcollects a dossier on a personby username only, checking for accounts on a huge number of sites and gathering all the available information from web pages. No API keys required.

## Contents

* In one minute
* Main features
* Demo
* Installation
* Usage
* Contributing
* Commercial Use
* About

## In one minute

Ensure you have Python 3.10 or higher.

pip install maigret
maigret YOUR_USERNAME

No install? Try theTelegram botor aCloud Shell.

Want a web UI? Seehow to launch it.

See also:Quick start.

## Main features

* Supports 3,000+ sites (see full list). A default run checks the 500 highest-ranked sites by traffic; pass-ato scan everything, or--tagsto narrow by category/country.
* Embeddable in Python projects — importmaigretand run searches programmatically (seelibrary usage).
* Extractsall available information about the account owner from profile pages and site APIs, including links to other accounts.
* Performs recursive search using discovered usernames and other IDs.
* Allows filtering by tags (site categories, countries).
* Detects and partially bypasses blocks, censorship, and CAPTCHA.
* Fetches anauto-updated site databasefrom GitHub each run (once per 24 hours), and falls back to the built-in database if offline.
* Works with Tor and I2P websites; able to check domains.
* Ships with aweb interfacefor browsing results as a graph and downloading reports in every format from a single page.

For the complete feature list, see thefeatures documentation.

### Used by

Professional OSINT and social-media analysis tools built on Maigret:

## Demo

### Video

### Reports

PDF report,HTML report

Full console output

## Installation

Already ran theIn one minutesteps? You're set. Below are alternative methods.

Don't want to install anything? Use theTelegram bot.

### Windows

Download a standalone EXE fromReleases. Video guide:https://youtu.be/qIgwTZOmMmM.

### Cloud Shells

Run Maigret in the browser via cloud shells or Jupyter notebooks:

### Local installation (pip)

#
 install from pypi

pip3 install maigret

#
 usage

maigret username

### From source

#
 or clone and install manually

git clone https://github.com/soxoj/maigret 
&&
 
cd
 maigret

#
 build and install

pip3 install 
.

#
 usage

maigret username

### Docker

Two image variants are published:

* soxoj/maigret:latest— CLI mode (default)
* soxoj/maigret:web— auto-launches theweb interface

#
 official image (CLI)

docker pull soxoj/maigret

#
 CLI usage

docker run -v /mydir:/app/reports soxoj/maigret:latest username --html

#
 Web UI (open http://localhost:5000)

docker run -p 5000:5000 soxoj/maigret:web

#
 Web UI on a custom port

docker run -e PORT=8080 -p 8080:8080 soxoj/maigret:web

#
 manual build

docker build -t maigret 
.
 
#
 CLI image (default target)

docker build --target web -t maigret-web 
.
 
#
 Web UI image

### Troubleshooting

Build errors? See thetroubleshooting guide.

## Usage

### Examples

#
 make HTML, PDF, and Xmind8 reports

maigret user --html
maigret user --pdf
maigret user --xmind 
#
Output not compatible with xmind 2022+

#
 machine-readable exports

maigret user --json ndjson 
#
 newline-delimited JSON (also: --json simple)

maigret user --csv
maigret user --txt
maigret user --graph 
#
 interactive D3 graph (HTML)

#
 search on sites marked with tags photo & dating

maigret user --tags photo,dating

#
 search on sites marked with tag us

maigret user --tags us

#
 search for three usernames on all available sites

maigret user1 user2 user3 -a

Runmaigret --helpfor all options. Docs:CLI options,more examples. Running into 403s or timeouts? SeeTROUBLESHOOTING.md.

### Web interface

Maigret has a built-in web UI with a results graph and downloadable reports.

Web Interface Screenshots

maigret --web 5000

Openhttp://127.0.0.1:5000, enter a username, and view results.

### Python library

Maigret can be embedded in your own Python projects.The CLI is a thin wrapper around an async function you can call directly — build custom pipelines, feed results into your own tooling, or run it inside a larger OSINT workflow.

See the fulllibrary usage guidefor a working example, async patterns, and how to filter sites by tag.

### Useful CLI flags

* --parse URL— parse a profile page, extract IDs/usernames, and use them to kick off a recursive search.
* --permute— generate likely username variants from two or more inputs (e.g.john doe→johndoe,j.doe, …) and search for all of them.
* --self-check [--auto-disable]— verifyusernameClaimed/usernameUnclaimedpairs against live sites for maintainers auditing the database.

### Tor / I2P / proxies

Maigret can route checks through a proxy, Tor, or I2P — useful for.onion/.i2psites and for bypassing WAFs that block datacenter IPs.

#
 any HTTP/SOCKS proxy

maigret user --proxy socks5://127.0.0.1:1080

#
 Tor (default gateway socks5://127.0.0.1:9050)

maigret user --tor-proxy socks5://127.0.0.1:9050

#
 I2P (default gateway http://127.0.0.1:4444)

maigret user --i2p-proxy http://127.0.0.1:4444

Start your Tor / I2P daemon before running the command — Maigret does not manage these gateways.

## Contributing

Add or fix new sites surgically indata.json(nojson.load/json.dump), then run./utils/update_site_data.pyto regeneratesites.mdand the database metadata, and open a pull request. For more details, see theCONTRIBUTING guideanddevelopment docs. Release history:CHANGELOG.md.

## Commercial Use

The open-source Maigret is MIT-licensed and free for commercial use without restriction — but site checks break over time and need active maintenance.

For serious commercial use — with adaily-updated site databaseor ausername-check API— reach out: 📧maigret@soxoj.com

* Private site database — 5 000+ sites, updated daily (separate from the public open-source database)
* Username check API — integrate Maigret into your product

## About

### Disclaimer

For educational and lawful purposes only.You are responsible for complying with all applicable laws (GDPR, CCPA, etc.) in your jurisdiction. The authors bear no responsibility for misuse.

### Feedback

Open an issue·GitHub Discussions·Telegram

### SOWEL classification

OSINT techniques used:

* SOTL-2.2. Search For Accounts On Other Platforms
* SOTL-6.1. Check Logins Reuse To Find Another Account
* SOTL-6.2. Check Nicknames Reuse To Find Another Account

### License

MIT ©Maigret

## About

🕵️‍♂️ Collect a dossier on a person by username from 3000+ sites

maigret.readthedocs.io

### Topics

 python

 cli

 open-source

 osint

 social-network

 scraping

 sherlock

 python3

 cybersecurity

 identification

 infosec

 pentesting

 blueteam

 investigation

 reconnaissance

 redteam

 osint-framework

 socmint

 osint-python

 namechecker

### Resources

 Readme

 

### License

 MIT license
 

### Code of conduct

 Code of conduct
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

19.8k

 stars
 

### Watchers

121

 watching
 

### Forks

1.4k

 forks
 

 Report repository

 

## Releases24

Development Windows Release [main]

 Latest

 

Apr 26, 2026

 

+ 23 releases

## Sponsor this project

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 
* patreon.com/soxoj
* buymeacoffee.com/soxoj

Learn more about GitHub Sponsors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python74.5%
* HTML22.2%
* Go Template2.0%
* Batchfile0.6%
* Makefile0.2%
* Jupyter Notebook0.2%
* Other0.3%