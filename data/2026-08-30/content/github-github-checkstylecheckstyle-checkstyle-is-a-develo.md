---
title: 'GitHub - checkstyle/checkstyle: Checkstyle is a development tool to help programmers write Java code that adheres to a coding standard. By default it supports the Google Java Style Guide and Sun Code Conventions, but is highly configurable. It can be invoked with an ANT task and a command line program. · GitHub'
url: https://github.com/checkstyle/checkstyle
site_name: github
content_file: github-github-checkstylecheckstyle-checkstyle-is-a-develo
fetched_at: '2026-08-30T15:11:54.710338'
original_url: https://github.com/checkstyle/checkstyle
author: checkstyle
description: Checkstyle is a development tool to help programmers write Java code that adheres to a coding standard. By default it supports the Google Java Style Guide and Sun Code Conventions, but is highly configurable. It can be invoked with an ANT task and a command line program. - checkstyle/checkstyle
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 checkstyle

 

/

checkstyle

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork4.2k
* Star9.1k

 
 
 
master
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

17,589 Commits
17,589 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.buildkite
.buildkite
 
 
.ci
.ci
 
 
.circleci
.circleci
 
 
.github
.github
 
 
.mvn
.mvn
 
 
.semaphore
.semaphore
 
 
config
config
 
 
docs
docs
 
 
src
src
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.mdlrc
.mdlrc
 
 
.shellcheckrc
.shellcheckrc
 
 
LICENSE
LICENSE
 
 
LICENSE.apache20
LICENSE.apache20
 
 
README.md
README.md
 
 
RIGHTS.antlr
RIGHTS.antlr
 
 
SECURITY.md
SECURITY.md
 
 
appveyor.yml
appveyor.yml
 
 
azure-pipelines.yml
azure-pipelines.yml
 
 
cdg-pitest-licence.txt
cdg-pitest-licence.txt
 
 
mvnw
mvnw
 
 
mvnw.cmd
mvnw.cmd
 
 
pom.xml
pom.xml
 
 
View all files

## Repository files navigation

# Checkstyle - Java Code Quality Tool

Checkstyle is a tool that ensures adherence to a code standard or a set of best practices.

The latest release version can be found atGitHub releasesor atMaven repo.

Documentation is available in HTML format, seeCheckstyle checks.

The latest deployed website frommasteris availablehere.

## Table of Contents

* Quick Start
* Contributing
* Feedback and Support
* Javadoc
* Sponsor Checkstyle
* Licensing

## Quick Start

* Download ourLatest Releasefrom GitHub
or add Checkstyle to your build fromMaven Central.
* Read our Documentation forusageandconfiguration.

$ cat config.xml

<
?
xml version=
"
1.0
"
?
>

<
!
DOCTYPE module PUBLIC
 
"
-//Puppy Crawl//DTD Check Configuration 1.3//EN
"

 
"
https://checkstyle.org/dtds/configuration_1_3.dtd
"
>

<
module name=
"
Checker
"
>

 
<
module name=
"
TreeWalker
"
>

 
<
module name=
"
FallThrough
"
/
>

 
<
/module
>

<
/module
>

$ cat Test.java
class Test {
 public void 
foo
() {
 int i = 0
;

 
while
 (i 
>
= 0) {
 switch (i) {
 
case
 1:
 
case
 2:
 i++
;

 
case
 3: // violation 
'
fall from previous branch of the switch
'

 i++
;

 }
 }
 }
}

$ java -jar checkstyle-10.18.1-all.jar -c config.xml Test.java
Starting audit...
[ERROR] Test.java:9:9: Fall through from previous branch of switch statement [FallThrough]
Audit done.
Checkstyle ends with 1 errors.

## Contributing

Thanks for your interest in contributing to CheckStyle! Please see theContribution Guidelinesfor information on how to contribute to the
project. This includes creating issues, submitting pull requests, and setting up your development
environment.

## Build Instructions

Please see theBuild Instructionsfor
information on how to build the project.

## Feedback and Support

* Visit ourDiscussions Page, where you
can ask questions and discuss the project with other users and contributors. This is our
preferred method of communication for topics
like usage and configuration questions, debugging, and other feedback.
* Stack Overflowis another place to
ask questions about Checkstyle usage.
* If you are interested in contributing to the project, you can join ourDiscord Contributors Chatwith invite link.
* OurGoogle Groups Forumis a
mailing list for discussion and support; however, we may be slow to respond there.

## Javadoc

Take a look at ourjavadocto see
our API documentation.

## Sponsor Checkstyle

Checkstyle is an open-source project that is developed and maintained by volunteers. If you
find Checkstyle useful, please consider sponsoring the project. Your support helps us to
maintain and improve Checkstyle.

* Liberapay
* OpenCollective

## Licensing

Checkstyle is licensed under theGNU LGPL v2.1 License.
Checkstyle uses libraries:

* ANTLR
* Apache Commons
* Google Guava
* Picocli

## Development Tools Powered by