---
title: 'GitHub - fastapi/fastapi: FastAPI framework, high performance, easy to learn, fast to code, ready for production · GitHub'
url: https://github.com/fastapi/fastapi
site_name: github
content_file: github-github-fastapifastapi-fastapi-framework-high-perfo
fetched_at: '2026-10-22T16:04:26.970564'
original_url: https://github.com/fastapi/fastapi
author: fastapi
description: FastAPI framework, high performance, easy to learn, fast to code, ready for production - fastapi/fastapi
---

master
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

7,933 Commits
7,933 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
docs
docs
 
 
docs_src
docs_src
 
 
fastapi
fastapi
 
 
scripts
scripts
 
 
tests
tests
 
 
.gitignore
.gitignore
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
.python-version
.python-version
 
 
CITATION.cff
CITATION.cff
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
pyproject.toml
pyproject.toml
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

FastAPI framework, high performance, easy to learn, fast to code, ready for production

Documentation:https://fastapi.tiangolo.com

Source Code:https://github.com/fastapi/fastapi

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python based on standard Python type hints.

The key features are:

* Fast: Very high performance, on par withNodeJSandGo(thanks to Starlette and Pydantic).One of the fastest Python frameworks available.
* Fast to code: Increase the speed to develop features by about 200% to 300%. *
* Fewer bugs: Reduce about 40% of human (developer) induced errors. *
* Intuitive: Great editor support. Completion everywhere. Less time debugging.
* Easy: Designed to be easy to use and learn. Less time reading docs.
* Short: Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.
* Robust: Get production-ready code. With automatic interactive documentation.
* Standards-based: Based on (and fully compatible with) the open standards for APIs:OpenAPI(previously known as Swagger) andJSON Schema.

* estimation based on tests conducted by an internal development team, building production applications.

## Sponsors

### Keystone Sponsor

### Gold Sponsors

### Silver Sponsors

Other sponsors

## Opinions

"[...] I'm usingFastAPIa ton these days. [...] I'm actually planning to use it for all of my team'sML services at Microsoft. Some of them are getting integrated into the coreWindowsproduct and someOfficeproducts."

Kabir Khan - 
Microsoft
 
(ref)

"We adopted theFastAPIlibrary to spawn aRESTserver that can be queried to obtainpredictions. [for Ludwig]"

Piero Molino, Yaroslav Dudin, and Sai Sumanth Miryala - 
Uber
 
(ref)

"Netflixis pleased to announce the open-source release of ourcrisis managementorchestration framework:Dispatch! [built withFastAPI]"

Kevin Glisson, Marc Vilanova, Forest Monsen - 
Netflix
 
(ref)

"If anyone is looking to build a production Python API, I would highly recommendFastAPI. It isbeautifully designed,simple to useandhighly scalable, it has become akey componentin our API first development strategy and is driving many automations and services such as our Virtual TAC Engineer."

Deon Pillsbury - 
Cisco
 
(ref)

## FastAPI mini documentary

There's aFastAPI mini documentaryreleased at the end of 2025, you can watch it online:

## Typer, the FastAPI of CLIs

If you are building a CLI app to be used in the terminal instead of a web API, check outTyper.

Typeris FastAPI's little sibling. And it's intended to be theFastAPI of CLIs. ⌨️ 🚀

## Requirements

FastAPI stands on the shoulders of giants:

* Starlettefor the web parts.
* Pydanticfor the data parts.

## Installation

First,installuv, and then add FastAPI to your project:

$ 
uv add 
"
fastapi[standard]
"

---> 100%

Note: Make sure you put"fastapi[standard]"in quotes to ensure it works in all terminals.

If you prefer to usepip, installfastapi[standard]inside a virtual environment. See theinstallation guidefor the alternative steps.

## Example

### Create it

Create a filemain.pywith:

from
 
fastapi
 
import
 
FastAPI

app
 
=
 
FastAPI
()

@
app
.
get
(
"/"
)

def
 
read_root
():
 
return
 {
"Hello"
: 
"World"
}

@
app
.
get
(
"/items/{item_id}"
)

def
 
read_item
(
item_id
: 
int
, 
q
: 
str
 
|
 
None
 
=
 
None
):
 
return
 {
"item_id"
: 
item_id
, 
"q"
: 
q
}

Or use 
async def
...

If your code usesasync/await, useasync def:

from
 
fastapi
 
import
 
FastAPI

app
 
=
 
FastAPI
()

@
app
.
get
(
"/"
)

async
 
def
 
read_root
():
 
return
 {
"Hello"
: 
"World"
}

@
app
.
get
(
"/items/{item_id}"
)

async
 
def
 
read_item
(
item_id
: 
int
, 
q
: 
str
 
|
 
None
 
=
 
None
):
 
return
 {
"item_id"
: 
item_id
, 
"q"
: 
q
}

Note:

If you don't know, check the"In a hurry?"section aboutasyncandawaitin the docs.

### Run it

Run the server with:

