---
title: Enabling developers in GitHub Codespaces - DEV Community
url: https://dev.to/fastly/enabling-developers-in-github-codespaces-1l3a
site_name: devto
fetched_at: '2025-10-11T19:07:03.809167'
original_url: https://dev.to/fastly/enabling-developers-in-github-codespaces-1l3a
author: Sue Smith
date: '2025-10-07'
description: Over the last few months I’ve been exploring GitHub codespaces for developer enablement. I needed to... Tagged with webdev, github, vscode, learning.
tags: '#webdev, #github, #vscode, #learning'
---

Over the last few months I’ve been exploring GitHub codespaces for developer enablement. I needed to replace our Fastly onboarding projects that had been hosted on Glitch, and ideally wanted to avoid the need for learners to install local tooling or even sign up for an account before trying our Compute platform. In this post I’ll run through what I’ve discovered about using codespaces for dev product learning.

Here’s an overview of what our codespace projects do:

* Install dependencies and automatically run an app
* Open previews of the app UI in the codespace
* Deploy apps at the click of a button using bash scripts
* Hide UI elements to minimize distractions
* Use an extension to show custom buttons in the editor for actions like splitting views, sharing app previews, opening the terminal, formatting code

This daft video runs through how they work:

## Wait, what is a codespace?

A codespace is a web editing environment you can open in the browser from a GitHub repository. Codespaces use a version of the VS Code editor, so you can specify editor settings much like you would in a local VS Code installation. Using codespaces lets you carry out development activities without downloading or installing anything onto your local machine – it all happens in the cloud.

You can access codespaces from the homepage of a GitHub repo, using theCodebutton to open an environment for editing the codebase on a specific repo branch.

Edits made in a codespace are automatically kept for a limited period of time you can set in your GitHub account – you’ll receive a warning if a codespace is about to be deleted and you can export your changes to a branchif you aren’t ready to lose them.

## Containers

A codespace runs in a Docker container, and you can specify requirements in the repodevcontainer.jsonfile. I usually include system features like Node (mostly I’m targeting JavaScript projects in the Node ecosystem), but the codespace will guess some dependencies based on the repo content.

Here’s an example container spec I’m using for edge computing projects:~learn-edge-computing/devcontainer.json

You can attach commands to container lifecycle events – these run when the codespace opens, so you can use them to carry out setup tasks and get the codespace in the state you want for your learners when they open the project. I’ve been using theupdateContentCommandandpostAttachCommandevents to install NPM packages and runpackage.jsonscripts I want to execute straight away.

📚 Thedevcontainer metadata referencelists the options.

This is part of a container config I used for projects originally developed on Glitch that I’d exported to GitHub:

"updateContentCommand"
:

"npm install"
,

"postAttachCommand"
:

"npm run start || npx --yes serve"

Enter fullscreen mode

Exit fullscreen mode

## Previews and ports

You can run apps “locally” in the codespace and they’ll be exposed through specific ports. With the Simple Browser you can automatically open these apps right inside the editor at anapp.github.devaddress. ThePORTSarea in theTerminalat the bottom of the editor provides access to port settings, so you can open previews, change visibility, and share URLs with collaborators.

In the container config, I include a section specifying that specific ports should automatically open in the preview. For my edge compute learning experience, it sets both the origin website and edge apps to open from their default ports, with custom labels making them more obvious to the learner:

"portsAttributes"
:

{


"3000"
:

{


"label"
:

"🚧 Origin"
,


"onAutoForward"
:

"openPreview"


},


"7676"
:

{


"label"
:

"🌎 Compute"
,


"onAutoForward"
:

"openPreview"


}

}

Enter fullscreen mode

Exit fullscreen mode

I also use a custom 🔗Sharebutton to set a port to public and provide the URL so that the user can copy it to share with collaborators – they can see the preview as long as they’re logged into GitHub.

💡 If your project is a fully static site and doesn’t use a framework, you can still run a preview usingnpx serve.

## Extensions

You can list required VS Code extensions in your codespace container config and they’ll automatically be installed when someone opens the project. I includeESLintbecause my projects typically use JavaScript, and the extension for custom buttons then runs the format command.

### Custom buttons

I’ve found theVS Code Action Buttonsextension extremely helpful when it comes to customizing the UI for my learning projects. The extension lets you specify buttons that appear along the bottom of the editor. Your buttons can call VS Code editor commands and CLI commands, so I use them to give users an easy way to toggle views, and run bash scripts orTerminalprocesses.

Here’s an excerpt of one of my button lists:

"actionButtons"
:

{


"commands"
:

[


{


"name"
:

"🌈 Prettify"
,


"singleInstance"
:

true
,


"useVsCodeApi"
:

true
,


"command"
:

"editor.action.formatDocument"
,


"tooltip"
:

"Tidy up your code"


},


{


"name"
:

"🚀 Publish"
,


"singleInstance"
:

true
,


"command"
:

"bash helpers/publish.sh"
,


"tooltip"
:

"Publish your content to Fastly Compute"


}


]

}

