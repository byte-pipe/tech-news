---
title: 'GitHub - DuarteSantos8/openGym: Self-hosted gym & body-weight tracker — plan routines, log workouts (supersets, warm-ups, cardio), see which muscles are trained, fatigued or detrained, import from FitNotes/Strong/Hevy, passkey login. Your data, your server. · GitHub'
url: https://github.com/DuarteSantos8/openGym
site_name: github
content_file: github-github-duartesantos8opengym-self-hosted-gym-body-w
fetched_at: '2026-10-06T16:47:43.673971'
original_url: https://github.com/DuarteSantos8/openGym
author: DuarteSantos8
description: Self-hosted gym & body-weight tracker — plan routines, log workouts (supersets, warm-ups, cardio), see which muscles are trained, fatigued or detrained, import from FitNotes/Strong/Hevy, passkey login. Your data, your server. - DuarteSantos8/openGym
---

DuarteSantos8

 

/

openGym

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork674
* Star4.5k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

1,197 Commits
1,197 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.gitea
.gitea
 
 
.github
.github
 
 
.gitlab
.gitlab
 
 
api
api
 
 
assets
assets
 
 
docs
docs
 
 
frontend
frontend
 
 
kubernetes
kubernetes
 
 
mcp
mcp
 
 
scripts
scripts
 
 
web
web
 
 
website
website
 
 
.dockerignore
.dockerignore
 
 
.env.example
.env.example
 
 
.gitignore
.gitignore
 
 
.gitlab-ci.yml
.gitlab-ci.yml
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
NOTICE.md
NOTICE.md
 
 
README.md
README.md
 
 
ROADMAP.md
ROADMAP.md
 
 
SECURITY.md
SECURITY.md
 
 
docker-compose.yml
docker-compose.yml
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
renovate.json
renovate.json
 
 
View all files

## Repository files navigation

A self-hosted gym and body-weight tracker you actually own.

Plan your week, run guided workouts, log every set and your body weight —on your phone, synced across your devices, behind your own passkey login.

Website·Live demo·Android APK·Self-hosting guide·Roadmap·Changelog

Home
 · today's workout and weight

Guided workout
 · demos and sets

Stats
 · heatmap, charts and PRs

## Why openGym

Most workout apps keep your data on their servers, push you towards a subscription, or vanish
when the company does. openGym runs on your own box, keeps your data in a folder you control, and
is yours to fork. It still behaves like a modern app: installable on the home screen, passkey
sign-in, works offline, syncs between your phone and your laptop.

No account on someone else's server, no subscription, no ads, no telemetry. Onedocker compose upand it's running.

Thein-browser demois the real app with example data,
if you want to try it before installing anything.

## Features

Planning

* A routine per weekday over a library of1,324 exerciseswith animated demos, searchable and
browsable by muscle on a body map. Filter by the equipment you own.
* Four starter plans (Push/Pull/Legs, Upper/Lower, Full Body, 5×5) that load as ordinary,
editable routines.
* Move a session to another day without touching the weekly plan. The week starts on Monday or
Sunday, your choice.
* Supersets, warm-up sets, drop sets and rest-pause, timed exercises (planks, hangs, carries),
cardio by time and speed, rest time per exercise, planned deloads.
* Your own exercises, with your own photo, GIF or short video. Location data is stripped on the
device before upload.

Training

* Guided sessions: today's workout starts itself, weights are pre-filled from last time, a rest
timer runs between sets, PRs are detected as you go. On a rest day it tells you when the next
session is.
* A quiet workout screen: one menu per exercise, the set number as the set's own menu, card or
list view. Switches in Settings bring the old button rows back if you liked them.
* Optional effort column as RIR or RPE, colour-coded, with a plain-language line per level.
* Plate math for barbell, EZ bar, trap bar and Smith machine, worked out from the plates you own.
* Bodyweight exercises know they carry no load: log reps, add a dip belt if you use one.
* Per-side reps for lunges and single-arm work, the screen stays awake while you train, and a
rest-timer alert can flash the screen for loud gyms.

Progress

* Progression rules per routine or per exercise: linear, Greyskull LP, double progression through a
visible rep range, or adding time. Each target explains why it is that number; missed reps never
add load, stalls trigger a deload.
* Estimated 1RM per exercise with its own curve, Structural Balance ratios (Poliquin, Thibaudeau,
ATG), a year-long activity heatmap.
* A muscle map in three modes: where your volume went, what is still recovering, and what has gone
untrained.
* Body-weight chart against a goal line.
* Edit any saved workout after the fact, log one you did on paper, or move it to the right date.
Records are re-read from the corrected history.

Accounts and data

