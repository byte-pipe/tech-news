---
title: 'GitHub - vercel-labs/portless: Replace port numbers with stable, named local URLs. For humans and agents. · GitHub'
url: https://github.com/vercel-labs/portless
site_name: github
content_file: github-github-vercel-labsportless-replace-port-numbers-wi
fetched_at: '2026-09-02T14:58:50.979825'
original_url: https://github.com/vercel-labs/portless
author: vercel-labs
description: Replace port numbers with stable, named local URLs. For humans and agents. - vercel-labs/portless
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 vercel-labs

 

/

portless

Public

* NotificationsYou must be signed in to change notification settings
* Fork379
* Star11.6k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

160 Commits
160 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github/
workflows
.github/
workflows
 
 
.husky
.husky
 
 
apps/
docs
apps/
docs
 
 
examples/
google-oauth
examples/
google-oauth
 
 
packages/
portless
packages/
portless
 
 
scripts/
windows-debug
scripts/
windows-debug
 
 
skills
skills
 
 
tests/
e2e
tests/
e2e
 
 
.gitignore
.gitignore
 
 
.node-version
.node-version
 
 
.prettierignore
.prettierignore
 
 
.prettierrc
.prettierrc
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
eslint.config.js
eslint.config.js
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
pnpm-workspace.yaml
pnpm-workspace.yaml
 
 
turbo.json
turbo.json
 
 
View all files

## Repository files navigation

# portless

Replace port numbers with stable, named .localhost URLs for local development. For humans and agents.

-
 "dev": "next dev" # http://localhost:3000

+
 "dev": "portless run next dev" # https://myapp.localhost

## Install

Global (recommended):

npm install -g portless

Or as a project dev dependency:

npm install -D portless

portless is pre-1.0. When installed per-project, different contributors may run different versions. The state directory format may change between releases, which can require re-runningportless trust.

## Run your app

portless myapp next dev

#
 -> https://myapp.localhost

HTTPS with HTTP/2 is enabled by default. On first run, portless generates a local CA, trusts it, and binds port 443 (auto-elevates with sudo on macOS/Linux). Use--no-tlsfor plain HTTP.

The proxy auto-starts when you run an app. A random port (4000-4999) is assigned via thePORTenvironment variable. Most frameworks (Next.js, Express, Nuxt, etc.) respect this automatically. For frameworks that ignorePORT(Vite, VitePlus, Astro, React Router, Angular, Expo, React Native), portless auto-injects the right--portflag and, when needed, a matching--hostflag. Injection reaches through a package script whose command starts with the framework or a known runner ("dev": "vite","dev": "bunx vite"). Only the framework's server commands get the flags (dev,serve,preview,start, a barevite, orvite [root]); a command that does not serve, such asvite build,vite optimize,vp testorastro check, rejects them and is left alone. Expo connection modes (--localhost,--lan,--tunnel) are preserved while the assigned port is still injected. A script portless cannot classify is left alone too: a flag before the subcommand on a CLI whose flag grammar it does not track (vp --mode dev build). Portless also leaves a script alone when appending flags to it would not work: a compound command (&&,|,;), a trailing#comment, its own--option terminator, an env prefix (NODE_ENV=production vite), delegation to another script ("dev": "npm run dev:vite"), or runner flags before the script name (bun run --bun dev). Those keep their own port, so set it in the script yourself.

When auto-starting, portless reuses the configuration (port, TLS, TLDs) from the most recent proxy run, so a restart or reboot does not silently revert to defaults. Explicit env vars (PORTLESS_PORT,PORTLESS_HTTPS, etc.) always take priority.

Portless stores per-user state in~/.portless. When the proxy runs under sudo, it resolves this path from the invoking user's home so the proxy and unprivileged app processes share the same route registrations.

In non-interactive environments (no TTY, orCI=1), portless exits with a descriptive error instead of prompting, so task runners like turborepo and CI scripts fail early with a clear message.

## Configuration

Bareportlessworks out of the box. It runs the"dev"script frompackage.jsonthrough the proxy, inferring the app name from the package name, git root, or directory:

portless 
#
 -> runs "dev" script, https://<project>.localhost

Use an optionalportless.jsonto override defaults:

{ 
"name"
: 
"
myapp
"
 }

portless 
#
 -> runs "dev" script, https://myapp.localhost

