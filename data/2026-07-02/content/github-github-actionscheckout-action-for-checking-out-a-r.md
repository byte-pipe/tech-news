---
title: 'GitHub - actions/checkout: Action for checking out a repo · GitHub'
url: https://github.com/actions/checkout
site_name: github
content_file: github-github-actionscheckout-action-for-checking-out-a-r
fetched_at: '2026-07-02T11:50:31.623225'
original_url: https://github.com/actions/checkout
author: actions
description: Action for checking out a repo. Contribute to actions/checkout development by creating an account on GitHub.
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 actions

 

/

checkout

Public

* NotificationsYou must be signed in to change notification settings
* Fork2.5k
* Star8.1k

 
 
 
Use this GitHub action with your project
Add this Action to an existing workflow or create a new one
View on Marketplace
 
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

228 Commits
228 Commits
.github
.github
 
 
.licenses/
npm
.licenses/
npm
 
 
__test__
__test__
 
 
adrs
adrs
 
 
dist
dist
 
 
images
images
 
 
src
src
 
 
.eslintignore
.eslintignore
 
 
.eslintrc.json
.eslintrc.json
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.licensed.yml
.licensed.yml
 
 
.prettierignore
.prettierignore
 
 
.prettierrc.json
.prettierrc.json
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CODEOWNERS
CODEOWNERS
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
action.yml
action.yml
 
 
jest.config.ts
jest.config.ts
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
tsconfig.json
tsconfig.json
 
 
View all files

## Repository files navigation

# Checkout v7

## What's new

