---
title: GitHub - ahujasid/blender-mcp · GitHub
url: https://github.com/ahujasid/blender-mcp
site_name: github
content_file: github-github-ahujasidblender-mcp-github
fetched_at: '2026-04-12T11:34:10.747696'
original_url: https://github.com/ahujasid/blender-mcp
author: ahujasid
description: Contribute to ahujasid/blender-mcp development by creating an account on GitHub.
---

ahujasid



/

blender-mcp

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.9k
* Star19k




 
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

139 Commits
139 Commits
assets
assets
 
 
src/
blender_mcp
src/
blender_mcp
 
 
.DS_Store
.DS_Store
 
 
.gitignore
.gitignore
 
 
.python-version
.python-version
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
TERMS_AND_CONDITIONS.md
TERMS_AND_CONDITIONS.md
 
 
addon.py
addon.py
 
 
main.py
main.py
 
 
pyproject.toml
pyproject.toml
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

# BlenderMCP - Blender Model Context Protocol Integration

BlenderMCP connects Blender to Claude AI through the Model Context Protocol (MCP), allowing Claude to directly interact with and control Blender. This integration enables prompt assisted 3D modeling, scene creation, and manipulation.

We have no official website. Any website you see online is unofficial and has no affiliation with this project. Use them at your own risk.

Full tutorial

### Join the Community

Give feedback, get inspired, and build on top of the MCP:Discord

### Supporters

CodeRabbit

All supporters:

Support this project

## Current version(1.5.5)

* Added Hunyuan3D support
* View screenshots for Blender viewport to better understand the scene
* Search and download Sketchfab models
* Support for Poly Haven assets through their API
* Support to generate 3D models using Hyper3D Rodin
* Run Blender MCP on a remote host
* Telemetry for tools executed (completely anonymous)

### Installating a new version (existing users)

* For newcomers, you can go straight to Installation. For existing users, see the points below
* Download the latest addon.py file and replace the older one, then add it to Blender
* Delete the MCP server from Claude and add it back again, and you should be good to go!

## Features

* Two-way communication: Connect Claude AI to Blender through a socket-based server
* Object manipulation: Create, modify, and delete 3D objects in Blender
* Material control: Apply and modify materials and colors
* Scene inspection: Get detailed information about the current Blender scene
* Code execution: Run arbitrary Python code in Blender from Claude

## Components

The system consists of two main components:

1. Blender Addon (addon.py): A Blender addon that creates a socket server within Blender to receive and execute commands
2. MCP Server (src/blender_mcp/server.py): A Python server that implements the Model Context Protocol and connects to the Blender addon

## Installation

### Prerequisites

* Blender 3.0 or newer
* Python 3.10 or newer
* uv package manager:

If you're on Mac, please install uv as

brew install uv

On Windows

powershell
-
c
"
irm https://astral.sh/uv/install.ps1 | iex
"


and then add uv to the user path in Windows (you may need to restart Claude Desktop after):

$localBin

=

"
$
env:
USERPROFILE
\.local\bin
"

$userPath

=
 [
Environment
]::GetEnvironmentVariable(
"
Path
"
,

"
User
"
)
[
Environment
]::SetEnvironmentVariable(
"
Path
"
,

"
$userPath
;
$localBin
"
,

"
User
"
)

Otherwise installation instructions are on their website:Install uv

⚠️Do not proceed before installing UV

### Environment Variables

The following environment variables can be used to configure the Blender connection:

* BLENDER_HOST: Host address for Blender socket server (default: "localhost")
* BLENDER_PORT: Port number for Blender socket server (default: 9876)

Example:

export
 BLENDER_HOST=
'
host.docker.internal
'

export
 BLENDER_PORT=9876

### Claude for Desktop Integration

Watch the setup instruction video(Assuming you have already installed uv)

Go to Claude > Settings > Developer > Edit Config > claude_desktop_config.json to include the following:

{

"mcpServers"
: {

"blender"
: {

"command"
:
"
uvx
"
,

"args"
: [

"
blender-mcp
"

 ]
 }
 }
}

Claude Code

Use the Claude Code CLI to add the blender MCP server:

claude mcp add blender uvx blender-mcp

### Cursor integration

For Mac users, go to Settings > MCP and paste the following

* To use as a global server, use "add new global MCP server" button and paste
* To use as a project specific server, create.cursor/mcp.jsonin the root of the project and paste

{

"mcpServers"
: {

"blender"
: {

"command"
:
"
uvx
"
,

"args"
: [

"
blender-mcp
"

 ]
 }
 }
}

For Windows users, go to Settings > MCP > Add Server, add a new server with the following settings:

