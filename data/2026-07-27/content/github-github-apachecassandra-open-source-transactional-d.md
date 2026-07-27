---
title: 'GitHub - apache/cassandra: Open source transactional distributed database. Linear scalability and proven fault-tolerance on commodity hardware or cloud infrastructure without compromising performance. · GitHub'
url: https://github.com/apache/cassandra
site_name: github
content_file: github-github-apachecassandra-open-source-transactional-d
fetched_at: '2026-07-27T12:06:34.120094'
original_url: https://github.com/apache/cassandra
author: apache
description: Open source transactional distributed database. Linear scalability and proven fault-tolerance on commodity hardware or cloud infrastructure without compromising performance. - apache/cassandra
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 apache

 

/

cassandra

Public

* NotificationsYou must be signed in to change notification settings
* Fork4k
* Star9.9k

 
 
 
trunk
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

32,081 Commits
32,081 Commits
.build
.build
 
 
.circleci
.circleci
 
 
.claude/
skills
.claude/
skills
 
 
.github
.github
 
 
.idea/
codeStyles
.idea/
codeStyles
 
 
.jenkins
.jenkins
 
 
bin
bin
 
 
ci
ci
 
 
conf
conf
 
 
debian
debian
 
 
doc
doc
 
 
examples
examples
 
 
ide
ide
 
 
lib
lib
 
 
modules
modules
 
 
pylib
pylib
 
 
redhat
redhat
 
 
src
src
 
 
test
test
 
 
tools
tools
 
 
.asf.yaml
.asf.yaml
 
 
.git-blame-ignore-revs
.git-blame-ignore-revs
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
.snyk
.snyk
 
 
AGENTS.md
AGENTS.md
 
 
CASSANDRA-14092.txt
CASSANDRA-14092.txt
 
 
CHANGES.txt
CHANGES.txt
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE.txt
LICENSE.txt
 
 
NEWS.txt
NEWS.txt
 
 
NOTICE.txt
NOTICE.txt
 
 
README.asc
README.asc
 
 
SECURITY.md
SECURITY.md
 
 
TESTING.md
TESTING.md
 
 
build-shaded-dtest-jar.sh
build-shaded-dtest-jar.sh
 
 
build.properties.default
build.properties.default
 
 
build.xml
build.xml
 
 
relocate-dependencies.pom
relocate-dependencies.pom
 
 
View all files

## Repository files navigation

    

    

## Apache Cassandra

Apache Cassandra is a highly-scalable partitioned row store. Rows are organized into tables with a required primary key.

Partitioningmeans that Cassandra can distribute your data across multiple machines in an application-transparent matter. Cassandra will automatically repartition as machines are added and removed from the cluster.

Row storemeans that like relational databases, Cassandra organizes data by rows and columns. The Cassandra Query Language (CQL) is a close relative of SQL.

For more information, seethe Apache Cassandra web site.

Issues should be reported onThe Cassandra Jira.

## Requirements

* Java: see supported versions in build.xml (search for property "java.supported").
* Python: forcqlsh, seebin/cqlsh(search for function "is_supported_version").

## Getting started

This short guide will walk you through getting a basic one node cluster up
and running, and demonstrate some simple reads and writes. For a more-complete guide, please see the Apache Cassandra website’sGetting Started Guide.

First, we’ll unpack our archive:

$ tar -zxvf apache-cassandra-$VERSION.tar.gz
$ cd apache-cassandra-$VERSION

After that we start the server. Running the startup script with the -f argument will cause
Cassandra to remain in the foreground and log to standard out; it can be stopped with ctrl-C.

$ bin/cassandra -f

Now let’s try to read and write some data using the Cassandra Query Language:

$ bin/cqlsh

The command line client is interactive so if everything worked you should
be sitting in front of a prompt:

Connected to Test Cluster at localhost:9160.
[cqlsh 6.3.0 | Cassandra 7.0-SNAPSHOT | CQL spec 3.4.8 | Native protocol v5]
Use HELP for help.
cqlsh>

As the banner says, you can use 'help;' or '?' to see what CQL has to
offer, and 'quit;' or 'exit;' when you’ve had enough fun. But lets try
something slightly more interesting:

cqlsh> CREATE KEYSPACE schema1
 WITH replication = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };
cqlsh> USE schema1;
cqlsh:Schema1> CREATE TABLE users (
 user_id varchar PRIMARY KEY,
 first varchar,
 last varchar,
 age int
 );
cqlsh:Schema1> INSERT INTO users (user_id, first, last, age)
 VALUES ('jsmith', 'John', 'Smith', 42);
cqlsh:Schema1> SELECT * FROM users;
 user_id | age | first | last
---------+-----+-------+-------
 jsmith | 42 | john | smith
cqlsh:Schema1>

If your session looks similar to what’s above, congrats, your single node
cluster is operational!

For more on what commands are supported by CQL, seethe CQL reference. A
reasonable way to think of it is as, "SQL minus joins and subqueries, plus collections."

Wondering where to go from here?

* Join us in #cassandra on theASF Slackand ask questions.
* Subscribe to the Users mailing list by sending a mail touser-subscribe@cassandra.apache.org.
* Subscribe to the Developer mailing list by sending a mail todev-subscribe@cassandra.apache.org.
* Visit thecommunity sectionof the Cassandra website for more information on getting involved.
* Visit thedevelopment sectionof the Cassandra website for more information on how to contribute.