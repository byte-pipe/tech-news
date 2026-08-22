---
title: 'GitHub - n8n-io/n8n: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations. · GitHub'
url: https://github.com/n8n-io/n8n
site_name: github
content_file: github-github-n8n-ion8n-fair-code-workflow-automation-pla
fetched_at: '2026-08-22T19:21:14.806297'
original_url: https://github.com/n8n-io/n8n
author: n8n-io
description: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations. - n8n-io/n8n
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 n8n-io

 

/

n8n

Public

* NotificationsYou must be signed in to change notification settings
* Fork60.3k
* Star202k

 
 
 
master
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

23,368 Commits
23,368 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.agents/
skills
.agents/
skills
 
 
.claude
.claude
 
 
.devcontainer
.devcontainer
 
 
.github
.github
 
 
.opencode/
skills/
setup-mcps
.opencode/
skills/
setup-mcps
 
 
.vscode
.vscode
 
 
assets
assets
 
 
docker
docker
 
 
docs
docs
 
 
packages
packages
 
 
patches
patches
 
 
scripts
scripts
 
 
security
security
 
 
.actrc
.actrc
 
 
.aikido
.aikido
 
 
.boundaries-baseline.json
.boundaries-baseline.json
 
 
.code-health-baseline.json
.code-health-baseline.json
 
 
.dockerignore
.dockerignore
 
 
.editorconfig
.editorconfig
 
 
.env.eval.example
.env.eval.example
 
 
.env.local.example
.env.local.example
 
 
.git-blame-ignore-revs
.git-blame-ignore-revs
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.npmignore
.npmignore
 
 
.npmrc
.npmrc
 
 
.poutine.yml
.poutine.yml
 
 
.prettierignore
.prettierignore
 
 
.prettierrc.js
.prettierrc.js
 
 
.tbls.postgres.yml
.tbls.postgres.yml
 
 
.tbls.sqlite.yml
.tbls.sqlite.yml
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
CONTRIBUTOR_LICENSE_AGREEMENT.md
CONTRIBUTOR_LICENSE_AGREEMENT.md
 
 
LICENSE.md
LICENSE.md
 
 
LICENSE_EE.md
LICENSE_EE.md
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
biome.jsonc
biome.jsonc
 
 
codecov.yml
codecov.yml
 
 
cubic.yaml
cubic.yaml
 
 
lefthook.yml
lefthook.yml
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
pnpm-workspace.yaml
pnpm-workspace.yaml
 
 
tsconfig.configs.json
tsconfig.configs.json
 
 
tsconfig.json
tsconfig.json
 
 
turbo.json
turbo.json
 
 
vitest.workspace.ts
vitest.workspace.ts
 
 
View all files

## Repository files navigation

# n8n – The Platform for AI Agents and Workflow Automation

Fair-code platform to build and deploy AI agents and workflows. Combine a visual canvas with custom code, run it self-hosted or in thecloud, and connect to 1500+ integrations. AI automation you can trust with real work, from prototype to production.

## Key Capabilities

* AI-Native Automation Platform: Build and operationalize AI workflows and multi-step agents using your own data, models, and tools
* Model Flexibility, No Lock-In: Connect to OpenAI, Anthropic, Google, or open-source models and switch providers without changing your architecture
* From Prototype to Production: Design multi-step AI workflows with logic, tool use, human approvals, and full observability
* Code When You Need It: Combine visual building with JavaScript, Python, and npm packages for advanced AI workflows
* Enterprise-Ready AI: Self-host or deploy securely with role-based access, audit trails, and support for sensitive data
* Leverage What Already Exists: 1500+ integrations and 9,000+ workflowtemplatesto connect AI with your existing systems

## Quick Start

Try n8n instantly with our install script (requiresDocker):

curl -fsSL https://get.n8n.io 
|
 sh

Or deploy manually withDocker:

docker volume create n8n_data
docker run -it --rm --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n

Access the editor athttp://localhost:5678

## Resources

* 📚Documentation
* 🔧1500+ Integrations
* 💡Example Workflows
* 🤖AI & LangChain Guide
* 👥Community Forum
* 📖Community Tutorials

## Support

Need help? Our community forum is the place to get support and connect with other users:community.n8n.io

## License

n8n isfair-codedistributed under theSustainable Use Licenseandn8n Enterprise License.

* Source Available: Always visible source code
* Self-Hostable: Deploy anywhere
* Extensible: Add your own nodes and functionality

Enterprise Licensesavailable for additional features and support.

Additional information about the license model can be found in thedocs.

## Contributing

Found a bug 🐛 or have a feature idea ✨? Check ourContributing Guidefor a setup guide & best practices.

## Join the Team

Want to shape the future of automation? Check out ourjob postsand join our team!

## What does n8n mean?

Short answer:It means "nodemation" and is pronounced as n-eight-n.

Long answer:"I get that question quite often (more often than I expected) so I decided it is probably best to answer it here. While looking for a good name for the project with a free domain I realized very quickly that all the good ones I could think of were already taken. So, in the end, I chose nodemation. 'node-' in the sense that it uses a Node-View and that it uses Node.js and '-mation' for 'automation' which is what the project is supposed to help with. However, I did not like how long the name was and I could not imagine writing something that long every time in the CLI. That is when I then ended up on 'n8n'." -Jan Oberhauser, Founder and CEO, n8n.io