$ 
uv run fastapi dev

 ╭────────── FastAPI CLI - Development mode ───────────╮

 │ │

 │ Serving at: http://127.0.0.1:8000 │

 │ │

 │ API docs: http://127.0.0.1:8000/docs │

 │ │

 │ Running in development mode, for production use: │

 │ │

 │ fastapi run │

 │ │

 ╰─────────────────────────────────────────────────────╯

INFO: Will watch for changes in these directories: ['/home/user/code/awesomeapp']

INFO: Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)

INFO: Started reloader process [2248755] using WatchFiles

INFO: Started server process [2248757]

INFO: Waiting for application startup.

INFO: Application startup complete.

About the command 
fastapi dev
...

The commandfastapi devreads yourmain.pyfile automatically, detects theFastAPIapp in it, and starts a server usingUvicorn.

By default,fastapi devwill start with auto-reload enabled for local development.

You can read more about it in theFastAPI CLI docs.

### Check it

Open your browser athttp://127.0.0.1:8000/items/5?q=somequery.

You will see the JSON response as:

{
"item_id"
: 
5
, 
"q"
: 
"
somequery
"
}

You already created an API that:

* Receives HTTP requests in thepaths/and/items/{item_id}.
* BothpathstakeGEToperations(also known as HTTPmethods).
* Thepath/items/{item_id}has apath parameteritem_idthat should be anint.
* Thepath/items/{item_id}has an optionalstrquery parameterq.

### Interactive API docs

Now go tohttp://127.0.0.1:8000/docs.

You will see the automatic interactive API documentation (provided bySwagger UI):

### Alternative API docs

And now, go tohttp://127.0.0.1:8000/redoc.

You will see the alternative automatic documentation (provided byReDoc):

## Example upgrade

Now modify the filemain.pyto receive a body from aPUTrequest.

Declare the body using standard Python types, thanks to Pydantic.

from
 
fastapi
 
import
 
FastAPI

from
 
pydantic
 
import
 
BaseModel

app
 
=
 
FastAPI
()

class
 
Item
(
BaseModel
):
 
name
: 
str

 
price
: 
float

 
is_offer
: 
bool
 
|
 
None
 
=
 
None

@
app
.
get
(
"/"
)

def
 
read_root
():
 
return
 {
"Hello"
: 
"World"
}

@
app
.
get
(
"/items/{item_id}"
)

def
 
read_item
(
item_id
: 
int
, 
q
: 
str
 
|
 
None
 
=
 
None
):
 
return
 {
"item_id"
: 
item_id
, 
"q"
: 
q
}

@
app
.
put
(
"/items/{item_id}"
)

def
 
update_item
(
item_id
: 
int
, 
item
: 
Item
):
 
return
 {
"item_name"
: 
item
.
name
, 
"item_id"
: 
item_id
}

Thefastapi devserver should reload automatically.

### Interactive API docs upgrade

Now go tohttp://127.0.0.1:8000/docs.

* The interactive API documentation will be automatically updated, including the new body:

* Click on the button "Try it out", it allows you to fill the parameters and directly interact with the API:

* Then click on the "Execute" button, the user interface will communicate with your API, send the parameters, get the results and show them on the screen:

### Alternative API docs upgrade

And now, go tohttp://127.0.0.1:8000/redoc.

* The alternative documentation will also reflect the new query parameter and body:

### Recap

In summary, you declareoncethe types of parameters, body, etc. as function parameters.

You do that with standard modern Python types.

You don't have to learn a new syntax, the methods or classes of a specific library, etc.

Just standardPython.

For example, for anint:

item_id
: 
int

or for a more complexItemmodel:

item
: 
Item

...and with that single declaration you get:

* Editor support, including:Completion.Type checks.
* Completion.
* Type checks.
* Validation of data:Automatic and clear errors when the data is invalid.Validation even for deeply nested JSON objects.
* Automatic and clear errors when the data is invalid.
* Validation even for deeply nested JSON objects.
* Conversion of input data: coming from the network to Python data and types. Reading from:JSON.Path parameters.Query parameters.Cookies.Headers.Forms.Files.
* JSON.
* Path parameters.
* Query parameters.
* Cookies.
* Headers.
* Forms.
* Files.
* Conversion of output data: converting from Python data and types to network data (as JSON):Convert Python types (str,int,float,bool,list, etc).datetimeobjects.UUIDobjects.Database models....and many more.
* Convert Python types (str,int,float,bool,list, etc).
* datetimeobjects.
* UUIDobjects.
* Database models.
* ...and many more.
* Automatic interactive API documentation, including 2 alternative user interfaces:Swagger UI.ReDoc.
* Swagger UI.
* ReDoc.

Coming back to the previous code example,FastAPIwill:

* Validate that there is anitem_idin the path forGETandPUTrequests.
* Validate that theitem_idis of typeintforGETandPUTrequests.If it is not, the client will see a useful, clear error.
* If it is not, the client will see a useful, clear error.
* Check if there is an optional query parameter namedq(as inhttp://127.0.0.1:8000/items/foo?q=somequery) forGETrequests.As theqparameter is declared with= None, it is optional.Without theNoneit would be required (as is the body in the case withPUT).
* As theqparameter is declared with= None, it is optional.
* Without theNoneit would be required (as is the body in the case withPUT).
* ForPUTrequests to/items/{item_id}, read the body as JSON:Check that it has a required attributenamethat should be astr.Check that it has a required attributepricethat has to be afloat.Check that it has an optional attributeis_offer, that should be abool, if present.All this would also work for deeply nested JSON objects.
* Check that it has a required attributenamethat should be astr.
* Check that it has a required attributepricethat has to be afloat.
* Check that it has an optional attributeis_offer, that should be abool, if present.
* All this would also work for deeply nested JSON objects.
* Convert from and to JSON automatically.
* Document everything with OpenAPI, that can be used by:Interactive documentation systems.Automatic client code generation systems, for many languages.
* Interactive documentation systems.
* Automatic client code generation systems, for many languages.
* Provide 2 interactive documentation web interfaces directly.

We just scratched the surface, but you already get the idea of how it all works.

Try changing the line with:

 
return
 {
"item_name"
: 
item
.
name
, 
"item_id"
: 
item_id
}

...from:

 ... 
"item_name"
: 
item
.
name
 ...

...to:

 ... 
"item_price"
: 
item
.
price
 ...

...and see how your editor will auto-complete the attributes and know their types:

For a more complete example including more features, see theTutorial - User Guide.

Spoiler alert: the tutorial - user guide includes:

* Declaration ofparametersfrom other different places such as:headers,cookies,form fieldsandfiles.
* How to setvalidation constraintssuch asmaximum_lengthorregex.
* A very powerful and easy to useDependency Injectionsystem.
* Security and authentication, including support forOAuth2withJWT tokensandHTTP Basicauth.
* More advanced (but equally easy) techniques for declaringdeeply nested JSON models(thanks to Pydantic).
* GraphQLintegration withStrawberryand other libraries.
* Many extra features (thanks to Starlette) such as:WebSocketsextremely easy tests based on HTTPX andpytestCORSCookie Sessions...and more.
* WebSockets
* extremely easy tests based on HTTPX andpytest
* CORS
* Cookie Sessions
* ...and more.

### Deploy your app (optional)

You can optionally deploy your FastAPI app toFastAPI Cloudwith a single command. 🚀

$ 
uv run fastapi deploy

Deploying to FastAPI Cloud...

✅ Deployment successful!

🐔 Ready the chicken! Your app is ready at https://myapp.fastapicloud.dev

The CLI will automatically detect your FastAPI application and deploy it to the cloud. If you are not logged in, your browser will open to complete the authentication process.

That's it! Now you can access your app at that URL. ✨

#### About FastAPI Cloud

FastAPI Cloudis built by the same author and team behindFastAPI.

It streamlines the process ofbuilding,deploying, andaccessingan API with minimal effort.

It brings the samedeveloper experienceof building apps with FastAPI todeployingthem to the cloud. 🎉

FastAPI Cloud is the primary sponsor and funding provider for theFastAPI and friendsopen source projects. ✨

#### Deploy to other cloud providers

FastAPI is open source and based on standards. You can deploy FastAPI apps to any cloud provider you choose.

Follow your cloud provider's guides to deploy FastAPI apps with them. 🤓

## Performance

Independent TechEmpower benchmarks showFastAPIapplications running under Uvicorn asone of the fastest Python frameworks available, only below Starlette and Uvicorn themselves (used internally by FastAPI). (*)

To understand more about it, see the sectionBenchmarks.

## Dependencies

FastAPI depends on Pydantic and Starlette.

### standardDependencies

When you install FastAPI withuv add "fastapi[standard]"it comes with thestandardgroup of optional dependencies:

Used by Pydantic:

* email-validator- for email validation.

Used by Starlette:

* httpx2(orhttpx) - Used by theTestClient.
* jinja2- Required if you want to use the default template configuration.
* python-multipart- Required if you want to support form "parsing", withrequest.form().

Used by FastAPI:

* uvicorn- for the server that loads and serves your application. This includesuvicorn[standard], which includes some dependencies (e.g.uvloop) needed for high performance serving.
* fastapi-cli[standard]- to provide thefastapicommand.This includesfastapi-cloud-cli, which allows you to deploy your FastAPI application toFastAPI Cloud.
* This includesfastapi-cloud-cli, which allows you to deploy your FastAPI application toFastAPI Cloud.

### WithoutstandardDependencies

If you don't want to include thestandardoptional dependencies, you can install withuv add fastapiinstead ofuv add "fastapi[standard]".

### Withoutfastapi-cloud-cli

If you want to install FastAPI with the standard dependencies but without thefastapi-cloud-cli, you can install withuv add "fastapi[standard-no-fastapi-cloud-cli]".

### Additional Optional Dependencies

There are some additional dependencies you might want to install.

Additional optional Pydantic dependencies:

* pydantic-settings- for settings management.
* pydantic-extra-types- for extra types to be used with Pydantic.

Additional optional FastAPI dependencies:

* orjson- Required if you want to useORJSONResponse.
* ujson- Required if you want to useUJSONResponse.

## License

This project is licensed under the terms of the MIT license.