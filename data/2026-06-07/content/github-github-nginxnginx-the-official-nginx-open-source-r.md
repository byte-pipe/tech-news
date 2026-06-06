---
title: 'GitHub - nginx/nginx: The official NGINX Open Source repository. · GitHub'
url: https://github.com/nginx/nginx
site_name: github
content_file: github-github-nginxnginx-the-official-nginx-open-source-r
fetched_at: '2026-06-07T06:00:12.759948'
original_url: https://github.com/nginx/nginx
author: nginx
description: The official NGINX Open Source repository. Contribute to nginx/nginx development by creating an account on GitHub.
---

nginx

 

/

nginx

Public

* NotificationsYou must be signed in to change notification settings
* Fork8k
* Star30.7k

 
 
 
 
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

8,610 Commits
8,610 Commits
.github
.github
 
 
auto
auto
 
 
conf
conf
 
 
contrib
contrib
 
 
docs
docs
 
 
misc
misc
 
 
src
src
 
 
.gitignore
.gitignore
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
SUPPORT.md
SUPPORT.md
 
 
View all files

## Repository files navigation

NGINX (pronounced "engine x" or "en-jin-eks") is the world's most popular Web Server, high performance Load Balancer, Reverse Proxy, API Gateway and Content Cache.

NGINX is free and open source software, distributed under the terms of a simplified2-clause BSD-like license.

Enterprise distributions, commercial support and training are available fromF5, Inc.

Important

The goal of this README is to provide a basic, structured introduction to NGINX for novice users. Please refer to thefull NGINX documentationfor detailed information oninstalling,building,configuring,debugging, and more. These documentation pages also contain a more detailedBeginners Guide, How-Tos,Development guide, and a complete module anddirective reference.

# Table of contents

* How it worksModulesConfigurationsRuntime
* Modules
* Configurations
* Runtime
* Downloading and installingStable and Mainline binariesLinux binary installation processFreeBSD installation processWindows executablesDynamic modules
* Stable and Mainline binaries
* Linux binary installation process
* FreeBSD installation process
* Windows executables
* Dynamic modules
* Getting started with NGINXInstalling SSL certificates and enabling TLS encryptionLoad BalancingRate limitingContent caching
* Installing SSL certificates and enabling TLS encryption
* Load Balancing
* Rate limiting
* Content caching
* Building from sourceInstalling dependenciesCloning the NGINX GitHub repositoryConfiguring the buildCompilingLocation of binary and installationRunning and testing the installed binary
* Installing dependencies
* Cloning the NGINX GitHub repository
* Configuring the build
* Compiling
* Location of binary and installation
* Running and testing the installed binary
* Asking questions and reporting issues
* Contributing code
* Additional help and resources
* Changelog
* License

# How it works

NGINX is installed software with binary packages available for all major operating systems and Linux distributions. SeeTested OS and Platformsfor a full list of compatible systems.

Important

While nearly all popular Linux-based operating systems are distributed with a community version of nginx, we highly advise installation and usage of officialpackagesor sources from this repository. Doing so ensures that you're using the most recent release or source code, including the latest feature-set, fixes and security patches.

## Modules

NGINX is comprised of individual modules, each extending core functionality by providing additional, configurable features. See "Modules reference" at the bottom ofnginx documentationfor a complete list of official modules.

NGINX modules can be built and distributed as static or dynamic modules. Static modules are defined at build-time, compiled, and distributed in the resulting binaries. SeeDynamic Modulesfor more information on how they work, as well as, how to obtain, install, and configure them.

Tip

You can issue the following command to see which static modules your NGINX binaries were built with:

nginx -V

SeeConfiguring the buildfor information on how to include specific Static modules into your nginx build.

## Configurations

NGINX is highly flexible and configurable. Provisioning the software is achieved via text-based config file(s) accepting parameters called "Directives". SeeConfiguration File's Structurefor a comprehensive description of how NGINX configuration files work.

Note

The set of directives available to your distribution of NGINX is dependent on whichmoduleshave been made available to it.

## Runtime

Rather than running in a single, monolithic process, NGINX is architected to scale beyond Operating System process limitations by operating as a collection of processes. They include:

* A "master" process that maintains worker processes, as well as, reads and evaluates configuration files.
* One or more "worker" processes that process data (eg. HTTP requests).

The number ofworker processesis defined in the configuration file and may be fixed for a given configuration or automatically adjusted to the number of available CPU cores. In most cases, the latter option optimally balances load across available system resources, as NGINX is designed to efficiently distribute work across all worker processes.

Tip

Processes synchronize data through shared memory. For this reason, many NGINX directives require the allocation of shared memory zones. As an example, when configuringrate limiting, connecting clients may need to be tracked in acommon memory zoneso all worker processes can know how many times a particular client has accessed the server in a span of time.

# Downloading and installing

Follow these steps to download and install precompiled NGINX binaries. You may also choose tobuild NGINX locally from source code.

## Stable and Mainline binaries

NGINX binaries are built and distributed in two versions: stable and mainline. Stable binaries are built from stable branches and only contain critical fixes backported from the mainline version. Mainline binaries are built from themaster branchand contain the latest features and bugfixes. You'll need todecide which is appropriate for your purposes.

## Linux binary installation process

The NGINX binary installation process takes advantage of package managers native to specific Linux distributions. For this reason, first-time installations involve adding the official NGINX package repository to your system's package manager. Followthese stepsto download, verify, and install NGINX binaries using the package manager appropriate for your Linux distribution.

