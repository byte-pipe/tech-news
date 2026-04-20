---
title: 'GitHub - localstack/localstack: 💻 A fully functional local AWS cloud stack. Develop and test your cloud & Serverless apps offline · GitHub'
url: https://github.com/localstack/localstack
site_name: hackernews_api
content_file: hackernews_api-github-localstacklocalstack-a-fully-functional-loc
fetched_at: '2026-03-25T01:01:42.839660'
original_url: https://github.com/localstack/localstack
author: ecshafer
date: '2026-03-24'
description: 💻 A fully functional local AWS cloud stack. Develop and test your cloud & Serverless apps offline - localstack/localstack
tags:
- hackernews
- trending
---

This repository was archived by the owner on Mar 23, 2026. It is now read-only.


 localstack



/

localstack

Public archive

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork4.6k
* Star64.8k




 
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

7,855 Commits
7,855 Commits
.github
.github
 
 
bin
bin
 
 
docs
docs
 
 
localstack-core
localstack-core
 
 
scripts
scripts
 
 
tests
tests
 
 
.dockerignore
.dockerignore
 
 
.git-blame-ignore-revs
.git-blame-ignore-revs
 
 
.gitignore
.gitignore
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
.python-version
.python-version
 
 
.test_durations
.test_durations
 
 
AGENTS.md
AGENTS.md
 
 
CODEOWNERS
CODEOWNERS
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
DOCKER.md
DOCKER.md
 
 
Dockerfile
Dockerfile
 
 
Dockerfile.s3
Dockerfile.s3
 
 
LICENSE.txt
LICENSE.txt
 
 
MANIFEST.in
MANIFEST.in
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
docker-compose-pro.yml
docker-compose-pro.yml
 
 
docker-compose.yml
docker-compose.yml
 
 
plux.ini
plux.ini
 
 
pyproject.toml
pyproject.toml
 
 
requirements-base-runtime.txt
requirements-base-runtime.txt
 
 
requirements-basic.txt
requirements-basic.txt
 
 
requirements-dev.txt
requirements-dev.txt
 
 
requirements-runtime.txt
requirements-runtime.txt
 
 
requirements-test.txt
requirements-test.txt
 
 
requirements-typehint.txt
requirements-typehint.txt
 
 
View all files

## Repository files navigation

Important

Project Update: Consolidation into the Unified LocalStack Image

To provide a more reliable and streamlined experience, we are consolidating our development into a single, unified image. As part of this transition, this repository is nowarchived and read-only.

This decision reflects our commitment to reducing fragmentation and focusing our resources on building the most robust AWS emulation layer possible. We are deeply grateful to the contributors who helped make this project into what it is today–your work remains integral to the future of the LocalStack ecosystem.

What this means for your workflow:

* LocalStack for AWS offers arange of optionsincluding a free Hobby plan for non-commercial use with the same capabilities as this project.
* Your input is still vital to us. Please continue to sharebug reports hereandsubmit feature requests hereor join ourSlack Community.

Thank you for your continued support as we grow together.

LocalStack is a cloud software development framework to develop and test your AWS applications locally.

Overview•Install•Quickstart•Run•Usage•Releases•Contributing📖 Docs•💻 LocalStack for AWS•☑️ LocalStack coverage

# Overview

LocalStackis a cloud service emulator that runs in a single container on your laptop or in your CI environment. With LocalStack, you can run your AWS applications or Lambdas entirely on your local machine without connecting to a remote cloud provider! Whether you are testing complex CDK applications or Terraform configurations, or just beginning to learn about AWS services, LocalStack helps speed up and simplify your testing and development workflow.

LocalStack supports a growing number of AWS services, like AWS Lambda, S3, DynamoDB, Kinesis, SQS, SNS, and many more! ThePro version of LocalStacksupports additional APIs and advanced features. You can find a comprehensive list of supported APIs on our☑️ Feature Coveragepage.

LocalStack also provides additional features to make your life as a cloud developer easier! Check out LocalStack'sUser Guidesfor more information.

## Install

The quickest way to get started with LocalStack is by using the LocalStack CLI. It enables you to start and manage the LocalStack Docker container directly through your command line. Ensure that your machine has a functionaldockerenvironmentinstalled before proceeding.

### Brew (macOS or Linux with Homebrew)

Install the LocalStack CLI through ourofficial LocalStack Brew Tap:

brew install localstack/tap/localstack-cli

### Binary download (macOS, Linux, Windows)

If Brew is not installed on your machine, you can download the pre-built LocalStack CLI binary directly:

* Visitlocalstack/localstack-cliand download the latest release for your platform.
* Extract the downloaded archive to a directory included in yourPATHvariable:For macOS/Linux, use the command:sudo tar xvzf ~/Downloads/localstack-cli-*-darwin-*-onefile.tar.gz -C /usr/local/bin
* For macOS/Linux, use the command:sudo tar xvzf ~/Downloads/localstack-cli-*-darwin-*-onefile.tar.gz -C /usr/local/bin

