---
title: 'GitHub - colinhacks/zod: TypeScript-first schema validation with static type inference · GitHub'
url: https://github.com/colinhacks/zod
site_name: github
content_file: github-github-colinhackszod-typescript-first-schema-valid
fetched_at: '2026-08-30T15:11:52.873770'
original_url: https://github.com/colinhacks/zod
author: colinhacks
description: TypeScript-first schema validation with static type inference - colinhacks/zod
---

colinhacks

 

/

zod

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork2.2k
* Star43.6k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

3,154 Commits
3,154 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.claude/
skills
.claude/
skills
 
 
.codex
.codex
 
 
.configs
.configs
 
 
.devcontainer
.devcontainer
 
 
.github/
workflows
.github/
workflows
 
 
.husky
.husky
 
 
.vscode
.vscode
 
 
logo
logo
 
 
packages
packages
 
 
rfcs
rfcs
 
 
scripts
scripts
 
 
wiki
wiki
 
 
.cursorrules
.cursorrules
 
 
.editorconfig
.editorconfig
 
 
.gitignore
.gitignore
 
 
.mcp.json
.mcp.json
 
 
.nojekyll
.nojekyll
 
 
.npmrc
.npmrc
 
 
.nvmrc
.nvmrc
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
FUNDING.yml
FUNDING.yml
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
biome.jsonc
biome.jsonc
 
 
logo.svg
logo.svg
 
 
mm.mjs
mm.mjs
 
 
package.json
package.json
 
 
play.ts
play.ts
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
pnpm-workspace.yaml
pnpm-workspace.yaml
 
 
tea.yaml
tea.yaml
 
 
tsconfig.json
tsconfig.json
 
 
vitest.compile.config.ts
vitest.compile.config.ts
 
 
vitest.config.ts
vitest.config.ts
 
 
vitest.root.mjs
vitest.root.mjs
 
 
View all files

## Repository files navigation

# Zod

TypeScript-first schema validation with static type inferenceby@colinhacks

Docs

  •  

Discord

  •  

𝕏

  •  

Bluesky

### Read the docs →

## What is Zod?

Zod is a TypeScript-first validation library. Define a schema and parse some data with it. You'll get back a strongly typed, validated result.

import
 
*
 
as
 
z
 
from
 
"zod"
;

const
 
User
 
=
 
z
.
object
(
{

 
name
: 
z
.
string
(
)
,

}
)
;

// some untrusted data...

const
 
input
 
=
 
{

 
/* stuff */

}
;

// the parsed result is validated and type safe!

const
 
data
 
=
 
User
.
parse
(
input
)
;

// so you can use it with confidence :)

console
.
log
(
data
.
name
)
;

## Features

* Zero external dependencies
* Works in Node.js and all modern browsers
* Tiny:2kbcore bundle (gzipped)
* Immutable API: methods return a new instance
* Concise interface
* Works with TypeScript and plain JS
* Built-in JSON Schema conversion
* Extensive ecosystem

## Installation

npm install zod

## Basic usage

Before you can do anything else, you need to define a schema. For the purposes of this guide, we'll use a simple object schema.

import
 
*
 
as
 
z
 
from
 
"zod"
;

const
 
Player
 
=
 
z
.
object
(
{

 
username
: 
z
.
string
(
)
,

 
xp
: 
z
.
number
(
)
,

}
)
;

### Parsing data

Given any Zod schema, use.parseto validate an input. If it's valid, Zod returns a strongly-typeddeep cloneof the input.

Player
.
parse
(
{
 
username
: 
"billie"
,
 
xp
: 
100
 
}
)
;

// => returns { username: "billie", xp: 100 }

Note— If your schema uses certain asynchronous APIs likeasyncrefinementsortransforms, you'll need to use the.parseAsync()method instead.

const
 
schema
 
=
 
z
.
string
(
)
.
refine
(
async
 
(
val
)
 
=>
 
val
.
length
 
<=
 
8
)
;

await
 
schema
.
parseAsync
(
"hello"
)
;

// => "hello"

### AOT compilation

For hot validation paths,z.compile(schema)returns a schema clone with an ahead-of-time compiled fast path. Valid inputs take the compiled path; invalid inputs fall back to the regular parser so error reporting stays identical.