Enter fullscreen mode

Exit fullscreen mode

You can include whateverTerminalcommands you need for your target frameworks – I tend to separate them into bash scripts so that the user can tweak them more readily if they like.

📋 Here are the commands you can run on button clicks:Built-in Commands

## Bash scripts

With the projects I’m working on being experimental, I wanted users to be able to see and tailor the CLI code that automates processing. For that reason I included the bash scripts in ahelpersfolder, calling those scripts from the container config and button clicks. The Fastly CLI commands have a little bit of control flow complexity that really needs a lot of testing, so I need to be able to make changes easily.

Here’s a more basic bash script I use for projects users have imported (and I therefore don’t know for sure which scripts they have in theirpackage.json):

# We're making some guesses about the package scripts lolol

if

[

!

-f
 package.json
]
;

then

printf

"
\n
🤔 No package.json found – try the Open button instead!
\n\n
"

else

OOPS
=
"
\n
🤬 hmm maybe check what's in your package.json scripts and try "
npm run script-name
"?
\n\n
"

 npm
install

||

printf

"
${
OOPS
}
"

 npm run start
||

printf

"
${
OOPS
}
"

fi

Enter fullscreen mode

Exit fullscreen mode

I also use scripts like this to write out instructional information to the user in theTerminal.

## Deployment

The Fastly projects support deployment to the edge, so I typically use a 🚀Publishbutton that runs the Fastly CLI tooling and deploys the app. Here's publish script for our Compute Static Publisher:publish.sh

Codespaces make a great editing environment for simple static website projects, and you can publish from the editor, for example if you have a blog. You can deploy to GitHub Pages at the click of a button by including thegh-pagespackage in your project, and a script in yourpackage.json, like this Vite example:

"scripts"
:

{


"start"
:

"vite"
,


"build"
:

"vite build"
,


"serve"
:

"vite preview"
,


"deploy"
:

"gh-pages -d dist"

}

Enter fullscreen mode

Exit fullscreen mode

To publish using a button, just call thedeploycommand from the custom button extension covered above. I’m using this flow for my own blog and static site projects that I migrated from Glitch.

## Environment variables

If your platform requires an API key, you can instruct users to acquire and add one inside the codespace. In theREADMEI include links and steps for grabbing a Fastly API key and adding it using the command palette. When a user adds an environment variable, the codespace will prompt them to reload, which they’ll need to do in order to use the variable in subsequent commands.

## File and feature visibility

You can specify settings for the VS Code editing experience in your container config just like you would in a local environment. I tend to hide some features to minimize distractions, like the minimap, and files / folders likenode_modules, so that the learner can focus on the core parts of the project I’m trying to familiarize them with.

You can include these in the settings object in your container JSON:

"settings"
:

{


"files.exclude"
:

{


"package-lock.json"
:

true
,


"node_modules/"
:

true


},


"editor.minimap.enabled"
:

false
,

}

Enter fullscreen mode

Exit fullscreen mode

## Source control

Although a codespace automatically stores your edits until it’s deleted, it’s a good idea to encourage users to regularly commit their changes to the underlying repo in case they lose them. You can do this in theSource Controlarea on the left.

Things can get a bit confusing depending on whether your users have started the codespace from your repo or from a fork of it – I encourage users to create their own fork so that it’s clearer where their changes should be saved.

🤔Something that gets a bit messy with codespaces for dev product onboarding is that the flow seems to be primarily optimized for devs making contributions to a repo rather than forking it to make their own project. If you don’t plan to publish changes you want your users to be able to sync their forks with, you can use template repos instead. This is one place I’ve felt the tension of what I was able to support users to do on Glitch vs this workflow.

## Optimizing your repos for codespaces

When you first open a codespace with a custom container config, it can be pretty slow to start up. You can reduce this withprebuildsthat target specific regions you expect your users to be in. Although the free tier is generous, you might want to keep an eye on the costs for storage and compute associated with your codespaces, and definitely set spending limits in your GitHub account.

📝 Some of the setup for codespaces can translate to users cloning your repos locally and opening them in VS Code on their computers – this is something I want to explore soon, as well as supporting other web based VS Code environments.

## Learn more

I found this post fromRizèl Scarlettsuper helpful when I was figuring out what I could do:How to run a frontend workshop in Codespaces🙌

Some official docs:

* Quickstart for GitHub Codespaces
* Create a Dev Container

Some of my codespace-optimized projects:

* One I used for people migrating from Glitch:~glitchy-editing
* Publishing an 11ty blog to the edge:~11ty-to-compute
* Edge computing intro:~learn-edge-computing

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
