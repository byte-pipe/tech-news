---
title: Build Your First (or Next) MCP Server with the TypeScript MCP Template - DEV Community
url: https://dev.to/nickytonline/build-your-first-or-next-mcp-server-with-the-typescript-mcp-template-3k3f
site_name: devto
fetched_at: '2025-10-09T11:07:19.849830'
original_url: https://dev.to/nickytonline/build-your-first-or-next-mcp-server-with-the-typescript-mcp-template-3k3f
author: Nick Taylor
date: '2025-10-07'
description: Build Your First (or Next) MCP Server with the TypeScript MCP Template If you've been... Tagged with typescript, mcp, ai.
tags: '#typescript, #mcp, #ai'
---

# Build Your First (or Next) MCP Server with the TypeScript MCP Template

If you've been wanting to build your own Model Context Protocol (MCP) server but weren't sure where to start, I've got something that might save you a bunch of time. I recently extracted a TypeScript template from my real-world MCP projects that handles all the boilerplate and lets you focus on what actually matters: building your tools and resources.

## nickytonline/mcp-typescript-template

### TypeScript template for building MCP servers

# MCP TypeScript Template

A TypeScript template for building remote Model Context Protocol (MCP) servers with modern tooling and best practices while leveraging theMCP TypeScript SDK.

## Features

This template provides:

* TypeScript- Full TypeScript support with strict configuration
* Vite- Fast build system with ES modules output
* Express- Fast, unopinionated web framework for HTTP server
* ESLint + Prettier- Code quality and formatting
* Docker- Containerization support
* Example Tool- Simple echo tool to demonstrate MCP tool implementation

## Getting Started

1. Clone or use this templategit clone<your-repo-url>cdmcp-typescript-templateEnter fullscreen modeExit fullscreen mode
2. Install dependenciesnpm installEnter fullscreen modeExit fullscreen mode
3. Build the projectnpm run buildEnter fullscreen modeExit fullscreen mode
4. Start the servernpm startEnter fullscreen modeExit fullscreen mode

The server will be available athttp://localhost:3000for MCP connections.

## Development

### Watch mode for development (with hot reloading)

npm run dev

Enter fullscreen mode

Exit fullscreen mode

### Build the project

npm run build

Enter fullscreen mode

Exit fullscreen mode

### Linting

* Lint the project

npm run lint

Enter fullscreen mode

Exit fullscreen mode

* Fix all auto-fixable lint errors

npm run
…

Enter fullscreen mode

Exit fullscreen mode

View on GitHub

## MCP Is Still Pretty New

Here's the thing: MCP is still pretty new, and people are just starting to explore building their own servers. There aren't a ton of templates and starter projects out there yet, so I decided to create one.

