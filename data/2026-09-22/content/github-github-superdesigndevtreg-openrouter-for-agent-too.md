---
title: 'GitHub - superdesigndev/treg: OpenRouter for agent tools. Join community here: https://discord.gg/6mQYYfFMAn · GitHub'
url: https://github.com/superdesigndev/treg
site_name: github
content_file: github-github-superdesigndevtreg-openrouter-for-agent-too
fetched_at: '2026-09-22T15:25:52.912271'
original_url: https://github.com/superdesigndev/treg
author: superdesigndev
description: 'OpenRouter for agent tools. Join community here: https://discord.gg/6mQYYfFMAn - superdesigndev/treg'
---

superdesigndev

 

/

treg

Public

* NotificationsYou must be signed in to change notification settings
* Fork208
* Star2.1k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

2,086 Commits
2,086 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.agents/
skills
.agents/
skills
 
 
.claude-plugin
.claude-plugin
 
 
.claude/
skills/
vendor-listing
.claude/
skills/
vendor-listing
 
 
.cursor-plugin
.cursor-plugin
 
 
.github
.github
 
 
assets/
brand
assets/
brand
 
 
deploy
deploy
 
 
docs
docs
 
 
dsh
dsh
 
 
examples/
proxy-demo
examples/
proxy-demo
 
 
marketing
marketing
 
 
packages/
npm
packages/
npm
 
 
plugin
plugin
 
 
plugins
plugins
 
 
scripts
scripts
 
 
skills/
treg
skills/
treg
 
 
src/
treg
src/
treg
 
 
tests
tests
 
 
.env.example
.env.example
 
 
.gitignore
.gitignore
 
 
.gitleaks.toml
.gitleaks.toml
 
 
.gitleaksignore
.gitleaksignore
 
 
AGENTS.md
AGENTS.md
 
 
ARCTERM-MUSIC-FIX.md
ARCTERM-MUSIC-FIX.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
USAGE.md
USAGE.md
 
 
alembic.ini
alembic.ini
 
 
e2e-server.sh
e2e-server.sh
 
 
e2e_check.py
e2e_check.py
 
 
package.json
package.json
 
 
pyproject.toml
pyproject.toml
 
 
skills.sh.json
skills.sh.json
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

# Treg (OpenRouter for Tools)

OpenRouter, but for agent tools instead of models.Point an agent at one base URL with one token
and it can do the job:3,000+ catalogued endpoints across 60+ providers— SEO and backlinks,
social and trends, people and company enrichment, ads, scraping, image and video generation —priced per call, from a cent,
with no provider signup. Plus your own team's keys, skills and CLIs, callable by every teammate's
agent without the credential ever leaving the server.

Ask for the task, not the tool.You do not need to know which vendor sells backlink data, or to
hold an account with them. Search for what you want to do, read the price, call it.

Built for the Superdesign team, live attreg.to— anyone can self-host.

## Why it exists

The tools an agent needs for real work sit behind subscriptions nobody buys for a single run —
Semrush $139/mo, Moz $99/mo, Crunchbase $99/mo, Apollo $59/seat — behind signup walls, or behind no
public API at all (invite-only, partner-only, app-review-only). treg carries those accounts and
bills fractions of a cent per call.

## Two kinds of tool, one token

* The catalog— external endpoints treg can serve with its own key or through a verified public
route that needs no provider key. Own-key calls use the team's prepaid balance; anonymous calls
are free. No account with the provider is needed. New verified accounts receive$1.00 freeonce, when they create an eligible team.
* Your own tools— anything a teammate registered: a paid API account, an OAuth connection, a
vendor CLI, aSKILL.md.Your own key always wins over treg's, and those calls are never
metered.

The vocabulary for the second half:

* tool= something the registry calls for you with the org's credential. Two kinds:endpoint— an upstreambase_url+ credentialbindings(each binding injects one
secret into the request; a request can carry several, e.g. an OAuth bearerandadeveloper-tokenheader).CLI— a vendor binary (stripe,gh,vercel, ...) run with the credential injected.
* endpoint— an upstreambase_url+ credentialbindings(each binding injects one
secret into the request; a request can carry several, e.g. an OAuth bearerandadeveloper-tokenheader).
* CLI— a vendor binary (stripe,gh,vercel, ...) run with the credential injected.
* skill / bundle= a recipe (SKILL.md) + its secrets + its tool(s), registered together.

The one rule:the proxyrelays, never modelsthe upstream, andinjects auth server-side— so it survives upstream API changes and callers never hold keys.

# Part 1 · Using the registry

