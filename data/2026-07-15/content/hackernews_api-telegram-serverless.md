---
title: Telegram Serverless
url: https://core.telegram.org/bots/serverless
site_name: hackernews_api
content_file: hackernews_api-telegram-serverless
fetched_at: '2026-07-15T19:30:55.095197'
original_url: https://core.telegram.org/bots/serverless
author: soheilpro
date: '2026-07-15'
description: Telegram Serverless
tags:
- hackernews
- trending
---

* Follow on X

* Home
* FAQ
* Apps
* API
* Protocol
* Schema

# Telegram Serverless

Telegram Serverless lets you run backend code for your bot and Mini Appdirectly on Telegram's infrastructure— no servers to provision, no containers to keep alive, no scaling to think about. You write plain JavaScript modules, deploy them with a single command, and Telegram runs them in a fast, isolated V8 sandbox that sits right next to the Bot API and a built‑in database.

If you have ever wired a bot to a VPS, a cloud function, or a hosting panel just to answer a/start, this is the part you no longer have to do.

On this page

* Why serverless
* Getting started
* Building with AI
* On the go with BotFather
* Projects & modules
* The database
* The SDK
* CLI reference

### Why serverless

A Telegram bot is, at heart, a program that reacts to updates. Traditionally you had to host that program somewhere that is always on, reachable, and secure — and then keep it that way. Telegram Serverless removes that layer entirely:

* No infrastructure.There is no machine to rent, patch, or monitor. Your code runs on demand and scales with your bot automatically.
* Batteries included.The Telegram Bot API, an SQLite‑backed database, and outbound HTTP are available to every module out of the box — nothing to install, no credentials to wire up.
* Fast, isolated execution.Each invocation runs in a lightweight V8 isolate, close to Telegram's own systems, so calls to the Bot API and your database are quick and reliable.
* A real developer workflow.A project lives in a folder on your machine under version control. You edit files, see exactly what changed, deploy atomically, and roll your database schema forward with reviewed migrations — the way you already work with everything else.

### The mental model

You work inthree places, and they map cleanly onto each other:

Where

What lives there

Your project folder

JavaScript modules — schema, shared code, update handlers

The cloud

The deployed copy of those modules, plus your bot's database

The 
tgcloud
 CLI

The bridge — it shows you differences and syncs them

You never SSH into anything. You edit files locally, runnpx tgcloud push, and the platform takes it from there. Your bot's traffic is handled by the deployed modules; your database persists between invocations.

A project has just three kinds of code:

handlers/ # entry points — one file per Telegram update type
lib/ # shared code you import from anywhere
schema.js # your database tables

When an update arrives — a message, a button press, an inline query — Telegram routes it to the matching handler (handlers/message.js,handlers/callback_query.js, …) and calls its default export. That function talks to the Bot API and the database through the SDK, and returns. That is the whole loop. An update with no matching handler is simply ignored, so you add only the handlers you need.

### Quick demo

Here is a complete, working demo bot. It replies to every message and remembers how many it has seen from each chat.

schema.js

import { table, integer } from 'sdk/db';

export const counters = table('counters', {
 chatId: integer('chat_id').primaryKey(),
 seen: integer('seen').notNull().default(0),
});

handlers/message.js

import { api, db } from 'sdk';
import { counters } from 'schema';
import { sql } from 'sdk/db';

export default async function (message) {
 const chatId = message.chat.id;

 // Insert the counter, or bump it if this chat already has one — and get the
 // resulting row back in the same statement via .returning().
 const [row] = await db.insert(counters)
 .values({ chatId, seen: 1 })
 .onConflictDoUpdate({
 target: counters.chatId,
 set: { seen: sql`${counters.seen} + 1` },
 })
 .returning()
 .run();

 await api.sendMessage({
 chat_id: chatId,
 text: `Hello! I've seen ${row.seen} message(s) from you.`,
 });
}

Deploy it:

npx tgcloud push # upload the modules
npx tgcloud migrate # create the `counters` table

That's a live bot with persistent state and no server. Everything in it —api,db, thetable()DSL — is described in the sections below.

Serverless is a general backend for Telegram bots and Mini Apps, not a template for one kind of app. It is ideal for:

* Conversational AI Botsthat need to store per‑user state in a database.
* Mini App Backendsthat store user data and serve dynamic content.
* Games and Tools— including leaderboards, quizzes and more.
* Automations and Integrationsthat call third‑party HTTP APIs and push results into chats.

### Getting started

This walkthrough takes you from an empty folder to a live bot that answers messages and stores data. It assumes you haveNode.js18 or newer installed and a bot registered with@BotFather. By the end you will have used every command you need day to day:push,migrate,run, andstatus.

Before anything else, switch Serverless on.In@BotFather, open your bot →Serverlessand turn it on. That turns the feature on for this bot and unlocks its CLI access token, handlers, library, and database.

#### 1. Create a project

The fastest way to start is the project creator, which scaffolds a project and installs the CLI into it:

npm create @tgcloud/bot example_bot
cd example_bot

The argument is the target folder: pass.to scaffold into the current folder, or any path. It works in an existing folder too and never overwrites files you already have.

This gives you a ready‑to‑edit project:

example_bot/
├─ docs/
│ └─ tgcloud-sdk.md # SDK reference (for you and your AI tools)
├─ handlers/
│ └─ message.js # a starter message handler (echoes text back)
├─ lib/ # your shared modules go here (empty to start)
├─ AGENTS.md # orientation for AI coding assistants
├─ package.json
└─ schema.js # your database tables

The scaffolded files are self‑documenting — each one contains commented examples of what you can do next.

The CLI installs into the project as a local dev‑dependency, so you run it withnpx tgcloud <command>(npx finds the copy in your project'snode_modules), or through thenpm runshortcuts the scaffold adds topackage.json(npm run deploy,npm run status). By default there is no globaltgcloudon yourPATH.

You can also install it globally —npm install -g @tgcloud/cli— if you'd rather type a baretgcloudfrom anywhere. That's handy for runningtgcloud initin any empty folder, and it's what shell tab‑completion needs. Either way you get the same project.

#### 2. Link your bot

Every project is tied to one bot. Connect them withlogin, which asks for your CLI access token (@BotFather→ your bot → Serverless → CLI Access → Access token — a separate token from yourbot's API token) and stores it locally:

npx tgcloud login

The token has the formapp<id>:<secret>. The CLI keeps it in.tgcloud/, which is git‑ignored, and never prints the secret part. Login is the only time you are asked for it — seeAuthenticationfor how tokens are resolved in CI.

#### 3. Look around

Two commands tell you where things stand at any moment, both fully offline:

npx tgcloud status # what has changed locally vs. the deployed copy
npx tgcloud diff # the line‑by‑line changes

Right afteriniteverything is new and nothing is deployed yet.statusshows the starter files waiting to go up.

#### 4. Deploy

Send your modules to the cloud:

npx tgcloud push

pushuploads every changed module in one atomic batch and updates your local record of what the cloud now holds. Your bot is live: open it in Telegram and send it a message — the starter handler echoes it back.

Deploying never touches your database.Pushing code and changing your database schema are deliberately separate steps, so a code deploy can never surprise you with a data migration. That is what the next step is for.

#### 5. Add a database table

Let's make the bot remember something. Openschema.jsand declare a table:

import { table, integer, text, sql } from 'sdk/db';

export const messages = table('messages', {
 id: integer('id').primaryKey({ autoIncrement: true }),
 chatId: integer('chat_id').notNull(),
 text: text('text'),
 created: integer('created_at', { mode: 'timestamp' }).default(sql`(unixepoch())`),
});

Deploy the schema, then apply it to the database:

npx tgcloud push # uploads the new schema.js
npx tgcloud migrate # creates the `messages` table

pushreports that the schema is out of sync and shows you the pending change, but applies nothing.migratewalks you through the change and, on your confirmation, creates the table. This two‑step model — and what happens with riskier changes like drops — is covered inMigrations.

#### 6. Store and read data

Now use the table from your handler. Edithandlers/message.js:

import { api, db } from 'sdk';
import { messages } from 'schema';
import { eq } from 'sdk/db';

export default async function (message) {
 // Save this message.
 await db.insert(messages)
 .values({ chatId: message.chat.id, text: message.text })
 .run();

 // Count how many we've stored for this chat.
 const count = await db.$count(messages, eq(messages.chatId, message.chat.id));

 await api.sendMessage({
 chat_id: message.chat.id,
 text: `Saved. That's ${count} message(s) from this chat so far.`,
 });
}

Deploy the updated handler withnpx tgcloud push, then send your bot a few messages and watch the count climb. The database persists between invocations — that's your bot's memory.

#### 7. Test without deploying

You don't have to deploy to try a change.npx tgcloud runexecutes a handler on the platform using yourlocalfiles, without publishing them:

npx tgcloud run handlers/message '{ chat: { id: 1 }, text: "hello" }'

The argument is the payload your handler receives — forhandlers/message, aMessage— written inJSON5(so you can skip quoting keys). The command prints anything the handler logged withconsole.*, the return value, and how long it took. This is the tightest loop for iterating on logic — no deploy, no waiting for a real message.

#### 8. Keep in sync

As you work, a handful of commands keep your local project and the cloud aligned:npx tgcloud statusshows what changed,npx tgcloud pushdeploys,npx tgcloud pullbrings your local project in line with the cloud,npx tgcloud fetchrefreshes the reference copy without touching your files, andnpx tgcloud resetdiscards local changes.

If two people (or two machines) deploy to the same bot, the platform detects the conflict andpushstops to let youpullfirst — you can never silently overwrite someone else's work. SeeStaying in sync.

### Building with AI

Prefer to build with an AI assistant — or is the only coder on your team an AI? You can still ship a bot. We've taken a first step to make an AI agent feel at home in a project: every new one is scaffolded with anAGENTS.mdand adocs/tgcloud-sdk.mdreference that agentic coding tools read automatically.

Together with a small, self‑contained runtime — one SDK, no npm packages to wrangle — that gives the assistant a running start on the conventions generic codegen tends to miss here: import by bare name, no foreign keys, everydbcall is async, one handler per update type, and the two‑steppush/migrateflow.

Try it:

npm create @tgcloud/bot my-bot
cd my-bot
opencode # or Claude Code, Cursor, … — any agent that reads AGENTS.md

Then just ask, in plain language:

Write a bot that remembers each person's to‑do list — add an item when they send text, and show the whole list when they send /list.

The assistant editsschema.jsand your handlers for you; you review, test a change instantly withnpx tgcloud run, then go live withnpx tgcloud pushandnpx tgcloud migrate.AGENTS.mdis part of your project — edit it as the bot grows so the guidance stays accurate.

### On the go with BotFather

Down to just your phone? The whole project lives in@BotFathertoo — open your bot →Serverlessand you get everything the CLI manages, on a touchscreen:

* Handlers— create, edit, and test‑run update handlers; BotFather keeps the webhook in sync with the handlers you have (the sameIn sync/Out of syncthe CLI reports).
* Library— your sharedlib/modules.
* Database— editschema.jsin the same Drizzle‑like syntax, review pending changes, and apply them;Savedeploys.
* CLI Access— grab the CLI access token here when you're back at a keyboard.

It's one and the same cloud project, so you can start a handler on your phone andnpx tgcloud pullit to your laptop later — nothing is tied to a single client. Running a handler even shows itsConsoleoutput right in the chat, just likenpx tgcloud run.

### Projects and modules

A serverless project is an ordinary folder under version control. It holds nothing but JavaScript modules and a little local state — there is no build step, nonode_modulesat runtime, and no server entry point.

#### Anatomy of a project

example_bot/
├─ handlers/ # update handlers — flat, one level only
│ ├─ message.js
│ └─ callback_query.js
├─ lib/ # shared modules; subdirectories allowed
│ ├─ reply.js
│ └─ internal/util.js
├─ schema.js # database schema — one file, at the root
└─ .tgcloud/ # CLI state — credentials, snapshot, cache (git‑ignored)

Onlyschema.jsand.jsfiles underlib/andhandlers/aredeployed. Everything else — Markdown, config files, the.tgcloud/folder — stays on your machine.

schema.js— your database. It declares tables as named exports using the schema DSL and lives at the project root as a single file. It is deployed like any other module, but deploying it never changes the database — schema changes are applied separately withnpx tgcloud migrate. SeeThe database.

lib/— shared code, anything you want to reuse across handlers: pure helpers, database access layers, formatting, integrations with outside services.lib/is the only directory that may containsubdirectories(lib/internal/util.js,lib/payments/stripe.js), so you can organize a larger codebase however you like. Modules inlib/are never invoked directly by the platform; they exist to be imported by handlers and by each other.

handlers/— the entry points of your bot. Each file corresponds to oneTelegram update type, and the platform routes each incoming update to the matching handler:

File

Handles

handlers/message.js

New incoming messages

handlers/inline_query.js

New incoming 
inline
 queries

handlers/callback_query.js

New incoming callback queries

…

any other Bot API update type

handlers/isflat— no subdirectories. A handler'sexport defaultis the function the platform calls (seeHandlers).

An update type is handledonly if its handler file exists and is non‑empty. If there is nohandlers/<type>.js— or the file is empty — updates of that type are ignored, and the platform runs nothing for them. So keep only the handlers you actually need: each one you add is another update type your bot wakes up to process, and leaving out the rest means Telegram doesn't spin up your code for updates you'd only discard anyway.

To scaffold a new handler, runnpx tgcloud add handlers/<type>.

.tgcloud/— machine‑local state managed entirely by the CLI: your saved credentials, a mirror of the deployed code used for offline diffs, and a small cache. It is git‑ignored, and you should never read from or write to it by hand — use the CLI commands instead.

#### The module system

At runtime, a module can see exactly two things:the platform SDKandthe other modules in your project. There are no npm packages, no filesystem, and no network except through the SDK'sfetch.

Modules are addressed by theirname— the path from the project root, without the.jsextension — not by their location on disk. Always import by that bare name:

import { users } from 'schema'; // 
 the schema module
import { addItem } from 'lib/cart'; // 
 a lib module
import { format } from 'lib/internal/fmt'; // 
 nested lib module
import { db, api, fetch } from 'sdk'; // 
 the platform SDK

Relative paths and file extensions donotwork — the platform resolves names in its module space, not files in a directory:

import { users } from './schema'; // 
 won't compile
import { users } from '../schema'; // 
 won't compile
import x from 'lib/cart.js'; // 
 drop the .js

What's available at runtime is exactly two things:sdkand its submodules (sdk/db,sdk/api,sdk/fetch) — the whole platform surface, seeThe SDK— andyour own modulesunderschema,lib/,handlers/. That's the complete list. If your codeimports anything else, it won't resolve. This constraint is what keeps modules fast to load and safe to run.

#### Handlers

A handler is a module inhandlers/whose default export the platform invokes when a matching update arrives.

// handlers/message.js
import { api } from 'sdk';

export default async function (message) {
 await api.sendMessage({
 chat_id: message.chat.id,
 text: `You said: ${message.text ?? '(no text)'}`,
 });
}

A handler receives the update'spayloadas its argument — the platform unwraps the TelegramUpdatefor you.handlers/message.jsgets theMessage(i.e.update.message);handlers/callback_query.jsgets theCallbackQuery; and so on. The handler'ssecond argumentis a per‑invocation context object,ctx. It carries the rawUpdateasctx.update— reach for it when you need something outside the payload, likeupdate_id.

A handler can beasync(usually is) and may return a value. It reaches the Bot API, the database, and outbound HTTP through the SDK.

You don't need a real update to test a handler.npx tgcloud runexecutes it on the platform with the payload you supply and your current local code:

npx tgcloud run handlers/message '{ chat: { id: 1 }, text: "hi" }'

The argument is the payload — the same object your handler receives — in JSON5. To supply the handler'sctx(its second argument), add--ctx, e.g.--ctx '{ update: { update_id: 1 } }'. This runs against yourlocalfiles, so you can try changes before deploying them. Seerun.

#### What gets deployed

When younpx tgcloud push, the CLI gathers every.jsfile underschema.js,lib/, andhandlers/, and sends that exact set as your project's module space. Anything present in the cloud but absent from your project is removed, so the deployed state always mirrors your folder — deletions included. Files outside those locations are ignored. A stray.jsat the project root (not a config file) is flagged so it doesn't silently go unnoticed, because the project root is meant to hold only serverless content. Markdown, dotfiles, and.tgcloud/are never deployed.

### The database

Every bot gets its own database — an SQLite‑backed store that persists between invocations and is available to every module throughdb. You describe your tables inschema.jswith a small, typed DSL; you read and write them with a fluent query builder; and you evolve them with reviewed migrations.

KnowDrizzle ORM?Then you already know how to talk to the database here. The schema DSL and query builder follow Drizzle — the column builders,select().from().where(), the operators,onConflictDoUpdate,.returning(), and thesqltag all behave the way you'd expect, so reading and writing data is the familiar API you already use. You just import it fromsdk/db, and a couple of platform specifics (most notablyno foreign keys) are pointed out where they come up.

#### Declaring tables

Tables arenamed exportsinschema.js. Callingtable()builds a description at load time (it does not touch the database); the platform discovers the exported tables when you deployschema.jsand migrates the database to match.

import { table, integer, text, boolean, json, index, sql } from 'sdk/db';

export const users = table('users', {
 id: integer('id').primaryKey({ autoIncrement: true }),
 tgId: integer('tg_id').unique(),
 name: text('name').notNull(),
 lang: text('lang').default('en'),
 isAdmin: boolean('is_admin').default(false),
 prefs: json('prefs'),
 created: integer('created_at', { mode: 'timestamp' }).default(sql`(unixepoch())`),
}, (t) => ({
 createdIdx: index('idx_users_created').on(t.created),
}));

table(name, columns, extras?):

* nameis the SQL table name;
* columnsis a map of JS property → column definition;
* extrasis an optional callback(t) => ({ … })wheretexposes the columns (t.createdis a reference to that column) — declare indexes and table‑level constraints here.

##### Column types

Factory

SQLite type

Notes

text()

TEXT

integer()

INTEGER

real()

REAL

alias 
float()

numeric()

NUMERIC

blob()

BLOB

reads/writes 
Uint8Array

boolean()

INTEGER

stored as 0/1, read as 
true
/
false

json()

TEXT

auto 
JSON.stringify
 / 
JSON.parse

The column name argument is optional — omit it and the JS key is used. Themodeoption controls how values convert between SQLite and JavaScript.

mode

Stored as

JS value

boolean

INTEGER 0/1

boolean

json

TEXT (JSON)

any object/array

timestamp

INTEGER (unix seconds)

Date

timestamp_ms

INTEGER (unix ms)

Date

bytes

BLOB

Uint8Array

boolean()andjson()are shorthands forinteger(name, { mode: 'boolean' })andtext(name, { mode: 'json' }).

Ablob()reads and writes aUint8Array— the runtime has no NodeBuffer(and aBufferis aUint8Arraysubclass, so this is the portable base type). Themodeabove governs only how a value isencoded, independent of the column's storage type: soblob('col', { mode: 'json' })is the BLOB counterpart ofjson()— the same JSON encoding, kept in a BLOB column rather than TEXT.

TLDR:blob()usesUint8Array.modecontrols encoding, not storage, soblob(..., { mode: 'json' })stores JSON as a BLOB, whilejson()stores it as TEXT.

##### Column modifiers

Column modifiers chain onto a column.

integer('id').primaryKey({ autoIncrement: true })
text('name').notNull()
text('tg').unique()
text('lang').default('en')
integer('created_at', { mode: 'timestamp' }).default(sql`(unixepoch())`)
text('slug').generatedAlwaysAs(sql`lower(name)`, { mode: 'stored' }) // or 'virtual'
text('email').deprecated('replaced by login') // marks the column for removal

.default()on ajson()column encodes the value for you; asql`…`default is passed through verbatim..deprecated()is terminal — seeMigrations.

##### Indexes and constraints

Indexes and constraints are declared in theextrascallback, where the columns are in scope.

table('t', { /* … */ }, (t) => ({
 uq: unique('uq_email').on(t.email),
 chk: check('chk_done', sql`${t.done} in (0, 1)`),
 idx: index('idx_name').on(t.col),
 uidx: uniqueIndex('uidx_email').on(t.email),
 lower: index('idx_lower').on(sql`lower(${t.email})`), // expression index
 active: index('idx_active').on(t.userId).where(sql`done = 0`), // partial index
}));

Table‑level modifiers chain aftertable(...):.strict(),.withoutRowid(),.deprecated('reason').

#### No foreign keys

The runtime runs withPRAGMA foreign_keysoff. A declared foreign key would be silently inert — no cascades, no orphan protection — which is worse than having none at all, so the DSL makes it impossible. Namely,.references()and table‑levelforeignKey()throw when declared, and a schema that uses them will not deploy.

You should model relationships with plain columns (userId: integer('user_id')) and enforceintegrityin your application code: insert parents before children, delete children before parents, handle errors properly and sweep orphans with aLEFT JOIN … WHERE parent.id IS NULLwhen you need to.

The absence of foreign keys is a deliberate constraint, not an oversight. Account for it early on when planning your bot.

#### Querying

dbis a fluent query builder.Every query is asynchronous— the terminal methods (.all(),.get(),.values(),.run()) return Promises, soalwaysawait.

import { db } from 'sdk';
import { users, todos } from 'schema';
import { eq, and, desc, asc, count, sql } from 'sdk/db';

await db.select().from(todos).all(); // all rows
await db.select().from(todos).where(eq(todos.id, 1)).get(); // first row or null
await db.select().from(todos).values(); // rows as value arrays

await db.select().from(todos)
 .where(and(eq(todos.userId, uid), eq(todos.done, false)))
 .orderBy(desc(todos.priority), asc(todos.id))
 .limit(10).offset(20)
 .all();

// custom projection: { alias: columnRef | sqlExpr | aggregate }
await db.select({ id: todos.id, title: todos.text, n: count() })
 .from(todos).groupBy(todos.userId).having(sql`count(*) > ${1}`).all();

// row count — a helper, not a builder terminal:
await db.$count(todos); // all rows
await db.$count(todos, eq(todos.done, false)); // with a filter

* Chainable:.where(),.orderBy(),.limit(),.offset(),.groupBy(),.having(),.distinct().
* Terminals:.all(),.get(),.values().
* Count rows withdb.$count(table, where?)(orcount()in a projection).

Insert, update, delete:

await db.insert(todos).values({ userId: 1, text: 'Buy milk' }).run();
await db.insert(todos).values([{ text: 'A' }, { text: 'B' }]).run(); // batch
await db.insert(todos).values({ text: 'X' }).returning().run(); // RETURNING *

await db.insert(users).values({ tgId: 42, name: 'Ann' })
 .onConflictDoUpdate({ target: users.tgId, set: { name: 'Ann' } }).run();

await db.update(todos).set({ done: true }).where(eq(todos.id, 1)).run();
await db.delete(todos).where(eq(todos.id, 1)).run();

Note that a batch insert is one statement, so it's capped by SQLite's variable limit (rows × columns); if you go over it, the insert errors out — chunk it yourself.

Operatorsare imported fromsdk/db:

import {
 eq, ne, gt, gte, lt, lte,
 like, notLike,
 isNull, isNotNull, and, or, not,
 between, notBetween, inArray, notInArray,
 count, sum, avg, min, max,
 asc, desc,
} from 'sdk/db';

.where(a, b)with multiple arguments is the same asand(a, b). A comparison's second argument is a value by default, but may be another column orsql`…`— e.g.eq(a.x, b.y). Aggregates (count/sum/avg/min/max) are sql fragments for a.select({ … })projection.

Raw SQL— when the builder isn't enough, drop to raw SQL. The mode is chosen by method:db.runfor writes,db.allfor many rows,db.getfor one row.

await db.run('UPDATE todos SET done = 1 WHERE id = :id', { ':id': 5 });
await db.all(sql`SELECT * FROM todos WHERE done = ${false}`);
await db.get(sql`SELECT count(*) AS c FROM todos`);

Thesql`…`tag turns${value}into a bound parameter and${table.column}into an identifier, and splices nestedsqlfragments. Usesql.raw('…')for a literal with no parameters.

Raw queries arenot bound to a table, so their rows come back without mode conversion — a boolean is0/1, a JSON column is a string, a timestamp is a number. Only the table‑bound builder converts values.

#### Migrations

Your database changes as your bot grows. The platform keeps that safe by separatingdeploying codefromchanging data, and by classifying every schema change by how risky it is.

Deploying never touches the database.When younpx tgcloud pusha changedschema.js, the platform records the new schema and tells you what the databasewouldchange — but applies nothing:

npx tgcloud push # deploy schema.js; reports pending DB changes
npx tgcloud migrate # review and apply them

npx tgcloud migratecomputes the difference between your schema and the live database and walks you through it. You are always asked before anything is applied. This means a routine code deploy can never trigger a data migration by accident.

Each pending change carries a status that determines howmigratetreats it:

Status

Meaning

In 
migrate

safe

Additive and non‑blocking — a new table, column, or index

Applied together in one step, on confirmation

warning

Potentially destructive or slow — dropping something, or an index on a huge table

Presented one at a time, each confirmed separately

manual

Can't be done automatically — e.g. changing a column's type

Shown with guidance; you perform it by hand

undocumented

Exists in the database but not in your schema

Shown for awareness; not applied

Safe changes are quick and reversible in spirit, so they go through together. Each warning is a deliberate, individual confirmation — there is no “apply all” for destructive changes.

Manual changes come with a reason and a suggested action.migrateends with a summary: how many changes were applied, skipped, awaiting a manual fix, or not in your schema.

Seemigratefor the flags (--dry-run,--safe,--yes,--local).

##### Removing things

Deleting a table or column fromschema.jsdoesnotdrop it — that would make an accidental deletion catastrophic. To remove something, mark it deprecated:

// drop a column
text('email').deprecated('replaced by login')

// drop a whole table
export const oldSessions = table('old_sessions', { /* … */ }).deprecated('unused');

On the nextmigrate, the deprecated object shows up as awarning‑status drop that you confirm individually. Once it's gone, remove the declaration.

##### Changing a column's type

Type changes aremanual— SQLite can't always do them in place, and coercing existing values is a judgment call.migratewill show the change and its reasoning; perform it yourself with raw SQL (db.run(...)), typically by creating a new column or table, copying data, and swapping.

### The SDK

At runtime a module has one library:sdk. It bundles the three things a bot backend needs — a database, the Telegram Bot API, and outbound HTTP — with nothing to install and no credentials to configure. The database (db) is covered inThe database; this section coversapi,fetch, and theconsoleglobal.

import { db, api, fetch, BotApiError } from 'sdk'; // the whole surface
// or from submodules:
import { table, integer, text, eq, sql } from 'sdk/db';
import { api } from 'sdk/api';
import { fetch } from 'sdk/fetch';

Import

What it is

db

Database — query builder and schema DSL → 
The database

api

Telegram Bot API — 
api.sendMessage(...)
 → 
below

fetch

Outbound HTTP → 
below

Import your own project modules by theirbare name(from 'schema',from 'lib/cart') — never a relative path or a.jsextension. SeeThe module system.

#### The Bot API

apigives you the entireTelegram Bot API. Call any method asapi.<method>(params). Every current — and future — Bot API method works withno SDK updaterequired.

import { api } from 'sdk';

const me = await api.getMe(); // → the unwrapped result
await api.sendMessage({ chat_id: id, text: 'Hello!' });
await api.editMessageText({ chat_id, message_id, text: 'Updated' });
await api.answerCallbackQuery({ callback_query_id, text: 'Done' });

The response envelope is unwrapped.The Bot API normally wraps results in{ ok: true, result: … }.apireturns theresultdirectly —getMe()resolves to the user object, not to a wrapper. Parameters use the Bot API's own snake_case names (chat_id,message_id,reply_markup, …).

Failures throwBotApiError.When the Bot API returns{ ok: false }, the call throws aBotApiErrorinstead of returning a falsy value, so you can't accidentally ignore it. The error carries.code(the Bot APIerror_code),.description(the human‑readable message),.method(which method failed), and.parameters(extra data such asretry_afteron a 429, ormigrate_to_chat_id). Catch it to handle an expected failure and rethrow the rest:

import { api, BotApiError } from 'sdk';

try {
 await api.deleteMessage({ chat_id, message_id });
} catch (e) {
 if (e instanceof BotApiError && e.code === 400) {
 // 400 = the message is already gone; that's fine here.
 } else {
 throw e;
 }
}

##### File Limitations

You can work with files already on Telegram's servers by theirfile_id— send, forward, or reuse them — but downloading a file's bytes (getFileplus fetching the content) or uploading a new file from a handlerisn't supported yet.

You can easily design around this temporary limitation by passingfile_ids rather than raw bytes.

#### HTTP

fetchis afetch‑like client for calling the outside world — third‑party APIs, webhooks, anything over HTTP.

import { fetch } from 'sdk';

const res = await fetch('https://api.example.com/users', {
 method: 'POST',
 headers: { 'Content-Type': 'application/json' },
 body: JSON.stringify({ name: 'Pavel' }),
});
if (!res.ok) throw new Error(res.statusText);
const data = await res.json();

The response mirrors the web platform:res.status,res.statusText,res.ok(true for 200–299),res.url,res.headers(.get(),.has(),.keys(),.entries()), and body readersawait res.json()/await res.text().

You can also read the body incrementally as astream—for await (const chunk of res.body) { … }— which is how you consume server‑sent events or token‑by‑token output fromAI APIs.

Body helpers set the matchingContent-Typefor you:

await fetch(url, { method: 'POST', body: fetch.body.json({ a: 1 }) }); // application/json
await fetch(url, { method: 'POST', body: fetch.body.form({ a: 1 }) }); // x-www-form-urlencoded
await fetch(url, { method: 'POST', body: fetch.body.text('hi') }); // text/plain

It otherwise behaves like the standardfetchyou already know, withtwo constraints:

* Response content istextual(binary payloads aren't supported).
* Thetotal response is capped at 32 MB. That cap covers the whole response — streaming withres.bodylets you process a large body incrementally, but it does not raise the limit.

#### Logging

The standard globalconsoleis available — nothing to import, it's just there as in any JavaScript. Its output is captured and shown bynpx tgcloud run, which makes it your primary debugging tool during development.

console.log('processing', { chatId: id }); // log / debug — plain
console.info('started'); // info — blue
console.warn('rate limited'); // warn — yellow
console.error(err); // error — red, with a stack trace

Each line is tagged with the[file:line]it came from.console.errorandconsole.traceappend a full stack, whileconsole.warndoes not. When younpx tgcloud runa module, these lines are printed with a colored prefix per level, the time since the run started, and the origin — seerun.

### Command-line interface

tgcloudis the bridge between your project folder and the cloud. It scaffolds projects, shows you what changed, deploys, runs modules, and applies database migrations. It needsNode.js18 or newer. Two ways to get it:

# Recommended — create a project with the CLI installed into it:
npm create @tgcloud/bot example_bot

# Or install the CLI globally and init an empty folder:
npm install -g @tgcloud/cli
tgcloud init

The npm package is@tgcloud/cli; the command it installs istgcloud. The CLI finds your project by walking up from the current directory to the nearest.tgcloud/, so every command works from any subfolder.

Command

Purpose

init

Scaffold a new project in the current folder

add

Scaffold a new module (a handler or a lib module)

login

Link the project to a bot (saves the token)

status

Show what changed locally vs. the cloud

diff

Show the line‑by‑line changes

push

Deploy changed modules to the cloud

migrate

Apply schema changes to the database

run

Execute a module on the platform without deploying

fetch

Refresh the local reference copy from the cloud

pull

Bring local files in line with the cloud

reset

Discard local changes; restore from the cloud state

webhook

Inspect and re‑sync the platform‑managed webhook

completion

Print a shell completion script (bash/zsh/fish)

#### Authentication

A project is tied to one bot by its token, which has the formapp<id>:<secret>. Theapp<id>part is public and may be printed; the secret never appears in logs or errors.

The token is resolved in this order:

1. TGCLOUD_TOKENenvironment variable — for CI; never written to disk.
2. .tgcloud/credentials— written bynpx tgcloud login.
3. Neither → an error pointing you atnpx tgcloud login.

The CLInever prompts for a token mid‑command— a surprise prompt would hang scripts and CI. Logging in is always the explicitloginstep, and if a saved token becomes invalid (401/403), the CLI clears it and asks you tologinagain rather than re‑prompting in place.

#### init

npx tgcloud init

Scaffolds a new project in the current directory:schema.js,lib/,handlers/, a starter handler,AGENTS.md,docs/, and the.tgcloud/state folder. The set of files it creates is provided by the platform, so new starter files and directories can appear without upgrading the CLI. Offline, it falls back to a built‑in copy, soinitalways works.

initrefuses tonestinside another project — an ancestor directory that already has a.tgcloud/— so you can't accidentally shadow one; re‑runninginitin a project's own root is fine and just fills in anything missing.

#### add

npx tgcloud add <target>

Scaffolds a single new module, wired up and ready to edit — a handler or alib/module.

npx tgcloud add handlers/callback_query # a new update handler
npx tgcloud add lib/cart # a new shared module

Note thataddnever overwrites an existing file.

The<target>is the module's path (a trailing.jsis optional). Forhandlers/, the name must be a Telegram update type; the platform advertises the valid set, so an invalid name is rejected up front.handlers/is flat;lib/may be nested (lib/payments/stripe).

The module name is required. Givingjust the directoryis an error — but a helpful one: forhandlers/it lists the update types you don't already have, so you can copy one.

$ npx tgcloud add handlers
Error: Specify a name, e.g. "npx tgcloud add handlers/callback_query".
Available handlers/ types: callback_query, inline_query, chat_member, …

<Tab>completion offers the same set — seecompletion.

The generated file has a liveexport default, so the handler is active as soon as you deploy — there's nothing to uncomment. Deploy the new module withpush.

#### login

npx tgcloud login

Prompts for your CLI access token — from@BotFather→ your bot → Serverless → CLI Access → Access token, a separate token from yourbot's API token— validates it against the platform, and saves it to.tgcloud/credentials.

loginis theonlycommand that asks for a token. It requires a real terminal and will not run without one, so it never hangs in CI.

#### status

npx tgcloud status

Shows, per file, what has changed between your working directory and the deployed copy: modified, new, deleted, unchanged. Fully offline — it compares against the local reference copy in.tgcloud/. A full run also warns about stray.jsfiles at the project root.

#### diff

npx tgcloud diff

Likestatus, but shows the actual line‑by‑line differences for changed modules. Also offline.

#### push

npx tgcloud push [files...]

Deploys your project to the cloud in one atomic batch.

Withno arguments, it deploys the whole project, and the deployed state is made to mirror your folder exactly — modules you deleted locally are removed in the cloud.

Withfile or directory arguments(npx tgcloud push handlers/message.js,npx tgcloud push handlers/), it narrowswhich changes are sent, but still sends the full manifest, so a targeted push never deletes untouched modules.

Its one option is--force— to skip the concurrency check and overwrite whatever is in the cloud. Only use it when you're sure (seeStaying in sync).

After a deploy, ifschema.jschanged and the database is out of sync,pushprints a summary of the pending changes and suggestsnpx tgcloud migrate. It never applies them itself.

#### migrate

npx tgcloud migrate

Applies your schema changes to the database. It computes the difference betweenschema.jsand the live database, then walks you through it one step at a time with a running[N/M]counter:

* A brief summary of all pending changes.
* Safe changes, applied together in a single step on your confirmation.
* Warnings(drops, slow operations), one at a time, each confirmed separately.
* Manual changes, shown with a reason and suggested action, not applied automatically.
* Undocumented objects(in the database but not your schema), shown for awareness.

It ends with a summary: applied, skipped, awaiting manual fix, not in schema.

SeeMigrationsfor the model.

Options:--dry-run(print everything, apply nothing),--safe(auto‑apply safe changes, skip warnings),--yes(auto‑apply safe changes and every warning, skip manual — use with care),--local(diff against your localschema.jsinstead of the deployed one). Without a flag,migraterequires a terminal and errors in a non‑interactive environment rather than guessing.

#### run

npx tgcloud run <module> [args] [--ctx <json5>]

Executes a handler on the platformwithout deploying, using your current local files. This is the fast inner loop for testing logic.

* <module>— a bare name (searched underhandlers/) or a path likehandlers/message.
* [args]— the payload passed to the handler, written inJSON5so you can skip quoting keys. It's the update‑type object your handler receives (e.g. a Message forhandlers/message).
* --ctx <json5>— the handler's context object (its second argument), also JSON5. Use it to supply what your handler reads offctx— e.g. the raw update:--ctx '{ update: { update_id: 1 } }'.

npx tgcloud run handlers/message '{ chat: { id: 1 }, text: "hi" }'

The platform runs the module against the module space assembled from yourlocalproject (so locally‑changedlib/code is used too) and returns the return value, anything logged withconsole.*, and the elapsed time. Read big arguments from a file withnpx tgcloud run handlers/message "$(cat message.json5)".

#### fetch

npx tgcloud fetch

Refreshes the local reference copy of the deployed state without touching your working files. Useful to re‑check a conflict before deciding how to resolve it.

#### pull

npx tgcloud pull

Brings your local project in line with the cloud — updates both the reference copy and your working files to the deployed state.

#### reset

npx tgcloud reset

Discards your local changes and restores the working directory from the last known cloud state. Use it to throw away an experiment.

#### webhook

npx tgcloud webhook
npx tgcloud webhook sync [--drop-pending]

Telegram delivers updates to your bot through a webhook, which the platform manages for you — you never point it anywhere by hand.npx tgcloud webhookshows its current state: the URL, theallowed_updateslist, how many updates are pending, the last delivery error (if any), and whether it isin syncwith your deployed handlers.

“In sync” means the webhook points at the platform and itsallowed_updatesmatch the handlers you've deployed — so Telegram delivers exactly the update types you handle, and nothing else. Deploying a new handler (or removing one) can leave the webhook out of sync until it's refreshed;npx tgcloud statusflags this too.

npx tgcloud webhook syncfixes it — it re‑points the webhook at the platform and rebuildsallowed_updatesfrom your deployed handlers. Add--drop-pendingto discard updates Telegram had already queued before the sync (otherwise they're delivered once the webhook is healthy again).

#### completion

Note:tab‑completion works only when a baretgcloudis on yourPATH— so install it globally (npm install -g @tgcloud/cli) or otherwise put the binary on yourPATH. It can't hook intonpx.

tgcloud completion <bash|zsh|fish>

Prints a shell completion script to stdout. Enable it once, then<Tab>completes commands, flags, module directories, the handler update‑types you don't have yet, and your local runnable modules — the suggestions are computed live, so they reflect the current project and the platform's advertised update‑types.

# bash — needs the bash-completion package:
echo 'eval "$(tgcloud completion bash)"' >> ~/.bashrc

# zsh — ensure `autoload -U compinit && compinit` runs in your ~/.zshrc:
echo 'eval "$(tgcloud completion zsh)"' >> ~/.zshrc

# fish:
tgcloud completion fish > ~/.config/fish/completions/tgcloud.fish

Restart your shell (or re‑source the file) afterwards. Runningtgcloud completionwith no shell prints these instructions again.

#### Staying in sync

Every project has a monotonically increasingrevisionin the cloud, bumped on each deploy. The CLI remembers the revision it last synced with and sends it on eachpush. If the cloud has moved ahead — because another machine or teammate deployed — the push isrejectedinstead of silently overwriting their work, and the CLI offers three ways forward:

npx tgcloud fetch # pull the latest into the reference copy, then re-check
npx tgcloud pull # pull the latest into both reference and working files
npx tgcloud push --force # overwrite the cloud state (dangerous)

This optimistic‑concurrency check is why you can share a bot across a team without a lockstep deploy process. Commands exit non‑zero on failure — a rejected deploy, a failed migration, an authentication error, a module that threw duringrun— so they compose cleanly in scripts and CI pipelines.

##### Telegram

 Telegram is a cloud-based mobile and desktop messaging app with a focus on security and speed.
 

##### About

* FAQ
* Privacy
* Press

##### Mobile Apps

* iPhone/iPad
* Android
* Mobile Web

##### Desktop Apps

* PC/Mac/Linux
* macOS
* Web-browser

##### Platform

* API
* Translations
* Instant View

##### About

##### Blog

##### Press

##### Safety