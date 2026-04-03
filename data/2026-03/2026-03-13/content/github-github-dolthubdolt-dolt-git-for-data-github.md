---
title: 'GitHub - dolthub/dolt: Dolt – Git for Data · GitHub'
url: https://github.com/dolthub/dolt
site_name: github
content_file: github-github-dolthubdolt-dolt-git-for-data-github
fetched_at: '2026-03-13T11:14:29.363931'
original_url: https://github.com/dolthub/dolt
author: dolthub
description: Dolt – Git for Data. Contribute to dolthub/dolt development by creating an account on GitHub.
---

dolthub

 

/

dolt

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork664
* Star20.8k

 
 
 
 
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

29,986 Commits
29,986 Commits
.github
.github
 
 
docker
docker
 
 
go
go
 
 
images
images
 
 
integration-tests
integration-tests
 
 
proto
proto
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
CODEOWNERS
CODEOWNERS
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
dolt.plugin.zsh
dolt.plugin.zsh
 
 
View all files

## Repository files navigation

# Dolt is Git for Data!

Dolt is a SQL database that you can fork, clone, branch, merge, push
and pull just like a Git repository.

Connect to Dolt just like any MySQL database to read or modify schema
and data. Version control functionality is exposed in SQL via system
tables, functions, and procedures.

Or, use the Git-like command line interface to import CSV files, commit
your changes, push them to a remote, or merge your teammate's changes.
All the commands you know for Git work exactly the same for Dolt.

Git versions files. Dolt versions tables. It's like Git and MySQL had a
baby.

We also builtDoltHub, a place to share
Dolt databases. We host public data for free. If you want to host
your own version of DoltHub, we haveDoltLab.
If you want us to run a Dolt server for you, we haveHosted Dolt.

Prefer Postgres instead of MySQL? TryDoltgres, now
in its Beta release.

Join us on Discordto say hi and
ask questions, orcheck out our roadmapto see what we're building next.

# Video Introduction

# What's it for?

Lots of things! Dolt is a generally useful tool with countless
applications. But if you want some ideas,here's how people are using
it so far.

Dolt can beset up as a replica of your existing MySQLdatabase using standard MySQL binlog replication. Every write becomes
a Dolt commit. This is a great way to get the version control benefits
of Dolt and keep an existing MySQL database.

# Dolt CLI

ThedoltCLI has the same commands asgit, with some extras.

$ dolt
Valid commands for dolt are
 init - Create an empty Dolt data repository.
 status - Show the working tree status.
 add - Add table changes to the list of staged table changes.
 diff - Diff a table.
 reset - Remove table changes from the list of staged table changes.
 clean - Remove untracked tables from working set.
 commit - Record changes to the repository.
 sql - Run a SQL query against tables in repository.
 sql-server - Start a MySQL-compatible server.
 log - Show commit logs.
 branch - Create, list, edit, delete branches.
 checkout - Checkout a branch or overwrite a table from HEAD.
 merge - Merge a branch.
 conflicts - Commands for viewing and resolving merge conflicts.
 cherry-pick - Apply the changes introduced by an existing commit.
 revert - Undo the changes introduced in a commit.
 clone - Clone from a remote data repository.
 fetch - Update the database from a remote data repository.
 pull - Fetch from a dolt remote data repository and merge.
 push - Push to a dolt remote.
 config - Dolt configuration.
 remote - Manage set of tracked repositories.
 backup - Manage a set of server backups.
 login - Login to a dolt remote host.
 creds - Commands for managing credentials.
 ls - List tables in the working set.
 schema - Commands for showing and importing table schemas.
 table - Commands for copying, renaming, deleting, and exporting tables.
 tag - Create, list, delete tags.
 blame - Show what revision and author last modified each row of a table.
 constraints - Commands for handling constraints.
 migrate - Executes a database migration to use the latest Dolt data format.
 read-tables - Fetch table(s) at a specific commit into a new dolt repo
 gc - Cleans up unreferenced data from the repository.
 filter-branch - Edits the commit history using the provided query.
 merge-base - Find the common ancestor of two commits.
 version - Displays the current Dolt cli version.
 dump - Export all tables in the working set into a file.

# Installation

Dolt is a single ~103 megabyte program.

dolt $ du -h /Users/timsehn/go/bin/dolt
103M	/Users/timsehn/go/bin/dolt

It's really easy to install. Download it and put it on yourPATH.
We have a bunch of ways to make this even easier for most platforms.

## From Latest Release

To install on Linux or Mac based systems run this command in your
terminal:

