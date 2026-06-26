---
title: 'GitHub - commaai/openpilot: openpilot is an operating system for robotics. Currently, it upgrades the driver assistance system on 300+ supported cars. · GitHub'
url: https://github.com/commaai/openpilot
site_name: github
content_file: github-github-commaaiopenpilot-openpilot-is-an-operating
fetched_at: '2026-06-26T11:55:35.006535'
original_url: https://github.com/commaai/openpilot
author: commaai
description: openpilot is an operating system for robotics. Currently, it upgrades the driver assistance system on 300+ supported cars. - commaai/openpilot
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 commaai

 

/

openpilot

Public

* NotificationsYou must be signed in to change notification settings
* Fork11k
* Star61.6k

 
 
 
 
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

17,302 Commits
17,302 Commits
.github
.github
 
 
.vscode
.vscode
 
 
docs
docs
 
 
msgq_repo @ 9beb84a
msgq_repo @ 9beb84a
 
 
opendbc_repo @ 58b8955
opendbc_repo @ 58b8955
 
 
openpilot
openpilot
 
 
panda @ 1a40b79
panda @ 1a40b79
 
 
rednose_repo @ 7ffefa3
rednose_repo @ 7ffefa3
 
 
scripts
scripts
 
 
site_scons/
site_tools
site_scons/
site_tools
 
 
teleoprtc_repo @ 22df577
teleoprtc_repo @ 22df577
 
 
tinygrad_repo @ f9c8c69
tinygrad_repo @ f9c8c69
 
 
tools
tools
 
 
.editorconfig
.editorconfig
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
.lfsconfig
.lfsconfig
 
 
.python-version
.python-version
 
 
Jenkinsfile
Jenkinsfile
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
RELEASES.md
RELEASES.md
 
 
SConstruct
SConstruct
 
 
SECURITY.md
SECURITY.md
 
 
conftest.py
conftest.py
 
 
launch_chffrplus.sh
launch_chffrplus.sh
 
 
launch_env.sh
launch_env.sh
 
 
launch_openpilot.sh
launch_openpilot.sh
 
 
msgq
msgq
 
 
opendbc
opendbc
 
 
pyproject.toml
pyproject.toml
 
 
rednose
rednose
 
 
teleoprtc
teleoprtc
 
 
tinygrad
tinygrad
 
 
uv.lock
uv.lock
 
 
zensical.toml
zensical.toml
 
 
View all files

## Repository files navigation

# openpilot

openpilot is an operating system for robotics.Currently, it upgrades the driver assistance system in 300+ supported cars.

### Docs·Roadmap·Contribute·Community·Try it on a comma four

Quick start:bash <(curl -fsSL openpilot.comma.ai)

## Using openpilot in a car

To use openpilot in a car, you need four things:

1. Supported Device:a comma four, available atcomma.ai/shop/comma-four.
2. Software:The setup procedure for the comma four allows users to enter a URL for custom software. Use the URLopenpilot.comma.aito install the release version.
3. Supported Car:Ensure that you have one ofthe 300+ supported cars.
4. Car Harness:You will also need acar harnessto connect your comma four to your car.

We have detailed instructions forhow to install the harness and device in a car. Note that it's possible to run openpilot onother hardware, although it's not plug-and-play.

### Branches

Runningmasterand other branches directly is supported, but it's recommended to run one of the following prebuilt branches:

comma four branch

comma 3X branch

URL

description

release-mici

release-tizi

openpilot.comma.ai

This is openpilot's release branch.

release-mici-staging

release-tizi-staging

openpilot-test.comma.ai

This is the staging branch for releases. Use it to get new releases slightly early.

nightly

nightly

openpilot-nightly.comma.ai

This is the bleeding edge development branch. Do not expect this to be stable.

nightly-dev

nightly-dev

installer.comma.ai/commaai/nightly-dev

Same as nightly, but includes experimental development features for some cars.

## To start developing openpilot

openpilot is developed bycommaand by users like you. We welcome both pull requests and issues onGitHub.

* Join thecommunity Discord
* Check outthe contributing docs
* Check out theopenpilot tools
* Code documentation lives athttps://docs.comma.ai
* Information about running openpilot lives on thecommunity wiki

Want to get paid to work on openpilot?comma is hiringand offers lots ofbountiesfor external contributors.

## Safety and Testing

* openpilot observesISO26262guidelines, seeSAFETY.mdfor more details.
* openpilot has software-in-the-loopteststhat run on every commit.
* The code enforcing the safety model lives in panda and is written in C, seecode rigorfor more details.
* panda has software-in-the-loopsafety tests.
* Internally, we have a hardware-in-the-loop Jenkins test suite that builds and unit tests the various processes.
* panda has additional hardware-in-the-looptests.
* We run the latest openpilot in a testing closet containing 10 comma devices continuously replaying routes.

MIT Licensed

openpilot is released under the MIT license. Some parts of the software are released under other licenses as specified.

Any user of this software shall indemnify and hold harmless Comma.ai, Inc. and its directors, officers, employees, agents, stockholders, affiliates, subcontractors and customers from and against all allegations, claims, actions, suits, demands, damages, liabilities, obligations, losses, settlements, judgments, costs and expenses (including without limitation attorneys’ fees and costs) which arise out of, relate to or result from any use of this software by user.

THIS IS ALPHA QUALITY SOFTWARE FOR RESEARCH PURPOSES ONLY. THIS IS NOT A PRODUCT.
YOU ARE RESPONSIBLE FOR COMPLYING WITH LOCAL LAWS AND REGULATIONS.
NO WARRANTY EXPRESSED OR IMPLIED.

User Data and comma Account

By default, openpilot uploads driving data to our servers. You can also access your data throughcomma connect. We use your data to train better models and improve openpilot for everyone.

openpilot is open source software, and users can disable data collection if they wish.

openpilot logs the road-facing cameras, CAN, GPS, IMU, magnetometer, thermal sensors, crashes, and operating system logs.
The driver-facing camera and microphone are only logged if you explicitly opt-in in settings.

By using openpilot, you agree toour Privacy Policy. You understand that use of this software or its related services will generate certain types of user data, which may be logged and stored at the sole discretion of comma. By accepting this agreement, you grant an irrevocable, perpetual, worldwide right to comma for the use of this data.

## About

openpilot is an operating system for robotics. Currently, it upgrades the driver assistance system on 300+ supported cars.

comma.ai/openpilot

### Topics

 robotics

 driver-assistance-systems

 advanced-driver-assistance-systems

### Resources

 Readme

 

### License

 MIT license
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

61.6k

 stars
 

### Watchers

1.3k

 watching
 

### Forks

11k

 forks
 

 Report repository

 

## Releases63

0.11.1 Release

 Latest

 

Jun 5, 2026

 

+ 62 releases

## Used by168

 + 160
 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python61.0%
* C++32.2%
* Cap'n Proto2.0%
* C1.9%
* Shell1.3%
* Jupyter Notebook1.3%
* Other0.3%