---
title: |
  GitHub - microsandbox/microsandbox: Self-Hosted Plaform for Secure Execution of Untrusted User/AI Code
url: |
  https://github.com/microsandbox/microsandbox
site_name: hackernews_api
fetched_at: |
  2025-06-01T01:56:14.078999
original_url: |
  https://github.com/microsandbox/microsandbox
author: makeboss
date: 2025-05-30
description: Self-Hosted Plaform for Secure Execution of Untrusted User/AI Code - microsandbox/microsandbox
tags:
  - hackernews
  - trending
---

[](/microsandbox/microsandbox/blob/main/#gh-dark-mode-only)

[](/microsandbox/microsandbox/blob/main/#gh-light-mode-only)

———   easy secure execution of untrusted user/ai code   ———

[](https://private-user-images.githubusercontent.com/20358651/449247679-d91df12c-e425-48c0-a881-dec9a8d45868.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDg3MDcyNzMsIm5iZiI6MTc0ODcwNjk3MywicGF0aCI6Ii8yMDM1ODY1MS80NDkyNDc2NzktZDkxZGYxMmMtZTQyNS00OGMwLWE4ODEtZGVjOWE4ZDQ1ODY4LmdpZj9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA1MzElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNTMxVDE1NTYxM1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWU4OTdlZmM5MTRlOGM3Zjk5OGQwNTBiYzU5M2YyYWU4MGUyMjU2MjQwOTg5ODk4MDZjZmJkNjgwMWE3YTk5MDgmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.6o6Sorov8tIvlztwx4rDM8YKHhMN-bJ8JH2ekRBdMuk)

[](https://docs.microsandbox.dev)

[](https://discord.gg/T95Y3XnEAK)

# WHY MICROSANDBOX?

[](#why-microsandbox)

Ever needed to run code you don't fully trust? Whether it's AI-generated code, user submissions, or experimental code, the traditional options all have serious drawbacks:

microsandboxcombines the best of all worlds:

• • •

# SDK QUICK START

[](#sdk-quick-start)

Get started in few easy steps:

Playground.Demo.mp4

[ASCIINEMA →]

[](https://camo.githubusercontent.com/50b009b96c229efe4bf861daa7f4d181bdcbb2fad3b080e552e6a304918cbf23/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6d61636f732d776f726b696e672d677265656e3f7374796c653d666f722d7468652d6261646765)

[](https://camo.githubusercontent.com/a2a62abf9a85d97ef6fb29ec6aa9b8c5917fa0166deb2709c38b5c4932e1c684/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c696e75782d776f726b696e672d677265656e3f7374796c653d666f722d7468652d6261646765)

[](https://camo.githubusercontent.com/ffc403a8e3e11f3fe56a1ba9257cac9907ecfb9814cd5c7312ae587237ec1bf1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f77696e646f77732d7769702d7265643f7374796c653d666f722d7468652d6261646765)

##

### 1Start the Server

[](#1start-the-server)

##### Install microsandbox

[](#install-microsandbox)

curl -sSL https://get.microsandbox.dev
|
 sh

##### And start the server

[](#and-start-the-server)

msb server start --dev

Tip

microsandbox server is also anMCP server, so it works directly with Claude, Agno and other MCP-enabled AI tools and agents.

For more information on setting up the server, see theself-hosting guide.

##### Optionally pull the environment image

[](#optionally-pull-the-environment-image)

msb pull microsandbox/python

##

### 2Install the SDK

[](#2install-the-sdk)

##### Python

[](#python)

pip install microsandbox

##### JavaScript

[](#javascript)

npm install microsandbox

##### Rust

[](#rust)

cargo add microsandbox

Note

There areSDKsfor other languages as well! Join us in expanding support for your favorite language.

##

### 3Execute the Code

[](#3execute-the-code)

microsandboxoffers a growing list of sandbox environment types optimized for different execution requirements. Choose the appropriate sandbox (e.g., PythonSandbox or NodeSandbox) to run your code in a secure tailored environment.

##### Python

[](#python-1)

import

asyncio

from

microsandbox

import

PythonSandbox

async

def

main
():

async

with

PythonSandbox
.
create
(
name
=
"test"
)
as

sb
:

exec

=

await

sb
.
run
(
"name = 'Python'"
)

exec

=

await

sb
.
run
(
"print(f'Hello {name}!')"
)


print
(
await

exec
.
output
())
# prints Hello Python!

asyncio
.
run
(
main
())

##### JavaScript

[](#javascript-1)

import

{

NodeSandbox

}

from

"microsandbox"
;

async

function

main
(
)

{


const

sb

=

await

NodeSandbox
.
create
(
{

name
:
"test"

}
)
;


try

{


let

exec

=

await

sb
.
run
(
"var name = 'JavaScript'"
)
;


exec

=

await

sb
.
run
(
"console.log(`Hello ${name}!`)"
)
;


console
.
log
(
await

exec
.
output
(
)
)
;

// prints Hello JavaScript!


}

finally

{


await

sb
.
stop
(
)
;


}

}

main
(
)
.
catch
(
console
.
error
)
;

##### Rust

[](#rust-1)

use
 microsandbox
::
{
SandboxOptions
,

PythonSandbox
}
;

#
[
tokio
::
main
]

async

fn

main
(
)
 ->
Result
<
(
)
,

Box
<
dyn
 std
::
error
::
Error
>
>

{


let

mut
 sb =
PythonSandbox
::
create
(
SandboxOptions
::
builder
(
)
.
name
(
"test"
)
.
build
(
)
)
.
await
?
;


let
 exec = sb
.
run
(
r#"name = "Python""#
)
.
await
?
;


let
 exec = sb
.
run
(
r#"print(f"Hello {name}!")"#
)
.
await
?
;


println
!
(
"{}"
,
 exec
.
output
(
)
.
await
?
)
;

// prints Hello Python!

    sb
.
stop
(
)
.
await
?
;


Ok
(
(
)
)

}

Note

If you haven't pulled the environment image, the first run will take a while as it tries to download it.
Executions will be much faster afterwards.

For more information on how to use the SDK,check out the SDK README.

# PROJECTSB E T A

[](#projectsb-e-t-a)

Beyond the SDK, microsandbox supports project-based development with the familiar package-manager workflow devs are used to. Think of it like npm or cargo, but for sandboxes!

Create aSandboxfile, define your environments, and manage your sandboxes with simple commands.

##

#### Create a Sandbox Project

[](#create-a-sandbox-project)

msb init

This creates aSandboxfilein the current directory, which serves as the configuration manifest for your sandbox environments.

##

#### Add a Sandbox to the Project

[](#add-a-sandbox-to-the-project)

msb add app \
    --image python \
    --cpus 1 \
    --memory 1024 \
    --start
'
python -c "print(\"hello\")"
'

The command above registers a new sandbox namedappin your Sandboxfile, configured to use thepythonimage.

You should now have aSandboxfilecontaining a sandbox namedapp:

cat Sandboxfile

#
 Sandbox configurations

sandboxes
:

app
:

image
:
python


memory
:
1024


cpus
:
1


scripts
:

start
:
python -c "print(\"hello\")"

Tip

Runmsb <subcommand> --helpto see all the options available for a subcommand.

For example,msb add --help.

##

#### Running a Sandbox

[](#running-a-sandbox)

##### Run a Sandbox Defined in Your Project

[](#run-a-sandbox-defined-in-your-project)

msb run --sandbox app

or

msr app

This executes the defaultstartscript of your sandbox. For more control, you can directly specify which script to run —msr app~start.

When running project sandboxes, all file changes and installations made inside the sandbox are automatically persisted to the./menvdirectory. This means you can stop and restart your sandbox any time without losing your work. Your development environment will be exactly as you left it.

##### Run an Temporary Sandbox

[](#run-an-temporary-sandbox)

For experimentation or one-off tasks, temporary sandboxes provide a clean environment that leaves no trace:

msb exe --image python

or

msx python

Temporary sandboxes are perfect for isolating programs you get from the internet. Once you exit the sandbox, all changes are discarded automatically.

##

#### Installing Sandboxes

[](#installing-sandboxes)

Themsb installcommand sets up a sandbox as a system-wide executable. It installs a slim launcher program that allows you to start your sandbox from anywhere in your system with a simple command.

msb install --image alpine

or

msi alpine

After installation, you can start your sandbox by simply typing its name in any terminal:

alpine

This makes frequently used sandboxes incredibly convenient to access — no need to navigate to specific directories or remember complex commands. Just type the sandbox name and it launches immediately with all your configured settings.

Tip

You can give your sandbox a descriptive, easy-to-remember name during installation:

msi alpine:20250108 slim-linux

This allows you to create multiple instances of the same sandbox image with different names and configurations. For example:

Installed sandboxes maintain their state between sessions, so you can pick up exactly where you left off each time you launch them.

• • •

# USE CASES

[](#use-cases)

### Coding & Dev Environments

[](#coding--dev-environments)

Let your AI agents build real apps with professional dev tools. When users ask their AI to create a web app, fix a bug, or build a prototype, it can handle everything from Git operations to dependency management to testing in a protected environment.

Your AI can create comprehensive development environments in milliseconds and run programs with full system access. The fast startup means developers get instant feedback and can iterate quickly. This makes it perfect for AI pair programming, coding education platforms, and automated code generation where quick results matter.

### Data Analysis

[](#data-analysis)

Transform raw numbers into meaningful insights with AI that works for you. Your AI can process spreadsheets, create charts, and generate reports safely. Whether it's analyzing customer feedback, sales trends, or research data, everything happens in a protected environment that respects data privacy.

Microsandbox lets your AI work with powerful libraries like NumPy, Pandas, and TensorFlow while creating visualizations that bring insights to life. Perfect for financial analysis tools, privacy-focused data processing, medical research, and any situation where you need serious computing power with appropriate safeguards.

### Web Browsing Agent

[](#web-browsing-agent)

Build AI assistants that can browse the web for your users. Need to compare prices across stores, gather info from multiple news sites, or automate form submissions? Your AI can handle it all while staying in a contained environment.

With microsandbox, your AI can navigate websites, extract data, fill out forms, and handle logins. It can visit any site and deliver only the useful information back to your application. This makes it ideal for price comparison tools, research assistants, content aggregators, automated testing, and web automation workflows that would otherwise require complex setup.

### Instant App Hosting

[](#instant-app-hosting)

Share working apps and demos in seconds without deployment headaches. When your AI creates a useful tool, calculator, visualization, or prototype, users can immediately access it through a simple link.

Zero-setup deployment means your AI-generated code can be immediately useful without complex configuration. Each app runs in its own protected space with appropriate resource limits, and everything cleans up automatically when no longer needed. Perfect for educational platforms hosting student projects, AI assistants creating live demos, and users needing immediate value.

• • •

### The Server Architecture

[](#the-server-architecture)

flowchart TB
    %% ── Client side ──────────────────────────
    subgraph ClientProcess["process"]
        A["Your Business Logic"]
        B["microsandbox SDK"]
        A -->|calls| B
    end

    %% ── Server side ─────────────────────────
    subgraph ServerProcess["process"]
        C["microsandbox server"]
    end
    B -->|sends untrusted code to| C

    %% ── Branching hub ───────────────────────
    D([ ])
    C -->|runs code in| D

    %% ── Individual MicroVMs ────────────────
    subgraph VM1["microVM"]
        VM1S["python environment"]
    end

    subgraph VM2["microVM"]
        VM2S["python environment"]
    end

    subgraph VM3["microVM"]
        VM3S["node environment"]
    end

    D --> VM1S
    D --> VM2S
    D --> VM3S

    %% ── Styling ─────────────────────────────
    style A    fill:#D6EAF8,stroke:#2E86C1,stroke-width:2px,color:#000000
    style B    fill:#D6EAF8,stroke:#2E86C1,stroke-width:2px,color:#000000
    style C    fill:#D5F5E3,stroke:#28B463,stroke-width:2px,color:#000000
    style D    fill:#F4F6F6,stroke:#ABB2B9,stroke-width:2px,color:#000000
    style VM1S fill:#FCF3CF,stroke:#F1C40F,stroke-width:2px,color:#000000
    style VM2S fill:#FCF3CF,stroke:#F1C40F,stroke-width:2px,color:#000000
    style VM3S fill:#FCF3CF,stroke:#F1C40F,stroke-width:2px,color:#000000


Loading

• • •

# DEVELOPMENT

[](#development)

Interested in contributing to microsandbox? Check out ourDevelopment Guidefor instructions on setting up your development environment, building the project, running tests, and creating releases.

For contribution guidelines, please refer toCONTRIBUTING.md.

• • •

# LICENSE

[](#license)

This project is licensed under theApache License 2.0.

• • •

# STAR HISTORY

[](#star-history)

Thanks for all the support!

[](https://star-history.com/#microsandbox/microsandbox&Date)

• • •