sudo bash -c 'curl -L https://github.com/dolthub/dolt/releases/latest/download/install.sh | bash'

This will download the latestdoltrelease and put it in/usr/local/bin/, which is probably on your$PATH.

The install script needs sudo in order to putdoltin/usr/local/bin. If you don't have root
privileges or aren't comfortable running a script with them, you can download the dolt binary
for your platform fromthe latest release, unzip it,
and put the binary somewhere on your$PATH.

### Linux

#### Arch Linux

Dolt is packaged in the official repositories for Arch Linux.

pacman -S dolt

### Mac

#### Homebrew

Dolt is on Homebrew, updated every release.

brew install dolt

#### MacPorts

On macOS, Dolt can also be installed via acommunity-managed portviaMacPorts:

sudo port install dolt

### Windows

Download the latest Microsoft Installer (.msifile) inreleasesand run
it.

For information on running on Windows, seehere.

#### Chocolatey

You can installdoltusingChocolatey:

choco install dolt

#### Docker

There are following official Docker images for Dolt:

* dolthub/doltfor running Dolt
as CLI tool.
* dolthub/dolt-sql-serverfor running Dolt in server mode.

## From Source

Make sure you have Go installed, and thatgois in your path. Dolt has a dependency oncgo, so you will need a working C compiler and toolchain as well.

Clone this repository and cd into thegodirectory. Then run:

go install ./cmd/dolt

The output will be in$GOPATH/bin, which defaults to~/go/bin. To test your build, try:

~/go/bin/dolt version

# Configuration

Verify that your installation has succeeded by runningdoltin your
terminal.

$ dolt
Valid commands for dolt are
[...]

Configuredoltwith your user name and email, which you'll need to
create commits. The commands work exactly the same as git.

$ dolt config --global --add user.email YOU@DOMAIN.COM
$ dolt config --global --add user.name "YOUR NAME"

# Getting started

## Navigate to the directory where you would like your data stored

Dolt needs a place to store your databases. I'm going to put my databases in~/dolt.

% 
cd
 
~

% mkdir dolt
% 
cd
 dolt

Any databases you create will be stored in this directory. So, for this example, a directory namedgetting_startedwill be created here once you runcreate database getting_started. Navigating to~/dolt/getting_startedwill allow you to access this database using the Dolt command line.

NOTE: For this example, thegetting_starteddirectory will be created after you runcreate database getting_started;in a SQL shell in theCreate a schema section. Don't do anything except make the directory and navigate to it just yet.

## Start a MySQL-compatible database server

Dolt ships with a MySQL compatible database server built in. To start it you use the commanddolt sql-server. Running this command starts the server on port 3306.

dolt sql-server
Starting server with Config HP=
"
localhost:3306
"
|
T=
"
28800000
"
|
R=
"
false
"
|
L=
"
info
"

Your terminal will just hang there. This means the server is running. Any errors will be printed in this terminal. Just leave it there and open a new terminal.

## Connect with a MySQL client (up to version 8.4)

In the new terminal, we will now connect to the running database server using a client. Dolt also ships with a MySQL compatible client.

% dolt -u root -p 
"
"
 sql

#
 Welcome to the Dolt MySQL client.

#
 Statements must be terminated with ';'.

#
 "exit" or "quit" (or Ctrl-D) to exit.

mysql
>

In the other terminal where you randolt sql-server, you'll see the following log line.

2022-06-06T13:14:32-07:00 INFO [conn 1] NewConnection {DisableClientMultiStatements=false}

You are connected!

While we're here let's grab a copy of MySQL so we can connect with that client. Head over to theMySQL Getting Starteddocumentation and install MySQL on your machine. I usedHomebrewto install MySQL on my Mac:brew install mysql@8.4. Alternatively, you can install only the client component by runningbrew install mysql-client@8.4.

NOTE: Make sure you install a MySQL 8.4 release. MySQL 8.4 is the current Long Term Support (LTS) release, meaning this is the stable and supported version of MySQL. MySQL 9.0 is also available, but is an "innovation" release, meaning it has more recent changes and features, but may not be as stable as the LTS release. The 9.0 release changes authentication support and isn't able to connect to a Dolt SQL server by default. You can install MySQL 8.4 with Homebrew by runningbrew install mysql@8.4. If you do want to use MySQL-9.0, readour post on how to configure Dolt forcaching_sha2_passwordauthentication.

MySQL comes with a MySQL server calledmysqldand a MySQL client calledmysql. You're only interested in the client. After following the instructions from MySQL's documentation, make sure you have a copy of themysqlclient on your path:

% mysql --version
mysql Ver 8.0.29 
for
 macos12.2 on x86_64 (Homebrew)

