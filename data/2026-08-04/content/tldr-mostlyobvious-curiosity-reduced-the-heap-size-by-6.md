---
title: mostlyobvio.us — Curiosity reduced the heap size by 60%
url: https://mostlyobvio.us/2026/07/curiosity-reduced-the-heap-size-by-60/
site_name: tldr
content_file: tldr-mostlyobvious-curiosity-reduced-the-heap-size-by-6
fetched_at: '2026-08-04T11:46:10.676797'
original_url: https://mostlyobvio.us/2026/07/curiosity-reduced-the-heap-size-by-60/
date: '2026-08-04'
description: Curiosity reduced the heap size by 60% (3 minute read)
tags:
- tldr
---

# Curiosity reduced the heap size by 60%

You may have noticed how agents get creative when they're parsing output of the tool run. They filter out the crap that hinders readability and makes the result of an action harder to understand. Just like we'd subconsciously do, pattern matching for the signal within the stream of noise.

I was working on new functionality when I noticed the agent filtering out a particular Ruby warning among the noise:

bundle exec rspec | rg -v "OpenTelemetry|export.*spans|redefining"

To be fair, I had seen this redefining warning before when running individual specs. It wasn't directly in scope of my task, but the repeated use of output filtering and followingThe Boy Scout Rulemandated at least a quick check. The kind of check agents are particularly good at:

aws-sdk-core-2.11.420/lib/aws-sdk-core/structure.rb:63: warning: redefining 'object_id' may cause serious problems

Diagnose it.

It wasn't long before it was all clear what was happening. The mix ofopentelemetry-instrumentation-aws_sdkandaws-sdk, in a slightly outdated version, was not quite compatible. The former was causing autoloading of entire AWS service implementations. Among them was aDataPipelineservice class that redefinedobject_id:

The app enables all OTel instrumentations viause_all(config/environment.rb:13), includingopentelemetry-instrumentation-aws_sdk. Its install block callsloaded_service_clients, which doesAws.const_geton every constant inAws.constants. Under the pinnedaws-sdkv2, every service is an autoload, so this force-loads all ~200 services at boot — includingDataPipeline, whose objectId shape member generates anobject_idStructaccessor and triggers Ruby's unconditional warning.

The application uses just a few services of the entire AWS catalog. It doesn't need all of them. Theaws-sdkgem by design ships all of them in one package, letting them be loaded lazily with autoload. As a side note — this gem has a newer version, which changed the design to modular "one gem, one capability". The version currently used in the project interacts with an API version that is still working but officially deprecated in 2020. By all means this dependency should have been taken care of earlier and it would not have caused such an issue in its latest release.

The fix wasn't particularly difficult and was well covered by unit tests ensuring it does not change installed instrumenters and that the warning output is gone.

OpenTelemetry
::
Instrumentation
::
AwsSdk
::
Instrumentation
.
prepend
(

 
Module
.
new
 
do

 
def
 
loaded_service_clients

 
::
Aws

 
.
constants

 
.
each_with_object
(

 
[]

 
)
 
do
 
|
c
,
 
constants
|

 
next
 
if
 
::
Aws
.
autoload?
(
c
)

 
m
 
=
 
::
Aws
.
const_get
(
c
)

 
unless
 
loaded_service?
(
c
,
 
m
)

 
next

 
end

 
begin

 
constants
 
<<
 
m
.
const_get
(

 
:Client

 
)

 
rescue
 
StandardError
 
=>
 
e

 
OpenTelemetry
.
logger
.
warn
(

 
"Constant could not be loaded: 
#{
e
}
"

 
)

 
end

 
end

 
end

 
end

)

OpenTelemetry
::
Instrumentation
::
AwsSdk
::
Instrumentation
.
prepend
(

 
Module
.
new
 
do

 
def
 
loaded_service_clients

 
::
Aws

 
.
constants

 
.
each_with_object
([])
 
do
 
|
c
,
 
constants
|

 
next
 
if
 
::
Aws
.
autoload?
(
c
)

 
m
 
=
 
::
Aws
.
const_get
(
c
)

 
next
 
unless
 
loaded_service?
(
c
,
 
m
)

 
begin

 
constants
 
<<
 
m
.
const_get
(
:Client
)

 
rescue
 
StandardError
 
=>
 
e

 
OpenTelemetry
.
logger
.
warn
(
"Constant could not be loaded: 
#{
e
}
"
)

 
end

 
end

 
end

 
end

)

I askedThe Clankerto run a one-off benchmark measuring the impact of this change. I think the result speaks for itself:

aws-sdk-core files 259 -> 2
services loaded 220 -> 0
classes in VM 33,265 -> 13,137 (-60%)
heap (memsize) 163.8MB -> 67.1MB (-59%)
hot boot (min/3) 2.69s -> 1.72s (-36%)

The point I'm trying to make here is that it has never been cheaper to continuously improve the codebase we interact with daily. It doesn't require loops, sophisticated heuristics or setting aside big chunks of time — just a bit of curiosity. Iterate in small steps, leave the place slightly better. For your future self, the agents, and the team.

So stay curious!

And don't listen to theNie interesuj się, bo kociej mordy dostanieszadvice.