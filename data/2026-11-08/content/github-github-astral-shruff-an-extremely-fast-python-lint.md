---
title: 'GitHub - astral-sh/ruff: An extremely fast Python linter and code formatter, written in Rust. · GitHub'
url: https://github.com/astral-sh/ruff
site_name: github
content_file: github-github-astral-shruff-an-extremely-fast-python-lint
fetched_at: '2026-11-08T09:02:53.795069'
original_url: https://github.com/astral-sh/ruff
author: astral-sh
description: An extremely fast Python linter and code formatter, written in Rust. - astral-sh/ruff
---

main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

18,030 Commits
18,030 Commits

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
 
 
.config
.config
 
 
.devcontainer
.devcontainer
 
 
.github
.github
 
 
.vscode
.vscode
 
 
assets
assets
 
 
changelogs
changelogs
 
 
crates
crates
 
 
docs
docs
 
 
fuzz
fuzz
 
 
playground
playground
 
 
python
python
 
 
scripts
scripts
 
 
.editorconfig
.editorconfig
 
 
.git-blame-ignore-revs
.git-blame-ignore-revs
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.ignore
.ignore
 
 
.markdownlint.yaml
.markdownlint.yaml
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
AGENTS.md
AGENTS.md
 
 
BREAKING_CHANGES.md
BREAKING_CHANGES.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
_typos.toml
_typos.toml
 
 
clippy.toml
clippy.toml
 
 
dist-workspace.toml
dist-workspace.toml
 
 
hawk.toml
hawk.toml
 
 
mkdocs.template.yml
mkdocs.template.yml
 
 
mkdocs.yml
mkdocs.yml
 
 
pyproject.toml
pyproject.toml
 
 
ruff.schema.json
ruff.schema.json
 
 
rust-toolchain.toml
rust-toolchain.toml
 
 
rustfmt.toml
rustfmt.toml
 
 
ty.schema.json
ty.schema.json
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

# Ruff

Docs|Playground

An extremely fast Python linter and code formatter, written in Rust.

Linting the CPython codebase from scratch.

* ⚡️ 10-100x faster than existing linters (like Flake8) and formatters (like Black)
* 🐍 Installable viapip
* 🛠️pyproject.tomlsupport
* 🤝 Python 3.15 compatibility
* ⚖️ Drop-in parity withFlake8,isort, andBlack
* 📦 Built-in caching, to avoid re-analyzing unchanged files
* 🔧 Fix support, for automatic error correction (e.g., automatically remove unused imports)
* 📏 Over900 built-in rules, with native re-implementations
of popular Flake8 plugins, like flake8-bugbear
* ⌨️ First-partyeditor integrationsforVS Codeandmore
* 🌎 Monorepo-friendly, withhierarchical and cascading configuration

Ruff aims to be orders of magnitude faster than alternative tools while integrating more
functionality behind a single, common interface.

Ruff can be used to replaceFlake8(plus dozens of plugins),Black,isort,pydocstyle,pyupgrade,autoflake, and more, all while executing tens or hundreds of
times faster than any individual tool.

Ruff is actively developed and used in major open-source projects like:

* Apache Airflow
* Apache Superset
* FastAPI
* Hugging Face
* Pandas
* SciPy

Ruff is backed byAstral, the creators ofuvandty.

Read thelaunch
post, or the
originalproject
announcement.

## Testimonials

Sebastián Ramírez, creator
ofFastAPI:

Ruff is so fast that sometimes I add an intentional bug in the code just to confirm it's actually
running and checking the code.

Nick Schrock, founder ofElementl,
co-creator ofGraphQL:

Why is Ruff a gamechanger? Primarily because it is nearly 1000x faster. Literally. Not a typo. On
our largest module (dagster itself, 250k LOC) pylint takes about 2.5 minutes, parallelized across 4
cores on my M1. Running ruff against ourentirecodebase takes .4 seconds.

Bryan Van de Ven, co-creator
ofBokeh, original author
ofConda:

Ruff is ~150-200x faster than flake8 on my machine, scanning the whole repo takes ~0.2s instead of
~20s. This is an enormous quality of life improvement for local dev. It's fast enough that I added
it as an actual commit hook, which is terrific.

Timothy Crosley,
creator ofisort:

Just switched my first project to Ruff. Only one downside so far: it's so fast I couldn't believe
it was working till I intentionally introduced some errors.

Tim Abbott, lead developer ofZulip(alsohere):

This is just ridiculously fast...ruffis amazing.

## Table of Contents

For more, see thedocumentation.

1. Getting Started
2. Configuration
3. Rules
4. Contributing
5. Support
6. Acknowledgements
7. Show Your Support
8. License

## Getting Started

For more, see thedocumentation.

### Installation

Ruff is available asruffon PyPI.