Now, to connect themysqlclient to Dolt, you are going to force the MySQL client through the TCP interface by passing in a host and port. The default is the socket interface which Dolt supports, but is only available onlocalhost. So, it's better to show off the TCP interface. The MySQL client also requires you specify a user, in this caseroot.

% mysql --host 127.0.0.1 --port 3306 -uroot
Welcome to the MySQL monitor. Commands end with 
;
 or 
\g
.
Your MySQL connection id is 2
Server version: 5.7.9-Vitess 

Copyright (c) 2000, 2022, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 
'
help;
'
 or 
'
\h
'
 
for
 help. Type 
'
\c
'
 to clear the current input statement.

mysql
>

Again, to ensure the client actually connected, you should see the following in thedolt sql-serverterminal

2022-06-06T13:26:55-07:00 INFO [conn 2] NewConnection {DisableClientMultiStatements=false}

As you can see, Dolt supports any MySQL-compatible client. Dolt ships with a client but you can use any MySQL client, like the one that comes with MySQL.

## Create a schema

Now we're actually ready to do something interesting. I'll stay in themysqlclient and execute the following SQL statements to create a database calledgetting_started. Thegetting_starteddatabase will have three tables:employees,teams, andemployees_teams.

mysql> create database getting_started;
Query OK, 1 row affected (0.04 sec)

mysql> use getting_started;
Database changed
mysql> create table employees (
 id int, 
 last_name varchar(255), 
 first_name varchar(255), 
 primary key(id));
Query OK, 0 rows affected (0.01 sec)

mysql> create table teams (
 id int, 
 team_name varchar(255), 
 primary key(id)); 
Query OK, 0 rows affected (0.00 sec)

mysql> create table employees_teams(
 team_id int, 
 employee_id int, 
 primary key(team_id, employee_id), 
 foreign key (team_id) references teams(id), 
 foreign key (employee_id) references employees(id));
Query OK, 0 rows affected (0.01 sec)

mysql> show tables;
+---------------------------+
| Tables_in_getting_started |
+---------------------------+
| employees |
| employees_teams |
| teams |
+---------------------------+
3 rows in set (0.00 sec)

Dolt supports foreign keys, secondary indexes, triggers, check constraints, and stored procedures. It's a modern, feature-rich SQL database.

## Make a Dolt commit

It's time to use your first Dolt feature. We're going to make a Doltcommit. A Dolt commit allows you to time travel and see lineage. Make a Dolt commit whenever you want to restore or compare to this point in time.

Dolt exposes version control functionality through a Git-style interface. On the command line, Dolt commands map exactly to their Git equivalent with the targets being tables instead of files. In SQL, Dolt exposes version control read operations assystem tablesand version control write operations asstored procedures.

The naming of the system tables and stored procedures follows thedolt_<command>pattern. Sodolt addon the CLI becomesdolt_addas a stored procedure. Passing options also follows the command line model. For instance, to specify tables to add, send the table names in as options to thedolt_addprocedure. For named arguments like sending a message into thedolt_commitcommand use two arguments in sequence like('-m', 'This is a message'). If you know Git, the version control procedures and system tables should feel familiar.

So, we add and commit our new schema like so.

mysql> call dolt_add('teams', 'employees', 'employees_teams');
+--------+
| status |
+--------+
| 0 |
+--------+
1 row in set (0.03 sec)

mysql> call dolt_commit('-m', 'Created initial schema');
+----------------------------------+
| hash |
+----------------------------------+
| ne182jemgrlm8jnjmoubfqsstlfi1s98 |
+----------------------------------+
1 row in set (0.02 sec)

mysql> select * from dolt_log;
+----------------------------------+-----------+-----------------+-------------------------+----------------------------+
| commit_hash | committer | email | date | message |
+----------------------------------+-----------+-----------------+-------------------------+----------------------------+
| ne182jemgrlm8jnjmoubfqsstlfi1s98 | Tim Sehn | tim@dolthub.com | 2022-06-07 16:35:49.277 | Created initial schema |
| vluuhvd0bn59598utedt77ed9q5okbcb | Tim Sehn | tim@dolthub.com | 2022-06-07 16:33:59.531 | Initialize data repository |
+----------------------------------+-----------+-----------------+-------------------------+----------------------------+
2 rows in set (0.01 sec)

There you have it. Your schema is created and you have a Dolt commit tracking the creation, as seen in thedolt_logsystem table.

