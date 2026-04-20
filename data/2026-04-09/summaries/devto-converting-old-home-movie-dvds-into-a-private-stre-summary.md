---
title: Converting old home movie DVDs into a private streaming site - DEV Community
url: https://dev.to/peter/converting-old-home-movie-dvds-into-a-private-streaming-site-5bmb
date: 2026-04-08
site: devto
model: llama3.2:1b
summarized_at: 2026-04-09T11:30:04.238319
---

# Converting old home movie DVDs into a private streaming site - DEV Community

**Converting Old Home Movie DVDs into a Private Streaming Site**

After receiving a few old home movies via DVDs that had become unplayable over time, the author was tasked with converting them to a private streaming site for their family to access. To accomplish this, they employed Claude Code, a free CLI tool that utilizes three other tools: `ddrescue`, `ffmpeg`, and `wrangler`. The process involved several steps:

### Step 1: Make a Safe Copy of Each Disc

The author described using `ddrescue` to create a bit-perfect copy of each disc. This ensured that any potential scratches or damage could be detected and corrected before proceeding.

*   **Install:** `brew install ddrescue`
*   **Enter fullscreen mode:** `brew run ./rip.sh disc-01`
*   **Repeat for all discs:** Wrap the process into a script using a build system like `mkbuild` to automate the process.
*   The `ddrescue` tool uses macOS-specific gotchas; addressing these issues, such as detecting the disk drive and specifying accurate file sizes.

### Step 2: Convert to a Playable Format

Once all the discs had been converted, they were then processed using `ffmpeg`. This program extracted the video content from the ISO files and converted it into a modern format suitable for streaming:

*   **Convert to H.264 MP4:** Use `ffmpeg` with specific settings to adjust the video quality.

    ```
    ffmpeg
-i
 VTS_01_1.VOB
  -c:v libx264
  -crf 22
  -c:a aac
  -b:a 128k
  clip-01.mp4
```

### Step 3: Deploy to a Private Streaming Site

Finally, the author uploaded their converted media files to a private streaming site of their choice. While YouTube is an option for easy visibility; `Google Drive` and `Dropbox` offer more control over access.

The process demonstrated not only successful DVD-to-streaming but also highlighted the versatility of open-source tools in handling this task.
