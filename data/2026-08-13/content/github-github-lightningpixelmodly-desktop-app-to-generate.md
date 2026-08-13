---
title: 'GitHub - lightningpixel/modly: Desktop app to generate 3D models from images using local AI — runs entirely on your GPU · GitHub'
url: https://github.com/lightningpixel/modly
site_name: github
content_file: github-github-lightningpixelmodly-desktop-app-to-generate
fetched_at: '2026-08-13T11:44:33.020018'
original_url: https://github.com/lightningpixel/modly
author: lightningpixel
description: Desktop app to generate 3D models from images using local AI — runs entirely on your GPU - lightningpixel/modly
---

lightningpixel

 

/

modly

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork565
* Star5.1k

 
 
 
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

366 Commits
366 Commits
.githooks
.githooks
 
 
.github
.github
 
 
api
api
 
 
arch/
decisions
arch/
decisions
 
 
docs
docs
 
 
electron
electron
 
 
resources
resources
 
 
scripts
scripts
 
 
src
src
 
 
tools/
modly-cli
tools/
modly-cli
 
 
.gitignore
.gitignore
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
electron.vite.config.ts
electron.vite.config.ts
 
 
eslint.config.mjs
eslint.config.mjs
 
 
launch.bat
launch.bat
 
 
launch.sh
launch.sh
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
postcss.config.js
postcss.config.js
 
 
tailwind.config.js
tailwind.config.js
 
 
tsconfig.builtins.json
tsconfig.builtins.json
 
 
tsconfig.json
tsconfig.json
 
 
tsconfig.node.json
tsconfig.node.json
 
 
tsconfig.web.json
tsconfig.web.json
 
 
View all files

## Repository files navigation

# Modly

Local, open source, AI-powered image-to-3D mesh generation.Turn any photo into a 3D model using open source AI models running entirely on your GPU.
Modly is a desktop application for Windows, Linux, and Apple Silicon macOS.

Created byLightning Pixel

## Download

Head to theReleasespage to download the latest installer for Windows, Linux, or Apple Silicon macOS.

Alternatively, you can clone the repository and run the app directly without installing:

#
 Windows

launch.bat

#
 Linux / macOS

./launch.sh

## Getting started

### 1. Install JS dependencies

npm install

### 2. Set up Python backend

cd
 api
python -m venv .venv
.venv
\S
cripts
\a
ctivate 
#
 Windows

source
 .venv/bin/activate 
#
 Linux / macOS

pip install -r requirements.txt

### 3. Run in development

npm run dev

### 4. Test

npm 
test

./node_modules/.bin/tsc --noEmit -p tsconfig.node.json
npm run build

## Platform notes

* macOS support targets Apple Silicon only.
* macOS uses native window controls. Windows and Linux keep the existing custom controls.
* The top bar includes a live RAM indicator sourced from the main process.
* Workflow wiring is validated before run; invalid graphs stay in place and surface inline/toast warnings instead of dropping the current mesh view.
* Package Apple Silicon macOS withnpm run package:mac.
* Imported meshes can be smoothed and decimated in-app; optimized results are written back into the workspace.

## Extension system

Modly supports external model and process extensions. Each extension is a GitHub repository containing amanifest.jsonplus the runtime entry files required by its type.

### Official extensions

Extension

Model

URL

modly-hunyuan3d-mini-extension

Hunyuan3D 2 Mini

https://github.com/lightningpixel/modly-hunyuan3d-mini-extension

modly-hunyuan3d-mini-turbo-extension

Hunyuan3D 2 Mini Turbo

https://github.com/lightningpixel/modly-hunyuan3d-mini-turbo-extension

modly-hunyuan3d-mini-fast-extension

Hunyuan3D 2 Mini Fast

https://github.com/lightningpixel/modly-hunyuan3d-mini-fast-extension

modly-triposg-extension

TripoSG

https://github.com/lightningpixel/modly-triposg-extension

modly-trellis2-gguf-extension

Trellis2 GGUF

https://github.com/lightningpixel/modly-trellis2-gguf-extension

### How to install an extension

1.Go to theModelspage and clickInstall from GitHub.

2.Enter the HTTPS URL of the extension repository and confirm.

3.If the extension exposes model nodes, download the model or one of its variants. Process extensions are ready once installation and setup complete.

## Workflows

Start with a basic workflow first. For example, on the "Workflows" tab, try: Image -> Generate Mesh -> Add to Scene. Make sure there is a connection between each of the steps. Go to the "Generate" tab, make sure the workflow is selected, then click on "Generate 3D Model". Click on "Settings/Logs/Errors" to see any issues.

## Modly CLI

Agents and scripts can call a running Modly desktop app without using the UI via the stdlib-only CLI. The CLI is a thin helper over Modly's canonical automation concepts and keeps final machine-readable JSON on stdout:

python tools/modly-cli/agent.py health
python tools/modly-cli/agent.py model list
python tools/modly-cli/agent.py workflow-run status 
<
run_id
>

python tools/modly-cli/agent.py generate --image ./input.png --output ./export.glb

Canonical commands arehealth,model,workflow-run,capability, andprocess-run. The friendlygeneratecommand startsPOST /workflow-runs/from-image, polls the returned run, exports the final mesh when requested, and includes recovery metadata such asworkflow-run status ...andworkflow-run cancel ...in the JSON response.

Compatibility and helper surfaces are intentionally separated:legacywraps old/generate/*job endpoints,dev serve-api/dev ensure-serverstart only the FastAPI backend and do not prove Electron/Desktop bridge readiness, andexperimental comfy-image/experimental generate-from-workfloware external ComfyUI orchestration helpers rather than the canonical Modly agent contract. Hidden helper aliases such asstatus,export, andbatchremain parseable for scripts, but they are not presented as canonical root commands.

experimental generate-from-workflow --workflow <name> --output <path>treats--outputas the final artifact location. When the ComfyUI workflow produces a downloadable 3D asset, the CLI downloads it directly; image-only workflows remain a compatibility path through Modly image-to-3D generation.

Seetools/modly-cli/SKILL.mdfor the agent workflow and output contract.

### Community

Join theDiscord serverto stay up to date with the latest news, report bugs, and share feedback.

## Sponsors

Thanks to our early sponsors for believing in Modly and helping make local AI 3D generation more accessible.

DrHepabenjapenjaminiammojogo-sudo

## License

MIT License — seeLICENSEfor details.

If you fork this project and build your own app from it, you must credit the original project and its creator:

Based onModlybyLightning Pixel

This is a requirement of the MIT license attribution clause. Please keep this credit visible in your app's UI or documentation.