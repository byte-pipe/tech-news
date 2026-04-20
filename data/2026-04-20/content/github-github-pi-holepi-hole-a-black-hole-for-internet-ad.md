---
title: 'GitHub - pi-hole/pi-hole: A black hole for Internet advertisements · GitHub'
url: https://github.com/pi-hole/pi-hole
site_name: github
content_file: github-github-pi-holepi-hole-a-black-hole-for-internet-ad
fetched_at: '2026-04-20T12:02:57.480262'
original_url: https://github.com/pi-hole/pi-hole
author: pi-hole
description: A black hole for Internet advertisements. Contribute to pi-hole/pi-hole development by creating an account on GitHub.
---

pi-hole

 

/

pi-hole

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork3k
* Star56.8k

 
 
 
 
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

7,077 Commits
7,077 Commits
.github
.github
 
 
advanced
advanced
 
 
automated install
automated install
 
 
manpages
manpages
 
 
test
test
 
 
.codespellignore
.codespellignore
 
 
.editorconfig
.editorconfig
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.shellcheckrc
.shellcheckrc
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
gravity.sh
gravity.sh
 
 
pihole
pihole
 
 
View all files

## Repository files navigation

Network-wide ad blocking via your own Linux hardware

The Pi-hole® is aDNS sinkholethat protects your devices from unwanted content without installing any client-side software.

* Easy-to-install: our dialogs walk you through the simple installation process in less than ten minutes
* Resolute: content is blocked innon-browser locations, such as ad-laden mobile apps and smart TVs
* Responsive: seamlessly speeds up the feel of everyday browsing by caching DNS queries
* Lightweight: runs smoothly withminimal hardware and software requirements
* Robust: a command-line interface that is quality assured for interoperability
* Insightful: a beautiful responsive Web Interface dashboard to view and control your Pi-hole
* Versatile: can optionally function as aDHCP server, ensuringallyour devices are protected automatically
* Scalable:capable of handling hundreds of millions of querieswhen installed on server-grade hardware
* Modern: blocks ads over both IPv4 and IPv6
* Free: open source software that helps ensureyouare the sole person in control of your privacy

## One-Step Automated Install

Those who want to get started quickly and conveniently may install Pi-hole using the following command:

curl -sSL https://install.pi-hole.net 
|
 bash

## Alternative Install Methods

Piping tobashiscontroversial, as it prevents you fromreading code that is about to runon your system. Therefore, we provide these alternative installation methods which allow code review before installation:

### Method 1: Clone our repository and run

git clone --depth 1 https://github.com/pi-hole/pi-hole.git Pi-hole

cd
 
"
Pi-hole/automated install/
"

sudo bash basic-install.sh

### Method 2: Manually download the installer and run

wget -O basic-install.sh https://install.pi-hole.net
sudo bash basic-install.sh

### Method 3: Using Docker to deploy Pi-hole

Please refer to thePi-hole docker repoto use the Official Docker Images.

## Post-install: Make your network take advantage of Pi-hole

Once the installer has been run, you will need toconfigure your router to haveDHCP clients use Pi-hole as their DNS server. This router configuration will ensure that all devices connecting to your network will have content blocked without any further intervention.

If your router does not support setting the DNS server, you canuse Pi-hole's built-in DHCP server; be sure to disable DHCP on your router first (if it has that feature available).

As a last resort, you can manually set each device to use Pi-hole as their DNS server.

## Pi-hole is free but powered by your support

There are many reoccurring costs involved with maintaining free, open-source, and privacy-respecting software; expenses whichour volunteer developerspitch in to cover out-of-pocket. This is just one example of how strongly we feel about our software and the importance of keeping it maintained.

Make no mistake:your support is absolutely vital to help keep us innovating!

### Donations

Donating using our Sponsor Button isextremely helpfulin offsetting a portion of our monthly expenses:

### Alternative support

If you'd rather not donate (which is okay!), there are other ways you can help support us:

