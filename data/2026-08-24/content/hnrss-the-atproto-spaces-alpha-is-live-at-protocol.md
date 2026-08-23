---
title: The Atproto Spaces Alpha is Live - AT Protocol
url: https://atproto.com/blog/atproto-spaces-alpha
site_name: hnrss
content_file: hnrss-the-atproto-spaces-alpha-is-live-at-protocol
fetched_at: '2026-08-24T07:46:55.974823'
original_url: https://atproto.com/blog/atproto-spaces-alpha
date: '2026-08-20'
description: Atproto Spaces, formerly known as “the permissioned data protocol,” is a new extension to atproto that enables non-public data. The alpha is now officially open. Here’s how to develop with it and what to expect as we work towards the full release.
tags:
- hackernews
- hnrss
---

# The Atproto Spaces Alpha is Live

Atproto Spaces, formerly known as “the permissioned data protocol,” is a new extension to atproto that enables non-public data. The alpha is now officially open. Here’s how to develop with it and what to expect as we work towards the full release.
August 20, 2026
By
 
Daniel Holmgren

The biggest update to atproto since it first launched is available as an alpha that you can develop on, starting right now!

This project has been a long time coming, as evidenced by the many names it’s had (firstprivate data, thenpermissioned data, brieflybuckets, and nowatproto spaces). Fromearly chatter on the forum, tothe first development diaryback in February, to thefull proposal, the design of the protocol has evolved through the feedback, contributions, and discussion of the ecosystem. This is a big undertaking, not just for the Blueksy team but for the entire Atmosphere.

Recall that, by design, all data stored on the protocol today is public — every post, every follow, every like,every block. All of this data is stored ona distributed network of serversanyone can host that gets collated andrebroadcast by a global firehoseanyone can tap into. This makes it possible to build high-scale applications likeBlueskyandTangledon a network that’s locked open.

There are, of course, features and entire products that rely on data that isn’t public. Settings, private bookmarks, forums ranging from dozens to millions of members, and subscription-only publishing apps all require a data model that isn’t fully public.

Spaces, a new protocol primitive, provide a way to store and sync non-public data while retaining the advantages of atproto like portable identity, interoperable/remixable data, and permissionless participation.

Today, we’re making the alpha available with running code, published SDKs, a sample app, and even a hosted PDS you can create an account on and develop against. This is truly an alpha. There will be breaking changes, and you absolutely should not run production code against it.

## What is a space?

You can think of an atproto space as a miniature atproto network that can be gated so that only certain people and applications are able to access the data published in it. It may sound a little “heavy-duty” to say each space is a mini-atproto, but spaces are actually very lightweight and low overhead. A space can have a single record in it with minimal overhead or scale up to a billion records.

Apart from the space itself, things should feel familiar. Users haveDIDs. Usershost their data in their repositories. Records are JSON and defined byLexicons.Applications sync reposand build views of the data.

Access to a space is controlled by a space authority, which is just a DID like any other account (and in some cases actuallyisyour account!). The space authority determines which other DIDs are allowed to access the space. Records live in per-space permissioned repos on the author’s PDS.

It’s important to remember that spaces give youaccess controlnotconfidentiality. The data in a space is readable by any user or application with access to that space, it’s not encrypted.

Spaces are a very flexible primitive, and the range of uses is deliberately broad. The smallest spaces will contain exactly one member and are useful for storing data like settings, drafts, bookmarks and other private data that an app might want to store. Spaces work for gated content as well, such as a publisher that wants to distribute a subscription-only publication. Where spaces really shine, and in some sense what they were designed for, is establishing a shared social context. In this capacity, the largest spaces will be communities that may grow to millions of participants.

The sync protocol for space data is significantly lighter-weight and provides facilities for real-time sync. This is because, unlike the public broadcast protocol, there is no concept of a relay for data stored in a space. For public data, the relay helps provide applications access to all of the data across the network. However for spaces, it’s often not desirable to rebroadcast content. Applications will sync space data directly from PDS hosts.

## A hosted PDS for experimenting

