---
title: 'GitHub - ahmedkhaleel2004/gitdiagram: Free, simple, fast interactive diagrams for any GitHub repository · GitHub'
url: https://github.com/ahmedkhaleel2004/gitdiagram
site_name: github
content_file: github-github-ahmedkhaleel2004gitdiagram-free-simple-fast
fetched_at: '2026-09-18T14:48:01.976509'
original_url: https://github.com/ahmedkhaleel2004/gitdiagram
author: ahmedkhaleel2004
description: Free, simple, fast interactive diagrams for any GitHub repository - ahmedkhaleel2004/gitdiagram
---

ahmedkhaleel2004

 

/

gitdiagram

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork1.3k
* Star16.3k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

381 Commits
381 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
docs
docs
 
 
patches
patches
 
 
public
public
 
 
scripts
scripts
 
 
src
src
 
 
.dockerignore
.dockerignore
 
 
.env.example
.env.example
 
 
.gitignore
.gitignore
 
 
.vercelignore
.vercelignore
 
 
CLAUDE.md
CLAUDE.md
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
bun.lock
bun.lock
 
 
components.json
components.json
 
 
eslint.config.mjs
eslint.config.mjs
 
 
next.config.js
next.config.js
 
 
package.json
package.json
 
 
postcss.config.js
postcss.config.js
 
 
prettier.config.js
prettier.config.js
 
 
railway.json
railway.json
 
 
tailwind.config.ts
tailwind.config.ts
 
 
tsconfig.json
tsconfig.json
 
 
vercel.json
vercel.json
 
 
vitest.config.ts
vitest.config.ts
 
 
vitest.setup.ts
vitest.setup.ts
 
 
View all files

## Repository files navigation

# GitDiagram

Turn any public or private GitHub repository into an interactive architecture diagram in seconds.

You can also replacehubwithdiagramin a GitHub URL to open its diagram.

Sponsor slot:Reach developers while they are actively exploring codebases.Sponsor GitDiagram.

## Features

* Architecture-first diagrams:converts a repository tree, README, and bounded source excerpts into a system-level graph instead of merely drawing folders.
* Interactive source links:click a component to open its real file or directory on GitHub.
* Streaming generation:see the explanation arrive while the graph is planned.
* Private repositories:provide a GitHub token locally in the browser; private artifacts use a separate protected storage namespace.
* Export:copy Mermaid source or download the rendered diagram as PNG.
* Provider choice:OpenAI by default, with OpenRouter available for self-hosted deployments.

## Stack

* Application:Next.js 16 App Router, React 19, TypeScript, Tailwind CSS, and Radix UI
* Generation API:same-origin Next.js Route Handlers running on Vercel's Bun runtime
* Storage:Cloudflare R2 for diagram artifacts
* Coordination:Upstash Redis for quota accounting, cancellation, locks, and short-lived failure state
* AI:OpenAI or OpenRouter throughAI_PROVIDER
* Analytics:PostHog
* Deployment:Vercel is the only live runtime; an offline Railway/Docker recipe is retained for disaster recovery

There is no separate FastAPI implementation, Postgres database, or Neon runtime.

## Production architecture

Vercel serves both the UI and the generation endpoints:

* /api/generate/costestimates a run after bounded GitHub ingestion, same-origin and rate limited.
* /api/generate/streamstreams Server-Sent Events for explanation and graph progress.
* /api/generate/cancelrecords authenticated, same-origin cancellation signals.
* /api/diagram-statereads and writes the persisted result contract.
* /api/healthzprovides a lightweight deployment health check.

Long-running generation uses a 300-second Vercel function budget with a shorter application deadline so quota reconciliation and persistence still have time to finish. Requests use explicit upstream deadlines, retries, structured logs, heartbeats, and distributed cancellation rather than process-local state.

The default managed OpenAI pipeline uses one GPT-5.6 Luna request at medium reasoning to produce a source-grounded graph and short streamed overview. The model returns a compact graph without redundant descriptions or type captions. Graphs are validated and compiled deterministically; additional Luna calls are reserved for structural repairs or one recovery after an 18-second slow request. The slow connection is cancelled before its replacement starts; its unavailable partial usage is included as an estimated cost. Managed GPT-5.6 requests explicitly use Fast mode (service_tier: "priority"); estimates include its premium, and final costs use the model and tier actually served. User-supplied keys retain standard service and their configured model. Explicit model overrides and OpenRouter retain the two-stage pipeline. Output token estimates reserve quota but do not cap provider output.

The same Next.js application can also build into a minimal, non-root standalone Docker image for Railway. No Railway service, source connection, or Railway domain is kept live. The checked-inDockerfileandrailway.jsonare a cold recovery recipe that can recreate the full application later without reviving a second backend implementation. Seedocs/deployment-failover.md.

## How generation works

1. GitDiagram fetches the repository's default branch, recursive tree, and README through the GitHub API. Truncated trees and oversized inputs are rejected before model work begins.
2. GitDiagram fetches bounded, integrity-checked source excerpts. Selection favors substantive runtime modules, distributes excerpts across long files, and preserves import bindings for sampled calls.
3. One managed Luna request streams a short architecture overview followed by a strict graph: groups, nodes, edges, shapes, labels, and repository paths. Explicit model overrides and user-supplied keys retain the separate explanation/graph flow.
4. The server validates identifiers, graph connectivity, limits, and every linked path against the actual repository. Invalid output is retried with focused feedback.
5. A deterministic compiler converts the validated AST to Mermaid with total text escaping and GitHub-only links.
6. The browser sanitizes the source, renders Mermaid in strict security mode, sanitizes the resulting SVG, and enforces the link allowlist again.
7. Successful artifacts and terminal audit state are persisted so later visits can reopen the diagram without another model call.

The full Mermaid parser remains in the test suite as a compiler contract test. It is deliberately not loaded into the production generation function, keeping the server bundle small without weakening diagram validation or browser safety.

## State

* Successful public generations:R2 object keyed by repository
* Successful private generations:separate R2 namespace derived with a server-side secret
* Complimentary quota and active cancellation tokens:Upstash Redis
* Terminal failures without a saved artifact:short-lived Upstash state
* Concurrent writes:distributed lock plus newest-session-wins persistence

## Private repositories

SelectPrivate Reposin the header and provide a fine-grained GitHub personal access token that can read the target repository. The token is sent only with the relevant same-origin request and is never embedded in public diagram links.

## Local development

For exact prerequisites and environment details, seedocs/dev-setup.md.

git clone https://github.com/ahmedkhaleel2004/gitdiagram.git

cd
 gitdiagram
bun install
cp .env.example .env
bun run dev

Openhttp://localhost:3000.

At minimum, configure R2, Upstash, and one AI provider in.env. A GitHub PAT or GitHub App is optional but strongly recommended for higher GitHub API limits.

Run the complete local gate before opening a pull request:

bun run lint
bun run typecheck
bun run 
test

bun run build

## Contributing

Contributions are welcome. Please open an issue or pull request with a focused description and verification notes.

## Acknowledgements

Inspired byRomain Courtois'sGitingest.