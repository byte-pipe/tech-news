---
title: 'GitHub - reconurge/flowsint: A modern platform for visual, flexible, and extensible graph-based investigations. For cybersecurity analysts and investigators. · GitHub'
url: https://github.com/reconurge/flowsint
site_name: github
content_file: github-github-reconurgeflowsint-a-modern-platform-for-vis
fetched_at: '2026-06-03T01:51:22.230932'
original_url: https://github.com/reconurge/flowsint
author: reconurge
description: A modern platform for visual, flexible, and extensible graph-based investigations. For cybersecurity analysts and investigators. - reconurge/flowsint
---

reconurge

 

/

flowsint

Public

* NotificationsYou must be signed in to change notification settings
* Fork572
* Star4.3k

 
 
 
 
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

806 Commits
806 Commits
.claude/
skills/
flowsint-enricher-builder
.claude/
skills/
flowsint-enricher-builder
 
 
.github/
workflows
.github/
workflows
 
 
.husky
.husky
 
 
docs
docs
 
 
flowsint-api
flowsint-api
 
 
flowsint-app
flowsint-app
 
 
flowsint-core
flowsint-core
 
 
flowsint-enrichers
flowsint-enrichers
 
 
flowsint-types
flowsint-types
 
 
neo4j-migrations
neo4j-migrations
 
 
scripts
scripts
 
 
.dockerignore
.dockerignore
 
 
.env.example
.env.example
 
 
.gitignore
.gitignore
 
 
.python-version
.python-version
 
 
.versionrc.json
.versionrc.json
 
 
CHANGELOG.md
CHANGELOG.md
 
 
DISCLAIMER.md
DISCLAIMER.md
 
 
ETHICS.md
ETHICS.md
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
NOTICE
NOTICE
 
 
README.md
README.md
 
 
commitlint.config.js
commitlint.config.js
 
 
docker-compose.dev.yml
docker-compose.dev.yml
 
 
docker-compose.prod.yml
docker-compose.prod.yml
 
 
docker-compose.yml
docker-compose.yml
 
 
package.json
package.json
 
 
pyproject.toml
pyproject.toml
 
 
uv.lock
uv.lock
 
 
yarn.lock
yarn.lock
 
 
View all files

## Repository files navigation

# Flowsint

Flowsint is an open-source OSINT graph exploration tool designed for ethical investigation, transparency, and verification.

Ethics:Please readETHICS.mdfor responsible use guidelines.

demo1.mp4

video2.mp4

demo3.mp4

## Contributing

Flowsint is still in early development and definetly needs the help of the community! Feel free to raise issues, propose features, etc.

## Get started

Don't want to read ? Got it. Here's your install instructions:

#### 1. Install pre-requisites

* Docker
* Make

#### 2. Run install command

git clone https://github.com/reconurge/flowsint.git

cd
 flowsint
make prod

Then go tohttp://localhost:5173/registerand create an account. There are no credentials or account by default.

✅ OSINT investigations need a high level of privacy. Everything is stored on your machine.

## What is it?

Flowsint is a graph-based investigation tool focused on reconnaissance and OSINT (Open Source Intelligence). It allows you to explore relationships between entities through a visual graph interface and automated enrichers.

### Available Enrichers

Domain Enrichers

* Reverse DNS Resolution - Find domains pointing to an IP
* DNS Resolution - Resolve domain to IP addresses
* Subdomain Discovery - Enumerate subdomains
* WHOIS Lookup - Get domain registration information
* Domain to Website - Convert domain to website entity
* Domain to Root Domain - Extract root domain
* Domain to ASN - Find ASN associated with domain
* Domain History - Retrieve historical domain data

IP Enrichers

* IP Information - Get geolocation and network details
* IP to ASN - Find ASN for IP address

ASN Enrichers

* ASN to CIDRs - Get IP ranges for an ASN

CIDR Enrichers

* CIDR to IPs - Enumerate IPs in a range

Social Media Enrichers

* Maigret - Username search across social platforms

Organization Enrichers

* Organization to ASN - Find ASNs owned by organization
* Organization Information - Get company details
* Organization to Domains - Find domains owned by organization

Cryptocurrency Enrichers

* Wallet to Transactions - Get transaction history
* Wallet to NFTs - Find NFTs owned by wallet

Website Enrichers

* Website Crawler - Crawl and map website structure
* Website to Links - Extract all links
* Website to Domain - Extract domain from URL
* Website to Webtrackers - Identify tracking scripts
* Website to Text - Extract text content

