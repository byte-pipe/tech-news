---
title: 'GitHub - dream-num/univer: The Office Harness for AI Agents — Spreadsheets, Docs, Slides, Canvas, Relational Tables, and PDF in one runtime. · GitHub'
url: https://github.com/dream-num/univer
site_name: github
content_file: github-github-dream-numuniver-the-office-harness-for-ai-a
fetched_at: '2026-09-22T15:25:49.619687'
original_url: https://github.com/dream-num/univer
author: dream-num
description: The Office Harness for AI Agents — Spreadsheets, Docs, Slides, Canvas, Relational Tables, and PDF in one runtime. - dream-num/univer
---

dream-num

 

/

univer

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork1.4k
* Star15.1k

 
 
 
dev
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

5,802 Commits
5,802 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
.husky
.husky
 
 
.vscode
.vscode
 
 
common
common
 
 
docs
docs
 
 
examples
examples
 
 
packages
packages
 
 
presets
presets
 
 
scripts
scripts
 
 
tests/
formula-integration
tests/
formula-integration
 
 
.editorconfig
.editorconfig
 
 
.gitignore
.gitignore
 
 
.semgrepignore
.semgrepignore
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
DREAMNUM.md
DREAMNUM.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
codecov.yml
codecov.yml
 
 
commitlint.config.cjs
commitlint.config.cjs
 
 
eslint.config.ts
eslint.config.ts
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
pnpm-workspace.yaml
pnpm-workspace.yaml
 
 
turbo.json
turbo.json
 
 
verso.toml
verso.toml
 
 
vitest.workspace.ts
vitest.workspace.ts
 
 
View all files

## Repository files navigation

The Office Harness for AI Agents

Spreadsheets · Documents · Presentations · Bases · Boards · PDFs (coming soon)

High-performance, fully customizable Office SDK

Build embeddable productivity experiences with a plugin architecture, Canvas-based rendering,
a formula engine, and one Facade API that works in the browser and on Node.js.

English |简体中文|繁體中文|日本語|한국어|Español

🌐 Website|📖 Documentation|✨ Showcase|📘 API Reference|📝 Blog

## ✨ What is Univer?

Univer is an open-source SDK for creating office applications inside your own product. It gives you the building blocks for spreadsheet, document, and presentation experiences without forcing you into a hosted app or a fixed UI.

Use Univer when you need to:

* Embed spreadsheet or document editing into a SaaS product, internal tool, BI workflow, or AI application.
* Run workbook/document processing on the server with the same architecture used in the browser.
* Compose only the features you need through plugins or start quickly with presets.
* Extend behavior through custom plugins, commands, services, UI components, and Facade APIs.

Univer is not a spreadsheet file viewer only. It is a framework for building your own productivity surface.

Across theUniver product family, Office tools share a runtime for storage and computation. Content can be composed and embedded across tools, with linked data and references updating together. People and AI agents can work in the same files. See thecapability matrixfor product coverage andOpen Source and Profor this repository's scope.

## Built with Univer Office SDK

These open-source projects are built with Univer Office SDK:

Project

Description

Univer Workspace

An Office workspace for people and AI agents, with shared editing and review of agent changes.

Univer Office for DeepSeek Harness

An Office plugin for DeepSeek Harness with connected content, validation, and isolated worktrees for agent collaboration.

Univer CLI

A local command-line workspace for agents to create, edit, inspect, and deliver Office content.

Univer Office for WorkBuddy

A local Office integration for WorkBuddy with MCP previews and draft review. Development preview.

Univer Office for OpenClaw

Tools for creating, reviewing, and delivering Office content in OpenClaw.

Each project documents its own setup and SDK licensing requirements.

## 🌟 Highlights

 ⚡

Built for large surfaces

Canvas-based rendering and a dedicated formula engine keep complex workbooks responsive.

 🧩

Plugin-shaped by default

Compose, replace, lazy-load, or extend capabilities without taking the whole stack.

 🤖

Headless for AI infrastructure

Run workbook and document logic in Node.js to power agents, automation, and server-side workflows.

 🛠️

Product-ready SDK

Framework adapters, Facade APIs, presets, and headless runtime fit real integration paths.

 🌗

Dark-mode ready

