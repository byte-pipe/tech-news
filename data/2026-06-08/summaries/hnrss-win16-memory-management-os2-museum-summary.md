---
title: Win16 Memory Management | OS/2 Museum
url: http://www.os2museum.com/wp/win16-memory-management/
date: 2026-06-05
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-06-08T11:02:09.794585
---

# Win16 Memory Management | OS/2 Museum

# Win16 Memory Management

## Introduction
- The article explains how memory management works in 16‑bit Windows (Windows 1.x, 2.x, 3.x) and why it is often overlooked in beginner material.  
- Early Windows acted as an overlay manager because PCs lacked paging support; only the most active 64 KB segments could stay in RAM.  
- “Windows” in this context refers to the 16‑bit line, not Windows NT.

## NE Executable Format
- Windows uses the “New Executable” (NE) format, which stores each segment separately on disk, allowing individual loading, reloading, and relocation.  
- NE supports imports (calls to OS code) and exports (code called by the OS), e.g., window procedures must be exported so Windows can adjust the DS register before calling them.

## Segment‑Based Memory Model
- Memory is organized into segments up to 64 KB.  
- Segments are identified by **handles** (16‑bit opaque values) rather than physical segment addresses.  
- Handles are similar to protected‑mode selectors: they uniquely identify a segment independent of its location.

## Locking and Accessing Segments
- `GlobalAlloc` allocates memory and returns a segment handle.  
- To obtain a usable segment address, an application calls `GlobalLock`, which also increments a lock count and prevents the segment from being moved.  
- After use, `GlobalUnlock` decrements the lock count; when it reaches zero the segment may be relocated or discarded.  
- Accessing a segment after unlocking it is unsafe because the address may become invalid, even if the segment has not yet moved.

## Segment Attributes
- **Fixed vs. Movable**: Fixed segments (e.g., interrupt handlers) stay at a constant address; movable segments can be shuffled to reduce fragmentation.  
- **Discardable vs. Non‑discardable**:  
  - Discardable segments (typically code or read‑only resources) can be removed from RAM and reloaded from the executable when needed.  
  - Non‑discardable segments (usually writable data) remain in memory because their contents cannot be restored automatically.  
- Applications may mark writable data as discardable if they can recreate the data after a reload.

## Memory Management Goals
- By moving and discarding segments, Windows avoids fragmentation and keeps free memory in larger contiguous blocks.  
- The system only moves or discards a segment when necessary; unlocked segments are candidates for relocation at any time.  

## Practical Implications for Developers
- Understand the need to export window procedures and follow the FAR PASCAL calling convention.  
- Use `GlobalLock`/`GlobalUnlock` correctly to avoid dangling pointers.  
- Design applications so that most code and read‑only resources are placed in discardable, movable segments, while writable data is kept in non‑discardable segments or handled with custom recreation logic.