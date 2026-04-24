---
title: 'GitHub - microsoft/typescript-go: Staging repo for development of native port of TypeScript · GitHub'
url: https://github.com/microsoft/typescript-go
site_name: github
content_file: github-github-microsofttypescript-go-staging-repo-for-dev
fetched_at: '2026-04-24T11:56:24.168211'
original_url: https://github.com/microsoft/typescript-go
author: microsoft
description: Staging repo for development of native port of TypeScript - microsoft/typescript-go
---

microsoft

 

/

typescript-go

Public

* NotificationsYou must be signed in to change notification settings
* Fork907
* Star24.9k

 
 
 
 
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

1,940 Commits
1,940 Commits
.devcontainer
.devcontainer
 
 
.github
.github
 
 
.vscode
.vscode
 
 
_build
_build
 
 
_extension
_extension
 
 
_packages/
native-preview
_packages/
native-preview
 
 
_scripts
_scripts
 
 
_submodules
_submodules
 
 
_tools
_tools
 
 
cmd/
tsgo
cmd/
tsgo
 
 
internal
internal
 
 
testdata
testdata
 
 
.custom-gcl.yml
.custom-gcl.yml
 
 
.dprint.jsonc
.dprint.jsonc
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
.golangci.yml
.golangci.yml
 
 
.gulp.js
.gulp.js
 
 
CHANGES.md
CHANGES.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Herebyfile.mjs
Herebyfile.mjs
 
 
LICENSE
LICENSE
 
 
NOTICE.txt
NOTICE.txt
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
SUPPORT.md
SUPPORT.md
 
 
go.mod
go.mod
 
 
go.sum
go.sum
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
View all files

## Repository files navigation

# TypeScript 7

Not sure what this is? Read the announcement post!

## Preview

A preview build is available on npm as@typescript/native-preview.

npm install @typescript/native-preview
npx tsgo 
#
 Use this as you would tsc.

A preview VS Code extension isavailable on the VS Code marketplace.

To use this, set this in your VS Code settings:

{
 
"js/ts.experimental.useTsgo"
: 
true

}

## What Works So Far?

This is still a work in progress and is not yet at full feature parity with TypeScript. Bugs may exist. Please check this list carefully before logging a new issue or assuming an intentional change.

Feature

Status

Notes

Program creation

done

Same files and module resolution as TS 6.0. Not all resolution modes supported yet.

Parsing/scanning

done

Exact same syntax errors as TS 6.0

Commandline and 
tsconfig.json
 parsing

done

Done, though 
tsconfig
 errors may not be as helpful.

Type resolution

done

Same types as TS 6.0.

Type checking

done

Same errors, locations, and messages as TS 6.0. Types printback in errors may display differently.

JavaScript-specific inference and JSDoc

in progress

Mostly complete, but intentionally lacking some features. Declaration emit not complete.

JSX

done

-

Declaration emit

in progress

Done for TypeScript files. Not yet complete for JavaScript files.

Emit (JS output)

done

-

Watch mode

prototype

Watches files and rebuilds, but no incremental rechecking. Not optimized.

Build mode / project references

done

-

Incremental build

done

-

Language service (LSP)

in progress

Nearly all features implemented.

API

not ready

-

Definitions:

* doneaka "believed done": We're not currently aware of any deficits or major work left to do. OK to log bugs
* in progress: currently being worked on; some features may work and some might not. OK to log panics, but nothing else please
* prototype: proof-of-concept only; do not log bugs
* not ready: either haven't even started yet, or far enough from ready that you shouldn't bother messing with it yet

## Other Notes

Long-term, we expect that this repo and its contents will be merged intomicrosoft/TypeScript.
As a result, the repo and issue tracker for typescript-go will eventually be closed, so treat discussions/issues accordingly.

For a list of intentional changes with respect to TypeScript 6.0, see CHANGES.md.

## Contributing

This project welcomes contributions and suggestions. Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visitContributor License Agreements.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted theMicrosoft Open Source Code of Conduct.
For more information see theCode of Conduct FAQor
contactopencode@microsoft.comwith any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft
trademarks or logos is subject to and must followMicrosoft's Trademark & Brand Guidelines.
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.

## About

Staging repo for development of native port of TypeScript

### Resources

 Readme

 

### License

 Apache-2.0 license
 

### Code of conduct

 Code of conduct
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

24.9k

 stars
 

### Watchers

115

 watching
 

### Forks

907

 forks
 

 Report repository

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Go84.7%
* TypeScript12.1%
* JavaScript3.2%