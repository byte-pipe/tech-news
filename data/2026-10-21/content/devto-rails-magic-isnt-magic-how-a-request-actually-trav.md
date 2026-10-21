---
title: '"Rails Magic" Isn''t Magic. How a Request Actually Travels Through Rails. - DEV Community'
url: https://dev.to/smtahosin/rails-magic-isnt-magic-how-a-request-actually-travels-through-rails-5gc5
site_name: devto
content_file: devto-rails-magic-isnt-magic-how-a-request-actually-trav
fetched_at: '2026-10-21T15:51:35.438714'
original_url: https://dev.to/smtahosin/rails-magic-isnt-magic-how-a-request-actually-travels-through-rails-5gc5
author: S M Tahosin
date: '2026-10-19'
description: A visual, 10-minute deep dive into how Ruby on Rails actually runs under the hood. From Rack middlewares and Zeitwerk autoloading to ActiveRecord schema reflection and the view_assigns bridge. Tagged with rails, ruby, webdev, architecture.
tags: '#rails, #ruby, #webdev, #architecture'
---

Ask any developer who has worked with modern web frameworks what they think of Ruby on Rails, and you will almost certainly hear the same word within thirty seconds:

"Magic."

You run a generator, and entire database tables spring to life. You write an empty model class, and it immediately knows every column in your schema without a single property declaration. You define an instance variable inside a controller action, and it appears inside a separate view template as if object boundaries ceased to exist. You reference a class you have never required, and Ruby finds it instantly.

To newcomers, it feels like witchcraft. To skeptics, it feels like a dangerous black box that cannot be reasoned about or debugged when things go wrong.

Except there is no magic in Rails.

Every single convention in Rails is built out of plain Ruby metaprogramming, standard object-oriented design patterns, and an elegant pipeline architecture that has quietly powered some of the largest applications on the web for over twenty years.

When you peel back the syntactic sugar, Rails reveals itself not as an inscrutable black box, but as a masterpiece of systems architecture.

To truly master Rails and debug it with total confidence, you have to follow an HTTP request from the moment it hits your server socket, through the middleware onion, into the router, through the model reflection engine, and out through the view renderer.

Here is what is actually happening behind the curtain.

## The Request Onion: From Puma to ActionDispatch

Before Rails ever touches your code, your request must travel through what software architects call theRequest Onion.

At the outer edge sits your web server (typically Puma). Puma listens on a raw TCP socket, accepts an incoming HTTP request, parses the raw headers and body, and wraps that data into a plain Ruby hash known as theRack environment(env).

Puma then hands this hash to Rails using the universal contract of the Ruby web world:the Rack interface.

[HTTP Request] ──> Puma Web Server ──> call(env) ──> [Rack Middleware Stack] ──> [ActionDispatch Router]

Enter fullscreen mode

Exit fullscreen mode

A Rack application is disarmingly simple: it is any Ruby object that responds tocall(env)and returns a three-element array containing:

1. An integer HTTP status code (such as200).
2. A hash of HTTP response headers.
3. An enumerable body stream.

When Puma callsRails.application.call(env), the request does not jump straight into your controller. Instead, it cascades through a stack of more than twenty built-inRack Middlewares.

Each middleware wraps the next one like layers of an onion:

1. ActionDispatch::HostAuthorization: Guards against DNS rebinding attacks by verifying theHostheader against authorized hostnames.
2. ActionDispatch::SSL: Enforces HTTPS redirection and sets Strict-Transport-Security headers.
3. Rack::Sendfile: Offloads static file serving to reverse proxies like Nginx when appropriate.
4. ActionDispatch::CookiesandCookieStore: Decrypts the signed session cookie, verifying its HMAC signature to prevent tampering, and deserializes your session payload into memory.
5. ActionDispatch::ShowExceptions: Catches unhandled errors raised deeper in the application, translating them into friendly HTML error pages or JSON diagnostics.

Only after surviving this protective gauntlet does the request arrive atActionDispatch::Journey, the Rails routing engine.