Visittreg.to(hosted on Render) — the dashboard,
sign-in, and every URL below live there.

## Quickstart

Same flow as the dashboard'sGetting startedguide:

#
 1. install the CLI — also points it at the registry

curl -fsSL https://treg.to/install.sh 
|
 sh

#
 2. sign in (GitHub default · --email for a one-time code · --token for agents/CI)

treg login

#
 3. do something useful immediately — no key, nothing registered

treg catalog search 
"
backlinks for a domain
"
 
#
 find a tool by what it DOES

treg call tikhub.tiktok.user.profile --query uniqueId=tiktok
treg balance 
#
 exactly what that cost

#
 (or `treg onboard` for the guided walkthrough)

Catalog tool inputs are described bytreg catalog get <id>. Tools markedstrict_queryreject undeclared or repeated query parameters, unsupported values and request bodies.

Your token identifies you on every call (X-Treg-Tokenheader) and is the same for all tools.
Discover what your team has shared:treg tool ls· check credential health:treg health.

### Or install it as a Claude Code plugin

/plugin marketplace add superdesigndev/treg
/plugin install treg@treg

Installs with no token and no configuration. The skill loads astreg:tregand, on its first run,
walks your agent through the rest — the CLI, sign-in, thentreg mcp install— so you end up with
the command lineandtreg's tools. Other agents:npx skills add superdesigndev/treg -s treg(the-smatters — without it you also get this repo's internal dev skills).
Seedocs/CLAUDE-PLUGIN.md. MiniMax Code / MiniMax Agent users: the same
skill ships via the MiniMax Plugin Marketplace (docs/MINIMAX-PLUGIN.md).

### Claude.ai connector

The Claude Connectors Directory surface ishttps://treg.to/mcp/v2/. It exposes only curated
catalog endpoints and separates read calls from write calls so Claude receives accurate safety
signals. The existing/mcp/surface remains available for catalog endpoints, team-owned tools,
and imported skills. See theMCP and OAuth architecturefor the boundary and implementation, and thesubmission runbookfor release gates.

## Call a tool you don't have a key for

The catalog is grouped by what endpointsdo: keyword and rank tracking, backlinks and authority,
AI visibility, trending and discovery, publishing to socials, people and company enrichment, ads
management and creative, measurement.

treg catalog 
#
 every platform, busiest first

treg catalog search 
"
find a work email
"
 
#
 by the job, not the vendor

treg catalog get hunter.people.email.find 
#
 params, PRICE, example response

treg call hunter.people.email.find --query domain=reddit.com --query full_name=
"
Alexis Ohanian
"

How a catalogued call is served— the credential ladder, in order:

1. your team registered its own tool for that provider → that tool, that key;
2. your team stored a secret for the provider → injected through a virtual tool;
3. neither, and the endpoint has a verified public route →no provider key, free;
4. otherwise →treg's own key, billed to the team's prepaid balance.

The anonymous price assumes the caller does not send a provider credential header. The faithful
relay preserves caller headers, so a caller-supplied provider key can use that key's credits.
Your own credential always beats treg's, so connecting a key you already pay for makes those calls
free of the balance rather than duplicating them. An endpoint treg has no published price for isrefused, not served free — you are told to connect your own key instead. Where several providers
serve one capability,treg catalog searchshows them side by side with prices;choosing is
yours— treg does not silently pick or fail over between providers for you. (When treg's own
account for a provider is out it may serve thesameendpoint through a treg-owned relay account,
disclosed on the response; a team can opt out.) The exception you opt into:treg.<capability>routed endpoints, where treg picks the provider for you and names it.

treg balance 
#
 credit left, calls in flight, recent spend

treg topup 
#
 add funds, or set up automatic top-ups

Out of balance is an HTTP402carryingbalance_micro,estimated_cost_microand atopup_url,
so an agent can act on it without reading prose.

Enrich Arenalives at/enrich-arena, outside the dashboard. Compare enrichment answers with each vendor’s cost and speed,
vote for the best answer in one click, or watch a sequential waterfall. Browsing is
public; submitting requires login, and billable attempts use your team's credits. See theArena guide.

## Share & use your own tools

The zero-thought path — point treg at a project and it figures out what's shareable:

treg scan 
#
 read-only preview: the keys, skills & CLIs upload would register

treg upload 
#
 register them (encrypted server-side); idempotent, --replace to update

treg uploadscans the.env(matching keys against ~80 known providers), every skill
subdirectory, and installed catalog CLIs. Three kinds of things go into the registry — here's how
to share and use each:

### 1. Endpoints (HTTP APIs)

