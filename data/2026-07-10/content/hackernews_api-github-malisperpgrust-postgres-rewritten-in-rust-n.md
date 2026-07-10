---
title: 'GitHub - malisper/pgrust: Postgres rewritten in Rust, now passing 100% of the Postgres regression tests · GitHub'
url: https://github.com/malisper/pgrust
site_name: hackernews_api
content_file: hackernews_api-github-malisperpgrust-postgres-rewritten-in-rust-n
fetched_at: '2026-07-10T12:02:06.392073'
original_url: https://github.com/malisper/pgrust
author: SweetSoftPillow
date: '2026-07-09'
description: Postgres rewritten in Rust, now passing 100% of the Postgres regression tests - malisper/pgrust
tags:
- hackernews
- trending
---

malisper

 

/

pgrust

Public

* NotificationsYou must be signed in to change notification settings
* Fork27
* Star971

 
 
 
 
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

7,103 Commits
7,103 Commits
.cargo
.cargo
 
 
crates
crates
 
 
docker
docker
 
 
scripts
scripts
 
 
vendor/
postgres-18.3
vendor/
postgres-18.3
 
 
.dockerignore
.dockerignore
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.gitleaks.toml
.gitleaks.toml
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
View all files

## Repository files navigation

# pgrust

A Postgres rewrite in Rust.

Browser demo

  |  

Discord

  |  

Get pgrust updates

  |  

Issues

pgrust targets compatibility with Postgres 18.3 and matches Postgres's
expected output across more than 46,000 regression queries.

pgrust is disk compatible with Postgres and can boot from an existing Postgres
18.3 data directory.

The goal is to make Postgres easier to change from the inside: keep the behavior
Postgres-shaped, keep the real Postgres tests as the oracle, and use Rust plus
AI-assisted programming to explore deeper server changes.

Update: We're working on a new not yet published version of pgrust that currently passes 100% of Postgres regression suite, has a thread per connection model instead of process per connection, is 50% faster than Postgres on transaction workloads, and is ~300x faster than Postgres on analytical workloads (2x slower than Clickhouse on clickbench and we think it can get faster than Clickhouse). Follow pgrust or join our Discord for updates!

## Follow pgrust

Get project updates by email, including new
releases, compatibility milestones, and architecture experiments.

## Status

pgrust is not production-ready yet. It is not performance optimized yet.

Existing Postgres extensions and procedural language extensions such as
PL/Python, PL/Perl, and PL/Tcl are not generally compatible yet. Some bundled
contrib modules are already ported, and more compatibility may be possible over
time.

## Roadmap

* multithreaded Postgres internals
* built-in connection pooling
* better JSON-heavy workload support
* fast forking and branching workflows
* storage experiments, including no-vacuum designs
* runtime guardrails for bad queries and AI-generated SQL
* fewer sudden bad plan switches

## Try It

Try the WebAssembly demo athttps://pgrust.com.

Docker:

docker run -d --name pgrust -e POSTGRES_PASSWORD=secret malisper/pgrust:v0.1 
&&
 
until
 docker 
exec
 -e PGPASSWORD=secret pgrust psql -h 127.0.0.1 -U postgres -c 
'
\q
'
 
>
/dev/null 
2>&1
;
 
do
 sleep 1
;
 
done
 
&&
 docker 
exec
 -it -e PGPASSWORD=secret pgrust psql -h 127.0.0.1 -U postgres
;
 docker rm -f pgrust

This uses thepsqlclient inside the Docker image.

malisper/pgrust:latestcurrently points at the same release, butv0.1is the
pinned launch image.

## Build From Source

macOS:

brew install icu4c openssl@3 libpq

export
 LIBRARY_PATH=
"
$(
brew --prefix openssl@3
)
/lib:
${LIBRARY_PATH
:-
}
"

export
 PKG_CONFIG_PATH=
"
$(
brew --prefix openssl@3
)
/lib/pkgconfig:
$(
brew --prefix icu4c
)
/lib/pkgconfig:
${PKG_CONFIG_PATH
:-
}
"

export
 PATH=
"
$(
brew --prefix libpq
)
/bin:
$PATH
"

Debian/Ubuntu:

sudo apt-get update
sudo apt-get install -y build-essential pkg-config libicu-dev libssl-dev libldap2-dev libpam0g-dev postgresql-client-18

Build:

PGRUST_PGSHAREDIR=
"
$PWD
/vendor/postgres-18.3/share
"
 \
cargo build --release --locked --bin postgres

Create a data directory:

target/release/postgres --initdb \
 -D /tmp/pgrust-data \
 -L 
"
$PWD
/vendor/postgres-18.3/share
"
 \
 --no-locale \
 --encoding UTF8 \
 -U postgres

Run pgrust:

ulimit
 -s 65520

RUST_MIN_STACK=33554432 target/release/postgres \
 -D /tmp/pgrust-data \
 -F \
 -c listen_addresses= \
 -k /tmp \
 -p 5432 \
 -c io_method=sync \
 -c max_stack_depth=60000

Connect:

psql -h /tmp -p 5432 -U postgres -d postgres \
 -c 
"
select version(), 1 + 1 as two
"

## Regression Tests

Run the Postgres regression tests against pgrust:

PGRUST_BIN=
"
$PWD
/target/release/postgres
"
 \
scripts/run-regression

The runner uses pgrust's own--initdbplus the vendored Postgres 18.3 test
files in this repository. It needs a Postgres 18psqlclient onPATH; ifpsqlis somewhere else, setPGRUST_PSQL=/path/to/psql.

Verified launch result: pgrust matched Postgres's expected output across more
than 46,000 regression queries.

## History

This repository now contains the newer pgrust implementation that reached the
regression-test milestone.

The older public implementation is archived onarchive/pre-fabled-2026-06-23.

Background:

* Original pgrust launch:https://malisper.me/pgrust-rebuilding-postgres-in-rust-with-ai/
* 67% regression update:https://malisper.me/pgrust-update-at-67-postgres-compatibility-and-accelerating/
* Four Horsemen roadmap:https://malisper.me/the-four-horsemen-behind-thousands-of-postgres-outages/

## Feedback

Please open an issue if something breaks, if setup is confusing, or if there is
a Postgres improvement you want to see first.

## Contact

* Email:maintainers@pgrust.com
* Discord:https://discord.gg/FZZ4dbdvwU
* Project updates:https://pgrust.com/#updates

## License

pgrust is licensed under AGPL-3.0. SeeLICENSE.

## About

Postgres rewritten in Rust, now passing 100% of the Postgres regression tests

pgrust.com

### Topics

 rust

 postgres

 database

 postgresql

 ai-assisted-development

### Resources

 Readme

 

### License

 AGPL-3.0 license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

971

 stars
 

### Watchers

9

 watching
 

### Forks

27

 forks
 

 Report repository

 

## Releases

1

tags

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Rust99.8%
* Other0.2%