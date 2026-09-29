---
title: 'GitHub - longbridge/gpui-kit: Rust GUI components for building fantastic cross-platform desktop application by using GPUI. · GitHub'
url: https://github.com/longbridge/gpui-kit
site_name: github
content_file: github-github-longbridgegpui-kit-rust-gui-components-for
fetched_at: '2026-09-29T16:48:35.732758'
original_url: https://github.com/longbridge/gpui-kit
author: longbridge
description: Rust GUI components for building fantastic cross-platform desktop application by using GPUI. - longbridge/gpui-kit
---

longbridge

 

/

gpui-kit

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork942
* Star15k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

2,480 Commits
2,480 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.agents
.agents
 
 
.cargo
.cargo
 
 
.claude
.claude
 
 
.github
.github
 
 
crates
crates
 
 
docs
docs
 
 
examples
examples
 
 
script
script
 
 
skills
skills
 
 
themes
themes
 
 
website
website
 
 
.gitignore
.gitignore
 
 
.rustfmt.toml
.rustfmt.toml
 
 
.theme-schema.json
.theme-schema.json
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
LICENSE-APACHE
LICENSE-APACHE
 
 
LICENSE-DOCS.md
LICENSE-DOCS.md
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
README.zh-CN.md
README.zh-CN.md
 
 
_typos.toml
_typos.toml
 
 
flake.lock
flake.lock
 
 
flake.nix
flake.nix
 
 
release-notes.md
release-notes.md
 
 
View all files

## Repository files navigation

GPUI Kit

English|简体中文

 
 

Build fantastic, high-performance desktop apps with Rust and GPUI.

GPUI Kit is a comprehensive Rust desktop application framework. It combines a
production-ready UI system with application-grade data, layout, and editing
capabilities, all built on a reusable foundation of behavior, state, and
infrastructure. GPUI Kit ships 75+ documented components and primitives,
WebAssembly support, AccessKit accessibility, UI integration testing, and an
optional JavaScript extension runtime.

Documentation:https://gpui-kit.com

gpui-kit The one crate applications depend on
├── gpui-base Unstyled behavior, state, and infrastructure
└── gpui-component GPUI Component: the complete styled UI system

gpui-kitpins the matching GPUI release and re-exports GPUI, base, component,
and assets, so a Rust application lists a single dependency. JavaScript extension
hosts addgpui-shellseparately;gpui-component-shellsupplies the styled catalog.

See theexecutable application recipe and AI-assisted development acceptance checksfor a tested starting point and verification commands.

## Features

* 75+ Components and Primitives: Forms, navigation, overlays, data display, editing, feedback, and layout, with polished interactions and productive defaults.
* Production Ready: Used to build Longbridge Pro from day one and continuously refined in a publicly shipped commercial desktop application.
* WebAssembly: Run applications and the same component showcases on the web withwasm32-unknown-unknown.
* Accessibility: AccessKit roles, names, states, relationships, and actions are built into the interaction layer and covered by tests.
* UI Integration Testing: Render real components in headless windows, drive pointer and keyboard input, and assert state, focus, layout, and accessibility.
* Native Feel: Modern controls inspired by macOS and Windows, backed by semantic themes and multiple sizes.
* 120 FPS: GPU-accelerated interfaces that remain smooth under load.
* Data Tables: Virtual scrolling, fixed and resizable columns, sorting, and cell selection across hundreds of thousands of rows.
* Virtual Lists: Render only the visible range, including lists whose items have different sizes.
* Code Editor: Stable performance at 200K lines with Tree-sitter highlighting and LSP diagnostics, completion, and hover.
* Dock Layout: Resizable panels, draggable tabs, nested splits, and edge docks — all serializable.
* Rich Content: Native Markdown and HTML rendering, syntax highlighting, and built-in charts.
* Design Freedom: Use the complete visual system or build your own on the behavior and infrastructure ingpui-base.
* JavaScript Extensions:gpui-shelllets a shipped Rust host load panels and business logic as scripts, with every capability granted explicitly.
* Cross Platform: Ship one Rust codebase to macOS, Windows, and Linux.

## Framework Architecture

### Three layers. One ecosystem.

Usegpui-componentto keep the application coherent with one complete visual
and interaction system. Usegpui-basewhen your product needs to create and
own that system itself. Usegpui-shellwhen the application should be
extensible in JavaScript after it ships.

gpui-component

gpui-base

gpui-shell

Complete, styled components

Unstyled behavior and infrastructure

JavaScript runtime hosted by Rust

Productive defaults with theming

Full control over structure and visual design

Capabilities granted one at a time

Best for building applications

Best for building design systems

Best for plugins and scripted applications

 APPLICATION
 │
 ┌───────────────────┼───────────────────┐
 │ │ │
 ▼ ▼ ▼
 ┌──────────────────┐ ┌──────────────────┐ ┌──────────────────┐
 │ gpui-component │ │ Your Design │ │ gpui-shell │
 │ Styled UI │ │ System │ │ JS extensions │
 └────────┬─────────┘ └────────┬─────────┘ └────────┬─────────┘
 │ │ │
 └────────────────────┼────────────────────┘
 ▼
 ┌──────────────────┐
 │ gpui-base │
 │ Behavior · State │
 │ Infrastructure │
 └────────┬─────────┘
 ▼
 GPUI