Note, a Dolt commit is different than a standard SQL transactionCOMMIT. In this case, I am running the database withAUTOCOMMITon, so each SQL statement is automatically generating a transactionCOMMIT. If you want system to generate a Dolt commit for every transaction use the system variable,@@dolt_transaction_commit.

## Insert some data

Now, I'm going to populate the database with a few employees here at DoltHub. Then, I'll assign the employees to two teams: engineering and sales. The CEO wears many hats at a start up so he'll be assigned to multiple teams.

mysql> insert into employees values 
 (0, 'Sehn', 'Tim'), 
 (1, 'Hendriks', 'Brian'), 
 (2, 'Son','Aaron'), 
 (3, 'Fitzgerald', 'Brian');
Query OK, 4 rows affected (0.01 sec)

mysql> select * from employees where first_name='Brian';
+------+------------+------------+
| id | last_name | first_name |
+------+------------+------------+
| 1 | Hendriks | Brian |
| 3 | Fitzgerald | Brian |
+------+------------+------------+
2 rows in set (0.00 sec)

mysql> insert into teams values 
 (0, 'Engineering'), 
 (1, 'Sales');
Query OK, 2 rows affected (0.00 sec)

mysql> insert into employees_teams values 
 (0,0), 
 (1,0), 
 (2,0), 
 (0,1), 
 (3,1);
ERROR 1452 (HY000): cannot add or update a child row - Foreign key violation on fk: `rv9ek7ft`, table: `employees_teams`, referenced table: `teams`, key: `[2]`

Oops, I violated a constraint. It looks like I created the table with teams before employees. You should always specify your columns when you insert, not rely on natural ordering. Serves me right! Dolt comes with the full power of a modern SQL relational database to ensure data integrity.

mysql> insert into employees_teams(employee_id, team_id) values 
 (0,0), 
 (1,0), 
 (2,0), 
 (0,1), 
 (3,1);
Query OK, 5 rows affected (0.01 sec)

mysql> select first_name, last_name, team_name from employees 
 join employees_teams on (employees.id=employees_teams.employee_id) 
 join teams on (teams.id=employees_teams.team_id) 
 where team_name='Engineering';
+------------+-----------+-------------+
| first_name | last_name | team_name |
+------------+-----------+-------------+
| Tim | Sehn | Engineering |
| Brian | Hendriks | Engineering |
| Aaron | Son | Engineering |
+------------+-----------+-------------+
3 rows in set (0.00 sec)

Looks like everything is inserted and correct. I was able to list the members of the engineering team using that three tableJOIN. Dolt supports up to twelve tableJOINs. Again, Dolt is a modern SQL relational database paired with Git-style version control.

## Examine the diff

Now, what if you want to see what changed in your working set before you make a commit? You use thedolt_statusanddolt_diff_<tablename>system tables.

mysql> select * from dolt_status;
+-----------------+--------+----------+
| table_name | staged | status |
+-----------------+--------+----------+
| teams | 0 | modified |
| employees | 0 | modified |
| employees_teams | 0 | modified |
+-----------------+--------+----------+
3 rows in set (0.01 sec)

mysql> select * from dolt_diff_employees;
+--------------+---------------+-------+-----------+----------------+----------------+-----------------+---------+----------------------------------+-------------------------+-----------+
| to_last_name | to_first_name | to_id | to_commit | to_commit_date | from_last_name | from_first_name | from_id | from_commit | from_commit_date | diff_type |
+--------------+---------------+-------+-----------+----------------+----------------+-----------------+---------+----------------------------------+-------------------------+-----------+
| Sehn | Tim | 0 | WORKING | NULL | NULL | NULL | NULL | ne182jemgrlm8jnjmoubfqsstlfi1s98 | 2022-06-07 16:35:49.277 | added |
| Hendriks | Brian | 1 | WORKING | NULL | NULL | NULL | NULL | ne182jemgrlm8jnjmoubfqsstlfi1s98 | 2022-06-07 16:35:49.277 | added |
| Son | Aaron | 2 | WORKING | NULL | NULL | NULL | NULL | ne182jemgrlm8jnjmoubfqsstlfi1s98 | 2022-06-07 16:35:49.277 | added |
| Fitzgerald | Brian | 3 | WORKING | NULL | NULL | NULL | NULL | ne182jemgrlm8jnjmoubfqsstlfi1s98 | 2022-06-07 16:35:49.277 | added |
+--------------+---------------+-------+-----------+----------------+----------------+-----------------+---------+----------------------------------+-------------------------+-----------+
4 rows in set (0.00 sec)

As you can see from the diff I've added the correct values to theemployeestable. The values were previouslyNULLand now they are populated.