Journey parses yourconfig/routes.rbfile on boot and compiles it into a deterministic routing tree. It matches the HTTP verb (GET) and path (/articles/42), extracts the parameters (id: "42"), determines thatArticlesController#showshould handle the request, and dispatches the call.

## The Mystery of Missing Columns: ActiveRecord Schema Reflection

Once inside the controller, you run your database query:

class
 
ArticlesController
 
<
 
ApplicationController

 
def
 
show

 
@article
 
=
 
Article
.
find
(
params
[
:id
])

 
end

end

Enter fullscreen mode

Exit fullscreen mode

Now consider your model file,app/models/article.rb:

class
 
Article
 
<
 
ApplicationRecord

end

Enter fullscreen mode

Exit fullscreen mode

Look closely at that class definition:there are no column declarations.

There is noattr_accessor :title. There is noproperty :body, String. There is no schema definition file inside your model directory.

Yet you can writearticle.title,article.body, andarticle.published?, and Ruby executes them flawlessly.

How does a pure Ruby object know the names and types of its attributes when you never declared them?

The answer lies inDynamic Schema Reflection.

When your Rails application boots, or the very first timeArticleis referenced in code, ActiveRecord does something clever:

1. Database Catalog Introspection:ActiveRecord connects to your database adapter and queries the database catalog (in PostgreSQL, it queriesinformation_schema.columns; in SQLite, it runsPRAGMA table_info(articles)).
2. Schema Ingestion:It retrieves the exact column names, data types, nullability constraints, and default values directly from the database engine itself.
3. Dynamic Module Generation:Instead of defining methods directly onArticle, ActiveRecord creates a hidden internal module calledGeneratedAttributeMethods.
4. Metaprogramming the Getters and Setters:For every column returned by the database catalog, ActiveRecord evaluates method definitions into this module:

# Conceptual representation of what ActiveRecord generates internally:

module
 
GeneratedAttributeMethods

 
def
 
title

 
_read_attribute
(
'title'
)

 
end

 
def
 
title
=
(
value
)

 
_write_attribute
(
'title'
,
 
value
)

 
end

 
def
 
title?

 
_query_attribute
(
'title'
)

 
end

end

Enter fullscreen mode

Exit fullscreen mode

1. Module Inclusion:ActiveRecord includesGeneratedAttributeMethodsintoArticle.

Because the methods live inside an included module rather than theArticleclass itself, you can easily overridedef titlein your own model, callsuper, and add custom formatting without breaking ActiveRecord's internal storage engine!

The database remains the single source of truth for your data model. Rails reflects that truth dynamically into Ruby's method tables, eliminating the need to synchronize manual class declarations with database migrations.

## Crossing the Object Boundary: How Controller State Reaches Views

Next comes one of the most baffling behaviors for programmers arriving from other languages:

# app/controllers/articles_controller.rb

class
 
ArticlesController
 
<
 
ApplicationController

 
def
 
show

 
@article
 
=
 
Article
.
find
(
params
[
:id
])

 
@comments
 
=
 
@article
.
comments

 
end

end

Enter fullscreen mode

Exit fullscreen mode

And in your view template:

<!-- app/views/articles/show.html.erb -->

<h1>
<%=
 
@article
.
title
 
%>
</h1>

<p>
<%=
 
@article
.
body
 
%>
</p>

Enter fullscreen mode

Exit fullscreen mode

In standard object-oriented programming, instance variables (@article,@comments) are strictly private to the specific object instance that created them. An instance ofArticlesControllercannot expose its private@variablesto an instance ofActionView::Base.

Controllers and views are entirely different classes instantiated at different points in time.

How does@articlecross the boundary between two completely separate objects?

The bridge is a method calledview_assigns.

When your controller action finishes running, Rails initiates the rendering sequence:

1. Extracting Instance State:The controller callsview_assigns. This method inspects all instance variables on the controller object, strips internal Rails variables (like@_responseand@_request), and converts the remaining user variables into a plain Ruby hash:

# What view_assigns returns:

{

 
"article"
 
=>
 
#<Article id: 42, title: "Rails Internals">,

 
"comments"
 
=>
 
[
#<Comment id: 1>, #<Comment id: 2>]

}

Enter fullscreen mode

Exit fullscreen mode

1. Instantiating the View Context:Rails instantiates a freshActionView::Baseobject responsible for rendering the template.
2. Metaprogramming the Handoff:Rails iterates through the assigns hash and injects each key and value directly into the new view instance using Ruby's reflection method:

assigns
.
each
 
do
 
|
key
,
 
value
|

 
view
.
instance_variable_set
(
"@
#{
key
}
"
,
 
value
)

end

Enter fullscreen mode

Exit fullscreen mode

1. Compiling the ERB Template:Rails takes your ERB template, compiles the HTML and embedded Ruby tags into a pure Ruby method, and executes that method in the context of the view instance.

Because the view instance now possesses identical@articleand@commentsinstance variables, your template reads them seamlessly.

What looked like boundary-defying magic was simply an automated dictionary handoff executed throughinstance_variable_set.

## Zeitwerk: Why You Never Writerequire

In standard Ruby, before you can use a class defined in another file, you must explicitly load it:

require_relative
 
"../services/payment_processor"

Enter fullscreen mode

Exit fullscreen mode

In Rails, you simply writePaymentProcessor.charge(user)anywhere in your codebase, and it works. You almost never writerequirestatements.

For many years, Rails accomplished this using a custom mechanism hooked into Ruby'sconst_missingcallback. Butconst_missingsuffered from notorious edge cases: circular dependency deadlocks, thread-safety hazards, and confusing load-order bugs.

Modern Rails solved this by adoptingZeitwerk, an autoloading engine written specifically for Ruby.

Zeitwerk enforces a clean convention:file paths must strictly mirror constant names.

* ConstantUsermaps toapp/models/user.rb.
* ConstantUsers::AccountNotifiermaps toapp/services/users/account_notifier.rb.

How does Zeitwerk handle this across different environments?

### In Development: Instant Reloading Without Restarts

In development, booting the server loads virtually zero application files into memory. When your code first encounters an unreferenced constant likeUser, Zeitwerk intercepts the lookup, inflects the name intoapp/models/user.rb, and requires the file on demand.

More importantly, Zeitwerk integrates with a file-system watcher. When you modify a file in your text editor, Zeitwerk unloads the matching constants from Ruby's memory space.

On your next browser reload, Rails re-evaluates the file freshly from disk. You get instant updates without restarting Puma or waiting for a compilation step.

### In Production: Eager Loading and Copy-on-Write

In production, on-demand autoloading is completely disabled.

Instead, during application boot, Zeitwerk executes aneager load. It crawls every directory insideapp/and loads every single class, module, and template into Ruby's memory space before Puma spawns its worker processes.

This delivers two vital production benefits:

1. Zero Runtime Disk I/O:Incoming user requests never spend CPU cycles looking up or requiring files from disk.
2. Copy-on-Write (CoW) Memory Optimization:Because all classes are allocated in the master process before Puma forks child workers, all worker processes share the exact same physical RAM pages. A Rails application with five worker processes consumes drastically less memory than five separate instances started independently.

## The Thread Highway: ActiveRecord Connection Pooling

When your application receives dozens of concurrent requests, how does Rails ensure that multiple threads do not corrupt your database connections?

Puma is a multi-threaded web server. Each Puma worker process runs a thread pool (typically 3 to 5 threads per worker). Each thread handles an independent HTTP request concurrently.

If two threads attempted to write raw SQL commands simultaneously across the same TCP connection to PostgreSQL, the protocol stream would interleave and crash the socket.

To manage this safely, ActiveRecord uses aConnection Pool.

The connection pool acts as a thread-safe leasing office:

1. Connection Checkout:When Thread 1 executesArticle.find(42), it asks theConnectionPoolfor a database connection.
2. Thread Affinity:The pool assigns an available connection to Thread 1 and associates that connection with the thread's local storage.
3. Query Execution:Thread 1 executes its SQL statements safely across its dedicated connection.
4. Connection Check-in:When the HTTP request finishes and the Rack response leaves the controller, an outer Rack middleware (ActiveRecord::Rack::ConnectionManagementor the executor hook) checks the connection back into the pool, making it available for other waiting threads.