Share— one upstream URL callable with a stored key, or bulk from a.env:

treg secret add STRIPE_KEY --value sk_live_123
treg add stripe --base-url https://api.stripe.com --secret STRIPE_KEY

treg upload env --select openai,stripe,resend 
#
 or straight from the .env

Use— the agent-native way: build therealupstream request and prefix it with the proxy.
treg resolves the tool by host, injects the credential, and relays everything else faithfully
(yourX-Treg-Tokenis stripped before the upstream sees it):

Real request: GET https://api.intercom.io/conversations?per_page=5
Through treg: GET https://treg.to/call/https://api.intercom.io/conversations?per_page=5
 header: X-Treg-Token: <your token>

Or the CLI shorthand — andtreg callsfor the audit log:

treg call intercom conversations --query per_page=5
treg call stripe v1/balance

### 2. CLIs

Share— automatic:treg uploaddetects installed catalog CLIs (stripe,gh,vercel, …)
and registers them; a recipe-only catalog CLI skill (e.g.stripe-cli) auto-becomes runnable too.

Use—treg runexecutes the vendor CLIwith the org's credential injected, so you never
hold the key or log in:

treg run stripe -- get /v1/balance
treg run gh -- pr list
treg run --server agentmail-cli inboxes list 
#
 runs on the registry server: the key never reaches you

--local(default) runs on your machine;--serverruns on the registry and streams output back.
For a whole session,treg shell startopens a subshell where every registered CLI injects
automatically — just usestripe,gh, … normally;exitreverts.treg runsis the audit log.

### 3. Skills

Share— a skill is a whole capability (SKILL.mdrecipe + its secrets + its tool(s)),
registered together so the whole team runs the same skill, maintained in one place:

treg upload skills --dir 
~
/.claude/skills --all 
#
 register a folder of skills in one pass

Use— pull any shared skill into your agent; its API calls go through treg with your token,
so the key stays on the server, never in the skill:

treg skill install seo-blog-writer 
#
 writes into ./.claude/skills/ (--all for the library)

### Manual registration — when the heuristics can't figure a tool out

#
 multi-credential tool (e.g. google-ads: OAuth bearer + a developer-token header)

treg tool add google-ads --base-url https://googleads.googleapis.com \
 --bind 
"
secret=<oauth-id>,injector=oauth
"
 \
 --bind 
"
secret=<dev-id>,name=developer-token,format={secret}
"

#
 one skill, step by step

treg skill init --dir ./my-skill 
#
 drafts treg.json (guesses base_url, finds secrets)

treg skill add --dir ./my-skill 
#
 registers recipe + secrets + tool, atomically

#
 OAuth via the browser (mints the first token, treg holds it and auto-refreshes)

treg oauth connect gsc --client-secret client_secret.json \
 --scopes https://www.googleapis.com/auth/webmasters.readonly

Full options for every command:USAGE.md.

The CLI sends anonymous command usage to PostHog when using treg.to (no arguments or credentials).
Disable withTREG_TELEMETRY=0orDO_NOT_TRACK=1.
Seeanalytics details.

## Teams

An account can own up to 10 teams. Joining other teams as a member does not count toward this limit.

Everything is scoped to anorg: a token = a(user, org)membership, and every secret, tool,
and skill belongs to the active org. Roles:owner / admin / member / viewer.

treg org create 
"
Acme
"
 
#
 make a team, become owner

treg org invite teammate@acme.com 
#
 invite by email (pick role + tool access)

treg org join 
<
code
>
 --email you@acme.com 
#
 accept an invite (creates you if new)

treg org ls 
|
 use 
<
slug
>
 
|
 members 
#
 switch orgs, see the roster

treg org access 
<
member
>
 --tools a,b 
#
 per-member tool access (admin+)

## Going deeper

* Feedback:treg feedback submit friction "The pagination example is unclear."Share problems or suggestions without private information. Seefeedback instructions.
* Review:treg review CALL_ID usefulRate an invited catalog call after using its result;not_sureis fine. Omit private data and continue the task.
* USAGE.md— the fulltregCLI reference.
* /llms.txt— the agent-onboarding file: call
protocol, discovery, auth, CLI, skills. One fetch teaches an agent the whole registry.
* The dashboardattreg.to— full CRUD, a guided
tutorial (Help → Tutorial), and copyable setup instructions for your agents.
* The API— everything the CLI does is plain HTTP; interactive OpenAPI docs live at/docs.
The proxy endpoint is/call/{...}; all endpoints take theX-Treg-Tokenheader.

# Part 2 · Self-hosting & development

## Run it locally