UI components and the rendering engine both adapt to light and dark themes.

 🔌

Unified Facade API

One consistent API surface for workbooks, ranges, formulas, and documents across browser and Node.js.

## 🚀 Why Univer?

* Isomorphic by design: run UI apps in browsers and headless processing in Node.js.
* Plugin-first architecture: every capability is delivered as a composable plugin, so features can be added, removed, replaced, or lazy-loaded.
* Preset mode for fast integration: use the curated plugin collections inpresets/when you want a working app quickly.
* Plugin mode for full control: manually compose packages when you need custom loading, smaller bundles, or deep integration.
* Facade API: work with workbooks, worksheets, ranges, documents, formulas, commands, and events through a higher-level API.
* Canvas rendering engine: support large editable document surfaces with a rendering layer shared across document types.
* Extensible UI: integrate with React, Vue, Web Components, and framework-specific application shells.

## 🤖 Office Workflows for AI Agents

Univer's AI and collaboration capabilities connect agent operations with interactive editing and human review:

* Programmatic editing: agents inspect and modify Office content through structured APIs.
* Output verification: agents check results through content inspection, rendered screenshots, and layout diagnostics.
* Worktree collaboration: agents work in isolated drafts, then people review their changes and decide what to merge.

See theAI SDK documentationfor integration details. Live editing, shared revisions, and Worktree workflows require the corresponding Web SDK and collaboration capabilities; package availability and licensing vary by feature.

## ⚡ Quick Start

UsePlugin Modefor complete product coverage and precise composition. For supported Sheets, Docs, and Node profiles,Preset Modeprovides a shorter curated setup.

Plugin Mode

Plugin Mode gives you lower-level control over packages, style imports, locale merging, Facade API registration, and plugin configuration.

pnpm add @univerjs/core @univerjs/design @univerjs/docs @univerjs/docs-ui @univerjs/engine-formula @univerjs/engine-render @univerjs/sheets @univerjs/sheets-formula @univerjs/sheets-formula-ui @univerjs/sheets-numfmt @univerjs/sheets-numfmt-ui @univerjs/sheets-ui @univerjs/ui

import
 
{
 
LocaleType
,
 
mergeLocales
,
 
Univer
 
}
 
from
 
'@univerjs/core'

import
 
{
 
FUniver
 
}
 
from
 
'@univerjs/core/facade'

import
 
DesignEnUS
 
from
 
'@univerjs/design/locale/en-US'

import
 
{
 
UniverDocsPlugin
 
}
 
from
 
'@univerjs/docs'

import
 
{
 
UniverDocsUIPlugin
 
}
 
from
 
'@univerjs/docs-ui'

import
 
DocsUIEnUS
 
from
 
'@univerjs/docs-ui/locale/en-US'

import
 
{
 
UniverFormulaEnginePlugin
 
}
 
from
 
'@univerjs/engine-formula'

import
 
{
 
UniverRenderEnginePlugin
 
}
 
from
 
'@univerjs/engine-render'

import
 
{
 
UniverSheetsPlugin
 
}
 
from
 
'@univerjs/sheets'

import
 
SheetsEnUS
 
from
 
'@univerjs/sheets/locale/en-US'

import
 
{
 
UniverSheetsFormulaPlugin
 
}
 
from
 
'@univerjs/sheets-formula'

import
 
SheetsFormulaEnUS
 
from
 
'@univerjs/sheets-formula/locale/en-US'

import
 
{
 
UniverSheetsFormulaUIPlugin
 
}
 
from
 
'@univerjs/sheets-formula-ui'

import
 
SheetsFormulaUIEnUS
 
from
 
'@univerjs/sheets-formula-ui/locale/en-US'

import
 
{
 
UniverSheetsNumfmtPlugin
 
}
 
from
 
'@univerjs/sheets-numfmt'

import
 
{
 
UniverSheetsNumfmtUIPlugin
 
}
 
from
 
'@univerjs/sheets-numfmt-ui'

import
 
SheetsNumfmtUIEnUS
 
from
 
'@univerjs/sheets-numfmt-ui/locale/en-US'

import
 
{
 
UniverSheetsUIPlugin
 
}
 
from
 
'@univerjs/sheets-ui'

import
 
