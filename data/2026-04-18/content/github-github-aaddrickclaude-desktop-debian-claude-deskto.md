---
title: 'GitHub - aaddrick/claude-desktop-debian: Claude Desktop for Debian-based Linux distributions · GitHub'
url: https://github.com/aaddrick/claude-desktop-debian
site_name: github
content_file: github-github-aaddrickclaude-desktop-debian-claude-deskto
fetched_at: '2026-04-18T11:33:50.415092'
original_url: https://github.com/aaddrick/claude-desktop-debian
author: aaddrick
description: Claude Desktop for Debian-based Linux distributions - aaddrick/claude-desktop-debian
---

aaddrick

 

/

claude-desktop-debian

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork378
* Star3.4k

 
 
 
 
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

556 Commits
556 Commits
.claude
.claude
 
 
.github
.github
 
 
docs
docs
 
 
nix
nix
 
 
scripts
scripts
 
 
tests
tests
 
 
.codespellrc
.codespellrc
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
LICENSE-APACHE
LICENSE-APACHE
 
 
LICENSE-MIT
LICENSE-MIT
 
 
README.md
README.md
 
 
STYLEGUIDE.md
STYLEGUIDE.md
 
 
build.sh
build.sh
 
 
flake.lock
flake.lock
 
 
flake.nix
flake.nix
 
 
View all files

## Repository files navigation

# Claude Desktop for Linux

This project provides build scripts to run Claude Desktop natively on Linux systems. It repackages the official Windows application for Linux distributions, producing.debpackages (Debian/Ubuntu),.rpmpackages (Fedora/RHEL), distribution-agnostic AppImages, anAUR packagefor Arch Linux, and a Nix flake for NixOS.

Note:This is an unofficial build script. For official support, please visitAnthropic's website. For issues with the build script or Linux implementation, pleaseopen an issuein this repository.

⚠️EXPERIMENTAL: Cowork Mode SupportCowork mode isenabled by defaultin this build with a pluggable isolation backend:

Backend

Isolation

Requirements

bubblewrap
 (default)

Namespace sandbox

bwrap
 installed and functional

host
 (fallback)

None — runs directly on host

No additional requirements

The best available backend is auto-detected at startup. Runclaude-desktop --doctorto check which backend will be used and which dependencies are missing.

Note:The bubblewrap backend mounts your home directory as read-only (only the project working directory is writable). The host backend provides no isolation — use it only if you understand the security implications.

