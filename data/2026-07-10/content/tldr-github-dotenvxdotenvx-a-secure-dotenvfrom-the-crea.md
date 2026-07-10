---
title: 'GitHub - dotenvx/dotenvx: a secure dotenv–from the creator of `dotenv` · GitHub'
url: https://github.com/dotenvx/dotenvx
site_name: tldr
content_file: tldr-github-dotenvxdotenvx-a-secure-dotenvfrom-the-crea
fetched_at: '2026-07-10T19:33:06.112752'
original_url: https://github.com/dotenvx/dotenvx
date: '2026-07-10'
description: a secure dotenv–from the creator of `dotenv`. Contribute to dotenvx/dotenvx development by creating an account on GitHub.
tags:
- tldr
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 dotenvx

 

/

dotenvx

Public

* NotificationsYou must be signed in to change notification settings
* Fork146
* Star5.6k

 
 
 
 
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

3,397 Commits
3,397 Commits
.github/
workflows
.github/
workflows
 
 
spec
spec
 
 
src
src
 
 
tests
tests
 
 
.gitignore
.gitignore
 
 
.npmignore
.npmignore
 
 
.npmrc
.npmrc
 
 
.shellspec
.shellspec
 
 
CHANGELOG.md
CHANGELOG.md
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
esbuild.js
esbuild.js
 
 
install.sh
install.sh
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
View all files

## Repository files navigation

a secure dotenv–from the creator ofdotenv.

* run anywhere (cross-platform)
* multi-environment
* encrypted envs

Read the whitepaper

 

### Quickstart

Install and use it in code just likedotenv.

npm install @dotenvx/dotenvx --save

// index.js

require
(
'@dotenvx/dotenvx'
)
.
config
(
)

// or import '@dotenvx/dotenvx/config' // for esm

console
.
log
(
`Hello 
${
process
.
env
.
HELLO
}
`
)

 

or install globally -unlocks dotenv for any language, framework, or platform!

with npm 🌍

npm i -g @dotenvx/dotenvx
dotenvx encrypt

 

with curl 🌐

curl -sfS https://dotenvx.sh 
|
 sh
dotenvx encrypt

 

with brew 🍺

brew tap dotenvx/brew
brew trust dotenvx/brew
brew install dotenvx
dotenvx encrypt

 

with docker 🐳

docker run -it --rm -v 
$(
pwd
)
:/app dotenv/dotenvx encrypt

 

with github releases 🐙

curl -L -o dotenvx.tar.gz 
"
https://github.com/dotenvx/dotenvx/releases/latest/download/dotenvx-
$(
uname -s
)
-
$(
uname -m
)
.tar.gz
"

tar -xzf dotenvx.tar.gz
./dotenvx encrypt

 

or windows 🪟

winget install dotenvx
dotenvx encrypt

 

## Run Anywhere

$ 
echo
 
"
HELLO=Dotenvx
"
 
>
 .env
$ 
echo
 
"
console.log('Hello ' + process.env.HELLO)
"
 
>
 index.js

$ node index.js
Hello undefined 
#
 without dotenvx

$ dotenvx run -- node index.js
Hello Dotenvx 
#
 with dotenvx

>
 :-D

seequickstart guides

More examples

TypeScript 📘

// package.json

{
 
"type"
: 
"
module
"
,
 
"dependencies"
: {
 
"chalk"
: 
"
^5.3.0
"

 }
}

// index.ts

import
 
chalk
 
from
 
'chalk'

console
.
log
(
chalk
.
blue
(
`Hello 
${
process
.
env
.
HELLO
}
`
)
)

$ npm install
$ 
echo
 
"
HELLO=Dotenvx
"
 
>
 .env

$ dotenvx run -- npx tsx index.ts
Hello Dotenvx

Astro 🚀

Preface Astro scripts withdotenvx run --and read your env values in Astro.

{
 
"scripts"
: {
 
"dev"
: 
"
dotenvx run -- astro dev
"
,
 
"build"
: 
"
dotenvx run -- astro build
"
,
 
"preview"
: 
"
dotenvx run -- astro preview
"

 }
}

export async function GET() 
{

 
return
 
new
 
Response
(
 
JSON
.
stringify
({
 HELLO: 
process
.
env
.
HELLO
,
 }),
 {
 status: 
200
,
 headers: {
 
"
Content-Type
"
: 
"
application/json
"
,
 },
 }
 );

}

seeastro guide

Expo 🧭

Preface Expo scripts withdotenvx run --.

{
 
"scripts"
: {
 
"start"
: 
"
dotenvx run -- expo start
"
,
 
"reset-project"
: 
"
node ./scripts/reset-project.js
"
,
 
"android"
: 
"
dotenvx run -- expo start --android
"
,
 
"ios"
: 
"
dotenvx run -- expo start --ios
"
,
 
"web"
: 
"
dotenvx run -- expo start --web
"
,
 
"lint"
: 
"
expo lint
"

 }
}

seeexpo guide

Next.js ▲

Install Dotenvx and@dotenvx/next-env.

$ npm install @dotenvx/dotenvx
$ npm install @dotenvx/next-env

Override@next/envin yourpackage.json.

{
 
"overrides"
: {
 
"@next/env"
: 
"
npm:@dotenvx/next-env
"

 }
}

Encrypt your.envfile.

$ npx dotenvx encrypt
◈ encrypted (.env)

Your encrypted secrets are automatically injected and readable in Next.js.

import
 
{
 
NextResponse
 
}
 
from
 
'next/server'

export
 
async
 
function
 
GET
(
)
 
{

 
return
 
NextResponse
.
json
(
{

 
HELLO
: 
process
.
env
.
HELLO

 
}
)

}

SetDOTENV_PRIVATE_KEYin production before deploying.

Cloudflare Workers ⛅️

$ dotenvx encrypt -f .env.txt

// src/index.js

import
 
envSrc
 
from
 
'../.env.txt'

import
 
dotenvx
 
from
 
'@dotenvx/dotenvx'

const
 
config
 
=
 
dotenvx
.
config
(
{
 
envs
: 
[
{
 
type
: 
'env'
,
 
value
: 
envSrc
,
 
privateKeyName
: 
'DOTENV_PRIVATE_KEY'
 
}
]
 
}
)

const
 
envx
 
=
 
config
.
parsed

export
 
default
 
{

 
async
 
fetch
(
request
,
 
env
,
 
ctx
)
 
{

 
return
 
new
 
Response
(
`Hello 
${
envx
.
HELLO
}
`
)

 
}

}

"scripts"
: {
 
"deploy"
: 
"
wrangler deploy
"
,
 
"dev"
: 
"
wrangler dev --var $(dotenvx keypair -f .env.txt --format=colon)
"
,
 
"start"
: 
"
wrangler dev --var $(dotenvx keypair -f .env.txt --format=colon)
"
,
}

Bun 🥟

$ 
echo
 
"
HELLO=Test
"
 
>
 .env.test
$ 
echo
 
"
console.log('Hello ' + process.env.HELLO)
"
 
>
 index.js

$ bun index.js
Hello undefined

$ dotenvx run -f .env.test -- bun index.js
Hello Test

Deno 🦕

$ 
echo
 
"
HELLO=Dotenvx
"
 
>
 .env
$ 
echo
 
"
console.log('Hello ' + Deno.env.get('HELLO'))
"
 
>
 index.ts

$ deno run --allow-env index.ts
Hello undefined

$ dotenvx run -- deno run --allow-env index.ts
Hello Dotenvx

[!WARNING]
Some of you are attempting to use the npm module directly withdeno run. Don't, because deno currently has incomplete support for these encryption ciphers.

$ deno run -A npm:@dotenvx/dotenvx encrypt
Unknown cipher

Instead, usedotenvxas designed, by installing the cli as a binary - via curl, brew, etc.

Python 🐍

$ 
echo
 
"
HELLO=Dotenvx
"
 
>
 .env
$ 
echo
 
'
import os;print("Hello " + os.getenv("HELLO", ""))
'
 
>
 index.py

$ dotenvx run -- python3 index.py
Hello Dotenvx

seeextended python guide

PHP 🐘

$ 
echo
 
"
HELLO=Dotenvx
"
 
>
 .env
$ 
echo
 
'
<?php echo "Hello {$_SERVER["HELLO"]}\n";
'
 
>
 index.php

$ dotenvx run -- php index.php
Hello Dotenvx

seeextended php guide

Ruby 💎

$ 
echo
 
"
HELLO=Dotenvx
"
 
>
 .env
$ 
echo
 
'
puts "Hello #{ENV["HELLO"]}"
'
 
>
 index.rb

$ dotenvx run -- ruby index.rb
Hello Dotenvx

seeextended ruby guide

Go 🐹

$ 
echo
 
"
HELLO=Dotenvx
"
 
>
 .env
$ 
echo
 
'
package main; import ("fmt"; "os"); func main() { fmt.Printf("Hello %s\n", os.Getenv("HELLO")) }
'
 
>
 main.go

$ dotenvx run -- go run main.go
Hello Dotenvx

seeextended go guide

Rust 🦀

$ 
echo
 
"
HELLO=Dotenvx
"
 
>
 .env
$ 
echo
 
'
fn main() {let hello = std::env::var("HELLO").unwrap_or("".to_string());println!("Hello {hello}");}
'
 
>
 src/main.rs

$ dotenvx run -- cargo run
Hello Dotenvx

seeextended rust guide

Java ☕️

$ 
echo
 
"
HELLO=Dotenvx
"
 
>
 .env
$ 
echo
 
'
public class Index { public static void main(String[] args) { System.out.println("Hello " + System.getenv("HELLO")); } }
'
 
>
 index.java

$ dotenvx run -- java index.java
Hello Dotenvx

Clojure 🌿

$ 
echo
 
"
HELLO=Dotenvx
"
 
>
 .env
$ 
echo
 
'
(println "Hello" (System/getenv "HELLO"))
'
 
>
 index.clj

$ dotenvx run -- clojure -M index.clj
Hello Dotenvx

Kotlin 📐

$ 
echo
 
"
HELLO=Dotenvx
"
 
>
 .env
$ 
echo
 
'
fun main() { val hello = System.getenv("HELLO") ?: ""; println("Hello $hello") }
'
 
>
 index.kt
$ kotlinc index.kt -include-runtime -d index.jar

$ dotenvx run -- java -jar index.jar
Hello Dotenvx

.NET 🔵

$ dotnet new console -n HelloWorld -o HelloWorld
$ 
cd
 HelloWorld
$ 
echo
 
"
HELLO=Dotenvx
"
 
|
 Out-File -FilePath .env -Encoding utf8
$ 
echo
 
'
Console.WriteLine($"Hello {Environment.GetEnvironmentVariable("HELLO")}");
'
 
>
 Program.cs

