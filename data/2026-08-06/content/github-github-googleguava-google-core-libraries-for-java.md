---
title: 'GitHub - google/guava: Google core libraries for Java · GitHub'
url: https://github.com/google/guava
site_name: github
content_file: github-github-googleguava-google-core-libraries-for-java
fetched_at: '2026-08-06T12:55:05.416257'
original_url: https://github.com/google/guava
author: google
description: Google core libraries for Java. Contribute to google/guava development by creating an account on GitHub.
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 google

 

/

guava

Public

* NotificationsYou must be signed in to change notification settings
* Fork11.2k
* Star51.6k

 
 
 
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

7,457 Commits
7,457 Commits
.github
.github
 
 
.mvn/
wrapper
.mvn/
wrapper
 
 
android
android
 
 
futures
futures
 
 
guava-bom
guava-bom
 
 
guava-gwt
guava-gwt
 
 
guava-testlib
guava-testlib
 
 
guava-tests
guava-tests
 
 
guava
guava
 
 
integration-tests/
gradle
integration-tests/
gradle
 
 
proguard
proguard
 
 
util
util
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
CONTRIBUTORS
CONTRIBUTORS
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
cycle_suppress_list.txt
cycle_suppress_list.txt
 
 
mvnw
mvnw
 
 
mvnw.cmd
mvnw.cmd
 
 
overview.html
overview.html
 
 
pom.xml
pom.xml
 
 
View all files

## Repository files navigation

# Guava: Google Core Libraries for Java

Guava is a set of core Java libraries from Google that includes new collection
types (such as multimap and multiset), immutable collections, a graph library,
and utilities for concurrency, I/O, hashing, primitives, strings, and more! It
is widely used on most Java projects within Google, and widely used by many
other companies as well.

Guava comes in two flavors:

* The JRE flavor requires JDK 1.8 or higher.
* If you need support for Android, usethe Android flavor. You can
find the Android Guava source in theandroiddirectory.

## Adding Guava to your build

Guava's Maven group ID iscom.google.guava, and its artifact ID isguava.
Guava provides two different "flavors": one for use on a (Java 8+) JRE and one
for use on Android or by any library that wants to be compatible with Android.
These flavors are specified in the Maven version field as either33.6.0-jreor33.6.0-android. For more about depending on Guava, seeusing Guava in your build.

To add a dependency on Guava using Maven, use the following:

<
dependency
>
 <
groupId
>com.google.guava</
groupId
>
 <
artifactId
>guava</
artifactId
>
 <
version
>33.6.0-jre</
version
>
 
<!--
 or, for Android: 
-->

 <
version
>33.6.0-android</
version
>
</
dependency
>

To add a dependency using Gradle:

dependencies
 {
 
//
 Pick one:

 
//
 1. Use Guava in your implementation only:

 implementation(
"
com.google.guava:guava:33.6.0-jre
"
)

 
//
 2. Use Guava types in your public API:

 api(
"
com.google.guava:guava:33.6.0-jre
"
)

 
//
 3. Android - Use Guava in your implementation only:

 implementation(
"
com.google.guava:guava:33.6.0-android
"
)

 
//
 4. Android - Use Guava types in your public API:

 api(
"
com.google.guava:guava:33.6.0-android
"
)
}

For more information on when to useapiand when to useimplementation,
consult theGradle documentation on API and implementation separation.

## Snapshots and Documentation

Snapshots of Guava built from themasterbranch are available through Maven
using version999.0.0-HEAD-jre-SNAPSHOT, or999.0.0-HEAD-android-SNAPSHOTfor the Android flavor.

Snapshot API Javadocas well asSnapshot API Diffsare also available.

Another easy way to get to the Javadoc is to openguava.dev/api. You can also jump right to a specific
class by appending the class name to guava.dev. For example,guava.dev/ImmutableList!

## Learn about Guava

* Our users' guide,Guava Explained
* A nice collectionof
other helpful links

## Links

* GitHub project
* Issue tracker: Report a defect or feature request
* StackOverflow: Ask "how-to" and "why-didn't-it-work" questions
* guava-announce: Announcements of releases and upcoming significant changes
* guava-discuss: For open-ended questions and discussion

## IMPORTANT WARNINGS

1. APIs marked with the@Betaannotation at the class or method level are
subject to change. They can be modified in any way, or even removed, at any
time. If your code is a library itself (i.e., it is used on the CLASSPATH of
users outside your own control), you should not use beta APIs unless yourepackagethem.If your code is a library, we strongly recommend using
theGuava Beta Checkerto ensure that you do not use any@BetaAPIs!
2. APIs without@Betawill remain binary-compatible for the indefinite
future. (Previously, we sometimes removed such APIs after a deprecation
period. The last release to remove non-@BetaAPIs was Guava 21.0.) Even@DeprecatedAPIs will remain (again, unless they are@Beta). We have no
plans to start removing things again, but officially, we're leaving our
options open in case of surprises (like, say, a serious security problem).
3. Guava has one dependency that is needed for linkage at runtime:com.google.guava:failureaccess:1.0.3. It also hassome annotation-only dependencies, which we discuss in more
detail at that link.
4. Serialized forms of ALL objects are subject to change unless noted
otherwise. Do not persist these and assume they can be read by a future
version of the library.
5. Our classes are not designed to protect against a malicious caller. You
should not use them for communication between trusted and untrusted code.
6. For the mainline flavor, we test the libraries using a range of OpenJDK
versions on Linux and Windows. Some features, especially incom.google.common.io, may not work correctly in non-Linux environments.
For the Android flavor, our unit tests also run on API level 24 (Nougat).