One command (needstmux+uv; it syncs the venv itself):

scripts/dev-local.sh up 
#
 server on http://localhost:18790, dev-safe settings

That runs the server in tmux with hot-reload, its own sqlite DB (treg-dev.db), and email OTP dev
mode (sign-in codes shown on the page — no mail sender needed). Day-to-day:

scripts/dev-local.sh cli login 
#
 sandboxed CLI: never touches your real ~/.treg/config.json

scripts/dev-local.sh logs 
#
 server output · status / restart / down

scripts/dev-local.sh reset 
#
 wipe the dev DB + CLI sandbox for a fresh start

Or run the server directly, without tmux:

uv sync 
#
 create the venv from uv.lock (pulls the server deps for dev)

uv run python -m treg upgrade 
#
 prepare schema + run idempotent release tasks without serving

uv run python -m treg 
#
 serve on 0.0.0.0:18790 (add --reload for dev)

uv run python -m treg keygen 
#
 print a fresh Fernet key for TREG_SECRET_KEY

Installing to run a server (not from source):the base package is theCLI only. To run a
registry, install the server extra —pip install "tools-registry[server]"— which adds FastAPI, the
database drivers, and encryption.pip install tools-registryalone gives just thetregcommand for
talking to an existing registry.

The official hosted service is available attreg.to. Its production topology and live settings are
maintained in the privateoperator runbook.

## Configuration

Environment variables (prefixTREG_, read from.env):

Var

Default

Purpose

TREG_DATABASE_URL

sqlite+aiosqlite:///./treg.db

DB URL (SQLite for dev, Postgres in prod)

TREG_READ_DATABASE_URL

(empty)

Optional SQLite / PostgreSQL read datasource; empty reuses the primary. Requires callers to opt in; existing queries are unchanged. See 
read datasource setup
.

TREG_SECRET_KEY

(empty)

