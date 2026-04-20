---
title: 'GitHub - moongate-community/moongatev2: Moongate is modern Ultima Online server built from scratch in C# with AOT compilation for high performance and nostalgic gameplay experience. · GitHub'
url: https://github.com/moongate-community/moongatev2
site_name: hnrss
content_file: hnrss-github-moongate-communitymoongatev2-moongate-is-mo
fetched_at: '2026-03-06T19:17:40.051948'
original_url: https://github.com/moongate-community/moongatev2
date: '2026-03-06'
description: Moongate is modern Ultima Online server built from scratch in C# with AOT compilation for high performance and nostalgic gameplay experience. - moongate-community/moongatev2
tags:
- hackernews
- hnrss
---

moongate-community



/

moongatev2

Public

* NotificationsYou must be signed in to change notification settings
* Fork4
* Star68




 
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

462 Commits
462 Commits
.github/
workflows
.github/
workflows
 
 
benchmarks
benchmarks
 
 
converters
converters
 
 
docs
docs
 
 
images
images
 
 
moongate_data
moongate_data
 
 
scripts
scripts
 
 
src
src
 
 
stack
stack
 
 
tests/
Moongate.Tests
tests/
Moongate.Tests
 
 
tools/
Moongate.Stress
tools/
Moongate.Stress
 
 
ui
ui
 
 
.dockerignore
.dockerignore
 
 
.editorconfig
.editorconfig
 
 
.gitignore
.gitignore
 
 
.releaserc.json
.releaserc.json
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CODE_CONVENTION.md
CODE_CONVENTION.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
Directory.Build.props
Directory.Build.props
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
Moongate.slnx
Moongate.slnx
 
 
README.md
README.md
 
 
global.json
global.json
 
 
View all files

## Repository files navigation

# Moongate v2

Moongate v2 is a modern Ultima Online server project built with .NET 10.
It targets a clean, modular architecture with strong packet tooling, deterministic game-loop processing, and practical test coverage.

Looking for collaborators: I am actively seeking contributors to help build Moongate v2, and I would especially appreciate support with technical/code reviews.
Want to help? Open an issue/discussion on GitHub or join Discord:

* Issues:https://github.com/moongate-community/moongatev2/issues
* Discussions:https://github.com/moongate-community/moongatev2/discussions
* Matrix room:https://matrix.to/#/#moongate:matrix.org

Moongate is not a clone of ModernUO, RunUO, ServUO or any other server, and it does not aim to be. In fact, we owe a great deal of inspiration to these projects. Their legacy and technical achievements are invaluable, and this project would not exist without them. Thank you.

## Acknowledgements

Special thanks to the teams and contributors behind these projects, which strongly inspired Moongate:

* POLServer:https://github.com/polserver/polserver
* ModernUO:https://github.com/modernuo/modernuo

Data credits:

* World decoration datasets (Assets/data/decoration/**) are imported from the ModernUO Distribution data pack.
* World location datasets (Assets/data/locations/**) are imported/adapted from the ModernUO Distribution data pack.
* Sign datasets (Assets/data/signs/signs.cfg) are imported/adapted from ModernUO data format and content.

Thanks to the ModernUO team for making these resources available.

## Index

* Project Goals
* Project Story
* Frontend Preview
* Current Status
* Spatial Chunk Strategy
* World Generation Pipeline
* UO Feature Support (Current)
* Persistence
* Email Delivery (Minimal SMTP)
* Templates
* Solution Structure
* Source Generators (AOT)
* Event And Packet Separation
* Game Loop Scheduling
* Requirements
* Server Startup Tutorial
* Quick Start
* Command System
* Scripting
* Item ScriptId Dispatch
* Scripts
* Benchmarks
* Docker
* Docker Monitoring Stack
* Documentation
* Development Notes
* Contributing
* License

## Project Goals

* Build a maintainable UO server foundation focused on correctness and iteration speed.
* Keep networking and game-loop boundaries explicit and thread-safe.
* Model protocol packets with typed definitions and source-generated registration.
* Stay AOT-aware while preserving a smooth local development workflow.

## Project Story

You can read the background and motivation behind Moongate v2 here:

* https://orivega.io/moongate-v2-rewriting-a-ultima-online-server-from-scratch-because-i-wanted-to/

## Frontend Preview

I hate building frontend myself, so thanks to Codex I started adding a UI layer inui/.

The UI now also includes Item Templates search with image previews.

## Current Status

The project is actively in development and already includes:

* TCP server startup and connection lifecycle handling.
* Packet framing/parsing for fixed and variable packet sizes.
* Attribute-based packet mapping ([PacketHandler(...)]) with source generation.
* Inbound message bus (IMessageBusService) for network thread -> game-loop crossing.
* Domain event bus (IGameEventBusService) with initial events (PlayerConnectedEvent,PlayerDisconnectedEvent).
* Outbound event listener abstraction (IOutboundEventListener<TEvent>) for domain-event -> network side effects.
* Session split between transport (GameNetworkSession) and gameplay/protocol context (GameSession).
* Unit tests for core server behaviors and packet infrastructure.
* Lua scripting runtime with module/function binding and.luarcgeneration support.
* Lua metadata files (definitions.lua,.luarc.json) generated in configuredLuaEngineConfig.LuarcDirectoryduring engine startup.
* Embedded HTTP host (Moongate.Server/Http) for health/admin endpoints and OpenAPI/Scalar docs.
* Dedicated HTTP rolling logs in the shared logs directory (moongate_http-*.log).
* Snapshot+journal persistence module (Moongate.Persistence) integrated in server lifecycle.
* ID-based persistence references for character equipment/container ownership.
* Interactive console UI with fixed prompt (moongate>) and Spectre-based colored log rendering.
* Timer wheel runtime metrics integrated in the metrics pipeline (timer.*).
* Timestamp-driven game loop scheduling with timer delta updates and optional idle CPU throttling.
* Region system adopted from ModernUO (chosen as the most robust baseline), including polymorphic JSON loading via$type.
* Spatial region resolution indexed by sector with deterministic ordering:higherPriorityfirstthen deeper parent/child hierarchy (ChildLevel) when priority ties.
* higherPriorityfirst
* then deeper parent/child hierarchy (ChildLevel) when priority ties.
* Region music mapped as typedMusicNameand resolved byMapId+ position.
* Minimal email stack with Scriban templates and SMTP sender (Moongate.Email), wired throughIEmailService.
* Basic/timid A* pathfinding service is available (IPathfindingService/AStarPathfindingService) and already used by Lua mobile movement primitives (MoveTowards).
* Light cycle is now isolated inILightService/LightService(separate from weather), including global override commands exposed to Lua.
* Lua command scripts are organized undermoongate_data/scripts/commands/gm(one command per file, imported frominit.lua).

## Recent Development Highlights

* Persistence serialization was migrated to MessagePack-CSharp source-generated contracts to resolve NativeAOT runtime instability.
* Outbound packet sending was split into a dedicated networking thread path to reduce game-loop contention.
* Spatial/game-loop hot paths received allocation-focused optimizations across login, packet dispatch, event bus, and persistence mapping.
* Light cycle logic was extracted fromWeatherServiceinto dedicatedILightService/LightService.
* New Lua GM command scripts were added undermoongate_data/scripts/commands/gm(.eclipse,.set_world_light,.teleports).

## Spatial Chunk Strategy

Moongate uses a sector/chunk-based world streaming strategy instead of a pure range-view scan model.

* World data is indexed by sectors (16x16) and loaded lazily.
* When a sector is touched, Moongate loads entities (items + mobiles) around it in a configurable sector radius.
* Around player login and sector changes, snapshots are sent using sector radius windows.
* Sectors are created, populated, and reused in memory; inactive areas stay unloaded until requested.

Why this choice:

* Predictable memory growth and lower steady-state CPU usage on large worlds.
* Better cache locality for entity queries and network snapshot generation.
* Simpler scalability path for high-concurrency shards.

Compared to classic server approaches that rely mainly on repeated range-view scans, this model is intentionally closer to chunk-streaming systems (Minecraft-style): load/unload by sector boundaries with configurable warmup and sync radii.

For a detailed internal status snapshot, seedocs/plans/status-2026-02-19.md.

## World Generation Pipeline

Moongate uses a world-generation pipeline based onIWorldGenerator.

* Each generator is a named unit (Name), orchestrated byIWorldGeneratorBuilderService.
* The builder supports:full execution (GenerateAsync()),targeted execution by name (GenerateAsync("doors")),optional progress callback (Action<string>) for logs/progress output.
* full execution (GenerateAsync()),
* targeted execution by name (GenerateAsync("doors")),
* optional progress callback (Action<string>) for logs/progress output.
* Door generation is implemented asDoorGeneratorBuilder(Name = "doors"), with hardcoded scan regions (ModernUO-style) andCanFitfiltering before accepting candidate placements.
* Generated doors are persisted as world items and include facing/link metadata for runtime behavior.
* Doors now support live open/close behavior on double-click through Lua +DoorService.
* ORA LE PORTE SI APRONO!! :D :D

Manual trigger:

* Command:.spawn_doors
* Scope: console + in-game admin command
* Behavior: runs only thedoorsgenerator and streams progress lines to command output.

## UO Feature Support (Current)

This section reflects the current server-side implementation status.

### Supported now

* Active inbound packet handlers:Login/auth:0xEF,0x80,0xA0,0x91,0x5D,0xBDCharacter:0x00Movement:0x02,0xC8Item interaction:0x07,0x08,0x09,0x13,0x06Speech/chat:0xAD,0xB5Targeting:0x6CGeneral info multiplexer:0xBFPlayer status:0x34Ping:0x73Tooltip:0xD6
* Login/auth:0xEF,0x80,0xA0,0x91,0x5D,0xBD
* Character:0x00
* Movement:0x02,0xC8
* Item interaction:0x07,0x08,0x09,0x13,0x06
* Speech/chat:0xAD,0xB5
* Targeting:0x6C
* General info multiplexer:0xBF
* Player status:0x34
* Ping:0x73
* Tooltip:0xD6
* 0xBFsubcommands currently wired in runtime:0x06Party System0x1AStat Lock Change0x2CUse Targeted Item0x2DCast Targeted Spell0x2EUse Targeted Skill
* 0x06Party System
* 0x1AStat Lock Change
* 0x2CUse Targeted Item
* 0x2DCast Targeted Spell
* 0x2EUse Targeted Skill
* Active outbound gameplay packets include:Login/session:0x8C,0xA8,0xA9,0x1B,0x55,0x82,0xB9World/entity sync:0x78,0x20,0x2E,0x24,0x3C,0x11,0x88,0xF3,0x23,0x76Movement/time:0x22,0x21,0x5B,0xF2Environment/effects:0xBC,0x4F,0x4E,0x6D,0x65,0x54,0x70,0xC0,0xC7UI/speech:0xAE,0xB0,0xDD
* Login/session:0x8C,0xA8,0xA9,0x1B,0x55,0x82,0xB9
* World/entity sync:0x78,0x20,0x2E,0x24,0x3C,0x11,0x88,0xF3,0x23,0x76
* Movement/time:0x22,0x21,0x5B,0xF2
* Environment/effects:0xBC,0x4F,0x4E,0x6D,0x65,0x54,0x70,0xC0,0xC7
* UI/speech:0xAE,0xB0,0xDD

### Partially implemented

* Protocol model coverage is broader than runtime gameplay wiring:many packet contracts exist inMoongate.Network.Packets,only the opcodes listed above are currently connected to live handlers/flows.
* many packet contracts exist inMoongate.Network.Packets,
* only the opcodes listed above are currently connected to live handlers/flows.
* Item pipeline is functional for pickup/drop/equip/container refresh, but advanced cases (full trade/vendor/economy semantics) are still expanding.
* Lua runtime is integrated (commands, speech, targeting, gump builder), but high-level game systems are still script-surface growth areas.

### Not yet implemented (major areas)

* Full combat loop (swing/spell damage pipeline, notoriety-driven combat rules).
* Skill system execution and progression.
* NPC AI, vendors, loot systems, and spawn regions are still evolving; pathfinding currently exists in a basic form and is not yet a full navigation stack.
* World simulation breadth (housing, boats, advanced map interactions, seasons/weather effects gameplay-side).
* Economy systems and complete trading/vendor behavior.
* Full UO protocol listener coverage (many opcodes intentionally unhandled yet).

## Persistence

Moongate uses a lightweight file-based persistence model implemented insrc/Moongate.Persistence:

* Snapshot file (world.snapshot.bin) for full world state checkpoints.
* Append-only journal (world.journal.bin) for incremental operations between snapshots.
* MessagePack-CSharp (source-generated) binary serialization for compact and fast read/write.
* Per-operation checksums in journal entries to detect truncated/corrupted tails.
* Runtime file-lock mode for snapshot/journal handles (PersistenceOptions.EnableFileLock, default: enabled).
* Thread-safe repositories for accounts, mobiles, and items.
* Mobile/item relations are persisted by serial references:UOMobileEntity.BackpackIdUOMobileEntity.EquippedItemIdsUOItemEntity.ParentContainerId+ContainerPositionUOItemEntity.EquippedMobileId+EquippedLayer
* UOMobileEntity.BackpackId
* UOMobileEntity.EquippedItemIds
* UOItemEntity.ParentContainerId+ContainerPosition
* UOItemEntity.EquippedMobileId+EquippedLayer

Runtime behavior:

* On startup,IPersistenceService.StartAsync()loads snapshot (if present) and replays journal.
* During runtime, repositories append operations to journal.
* On save/stop,SaveSnapshotAsync()writes a new snapshot and resets the journal.
* With file-lock mode enabled, snapshot/journal handles remain open for process lifetime and prevent concurrent writers.

NativeAOT note (post-mortem):

* We hit an insidious NativeAOT crash (Segmentation fault: 11) during persistence save.
* Root cause: the previous MemoryPack-based snapshot/journal path crashed under AOT in our runtime scenario.
* Resolution: full persistence serializer migration from MemoryPack to MessagePack-CSharp source-generated contracts (MessagePackObject), covering both snapshot and journal payloads.
* Result: AOT startup + first admin account creation + save cycle now complete without crash.

Storage location:

* Files are written under the serversavedirectory (DirectoriesConfig[DirectoryType.Save]).

Query support:

* IAccountRepository,IMobileRepository, andIItemRepositoryexposeQueryAsync(...).
* Queries are evaluated on immutable snapshots with ZLinq-backed projection/filtering.

## Email Delivery (Minimal SMTP)

Moongate includes a minimal email pipeline:

* IEmailService: orchestration entrypoint.
* IEmailTemplateService: template rendering via Scriban (Moongate.Email).
* IEmailSender: transport abstraction with SMTP implementation (SmtpEmailSender).
* NoOpEmailSender: selected automatically when email is disabled.
* websiteUrl: global Scriban variable injected fromHttp.WebsiteUrl.

Default templates are loaded from:

* moongate_data/email/templates/registration_ok/*
* moongate_data/email/templates/recover_password/*

Runtime directory mapping usesDirectoryType.EmailTemplates.

Minimal config shape:

{

"email"
: {

"isEnabled"
:
false
,

"fromAddress"
:
"
noreply@localhost
"
,

"fallbackLocale"
:
"
en
"
,

"smtp"
: {

"host"
:
"
localhost
"
,

"port"
:
25
,

"useSsl"
:
false
,

"username"
:
null
,

"password"
:
null

 }
 }
}

## Templates

Moongate loads gameplay templates fromDirectoriesConfig[DirectoryType.Templates]:

* templates/items/**/*.json-> loaded byItemTemplateLoaderintoIItemTemplateService
* templates/mobiles/**/*.json-> loaded byMobileTemplateLoaderintoIMobileTemplateService

Template values are data-driven and resolved at runtime using spec objects:

* HueSpec: supports fixed values ("4375","0x1117") and ranges ("hue(5:55)")
* GoldValueSpec: supports fixed values ("0") and dice notation ("dice(1d8+8)")

Example item template:

{

"type"
:
"
item
"
,

"id"
:
"
leather_backpack
"
,

"name"
:
"
Leather Backpack
"
,

"category"
:
"
Container
"
,

"itemId"
:
"
0x0E76
"
,

"hue"
:
"
hue(10:80)
"
,

"goldValue"
:
"
dice(2d8+12)
"
,

"lootType"
:
"
Regular
"
,

"stackable"
:
false
,

"isMovable"
:
true

}

Example startup item template:

{

"type"
:
"
item
"
,

"id"
:
"
inner_torso
"
,

"category"
:
"
Start Clothes
"
,

"itemId"
:
"
0x1F7B
"
,

"hue"
:
"
4375
"
,

"goldValue"
:
"
dice(1d4+1)
"
,

"weight"
:
1

}

Example mobile template:

{

"type"
:
"
mobile
"
,

"id"
:
"
orione
"
,

"name"
:
"
Orione
"
,

"category"
:
"
animals
"
,

"body"
:
"
0xC9
"
,

"skinHue"
:
779
,

"hairStyle"
:
0
,

"brain"
:
"
orion
"

}

Resolution model:

* JSON loading parses to typed specs (HueSpec,GoldValueSpec)
* final random values are resolved when creating runtime entities (not at JSON load time)

## Solution Structure

* src/Moongate.Server: host/bootstrap, game loop, network orchestration, session/event services.
* src/Moongate.Network.Packets: packet contracts, descriptors, registry, packet definitions.
* src/Moongate.Generators: unified source generators for packets, handlers, metrics, script-module registry, and version metadata.
* src/Moongate.UO.Data: UO domain data types and utility models.
* src/Moongate.Core: shared low-level utilities.
* src/Moongate.Network: TCP/network primitives.
* src/Moongate.Scripting: Lua engine service, script modules, script loaders, and scripting helpers.
* src/Moongate.Server/Http: embedded ASP.NET Core host service used by the server bootstrap.
* tests/Moongate.Tests: unit tests.
* benchmarks/Moongate.Benchmarks: BenchmarkDotNet performance suite.
* docs/: documentation and project notes (plans, sprints, protocol notes, journal).

## Source Generators (AOT)

Moongate uses source generators to reduce runtime reflection/discovery work and improve Native AOT compatibility and startup performance.

Current generator project:

* Moongate.GeneratorsGenerates packet table/registry wiring andPacketDefinitionconstants from packet metadata.Generates bootstrap packet-listener registrations from[RegisterPacketHandler(...)].Generates bootstrap game-event-listener subscriptions from[RegisterGameEventListener].Generates bootstrap file-loader registrations from[RegisterFileLoader(order)].Generates metric snapshot mappers from metric-decorated models.Generates script module registries from[ScriptModule(...)]inMoongate.ScriptingandMoongate.Server.GeneratesVersionUtilsmetadata for server version/codename.
* Generates packet table/registry wiring andPacketDefinitionconstants from packet metadata.
* Generates bootstrap packet-listener registrations from[RegisterPacketHandler(...)].
* Generates bootstrap game-event-listener subscriptions from[RegisterGameEventListener].
* Generates bootstrap file-loader registrations from[RegisterFileLoader(order)].
* Generates metric snapshot mappers from metric-decorated models.
* Generates script module registries from[ScriptModule(...)]inMoongate.ScriptingandMoongate.Server.
* GeneratesVersionUtilsmetadata for server version/codename.

Why this helps for AOT:

* Moves dynamic mapping logic from runtime to compile time.
* Reduces dependency on reflection-based registration paths.
* Improves deterministic startup behavior.

## Event And Packet Separation

Moongate uses a strict separation between inbound protocol parsing and outbound event projections:

* IPacketListenerhandles inbound packets only (Client -> Server) and applies domain use-cases.
* Domain services publishIGameEventmessages throughIGameEventBusService.
* Game event listeners are declared withIGameEventListener<TEvent>and auto-subscribed at bootstrap via[RegisterGameEventListener].
* IOutboundEventListener<TEvent>handles outbound side-effects from domain events (for example enqueueing packets).
* RegisterOutboundEventListener<TEvent, TListener>()is the bootstrap helper to register outbound listeners as hosted services with priority.
* IOutgoingPacketQueueandIOutboundPacketSenderdeliver outbound packets on the game-loop/network boundary.

## Game Loop Scheduling

The server loop is timestamp-driven (monotonicStopwatch) rather than fixed-sleep tick stepping:

* GameLoopServicecomputes current loop timestamp and callsITimerService.UpdateTicksDelta(...).
* TimerWheelServiceaccumulates elapsed milliseconds and advances only the required number of wheel ticks.
* This keeps timer semantics stable while adapting to real runtime load.
* Optional idle throttling (Game.IdleCpuEnabled,Game.IdleSleepMilliseconds) sleeps briefly when no work was processed.

### Background Jobs And Main-Thread Dispatch

Moongate providesIBackgroundJobServiceto run non-gameplay work in parallel and safely marshal results back to the game loop thread.

Use it for:

* file parsing/import tasks
* image generation and offline processors
* CPU/I/O work that does not directly mutate world state

Do not mutate gameplay state directly inside background workers.Post results back to game loop callbacks instead.

Example:

public

sealed

class

SeedImportService

{


private

readonly

IBackgroundJobService

_backgroundJobService
;


public

SeedImportService
(
IBackgroundJobService

backgroundJobService
)


{


_backgroundJobService

=

backgroundJobService
;


}


public

void

ImportAsync
(
)


{


_backgroundJobService
.
RunBackgroundAndPostResultAsync
(


async

(
)

=>

await

LoadSeedStatsAsync
(
)
,

 result
=>


{


// This callback executes on game-loop thread.


ApplyStatsToRuntime
(
result
)
;


}
,

 ex
=>


{


// Also marshaled on game-loop thread.


Log
.
Error
(
ex
,

"Seed import failed."
)
;


}


)
;


}

}

## Requirements

* .NET SDK 10.0.x

## Server Startup Tutorial

This is the recommended first-time setup to run the server locally.

1. Prepare directories:* MOONGATE_ROOT_DIRECTORY: server root (config, save, logs, scripts, templates).
* MOONGATE_UO_DIRECTORY: Ultima Online client data directory.
2. Export env vars:

export
 MOONGATE_ROOT_DIRECTORY=
"
$HOME
/moongate
"

export
 MOONGATE_UO_DIRECTORY=
"
/path/to/uo-client
"

1. Restore/build/test:

dotnet restore
dotnet build
dotnet
test

1. Start server:

dotnet run --project src/Moongate.Server

1. First startup behavior:* Ifmoongate.jsonis missing, it is created inMOONGATE_ROOT_DIRECTORY.
* Asset/data files are copied only when missing.
* If no accounts exist, a default admin is created.
2. Optional admin credentials override:

export
 MOONGATE_ADMIN_USERNAME=
"
admin
"

export
 MOONGATE_ADMIN_PASSWORD=
"
change-me-now
"

1. Verify runtime:* Game TCP server: port2593
* HTTP endpoints (default):http://localhost:8088/,http://localhost:8088/health,http://localhost:8088/metrics,http://localhost:8088/scalar
* Logs:MOONGATE_ROOT_DIRECTORY/logs

## Environment Configuration

Moongate now supports full configuration override through environment variables.

* Prefix:MOONGATE_
* Nested properties: use__(double underscore)
* Precedence:MOONGATE_*env vars overridemoongate.json

Example:

* MOONGATE_HTTP__PORT=8088
* MOONGATE_HTTP__JWT__ISSUER=moongate-http
* MOONGATE_SPATIAL__SECTOR_ENTER_SYNC_RADIUS=3

Supported config env variables:

* Core:MOONGATE_ROOT_DIRECTORYMOONGATE_UO_DIRECTORYMOONGATE_LOG_LEVELMOONGATE_LOG_PACKET_DATAMOONGATE_IS_DEVELOPER_MODE
* MOONGATE_ROOT_DIRECTORY
* MOONGATE_UO_DIRECTORY
* MOONGATE_LOG_LEVEL
* MOONGATE_LOG_PACKET_DATA
* MOONGATE_IS_DEVELOPER_MODE
* HTTP:MOONGATE_HTTP__IS_ENABLEDMOONGATE_HTTP__PORTMOONGATE_HTTP__WEBSITE_URLMOONGATE_HTTP__IS_OPEN_API_ENABLEDMOONGATE_HTTP__JWT__IS_ENABLEDMOONGATE_HTTP__JWT__SIGNING_KEYMOONGATE_HTTP__JWT__ISSUERMOONGATE_HTTP__JWT__AUDIENCEMOONGATE_HTTP__JWT__EXPIRATION_MINUTES
* MOONGATE_HTTP__IS_ENABLED
* MOONGATE_HTTP__PORT
* MOONGATE_HTTP__WEBSITE_URL
* MOONGATE_HTTP__IS_OPEN_API_ENABLED
* MOONGATE_HTTP__JWT__IS_ENABLED
* MOONGATE_HTTP__JWT__SIGNING_KEY
* MOONGATE_HTTP__JWT__ISSUER
* MOONGATE_HTTP__JWT__AUDIENCE
* MOONGATE_HTTP__JWT__EXPIRATION_MINUTES
* Game:MOONGATE_GAME__SHARD_NAMEMOONGATE_GAME__TIMER_TICK_MILLISECONDSMOONGATE_GAME__TIMER_WHEEL_SIZEMOONGATE_GAME__IDLE_CPU_ENABLEDMOONGATE_GAME__IDLE_SLEEP_MILLISECONDS
* MOONGATE_GAME__SHARD_NAME
* MOONGATE_GAME__TIMER_TICK_MILLISECONDS
* MOONGATE_GAME__TIMER_WHEEL_SIZE
* MOONGATE_GAME__IDLE_CPU_ENABLED
* MOONGATE_GAME__IDLE_SLEEP_MILLISECONDS
* Metrics:MOONGATE_METRICS__ENABLEDMOONGATE_METRICS__INTERVAL_MILLISECONDSMOONGATE_METRICS__LOG_ENABLEDMOONGATE_METRICS__LOG_TO_CONSOLEMOONGATE_METRICS__LOG_LEVEL
* MOONGATE_METRICS__ENABLED
* MOONGATE_METRICS__INTERVAL_MILLISECONDS
* MOONGATE_METRICS__LOG_ENABLED
* MOONGATE_METRICS__LOG_TO_CONSOLE
* MOONGATE_METRICS__LOG_LEVEL
* Persistence:MOONGATE_PERSISTENCE__SAVE_INTERVAL_SECONDS
* MOONGATE_PERSISTENCE__SAVE_INTERVAL_SECONDS
* Spatial:MOONGATE_SPATIAL__LAZY_SECTOR_ITEM_LOAD_ENABLEDMOONGATE_SPATIAL__SECTOR_WARMUP_RADIUSMOONGATE_SPATIAL__SECTOR_ENTER_SYNC_RADIUSMOONGATE_SPATIAL__LAZY_SECTOR_ENTITY_LOAD_RADIUSMOONGATE_SPATIAL__SECTOR_UPDATE_BROADCAST_RADIUSMOONGATE_SPATIAL__LIGHT_WORLD_START_UTCMOONGATE_SPATIAL__LIGHT_SECONDS_PER_UO_MINUTE
* MOONGATE_SPATIAL__LAZY_SECTOR_ITEM_LOAD_ENABLED
* MOONGATE_SPATIAL__SECTOR_WARMUP_RADIUS
* MOONGATE_SPATIAL__SECTOR_ENTER_SYNC_RADIUS
* MOONGATE_SPATIAL__LAZY_SECTOR_ENTITY_LOAD_RADIUS
* MOONGATE_SPATIAL__SECTOR_UPDATE_BROADCAST_RADIUS
* MOONGATE_SPATIAL__LIGHT_WORLD_START_UTC
* MOONGATE_SPATIAL__LIGHT_SECONDS_PER_UO_MINUTE
* Scripting:MOONGATE_SCRIPTING__ENABLE_FILE_WATCHER
* MOONGATE_SCRIPTING__ENABLE_FILE_WATCHER
* Email:MOONGATE_EMAIL__IS_ENABLEDMOONGATE_EMAIL__FROM_ADDRESSMOONGATE_EMAIL__FALLBACK_LOCALEMOONGATE_EMAIL__SMTP__HOSTMOONGATE_EMAIL__SMTP__PORTMOONGATE_EMAIL__SMTP__USE_SSLMOONGATE_EMAIL__SMTP__USERNAMEMOONGATE_EMAIL__SMTP__PASSWORD
* MOONGATE_EMAIL__IS_ENABLED
* MOONGATE_EMAIL__FROM_ADDRESS
* MOONGATE_EMAIL__FALLBACK_LOCALE
* MOONGATE_EMAIL__SMTP__HOST
* MOONGATE_EMAIL__SMTP__PORT
* MOONGATE_EMAIL__SMTP__USE_SSL
* MOONGATE_EMAIL__SMTP__USERNAME
* MOONGATE_EMAIL__SMTP__PASSWORD

Additional runtime env variables (not part ofMoongateConfig):

* MOONGATE_ADMIN_USERNAME
* MOONGATE_ADMIN_PASSWORD
* MOONGATE_UI_DIST
* MOONGATE_HTTP_JWT_SIGNING_KEY(legacy explicit fallback;MOONGATE_HTTP__JWT__SIGNING_KEYis preferred)

### Docker Compose Example

services
:

moongate
:

image
:
tgiachi/moongate:latest


environment
:

MOONGATE_ROOT_DIRECTORY
:
/data/moongate


MOONGATE_UO_DIRECTORY
:
/data/uo


MOONGATE_HTTP__PORT
:
"
8088
"


MOONGATE_HTTP__IS_OPEN_API_ENABLED
:
"
true
"


MOONGATE_HTTP__JWT__SIGNING_KEY
:
"
change-me
"


MOONGATE_SPATIAL__SECTOR_ENTER_SYNC_RADIUS
:
"
3
"


MOONGATE_SPATIAL__SECTOR_UPDATE_BROADCAST_RADIUS
:
"
3
"


MOONGATE_SPATIAL__LIGHT_WORLD_START_UTC
:
"
1997-09-01T00:00:00Z
"


MOONGATE_SPATIAL__LIGHT_SECONDS_PER_UO_MINUTE
:
"
5
"


MOONGATE_PERSISTENCE__SAVE_INTERVAL_SECONDS
:
"
60
"


MOONGATE_EMAIL__IS_ENABLED
:
"
true
"


MOONGATE_EMAIL__SMTP__HOST
:
"
smtp.example.com
"


MOONGATE_EMAIL__SMTP__PORT
:
"
587
"


MOONGATE_EMAIL__SMTP__USE_SSL
:
"
true
"


MOONGATE_EMAIL__SMTP__USERNAME
:
"
smtp-user
"


MOONGATE_EMAIL__SMTP__PASSWORD
:
"
smtp-pass
"


volumes
:
 -
./moongate_data:/data/moongate

 -
./uo:/data/uo:ro


ports
:
 -
"
2593:2593
"

 -
"
8088:8088
"

## Quick Start

dotnet restore
dotnet build
dotnet
test

dotnet run --project src/Moongate.Server

By default, the server starts with packet data logging enabled inProgram.cs.

Console logging:

* Custom Serilog console sink with output template compatible formatting.
* Level-based colored output in terminal (Spectre.Console).
* Placeholder values (message properties) highlighted with dedicated styling.
* Fixed bottom prompt row (moongate>) when running in an interactive terminal.

HTTP service defaults:

* Http.IsEnabled = true
* Http.Port = 8088
* Http.WebsiteUrl = "http://localhost"
* Http.IsOpenApiEnabled = true
* Base endpoint:/
* Health endpoint:/health
* OpenAPI JSON:/openapi/v1.json
* Scalar UI:/scalar
* Users API:GET /api/usersGET /api/users/{accountId}POST /api/usersPUT /api/users/{accountId}DELETE /api/users/{accountId}
* GET /api/users
* GET /api/users/{accountId}
* POST /api/users
* PUT /api/users/{accountId}
* DELETE /api/users/{accountId}

## Command System

Commands now use a hybrid model:

* Primary path (C# built-ins):ICommandExecutor+[RegisterConsoleCommand(...)]Discovered and registered at compile-time byConsoleCommandRegistrationGeneratorExecutors are registered as DryIoc singletons
* Discovered and registered at compile-time byConsoleCommandRegistrationGenerator
* Executors are registered as DryIoc singletons
* Secondary path (dynamic/Lua/future): manualICommandSystemService.RegisterCommand(...)Kept intentionally for runtime registration scenarios
* Kept intentionally for runtime registration scenarios

Authorization behavior:

* Console source is always evaluated asAccountType.Administrator.
* In-game source is evaluated usingGameSession.AccountType(set during login).
* If source is valid but role is too low, command execution is rejected with warning output.

Example C# command registration (source-generated):

using

Moongate
.
Server
.
Attributes
;

using

Moongate
.
Server
.
Data
.
Internal
.
Commands
;

using

Moongate
.
Server
.
Interfaces
.
Services
.
Console
;

using

Moongate
.
Server
.
Types
.
Commands
;

using

Moongate
.
UO
.
Data
.
Types
;

[
RegisterConsoleCommand
(


"whoami|me"
,


"Shows basic identity information."
,


CommandSourceType
.
Console

|

CommandSourceType
.
InGame
,


AccountType
.
Regular

)
]

public

sealed

class

WhoAmICommand

:

ICommandExecutor

{


public

Task

ExecuteCommandAsync
(
CommandSystemContext

context
)


{


context
.
Print
(
"You are connected."
)
;


return

Task
.
CompletedTask
;


}

}

Example dynamic/manual registration (runtime, e.g. Lua bridge):

commandSystemService
.
RegisterCommand
(


"lua_ping"
,

 context
=>


{


context
.
Print
(
"pong"
)
;


return

Task
.
CompletedTask
;


}
,


source
:

CommandSourceType
.
Console

|

CommandSourceType
.
InGame
,


minimumAccountType
:

AccountType
.
Regular

)
;

Usage:

* Console: type command directly, for examplehelp.
* In-game: prefix with.in Unicode chat, for example.help.

Built-in commands:

* help|?-> Console + InGame,Regular
* lock|*-> Console only,Administrator
* exit|shutdown-> Console only,Administrator
* add_user-> Console + InGame,Administrator
* send_target-> InGame only,Regular
* orion-> InGame only,Regular(opens target cursor and spawns Orion on selected location)
* teleport|tp-> InGame only,GameMaster(usage:.teleport <mapId> <x> <y> <z>)
* add_item_backpack|.add_item_backpack-> InGame only,GameMaster(usage:.add_item_backpack <templateId>)

## Scripting

Moongate includes a Lua scripting subsystem insrc/Moongate.Scripting, based on MoonSharp.

* LuaScriptEngineServicehandles script execution, callbacks, constants, and function invocation.
* Script modules are exposed with attributes ([ScriptModule],[ScriptFunction]).
* Script module registration is compile-time generated (ScriptModuleRegistry) and invoked from bootstrap.
* LuaScriptLoaderresolves scripts from configured script directories.
* .luarcmetadata generation is included to improve editor tooling.

Current automated coverage includes:

* LuaScriptLoaderfile resolution and load behavior.
* LuaScriptEngineServiceconstants, callbacks, module calls, error path, and naming conversions.
* ScriptResultBuildersuccess/error contract behavior.

Example script callback (for example in<root>/scripts/init.lua):

function

on_player_connected
(
p
)

log
.
info
(
"
Toh! un player s'e' connesso
"
)

end

### NPC Brain Example (brain_loop+on_event)

Mobile template:

{

"type"
:
"
mobile
"
,

"id"
:
"
orc_warrior
"
,

"name"
:
"
an orc warrior
"
,

"body"
:
"
0x11
"
,

"brain"
:
"
orc_warrior
"

}

Lua script (<root>/scripts/ai/orc_warrior.lua):

function

brain_loop
(
npc_id
)

while

true

do


--
 tactical tick sleep in milliseconds


coroutine.yield
(
250
)

end

end

function

on_event
(
event_type
,
from_serial
,
event_obj
)

if

event_type

~=

"
speech_heard
"
or

event_obj

==

nil

then


return


end


local

listener_npc_id

=

event_obj
.
listener_npc_id


local

text

=

event_obj
.
text


if

listener_npc_id

==

nil

or

text

==

nil

then


return


end


if

string.find
(
string.lower
(
text
),
"
hello
"
,
1
,
true
)
then


log
.
info
(
"
NPC
"
..

tostring
(
listener_npc_id
)
..

"
 heard hello from
"
..

tostring
(
from_serial
))

end

end

Notes:

* brainin mobile templates is treated as a brain id.
* Scripts are loaded frommoongate_data/scripts/**(usually viarequire(...)ininit.lua).
* brain_loopis resumed by the runner and can control next wake time viacoroutine.yield(ms).
* on_eventis invoked with(eventType, fromSerial, eventObject).
* Current event type emitted by the brain runner:speech_heard.
* eventObjectcontains:listener_npc_id,speaker_id,text,speech_type,map_id, andlocation(x,y,z).

### Visual Effects From Lua

Moongate now exposes visual effect helpers both on mobile proxies and as a global module:

local

npc

=

mobile
.
get
(
0x00000030
)

if

npc

then


npc
:
SetEffect
(
0x3728
,
10
,
10
,
0
,
0
,
2023
)

end

--
 broadcast location effect

effect
.
send
(
1
,
3613
,
2585
,
0
,
0x3728
,
10
,
10
,
0
,
0
,
2023
)

--
 single target effect

effect
.
send_to_player
(
0x00000022
,
3613
,
2585
,
0
,
0x3728
,
10
,
10
,
0
,
0
,
5023
)

Related runtime events:

* MobilePlayEffectEvent(broadcast in range)
* PlayEffectToPlayerEvent(single session via character id)

### ItemScriptIdDispatch

Items can definescriptIdin templates and runtime entities (UOItemEntity.ScriptId).IItemScriptDispatcherresolvesscriptIdas a Lua table and invokes hook functions on that table.

Dispatch convention:

* IfscriptIdis set and notnone: table name is normalizedscriptId(non-alphanumeric ->_, lowercase)
* IfscriptId == "none": fallback table resolution from item name
* First candidate:<normalized_item_name>
* Second candidate:items_<normalized_item_name>
* Hook names:
* single_click->on_click
* double_click->on_double_click

GM Lua command examples shipped today:

* moongate_data/scripts/commands/gm/eclipse.lua->.eclipse
* moongate_data/scripts/commands/gm/set_world_light.lua->.set_world_light <0-255>
* moongate_data/scripts/commands/gm/teleports.lua->.teleports

Example:

* scriptId = "items.healing-potion"
* Lua table resolved:items_healing_potion
* On single click dispatcher tries:items_healing_potion.on_click(and aliases)

Example template:

{

"type"
:
"
item
"
,

"id"
:
"
healing_potion
"
,

"name"
:
"
a healing potion
"
,

"itemId"
:
"
0x0F0C
"
,

"scriptId"
:
"
items.healing_potion
"

}

Example Lua:

items_healing_potion

=
 {

on_click

=

function
(
ctx
)

log
.
info
(
"
Potion clicked, serial=
"
..

tostring
(
ctx
.
item
.
serial
))

end
,

on_double_click

=

function
(
ctx
)

log
.
info
(
"
Potion double clicked by mobile=
"
..

tostring
(
ctx
.
mobile_id
))

end

}

Fallback example (scriptId = "none"and item nameBrick):

brick

=
 {

on_double_click

=

function
(
ctx
)

log
.
info
(
"
Brick double-click from session
"
..

tostring
(
ctx
.
session_id
))

end

}

ctxpayload keys:

* hook
* session_id
* mobile_id
* metadata
* item:
* serial,script_id,name,map_id,item_id,amount,hue,location.{x,y,z}

### Lua Gump Example

Moongate now supports two complementary gump flows:

* file-based layout table (recommended) withgump.send_layout(...)
* runtime fluent builder withgump.create()/gump.send(...)

File-based layout conventions:

* store gump files inmoongate_data/scripts/gumps/**.lua
* each file returns a table withuiand optionalhandlers
* button click wiring is declarative:onclick = "handler_name"
* optionalctxcan be passed togump.send_layout(...)for text placeholders ($ctx.name,$ctx.level, ...)

Example file (moongate_data/scripts/gumps/test_shop.lua):

return
 {

ui

=
 {
 {
type

=

"
page
"
,
index

=

0
 },
 {
type

=

"
background
"
,
x

=

0
,
y

=

0
,
gump_id

=

9200
,
width

=

320
,
height

=

180
 },
 {
type

=

"
label
"
,
x

=

20
,
y

=

20
,
hue

=

1152
,
text

=

"
Hello $ctx.name
"
},
 {
type

=

"
button
"
,
id

=

1
,
x

=

20
,
y

=

130
,
normal_id

=

4005
,
pressed_id

=

4007
,
onclick

=

"
open_next
"
}
 },

handlers

=
 {

open_next

=

function
(
cb_ctx
)

log
.
info
(
"
Button clicked:
"
..

tostring
(
cb_ctx
.
button_id
))

end

 }
}

Usage:

local

layout

=

require
(
"
gumps/test_shop
"
)

local

ui_ctx

=
 {
name

=

"
Orion
"
,
level

=

42
 }

gump
.
send_layout
(
session_id
,
layout
,
character_id
,
0xB300
,
120
,
80
,
ui_ctx
)

Runtime builder mode remains available for dynamic/UI-generated-at-runtime scenarios.

## Scripts

Repository helper scripts inscripts/:

* scripts/build_image.sh: builds the Docker image usingdocker buildx, with options for tag, platform, push, and no-cache.
* scripts/run_aot.sh: publishes and runs the server with NativeAOT settings for local AOT verification.
* scripts/run_benchmarks.sh: runs BenchmarkDotNet benchmarks (markdown+csvexporters).
* scripts/run_benchmarks_compare.sh: runs side-by-sideJIT vs NativeAOTmicro-benchmark comparison and writesBenchmarkDotNet.Artifacts/results/aot-vs-jit.md.
* scripts/run_benchmarks_lua.sh: runs Lua script engine benchmarks only (JIT, MoonSharp is NativeAOT-incompatible). Accepts extra BenchmarkDotNet args.

## Benchmarks

Run locally:

./scripts/run_benchmarks.sh --filter
'
*
'

Latest local snapshot (2026-02-23,BenchmarkDotNet 0.14.0, macOSDarwin 25.3.0, AppleM4 Max,.NET 10.0.3):

Benchmark

Mean

Allocated

PacketParsingBenchmark.ParseLoginSeedPacket

94.82 ns

664 B

PacketSerializationBenchmark.WriteServerListPacket

64.19 ns

128 B

PacketStreamParsingBenchmark.ParseMixedPacketStreamInChunks

24.25 us

56 KB

PacketDispatchBenchmark.DispatchToThreeListeners

68.21 ns

296 B

PacketDispatchBenchmark.DispatchWithoutListeners

8.99 ns

64 B

NetworkCompressionBenchmark.Compress256Bytes

220.76 ns

-

NetworkCompressionBenchmark.CompressAndDecompress1024Bytes

60.03 us

48.10 KB

NetworkCompressionBenchmark.CompressionMiddlewareProcessSend1024Bytes

908.72 ns

1.48 KB

QueueThroughputBenchmark.OutgoingQueueEnqueueThenDrain

24.309 us

-

QueueThroughputBenchmark.MessageBusPublishThenDrain

9.725 us

-

TimerWheelBenchmark.UpdateTicksDelta

2.893 us

4.05 KB

### Gameplay Hot-Path Benchmarks

Run only the new gameplay-focused suites:

dotnet run -c Release --project benchmarks/Moongate.Benchmarks/Moongate.Benchmarks.csproj -- \
 --filter
'
*SpatialWorldServiceBenchmark*
'

'
*ItemServiceBenchmark*
'

'
*PacketGameplayHotPathBenchmark*
'

Latest quick snapshot (2026-03-02,BenchmarkDotNet 0.15.8, macOSDarwin 25.3.0, AppleM4 Max,.NET 10.0.3, quick configLaunch=1/Warmup=1/Iteration=1):

Benchmark

Mean

Allocated

SpatialWorldServiceBenchmark.AddOrUpdateMobiles (500)

75.939 us

74.56 KB

SpatialWorldServiceBenchmark.MoveMobilesAcrossSectors (500)

27.548 us

117.53 KB

SpatialWorldServiceBenchmark.GetPlayersInHotSector (500)

1.769 us

6.16 KB

SpatialWorldServiceBenchmark.AddOrUpdateMobiles (2000)

325.353 us

297.27 KB

SpatialWorldServiceBenchmark.MoveMobilesAcrossSectors (2000)

105.423 us

469.15 KB

SpatialWorldServiceBenchmark.GetPlayersInHotSector (2000)

1.745 us

6.16 KB

ItemServiceBenchmark.MoveItemBetweenContainers

359.772 ns

1.85 KB

ItemServiceBenchmark.DropItemToGroundFromContainer

489.566 ns

2.25 KB

PacketGameplayHotPathBenchmark.ParseMoveRequestPacket

8.930 ns

32 B

PacketGameplayHotPathBenchmark.ParsePickUpItemPacket

8.620 ns

32 B

PacketGameplayHotPathBenchmark.ParseDropItemPacket

11.192 ns

48 B

PacketGameplayHotPathBenchmark.ParseDropWearItemPacket

8.955 ns

32 B

PacketGameplayHotPathBenchmark.ParseMixedGameplayPacketBurst

10.956 ns

36 B

PacketGameplayHotPathBenchmark.WriteObjectInformationPacket

63.047 ns

-

PacketGameplayHotPathBenchmark.WriteDraggingOfItemPacket

51.664 ns

-

Notes:

* This snapshot is intended for fast regression checks, not for publication-grade comparisons.
* Use default/full BenchmarkDotNet settings for release notes and long-term trend baselines.

### Lua Script Engine

Run locally:

./scripts/run_benchmarks_lua.sh

Note: MoonSharp relies on reflection and dynamic code generation — NativeAOT is not supported for this suite.

Latest local snapshot (2026-02-25,BenchmarkDotNet 0.15.8, macOSDarwin 25.3.0, AppleM4 Max,.NET 10.0):

Benchmark

Mean

Allocated

LuaScriptEngineBenchmark.ExecuteSimpleScriptCached

328.87 ns

800 B

LuaScriptEngineBenchmark.ExecuteLoopScriptCached

5.68 us

19.67 KB

LuaScriptEngineBenchmark.ExecuteSimpleScriptUncached

6.28 us

6.12 KB

LuaScriptEngineBenchmark.CallFunctionNoArgs

49.22 ns

256 B

LuaScriptEngineBenchmark.CallFunctionWithArgs

135.40 ns

864 B

Generated reports are stored in:

* BenchmarkDotNet.Artifacts/results/*.md
* BenchmarkDotNet.Artifacts/results/*.csv

### AOT vs JIT

Run side-by-side comparison:

./scripts/run_benchmarks_compare.sh

Latest comparison snapshot (2026-02-23,net10.0, AppleM4 Max,osx-arm64):

Benchmark

JIT Mean

AOT Mean

Speedup (JIT/AOT)

Compress256Bytes

934.48 ns

319.04 ns

2.93x

CompressAndDecompress1024Bytes

59.60 us

102.20 us

0.58x

CompressionMiddlewareProcessSend1024Bytes

974.86 ns

1.34 us

0.73x

ParseLoginSeedPacket

360.97 ns

71.66 ns

5.04x

ParseMixedPacketStreamInChunks

26.10 us

37.71 us

0.69x

WriteServerListPacket

585.93 ns

98.31 ns

5.96x

Detailed report:

* BenchmarkDotNet.Artifacts/results/aot-vs-jit.md

## Stress Test (Socket UO, Black-Box)

Use the dedicated stress runner to validate server stability with real UO socket clients.

Scenario target (default):

* 100concurrent clients
* 300sduration
* account bootstrap via HTTP users API
* login + enter world + continuous movement loop
* SLO checks:login success rate>= 99%unexpected disconnects= 0movement ACK p95< 200ms
* login success rate>= 99%
* unexpected disconnects= 0
* movement ACK p95< 200ms

Run:

dotnet run --project tools/Moongate.Stress -- \
 --host 127.0.0.1 --port 2593 \
 --http http://localhost:8088 \
 --clients 100 --duration 300 --ramp-up-per-second 10

When JWT protection is enabled on/api/users, provide admin credentials:

dotnet run --project tools/Moongate.Stress -- \
 --admin-username admin --admin-password your_password

Output:

* console summary with pass/fail and SLO violations
* JSON report atartifacts/stress/latest.json

## Docker

Build the image:

./scripts/build_image.sh -t moongate-server:local

Run the container:

docker run --rm -it \
 -p 2593:2593 \
 -p 8088:8088 \
 -v /path/host/moongate-root:/app \
 -v /path/host/uo-client:/uo:ro \
 --name moongate \
 moongate-server:local

The Docker image publishes a NativeAOT binary and runs it on Alpine (linux-muslruntime).
It also builds the frontend inui/and serves it from/via the HTTP service.
Container defaults:

* MOONGATE_ROOT_DIRECTORY=/app
* MOONGATE_UO_DIRECTORY=/uo
* MOONGATE_UI_DIST=/opt/moongate/ui/dist

/path/host/uo-clientmust contain required UO client files (e.g.client.exe).

Console behavior in Docker:

* Run with-itto enable the interactive prompt UI (moongate>).
* Without TTY (-itomitted), logs still work but prompt interaction is disabled.

## Docker Monitoring Stack

The repository includes a complete monitoring stack understack/:

* Moongate server container
* Prometheus scrapinghttp://moongate:8088/metrics
* Grafana with pre-provisioned datasource and dashboard

Quick start:

cd
 stack
docker compose up -d --build

Useful endpoints:

* Grafana:http://localhost:3000
* Prometheus:http://localhost:9090
* Moongate metrics:http://localhost:8088/metrics

For full setup details, volumes, troubleshooting, and dashboard notes, seestack/README.md.

## Documentation

Project documentation is indocs/.
Published documentation is available at:

* https://moongate-community.github.io/moongatev2/
* Docs home:docs/Home.md
* Development plan:docs/plans/moongate-v2-development-plan.md
* Current status snapshot:docs/plans/status-2026-02-19.md
* Sprint tracking:docs/sprints/sprint-001.md
* Sprint closeout:docs/sprints/sprint-001-closeout-2026-02-18.md
* Protocol notes index:docs/protocol/README.md

## Development Notes

* Shared build/analyzer/version settings are centralized inDirectory.Build.props.
* Current global version baseline:0.17.0.
* CI validates build/tests/coverage/quality/security; release and Docker image publishing run through dedicated workflows.

## Contributing

We welcome contributions. Please fork the repository and submit pull requests with your changes.
Make sure code follows the project coding standards and includes appropriate tests.

## License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0).
SeeLICENSEfor details.

## About

Moongate is modern Ultima Online server built from scratch in C# with AOT compilation for high performance and nostalgic gameplay experience.

moongate-community.github.io/moongatev2/

### Topics

 rpg

 high-performance

 mmo

 mmorpg

 retrogaming

 runuo

 servuo

 ultimaonline

 uox3

 modernuo

### Resources

 Readme



### License

 GPL-3.0 license


### Code of conduct

 Code of conduct


### Uh oh!

There was an error while loading.Please reload this page.





Activity


Custom properties


### Stars

68

 stars


### Watchers

1

 watching


### Forks

4

 forks


 Report repository



## Releases31

v0.31.0

 Latest



Mar 6, 2026



+ 30 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.





## Contributors3

* tgiachiTom
* semantic-release-botSemantic Release Bot
* github-actions[bot]

## Languages

* C#95.4%
* TypeScript2.3%
* JavaScript1.2%
* Lua0.7%
* Shell0.2%
* CSS0.1%
* Other0.1%