### Upgrades

Future upgrades to the latest version can be managed using the same package manager without the need to manually download and verify binaries.

## FreeBSD installation process

For more information on installing NGINX on FreeBSD system, visithttps://nginx.org/en/docs/install.html

## Windows executables

Windows executables for mainline and stable releases can be found on the mainNGINX download page. Note that the current implementation of NGINX for Windows is at the Proof-of-Concept stage and should only be used for development and testing purposes. For additional information, please seenginx for Windows.

## Dynamic modules

NGINX version 1.9.11 added support forDynamic Modules. Unlike Static modules, dynamically built modules can be downloaded, installed, and configured after the core NGINX binaries have been built.Official dynamic module binariesare available from the same package repository as the core NGINX binaries described in previous steps.

Tip

NGINX JavaScript (njs), is a popular NGINX dynamic module that enables the extension of core NGINX functionality using familiar JavaScript syntax.

Important

If desired, dynamic modules can also be built statically into NGINX at compile time.

# Getting started with NGINX

For a gentle introduction to NGINX basics, please see ourBeginner’s Guide.

## Installing SSL certificates and enabling TLS encryption

SeeConfiguring HTTPS serversfor a quick guide on how to enable secure traffic to your NGINX installation.

## Load Balancing

For a quick start guide on configuring NGINX as a Load Balancer, please seeUsing nginx as HTTP load balancer.

## Rate limiting

See ourRate Limiting with NGINXblog post for an overview of core concepts for provisioning NGINX as an API Gateway.

## Content caching

SeeA Guide to Caching with NGINX and NGINX Plusblog post for an overview of how to use NGINX as a content cache (e.g. edge server of a content delivery network).

# Building from source

The following steps can be used to build NGINX from source code available in this repository.

## Installing dependencies

Most Linux distributions will require several dependencies to be installed in order to build NGINX. The following instructions are specific to theaptpackage manager, widely available on most Ubuntu/Debian distributions and their derivatives.

Tip

It is always a good idea to update your package repository lists prior to installing new packages.

sudo apt update

### Installing compiler and make utility

Use the following command to install the GNU C compiler and Make utility.

sudo apt install gcc make

### Installing dependency libraries

sudo apt install libpcre3-dev zlib1g-dev

Warning

This is the minimal set of dependency libraries needed to build NGINX with rewriting and gzip capabilities. Other dependencies may be required if you choose to build NGINX with additional modules. Monitor the output of theconfigurecommand discussed in the following sections for information on which modules may be missing. For example, if you plan to use SSL certificates to encrypt traffic with TLS, you'll need to install the OpenSSL library. To do so, issue the following command.

sudo apt install libssl-dev

## Cloning the NGINX GitHub repository

Using your preferred method, clone the NGINX repository into your development directory. SeeCloning a GitHub Repositoryfor additional help.

git clone https://github.com/nginx/nginx.git

## Configuring the build

Prior to building NGINX, you must run theconfigurescript withappropriate flags. This will generate a Makefile in your NGINX source root directory that can then be used to compile NGINX withoptions specified during configuration.

From the NGINX source code repository's root directory:

auto/configure

Important

Configuring the build without any flags will compile NGINX with the default set of options. Please refer tohttps://nginx.org/en/docs/configure.htmlfor a full list of available build configuration options.

## Compiling

Theconfigurescript will generate aMakefilein the NGINX source root directory upon successful execution. To compile NGINX into a binary, issue the following command from that same directory:

make

## Location of binary and installation

After successful compilation, a binary will be generated at<NGINX_SRC_ROOT_DIR>/objs/nginx. To install this binary, issue the following command from the source root directory:

sudo make install

Important

The binary will be installed into the/usr/local/nginx/directory.

## Running and testing the installed binary

To run the installed binary, issue the following command:

sudo /usr/local/nginx/sbin/nginx

You may test NGINX operation usingcurl.

curl localhost

The output of which should start with:

<!DOCTYPE html
>

<
html
>

<
head
>

<
title
>
Welcome to nginx!
</
title
>

# Asking questions and reporting issues

See ourSupportguidelines for information on how discuss the codebase, ask troubleshooting questions, and report issues.

# Contributing code

Please see theContributingguide for information on how to contribute code.

# Additional help and resources

* See theNGINX Community Blogfor more tips, tricks and HOW-TOs related to NGINX and related projects.
* Accessnginx.org, your go-to source for all documentation, information and software related to the NGINX suite of projects.

# Changelog

See ourchangelogto keep track of updates.

# License

2-clause BSD-like license

Additional documentation available at:https://nginx.org/en/docs

## About

The official NGINX Open Source repository.

nginx.org/

### Topics

 nginx

 tls

 http

 security

 web-server

 https

 http2

 load-balancer

 reverse-proxy

 quic

 http3

 tcp-proxy-server

 content-cache

 udp-proxy-server

 mail-proxy-server

### Resources

 Readme

 

### License

 BSD-2-Clause license
 

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

30.7k

 stars
 

### Watchers

949

 watching
 

### Forks

8k

 forks
 

 Report repository

 

## Releases23

release-1.31.1

 Latest

 

May 22, 2026

 

+ 22 releases

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* C97.7%
* Vim Script1.7%
* XS0.4%
* Perl0.1%
* Makefile0.1%
* Shell0.0%