SheetsUIEnUS
 
from
 
'@univerjs/sheets-ui/locale/en-US'

import
 
{
 
UniverUIPlugin
 
}
 
from
 
'@univerjs/ui'

import
 
UIEnUS
 
from
 
'@univerjs/ui/locale/en-US'

import
 
'@univerjs/design/lib/index.css'

import
 
'@univerjs/ui/lib/index.css'

import
 
'@univerjs/docs-ui/lib/index.css'

import
 
'@univerjs/sheets-ui/lib/index.css'

import
 
'@univerjs/sheets-formula-ui/lib/index.css'

import
 
'@univerjs/sheets-numfmt-ui/lib/index.css'

import
 
'@univerjs/engine-formula/facade'

import
 
'@univerjs/ui/facade'

import
 
'@univerjs/sheets/facade'

import
 
'@univerjs/sheets-ui/facade'

import
 
'@univerjs/sheets-formula/facade'

import
 
'@univerjs/sheets-numfmt/facade'

const
 
univer
 
=
 
new
 
Univer
(
{

 
locale
: 
LocaleType
.
EN_US
,

 
locales
: 
{

 
[
LocaleType
.
EN_US
]
: 
mergeLocales
(

 
DesignEnUS
,

 
UIEnUS
,

 
DocsUIEnUS
,

 
SheetsEnUS
,

 
SheetsUIEnUS
,

 
SheetsFormulaEnUS
,

 
SheetsFormulaUIEnUS
,

 
SheetsNumfmtUIEnUS
,

 
)
,

 
}
,

}
)

univer
.
registerPlugin
(
UniverRenderEnginePlugin
)

univer
.
registerPlugin
(
UniverFormulaEnginePlugin
)

univer
.
registerPlugin
(
UniverUIPlugin
,
 
{
 
container
: 
'app'
 
}
)

univer
.
registerPlugin
(
UniverDocsPlugin
)

univer
.
registerPlugin
(
UniverDocsUIPlugin
)

univer
.
registerPlugin
(
UniverSheetsPlugin
)

univer
.
registerPlugin
(
UniverSheetsUIPlugin
)

univer
.
registerPlugin
(
UniverSheetsFormulaPlugin
)

univer
.
registerPlugin
(
UniverSheetsFormulaUIPlugin
)

univer
.
registerPlugin
(
UniverSheetsNumfmtPlugin
)

univer
.
registerPlugin
(
UniverSheetsNumfmtUIPlugin
)

const
 
univerAPI
 
=
 
FUniver
.
newAPI
(
univer
)

univerAPI
.
createWorkbook
(
{
}
)

Preset Mode

Presets are curated collections of Univer plugins that include the required Facade API registrations and styles.

pnpm add @univerjs/presets @univerjs/preset-sheets-core

import
 
{
 
UniverSheetsCorePreset
 
}
 
from
 
'@univerjs/preset-sheets-core'

import
 
UniverPresetSheetsCoreEnUS
 
from
 
'@univerjs/preset-sheets-core/locales/en-US'

import
 
{
 
createUniver
,
 
LocaleType
,
 
mergeLocales
 
}
 
from
 
'@univerjs/presets'

import
 
'@univerjs/preset-sheets-core/lib/index.css'

const
 
{
 univerAPI 
}
 
=
 
createUniver
(
{

 
locale
: 
LocaleType
.
EN_US
,

 
locales
: 
{

 
[
LocaleType
.
EN_US
]
: 
mergeLocales
(
UniverPresetSheetsCoreEnUS
)
,

 
}
,

 
presets
: 
[

 
UniverSheetsCorePreset
(
{

 
container
: 
'app'
,

 
}
)
,

 
]
,

}
)

univerAPI
.
createWorkbook
(
{
}
)

Your page needs a container:

<
div
 
id
="
app
" 
style
="
height: 100vh
"
>
</
div
>

Learn more in theInstallation & Basic Usage guide, thecreateUniverreference, and theFacade API reference.

## 🧩 Preset Mode vs Plugin Mode

Choose

When to use it

Start here

Plugin Mode

You need strict control over packages, configured dependencies, lazy loading, or custom runtime composition.

This repository's 
examples/
 and 
architecture guide

Preset Mode

