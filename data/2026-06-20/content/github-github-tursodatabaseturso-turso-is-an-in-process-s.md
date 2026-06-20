---
title: 'GitHub - tursodatabase/turso: Turso is an in-process SQL database, compatible with SQLite. · GitHub'
url: https://github.com/tursodatabase/turso
site_name: github
content_file: github-github-tursodatabaseturso-turso-is-an-in-process-s
fetched_at: '2026-06-20T11:42:16.317661'
original_url: https://github.com/tursodatabase/turso
author: tursodatabase
description: Turso is an in-process SQL database, compatible with SQLite. - tursodatabase/turso
---

tursodatabase

 

/

turso

Public

* NotificationsYou must be signed in to change notification settings
* Fork1k
* Star20k

 
 
 
 
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

18,011 Commits
18,011 Commits
.cargo
.cargo
 
 
.claude/
skills
.claude/
skills
 
 
.codex
.codex
 
 
.config
.config
 
 
.devcontainer
.devcontainer
 
 
.github
.github
 
 
assets
assets
 
 
bindings
bindings
 
 
cli
cli
 
 
core
core
 
 
docs
docs
 
 
examples
examples
 
 
extensions
extensions
 
 
fuzz
fuzz
 
 
licenses
licenses
 
 
macros
macros
 
 
packages/
turso-cli
packages/
turso-cli
 
 
parser
parser
 
 
perf
perf
 
 
scripts
scripts
 
 
sdk-kit-macros
sdk-kit-macros
 
 
sdk-kit
sdk-kit
 
 
serverless/
javascript
serverless/
javascript
 
 
sql_generation
sql_generation
 
 
sqlite3
sqlite3
 
 
sync
sync
 
 
testing
testing
 
 
tests
tests
 
 
tlaplus/
sqlite-tx
tlaplus/
sqlite-tx
 
 
tools/
dbhash
tools/
dbhash
 
 
.dockerignore
.dockerignore
 
 
.github.json
.github.json
 
 
.gitignore
.gitignore
 
 
.python-version
.python-version
 
 
.rp.yml
.rp.yml
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
COMPAT.md
COMPAT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
Dockerfile.antithesis
Dockerfile.antithesis
 
 
Dockerfile.cli
Dockerfile.cli
 
 
LICENSE.md
LICENSE.md
 
 
Makefile
Makefile
 
 
NOTICE.md
NOTICE.md
 
 
PERF.md
PERF.md
 
 
Pipfile
Pipfile
 
 
Pipfile.lock
Pipfile.lock
 
 
README.md
README.md
 
 
VOUCHED.td
VOUCHED.td
 
 
deny.toml
deny.toml
 
 
dist-workspace.toml
dist-workspace.toml
 
 
flake.lock
flake.lock
 
 
flake.nix
flake.nix
 
 
pyproject.toml
pyproject.toml
 
 
rust-toolchain.toml
rust-toolchain.toml
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

# Turso Database

An in-process SQL database, compatible with SQLite.

## About

Turso Database is an in-process SQL database written in Rust, compatible with SQLite.

⚠️Warning:This software is in BETA. It may still contain bugs and unexpected behavior. Use caution with production data and ensure you have backups.

## Features and Roadmap

* SQLite compatibilityfor SQL dialect, file formats, and the C API [seedocumentfor details]
* BEGIN CONCURRENTfor improved write throughput using multi-version concurrency control (MVCC).
* Change data capture (CDC)for real-time tracking of database changes.
* Multi-language supportforGoJavaScriptJava.NETPythonRustWebAssembly
* Go
* JavaScript
* Java
* .NET
* Python
* Rust
* WebAssembly
* Asynchronous I/Osupport on Linux withio_uring
* Cross-platformsupport for Linux, macOS, Windows and browsers (through WebAssembly)
* Vector supportsupport including exact search and vector manipulation
* Improved schema managementincluding extendedALTERsupport and faster schema changes.

The database has the following experimental features:

