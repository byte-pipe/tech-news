---
title: 'GitHub - apple/container: A tool for creating and running Linux containers using lightweight virtual machines on a Mac. It is written in Swift, and optimized for Apple silicon. · GitHub'
url: https://github.com/apple/container
site_name: github
content_file: github-github-applecontainer-a-tool-for-creating-and-runn
fetched_at: '2026-06-10T12:07:32.544430'
original_url: https://github.com/apple/container
author: apple
description: 'A tool for creating and running Linux containers using lightweight virtual machines on a Mac. It is written in Swift, and optimized for Apple silicon. - GitHub - apple/container: A tool for creating and running Linux containers using lightweight virtual machines on a Mac. It is written in Swift, and optimized for Apple silicon.'
---

apple

 

/

container

Public

* NotificationsYou must be signed in to change notification settings
* Fork800
* Star28.4k

 
 
 
 
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

639 Commits
639 Commits
.github
.github
 
 
Sources
Sources
 
 
Tests
Tests
 
 
assets
assets
 
 
docs
docs
 
 
examples/
container-machine-vscode
examples/
container-machine-vscode
 
 
scripts
scripts
 
 
signing
signing
 
 
.gitignore
.gitignore
 
 
.spi.yml
.spi.yml
 
 
.swift-format
.swift-format
 
 
.swift-format-nolint
.swift-format-nolint
 
 
BUILDING.md
BUILDING.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
MAINTAINERS.txt
MAINTAINERS.txt
 
 
Makefile
Makefile
 
 
NOTICE.md
NOTICE.md
 
 
Package.resolved
Package.resolved
 
 
Package.swift
Package.swift
 
 
Protobuf.Makefile
Protobuf.Makefile
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
licenserc.toml
licenserc.toml
 
 
View all files

## Repository files navigation

# container

containeris a tool that you can use to create and run Linux containers as lightweight virtual machines on your Mac. It's written in Swift, and optimized for Apple silicon.

The tool consumes and producesOCI-compatible container images, so you can pull and run images from any standard container registry. You can push images that you build to those registries as well, and run the images in any other OCI-compatible application.

containeruses theContainerizationSwift package for low-level container, image, and process management.

## Get started

### Requirements

You need a Mac with Apple silicon to runcontainer. To build it, see theBUILDINGdocument.

containeris supported on macOS 26, since it takes advantage of new features and enhancements to virtualization and networking in this release. We do not support older versions of macOS and thecontainermaintainers typically will not address issues that cannot be reproduced on macOS 26.

### Initial install

Download the latest signed installer package forcontainerfrom theGitHub release page.

To install the tool, double-click the package file and follow the instructions. Enter your administrator password when prompted, to give the installer permission to place the installed files under/usr/local.

Start the system service with:

container system start

### Upgrade or downgrade

For both upgrading and downgrading, you can manually download and install the signed installer package by following the steps frominitial installor use theupdate-container.shscript (installed to/usr/local/bin).

If you're upgrading or downgrading, you must stop your existingcontainer:

container system stop

To upgrade to the latest release, simply run the command below:

/usr/local/bin/update-container.sh

To downgrade, you must uninstall your existingcontainer(the-kflag keeps your user data, while-dremoves it):

/usr/local/bin/uninstall-container.sh -k
/usr/local/bin/update-container.sh -v 0.3.0

Start the system service with:

container system start

### Uninstall

Use theuninstall-container.shscript (installed to/usr/local/bin) to removecontainerfrom your system. To remove your user data along with the tool, run:

/usr/local/bin/uninstall-container.sh -d

To retain your user data so that it is available should you reinstall later, run:

/usr/local/bin/uninstall-container.sh -k

## Next steps

* Takea guided tour ofcontainerby building, running, and publishing a simple web server image.
* Learn how touse variouscontainerfeatures.
* Read a brief description andtechnical overviewofcontainer.
* Browse thefull command reference.
* Build and runcontaineron your own development system.
* View the projectAPI documentation.

## Contributing

Contributions tocontainerare welcome and encouraged. Please see ourmain contributing guidefor more information.

## Project Status

The container project is currently under active development. Its stability, both for consuming the project as a Swift package and thecontainertool, is only guaranteed within patch versions, such as between 0.1.1 and 0.1.2. Minor version releases may include breaking changes until we reach a 1.0.0 release.

## About

A tool for creating and running Linux containers using lightweight virtual machines on a Mac. It is written in Swift, and optimized for Apple silicon.

apple.github.io/container/documentation/

### Resources

 Readme

 

### License

 Apache-2.0 license
 

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

28.4k

 stars
 

### Watchers

130

 watching
 

### Forks

800

 forks
 

 Report repository

 

## Releases16

1.0.0

 Latest

 

Jun 9, 2026

 

+ 15 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Swift98.2%
* Other1.8%