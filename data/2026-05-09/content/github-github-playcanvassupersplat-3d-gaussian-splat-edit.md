---
title: 'GitHub - playcanvas/supersplat: 3D Gaussian Splat Editor · GitHub'
url: https://github.com/playcanvas/supersplat
site_name: github
content_file: github-github-playcanvassupersplat-3d-gaussian-splat-edit
fetched_at: '2026-05-09T11:49:38.464056'
original_url: https://github.com/playcanvas/supersplat
author: playcanvas
description: 3D Gaussian Splat Editor. Contribute to playcanvas/supersplat development by creating an account on GitHub.
---

playcanvas

 

/

supersplat

Public

* NotificationsYou must be signed in to change notification settings
* Fork695
* Star6k

 
 
 
 
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

619 Commits
619 Commits
.github/
workflows
.github/
workflows
 
 
docs
docs
 
 
src
src
 
 
static
static
 
 
.gitignore
.gitignore
 
 
.prettierignore
.prettierignore
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
copy-and-watch.mjs
copy-and-watch.mjs
 
 
eslint.config.mjs
eslint.config.mjs
 
 
global.d.ts
global.d.ts
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
renovate.json
renovate.json
 
 
rollup.config.mjs
rollup.config.mjs
 
 
tsconfig.json
tsconfig.json
 
 
View all files

## Repository files navigation

# SuperSplat Editor

|SuperSplat Editor|User Guide|Blog|Forum|

The SuperSplat Editor is a free and open source tool for inspecting, editing, optimizing and publishing 3D Gaussian Splats. It is built on web technologies and runs in the browser, so there's nothing to download or install.

A live version of this tool is available at:https://superspl.at/editor

To learn more about using SuperSplat, please refer to theUser Guide.

## Local Development

To initialize a local development environment for SuperSplat, ensure you haveNode.js18 or later installed. Follow these steps:

1. Clone the repository:git clone https://github.com/playcanvas/supersplat.gitcdsupersplat
2. Install dependencies:npm install
3. Build SuperSplat and start a local web server:npm run develop
4. Open a web browser tab and make sure network caching is disabled on the network tab and the other application caches are clear:* On Safari you can useCmd+Option+eor Develop->Empty Caches.
* On Chrome ensure the options "Update on reload" and "Bypass for network" are enabled in the Application->Service workers tab:
5. Navigate tohttp://localhost:3000

When changes to the source are detected, SuperSplat is rebuilt automatically. Simply refresh your browser to see your changes.

## Localizing the SuperSplat Editor

The currently supported languages are available here:

https://github.com/playcanvas/supersplat/tree/main/static/locales

### Adding a New Language

1. Add a new<locale>.jsonfile in thestatic/localesdirectory.
2. Add the locale to the list here:https://github.com/playcanvas/supersplat/blob/main/src/ui/localization.ts

### Testing Translations

To test your translations:

1. Run the development server:npm run develop
2. Open your browser and navigate to:http://localhost:3000/?lng=<locale>Replace<locale>with your language code (e.g.,fr,de,es).

## Contributors

SuperSplat is made possible by our amazing open source community:

## About

3D Gaussian Splat Editor

superspl.at/editor

### Topics

 webgl

 typescript

 playcanvas

 webgpu

 pcui

 gaussian-splatting

 3d-gaussian-splatting

 3dgs

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

6k

 stars
 

### Watchers

63

 watching
 

### Forks

695

 forks
 

 Report repository

 

## Releases144

v2.25.1

 Latest

 

May 8, 2026

 

+ 143 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript92.3%
* SCSS5.3%
* JavaScript2.3%
* HTML0.1%