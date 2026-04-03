---
title: Litestar is worth a look
url: https://www.b-list.org/weblog/2025/aug/06/litestar/
site_name: hackernews
fetched_at: '2025-08-07T19:08:32.827574'
original_url: https://www.b-list.org/weblog/2025/aug/06/litestar/
author: James Bennett
date: '2025-08-07'
description: A few years ago at work, I had a project which offered an opportunity to look at the new generation …
---

# Litestar is worth a look

Published on:August 6, 2025Categories:Django,Python

A few years ago at work, I had a project which offered an opportunity to look at the new generation of async-first, type-hint-driven Python web frameworks. For reasons which aren’t particularly relevant today, on that project I ended up choosingLitestar, which is the one thatdoesn’thave a ravenous all-consuming hype machine surrounding it. And I’m very glad I did, because today I’m more convinced than ever it was the right choice, and for the last 18 months or so every new project I’ve started at my day job has been built with Litestar.

But even if you’re someone who does Python web apps for a living, and even if you’re someone who builds asynchronous type-hint-driven web apps, you might not be familiar with this absolute gem of the Python web ecosystem, and today I want to remedy that.

## A taste

Here’s the traditional single-file-app demo:

from

litestar

import

Litestar
,

get

@get
(
"/greet"
)

async

def

greet
(
name
:

str
)

->

str
:


return

f
"Hi,
{
name
}
!"

app

=

Litestar
([
greet
])

You save this asapp.py, run withlitestar runor hand it directly to theASGIserver of your choice, and it launches a web application. You go to/greet?name=Boband it replies “Hi, Bob!”. Leave out thenameparameter and it responds with anHTTP400 telling you thenameparameter is required.

So what. Big deal. The FastAPI Evangelism Strike Force will be along soon to bury you under rocket-ship emoji while explaining that FastAPI does the same thing but a million times better. And if you’re a Java person used to Spring, or a .NETperson used toASP.NETMVC, well, there’s nothing here that’s new to you; you’ve had this style of annotation/signature-driven framework for years (and in fact one thing I like about Litestar is how often it reminds me of the good parts of those frameworks). And did anyone tell you FastAPI does this, too! 🚀🚀🚀🚀🚀🚀🚀🚀🚀

But there are a lot of things that make Litestar stand out to me in the Python world. I’m going to pick out three to talk about today, and one of them is hiding in plain sight in that simple example application.

What’s in a name?

You might see older material referring to Litestar as “Starlite”, which was its original name.

Starletteis a toolkit for doing async Python web development, which can be used standalone or as a component in a more complex library or framework. FastAPI still uses Starlette under the hood, for example. And Litestar originally was built on Starlette too, and was named “Starlite”, presumably in recognition of that. Over time, though, it dropped the Starlette dependency in favor of its own implementations for that functionality, and people on social media complained that the “Starlite” name was confusing, especially since Starlettewas no longer being used. So the project which had been “Starlite” was renamed to Litestar for version 2.0, released in 2023, and has had that name ever since.

### Scaling (the other kind)

It’s a bit unfortunate that the term “scaling” is almost always assumed to mean handling larger and larger quantities of traffic, because that’s only one axis on which any given piece of of technology can “scale” (and, I’d argue, possibly the least important one). The type of scaling I want to talk about here is scaling of a codebase: how does something (in this case, a web framework) help or hinder you as you deal with different amounts of code?

Django, for example, has a reputation for not scaling “down” all that well. Youcando it if you really want to, and every so often someone will come up with a new demo of doing a Django project in a single Python file, but it’s just not something that comes naturally to Django. Quite the opposite: if you work through the official beginner Django tutorial and do things the “Django way”, you’ll have around a dozen files laid out in a specific structure of directories and subdirectories before you’ve written a single meaningful line of your own code.

But “micro” frameworks have often had the opposite problem: they’re great at starting out with a tiny single-file application, and then get painful as your codebase grows and needs to spread out (single-file Django approaches have the same problem: you have to do a lot of work to get a “micro-Django” working, and then you have toundoall that work as soon as the code grows large enough to be worth splitting across multiple files).

Let’s look at an example. Here’s a FastAPI equivalent of the basic Litestar application I showed above:

from

fastapi

import

FastAPI

app

=

FastAPI
()

@app
.
get
(
"/greet"
)

async

def

greet
(
name
:

str
)

->

str
:


return

f
"Hello,
{
name
}
!"

