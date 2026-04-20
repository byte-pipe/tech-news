---
title: Block the “Upgrade to Tahoe” alerts and System Settings indicator – The Robservatory
url: https://robservatory.com/block-the-upgrade-to-tahoe-alerts-and-system-settings-indicator/
date: 2026-03-01
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-03-02T08:26:49.808744
---

# Block the “Upgrade to Tahoe” alerts and System Settings indicator – The Robservatory

# Block the “Upgrade to Tahoe” alerts and System Settings indicator

## Background
- macOS 15.7.3 contains a bug that lets the 90‑day deferral period for major updates be treated as a rolling window, allowing users to suppress the “Upgrade to Tahoe” notification.
- The author prefers to keep a machine on macOS Sequoia while supporting customers on macOS Tahoe, but dislikes the frequent upgrade alerts and the red badge on the System Settings icon.

## Solution Overview
- Use a device‑management configuration profile to block major macOS updates for up to 90 days.
- The “Stop Tahoe Update” GitHub project provides a ready‑made profile (`deferral-90days.mobileconfig`) that implements this policy.

## Step‑by‑Step Instructions
1. **Clone the repository**
   ```bash
   git clone https://github.com/travisvn/stop-tahoe-update.git
   cd stop-tahoe-update
   ```
2. **Make the scripts executable** (not mentioned in the original README)
   ```bash
   chmod 755 ./scripts/*.sh
   ```
3. **Generate two unique UUIDs** and replace the placeholders in `profiles/deferral-90days.mobileconfig`:
   - Locate `<key>PayloadUUID</key><string>REPLACE-WITH-UUID</string>` lines.
   - Run `uuidgen` twice, copy each UUID, and substitute the placeholders.
4. **Optional: limit the policy to major OS updates only**
   - Edit the `<key>forceDelayedSoftwareUpdates</key>` entry to `<false/>` so minor updates still appear.
5. **Run the install script**
   ```bash
   ./scripts/install-profile.sh profiles/deferral-90days.mobileconfig
   ```
   - The script will report that the `profiles` tool is deprecated and instruct you to approve the profile in System Settings → Privacy & Security → Profiles.
6. **Complete installation via System Settings**
   - Open System Settings, select the “Profile Downloaded” entry, double‑click the profile, and click **Install** through the subsequent dialogs.
   - After a restart of System Settings, a message confirming the deferral appears at the top of the Software Update pane.
7. **Create a shortcut for re‑applying the profile** (after the 90‑day period expires):
   - Save the edited `.mobileconfig` file somewhere convenient.
   - Add an alias to `~/.zshrc`:
     ```zsh
     alias notahoe='open "/path/to/deferral-90days.mobileconfig"; sleep 2; open "x-apple.systempreferences:com.apple.preferences.configurationprofiles"'
     ```
   - Running `notahoe` will reopen the profile and bring up the Profiles panel for a quick reinstall.

## Expected Behaviour
- For the next 90 days the “Upgrade to Tahoe” notification and the red badge on System Settings are suppressed.
- After the period ends, the policy may expire or the upgrade alert will reappear; reinstalling the profile via the alias restores the block.

## Personal Outcome
- The author reports a much smoother experience, free from intrusive upgrade prompts, while still maintaining a separate Tahoe machine for customer support.
