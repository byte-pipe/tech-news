---
title: 'GitHub - bwya77/vscode-dark-islands: VSCode theme based off the easemate IDE and Jetbrains islands theme · GitHub'
url: https://github.com/bwya77/vscode-dark-islands
site_name: github
content_file: github-github-bwya77vscode-dark-islands-vscode-theme-base
fetched_at: '2026-05-05T11:59:31.124495'
original_url: https://github.com/bwya77/vscode-dark-islands
author: bwya77
description: VSCode theme based off the easemate IDE and Jetbrains islands theme - bwya77/vscode-dark-islands
---

bwya77

 

/

vscode-dark-islands

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork228
* Star7.6k

 
 
 
 
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

84 Commits
84 Commits
.github
.github
 
 
assets
assets
 
 
fonts
fonts
 
 
issues
issues
 
 
themes
themes
 
 
.gitignore
.gitignore
 
 
.islands_dark_first_run
.islands_dark_first_run
 
 
.islands_dark_first_run_antigravity
.islands_dark_first_run_antigravity
 
 
.vscodeignore
.vscodeignore
 
 
CHANGELOG.md
CHANGELOG.md
 
 
README.md
README.md
 
 
animations.css
animations.css
 
 
bootstrap.ps1
bootstrap.ps1
 
 
bootstrap.sh
bootstrap.sh
 
 
flake.lock
flake.lock
 
 
flake.nix
flake.nix
 
 
install-antigravity.bat
install-antigravity.bat
 
 
install-antigravity.ps1
install-antigravity.ps1
 
 
install.ps1
install.ps1
 
 
install.sh
install.sh
 
 
merge-settings.ps1
merge-settings.ps1
 
 
package.json
package.json
 
 
settings.json
settings.json
 
 
uninstall.ps1
uninstall.ps1
 
 
uninstall.sh
uninstall.sh
 
 
View all files

## Repository files navigation

# Islands Dark

A dark color theme for Visual Studio Code inspired by the easemate IDE. Features floating glass-like panels, rounded corners, smooth animations, and a deeply refined UI.

* easemate
* easemate Nav
* easemate effects

## Features

