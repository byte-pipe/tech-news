---
title: 'GitHub - webpack/webpack: A bundler for javascript and friends. Packs many modules into a few bundled assets. Code Splitting allows for loading parts of the application on demand. Through "loaders", modules can be CommonJs, AMD, ES6 modules, CSS, Images, JSON, Coffeescript, LESS, ... and your custom stuff. · GitHub'
url: https://github.com/webpack/webpack
site_name: github
content_file: github-github-webpackwebpack-a-bundler-for-javascript-and
fetched_at: '2026-08-04T11:45:58.261913'
original_url: https://github.com/webpack/webpack
author: webpack
description: A bundler for javascript and friends. Packs many modules into a few bundled assets. Code Splitting allows for loading parts of the application on demand. Through "loaders", modules can be CommonJs, AMD, ES6 modules, CSS, Images, JSON, Coffeescript, LESS, ... and your custom stuff. - webpack/webpack
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 webpack

 

/

webpack

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork9.5k
* Star65.9k

 
 
 
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

19,124 Commits
19,124 Commits
.changeset
.changeset
 
 
.github
.github
 
 
.husky
.husky
 
 
assembly
assembly
 
 
bin
bin
 
 
declarations
declarations
 
 
examples
examples
 
 
hot
hot
 
 
lib
lib
 
 
schemas
schemas
 
 
setup
setup
 
 
test
test
 
 
tooling
tooling
 
 
.editorconfig
.editorconfig
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
.istanbul.yml
.istanbul.yml
 
 
.npmrc
.npmrc
 
 
.prettierignore
.prettierignore
 
 
.prettierrc.js
.prettierrc.js
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
GOVERNANCE.md
GOVERNANCE.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
TESTING_DOCS.md
TESTING_DOCS.md
 
 
WORKING_GROUP.md
WORKING_GROUP.md
 
 
_SETUP.md
_SETUP.md
 
 
codecov.yml
codecov.yml
 
 
cspell.json
cspell.json
 
 
declarations.d.ts
declarations.d.ts
 
 
declarations.test.d.ts
declarations.test.d.ts
 
 
eslint.config.mjs
eslint.config.mjs
 
 
generate-types-config.js
generate-types-config.js
 
 
jest.config.js
jest.config.js
 
 
module.d.ts
module.d.ts
 
 
open-bot.yaml
open-bot.yaml
 
 
package.json
package.json
 
 
tsconfig.hot.json
tsconfig.hot.json
 
 
tsconfig.json
tsconfig.json
 
 
tsconfig.module.test.json
tsconfig.module.test.json
 
 
tsconfig.types.benchmark.json
tsconfig.types.benchmark.json
 
 
tsconfig.types.json
tsconfig.types.json
 
 
tsconfig.types.test.json
tsconfig.types.test.json
 
 
tsconfig.validation.json
tsconfig.validation.json
 
 
types.d.ts
types.d.ts
 
 
yarn.lock
yarn.lock
 
 
View all files

## Repository files navigation

# webpack

Webpack is a module bundler. Its main purpose is to bundle JavaScript files for usage in a browser, yet it is also capable of transforming, bundling, or packaging just about any resource or asset.

## Table of Contents

* Install
* Introduction
* Concepts
* Contributing
* Support
* Current project membersTSC (Technical Steering Committee)Core Collaborators
* TSC (Technical Steering Committee)
* Core Collaborators
* SponsoringPremium PartnersGold SponsorsSilver SponsorsBronze SponsorsBackers
* Premium Partners
* Gold Sponsors
* Silver Sponsors
* Bronze Sponsors
* Backers
* Special Thanks

## Install

Install with npm:

npm install --save-dev webpack

Install with yarn:

yarn add webpack --dev

## Introduction

Webpack is a bundler for modules. The main purpose is to bundle JavaScript
files for usage in a browser, yet it is also capable of transforming, bundling,
or packaging just about any resource or asset.

TL;DR

* BundlesES Modules,CommonJS, andAMDmodules (even combined).
* Can create a single bundle or multiple chunks that are asynchronously loaded at runtime (to reduce initial loading time).
* Dependencies are resolved during compilation, reducing the runtime size.
* Loaders can preprocess files while compiling, e.g. TypeScript to JavaScript, Handlebars strings to compiled functions, images to Base64, etc.
* Highly modular plugin system to do whatever else your application requires.