Let's finish off with another Dolt commit this time adding all effected tables using-am.

mysql> call dolt_commit('-am', 'Populated tables with data');
+----------------------------------+
| hash |
+----------------------------------+
| 13qfqa5rojq18j84d1n2htjkm6fletg4 |
+----------------------------------+
1 row in set (0.02 sec)

You can inspect the log usingdolt_logand see which tables changed in each commit using an unscopeddolt_diff. Unscopeddolt_difftells you whether schema, data, or both changed in that particular commit for the table.

mysql> select * from dolt_log;
+----------------------------------+-----------+-----------------+-------------------------+----------------------------+
| commit_hash | committer | email | date | message |
+----------------------------------+-----------+-----------------+-------------------------+----------------------------+
| 13qfqa5rojq18j84d1n2htjkm6fletg4 | Tim Sehn | tim@dolthub.com | 2022-06-07 16:39:32.066 | Populated tables with data |
| ne182jemgrlm8jnjmoubfqsstlfi1s98 | Tim Sehn | tim@dolthub.com | 2022-06-07 16:35:49.277 | Created initial schema |
| vluuhvd0bn59598utedt77ed9q5okbcb | Tim Sehn | tim@dolthub.com | 2022-06-07 16:33:59.531 | Initialize data repository |
+----------------------------------+-----------+-----------------+-------------------------+----------------------------+
3 rows in set (0.00 sec)

mysql> select * from dolt_diff;
+----------------------------------+-----------------+-----------+-----------------+-------------------------+----------------------------+-------------+---------------+
| commit_hash | table_name | committer | email | date | message | data_change | schema_change |
+----------------------------------+-----------------+-----------+-----------------+-------------------------+----------------------------+-------------+---------------+
| 13qfqa5rojq18j84d1n2htjkm6fletg4 | teams | Tim Sehn | tim@dolthub.com | 2022-06-07 16:39:32.066 | Populated tables with data | 1 | 0 |
| 13qfqa5rojq18j84d1n2htjkm6fletg4 | employees | Tim Sehn | tim@dolthub.com | 2022-06-07 16:39:32.066 | Populated tables with data | 1 | 0 |
| 13qfqa5rojq18j84d1n2htjkm6fletg4 | employees_teams | Tim Sehn | tim@dolthub.com | 2022-06-07 16:39:32.066 | Populated tables with data | 1 | 0 |
| ne182jemgrlm8jnjmoubfqsstlfi1s98 | employees | Tim Sehn | tim@dolthub.com | 2022-06-07 16:35:49.277 | Created initial schema | 0 | 1 |
| ne182jemgrlm8jnjmoubfqsstlfi1s98 | employees_teams | Tim Sehn | tim@dolthub.com | 2022-06-07 16:35:49.277 | Created initial schema | 0 | 1 |
| ne182jemgrlm8jnjmoubfqsstlfi1s98 | teams | Tim Sehn | tim@dolthub.com | 2022-06-07 16:35:49.277 | Created initial schema | 0 | 1 |
+----------------------------------+-----------------+-----------+-----------------+-------------------------+----------------------------+-------------+---------------+
6 rows in set (0.00 sec)

## Oh no! I made a mistake.

Dolt supports undoing changes viacall dolt_reset(). Let's imagine I accidentally drop a table.

mysql> drop table employees_teams;
Query OK, 0 rows affected (0.01 sec)

mysql> show tables;
+---------------------------+
| Tables_in_getting_started |
+---------------------------+
| employees |
| teams |
+---------------------------+
2 rows in set (0.00 sec)

In a traditional database, this could be disastrous. In Dolt, you're one command away from getting your table back.

mysql> call dolt_reset('--hard');
+--------+
| status |
+--------+
| 0 |
+--------+
1 row in set (0.01 sec)

mysql> show tables;
+---------------------------+
| Tables_in_getting_started |
+---------------------------+
| employees |
| employees_teams |
| teams |
+---------------------------+
3 rows in set (0.01 sec)

Dolt makes operating databases less error prone. You can always back out changes you have in progress or rewind to a known good state. You also have the ability to undo specific commits usingdolt_revert(). Even if you accidentally rundrop databaseon the wrong database, Dolt lets you undo that by calling thedolt_undrop()stored procedure.

## See the data in a SQL Workbench

Hate the command line? Let's useTableplusto make some modifications. Tableplus is a free SQL Workbench. Follow the installation instructions from their website.

Now, to connect you must select MySQL as the connection type. Then enter a name for your connection,getting_startedas your database, androotas your user.

Click connect and you'll be presented with a familiar database workbench GUI.

