---
title: Backblaze has quietly stopped backing up your data | Robert Reese's Website
url: https://rareese.com/posts/backblaze/
site_name: hnrss
content_file: hnrss-backblaze-has-quietly-stopped-backing-up-your-data
fetched_at: '2026-04-14T11:57:26.875624'
original_url: https://rareese.com/posts/backblaze/
date: '2026-04-14'
description: Backblaze has stopped backing up your data
tags:
- hackernews
- hnrss
---

# Backblaze has quietly stopped backing up your data

TLDR: Despite claiming to backup all your data, Backblaze quietly stopped backing up OneDrive and Dropbox folders - along with potentially many other things.

### A good decade

For ten years I have been using Backblaze for my personal computer backup. Before 2015 I would backup files to one of two large external hard discs. I then rotated these drives between, first my father’s house, and after I moved to the UK, my office drawers.

In 2015 Backblaze seemed like a good bet. Unlike Crashplan their software wasn’t a bloated Java app, but they did have unlimited storage. If you could cram it into your PC they would back it up. With their yearly Hard Drive reviews making good press, a lot of personal recommendations from my friends and colleagues, their service sounded great. I installed the software, ran it for several weeks, and sure enough my data was safely stored in their cloud.

I had further reason to be impressed when several years later one of my hard drives failed. I made use of their “send me a hard drive with my stuff on it service”. A drive turned up filled with my precious data. That for me was proof that this system worked, and that it worked well.

And so I recommended Backblaze for years. What do you do for backup? I would extoll the virtues of Backblaze, and they made many sales from such recommendations.

There were a few things I didn’t like. The app, could use a lot of memory, especially after doing a large import of photographs. The website, which I often used to restore single files or folders, was slow and clunky to use. The windows app in particular was clunky with an early 2000s aesthetic and cramped lists. There was the timethey leaked all your filenames to Facebook, but they probably fixed that.

But no matter, small problems for the peace of mind of having all my files backed up.

### A disturbing trend

Backup software is meant to back up your files. Which files? Well the files you need. Given everyone is different, with different workflows and filetypes, the ideal thing is to back up all your files. No backup provider knows what I will need in the future. The provider must plan accordingly.

My first troubling discovery was in 2025, when I made several errors then did apush -fto GitHub and blew away the git history for a half decade old repo. No data was lost, but the log of changes was. No problem I thought, I’ll just restore this from Backblaze. Sadly it was not to be. At some point Backblaze had started to ignore.gitfolders.

This annoyed me. Firstly I needed that folder and Backblaze had let me down. Secondly within the Backblaze preferences I could find no way to re-enable this. In fact looking at the list of exclusions I could find no mention of.gitwhatsoever.

This made me wonder - I had checked the exclusions list when I installed Backblaze 9 years before, had I missed it? Had I missed anything else?

Well lesson learned I guess, but then a week ago I came across this thread on reddit: “Doesn’t back up Dropbox folder??”. A user was surprised to find their Dropbox folder no longer being backed up. Alarmed I logged into Backblaze, and lo and behold, my OneDrive folder was missing.

I. Am. Fucking. Furious.

Backblaze has one job, and apparently they are unable to do that job. Back up my stuff. But they have decided not to.

### Sync is not backup

Lets take an aside.

A reasonable person might point out those files on OneDrive are already being backed up - by OneDrive! No. Dropbox and OneDrive are for file syncing - syncing your files to the cloud. They offer limited protection. OneDrive and Dropbox only retain deleted files for one month. Backblaze has one year file retention, or if you pay per GB, unlimited retention. While OneDrive retains version changes for longer, Dropbox only retains version changes for a month - again unless you pay for more. Your files are less secure and less backed up when you stick them in a cloud storage provider folder compared to just being on your desktop.

And that’s assuming your cloud provider is playing ball. If Microsoft or Dropbox bans your account you may find yourself with no backup whatsoever.

### The betrayal

For me the larger issue is they never told us. My OneDrive folder sits at 383GB. You would think that having decided to no longer back this up I might get an email, and alert or some other notification. Of course not.

Nestled into theirrelease notesunder “Improvements” we see:

The Backup Client now excludes popular cloud storage providers from backup, including both mount points and cache directories. This prevents performance issues, excessive data usage, and unintended uploads from services like OneDrive, Google Drive, Dropbox, Box, iDrive, and others. This change aligns with Backblaze’s policy to back up only local and directly connected storage.

First, I would hardly call this change in policy an improvement, its hard to imagine anyone reading this as anything other than a downgrade in service. Secondly does Backblaze believe most of its users are reading their release notes?

And if you joined today and looked at their list offile exclusionsyou would find no reference to Dropbox or OneDrive. No mention of Git either.

Here’s the thing, today they don’t back up Git or OneDrive. Who’s to say tomorrow they wont add to the list. Maybe some obscure file format that’s critical to your work flow. Or they will ignore a file extension that just happens be the same as one used by your DAW or 3D Modelling software. And they won’t tell you this. They wont even list it on their site.

By deciding not to back up everything, Backblaze has made it as if they are backing up nothing.

### Promises wept

But really this feels like a promise broken. Back in2015their website proudly proclaimed:

All user data included by default
No restrictions on file type or size

Protect the digital memories and files that matter most to you.

File backup is a matter of trust. You are paying a monthly fee so that if and when things go wrong you can get your data back. By silently changing the rules, Backblaze has not simply eroded my trust, but swept it away.

I wrote this to warn you - Backblaze is no longer doing their part, they are no longer backing up your data. Some of your data sure, but not all of it.

Finally let me leave you with Backblaze’s own words from 2015:

Unlimited, Simplified, Secure Personal Online Backup Cloud Storage

They promised to simplify backup. They succeeded - they don’t even do the backup part anymore.