* Encryption at restfor protecting the data locally.
* Incremental computationusing DBSP for incremental view maintenance and query subscriptions.
* Full-Text-Searchpowered by the awesometantivylibrary
* Multi-process WAL coordinationvia the.tshmsidecar for cross-process WAL readers and writers.

The following features are on our current roadmap:

* Vector indexingfor fast approximate vector search, similar tolibSQL vector search.

## Getting Started

Please see theTurso Database Manualfor more information.

💻 Command Line

You can install the latest `turso` release with:

curl --proto 
'
=https
'
 --tlsv1.2 -LsSf \
 https://github.com/tursodatabase/turso/releases/latest/download/turso_cli-installer.sh 
|
 sh

Then launch the interactive shell:

$ tursodb

This will start the Turso interactive shell where you can execute SQL statements:

Turso

Enter ".help" for usage hints.

Connected to a transient in-memory database.

Use ".open FILENAME" to reopen on a persistent database

turso> CREATE TABLE users (id INT, username TEXT);

turso> INSERT INTO users VALUES (1, 'alice');

turso> INSERT INTO users VALUES (2, 'bob');

turso> SELECT * FROM users;

1|alice

2|bob

You can also build and run the latest development version with:

cargo run

If you like docker, we got you covered. Simply run this in the root folder:

make docker-cli-build 
&&
 \
make docker-cli-run

🦀 Rust

cargo add turso

Example usage:

let
 db = 
Builder
::
new_local
(
"sqlite.db"
)
.
build
(
)
.
await
?
;

let
 conn = db
.
connect
(
)
?
;

let
 res = conn
.
query
(
"SELECT * FROM users"
,
 
(
)
)
.
await
?
;

✨ JavaScript

npm i @tursodatabase/database

Example usage:

import
 
{
 
connect
 
}
 
from
 
'@tursodatabase/database'
;

const
 
db
 
=
 
await
 
connect
(
'sqlite.db'
)
;

const
 
stmt
 
=
 
db
.
prepare
(
'SELECT * FROM users'
)
;

const
 
users
 
=
 
stmt
.
all
(
)
;

console
.
log
(
users
)
;

🐍 Python

uv pip install pyturso

Example usage:

import
 
turso

con
 
=
 
turso
.
connect
(
"sqlite.db"
)

cur
 
=
 
con
.
cursor
()

res
 
=
 
cur
.
execute
(
"SELECT * FROM users"
)

print
(
res
.
fetchone
())

🦫 Go

go get turso.tech/database/tursogo

go install turso.tech/database/tursogo

Example usage:

import
 (
 
"database/sql"

 _ 
"turso.tech/database/tursogo"

)

conn
, 
_
 
=
 
sql
.
Open
(
"turso"
, 
"sqlite.db"
)

defer
 
conn
.
Close
()

stmt
, 
_
 
:=
 
conn
.
Prepare
(
"select * from users"
)

defer
 
stmt
.
Close
()

rows
, 
_
 
=
 
stmt
.
Query
()

for
 
rows
.
Next
() {
 
var
 
id
 
int

 
var
 
username
 
string

 
_
 
:=
 
rows
.
Scan
(
&
id
, 
&
username
)
 
fmt
.
Printf
(
"User: ID: %d, Username: %s
\n
"
, 
id
, 
username
)
}

️#️⃣ .NET

Example usage:

using
 
Turso
;

using
 
var
 
connection
 
=
 
new
 
TursoConnection
(
"Data Source=:memory:"
)
;

connection
.
Open
(
)
;

connection
.
ExecuteNonQuery
(
"CREATE TABLE t(a, b)"
)
;

var
 
rowsAffected
 
=
 
connection
.
ExecuteNonQuery
(
"INSERT INTO t(a, b) VALUES (1, 2), (3, 4)"
)
;

Console
.
WriteLine
(
$
"RowsAffected: 
{
rowsAffected
}
"
)
;

using
 
var
 
command
 
