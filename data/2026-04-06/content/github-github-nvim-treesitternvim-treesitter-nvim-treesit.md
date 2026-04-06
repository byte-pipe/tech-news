---
title: 'GitHub - nvim-treesitter/nvim-treesitter: Nvim Treesitter configurations and abstraction layer · GitHub'
url: https://github.com/nvim-treesitter/nvim-treesitter
site_name: github
content_file: github-github-nvim-treesitternvim-treesitter-nvim-treesit
fetched_at: '2026-04-06T11:21:45.723578'
original_url: https://github.com/nvim-treesitter/nvim-treesitter
author: nvim-treesitter
description: Nvim Treesitter configurations and abstraction layer - nvim-treesitter/nvim-treesitter
---

This repository was archived by the owner on Apr 3, 2026. It is now read-only.
 

 nvim-treesitter

 

/

nvim-treesitter

Public archive

* NotificationsYou must be signed in to change notification settings
* Fork1.2k
* Star13.5k

 
 
 
 
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

6,388 Commits
6,388 Commits
.github
.github
 
 
doc
doc
 
 
lua/
nvim-treesitter
lua/
nvim-treesitter
 
 
plugin
plugin
 
 
runtime/
queries
runtime/
queries
 
 
scripts
scripts
 
 
tests
tests
 
 
.editorconfig
.editorconfig
 
 
.emmyrc.json
.emmyrc.json
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.luarc.json
.luarc.json
 
 
.stylua.toml
.stylua.toml
 
 
.styluaignore
.styluaignore
 
 
.tsqueryrc.json
.tsqueryrc.json
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
SUPPORTED_LANGUAGES.md
SUPPORTED_LANGUAGES.md
 
 
View all files

## Repository files navigation

Thenvim-treesitterplugin provides

1. functions for installing, updating, and removingtree-sitter parsers;
2. a collection ofqueriesfor enabling tree-sitter features built into Neovim for these languages;
3. a staging ground fortreesitter-based featuresconsidered for upstreaming to Neovim.

For details on these and how to help improving them, seeCONTRIBUTING.md.

Caution

This is a full, incompatible, rewrite: Treat this as a different plugin you need to set up from scratch following the instructions below. If you can't or don't want to update, specify themasterbranch(which is locked but will remain available for backward compatibility with Nvim 0.11).

# Quickstart

## Requirements