## Make changes on a branch

To make changes on a branch, I use thedolt_checkout()stored procedure. Using the-boption creates a branch, just like in Git.

Tableplus gives me the ability to enter a multiple line SQL script on the SQL tab. I entered the following SQL to checkout a branch, update, insert, delete, and finally Dolt commit my changes.

call dolt_checkout(
'
-b
'
,
'
modifications
'
);

update
 employees 
SET
 first_name
=
'
Timothy
'
 
where
 first_name
=
'
Tim
'
;

insert INTO
 employees (id, first_name, last_name) 
values
 (
4
,
'
Daylon
'
, 
'
Wilkins
'
);

insert into
 employees_teams(team_id, employee_id) 
values
 (
0
,
4
);

delete
 
from
 employees_teams 
where
 employee_id
=
0
 
and
 team_id
=
1
;
call dolt_commit(
'
-am
'
, 
'
Modifications on a branch
'
);

Here's the result in Tableplus.

Back in my terminal, I cannot see the table modifications made in Tableplus because they happened on a different branch than the one I have checked out in my session.

mysql> select * from dolt_branches;
+---------------+----------------------------------+------------------+------------------------+-------------------------+----------------------------+
| name | hash | latest_committer | latest_committer_email | latest_commit_date | latest_commit_message |
+---------------+----------------------------------+------------------+------------------------+-------------------------+----------------------------+
| main | 13qfqa5rojq18j84d1n2htjkm6fletg4 | Tim Sehn | tim@dolthub.com | 2022-06-07 16:39:32.066 | Populated tables with data |
| modifications | uhkv57j4bp2v16vcnmev9lshgkqq8ppb | Tim Sehn | tim@dolthub.com | 2022-06-07 16:41:49.847 | Modifications on a branch |
+---------------+----------------------------------+------------------+------------------------+-------------------------+----------------------------+
2 rows in set (0.00 sec)

mysql> select active_branch();
+-----------------+
| active_branch() |
+-----------------+
| main |
+-----------------+
1 row in set (0.00 sec)

mysql> select * from employees;
+------+------------+------------+
| id | last_name | first_name |
+------+------------+------------+
| 0 | Sehn | Tim |
| 1 | Hendriks | Brian |
| 2 | Son | Aaron |
| 3 | Fitzgerald | Brian |
+------+------------+------------+
4 rows in set (0.00 sec)

I can query the branch no matter what I have checked out using SQLas ofsyntax.

mysql> select * from employees as of 'modifications';
+------+------------+------------+
| id | last_name | first_name |
+------+------------+------------+
| 0 | Sehn | Timothy |
| 1 | Hendriks | Brian |
| 2 | Son | Aaron |
| 3 | Fitzgerald | Brian |
| 4 | Wilkins | Daylon |
+------+------------+------------+
5 rows in set (0.01 sec)

If I'd like to see the diff between the two branches, I can use thedolt_diff()table function. It takes two branches and the table name as arguments.

mysql> select * from dolt_diff('main', 'modifications', 'employees');
+--------------+---------------+-------+---------------+-------------------------+----------------+-----------------+---------+-------------+-------------------------+-----------+
| to_last_name | to_first_name | to_id | to_commit | to_commit_date | from_last_name | from_first_name | from_id | from_commit | from_commit_date | diff_type |
+--------------+---------------+-------+---------------+-------------------------+----------------+-----------------+---------+-------------+-------------------------+-----------+
| Sehn | Timothy | 0 | modifications | 2022-06-07 16:41:49.847 | Sehn | Tim | 0 | main | 2022-06-07 16:39:32.066 | modified |
| Wilkins | Daylon | 4 | modifications | 2022-06-07 16:41:49.847 | NULL | NULL | NULL | main | 2022-06-07 16:39:32.066 | added |
+--------------+---------------+-------+---------------+-------------------------+----------------+-----------------+---------+-------------+-------------------------+-----------+
2 rows in set (0.00 sec)

As you can see, you have the full power of Git-style branches and diffs in a SQL database with Dolt.

## Make a schema change on another branch

I can also make schema changes on branches for isolated testing of new schema. I'm going to add astart_datecolumn on a new branch and populate it.

mysql> call dolt_checkout('-b', 'schema_changes');
+--------+
| status |
+--------+
| 0 |
+--------+
1 row in set (0.01 sec)

mysql> alter table employees add column start_date date;
Query OK, 0 rows affected (0.02 sec)

mysql> update employees set start_date='2018-09-08';
Query OK, 4 rows affected (0.01 sec)
Rows matched: 4 Changed: 4 Warnings: 0

