---
title: 'GitHub - electrikmilk/cherri: Siri Shortcuts Programming Language 🍒 · GitHub'
url: https://github.com/electrikmilk/cherri
site_name: hnrss
content_file: hnrss-github-electrikmilkcherri-siri-shortcuts-programmi
fetched_at: '2026-03-31T11:22:30.860436'
original_url: https://github.com/electrikmilk/cherri
date: '2026-03-27'
description: Siri Shortcuts Programming Language 🍒. Contribute to electrikmilk/cherri development by creating an account on GitHub.
tags:
- hackernews
- hnrss
---

electrikmilk



/

cherri

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork44
* Star1.1k




 
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

1,990 Commits
1,990 Commits
.github
.github
 
 
actions
actions
 
 
assets
assets
 
 
tests
tests
 
 
.gitignore
.gitignore
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
ReadMe.md
ReadMe.md
 
 
action.go
action.go
 
 
actions_std.go
actions_std.go
 
 
args.go
args.go
 
 
cherri_test.go
cherri_test.go
 
 
copy_paste.go
copy_paste.go
 
 
decompile.go
decompile.go
 
 
docs.go
docs.go
 
 
flake.lock
flake.lock
 
 
flake.nix
flake.nix
 
 
functions.go
functions.go
 
 
glyphs.go
glyphs.go
 
 
go.mod
go.mod
 
 
go.sum
go.sum
 
 
import.go
import.go
 
 
includes.go
includes.go
 
 
main.go
main.go
 
 
output.go
output.go
 
 
packages.go
packages.go
 
 
parser.go
parser.go
 
 
search.go
search.go
 
 
shortcut.go
shortcut.go
 
 
shortcutgen.go
shortcutgen.go
 
 
signing.go
signing.go
 
 
stdlib.cherri
stdlib.cherri
 
 
token.go
token.go
 
 
toolkit.go
toolkit.go
 
 
variables.go
variables.go
 
 
version.go
version.go
 
 
View all files

## Repository files navigation

# Cherri

Cherri(pronounced cherry) is aShortcutsprogramming language that compiles directly to a valid runnable Shortcut.

The primary goal is to make it practical to create large Shortcut projects (within the limitations of Shortcuts) and maintain them long term.

### 🌟 Top Features

* 🖥️ Laptop/Desktop-based development (CLI,VSCode extension, macOS app)
* 🎓 Easy to learn and syntax similar to other languages
* 🐞 1-1 translation to Shortcut actions as much as possible to make debugging easier
* 🥾 Half-bootstrapped: Most actions and types are written in the language
* 💻 Import actions on your Mac
* 📦 Package manager: Remote Git repo-based package manager built in, allowing for automatic inclusion and updates.
* 🪄 No magic variables syntax, they're constants instead
* 🪶 Optimized to create as small as possible Shortcuts and reduce memory usage at runtime
* #️⃣ Include files within others for large Shortcut projects
* 🔧 Define actions with type checking, enums, optionals, default values, raw identifiers, and raw keys.
* 🔄 Define functions to run within their own scope at the top of your Shortcut to reduce duplicate actions.
* 📋 Copy-paste actions automatically
* 🥩 Enter action identifier and parameters manually using Raw Actions.
* ❓ Define import questions
* 📇 Generate VCards for menus
* 📄 Embed files in base64
* 🔀 Convert Shortcuts from an iCloud link with the--import=option
* 🔢 Type system and type inference
* 🔏 Signs using macOS, falls back onHubSignor another server that usesscaxyz/shortcut-signing-server.

### Resources

* 🍒Cherri VSCode Extension
* 🛝Playground- Try out Cherri on any platform, preview the result, and export signed Shortcuts
* 🖥️macOS IDE- Defines Cherri file type, write and build Shortcuts on Mac with a GUI
* 📄Documentation- Learn Cherri or how to contribute
* 🔍Glyph Search- Search glyphs you can use in Cherri!
* ❓FAQ

## Installation

You can install Cherri by downloading the latest release or via the Homebrew or Nix package managers:

### Install via Homebrew

If you have Homebrew installed, you can run:

Add Tap:

brew tap electrikmilk/cherri

Install:

brew install electrikmilk/cherri/cherri

### Install via Nix

If you have Nix installed, you can run:

nix profile install github:electrikmilk/cherri

Alternatively, you can usenix-direnvto get an isolated,effortless dev environmentwherecherriis available based on which directory you're in. Then you would use_flake and add Cherri to flake.nix:

{


inputs
.
cherri
.
url

=

"github:electrikmilk/cherri"
;


{

# outputs.packages.${system}.default = pkgs.mkShell etc - omitted for brevity


buildInputs

=

[


inputs
.
cherri
.
packages
.
${
system
}
.
cherri


]


}

}

Then rundirenv allowin the directory with the flake.nix file.

## Usage

cherri file.cherri

Runcherriwithout any arguments to see all options and usage. For development, use the--debug(or-d) option to print
stack traces, debug information, and output a.plistfile.

## Why another Shortcuts language?

Because it's fun :)

Some languages have been abandoned, don't work well, or no longer work. I don't want Shortcuts languages to die.
There should be more, not less.

Plus, some stability comes with this project being on macOS and not iOS, and I'm not aware of another Shortcuts language with macOS as its platform other thanButtermilk.

## Community

* VS Code Syntax Highlighting(repo)
* Zed Editor

## Credits

### Reference

* zachary7829/Shortcuts File Format Documentation
* sebj/iOS-Shortcuts-Reference
* [Tip] Reducing memory usage of repeat loops

### Inspiration

* Go syntax
* Ruby syntax
* ScPL
* Buttermilk
* Jelly

The original Workflow app assigned a code name to each release. Cherri is named after the second-to-last
update "Cherries" (also cherry is one of my favorite flavors).

This project started on October 5, 2022.

## About

Siri Shortcuts Programming Language 🍒

cherrilang.org

### Topics

 go

 macos

 programming-language

 golang

 ios

 apple

 compiler

 domain-specific-language

 siri-shortcuts

 ios-shortcuts

 apple-shortcuts

 cherri-lang

 cherri

### Resources

 Readme



### License

 GPL-2.0 license


### Code of conduct

 Code of conduct


### Contributing

 Contributing


### Uh oh!

There was an error while loading.Please reload this page.





Activity


### Stars

1.1k

 stars


### Watchers

11

 watching


### Forks

44

 forks


 Report repository



## Releases44

v2.1.1

 Latest



Mar 30, 2026



+ 43 releases

## Sponsor this project

### Uh oh!

There was an error while loading.Please reload this page.






* https://www.paypal.me/johnwaynepizzaparty
* https://routinehub.co/user/electrikmilk
* https://cherrilang.redbubble.com

Learn more about GitHub Sponsors

### Uh oh!

There was an error while loading.Please reload this page.





## Contributors

### Uh oh!

There was an error while loading.Please reload this page.





## Languages

* Go99.5%
* Nix0.5%