Invoke Ruff directly withuvx:

uvx ruff@0.17.4 check 
#
 Lint all files in the current directory.

uvx ruff@0.17.4 format 
#
 Format all files in the current directory.

Or install Ruff withuv(recommended),pip, orpipx:

#
 With uv.

uv tool install ruff@latest 
#
 Install Ruff globally.

uv add --dev ruff 
#
 Or add Ruff to your project.

#
 With pip.

pip install ruff

#
 With pipx.

pipx install ruff

Starting with version0.5.0, Ruff can be installed with our standalone installers:

#
 On macOS and Linux.

curl -LsSf https://astral.sh/ruff/install.sh 
|
 sh

#
 On Windows.

powershell -c 
"
irm https://astral.sh/ruff/install.ps1 | iex
"

#
 For a specific version.

curl -LsSf https://astral.sh/ruff/0.17.4/install.sh 
|
 sh
powershell -c 
"
irm https://astral.sh/ruff/0.17.4/install.ps1 | iex
"

You can also install Ruff viaHomebrew,Conda,
and witha variety of other package managers.

### Usage

To run Ruff as a linter, try any of the following:

ruff check 
#
 Lint all files in the current directory (and any subdirectories).

ruff check path/to/code/ 
#
 Lint all files in `/path/to/code` (and any subdirectories).

ruff check path/to/code/
*
.py 
#
 Lint all `.py` files in `/path/to/code`.

ruff check path/to/code/to/file.py 
#
 Lint `file.py`.

ruff check @arguments.txt 
#
 Lint using an input file, treating its contents as newline-delimited command-line arguments.

Or, to run Ruff as a formatter:

ruff format 
#
 Format all files in the current directory (and any subdirectories).

ruff format path/to/code/ 
#
 Format all files in `/path/to/code` (and any subdirectories).

ruff format path/to/code/
*
.py 
#
 Format all `.py` files in `/path/to/code`.

ruff format path/to/code/to/file.py 
#
 Format `file.py`.

ruff format @arguments.txt 
#
 Format using an input file, treating its contents as newline-delimited command-line arguments.

Ruff can also be used as apre-commithook viaruff-pre-commit:

- 
repo
: 
https://github.com/astral-sh/ruff-pre-commit

 
#
 Ruff version.

 
rev
: 
v0.17.4

 
hooks
:
 
#
 Run the linter.

 - 
id
: 
ruff-check

 
args
: 
[ --fix ]

 
#
 Run the formatter.

 - 
id
: 
ruff-format

Ruff can also be used as aVS Code extensionor withvarious other editors.

Ruff can also be used as aGitHub Actionviaruff-action:

name
: 
Ruff

on
: 
[ push, pull_request ]

jobs
:
 
ruff
:
 
runs-on
: 
ubuntu-latest

 
steps
:
 - 
uses
: 
actions/checkout@v4

 - 
uses
: 
astral-sh/ruff-action@v3

### Configuration

Ruff can be configured through apyproject.toml,ruff.toml, or.ruff.tomlfile (see:Configuration, orSettingsfor a complete list of all configuration options).

For the complete list of enabled rules, seeDefault Rules.

If left unspecified, Ruff's default configuration is equivalent to the followingruff.tomlfile:

#
 Exclude a variety of commonly ignored directories.

exclude
 = [
 
"
.bzr
"
,
 
"
.direnv
"
,
 
"
.eggs
"
,
 
"
.git
"
,
 
"
.git-rewrite
"
,
 
"
.hg
"
,
 
"
.ipynb_checkpoints
"
,
 
"
.mypy_cache
"
,
 
"
.nox
"
,
 
"
.pants.d
"
,
 
"
.pyenv
"
,
 
"
.pytest_cache
"
,
 
"
.pytype
"
,
 
"
.ruff_cache
"
,
 
"
.svn
"
,
 
"
.tox
"
,
 
"
.venv
"
,
 
"
.vscode
"
,
 
"
__pypackages__
"
,
 
"
_build
"
,
 
"
buck-out
"
,
 
"
build
"
,
 
"
dist
"
,
 
"
node_modules
"
,
 
"
site-packages
"
,
 
"
venv
"
,
]

#
 Same as Black.

line-length
 = 
88

indent-width
 = 
4

#
 Assume Python 3.11

target-version
 = 
"
py311
"

[
lint
]

#
 select = [...] # See the Default Rules page for the full listing.

ignore
 = []

#
 Allow fix for all enabled rules (when `--fix`) is provided.

fixable
 = [
"
ALL
"
]

unfixable
 = []

#
 Allow unused variables when underscore-prefixed.

dummy-variable-rgx
 = 
"
^(_+|(_+[
\\
p{XID_Continue}]*[
\\
p{XID_Continue}--_]+?))$
"

[
format
]

