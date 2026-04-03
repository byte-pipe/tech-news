---
title: New And Upcoming IRCv3 Features | Libera Chat
url: https://libera.chat/news/new-and-upcoming-features-3
date: 2026-02-13
site: lobsters
model: gemma3n:latest
summarized_at: 2026-02-13T06:02:48.979701
---

# New And Upcoming IRCv3 Features | Libera Chat

# New And Upcoming IRCv3 Features

This article from Libera.Chat announces several new and upcoming features for the IRCv3 protocol, highlighting their significance for the development of Libera.Chat.

## Message-tags
Libera.Chat now fully supports message tags, a core feature of IRCv3, enabling the transmission of tagged messages between servers. This was a prerequisite for several other new features.

### msgid
When a client requests message-tags, each received message will have a unique identifier, allowing unambiguous referencing. These IDs are not cryptographic signatures and cannot be used for message validation.

### server-time
Server-time is now processed based on the server the sender is connected to, significantly improving message order consistency across clients. This has the potential to impact games like duck hunt.

### Client Tags
Client tags allow clients to attach additional information to messages or send new types of messages without server understanding. Libera.Chat supports the `+typing` tag for typing notifications and is considering support for other tags like `+draft/channel-context`, `+draft/react`, `+draft/reply`, and `+draft/unreact`.

## Batch
The batch feature allows servers to group logical messages, primarily useful for handling netsplits and netjoins. When enabled, QUIT and JOIN events due to server-to-server connection changes will be grouped into a batch, enabling more nuanced handling of these events by clients.

## Invite-notify
Libera.Chat now supports invite-notify. If a client requests this capability, it will be informed when someone is invited to a channel they are in. This helps channel operators manage channel mode +gon.

## Echo-messagefor services
A bug fix has been implemented to ensure Libera.Chat correctly receives echo messages when sending to services like NickServ and alis.

## What’s Next?
Libera.Chat staff are considering implementing several IRCv3 extensions in the near future:

* **`+draft/multilinbatch`**: Allows clients to group messages into a single long message.
* **`labeled-response`**: Facilitates associating automatic server replies with specific requests.
* **Bot mode**: Aims to provide a standardized way for bots to operate, though integration challenges remain.
* **`setname`**: Would allow users to set a name beyond their realname, but requires careful implementation to prevent misuse by bridges and address potential noise.



## References:
The article directs readers to their IRCv3 client support table for compatibility information.
