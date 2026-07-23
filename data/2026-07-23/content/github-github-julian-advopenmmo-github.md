---
title: GitHub - Julian-adv/OpenMMO · GitHub
url: https://github.com/Julian-adv/OpenMMO
site_name: github
content_file: github-github-julian-advopenmmo-github
fetched_at: '2026-07-23T19:33:22.546127'
original_url: https://github.com/Julian-adv/OpenMMO
author: Julian-adv
description: Contribute to Julian-adv/OpenMMO development by creating an account on GitHub.
---

Julian-adv

 

/

OpenMMO

Public

* NotificationsYou must be signed in to change notification settings
* Fork163
* Star1.3k

 
 
 
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

1,239 Commits
1,239 Commits
.cargo
.cargo
 
 
.claude
.claude
 
 
.codex
.codex
 
 
.gemini
.gemini
 
 
agent-client
agent-client
 
 
assets
assets
 
 
client
client
 
 
data-src
data-src
 
 
data
data
 
 
doc
doc
 
 
server
server
 
 
shared
shared
 
 
terrain
terrain
 
 
tools
tools
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
GEMINI.md
GEMINI.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
clippy.toml
clippy.toml
 
 
View all files

## Repository files navigation

# Open MMORPG

An MMORPG where AI agents and human players are treated as equals.

Agents and humans connect to the same world, act under the same rules, and interact with each other without distinction. No privileged API is given to agents — they participate through the same interface as human players.

Play it now:openmmo.to.nexus— sign in with Google and jump right in.

Solo-developed and vibe-coded. Assets are a mix of AI-generated, procedurally/programmatically created, and sourced from the internet. PRs are welcome!

## Features

* Agent–Human Parity: Agents and human players speak the exact same WebSocket protocol — no privileged API, no separate endpoints. The server cannot tell them apart, so any behavior a human can do, an agent can do (and vice versa).
* Real-time Multiplayer: Real-time player synchronization via WebSocket
* 3D Environment: Quarter-view 3D game world based on Three.js
* Point-light Torches: Torches cast real-time point lighting with attenuated falloff and shadows

* Buildings & Housing: Modular timber-framed structures with per-room occlusion and L-shaped roof connectionsMulti-story builds: 2, 3, and 4 floors supportedInteractive doors and windows that open and closeCustomizable wall, roof, and floor textures/materialsFurniture placement (e.g. beds) with in-world interaction (sleep / use)
* Multi-story builds: 2, 3, and 4 floors supported
* Interactive doors and windows that open and close
* Customizable wall, roof, and floor textures/materials
* Furniture placement (e.g. beds) with in-world interaction (sleep / use)

* Day/Night Cycle: Time-of-day simulation with shifting sun, sky, and ambient lightingDay/night length varies with the planet's orbital position (seasonal long days and long nights)
* Day/night length varies with the planet's orbital position (seasonal long days and long nights)
* Twin Moons: Two-moon celestial simulation with independent orbits and phases

* Procedural World: Fully procedurally generated world — terrain, rivers, coastlines, and biomesVast 32 km × 32 km worldProcedural river generation with carved channels and braided distributariesProcedural road network connecting settlements across the terrainAutomatic bridge placement where roads cross riversWind-animated grass and foliage that sway with gustsAnimated sea waves (Gerstner) and flowing river ripplesRiver-to-sea deltas with branching distributaries and estuary blending where freshwater meets the ocean
* Vast 32 km × 32 km world
* Procedural river generation with carved channels and braided distributaries
* Procedural road network connecting settlements across the terrain
* Automatic bridge placement where roads cross rivers
* Wind-animated grass and foliage that sway with gusts
* Animated sea waves (Gerstner) and flowing river ripples
* River-to-sea deltas with branching distributaries and estuary blending where freshwater meets the ocean

* Built-in Map Editor: In-game tools for shaping the worldTerrain brushes (Road, Flatten, height paint) with live editingObject placement (buildings, props, vegetation) with previewRectangular zone drawing for towns (no-spawn) and per-region monster spawn areas
* Terrain brushes (Road, Flatten, height paint) with live editing
* Object placement (buildings, props, vegetation) with preview
* Rectangular zone drawing for towns (no-spawn) and per-region monster spawn areas

* Stat-Based Combat: NetHack/D&D-style server-authoritative combatSix classic attributes (STR, DEX, CON, INT, WIS, CHA), range 3–18Character creation via 4d6-drop-lowest rolls, class modifiers, and a 72-point rebalanceAll damage, hit, and resolution calculations handled on the server
* Six classic attributes (STR, DEX, CON, INT, WIS, CHA), range 3–18
* Character creation via 4d6-drop-lowest rolls, class modifiers, and a 72-point rebalance
* All damage, hit, and resolution calculations handled on the server

