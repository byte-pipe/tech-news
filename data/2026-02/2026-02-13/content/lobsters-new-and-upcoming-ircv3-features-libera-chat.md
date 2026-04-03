---
title: New And Upcoming IRCv3 Features | Libera Chat
url: https://libera.chat/news/new-and-upcoming-features-3
site_name: lobsters
content_file: lobsters-new-and-upcoming-ircv3-features-libera-chat
fetched_at: '2026-02-13T06:00:36.976706'
original_url: https://libera.chat/news/new-and-upcoming-features-3
author: She
date: '2026-02-13'
published_date: '2026-02-11T00:00:00+00:00'
description: Adding message-tags, batch, msgid, and invite-notify.
tags: culture, release
---

# New And Upcoming IRCv3 Features

11th February 2026by She

It’s been a while since we’ve had new features to announce,
but this set of features is particularly special, as it brings Libera.Chat
closer to the forefront of IRC development.
To check whether your IRC client supports these features,
refer either to your client’s documentation or tothis IRCv3 client support table.

## message-tags

Solanum, the IRC server software Libera.Chat uses, has supported tagged
messages going to/from clients for years, but only recently gained the
ability to send messages containing tags between servers.
This is one of the core features of IRCv3, and we’re excited to be able to
support it properly. In particular, not having this feature was a blocker
for the following features we now also support:

### msgid

If your client requests themessage-tagscapability,
each message you receive will be tagged with aunique identifier.
This makes it possible for clients to unambiguously reference messages.
Note that Libera.Chat’s message IDs are not cryptographic signatures of the
messages they are attached to. As a result, they cannot be used on their own
to validate messages.

### server-time

Libera.Chat supportedserver-timebefore today, but it was
of limited use because the timestamp would reflect when the message was sent
to you by the server you’re connected to. Now, the timestamp will reflect
when the message was processed by the server its sender is connected to.
Aside from greatly improving message order consistency between clients,
this has the potential to revolutionise the popular IRC game of duck hunt
by reducing the advantage provided by the long-standing
“connect to the same server as the duck hunt bot” meta.

### Client Tags

Client tags are a way for clients to attach additional information to
messages or even send all-new kinds of messages without the server having
to understand them. They can be thought of as an IRCv3 successor to CTCP.

Libera.Chat allows client tags on a case-by-case basis and
validates their values to prevent deviation from their specifications.
Currently, Libera.Chat supports just the+typingtag
which allows clients to send optional typing notifications. We are also
considering allowing the following tags when client support for them improves:

* +draft/channel-context
* +draft/react
* +draft/reply
* +draft/unreact

Please let us know if there are any other client tags that you would like
Libera.Chat to support.

## batch

batchallows servers to create logical groups of messages. Right now,
the main use for this feature is nicer handling of netsplits and netjoins.
If your client requests this capability,QUITs andJOINs that
happen as a result of changes in server-to-server connections will be grouped
into a batch. This makes it possible to differentiate between
massJOINs due to a server reconnecting and other forms of massJOINs,
which in turn makes it possible for your client to handle a netjoin the same
way it handles a netsplit.

## invite-notify

It’sfinallyhere. If your client requests theinvite-notifycapability, you will be informed whenever someone is/invited to a channel
you’re in. If you’re a channel operator, this means you can keep channel mode+gon and not worry that invites are being abused behind your back.

## echo-messagefor services

This is more of a bugfix than a feature.
If your client requestsecho-message, it will now correctly receive
echo messages when sending messages to services (e.g. NickServ, alis).

## What’s Next?

While we don’t want to promise anything that isn’t nearly ready for
deployment, here are a few notable IRCv3 extensions that staff have
at least some interest in implementing, in descending order of likelihood to
be supported by Libera.Chat in the near future:

Thedraft/multilinebatch type makes it possible for clients
to logically group messages together into a single long (possibly multi-line)
message. The module that implements it requires further testing, but support
for this could potentially be deployed soon.

labeled-responsemakes it much easier for clients to
always associate particular automatic replies from the server with
particular requests. Eventual support for this extension was a big part of the
motivation for addingbatchsupport now. However, there’s still more
development work that needs to be done before we can support this feature.

Bot modewould be nice to have in principle, but there remain
some challenges to resolve around integration with services and getting bots
to use it. Further internal staff discussion is needed.

setnamewould also be nice to have, but we would need to develop
a way to prevent one-to-one bridges from using the command. Otherwise, users
would be able to override realnames set by bridge, which should include
information about the remote user’s accountper our guidelines.
Additionally, the fallback behaviour has the potential of being quite noisy,
and several notable clients (e.g. ZNC as a client) do not support it.
Once client support improves, staff may consider adding support for it once
we figure out how best to implement the restrictions on bridges.