You want a working Sheets, Docs, or Node setup with minimal configuration.

This repository's 
presets/
 and the 
getting started guide

Headless Mode

You need server-side workbook/document processing, formula calculation, or automation without UI.

Headless Univer

Keep the@univerjs/*SDK packages in the same coordinated Univer release line on the same version. Independently released packages, including@univerjs/iconsand@univerjs/icons-svg, use the compatible versions declared by package manifests instead of the SDK version. If you use Univer Pro packages, keep@univerjs-pro/*aligned with the matching coordinated release line.

For API compatibility expectations, experimental APIs, internal APIs, and deprecation rules, see theAPI Stability Policy.

## 🧭 Compatibility

* Browser runtime: Univer is compiled with a Chrome 88 target and aims to work on Edge>=88, Firefox>=90, Chrome>=88, Safari>=14.1, and Electron>=12.
* Polyfills: Univer relies onIntl.Segmenter. Add a polyfill such as@formatjs/intl-segmenterif your target browser or runtime does not provide it.
* Build tools: We recommend Vite, esbuild, or Webpack 5. If your build tool does not support theexportsfield inpackage.json(common in Webpack 4), you may need extra path mapping.
* React: Univer's view layer is built on React 18, supports React 18 and 19, and provides minimal compatibility support for React 16.9+ and 17.
* Node.js runtime: Headless Univer supports Node.js>=18.17.0. Developing this monorepo requires Node.js>=22.18.

## 🛠️ What You Can Build

Area

Open-source capabilities

Univer Pro extensions

Sheets

Workbooks, worksheets, ranges, selection, formulas, number formatting, filtering, sorting, data validation, conditional formatting, hyperlinks, comments, find and replace, notes, tables, drawing integration, and extensible UI plugins.

Real-time collaboration, edit history, import/export, printing, charts, pivot tables, sparklines, outlines, shapes, in-cell graphics, data connectors, server-side calculation, and performance-enhanced formula features.

Docs

Rich document model, editing UI, lists, hyperlinks, drawing integration, comments, quick insert, and shared document architecture.

Collaboration, import/export, printing, enhanced tables and lists, columns, callouts, code blocks, quotes, shapes, and remote comment resources.

Slides

Presentation data model and UI packages under active development.

Pro slide model and UI, slide import/export, chart and table model/UI plugins, and shared shape-editing infrastructure.

Bases

Build custom structured-data experiences on top of Univer's plugin, command, and model architecture.

Base database model, commands, formula integration, workbench UI, field editors, and render-engine views.

Runtime

Browser apps, Node.js headless usage, Web Worker/RPC patterns, multi-instance usage, and server-oriented automation.

Collaboration client/server packages, Node.js collaboration client, Pro server services, SSR, computing delegation, server-side calculation, and changeset replay tooling.

Integrations

React, Vue, Web Components, framework templates, theming, localization, and custom plugins.

Pro presets and enterprise deployment packages.

Sheets are the most mature product surface today. Docs and Slides share Univer's architecture and continue to evolve in the same SDK.

## 🔓 Open Source and Pro

This repository contains Univer's open-source core and first-party OSS plugins. Univer Pro is developed separately as a commercial extension layer for advanced product surfaces, collaboration, server features, and enterprise integrations.

Category

Open source

Univer Pro / commercial

Foundation

Core SDK, plugin system, rendering engine, formula engine, Facade API, themes, i18n, and framework adapters.

Pro presets and enterprise deployment packages.

Sheets

Core spreadsheet editing, formulas, number formatting, filter/sort, data validation, conditional formatting, notes, tables, hyperlinks, comments, drawing, find and replace.

Collaboration, edit history, import/export, print, charts, pivot tables, sparklines, outlines, shapes, in-cell graphics, data connectors, range preprocessing, and enhanced formula engine features.

Docs

Document model and editor UI, lists, hyperlinks, comments, quick insert, and drawing integration.

Collaboration, import/export, print, enhanced tables/lists, columns, callouts, code blocks, quotes, shapes, and remote thread-comment resources.

Slides

OSS presentation model and UI packages.

Pro slide model/UI packages, slide import/export, charts, tables, and reusable shape editor UI.

Bases

Extensible plugin architecture for custom data-centric products.

Base database core model, commands, mutations, formula integration, workbench UI, field editors, and render-engine integration.

Server and runtime

Node.js headless runtime, RPC/Web Worker patterns, and server-oriented automation primitives.

Collaboration server, Node.js collaboration client, SSR services, computing delegation, server-side calculation, and collaboration changeset replay tooling.

Pro features are documented in theUniver Pro guide. They are intentionally separated here so the OSS package surface is clear.

Boundary principles:

* OSS packages in this repository are intended to be useful on their own under the Apache-2.0 license. Univer Pro is optional and is not required to use the public OSS SDK APIs.
* Bugs, regressions, and security issues in OSS packages should be reported and fixed in the OSS repository, even when a related Pro feature exists.
* OSS documentation should not imply that Pro-only capabilities are available in public@univerjs/*packages. Pro-only APIs, packages, and deployment paths should be named explicitly.
* When an OSS feature has a Pro enhancement, the OSS behavior should remain documented independently so users can evaluate the open-source surface without reading commercial docs first.

## 🌐 Ecosystem

* Core SDK:dream-num/univer, this monorepo.
* Presets: this repository'spresets/, curated plugin collections for browser and Node.js apps.
* AI agent skills:dream-num/univer-sdk-skills, reusable instructions for AI agents working with Univer integration, Pro features, plugin development, and Node backends. See theAI Skills guide.
* Documentation:docs.univer.ai, including Sheets, Docs, Slides, recipes, and Pro guides.
* Web SDK:embedded editors and headless processingin the browser and Node.js.
* Server SDK:collaboration and file conversion, integrated with your application's storage, identity, and permissions.
* AI SDK:agent workflowsfor inspecting, editing, and verifying Office content.
* API Reference:docs.univer.ai/reference, the Facade API and generated API reference.
* Examples and showcase:Univer Showcaseand this repository'sexamples/.
* AI-native spreadsheets:dream-num/univer-mcp, Univer Platform / MCP integration for driving Univer Sheets with natural language.

## 📦 Repository Guide

.
├── packages/ Core packages, engines, document types, UI plugins, and feature plugins
├── examples/ All-in-one Vite workbench used for local browser development
├── common/ Shared internal tooling, storybook, and utilities
├── tests/ Additional integration test projects
└── docs/ Architecture notes, images, and repository-local documentation

Package-level READMEs live beside each package underpackages/.

## 🧑‍💻 Development

Requirements:

* Node.js>=22.18
* pnpm>=11

git clone https://github.com/dream-num/univer.git

cd
 univer
pnpm install
pnpm dev

Useful commands:

Command

Purpose

pnpm dev

Start the all-in-one Sheets, Docs, and Slides workbench with Vite 8 Bundled Dev and HMR.

pnpm build

Build workspace packages, excluding internal common packages.

pnpm test

Run unit tests through Turbo.

pnpm typecheck

Run TypeScript checks through Turbo.

pnpm lint

Run ESLint.

pnpm storybook:dev

Start Storybook for UI component development.

ReadCONTRIBUTING.mdbefore opening a pull request.

## 📝 Contributor Notes

Repository-local notes worth reading before deeper changes:

* Building Isomorphic Univer: how to split browser, Node.js, UI, and shared plugin logic.
* API Stability Policy: stable, experimental, internal, deprecated, and breaking-change expectations.
* Contributing to Facade API: API design expectations forFUniver,FWorkbook,FRange, and related Facade classes.
* Naming Convention: file, folder, interface, plugin, command, and dependency injection token conventions.
* Fixing Memory Leaks: common leak patterns and debugging workflow for Univer instances.
* Architecture TLDRs: concise notes for formula engine, web worker, permission, selection, and ref-range behavior.

## 💬 Community

* Ask questions inGitHub Discussions.
* Chat with the community onDiscord.
* FollowTwitter / XandYouTube.

Please read theCode of Conductbefore participating.

## 🔒 Security

If you believe you have found a security issue, please follow theSecurity Policy.

## ❤️ Sponsors

Univer is supported by the community and sponsors. You can support the project throughOpen Collective.

## 📄 License

Copyright (c) 2021-present DreamNum Co., Ltd.

Licensed under theApache-2.0license.