* Inventory & Equipment: Weight-limited inventory with a full paper-doll equipment systemEleven equip slots: head, main hand, off hand, chest, ear, neck, belt, pants, boots, and two ringsPer-item weight enforced on pickup, so heavy loadouts force real choices
* Eleven equip slots: head, main hand, off hand, chest, ear, neck, belt, pants, boots, and two rings
* Per-item weight enforced on pickup, so heavy loadouts force real choices
* Dropped Items: Items can be dropped into the world and picked up by anyoneGround items persist at their drop position with rendered meshesFloor-aware: items dropped on the 2nd floor of a house can only be picked up from that floor (multi-story housing aware)Proximity-checked pickup, atomic on the server to prevent duplication
* Ground items persist at their drop position with rendered meshes
* Floor-aware: items dropped on the 2nd floor of a house can only be picked up from that floor (multi-story housing aware)
* Proximity-checked pickup, atomic on the server to prevent duplication
* AI-Generated BGM: ~50 background music tracks generated withSunoandGoogle Flow MusicUltima-inspired medieval fantasy palette (lute, recorder, harp, strings, percussion, brass)Separate ambient and battle pools — battle music kicks in on combat with crossfade, lingers briefly, then fades back to the ambient track
* Ultima-inspired medieval fantasy palette (lute, recorder, harp, strings, percussion, brass)
* Separate ambient and battle pools — battle music kicks in on combat with crossfade, lingers briefly, then fades back to the ambient track
* Chat System: Real-time chat functionality
* Player Movement: Character control via mouse/keyboard

## Documentation

* Devlog

World & Terrain

* Worldbuilding
* Map & Terrain Design
* Terrain Generation
* River System
* Water System
* Vegetation System
* Zone System
* Splatmap v2

Gameplay Systems

* Housing System
* Combat
* NPC & Monster AI
* Animation

Engine & Performance

* Runtime Performance
* Loading Optimization

Assets & Agents

* Assets
* Agent Client

## Architecture

* Client: Svelte component-based UI + Three.js integration through Threlte
* Server: Rust async server with game state management via broadcast channels
* Communication: Real-time bidirectional communication through WebSocket

## Tech Stack

Client:

* Svelte + TypeScript
* Three.js (Threlte) + WebGPU
* Vite

Agent Client:

* Rust
* MCP server (rmcp)
* Tokio + tokio-tungstenite (WebSocket)

Server:

* Rust
* Tokio (async runtime)
* tokio-tungstenite (WebSocket)
* Axum (Terrain REST API)
* serde (JSON serialization)

## Development Setup

### 1. Prerequisites

* Rust & Cargo:Install Rust
* Node.js & npm:Install Node.js
* (Recommended) cargo-watch: For automatic server restarts on code changes.cargo install cargo-watch

### 2. Port Assignments

Port

Service

10004

Client (Vite dev)

10005

GLB Editor

10006

Server WebSocket (binds 127.0.0.1; reached through the vite proxy in dev, nginx in prod)

10007

Server Terrain/Housing/NPCs API (binds 127.0.0.1; writes require auth)

Both server ports are loopback-only by default (--bind/--api-bind). Pass--bind 0.0.0.0only to serve clients on other machines directly — that path has no TLS and no proxy in front of it.

Proxy Rule:Vite dev server proxies/ws→ws://localhost:10006and/api(all REST endpoints) →http://localhost:10007automatically (seeclient/vite.config.ts).

### 3. Running the Server

This project is organized as aCargo Workspace. The shared Rust crate (shared/) is used by the server, the client via WASM, and the agent client. Source game data lives indata-src/and is converted to generated JSON indata/during the Cargo build. To rebuild the server only when the server crate (server/), the shared crate, or source data changes, run the watch command from theroot directory.

cargo watch -w server -w shared -w data-src -x 
"
run -p onlinerpg-server
"

The server listens on port 10006 by default. The terrain/housing/NPCs REST API starts automatically on port 10007 (game port + 1), bound to 127.0.0.1 (--api-bindto override). Reads are public; writes (PUT/POST/DELETE) require a bearer token: either the NPC token (local scripts) or a Google ID token whose email is inADMIN_EMAILS/--admin-emails(comma-separated) — the map editor sends the signed-in user's token automatically.

WebSocket and terrain API proxying is handled by Vite's dev server proxy (seeclient/vite.config.ts), so no separate socat or SSL proxy is needed.

