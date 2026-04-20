---
title: 'Google Maps for Codebases: Paste a GitHub URL, Ask Anything - DEV Community'
url: https://dev.to/copilotkit/google-maps-for-codebases-paste-a-github-url-ask-anything-3hk8
site_name: devto
content_file: devto-google-maps-for-codebases-paste-a-github-url-ask-a
fetched_at: '2026-04-08T19:33:18.069567'
original_url: https://dev.to/copilotkit/google-maps-for-codebases-paste-a-github-url-ask-anything-3hk8
author: Anmol Baranwal
date: '2026-04-06'
description: Navigating a large codebase for the first time is painful. You clone the repo, realize there are 300... Tagged with javascript, opensource, tutorial, ai.
tags: '#javascript, #opensource, #tutorial, #ai'
---

Live dependency graphs and local LLM support

Navigating a large codebase for the first time is painful. You clone the repo, realize there are 300 files, and have no idea where anything lives.

You can ask an AI assistant, but it burns through context fast and you never know if it hallucinated a file path that does not even exist.

Codebase Navigatorsolves this. Paste a URL, ask anything in plain English, and watch a real dependency graph built from actual import statements appear in real time.

It is built usingCopilotKit,Zenflow, GitHub API andReact Flow. You can run it completely free usingOllamalocally.

In this blog, we will go through the architecture, the key patterns and how everything works end-to-end.

## What are we building?

Codebase Navigator lets you paste any public GitHub repo URL and ask questions about it in plain English. Instead of getting a wall of text back, you get four panels that all update at once.

Panel

What it does

Graph Canvas

Live dependency graph built from real import statements

Code Viewer

File content fetched live from GitHub, relevant lines highlighted

Repo Explorer

Full file tree, click any file to open it

Chat

Follow-up questions and plain English explanations

The graph morphs to show every relevant file connected by real imports, the code viewer opens the file, and the chat explains what each piece does. No context switching.

You can run it completely free using Ollama locally without any API key.

Here is the full request → response flow of what happens when you ask a question:

User types "how does auth work?"
 ↓
CopilotChat → POST /api/copilotkit
 ↓
LLM receives repo context (file paths, current selection, system rules)
 ↓
LLM calls analyzeRepository tool
 ↓
Tool fetches relevant files via /api/github/file
 ↓
Extracts import/require statements → resolves paths → builds dependency graph
 ↓
Zustand store updates
 ↓
All four panels re-render live: graph, file tree, code viewer, chat response

Enter fullscreen mode

Exit fullscreen mode

## Tech Stack & Tools

At a high level, this project is built by combining:

* Next.js 16- frontend and API routes
* CopilotKit- agent-UI state sync and chat interface. provides built-in hooks & components likeuseAgentContext,useFrontendTool,CopilotChat
* Zenflow- workflow tool that planned, tested and orchestrated the build
* React Flow&dagre- interactive dependency graphs with automatic layout
* Octokit- GitHub API proxy for fetching repo trees and file contents
* Zustand- shared state across all four panels
* Tailwind CSS- styling
* Ollama / OpenAI - local or cloud LLM backend switchable from the UI

The CopilotKit runtime is self-hosted inside a Next.js API route, which lets you plug into any OpenAI-compatible backend, including Ollama, for completely free local inference.

It connects your UI, agents, and tools into a single interaction loop.

 

### What is Zenflow?

Zenflowis an AI development tool that treats building software as a structured engineering process rather than just autocompleting code.

