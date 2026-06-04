---
title: 'GitHub - github/copilot-sdk: Multi-platform SDK for integrating GitHub Copilot Agent into apps and services · GitHub'
url: https://github.com/github/copilot-sdk
site_name: github
content_file: github-github-githubcopilot-sdk-multi-platform-sdk-for-in
fetched_at: '2026-06-04T12:02:16.192413'
original_url: https://github.com/github/copilot-sdk
author: github
description: Multi-platform SDK for integrating GitHub Copilot Agent into apps and services - github/copilot-sdk
---

github

 

/

copilot-sdk

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.2k
* Star8.8k

 
 
 
 
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

625 Commits
625 Commits
.devcontainer
.devcontainer
 
 
.githooks
.githooks
 
 
.github
.github
 
 
.vscode
.vscode
 
 
assets
assets
 
 
docs
docs
 
 
dotnet
dotnet
 
 
go
go
 
 
java
java
 
 
nodejs
nodejs
 
 
python
python
 
 
rust
rust
 
 
scripts
scripts
 
 
test
test
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
SUPPORT.md
SUPPORT.md
 
 
justfile
justfile
 
 
sdk-protocol-version.json
sdk-protocol-version.json
 
 
View all files

## Repository files navigation

# GitHub Copilot CLI SDKs

Agents for every app.

Embed Copilot's agentic workflows in your application with the GitHub Copilot SDK for Python, TypeScript, Go, .NET, Java, and Rust.

The GitHub Copilot SDK exposes the same engine behind Copilot CLI: a production-tested agent runtime you can invoke programmatically. No need to build your own orchestration—you define agent behavior, Copilot handles planning, tool invocation, file edits, and more.

## Available SDKs

SDK

Location

Cookbook

Installation

Node.js / TypeScript

nodejs/

Cookbook

npm install @github/copilot-sdk

Python

python/

Cookbook

pip install github-copilot-sdk

Go

go/

Cookbook

go get github.com/github/copilot-sdk/go

.NET

dotnet/

Cookbook

dotnet add package GitHub.Copilot.SDK

Rust

rust/

—

cargo add github-copilot-sdk

Java

java/

Cookbook

Maven coordinates
com.github:copilot-sdk-java
See instructions for 
Maven
 and 
Gradle

See the individual SDK READMEs for installation, usage examples, and API reference.

## Getting Started

For a complete walkthrough, see theGetting Started Guide.

Quick steps:

1. (Optional) Install the Copilot CLI

For Node.js, Python, and .NET SDKs, the Copilot CLI is bundled automatically and no separate installation is required.
For Go, Java, and Rust,install the CLI manuallyor ensurecopilotis available in your PATH. Go and Rust also expose application-level CLI bundling features.

1. Install your preferred SDKusing the commands above.
2. See the SDK READMEfor usage examples and API documentation.

## Architecture

All SDKs communicate with the Copilot CLI server via JSON-RPC:

Your Application
 ↓
 SDK Client
 ↓ JSON-RPC
 Copilot CLI (server mode)

The SDK manages the CLI process lifecycle automatically. You can also connect to an external CLI server—see theGetting Started Guidefor details on running the CLI in server mode.

## FAQ

### Do I need a GitHub Copilot subscription to use the SDK?

Yes, a GitHub Copilot subscription is required to use the GitHub Copilot SDK,unless you are using BYOK (Bring Your Own Key). With BYOK, you can use the SDK without GitHub authentication by configuring your own API keys from supported LLM providers. For standard usage (non-BYOK), refer to theGitHub Copilot pricing page, which includes a free tier with limited usage.

### How does billing work for SDK usage?

Billing for the GitHub Copilot SDK is based on the same model as the Copilot CLI, with each prompt being counted towards your premium request quota. For more information on premium requests, seeRequests in GitHub Copilot.

### Does it support BYOK (Bring Your Own Key)?

