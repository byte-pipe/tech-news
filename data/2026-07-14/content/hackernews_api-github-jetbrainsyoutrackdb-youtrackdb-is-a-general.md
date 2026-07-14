---
title: 'GitHub - JetBrains/youtrackdb: YouTrackDB is a general-use object-oriented graph database with storage format native to handle graph relations. YouTrackDB supports Gremlin queries and ACID transactions. · GitHub'
url: https://github.com/JetBrains/youtrackdb
site_name: hackernews_api
content_file: hackernews_api-github-jetbrainsyoutrackdb-youtrackdb-is-a-general
fetched_at: '2026-07-14T19:32:31.172420'
original_url: https://github.com/JetBrains/youtrackdb
author: gjvc
date: '2026-07-14'
description: YouTrackDB is a general-use object-oriented graph database with storage format native to handle graph relations. YouTrackDB supports Gremlin queries and ACID transactions. - JetBrains/youtrackdb
tags:
- hackernews
- trending
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 JetBrains

 

/

youtrackdb

Public

* NotificationsYou must be signed in to change notification settings
* Fork14
* Star347

 
 
 
 
develop
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

25,121 Commits
25,121 Commits
.claude
.claude
 
 
.githooks
.githooks
 
 
.github
.github
 
 
.mvn
.mvn
 
 
.pi
.pi
 
 
.reuse
.reuse
 
 
LICENSES
LICENSES
 
 
console
console
 
 
core
core
 
 
docker-tests
docker-tests
 
 
docs
docs
 
 
driver
driver
 
 
embedded
embedded
 
 
examples
examples
 
 
gremlin-annotations
gremlin-annotations
 
 
jmh-ldbc
jmh-ldbc
 
 
lucene
lucene
 
 
project-config
project-config
 
 
server
server
 
 
test-commons
test-commons
 
 
tests
tests
 
 
workflow-book-builder
workflow-book-builder
 
 
workflow-issues
workflow-issues
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
README.md
README.md
 
 
WORKFLOW_ISSUE_implementer_silent_exit.md
WORKFLOW_ISSUE_implementer_silent_exit.md
 
 
issue-perf-eager-pricing-load.md
issue-perf-eager-pricing-load.md
 
 
issue-perf-month-totals-aggregate.md
issue-perf-month-totals-aggregate.md
 
 
issue-perf-store-cache-full-rewrite.md
issue-perf-store-cache-full-rewrite.md
 
 
license.txt
license.txt
 
 
mvnw
mvnw
 
 
mvnw.cmd
mvnw.cmd
 
 
pom.xml
pom.xml
 
 
qodana.yaml
qodana.yaml
 
 
View all files

## Repository files navigation

## YouTrackDB

 

Issue tracker|Getting started

### Join our Zulip community!

If you are interested in YouTrackDB, consider joining ourZulipcommunity.
Tell us about exciting applications you are building, ask for help, or just chat with friends 😃

### What is YouTrackDB?

YouTrackDB is ageneral useobject-oriented graph database.
YouTrackDB is being supported and developed by JetBrains and is used internally in production.

YouTrackDB's key features are:

1. Fast data processing: Links traversal is processed with O(1) complexity. There are no
expensive run-time JOINs.
2. Object-oriented API: This API implements rich graph and
object-oriented data models. Fundamental concepts ofinheritance and polymorphismare implemented on the database
level.
3. Snapshot isolation by default: All transactions run under snapshot isolation. Each
transaction sees a stable snapshot of the database as of its start time, eliminating dirty
reads, non-repeatable reads, and phantom reads.
4. Implementation of TinkerPop API andGremlin query language:
You can use both Gremlin query language for your queries and TinkerPop API out of the box.
Support ofGQLwith seamless integration withGremlinisin progress.
For maximum query performance, we suggest usingYQLfor initial
data prefetching.
5. YQL(YouTrackDB Query Language): A SQL-based query language
with extensions for graph functionality. YQL uses intuitive dot notation for link traversal
instead of JOINs, supports the powerfulMATCH statementfor graph
pattern matching, and includes automatic index usage for query optimization.
6. Scalable development workflow: YouTrackDB works in schema-less, schema-mixed, and schema-full
modes.
7. Strong security: A strong security profiling system based on user, role,
and predicatesecurity policies.
8. Encryption of data at rest: Optionally encrypts all data stored on disk.

