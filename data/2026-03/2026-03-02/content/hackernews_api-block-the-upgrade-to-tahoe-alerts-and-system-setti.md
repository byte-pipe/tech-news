---
title: Block the “Upgrade to Tahoe” alerts and System Settings indicator – The Robservatory
url: https://robservatory.com/block-the-upgrade-to-tahoe-alerts-and-system-settings-indicator/
site_name: hackernews_api
content_file: hackernews_api-block-the-upgrade-to-tahoe-alerts-and-system-setti
fetched_at: '2026-03-02T08:25:11.919011'
original_url: https://robservatory.com/block-the-upgrade-to-tahoe-alerts-and-system-settings-indicator/
author: todsacerdoti
date: '2026-03-01'
description: Block the “Upgrade to Tahoe” alerts
tags:
- hackernews
- trending
---

# Block the “Upgrade to Tahoe” alerts and System Settings indicator

* Jan 17 '26Jan 17 '26
* Apple Universe,Mac OS X Hints,macOS,Terminal
Based on some comments on 
my Mastodon post
, this only works due to a bug in macOS 15.7.3! The 90 day period isn't supposed to be a rolling date, but 90 days from release date. So it should have no impact…but it does, so I hope Apple doesn't fix the bug.

Although I have to have a machine running macOS Tahoe to support our customers, I personally don't like the look of Liquid Glass, nor do I like some of the functional changes Apple has made in macOS Tahoe.

So I have macOS Tahoe on my laptop, but I'm keeping my desktop Mac on macOS Sequoia for now. Which means I have the joy of seeing things like this wonderful notification on a regular basis.

Or I did, until I found a way to block them, at least in 90 day chunks. Now when I open System Settings → General → Software Update, I see this:

The secret? Usingdevice management profiles, which let you enforce policies on Macs in your organization, even if that "organization" is one Mac on your desk. One of the available policies is the ability to block activities related to major macOS updates for up to 90 days at a time (the max the policy allows), which seems like exactly what I needed.

Not being anywhere near an expert on device profiles, I went looking to see what I could find, and stumbled on theStop Tahoe Update project. The eventual goals of this project are quite impressive, but what they've done so far is exactly what I needed: A configuration profile that blocks Tahoe update activities for 90 days.

I first tried to get things working by following the Read Me, but it's missing some key steps. After some fumbling about, I managed to get it working by using these modified instructions:

1. Clone the repo and switch to its directory in Terminal; run the two commands as shown in the project's Read Me:$ git clone https://github.com/travisvn/stop-tahoe-update.git
$ cd stop-tahoe-update
2. Set all the scripts to executable (not in the instructions):$ chmod 755 ./scripts/*.sh
3. Create and insert two UUIDs into the profile (not in the instructions). To do this, use your favorite text editor to edit the file nameddeferral-90days.mobileconfigin theprofilesfolder. Look for two lines like this:<key>PayloadUUID</key><string>REPLACE-WITH-UUID</string>You need to replace that text with two distinct UUIDs; the easiest way to do that is to runuuidgentwice in Terminal, then copy and paste each UUID, replacing eachREPLACE-WITH-UUIDtext with the UUID. Save the changes and quit the editor, unless you want to make the following optional change...
4. Optional step:I didn't want to defer normal updates, just the major OS update, so I changed theOptional (set to your taste)section to look like this:<!-- Optional (set to your taste) -->
 <key>forceDelayedSoftwareUpdates</key><false/>This way, I'll still get notifications for updates other than the major OS update, in case Apple releases anything further for macOS Sequoia. Remember to save your changes, then quit the editor.
5. Run the script as described in the project's Read Me:./scripts/install-profile.sh profiles/deferral-90days.mobileconfigWhen run, you'll see output in Terminal indicating that you're not done yet:Installing profile: profiles/deferral-90days.mobileconfig
profiles tool no longer supports installs. Use System Settings Profiles to add configuration profiles.
Done. You may need to open System Settings → Privacy & Security → Profiles to approve.You'll also get an onscreen alert saying basically the same thing.
6. To finish the installation, open System Settings and click on theProfile Downloadedentry in the sidebar. This will take you to a screen showing the profile you just added. Double-click on that profile, and a dialog appears showing the settings; here's how mine looked, reflecting the changes I made to remove minor updates from the policy:Click the Install button, which will lead you to Yet Another Dialog; again click Install and you'll finally be done. Quit and relaunch System Settings, and you should see a message like mine at the top of the Software Update panel.

As I've just done all this today, I'm not sure exactly what happens in 90 days. I imagine I may be notified that the policy has expired, or maybe I'll just see a macOS Tahoe update notification. Either way, you can reinstall the policy again by just running theinstall-profile.shcommand again. Alternatively, and to make things much simpler, here's what I've done…

I copied my modified profile (thedeferral-90days.mobileconfigfile in theProfilesfolder) to one of my utility folders, so I could remove the repo as I won't need it any more. Then I looked at the install script, which tries to install the profile using theprofilescommand, and if that fails, it then opens the profile to install it. In Sequoia, you can't useprofilesto install a profile, so only theopenpart of the command is needed.

Once I figured out I only needed to use theopencommand, I added a simplealiasin my.zshrcconfiguration file:

# Reinstall the no-Tahoe 90 day policy
alias notahoe='open "/path/to/deferral-90days.mobileconfig"; sleep 2; open "x-apple.systempreferences:com.apple.preferences.configurationprofiles"'

Now I just have to typenotahoeevery 90 days, and the profile will be reinstalled, and System Settings will open to the profiles panel, where a few clicks will finish activating the installed profile. We'll see how that goes in April :).

I amsomuch happier now, not being interrupted with the Tahoe update notification, and not having the glaring red "1" on the System Settings icon.

### Related Posts:

* How to enable the "Beta updates" feature in macOS 13.4+
* It's been quiet around here lately…
* A full history of macOS (OS X) release dates and rates
* A simple AppleScript to reveal System Settings' anchors
* The macOS' version of the cp Unix command won't create links
* Create macOS automations using a little-known app