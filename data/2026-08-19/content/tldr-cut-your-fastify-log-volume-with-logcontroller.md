---
title: Cut your Fastify log volume with logController
url: https://backend.cafe/million-log-lines-a-month
site_name: tldr
content_file: tldr-cut-your-fastify-log-volume-with-logcontroller
fetched_at: '2026-08-19T11:23:00.087954'
original_url: https://backend.cafe/million-log-lines-a-month
date: '2026-08-19'
published_date: '2026-08-13T17:57:11.775Z'
description: A Fastify health check can produce over a million useless log lines a month. Here is how to silence, reshape or sample every log line Fastify writes
tags:
- tldr
---

## Command Palette

Search for a command to run...

M
Manuel Spigolon

I'm Manuel and I work at NearForm as a Full Remote Software Developer from 🇮🇹 Italy.
I'm one of the Fastify maintainers since 2019. Contributing to Open Source Software teaches me something new every day. You should join this extraordinary world.

Part of series
Fastify

A few days ago I reviewed aFastify pull requestthat added a new route option,requestLogLevel.
The motivation was one every backend developer recognizes: your orchestrator calls/healthevery 5 seconds, which is 17.280 requests a day, and Fastify logs two lines for each one.
That ismore than 1.000.000 log lines a month, and every single one of them says that everything is fine. You are storing them, indexing them, and paying for them.

It is a real problem. But that pull request did not need to touch Fastify's core, because Fastify already ships two ways to solve it.
The author had not spotted either one, and honestly that is fair: one of them is a plugin trick that is easy to forget, and the other is a fairly recent addition.

NoteThelogControlleroption is available sinceFastify v5.10.0, no alpha or release candidate needed.

## The quick way: a silenced plugin

Before writing any class, here is the two-line answer to the health check problem.

Everyregistercall in Fastify creates anencapsulated context, and each context gets its own child logger.
ThelogLeveloption sets the level of that child logger, andsilentdrops everything:

import Fastify from 'fastify'

const app = Fastify({ logger: { level: 'info' } })

// Everything registered inside this plugin gets a child logger set to
// `silent`, so Fastify's automatic request logs are dropped for these routes.
app.register(async function healthChecks (app) {
 app.get('/health', async () => ({ status: 'ok' }))
 app.get('/ready', async () => ({ status: 'ok' }))
}, { logLevel: 'silent' })

// Outside that plugin, the default `info` level is untouched.
app.get('/orders', async (request) => {
 request.log.info('loading orders')
 return { orders: [] }
})

// `inject` runs a full request through the whole lifecycle, logs included,
// without opening a port.
await app.inject('/health')
await app.inject('/ready')
await app.inject('/orders')
await app.close()

Running it prints three lines, and all three come from/orders:

{"level":30,"reqId":"req-3","req":{"method":"GET","url":"/orders"},"msg":"incoming request"}
{"level":30,"reqId":"req-3","msg":"loading orders"}
{"level":30,"reqId":"req-3","res":{"statusCode":200},"responseTime":0.12,"msg":"request completed"}

Two calls to/healthand/ready, zero log lines. If muting is all you need, stop here 🎉.

Notice that I am not starting a real server:injectruns the complete request lifecycle in memory, so the logs are exactly the ones you would get in production. It is also how you can assert on your logs in a test.

The catch is thatsilentis all or nothing. You lose the handler's own log lines too, and you cannot say "keep the failures". For that, we need the other tool.

## Every Fastify log line, in one place

Fastify does not only log the incoming and completed request. It also logs the errors caught by the default error handler, the 404s, the stream failures that happen after the headers are sent, the serializer failures, and the 503 it returns while shutting down.

Historically, changing any of those meant asking for a new top-level option:disableRequestLoggingto mute a couple of them,requestIdLogLabelto rename one property, and a queue of pull requests asking for one more knob each.
Both of those options are now deprecated as top-level Fastify options, and they will be removed infastify@6: you pass them to the controller instead.

PR #6580took a different route: put a layer between what Fastify wants to log and what you want to log.
That layer is theLogControllerclass, and it is exported fromfastify:

import Fastify, { LogController } from 'fastify'

Everyautomatic log line Fastify emits is a method on this class:

Method

Emits

incomingRequest

incoming request
, at 
info

requestCompleted

request completed
 at 
info
, or 
request errored
 at 
error

defaultErrorLog

the error handled by the default error handler: 
error
 for 5xx, 
info
 for 4xx

routeNotFound

Route GET:/nope not found
, at 
info

streamError

a stream failure after the headers were sent

writeHeadError

a 
writeHead
 failure during error handling

serializerError

a response serialization failure

serviceUnavailable

the 503 emitted while the server is closing

isLogDisabled

not a log line: the gate every other method checks

