---
title: How Microsoft abuses its users
url: https://lzon.ca/posts/other/microsoft-user-abuse/
site_name: hackernews_api
content_file: hackernews_api-how-microsoft-abuses-its-users
fetched_at: '2026-04-10T11:21:48.329179'
original_url: https://lzon.ca/posts/other/microsoft-user-abuse/
author: jpmitchell
date: '2026-04-09'
description: Microsoft is employing dark patterns to goad users into paying for storage?
tags:
- hackernews
- trending
---

## How Microsoft abuses its users






Blog



Other



 How Microsoft abuses its users





 Posted April 09, 2026




 7 min read



I’d like to tell the story of job I just completed for a customer, so that I can make a point about how I feel Microsoft and other large technology companies are actively hostile to their users.

### The Story

 An error message similar to what my customer would have seen.

I received a call from my neighbour asking if I would be willing to help her husband with an issue he’d been having with his laptop. As the proud new owner of my own IT services company, I of course agreed to take a look.I spoke with my neighbour’s husband, and immediately saw that he was not tech literate. I learned to identify the type while doing IT work for my previous employer. This made understanding his problem difficult, but through conversation we did manage to come to an understanding about what the real issue was that he was experiencing.What he was seeing was that he was no longer receiving email in Outlook, and that there was an error message claiming he had ‘run out of available storage’, or some other similar nonsense. He is a very light email user, and he knows it. He was confused as to why he’d run out of storage. I was confused as well, at first.Through investigation I discovered that the Outlook email service uses Onedrive for storage ofallmessages and attachments. He had 5 GB of available storage, the amount that is given with his free account. This had yet to explain why he was seeing that error message, there was no way he had consumed 5 GB of storage with just his email use.Unsurprisingly, his Onedrive storage wasn’t filled by his email, it was filled by the personal files from his Windows 11 desktop. Did he configure Windows to save those files to his Onedrive directory, instead of his local home directory? Of course not, that was done by default. Did he even know that this was happening? Also, no. He had no idea this was happening until he saw that error message, which oh-so-helpfully offered to ‘solve’ his problem by offering him a subscription to additional paid storage capacity on the account.He did manage to loosely understand what was happening, enough at least to start deleting files from his computer to try and make the error message go away. I was never able to confirm with him, but I suspect that he deleted files (including family photos) for which he had no other backup.I will be blunt, thisinfuriatesme. This wasn’t the first time I’ve seen this. I saw it many times while working for my previous employer. Microsoft has intentionally broken a fundamental assumption about how files are stored on a computer running Windows. They do this without asking the user, and without adequately explaining what they have done. Microsoft is very obviously employing dark patterns in order to goad its users into paying for Onedrive storage.I’m a computer nerd, and if you are reading this you probably are as well. We can change that setting ourselves without much thought, and we probably have backups of our important data in case recovery is necessary. I will tell you that many people are extremely utilitarian about their computer use. They use their computers only to the degree that they must to serve their other interests in life. They alsotrustthat theirproperty, the device that cost them hundreds of dollars isn’t trying tocheat themlike some back-alley con artist.This isn’t a game. My customer isn’t a number on a spreadsheet, merely an increment towards reaching some useless KPI. He deleted family photos to try and get that error message to go away, so that he could just receive emails again. He may not understand what happened, but he’snotstupid. He suspected that this was a scam to get him to pay for something he didn’t need, he just didn’t understand how the scam worked.### The FixWinUtil, an extremely useful tool made by Chris Titus.First and foremost, I performed a complete backup of his data. I took everything that I could find locally on the machine, as well as everything from the Onedrive account, including the Trash. It wasn’t much, only a few gigabytes, which I transferred to a separate USB drive.I carefully transferred all files out of the Onedrive directory structure and back into his home folder. The Windows file explorer did not make this easy or intuitive.I proceeded to delete everything from the Onedrive account, through the web interface. I did notice that deleting files merely moved them into the Trash, which was still being counted towards total storage usage. I assumed this was yet another subtle dark pattern.I alluded to changing settings as a way to solve this. The approach we often took at my previous employer was to simply disable Onedrive in the Windows startup list. That could have worked in this case but I had a better idea.Remove Onedrive entirely.I have muscle memory at this point for how to do it, if you were wondering this is the procedure I used:Open an admin Terminal and load up theChris Titus’ winutil.1irmchristitus.com/win|iexOpen the Tweaks TabIn the Advanced Tweaks section, Select ‘Remove Onedrive’Press ‘Run Tweaks’ buttonThis entirely removes the Onedrive application from Windows, including all integrations into other programs, such as the file explorer.I then proceeded to delete everything from the Onedrive account, including the Trash. The error messages finally went away in Outlook and he was able to recieve email messages again.### TakeawayI may be preaching to the choir, but regardless I want to use this post as my opportunity to make these points in my own way.Microsoft is actively hostile towards its users.They have become a basket-case of an organisation, where chasing irrelevant KPI’s has become more important than product quality, or even baseline respect for their users.The exact same can be said, to varying degrees, to every other large consumer-tech company.I see this as the result of bad incentive structures. A toxic game theory that has been allowed to play out over many years without proper scrutiny. The lefty in me might think that this is a manifestation ofLate Capitalism. If so then it feels like we’re about 30 seconds away from midnight.I think a lot about the possible ways to tweak said incentive structures, to build a choice architecture that can prevent even the first step in the process that led to this.Days like today, when I’m thinking about thereal actualways that this nonsense impactsreal actualpeople, I can’t ignore the humans in this loop. People need to actually take responsibility for their choices, not just turn their brain off when the number looks right in the spreadsheet.### ConclusionIf you enjoyed this post, let me know! Email me atmail@lzon.ca, or reach out through one of my social accounts linked on thehomepage.