Email Enrichers

* Email to Gravatar - Find Gravatar profile
* Email to Breaches - Check data breach databases
* Email to Domains - Find associated domains

Phone Enrichers

* Phone to Breaches - Check phone number in breaches

Individual Enrichers

* Individual to Organization - Find organizational affiliations
* Individual to Domains - Find domains associated with person

Integration Enrichers

* N8n Connector - Connect to N8n workflows

## Project structure

The project is organized into autonomous modules:

### Core modules

* flowsint-core: Core utilities, orchestrator, vault, celery tasks, and base classes
* flowsint-types: Pydantic models and type definitions
* flowsint-enrichers: Enricher modules, scanning logic, and tools
* flowsint-api: FastAPI server, API routes, and schemas only
* flowsint-app: Frontend application

### Module dependencies

flowsint-app (frontend)
 ↓
flowsint-api (API server)
 ↓
flowsint-core (orchestrator, tasks, vault)
 ↓
flowsint-enrichers (enrichers & tools)
 ↓
flowsint-types (types)

## Development setup

### Prerequisites

* Docker

### Run

Make sure you haveMakeinstalled.

make dev

### Development

The app is accessible athttp://localhost:5173.

## Module details

### flowsint-core

Core utilities and base classes used by all other modules:

* Database connections (PostgreSQL, Neo4j)
* Authentication and authorization
* Logging and event handling
* Configuration management
* Base classes for enrichers and tools
* Utility functions

### flowsint-types

Pydantic models for all data types:

* Domain, IP, ASN, CIDR
* Individual, Organization, Email, Phone
* Website, Social profiles, Credentials
* Crypto wallets, Transactions, NFTs
* And many more...

### flowsint-enrichers

Enricher modules that process data:

* Domain enrichers (subdomains, WHOIS, resolution)
* IP enrichers (geolocation, ASN lookup)
* Social media enrichers (Maigret, Sherlock)
* Email enrichers (breaches, Gravatar)
* Crypto enrichers (transactions, NFTs)
* And many more...

### flowsint-api

FastAPI server providing:

* REST API endpoints
* Authentication and user management
* Graph database integration
* Real-time event streaming

### flowsint-app

Frontend application.

* Modern and UI friendly interface
* Built for performance (no lag even on thousands of nodes)

## Development workflow

1. Adding new types: Add toflowsint-typesmodule
2. Adding new enrichers: Add toflowsint-enrichersmodule
3. Adding new API endpoints: Add toflowsint-apimodule
4. Adding new utilities: Add toflowsint-coremodule

## Testing

Each module has its own (incomplete) test suite:

#
 Test core module

cd
 flowsint-core
uv run pytest

#
 Test types module

cd
 ../flowsint-types
uv run pytest

#
 Test enrichers module

cd
 ../flowsint-enrichers
uv run pytest

#
 Test API module

cd
 ../flowsint-api
uv run pytest

## Contributing

1. Follow the modular structure
2. Use Poetry for dependency management
3. Write tests for new functionality
4. Update documentation as needed

## ⚖️ Legal & Ethical Use

Ethics:Please readETHICS.mdfor responsible use guidelines.

Flowsint is designedstrictly for lawful, ethical investigation and research purposes.

It was created to assist:

* Cybersecurity researchers and analysts
* Journalists and OSINT investigators
* Law enforcement or fraud investigation teams
* Organizations conducting internal threat intelligence or digital risk analysis

Flowsint must not be used for:

* Unauthorized intrusion, surveillance, or data collection
* Harassment, doxxing, or targeting of individuals
* Political manipulation, misinformation, or violation of privacy laws

Any misuse of this software is strictly prohibited and goes against the ethical principles defined inETHICS.md.

## ❤️ Support

## About

A modern platform for visual, flexible, and extensible graph-based investigations. For cybersecurity analysts and investigators.

flowsint.io

### Topics

 python

 osint

 recon

 investigation

### Resources

 Readme

 

### License

 Apache-2.0 license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

4.3k

 stars
 

### Watchers

36

 watching
 

### Forks

572

 forks
 

 Report repository

 

## Releases12

v1.2.9

 Latest

 

May 31, 2026

 

+ 11 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript53.2%
* Python44.6%
* CSS1.2%
* JavaScript0.5%
* Makefile0.2%
* Cypher0.2%
* Other0.1%