$ dotenvx run -- dotnet run
Hello Dotenvx

Bash 🖥️

$ 
echo
 
"
HELLO=Dotenvx
"
 
>
 .env

$ dotenvx run --quiet -- sh -c 
'
echo Hello $HELLO
'

Hello Dotenvx

Fish 🐠

$ 
echo
 
"
HELLO=Dotenvx
"
 
>
 .env

$ dotenvx run --quiet -- sh -c 
'
echo Hello $HELLO
'

Hello Dotenvx

Cron ⏰

#
 run every day at 8am

0 8 
*
 
*
 
*
 dotenvx run -- /path/to/myscript.sh

Frameworks ▲

$ dotenvx run -- next dev
$ dotenvx run -- npm start
$ dotenvx run -- bin/rails s
$ dotenvx run -- php artisan serve

seeframework guides

Docker 🐳

$ docker run -it --rm -v 
$(
pwd
)
:/app dotenv/dotenvx run -- node index.js

Or in any image:

FROM
 node:latest

RUN
 echo 
"HELLO=Dotenvx"
 > .env && echo 
"console.log('Hello ' + process.env.HELLO)"
 > index.js

RUN
 curl -fsS https://dotenvx.sh/install.sh | sh

CMD
 [
"/usr/local/bin/dotenvx"
, 
"run"
, 
"--"
, 
"echo"
, 
"Hello $HELLO"
]

seedocker guide

CI/CDs 🐙

name
: 
build

on
: 
[push]

jobs
:
 
build
:
 
runs-on
: 
ubuntu-latest

 
steps
:
 - 
uses
: 
actions/checkout@v3

 - 
uses
: 
actions/setup-node@v3

 
with
:
 
node-version
: 
16

 - 
run
: 
curl -fsS https://dotenvx.sh/install.sh | sh

 - 
run
: 
dotenvx run -- node build.js

 
env
:
 
DOTENV_KEY
: 
${{ secrets.DOTENV_KEY }}

seegithub actions guide

Platforms

#
 heroku

heroku buildpacks:add https://github.com/dotenvx/heroku-buildpack-dotenvx

#
 docker

RUN curl -fsS https://dotenvx.sh 
|
 sh

#
 vercel

npm install @dotenvx/dotenvx --save

seeplatform guides

Process Managers

// pm2

"scripts"
: 
{

 
"start"
: 
"dotenvx run -- pm2-runtime start ecosystem.config.js --env production"

}
,

seeprocess manager guides

npx

#
 alternatively use npx

$ npx @dotenvx/dotenvx run -- node index.js
$ npx @dotenvx/dotenvx run -- next dev
$ npx @dotenvx/dotenvx run -- npm start

npm

$ npm install @dotenvx/dotenvx --save

{
 
"scripts"
: {
 
"start"
: 
"
./node_modules/.bin/dotenvx run -- node index.js
"

 },
 
"dependencies"
: {
 
"@dotenvx/dotenvx"
: 
"
^0.5.0
"

 }
}

$ npm run start

>
 start

>
 ./node_modules/.bin/dotenvx run -- node index.js

[dotenvx@1.X.X] injecting env (1) from .env.production
Hello Dotenvx

asdf

#
 use dotenvx with asdf

$ asdf plugin add dotenvx
$ asdf install dotenvx latest

thank you@jgburetof Paris 🇫🇷

Git

#
 use as a git submodule

$ git dotenvx run -- node index.js
$ git dotenvx run -- next dev
$ git dotenvx run -- npm start

Variable Expansion

Reference and expand variables already on your machine for use in your .env file.

#
 .env

USERNAME
=
"
username
"

DATABASE_URL
=
"
postgres://${USERNAME}@localhost/my_database
"

// index.js

console
.
log
(
'DATABASE_URL'
,
 
process
.
env
.
DATABASE_URL
)

$ dotenvx run --debug -- node index.js
[dotenvx@0.14.1] injecting env (2) from .env
DATABASE_URL postgres://username@localhost/my_database

Command Substitution

Add the output of a command to one of your variables in your .env file.

#
 .env

DATABASE_URL
=
"
postgres://$(whoami)@localhost/my_database
"

// index.js

console
.
log
(
'DATABASE_URL'
,
 
process
.
env
.
DATABASE_URL
)

$ dotenvx run --debug -- node index.js
[dotenvx@0.14.1] injecting env (1) from .env
DATABASE_URL postgres://yourusername@localhost/my_database

 

## Multiple Environments

Create a.env.productionfile and use-fto load it. It's straightforward, yet flexible.

$ 
echo
 
"
HELLO=production
"
 
>
 .env.production
$ 
echo
 
"
console.log('Hello ' + process.env.HELLO)
"
 
>
 index.js

$ dotenvx run -f .env.production -- node index.js
[dotenvx@1.X.X] injecting env (1) from .env.production
Hello production

>
 ^^

More examples

multiple `.env` files

$ 
echo
 
"
HELLO=local
"
 
>
 .env.local

$ 
echo
 
"
HELLO=Dotenvx
"
 
>
 .env

$ dotenvx run -f .env.local -f .env -- node index.js
[dotenvx@1.X.X] injecting env (1) from .env.local,.env
Hello 
local

Note subsequent files do NOT override pre-existing variables defined in previous files or env. This follows historic principle. For example, abovelocalwins – from the first file.

`--overload` flag

$ 
echo
 
"
HELLO=local
"
 
>
 .env.local

$ 
echo
 
"
HELLO=Dotenvx
"
 
>
 .env

$ dotenvx run -f .env.local -f .env --overload -- node index.js
[dotenvx@1.X.X] injecting env (1) from .env.local,.env
Hello Dotenvx

Note that with--overloadsubsequent files DO override pre-existing variables defined in previous files.

`--verbose` flag

$ 
echo
 
"
HELLO=production
"
 
>
 .env.production

$ dotenvx run -f .env.production --verbose -- node index.js
[dotenvx][verbose] injecting env from /path/to/.env.production
[dotenvx][verbose] HELLO 
set

[dotenvx@1.X.X] injecting env (1) from .env.production
Hello production

`--debug` flag

$ 
echo
 
"
HELLO=production
"
 
>
 .env.production

$ dotenvx run -f .env.production --debug -- node index.js
[dotenvx][debug] configuring options
[dotenvx][debug] {
"
envFile
"
:[
"
.env.production
"
]}
[dotenvx][verbose] injecting env from /path/to/.env.production
[dotenvx][debug] reading env from /path/to/.env.production
[dotenvx][debug] parsing env from /path/to/.env.production
[dotenvx][debug] {
"
HELLO
"
:
"
production
"
}
[dotenvx][debug] writing env from /path/to/.env.production
[dotenvx][verbose] HELLO 
set

[dotenvx][debug] HELLO 
set
 to production
[dotenvx@1.X.X] injecting env (1) from .env.production
Hello production

`--quiet` flag

Use--quietto suppress all output (except errors).

$ 
echo
 
"
HELLO=production
"
 
>
 .env.production

$ dotenvx run -f .env.production --quiet -- node index.js
Hello production

You can also setDOTENV_CONFIG_QUIET=true.

$ DOTENV_CONFIG_QUIET=true dotenvx run -f .env.production -- node index.js
Hello production

`--log-level` flag

Set--log-levelto whatever you wish. For example, to suppress warnings (risky), set log level toerror:

$ 
echo
 
"
HELLO=production
"
 
>
 .env.production

$ dotenvx run -f .env.production --log-level=error -- node index.js
Hello production

Available log levels areerror, warn, info, verbose, debug, silly

`--convention` flag

Load envs usingNext.js' conventionordotenv-flow convention. Set--conventiontonextjsorflow:

$ 
echo
 
"
HELLO=development local
"
 
>
 .env.development.local
$ 
echo
 
"
HELLO=local
"
 
>
 .env.local
$ 
echo
 
"
HELLO=development
"
 
>
 .env.development
$ 
echo
 
"
HELLO=env
"
 
>
 .env

$ dotenvx run --convention=nextjs -- node index.js
Hello development 
local

$ dotenvx run --convention=flow -- node index.js
Hello development 
local

(more conventions available upon request)

 

## Encryption

Add encryption to your.envfiles with a single command. Usedotenvx encrypt.

$ dotenvx encrypt
◈ encrypted (.env)

ADOTENV_PUBLIC_KEY(encryption key) and aDOTENV_PRIVATE_KEY(decryption key) are generated using the same public-key cryptography asBitcoin.

More examples

`.env`

$ 
echo
 
"
HELLO=Dotenvx
"
 
>
 .env
$ dotenvx encrypt
$ 
echo
 
"
console.log('Hello ' + process.env.HELLO)
"
 
>
 index.js

$ dotenvx run -- node index.js
[dotenvx@1.X.X] injecting env (2) from .env
Hello Dotenvx

`.env.production`

$ 
echo
 
"
HELLO=Production
"
 
>
 .env.production
$ dotenvx encrypt -f .env.production
$ 
echo
 
"
console.log('Hello ' + process.env.HELLO)
"
 
>
 index.js

$ DOTENV_PRIVATE_KEY_PRODUCTION=
"
<.env.production private key>
"
 dotenvx run -- node index.js
[dotenvx@1.X.X] injecting env (2) from .env.production
Hello Production

Note theDOTENV_PRIVATE_KEY_PRODUCTIONends with_PRODUCTION. This instructsdotenvx runto load the.env.productionfile.

`.env.ci`

$ 
echo
 
"
HELLO=Ci
"
 
>
 .env.ci
$ dotenvx encrypt -f .env.ci
$ 
echo
 
"
console.log('Hello ' + process.env.HELLO)
"
 
>
 index.js

$ DOTENV_PRIVATE_KEY_CI=
"
<.env.ci private key>
"
 dotenvx run -- node index.js
[dotenvx@1.X.X] injecting env (2) from .env.ci
Hello Ci

Note theDOTENV_PRIVATE_KEY_CIends with_CI. This instructsdotenvx runto load the.env.cifile. See the pattern?

combine multiple encrypted .env files

$ dotenvx 
set
 HELLO Dotenvx -f .env
$ dotenvx 
set
 HELLO Production -f .env.production
$ 
echo
 
"
console.log('Hello ' + process.env.HELLO)
"
 
>
 index.js

$ DOTENV_PRIVATE_KEY=
"
<.env private key>
"
 DOTENV_PRIVATE_KEY_PRODUCTION=
"
<.env.production private key>
"
 dotenvx run -- node index.js
[dotenvx@1.X.X] injecting env (3) from .env, .env.production
Hello Dotenvx

Note theDOTENV_PRIVATE_KEYinstructsdotenvx runto load the.envfile and theDOTENV_PRIVATE_KEY_PRODUCTIONinstructs it to load the.env.productionfile. See the pattern?

use directories with monorepos