* Passkeys (Face ID, Touch ID, fingerprint) with per-profile data synced across devices. Password
sign-in can be switched on per instance; new devices pair with a one-time code or QR.
* Two devices editing at once merge instead of overwriting each other (seesync).
* Import from FitNotes, Strong, Hevy (CSV or API key) and Apple Health weight exports. Export
everything as one JSON file whenever you like.
* Share a plan as a small file or print it as a PDF.
* Optional admin dashboard with invite-only signup and an activity log.
* 17 languages, including right-to-left Arabic. Exercise names and instructions are translated
for most of them.

Optional extras, off by default

* AnAI coachthat drafts a week of routines and later suggests changes based on
what you logged. You approve every change. It runs on your server with your own provider key
(Anthropic, OpenAI, Gemini or any OpenAI-compatible endpoint, Ollama included).
* AnMCP serverso an assistant like Claude Desktop can answer questions about your
training history. Read-only and local; not part of the Docker build.

The full list of what changed release by release is in thechangelog.

## Quick start

You needDockerwith Compose.

git clone https://github.com/DuarteSantos8/openGym

cd
 openGym
cp .env.example .env
docker compose pull 
#
 prebuilt images, amd64 + arm64 (skip this to build from source)

docker compose up -d

Openhttp://localhost:8080, tapCreate profile, and you're in. The first start downloads
the exercise media (about 140 MB) once.

To reach it from your phone with passkeys you need HTTPS on a domain; that's a two-line change in.env. Theself-hosting guidewalks through Cloudflare Tunnel, Caddy,
Traefik and nginx, and there are separate guides forHTTPS on a LANandKubernetes.

Note

Images are published from the same tag toregistry.gitlab.com/duartesantos8/opengym/{api,web}(whatdocker-compose.ymlpulls) andghcr.io/duartesantos8/opengym-{api,web}. Swap theimage:lines if you prefer GHCR, or rundocker compose up -d --buildto build locally. Either
way you don't need Node on the host.

Configuration reference
 (all through 
.env
)

Variable

What it does

Default

RP_ID

Hostname passkeys are bound to

localhost

ORIGIN

Full URL the app is served from

http://localhost:8080

WEB_PORT

Host port for the web UI

8080

NGINX_PORT

Port the web container listens on inside the container

80

BACKEND

Name of the API service that 
/api
 is proxied to

api

PORT

Port the API listens on; the web container proxies to the same value

3000

RP_NAME

Name shown in the passkey prompt

openGym

SESSION_DAYS

How long a sign-in lasts, in days

90

ADMIN_UIDS

User ids that get the admin dashboard, comma-separated

(none)

INVITE_ONLY

Require an invite code to create a profile

(off)

ALLOW_GUEST

Offer "Continue without account"; 
0
 requires a profile

(on)

PASSWORD_LOGIN

Offer name-and-password sign-in next to passkeys

(off)

TRUST_PROXY

Let the sign-in throttle read the client address from proxy headers

1
 in 
docker-compose.yml

AUDIT_LOG

Record sign-ins and admin actions; 
0
 records nothing

(on)

AUDIT_MAX

Events kept in the activity log; 
0
 for no limit

5000

AUDIT_DAYS

Days kept in the activity log; 
0
 keeps until 
AUDIT_MAX

90

AUDIT_IP

Record the caller's address: 
off
, 
net
 (network only) or 
full

off

VAPID_SUBJECT

Contact URL sent with push notifications

your 
ORIGIN

API_TARGET

API image to build: 
default
, or 
coach
 with the Claude Agent SDK and Codex CLI

default

COACH_DISABLED

1
 forces the AI coach off instance-wide

(unset)

Push-notification keys are generated on first run into./data/vapid.json.DATA_DIRis pinned to/datainside the container and mapped to./dataon the host; change the volume, not the
variable. Theself-hosting guidecovers every option in detail.

## Phone app

The same codebase builds a standalone app with Capacitor: no account, no server, everything stays
on the phone, with native reminders and a rest countdown in the notification shade.

* Android:download the signed APK from thelatest releaseor thewebsite. Each build sits next to its.sha256, and
the app checks for updates itself. openGym is deliberately not on the Play Store.
* iPhone:Apple doesn't allow installs outside the App Store. Self-host and add the PWA to your
home screen from Safari, or build the native app onto your own device with Xcode.

Details and build instructions:docs/MOBILE.md.

## How it works

* frontend/is React 19 and Vite (React Router, Zustand), built to static files inside Docker.
* api/is plainnode:httpwith two dependencies:@simplewebauthn/serverfor passkeys andweb-pushfor notifications. Everything is stored as JSON under./data.
* web/builds the frontend and serves it with nginx, proxying/apiso the whole app sits on
one origin, which passkeys require.