Notice that theget()decorator here is attached to the application object. This is a common pattern (Flask/Quart do the same thing, for example, and Starlette used to but has deprecated its entire decorator-based routing system), but it creates a problem once you have multiple files. You need to import the main application object into the other files in order to decorate the routes, but you need to import the other files into your “main” application file to make sure the route registrations are visible from there, and now you have a circular import, and that doesn’t work.

The general solution these frameworks offer is some sort of alternative sub-application object which can act as a per-file route registry that’s safe to import into the file where your application object is defined. FastAPI calls this object an “APIrouter”; Flask/Quart call it a “blueprint”. Either way, it’s a necessary construct for those frameworks because their route decorators are always bound to some parent object, either the application object in a single-file app or an “APIrouter”/“blueprint”/etc. object in a multi-file app.

That solves the circular-import problem, but creates a new issue: the whiz-bang quickstart demos of “micro” frameworks generally register all the example routes on the application object in a single file in order to keep everything as simple and flashy as possible, but now in order to build a real application (which will almost never stay in a single file) you’ll need to use a different mechanism, or start out following the demo and then switch later on. You also have toknowabout that different mechanism; in one framework’s documentation that I looked at, you can (at the time I’m writing this post) apparently get 40 pages into the user guide before encountering the section on how to register routes in a multi-file app 😖😖😖.

Litestar avoids this entire mess by having the route decorators be standalone functions, not bound to a parent application or application-like object. This may seem like a small thing to focus on, but if you’ve spent time with popular Python microframeworks you’ve probably had to deal with the transition from single- to multi-file applications.

More importantly, this small change in approach frees up Litestar’s documentation to introduce route-grouping constructs early on and to present them as part ofa coherent layered architecture/configuration conceptrather than as an escape hatch for avoiding circular imports. Which is great, because Litestar’s layered architecture is one of its best features: its grouping constructs, and their ability to share configuration, offer an elegant way to compose functionality. For example, a common pattern I use when writing a set ofCRUDendpoints looks like this:

from

litestar

import

Router

from

litestar.di

import

Provide

# Imagine some CRUD routes for widgets defined here...

_write_widget_router

=

Router
(


guards
=
[
some_auth_function
],


route_handlers
=
[


create_widget
,


delete_widget
,


update_widget
,


]

)

widget_router

=

Router
(


dependencies
=
{
"widget_dependency"
:

Provide
(
some_widget_dependency
)},


path
=
"/widgets"
,


route_handlers
=
[


get_widget
,


get_widget_list
,


_write_widget_router
,


]

)

This provides a single “public”Routerinstance with all the widget routes, all of which have access to the same core dependencies, but with the data-modifying routes also having auth applied. That composability is extremely powerful, and is less obvious if the “router” has to be introduced initially as a way to solve circular-import problems.

Litestar’s approach also means it’s easy to do things like register a single route multiple times, each with different configuration. Which enables use cases like:

* Different authentication/authorization schemes for each registration. For example, a data-editing route might be written once, and registered once under a router which appliesAPIkey auth for machine-to-machine requests, then registered again under a router which uses session auth for interaction by a human user.
* Different sets of dependencies for each registration. For example, a route which queries and returns a list of widgets might just declare that it accepts an argument of typeWidgetRepository, and leave it up to the router configuration to decide whether to dependency-inject one that sees all widgets, or perhaps only a subset, or only those which are active, etc.

If you know what you’re doing, you can emulate some of this in the FastAPI/Flask style of bound route registration, but the techniques you’ll end up using for that feel to me like fighting against the framework, which is something I usually want to avoid.

## Not to be too Pydantic

Pydanticis a popular package for defining schema objects which perform validation and serialization/deserialization, driven by Python type annotations, and one major use case for this is the input/output schemas of web applications. FastAPI appears to use Pydantic exclusively, which comes with both upsides and downsides. Pydantic is very useful and very powerful, of course, but it also means FastAPI is somewhat limited by what Pydantic can support: mostly, this is Pydantic’s own classes, andthe Python standard library’sdataclasses.

One crucial limitation is an inability to derive validation/serialization behavior directly fromSQLAlchemyORMclasses, even though they both support a very similar type-annotation-based declaration format. Which means that to use SQLAlchemy with a Pydantic-only framework (and SQLAlchemy is basicallythestandard database toolkit andORMfor Python), you either have to write out the shape of your data multiple times—once for SQLAlchemy, and then at least one more time (possibly more than one time) for Pydantic—or turn to a third-party package to help bridge the gap. FastAPI’s author worked around this by writinga newDBtoolkit which combines SQLAlchemy and Pydantic, and pushing it in FastAPI’s documentation.