Point-fat a directory to load the.envinside it. From a workspace, this makes a shared root.envavailable without repeating its filename.

my-monorepo/
 .env
 .env.keys
 apps/
 web/
 index.js

$ 
cd
 apps/web

$ dotenvx get HELLO -f ../..
World

$ dotenvx run -f ../.. -- node index.js
[dotenvx@1.X.X] injecting env (1) from ../../.env
Hello World

Encrypted values work without extra configuration when.env.keyssits beside the resolved.env.

The directory also becomes the base when using a convention:

$ dotenvx run -f ../.. --convention=nextjs -- node index.js
[dotenvx@1.X.X] injecting env (1) from ../../.env.development.local, ../../.env.local, ../../.env.development, ../../.env
Hello development 
local

If a workspace has its own.envbut shares the root.env.keys, point-fkat the root directory:

$ dotenvx run -f 
.
 -fk ../.. -- node index.js

`--stdout`

$ 
echo
 
"
HELLO=Dotenvx
"
 
>
 .env
$ dotenvx encrypt --stdout
$ dotenvx encrypt --stdout 
>
 .env.encrypted

other curves

secp256k1is a well-known and battle tested curve, in use with Bitcoin and other cryptocurrencies, but we are open to adding support for more curves.

If your organization's compliance department requiresNIST approved curvesor other curves likecurve25519, please reach out atsecurity@dotenvx.com.

agents

After encryption,DOTENV_PUBLIC_KEYlives in your encrypted.envfile. This means agents and automation can keep runningdotenvx setanddotenvx encryptwithout reading.env.keys.

$ chmod a-r .env.keys

$ dotenvx 
set
 HELLO World
◈ encrypted HELLO (.env)

$ dotenvx encrypt
◈ encrypted (.env)

Keep.env.keysunreadable by agents, while still letting them safely update encrypted values.

 

## Advanced

Become adotenvxpower user.

### CLI 📟

Advanced CLI commands.

`run` - Variable Expansion

Reference and expand variables already on your machine for use in your .env file.

#
 .env

USERNAME
=
"
username
"

DATABASE_URL
=
"
postgres://${USERNAME}@localhost/my_database
"

// index.js

console
.
log
(
'DATABASE_URL'
,
 
process
.
env
.
DATABASE_URL
)

$ dotenvx run --debug -- node index.js
[dotenvx@1.X.X] injecting env (2) from .env
DATABASE_URL postgres://username@localhost/my_database

`run` - Default Values

Use default values when environment variables are unset or empty.

#
 .env

#
 Default value syntax: use value if set, otherwise use default

DATABASE_HOST
=${DB_HOST:-localhost}

DATABASE_PORT
=${DB_PORT:-5432}

#
 Alternative syntax (no colon): use value if set, otherwise use default