The script defaults to"dev". The name is inferred frompackage.jsonif not set in config.

### Monorepo

Oneportless.jsonat the repo root covers all workspace packages. Portless discovers packages frompnpm-workspace.yaml, or the"workspaces"field inpackage.json(npm, yarn, bun):

{
 
"apps"
: {
 
"apps/web"
: { 
"name"
: 
"
myapp
"
 },
 
"apps/api"
: { 
"name"
: 
"
api.myapp
"
 }
 }
}

portless 
#
 from repo root: starts all workspace packages with a "dev" script

cd
 apps/web 
&&
 portless 
#
 start just one package

Theappsmap is optional and only needed for name overrides. Packages not listed still auto-discover with names inferred from theirpackage.json.

Without anappsmap, hostnames follow the<package>.<project>.localhostconvention. The project name comes from the most common npm scope across workspace packages (e.g.@myorg/weband@myorg/apiproducemyorg), falling back to the workspace root directory name. If a package's short name matches the project name, it gets the bare<project>.localhostwithout duplication.

### Config fields

Field

Type

Default

Description

name

string

inferred

Base app name. Worktree prefix still applies.

script

string

"dev"

Name of a 
package.json
 script to run.

appPort

number

auto

Fixed port for the child process.

proxy

boolean

auto

Whether to route through the proxy. Auto-detected.

apps

object

Overrides for workspace packages, keyed by relative path.

turbo

boolean

true

Set 
false
 to use direct spawning instead of turborepo.

### package.json "portless" key

Instead of a separateportless.json, you can add a"portless"key to yourpackage.json. A string value is shorthand for setting the name:

{
 
"name"
: 
"
@myorg/web
"
,
 
"portless"
: 
"
myapp
"

}

An object supports all per-app fields (name,script,appPort,proxy):

{
 
"name"
: 
"
@myorg/web
"
,
 
"portless"
: { 
"name"
: 
"
myapp
"
, 
"script"
: 
"
dev:app
"
 }
}

Thepackage.json"portless"key takes precedence overportless.jsonapp entries but is overridden by CLI flags.

### --script flag

Override the default script for a single invocation:

portless --script start 
#
 run "start" instead of "dev"

portless --script 
test
 
#
 run "test" instead of "dev"

### Turborepo

To use portless with turborepo, putportlessas thedevscript and the real command in a separate script:

{
 
"scripts"
: {
 
"dev"
: 
"
portless
"
,
 
"dev:app"
: 
"
next dev
"

 },
 
"portless"
: { 
"name"
: 
"
myapp
"
, 
"script"
: 
"
dev:app
"
 }
}

Turbo runs each package'sdevscript, which invokes portless. Portless reads the config, detects the package manager, and runspnpm run dev:app(or yarn/bun/npm) through the proxy. No changes toturbo.jsonare needed.

pnpm devat the root works through turbo as usual. People without portless can runpnpm run dev:appdirectly.

## Use in package.json

You can still use portless inpackage.jsonscripts:

{
 
"scripts"
: {
 
"dev"
: 
"
portless run next dev
"

 }
}

With aportless.json, you can simplify to:

{
 
"scripts"
: {
 
"dev"
: 
"
next dev
"

 }
}

Then runportlessorportless runto go through the proxy.

When you press Ctrl+C, portless forwards the interrupt and waits for the command's process tree to
exit. Press Ctrl+C again to forward another interrupt. Any remaining descendants are terminated
after a short grace period.

## Subdomains

Organize services with subdomains:

portless api.myapp pnpm start

#
 -> https://api.myapp.localhost

portless docs.myapp next dev

#
 -> https://docs.myapp.localhost

By default, only explicitly registered subdomains are routed (strict mode). Use--wildcardwhen starting the proxy to allow any subdomain of a registered route to fall back to that app (e.g.tenant1.myapp.localhostroutes to themyappapp without extra registration).

## Git Worktrees

portless runautomatically detects git worktrees. In a linked worktree, the branch name is prepended as a subdomain so each worktree gets its own URL without any config changes:

#
 Main worktree (no prefix)

portless run next dev 
#
 -> https://myapp.localhost

#
 Linked worktree on branch "fix-ui"

portless run next dev 
#
 -> https://fix-ui.myapp.localhost

Use--nameto override the inferred base name while keeping the worktree prefix:

portless run --name myapp next dev 
#
 -> https://fix-ui.myapp.localhost

Putportless runin yourpackage.jsononce and it works everywhere. The main checkout uses the plain name, each worktree gets a unique subdomain. No collisions, no--force.

## Custom TLD

By default, portless uses.localhostwhich auto-resolves to127.0.0.1in most browsers. If you prefer a different TLD (e.g..test), use--tld:

portless proxy start --tld 
test

portless myapp next dev

#
 -> https://myapp.test

The proxy auto-syncs/etc/hostsfor route hostnames (including.test), so those domains resolve on your machine.

Repeat--tldto serve the same app names under multiple TLDs from one proxy:

portless proxy start --tld localhost --tld 
test

portless myapp next dev

#
 -> https://myapp.localhost

#
 -> https://myapp.test

When multiple TLDs are configured,PORTLESS_URLuses the first TLD.PORTLESS_TLDalso accepts a comma separated list, e.g.PORTLESS_TLD=localhost,test.

Recommended:.test(IANA-reserved, no collision risk). Avoid.local(conflicts with mDNS/Bonjour) and.dev(Google-owned, forces HTTPS via HSTS).

### Multi-segment TLDs

The--tldvalue accepts a lowercase DNS name (one or more dot-separated labels, no trailing dot), so a domain you own can be used as the "TLD". This gives local URLs the same structure as production, which keeps OAuth redirect URIs, cross-subdomain cookies, and host-based routing working the same way in both environments:

portless proxy start --tld dev.example.com
portless myapp next dev

#
 -> https://myapp.dev.example.com

Each label must follow DNS rules: lowercase letters, digits, and interior hyphens, with at most 63 characters per label and 253 characters total. The full hostname (app.TLD) is also subject to the 253-character DNS limit.

The proxy auto-syncs/etc/hostsfor registered hostnames, somyapp.dev.example.comresolves to127.0.0.1on your machine. This is a loopback-only setup: outside LAN mode the proxy binds only to127.0.0.1and::1(see below), so a custom TLD is reachable only from the machine running the proxy. Reaching the proxy from other devices requires LAN mode (--lan), but LAN mode serves apps under the.localTLD and ignores a custom--tld, so the two cannot be combined today.

Strict OAuth providers (Google, Apple) reject.localhostand.testredirect URIs but accept a real domain, sohttps://myapp.dev.example.com/api/auth/callback/googleworks as a redirect URI.

## How it works

flowchart TD
 Browser["Browser<br>myapp.localhost"]
 Proxy["portless proxy<br>(port 80 or 443)"]
 App1[":4123<br>myapp"]
 App2[":4567<br>api"]

 Browser --> Proxy
 Proxy --> App1
 Proxy --> App2

 
Loading

1. Start the proxy: auto-starts when you run an app, or start explicitly withportless proxy start
2. Run apps:portless <name> <command>assigns a free port and registers with the proxy
3. Access via URL:https://<name>.localhostroutes through the proxy to your app

Outside LAN mode, the proxy and its HTTP redirect listener bind only to the IPv4 and IPv6 loopback addresses,127.0.0.1and::1. They do not accept connections through LAN, VPN, or other network interfaces.

## HTTP/2 + HTTPS

HTTPS with HTTP/2 is enabled by default. Browsers limit HTTP/1.1 to 6 connections per host, which bottlenecks dev servers that serve many unbundled files (Vite, Nuxt, etc.). HTTP/2 multiplexes all requests over a single connection.

WebSockets work over both protocol versions, so dev server HMR (Next.js, Vite, etc.) works through the proxy: HTTP/1.1Upgraderequests are forwarded as-is, and WebSockets opened over an HTTP/2 connection use extended CONNECT (RFC 8441).

On first run, portless generates a local CA and adds it to your system trust store. No browser warnings. No manual setup.

#
 Use your own certs (e.g., from mkcert)

portless proxy start --cert ./cert.pem --key ./key.pem

#
 Disable HTTPS (plain HTTP on port 80)

portless proxy start --no-tls

#
 If you skipped the trust prompt on first run, trust the CA later

portless trust

On Linux,portless trustsupports Debian/Ubuntu, Arch, Fedora/RHEL/CentOS, and openSUSE (viaupdate-ca-certificatesorupdate-ca-trust). On Windows, it usescertutilto add the CA to the system trust store. On WSL, it updates both the Linux trust store and the Windows current-user Root store so Windows browsers trust portless HTTPS certificates.