* GitHub Sponsors
* Patreon
* Hetzner Cloudaffiliate link
* Digital Oceanaffiliate link
* Stickermuleearn a $10 credit after your first purchase
* Amazon USaffiliate link
* Spreading the word about our software and how you have benefited from it

### Contributing via GitHub

We welcomeeveryoneto contribute to issue reports, suggest new features, and create pull requests.

If you have something to add - anything from a typo through to a whole new feature, we're happy to check it out! Just make sure to fill out our template when submitting your request; the questions it asks will help the volunteers quickly understand what you're aiming to achieve.

You'll find that theinstall scriptand thedebug scripthave an abundance of comments, which will help you better understand how Pi-hole works. They're also a valuable resource to those who want to learn how to write scripts or code a program! We encourage anyone who likes to tinker to read through it and submit a pull request for us to review.

## Getting in touch with us

While we are primarily reachable on ourDiscourse User Forum, we can also be found on various social media outlets.

Please be sure to check the FAQsbefore starting a new discussion, as we do not have the spare time to reply to every request for assistance.

* Frequently Asked Questions
* Feature Requests
* Reddit
* Twitter

## Breakdown of Features

### Faster-than-light Engine

FTLDNSis a lightweight, purpose-built daemon used to provide statistics needed for the Web Interface, and its API can be easily integrated into your own projects. As the name implies, FTLDNS does this allvery quickly!

Some of the statistics you can integrate include:

* Total number of domains being blocked
* Total number of DNS queries today
* Total number of ads blocked today
* Percentage of ads blocked
* Unique domains
* Queries forwarded (to your chosen upstream DNS server)
* Queries cached
* Unique clients

Access the API using:

* your browser:http://pi.hole/api/docs
* curl:curl --connect-timeout 2 -ks "https://pi.hole/api/stats/summary" -H "Accept: application/json";
* the command line - examples:pihole api config/webserver/portorpihole api stats/summary.

### The Command-Line Interface

Thepiholecommand has all the functionality necessary to fully administer the Pi-hole, without the need for the Web Interface. It's fast, user-friendly, and auditable by anyone with an understanding ofbash.

Some notable features include:

* Allowlisting, Denylisting (fka Whitelisting, Blacklisting), and Regex
* Debugging utility
* Viewing the live log file
* Updating Ad Lists
* Querying Ad Lists for blocked domains
* Enabling and Disabling Pi-hole
* ... andmanymore!

You can read ourCore Feature Breakdownfor more information.

### The Web Interface Dashboard

Thisoptional dashboardallows you to view stats, change settings, and configure your Pi-hole. It's the power of the Command Line Interface, with none of the learning curve!

Some notable features include:

* Mobile-friendly interface
* Password protection
* Detailed graphs and doughnut charts
* Top lists of domains and clients
* A filterable and sortable query log
* Long Term Statistics to view data over user-defined time ranges
* The ability to easily manage and configure Pi-hole features
* ... and all the main features of the Command Line Interface!

There are several ways toaccess the dashboard:

1. http://pi.hole/admin/(when using Pi-hole as your DNS server)
2. http://<IP_ADDRESS_OF_YOUR_PI_HOLE>/admin/

## About

A black hole for Internet advertisements

pi-hole.net

### Topics

 shell

 raspberry-pi

 cloud

 dashboard

 dhcp

 pi-hole

 ad-blocker

 dnsmasq

 dhcp-server

 blocker

 dns-server

### Resources

 Readme

 

### License

 View license
 

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

56.8k

 stars
 

### Watchers

708

 watching
 

### Forks

3k

 forks
 

 Report repository

 

## Releases124

v6.4.1

 Latest

 

Apr 3, 2026

 

+ 123 releases

## Sponsor this project

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 
* https://pi-hole.net/donate
* patreon.com/pihole

Learn more about GitHub Sponsors

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors240

+ 226 contributors

## Languages

* Shell88.2%
* Python7.2%
* Dockerfile2.6%
* Roff2.0%