API_URL
=${API_BASE_URL-https://api.example.com}

// index.js

console
.
log
(
'DATABASE_HOST'
,
 
process
.
env
.
DATABASE_HOST
)

console
.
log
(
'DATABASE_PORT'
,
 
process
.
env
.
DATABASE_PORT
)

console
.
log
(
'API_URL'
,
 
process
.
env
.
API_URL
)

$ dotenvx run --debug -- node index.js
[dotenvx@1.X.X] injecting env (3) from .env
DATABASE_HOST localhost
DATABASE_PORT 5432
API_URL https://api.example.com

`run` - Alternate Values

Use alternate values when environment variables are set and non-empty.

#
 .env

NODE_ENV
=production

#
 Alternate value syntax: use alternate if set and non-empty, otherwise empty

DEBUG_MODE
=${NODE_ENV:+false}

LOG_LEVEL
=${NODE_ENV:+error}

#
 Alternative syntax (no colon): use alternate if set, otherwise empty 

CACHE_ENABLED
=${NODE_ENV+true}

// index.js

console
.
log
(
'NODE_ENV'
,
 
process
.
env
.
NODE_ENV
)

console
.
log
(
'DEBUG_MODE'
,
 
process
.
env
.
DEBUG_MODE
)

console
.
log
(
'LOG_LEVEL'
,
 
process
.
env
.
LOG_LEVEL
)

console
.
log
(
'CACHE_ENABLED'
,
 
process
.
env
.
CACHE_ENABLED
)

$ dotenvx run --debug -- node index.js
[dotenvx@1.X.X] injecting env (4) from .env
NODE_ENV production
DEBUG_MODE 
false

LOG_LEVEL error
CACHE_ENABLED 
true

`run` - Interpolation Syntax Summary (Variable Expansion, Default/Alternate Values)

Complete reference for variable interpolation patterns supported by dotenvx:

#
 .env

DEFINED_VAR
=hello

EMPTY_VAR
=

#
 UNDEFINED_VAR is not set

#
 Default value syntax - use variable if set/non-empty, otherwise use default

TEST1
=${DEFINED_VAR:-fallback} 
#
 Result: "hello"

TEST2
=${EMPTY_VAR:-fallback} 
#
 Result: "fallback" 

TEST3
=${UNDEFINED_VAR:-fallback} 
#
 Result: "fallback"

#
 Default value syntax (no colon) - use variable if set, otherwise use default

TEST4
=${DEFINED_VAR-fallback} 
#
 Result: "hello"

TEST5
=${EMPTY_VAR-fallback} 
#
 Result: "" (empty, but set)

TEST6
=${UNDEFINED_VAR-fallback} 
#
 Result: "fallback"

#
 Alternate value syntax - use alternate if variable is set/non-empty, otherwise empty

TEST7
=${DEFINED_VAR:+alternate} 
#
 Result: "alternate"

TEST8
=${EMPTY_VAR:+alternate} 
#
 Result: "" (empty)

TEST9
=${UNDEFINED_VAR:+alternate} 
#
 Result: "" (empty)

#
 Alternate value syntax (no colon) - use alternate if variable is set, otherwise empty 

TEST10
=${DEFINED_VAR+alternate} 
#
 Result: "alternate"

TEST11
=${EMPTY_VAR+alternate} 
#
 Result: "alternate" (empty but set)

TEST12
=${UNDEFINED_VAR+alternate} 
#
 Result: "" (empty)

Key differences:

* :-vs-: The colon makes empty values trigger the fallback
* :+vs+: The colon makes empty values not trigger the alternate
* Default syntax (-): Use variable value or fallback
* Alternate syntax (+): Use alternate value or empty string

`run` - Command Substitution

Add the output of a command to one of your variables in your .env file.

#
 .env

DATABASE_URL
=
"
postgres://$(whoami)@localhost/my_database
"

// index.js

console
.
log
(
'DATABASE_URL'
,
 
process
.
env
.
DATABASE_URL
)

$ dotenvx run --debug -- node index.js
[dotenvx@1.X.X] injecting env (1) from .env
DATABASE_URL postgres://yourusername@localhost/my_database

`run` - Shell Expansion

Prevent your shell from expanding inline$VARIABLESbefore dotenvx has a chance to inject it. Use a subshell.

$ dotenvx run --env=
"
HELLO=Dotenvx
"
 -- sh -c 
'
echo Hello $HELLO
'

Hello Dotenvx

`run` - Multiline

Dotenvx supports multiline values. This is particularly useful in conjunction with Docker - whichdoes not support multiline values.

#
 .env

MULTILINE_PEM
=
"
-----BEGIN PUBLIC KEY-----

MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAnNl1tL3QjKp3DZWM0T3u

LgGJQwu9WqyzHKZ6WIA5T+7zPjO1L8l3S8k8YzBrfH4mqWOD1GBI8Yjq2L1ac3Y/

bTdfHN8CmQr2iDJC0C6zY8YV93oZB3x0zC/LPbRYpF8f6OqX1lZj5vo2zJZy4fI/

kKcI5jHYc8VJq+KCuRZrvn+3V+KuL9tF9v8ZgjF2PZbU+LsCy5Yqg1M8f5Jp5f6V

u4QuUoobAgMBAAE=

-----END PUBLIC KEY-----
"

// index.js

console
.
log
(
'MULTILINE_PEM'
,
 
process
.
env
.
MULTILINE_PEM
)

$ dotenvx run -- node index.js
MULTILINE_PEM -----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAnNl1tL3QjKp3DZWM0T3u
LgGJQwu9WqyzHKZ6WIA5T+7zPjO1L8l3S8k8YzBrfH4mqWOD1GBI8Yjq2L1ac3Y/
bTdfHN8CmQr2iDJC0C6zY8YV93oZB3x0zC/LPbRYpF8f6OqX1lZj5vo2zJZy4fI/
kKcI5jHYc8VJq+KCuRZrvn+3V+KuL9tF9v8ZgjF2PZbU+LsCy5Yqg1M8f5Jp5f6V
u4QuUoobAgMBAAE=
-----END PUBLIC KEY-----

`run` - Contextual Help

Unlike other dotenv libraries, dotenvx attempts to unblock you with contextual help.

For example, when missing a custom .env file:

$ dotenvx run -f .env.missing -- 
echo
 
$HELLO

[MISSING_ENV_FILE] missing file (/Users/scottmotte/Code/dotenvx/playground/apr-16/.env.missing). fix: [echo 
"
HELLO=Dotenvx
"
 
>
 .env.missing]

or when missing a KEY:

$ 
echo
 
"
HELLO=Dotenvx
"
 
>
 .env
$ dotenvx get GOODBYE
[MISSING_KEY] missing key (GOODBYE)

`run -f `

Run a command using the.envfile in a directory. This is useful with monorepos.

$ dotenvx run -f ../.. -- node index.js
[dotenvx@1.X.X] injecting env (1) from ../../.env
Hello World

`run` - multiple `-f` flags

Compose multiple.envfiles for environment variables loading, as you need.

$ 
echo
 
"
HELLO=local
"
 
>
 .env.local
$ 
echo
 
"
HELLO=Dotenvx
"
 
>
 .env
$ 
echo
 
"
console.log('Hello ' + process.env.HELLO)
"
 
>
 index.js

$ dotenvx run -f .env.local -f .env -- node index.js
[dotenvx@1.X.X] injecting env (1) from .env.local, .env
Hello 
local

Note subsequent files do NOT override pre-existing variables defined in previous files or env. This follows historic principle. For example, abovelocalwins – from the first file.

`run --env HELLO=String`

Set environment variables as a simpleKEY=valuestring pair.

$ 
echo
 
"
HELLO=Dotenvx
"
 
>
 .env
$ 
echo
 
"
console.log('Hello ' + process.env.HELLO)
"
 
>
 index.js

$ dotenvx run --env HELLO=String -f .env -- node index.js
[dotenvx@1.X.X] injecting env (1) from .env, and --env flag
Hello String

`run --overload`

Override existing env variables. These can be variables already on your machine or variables loaded as files consecutively. The last variable seen will 'win'.

$ 
echo
 
"
HELLO=local
"
 
>
 .env.local
$ 
echo
 
"
HELLO=Dotenvx
"
 
>
 .env
$ 
echo
 
"
console.log('Hello ' + process.env.HELLO)
"
 
>
 index.js

$ dotenvx run -f .env.local -f .env --overload -- node index.js
[dotenvx@1.X.X] injecting env (1) from .env.local, .env
Hello Dotenvx

Note that with--overloadsubsequent files DO override pre-existing variables defined in previous files.

`run` - Environment Variable Precedence (Container/Cloud Deployments)

When deploying applications in containers or cloud environments, you often need to override specific environment variables at runtime without modifying committed.envfiles. By default, dotenvx follows the historic dotenv principle:environment variables already present take precedence over.envfiles.

#
 .env.prod contains: MODEL_REGISTRY=registry.company.com/models/v1

$ 
echo
 
"
MODEL_REGISTRY=registry.company.com/models/v1
"
 
>
 .env.prod
$ 
echo
 
"
console.log('MODEL_REGISTRY:', process.env.MODEL_REGISTRY)
"
 
>
 app.js

#
 Without environment variable set - uses .env.prod value

$ dotenvx run -f .env.prod -- node app.js
MODEL_REGISTRY: registry.company.com/models/v1

#
 With environment variable set (e.g., via Azure Container Service) - environment variable takes precedence

$ MODEL_REGISTRY=registry.azure.com/models/v2 dotenvx run -f .env.prod -- node app.js
MODEL_REGISTRY: registry.azure.com/models/v2

#
 To force .env.prod to override environment variables, use --overload

$ MODEL_REGISTRY=registry.azure.com/models/v2 dotenvx run -f .env.prod --overload -- node app.js
MODEL_REGISTRY: registry.company.com/models/v1

For container deployments:Set environment variables through your cloud provider's UI/configuration (Azure Container Service, AWS ECS, etc.) to override specific values from committed.envfiles without rebuilding your application.

`DOTENV_PRIVATE_KEY=key run`

Decrypt your encrypted.envby settingDOTENV_PRIVATE_KEYbeforedotenvx run.

$ touch .env
$ dotenvx 
set
 HELLO encrypted
$ 
echo
 
"
console.log('Hello ' + process.env.HELLO)
"
 
>
 index.js

#
 check your .env.keys files for your privateKey

$ DOTENV_PRIVATE_KEY=
"
122...0b8
"
 dotenvx run -- node index.js
[dotenvx@1.X.X] injecting env (2) from .env
Hello encrypted

`DOTENV_PRIVATE_KEY_PRODUCTION=key run`

Decrypt your encrypted.env.productionby settingDOTENV_PRIVATE_KEY_PRODUCTIONbeforedotenvx run. Alternatively, this can be already set on your server or cloud provider.

$ touch .env.production
$ dotenvx 
set
 HELLO 
"
production encrypted
"
 -f .env.production
$ 
echo
 
"
console.log('Hello ' + process.env.HELLO)
"
 
>
 index.js

#
 check .env.keys for your privateKey

$ DOTENV_PRIVATE_KEY_PRODUCTION=
"
122...0b8
"
 dotenvx run -- node index.js
[dotenvx@1.X.X] injecting env (2) from .env.production
Hello production encrypted

Note theDOTENV_PRIVATE_KEY_PRODUCTIONends with_PRODUCTION. This instructs dotenvx run to load the.env.productionfile.

`DOTENV_PRIVATE_KEY_CI=key dotenvx run`

Decrypt your encrypted.env.ciby settingDOTENV_PRIVATE_KEY_CIbeforedotenvx run. Alternatively, this can be already set on your server or cloud provider.

$ touch .env.ci
$ dotenvx 
set
 HELLO 
"
ci encrypted
"
 -f .env.ci
$ 
echo
 
"
console.log('Hello ' + process.env.HELLO)
"
 
>
 index.js

#
 check .env.keys for your privateKey

$ DOTENV_PRIVATE_KEY_CI=
"
122...0b8
"
 dotenvx run -- node index.js
[dotenvx@1.X.X] injecting env (2) from .env.ci
Hello ci encrypted

Note theDOTENV_PRIVATE_KEY_CIends with_CI. This instructs dotenvx run to load the.env.cifile. See the pattern?

`DOTENV_PRIVATE_KEY=key DOTENV_PRIVATE_KEY_PRODUCTION=key run` - Combine Multiple

Decrypt your encrypted.envand.env.productionfiles by settingDOTENV_PRIVATE_KEYandDOTENV_PRIVATE_KEY_PRODUCTIONbeforedotenvx run.

$ touch .env
$ touch .env.production
$ dotenvx 
set
 HELLO encrypted
$ dotenvx 
set
 HELLO 
"
production encrypted
"
 -f .env.production
$ 
echo
 
"
console.log('Hello ' + process.env.HELLO)
"
 
>
 index.js

#
 check .env.keys for your privateKeys

$ DOTENV_PRIVATE_KEY=
"
122...0b8
"
 DOTENV_PRIVATE_KEY_PRODUCTION=
"
122...0b8
"
 dotenvx run -- node index.js
[dotenvx@1.X.X] injecting env (3) from .env, .env.production
Hello encrypted

$ DOTENV_PRIVATE_KEY_PRODUCTION=
"
122...0b8
"
 DOTENV_PRIVATE_KEY=
"
122...0b8
"
 dotenvx run -- node index.js
[dotenvx@1.X.X] injecting env (3) from .env.production, .env
Hello production encrypted

Compose any encrypted files you want this way. As long as aDOTENV_PRIVATE_KEY_${environment}is set, the values from.env.${environment}will be decrypted at runtime.

`run --verbose`

Set log level toverbose. (log levels)

$ 
echo
 
"
HELLO=production
"
 
>
 .env.production
$ 
echo
 
"
console.log('Hello ' + process.env.HELLO)
"
 
>
 index.js

$ dotenvx run -f .env.production --verbose -- node index.js
loading env from .env.production (/path/to/.env.production)
HELLO 
set

[dotenvx@1.X.X] injecting env (1) from .env.production
Hello production

`run --debug`

Set log level todebug. (log levels)

$ 
echo
 
"
HELLO=production
"
 
>
 .env.production
$ 
echo
 
"
console.log('Hello ' + process.env.HELLO)
"
 
>
 index.js

$ dotenvx run -f .env.production --debug -- node index.js
process 
command
 [node index.js]
options: {
"
env
"
:[],
"
envFile
"
:[
"
.env.production
"
]}
loading env from .env.production (/path/to/.env.production)
{
"
HELLO
"
:
"
production
"
}
HELLO 
set

HELLO 
set
 to production
[dotenvx@1.X.X] injecting env (1) from .env.production
executing process 
command
 [node index.js]
expanding process 
command
 to [/opt/homebrew/bin/node index.js]
Hello production

`run --quiet`

Use--quietto suppress all output (except errors). (log levels)

$ 
echo
 
"
HELLO=production
"
 
>
 .env.production
$ 
echo
 
"
console.log('Hello ' + process.env.HELLO)
"
 
>
 index.js

$ dotenvx run -f .env.production --quiet -- node index.js
Hello production

You can also setDOTENV_CONFIG_QUIET=true.

$ DOTENV_CONFIG_QUIET=true dotenvx run -f .env.production -- node index.js
Hello production

`run --log-level`

Set--log-levelto whatever you wish. For example, to suppress warnings (risky), set log level toerror:

$ 
echo
 
"
HELLO=production
"
 
>
 .env.production
$ 
echo
 
"
console.log('Hello ' + process.env.HELLO)
"
 
>
 index.js

$ dotenvx run -f .env.production --log-level=error -- node index.js
Hello production

Available log levels areerror, warn, info, verbose, debug, silly(source)

`run --strict`

Exit with code1if any errors are encountered - like a missing .env file or decryption failure.

$ 
echo
 
"
console.log('Hello ' + process.env.HELLO)
"
 
>
 index.js

$ dotenvx run -f .env.missing --strict -- node index.js
[MISSING_ENV_FILE] missing file (/path/to/.env.missing). fix: [echo 
"
HELLO=Dotenvx
"
 
>
 .env.missing]

This can be useful inciscripts where you want to fail the ci if your.envfile could not be decrypted at runtime.

`run --ignore`

Ignore errors likeMISSING_ENV_FILE.

$ 
echo
 
"
console.log('Hello ' + process.env.HELLO)
"
 
>
 index.js

$ dotenvx run -f .env.missing --ignore=MISSING_ENV_FILE -- node index.js
...

`run --convention=nextjs`

Load envs usingNext.js' convention. Set--conventiontonextjs:

$ 
echo
 
"
HELLO=development local
"
 
>
 .env.development.local
$ 
echo
 
"
HELLO=local
"
 
>
 .env.local
$ 
echo
 
"
HELLO=development
"
 
>
 .env.development
$ 
echo
 
"
HELLO=env
"
 
>
 .env
$ 
echo
 
"
console.log('Hello ' + process.env.HELLO)
"
 
>
 index.js

$ dotenvx run --convention=nextjs -- node index.js
[dotenvx@1.X.X] injecting env (1) from .env.development.local, .env.local, .env.development, .env
Hello development 
local

You can also setDOTENV_CONFIG_CONVENTION=nextjs.

$ DOTENV_CONFIG_CONVENTION=nextjs dotenvx run -- node index.js
[dotenvx@1.X.X] injecting env (1) from .env.development.local, .env.local, .env.development, .env
Hello development 
local

(more conventions available upon request)

`run -f --convention=nextjs`

Run a command using Next.js' convention from a directory. This is useful with monorepos.

$ dotenvx run -f ../.. --convention=nextjs -- node index.js
[dotenvx@1.X.X] injecting env (1) from ../../.env.development.local, ../../.env.local, ../../.env.development, ../../.env
Hello development 
local

`run --convention=flow`

Load envs usingdotenv-flow's convention. Set--conventiontoflow:

$ 
echo
 
"
HELLO=development local
"
 
>
 .env.development.local
$ 
echo
 
"
HELLO=development
"
 
>
 .env.development
$ 
echo
 
"
HELLO=local
"
 
>
 .env.local
$ 
echo
 
"
HELLO=env
"
 
>
 .env
$ 
echo
 
"
console.log('Hello ' + process.env.HELLO)
"
 
>
 index.js

$ NODE_ENV=development dotenvx run --convention=flow -- node index.js 
[dotenvx@1.X.X] injecting env (1) from .env.development.local, .env.development, .env.local, .env
Hello development 
local

You can also setDOTENV_CONFIG_CONVENTION=flow.

$ NODE_ENV=development DOTENV_CONFIG_CONVENTION=flow dotenvx run -- node index.js
[dotenvx@1.X.X] injecting env (1) from .env.development.local, .env.development, .env.local, .env
Hello development 
local

Further, we recommend usingDOTENV_ENVoverNODE_ENV– asdotenvxworks everywhere, not just node.

$ DOTENV_ENV=development dotenvx run --convention=flow -- node index.js 
[dotenvx@1.X.X] injecting env (1) from .env.development.local, .env.development, .env.local, .env
Hello development 
local

`run -fk`

Specify path to.env.keys. This is useful with monorepos.

$ mkdir -p apps/app1
$ touch apps/app1/.env
$ dotenvx 
set
 HELLO Dotenvx -fk .env.keys -f apps/app1/.env

$ dotenvx run -fk .env.keys -f apps/app1/.env -- yourcommand

`run --token`

Set Armor ⛨ token for retrieving armored private keys.

$ dotenvx run --token 
"
$DOTENVX_ARMOR_TOKEN
"
 -- yourcommand

`run --no-native`

Turn off OS secret store lookups.

$ dotenvx run --no-native -- yourcommand

`run --no-armor`

Turn offDotenvx Armor ⛨features.

$ dotenvx run --no-armor -- yourcommand

`get KEY`

Return a single environment variable's value.

$ 
echo
 
"
HELLO=Dotenvx
"
 
>
 .env

$ dotenvx get HELLO
World

`get KEY --no-native`

Turn off OS secret store lookups for get.

$ dotenvx get HELLO --no-native

`get KEY -f`

Return a single environment variable's value from a specific.envfile.

$ 
echo
 
"
HELLO=Dotenvx
"
 
>
 .env
$ 
echo
 
"
HELLO=production
"
 
>
 .env.production

$ dotenvx get HELLO -f .env.production
production

`get KEY -f `

Return a single environment variable's value from the.envfile in a directory. This is useful with monorepos.

$ dotenvx get HELLO -f ../..
World

`get KEY -fk`

Specify path to.env.keys. This is useful with monorepos.

$ mkdir -p apps/app1
$ touch apps/app1/.env
$ dotenvx 
set
 HELLO Dotenvx -fk .env.keys -f apps/app1/.env

$ dotenvx get HELLO -fk .env.keys -f apps/app1/.env
world

`get KEY --env`

Return a single environment variable's value from a--envstring.

$ dotenvx get HELLO --env HELLO=String -f .env.production
String

`get KEY --overload`

Return a single environment variable's value where each found value is overloaded.

$ 
echo
 
"
HELLO=Dotenvx
"
 
>
 .env
$ 
echo
 
"
HELLO=production
"
 
>
 .env.production

$ dotenvx get HELLO -f .env.production --env HELLO=String -f .env --overload
World

`get KEY --strict`

Exit with code1if any errors are encountered - like a missing key, missing .env file, or decryption failure.

$ dotenvx get DOES_NOT_EXIST --strict
[MISSING_KEY] missing key (DOES_NOT_EXIST)

`get KEY --convention=nextjs`

Return a single environment variable's value usingNext.js' convention. Set--conventiontonextjs:

$ 
echo
 
"
HELLO=development local
"
 
>
 .env.development.local
$ 
echo
 
"
HELLO=local
"
 
>
 .env.local
$ 
echo
 
"
HELLO=development
"
 
>
 .env.development
$ 
echo
 
"
HELLO=env
"
 
>
 .env
$ 
echo
 
"
console.log('Hello ' + process.env.HELLO)
"
 
>
 index.js

$ dotenvx get HELLO --convention=nextjs
development 
local

You can also setDOTENV_CONFIG_CONVENTION=nextjs.

$ DOTENV_CONFIG_CONVENTION=nextjs dotenvx get HELLO
development 
local

`get KEY -f --convention=nextjs`

Return a single environment variable's value using Next.js' convention from a directory. This is useful with monorepos.

$ dotenvx get HELLO -f ../.. --convention=nextjs
development 
local

`get KEY --convention=flow`

Return a single environment variable's value usingdotenv-flow's convention. Set--conventiontoflow:

$ 
echo
 
"
HELLO=development local
"
 
>
 .env.development.local
$ 
echo
 
"
HELLO=development
"
 
>
 .env.development
$ 
echo
 
"
HELLO=local
"
 
>
 .env.local
$ 
echo
 
"
HELLO=env
"
 
>
 .env
$ 
echo
 
"
console.log('Hello ' + process.env.HELLO)
"
 
>
 index.js

$ NODE_ENV=development dotenvx get HELLO --convention=flow
development 
local

You can also setDOTENV_CONFIG_CONVENTION=flow.

$ NODE_ENV=development DOTENV_CONFIG_CONVENTION=flow dotenvx get HELLO
development 
local

Further, we recommend usingDOTENV_ENVoverNODE_ENV– asdotenvxworks everywhere, not just node.

$ DOTENV_ENV=development dotenvx get HELLO --convention=flow
development 
local

`get` (json)

Return a json response of all key/value pairs in a.envfile.

$ 
echo
 
"
HELLO=Dotenvx
"
 
>
 .env

$ dotenvx get
{
"
HELLO
"
:
"
Dotenvx
"
}

`get --format shell`

Return a shell formatted response of all key/value pairs in a.envfile.

$ 
echo
 
"
HELLO=Dotenvx
"
 
>
 .env
$ 
echo
 
"
KEY=value
"
 
>>
 .env

$ dotenvx get --format shell
HELLO=Dotenvx KEY=value

This can be useful when combined withenvon the command line.

$ echo "console.log('Hello ' + process.env.KEY + ' ' + process.env.HELLO)" > index.js
$ env $(dotenvx get --format=shell) node index.js
Hello value World

or withexport.

$ echo "console.log('Hello ' + process.env.KEY + ' ' + process.env.HELLO)" > index.js
$ export $(dotenvx get --format=shell)
$ node index.js
Hello value World

`get --format eval`

Return aneval-ready shell formatted response of all key/value pairs in a.envfile.

$ 
echo
 
"
HELLO=Dotenvx
"
 
>
 .env
$ 
echo
 
"
KEY=value
"
 
>>
 .env

$ dotenvx get --format 
eval

HELLO=
"
Dotenvx
"

KEY=
"
value
"

Note that this exports newlines and quoted strings.

This can be useful for more complex .env values (spaces, escaped characters, quotes, etc) combined withevalon the command line.

$ 
echo
 
"
console.log('Hello ' + process.env.KEY + ' ' + process.env.HELLO)
"
 
>
 index.js
$ 
eval
 
$(
dotenvx get --format=eval
)
 node index.js
Hello value World

Be careful withevalas it allows for arbitrary execution of commands. Preferdotenvx run --but in some casesevalis a sharp knife that is useful to have.

`get --all`

Return preset machine envs as well.

$ 
echo
 
"
HELLO=Dotenvx
"
 
>
 .env

$ dotenvx get --all
{
"
PWD
"
:
"
/some/file/path
"
,
"
USER
"
:
"
username
"
,
"
LIBRARY_PATH
"
:
"
/usr/local/lib
"
, ..., 
"
HELLO
"
:
"
Dotenvx
"
}

`get --all --pretty-print`

Make the output more readable - pretty print it.

$ 
echo
 
"
HELLO=Dotenvx
"
 
>
 .env

$ dotenvx get --all --pretty-print
{
 
"
PWD
"
: 
"
/some/filepath
"
,
 
"
USER
"
: 
"
username
"
,
 
"
LIBRARY_PATH
"
: 
"
/usr/local/lib
"
,
 ...,
 
"
HELLO
"
: 
"
Dotenvx
"

}

`set KEY value`

Set an encrypted key/value (on by default).

$ touch .env

$ dotenvx 
set
 HELLO Dotenvx

set
 HELLO with encryption (.env)

Works with unreadable.env.keyswhen.envalready containsDOTENV_PUBLIC_KEY.

`set KEY value -f`

Set an (encrypted) key/value for another.envfile.

$ touch .env.production

$ dotenvx 
set
 HELLO production -f .env.production

set
 HELLO with encryption (.env.production)

`set KEY value -fk`

Specify path to.env.keys. This is useful with monorepos.

$ mkdir -p apps/app1
$ touch apps/app1/.env

$ dotenvx 
set
 HELLO Dotenvx -fk .env.keys -f apps/app1/.env

set
 HELLO with encryption (.env)

Put it to use.

$ dotenvx get -fk .env.keys -f apps/app1/.env

Use it with a relative path.

$ 
cd
 apps/app1
$ dotenvx get -fk ../../.env.keys -f .env

`set KEY "value with spaces"`

Set a value containing spaces.

$ touch .env.ci

$ dotenvx 
set
 HELLO 
"
my ci
"
 -f .env.ci

set
 HELLO with encryption (.env.ci)

`set KEY -- "- + * ÷"`

If your value starts with a dash (-), then place two dashes instructing the cli that there are no more flag arguments.

$ touch .env.ci

$ dotenvx 
set
 HELLO -f .env.ci -- 
"
- + * ÷
"

set
 HELLO with encryption (.env.ci)

`set KEY value --plain`

Set a plaintext key/value.

$ touch .env

$ dotenvx 
set
 HELLO Dotenvx --plain

set
 HELLO (.env)

`set KEY_PLAIN value`

Set a plaintext key/value inside an encrypted.envfile by ending the key with_PLAIN.

$ touch .env

$ dotenvx 
set
 HELLO_PLAIN Dotenvx

set
 HELLO_PLAIN (.env)

Keys ending in_PLAINare not encrypted bydotenvx setordotenvx encrypt.

`set KEY value --no-native`

Turn off OS secret store lookups for set.

$ dotenvx 
set
 HELLO Dotenvx --no-native

`encrypt`

Encrypt the contents of a.envfile to an encrypted.envfile.

$ 
echo
 
"
HELLO=Dotenvx
"
 
>
 .env

$ dotenvx encrypt
◈ encrypted (.env) + 
local
 key (.env.keys)
⮕ next run [dotenvx gitignore --pattern .env.keys] to gitignore .env.keys
⮕ next run [DOTENV_PRIVATE_KEY
=
'
122...0b8
'
 dotenvx run -- yourcommand] to 
test
 decryption locally

Works with unreadable.env.keyswhen.envalready containsDOTENV_PUBLIC_KEY.

`encrypt -f`

Encrypt the contents of a specified.envfile to an encrypted.envfile.

$ 
echo
 
"
HELLO=Dotenvx
"
 
>
 .env
$ 
echo
 
"
HELLO=Production
"
 
>
 .env.production

$ dotenvx encrypt -f .env.production
◈ encrypted (.env.production) + 
local
 key (.env.keys)
⮕ next run [dotenvx gitignore --pattern .env.keys] to gitignore .env.keys
⮕ next run [DOTENV_PRIVATE_KEY
=
'
bff...bc4
'
 dotenvx run -- yourcommand] to 
test
 decryption locally

`encrypt --no-native`

Turn off OS secret store lookups for encrypt.

$ dotenvx encrypt --no-native
◈ encrypted (.env)

`encrypt --no-armor`

Turn offDotenvx Armor ⛨features for encrypt.

$ dotenvx encrypt --no-armor
◈ encrypted (.env)

`encrypt -fk`

Specify path to.env.keys. This is useful with monorepos.

$ mkdir -p apps/app1
$ 
echo
 
"
HELLO=Dotenvx
"
 
>
 apps/app1/.env

$ dotenvx encrypt -fk .env.keys -f apps/app1/.env
◈ encrypted (apps/app1/.env)

Put it to use.

$ dotenvx run -fk .env.keys -f apps/app1/.env

Use with a relative path.

$ 
cd
 apps/app1
$ dotenvx run -fk ../../.env.keys -f .env

`encrypt -k`

Specify the key(s) to encrypt by passing--key.

$ 
echo
 
"
HELLO=Dotenvx\nHELLO2=Universe
"
 
>
 .env

$ dotenvx encrypt -k HELLO2
◈ encrypted (.env)

Even specify a glob pattern.

$ 
echo
 
"
HELLO=Dotenvx\nHOLA=Mundo
"
 
>
 .env

$ dotenvx encrypt -k 
"
HE*
"

◈ encrypted (.env)

`encrypt -ek`

Specify the key(s) to NOT encrypt by passing--exclude-key.

$ 
echo
 
"
HELLO=Dotenvx\nHELLO2=Universe
"
 
>
 .env

$ dotenvx encrypt -ek HELLO
◈ encrypted (.env)

Even specify a glob pattern.

$ 
echo
 
"
HELLO=Dotenvx\nHOLA=Mundo
"
 
>
 .env

$ dotenvx encrypt -ek 
"
HO*
"

◈ encrypted (.env)

`encrypt KEY_PLAIN`

Skip encryption for keys ending in_PLAIN.

$ 
echo
 
"
HELLO=Dotenvx\nHELLO_PLAIN=visible
"
 
>
 .env

$ dotenvx encrypt
◈ encrypted (.env)

HELLOis encrypted.HELLO_PLAINstays plaintext.

`encrypt --stdout`

Encrypt the contents of a.envfile and send to stdout.

$ 
echo
 
"
HELLO=Dotenvx
"
 
>
 .env
$ dotenvx encrypt --stdout

#
/-------------------[DOTENV_PUBLIC_KEY]--------------------/

#
/ public-key encryption for .env files /

#
/ [how it works](https://dotenvx.com/encryption) /

#
/----------------------------------------------------------/

DOTENV_PUBLIC_KEY=
"
034af93e93708b994c10f236c96ef88e47291066946cce2e8d98c9e02c741ced45
"

#
 .env

HELLO=
"
encrypted:BDqDBibm4wsYqMpCjTQ6BsDHmMadg9K3dAt+Z9HPMfLEIRVz50hmLXPXRuDBXaJi/LwWYEVUNiq0HISrslzQPaoyS8Lotg3gFWJTsNCdOWnqpjF2xNUX2RQiP05kAbEXM6MWVjDr
"

or send to a file:

$ 
echo
 
"
HELLO=Dotenvx
"
 
>
 .env
$ dotenvx encrypt --stdout 
>
 somefile.txt

`decrypt`

Decrypt the contents of an encrypted.envfile to an unencrypted.envfile.

$ 
echo
 
"
HELLO=Dotenvx
"
 
>
 .env
$ dotenvx encrypt
◈ encrypted (.env)
$ dotenvx decrypt
◇ decrypted (.env)

`decrypt --no-native`

Turn off OS secret store lookups for decrypt.

$ dotenvx decrypt --no-native
◇ decrypted (.env)

`decrypt -f`

Decrypt the contents of a specified encrypted.envfile to an unencrypted.envfile.

$ 
echo
 
"
HELLO=Dotenvx
"
 
>
 .env
$ 
echo
 
"
HELLO=Production
"
 
>
 .env.production

$ dotenvx encrypt -f .env.production
◈ encrypted (.env.production)
$ dotenvx decrypt -f .env.production
◇ decrypted (.env.production)

`decrypt -fk`

Specify path to.env.keys. This is useful with monorepos.

$ mkdir -p apps/app1
$ 
echo
 
"
HELLO=Dotenvx
"
 
>
 apps/app1/.env

$ dotenvx encrypt -fk .env.keys -f apps/app1/.env
◈ encrypted (apps/app1/.env)
$ dotenvx decrypt -fk .env.keys -f apps/app1/.env
◇ decrypted (apps/app1/.env)

`decrypt -k`

Decrypt the contents of a specified key inside an encrypted.envfile.

$ 
echo
 
"
HELLO=Dotenvx\nHOLA=Mundo
"
 
>
 .env
$ dotenvx encrypt
◈ encrypted (.env)
$ dotenvx decrypt -k HELLO
◇ decrypted (.env)

Even specify a glob pattern.

$ 
echo
 
"
HELLO=Dotenvx\nHOLA=Mundo
"
 
>
 .env
$ dotenvx encrypt
◈ encrypted (.env)
$ dotenvx decrypt -k 
"
HE*
"

◇ decrypted (.env)

`decrypt -ek`

Decrypt the contents inside an encrypted.envfile except for an excluded key.

$ 
echo
 
"
HELLO=Dotenvx\nHOLA=Mundo
"
 
>
 .env
$ dotenvx encrypt
◈ encrypted (.env)
$ dotenvx decrypt -ek HOLA
◇ decrypted (.env)

Even specify a glob pattern.

$ 
echo
 
"
HELLO=Dotenvx\nHOLA=Mundo
"
 
>
 .env
$ dotenvx encrypt
◈ encrypted (.env)
$ dotenvx decrypt -ek 
"
HO*
"

◇ decrypted (.env)

`decrypt --stdout`

Decrypt the contents of an encrypted.envfile and send to stdout.

$ dotenvx decrypt --stdout

#
/-------------------[DOTENV_PUBLIC_KEY]--------------------/

#
/ public-key encryption for .env files /

#
/ [how it works](https://dotenvx.com/encryption) /

#
/----------------------------------------------------------/

DOTENV_PUBLIC_KEY=
"
034af93e93708b994c10f236c96ef88e47291066946cce2e8d98c9e02c741ced45
"

#
 .env

HELLO=
"
Dotenvx
"

or send to a file:

$ dotenvx decrypt --stdout 
>
 somefile.txt

`keypair`

Print public/private keys for.envfile.

$ 
echo
 
"
HELLO=Dotenvx
"
 
>
 .env
$ dotenvx encrypt

$ dotenvx keypair
{
"
DOTENV_PUBLIC_KEY
"
:
"
<publicKey>
"
,
"
DOTENV_PRIVATE_KEY
"
:
"
<privateKey>
"
}

`keypair --no-native`

Turn off OS secret store lookups for keypair.

$ dotenvx keypair --no-native
{
"
DOTENV_PUBLIC_KEY
"
:
"
<publicKey>
"
,
"
DOTENV_PRIVATE_KEY
"
:
"
<privateKey>
"
}

`keypair -f`

Print public/private keys for.env.productionfile.

$ 
echo
 
"
HELLO=Production
"
 
>
 .env.production
$ dotenvx encrypt -f .env.production

$ dotenvx keypair -f .env.production
{
"
DOTENV_PUBLIC_KEY_PRODUCTION
"
:
"
<publicKey>
"
,
"
DOTENV_PRIVATE_KEY_PRODUCTION
"
:
"
<privateKey>
"
}

`keypair -fk`

Specify path to.env.keys. This is useful for printing public/private keys for monorepos.

$ mkdir -p apps/app1
$ 
echo
 
"
HELLO=Dotenvx
"
 
>
 apps/app1/.env
$ dotenvx encrypt -fk .env.keys -f apps/app1/.env

$ dotenvx keypair -fk .env.keys -f apps/app1/.env
{
"
DOTENV_PUBLIC_KEY
"
:
"
<publicKey>
"
,
"
DOTENV_PRIVATE_KEY
"
:
"
<privateKey>
"
}

`keypair DOTENV_PRIVATE_KEY`

Print specific keypair for.envfile.

$ 
echo
 
"
HELLO=Dotenvx
"
 
>
 .env
$ dotenvx encrypt

$ dotenvx keypair DOTENV_PRIVATE_KEY

<
privateKey
>

`keypair --format shell`

Print a shell formatted response of public/private keys.

$ 
echo
 
"
HELLO=Dotenvx
"
 
>
 .env
$ dotenx encrypt

$ dotenvx keypair --format shell
DOTENV_PUBLIC_KEY=
<
publicKey
>
 DOTENV_PRIVATE_KEY=
<
privateKey
>

`ls`

Print all.envfiles in a tree structure.

$ touch .env
$ touch .env.production
$ mkdir -p apps/backend
$ touch apps/backend/.env

$ dotenvx ls
├─ .env.production
├─ .env
└─ apps
 └─ backend
 └─ .env

`ls directory`

Print all.envfiles inside a specified path to a directory.

$ touch .env
$ touch .env.production
$ mkdir -p apps/backend
$ touch apps/backend/.env

$ dotenvx ls apps/backend
└─ .env

`ls -f`

Glob.envfilenames matching a wildcard.

$ touch .env
$ touch .env.production
$ mkdir -p apps/backend
$ touch apps/backend/.env
$ touch apps/backend/.env.prod

$ dotenvx ls -f 
**
/.env.prod
*

├─ .env.production
└─ apps
 └─ backend
 └─ .env.prod

`ls -ef`

Glob.envfilenames excluding a wildcard.

$ touch .env
$ touch .env.production
$ mkdir -p apps/backend
$ touch apps/backend/.env
$ touch apps/backend/.env.prod

$ dotenvx ls -ef 
'
**/.env.prod*
'

├─ .env
└─ apps
 └─ backend
 └─ .env

`genexample`

In one command, generate a.env.examplefile from your current.envfile contents.

$ 
echo
 
"
HELLO=Dotenvx
"
 
>
 .env

$ dotenvx genexample
▣ generated (.env.example)

#
 .env.example

HELLO
=
"
"

`genexample -f`

Pass multiple.envfiles to generate your.env.examplefile from the combination of their contents.

$ 
echo
 
"
HELLO=Dotenvx
"
 
>
 .env
$ 
echo
 
"
DB_HOST=example.com
"
 
>
 .env.production

$ dotenvx genexample -f .env -f .env.production
▣ generated (.env.example)

#
 .env.example

HELLO
=
"
"

DB_HOST
=
"
"

`genexample directory`

Generate a.env.examplefile inside the specified directory. Useful for monorepos.

$ 
echo
 
"
HELLO=Dotenvx
"
 
>
 .env
$ mkdir -p apps/backend
$ 
echo
 
"
HELLO=Backend
"
 
>
 apps/backend/.env

$ dotenvx genexample apps/backend
▣ generated (.env.example)

#
 apps/backend/.env.example

HELLO
=
"
"

`gitignore`

Gitignore your.envfiles.

$ dotenvx gitignore
▣ ignored .env
*
 (.gitignore)

`gitignore --pattern`

Gitignore specific pattern(s) of.envfiles.

$ dotenvx gitignore --pattern .env.keys
▣ ignored .env.keys (.gitignore)

`precommit`

Prevent.envfiles from being committed to code.

$ dotenvx precommit
▣ .env files (1) protected (encrypted or gitignored)

`precommit --install`

Install a shell script to.git/hooks/pre-committo prevent accidentally committing any.envfiles to source control.

$ dotenvx precommit --install
▣ dotenvx precommit installed [.git/hooks/pre-commit]

`precommit directory`

Prevent.envfiles from being committed to code inside a specified path to a directory.

$ 
echo
 
"
HELLO=Dotenvx
"
 
>
 .env
$ mkdir -p apps/backend
$ 
echo
 
"
HELLO=Backend
"
 
>
 apps/backend/.env

$ dotenvx precommit apps/backend
▣ apps/backend/.env not protected (encrypted or gitignored)

`prebuild`

Prevent.envfiles from being built into your docker containers.

Add it to yourDockerfile.

#
 Install via script

RUN
 curl -fsS https://dotenvx.sh | sh

#
 Or copy binary from official image

COPY
 --from=dotenv/dotenvx:latest /usr/local/bin/dotenvx /bin/local/bin

#
 ... orther container commands

RUN
 dotenvx prebuild

CMD
 [
"/usr/local/bin/dotenvx"
, 
"run"
, 
"--"
, 
"node"
, 
"index.js"
]

`prebuild directory`

Prevent.envfiles from being built into your docker containers inside a specified path to a directory.

Add it to yourDockerfile.

#
 Install via script

RUN
 curl -fsS https://dotenvx.sh | sh

#
 Or copy binary from official image

COPY
 --from=dotenv/dotenvx:latest /usr/local/bin/dotenvx /bin/local/bin

#
 ... orther container commands

RUN
 dotenvx prebuild apps/backend

CMD
 [
"/usr/local/bin/dotenvx"
, 
"run"
, 
"--"
, 
"node"
, 
"apps/backend/index.js"
]

`lock`

Lock private keys with a local passphrase to keep them protected inside.env.keys.

# example
DOTENV_PRIVATE_KEY=locked:02f5b97ad58b49ae324cd4e7937bc19b251d006b31cacf46f789eeaf03f923cedc:AZIPDxKqjPLiGl5b4CqVGbR3CIBDUcqHthGaoeWLoUvxbTHJkj3jGoGWGaxFSDUJGQUmWDaExRzxKpVydYF_7qiWr1ecqksOFho5t3EMwKbqX2-y-LZO9K3a4SJaYAjDJXpn3NwG4vAt1oLmGA

`lock up`

Lock a private key in.env.keyswith a local passphrase.

$ dotenvx lock up

Here's what a locked key looks like:

#
 .env.keys

DOTENV_PRIVATE_KEY
=locked:02f5b97ad58b49ae324cd4e7937bc19b251d006b31cacf46f789eeaf03f923cedc:AZIPDxKqjPLiGl5b4CqVGbR3CIBDUcqHthGaoeWLoUvxbTHJkj3jGoGWGaxFSDUJGQUmWDaExRzxKpVydYF_7qiWr1ecqksOFho5t3EMwKbqX2-y-LZO9K3a4SJaYAjDJXpn3NwG4vAt1oLmGA

Specify files with-fand-fk.

$ dotenvx lock up -f .env.production -fk .env.keys

`lock down`

Unlock a private key in.env.keyswith its local passphrase.

$ dotenvx lock down

`native`

Move private keys into your OS secret store (macOS Keychain supported).

Currently supported on macOS.

`native up`

Move a private key from.env.keysinto your OS secret store.

$ dotenvx native up

Specify files with-fand-fk.

$ dotenvx native up -f .env.production -fk .env.keys

`native down`

Move a private key from your OS secret store back into.env.keys.

$ dotenvx native down

`native push`

Copy a private key from.env.keysinto your OS secret store.

$ dotenvx native push

`native pull`

Copy a private key from your OS secret store into.env.keys.

$ dotenvx native pull

`armor`

Move private keys intoDotenvx Armor ⛨for off-device storage, sharing with your team, and audited access.

`armor up`

Move a private key from.env.keysinto Dotenvx Armor.

$ dotenvx armor login
$ dotenvx armor up

Specify environment and team.

$ dotenvx armor up -f .env.production --team acme

`armor down`

Move a private key from Dotenvx Armor back into.env.keys.

$ dotenvx armor down

`armor push`

Copy a private key from.env.keysinto Dotenvx Armor.

$ dotenvx armor push

`armor pull`

Copy a private key from Dotenvx Armor into.env.keys.

$ dotenvx armor pull

Use a token when running non-interactively.

$ dotenvx armor pull -f .env.production --token 
"
$DOTENVX_ARMOR_TOKEN
"

`armor move`

Move an armored key to another team.

$ dotenvx armor move --team acme

`armor login`

Log in to Dotenvx Armor.

$ dotenvx armor login

`armor logout`

Log out of Dotenvx Armor.

$ dotenvx armor 
logout

`help`

Output help fordotenvx.

$ dotenvx 
help

Usage: dotenvx run -- yourcommand

a secure dotenv–from the creator of 
`
dotenv
`

Options:
 -l, --log-level 
<
level
>
 
set
 log level (default: 
"
info
"
)
 -q, --quiet sets log level to error
 -v, --verbose sets log level to verbose
 -d, --debug sets log level to debug
 -V, --version output the version number
 -h, --help display 
help
 
for
 
command

Commands:
 run inject env at runtime [dotenvx run -- yourcommand]
 get [KEY] 
return
 a single environment variable
 
set
 
<
KEY
>
 
<
value
>
 
set
 a single environment variable
 encrypt encrypt .env file(s)
 decrypt decrypt .env file(s)
 keypair [KEY] print public/private keys 
for
 .env file(s)
 ls [directory] print all .env files 
in
 a tree structure
 genexample [directory]
 generate .env.example
 gitignore append to .gitignore
 precommit [directory]
 prevent committing .env files to code
 prebuild [directory]
 prevent including .env files 
in
 docker
 
Professional Security: 
 lock ⊡ lock private keys with a 
local
 passphrase
 native ⌥ move private keys into your OS secret store (macOS Keychain supported)
 armor ⛨ move private keys into Dotenvx Armor [www.dotenvx.com/armor]

You can get more detailed help per command withdotenvx help COMMAND.

$ dotenvx 
help
 run
Usage: @dotenvx/dotenvx run [options]

inject env at runtime [dotenvx run -- yourcommand]

Options:
 -e, --env 
<
strings...
>
 environment variable(s) 
set
 as string (example: 
"
HELLO=Dotenvx
"
) (default: [])
 -f, --env-file 
<
paths...
>
 path(s) to your env file(s) (default: [])
 -fv, --env-vault-file 
<
paths...
>
 path(s) to your .env.vault file(s) (default: [])
 -o, --overload override existing env variables
 --convention 
<
name
>
 load a .env convention (available conventions: [
'
nextjs
'
])
 -h, --help display 
help
 
for
 
command

Examples:

 $ dotenvx run -- npm run dev
 $ dotenvx run -- flask --app index run
 $ dotenvx run -- php artisan serve
 $ dotenvx run -- bin/rails s

Try it:

 $ 
echo
 
"
HELLO=Dotenvx
"
 
>
 .env
 $ 
echo
 
"
console.log('Hello ' + process.env.HELLO)
"
 
>
 index.js

 $ dotenvx run -- node index.js
 [dotenvx@1.X.X] injecting env (1) from .env
 Hello Dotenvx

`--version`

Check current version ofdotenvx.

$ dotenvx --version
X.X.X

### Library 📦

Use dotenvx directly in code.

`config()`

Use directly in node.js code.

#
 .env

HELLO
=
"
Dotenvx
"

// index.js

require
(
'@dotenvx/dotenvx'
)
.
config
(
)

console
.
log
(
`Hello 
${
process
.
env
.
HELLO
}
`
)

$ node index.js
[dotenvx@1.X.X] injecting env (1) from .env
Hello Dotenvx

It defaults to looking for a.envfile.

`config(path: ['.env.local', '.env'])` - multiple files

Specify path(s) to multiple .env files.

#
 .env.local

HELLO
=
"
Me
"

#
 .env

HELLO
=
"
Dotenvx
"

// index.js

require
(
'@dotenvx/dotenvx'
)
.
config
(
{
path
: 
[
'.env.local'
,
 
'.env'
]
}
)

// esm

// import dotenvx from "@dotenvx/dotenvx";

// dotenvx.config({path: ['.env.local', '.env']});

console
.
log
(
`Hello 
${
process
.
env
.
HELLO
}
`
)

$ node index.js
[dotenvx@1.X.X] injecting env (1) from .env.local, .env
Hello Me

`config(overload: true)` - overload

Useoverloadto overwrite the prior set value.

#
 .env.local

HELLO
=
"
Me
"

#
 .env

HELLO
=
"
Dotenvx
"

// index.js

require
(
'@dotenvx/dotenvx'
)
.
config
(
{
path
: 
[
'.env.local'
,
 
'.env'
]
,
 
overload
: 
true
}
)

// esm

// import dotenvx from "@dotenvx/dotenvx";

// dotenvx.config({path: ['.env.local', '.env'], overload: true});

console
.
log
(
`Hello 
${
process
.
env
.
HELLO
}
`
)

$ node index.js
[dotenvx@1.X.X] injecting env (1) from .env.local, .env
Hello Dotenvx

`config(quiet: true)` - quiet

Suppress all output (except errors).

#
 .env

HELLO
=
"
Dotenvx
"

// index.js

require
(
'@dotenvx/dotenvx'
)
.
config
(
{
path
: 
[
'.env.missing'
,
 
'.env'
]
,
 
quiet
: 
true
}
)

// esm

// import dotenvx from "@dotenvx/dotenvx";

// dotenvx.config({path: ['.env.missing', '.env'], quiet: true});

console
.
log
(
`Hello 
${
process
.
env
.
HELLO
}
`
)

$ node index.js
Error: [MISSING_ENV_FILE] missing .env.missing file (/path/to/.env.missing)
Hello Dotenvx

You can also setDOTENV_CONFIG_QUIET=true.

$ DOTENV_CONFIG_QUIET=true node index.js
Error: [MISSING_ENV_FILE] missing .env.missing file (/path/to/.env.missing)
Hello Dotenvx

`config(strict: true)` - strict

Exit with code1if any errors are encountered - like a missing .env file or decryption failure.

#
 .env

HELLO
=
"
Dotenvx
"

// index.js

require
(
'@dotenvx/dotenvx'
)
.
config
(
{
path
: 
[
'.env.missing'
,
 
'.env'
]
,
 
strict
: 
true
}
)

// esm

// import dotenvx from "@dotenvx/dotenvx";

// dotenvx.config({path: ['.env.missing', '.env'], strict: true});

console
.
log
(
`Hello 
${
process
.
env
.
HELLO
}
`
)

$ node index.js
Error: [MISSING_ENV_FILE] missing .env.missing file (/path/to/.env.missing)

`config(ignore:)` - ignore

Useignoreto suppress specific errors likeMISSING_ENV_FILE.

#
 .env

HELLO
=
"
Dotenvx
"

// index.js

require
(
'@dotenvx/dotenvx'
)
.
config
(
{
path
: 
[
'.env.missing'
,
 
'.env'
]
,
 
ignore
: 
[
'MISSING_ENV_FILE'
]
}
)

// esm

// import dotenvx from "@dotenvx/dotenvx";

// dotenvx.config({path: ['.env.missing', '.env'], ignore: ['MISSING_ENV_FILE']});

console
.
log
(
`Hello 
${
process
.
env
.
HELLO
}
`
)

$ node index.js
[dotenvx@1.X.X] injecting env (1) from .env
Hello Dotenvx

`config(envKeysFile:)` - envKeysFile

UseenvKeysFileto customize the path to your.env.keysfile. This is useful with monorepos.

#
 .env

HELLO
=
"
Dotenvx
"

// index.js

require
(
'@dotenvx/dotenvx'
)
.
config
(
{
path
: 
[
'.env'
]
,
 
envKeysFile
: 
'../../.env.keys'
}
)

`config(convention:)` - convention

Set a convention when usingdotenvx.config(). This allows you to use the same file loading order as the CLI without needing to specify each file individually.

#
 Setup environment files

$ 
echo
 
"
HELLO=development local
"
 
>
 .env.development.local
$ 
echo
 
"
HELLO=local
"
 
>
 .env.local
$ 
echo
 
"
HELLO=development
"
 
>
 .env.development
$ 
echo
 
"
HELLO=env
"
 
>
 .env

// index.js

require
(
'@dotenvx/dotenvx'
)
.
config
(
{
 
convention
: 
'nextjs'
 
}
)

console
.
log
(
`Hello 
${
process
.
env
.
HELLO
}
`
)

$ NODE_ENV=development node index.js
[dotenvx@1.28.0] injecting env (1) from .env.development.local, .env.local, .env.development, .env
Hello development 
local

This is equivalent to using--convention=nextjswith the CLI:

$ dotenvx run --convention=nextjs -- node index.js

You can also setDOTENV_CONFIG_CONVENTION=nextjs.

$ DOTENV_CONFIG_CONVENTION=nextjs node index.js

`config(path: directory, convention: 'nextjs')` - directory

Use a directory aspathto make it the base for convention files. This is useful when loading a workspace's env files from a monorepo root.

// index.js

require
(
'@dotenvx/dotenvx'
)
.
config
(
{

 
path
: 
'apps/web'
,

 
convention
: 
'nextjs'

}
)

This loads the convention fromapps/web:

apps/web/.env.development.local
apps/web/.env.local
apps/web/.env.development
apps/web/.env

`config(noArmor:)` - noArmor

Turn offDotenvx Armor ⛨features.

// index.js

require
(
'@dotenvx/dotenvx'
)
.
config
(
{
noArmor
: 
true
}
)

`parse(src)`

Parse a.envstring directly in node.js code.

// index.js

const
 
dotenvx
 
=
 
require
(
'@dotenvx/dotenvx'
)

const
 
src
 
=
 
'HELLO=Dotenvx'

const
 
parsed
 
=
 
dotenvx
.
parse
(
src
)

console
.
log
(
`Hello 
${
parsed
.
HELLO
}
`
)

$ node index.js
Hello Dotenvx

`parse(src, {processEnv:})`

Sometimes, you want to runparsewithout it accessingprocess.env. (You can pass a fake processEnv this way as well - sometimes useful.)

// index.js

const
 
dotenvx
 
=
 
require
(
'@dotenvx/dotenvx'
)

const
 
src
 
=
 
'USER=Me'

const
 
parsed
 
=
 
dotenvx
.
parse
(
src
,
 
{
 
processEnv
: 
{
}
 
}
)

console
.
log
(
`Hello 
${
parsed
.
USER
}
`
)

$ node index.js
Hello Me

`parse(src, {privateKey:})`

Decrypt an encrypted.envstring withprivateKey.

// index.js

const
 
dotenvx
 
=
 
require
(
'@dotenvx/dotenvx'
)

const
 
src
 
=
 
'HELLO="encrypted:BE9Y7LKANx77X1pv1HnEoil93fPa5c9rpL/1ps48uaRT9zM8VR6mHx9yM+HktKdsPGIZELuZ7rr2mn1gScsmWitppAgE/1lVprNYBCqiYeaTcKXjDUXU5LfsEsflnAsDhT/kWG1l"'

const
 
parsed
 
=
 
dotenvx
.
parse
(
src
,
 
{
 
privateKey
: 
'a4547dcd9d3429615a3649bb79e87edb62ee6a74b007075e9141ae44f5fb412c'
 
}
)

console
.
log
(
`Hello 
${
parsed
.
HELLO
}
`
)

$ node index.js
Hello Dotenvx

`set(KEY, value)`

Programmatically set an environment variable.

// index.js

const
 
dotenvx
 
=
 
require
(
'@dotenvx/dotenvx'
)

dotenvx
.
set
(
'HELLO'
,
 
'Dotenvx'
,
 
{
 
path
: 
'.env'
 
}
)

`set(KEY, value, {plain:})`

Programmatically set a plaintext environment variable.

// index.js

const
 
dotenvx
 
=
 
require
(
'@dotenvx/dotenvx'
)

dotenvx
.
set
(
'HELLO'
,
 
'Dotenvx'
,
 
{
 
plain
: 
true
 
}
)

`get(KEY)` - 
Decryption at Access

Programmatically get an environment variable at access/runtime.

// index.js

const
 
dotenvx
 
=
 
require
(
'@dotenvx/dotenvx'
)

const
 
decryptedValue
 
=
 
await
 
dotenvx
.
get
(
'HELLO'
)

console
.
log
(
decryptedValue
)

This is known asDecryption at Accessand is written about inthe whitepaper.

 

## Armor ⛨

⛨ ARMORED KEYS: Harden your private keys.
⮕ install [curl -sfS https://dotenvx.sh/armor | sh]
⮕ then run [dotenvx armor login]

Learn more

 

## Guides

Go deeper withdotenvx– detailed framework and platform guides.

* LanguagesNode.jsPythonRubyGoPHPRust
* Node.js
* Python
* Ruby
* Go
* PHP
* Rust
* FrameworksAstroExpoExpressNextRemixFlaskSinatraRocket
* Astro
* Expo
* Express
* Next
* Remix
* Flask
* Sinatra
* Rocket
* PlatformsDigital OceanDockerFlyHerokuNetlifyVercelRailwayRender
* Digital Ocean
* Docker
* Fly
* Heroku
* Netlify
* Vercel
* Railway
* Render
* CI/CDsGitHub Actions
* GitHub Actions
* Password Managers1PasswordBitwarden
* 1Password
* Bitwarden
* Background JobsTrigger.dev
* Trigger.dev
* Package ManagersNPMPNPM
* NPM
* PNPM
* Process ManagersPM2
* PM2
* MonoreposNxTurborepo
* Nx
* Turborepo
* Concepts.env.env.keys
* .env
* .env.keys

 

## FAQ

#### How does encryption work?

Dotenvx uses Elliptic Curve Integrated Encryption Scheme (ECIES) to encrypt each secret with a unique ephemeral key, while ensuring it can be decrypted using a long-term private key.

When you initialize encryption, a DOTENV_PUBLIC_KEY (encryption key) and DOTENV_PRIVATE_KEY (decryption key) are generated. The DOTENV_PUBLIC_KEY is used to encrypt secrets, and the DOTENV_PRIVATE_KEY is securely stored in your cloud secrets manager or .env.keys file.

Your encrypted .env file is then safely committed to code. Even if the file is exposed, secrets remain protected since decryption requires the separate DOTENV_PRIVATE_KEY, which is never stored alongside it. Readthe whitepaperfor more details.

#### Is it safe to commit an encrypted .env file to code?

Yes. Dotenvx encrypts secrets using AES-256 with ephemeral keys, ensuring that even if the encrypted .env file is exposed, its contents remain secure. The encryption keys themselves are protected using Secp256k1 elliptic curve cryptography, which is widely used for secure key exchange in technologies like Bitcoin.

This means that every secret in the .env file is encrypted with a unique AES-256 key, and that key is further encrypted using a public key (Secp256k1). Even if an attacker obtains the encrypted .env file, they would still need the corresponding private key—stored separately in a secrets manager—to decrypt anything.

Breaking this encryption would require brute-forcing both AES-256 and elliptic curve cryptography, which is computationally infeasible with current technology. Readthe whitepaperfor more details.

#### Why am I getting the errornode: .env: not found?

You are using Node 20 or greater and it adds a differing implementation of--env-fileflag support. Rather than warn on a missing.envfile (like dotenv has historically done), it raises an error:node: .env: not found.

This fix is easy. Replace--env-filewith-f.

#
 from this:

./node_modules/.bin/dotenvx run --env-file .env -- yourcommand

#
 to this:

./node_modules/.bin/dotenvx run -f .env -- yourcommand

more context

 

## Contributing

You can fork this repo and createpull requestsor if you have questions or feedback:

* github.com/dotenvx/dotenvx- bugs and discussions
* @dotenvx 𝕏(DMs are open)

## About

a secure dotenv–from the creator of `dotenv`

dotenvx.com

### Topics

 cli

 homebrew

 dotenv

 curl

 secret-management

 secrets

 environment-variables

 env

 configuration-file

 security-tools

 end-to-end-encryption

 winget

 secrets-management

 secret-manager

 dotenvx

### Resources

 Readme

 

### License

 BSD-3-Clause license
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

5.6k

 stars
 

### Watchers

10

 watching
 

### Forks

146

 forks
 

 Report repository

 

## Releases348

v2.4.1

 Latest

 

Jul 10, 2026

 

+ 347 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* JavaScript95.7%
* Shell4.2%
* Dockerfile0.1%