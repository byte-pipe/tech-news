---
title: We want you to build the next Git platform on Cloudflare | Cloudflare Blog
url: https://blog.cloudflare.com/next-git-platform-on-cloudflare/
site_name: hackernews_api
content_file: hackernews_api-we-want-you-to-build-the-next-git-platform-on-clou
fetched_at: '2026-10-05T12:19:43.518374'
original_url: https://blog.cloudflare.com/next-git-platform-on-cloudflare/
author: geoffbp
date: '2026-10-04'
published_date: '2026-10-01T13:00:00.000Z'
description: Cloudflare is hosting a competition to see who will build the next Git platform for an era of AI agents. Artifacts is in open beta, with Workers bindings, data jurisdiction controls, and event subscriptions for repository changes.
tags:
- hackernews
- trending
---

GitHub was built for a world where humans write code, organize it into repositories, and collaborate through branches, commits, issues, and pull requests.

But the next generation of software is going to be built differently because it is going to be built by a different kind of developer: agents.

Agents are already writing more code than ever before — they’re fixing bugs, building features, writing tests, reviewing changes, updating dependencies, and doing the routine maintenance required to keep an application running.

So in this new world where you have hundreds, or even thousands, of agents working on the same codebase at the same time, what does the foundation look like?

How do agents know what other agents are working on? What happens when they make conflicting changes? How do you review everything they produce? How do you keep track of not just what changed, butwhya change was made?

And so the burning question is:What does the next GitHub look like?

We want you to help us answer it, by building it out.

Earlier this year, we launchedArtifacts, a versioned filesystem that speaks Git and can scale to millions of repositories. From the start, we designed Artifacts as a set of programmable primitives that developers could use to build their own products, workflows, and abstractions.

Artifacts provides the foundation: repositories that can be created and forked programmatically, versioned storage for code and agent context, and the Git operations agents already know how to use.

With that foundation in place, you can focus on the layer above it: how agents coordinate their work, how changes are reviewed and merged, and what the developer experience should look like when hundreds or thousands of agents are working on the same codebase.

That is the layer we want you to build.

Now that Artifacts is in open beta,we’re holding a competitionto see who can build the next Git platform on Cloudflare using Workers and Artifacts.

## Artifacts is in open beta. Here’s why you should build on it

When we launched Artifacts, our goal was to make it possible to create a repository for every agent, session, task, or user — and to do that at the scale agents require.

Since then, we’ve seen developers use Artifacts in a range of ways: Vibe-coding platforms are using it to store the projects their users create. Developers are using it to persist the code and context from agent sessions. Others are creating isolated repositories, so multiple agents can safely work from the same starting point and compare or merge the results later.

Here are some new capabilities we’ve added since the initial launch.

### Deploy Artifacts repos to Workers

You can now connect an Artifacts repository to a Worker throughWorkers Builds. When you or an agent pushes code to the Artifacts repository, Cloudflare will build the project and, for the production branch, deploy the updated Worker. Pushes to other branches automatically create or updateWorkers Previews, giving you an isolated, shareable version of your Worker where you can test changes before they go live.

You can connect an existing Worker to an Artifacts repository or start a new project and automatically store it in Artifacts.

### Manage Artifacts directly from Workers

You can interact with Artifacts repositories directly from a Worker using anArtifacts bindingto create or fork repos, inspect files and commits, and issue repo-scoped Git tokens. This makes your Git workflow programmable. When a new task arrives, a Worker can fork the project for an agent, read the files it needs for context, and give it a repository to work in. When the agent pushes a change, your automation can inspect the result and start a review. You define those steps in code to fit how your agents work.

For example, here’s how to fork a project for a new agent task and read itsAGENTS.mdfor instructions:

using
 project
 =
 await
 env.
ARTIFACTS
.
get
(
"my-project"
);

const
 { 
defaultBranch
 } 
=
 await
 project.
info
();

const
 workspace
 =
 await
 project.
fork
(
`task-${
crypto
.
randomUUID
()
}`
);

using
 repo
 =
 await
 env.