KVM status:The KVM/QEMU backend code exists but is non-functional — VM file downloads are disabled on Linux to prevent a checksum loop (#337). The backend code remains for potential future use.

## Features

* Native Linux Support: Run Claude Desktop without virtualization or Wine
* MCP Support: Full Model Context Protocol integration
Configuration file location:~/.config/Claude/claude_desktop_config.json
* System Integration:Global hotkey support (Ctrl+Alt+Space) - works on X11 and Wayland (via XWayland)System tray integrationDesktop environment integration
* Global hotkey support (Ctrl+Alt+Space) - works on X11 and Wayland (via XWayland)
* System tray integration
* Desktop environment integration

### Screenshots

## Installation

### Using APT Repository (Debian/Ubuntu - Recommended)

Add the repository for automatic updates viaapt:

#
 Add the GPG key

curl -fsSL https://aaddrick.github.io/claude-desktop-debian/KEY.gpg 
|
 sudo gpg --dearmor -o /usr/share/keyrings/claude-desktop.gpg

#
 Add the repository

echo
 
"
deb [signed-by=/usr/share/keyrings/claude-desktop.gpg arch=amd64,arm64] https://aaddrick.github.io/claude-desktop-debian stable main
"
 
|
 sudo tee /etc/apt/sources.list.d/claude-desktop.list

#
 Update and install

sudo apt update
sudo apt install claude-desktop

Future updates will be installed automatically with your regular system updates (sudo apt upgrade).

### Using DNF Repository (Fedora/RHEL - Recommended)

Add the repository for automatic updates viadnf:

#
 Add the repository

sudo curl -fsSL https://aaddrick.github.io/claude-desktop-debian/rpm/claude-desktop.repo -o /etc/yum.repos.d/claude-desktop.repo

#
 Install

sudo dnf install claude-desktop

Future updates will be installed automatically with your regular system updates (sudo dnf upgrade).

### Using AUR (Arch Linux)

Theclaude-desktop-appimagepackage is available on the AUR and is automatically updated with each release.

#
 Using yay

yay -S claude-desktop-appimage

#
 Or using paru

paru -S claude-desktop-appimage

The AUR package installs the AppImage build of Claude Desktop.

### Using Nix Flake (NixOS)

Install directly from the flake:

#
 Basic install

nix profile install github:aaddrick/claude-desktop-debian

#
 With MCP server support (FHS environment)

nix profile install github:aaddrick/claude-desktop-debian#claude-desktop-fhs

Or add to your NixOS configuration:

# flake.nix

{

 
inputs
.
claude-desktop
.
url
 
=
 
"github:aaddrick/claude-desktop-debian"
;

 
outputs
 
=
 
{
 
nixpkgs
,
 
claude-desktop
,
 ... 
}
: 
{

 
nixosConfigurations
.
myhost
 
=
 
nixpkgs
.
lib
.
nixosSystem
 
{

 
modules
 
=
 
[

 
(
{
 
pkgs
,
 ... 
}
: 
{

 
nixpkgs
.
overlays
 
=
 
[
 
claude-desktop
.
overlays
.
default
 
]
;

 
environment
.
systemPackages
 
=
 
[
 
pkgs
.
claude-desktop
 
]
;

 
}
)

 
]
;

 
}
;

 
}
;

}

### Using Pre-built Releases

Download the latest.deb,.rpm, or.AppImagefrom theReleases page.

### Building from Source

Seedocs/BUILDING.mdfor detailed build instructions.

## Configuration

Model Context Protocol settings are stored in:

~/.config/Claude/claude_desktop_config.json

For additional configuration options including environment variables and Wayland support, seedocs/CONFIGURATION.md.

## Troubleshooting

Runclaude-desktop --doctorfor built-in diagnostics that check common issues (display server, sandbox permissions, MCP config, stale locks, and more). It also reports cowork mode readiness — which isolation backend will be used, and which dependencies (KVM, QEMU, vsock, socat, virtiofsd, bubblewrap) are installed or missing.

For additional troubleshooting, uninstallation instructions, and log locations, seedocs/TROUBLESHOOTING.md.

## Acknowledgments

This project was inspired byk3d3's claude-desktop-linux-flakeand theirReddit postabout running Claude Desktop natively on Linux.

Special thanks to:

* k3d3Original NixOS implementationNative bindings insights
* Original NixOS implementation
* Native bindings insights
* emsiTitle bar fixAlternative implementation approach
* Title bar fix
* Alternative implementation approach
* leobuskinfor the Playwright-based URL resolution approach
* yarikopticCodespell supportShellcheck compliance
* Codespell support
* Shellcheck compliance
* IamGianlucafor build dependency check improvements
* ing03201for IBus/Fcitx5 input method support
* ajescuderofor pinning @electron/asar for Node compatibility
* delorenjfor Wayland compatibility support
* Regen-forestfor suggesting Gear Lever as AppImageLauncher replacement
* niekvugteveenfor fixing Debian packaging permissions
* speleoalexfor native window decorations support
* imaginalnikafor moving logs to~/.cache/
* richardspicerfor the menu bar visibility fix on Linux
* jacobfrantz1Claude Desktop code preview supportQuick window submit fix
* Claude Desktop code preview support
* Quick window submit fix
* janfrederikfor the--exeflag to use a local installer
* MrEdwards007for discovering the OAuth token cache fix
* lizthegreyfor version update contributions
* mathys-lopintoAUR packageAutomated deployment
* AUR package
* Automated deployment
* pkuijpersfor root cause analysis of the RPM repo GPG signing issue
* dlepoldfor identifying the tray icon variable name bug with a working fix
* Voork1144Detailed analysis of the tray icon minifier bugRoot-cause analysis of the Chromium layout cache bugDirect childsetBounds()fix approach
* Detailed analysis of the tray icon minifier bug
* Root-cause analysis of the Chromium layout cache bug
* Direct childsetBounds()fix approach
* sabiut--doctordiagnostic commandSHA-256 checksum validation for downloadsPost-build integration tests for deb, rpm, and AppImage artifacts
* --doctordiagnostic command
* SHA-256 checksum validation for downloads
* Post-build integration tests for deb, rpm, and AppImage artifacts
* milog1994Popup detectionFunctional stubsWayland compositor support
* Popup detection
* Functional stubs
* Wayland compositor support
* jarrodcolburnPasswordless sudo support in container/CI environmentsIdentifying the gh-pages 4GB bloat fixIdentifying the virtiofsd PATH detection issue on DebianDetailed analysis of the CI release pipeline failure caused by runner kills during compare-releasesDiagnosing the session-start hook sudo blocking issue with three solution approaches
* Passwordless sudo support in container/CI environments
* Identifying the gh-pages 4GB bloat fix
* Identifying the virtiofsd PATH detection issue on Debian
* Detailed analysis of the CI release pipeline failure caused by runner kills during compare-releases
* Diagnosing the session-start hook sudo blocking issue with three solution approaches
* chukfinleyfor experimental Cowork mode support on Linux
* CyPackfor orphaned cowork daemon cleanup on startup
* IliyaBrookfor fixing the platform patch for Claude Desktop >= 1.1.3541 arm64 refactor
* MichaelMKennyDiagnosing the$-prefixed electron variable bugRoot cause analysis and workaround
* Diagnosing the$-prefixed electron variable bug
* Root cause analysis and workaround
* daa25209for detailed root cause analysis of the cowork platform gate crash and patch script
* noctuumCLAUDE_MENU_BARenv var with configurable menu bar visibilityBoolean alias support
* CLAUDE_MENU_BARenv var with configurable menu bar visibility
* Boolean alias support
* typedratNixOS flake integration with build.shnode-pty derivationCI auto-updateFixing the flake package scoping regression
* NixOS flake integration with build.sh
* node-pty derivation
* CI auto-update
* Fixing the flake package scoping regression
* cbonnissentReverse-engineering the Cowork VM guest RPC protocolFixing the KVM startup blockerFixing RPC response id echoing for persistent connectionsConfigurable bwrap mount points via a dedicated Linux config file
* Reverse-engineering the Cowork VM guest RPC protocol
* Fixing the KVM startup blocker
* Fixing RPC response id echoing for persistent connections
* Configurable bwrap mount points via a dedicated Linux config file
* joekale-ppfor adding--doctorsupport to the RPM launcher
* ecrevisseMiroirfor the bwrap backend sandbox isolation with tmpfs-based minimal root
* arauhalafor detailed root cause analysis of the NixOSisPackagedregression
* cromagnonefor confirming the VM download loop on bwrap installs with detailed logs that disproved the initial triage
* aHk-coderfor diagnosing the hardcoded minified variable crash in the cowork smol-bin patch
* RayCharlizardDetailed analysis of the self-referential.mcpb-cachesymlink ELOOP bugFixing auto-memory path translation on HostBackend
* Detailed analysis of the self-referential.mcpb-cachesymlink ELOOP bug
* Fixing auto-memory path translation on HostBackend
* reinthalfor fixing the NixOS build breakage caused by the nixpkgsnodePackagesremoval
* gianluca-periReporting the GNOME quit accessibility issueConfirming tray behavior with AppIndicator
* Reporting the GNOME quit accessibility issue
* Confirming tray behavior with AppIndicator

## Sponsorship

Anthropic doesn't publish release notes for Claude Desktop. Each release here includes AI-generated notes that analyze code changes between versions. I wrote up how that process works if you're curious:Generating Real Release Notes from Minified Electron Apps.

The analysis runs against Claude's API. Costs vary a lot depending on how big the update is. Recent releases have run between$3.36 and $76.16 per release.

If this project is useful to you, considersponsoring on GitHubto help cover those costs.

## License

The build scripts in this repository are dual-licensed under:

* MIT License (seeLICENSE-MIT)
* Apache License 2.0 (seeLICENSE-APACHE)

The Claude Desktop application itself is subject toAnthropic's Consumer Terms.

## Contributing

Contributions are welcome! By submitting a contribution, you agree to license it under the same dual-license terms as this project.

## About

Claude Desktop for Debian-based Linux distributions

### Resources

 Readme

 

### License

 Apache-2.0, Unknown licenses found
 

### Licenses found

Apache-2.0

LICENSE-APACHE

 

Unknown

LICENSE-MIT

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

3.4k

 stars
 

### Watchers

51

 watching
 

### Forks

378

 forks
 

 Report repository

 

## Releases84

v1.3.32+claude1.3109.0

 Latest

 

Apr 17, 2026

 

+ 83 releases

## Sponsor this project

 

 

 Sponsor

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

Learn more about GitHub Sponsors

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Shell76.3%
* JavaScript20.0%
* Nix2.3%
* Python1.4%