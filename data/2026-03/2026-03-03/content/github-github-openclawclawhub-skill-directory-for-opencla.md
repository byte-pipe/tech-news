---
title: 'GitHub - openclaw/clawhub: Skill Directory for OpenClaw · GitHub'
url: https://github.com/openclaw/clawhub
site_name: github
content_file: github-github-openclawclawhub-skill-directory-for-opencla
fetched_at: '2026-03-03T19:19:39.979584'
original_url: https://github.com/openclaw/clawhub
author: openclaw
description: Skill Directory for OpenClaw. Contribute to openclaw/clawhub development by creating an account on GitHub.
---

openclaw



/

clawhub

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork703
* Star3.8k




 
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

587 Commits
587 Commits
.github/
workflows
.github/
workflows
 
 
convex
convex
 
 
docs
docs
 
 
e2e
e2e
 
 
packages
packages
 
 
public
public
 
 
scripts
scripts
 
 
server
server
 
 
src
src
 
 
.env.local.example
.env.local.example
 
 
.gitignore
.gitignore
 
 
.oxfmtrc.jsonc
.oxfmtrc.jsonc
 
 
.oxlintrc.json
.oxlintrc.json
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
DEPRECATIONS.md
DEPRECATIONS.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
VISION.md
VISION.md
 
 
bun.lock
bun.lock
 
 
clawdhub
clawdhub
 
 
clawhub
clawhub
 
 
convex.json
convex.json
 
 
package.json
package.json
 
 
playwright.config.ts
playwright.config.ts
 
 
tsconfig.json
tsconfig.json
 
 
tsconfig.oxlint.json
tsconfig.oxlint.json
 
 
vercel.json
vercel.json
 
 
vite.config.ts
vite.config.ts
 
 
vitest.config.ts
vitest.config.ts
 
 
vitest.e2e.config.ts
vitest.e2e.config.ts
 
 
vitest.setup.ts
vitest.setup.ts
 
 
View all files

## Repository files navigation

# ClawHub

ClawHub is thepublic skill registry for Clawdbot: publish, version, and search text-based agent skills (aSKILL.mdplus supporting files).
It's designed for fast browsing + a CLI-friendly API, with moderation hooks and vector search.

onlycrabs.ai is theSOUL.md registry: publish and share system lore the same way you publish skills.

ClawHub·onlycrabs.ai·Vision·Docs·Contributing·Discord

## What you can do with it

* Browse skills + render theirSKILL.md.
* Publish new skill versions with changelogs + tags (includinglatest).
* Browse souls + render theirSOUL.md.
* Publish new soul versions with changelogs + tags.
* Search via embeddings (vector index) instead of brittle keywords.
* Star + comment; admins/mods can curate and approve skills.

## onlycrabs.ai (SOUL.md registry)

* Entry point is host-based:onlycrabs.ai.
* On the onlycrabs.ai host, the home page and nav default to souls.
* On ClawHub, souls live under/souls.
* Soul bundles only acceptSOUL.mdfor now (no extra files).

## How it works (high level)

* Web app: TanStack Start (React, Vite/Nitro).
* Backend: Convex (DB + file storage + HTTP actions) + Convex Auth (GitHub OAuth).
* Search: OpenAI embeddings (text-embedding-3-small) + Convex vector search.
* API schema + routes:packages/schema(clawhub-schema).

## CLI

Common CLI flows:

* Auth:clawhub login,clawhub whoami
* Discover:clawhub search ...,clawhub explore
* Manage local installs:clawhub install <slug>,clawhub uninstall <slug>,clawhub list,clawhub update --all
* Inspect without installing:clawhub inspect <slug>
* Publish/sync:clawhub publish <path>,clawhub sync

Docs:docs/quickstart.md,docs/cli.md.

### Removal permissions

* clawhub uninstall <slug>only removes a local install on your machine.
* Uploaded registry skills use soft-delete/restore (clawhub delete <slug>/clawhub undelete <slug>or API equivalents).
* Soft-delete/restore is allowed for the skill owner, moderators, and admins.
* Hard delete is admin-only (management tools / ban flows).

## Telemetry

ClawHub tracks minimalinstall telemetry(to compute install counts) when you runclawhub syncwhile logged in.
Disable via:

export
 CLAWHUB_DISABLE_TELEMETRY=1

Details:docs/telemetry.md.

## Repo layout

