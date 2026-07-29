---
title: 'GitHub - grokability/snipe-it: A free open source IT asset/license management system · GitHub'
url: https://github.com/grokability/snipe-it
site_name: github
content_file: github-github-grokabilitysnipe-it-a-free-open-source-it-a
fetched_at: '2026-07-29T11:46:59.803314'
original_url: https://github.com/grokability/snipe-it
author: grokability
description: A free open source IT asset/license management system - grokability/snipe-it
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 grokability

 

/

snipe-it

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork3.9k
* Star14.3k

 
 
 
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

24,106 Commits
24,106 Commits
.github
.github
 
 
.screenshotter
.screenshotter
 
 
ansible
ansible
 
 
app
app
 
 
bootstrap
bootstrap
 
 
config
config
 
 
database
database
 
 
docker
docker
 
 
public
public
 
 
resources
resources
 
 
routes
routes
 
 
sample_csvs
sample_csvs
 
 
storage
storage
 
 
stubs
stubs
 
 
tests
tests
 
 
.all-contributorsrc
.all-contributorsrc
 
 
.dockerignore
.dockerignore
 
 
.env.dev.docker
.env.dev.docker
 
 
.env.docker
.env.docker
 
 
.env.dusk.example
.env.dusk.example
 
 
.env.example
.env.example
 
 
.env.testing-ci
.env.testing-ci
 
 
.env.testing.example
.env.testing.example
 
 
.env.tests
.env.tests
 
 
.env.unit-tests
.env.unit-tests
 
 
.git-blame-ignore-revs
.git-blame-ignore-revs
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.htaccess
.htaccess
 
 
.nvmrc
.nvmrc
 
 
.pa11yci.json
.pa11yci.json
 
 
.upgrade_requirements.json
.upgrade_requirements.json
 
 
CLAUDE.md
CLAUDE.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
CONTRIBUTORS.md
CONTRIBUTORS.md
 
 
Dockerfile
Dockerfile
 
 
Dockerfile.alpine
Dockerfile.alpine
 
 
Dockerfile.fpm-alpine
Dockerfile.fpm-alpine
 
 
LICENSE
LICENSE
 
 
Procfile
Procfile
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
TESTING.md
TESTING.md
 
 
Vagrantfile
Vagrantfile
 
 
_config.yml
_config.yml
 
 
app.json
app.json
 
 
artisan
artisan
 
 
composer.json
composer.json
 
 
composer.lock
composer.lock
 
 
crowdin.yml
crowdin.yml
 
 
dev.docker-compose.yml
dev.docker-compose.yml
 
 
docker-compose.yml
docker-compose.yml
 
 
install.sh
install.sh
 
 
pa11y.js
pa11y.js
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
phpstan.neon.dist
phpstan.neon.dist
 
 
phpstan.neon.example
phpstan.neon.example
 
 
phpunit.xml
phpunit.xml
 
 
pint.json
pint.json
 
 
psalm.xml
psalm.xml
 
 
server.php
server.php
 
 
snipeit.sh
snipeit.sh
 
 
upgrade.php
upgrade.php
 
 
webpack.mix.js
webpack.mix.js
 
 
View all files

## Repository files navigation

 
 

 

## Snipe-IT - Open Source Asset Management System

This is a FOSS project for asset management in IT Operations. Knowing who has which laptop, when it was purchased in order to depreciate it correctly, handling software licenses, etc.

It is built onLaravel 12.

Snipe-IT is actively developed and werelease quite frequently. (Check out the live demo here.)

Tip

This is web-based software. This means there is no executable file (aka no .exe files), and it must be run on a web server and accessed through a web browser. It runs on any Mac OSX, any flavor of Linux, as well as Windows, and we have aDocker imageavailable if that's what you're into.

### Table of Contents

* Installation
* User's Manual
* Bug Reports & Feature Requests
* Security
* Upgrading
* Translations!
* Libraries, Modules & Related Projects
* Join the Community!
* Contributing
* Announcement List

### Installation

For instructions on installing and configuring Snipe-IT on your server, check out theinstallation manual. (Please see therequirements documentationfor full requirements.)

If you're having trouble with the installation, please check theCommon IssuesandGetting Helpdocumentation, and search this repository's openandclosed issues for help.

### User's Manual

For help using Snipe-IT, check out theuser's manual.

### Bug Reports & Feature Requests

Feel free to check out theGitHub Issues for this projectto open a bug report or see what open issues you can help with. Please search through existing issues (openandclosed) to see if your question has already been answered before opening a new issue.

Important

PLEASE see theGetting Help GuidelinesandCommon Issuesbefore opening a ticket, and be sure to complete all of the questions in the Github Issue template to help us to help you as quickly as possible.