#### Learn about webpack through videos!

* Understanding Webpack - Video 1
* Understanding Webpack - Video 2

### Get Started

Check out webpack's quickGet Startedguide and theother guides.

### Browser Compatibility

Webpack supports all browsers that areES5-compliant(IE8 and below are not supported).
Webpack also needsPromiseforimport()andrequire.ensure(). If you want to support older browsers, you will need toload a polyfillbefore using these expressions.

## Concepts

### Plugins

Webpack has arich plugin
interface. Most of the features
within webpack itself use this plugin interface. This makes webpack veryflexible.

Name

Status

Install Size

Description

mini-css-extract-plugin

Extracts CSS into separate files. It creates a CSS file per JS file which contains CSS.

compression-webpack-plugin

Prepares compressed versions of assets to serve them with Content-Encoding

html-bundler-webpack-plugin

Renders a template (EJS, Handlebars, Pug) with referenced source asset files into HTML.

html-webpack-plugin

Simplifies creation of HTML files (
index.html
) to serve your bundles

pug-plugin

Renders Pug files to HTML, extracts JS and CSS from sources specified directly in Pug.

### Loaders

Webpack enables the use of loaders to preprocess files. This allows you to bundleany static resourceway beyond JavaScript. You can easilywrite your own
loadersusing Node.js.

Loaders are activated by usingloadername!prefixes inrequire()statements,
or are automatically applied via regex from your webpack configuration.

#### JSON

Name

Status

Install Size

Description

Loads and transpiles a CSON file

#### Transpiling

Name

Status

Install Size

Description

Loads ES2015+ code and transpiles to ES5 using 
Babel

Loads TypeScript like JavaScript

Loads CoffeeScript like JavaScript

#### Templating

Name

Status

Install Size

Description

Exports HTML as string, requires references to static resources

Compiles Pug to a function or HTML string, useful for use with Vue, React, Angular

Compiles Markdown to HTML

Loads and transforms a HTML file using 
PostHTML

Compiles Handlebars to HTML

#### Styling

Name

Status

Install Size

Description

<style>

Add exports of a module as style to DOM

Loads CSS file with resolved imports and returns CSS code

Loads and compiles a LESS file

Loads and compiles a Sass/SCSS file

Loads and compiles a Stylus file

Loads and transforms a CSS/SSS file using 
PostCSS

#### Frameworks

Name

Status

Install Size

Description

Loads and compiles Vue Components

Process HTML & CSS with preprocessor of choice and 
require()
 Web Components like first-class modules

Loads and compiles Angular 2 Components

Riot official webpack loader

Official Svelte loader

### Performance

Webpack uses async I/O and has multiple caching levels. This makes webpack fast
and incrediblyfaston incremental compilations.

### Module Formats

Webpack supports ES2015+, CommonJS and AMD modulesout of the box. It performs clever static
analysis on the AST of your code. It even has an evaluation engine to evaluate
simple expressions. This allows you tosupport most existing librariesout of the box.

### Code Splitting

Webpack allows you to split your codebase into multiple chunks. Chunks are
loaded asynchronously at runtime. This reduces the initial loading time.

### Optimizations

Webpack can do many optimizations toreduce the output size of your
JavaScriptby deduplicating frequently used modules, minifying, and giving
you full control of what is loaded initially and what is loaded at runtime
through code splitting. It can also make your code chunkscache
friendlyby using hashes.

### Developer Tools

If you're working on webpack itself, or building advanced plugins or integrations, the tools below can help you explore internal mechanics, debug plugin life-cycles, and build custom tooling.

#### Instrumentation

Name

Status

Description

tapable-tracer

Traces tapable hook execution in real-time and collects structured stack frames. Can export to UML for generating visualizations.

## Contributing

We want contributing to webpack to be fun, enjoyable, and educational for anyone, and everyone.We have avibrant ecosystemthat spans beyond this single repo. We welcome you to check out any of the repositories inour organizationorwebpack-contrib organizationwhich houses all of our loaders and plugins.

