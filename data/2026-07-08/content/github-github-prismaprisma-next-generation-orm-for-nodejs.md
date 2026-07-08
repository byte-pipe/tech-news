---
title: 'GitHub - prisma/prisma: Next-generation ORM for Node.js & TypeScript | PostgreSQL, MySQL, MariaDB, SQL Server, SQLite, MongoDB and CockroachDB · GitHub'
url: https://github.com/prisma/prisma
site_name: github
content_file: github-github-prismaprisma-next-generation-orm-for-nodejs
fetched_at: '2026-07-08T11:37:46.881724'
original_url: https://github.com/prisma/prisma
author: prisma
description: Next-generation ORM for Node.js & TypeScript | PostgreSQL, MySQL, MariaDB, SQL Server, SQLite, MongoDB and CockroachDB - prisma/prisma
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 prisma

 

/

prisma

Public

* NotificationsYou must be signed in to change notification settings
* Fork2.3k
* Star46.4k

 
 
 
 
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

12,230 Commits
12,230 Commits
.github
.github
 
 
.husky
.husky
 
 
.vscode
.vscode
 
 
docker
docker
 
 
docs
docs
 
 
drive/
spec
drive/
spec
 
 
eslint-local-rules
eslint-local-rules
 
 
examples
examples
 
 
graphs
graphs
 
 
helpers
helpers
 
 
packages
packages
 
 
projects/
agent-native
projects/
agent-native
 
 
sandbox
sandbox
 
 
scripts
scripts
 
 
.db.env
.db.env
 
 
.dockerignore
.dockerignore
 
 
.envrc
.envrc
 
 
.gitignore
.gitignore
 
 
.gitleaksignore
.gitleaksignore
 
 
.npmrc
.npmrc
 
 
.prettierignore
.prettierignore
 
 
.prettierrc.yml
.prettierrc.yml
 
 
AGENTS.md
AGENTS.md
 
 
ARCHITECTURE.md
ARCHITECTURE.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
GEMINI.md
GEMINI.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
TESTING.md
TESTING.md
 
 
eslint.config.cjs
eslint.config.cjs
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
pnpm-workspace.yaml
pnpm-workspace.yaml
 
 
tsconfig.build.bundle.json
tsconfig.build.bundle.json
 
 
tsconfig.build.regular.json
tsconfig.build.regular.json
 
 
tsconfig.json
tsconfig.json
 
 
tsconfig.utils.typecheck.json
tsconfig.utils.typecheck.json
 
 
turbo.json
turbo.json
 
 
vitest.config.ts
vitest.config.ts
 
 
View all files

## Repository files navigation

# Prisma

Quickstart

  •  

Website

  •  

Docs

  •  

Examples

  •  

Blog

  •  

Discord

  •  

Twitter

  •  

Youtube

## What is Prisma?

Prisma ORM is anext-generation ORMthat consists of these tools:

* Prisma Client: Auto-generated and type-safe query builder for Node.js & TypeScript
* Prisma Migrate: Declarative data modeling & migration system
* Prisma Studio: GUI to view and edit data in your database

Prisma Client can be used inanyNode.js or TypeScript backend application (including serverless applications and microservices). This can be aREST API, aGraphQL API, a gRPC API, or anything else that needs a database.

If you need a database to use with Prisma ORM, check outPrisma Postgresor if you are looking for our MCP Server, headhere.

## Getting started

### Quickstart (5min)

The fastest way to get started with Prisma is by following the quickstart guides. You can choose either of two databases:

* Prisma Postgres
* SQLite

### Bring your own database

If you already have your own database, you can follow these guides:

* Add Prisma to an existing project
* Set up a new project with Prisma from scratch

## How Prisma ORM works

This section provides a high-level overview of how Prisma ORM works and its most important technical components. For a more thorough introduction, visit thePrisma documentation.

### The Prisma schema

Every project that uses a tool from the Prisma toolkit starts with aPrisma schema file. The Prisma schema allows developers to define theirapplication modelsin an intuitive data modeling language and configuregenerators.

// Data source

datasource
 
db
 {

 
provider
 
=
 
"
postgresql
"

}

// Generator

generator
 
client
 {

 
provider
 
=
 
"
prisma-client
"

 
output
 
=
 
"
../generated
"

}

// Data model

model
 
Post
 {

 
id
 
Int
 
@id
 
@default
(
autoincrement
()
)

 
title
 
String

 
content
 
String
?

 
published
 
Boolean
 
@default
(
false
)

 
author
 
User
?
 
@relation
(
fields
: 
[
authorId
]
, 
references
: 
[
id
]
)

 
authorId
 
Int
?

}

model
 
User
 {

 
id
 
Int
 
@id
 
@default
(
autoincrement
()
)

 
email
 
String
 
@unique

 
name
 
String
?

 
posts
 
Post
[]

}