## Start at OS startup

Install the proxy as an OS startup service so clean HTTPS URLs are available after reboot without starting the proxy from a terminal:

portless service install
portless service install --lan
portless service install --wildcard
PORTLESS_STATE_DIR=
~
/.portless-lan PORTLESS_LAN=1 portless service install
portless service status
portless service uninstall

The service uses portless defaults unless install options orPORTLESS_*environment variables are provided: HTTPS on port 443 with.localhostnames.service installaccepts the proxy options you would use withproxy start, including--port,--no-tls,--lan,--ip,--tld,--wildcard,--cert, and--key. Use--state-dir <path>orPORTLESS_STATE_DIR=<path>to choose where service state and logs are written.

The chosen service configuration is written into launchd, systemd, or Task Scheduler and reused after reboot.portless service statusreports the installed port, HTTPS mode, TLDs, LAN mode, wildcard mode, and state directory. macOS and Linux install a root-owned service so port 443 can bind at boot. Windows installs a Task Scheduler startup task that runs as SYSTEM. Installation and removal may require administrator privileges.portless cleanautomatically removes the service.

## LAN mode

portless proxy start --lan
portless proxy start --lan --https
portless proxy start --lan --ip 192.168.1.42

--lanexplicitly binds the proxy to the IPv4 and IPv6 unspecified addresses,0.0.0.0and::, and switches to mDNS discovery. This makes services available as<name>.localto devices on the same network. Portless auto-detects your LAN IP and follows Wi-Fi/IP changes automatically, but you can pin another address with--ip <address>or by exportingPORTLESS_LAN_IP. SetPORTLESS_LAN=1in your shell (0/1 boolean) to make LAN mode the default whenever the proxy starts.

Portless remembers LAN mode viaproxy.lan, so if you stop a LAN proxy and start it again, it stays in LAN mode. All proxy settings (port, TLS, TLDs, LAN) are persisted and reused on auto-start unless overridden by explicit flags or env vars. UsePORTLESS_LAN=0for one start to switch back to.localhostmode. If a proxy is already running with different explicit LAN/TLS/TLD settings, portless warns and asks you to stop it first.

LAN mode depends on the system mDNS tools that portless already spawns: macOS ships withdns-sd, while Linux usesavahi-publish-addressfromavahi-utils(install viasudo apt install avahi-utilsor your distro’s equivalent). If the command is missing or your network isn’t reachable,portless proxy start --lanprints the relevant error and exits.

### Framework notes

* Next.js: add your.localhostnames toallowedDevOrigins:// next.config.jsmodule.exports={allowedDevOrigins:["myapp.local","*.myapp.local"],};
* Expo / React Native: portless always injects--port. React Native also gets--host 127.0.0.1. Expo gets--host localhostoutside LAN mode, but in LAN mode portless leaves Metro on its default LAN host behavior instead of forcing--hostorHOST.

## Tailscale sharing

Share your dev server with teammates on yourTailscalenetwork:

portless myapp --tailscale next dev

#
 -> https://myapp.localhost (local)

#
 -> https://devbox.yourteam.ts.net (tailnet)

Each--tailscaleapp is root-mounted on its own Tailscale HTTPS port, so no frameworkbasePathconfiguration is needed. The first app gets port 443, subsequent apps get 8443, 8444, etc.

portless myapp --tailscale next dev 
#
 -> https://devbox.ts.net

portless api --tailscale pnpm start 
#
 -> https://devbox.ts.net:8443

Use--funnelto expose your dev server to the public internet viaTailscale Funnel:

portless myapp --funnel next dev

#
 -> https://devbox.yourteam.ts.net (public)

Tailscale HTTPS certificates must be enabled before--tailscaleor--funnelcan register HTTPS URLs. Funnel must also be enabled for the tailnet and node before--funnelcan register the public URL. If either setting is missing, portless exits before starting the child process.

SetPORTLESS_TAILSCALE=1in your shell profile or.envto share every app by default.portless listshows both local and tailnet URLs. Tailscale serve registrations are cleaned up automatically when the app exits.

Requires the Tailscale CLI to be installed and connected (tailscale up), with Tailscale HTTPS certificates enabled.