The training logic (progression rules, 1RM, how a logged session is read back) lives in pure
functions underfrontend/src/lib/with tests beside them. The HTTP API is documented as an
OpenAPI spec inapi/openapi.yaml, browsable atopengym.duarte-santos.ch/api.html.

### How sync works

Each profile's data is one document with a server revision. A device sends the revision it last
saw along with its changes; if another device wrote in between, the server refuses and returns the
current document so the device can merge and retry.

Nothing that hasn't reached the server is discarded on disconnect or sign-out, and the app shows a
banner whenever it's working offline.

### Your data

Everything lives in./dataon your host:

File

Contents

db.json

Profiles and public passkey data

state-<user>.json

Each user's plan, workouts, body weight and settings

audit.log

Admin activity log (no IP addresses unless you turn that on)

secret

Session-cookie signing key

Back up./dataand you've backed up everything. Passkey private keys never reach the server; they
stay in your phone's secure hardware or your password manager.

## Documentation

Thedocumentation indexsorts every guide by who it's for. The most used ones:

I want to

Read

Get a quick answer

FAQ

Set up my own instance

Self-hosting

Use the Android or iPhone app

Phone app

Bring my history from another app

Importing data

Turn on the AI coach

AI coach

Contribute code

Contributing

Report a security problem

Security

## Roadmap

A release roughly every two weeks, each small and themed. The full plan is inROADMAP.md, and the issues sit in theGitHub milestones.

Release

Planned

Theme

v1.3.10

Oct 2026

Session queue and rotation

v1.3.11

Nov 2026

Programmes and phases

v1.3.12–13

Nov–Dec 2026

Progression engine: AMRAP, %1RM, 5/3/1

v1.3.14

Dec 2026

Cardio, exercise alternatives, groups

v1.4.0

Jan 2027

Database storage (the one compatibility break)

v1.4.1–3

Jan–Feb 2027

Search, OIDC login, trainer role

v1.4.4–7

Mar–Apr 2027

iOS app, Health Connect, catalogue, skins

## Community

* Discordfor release announcements, self-hosting help and
quick back-and-forth. Usually the fastest way to get an answer.
* Discussionsfor questions and ideas
you want the next person to find by searching.
* Issuesfor reproducible bugs and agreed-on
work. Login trouble is almost always anRP_ID/ORIGINmismatch; theself-hosting guidecovers it.
* Pull requestsare welcome; start withCONTRIBUTING.md.

### Where the code lives

GitHub is the home of the project.gitlab.com/DuarteSantos8/opengymis a mirror, updated by a GitHub Actions workflow on every push tomainand every release tag. It
exists because its CI builds the release artifacts: the signed APK, the multi-arch images and the
SBOMs. Nothing is merged there by hand. In the changelog,!NNrefers to a GitLab merge request
from the weeks in August and September 2026 when the project lived there.

## How openGym is built

People have asked about this, so plainly:openGym is developed withClaude Code, Anthropic's coding agent. A large share of the
code, tests and documentation is drafted in Claude Code sessions, and the repository carries aCLAUDE.mdwith the project context those sessions start from.

What that does and doesn't mean:

* A person decides and ships.What goes in, what gets reviewed and merged, and every release
are the maintainer's call. Changes are tested on a staging instance and on real phones before
they are tagged.
* Tests hold the logic in place.The training logic is covered by unit tests, and pull requests
run the frontend, API and MCP suites in CI. That is the guard against plausible-looking code
that is wrong, whoever or whatever wrote it.
* The app itself doesn't need an LLM.Nothing in a default install calls an AI service. The AI
coach and the MCP server are opt-in, and the coach only talks to the provider you configure, with
your own key.

Community pull requests are written by their authors, with whatever tools they like, and reviewed
the same way.

## Support

openGym is free and stays free: AGPL, no paid tier, nothing held back for sponsors. If it replaced a
paid tracker for you and you'd like to chip in, there's a coffee button below. A star, a bug report
or a pull request helps just as much.

## License

openGym's own codeis licensed under theGNU AGPL v3.0. You can self-host, use,
modify and share it; if you run a modified version as a network service, you have to offer that
version's source under the same license.

Important

The exercise media is not covered by that license.Exercise metadata and instruction text come
fromExerciseDB v1throughhasaneyldrm/exercises-datasetunder MIT. The
images and animations are third-party content under neither MIT nor the AGPL, and their ownership
is disputed: the dataset attributes them toGym visual, whileExerciseDB/AscendAPIclaims to own them. openGym doesn't redistribute
them (your instance downloads them on first start) and doesn't relicense them. To reuse that
media, clear it with the rights holder first.

Full third-party notices, including the body-diagram geometry, are inNOTICE.md.