In this schema, you configure three things:

* Data source: Specifies your database type and thus defines the features and data types you can use in the schema
* Generator: Indicates that you want to generate Prisma Client
* Data model: Defines your application models

### prisma.config.ts

Database connection details are defined viaprisma.config.ts.

import
 
{
 
defineConfig
 
}
 
from
 
'prisma/config'

export
 
default
 
defineConfig
(
{

 
datasource
: 
{

 
url
: 
'postgres://...'
,

 
}
,

}
)

If you store the database connection string inprocess.env, anenvfunction can help you access it in a type safe way and throw an error if it is missing at run time:

import
 
{
 
defineConfig
,
 
env
 
}
 
from
 
'prisma/config'

export
 
default
 
defineConfig
(
{

 
datasource
: 
{

 
url
: 
env
(
'DATABASE_URL'
)
,

 
}
,

}
)

Prisma ORM does not load the.envfiles for you automatically. If you want to populate the environment variables from a.envfile, consider using a package such asdotenvor@dotenvx/dotenvx.

The configuration file may look like this in that case:

import
 
'dotenv/config'

import
 
{
 
defineConfig
,
 
env
 
}
 
from
 
'prisma/config'

export
 
default
 
defineConfig
(
{

 
datasource
: 
{

 
url
: 
env
(
'DATABASE_URL'
)
,

 
}
,

}
)

To start a local PostgreSQL development server without using Docker and without any configuration, runprisma dev:

npx prisma dev

Alternatively, spin up an instant Prisma Postgres® database in the cloud:

npx create-db --interactive

### The Prisma data model

On this page, the focus is on the data model. You can learn more aboutData sourcesandGeneratorson the respective docs pages.

#### Functions of Prisma models

The data model is a collection ofmodels. A model has two major functions:

* Represent a table in the underlying database
* Provide the foundation for the queries in the Prisma Client API

#### Getting a data model

There are two major workflows for "getting" a data model into your Prisma schema:

* Generate the data model fromintrospectinga database
* Manually writing the data model and mapping it to the database withPrisma Migrate