* Neovim 0.12.0 or later (nightly)
* tarandcurlin your path
* tree-sitter-cli(0.26.1 or later, installed via your package manager,not npm)
* a C compiler in your path (seehttps://docs.rs/cc/latest/cc/#compile-time-requirements)

Important

The currentsupport policyfor Neovim is

* thelateststable release,
* thelatestnightly prerelease.
Other versions may work but are neither tested nor considered for fixes.

## Installation

You can installnvim-treesitterwith your favorite package manager (or using the nativepackagefeature of vim, see:h packages).

This plugin is only guaranteed to work with specific versions of language parsers** (as specified in theparser.luatable).When upgrading the plugin, you must make sure that all installed parsers are updated to the latest versionvia:TSUpdate.
It is strongly recommended to automate this; e.g., using the following spec withlazy.nvim:

{
 
'
nvim-treesitter/nvim-treesitter
'
,
 
lazy
 
=
 
false
,
 
build
 
=
 
'
:TSUpdate
'

}

Important

This plugin does not support lazy-loading.

## Setup

nvim-treesittercan be configured by callingsetup.You do not need to callsetupfornvim-treesitterto work using default values.

require
(
'
nvim-treesitter
'
).
setup
 {
 
--
 Directory to install parsers and queries to (prepended to `runtimepath` to have priority)

 
install_dir
 
=
 
vim
.
fn
.
stdpath
(
'
data
'
) 
..
 
'
/site
'

}

Parsers and queries can then be installed with

require
(
'
nvim-treesitter
'
).
install
 { 
'
rust
'
, 
'
javascript
'
, 
'
zig
' 
}

(This is a no-op if the parsers are already installed.) Note that this function runs asynchronously; for synchronous installation in a script context ("bootstrapping"), you need towait()for it to finish:

require
(
'
nvim-treesitter
'
).
install
({ 
'
rust
'
, 
'
javascript
'
, 
'
zig
' 
}):
wait
(
300000
) 
--
 wait max. 5 minutes

Check:h nvim-treesitter-commandsfor a list of all available commands.

# Supported languages

Fornvim-treesitterto support a specific feature for a specific language requires both a parser for that language and an appropriate language-specific query file for that feature.

A list of the currently supported languages can be foundon this page. If you wish to add a new language or improve the queries for an existing one, please see ourcontributing guide.

# Supported features

nvim-treesitterprovides queries for the following features.These are not automatically enabled.

## Highlighting

Treesitter highlighting is provided by Neovim, see:h treesitter-highlight. To enable it for a filetype, putvim.treesitter.start()in aftplugin/<filetype>.luain your config directory, or place the following in yourinit.lua:

vim
.
api
.
nvim_create_autocmd
(
'
FileType
'
, {
 
pattern
 
=
 { 
'
<filetype>
' 
},
 
callback
 
=
 
function
() 
vim
.
treesitter
.
start
() 
end
,
})

## Folds

Treesitter-based folding is provided by Neovim. To enable it, put the following in yourftpluginorFileTypeautocommand:

vim
.
wo
[
0
][
0
].
foldexpr
 
=
 
'
v:lua.vim.treesitter.foldexpr()
'

vim
.
wo
[
0
][
0
].
foldmethod
 
=
 
'
expr
'

## Indentation

Treesitter-based indentation is provided by this plugin but consideredexperimental. To enable it, put the following in yourftpluginorFileTypeautocommand:

vim
.
bo
.
indentexpr
 
=
 
"
v:lua.require'nvim-treesitter'.indentexpr()
"

(Note the specific quotes used.)

## Injections

Injections are used for multi-language documents, see:h treesitter-language-injections. No setup is needed.

## Locals

These queries can be used to look up definitions and references to identifiers in a given scope. They are not used in this plugin and are provided for (limited) backward compatibility.

# Advanced setup

## Adding custom languages

If you have a parser that is not on the list of supported languages (either as a repository on Github or in a local directory), you can add it manually for use bynvim-treesitteras follows:

1. Add the following snippet in aUser TSUpdateautocommand:

vim
.
api
.
nvim_create_autocmd
(
'
User
'
, { 
pattern
 
=
 
'
TSUpdate
'
,

callback
 
=
 
function
()
 
require
(
'
nvim-treesitter.parsers
'
).
zimbu
 
=
 {
 
install_info
 
=
 {
 
url
 
=
 
'
https://github.com/zimbulang/tree-sitter-zimbu
'
,
 
revision
 
=
 
<sha>
, 
--
 commit hash for revision to check out; HEAD if missing

 
--
 optional entries:

 
branch
 
=
 
'
develop
'
, 
--
 only needed if different from default branch

 
location
 
=
 
'
parser
'
, 
--
 only needed if the parser is in subdirectory of a "monorepo"

 
generate
 
=
 
true
, 
--
 only needed if repo does not contain pre-generated `src/parser.c`

 
generate_from_json
 
=
 
false
, 
--
 only needed if repo does not contain `src/grammar.json` either

 
queries
 
=
 
'
queries/neovim
'
, 
--
 also install queries from given directory

 },
 }

end
})

Alternatively, if you have a local checkout, you can instead use

 
install_info
 
=
 {
 
path
 
=
 
'
~/parsers/tree-sitter-zimbu
'
,
 
--
 optional entries

 
location
 
=
 
'
parser
'
,
 
generate
 
=
 
true
,
 
generate_from_json
 
=
 
false
,
 
queries
 
=
 
'
queries/neovim
'
, 
--
 symlink queries from given directory

 },

This will always use the state of the directory as-is (i.e.,branchandrevisionwill be ignored).

1. If the parser name differs from the filetype(s) used by Neovim, you need to register the parser via

vim
.
treesitter
.
language
.
register
(
'
zimbu
'
, { 
'
zu
' 
})

If Neovim does not detect your language's filetype by default, you can useNeovim'svim.filetype.add()to add a custom detection rule.

1. Startnvimand:TSInstall zimbu.

Important

If the parser requires an external scanner, this must be written in C.

### Modifying parsers

You can use the same approach for overriding parser information. E.g., if you always want to generate theluaparser from grammar, add

vim
.
api
.
nvim_create_autocmd
(
'
User
'
, { 
pattern
 
=
 
'
TSUpdate
'
,

callback
 
=
 
function
()
 
require
(
'
nvim-treesitter.parsers
'
).
lua
.
install_info
.
generate
 
=
 
true

end
})

## Adding queries

Queries can be placed anywhere in yourruntimepathunderqueries/<language>, with earlier directories taking precedence unless the queries are marked with; extends; see:h treesitter-query-modelines.

## About

Nvim Treesitter configurations and abstraction layer

### Topics

 tree-sitter

 neovim

 nvim-treesitter

### Resources

 Readme

 

### License

 Apache-2.0 license
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

13.5k

 stars
 

### Watchers

57

 watching
 

### Forks

1.2k

 forks
 

 Report repository

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Tree-sitter Query74.6%
* Lua14.0%
* Cap'n Proto3.1%
* Python0.8%
* Shell0.7%
* Nix0.6%
* Other6.2%