mysql> update employees set start_date='2021-04-19' where last_name='Fitzgerald';
Query OK, 1 row affected (0.01 sec)
Rows matched: 1 Changed: 1 Warnings: 0

mysql> select * from employees;
+------+------------+------------+------------+
| id | last_name | first_name | start_date |
+------+------------+------------+------------+
| 0 | Sehn | Tim | 2018-09-08 |
| 1 | Hendriks | Brian | 2018-09-08 |
| 2 | Son | Aaron | 2018-09-08 |
| 3 | Fitzgerald | Brian | 2021-04-19 |
+------+------------+------------+------------+
4 rows in set (0.00 sec)

mysql> call dolt_commit('-am', 'Added start_date column to employees');
+----------------------------------+
| hash |
+----------------------------------+
| pg3nfi0j1dpc5pf1rfgckpmlteaufdrt |
+----------------------------------+
1 row in set (0.01 sec)

Changing schema on a branch gives you a new method for doing isolated integration testing of new schema changes.

## Merge it all together

Let's assume all the testing of the new schema on theschema_changesbranch and data on themodificationsbranch completed flawlessly. It's time to merge all our edits together ontomain. This is done using thedolt_mergestored procedure.

mysql> call dolt_checkout('main');
+--------+
| status |
+--------+
| 0 |
+--------+
1 row in set (0.01 sec)

mysql> select * from dolt_status;
Empty set (0.00 sec)

mysql> call dolt_merge('schema_changes');
+--------------+
| no_conflicts |
+--------------+
| 1 |
+--------------+
1 row in set (0.01 sec)

mysql> select * from employees;
+------+------------+------------+------------+
| id | last_name | first_name | start_date |
+------+------------+------------+------------+
| 0 | Sehn | Tim | 2018-09-08 |
| 1 | Hendriks | Brian | 2018-09-08 |
| 2 | Son | Aaron | 2018-09-08 |
| 3 | Fitzgerald | Brian | 2021-04-19 |
+------+------------+------------+------------+
4 rows in set (0.00 sec)

Schema change successful. We now have start dates. Data changes are next.

mysql> call dolt_merge('modifications');
+--------------+
| no_conflicts |
+--------------+
| 1 |
+--------------+
1 row in set (0.02 sec)

mysql> select * from employees;
+------+------------+------------+------------+
| id | last_name | first_name | start_date |
+------+------------+------------+------------+
| 0 | Sehn | Timothy | 2018-09-08 |
| 1 | Hendriks | Brian | 2018-09-08 |
| 2 | Son | Aaron | 2018-09-08 |
| 3 | Fitzgerald | Brian | 2021-04-19 |
| 4 | Wilkins | Daylon | NULL |
+------+------------+------------+------------+
5 rows in set (0.00 sec)

Data changes successful as well. As you can see, I am now "Timothy" instead of "Tim", Daylon is added, and we all have start dates except for Daylon who was added on a different branch.

mysql> select first_name, last_name, team_name from employees 
 join employees_teams on (employees.id=employees_teams.employee_id) 
 join teams on (teams.id=employees_teams.team_id) 
 where team_name='Sales';
+------------+------------+-----------+
| first_name | last_name | team_name |
+------------+------------+-----------+
| Brian | Fitzgerald | Sales |
+------------+------------+-----------+
1 row in set (0.01 sec)

I'm also gone from the Sales Team. Engineering is life.

I have to commit all my changes because the last merge was not a fast-forward merge.

mysql> call dolt_commit('-m', 'Merged all branches');
+----------------------------------+
| hash |
+----------------------------------+
| vn9b0qcematsj2f6ka0hfoflhr5s6p0b |
+----------------------------------+
1 row in set (0.01 sec)

mysql> select * from dolt_log;
+----------------------------------+-----------+-----------------+-------------------------+--------------------------------------+
| commit_hash | committer | email | date | message |
+----------------------------------+-----------+-----------------+-------------------------+--------------------------------------+
| vn9b0qcematsj2f6ka0hfoflhr5s6p0b | Tim Sehn | tim@dolthub.com | 2022-06-07 17:10:02.07 | Merged all branches |
| pg3nfi0j1dpc5pf1rfgckpmlteaufdrt | Tim Sehn | tim@dolthub.com | 2022-06-07 16:44:37.513 | Added start_date column to employees |
| uhkv57j4bp2v16vcnmev9lshgkqq8ppb | Tim Sehn | tim@dolthub.com | 2022-06-07 16:41:49.847 | Modifications on a branch |
| 13qfqa5rojq18j84d1n2htjkm6fletg4 | Tim Sehn | tim@dolthub.com | 2022-06-07 16:39:32.066 | Populated tables with data |
| ne182jemgrlm8jnjmoubfqsstlfi1s98 | Tim Sehn | tim@dolthub.com | 2022-06-07 16:35:49.277 | Created initial schema |
| vluuhvd0bn59598utedt77ed9q5okbcb | Tim Sehn | tim@dolthub.com | 2022-06-07 16:33:59.531 | Initialize data repository |
+----------------------------------+-----------+-----------------+-------------------------+--------------------------------------+
6 rows in set (0.00 sec)