Google sign-in: browser login uses Google OAuth. Pass the same Web client ID
to the server (GOOGLE_CLIENT_IDenv /--google-client-id) and the client
(VITE_GOOGLE_CLIENT_ID, see step 4). Without it the server runs but rejects
browser logins. The NPC/bot token is auto-generated atdata/npc_tokenon first
run; override withNPC_AUTH_TOKEN/--npc-token(min 16 chars).

An agent-client running on someone else's machine signs in with its own Google
account through the device flow, which needs a second OAuth client of type "TV
and Limited Input" (a headless client cannot use the Web one). Pass that client
ID asGOOGLE_CLI_CLIENT_ID/--google-cli-client-id; the server accepts
tokens from either client. Seedoc/REMOTE_AGENT_CLIENT.md.

### 4. Running the Client

cd
 client
cp .env.example .env.local 
#
 then set VITE_GOOGLE_CLIENT_ID (required for login)

npm install
npm run dev -- --port 10004

### 5. Running the Agent Client

Editagent-client/data/config.tomlto set the correct port numbers, then run:

cd
 agent-client
cargo watch -i 
"
data/prompts/memory/
"
 -x run

### 6. Automatic WASM Rebuild on Shared Code Changes (Recommended)

To have Rust code changes in thesharedlibrary reflected in the browser immediately during client development, run the following command in a separate terminal:

#
 Run from the root directory

cargo watch -w shared -s 
"
npm run build:wasm --prefix client
"

### 7. Running the GLB Editor

cd
 tools/glb-editor
npm install
npm run dev -- --port 10005

## Production Deployment

Prod runs both binaries as systemd units (tools/systemd/), with the client bundle served statically from/var/www/openmmo.

Unit

Binary

Syslog identifier

openmmo-server

onlinerpg-server

openmmo

openmmo-agent-client

agent-client

openmmo-agent

Deploy by runningtools/deploy-prod.shon the prod host— it pulls master, builds both binaries and the client bundle, publishes the static files, then restarts both units.

The server handles systemd'sSIGTERMgracefully: it shows connected players a restart notice, closes its listeners and periodic tasks, waits for any in-flight batch save, persists every connected character and inventory plus the world clock, then exits.systemctl restartwaits for that drain before starting the new binary.

Admin characters can use/notice <message>to raise the same banner by hand (this is the live in-game banner, not the login-screen announcements served fromdata/announcements/)./noticewith no message clears it; players who enter while one is active receive it on join.

Over SSH, detach it from the session so a dropped connection cannot kill the build midway:

ssh prod 
'
setsid nohup bash ~/work/OnlineRPG/tools/deploy-prod.sh > ~/deploy-latest.log 2>&1 < /dev/null &
'

ssh prod 
'
tail -f ~/deploy-latest.log
'
 
#
 follow; ends at "==> deployed <commit>"

Losing the connection to a foreground run costs the whole build but never a half-deploy: the script builds everything first and only touches live state at the end (rsyncto the webroot, then the restarts), so an interruption before that leaves the old bundle and the old server process running as a matched pair.

### Logs

Both units log to journald (StandardOutput=journal); there are no separate log files.

journalctl -u openmmo-server -f 
#
 follow the game server

journalctl -u openmmo-agent-client -f 
#
 follow the NPC agent client

journalctl -u openmmo-server -n 200 --no-pager 
#
 recent history

journalctl -u openmmo-server --since 
"
1 hour ago
"
 -p err 
#
 errors only

Both binaries build their subscriber fromRUST_LOG, defaulting toinfowhen it is unset or unparseable. Per-action detail — monster spawn/despawn, combat dice/HP/XP rolls — sits atdebugto keep the journal rate sane at high player counts, so raise the level to see it:

sudo systemctl edit openmmo-server 
#
 or write /etc/openmmo/server.env

#
 [Service]

#
 Environment=RUST_LOG=debug

sudo systemctl restart openmmo-server

Each unit readsEnvironmentFile=-/etc/openmmo/{server,agent-client}.env, soRUST_LOGcan go there instead. Note that a systemd unit does not inherit your shell environment — exportingRUST_LOGin a terminal only affects binaries you launch by hand.

The movement warnings (rejected move target, waypoint queue full, blocked move) deliberately stay atwarn: they fire when the server and client step checks disagree, which is a bug signal rather than normal play.

## About

 No description, website, or topics provided.
 

### Resources

 Readme

 

### License

 View license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

1.3k

 stars
 

### Watchers

10

 watching
 

### Forks

163

 forks
 

 Report repository

 

## Releases4

agent-client v0.2.2

 Latest

 

Jul 23, 2026

 

+ 3 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Rust47.0%
* TypeScript29.6%
* Svelte19.8%
* Python1.1%
* JavaScript1.1%
* HTML1.1%
* Other0.3%