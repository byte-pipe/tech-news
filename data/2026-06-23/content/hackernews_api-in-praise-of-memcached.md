---
title: In praise of memcached
url: https://jchri.st/blog/in-praise-of-memcached/
site_name: hackernews_api
content_file: hackernews_api-in-praise-of-memcached
fetched_at: '2026-06-23T12:04:23.135943'
original_url: https://jchri.st/blog/in-praise-of-memcached/
author: j03b
date: '2026-06-23'
tags:
- hackernews
- trending
---

# In praise of memcached

 2nd June 2026
 from 
jc's blog

If you happen to find yourself in a sysadmin position, or a position where you
just so happen to maintainsomeone’s
infrastructure, chances are that at
some point in time the topic “we need a cache” comes up.

You think for a moment and reach out for Redis, because you’re used to it, it’s
fully featured, and it works! You remember it being a good, solid cache, and you
wonder which new features recent releases have brought, and head to its
homepage:

Your agents aren’t failing. Their context is.

Inquiring agents want to know:

How can I use Redis Iris as a real-time context engine for AI apps?1

Right, so probably something with AI2. This is sort of understandable, because
Redis is a company that wants to make money.

Anyways, Redis homepage aside, you deploy it, and off you go - your trusty
cache. You hand the connection string to the people who asked for it, and off
you go.

## Few months later

After a while, it turns out thatcache.set("key", "value")is a really simple
abstraction, and definitely easier thanINSERT INTO table VALUES ('key', 'value'). People start treating theREmote DIctionary Serveras something
that’salwaysthere, something thatpersistsdata, something that isa
database.

You don’t know this. Your ops colleagues don’t know this. Therefore, your
alerting doesn’t know this either, because you assume that people treat thecacheas something volatile.

You find out that this has been going on when you happen to do something to
Redis. Maybe you upgrade it, maybe you move it to another node, maybe your cat
hits the eject button on your RAID0 server’s HDD tray.

The issue isn’t that Redis doesn’t have persistence, the issue is that usually,
Redis is brought into a stack as acache, and it is run with the assumption
that people treat it that way.

Usually, by the time you realize this, it is already too late, and Redis is too
intertwined in the app to really leave its place. Instead, you have the eternal
pleasure of maintaining it and monitoring it like a pet.

## Enter memcached

First off - what’s a memcached? Easy, askits website:

What is Memcached?

Free & open source, high-performance, distributed memory object caching
system, generic in nature, but intended for use in speeding up dynamic web
applications by alleviating database load.3

Wow, first sentence on the page, even with code examples. And look at those cute
little mascots at the top!

Memcached is also a cache, similar to Redis. Chances are that you’re using a
framework like Django,which supports pluggable
cachingand allows you to
switch between different caching backends.

Butwhy should you use memcachedwhen it has much less features than Redis?
Here are my reasons for why these days, I will always prefer memcached over
Redis:

* Dealing withmemcached downtimeis incredibly easy, because client
libraries generally ignore connection exceptions. For instance, a simplegetwill just return the default value (or none) if the server is down.
* Clusteringmemcached is wonderful, because memcached actually has no
clustering built-in. To “cluster” it, you configure the client library with
multiple URLs4, and the client will select the target instance based on
hashing the key. If a client-side call detects an instance as done,it
removes the node from the
hasher.
After a certain time, the client will automatically attempt to reconnect and
use the dead node.
* memcached “solves” the whole persistence issue, because it does not persist to
disk. It is therefore a perfect fit to just being scheduled as a stateless
workload wherever you desire it.

None of these things are impossible with Redis, it’s just that memcached’s
architecture in general more leans towards these directions, which makes it
much, much more straightforward from an operations point of view.

But because of memcached being such a relatively simple application (plus the
fact that you can run dozens instances of it with ~64 MB cache size and close to
no overhead), if I need a cache these days, I usually reach out to memcached.

That said, a lot of “database too slow” problems actually begin their life as
“query too slow” or “missing indices”, so be a kind person and help your
developers with optimizing their queries.

Also, if you’re curious about some of the decisions behind memcached, theblogcontains interesting posts, with one
published just in May:“How Long Does That Response Take… For
Real?”.

1. https://redis.io/, accessed 2026-06-02↩︎
2. That said,https://redis.iois probably not the best entrypoint for
engineers, that website seems geared to people making purchasing decisions.↩︎
3. https://memcached.org, accessed 2026-06-02↩︎
4. Bonus points for using a service discovery mechanism to automatically
generate this setting.↩︎

reply via email