Now, we have a database with all the schema and data changes merged and ready for use.

## Audit Cell Lineage

Which commit changed my first name? With Dolt you have lineage for every cell in your database. Let's use thedolt_history_<tablename>anddolt_diff_<tablename>to explore the lineage features in Dolt.

dolt_history_<tablename>shows you the state of the row at every commit.

mysql> select * from dolt_history_employees where id=0 order by commit_date;
+------+-----------+------------+------------+----------------------------------+-----------+-------------------------+
| id | last_name | first_name | start_date | commit_hash | committer | commit_date |
+------+-----------+------------+------------+----------------------------------+-----------+-------------------------+
| 0 | Sehn | Tim | NULL | 13qfqa5rojq18j84d1n2htjkm6fletg4 | Tim Sehn | 2022-06-07 16:39:32.066 |
| 0 | Sehn | Timothy | NULL | uhkv57j4bp2v16vcnmev9lshgkqq8ppb | Tim Sehn | 2022-06-07 16:41:49.847 |
| 0 | Sehn | Tim | 2018-09-08 | pg3nfi0j1dpc5pf1rfgckpmlteaufdrt | Tim Sehn | 2022-06-07 16:44:37.513 |
| 0 | Sehn | Timothy | 2018-09-08 | vn9b0qcematsj2f6ka0hfoflhr5s6p0b | Tim Sehn | 2022-06-07 17:10:02.07 |
+------+-----------+------------+------------+----------------------------------+-----------+-------------------------+
4 rows in set (0.00 sec)

dolt_diff_<tablename>allows you to filter the history down to only commits when the cell in question changed. In this case, I'm interested in the commits that are changing my first name. Note, there are two commits that changed my name because one is the original change and the second is the merge commit.

mysql> select to_commit,from_first_name,to_first_name from dolt_diff_employees 
 where (from_id=0 or to_id=0) and (from_first_name <> to_first_name or from_first_name is NULL)
 order by to_commit_date;
+----------------------------------+-----------------+---------------+
| to_commit | from_first_name | to_first_name |
+----------------------------------+-----------------+---------------+
| 13qfqa5rojq18j84d1n2htjkm6fletg4 | NULL | Tim |
| uhkv57j4bp2v16vcnmev9lshgkqq8ppb | Tim | Timothy |
| vn9b0qcematsj2f6ka0hfoflhr5s6p0b | Tim | Timothy |
+----------------------------------+-----------------+---------------+
3 rows in set (0.01 sec)

Dolt provides powerful data audit capabilities down to individual cells. When, how, and why has each cell in your database changed over time?

# Additional Reading

Head over toour documentationnow that you have a feel for Dolt. You can also read about what we've been working on inour blog.

# Security Policy

Dolt's current security policyis maintained in this repository. Please follow the disclosure instructions there. Please do not initially report security issues in this repository's public GitHub issues.

# Credits and License

Dolt relies heavily on open source code and ideas from theNomsproject. We are very
thankful to the Noms team for making this code freely available,
without which we would not have been able to build Dolt so rapidly.

Dolt is licensed under the Apache License, Version 2.0. SeeLICENSEfor
details.

## About

Dolt – Git for Data

www.dolthub.com

### Topics

 mysql

 git

 sql

 database

 mariadb

 immutable-database

 data-version-control

 data-versioning

 ai-agents

 database-version-control

 decentralized-database

 git-database

 git-for-data

 database-versioning

 version-controlled-database

 git-for-databases

 git-sql

 agent-memory

 ai-database

 agent-memory-server

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

20.8k

 stars
 

### Watchers

121

 watching
 

### Forks

664

 forks
 

 Report repository

 

## Releases597

1.83.5

 Latest

 

Mar 11, 2026

 

+ 596 releases

## Sponsor this project

 

 

 Sponsor

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

Learn more about GitHub Sponsors

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Go79.6%
* Shell19.5%
* JavaScript0.3%
* Java0.2%
* Python0.1%
* C0.1%
* Other0.2%