If you want to test out the protocol without running any infrastructure, you’re in luck! We’re hosting one for you and will keep it up to date with the latest changes.

Head over to yourBPS accountfor an invite code and a link to the alpha PDS.

This is a shared sandbox and we intend to keep it usable. If you cause moderation problems, engage in unproductive abuse of the network, or otherwise try to use the PDS for purposes other than experimenting with spaces, you will be permanently banned from the alpha.

You should also expect the data stored in the PDS is neither permanent nor stable. The data model will change, we may even delete everything without warning. The PDS as a whole will be deleted after the alpha.

We plan to update the hosted PDS and SDKs on Thursdays. We’ll post changes to the announcements thread on atmosphere.community, please subscribe.

## Running a spaces-capable PDS

If you want to run your own PDS, we’ll maintain a tagged Docker image atghcr.io/bluesky-social/atproto:pds-spaces-alphawith support for spaces. This image is compatible with thereference PDS distributionand does not require any new configuration.

THIS IS ALPHA SOFTWARE DO NOT USE IT IN PRODUCTION. Breaking changes will happen and database schemas may change without clean migrations. We strongly recommend that you do not migrate your real accounts to this version. Do not expect that you’ll even be able to cleanly upgrade between versions.

That said,doplease use the new PDS with test data. Explore spaces and the kinds of applications you can build with them. Report bugs, let us know if you were expecting something to work one way and it turns out to work differently.

We’ve already seen a few ecosystem projects that have begun to implement the proposed spec:

* ZDS, a PDS written in the Zig programming language
* atproto-crates PDS, a Rust PDS
* rsky PDS, another Rust PDS maintained by Blacksky
* HappyView, an AppView framework

Real protocols have many interoperating implementations, and it’s been amazing to see the ecosystem lead the way on this.

## Example app and alpha SDK

There’s an example app running athttps://bulletin.my. This app lets you host a bulletin board (as a space!) that your mutuals can leave sticky notes on. Only your followers can see your board. The code is availablehttps://github.com/bluesky-social/bulletin. Give it a run locally, or fork it and remix it into something new! If you have your own PDS implementation, try logging in and seeing if everything works as expected.

To support this, we released the TypeScript@atprotopackages as alpha snapshot versions. These can be installed with thealphatag. Check out the bulletin repo to see them in action.

## The proposal and the code

If you want to dive deeper into the protocol, the latest version of the protocol specification can be found in theproposals repo. If you’re working on your own implementation of atproto spaces, this is the thing to collaborate around. We’ll keep the proposal up to date with the current reference implementation. If you find ambiguities or places where the implementation and proposal diverge, please open an issue.

The reference implementation can be found on theatproto spacesbranch of the atproto repo. This branch is being actively developed and may temporarily diverge from the packages and PDS that are published.

## Remember, this is an alpha

As has already been mentioned several times, expect changes as we continue to develop the code. Specifically, this means:

* The code has not undergone careful security review.Do not upload sensitive information. Not your own, and especially not anyone else’s.
* We are not running backups, and we may do destructive data migrations.Do not upload content you are not willing to lose. There is no recovery path and we will not be able to make one for you.
* The alpha PDS goes away at the end of the alpha.Accounts on it are not accounts you should encourage anyone to depend on. Do not point non-developer users at it.
* The protocol design, SDKs, and database schema are not final.Anything you build will likely need revising.

## How to start testing atproto spaces

We will continue to iterate and build tooling throughout the fall, with a goal of launching later this year. Followthe announcement post in the Atmosphere Community forumfor updates on new builds, which we plan to drop on Thursdays.

Feel free to start building apps with test, non-production data against the hosted PDS. Or host your own PDS—either the reference implementation or one of the community-managed ones. Run the sample app or build your own.Report issueswhere you find them.

We are excited about the entire new class of applications atproto spaces enables and for developers to get their hands on the code.

What is a space?
A hosted PDS for experimenting
Running a spaces-capable PDS
Example app and alpha SDK
The proposal and the code
Remember, this is an alpha
How to start testing atproto spaces
Discussion

## Discussion