---
title: 's@: social networking over static sites | sAT Protocol'
url: http://satproto.org/
site_name: hnrss
content_file: hnrss-s-social-networking-over-static-sites-sat-protocol
fetched_at: '2026-03-12T11:16:06.152048'
original_url: http://satproto.org/
date: '2026-03-12'
description: Social networking over static sites
tags:
- hackernews
- hnrss
---

# s@: social networking over static sites

 simple *
 static * social networking
self-reliant *

## Quick start

1. Forkthis repo(see below if you need a different name fromsatellite)
2. EnableGitHub Pageson your fork (deploy from themainbranch).
3. Visit the GitHub Pages URL (e.g.https://username.github.io/satellite/)

While this sample implementation uses GitHub, the protocol is agnostic to the hosting service.

Using a custom repo name:
by default, the client looks for data athttps://{domain}/satellite/.
If you already have asatellite/path for something else, add asatproto_root.jsonfile to the root of your main site (e.g. theusername.github.iorepo)
pointing to the actual repo:

{

"sat_root"
:

"my-custom-repo"

}

## sAT Protocol

sAT Protocol (s@) is a decentralized social networking protocol based on static sites.
Each user owns a static website storing all their data in encrypted JSON stores.
A client running in the browser aggregates feeds and publishes posts.
It does not rely on any servers or relays.

In plain terms,s@is designed for you and your friends, and no one else.
This applies to both the technical implementation and the user experience.
At the technical level, data only moves from your own website to your friend’s browser.
There are no servers (like Mastodon) or relays (like the AT Protocol) in the middle1.
And unlike almost all social media platform today,s@is not designed forinfluencers.
To see a friend’s post or to have a friend see your post, you must followeach other2.

## Identity

A user’s identity is their domain name.
Identity is authenticated by HTTPS/TLS - fetching content from a domain proves
the domain owner published it.

## Discovery

As@-enabled site exposes a discovery document at:

GET https://{domain}/satellite/satproto.json

The discovery document simply contains the protocol version and the user’s public key:

{


"satproto_version"
:

"0.1.0"
,


"public_key"
:

"<base64-encoded X25519 public key>"

}

By convention, the client looks under/satellite/by default.
If that path is already taken, place asatproto_root.jsonfile at the domain
root containing{ "sat_root": "my-custom-repo" }— the client checks this first.

## Encryption Model

All user data is stored in an encrypted JSON store.
Only the user and users in the owner’s follow list can decrypt it.

### Keys

* Each user generates anX25519 keypair.
The public key is published in the discovery document.
The private key is stored in the browser’s localStorage.
* A randomcontent key(256-bit symmetric key) encrypts
post data with XChaCha20-Poly1305.
* The content key is encrypted per-follower using libsodium sealed boxes
(crypto_box_sealwith the follower’s X25519 public key)
and stored atkeys/{follower-domain}.json.

### Self Key (keys/_self.json)

The user’s content key and publishing secrets (e.g. GitHub access tokens)
 are bundled into a single sealed box (crypto_box_sealwith the user’s own public key)
and stored atkeys/_self.json. Only the user’s private key can open it.

This allows a user to sign back in on a new device or after clearing
browser storage — they only need their domain and private key.

### Key Rotation (Unfollow)

When the user unfollows someone:

1. Generate a new content key
2. Re-encrypt all posts with the new key
3. Re-create key envelopes for all remaining followers
4. Updatekeys/_self.jsonwith the new content key
5. The unfollowed user’s old key no longer decrypts anything

### Decryption Flow

When Bob visits Alice’s site:

1. Resolve Alice’s data path (viasatproto_root.jsonor the default/satellite/)
2. Fetchkeys/bob.example.com.json
3. Decrypt the content key using Bob’s private key (crypto_box_seal_open)
4. Fetchposts/index.jsonto get the list of post IDs
5. Fetch and decrypt individual posts fromposts/{id}.json.enc(XChaCha20-Poly1305 with the content key)

## Data Schema

Each post is stored as an individually encrypted file. The post index
(posts/index.json) is a plaintext JSON file listing post IDs
newest-first, allowing clients to lazily load only recent posts.

A post object:

{


"id"
:

"20260309T141500Z-a1b2"
,


"author"
:

"alice.com"
,


"created_at"
:

"2026-03-09T14:15:00Z"
,


"text"
:

"Hello, decentralized world!"
,


"reply_to"
:

null
,


"reply_to_author"
:

null

}

Post IDs are{ISO8601-compact-UTC}-{4-hex-random}, e.g.20260309T141500Z-a1b2.
The timestamp prefix gives natural sort order; the random suffix prevents collisions.

## Follow List

The follow list is stored as a plain JSON file (unencrypted, since the key
envelopes already reveal follows):

GET https://{domain}/satellite/follows/index.json

{


"follows"
:

[
"bob.example.com"
,

"carol.example.com"
]

}

## Feed Aggregation

The client builds a feed by:

1. Reading the user’s follow list
2. For each followed user, resolving their repo path
3. For each followed user, decrypting their posts (using the key envelope
the followed user published for this user)
4. Merging all posts, sorted bycreated_atdescending

## Replies

A reply is a post withreply_toandreply_to_authorset.
Replies are grouped as flat threads under the original post — nested replies
(replying to a reply) are not supported; you can only reply to top-level posts.

Threads are positioned in the timeline by the original post’screated_at;
replies within a thread are sorted by their owncreated_atascending.

If the original post is inaccessible (e.g. the viewer doesn’t follow the
author), the reply is hidden entirely. A user only sees replies from people
they follow — this is the spam prevention mechanism.

## Publishing

The client publishes posts by:

1. Creating a new post with a unique ID
2. Encrypting the post JSON with the content key
3. Pushing the encrypted post asposts/{id}.json.encto user’s static site (e.g. via the GitHub Contents API)
4. Updatingposts/index.jsonto include the new post ID

Any secrets needed for publishing (e.g. GitHub token)
 is encrypted inkeys/_self.json(seeSelf Key).

## Static Site Structure

{domain}/satellite/
 satproto.json # Discovery + profile + public key
 posts/
 index.json # Post ID list (plaintext, newest first)
 {id}.json.enc # Individually encrypted post files
 follows/
 index.json # Follow list (unencrypted)
 keys/
 _self.json # Sealed box: content key + credentials (owner only)
 {domain}.json # Sealed box: content key for follower

## FAQ

Is this just RSS + PGP?

Yes!

Is this justAT Protocolbut no firehose?

Yes!

Does this scale?

No! Neither does friendship.

Does the “s” also stand for “slow” and “shitty”?

Absolutely!

Wait so I can self-host this?

Yes, you’ll need to enableCORS.

1. Of course, if you use a service to host your website, the server will have your (encrypted) data.↩
2. How do you ask a friend to follow? Idk, text them. Or just ask them in person. You’re friends, right?↩

 This site is open source.
Improve this page
.