Litestar, meanwhile,supportsPydantic, but is nottightly coupled toPydantic, which gives a bit more flexibility. By default Litestar lets you define input/output schemas using Pydantic models,dataclasses, ormsgspec; ships with plugins to enable the use ofattrsand of SQLAlchemy models; andprovides a protocol for writing your own serialization pluginsto extend support to other kinds of objects.

That’s very convenient already, but the convenience is amplified by Litestar’ssystem for automatically deriving data-transfer objectsfrom data-access or domain objects. Suppose, for example, that we have the following SQLAlchemy model class:

from

sqlalchemy.orm

import

DeclarativeBase
,

Mapped
,

mapped_column

Base

=

DeclarativeBase
()

class

Widget
(
Base
):


__tablename__

=

"widget"


id
:

Mapped
[
int
]

=

mapped_column
(
primary_key
=
True
)


internal_notes
:

Mapped
[
str
]


sku
:

Mapped
[
str
]

=

mapped_column
(
unique
=
True
)


name
:

Mapped
[
str
]


price_cents
:

Mapped
[
int
]

In a Pydantic-only world, we’d need to write multiple Pydantic models representing different use cases:

* A “read” schema for use inHTTPresponses, which would probably not include theinternal_notesfield and probably also notid(sinceskuis more likely to be the public identifier)
* A “write” schema for creating widgets, which would excludeidsince that likely is auto-generated on insert
* Another “write” schema for updating widgets, setting all fields optional to allow partial update

As well as possibly more schemas like an admin-view “read” schema that does include the internal fields, etc. Even if you get clever and use inheritance to share field definitions among all these Pydantic classes, you still will write out the full set of fields for widgets at least twice, and the second time it will be fragmented across multiple Pydantic classes, creating the risk of making a change to theORMmodel and forgetting to update all the corresponding field definitions in the Pydantic models.

Litestar’s approach is a significant improvement on this. For example, here’s how to use Litestar’sDTOhelpers to define the “read” schema:

from

litestar.dto

import

DTOConfig

from

litestar.plugins.sqlalchemy

import

SQLAlchemyDTO

class

ReadWidget
(
SQLAlchemyDTO
[
Widget
]):


config

=

DTOConfig
(
exclude
=
{
"id"
,

"internal_notes"
})

This will give you aDTOclass containing all the fields of theWidgetORMmodelexceptthe two explicitly excluded, and will derive that set of fields, and the correct data types, from introspectingWidget. It will also automatically handle conversion to and from instances ofWidgetwhen you specify it as the input or returnDTOtype of a route. Similarly, it’s possible to declare a list of fields to include, or to re-map field names for public consumption, or to declare aDTOwhich makes fields optional for partial updates. This means there’s only one canonical definition of the fields—on the original class, which might be a SQLAlchemyORMmodel, might be adataclass, etc.—and it doesn’t have to be repeated in the DTOs because the DTOs will always derive their field definitions directly from the source class you point them at.

Of course, there are going to be cases where your DTOs are sufficiently different from your DAOs and domain objects that this isn’t a big help, but my own experience is that “theDTOis a subset of theDAO’s fields” is extremely common in real-world applications, so Litestar’s approach really pays off in both reduced boilerplate and reduced errors from manual “transcription” of fields between different class definitions.

## Alchemical architecture

I wasn’t exaggerating earlier when I said that SQLAlchemy isthedatabase toolkit andORMfor Python. While there are others out there, the only one I’m aware of that sees anything close to SQLAlchemy’s usage is the DjangoORM, and only because it’s built into and tightly integrated with Django. So if you’re going to be writing a database-backed web application in Python, and you’re not doing Django, you are almost certainly going to be using SQLAlchemy.

And Litestar makes that easy. While officially remaining agnostic as to whether you even have a persistence layer, it still includes good integrations for SQLAlchemy: the serialization plugin mentioned earlier allows the direct use of SQLAlchemyORMclasses as input and output schemas; theDTOhelpers can derive subsets and remappings of fields from SQLAlchemyORMclasses; and Litestar also ships witha plugin that manages a SQLAlchemy engine and per-requestORMsession for you, as well asa single SQLAlchemy mega-plugincombining all the SQLAlchemy plugins’ functionality.