## ngrok sharing

Expose your dev server to the public internet withngrok:

portless myapp --ngrok next dev

#
 -> https://myapp.localhost (local)

#
 -> https://abc123.ngrok.app (public)

SetPORTLESS_NGROK=1in your shell profile or.envto enable ngrok by default when portless runs an app.portless listshows both local and ngrok URLs. The ngrok tunnel is cleaned up automatically when the app exits.

Requires the ngrok CLI to be installed and authenticated. If ngrok reports an authentication error, runngrok config add-authtoken <token>and try again.

## Commands

portless 
#
 Run dev script through proxy

portless 
#
 From monorepo root: run all workspace packages

portless run [--name 
<
name
>
] [cmd] [args...] 
#
 Infer name, run through proxy

portless 
<
name
>
 
<
cmd
>
 [args...] 
#
 Run app at https://<name>.localhost

portless 
alias
 
<
name
>
 
<
port
>
 
#
 Register a static route (e.g. for Docker)

portless 
alias
 
<
name
>
 
<
port
>
 --force 
#
 Overwrite an existing route

portless 
alias
 --remove 
<
name
>
 
#
 Remove a static route

portless list 
#
 Show active routes

portless doctor 
#
 Check proxy, routes, DNS, and CA trust

portless trust 
#
 Add local CA to system trust store

portless clean 
#
 Remove state, CA trust entry, and hosts block

portless prune 
#
 Kill orphaned dev servers from crashed sessions

portless hosts sync 
#
 Add routes to /etc/hosts (fixes Safari)

portless hosts clean 
#
 Remove portless entries from /etc/hosts

#
 Disable portless (run command directly)

PORTLESS=0 pnpm dev 
#
 Bypasses proxy, uses default port

#
 Proxy control

portless proxy start 
#
 Start the HTTPS proxy (port 443, daemon)

portless proxy start --no-tls 
#
 Start without HTTPS (port 80)

portless proxy start --lan 
#
 Start in LAN mode (mDNS .local for devices)

portless proxy start -p 1355 
#
 Start on a custom port (no sudo)

portless proxy start --foreground 
#
 Start in foreground (for debugging)

portless proxy start --wildcard 
#
 Allow unregistered subdomains to fall back to parent

portless proxy stop 
#
 Stop the proxy

#
 OS startup service

portless service install 
#
 Start HTTPS proxy when the OS starts

portless service install --lan 
#
 Start service in LAN mode

portless service install --wildcard 
#
 Persist wildcard routing in the service

portless service status 
#
 Show service and proxy status

portless service uninstall 
#
 Remove the startup service

### Options

-p, --port <number> Port for the proxy (default: 443, or 80 with --no-tls)
--no-tls Disable HTTPS (use plain HTTP on port 80)
--https Enable HTTPS (default, accepted for compatibility)
--lan Enable LAN mode (mDNS .local for real devices)
--ip <address> Pin a specific LAN IP (disables auto-follow; use with --lan)
--cert <path> Use a custom TLS certificate
--key <path> Use a custom TLS private key
--foreground Run proxy in foreground instead of daemon
--tld <tld> Use a custom TLD instead of .localhost; repeat for more
--wildcard Allow unregistered subdomains to fall back to parent route
--state-dir <path> Use a custom state directory with service install
--script <name> Run a specific package.json script (default: dev)
--app-port <number> Use a fixed port for the app (skip auto-assignment)
--tailscale Share the app on your Tailscale network (tailnet)
--funnel Share the app publicly via Tailscale Funnel
--ngrok Share the app publicly via ngrok
--force Kill the existing process and take over its route
--name <name> Use <name> as the app name

### Environment variables

# Configuration
PORTLESS_PORT=<number> Override the default proxy port
PORTLESS_APP_PORT=<number> Use a fixed port for the app (same as --app-port)
PORTLESS_HTTPS=0 Disable HTTPS (same as --no-tls)
PORTLESS_LAN=1 Enable LAN mode when set to 1 (auto-detects LAN IP)
PORTLESS_LAN_IP=<address> Pin a specific LAN IP for LAN mode
PORTLESS_TLD=<tld>[,<tld>] Use one or more TLDs (e.g. localhost,test)
PORTLESS_WILDCARD=1 Allow unregistered subdomains to fall back to parent route
PORTLESS_SYNC_HOSTS=0 Disable auto-sync of /etc/hosts (on by default)
PORTLESS_TAILSCALE=1 Share apps on your Tailscale network (same as --tailscale)
PORTLESS_FUNNEL=1 Share apps publicly via Tailscale Funnel (same as --funnel)
PORTLESS_NGROK=1 Share apps publicly via ngrok (same as --ngrok)
PORTLESS_STATE_DIR=<path> Override the state directory

