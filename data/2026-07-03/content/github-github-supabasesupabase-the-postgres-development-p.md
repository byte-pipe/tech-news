---
title: 'GitHub - supabase/supabase: The Postgres development platform. Supabase gives you a dedicated Postgres database to build your web, mobile, and AI applications. · GitHub'
url: https://github.com/supabase/supabase
site_name: github
content_file: github-github-supabasesupabase-the-postgres-development-p
fetched_at: '2026-07-03T11:49:32.302676'
original_url: https://github.com/supabase/supabase
author: supabase
description: The Postgres development platform. Supabase gives you a dedicated Postgres database to build your web, mobile, and AI applications. - supabase/supabase
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 supabase

 

/

supabase

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork13k
* Star105k

 
 
 
 
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

37,178 Commits
37,178 Commits
.agents/
skills/
vitest
.agents/
skills/
vitest
 
 
.claude
.claude
 
 
.cursor
.cursor
 
 
.github
.github
 
 
.vscode
.vscode
 
 
apps
apps
 
 
blocks/
vue
blocks/
vue
 
 
docker
docker
 
 
e2e/
studio
e2e/
studio
 
 
examples
examples
 
 
i18n
i18n
 
 
packages
packages
 
 
patches
patches
 
 
scripts
scripts
 
 
supa-mdx-lint
supa-mdx-lint
 
 
supabase
supabase
 
 
.coderabbit.yaml
.coderabbit.yaml
 
 
.cursorignore
.cursorignore
 
 
.dockerignore
.dockerignore
 
 
.gitignore
.gitignore
 
 
.mcp.json
.mcp.json
 
 
.misspell-fixer.ignore
.misspell-fixer.ignore
 
 
.npmrc
.npmrc
 
 
.nvmrc
.nvmrc
 
 
.prettierignore
.prettierignore
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
DEVELOPERS.md
DEVELOPERS.md
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
knip.jsonc
knip.jsonc
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
pnpm-workspace.yaml
pnpm-workspace.yaml
 
 
prettier.config.mjs
prettier.config.mjs
 
 
supa-mdx-lint.config.toml
supa-mdx-lint.config.toml
 
 
tsconfig.json
tsconfig.json
 
 
turbo.jsonc
turbo.jsonc
 
 
View all files

## Repository files navigation

# Supabase

Supabaseis the Postgres development platform. We're building the features of Firebase using enterprise-grade open source tools.

* Hosted Postgres Database.Docs
* Authentication and Authorization.Docs
* Auto-generated APIs.REST.DocsGraphQL.DocsRealtime subscriptions.Docs
* REST.Docs
* GraphQL.Docs
* Realtime subscriptions.Docs
* Functions.Database Functions.DocsEdge FunctionsDocs
* Database Functions.Docs
* Edge FunctionsDocs
* File Storage.Docs
* AI + Vector/Embeddings Toolkit.Docs
* Dashboard

Watch "releases" of this repo to get notified of major updates.

## Documentation

For full documentation, visitsupabase.com/docs

To see how to Contribute, visitGetting Started

## Community & Support

* Community Forum. Best for: help with building, discussion about database best practices.
* GitHub Issues. Best for: bugs and errors you encounter using Supabase.
* Email Support. Best for: problems with your database or infrastructure.
* Discord. Best for: sharing your applications and hanging out with the community.

## How it works

Supabase is a combination of open source tools. We’re building the features of Firebase using enterprise-grade, open source products. If the tools and communities exist, with an MIT, Apache 2, or equivalent open license, we will use and support that tool. If the tool doesn't exist, we build and open source it ourselves. Supabase is not a 1-to-1 mapping of Firebase. Our aim is to give developers a Firebase-like developer experience using open source tools.

Architecture

Supabase is ahosted platform. You can sign up and start using Supabase without installing anything.
You can alsoself-hostanddevelop locally.

* Postgresis an object-relational database system with over 30 years of active development that has earned it a strong reputation for reliability, feature robustness, and performance.
* Realtimeis an Elixir server that allows you to listen to PostgreSQL inserts, updates, and deletes using websockets. Realtime polls Postgres' built-in replication functionality for database changes, converts changes to JSON, then broadcasts the JSON over websockets to authorized clients.
* PostgRESTis a web server that turns your PostgreSQL database directly into a RESTful API.
* GoTrueis a JWT-based authentication API that simplifies user sign-ups, logins, and session management in your applications.
* Storagea RESTful API for managing files in S3, with Postgres handling permissions.
* pg_graphqla PostgreSQL extension that exposes a GraphQL API.
* postgres-metais a RESTful API for managing your Postgres, allowing you to fetch tables, add roles, and run queries, etc.
* Kongis a cloud-native API gateway.