After building thedev.to MCP server, I realized I had a solid foundation that other folks could benefit from. So I extracted all the good parts (the TypeScript config, the MCP SDK integration, the Vite bundling setup, and Node.js's type-stripping development mode starting from v22.18.0) into a template anyone can use.

## Introducing the dev.to MCP server

### Nick Taylor ・ Jul 29

#mcp

#agenticai

#devto

#ai

Just yesterday, I used this template to spin up my newPimp My Ride MCP server. I was able to vibe code with the template in about 30 minutes to build my new MCP server.

## What You Get Out of the Box

This template comes loaded with everything you need for modern MCP server development:

MCP Foundation:

* Built on the officialMCP TypeScript SDK
* HTTP Streamable transport (not SSE, which is deprecated)
* Express-based server for handling MCP connections (I'm a fan ofHono.js, but the MCP SDK leans on Express, so that's what we're using here)
* Ready-to-extend structure for tools and resources

Modern TypeScript Development:

* Live reload using Node.js's built-in type stripping during development (Node.js 22.18.0+, no build step needed while coding)
* Vite for production-ready ES module bundling
* Full TypeScript support with sensible defaults

Quality Tools:

* Vitest for testing
* ESLint and Prettier configured and ready to go with sensible defaults
* Zodfor runtime validation of environment variables and tool inputs

Production Ready:

* Express-based MCP server setup
* Pino for structured logging
* Docker support included
* Environment configuration through a clean config layer

## Getting Started

GitHub makes it easy to use this as a starting point. Instead of forking, you cancreate a repository from the template. Just click "Use this template" on the repo page, give your new MCP server a name, and you're good to go.

Once you've created your repo from the template:

git clone https://github.com/YOUR_USERNAME/your-mcp-server.git

cd
your-mcp-server
npm
install

npm run dev

Enter fullscreen mode

Exit fullscreen mode

or my favourite, leverage the GitHub CLI

gh repo clone YOUR_USERNAME/your-mcp-server

Enter fullscreen mode

Exit fullscreen mode

New to the GitHub CLI? Check out 👇

## Boost productivity with the GitHub CLI

### Nick Taylor for OpenSauced ・ Nov 14 '23

#github

#cli

#git

#productivity

## The Project Structure

Here's how everything's organized:

src/
├── index.ts # Your MCP Express server lives here
├── config.ts # Environment variable validation with Zod
├── logger.ts # Pino logging setup
└── lib/ # Your tools, resources, and helpers
 └── utils.test.ts # Tests colocated with code

Enter fullscreen mode

Exit fullscreen mode

Your server code goes insrc/index.ts, reusable utilities and MCP tools live insrc/lib/, and tests sit right next to the code they're testing. Tool input schemas use Zod for runtime validation, so you get type safety and validation in one shot.

## Testing with Vitest

npm run
test

# Interactive mode for development

npm run
test
:ci
# CI mode with JSON output

Enter fullscreen mode

Exit fullscreen mode

Write your tests in*.test.tsfiles colocated to what it's testing

## Configuration Through Environment Variables

All configuration comes through environment variables, validated with Zod and parsed insrc/config.ts:

* PORT- Server port (default: 3000)
* SERVER_NAME- Your server's name
* LOG_LEVEL- Pino log level (info, debug, etc.)

The Zod schema ensures your environment variables are valid at startup, so you catch config issues early instead of at runtime. Add new config values by extending the schema insrc/config.ts. No hard-coded secrets, everything's validated and documented with defaults.

## Logging with Pino

Pino is wired up and ready for structured logging. Just import the logger and use it:

import

logger

from

'
./logger
'
;

logger
.
info
({

userId
:

123

},

'
User logged in
'
);

logger
.
error
({

error
:

err

},

'
Something broke
'
);

Enter fullscreen mode

Exit fullscreen mode

The logs are structured JSON in production and pretty-printed during development. Perfect for debugging locally and parsing in production.

## Linting and Formatting

The template comes with ESLint and Prettier pre-configured:

npm run lint
# Check for issues

npm run lint:fix
# Auto-fix what we can

npm run format
# Format everything

npm run format:check
# CI-friendly format check

Enter fullscreen mode

Exit fullscreen mode

The rules are sensible: two-space indent, double quotes, trailing commas, and TypeScript-aware linting that catches the stuff that matters. Unused variables prefixed with_are fine (because sometimes you need that for API contracts), andanyis discouraged but not forbidden.

## Production Ready

When you're ready to ship:

npm run build
# Compile to dist/

npm start
# Run the compiled version

Enter fullscreen mode

Exit fullscreen mode

Or use the included Dockerfile:

docker build
-t
 my-mcp-server
.

docker run
-p
 3000:3000 my-mcp-server

Enter fullscreen mode

Exit fullscreen mode

Securing Your MCP Server

If you're deploying your MCP server remotely (not just localhost), theMCP security best practicesrecommend using a proxy or gateway for authentication and authorization. I usePomerium to secure my MCP serverssince it handles auth and access policies without me having to build that stuff myself. It's how I secure the dev.to MCP server and pimp-my-ride-mcp in production.

Full disclosure: I work at Pomerium, but I'd be using it for this even if I didn't. Managing auth and access control for remote services is a pain, and having a proxy that handles it cleanly is genuinely useful.

## Why This Setup Works

After building the dev.to MCP server and now pimp-my-ride-mcp with this setup, here's what I appreciate most:

1. The dev loop is fast.Node.js 22.18.0+ includes built-in type stripping, which means instant reloads without a build step during development.
2. Vite handles production bundling.When you're ready to ship, Vite compiles everything into clean ES modules.
3. The MCP SDK integration is straightforward.You can focus on building tools and resources, not wrestling with protocol details.
4. It's opinionated but not rigid.You can swap out pieces if you want, but the defaults work great.

## What's Next

I've got anOAuth 2.0 PR in the worksthat streamlines authentication and adds coarse-grained authorization. Should be merged soon.

# feat: Add OAuth#2

nickytonline

 posted on
Oct 07, 2025

This PR adds OAuth to the template.

View on GitHub

Clone the template and start building your MCP server. Whether you're exposing an API (like I did with thedev.to MCP server), wrapping a database, or creating custom tools for your AI workflow (likepimp-my-ride-mcp), the template handles the boring parts so you can focus on the interesting problems.

Check out thetemplate repoand give it a star if you find it useful. And if you build something cool with it, let me know!

If you want to stay in touch, all my socials are onnickyt.online.

Until the next one!

Photo byHoma AppliancesonUnsplash

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
