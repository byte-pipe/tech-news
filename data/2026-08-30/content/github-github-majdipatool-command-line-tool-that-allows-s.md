---
title: 'GitHub - majd/ipatool: Command-line tool that allows searching and downloading app packages (known as ipa files) for iOS, iPadOS, tvOS, and visionOS from the App Store. · GitHub'
url: https://github.com/majd/ipatool
site_name: github
content_file: github-github-majdipatool-command-line-tool-that-allows-s
fetched_at: '2026-08-30T15:11:54.062841'
original_url: https://github.com/majd/ipatool
author: majd
description: Command-line tool that allows searching and downloading app packages (known as ipa files) for iOS, iPadOS, tvOS, and visionOS from the App Store. - majd/ipatool
---

majd

 

/

ipatool

Public

* NotificationsYou must be signed in to change notification settings
* Fork871
* Star10.1k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

216 Commits
216 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
cmd
cmd
 
 
internal/
sap
internal/
sap
 
 
pkg
pkg
 
 
resources
resources
 
 
tools
tools
 
 
.gitignore
.gitignore
 
 
.golangci.yml
.golangci.yml
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
go.mod
go.mod
 
 
go.sum
go.sum
 
 
main.go
main.go
 
 
tools.go
tools.go
 
 
View all files

## Repository files navigation

# IPATool

ipatoolis a command line tool that allows you to search for iOS, iPadOS, tvOS, and visionOS apps on theApp Storeand download a copy of the app package, known as anipafile.

* Requirements
* InstallationManualPackage Manager (macOS)
* Manual
* Package Manager (macOS)
* Usage
* Compiling
* License
* Releases
* FAQ

## Requirements

* Supported operating system (Windows, Linux or macOS).
* Apple ID set up to use the App Store.

## Installation

### Manual

You can grab the latest version ofipatoolfromGitHub releases.

### Package Manager (macOS)

You can installipatoolusingHomebrew.

$ brew install ipatool

## Usage

To authenticate with the App Store, use theauthcommand.

Authenticate with the App Store

Usage:
 ipatool auth [command]

Available Commands:
 info Show current account info
 login Login to the App Store
 revoke Revoke your App Store credentials

Flags:
 -h, --help help for auth

Global Flags:
 --format format sets output format for command; can be 'text', 'json' (default text)
 --non-interactive run in non-interactive session
 --verbose enables verbose logs

Use "ipatool auth [command] --help" for more information about a command.

To search for apps on the App Store, use thesearchcommand.

Search for iOS, iPadOS, tvOS, and visionOS apps available on the App Store

Usage:
 ipatool search <term> [flags]

Flags:
 -h, --help help for search
 -l, --limit int maximum amount of search results to retrieve; visionOS supports up to 12 (default 5)
 --platform string Platform to search: iphone (iOS), ipad (iPadOS), appletv (tvOS), or visionos

Global Flags:
 --format format sets output format for command; can be 'text', 'json' (default text)
 --non-interactive run in non-interactive session
 --verbose enables verbose logs

To obtain a license for an app, use thepurchasecommand.

Obtain a license for the app from the App Store

Usage:
 ipatool purchase [flags]

Flags:
 -b, --bundle-identifier string Bundle identifier of the target iOS app (required)
 -h, --help help for purchase

Global Flags:
 --format format sets output format for command; can be 'text', 'json' (default text)
 --non-interactive run in non-interactive session
 --verbose enables verbose logs

To list apps owned by the authenticated account, use thelist-purchasescommand. Results are ordered by purchase date, newest first.

List apps owned by the authenticated App Store account

Usage:
 ipatool list-purchases [flags]

Flags:
 -h, --help help for list-purchases
 -l, --max-results int maximum number of apps to return per page (default 10)
 -p, --page int page of owned apps to return (default 1)

Global Flags:
 --format format sets output format for command; can be 'text', 'json' (default text)
 --keychain-passphrase string passphrase for unlocking keychain
 --non-interactive run in non-interactive session
 --verbose enables verbose logs

To obtain a list of availble app versions to download, use thelist-versionscommand.

List the available versions of an iOS app

Usage:
 ipatool list-versions [flags]

Flags:
 -i, --app-id int ID of the target iOS app (required)
 -b, --bundle-identifier string The bundle identifier of the target iOS app (overrides the app ID)
 -h, --help help for list-versions

Global Flags:
 --format format sets output format for command; can be 'text', 'json' (default text)
 --keychain-passphrase string passphrase for unlocking keychain
 --non-interactive run in non-interactive session
 --verbose enables verbose logs

To download a copy of the ipa file, use thedownloadcommand.

Download (encrypted) iOS, iPadOS, tvOS, and visionOS app packages from the App Store

Usage:
 ipatool download [flags]

Flags:
 -i, --app-id int ID of the target app (required)
 -b, --bundle-identifier string The bundle identifier of the target app (overrides the app ID)
 --external-version-id string External version identifier of the target app (defaults to latest version when not specified)
 -h, --help help for download
 -o, --output string The destination path of the downloaded app package
 --platform string Platform to download for: iphone (iOS), ipad (iPadOS), appletv (tvOS), or visionos
 --purchase Obtain a license for the app if needed

Global Flags:
 --format format sets output format for command; can be 'text', 'json' (default text)
 --keychain-passphrase string passphrase for unlocking keychain
 --non-interactive run in non-interactive session
 --verbose enables verbose logs

To resolve an external version identifier, returned by thelist-versionscommand, use theget-version-metadatacommand.

Retrieves the metadata for a specific version of an app

Usage:
 ipatool get-version-metadata [flags]

Flags:
 -i, --app-id int ID of the target iOS app (required)
 -b, --bundle-identifier string The bundle identifier of the target iOS app (overrides the app ID)
 --external-version-id string External version identifier of the target iOS app (required)
 -h, --help help for get-version-metadata

Global Flags:
 --format format sets output format for command; can be 'text', 'json' (default text)
 --keychain-passphrase string passphrase for unlocking keychain
 --non-interactive run in non-interactive session
 --verbose enables verbose logs

Note:the tool runs in interactive mode by default. Use the--non-interactiveflag
if running in an automated environment.

## Compiling

The tool can be compiled using the Go toolchain.

$ go build -o ipatool

Unit tests can be executed with the following commands.

$ go generate ./...
$ go 
test
 -v ./...

## License

IPATool is released under theMIT license.