### Easy to install and use

YouTrackDB can run on any platform without configuration and installation.

If you want to experiment with YouTrackDB, please check out our REPLconsole.

docker run -it youtrackdb/youtrackdb-console

To install YouTrackDB as an embedded database, add the following dependency to your Maven project:

<
dependency
>
 <
groupId
>io.youtrackdb</
groupId
>
 <
artifactId
>youtrackdb-embedded</
artifactId
>
 <
version
>0.5.0-SNAPSHOT</
version
>
</
dependency
>

Theyoutrackdb-embeddedartifact is a shaded uber-jar that relocates all third-party
dependencies (Guava, Jackson, Groovy, etc.) undercom.jetbrains.youtrackdb.shade,
so they won't conflict with versions used by your application.

You also need to add a YTDB snapshot repository to your Maven pom.xml file:

<
repositories
>
 <
repository
>
 <
name
>Central Portal Snapshots</
name
>
 <
id
>central-portal-snapshots</
id
>
 <
url
>https://central.sonatype.com/repository/maven-snapshots/</
url
>
 <
releases
>
 <
enabled
>false</
enabled
>
 </
releases
>
 <
snapshots
>
 <
enabled
>true</
enabled
>
 </
snapshots
>
 </
repository
>
</
repositories
>

or in case of Gradle:

dependencies {
 implementation 'io.youtrackdb:youtrackdb-embedded:0.5.0-SNAPSHOT'
}

and

repositories {
 maven {
 url = uri("https://central.sonatype.com/repository/maven-snapshots/")
 mavenContent {
 snapshotsOnly()
 }
 }
}

If you want to work with YouTrackDB server, you can start it using the Docker image:

docker run -p 8182:8182 \
 -v 
$(
pwd
)
/secrets:/opt/ytdb-server/secrets \
 -v 
$(
pwd
)
/databases:/opt/ytdb-server/databases \
 -v 
$(
pwd
)
/conf:/opt/ytdb-server/conf \
 -v 
$(
pwd
)
/log:/opt/ytdb-server/log \
 youtrackdb/youtrackdb-server

and provide root password for the database in thesecrets/root_passwordfile.

YouTrackDB requires at least JDK 21.

To learn how to use YouTrackDB, see theGetting Startedguide.

For more examples covering both server and embedded deployments, check out theexamplesproject.

### Contributing

YouTrackDB runs every non-trivial change through a structured development
workflow: research, design, plan review, track-by-track implementation, and
review. New contributors can learn to run it end to end in the development
workflow book, starting atChapter 1 — The workflow at a glance.

## About

YouTrackDB is a general-use object-oriented graph database with storage format native to handle graph relations. YouTrackDB supports Gremlin queries and ACID transactions.

youtrackdb.io

### Topics

 nosql

 dbms

 nosql-databases

 graph-database

 gremlin

 acid

 nosql-data-storage

 graph-databases

 nosql-database

 gremlin-server

 object-database

 dbms-project

 object-oriented-database

 gremlin-api

 graphdatabase

 youtrackdb

### Resources

 Readme

 

### License

 Apache-2.0 license
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

347

 stars
 

### Watchers

5

 watching
 

### Forks

14

 forks
 

 Report repository

 

## Releases

7

tags

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Java96.0%
* Python3.0%
* Shell0.5%
* TypeScript0.2%
* PLpgSQL0.2%
* Gherkin0.1%