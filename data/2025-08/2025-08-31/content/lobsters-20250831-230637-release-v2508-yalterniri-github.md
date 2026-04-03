---
title: Release v25.08 · YaLTeR/niri · GitHub
url: https://github.com/YaLTeR/niri/releases/tag/v25.08
site_name: lobsters
fetched_at: '2025-08-31T23:06:37.406428'
original_url: https://github.com/YaLTeR/niri/releases/tag/v25.08
date: '2025-08-31'
description: A scrollable-tiling Wayland compositor. Contribute to YaLTeR/niri development by creating an account on GitHub.
tags: linux, release, rust
---

YaLTeR



/

niri

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork402
* Star10.8k



# v25.08

Latest

Latest


Compare


Loading

github-actions

 released this



 30 Aug 13:38


 ·


 2 commits


 to main
 since this release


 v25.08


01be0e6

Niri is a scrollable-tiling Wayland compositor. Windows are arranged in columns on an infinite strip going to the right. Opening a new window never causes existing windows to resize.

A month ago, on July 31st, we hit 10,000 stars on GitHub! Thanks everyone for your support. 😄 Also, on August 10, niri turned two years old since theinitial commit.

With introductions out of the way, here are the improvements from the last release.

Note

Packagers:

* Niri still requires libdisplay-info 0.2 (not 0.3). When libdisplay-info-rsupdates its requirement, you will likely be able to bump it in niri with no other changes.
* Some tests now require surfaceless EGL to be available at test time. If this is problematic, you can ignore them withcargo test -- --skip=::egl.
* The wiki contents have moved fromwiki/todocs/wiki/.
* We have a newIntegrating niriwiki page with information on integrating niri into distributions, which you may find helpful.

## A logo

After many,manyideas and discussions (first on Matrix, thenon GitHub), and several cool design proposals, niri now has logo!

It's a candle! The logo comes in four versions: full-sized, simple full-sized, icon, and simple icon. The simple versions are single-color and suitable for smaller sizes.

full-sized

icon

normal

simple

The logo is intentionally recolorable, and you might've already seen several versions across our wiki, Matrix, and Discord. In fact, there'sa webpagethat lets you quickly adjust the color and download an SVG.

Big thanks to@ixxie,@bluelinden, and@HumpityDumpityDumberfor creating and iterating on this design.

## New wiki

Thanks to@chinatsu, we have a new interface to browse our wiki! Check it out:https://yalter.github.io/niri/

The main improvement over GitHub Wiki is the interactive full-text search.

The site usesMaterial for MkDocs, and we retained full compatibility with GitHub Wiki, meaning all existing links keep working. All wiki pages will continue to be deployed to both the new site and the GitHub Wiki.

The new site allows us to make various customizations. For example,@chinatsumade all of our "Since: version" annotations render as badges and link to the corresponding release notes.

Also, thanks everyone for several suggestions and test wikis in theGitHub discussion!

## xwayland-satellite integration

There are still plenty of apps, and notably games, that use X11 and thus require Xwayland to work. Setting this up has been a common stumbling block for new niri users, because unlike most other compositors,we don't integrate Xwayland.

This niri release solves that problem by integratingxwayland-satellite. Make sure xwayland-satellite >= 0.7 is installed, remove any manual$DISPLAYconfiguration you may have had, and Xwayland will just work. If your xwayland-satellite binary is in a non-standard location, you can configure it witha new option.

For all intents and purposes, this integration works the same way as Xwayland integration in other compositors. Niri will create X11 sockets on disk, export$DISPLAY, and spawn xwayland-satellite on-demand when an X11 client connects. If xwayland-satellite dies, niri will automatically restart it.

This integration also removes the startup race condition, meaning you can put X11 apps intospawn-at-startupand systemd autostart.

We're using xwayland-satellite rather than Xwayland directly becausethose same reasonsfor avoiding Xwayland still apply. xwayland-satellite takes on the bulk of the work of dealing with the X11 peculiarities, giving niri normal Wayland windows to manage.

As a reminder, xwayland-satellite can perfectly run Steam, games, Proton, JetBrains IDEs, Ghidra, Electron apps, and most other X11 clients. But, applications that try to position windows and bars at specific screen coordinates will likely break andneed a nested compositorto run.