=
 
connection
.
CreateCommand
(
)
;

command
.
CommandText
 
=
 
"SELECT * FROM t"
;

using
 
var
 
reader
 
=
 
command
.
ExecuteReader
(
)
;

while
 
(
reader
.
Read
(
)
)

{

 
var
 
a
 
=
 
reader
.
GetInt32
(
0
)
;

 
var
 
b
 
=
 
reader
.
GetInt32
(
1
)
;

 
Console
.
WriteLine
(
$
"Value1: 
{
a
}
, Value2: 
{
b
}
"
)
;

}

☕️ Java

We integrated Turso Database into JDBC. For detailed instructions on how to use Turso Database with java, please refer to
theREADME.md under bindings/java.

🤖 MCP Server Mode

The Turso CLI includes a built-inModel Context Protocol (MCP)server that allows AI assistants to interact with your databases.

Start the MCP server with:

tursodb your_database.db --mcp

### Configuration

Add Turso to your MCP client configuration:

{
 
"mcpServers"
: {
 
"turso"
: {
 
"command"
: 
"
/path/to/.turso/tursodb
"
,
 
"args"
: [
"
/path/to/your/database.db
"
, 
"
--mcp
"
]
 }
 }
}

### Available Tools

The MCP server provides nine tools for database interaction:

1. open_database- Open a new database
2. current_database- Describe the current database
3. list_tables- List all tables in the database
4. describe_table- Describe the structure of a specific table
5. execute_query- Execute read-only SELECT queries
6. insert_data- Insert new data into tables
7. update_data- Update existing data in tables
8. delete_data- Delete data from tables
9. schema_change- Execute schema modification statements (CREATE TABLE, ALTER TABLE, DROP TABLE)

Once connected, you can ask your AI assistant:

* "Show me all tables in the database"
* "What's the schema for the users table?"
* "Find all posts with more than 100 upvotes"
* "Insert a new user with name 'Alice' and email 'alice@example.com'"

### MCP Clients

Claude Code

If you're usingClaude Code, you can easily connect to your Turso MCP server using the built-in MCP management commands:

#### Quick Setup

1. Add the MCP serverto Claude Code:claude mcp add my-database -- tursodb ./path/to/your/database.db --mcp
2. Restart Claude Codeto activate the connection
3. Start queryingyour database through natural language!

#### Command Breakdown

claude mcp add my-database -- tursodb ./path/to/your/database.db --mcp

#
 ↑ ↑ ↑ ↑

#
 | | | |

#
 Name | Database path MCP flag

#
 Separator

* my-database- Choose any name for your MCP server
* --- Required separator between Claude options and your command
* tursodb- The Turso database CLI
* ./path/to/your/database.db- Path to your SQLite database file
* --mcp- Enables MCP server mode

#### Example Usage

#
 For a local project database

cd
 /your/project
claude mcp add my-project-db -- tursodb ./data/app.db --mcp

#
 For an absolute path

claude mcp add analytics-db -- tursodb /Users/you/databases/analytics.db --mcp

#
 For a specific project (local scope)

claude mcp add project-db --local -- tursodb ./database.db --mcp

#### Managing MCP Servers

#
 List all configured MCP servers

claude mcp list

#
 Get details about a specific server

claude mcp get my-database

#
 Remove an MCP server

claude mcp remove my-database

Claude Desktop

For Claude Desktop, add the configuration to yourclaude_desktop_config.jsonfile:

{
 
"mcpServers"
: {
 
"turso"
: {
 
"command"
: 
"
/path/to/.turso/tursodb
"
,
 
"args"
: [
"
./path/to/your/database.db.db
"
, 
"
--mcp
"
]
 }
 }
}

Cursor

For Cursor, configure MCP in your settings:

1. Open Cursor settings
2. Navigate to Extensions → MCP
3. Add a new server with:* Name:turso
* Command:/path/to/.turso/tursodb
* Args:["./path/to/your/database.db.db", "--mcp"]

