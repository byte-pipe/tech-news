---
title: Someone on Torrent Sites Kept Fucking With My Sonarr
url: https://thereallo.dev/blog/someone-on-torrent-sites-kept-fucking-with-my-sonarr-setup
date: 2026-10-15
site: hackernews_api
model: llama3.2:1b
summarized_at: 2026-10-16T15:14:39.588642
---

# Someone on Torrent Sites Kept Fucking With My Sonarr

# Someone on Torrent Sites Kept Hacking with My Sonarr

## Key Points

* A torrent had an EXE file attached to it, containing a South Park episode, and was being downloaded on the NAS stack.
* Someone found and uploaded the file to public trackers, then used Sonarr to import it.
* Sonarr blocked the file because it exceeded 90-second import periods, despite not modifying the disk.
* The uploaded EXE file was found to contain a decrypted payload, which was then used to decrypt the main file.
* The payload was found to be a simple XOR encrypted 32-byte block, which was hidden within the file.
* The XOR block was used to map the payload into memory without touching the disk.
* The remaining 886 MB of the file were random junk, and it's unclear why it was uploaded and then deleted.

## Summary

Someone on a torrent site found and uploaded an EXE file to public trackers, containing a South Park episode. Someone else downloaded the file onto the NAS stack using Sonarr and tried to import it without modifying the disk. Despite this, Sonarr blocked the file due to the large delay in import periods. The uploaded EXE file contained a simple XOR encrypted 32-byte block, which was used to decrypt the main file. The payload was mapped into memory without touching the disk, and the remaining 886 MB consisted of random junk.

## Obscure Details

* The XOR block in the EXE file was used to perform a series of six steps: open its own file, read the last 64 bytes, use those to find and decrypt a payload, map it as a PE in memory, find the payload size and use it to map another PE into memory, and point the PEB's ImageBaseAddress.
* The payload was a simple ChaCha20 cipher, hidden in the EXE file by building it out of global variables.
* ChaCha20 was still detectable, despite being hidden in a 32-byte k value.