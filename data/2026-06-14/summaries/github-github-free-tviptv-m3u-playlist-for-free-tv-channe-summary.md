---
title: GitHub - Free-TV/IPTV: M3U Playlist for free TV channels · GitHub
url: https://github.com/Free-TV/IPTV
date: 
site: github
model: llama3.2:1b
summarized_at: 2026-06-14T11:48:08.685466
---

# GitHub - Free-TV/IPTV: M3U Playlist for free TV channels · GitHub

**Free-TV IPTV Playlist**
=======================

**Overview**
------------

This is an M3U playlist for free TV channels around the world, hosted on GitHub and provided by Plex TV, Pluto TV, and other free IPTV services. The playlist includes a variety of content from these providers, including live feeds and offline streams.

**Key Points**
---------------

1. **Quality over Quantity**: The main goal is to provide high-quality content in HD.
2. **Free Channels Only**: No paid channels or regional dedications are allowed.
3. **Mainstream Content**: This playlist includes no adult or religious channels, nor parties supported by external funding.
4. **Updated Feed Sources**: A list of sources used for updating the M3U files.

**Structure**
--------------

* Main sections:
	+ **Feed Sources**: List of websites providing free IPTV content
	+ **Format**: Explanation of how channels are organized and parsed
	+ **Issues and Pull Requests**: Guidelines for contributors

**Contents**
-------------

* **Feeds**
	+ M3U playlist files (`.m3u8`, `.md` files)
* **Streams**
	+ IPTV player to download the playlist file (`make_flags.sh` script): `https://raw.githubusercontent.com/Free-TV/IPTV/master/playlist.m3u8`

**Repository Files Navigation**
---------------------------------

To use this playlist, navigate to the repository and point your IPTV player at:

```bash
https://raw.githubusercontent.com/Free-TV/IPTV/master/playlist.m3u8
```

This is a free TV channel playlist. The less channels we support the better.

* All channels should work well.
* As much as possible channels should be in HD, not SD.
* Only one URL per channel (no +1, no alternate feeds, no regional declinations)

Only free channels are included, with exception to paid channels that can be obtained with a commercial subscription. These channels should appear here; paid ones will simply use the next available alternative.

As an added note that adult content is excluded or filtered from this playlist.

* No adult content
* Only mainstream channels

This playlist includes no copyrighted material of any kind, including but not limited to music and TV shows.

* Content belongs to their respective owners.
* This list is meant for informational purposes only.

**Issues and Pull Requests**
---------------------------

No new bug reports, edited channels or pull requests will be accepted. Please use GitHub Issues or pull requests instead.