ARTIFACTS
.
get
(workspace.name);

const
 instructions
 =
 await
 repo.
readFile
({

 ref: defaultBranch,

 path: 
"AGENTS.md"
,

});

const
 agentTask
 =
 {

 remote: workspace.remote,

 token: workspace.token,

 instructions: instructions 
?
 await
 instructions.
text
() 
:
 null
,

};

### React to every change with event subscriptions

Artifacts publishes events whenever a repository is created, imported, forked, deleted, pushed to, cloned, or fetched. You can subscribe to these events to decide what happens next: run CI, kick off a code review agent, or deploy a change.

For example, you can subscribe to Artifacts push events and have a Worker start a code review workflow for each push. The Worker passes the repository, branch, and new commit to the Workflow, giving a review agent the context it needs to inspect the change:

export
 default
 {

 async
 queue
(
batch
, 
env
) {

 for
 (
const
 message
 of
 batch.messages) {

 const
 event
 =
 message.body;

 if
 (event.type 
!==
 "cf.artifacts.repo.pushed"
) 
continue
;

 await
 env.
REVIEW_WORKFLOW
.
create
({

 params: {

 namespace: event.source.namespace,

 repo: event.source.repoName,

 ref: event.payload.ref,

 commit: event.payload.after,

 },

 });

 }

 },

};

### Data jurisdiction for Artifacts repos

You can nowchoose where Artifacts stores and processesyour repository data. Set a U.S. or EU jurisdiction when you create a namespace, and every repository created in that namespace will automatically follow the same restriction.

curl
 "https://api.cloudflare.com/client/v4/accounts/
$ACCOUNT_ID
/artifacts/namespaces"
 \

 -H
 "Authorization: Bearer 
$CLOUDFLARE_API_TOKEN
"
 \

 --json
 '{"namespace":"my-eu-namespace","jurisdiction":"eu"}'

### View Artifacts metrics

You can now see metrics for your Artifacts repositories in the Cloudflare dashboard. For each repository, you can now see total operations, pulls, pushes, errors, and error rate, helping you understand how the repository is being used and spot failures. You can also queryArtifacts metricsdirectly to build your own dashboards or monitoring.

### Pricing

Artifacts pricing is based on repository operations and the amount of data stored. We will begin billing for Artifacts usage on October 15, 2026.

## Competition: Build the next Git platform on Cloudflare

We want you to build your vision for the Git platform of the agentic era using Cloudflare Workers and Artifacts.

You could rethink repositories, branches, pull requests, worktrees, code review, and merge conflicts — or build new ways to preserve agent context, compare multiple changes at the same time, and decide which one should ship.

We aren’t looking for GitHub as it exists today with agents added on top. At a minimum, we want to see multiple agents working on changes concurrently. Beyond that, we want you to get creative — what you think comes next.

### How to enter

Submit:

* A 5-10 minute video demonstrating what you built, what it enables agents and developers to do, and how it works
* A link to the source code, which must be provided under a permissive open source license (MIT, Apache, BSD)
* Instructions for running or trying the project

### Deadline

Submissionsare open until October 14, 2026.

### Why should you participate?

We’ll select the top three projects and fly up to two members from each team to San Francisco to attendCloudflare Connectand show what they built.

The first-place team will also receive $25,000 in Cloudflare credits, along with invitations to the VIP speaker dinner on Monday night at Connect.

## Get started

Artifacts is available in open beta to customers on the Workers Paid plan.

Get started with your coding agent:copy the prompt below to set up your first Artifacts repository and start pushing code to it.

Copy prompt
Copy prompt
Prompt copied!

You can view or create the Artifacts repositories in thedashboardor if you’re looking to learn more, check out thedocumentation.

## Related tags

Birthday Week
Developers
Workers

Follow on Social Media

* Cloudflare
* Dina Kozlov
* Zebulon Piasecki

## Subscribe to receive notifications of new posts

Email address

We’ll never share your email address.

Subscribe

Thanks for subscribing! Check your inbox to confirm.