#### Client libraries

Our approach for client libraries is modular. Each sub-library is a standalone implementation for a single external system. This is one of the ways we support existing tools.

Language

Client

Feature-Clients (bundled in Supabase client)

Supabase

PostgREST

GoTrue

Realtime

Storage

Functions

⚡️ Official ⚡️

JavaScript (TypeScript)

supabase-js

postgrest-js

auth-js

realtime-js

storage-js

functions-js

Flutter

supabase-flutter

postgrest-dart

gotrue-dart

realtime-dart

storage-dart

functions-dart

Swift

supabase-swift

postgrest-swift

auth-swift

realtime-swift

storage-swift

functions-swift

Python

supabase-py

postgrest-py

gotrue-py

realtime-py

storage-py

functions-py

💚 Community 💚

C#

supabase-csharp

postgrest-csharp

gotrue-csharp

realtime-csharp

storage-csharp

functions-csharp

Go

-

postgrest-go

gotrue-go

-

storage-go

functions-go

Java

-

-

gotrue-java

-

storage-java

-

Kotlin

supabase-kt

postgrest-kt

auth-kt

realtime-kt

storage-kt

functions-kt

Ruby

supabase-rb

postgrest-rb

-

-

-

-

Rust

-

postgrest-rs

-

-

-

-

Godot Engine (GDScript)

supabase-gdscript

-

-

-

-

-

## Badges

[
![
Made with Supabase
]
(
https://supabase.com/badge-made-with-supabase.svg
)]
(
https://supabase.com
)

<
a
 
href
="
https://supabase.com
"
>

 
<
img

 
width
="
168
"
 
height
="
30
"
 
src
="
https://supabase.com/badge-made-with-supabase.svg
"
 
alt
="
Made with Supabase
"
 
/>

</
a
>

[
![
Made with Supabase
]
(
https://supabase.com/badge-made-with-supabase-dark.svg
)]
(
https://supabase.com
)

<
a
 
href
="
https://supabase.com
"
>

 
<
img

 
width
="
168
"
 
height
="
30
"
 
src
="
https://supabase.com/badge-made-with-supabase-dark.svg
"
 
alt
="
Made with Supabase
"
 
/>

</
a
>

## Translations

* Arabic | العربية
* Albanian / Shqip
* Bangla / বাংলা
* Bulgarian / Български
* Catalan / Català
* Croatian / Hrvatski
* Czech / čeština
* Danish / Dansk
* Dutch / Nederlands
* English
* Estonian / eesti keel
* Finnish / Suomalainen
* French / Français
* German / Deutsch
* Greek / Ελληνικά
* Gujarati / ગુજરાતી
* Hebrew / עברית
* Hindi / हिंदी
* Hungarian / Magyar
* Nepali / नेपाली
* Indonesian / Bahasa Indonesia
* Italiano / Italian
* Japanese / 日本語
* Korean / 한국어
* Lithuanian / lietuvių
* Latvian / latviski
* Malay / Bahasa Malaysia
* Norwegian (Bokmål) / Norsk (Bokmål)
* Persian / فارسی
* Polish / Polski
* Portuguese / Português
* Portuguese (Brazilian) / Português Brasileiro
* Romanian / Română
* Russian / Pусский
* Serbian / Srpski
* Sinhala / සිංහල
* Slovak / slovenský
* Slovenian / Slovenščina
* Spanish / Español
* Simplified Chinese / 简体中文
* Swedish / Svenska
* Thai / ไทย
* Traditional Chinese / 繁體中文
* Turkish / Türkçe
* Ukrainian / Українська
* Vietnamese / Tiếng Việt
* List of translations

## About

The Postgres development platform. Supabase gives you a dedicated Postgres database to build your web, mobile, and AI applications.

supabase.com

### Topics

 alternative

 postgres

 firebase

 oauth2

 database

 ai

 example

 nextjs

 websockets

 realtime

 postgresql

 auth

 postgis

 embeddings

 postgrest

 vectors

 deno

 supabase

 pgvector

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

105k

 stars
 

### Watchers

715

 watching
 

### Forks

13k

 forks
 

 Report repository

 

## Releases28

Developer Update - May 2026

 Latest

 

May 7, 2026

 

+ 27 releases

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

* TypeScript70.8%
* MDX27.0%
* JavaScript0.8%
* CSS0.7%
* Shell0.4%
* Vue0.2%
* Other0.1%