Across a 55-schema benchmark the median speedup is2.4x, and it scales with how much work the schema does per parse: a large array of objects is ~9x, a 20-key object ~9x, a nested object ~4.5x, while a barez.string()gains nothing — compilation removes per-node dispatch and allocation, and a singletypeofhas none to remove.

const
 
CompiledPlayer
 
=
 
z
.
compile
(
Player
)
;

CompiledPlayer
.
parse
(
{
 
username
: 
"billie"
,
 
xp
: 
100
 
}
)
;

To enable compilation globally for schemas constructed after import:

import
 
"zod/compile"
;
 
// place before modules that define schemas

Things to know:

* Compilation usesnew Function. Global mode is automatically disabled whenz.config({ jitless: true })is set (e.g. CSP environments); callingz.compile()directly is an explicit opt-in.
* Schemas with async refinements or transforms can't be compiled, and neither can a few other constructs. That is not an error:z.compile()hands the schema back unchanged and it keeps using the regular parser, exactly as global mode leaves it. Pass{ strict: true }to throwZodCompileAsyncError/ZodCompileUnsupportedErrorinstead.
* On invalid input, refinements and transforms may run twice (fast path, then fallback).
* Deriving a new schema from a compiled one (.refine(),.extend(), etc.) returns an uncompiled schema — compile the final schema.

Seecompiledocsfor details.

### Handling errors

When validation fails, the.parse()method will throw aZodErrorinstance with granular information about the validation issues.

try
 
{

 
Player
.
parse
(
{
 
username
: 
42
,
 
xp
: 
"100"
 
}
)
;

}
 
catch
 
(
err
)
 
{

 
if
 
(
err
 
instanceof
 
z
.
ZodError
)
 
{

 
err
.
issues
;

 
/* [

 {

 expected: 'string',

 code: 'invalid_type',

 path: [ 'username' ],

 message: 'Invalid input: expected string'

 },

 {

 expected: 'number',

 code: 'invalid_type',

 path: [ 'xp' ],

 message: 'Invalid input: expected number'

 }

 ] */

 
}

}

To avoid atry/catchblock, you can use the.safeParse()method to get back a plain result object containing either the successfully parsed data or aZodError. The result type is adiscriminated union, so you can handle both cases conveniently.

const
 
result
 
=
 
Player
.
safeParse
(
{
 
username
: 
42
,
 
xp
: 
"100"
 
}
)
;

if
 
(
!
result
.
success
)
 
{

 
result
.
error
;
 
// ZodError instance

}
 
else
 
{

 
result
.
data
;
 
// { username: string; xp: number }

}

Note— If your schema uses certain asynchronous APIs likeasyncrefinementsortransforms, you'll need to use the.safeParseAsync()method instead.

const
 
schema
 
=
 
z
.
string
(
)
.
refine
(
async
 
(
val
)
 
=>
 
val
.
length
 
<=
 
8
)
;

await
 
schema
.
safeParseAsync
(
"hello"
)
;

// => { success: true; data: "hello" }

### Inferring types

Zod infers a static type from your schema definitions. You can extract this type with thez.infer<>utility and use it however you like.

const
 
Player
 
=
 
z
.
object
(
{

 
username
: 
z
.
string
(
)
,

 
xp
: 
z
.
number
(
)
,

}
)
;

// extract the inferred type

type
 
Player
 
=
 
z
.
infer
<
typeof
 
Player
>
;

// use it in your code

const
 
player
: 
Player
 
=
 
{
 
username
: 
"billie"
,
 
xp
: 
100
 
}
;

In some cases, the input & output types of a schema can diverge. For instance, the.transform()API can convert the input from one type to another. In these cases, you can extract the input and output types independently:

const
 
mySchema
 
=
 
z
.
string
(
)
.
transform
(
(
val
)
 
=>
 
val
.
length
)
;

type
 
MySchemaIn
 
=
 
z
.
input
<
typeof
 
mySchema
>
;

// => string

type
 
MySchemaOut
 
=
 
z
.
output
<
typeof
 
mySchema
>
;
 
// equivalent to z.infer<typeof mySchema>

// number