* Safer fork pull request handling: checkout now refuses to check out fork pull request code by default when the workflow is triggered bypull_request_targetorworkflow_run. These triggers run with the base repository'sGITHUB_TOKEN, secrets, and runner access, where executing a fork's code commonly leads to "pwn request" vulnerabilities.To opt in afterreviewing the risks, set the newallow-unsafe-pr-checkout: trueinput.
* To opt in afterreviewing the risks, set the newallow-unsafe-pr-checkout: trueinput.
* Migratedactions/checkoutto ESM to support new versions of the@actions/*packages.
* Updated direct and transitive dependencies, including security fixes for known vulnerabilities.

# Checkout v6

## What's new

* Improved credential security:persist-credentialsnow stores credentials in a separate file under$RUNNER_TEMPinstead of directly in.git/config
* No workflow changes required —git fetch,git push, etc. continue to work automatically
* Running authenticated git commands from aDocker container actionrequires Actions Runnerv2.329.0or later

# Checkout v5

## What's new

* Updated to the node24 runtimeThis requires a minimum Actions Runner version ofv2.327.1to run.
* This requires a minimum Actions Runner version ofv2.327.1to run.

# Checkout v4

This action checks-out your repository under$GITHUB_WORKSPACE, so your workflow can access it.

Only a single commit is fetched by default, for the ref/SHA that triggered the workflow. Setfetch-depth: 0to fetch all history for all branches and tags. Referhereto learn which commit$GITHUB_SHApoints to for different events.

The auth token is persisted in the local git config. This enables your scripts to run authenticated git commands. The token is removed during post-job cleanup. Setpersist-credentials: falseto opt-out.

When Git 2.18 or higher is not in your PATH, falls back to the REST API to download the files.

### Note

Thank you for your interest in this GitHub action, however, right now we are not taking contributions.

We continue to focus our resources on strategic areas that help our customers be successful while making developers' lives easier. While GitHub Actions remains a key part of this vision, we are allocating resources towards other areas of Actions and are not taking contributions to this repository at this time. The GitHub public roadmap is the best place to follow along for any updates on features we’re working on and what stage they’re in.

We are taking the following steps to better direct requests related to GitHub Actions, including:

1. We will be directing questions and support requests to ourCommunity Discussions area
2. High Priority bugs can be reported through Community Discussions or you can report these to our support teamhttps://support.github.com/contact/bug-report.
3. Security Issues should be handled as per oursecurity.md

We will still provide security updates for this project and fix major breaking changes during this time.

You are welcome to still raise bugs in this repo.

# What's new

Please refer to therelease pagefor the latest release notes.

# Usage

- 
uses
: 
actions/checkout@v7

 
with
:
 
#
 Repository name with owner. For example, actions/checkout

 
#
 Default: ${{ github.repository }}

 
repository
: 
'
'

 
#
 The branch, tag or SHA to checkout. When checking out the repository that

 
#
 triggered a workflow, this defaults to the reference or SHA for that event.

 
#
 Otherwise, uses the default branch.

 
ref
: 
'
'

 
#
 Personal access token (PAT) used to fetch the repository. The PAT is configured

 
#
 with the local git config, which enables your scripts to run authenticated git

 
#
 commands. The post-job step removes the PAT.

 
#

 
#
 We recommend using a service account with the least permissions necessary. Also

 
#
 when generating a new PAT, select the least scopes necessary.

 
#

 
#
 [Learn more about creating and using encrypted secrets](https://help.github.com/en/actions/automating-your-workflow-with-github-actions/creating-and-using-encrypted-secrets)

 
#

 
#
 Default: ${{ github.token }}

 
token
: 
'
'

 
#
 SSH key used to fetch the repository. The SSH key is configured with the local

 
#
 git config, which enables your scripts to run authenticated git commands. The

 
#
 post-job step removes the SSH key.

 
#

 
#
 We recommend using a service account with the least permissions necessary.

 
#

 
#
 [Learn more about creating and using encrypted secrets](https://help.github.com/en/actions/automating-your-workflow-with-github-actions/creating-and-using-encrypted-secrets)

 
ssh-key
: 
'
'

 
#
 Known hosts in addition to the user and global host key database. The public SSH

 
#
 keys for a host may be obtained using the utility `ssh-keyscan`. For example,

 
#
 `ssh-keyscan github.com`. The public key for github.com is always implicitly

 
#
 added.

 
ssh-known-hosts
: 
'
'

 
#
 Whether to perform strict host key checking. When true, adds the options

 
#
 `StrictHostKeyChecking=yes` and `CheckHostIP=no` to the SSH command line. Use

 
#
 the input `ssh-known-hosts` to configure additional hosts.

 
#
 Default: true

 
ssh-strict
: 
'
'

 
#
 The user to use when connecting to the remote SSH host. By default 'git' is

 
#
 used.

 
#
 Default: git

 
ssh-user
: 
'
'

 
#
 Whether to configure the token or SSH key with the local git config

 
#
 Default: true

 
persist-credentials
: 
'
'

 
#
 Relative path under $GITHUB_WORKSPACE to place the repository

 
path
: 
'
'

 
#
 Whether to execute `git clean -ffdx && git reset --hard HEAD` before fetching

 
#
 Default: true

 
clean
: 
'
'

 
#
 Partially clone against a given filter. Overrides sparse-checkout if set.

 
#
 Default: null

 
filter
: 
'
'

 
#
 Do a sparse checkout on given patterns. Each pattern should be separated with

 
#
 new lines.

 
#
 Default: null

 
sparse-checkout
: 
'
'

 
#
 Specifies whether to use cone-mode when doing a sparse checkout.

 
#
 Default: true

 
sparse-checkout-cone-mode
: 
'
'

 
#
 Number of commits to fetch. 0 indicates all history for all branches and tags.

 
#
 Default: 1

 
fetch-depth
: 
'
'

 
#
 Whether to fetch tags, even if fetch-depth > 0.

 
#
 Default: false

 
fetch-tags
: 
'
'

 
#
 Whether to show progress status output when fetching.

 
#
 Default: true

 
show-progress
: 
'
'

 
#
 Whether to download Git-LFS files

 
#
 Default: false

 
lfs
: 
'
'

 
#
 Whether to checkout submodules: `true` to checkout submodules or `recursive` to

 
#
 recursively checkout submodules.

 
#

 
#
 When the `ssh-key` input is not provided, SSH URLs beginning with

 
#
 `git@github.com:` are converted to HTTPS.

 
#

 
#
 Default: false

 
submodules
: 
'
'

 
#
 Add repository path as safe.directory for Git global config by running `git

 
#
 config --global --add safe.directory <path>`

 
#
 Default: true

 
set-safe-directory
: 
'
'

 
#
 The base URL for the GitHub instance that you are trying to clone from, will use

 
#
 environment defaults to fetch from the same instance that the workflow is

 
#
 running from unless specified. Example URLs are https://github.com or

 
#
 https://my-ghes-server.example.com

 
github-server-url
: 
'
'

 
#
 Required to check out fork pull request code from a workflow triggered by

 
#
 `pull_request_target` or `workflow_run`. These workflows run with the base

 
#
 repository's GITHUB_TOKEN, secrets, default-branch cache scope, and runner

 
#
 access; fetching and executing a fork's code in that trusted context commonly

 
#
 leads to "pwn request" vulnerabilities. Set to `true` only after reviewing the

 
#
 risks at https://gh.io/securely-using-pull_request_target.

 
#
 Default: false

 
allow-unsafe-pr-checkout
: 
'
'

# Scenarios

* Checkout V5What's new
* What's new
* Checkout V4Note
* Note
* What's new
* Usage
* ScenariosFetch only the root filesFetch only the root files and.githubandsrcfolderFetch only a single fileFetch all history for all tags and branchesCheckout a different branchCheckout HEAD^Checkout multiple repos (side by side)Checkout multiple repos (nested)Checkout multiple repos (private)Checkout pull request HEAD commit instead of merge commitCheckout pull request on closed eventPush a commit using the built-in tokenPush a commit to a PR using the built-in token
* Fetch only the root files
* Fetch only the root files and.githubandsrcfolder
* Fetch only a single file
* Fetch all history for all tags and branches
* Checkout a different branch
* Checkout HEAD^
* Checkout multiple repos (side by side)
* Checkout multiple repos (nested)
* Checkout multiple repos (private)
* Checkout pull request HEAD commit instead of merge commit
* Checkout pull request on closed event
* Push a commit using the built-in token
* Push a commit to a PR using the built-in token
* Recommended permissions
* License

## Fetch only the root files

- 
uses
: 
actions/checkout@v7

 
with
:
 
sparse-checkout
: 
.

## Fetch only the root files and.githubandsrcfolder

- 
uses
: 
actions/checkout@v7

 
with
:
 
sparse-checkout
: 
|

 .github

 src

## Fetch only a single file

- 
uses
: 
actions/checkout@v7

 
with
:
 
sparse-checkout
: 
|

 README.md

 
sparse-checkout-cone-mode
: 
false

## Fetch all history for all tags and branches

- 
uses
: 
actions/checkout@v7

 
with
:
 
fetch-depth
: 
0

## Checkout a different branch

- 
uses
: 
actions/checkout@v7

 
with
:
 
ref
: 
my-branch

## Checkout HEAD^

- 
uses
: 
actions/checkout@v7

 
with
:
 
fetch-depth
: 
2

- 
run
: 
git checkout HEAD^

## Checkout multiple repos (side by side)

- 
name
: 
Checkout

 
uses
: 
actions/checkout@v7

 
with
:
 
path
: 
main

- 
name
: 
Checkout tools repo

 
uses
: 
actions/checkout@v7

 
with
:
 
repository
: 
my-org/my-tools

 
path
: 
my-tools

* If your secondary repository is private or internal you will need to add the option noted inCheckout multiple repos (private)

## Checkout multiple repos (nested)

- 
name
: 
Checkout

 
uses
: 
actions/checkout@v7

- 
name
: 
Checkout tools repo

 
uses
: 
actions/checkout@v7

 
with
:
 
repository
: 
my-org/my-tools

 
path
: 
my-tools

* If your secondary repository is private or internal you will need to add the option noted inCheckout multiple repos (private)

## Checkout multiple repos (private)

- 
name
: 
Checkout

 
uses
: 
actions/checkout@v7

 
with
:
 
path
: 
main

- 
name
: 
Checkout private tools

 
uses
: 
actions/checkout@v7

 
with
:
 
repository
: 
my-org/my-private-tools

 
token
: 
${{ secrets.GH_PAT }} 
#
 `GH_PAT` is a secret that contains your PAT

 
path
: 
my-tools

* ${{ github.token }}is scoped to the current repository, so if you want to checkout a different repository that is private you will need to provide your ownPAT.

## Checkout pull request HEAD commit instead of merge commit

- 
uses
: 
actions/checkout@v7

 
with
:
 
ref
: 
${{ github.event.pull_request.head.sha }}

## Checkout pull request on closed event

on
:
 
pull_request
:
 
branches
: 
[main]

 
types
: 
[opened, synchronize, closed]

jobs
:
 
build
:
 
runs-on
: 
ubuntu-latest

 
steps
:
 - 
uses
: 
actions/checkout@v7

## Push a commit using the built-in token

on
: 
push

jobs
:
 
build
:
 
runs-on
: 
ubuntu-latest

 
steps
:
 - 
uses
: 
actions/checkout@v7

 - 
run
: 
|

 date > generated.txt

 # Note: the following account information will not work on GHES

 git config user.name "github-actions[bot]"

 git config user.email "41898282+github-actions[bot]@users.noreply.github.com"

 git add .

 git commit -m "generated"

 git push

NOTE:The user email is{user.id}+{user.login}@users.noreply.github.com. See users API:https://api.github.com/users/github-actions%5Bbot%5D

## Push a commit to a PR using the built-in token

In a pull request trigger,refis required as GitHub Actions checks out in detached HEAD mode, meaning it doesn’t check out your branch by default.

on
: 
pull_request

jobs
:
 
build
:
 
runs-on
: 
ubuntu-latest

 
steps
:
 - 
uses
: 
actions/checkout@v7

 
with
:
 
ref
: 
${{ github.head_ref }}

 - 
run
: 
|

 date > generated.txt

 # Note: the following account information will not work on GHES

 git config user.name "github-actions[bot]"

 git config user.email "41898282+github-actions[bot]@users.noreply.github.com"

 git add .

 git commit -m "generated"

 git push

NOTE:The user email is{user.id}+{user.login}@users.noreply.github.com. See users API:https://api.github.com/users/github-actions%5Bbot%5D

# Recommended permissions

When using thecheckoutaction in your GitHub Actions workflow, it is recommended to set the followingGITHUB_TOKENpermissions to ensure proper functionality, unless alternative auth is provided via thetokenorssh-keyinputs:

permissions
:
 
contents
: 
read

# License

The scripts and documentation in this project are released under theMIT License

## About

Action for checking out a repo

github.com/features/actions

### Resources

 Readme

 

### License

 MIT license
 

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

8.1k

 stars
 

### Watchers

172

 watching
 

### Forks

2.5k

 forks
 

 Report repository

 

## Releases52

v7.0.0

 Latest

 

Jun 18, 2026

 

+ 51 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Used by15.3m

 + 15,279,774
 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript95.1%
* Shell4.6%
* Other0.3%