You subclass it, you override only the methods you care about, and every method you leave alone keeps its default behaviour.
Then you hand the instance to Fastify:

const app = Fastify({
 logger: { level: 'info' },
 logController: new MyLogController()
})

That is the whole API. The full method signatures, the constructor options and the exact defaults are documented in thelogControllersection of the Fastify docs, which is worth a read before you override anything.

Now let's build three things with it:

* a health check that stays quiet while every other route keeps logging
* a single access log line, carrying exactly the fields your dashboard wants
* a sampler that logs one successful request out of ten, and every failure

## Silence one route, keep the rest

This is the use case from the pull request, done without patching Fastify: I want the health check's automatic logs atdebugso aninfologger drops them, while the rest of the application stays atinfo.

The two methods that emit the automatic request logs areincomingRequestandrequestCompleted, so those are the two I override:

import Fastify, { LogController } from 'fastify'

class LevelPerRoute extends LogController {
 // Read the level from the route definition, falling back to Fastify's
 // default of `info` when the route does not set one.
 levelFor (request) {
 return request.routeOptions?.config?.requestLogLevel ?? 'info'
 }

 incomingRequest (request, reply) {
 // Overriding a method means the default `disableRequestLogging` check is
 // gone, so call it yourself to keep that option working.
 if (this.isLogDisabled(request)) return
 // Same payload as the default line, only the level is dynamic.
 request.log[this.levelFor(request)]({ req: request }, 'incoming request')
 }

 requestCompleted (error, request, reply) {
 if (this.isLogDisabled(request)) return
 if (error) {
 // A health check that starts failing is exactly what you want to see,
 // so failures stay at `error` whatever the route asked for.
 reply.log.error({ res: reply, err: error, responseTime: reply.elapsedTime }, 'request errored')
 return
 }
 reply.log[this.levelFor(request)]({ res: reply, responseTime: reply.elapsedTime }, 'request completed')
 }
}

ThatisLogDisabledcall deserves the comment I gave it. When you override a method you takefullcontrol of it: the base class no longer applies its own gate for you.

Where doesrequestLogLevelcome from? It is just a property I invented, read from the route'sconfigobject, which Fastify exposes onrequest.routeOptions.config:

const app = Fastify({
 logger: { level: 'info' },
 logController: new LevelPerRoute()
})

// `config` is free-form: anything you put here is readable from the request.
// The automatic logs of this route are emitted at `debug`, and the `info`
// logger drops them.
app.get('/health', { config: { requestLogLevel: 'debug' } }, async () => ({ status: 'ok' }))

// No `config`, so `levelFor` falls back to `info` and this route logs normally.
app.get('/orders', async (request) => {
 request.log.info('loading orders')
 return { orders: [] }
})

await app.inject('/health')
await app.inject('/orders')
await app.close()

The output is the same three/orderslines as before:

{"level":30,"reqId":"req-2","req":{"method":"GET","url":"/orders"},"msg":"incoming request"}
{"level":30,"reqId":"req-2","msg":"loading orders"}
{"level":30,"reqId":"req-2","res":{"statusCode":200},"responseTime":0.20,"msg":"request completed"}

Same result as the silenced plugin, but now the difference matters: the handler's ownrequest.log.infostill works everywhere, failures still get logged, and flipping the application logger todebugbrings the health checks back for as long as you need them. You demoted Fastify's automatic logs without gagging your own.

## Two lines become one

Two lines per request is a strange default once you are shipping logs to a paid service. Theincoming requestline only tells you that a request started, and therequest completedline does not repeat the method and the URL, so neither is useful on its own.

Let's collapse them into one line, shaped the way our dashboards want it:

class AccessLog extends LogController {
 // An empty override is how you drop a log line entirely.
 incomingRequest () {}

 requestCompleted (error, request, reply) {
 reply.log.info({
 method: request.method,
 url: request.url,
 // The route *pattern*, so /orders/42 and /orders/43 group together
 // under /orders/:id instead of exploding your cardinality.
 route: request.routeOptions.url,
 status: reply.statusCode,
 // elapsedTime is a float in milliseconds: round it before shipping.
 ms: Math.round(reply.elapsedTime),
 // Any request property can become a log field, no `onRequest` hook needed.
 tenant: request.headers['x-tenant-id'],
 // `undefined` keys are skipped by the serializer, so successful
 // requests do not carry an empty `err`.
 err: error ?? undefined
 }, 'access')
 }
}

Then a request with that header, throughinject:

const app = Fastify({
 logger: { level: 'info' },
 logController: new AccessLog()
})

app.get('/orders/:id', async (request) => ({ id: request.params.id }))

await app.inject({ url: '/orders/42', headers: { 'x-tenant-id': 'acme' } })
await app.close()

One request, one line, every field you asked for:

{"level":30,"reqId":"req-1","method":"GET","url":"/orders/42","route":"/orders/:id","status":200,"ms":2,"tenant":"acme","msg":"access"}

## Log 1 request out of 10, and every single failure

Here is my favourite one, because it is the kind of thing that usually needs a dedicated plugin.

On a busy service, successful requests are repetitive: if one in ten is enough to see the shape of your traffic, logging the other nine is money spent on nothing. Failures are the opposite, you want every single one.

The controller is a plain class instance, which means it can hold state across requests:

class SampledLog extends LogController {
 constructor (options = {}) {
 // Forward the options to the base class so `disableRequestLogging` and
 // `requestIdLogLabel` keep working alongside my own settings.
 super(options)
 this.sampleRate = options.sampleRate ?? 10
 this.counter = 0
 }

 incomingRequest () {}

 requestCompleted (error, request, reply) {
 const failed = Boolean(error) || reply.statusCode >= 500
 this.counter++

 // Keep one successful request out of `sampleRate`, and never drop a failure.
 if (!failed && this.counter % this.sampleRate !== 0) {
 return
 }

 reply.log.info({
 url: request.url,
 status: reply.statusCode,
 ms: Math.round(reply.elapsedTime),
 sampled: !failed, // so you know this line represents `sampleRate` requests
 err: error ?? undefined
 }, 'access')
 }
}

Seven successful calls and one failing one, with a sample rate of 5:

const app = Fastify({
 logger: { level: 'info' },
 logController: new SampledLog({ sampleRate: 5 })
})

app.get('/ping', async () => ({ pong: true }))
app.get('/boom', async () => { throw new Error('kaboom') })

for (let i = 0; i < 7; i++) {
 await app.inject('/ping')
}
await app.inject('/boom')
await app.close()

The output:

{"level":30,"reqId":"req-5","url":"/ping","status":200,"ms":0,"sampled":true,"msg":"access"}
{"level":50,"reqId":"req-8","req":{"method":"GET","url":"/boom"},"res":{"statusCode":500},"err":{"type":"Error","message":"kaboom","stack":"..."},"msg":"kaboom"}
{"level":30,"reqId":"req-8","url":"/boom","status":500,"ms":0,"sampled":false,"msg":"access"}

Seven successful requests, one access line. The failure gets through immediately.

Did you spot the middle line, the one with the stack trace? It is not mine.
That isdefaultErrorLog, adifferentmethod of the controller, the one Fastify's default error handler uses. I never overrode it, so it kept its default shape. If you want your error lines to match your access lines, that is the method to override too, and the table above tells you which method owns every other line you might be surprised by.

## Trade-offs

ThelogControlleris a single instance for the whole server, it is not encapsulated per plugin likelogLevelis. So per-route behaviour has to be derived from the request, as in the/healthexample above, and not from where the route was registered. The two techniques compose nicely, though: a silenced plugin for the routes you never want to hear from, a controller for everything that needs judgement.

These methods also sit on the hot path of every single request. Keep them cheap: read a property, pick a level, log. This is not the place for anawaitor a JSON round trip.

And if what you actually need is to change the log level of analready runningapplication, that is a different problem, and I wrote about it in"Unlock the Power of Runtime Log Level Control".

## Summary

Fastify gives you two levels of control over the logs it writes on your behalf:

* register(plugin, { logLevel: 'silent' })mutes an entire encapsulated context. Two lines of code, no logs at all, including your own
* logControllertakes an instance of aLogControllersubclass, where every automatic log line is a method you may override. Override the ones you care about, leave the rest to their defaults

With the second one you can change the level of a line, rewrite its payload, merge two lines into one, or drop a line entirely with an empty method body. Two things to remember while doing it: callthis.isLogDisabled(request)yourself, because overriding removes that gate, and callsuper(options)if you accept your own constructor options.

So next time you catch yourself wishing for a new Fastify logging option, check whether a five-line subclass gets you there first. That was the whole point of building this layer.

All the runnable examples live in thebonus/log-controllerdirectory of this repository.

If you enjoyed this article, you might like"Accelerating Server-Side Development with Fastify".
Comment, share and follow me onX/Twitter!

#
fastify
#
logging
390
 views

## Comments

Join the discussion

No comments yet.Be the first to comment.

## Fastify

Part 
16
 of 
16

This series will take a deep dive into the Fastify world, its paradigms, and its ecosystem. We intend it to be a companion to the upcoming Fastify book written by us and published by Packt.

Start from the beginning

### Fastify Error Handlers

Understand how Fastify manage your application errors

## More from this blog

Mar 16, 2026
·
4 min read
·
134
Jan 18, 2026
·
7 min read
·
209
Aug 7, 2025
·
12 min read
·
416
May 30, 2025
·
7 min read
·
303
B

Backend Cafe

38posts