---
title: 'GitHub - biomejs/biome: A toolchain for web projects, aimed to provide functionalities to maintain them. Biome offers formatter and linter, usable via CLI and LSP. · GitHub'
url: https://github.com/biomejs/biome
site_name: github
content_file: github-github-biomejsbiome-a-toolchain-for-web-projects-a
fetched_at: '2026-06-18T12:19:22.080250'
original_url: https://github.com/biomejs/biome
author: biomejs
description: A toolchain for web projects, aimed to provide functionalities to maintain them. Biome offers formatter and linter, usable via CLI and LSP. - biomejs/biome
---

biomejs

 

/

biome

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork1k
* Star25.1k

 
 
 
 
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

10,312 Commits
10,312 Commits
.cargo
.cargo
 
 
.changeset
.changeset
 
 
.claude
.claude
 
 
.devcontainer
.devcontainer
 
 
.github
.github
 
 
crates
crates
 
 
e2e-tests
e2e-tests
 
 
fuzz
fuzz
 
 
packages
packages
 
 
plugins
plugins
 
 
scripts
scripts
 
 
xtask
xtask
 
 
.biome.json
.biome.json
 
 
.coderabbit.yaml
.coderabbit.yaml
 
 
.dockerignore
.dockerignore
 
 
.editorconfig
.editorconfig
 
 
.git-blame-ignore-revs
.git-blame-ignore-revs
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.markdownlint.json
.markdownlint.json
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CHANGELOG_v1.md
CHANGELOG_v1.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
GOVERNANCE.md
GOVERNANCE.md
 
 
LICENSE-APACHE
LICENSE-APACHE
 
 
LICENSE-MIT
LICENSE-MIT
 
 
README.md
README.md
 
 
RELEASES.md
RELEASES.md
 
 
clippy.toml
clippy.toml
 
 
deny.toml
deny.toml
 
 
insta.yml
insta.yml
 
 
justfile
justfile
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
pnpm-workspace.yaml
pnpm-workspace.yaml
 
 
rust-toolchain.toml
rust-toolchain.toml
 
 
rustfmt.toml
rustfmt.toml
 
 
tombi.toml
tombi.toml
 
 
View all files

## Repository files navigation

हिन्दी| English |Español|Français|繁體中文|简体中文|日本語|Polski|Português do Brasil|한국어|Русский|Українська

Biomeis a performant toolchain for web projects, it aims to provide developer tools to maintain the health of said projects.

Biome is afast formatterforJavaScript,TypeScript,JSX,JSON,CSSandGraphQLthat scores97% compatibility withPrettier.

Biome is aperformant linterforJavaScript,TypeScript,JSX,JSON,CSS, andGraphQLthat featuresmore than 500 rulesfrom ESLint, typescript-eslint, andother sources.
Itoutputs detailed and contextualized diagnosticsthat help you to improve your code and become a better programmer!

Biomeis designed from the start to be usedinteractively within an editor.
It can format and lint malformed code as you are writing it.

### Installation

npm install --save-dev --save-exact @biomejs/biome

### Usage

#
 format files

npx @biomejs/biome format --write

#
 lint files and apply the safe fixes

npx @biomejs/biome lint --write

#
 run format, lint, etc. and apply the safe fixes

npx @biomejs/biome check --write

#
 check all files against format, lint, etc. in CI environments

npx @biomejs/biome ci

If you want to give Biome a run without installing it, use theonline playground, compiled to WebAssembly.

## Documentation

Check out ourhomepageto learn more about Biome,
or directly head to theGetting Started guideto start using Biome.

## More about Biome

Biomehas sane defaults and it doesn't require configuration.

Biomeaims to supportall main languagesof modern web development.

Biomedoesn't require Node.jsto function.

Biomehas first-class LSP support, with a sophisticated parser that represents the source text in full fidelity and top-notch error recovery.

Biomewants to offer a high-qualityDeveloper Experience, with descriptive diagnostics and great performance.

Biomeunifies functionalities that have previously been separate tools. Building upon a shared base allows us to provide a cohesive experience for processing code, displaying errors, parallelize work, caching, and configuration.

Read more about ourproject philosophy.

BiomeisMIT licensedorApache 2.0 licensedand moderated under theContributor Covenant Code of Conduct.

## Funding

You can fund the project in different ways

### Project sponsorship and funding

You can sponsor or fund the project viaOpen collectiveorGitHub sponsors

Biome offers a simple sponsorship program that allows companies to get visibility and recognition among various developers.

Biome offersenterprise support, where Core Contributors can be employed to work on company-focused projects.

## Sponsors

### Platinum Sponsors

### Silver Sponsors

### Bronze Sponsors

## About

A toolchain for web projects, aimed to provide functionalities to maintain them. Biome offers formatter and linter, usable via CLI and LSP.

biomejs.dev

### Topics

 javascript

 css

 json

 formatter

 typescript

 web

 static-code-analysis

 jsx

 linter

### Resources

 Readme

 

### License

 Apache-2.0, MIT licenses found
 

### Licenses found

Apache-2.0

LICENSE-APACHE

 

MIT

LICENSE-MIT

 

### Code of conduct

 Code of conduct
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

25.1k

 stars
 

### Watchers

92

 watching
 

### Forks

1k

 forks
 

 Report repository

 

## Releases146

Biome CLI v2.5.0

 Latest

 

Jun 12, 2026

 

+ 145 releases

## Sponsor this project

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 
* opencollective.com/biome
* thanks.dev/u/gh/biomejs

Learn more about GitHub Sponsors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Rust85.7%
* JavaScript6.9%
* TypeScript3.5%
* CSS1.6%
* SCSS0.6%
* HTML0.6%
* Other1.1%