#
 Like Black, use double quotes for strings.

quote-style
 = 
"
double
"

#
 Like Black, indent with spaces, rather than tabs.

indent-style
 = 
"
space
"

#
 Like Black, respect magic trailing commas.

skip-magic-trailing-comma
 = 
false

#
 Like Black, automatically detect the appropriate line ending.

line-ending
 = 
"
auto
"

Note that, in apyproject.toml, each section header should be prefixed withtool.ruff. For
example,[lint]should be replaced with[tool.ruff.lint].

Some configuration options can be provided via dedicated command-line arguments, such as those
related to rule enablement and disablement, file discovery, and logging level:

ruff check --select F401 --select F403 --quiet

The remaining configuration options can be provided through a catch-all--configargument:

ruff check --config 
"
lint.per-file-ignores = {'some_file.py' = ['F841']}
"

To opt in to the latest lint rules, formatter style changes, interface updates, and more, enablepreview modeby settingpreview = truein your configuration
file or passing--previewon the command line. Preview mode enables a collection of unstable
features that may change prior to stabilization.

Seeruff helpfor more on Ruff's top-level commands, orruff help checkandruff help formatfor more on the linting and formatting commands, respectively.

## Rules

Ruff supports over 900 lint rules, many of which are inspired by popular tools like Flake8,
isort, pyupgrade, and others. Regardless of the rule's origin, Ruff re-implements every rule in
Rust as a first-party feature.

By default, Ruff enables rules from theF,E,B,UP, andRUFcategories,
as well as many more, omitting any stylistic rules that overlap with the use of a formatter, likeruff formatorBlack.

If you're just getting started with Ruff,the default rule set is a great place to start: it
catches a wide variety of common errors (like unused imports) with zero configuration. SeeDefault Rulesfor the complete list.

Beyond the defaults, Ruff re-implements some of the most popular Flake8 plugins and related code
quality tools, including:

* autoflake
* eradicate
* flake8-2020
* flake8-annotations
* flake8-async
* flake8-bandit(#1646)
* flake8-blind-except
* flake8-boolean-trap
* flake8-bugbear
* flake8-builtins
* flake8-commas
* flake8-comprehensions
* flake8-copyright
* flake8-datetimez
* flake8-debugger
* flake8-django
* flake8-docstrings
* flake8-eradicate
* flake8-errmsg
* flake8-executable
* flake8-future-annotations
* flake8-gettext
* flake8-implicit-str-concat
* flake8-import-conventions
* flake8-logging
* flake8-logging-format
* flake8-no-pep420
* flake8-pie
* flake8-print
* flake8-pyi
* flake8-pytest-style
* flake8-quotes
* flake8-raise
* flake8-return
* flake8-self
* flake8-simplify
* flake8-slots
* flake8-super
* flake8-tidy-imports
* flake8-todos
* flake8-type-checking
* flake8-use-pathlib
* flynt(#2102)
* isort
* mccabe
* pandas-vet
* pep8-naming
* pydocstyle
* pygrep-hooks
* pylint-airflow
* pyupgrade
* tryceratops
* yesqa

For the complete list of supported rules, seeRules.

## Contributing

Contributions are welcome and highly appreciated. To get started, check out thecontributing guidelines.

You can also join us onDiscord.

## Support

Having trouble? Check out the existing issues onGitHub,
or feel free toopen a new one.

You can also ask for help onDiscord.

## Acknowledgements

Ruff's linter draws on both the APIs and implementation details of many other
tools in the Python ecosystem, especiallyFlake8,Pyflakes,pycodestyle,pydocstyle,pyupgrade, andisort.

In some cases, Ruff includes a "direct" Rust port of the corresponding tool.
We're grateful to the maintainers of these tools for their work, and for all
the value they've provided to the Python community.

Ruff's formatter is built on a fork of Rome'srome_formatter,
and again draws on both API and implementation details fromRome,Prettier, andBlack.

Ruff's import resolver is based on the import resolution algorithm fromPyright.

Ruff is also influenced by a number of tools outside the Python ecosystem, likeClippyandESLint.

Ruff is the beneficiary of a large number ofcontributors.

Ruff is released under the MIT license.

## Show Your Support

If you're using Ruff, consider adding the Ruff badge to your project'sREADME.md:

[
![
Ruff
]
(
https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
)]
(
https://github.com/astral-sh/ruff
)

...orREADME.rst:

.. 
image
:: 
https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json

 
:target:
 
https://github.com/astral-sh/ruff

 
:alt:
 
Ruff

...or, as HTML:

<
a
 
href
="
https://github.com/astral-sh/ruff
"
>
<
img
 
src
="
https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
" 
alt
="
Ruff
" 
style
="
max-width:100%;
"
>
</
a
>

## License

This repository is licensed under theMIT License