* Deep dark canvas (#131217) with floating panels
* Glass-effect borders with directional light simulation (brighter top/left, subtle bottom/right)
* Rounded corners on all panels, notifications, command palette, and sidebars
* Pill-shaped activity bar with glass selection indicators
* Breadcrumb bar and status bar that dim when not hovered
* Tab close buttons that fade in on hover
* Smooth transitions on sidebar selections, scrollbars, and status bar
* Pill-shaped scrollbar thumbs
* Color-matched icon glow effect (works best withSeti Foldericon theme)
* Warm syntax highlighting with comprehensive language support (JS/TS, Python, Go, Rust, HTML/CSS, JSON, YAML, Markdown)
* IBM Plex Mono in the editor, FiraCode Nerd Font Mono in the terminal

## Installation

This theme has two parts: acolor themeandCSS customizationsthat create the floating glass panel look.

### One-Liner Install (Recommended)

The fastest way to install:

#### macOS/Linux

curl -fsSL https://raw.githubusercontent.com/bwya77/vscode-dark-islands/main/bootstrap.sh 
|
 bash

#### Windows

irm https:
//
raw.githubusercontent.com
/
bwya77
/
vscode
-
dark
-
islands
/
main
/
bootstrap.ps1 
|
 iex

### Manual Clone Install

If you prefer to clone first:

#### macOS/Linux

git clone https://github.com/bwya77/vscode-dark-islands.git islands-dark

cd
 islands-dark
./install.sh

#### Windows

git clone https:
//
github.com
/
bwya77
/
vscode
-
dark
-
islands.git islands
-
dark
cd islands
-
dark
.\install.ps1

The scripts will automatically:

* ✅ Install the Islands Dark theme extension
* ✅ Install the Custom UI Style extension
* ✅ Install Bear Sans UI fonts
* ✅ Back up your existing settings and apply Islands Dark settings
* ✅ Enable Custom UI Style and reload VS Code

Note:IBM Plex Mono and FiraCode Nerd Font Mono must be installed separately (the script will remind you).

### Nix Flake Install

If you use Nix, you can run a pre-configured instance of VS Code (or VSCodium) with the theme, extensions, and fonts already bundled.

To run it directly without installing:

#
 Run VS Code

nix run github:bwya77/vscode-dark-islands#vscode

#
 Or run VSCodium

nix run github:bwya77/vscode-dark-islands#vscodium

To use it in your NixOS or Home Manager configuration, add it to your flake inputs:

{

 
inputs
.
islands-dark
.
url
 
=
 
"github:bwya77/vscode-dark-islands"
;

 
outputs
 
=
 
{
 
self
,
 
nixpkgs
,
 
islands-dark
,
 ... 
}
: 
{

 
# Then you can add and use it:

 
# islands-dark.packages.${pkgs.stdenv.hostPlatform.system}.vscode

 
# islands-dark.packages.${pkgs.stdenv.hostPlatform.system}.vscodium

 
}
;

}

Note:The Nix flake automatically includes theCustom UI Styleextension,Seti Foldericon theme, and all required fonts (Bear Sans UI,IBM Plex Mono, andFiraCode Nerd Font). It will also copy the recommendedsettings.jsonon the first run.

### Manual Installation

If you prefer to install manually, follow these steps:

#### Step 1: Install the theme

Clone this repo and copy the extension files:

git clone https://github.com/bwya77/vscode-dark-islands.git islands-dark

cd
 islands-dark
mkdir -p 
~
/.vscode/extensions/bwya77.islands-dark-1.0.0
cp package.json 
~
/.vscode/extensions/bwya77.islands-dark-1.0.0/
cp -r themes 
~
/.vscode/extensions/bwya77.islands-dark-1.0.0/

On Windows (PowerShell):

git clone https:
//
github.com
/
bwya77
/
vscode
-
dark
-
islands.git islands
-
dark
cd islands
-
dark

$ext
 
=
 
"
$
env:
USERPROFILE
\.vscode\extensions\bwya77.islands-dark-1.0.0
"

New-Item
 
-
ItemType Directory 
-
Path 
$ext
 
-
Force

Copy-Item
 package.json 
$ext
\

Copy-Item
 themes 
$ext
\themes 
-
Recurse

#### Step 2: Install the Custom UI Style extension

The floating panels, rounded corners, glass borders, and animations are powered by theCustom UI Styleextension.

1. OpenExtensionsin VS Code: (Cmd+Shift+X/Ctrl+Shift+X)
2. Search forCustom UI Style(bysubframe7536)
3. ClickInstall

#### Step 3: Install recommended icon theme

For the best experience with the color-matched icon glow effect, install theSeti Foldericon theme:

1. OpenExtensionsin VS Code (Cmd+Shift+X/Ctrl+Shift+X)
2. Search forSeti Folder(byl-igh-t)
3. ClickInstall
4. Set it as your icon theme:Command Palette>Preferences: File Icon Theme>Seti Folder

#### Step 5: Install fonts

This theme uses two fonts:

* IBM Plex Mono— used in the editor
* FiraCode Nerd Font Mono— used in the terminal
* Bear Sans UI— used in the sidebar, tabs, command center, and status bar (included infonts/folder)

To install Bear Sans UI:

1. Open thefonts/folder in this repo
2. Select all.otffiles and double-click to open in Font Book (macOS) or right-click > Install (Windows)

If you prefer different fonts, update theeditor.fontFamily,terminal.integrated.fontFamily, andfont-familyvalues in the settings.

#### Step 6: Apply the settings

Copy the contents ofsettings.jsonfrom this repo into your VS Code: settings:

1. OpenCommand Palette(Cmd+Shift+P/Ctrl+Shift+P)
2. Search forPreferences: Open User Settings (JSON)
3. Merge the contents of this repo'ssettings.jsoninto your settings file

Note:If you already have existing settings, merge carefully. The key settings areworkbench.colorTheme,custom-ui-style.stylesheet, and the font/indent preferences.

#### Step 7: Enable Custom UI Style

1. OpenCommand Palette(Cmd+Shift+P/Ctrl+Shift+P)
2. RunCustom UI Style: Enable
3. VS Code will reload

Note:You may see a "corrupt installation" warning after enabling. This is expected since Custom UI Style injects CSS into VS Code. Click the gear icon on the warning and selectDon't Show Again.

## What the CSS customizations do

Element

Effect

Canvas

Deep dark background (
--islands-bg-canvas
) behind all panels

Sidebar

Floating with rounded corners (
--islands-panel-radius
), glass borders, drop shadow

Editor

Floating with rounded corners (
--islands-panel-radius
), glass borders, browser-tab effect

Activity bar

Pill-shaped with glass inset shadows, circular selection indicator

Command center

Pill-shaped with glass effect

Bottom panel

Floating with rounded corners (
--islands-panel-radius
), glass borders

Right sidebar

Floating with rounded corners (
--islands-panel-radius
), glass borders

Notifications

Rounded corners (
--islands-widget-radius
), glass borders, deep drop shadow

Command palette

Rounded corners (
--islands-widget-radius
), glass borders, rounded list rows

Scrollbars

Pill-shaped thumbs with fade transition

Tabs

Browser-tab style (active tab open at bottom), close button fades in on hover

Breadcrumbs

Hidden until hover with smooth fade transition

Status bar

Dimmed text that brightens on hover

File icons

Color-matched glow via drop-shadow (best with Seti Folder icon theme)

## Customization

All key visual properties are controlled by CSS custom properties defined at the top of thecustom-ui-style.stylesheetinsettings.json. Edit the variables on.monaco-workbenchto quickly adjust the look:

".monaco-workbench"
: {
 
"--islands-panel-radius"
: 
"
24px
"
,
 
"--islands-widget-radius"
: 
"
14px
"
,
 
"--islands-input-radius"
: 
"
12px
"
,
 
"--islands-item-radius"
: 
"
6px
"
,
 
"--islands-panel-gap"
: 
"
8px
"
,
 
"--islands-panel-top"
: 
"
8px
"
,
 
"--islands-bg-canvas"
: 
"
#121216
"
,
 
"--islands-bg-surface"
: 
"
#181a1d
"
,
 
"background-color"
: 
"
var(--islands-bg-canvas) !important
"

}

### Colors

Variable

Default

Applies to

--islands-bg-canvas

#121216

Deep background behind all panels (workbench, title bar, status bar, activity bar)

--islands-bg-surface

#181a1d

Panel/surface background (chat input, editor widgets)

These two colors define the theme's depth. The canvas is the darker base layer visible between panels, while the surface is the slightly lighter color used for interactive elements. To override the theme's panel colors (sidebar, editor, terminal backgrounds), use VS Code'sworkbench.colorCustomizationsin your settings.

### Border Radius

Variable

Default

Applies to

--islands-panel-radius

24px

Sidebar, editor, terminal/bottom panel, auxiliary bar

--islands-widget-radius

14px

Notifications, chat input, command palette

--islands-input-radius

12px

Search bars, SCM commit input, buttons, hover tooltips

--islands-item-radius

6px

List rows, tabs, pane headers, terminal tabs

For example, to make everything sharper, set all values to8px. For a fully rounded look, try32px/20px/16px/8px. Pill-shaped elements (activity bar, scrollbar thumbs, command center, badges) are not affected by these variables.

### Panel Spacing

Variable

Default

Applies to

--islands-panel-gap

8px

Horizontal spacing between sidebar, editor, chat/auxiliary bar, terminal, and notifications

--islands-panel-top

8px

Top margin of panels (space below the title bar)

Increase to12pxor16pxfor a more spaced-out layout, or reduce to4pxfor a tighter look.

## Troubleshooting

### Changes aren't taking effect

Try disabling and re-enabling Custom UI Style:

1. Command Palette>Custom UI Style: Disable
2. Reload VS Code
3. Command Palette>Custom UI Style: Enable
4. Reload VS Code

### "Corrupt installation" warning

This is expected after enabling Custom UI Style. Dismiss it or selectDon't Show Again.

### Previously used "Custom CSS and JS Loader" extension

If you previously used theCustom CSS and JS Loaderextension (be5invis.vscode-custom-css), it may have injected CSS directly into VS Code'sworkbench.htmlthat persists even after disabling. If styles conflict, reinstall VS Code to get a cleanworkbench.html, then use onlyCustom UI Style.

## Uninstalling

Run the uninstall script to restore your VS Code to its previous state:

macOS/Linux:

#
 If you still have the repo cloned:

cd
 islands-dark
./uninstall.sh

#
 Or download and run directly:

curl -fsSL https://raw.githubusercontent.com/bwya77/vscode-dark-islands/main/uninstall.sh 
|
 bash

Windows (PowerShell):

#
 If you still have the repo cloned:

cd islands
-
dark
.\uninstall.ps1

#
 Or download and run directly:

irm https:
//
raw.githubusercontent.com
/
bwya77
/
vscode
-
dark
-
islands
/
main
/
uninstall.ps1 
|
 iex

The uninstall script will:

* Restore your previous settings from thesettings.json.pre-islands-darkbackup
* Remove the Islands Dark theme extension
* Unregister the extension from VS Code

After running the script, you'll need to:

1. OpenCommand Palette(Cmd+Shift+P/Ctrl+Shift+P) and runCustom UI Style: Disable
2. OpenCommand Paletteand searchPreferences: Color Themeto select a new theme
3. Reload VS Code

## Credits

Inspired by theJetBrains Islands DarkUI theme.

## License

MIT

## About

VSCode theme based off the easemate IDE and Jetbrains islands theme

### Topics

 jetbrains

 vscode

 visual-studio-code

 vscode-theme

 easemate

### Resources

 Readme

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

7.6k

 stars
 

### Watchers

12

 watching
 

### Forks

228

 forks
 

 Report repository

 

## Releases1

v0.0.2

 Latest

 

Feb 19, 2026

## Sponsor this project

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 
* buymeacoffee.com/bwya77

Learn more about GitHub Sponsors

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* PowerShell51.5%
* Shell22.8%
* Nix14.3%
* CSS10.6%
* Batchfile0.8%