### The Pool Size Equation

Understanding the connection pool prevents one of the most common production disasters in Rails:ActiveRecord::ConnectionTimeoutError.

Yourconfig/database.ymldefines the pool size:

production
:

 
adapter
:
 
postgresql

 
pool
:
 
<%= ENV.fetch("RAILS_MAX_THREADS") { 5 } %>

Enter fullscreen mode

Exit fullscreen mode

If Puma is configured to run 10 threads, but your database pool size is set to 5, the sixth concurrent thread will freeze, waiting up to 5 seconds for an active connection to become free before throwing a fatal timeout error.

Keeping your database pool size equal to or slightly greater than Puma'smax_threadsguarantees that every active worker thread can execute queries without contention.

## Guarding the Mass Assignment Door: Strong Parameters

One of the most consequential security innovations in Rails history isStrong Parameters.

In early versions of Rails, developers wrote:

# ❌ The old, dangerous way:

def
 
create

 
@user
 
=
 
User
.
create
(
params
[
:user
])

end

Enter fullscreen mode

Exit fullscreen mode

This created a critical vulnerability known as aMass Assignment Attack. A malicious user could send a crafted POST request including unintended attributes:

{

 
"user"
:
 
{

 
"name"
:
 
"Attacker"
,

 
"email"
:
 
"attacker@evil.com"
,

 
"admin"
:
 
true

 
}

}

Enter fullscreen mode

Exit fullscreen mode

Because ActiveRecord mapped all hash keys directly to database columns, the attacker could elevate themselves to an administrator simply by appending"admin": trueto the form payload.

Modern Rails prevents this by wrapping all incoming request parameters insideActionController::Parameters.

By default, anActionController::Parametersinstance is marked with an internal flag:permitted: false.

If you attempt to pass an unpermitted parameters object directly into an ActiveRecord write method likeUser.create(params[:user]), ActiveRecord intercepts the call and immediately raises anActiveModel::ForbiddenAttributesError.

To persist the data, you must explicitly declare an attribute whitelist:

private

def
 
user_params

 
params
.
require
(
:user
).
permit
(
:name
,
 
:email
)

end

Enter fullscreen mode

Exit fullscreen mode

The pipeline operates in two stages:

1. require(:user): Verifies that the:userkey exists in the payload, raisingActionController::ParameterMissing(which automatically renders a 400 Bad Request) if absent.
2. permit(:name, :email): Iterates across the keys, strips out unauthorized attributes (such as:adminor:account_balance), and returns a new Parameters instance markedpermitted: true.

Only sanitized, explicitly authorized data ever reaches your database layer.

## The Paradigm Shift: From Magic to Mastery

When developers complain about "Rails magic," they are usually reacting to the fact that Rails hides boilerplate code so effectively that the underlying mechanics become invisible.

Yet none of these behaviors are mysterious:

1. The Request Onionis a modular chain of Rack middleware wrappers following a universal Ruby interface.
2. ActiveRecord Schema Reflectionis dynamic database catalog introspection paired with runtime module inclusion.
3. The View Handoffis automated dictionary assignment viaview_assigns.
4. Zeitwerk Autoloadingis strict constant-to-path inflection optimized with production eager loading.
5. Connection Poolingis thread-safe connection leasing tailored to Puma's concurrency model.
6. Strong Parametersis strict parameter filtering protecting models from mass assignment exploits.

When you understand the machinery powering these conventions, Rails stops feeling like an unpredictable trick. It becomes what it was always designed to be: an exceptionally well-engineered, productive framework that lets you focus on building features without getting bogged down in low-level plumbing.

When you first started working with Rails, which of these "magical" behaviors felt the most puzzling? And what under-the-hood discovery made the biggest difference in how you write and debug your code?

References:

* Ruby on Rails Official Guides: Rails on Rack
* Ruby on Rails Official Guides: Autoloading and Reloading Constants (Zeitwerk)
* Ruby on Rails Official Guides: Action Controller Overview & Strong Parameters
* ActiveRecord Source Code: ConnectionPool Architecture
* Aaron Patterson: How ActiveRecord Finds Your Attributes

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse