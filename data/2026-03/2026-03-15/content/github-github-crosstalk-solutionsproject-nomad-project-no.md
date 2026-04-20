---
title: 'GitHub - Crosstalk-Solutions/project-nomad: Project N.O.M.A.D, is a self-contained, offline survival computer packed with critical tools, knowledge, and AI to keep you informed and empowered—anytime, anywhere. · GitHub'
url: https://github.com/Crosstalk-Solutions/project-nomad
site_name: github
content_file: github-github-crosstalk-solutionsproject-nomad-project-no
fetched_at: '2026-03-15T11:10:18.013401'
original_url: https://github.com/Crosstalk-Solutions/project-nomad
author: Crosstalk-Solutions
description: Project N.O.M.A.D, is a self-contained, offline survival computer packed with critical tools, knowledge, and AI to keep you informed and empowered—anytime, anywhere. - Crosstalk-Solutions/project-nomad
---

Crosstalk-Solutions



/

project-nomad

Public

* NotificationsYou must be signed in to change notification settings
* Fork84
* Star663




 
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

345 Commits
345 Commits
.github
.github
 
 
admin
admin
 
 
collections
collections
 
 
install
install
 
 
.dockerignore
.dockerignore
 
 
.gitignore
.gitignore
 
 
.releaserc.json
.releaserc.json
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
View all files

## Repository files navigation

# Project N.O.M.A.D.

### Node for Offline Media, Archives, and Data

Knowledge That Never Goes Offline

Project N.O.M.A.D. is a self-contained, offline-first knowledge and education server packed with critical tools, knowledge, and AI to keep you informed and empowered—anytime, anywhere.

## Installation & Quickstart

Project N.O.M.A.D. can be installed on any Debian-based operating system (we recommend Ubuntu). Installation is completely terminal-based, and all tools and resources are designed to be accessed through the browser, so there's no need for a desktop environment if you'd rather setup N.O.M.A.D. as a "server" and access it through other clients.

Note: sudo/root privileges are required to run the install script

#### Quick Install

sudo apt-get update
&&
 sudo apt-get install -y curl
&&
 curl -fsSL https://raw.githubusercontent.com/Crosstalk-Solutions/project-nomad/refs/heads/main/install/install_nomad.sh -o install_nomad.sh
&&
 sudo bash install_nomad.sh

Project N.O.M.A.D. is now installed on your device! Open a browser and navigate tohttp://localhost:8080(orhttp://DEVICE_IP:8080) to start exploring!

## How It Works

N.O.M.A.D. is a management UI ("Command Center") and API that orchestrates a collection of containerized tools and resources viaDocker. It handles installation, configuration, and updates for everything — so you don't have to.

Built-in capabilities include:

* AI Chat with Knowledge Base— local AI chat powered byOllama, with document upload and semantic search (RAG viaQdrant)
* Information Library— offline Wikipedia, medical references, ebooks, and more viaKiwix
* Education Platform— Khan Academy courses with progress tracking viaKolibri
* Offline Maps— downloadable regional maps viaProtoMaps
* Data Tools— encryption, encoding, and analysis viaCyberChef
* Notes— local note-taking viaFlatNotes
* System Benchmark— hardware scoring with acommunity leaderboard
* Easy Setup Wizard— guided first-time configuration with curated content collections

N.O.M.A.D. also includes built-in tools like a Wikipedia content selector, ZIM library manager, and content explorer.

## What's Included

Capability

Powered By

What You Get

Information Library

Kiwix

Offline Wikipedia, medical references, survival guides, ebooks

AI Assistant

Ollama + Qdrant

Built-in chat with document upload and semantic search

Education Platform

Kolibri

Khan Academy courses, progress tracking, multi-user support

Offline Maps

ProtoMaps

Downloadable regional maps with search and navigation

Data Tools

CyberChef

Encryption, encoding, hashing, and data analysis

Notes

FlatNotes

Local note-taking with markdown support

System Benchmark

Built-in

Hardware scoring, Builder Tags, and community leaderboard

## Device Requirements

While many similar offline survival computers are designed to be run on bare-minimum, lightweight hardware, Project N.O.M.A.D. is quite the opposite. To install and run the
available AI tools, we highly encourage the use of a beefy, GPU-backed device to make the most of your install.

At it's core, however, N.O.M.A.D. is still very lightweight. For a barebones installation of the management application itself, the following minimal specs are required:

Note: Project N.O.M.A.D. is not sponsored by any hardware manufacturer and is designed to be as hardware-agnostic as possible. The harware listed below is for example/comparison use only

#### Minimum Specs

* Processor: 2 GHz dual-core processor or better
* RAM: 4GB system memory
* Storage: At least 5 GB free disk space
* OS: Debian-based (Ubuntu recommended)
* Stable internet connection (required during install only)

To run LLM's and other included AI tools:

#### Optimal Specs

* Processor: AMD Ryzen 7 or Intel Core i7 or better
* RAM: 32 GB system memory
* Graphics: NVIDIA RTX 3060 or AMD equivalent or better (more VRAM = run larger models)
* Storage: At least 250 GB free disk space (preferably on SSD)
* OS: Debian-based (Ubuntu recommended)
* Stable internet connection (required during install only)

For detailed build recommendations at three price points ($200–$800+), see theHardware Guide.

Again, Project N.O.M.A.D. itself is quite lightweight - it's the tools and resources you choose to install with N.O.M.A.D. that will determine the specs required for your unique deployment

## About Internet Usage & Privacy

Project N.O.M.A.D. is designed for offline usage. An internet connection is only required during the initial installation (to download dependencies) and if you (the user) decide to download additional tools and resources at a later time. Otherwise, N.O.M.A.D. does not require an internet connection and has ZERO built-in telemetry.

To test internet connectivity, N.O.M.A.D. attempts to make a request to Cloudflare's utility endpoint,https://1.1.1.1/cdn-cgi/traceand checks for a successful response.

## About Security