Fernet key for secrets-at-rest; empty → an ephemeral key is minted (secrets won't survive a restart)

TREG_PUBLIC_URL

https://treg.to

treg's public base, used to build the OAuth callback URI

TREG_SESSION_SECRET

(empty)

signs the dashboard session cookie; falls back to 
TREG_SECRET_KEY
. Set a real value in prod

TREG_GITHUB_CLIENT_ID
 / 
_SECRET

(empty)

GitHub OAuth sign-in (callback 
<public_url>/auth/github/callback
); empty hides the button

TREG_GOOGLE_CLIENT_ID
 / 
_SECRET

(empty)

Google OAuth sign-in (redirect 
<public_url>/auth/google/callback
); empty hides the button

TREG_INSTAGRAM_CLIENT_ID
 / 
_SECRET

(empty)

Instagram App ID and secret for direct Instagram Login (redirect 
<public_url>/oauth/callback
)

TREG_META_CLIENT_ID
 / 
_SECRET

(empty)

Meta app credentials for Facebook Pages, Meta Ads, and optional Instagram 
page-tools

TREG_OAUTH_REVIEW_PENDING

instagram-login,page-messages

Comma-separated registry review keys whose capabilities must remain gated; hosted review state is maintained privately.

TREG_RESEND_API_KEY
 / 
TREG_EMAIL_FROM

(empty)

transactional email via Resend (OTP codes + invites); From must be a Resend-verified sender

TREG_BLOCKED_EMAIL_DOMAINS

(empty)

comma-separated email domains refused at every sign-up/sign-in door and at team creation (subdomains included, case-insensitive). Empty blocks nothing — no list ships in the code

TREG_ADMIN_TOKEN

(empty)

cross-tenant 
super-admin
 bearer; authorizes every 
/admin/*
 endpoint. Empty disables the env path (only 
is_superadmin
 users reach 
/admin
). Keep it long + secret.

TREG_EMAIL_DEV_MODE

false

when true, 
/auth/email/start
 returns the OTP in its response (no mail sender needed) — 
dev/local only
, never in prod.

TREG_KV_URL

(empty)

shared key-value store (Redis protocol) for counters every worker must agree on, today the per-team review-invitation budget. Empty = an in-process fallback, fine for one worker

No.envis needed for local dev — every setting has a working default (ephemeral key, sqlite).

⚠️Back these up before moving or redeploying:the Fernet key (TREG_SECRET_KEY) and the
database (Postgres in prod;treg.dbfor a local sqlite run). Lose the Fernet key and every
stored secret becomes unrecoverable.

## Architecture

Request flow for/call:resolve tool (by URL host + longestbase_urlprefix, or by name) →
decrypt its secret(s) → apply each binding's injector → stream to the upstream → fire-and-forget
audit record. The infra relay streams bytes without business logic. The call application buffers
responses needing settlement or ownership evidence up to 8 MiB; larger responses return a 502
without charging instead of a truncated success. Authorized free final downloads needing no body
evidence stream in full, as do own-key and own-tool responses.

Module map(src/treg/):

Module

Role

proxy.py

relay()
 — the whole product in one function: a faithful streaming proxy

injectors.py

the auth-shape seam: 
env
, 
cli_auth
, 
secret_file
, 
oauth
 place a secret into a header/query

oauth.py

token freshness (single-flight refresh) + the connect flow (consent URL, code exchange)

health.py

credential health: refresh oauth, probe tools, webhook the owner of anything broken

convert.py

scaffold a skill directory into a registerable bundle manifest

api.py

the API — the only brain; CLI + skill are thin clients over it

cli.py

the 
treg
 CLI

models.py

SQLModel tables: 
Org
, 
User
, 
Membership
, 
Invite
, 
Secret
, 
Tool
, 
Bundle
, 
PendingOAuth
, 
CallRecord

crypto.py
 
config.py
 
db.py
 
audit.py

Fernet encryption + tokens · settings · async DB · deferred audit writer

The 4 auth shapes(per bindinginjector):env(plain string / API key) ·secret_file(a
JSON token file, pull a field) ·oauth(a JSON OAuth token, auto-refreshed if refreshable) ·cli_auth(material lifted from a CLI's keychain).

Faithful-relay contract:the proxy altersonlythree things, everything else is verbatim:

1. hop-by-hop transport headers (re-derived per hop),
2. treg's own control + edge-forwarding headers (x-treg-token,x-treg-org,ngrok-skip-browser-warning,x-forwarded-*,via, …) and treg's session cookie — all stripped,
never leak upstream,
3. the injected credential(s).

OAuth, three ways to get the first token:manual upload(drop in atoken.json) ·auto-refresh(if the token carriesrefresh_token+ client creds, treg keeps it fresh, you never
re-upload) ·hosted connect flow(treg oauth connect→ browser consent → treg captures the
token itself).

Health checks:give a tool an optional probe ({method, path, expect_status}); a periodic run
(on demand or via cron) validates every credential, refreshes OAuth, and webhooks the owner of any
that break.

Deep design lives indocs/context/(per-subsystem fragments).

## Tests

uv run --with pytest-xdist pytest -n auto -q 
#
 daily local default (same shape as CI)

uv run --frozen python -m pytest -q 
#
 serial: debugging one test, or order

Coverage: proxy walking-skeleton, all injector shapes, per-user auth + CRUD + audit, skill composer,
URL-passthrough + faithful relay, OAuth refresh + connect flow, health checks,treg run/shell,
upload/scan, orgs + invites, the dashboard API, CLI.

## Contributing & docs

treg/
├── src/treg/ # the package (api, cli, proxy, injectors, oauth, health, convert, models, …)
│ └── web/ # dashboard, landing, tutorial, llms.txt, skill.md, install.sh
├── tests/ # pytest suite (CI + local default: pytest-xdist -n auto)
├── docs/
│ ├── context/ # design fragments (codemap system) + generated index
│ └── ONBOARDING.md # first-time bootstrap
├── USAGE.md # full treg CLI reference
└── pyproject.toml

Per-subsystem design docs arefragmentsindocs/context/, each citing itssrc/treg/*sources. Working in this repo with an AI agent? The/tools-registry-contextskill loads the
right fragment for what you're touching and keeps the docs in sync — run/tools-registry-context syncbefore pushing.

Roadmap:MCP support · finer permission tiers · at-rest key-management hardening · possible
Loopni merge.

## License

Apache 2.0 with additional terms (LICENSE): use it freely — including commercially,
inside your own organization (self-hosting your own registry is encouraged). The restriction: don't
redistribute the code to third parties as a competing hosted/managed registry service without written
permission (jason@superdesign.dev).Using the hosted treg.to APIinside your own product —
with pass-through billing viaX-Treg-Metaandusage/by-tag— is allowed without permission;
that's calling our API, not redistributing our software.

### Pinned customer read scopes

For a restricted customer agent,treg org agent-new bot --pin customer=cust_Aenforces attribution
and scopes call/run history, archived results and shared-provider async ownership to that pin.
Foreign or unattributed ids return 404; an unpinned operator keeps the org-wide view and shared
balance. BYOK account access and public media URLs retain their existing permissions. See themulti-tenancy contractfor multiple pins, migration and replay behavior.