# Injected into child processes
PORT Ephemeral port the child should listen on
HOST Usually 127.0.0.1 (omitted for Expo in LAN mode)
PORTLESS_URL Primary public URL (e.g. https://myapp.localhost)
PORTLESS_TAILSCALE_URL Tailscale URL of the app (when --tailscale is active)
PORTLESS_NGROK_URL ngrok URL of the app (when --ngrok is active)
NODE_EXTRA_CA_CERTS Path to the portless CA (when HTTPS is active)

Reserved names:run,get,alias,hosts,list,doctor,trust,clean,prune,proxy, andserviceare subcommands and cannot be used as app names directly. Useportless run <cmd>to infer the name from your project, orportless --name <name> <cmd>to force any name including reserved ones.

## Uninstall / reset

To remove portless data from your machine (proxy state under~/.portlessand the system state directory, the local CA from the OS trust store when portless installed it, and the portless block in/etc/hosts):

portless clean

macOS/Linux may prompt forsudo. Custom certificate paths passed with--certand--keyare not deleted. If trust-store removal fails, portless retains its CA certificate and key so a laterportless cleancan safely retry.

## Safari / DNS

.localhostsubdomains auto-resolve to127.0.0.1in Chrome, Firefox, and Edge. Safari relies on the system DNS resolver, which may not handle.localhostsubdomains on all configurations.

If Safari can't find your.localhostURL:

portless hosts sync 
#
 Add current routes to /etc/hosts

portless hosts clean 
#
 Clean up later

Auto-syncs/etc/hostsfor route hostnames by default (.localhost, custom TLDs, LAN.local). SetPORTLESS_SYNC_HOSTS=0to disable. If a route hostname will not resolve, the command that registered it warns and points you toportless hosts sync.

## Troubleshooting

Runportless doctorto inspect local health without changing state. It checks Node.js, the state directory, proxy liveness, route entries, HTTPS CA trust, hostname resolution, and LAN mode prerequisites, then prints suggested fixes.

## Proxying Between Portless Apps

If your frontend dev server (e.g. Vite, webpack) proxies API requests to another portless app, make sure the proxy rewrites theHostheader. Without this, portless routes the request back to the frontend in an infinite loop.

Vite(vite.config.ts):

server: 
{

 
proxy
: 
{

 
"/api"
: 
{

 
target
: 
"https://api.myapp.localhost"
,

 
changeOrigin
: 
true
,

 
ws
: 
true
,

 
}
,

 
}
,

}

webpack-dev-server(webpack.config.js):

devServer: 
{

 
proxy
: 
[
{

 
context
: 
[
"/api"
]
,

 
target
: 
"https://api.myapp.localhost"
,

 
changeOrigin
: 
true
,

 
}
]
,

}

Portless automatically setsNODE_EXTRA_CA_CERTSin child processes so Node.js trusts the portless CA. If you run a separate Node.js process outside portless, point it at the CA manually:NODE_EXTRA_CA_CERTS=~/.portless/ca.pem. Alternatively, use--no-tlsfor plain HTTP.

Portless detects this misconfiguration and responds with508 Loop Detectedalong with a message pointing to this fix.

## Development

This repo is a pnpm workspace monorepo usingTurborepo. The publishable package lives inpackages/portless/.

Use Node.js 24+ and pnpm 11 for repository development. The.node-versionfile pins the Node major for version managers.

pnpm install 
#
 Install all dependencies

pnpm build 
#
 Build all packages

pnpm 
test
 
#
 Run tests

pnpm test:coverage 
#
 Run tests with coverage

pnpm lint 
#
 Lint all packages

pnpm type-check 
#
 Type-check all packages

pnpm format 
#
 Format all files with Prettier

## Requirements

* Node.js 24+
* macOS, Linux, or Windows
* Tailscale CLI (optional, for--tailscaleand--funnel)
* ngrok CLI (optional, for--ngrok)