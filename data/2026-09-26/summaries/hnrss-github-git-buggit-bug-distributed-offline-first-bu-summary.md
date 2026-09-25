---
title: GitHub - git-bug/git-bug: Distributed, offline-first bug tracker integrated in git · GitHub
url: https://github.com/git-bug/git-bug
date: 2026-09-25
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-09-26T05:57:15.846167
---

# GitHub - git-bug/git-bug: Distributed, offline-first bug tracker integrated in git · GitHub

# git-bug Overview

## Key Features
- Fully integrated in git; no extra files added to the project.  
- Distributed: bugs are stored in the git repository and can be pushed/pulled like code.  
- Offline‑first: create, read and edit bugs without network access.  
- Fast operations (listing, opening) run in milliseconds.  
- Multiple user interfaces: CLI, interactive terminal UI, web UI, and GraphQL API.  
- Bridges to other trackers (GitHub, GitLab, Jira, Launchpad) for import/export.  

## Installation
- Detailed steps are in **INSTALLATION.md**, including building from source and verification of the binary.

## Workflows
- **Native workflow** – use `git bug push` and `git bug pull` to synchronize bugs via normal git remotes.  
- **Bridge workflow** – configure a bridge (`git bug bridge new`) and sync bugs with external trackers using `git bug bridge pull/push`. Works offline.  
- **Web UI workflow (WIP)** – planned public portal with OAuth authentication; contributions are welcome.

## CLI Usage
- Create identity: `git bug user create`  
- Add bug: `git bug add` (opens editor for title and description)  
- Push/pull: `git bug push [remote]`, `git bug pull [remote]`  
- List bugs: `git bug ls` (supports query filters, e.g., `status:open sort:edit`)  
- Search by text: `git bug ls "foo bar"`  
- Additional commands: `show`, `comment`, `open`, `close`, etc. (`git bug <command> --help` for details)

## Interactive Terminal UI
- Launch with `git bug termui` to browse and edit bugs in a curses‑based interface.

## Web UI
- Start with `git bug webui`; a local HTTP server serves a rich interface for browsing, searching, commenting, and editing bugs.  
- Includes a code browser (file tree, syntax highlighting, commit history, diffs).  
- Communicates with the backend via a GraphQL API (schema available in the repository).

## Bridges
- Supported targets: GitHub, GitLab, Jira, Launchpad.  
- Configure a bridge: `git bug bridge new --name=<bridge> --target=github --url=<url> --login=<login> --token=<token>`  
- Import bugs: `git bug bridge pull <name>`  
- Export modifications: `git bug bridge push <name>`  
- Remove a bridge: `git bug bridge rm <name>`

## Internals
- Data model and on‑disk format are defined in the git‑bug specification (DAG entity format, identities, bug entity).  
- Documentation provides details for implementing other tools or custom data structures on top of git.

## Miscellaneous
- Shell completions for Bash, Zsh, Fish, PowerShell.  
- Man pages are provided.

## Planned Features
- Public web UI portal for external contributions.  
- Additional items (e.g., “inflatable raptor”) listed in the feature matrix.

## Contribute
- Pull requests are welcome.  
- Join the Matrix room for chat, consult the feature matrix, and browse issues/discussions.  
- Development setup instructions are in **CONTRIBUTING.md**; separate README for the web UI.

## License
- Project is released under GPLv3 or later.  
- Logo by Viktor Teplov, licensed under CC BY 4.0.