{

"mcpServers"
: {

"blender"
: {

"command"
:
"
cmd
"
,

"args"
: [

"
/c
"
,

"
uvx
"
,

"
blender-mcp
"

 ]
 }
 }
}

Cursor setup video

⚠️Only run one instance of the MCP server (either on Cursor or Claude Desktop), not both

### Visual Studio Code Integration

Prerequisites: Make sure you haveVisual Studio Codeinstalled before proceeding.

### Installing the Blender Addon

1. Download theaddon.pyfile from this repo
2. Open Blender
3. Go to Edit > Preferences > Add-ons
4. Click "Install..." and select theaddon.pyfile
5. Enable the addon by checking the box next to "Interface: Blender MCP"

## Usage

### Starting the Connection

1. In Blender, go to the 3D View sidebar (press N if not visible)
2. Find the "BlenderMCP" tab
3. Turn on the Poly Haven checkbox if you want assets from their API (optional)
4. Click "Connect to Claude"
5. Make sure the MCP server is running in your terminal

### Using with Claude

Once the config file has been set on Claude, and the addon is running on Blender, you will see a hammer icon with tools for the Blender MCP.

#### Capabilities

* Get scene and object information
* Create, delete and modify shapes
* Apply or create materials for objects
* Execute any Python code in Blender
* Download the right models, assets and HDRIs throughPoly Haven
* AI generated 3D models throughHyper3D Rodin

### Example Commands

Here are some examples of what you can ask Claude to do:

* "Create a low poly scene in a dungeon, with a dragon guarding a pot of gold"Demo
* "Create a beach vibe using HDRIs, textures, and models like rocks and vegetation from Poly Haven"Demo
* Give a reference image, and create a Blender scene out of itDemo
* "Generate a 3D model of a garden gnome through Hyper3D"
* "Get information about the current scene, and make a threejs sketch from it"Demo
* "Make this car red and metallic"
* "Create a sphere and place it above the cube"
* "Make the lighting like a studio"
* "Point the camera at the scene, and make it isometric"

## Hyper3D integration

Hyper3D's free trial key allows you to generate a limited number of models per day. If the daily limit is reached, you can wait for the next day's reset or obtain your own key from hyper3d.ai and fal.ai.

## Troubleshooting

* Connection issues: Make sure the Blender addon server is running, and the MCP server is configured on Claude, DO NOT run the uvx command in the terminal. Sometimes, the first command won't go through but after that it starts working.
* Timeout errors: Try simplifying your requests or breaking them into smaller steps
* Poly Haven integration: Claude is sometimes erratic with its behaviour
* Have you tried turning it off and on again?: If you're still having connection errors, try restarting both Claude and the Blender server

## Technical Details

### Communication Protocol

The system uses a simple JSON-based protocol over TCP sockets:

* Commandsare sent as JSON objects with atypeand optionalparams
* Responsesare JSON objects with astatusandresultormessage

## Limitations & Security Considerations

* Theexecute_blender_codetool allows running arbitrary Python code in Blender, which can be powerful but potentially dangerous. Use with caution in production environments. ALWAYS save your work before using it.
* Poly Haven requires downloading models, textures, and HDRI images. If you do not want to use it, please turn it off in the checkbox in Blender.
* Complex operations might need to be broken down into smaller steps

#### Telemetry Control

BlenderMCP collects anonymous usage data to help improve the tool. You can control telemetry in two ways:

1. In Blender: Go to Edit > Preferences > Add-ons > Blender MCP and uncheck the telemetry consent checkbox* With consent (checked): Collects anonymized prompts, code snippets, and screenshots
* Without consent (unchecked): Only collects minimal anonymous usage data (tool names, success/failure, duration)
2. Environment Variable: Completely disable all telemetry by running:

DISABLE_TELEMETRY=true uvx blender-mcp

Or add it to your MCP config:

{

"mcpServers"
: {

"blender"
: {

"command"
:
"
uvx
"
,

"args"
: [
"
blender-mcp
"
],

"env"
: {

"DISABLE_TELEMETRY"
:
"
true
"

 }
 }
 }
}

All telemetry data is fully anonymized and used solely to improve BlenderMCP.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Disclaimer

This is a third-party integration and not made by Blender. Made bySiddharth

## About

 No description, website, or topics provided.


### Resources

 Readme



### License

 MIT license


### Uh oh!

There was an error while loading.Please reload this page.





Activity


### Stars

19k

 stars


### Watchers

168

 watching


### Forks

1.9k

 forks


 Report repository



## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.





### Uh oh!

There was an error while loading.Please reload this page.





## Contributors

### Uh oh!

There was an error while loading.Please reload this page.





## Languages

* Python100.0%