* src/— TanStack Start app (routes, components, styles).
* convex/— schema + queries/mutations/actions + HTTP API routes.
* packages/schema/— shared API types/routes for the CLI and app.
* docs/— project documentation (architecture, CLI, auth, deployment, and more).
* docs/spec.md— product + implementation spec (good first read).

## Local dev

Prereqs:Bun(Convex runs viabunx, no global install needed).

bun install
cp .env.local.example .env.local

#
 edit .env.local — see CONTRIBUTING.md for local Convex values

#
 terminal A: local Convex backend

bunx convex dev

#
 terminal B: web app (port 3000)

bun run dev

#
 seed sample data

bunx convex run --no-push devSeed:seedNixSkills

For full setup instructions (env vars, GitHub OAuth, JWT keys, database seeding), seeCONTRIBUTING.md.

## Environment

* VITE_CONVEX_URL: Convex deployment URL (https://<deployment>.convex.cloud).
* VITE_CONVEX_SITE_URL: Convex site URL (https://<deployment>.convex.site).
* VITE_SOULHUB_SITE_URL: onlycrabs.ai site URL (https://onlycrabs.ai).
* VITE_SOULHUB_HOST: onlycrabs.ai host match (onlycrabs.ai).
* VITE_SITE_MODE: Optional override (skillsorsouls) for SSR builds.
* CONVEX_SITE_URL: same asVITE_CONVEX_SITE_URL(auth + cookies).
* SITE_URL: App URL (local:http://localhost:3000).
* AUTH_GITHUB_ID/AUTH_GITHUB_SECRET: GitHub OAuth App.
* JWT_PRIVATE_KEY/JWKS: Convex Auth keys.
* OPENAI_API_KEY: embeddings for search + indexing.

## Nix plugins (nixmode skills)

ClawHub can store a nix-clawdbot plugin pointer in SKILL frontmatter so the registry knows which
Nix package bundle to install. A nix plugin is different from a regular skill pack: it bundles the
skill pack, the CLI binary, and its config flags/requirements together.

Add this toSKILL.md:

---

name
:
peekaboo

description
:
Capture and automate macOS UI with the Peekaboo CLI.

metadata
:
{"clawdbot":{"nix":{"plugin":"github:clawdbot/nix-steipete-tools?dir=tools/peekaboo","systems":["aarch64-darwin"]}}}

---

Install via nix-clawdbot:

programs
.
clawdbot
.
plugins

=

[


{

source

=

"github:clawdbot/nix-steipete-tools?dir=tools/peekaboo"
;

}

]
;

You can also declare config requirements + an example snippet:

---

name
:
padel

description
:
Check padel court availability and manage bookings via Playtomic.

metadata
:
{"clawdbot":{"config":{"requiredEnv":["PADEL_AUTH_FILE"],"stateDirs":[".config/padel"],"example":"config = { env = { PADEL_AUTH_FILE = \\\"/run/agenix/padel-auth\\\"; }; };"}}}

---

To show CLI help (recommended for nix plugins), include thecli --helpoutput:

---

name
:
padel

description
:
Check padel court availability and manage bookings via Playtomic.

metadata
:
{"clawdbot":{"cliHelp":"padel --help\\nUsage: padel [command]\\n"}}

---

metadata.clawdbotis preferred, butmetadata.clawdisandmetadata.openclaware accepted as aliases.

## Skill metadata

Skills declare their runtime requirements (env vars, binaries, install specs) in theSKILL.mdfrontmatter. ClawHub's security analysis checks these declarations against actual skill behavior.

Full reference:docs/skill-format.md

Quick example:

---

name
:
my-skill

description
:
Does a thing with an API.

metadata
:

openclaw
:

requires
:

env
:
 -
MY_API_KEY


bins
:
 -
curl


primaryEnv
:
MY_API_KEY

---

## Scripts

bun run dev
bun run build
bun run
test

bun run coverage
bun run lint

## About

Skill Directory for OpenClaw

clawhub.ai

### Topics

 skill

 directory

### Resources

 Readme



### License

 MIT license


### Contributing

 Contributing


### Security policy

 Security policy


### Uh oh!

There was an error while loading.Please reload this page.





Activity


Custom properties


### Stars

3.8k

 stars


### Watchers

35

 watching


### Forks

703

 forks


 Report repository



## Sponsor this project

### Uh oh!

There was an error while loading.Please reload this page.





### Uh oh!

There was an error while loading.Please reload this page.





## Contributors

### Uh oh!

There was an error while loading.Please reload this page.





## Languages

* TypeScript95.0%
* CSS4.0%
* Other1.0%