Huge thanks to@Supreeemefor all the continued development on xwayland-satellite, and making it work as well as it does!

## Screen reader support

Aseries of postsby fireborn earlier this year on the screen reader situation in Linux got me curious: howdoesone support screen readers in a Wayland compositor? The documentation is unfortunately scarce and difficult to find. Thankfully,@DataTrinyfrom theAccessKitproject came acrossmy issue, pointed me at the right protocols, and answered a lot of my questions.

So, as of this release, niri has basic support for screen readers! We implement theorg.freedesktop.a11y.KeyboardMonitorD-Bus interface forOrcato listen and grab keyboard keys, and we expose the main niri UI elements via AccessKit. Specifically, niri will announce:

* workspace switching, for example it'll say "Workspace 2";
* the exit confirmation dialog;
* entering the screenshot UI and the overview;
* whenever a config parse error occurs;
* the important hotkeys list.

Here's a demo video, watch with sound on.

niri-orca.mp4

I also added a default config bindingSuperAltSto toggle Orca, which is the standard key binding for this. Orca still requires an X11 socket, so the new xwayland-satellite integration really helps here too.

The current screen reader support and further considerations are documented on the newAccessibilitywiki page.

I also want to thank@tyrylufor histalkat this year's GUADEC that sheds some light on the current developments in Linux accessibility, and for answering a slew of my questions when I caught him afterward.

## Modal exit confirmation

The screen reader integration necessitated making our exit confirmation dialog a proper modal dialog that takes full keyboard focus. A natural extension of this was to add full-screen dimming, emphasizing that you're about to log out of the entire session, and a nice open/close animation (which you can of coursedisableif you want).

