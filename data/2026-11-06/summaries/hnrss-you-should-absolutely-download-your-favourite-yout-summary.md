---
title: You should absolutely download your favourite youtube videos – The Sun and The Air
url: https://criminallyvulgar.dev/you-should-absolutely-download-your-favourite-youtube-videos/
date: 2026-11-05
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-11-06T12:28:57.085275
---

# You should absolutely download your favourite youtube videos – The Sun and The Air

# You should absolutely download your favourite youtube videos

## Main argument
- The corporate internet is hostile to art; the things you love don’t belong to you unless you claim them.
- Many liked videos disappear over time, so downloading ensures you always have access.

## Basic tools
- **yt‑dlp** (or one of its many wrappers) can download videos with good defaults.
- Store the files on a bulk storage drive or NAS for reliable access.

## Personal (over‑engineered) setup
### Jellyfin
- Created a library in *TV Shows* mode called “YouTube”.
- Turned off all metadata scrapers and set the system to prefer file data over filenames.

### ytdl‑sub
- The only yt‑dlp wrapper that preserves playlist structure, driven by `.yaml` configuration files.
- Runs in a self‑hosted Docker‑Compose container with a web‑app VSCode IDE.
- Custom genres and playlists are defined; some videos are tagged as “Documentaries” to fit the tool’s expectations.
- Issue: Jellyfin placed each video in two series (Year and Playlist). Fixed by assigning the playlist title as the Season Number in the ytdl‑sub config.
- Changing the Season Number after import requires a full library re‑import, which is impractical for a terabyte‑scale collection.

### Tdarr
- Service that automatically re‑encodes videos (e.g., to HEVC/H.265) to save storage.
- UI is complex; most users end up using the default workflow because it works.
- Can break on complex setups; a small script tweak prevented crashes on certain data streams.
- May cause Jellyfin to lose thumbnail images (fixable by refreshing metadata).
- Saved roughly 700 GB on a 2 TB library, though more selective downloading could have reduced the need.

## Practical considerations
- Need to play videos on a TV, integrate with existing NAS, and organise hundreds of videos across dozens of playlists without manual effort.
- Jellyfin’s rigid hierarchy (Movies, TV Shows, Artists) makes playlist‑centric organization tricky.
- Re‑importing large libraries is time‑consuming, so configuration must be correct from the start.

## Recommendations
- Use yt‑dlp (or a wrapper) for bulk downloading of YouTube content.
- Choose ytdl‑sub if preserving playlist hierarchy is important and you’re comfortable with YAML configuration and Docker.
- Consider Tdarr for storage‑saving transcoding only if you can tolerate its UI complexity and occasional thumbnail issues.
- Be selective about what you download to avoid unnecessary storage pressure.

## Footnotes
- Vibe‑coding note: yt‑dlp scripts are well documented online, but the command line can be daunting for most users.  
- As with all homelab projects, the setup is never perfect; ongoing tinkering keeps the hobby alive.