So it’s already pretty convenient to use SQLAlchemy in Litestar applications. But there’s more! The Litestar team also maintainsthe excellent Advanced Alchemy librarywhich provides a bunch of useful features on top of SQLAlchemy. While Advanced Alchemy is framework-agnostic, Litestar’s SQLAlchemy plugin makes use of it and re-exports much of its functionality, giving you access to it automatically, and it does include Litestar-specific helpers for registering certain utility classes with Litestar’s dependency injection.

Advanced Alchemy provides a lot of quality-of-life improvements for SQLAlchemy, including a variety of base classes and mixins and data types doing useful things like database-agnostic big-integer primary keys, automatic create/update timestamps,UUID-keyed models, a properUTCtimestamp type, and aJSONtype which chooses the best column type for your database. There are also command-line helpers for database management (including creating and working withAlembic migrations), database dumping and seeding to/fromJSON, and a lot more.

But the place where Advanced Alchemy really shines is in providinga generic repository implementation(both sync and async flavors) on top of SQLAlchemy models, along witha service-layer abstractionand helpers to integrate them into Litestar’s dependency injection system.

Here’s a basic example using theWidgetclass from above:

from

litestar.plugins.sqlalchemy

import

repository

class

WidgetRepository
(
repository
.
SQLAlchemyAsyncRepository
[
Widget
]):


model_type

=

Widget

WidgetRepositorywill have all the methods you’d expect—list(),get_one(),add(),delete(), etc.—automatically derived from theWidgetmodel. And let me just say that having repository implementations automatically derived from any SQLAlchemy model, with not just basicCRUDoperations but also things like paginated fetches, is amassiveproductivity boost compared to just using vanilla SQLAlchemy. It’s maybe not quite on the level of Django’s generic views, but it’s a big step in that direction, and you probably could produce something like Django’s generic views with Litestar and Advanced Alchemy if you wanted to (perhaps one day, in my copious free time, I’ll even make an attempt at it).

I know it may seem strange to hear me saying this, since a few years ago I went on record as being stronglyagainstthese sorts of abstractions—specifically service layers—in Django. And I still think you absolutely should not try to retrofit repository or service-layer abstractions onto Django! They’re not the native patterns of Django’s architecture, and instead I think you should stick towhat I recommended back then, which is to leverage Django’s own architecture, especially its “manager” abstraction, rather than trying to force abstractions onto it that don’t fit.

I also still think there are a lot of bad use cases for repositories and service layers that people should avoid, but that’s a digression which should probably become its own post, so I’ll just say for now that I think it’s fine to use repositories and service layersas an organizing principlewhen you’re using a less-structured framework which doesn’t express strong opinions about how you should lay out your code. And that’s exactly what I do when working with Litestar.

## A lightweight star of Python

There are plenty of other features and conveniences in Litestar, many of which I use daily. Its auth system, supporting bothsimple guard functionsandmiddlewaresfor attaching identity and complex authn/authz logic to requests. Its“stores” framework, which makes caching and similar tasks convenient. Itslogging integrationswhich support both the Python standard library’sloggingmodule and popular third-party tools likestructlog. Its built-in support fortransforming errors to standard “problem details” structures. Its built-in support forrecording and exporting metrics in standard Prometheus or OpenTelemetry formats. Itshtmx support.

You can do this stuff in other microframeworks, but it typically involves a lot of tracking down of third-party add-ons and/or writing your own glue code to integrate things. Litestar manages to keep the “microframework” feel when starting a new project while also having all these nice bits optionally available with the framework itself when and if you decide you want them, and that’s nothing to sneeze at. That’s what I was getting at earlier when I said it reminds me of the things I like in certain frameworks from other languages. Litestar doesn’t feel, to me, like it’s trying to be a replacement for any pre-existing Python web framework. It’s not trying to be the next Django or the next Flask or whatever; instead, it feels to me like a Pythonic take on the good parts of something like Spring Boot (and the way I like to set it up, doing things like usingsvcsbehind the scenes as a service locator to feed things to both Litestar’s andpytest’sdependency injection, makes it feel even more that way).

I could go on for a lot longer listing things I like about Litestar, and probably wind up way too far into my own subjective preferences, but hopefully I’ve given you enough of a realistic taste of what it offers that, next time you’re about to build a Python web app, you might decide to reach for 💡⭐ to carry you to the moon 🚀🚀🚀.