Hopefully, this will mark the end of me accidentally logging out instead of closing the nested development niri window.(It didn't. Mere dimming is no match for the speed of a well-practicedSuperShiftE⇒Entermotion.)

niri-exit-confirmation-anim.mp4

## Screenshot UI improvements

In the last release, the screenshot UI learned to respond to some keyboard window movement bindings by moving the screenshot selection. Now,@iostapyshynmade the screenshot UI also handle themove-column-left-or-to-monitor-left/rightandmove-window-up-or-to-workspace-up/downactions, while I implementedmove-column/window-to-monitorthat moves the selection across monitors.

This works similarly to a floating window: the selection origin is preserved relatively, and the size is adjusted by the monitor scale difference. Under the right conditions, it'll match a floating window exactly.

Also, holdingSpacewhile dragging out a selection with the mouse will now let you move the selection!

niri-screenshot-kb-move.mp4

I made it work with a second touch on a touchscreen too. This was inspired by how inosu!you can drag the cursor with one finger and touch with a second/third to "click".

niri-screenshot-move-touch.mp4

## Keyboard layout from systemd-localed

To aid distribution integration, niri learned to read the keyboard layout from systemd-localed atorg.freedesktop.locale1over D-Bus. This is now the default behavior when there's noexplicit XKB layout configuration, so it should "just work" for distribution installers that set the layout via localed.

## Screencasting fixes

Some NVIDIA users saw flickering when screencasting in Discord or OBS. Last release added await-for-frame-completion-in-pipewiredebug flag to work around the problem.

In this release, I fixed the problem properly (by delaying sending screencast frames over PipeWire until they finished rendering) and removed the debug flag. As a reminder, debug flags are not covered by ourconfig breaking change policy.

I also corrected the app IDs that niri communicates to xdg-desktop-portal-gnome, making it correctly show the icons for most applications in the window picker.

## ext-workspace protocol

I implemented theext-workspaceWayland protocol in niri. It gives desktop components information about workspaces, so bars can use it to make a workspace indicator compatible with different compositors.

Along the way, I found a number of bugs in the ext-workspace code in various bars. All those bugs are now fixed, so you can use theext/workspacesmodule inWaybar 0.14, and in upcoming versions ofsfwbarandxfce4-panel. Work is ongoing to implement ext-workspace inlxqt-panelandQuickshell.

## Window positions and sizes in the IPC

After consuming several people (thanks@calopsand@aeghnfor the intermediate discussions and PRs), the challenge of adding window sizes and positions to the niri IPC was finally bested by@yrkv. Windows returned byniri msg windowsand the event stream now provide the following layout information:

* for windows in the scrolling layout: index of the window's column on the workspace, and index of the window inside that column;
* for floating windows: position on screen;
* for all windows: size of the tile (including borders) and of the underlying Wayland window, and the Wayland window's offset inside the tile.

You can findthe detailed documentationin niri-ipc.

This data already lets you order your window lists to match the workspace, make visual displays for floating windows, or keep track of how many columns are to the left/right of a given window. Here's a quick demo I put together in quickshell which tracks floating windows on the current workspace.

niri-floating-window-ipc-test.mp4

Some things are still missing, like the current "scroll position" or floating window stacking order. They will be added later, when we figure out the best way to expose them (there's a tricky trade-off between ease of use and spamming the IPC too much).

As another small IPC improvement,@HigherOrderLogicadded theConfigLoadedevent and adisable-failedoption for the built-in niri config notification. Together, these let desktop shells implement this notification in a custom manner.

## Config additions and fixes

One common source of confusion about the niri config is thespawncommand used for running programs. Unlike similar commands in other compositors, niri'sspawnruns the given binary directly, without going through the shell, meaning that you have to manually split arguments and cannot use shell expansions or pipelines.

In this release, I addedspawn-shandspawn-sh-at-startupthat accept a single argument—the command to run—and run it through the shell. Withspawn-sh, all complex commands work as expected:

binds
 {

// Works with spawn-sh: all arguments in the same string.

 Mod+D
 {
 spawn-sh

"alacritty -e /usr/bin/fish"
; }


// Works with spawn-sh: shell variable ($MAIN_OUTPUT), ~ expansion.

 Mod+T
 {
 spawn-sh

"grim -o $MAIN_OUTPUT ~/screenshot.png"
; }


// Works with spawn-sh: process substitution.

 Mod+Q
 {
 spawn-sh

"notify-send clipboard
\"
$(wl-paste)
\"
"
; }


// Works with spawn-sh: multiple commands.

 Super+Alt+S
 {
 spawn-sh

"pkill orca || exec orca"
; }
}

Under the hood,spawn-sh "some command"is equivalent tospawn "sh" "-c" "some command"—it's just a less confusing shorthand.

Now, on to the rest of the config additions and improvements in this release:

* @two-hornedimplemented theswitch-preset-column-width-backandswitch-preset-window-height-backactions that reverse the existing preset-switching ones.
* @HigherOrderLogicadded thecubic-bezieranimation easing typethat lets you use a custom cubic Bézier curve with the same parameters as in CSS.
* @chinatsuadded thehide-not-boundhotkey-overlay setting that prevents the Important Hotkeys dialog from showing(not bound)hotkeys.
* The pointing deviceaccel-speedand animationslowdownwere changed to accept integer values without having to spell out the floating point.0. This also added parsing-time limits to the values: [-1; 1] toaccel-speedand [0; 231) toslowdown. While this is technically a config breaking change, the values outside that range weren't valid either way.
* @lierdakiladded thescroll-button-lockoption forpointing devices.
* @bkuri, after some struggling against Claude Code, implemented separate vertical and horizontalscroll-factoroptions forpointing devices.
* Fixed hot reloading for trackball, tablet, and touch libinput settings.
* @abdavisadded clamping to configured color values after color space conversion, fixing a rendering difference between solid colors and gradients.
* @Gwenodaiadded theskip-cursor-only-updates-during-vrrdebug flag that prevents cursor movement from redrawing the screen when variable refresh rate is on. This is useful for games where the cursor isn't drawn internally to prevent erratic VRR shifts in response to cursor movement.
* @sashomashoadded thedeactivate-unfocused-windowsdebug flag that works around incorrect keyboard focus tracking from various Chromium- and Electron-based applications. If your chat window thinks it's focused, and doesn't show message notifications, despite being on a different workspace, then this debug flag might help.
* @bbedwardadded thekeep-max-bpc-unchangeddebug flag as a workaround fora bugwith AMDGPU and some OLED panels that causes niri to fail to turn them on.
* Clarified and improved the example values for some options in the default config.@schuelermineset theclose-windowbind asrepeat=false.@dev-nicolaosadded backlight adjustment binds usingbrightnessctl.
* Num Lock state is now preserved acrossXKB configchanges.
* @sodiboomade config hot reloading work for/etc/niri/config.kdl.

## Other improvements in this release

* @HigherOrderLogicmade our FreeDesktop idle inhibitor also register its D-Bus service at/ScreenSaver, making it work with more apps, like VLC.
* @my4ngmade niri turn off HDR. We don't support HDR yet, so enabled HDR carried over from other compositors would just result in broken colors.
* @zgibberishfixed--focus=falsenot working when usingmove-column-to-workspace-up/downon a floating window.
* Added--focus=falseargument tomove-window-to-workspace-up/down.
* @artrixdotdevadded Nushell completion support:niri completions nushell.
* Fixed tiled window popup menus sometimes appearing underneath exclusive-zone layer-shell components (the unconstraining logic wasn't taking these exclusive zones into account).
* Changed the ext-session-lock surface size to round rather than floor, which removes a 1 px "border" on some fractional scales.
* Fixed ext-session-lock clients that got denied the lock being able to create and show a lock surface. In particular, this fixes extra gtklock instances being able to destroy the active lock client, leaving you with an empty red locked session screen.
* @notpeelzmade niri set the logind LockedHint when the screen is locked through ext-session-lock. This for example enables idle daemons to only put the computer to sleep when it is locked.
* @sodibooadded SIGINT, SIGTERM and SIGHUP handling to niri: these will now exit niri properly, cleaning up the Wayland sockets and other resources.
* @Vladimir-cspadded a check that makesuwsm start niri.desktopwork for those who useUWSM.
* @vanderlokkenaddedniri msg action load-config-fileto force-reload the config file without waiting for hot reloading.
* Fixeda small animation bugwhen quickly resizing tiled windows back and forth. This problem was fairly difficult to trigger by accident (unless you're specifically trying to reproduce it), but it caused further problems "downstream" for combined window actions.
* Removed redundant "device is inactive" warning spam when switching to a different TTY.
* Fixed changing floating window height resetting the presetwidthindex rather than the preset height index.
* Thanks to@zimwardand@matejcfor adding Alpine/musl and FreeBSD CI jobs respectively, ensuring that niri keeps building on those systems.
* Updated Smithay:Added support for version 2 of the cursor-shape protocol.Fixed the keymap sent to clients, makingwvkbdwork.Fixed integer overflows from layer surfaces setting extremely high margin values.Fixed an issue where a clipboard client that terminates unexpectedly did not cause an immediate empty clipboard event.Fixed mouse input to the bottommost and rightmost edges of a surface sometimes getting missed.
* Added support for version 2 of the cursor-shape protocol.
* Fixed the keymap sent to clients, makingwvkbdwork.
* Fixed integer overflows from layer surfaces setting extremely high margin values.
* Fixed an issue where a clipboard client that terminates unexpectedly did not cause an immediate empty clipboard event.
* Fixed mouse input to the bottommost and rightmost edges of a surface sometimes getting missed.

## Funding

I work on niri in the spare time that I have from my university studies. If you like what I do, you can support my work onGitHub Sponsors. Big thanks to all current and past sponsors!



### Contributors

 sashomasho, bkuri, and 28 other contributors




Assets

3




Loading

### Uh oh!

There was an error while loading.Please reload this page.






👍

37


CIAvash, YannMagnin, IgnIVertiKalCaD, ClixTW, msmafra, pulcinello, dimsuz, blurgyy, XDream8, psinus, and 27 more reacted with thumbs up emoji


😄

3


devxan, psi4j, and helixoid reacted with laugh emoji


🎉

78


deviantsemicolon, knuesel, gizmogoat, Luk-ESC, my4ng, stefur, MisterKartoffel, Mitchyopp, clot27, FelipeFMA, and 68 more reacted with hooray emoji


❤️

48


zgibberish, FelipeFMA, peterhirn, Alanazane, anotherwanwanyi, applejag, YannMagnin, Hari-c137, IgnIVertiKalCaD, ClixTW, and 38 more reacted with heart emoji


🚀

10


scottmckendry, hmamigo, devxan, Methapon2001, psi4j, helixoid, chmanie, dikesh, deathtrip, and hypernova7 reacted with rocket emoji


👀

3


msmafra, devxan, and psi4j reacted with eyes emoji



All reactions


121 people reacted

 13




Join discussion
