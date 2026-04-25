---
title: 'GitHub - Universal-Commerce-Protocol/ucp: Specification and documentation for the Universal Commerce Protocol (UCP) · GitHub'
url: https://github.com/Universal-Commerce-Protocol/ucp
site_name: github
content_file: github-github-universal-commerce-protocolucp-specificatio
fetched_at: '2026-04-25T11:37:21.467239'
original_url: https://github.com/Universal-Commerce-Protocol/ucp
author: Universal-Commerce-Protocol
description: Specification and documentation for the Universal Commerce Protocol (UCP) - Universal-Commerce-Protocol/ucp
---

Universal-Commerce-Protocol

 

/

ucp

Public

* NotificationsYou must be signed in to change notification settings
* Fork339
* Star2.7k

 
 
 
 
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

147 Commits
147 Commits
.cspell
.cspell
 
 
.github
.github
 
 
docs
docs
 
 
scripts
scripts
 
 
source
source
 
 
.cspell.json
.cspell.json
 
 
.gitignore
.gitignore
 
 
.linkignore
.linkignore
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
.prettierignore
.prettierignore
 
 
.prettierrc
.prettierrc
 
 
.stylelintrc.json
.stylelintrc.json
 
 
LICENSE
LICENSE
 
 
MAINTAINERS.md
MAINTAINERS.md
 
 
README.md
README.md
 
 
biome.json
biome.json
 
 
hooks.py
hooks.py
 
 
main.py
main.py
 
 
mkdocs.yml
mkdocs.yml
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
pyproject.toml
pyproject.toml
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

# Universal Commerce Protocol (UCP)

An open standard enabling interoperability between various commerce
 entities to facilitate seamless commerce integrations.

Documentation|Specification|Discussions

## Overview

The Universal Commerce Protocol (UCP) addresses a fragmented commerce landscape
by providing a standardized common language and functional primitives. It
enables platforms (like AI agents and apps), businesses, Payment Service
Providers (PSPs), and Credential Providers (CPs) to communicate effectively,
ensuring secure and consistent commerce experiences across the web.

With UCP, businesses can:

* Declaresupported capabilities to enable autonomous discovery by
platforms.
* Facilitatesecure checkout sessions, with or without human intervention.
* Offerpersonalized shopping experiences through standardized data
exchange.

## Why UCP?

As commerce becomes increasingly agentic and distributed, the ability for
different systems to interoperate without custom, one-off integrations is vital.
UCP aims to:

* Standardize Interaction:Provide a uniform way for platforms to interact
with businesses, regardless of the underlying backend.
* Modularize Commerce:Breakdown commerce into distinctCapabilities(e.g., Checkout, Order) andExtensions(e.g., Discounts,
Fulfillment), allowing for flexible implementation.
* Enable Agentic Commerce:Designed from the ground up to support AI
agents acting on behalf of users to discover products, fill carts, and
complete purchases securely.
* Enhance Security:Support for advanced security patterns like AP2
mandates and verifiable credentials.

### Key Features

* Composable Architecture:UCP definesCapabilities(such as
"Checkout" or "Identity Linking") that businesses implement to enable easy
integration. On top of that, specificExtensionscan be added to enhance
the consumer experience without bloating the capability definitions.
* Dynamic Discovery:Businesses declare their supported Capabilities in a
standardized profile, allowing platforms to autonomously discover and
configure themselves.
* Transport Agnostic:The protocol is designed to work across various
transports. Businesses can offer Capabilities via REST APIs, MCP (Model
Context Protocol), or A2A, depending on their infrastructure.
* Built on Standards:UCP leverages existing open standards for payments,
identity, and security wherever applicable, rather than reinventing the
wheel.
* Developer Friendly:A comprehensive set of SDKs and libraries
facilitates rapid development and integration.

## Key Capabilities

The initial release focuses on the essential primitives for transacting:

* Checkout:Facilitates checkout sessions including cart management and
tax calculation, supporting flows with or without human intervention.
* Identity Linking:Enables platforms to obtain authorization to perform
actions on a user's behalf via OAuth 2.0.
* Order:Webhook-based updates for order lifecycle events (shipped,
delivered, returned).
* Payment Token Exchange:Protocols for PSPs and Credential Providers to
securely exchange payment tokens and credentials.

## Getting Started

* 📚Explore the Documentation:Visitucp.devfor a
complete overview, the full protocol specification, tutorials, and guides.
* 🎬Review oursamplesfor
implementation examples.
* 🛠️Use ourSDKsto start building your own integrations.
* 📝Check conformancewith ourconformance tests.

## Contributing

We welcome community contributions to enhance and evolve UCP.

* Questions & Discussions:Join ourGitHub
Discussions.
* Issues & Feedback:Report issues or suggest improvements via GitHub
Issues.
* Contribution Guide:See ourCONTRIBUTING.mdfor details on how to contribute.

## What's Next

Take a look atour roadmap on ucp.dev.
Future enhancements include:

* New Verticals:Applications beyond Shopping (e.g., Travel, Services).
* Loyalty:Standardized management of loyalty programs and rewards.
* Personalization:Enhanced signals for personalized product discovery.

## About

UCP is an open-source project under theApache License 2.0and is
open to contributions from the community.

## About

Specification and documentation for the Universal Commerce Protocol (UCP)

ucp.dev

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

2.7k

 stars
 

### Watchers

73

 watching
 

### Forks

339

 forks
 

 Report repository

 

## Releases3

Release v2026-04-08

 Latest

 

Apr 9, 2026

 

+ 2 releases

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python95.1%
* Shell4.9%