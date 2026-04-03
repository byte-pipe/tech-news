---
title: 'PSA: SQLite WAL checksums fail silently and may lose data - blag'
url: https://avi.im/blag/2025/sqlite-wal-checksum/
site_name: hackernews
fetched_at: '2025-07-25T07:05:12.470308'
original_url: https://avi.im/blag/2025/sqlite-wal-checksum/
date: '2025-07-25'
description: SQLite WAL has checksums, but on corruption it drops all the data and does not raise error
---

This is a follow-up post to myPSA: SQLite does not do checksumsandPSA: Most databases do not do checksums by default. In the previous posts I mentioned that SQLite does not do checksums by default, but it has checksums in WAL mode. However, on checksum errors, instead of raising error, it drops all the subsequent frames. Even if they are not corrupt. This is not a bug; it’s intentional.

## SQLite WAL

SQLite introduced WAL in 2010. It’s not the default mode, but you’re likely using it if you want higher write throughput. Whenever you make writes, they are first written to the WAL file. Then, during checkpoint operations, the database pages are written from the WAL to the main DB file. Each page in the WAL is called a frame. Each frame has a header, which comprises the frame number, page number, commit marker, and checksums.

The way checksums work in WAL is interesting. They use rolling checksums, meaning the checksum of the n+1 frame is computed with the checksum of the nth frame. In other words, a frame’s checksum depends on the previous frame.

## Recovery

If one frame is found to have a checksum mismatch, you can’t be sure that the next frame isn’t corrupted either. What’s interesting is that when a frame is found to have a missing or invalid checksum, SQLite drops that frame and all the subsequent frames. This isdocumented:

Recovery works by doing a single pass over the WAL, from beginning to end. The checksums are verified on each frame of the WAL as it is read. The scan stops at the end of the file or at the first invalid checksum. The mxFrame field is set to the index of the last valid commit frame in WAL.

Earlier I mentioned SQLite does not do checksums by default, so it won’t ever notice if a page is corrupt. So when is WAL checksum verification triggered? A WAL may contain multiple frames for the same page number. To make lookups faster, SQLite maintains an index called the WAL Index. This is the.db-shmfile you often see. During the building of this index, SQLite checks the checksums.

You can verify this in the code as well. The recovery process happens inwalIndexRecover, this callswalDecodeFramewhich has this:

/* A frame is only valid if a checksum of the WAL header,

** all prior frames, the first 16 bytes of this frame-header,

** and the frame-data matches the checksum in the last 8

** bytes of this frame-header.

*/

nativeCksum
=
 (pWal
->
hdr.bigEndCksum
==
SQLITE_BIGENDIAN);

walChecksumBytes
(nativeCksum, aFrame,
8
, aCksum, aCksum);

walChecksumBytes
(nativeCksum, aData, pWal
->
szPage, aCksum, aCksum);

if
( aCksum[
0
]
!=
sqlite3Get4byte
(
&
aFrame[
16
])


||
 aCksum[
1
]
!=
sqlite3Get4byte
(
&
aFrame[
20
])

){


/* Checksum failed. */


return

0
;

}

To trigger this issue, the following needs to happen:

1. You have SQLite.dband.db-walfiles, but no accompanying.db-shmfile. Maybe your friend shared it with you, or you downloaded some data off the internet.
2. Unclean shutdown during WAL write. The WAL index is updated after a successful write. Maybe after the WAL write, the process crashed, and the index wasn’t updated. On the next start, SQLite rebuilds the index.

During this process, if there’s a checksum mismatch on a frame, that frame and the rest of the WAL frames are dropped. Even if they are not corrupt (technically)! Note that SQLite always checkpoints and truncates the WAL file on the last connection close.

## Demo

Alice would have lost money,again. Poor Alice.

## Thoughts

1. I really don’t like that SQLite doesn’t throw any error on detection of corruption
2. Since it automatically checkpoints every time, the data is lost too

I’m not sure why this is the default behavior. Backward compatibility reasons? The checksums in WAL are likely not meant to check for random page corruption in the middle; maybe they’re just to check if the last write of a frame was fsynced properly or not?

What I want: throw an error when corruption is detected and let the code handle it. Don’t checkpoint and truncate the WAL! Maybe provide an option for users to opt in to ignore the corruption and work with the existing behavior.

In the demo, I corrupted a frame that belonged to an older version of a page. Meaning no new transactions can ever read that data. That frame is practically useless, yet it caused data loss. There are pages like belonging to an index or maybe some table that we don’t care about at all. With sophisticated recovery mechanisms, we could sometimes able to recover all the data.

Overall, I don’t like this as a default. However,Pekka Enbergoffered a different perspective that SQLite runs in embedded environments where there’s no server, and maybe core developers decided it may be better to limp along than crash.

I would guess that other databases behave the same way, but I haven’t verified it myself. I was discussing this withAlex Miller, and he raised an interesting point: SQLite mostly runs on mobile devices with cheap SD cards (as opposed to running on enterprise-grade SSDs), and corruptions are more common. So, it’s more important for SQLite to have corruption detection than other databases.