### Security

Important

To report a security vulnerability, please emailsecurity@snipeitapp.cominstead of using the issue tracker.

### Upgrading

Please see theupgrading documentationfor instructions on upgrading Snipe-IT.

### Translations!

Please see thetranslations documentationfor information about available languages and how to add translations to Snipe-IT.

### Libraries, Modules & Related Projects

Since the release of the JSON REST API, several third-party developers have been developing modules and libraries to work with Snipe-IT.

Note

As these were created by third-parties, Snipe-IT cannot provide support for these project, and you should contact the developers directly if you need assistance. Additionally, Snipe-IT makes no guarantees as to the reliability, accuracy or maintainability of these libraries. Use at your own risk. :)

#### Libraries & Modules

* SnipeSchedulerby@JSY-Ben- An Asset Reservation/Checkout System for Snipe-IT
* Snipe-IT MCP Serverby@jameshgordy- A Model Context Protocol (MCP) server for managing Snipe-IT inventory systems
* SnipeSharp - .NET module in C#by@barrycarey
* SnipeitPSby@snazy2000- Powershell API Wrapper for Snipe-it
* jamf2snipe- Python script to sync assets between a JAMFPro instance and a Snipe-IT instance
* jamf-snipe-rename- Python script to rename computers in Jamf from Snipe-IT
* Snipe-IT plugin for Jira Service Desk
* Rudder2Snipeby@norbertoaquino- Rudder.io integration for Snipe-IT
* Python 3 CSV importer- allows importing assets into Snipe-IT based on Item Name rather than Asset Tag.
* Snipe-IT Kubernetes Helm Chart- For more information,click here.
* Snipe-IT Bulk Edit- Google Script files to use Google Sheets as a bulk checkout/checkin/edit tool for Snipe-IT.
* MosyleSnipeSyncby@Karpadiem- Python script to synchronize information between Mosyle and Snipe-IT.
* WWW::SnipeITby@SEDC- perl module for accessing the API
* UniFi to Snipe-IToriginally by@karpadiem- Python script that synchronizes UniFi devices with Snipe-IT.
* Kandji2Snipeby@briangoldstein- Python script that synchronizes Kandji with Snipe-IT.
* SnipeAgentby@ReticentRobot- Windows agent for Snipe-IT.
* Gate Pass Generatorby@cha7uraAE- A Streamlit application for generating gate passes based on hardware data from a Snipe-IT API.
* InQRy (archived)by@Microsoft
* Marksman (archived)- A Windows agent for Snipe-IT
* Python Module (archived)by@jbloomerIT-Toolsby @chrisnox - Browser bookmarklets for PDF handover/return protocols, digital signatures, label printing (Zebra ZD410), AirWatch MDM sync and Lansweeper CSV import.

We also have a handful ofGoogle Apps scriptsto help with various tasks.

#### Mobile Apps

We're currently working on our own mobile app, but in the meantime, check out these third-party apps that work with Snipe-IT:

* SnipeMate(iOS, Google Play, Huawei AppGallery) by Mars Technology
* Snipe-Scan(iOS) by Nicolas Maton
* Snipe-IT Assets Management(Google Play) by DiegoGarciaDEV
* AssetX(iOS) for Snipe-IT by Rishi Gupta

### Join the Community!

* Join our Discord!It’s full of great people. We even wrote about ithere!
* Follow us on Blueskyat@snipeitapp.com
* Follow us on Mastodonathachyderm.io/@grokability
* Follow our blogatGrokstar.Dev
* Subscribe hereon Github for notifications about new releases. (We recommend selecting "Releases" only for most users - this repo can get noisy.)

### Contributing

Please refrain from submitting issues or pull requests generated by fully-automated tools. Maintainers reserve the right, at their sole discretion, to close such submissions and to block any account responsible for them.Please see ourAI Contribution Policyfor more information.

Contributions should follow from a human-to-human discussion in the form of an issue for the best chances of being merged into the core project. (Sometimes we might already be working on that feature, sometimes we've decided against )

Please see the complete documentation oncontributing and developing for Snipe-IT.

This project is released with aContributor Code of Conduct. By participating in this project you agree to abide by its terms.

The ERD is availableonline here.

Be sure to check out all of theamazing peoplethat have contributed to Snipe-IT over the years!

### Star History

### Announcement List

To be notified of important news (such as new releases, security advisories, etc),sign up for our list. We'll never sell or give away your info, and we'll only email you when it's important.

We also usually make smaller announcements on our social accounts, our Discord, and our blog, so be sure to subscribe to those if you're looking for more granular announcements.