This project was planned, built, tested, reviewed and deployed using Zenflow (Zencoder's workflow engine) in a single session.

It ran a six-phase process from scratch:

* Architecture and spec
* Scaffolding and foundation
* Data layer (GitHub API integration)
* AI layer (CopilotKit actions and context)
* Visual layer (React Flow graphs)
* Final assembly and wiring

Each phase was verified with lint, type checks and tests before moving to the next. After the build, it performed a code review, found 14 issues and fixed 11 systematically:

* API keys exposed in headers → moved to httpOnly cookies
* Fake star-shaped graphs → replaced with real import-based dependency resolution
* Duplicate file-fetching logic → consolidated into a single cached utility

The.zenflow/folder in the repo contains the task plan, spec, and report files it generated along the way.

That's how we built it with Zenflow. Here's the architecture that came out of it.

## Architecture & Project Structure

The app is split into three layers: the browser handles all UI and AI tool logic, Next.js API routes act as a secure proxy to external services, and GitHub API, plus the LLM backend sits at the bottom. Nothing in the browser talks to GitHub or the LLM directly.

Below is a high-level overview of all the layers and how they are organized.

┌─────────────────────────────────────────────────────────┐
│ BROWSER │
│ │
│ ┌─────────┐ ┌──────────┐ ┌──────────┐ ┌────────┐ │
│ │ Chat │ │ Graph │ │ Code │ │ File │ │
│ │ Panel │ │ Canvas │ │ Viewer │ │ Tree │ │
│ └────┬────┘ └────┬─────┘ └────┬─────┘ └───┬────┘ │
│ └────────────┴─────────────┴────────────┘ │
│ │ │
│ ┌──────▼──────┐ │
│ │ Zustand │ ← shared state │
│ └──────┬──────┘ │
│ │ │
│ ┌───────────▼────────────┐ │
│ │ CopilotKit │ │
│ │ frontend tools │ │
│ │ analyzeRepository │ │
│ │ fetchFileContent │ │
│ │ highlightCode │ │
│ └───────────┬────────────┘ │
└──────────────────────────┼──────────────────────────────┘
 │
┌──────────────────────────▼──────────────────────────────┐
│ NEXT.JS API ROUTES │
│ │
│ /api/copilotkit /api/github/* /api/settings │
│ (LLM runtime) (proxy) (httpOnly cookie)│
└──────────┬────────────────┬─────────────────────────────┘
 │ │
 ┌─────▼─────┐ ┌──────▼──────┐
 │ Ollama │ │ GitHub API │
 │ / OpenAI │ │ (Octokit) │
 └───────────┘ └─────────────┘

Enter fullscreen mode

Exit fullscreen mode

Here is a simplified view of how the project is structured.

src/
├── app/api/
│ ├── copilotkit/route.ts → CopilotKit runtime endpoint
│ ├── github/
│ │ ├── tree/route.ts → fetch repo tree
│ │ ├── file/route.ts → fetch + base64-decode file
│ │ └── search/route.ts → code search
│ └── settings/route.ts → LLM config (httpOnly cookie)
├── components/
│ ├── panels/ → 5 UI panels (chat, graph, code, analysis, repo)
│ └── flow/ → custom React Flow node types
├── hooks/ → AI tool registration, agent context sync, repo loading
├── lib/ → import extraction, dagre layout, Octokit client
├── store/ → Zustand (AppState + SettingsState)
└── .zenflow/ → Zenflow task plan, spec and report

Enter fullscreen mode

Exit fullscreen mode

Let's get into how everything works behind the scenes. This will help you understand the key patterns.

## How everything works under the hood

Now that you have the big picture, let's go through each piece in detail.

A lot is happening under the surface, so we will break it down into ten parts, starting from when you first load a repo all the way to how state flows across the panels.

### 1. Loading a repository

When you paste a GitHub URL and click Explore,useRepository.loadRepository()fires (fromuseRepository.tshook).

It calls/api/github/treeon the server, which uses Octokit to:

* Parse the repo URL into{ owner, repo }
* Fetch the default branch
* Get the full recursive file tree from the GitHub Trees API
* Convert the flat array into a nestedTreeNodestructure

Here is what thesrc/api/github/tree/route.tsroute looks like:

export

async

function

GET
(
request
:

NextRequest
)

{


const

{

owner
,

repo

}

=

parseRepoUrl
(
repoUrl
);


const

resolvedBranch

=

branch

||

(
await

getDefaultBranch
(
owner
,

repo
));


const

tree

=

await

getRepoTree
(
owner
,

repo
,

resolvedBranch
);


return

NextResponse
.
json
({

owner
,

repo
,

branch
:

resolvedBranch
,

tree

});

}

Enter fullscreen mode

Exit fullscreen mode

That nested tree powers the sidebar file explorer and becomes the starting point for everything else.

All GitHub calls are proxied through Next.js API routes. The browser never talks to GitHub directly to keep tokens secure.

 

### 2. From architecture view to dependency graph

This is the visual moment that makes the app feel alive. The graph you see on load (the architecture view) and the graph you see after asking a question (the dependency graph) are two completely different things, built two different ways.

Both live insrc/lib/analyzer.ts-buildOverviewGraphfor the architecture view andbuildDependencyNodesfor the dependency graph.

When the repo loads,useRepository.tscallsbuildOverviewGraphright after the tree response comes back and pushes the result straight to the graph:

const

overview

=

buildOverviewGraph
(
data
.
tree
);

setVisualization
(
overview
.
nodes
,

overview
.
edges
,

"
architecture
"
);

Enter fullscreen mode

Exit fullscreen mode

buildOverviewGraphnever fetches any files. It just walks the tree structure and builds a folder map: root node at the top, top-level directories as children, one level of sub-folders below that:

export

function

buildOverviewGraph
(
tree
:

TreeNode
)

{


const

rootId

=

`node-
${
nodeId
++
}
`
;


nodes
.
push
({

id
:

rootId
,

type
:

"
module
"
,

label
:

tree
.
path

||

"
root
"

});


const

topDirs

=

(
tree
.
children

||

[]).
filter
((
c
)

=>

c
.
type

===

"
directory
"
);


for
(
const

dir

of

topDirs
)

{


const

fileCount

=

flattenTree
(
dir
).
length
;


nodes
.
push
({

id
,

label
:

`
${
dir
.
name
}
 (
${
fileCount
}
)`
,

type
:

categorizeDirType
(
dir
.
path
)

});


edges
.
push
({

source
:

rootId
,

target
:

id
,

type
:

"
flow
"

});


}

}

Enter fullscreen mode

Exit fullscreen mode

The edges here mean nothing beyond "this folder is inside that folder."

Once you ask a question,useCopilotActions.tsfetches the actual file content and callsbuildDependencyNodesinstead:

const

graph

=

buildDependencyNodes
(
fileData
);

setVisualization
(
graph
.
nodes
,

graph
.
edges
,

"
dependency
"
);

Enter fullscreen mode

Exit fullscreen mode

buildDependencyNodescreates one node per file and one edge per real import statement:

export

function

buildDependencyNodes
(
files
:

{

path
:

string
;

imports
:

string
[]

}[])

{


const

nodes

=

files
.
map
((
file
)

=>

({


id
:

file
.
path
,


type
:

"
file
"
,


label
:

file
.
path
.
split
(
"
/
"
).
pop
()

||

file
.
path
,


metadata
:

{

fullPath
:

file
.
path

},


}));


for
(
const

file

of

files
)

{


for
(
const

imp

of

file
.
imports
)

{


const

resolved

=

resolveImportPath
(
imp
,

file
.
path
,

filePathSet
);


if
(
resolved
)

{


edges
.
push
({

source
:

file
.
path
,

target
:

resolved
,

type
:

"
import
"

});


}


}


}


return

{

nodes
,

edges

};

}

Enter fullscreen mode

Exit fullscreen mode

SamesetVisualizationcall, different data. React Flow re-renders and the graph morphs from a folder map into a real dependency graph focused on exactly the files relevant to your question.

 

### 3. The CopilotKit runtime

The/api/copilotkitroute is where LLM requests actually land. The API key and provider config are stored in an httpOnly cookie, meaning they live on the server and never get sent to the browser.

The route reads that config, creates an OpenAI-compatible client, and hands the request to the CopilotKit runtime:

export

const

POST

=

async
(
req
:

NextRequest
)

=>

{


const

{

baseURL
,

apiKey
,

model

}

=

await

getLLMConfig
();


const

openai

=

new

OpenAI
({

baseURL
,

apiKey

});


const

serviceAdapter

=

new

OpenAIAdapter
({

openai
,

model

});


const

runtime

=

new

CopilotRuntime
();


const

{

handleRequest

}

=

copilotRuntimeNextJSAppRouterEndpoint
({


runtime
,


serviceAdapter
,


endpoint
:

"
/api/copilotkit
"
,


});


return

handleRequest
(
req
);

};

Enter fullscreen mode

Exit fullscreen mode

The defaults point to Ollama onlocalhost:11434/v1withqwen2.5.

Because the OpenAI SDK accepts a custombaseURL, swapping to OpenAI, Groq or any other provider is just a config change with no code changes needed.

 

### 4. Feeding the LLM context

Before the LLM can answer anything useful, it needs to know what repo is loaded and what files exist. That is the job of theuseCopilotContext.tshook.

It callsuseAgentContext, a CopilotKit hook that attaches structured data to every message you send. You can call it multiple times to attach different pieces of context.

Here it is called twice: once for the file list and once for the system instructions that tell the LLM how to behave:

useAgentContext
({


description
:

"
File paths in the repository (max 500), one per line
"
,


value
:

fileList
,

// flattened from the TreeNode structure

});

useAgentContext
({


description
:

"
System instructions
"
,


value
:

`You are a Codebase Navigator assistant. You MUST use tool calls to answer questions.
CRITICAL RULES:
1. For ANY question about the repository call the "analyzeRepository" tool.
2. To show a file, call "fetchFileContent" with the exact file path.
3. NEVER respond with only text. ALWAYS call a tool first.
4. Use ONLY file paths from the file list above.`

});

Enter fullscreen mode

Exit fullscreen mode

The file list is capped at 500 paths to stay within token limits.

Because this hook re-runs every time the Zustand store changes, the LLM always sees the current repo, selected file and analysis state rather than a stale snapshot from when the page loaded.

Note: If you are running a local model with a large context window, you can raise this limit inuseCopilotContext.ts.

 

### 5. The four frontend tools

This is the core of how the app works. Instead of just replying with text, the LLM can call tools. Each tool has a name, a set of parameters it accepts and a handler, which is just a function that runs when the LLM calls it.

CopilotKit lets you register these tools directly in the browser using theuseFrontendToolhook, which is defined inuseCopilotActions.ts.

When a tool's handler runs, it updates Zustand state directly, which is why all four panels, the graph, code viewer, analysis panel, and chat, react at the same time without any extra wiring.

analyzeRepositoryis the main tool the LLM calls for almost every question. Here is what it does step by step:

useFrontendTool
({


name
:

"
analyzeRepository
"
,


parameters
:

z
.
object
({


query
:

z
.
string
(),


explanation
:

z
.
string
(),


}),


handler
:

async
({

query
,

explanation

})

=>

{


// 1. Find relevant files using keyword matching


const

matchedPaths

=

findFilesByQuery
(
repo
.
tree
,

query
);


// 2. Cap at 15 files to keep things fast


const

capped

=

matchedPaths
.
slice
(
0
,

15
);


// 3. Fetch each file content (cached)


const

fileData

=

await

Promise
.
all
(


capped
.
map
(
async
(
p
)

=>

({


path
:

p
,


imports
:

extractImports
(
await

fetchFile
(
owner
,

repo
,

p
,

branch
)),


}))


);


// 4. Build real dependency graph from actual import statements


const

graph

=

buildDependencyNodes
(
fileData
);


// 5. Categorize each node by file type


graph
.
nodes
.
forEach
(
node

=>

{


node
.
type

=

categorizeFileType
(
node
.
metadata
.
fullPath
);


});


// 6. Push to Zustand - all four panels react


setAnalysisResult
({

explanation
,

relevantFiles
,

flowDiagram
:

graph

});


setVisualization
(
graph
.
nodes
,

graph
.
edges
,

"
dependency
"
);


},

});

Enter fullscreen mode

Exit fullscreen mode

fetchFileContentopens a specific file in the code viewer. The LLM calls this when you ask it to show you a file, it just fetches the content and callssetCodeViewer:

useFrontendTool
({


name
:

"
fetchFileContent
"
,


parameters
:

z
.
object
({


filePath
:

z
.
string
(),


}),


handler
:

async
({

filePath

})

=>

{


const

content

=

await

fetchFile
(
repo
.
repoInfo
.
owner
,

repo
.
repoInfo
.
repo
,

filePath
,

repo
.
repoInfo
.
branch
);


setCodeViewer
(
filePath
,

content
);


},

});

Enter fullscreen mode

Exit fullscreen mode

generateFlowDiagramis similar toanalyzeRepositorybut more focused. Instead of searching the whole repo, you give it a specific list of file paths and it builds a graph for just those files. Useful when you want to visualize a slice of the codebase like just the API layer:

useFrontendTool
({


name
:

"
generateFlowDiagram
"
,


parameters
:

z
.
object
({


files
:

z
.
array
(
z
.
string
()),


diagramType
:

z
.
enum
([
"
dependency
"
,

"
flow
"
,

"
architecture
"
]),


}),


handler
:

async
({

files
,

diagramType

})

=>

{


const

fileData

=

await

Promise
.
all
(
files
.
slice
(
0
,

20
).
map
(
async
(
f
)

=>

({


path
:

f
,


imports
:

extractImports
(
await

fetchFile
(
repo
.
repoInfo
.
owner
,

repo
.
repoInfo
.
repo
,

f
,

repo
.
repoInfo
.
branch
)),


})));


const

graph

=

buildDependencyNodes
(
fileData
);


setVisualization
(
graph
.
nodes
,

graph
.
edges
,

diagramType
);


},

});

Enter fullscreen mode

Exit fullscreen mode

highlightCodefetches a file and highlights specific line numbers with an explanation. The LLM uses this when it wants to point at exactly where something happens in the code:

useFrontendTool
({


name
:

"
highlightCode
"
,


parameters
:

z
.
object
({


filePath
:

z
.
string
(),


lines
:

z
.
array
(
z
.
number
()),


explanation
:

z
.
string
(),


}),


handler
:

async
({

filePath
,

lines
,

explanation

})

=>

{


const

content

=

await

fetchFile
(
repo
.
repoInfo
.
owner
,

repo
.
repoInfo
.
repo
,

filePath
,

repo
.
repoInfo
.
branch
);


setCodeViewer
(
filePath
,

content
,

lines
,

explanation
);


},

});

Enter fullscreen mode

Exit fullscreen mode

Notice that none of these tools returns text to the chat. They all just update the state. The LLM is not describing what it found, it is directly controlling what you see on screen.

For instance, I asked about the architecture of v2 packages.

 

### 6. Finding relevant files

WhenanalyzeRepositorygets a query like "how does authentication work?", it needs to figure out which files to actually look at. That is handled byfindFilesByQueryinsrc/lib/analyzer.ts.

It checks if the query matches one of six predefined categories, each with a set of keywords and file path patterns:

const

ANALYSIS_CATEGORIES

=

[


{


name
:

"
authentication
"
,


keywords
:

[
"
auth
"
,

"
login
"
,

"
logout
"
,

"
token
"
,

"
jwt
"
,

"
session
"
,

"
oauth
"
],


filePatterns
:

[
/auth/i
,

/login/i
,

/session/i
,

/oauth/i
,

/jwt/i
],


},


{


name
:

"
database
"
,


keywords
:

[
"
database
"
,

"
db
"
,

"
model
"
,

"
schema
"
,

"
prisma
"
,

"
mongoose
"
],


filePatterns
:

[
/model/i
,

/schema/i
,

/migration/i
,

/prisma/i
,

/db/i
],


},


// ... api, configuration, testing, styling

]

Enter fullscreen mode

Exit fullscreen mode

If the query matches a category, it filters all file paths using that category's regex patterns.

If nothing matches, it falls back to splitting the query into individual terms and checking if any file path contains them. So even a vague query like "where is the config" will still find files with "config" in the name.

This is intentionally simple. No embeddings, no vector search, just regex on file names. It works well because file names in well-structured projects are usually descriptive enough that matching on them gets you the right files.

 

### 7. File caching

Every time a tool fetches a file, it goes throughsrc/lib/fetch-file.tswhich maintains an in-memory cache with a 5-minute TTL:

const

cache

=

new

Map
<
string
,

{

content
:

string
;

timestamp
:

number

}
>
();

const

CACHE_TTL

=

5

*

60

*

1000
;

// 5 minutes

export

async

function

fetchFile
(
owner
,

repo
,

path
,

ref
)

{


const

key

=

`
${
owner
}
/
${
repo
}
/
${
ref
}
/
${
path
}
`
;


const

cached

=

cache
.
get
(
key
);


if
(
cached

&&

Date
.
now
()

-

cached
.
timestamp

<

CACHE_TTL
)

{


return

cached
.
content
;

// serve from cache


}


const

res

=

await

fetch
(
`/api/github/file?repo=...&path=...&ref=...`
);


const

data

=

await

res
.
json
();


cache
.
set
(
key
,

{

content
:

data
.
content
,

timestamp
:

Date
.
now
()

});


// LRU eviction: if over 200 items, drop the oldest 50


if
(
cache
.
size

>

200
)

{


const

oldest

=

[...
cache
.
entries
()].
sort
((
a
,

b
)

=>

a
[
1
].
timestamp

-

b
[
1
].
timestamp
);


for
(
let

i

=

0
;

i

<

50
;

i
++
)

cache
.
delete
(
oldest
[
i
][
0
]);


}


return

data
.
content
;

}

Enter fullscreen mode

Exit fullscreen mode

This matters becauseanalyzeRepositoryfetches up to 15 files at once. A follow-up question about the same files hits the cache instead of making 15 more API requests.

Without a GitHub token, you are limited to 60 requests per hour, so caching is what makes repeated questions fast and free.

The cache also evicts the oldest entries once it crosses 200 items, so it never grows unbounded in long sessions.

 

### 8. Parsing imports and resolving paths

OnceanalyzeRepositoryhas the relevant file paths, it fetches each file and parses it for import statements. Both functions that handle this live insrc/lib/analyzer.ts.

extractImportsruns on the raw file content and pulls out every import, handling both ES6 and CommonJS syntax:

export

function

extractImports
(
content
:

string
):

string
[]

{


const

imports
:

string
[]

=

[];


// ES6: import X from 'y' and import 'y'


const

esImports

=

content
.
matchAll
(


/
(?:
import
\s
+.*
?\s
+from
\s
+
[
'"
](
.+
?)[
'"
]
|import
\s
+
[
'"
](
.+
?)[
'"
])
/g


);


for
(
const

match

of

esImports
)

imports
.
push
(
match
[
1
]

||

match
[
2
]);


// CommonJS: require('y')


const

requires

=

content
.
matchAll
(
/require
\s
*
\(\s
*
[
'"
](
.+
?)[
'"
]\s
*
\)
/g
);


for
(
const

match

of

requires
)

imports
.
push
(
match
[
1
]);


return

imports
;

}

Enter fullscreen mode

Exit fullscreen mode

But raw import strings like"./utils"or"@/lib/github"are not file paths yet.

buildDependencyNodescallsresolveImportPathon each one to turn them into actual paths that exist in the repo:

function

resolveImportPath
(
importPath
,

fromFile
,

filePathSet
)

{


// Skip npm packages (no ./ or @/)


if
(
!
importPath
.
startsWith
(
"
.
"
)

&&

!
importPath
.
startsWith
(
"
@/
"
))

return

null
;


// Resolve @/ alias to src/


if
(
importPath
.
startsWith
(
"
@/
"
))

{


resolved

=

"
src/
"

+

importPath
.
slice
(
2
);


}


// Try with common extensions: .ts, .tsx, .js, /index.ts, etc.


const

extensions

=

[
""
,

"
.ts
"
,

"
.tsx
"
,

"
.js
"
,

"
.jsx
"
,

"
/index.ts
"
,

"
/index.tsx
"
];


for
(
const

ext

of

extensions
)

{


if
(
filePathSet
.
has
(
resolved

+

ext
))

return

resolved

+

ext
;


}


return

null
;

}

Enter fullscreen mode

Exit fullscreen mode

npm packages likereactorzodare skipped immediately since they do not start with./or@/. For local imports, it tries common extensions like.ts,.tsx, and/index.ts, so it handles both direct file imports and folders that export through an index file.

If the resolved path does not exist in the repo, it returns null and no edge is created. That is what keeps the graph honest.

 

### 9. Graph layout with Dagre

Once the nodes and edges are built, they need actual positions on screen before React Flow can render them. That is whatapplyDagreLayoutdoes insrc/lib/graph-layout.ts.

It usesDagre, a JavaScript library that automatically calculates x and y coordinates for every node in a directed graph so nothing overlaps, all on the client side with no server needed:

export

function

applyDagreLayout
(
nodes
,

edges
,

options

=

{})

{


const

g

=

new

dagre
.
graphlib
.
Graph
();


g
.
setGraph
({

rankdir
:

"
TB
"
,

ranksep
:

80
,

nodesep
:

40

});


// Tell dagre the size of each node


for
(
const

node

of

nodes
)

{


g
.
setNode
(
node
.
id
,

{

width
:

200
,

height
:

60

});


}


for
(
const

edge

of

edges
)

{


g
.
setEdge
(
edge
.
source
,

edge
.
target
);


}


dagre
.
layout
(
g
);

// dagre calculates x,y for every node


return

nodes
.
map
((
node
)

=>

{


const

pos

=

g
.
node
(
node
.
id
);


return

{

...
node
,

position
:

{

x
:

pos
.
x

-

100
,

y
:

pos
.
y

-

30

}

};


});

}

Enter fullscreen mode

Exit fullscreen mode

The direction can be toggled between top-to-bottom (TB) and left-to-right (LR) from the UI.

Each node type maps to a React Flow component based on the file typecategorizeFileTypeassigned earlier:

* module/service→ModuleNode(indigo)
* function→FunctionNode(teal)
* file→FileNode(gray)

 

### 10. State management with Zustand

All four panels stay in sync because they all read from the same Zustand store insrc/store/index.ts. The store has four slices, one for each major concern:

interface

AppState

{


repo
:

{


repoInfo
:

RepoInfo

|

null
;

// owner, repo, branch


tree
:

TreeNode

|

null
;

// full file tree


selectedFile
:

string

|

null
;

// active file path


loading
:

boolean
;


error
:

string

|

null
;


};


analysis
:

{


result
:

AnalysisResult

|

null
;

// explanation + relevant files + graph


loading
:

boolean
;


error
:

string

|

null
;


};


visualization
:

{


nodes
:

FlowNode
[];


edges
:

FlowEdge
[];


graphType
:

"
dependency
"

|

"
flow
"

|

"
architecture
"

|

null
;


};


codeViewer
:

{


filePath
:

string

|

null
;


content
:

string

|

null
;


highlightedLines
:

number
[];


explanation
:

string

|

null
;


};

}

Enter fullscreen mode

Exit fullscreen mode

Each panel subscribes to only the slice it needs using a selector likeuseAppStore((s) => s.visualization).

So when a tool callssetVisualization, only the graph panel re-renders. WhensetCodeViewerfires, only the code viewer updates. Nothing else moves.

Settings like LLM provider, API key and model live in a separateSettingsStatestore. It syncs to two places:

* localStorageso the browser remembers your config across reloads
* an httpOnly cookie so the server-side/api/copilotkitroute can read them without the API key ever appearing in request headers

This is how everything works behind the scenes. It's time to run it locally.

## Running it locally

Clone the GitHub repository and install the dependencies.

git clone <repo-url>

cd
codebase-navigator
npm
install

npm run dev

Enter fullscreen mode

Exit fullscreen mode

Openhttp://localhost:3000to view it live in the browser. Here is how to set up each provider.

 

### Using OpenAI

You will need anOpenAI API Key. Then just click the Settings icon in the top right, switch the provider to OpenAI, paste your API key and pick a model likegpt-5.2. That's it.

 

Using Ollama (free, runs locally)

You can download it fromollama.comor install it via these commands based on the operating system you use.

brew
install
ollama
#macOS

curl
-fsSL
 https://ollama.com/install.sh | sh
#linux

Enter fullscreen mode

Exit fullscreen mode

Then pull the model and start the server:

ollama serve
ollama pull qwen2.5
# in another terminal

Enter fullscreen mode

Exit fullscreen mode

The app points to Ollama by default so nothing else needs to change. Just openhttp://localhost:3000and it works.

 

For GitHub, public repos work without a token (the only catch is that it's limited to 60 requests per hour). Add aGITHUB_TOKENto a.env.localfile for higher limits:

GITHUB_TOKEN
=
your_token_here

Enter fullscreen mode

Exit fullscreen mode

I tried it with the CopilotKit GitHub repo and it immediately maps out the entire repo structure.

I asked it, "tell me about architecture" and it gave me:

* a graph of every relevant file connected by real imports
* a plain english breakdown of what each file does
* raw code fetched live from GitHub
* a detailed chat response I could keep following up on

I tried difficult and vague questions and it handled all of them.

## The bigger picture

This project started with wiring three ideas together and seeing what happened.

GitHub is the data source, not just a host. Every file the AI references gets fetched live, parsed, and reasoned about on the spot. No hallucination, no guessing from memory.

CopilotKit changes what the AI can actually do in the browser. Instead of replying with text, it calls tools that update the state directly. The graph changes. The code viewer opens. The AI is not describing what it found, it is showing you.

The dependency edges are real. A lot of tools draw graphs that look impressive but mean nothing. Every edge here exists because one file has an actual import statement pointing to another. That is it.

Wire those three together and you get something that actually understands the codebase instead of just searching through it.

There is a lot you could extend from here: PR diff exploration, multi-repo comparison, security audit mode. But as a starting point for understanding any codebase, it already does exactly what it needs to.

Let me know what you think in the comments!

You can connect me onGitHub,TwitterandLinkedIn.

Follow CopilotKit onTwitterand say hi, and if you'd like to build something cool, join theDiscordcommunity.

## CopilotKitFollow

 React UI + elegant infrastructure for AI Copilots, in-app AI agents, AI chatbots, and AI-powered Textareas 🪁


 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (14 comments)


For further actions, you may consider blocking this person and/orreporting abuse