Yes, the GitHub Copilot SDK supports BYOK (Bring Your Own Key). You can configure the SDK to use your own API keys from supported LLM providers (e.g. OpenAI, Azure AI Foundry, Anthropic) to access models through those providers. See theBYOK documentationfor setup instructions and examples.

Note:BYOK uses key-based authentication only. Microsoft Entra ID (Azure AD), managed identities, and third-party identity providers are not supported.

### What authentication methods are supported?

The SDK supports multiple authentication methods:

* GitHub signed-in user- Uses stored OAuth credentials fromcopilotCLI login
* OAuth GitHub App- Pass user tokens from your GitHub OAuth app
* Environment variables-COPILOT_GITHUB_TOKEN,GH_TOKEN,GITHUB_TOKEN
* BYOK- Use your own API keys (no GitHub auth required)

See theAuthentication documentationfor details on each method.

### Do I need to install the Copilot CLI separately?

No — for Node.js, Python, and .NET SDKs, the Copilot CLI is bundled automatically as a dependency. You do not need to install it separately.

For Go, Java, and Rust SDKs, the CLI isnotbundled by default. Install the CLI manually or ensurecopilotis available in your PATH. Go and Rust also expose application-level CLI bundling features.

Advanced: You can override the CLI binary or connect to an external server. See the individual SDK README for language-specific options.

### What tools are enabled by default?

By default, the SDK exposes the Copilot CLI's first-party tools, similar to running the CLI with--allow-all. Tool execution is still governed by each SDK's permission handler, so applications can approve, deny, or customize tool calls. You can customize tool availability by configuring the SDK client options to enable and disable specific tools. Refer to the individual SDK documentation for details on tool configuration and to the Copilot CLI documentation for the list of available tools.

### Can I use custom agents, skills or tools?

Yes, the GitHub Copilot SDK allows you to define custom agents, skills, and tools. You can extend the functionality of the agents by implementing your own logic and integrating additional tools as needed. Refer to the SDK documentation of your preferred language for more details.

### Are there instructions or SDK guidance for Copilot to speed up development?

Yes, check out the custom instructions and SDK-specific guidance:

* Node.js / TypeScript
* Python
* .NET
* Go
* Rust(SDK guidance; custom instructions not yet published)
* Java

### What models are supported?

All models available via Copilot CLI are supported in the SDK. The SDK also exposes a method which will return the models available so they can be accessed at runtime.

### Is the SDK production-ready?

The GitHub Copilot SDK is generally available and follows semantic versioning. SeeCHANGELOG.mdfor release notes.

### How do I report issues or request features?

Please use theGitHub Issuespage to report bugs or request new features. We welcome your feedback to help improve the SDK.

## Quick Links

* Documentation– Full documentation index
* Getting Started– Tutorial to get up and running
* Setup Guides– Architecture, deployment, and scaling
* Authentication– GitHub OAuth, BYOK, and more
* Features– Hooks, custom agents, MCP, skills, and more
* Troubleshooting– Common issues and solutions
* Cookbook– Practical recipes for common tasks across all languages
* More Resources– Additional examples, tutorials, and community resources

## Unofficial, Community-maintained SDKs

⚠️Disclaimer: These are unofficial, community-driven SDKs and they are not supported by GitHub. Use at your own risk.

SDK

Location

Clojure

copilot-community-sdk/copilot-sdk-clojure

C++

0xeb/copilot-sdk-cpp

## Contributing

SeeCONTRIBUTING.mdfor contribution guidelines.

## License

MIT

## About

Multi-platform SDK for integrating GitHub Copilot Agent into apps and services

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

8.8k

 stars
 

### Watchers

83

 watching
 

### Forks

1.2k

 forks
 

 Report repository

 

## Releases67

GitHub Copilot SDK for Java 1.0.0

 Latest

 

Jun 2, 2026

 

+ 66 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Java27.5%
* Rust23.5%
* TypeScript17.3%
* C#11.4%
* Go10.5%
* Python9.5%
* Other0.3%