Behavior belongs to the foundation. Presentation belongs to the application.

Usegpui-componentwhen you want polished controls ready to ship. Build ongpui-basewhen your application should own its component source, layout,
styling, and motion while reusing difficult interaction behavior. Addgpui-shellwhen contributors should extend the product without a fork or
a release.

The layering follows the same separation that makes theshadcnecosystem flexible:

GPUI Kit ecosystem

Web ecosystem

GPUI

HTML + Tailwind CSS

gpui-base

Base UI

gpui-component

shadcn's styled component layer

Explore the architecture →

## Showcase

GPUI Kit has poweredLongbridge Profrom day one. The framework is extracted from the demands of a publicly shipped
commercial desktop application rather than designed in isolation.

GPUI provides the rendering foundation. Longbridge provides the production foundation.

## Usage

[
dependencies
]

gpui-kit
 = 
"
0.7
"

gpui-kitalways brings in GPUI andgpui-base;gpui-componentand the
default icon set are on by default. Turn default
features off to keep only the layers you use. Thegpui-componentfeatures (inspector,decimal,tree-sitter, and eachtree-sitter-<language>) are available under the same
names.

### Basic Example

use
 gpui_kit
::
component
::
button
::
*
;

use
 gpui_kit
::
component
::
*
;

use
 gpui_kit
::
*
;

pub
 
struct
 
HelloWorld
;

impl
 
Render
 
for
 
HelloWorld
 
{

 
fn
 
render
(
&
mut
 
self
,
 _
:
 
&
mut
 
Window
,
 _
:
 
&
mut
 
Context
<
Self
>
)
 -> 
impl
 
IntoElement
 
{

 
div
(
)

 
.
v_flex
(
)

 
.
gap_2
(
)

 
.
size_full
(
)

 
.
items_center
(
)

 
.
justify_center
(
)

 
.
child
(
"Hello, World!"
)

 
.
child
(

 
Button
::
new
(
"ok"
)

 
.
primary
(
)

 
.
label
(
"Let's Go!"
)

 
.
on_click
(
|_
,
 _
,
 _| 
println
!
(
"Clicked!"
)
)
,

 
)

 
}

}

fn
 
main
(
)
 
{

 gpui_kit
::
application
(
)
.
run
(
move
 |cx| 
{

 
// This must be called before using any GPUI Component features.

 gpui_kit
::
init
(
cx
)
;

 gpui_kit
::
open_window
(
WindowOptions
::
default
(
)
,
 cx
,
 |_
,
 cx| 
{

 cx
.
new
(
|_| 
HelloWorld
)

 
}
)

 
.
expect
(
"Failed to open window"
)
;

 
}
)
;

}

gpui_kit::open_windowis the application window entry point and always mounts a BaseRoot. Component initialization registers styled window facilities; Cargo features do not select a different root type.

### Icons

The defaultassetsfeature bundles theLucideicon set
asgpui-kit-assets; pass it to the application withgpui_kit::application().with_assets(gpui_kit::assets::Assets). To ship your
own icons instead, leave that feature out and name the SVG files as defined inIconName.

## Skills for AI Coding Agents

Install the GPUI Kit skills for your AI coding agent (Cursor, Claude Code, Gemini CLI, Codex, etc.):

npx skills add longbridge/gpui-kit

Skill

Description

gpui-kit

Setup, component catalog, usage patterns, GPUI mechanics (elements, entities, async, focus, actions, tests), and the Coding Guides.

gpui-kit-design-guides

The Design Guides: layout, spacing, hierarchy, interaction states, overlays, and interface copy.

## Development

### Desktop Gallery (Story)

Thestorycrate is a gallery application that showcases all available components. Run it with:

cargo run

### Examples

Some larger examples reuse thestorygallery components and run as standalone packages:

#
 Dock layout system (panels, split views, tabs)

cargo run -p example-dock

#
 Markdown rendering

cargo run -p example-markdown

#
 HTML rendering

cargo run -p example-html

Theexamplesdirectory also contains standalone examples, each focused on a single feature. Each example is a separate crate, run them withcargo run -p <name>:

#
 Code editor with LSP support and syntax highlighting

cargo run -p example-editor

#
 Basic hello world

cargo run -p hello_world

#
 System monitor (real-time charts with CPU/memory data)

cargo run -p system_monitor

#
 Window title customization

cargo run -p window_title

Check outCONTRIBUTING.mdfor more details.

## Compare to others

See thecomparison with Iced, egui and Qt 6on the site.

## License

Software source and documentation code examples:Apache-2.0.

Documentation prose and original illustrations in the Docs, Base, Component, and Shell sections (including Chinese translations) for which GPUI Kit holds licensing rights are also offered underCC BY 4.0. When copying or adapting that material, creditGPUI Kit, link to the source page andCC BY 4.0 license, and indicate changes. Existing Apache-2.0 permissions remain; earlier revisions retain their prior terms, and third-party contributions keep their own licenses unless separately authorized. Using facts or ideas without copying protected expression does not require attribution under CC BY 4.0.

* Built onGPUI, the UI framework from Zed Industries, also Apache-2.0. Thegpui-pre-*crates are snapshots of it, published with Zed's license and notices intact.
* UI design based onshadcn/ui, some fromReui.
* Icons fromLucide.