Alternatively, you can add it to your Cursor configuration file directly.

### Direct JSON-RPC Usage

The MCP server runs as a single process that handles multiple JSON-RPC requests over stdin/stdout. Here's how to interact with it directly:

#### Example with In-Memory Database

cat 
<<
 '
EOF
' | tursodb --mcp

{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {"name": "client", "version": "1.0"}}}

{"jsonrpc": "2.0", "id": 2, "method": "tools/call", "params": {"name": "schema_change", "arguments": {"query": "CREATE TABLE users (id INTEGER, name TEXT, email TEXT)"}}}

{"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": "list_tables", "arguments": {}}}

{"jsonrpc": "2.0", "id": 4, "method": "tools/call", "params": {"name": "insert_data", "arguments": {"query": "INSERT INTO users VALUES (1, 'Alice', 'alice@example.com')"}}}

{"jsonrpc": "2.0", "id": 5, "method": "tools/call", "params": {"name": "execute_query", "arguments": {"query": "SELECT * FROM users"}}}

EOF

#### Example with Existing Database

#
 Working with an existing database file

cat 
<<
 '
EOF
' | tursodb mydb.db --mcp

{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {"name": "client", "version": "1.0"}}}

{"jsonrpc": "2.0", "id": 2, "method": "tools/call", "params": {"name": "list_tables", "arguments": {}}}

EOF

## Contributing

We'd love to have you contribute to Turso Database! Please check out thecontribution guideto get started.

## FAQ

### Is Turso Database ready for production use?

Turso powers production apps today. That includesTurso Cloud, theKin AI assistant, andSpice.ai. However, it is still under active development and for mission-critical applications, caution is advised. Independent backups are encouraged. Turso is extensively tested by a collection of tools including a native Deterministic Simulation Testing suite andAntithesis, so we are generally confident in the end result. But our bar is SQLite-level reliability, and we will still recommend caution until we are confident it meets that bar.

### How is Turso Database different from Turso's libSQL?

Turso Database is a project to build the next evolution of SQLite in Rust, with a strong open contribution focus and features like native async support, vector search, and more. The libSQL project is also an attempt to evolve SQLite in a similar direction, but through a fork rather than a rewrite.

Rewriting SQLite in Rust started as an unassuming experiment, and due to its incredible success, replaces libSQL as our intended direction. At this point, libSQL is production ready, Turso Database is not - although it is evolving rapidly. More detailshere.

## Publications

* Pekka Enberg, Sasu Tarkoma, Jon Crowcroft Ashwin Rao (2024). Serverless Runtime / Database Co-Design With Asynchronous I/O. InEdgeSys ‘24.[PDF]
* Pekka Enberg, Sasu Tarkoma, and Ashwin Rao (2023). Towards Database and Serverless Runtime Co-Design. InCoNEXT-SW ’23. [PDF] [Slides]
* Alperen Keles, Ethan Chou, Harrison Goldstein, Leonidas Lampropoulos (2026). DIRT: Database-Integrated Random Testing. InDBTest '26.[PDF]

## License

This project is licensed under theMIT license.

### Contribution

Unless you explicitly state otherwise, any contribution intentionally submitted
for inclusion in Turso Database by you, shall be licensed as MIT, without any additional
terms or conditions.

## Partners

Thanks to all the partners of Turso!

## Contributors

Thanks to all the contributors to Turso Database!

## About

Turso is an in-process SQL database, compatible with SQLite.

### Topics

 sql

 database

 webassembly

 sqlite3

 embedded-database

### Resources

 Readme

 

### License

 MIT license
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

20k

 stars
 

### Watchers

83

 watching
 

### Forks

1k

 forks
 

 Report repository

 

## Releases203

0.6.1 -- 2026-05-22

 Latest

 

May 22, 2026

 

+ 202 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Rust85.7%
* C3.9%
* Python2.6%
* TypeScript2.3%
* Java1.4%
* C#1.2%
* Other2.9%