Contributions go far beyond pull requests and commits. Although we love giving you the opportunity to put your stamp on webpack, we also are thrilled to receive a variety of other contributions including:

* Documentationupdates, enhancements, designs, or bugfixes
* Spelling or grammar fixes
* README.md corrections or redesigns
* Adding unit, or functional tests
* Triaging GitHub issues -- especially determining whether an issue still persists or is reproducible.
* Searching #webpack on twitterand helping someone else who needs help
* Teaching others how to contribute to one of the many webpack's repos!
* Blogging, speaking about, or creating tutorialsabout one of webpack's many features.
* Helping others in our webpackgitter channel.
* The Contributor's Guide to webpack

To get started have a look at ourdocumentation on contributing.

### Creating your own plugins and loaders

If you create a loader or plugin, we would <3 for you to open source it, and put it on npm. We follow thex-loader,x-webpack-pluginnaming convention.

## Support

We consider webpack to be a low-level tool used not only individually but also layered beneath other awesome tools. Because of its flexibility, webpack isn't always theeasiestentry-level solution, however we do believe it is the most powerful. That said, we're always looking for ways to improve and simplify the tool without compromising functionality. If you have any ideas on ways to accomplish this, we're all ears!

If you're just getting started, take a look atour new docs and concepts page. This has a high level overview that is great for beginners!!

If you have discovered a 🐜 or have a feature suggestion, feel free to create an issue on GitHub.

## Current project members

For information about the governance of the webpack project, seeGOVERNANCE.md.

### TSC (Technical Steering Committee)

* alexander-akait-Alexander Akait<sheo13666q@gmail.com> (he/him)
* avivkeller-Aviv Keller<me@aviv.sh> (he/him)
* evenstensberg-Even Stensberg<evenstensberg@gmail.com> (he/him)
* ovflowd-Claudio Wunder<cwunder@gnome.org> (he/they)
* thelarkinn-Sean Larkin<selarkin@microsoft.com> (he/him)

### Maintenance

This webpack repository is maintained by theCore Working Group.

## Sponsoring

Most of the core team members, webpack contributors and contributors in the ecosystem do this open source work in their free time. If you use webpack for a serious task, and you'd like us to invest more time on it, please donate. This project increases your income/productivity too. It makes development and applications faster and it reduces the required bandwidth.

This is how we use the donations:

* Allow the core team to work on webpack
* Thank contributors if they invested a large amount of time in contributing
* Support projects in the ecosystem that are of great value for users
* Support projects that are voted most (work in progress)
* Infrastructure cost
* Fees for money handling

### Premium Partners

### Other Backers and Sponsors

Before we started using OpenCollective, donations were made anonymously. Now that we have made the switch, we would like to acknowledge these sponsors (and the ones who continue to donate using OpenCollective). If we've missed someone, please send us a PR, and we'll add you to this list.

AngularMoonMailMONEI

### Gold Sponsors

Become a gold sponsorand get your logo on our README on GitHub with a link to your site.

### Silver Sponsors

Become a silver sponsorand get your logo on our README on GitHub with a link to your site.

### Bronze Sponsors

Become a bronze sponsorand get your logo on our README on GitHub with a link to your site.

### Backers

Become a backerand get your image on our README on GitHub with a link to your site.

## Other Partners

* CodSpeedfor generously supporting us with benchmarks on their paid runners.

## Special Thanks to

(In chronological order)

* @googleforGoogle Web Toolkit (GWT), which aims to compile Java to JavaScript. It features a similarCode Splittingas webpack.
* @medikooformodules-webmake, which is a similar project. webpack was born because of the desire for code splitting for modules such as Webmake. Interestingly, theCode Splitting issue is still open(thanks also to @Phoscur for the discussion).
* @substackforbrowserify, which is a similar project and source for many ideas.
* @jrburkeforrequire.js, which is a similar project and source for many ideas.
* @defunctzombiefor thebrowser-field spec, which makes modules available for node.js, browserify and webpack.
* @sokrafor creating webpack.
* Every early webpack user, which contributed to webpack by writing issues or PRs. You influenced the direction.
* All past and current webpack maintainers and collaborators.
* Everyone who has written a loader for webpack. You are the ecosystem...
* Everyone not mentioned here but that has also influenced webpack.