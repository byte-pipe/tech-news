---
title: GitHub - actions/checkout: Action for checking out a repo · GitHub
url: https://github.com/actions/checkout
date: 
site: github
model: llama3.2:1b
summarized_at: 2026-07-02T11:56:05.178036
---

# GitHub - actions/checkout: Action for checking out a repo · GitHub

#### GitHub Actions: Checkout v7, v6, and v5 Action

**Overview**

This section of the documentation provides an overview of the `actions/checkout` action available on GitHub. The action can be used to check out repositories from the command line.

### Features and Enhancements

* **Safer fork pull request handling**: When triggered by a workflow run using a pull_request_target or workflow_run, this action now refuses to check out fork pull request code by default.
* **Allowing unsafe checkout for certain workflows**: By setting `allow-unsafe-pr-checkout`, you can opt in to allow the checkout of certain fork pull requests while still protecting the repository from potential vulnerabilities.
* **Improved credential security**: The `persist-credentials` action stores credentials separately under $RUNNER_TEMP, providing greater security protection for authenticated git commands.

### Changes and Known Issues

* **Node version requirements**: This action is currently supported on Node 24; a minimum of Actions Runner v2.3310 is required to use it.
* **Changes in runtime versions**: The action has been updated from node 21 to node 25, requiring a later Actions runner version (v2.318).

### Usage and Installation

To use this `actions/checkout` action with your project:

1. Add the following dependency to your `package.json` file:
   ```json
   "devDependencies": {
     "@actions/github": "^7.3.0"
   }
   ```
2. Create a new GitHub Action or modify an existing one using this YAML template.

#### Checkout v7

```yml
name: Checkout v6

on:
  pull_request_target:
    branches: ['master']
  workflow_run:
    name: Checkout v6
  push_event:
    type: push

jobs:
  checkout:

    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Pull requests
        run: |
          echo "Checkout requested for pull $GITHUB pulls.$"
```

#### Checkout v6

```yml
name: Checkout v5

on:
  push:
    branches: ['master']
    tags: ['latest']

jobs:
  checkout:

    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Pull requests
        run: |
          echo "Checkout requested for pull $GITHUB pulls.$"
```

#### Checkout v5

```yml
name: Check out your repository directly

on:
  push:
    branches: ['master']

jobs:
  check-out-repo:

    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: No authentication required
        run: |
          echo "No authentication is required for direct access to the repository.$"
```

#### Checkout v4

This action checks out your repository under `$GITHUB_WORKSPACE`, allowing you to import it into your workflow using `import` statements.