### PyPI (macOS, Linux, Windows)

LocalStack is developed using Python. To install the LocalStack CLI usingpip, run the following command:

python3 -m pip install localstack

Thelocalstack-cliinstallation enables you to run the Docker image containing the LocalStack runtime. To interact with the local AWS services, you need to install theawslocalCLI separately. For installation guidelines, refer to theawslocaldocumentation.

Important: Do not usesudoor run asrootuser. LocalStack must be installed and started entirely under a local non-root user. If you have problems with permissions in macOS High Sierra, install withpip install --user localstack

## Quickstart

Start LocalStack inside a Docker container by running:

 % localstack start -d

 __ _______ __ __
 / / ____ _________ _/ / ___// /_____ ______/ /__
 / / / __
\/
 ___/ __
`
/ /
\_
_
\/
 __/ __
`
/ ___/ //_/
 / /___/ /_/ / /__/ /_/ / /___/ / /_/ /_/ / /__/ ,
<

 /_____/
\_
___/
\_
__/
\_
_,_/_//____/
\_
_/
\_
_,_/
\_
__/_/
|
_
|

- LocalStack CLI: 4.9.0
- Profile: default
- App: https://app.localstack.cloud

[17:00:15] starting LocalStack
in
 Docker mode 🐳 localstack.py:512
 preparing environment bootstrap.py:1322
 configuring container bootstrap.py:1330
 starting container bootstrap.py:1340
[17:00:16] detaching bootstrap.py:1344

You can query the status of respective services on LocalStack by running:

% localstack status services
┏━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┓
┃ Service ┃ Status ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━┩
│ acm │ ✔ available │
│ apigateway │ ✔ available │
│ cloudformation │ ✔ available │
│ cloudwatch │ ✔ available │
│ config │ ✔ available │
│ dynamodb │ ✔ available │
...

To use SQS, a fully managed distributed message queuing service, on LocalStack, run:

% awslocal sqs create-queue --queue-name sample-queue
{

"
QueueUrl
"
:
"
http://sqs.us-east-1.localhost.localstack.cloud:4566/000000000000/sample-queue
"

}

Learn more aboutLocalStack AWS servicesand using them with LocalStack'sawslocalCLI.

## Running

You can run LocalStack through the following options:

* LocalStack CLI
* Docker
* Docker Compose
* Helm

## Usage

To start using LocalStack, check out ourdocumentation.

* LocalStack Configuration
* LocalStack in CI
* LocalStack Integrations
* LocalStack Tools
* Understanding LocalStack
* Frequently Asked Questions

To use LocalStack with a graphical user interface, you can use the following UI clients:

* LocalStack Web Application
* LocalStack Desktop
* LocalStack Docker Extension

## Releases

Please refer toGitHub releasesto see the complete list of changes for each release. For extended release notes, please refer to thechangelog.

## Contributing

If you are interested in contributing to LocalStack:

* Start by reading ourcontributing guide.
* Check out ourdevelopment environment setup guide.
* Navigate our codebase andopen issues.

We are thankful for all the contributions and feedback we receive.

## Get in touch

Get in touch with the LocalStack Team to
report 🐞issues,
upvote 👍feature requests,
🙋🏽 asksupport questions,
or 🗣️ discuss local cloud development:

* LocalStack Slack Community
* LocalStack GitHub Issue tracker

### Contributors

We are thankful to all the people who have contributed to this project.

### Backers

We are also grateful to all our backers who have donated to the project. You can become a backer onOpen Collective.

### Sponsors

You can also support this project by becoming a sponsor onOpen Collective. Your logo will show up here along with a link to your website.

## License

Copyright (c) 2017-2026 LocalStack maintainers and contributors.

Copyright (c) 2016 Atlassian and others.

This version of LocalStack is released under the Apache License, Version 2.0 (seeLICENSE). By downloading and using this software you agree to theEnd-User License Agreement (EULA).

## About

💻 A fully functional local AWS cloud stack. Develop and test your cloud & Serverless apps offline

localstack.cloud

### Topics

 python

 testing

 aws

 cloud

 continuous-integration

 developer-tools

 localstack

### Resources

 Readme



### License

 View license


### Code of conduct

 Code of conduct


### Contributing

 Contributing


### Uh oh!

There was an error while loading.Please reload this page.





Activity


Custom properties


### Stars

64.8k

 stars


### Watchers

513

 watching


### Forks

4.6k

 forks


 Report repository



## Releases106

v4.14.0

 Latest



Feb 26, 2026



+ 105 releases

## Sponsor this project

### Uh oh!

There was an error while loading.Please reload this page.






* opencollective.com/localstack

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.





## Contributors

### Uh oh!

There was an error while loading.Please reload this page.





## Languages

* Python99.2%
* Makefile0.2%
* Shell0.2%
* ANTLR0.1%
* JavaScript0.1%
* Java0.1%
* Other0.1%