Once the data model is defined, you cangenerate Prisma Clientwhich will expose CRUD and more queries for the defined models. If you're using TypeScript, you'll get full type-safety for all queries (even when only retrieving the subsets of a model's fields).

### Accessing your database with Prisma Client

#### Step 1: Install Prisma

First, install Prisma CLI as a development dependency and Prisma Client:

npm install prisma --save-dev
npm install @prisma/client

#### Step 2: Set up your Prisma schema

Ensure your Prisma schema includes ageneratorblock with anoutputpath specified:

generator
 
client
 {

 
provider
 
=
 
"
prisma-client
"

 
output
 
=
 
"
../generated
"

}

datasource
 
db
 {

 
provider
 
=
 
"
postgresql
"
 
// mysql, sqlite, sqlserver, mongodb or cockroachdb

}

#### Step 3: Configure Prisma Config

Configure the Prisma CLI using aprisma.config.tsfile. This file configures Prisma CLI subcommands likemigrateandstudio. Create aprisma.config.tsfile in your project root:

import
 
{
 
defineConfig
,
 
env
 
}
 
from
 
'prisma/config'

type
 
Env
 
=
 
{

 
DATABASE_URL
: 
string

}

export
 
default
 
defineConfig
(
{

 
schema
: 
'prisma/schema.prisma'
,

 
migrations
: 
{

 
path
: 
'prisma/migrations'
,

 
}
,

 
datasource
: 
{

 
url
: 
env
<
Env
>
(
'DATABASE_URL'
)
,

 
}
,

}
)

Note: Environment variables from.envfiles are not automatically loaded when usingprisma.config.ts. You can usedotenvby importingdotenv/configat the top of your config file. For Bun,.envfiles are automatically loaded.

Learn more aboutPrisma Configand all available configuration options.

#### Step 4: Generate Prisma Client

Generate Prisma Client with the following command:

npx prisma generate

This command reads your Prisma schema andgeneratesthe Prisma Client code in the location specified by theoutputpath in your generator configuration.

After you change your data model, you'll need to manually re-generate Prisma Client to ensure the generated code gets updated:

npx prisma generate

Refer to the documentation for more information about"generating the Prisma client".

#### Step 5: Use Prisma Client to send queries to your database

Once the Prisma Client is generated, you can import it in your code and send queries to your database.

##### Import and instantiate Prisma Client

You can import and instantiate Prisma Client from the output path specified in your generator configuration. When instantiating the Client, you need to provide adriver adapterto its constructor. For example, when using PostgreSQL with a driver adapter:

import
 
{
 
PrismaClient
 
}
 
from
 
'./generated/client'

import
 
{
 
PrismaPg
 
}
 
from
 
'@prisma/adapter-pg'

const
 
adapter
 
=
 
new
 
PrismaPg
(
{
 
connectionString
: 
process
.
env
.
DATABASE_URL
 
}
)

const
 
prisma
 
=
 
new
 
PrismaClient
(
{
 adapter 
}
)

To load environment variables, you can usedotenvby importingdotenv/config, usetsx --env-file=.env,node --env-file=.env, or Bun (which loads.envautomatically).

Now you can start sending queries via the generated Prisma Client API, here are a few sample queries. Note that all Prisma Client queries returnplain old JavaScript objects.

Learn more about the available operations in thePrisma Client docsor watch thisdemo video(2 min).

##### Retrieve allUserrecords from the database

const
 
allUsers
 
=
 
await
 
prisma
.
user
.
findMany
(
)

##### Include thepostsrelation on each returnedUserobject

const
 
allUsers
 
=
 
await
 
prisma
.
user
.
findMany
(
{

 
include
: 
{
 
posts
: 
true
 
}
,

}
)

##### Filter allPostrecords that contain"prisma"

const
 
filteredPosts
 
=
 
await
 
prisma
.
post
.
findMany
(
{

 
where
: 
{

 
OR
: 
[
{
 
title
: 
{
 
contains
: 
'prisma'
 
}
 
}
,
 
{
 
content
: 
{
 
contains
: 
'prisma'
 
}
 
}
]
,

 
}
,

}
)

##### Create a newUserand a newPostrecord in the same query

const
 
user
 
=
 
await
 
prisma
.
user
.
create
(
{

 
data
: 
{

 
name
: 
'Alice'
,

 
email
: 
'alice@prisma.io'
,

 
posts
: 
{

 
create
: 
{
 
title
: 
'Join us for Prisma Day 2021'
 
}
,

 
}
,

 
}
,

}
)

##### Update an existingPostrecord

const
 
post
 
=
 
await
 
prisma
.
post
.
update
(
{

 
where
: 
{
 
id
: 
42
 
}
,

 
data
: 
{
 
published
: 
true
 
}
,

}
)

#### Usage with TypeScript

Note that when using TypeScript, the result of this query will bestatically typedso that you can't accidentally access a property that doesn't exist (and any typos are caught at compile-time). Learn more about leveraging Prisma Client's generated types on theAdvanced usage of generated typespage in the docs.

## Community

Prisma has a large and supportivecommunityof enthusiastic application developers. You can join us onDiscordand here onGitHub.

## Badges

 

Built something awesome with Prisma? 🌟 Show it off with thesebadges, perfect for your readme or website.

[![Made with Prisma](https://made-with.prisma.io/dark.svg)](https://prisma.io)

[![Made with Prisma](https://made-with.prisma.io/indigo.svg)](https://prisma.io)

## Security

If you have a security issue to report, please contact us atsecurity@prisma.io.

## Support

### Ask a question about Prisma

You can ask questions and initiatediscussionsabout Prisma-related topics in theprismarepository on GitHub.

👉Ask a question

### Create a bug report for Prisma

If you see an error message or run into an issue, please make sure to create a bug report! You can findbest practices for creating bug reports(like including additional debugging output) in the docs.

👉Create bug report

### Submit a feature request

If Prisma currently doesn't have a certain feature, be sure to check out theroadmapto see if this is already planned for the future.

If the feature on the roadmap is linked to a GitHub issue, please make sure to leave a 👍 reaction on the issue and ideally a comment with your thoughts about the feature!

👉Submit feature request

## Contributing

Refer to ourcontribution guidelinesandCode of Conduct for contributors.

## Tests Status

* Prisma Tests Status:

Scheduled CI is currently disabled across the ORM repos; test workflows run on push, pull request, and manualworkflow_dispatch. See theActions tabfor recent runs.

## About

Next-generation ORM for Node.js & TypeScript | PostgreSQL, MySQL, MariaDB, SQL Server, SQLite, MongoDB and CockroachDB

www.prisma.io

### Topics

 nodejs

 javascript

 mysql

 postgres

 mongo

 typescript

 sql-server

 orm

 database

 mongodb

 sqlite

 postgresql

 mariadb

 query-builder

 mssql

 sqlserver

 mongodb-orm

 cockroachdb

 prisma

 prisma-client

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

46.4k

 stars
 

### Watchers

296

 watching
 

### Forks

2.3k

 forks
 

 Report repository

 

## Releases247

7.8.0

 Latest

 

Apr 22, 2026

 

+ 246 releases

## Used by773k

 + 773,462
 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript99.0%
* JavaScript0.9%
* Shell0.1%
* Dockerfile0.0%
* PLpgSQL0.0%
* Batchfile0.0%