By design, Project N.O.M.A.D. is intended to be open and available without hurdles - it includes no authentication. If you decide to connect your device to a local network after install (e.g. for allowing other devices to access it's resources), you can block/open ports to control which services are exposed.

Will authentication be added in the future?Maybe. It's not currently a priority, but if there's enough demand for it, we may consider building in an optional authentication layer in a future release to support uses cases where multiple users need access to the same instance but with different permission levels (e.g. family use with parental controls, classroom use with teacher/admin accounts, etc.). For now, we recommend using network-level controls to manage access if you're planning to expose your N.O.M.A.D. instance to other devices on a local network. N.O.M.A.D. is not designed to be exposed directly to the internet, and we strongly advise against doing so unless you really know what you're doing, have taken appropriate security measures, and understand the risks involved.

## Contributing

Contributions are welcome and appreciated! Please read this section fully to understand how to contribute to the project.

### General Guidelines

* Open an issue first: Before starting work on a new feature or bug fix, please open an issue to discuss your proposed changes. This helps ensure that your contribution aligns with the project's goals and avoids duplicate work. Title the issue clearly and provide a detailed description of the problem or feature you want to work on.
* Fork the repository: Click the "Fork" button at the top right of the repository page to create a copy of the project under your GitHub account.
* Create a new branch: In your forked repository, create a new branch for your work. Use a descriptive name for the branch that reflects the purpose of your changes (e.g.,fix/issue-123orfeature/add-new-tool).
* Make your changes: Implement your changes in the new branch. Follow the existing code style and conventions used in the project. Be sure to test your changes locally to ensure they work as expected.
* Add Release Notes: If your changes include new features, bug fixes, or improvements, please see the "Release Notes" section below to properly document your contribution for the next release.
* Conventional Commits: When committing your changes, please use conventional commit messages to provide clear and consistent commit history. The format is<type>(<scope>): <description>, where:typeis the type of change (e.g.,featfor new features,fixfor bug fixes,docsfor documentation changes, etc.)scopeis an optional area of the codebase that your change affects (e.g.,api,ui,docs, etc.)descriptionis a brief summary of the change
* typeis the type of change (e.g.,featfor new features,fixfor bug fixes,docsfor documentation changes, etc.)
* scopeis an optional area of the codebase that your change affects (e.g.,api,ui,docs, etc.)
* descriptionis a brief summary of the change
* Submit a pull request: Once your changes are ready, submit a pull request to the main repository. Provide a clear description of your changes and reference any related issues. The project maintainers will review your pull request and may provide feedback or request changes before it can be merged.
* Be responsive to feedback: If the maintainers request changes or provide feedback on your pull request, please respond in a timely manner. Stale pull requests may be closed if there is no activity for an extended period.
* Follow the project's code of conduct: Please adhere to the project's code of conduct when interacting with maintainers and other contributors. Be respectful and considerate in your communications.
* No guarantee of acceptance: The project is community-driven, and all contributions are appreciated, but acceptance is not guaranteed. The maintainers will evaluate each contribution based on its quality, relevance, and alignment with the project's goals.
* Thank you for contributing to Project N.O.M.A.D.!Your efforts help make this project better for everyone.

### Versioning

This project uses semantic versioning. The version is managed in the rootpackage.jsonand automatically updated by semantic-release. For simplicity's sake, the "project-nomad" image
uses the same version defined there instead of the version inadmin/package.json(stays at 0.0.0), as it's the only published image derived from the code.

### Release Notes

Human-readable release notes live inadmin/docs/release-notes.mdand are displayed in the Command Center's built-in documentation.

When working on changes, add a summary to the## Unreleasedsection at the top of that file under the appropriate heading:

* Features— new user-facing capabilities
* Bug Fixes— corrections to existing behavior
* Improvements— enhancements, refactors, docs, or dependency updates

Use the format- **Area**: Descriptionto stay consistent with existing entries. When a release is triggered, CI automatically stamps the version and date, commits the update, and pushes the content to the GitHub release.

## Community & Resources

* Website:www.projectnomad.us- Learn more about the project
* Discord:Join the Community- Get help, share your builds, and connect with other NOMAD users
* Benchmark Leaderboard:benchmark.projectnomad.us- See how your hardware stacks up against other NOMAD builds

## License

Project N.O.M.A.D. is licensed under theApache License 2.0.

## Helper Scripts

Once installed, Project N.O.M.A.D. has a few helper scripts should you ever need to troubleshoot issues or perform maintenance that can't be done through the Command Center. All of these scripts are found in Project N.O.M.A.D.'s install directory,/opt/project-nomad

###### Start Script - Starts all installed project containers

sudo bash /opt/project-nomad/start_nomad.sh

###### Stop Script - Stops all installed project containers

sudo bash /opt/project-nomad/stop_nomad.sh

###### Update Script - Attempts to pull the latest images for the Command Center and its dependencies (i.e. mysql) and recreate the containers. Note: thisonlyupdates the Command Center containers. It does not update the installable application containers - that should be done through the Command Center UI

sudo bash /opt/project-nomad/update_nomad.sh

###### Uninstall Script - Need to start fresh? Use the uninstall script to make your life easy. Note: this cannot be undone!

curl -fsSL https://raw.githubusercontent.com/Crosstalk-Solutions/project-nomad/refs/heads/main/install/uninstall_nomad.sh -o uninstall_nomad.sh
&&
 sudo bash uninstall_nomad.sh

## About

Project N.O.M.A.D, is a self-contained, offline survival computer packed with critical tools, knowledge, and AI to keep you informed and empowered—anytime, anywhere.

### Resources

 Readme



### License

 Apache-2.0 license


### Code of conduct

 Code of conduct


### Contributing

 Contributing


### Uh oh!

There was an error while loading.Please reload this page.





Activity


Custom properties


### Stars

663

 stars


### Watchers

14

 watching


### Forks

84

 forks


 Report repository



## Releases47

v1.29.1

 Latest



Mar 13, 2026



+ 46 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.





### Uh oh!

There was an error while loading.Please reload this page.





## Contributors

### Uh oh!

There was an error while loading.Please reload this page.





## Languages

* TypeScript91.5%
* Shell7.8%
* Other0.7%
