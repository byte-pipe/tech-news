---
title: Bringing uv and ty together
url: https://astral.sh/blog/uv-ty-integration
site_name: hnrss
content_file: hnrss-bringing-uv-and-ty-together
fetched_at: '2026-10-24T14:29:59.227852'
original_url: https://astral.sh/blog/uv-ty-integration
date: '2026-10-20'
description: Experimental uv-ty integration enables first-class support for Python scripts on the CLI and in the editor, and a unified uv check command.
tags:
- hackernews
- hnrss
---

Back to blog

October 
 13, 
 2026

# Bringing uv and ty together

##### Sara Sklenka

@
sarasklenka

TL;DR:Experimental uv-ty integration is now available, enabling first-class support for Python
scripts (on the CLI and in the editor) and a unifieduv checkcommand.

This is a step towards an integrated Astral toolchain, one that uses a shared understanding of your
project to enable entirely new capabilities.

At Astral, we build high-performance tools for the Python ecosystem:uv, our package manager;Ruff, our linter and formatter; andty, our type checker and language server.

Historically, each Astral tool has focused on making a different component of Python development
more productive. But we see an opportunity to further Python by unifying traditionally separate
capabilities into an integrated toolchain.

Our vision for the Astral toolchain is simple: while each tool should be individually usable,
useful, and interoperable with the rest of the ecosystem, they should be even more capable when used
together.

Today, we’re announcing an experimentalintegration between uv and ty, available in preview. uv
understands your Python project’s environment and dependencies, while ty understands your code. By
combining the two, we can unlock new functionality beyond what either tool can provide individually.

## First-class support for Python scripts#

PEP 723enables Python scripts to declare their dependencies
and Python version requirements through inline metadata. uv already uses this metadata to prepare an
environment when running a script. Now, ty can use this metadata to understand your scripts.

On both the command line and in the editor, ty now uses inline metadata to discover scripts
throughout your project and leverages uv to prepare an environment for each script. These
environments allow ty to check your scripts against their declared requirements.

Scripts can have different requirements within the same repository. Each script is checked against
its own dependency declarations, even if those dependencies or Python requirements differ from the
surrounding project.

Declare dependencies inline with PEP 723, save to sync with uv, and use ty’s completions, hover information, and Go to Definition capabilities in your editor.

Declare dependencies inline with PEP 723, save to sync with uv, and use ty’s completions, hover
information, and Go to Definition capabilities in your editor.

When the integration is enabled in your editor, ty automatically invokes uv to prepare the script’s
environment in the background, which it uses to provide type checking, code navigation, and
completions based on the script’s declared requirements.

Over time, we plan to enable script support by default, and enable automatic environment setup for
standard Python projects.

## A unified checking command#

uv checkintroduces a unified diagnostic interface to uv, starting with support for ty. Over time,
we plan to support Ruff inuv checkto unify linting and type checking into a single command.

Runninguv checkwill automatically prepare your project’s environment, install the required
dependencies, and check your project with ty. It “just works.” (If you never runuv check, nothing
changes for your uv experience; the ty binary is installed separately on first invocation.)

Withuv check, you can check individual packages, or an entire workspace. In a workspace, useuv check --package <name>to select an individual package, oruv check --all-packagesto check
every package. uv uses your workspace configuration to determine what to check, so the command stays
the same as your workspace grows.

Sync your project’s dependencies and type-check your code with a single command.

Sync your project’s dependencies and type-check your code with a single command.

Standalone PEP 723 scripts have independent environments and are checked separately. Useuv check --script example.pyto check a script using its declared requirements.

uv checkautomatically uses the ty version recorded in your project’s lockfile. Commit your
project configuration and lockfile, and developers and CI runninguv checkwill share the same ty
version without separately maintained pins.

Thety pre-commit hookalso usesuv checkunder the
hood to run ty before each commit over your Python project. By usinguv check, the hook
automatically sets up the environment for ty from your project’s dependency declarations.

## How it works#

The uv-ty integration is powered byuv workspace metadata, which gives ty a
structured view of your project or script’s packages, dependencies, and Python environment. ty then
uses this information to provide type checking and editor features that reflect the configured
environment.

For PEP 723 scripts, ty invokes uv to prepare the script’s environment, which includes installing
declared dependencies. As dependency installation can require execution of third-party Python code,
automatic environment setup is currently opt-in.

Totry the integrationfor
PEP 723 scripts in VS Code,install uvand thety VS Code extension,
then enable the uv integration in your VS Codesettings.json.

{

 
"
ty.experimental.useUv
"
:
 
"
on
"

}

You can also check your project and its PEP 723 scripts from the command line with:

TY_UV
=
scripts
 ty 
check

Runninguv checkenables the integration
automatically and requires no additional configuration.

Support for PEP 723 scripts and theuv checkcommand requires uv 0.12.3 or later, and ty 0.0.76 or
later.

## Up next#

This integration is experimental, and we’d love your feedback as we refine the experience.

While this initial support largely leverages uv’s environment capabilities to power ty execution,
we’re also working on a new category of checks that combine uv’s knowledge of your project’s
dependencies with ty’s understanding of your code (e.g., to detect unused dependencies), which we’ll
cover in a future post.

And, in parallel, we’re continuing toward ty’s stable release.

Thank you for building with us!

Thanks toAria Desires,Micha Reiser, andZsolt Dollensteinfrom the Astral team for implementing the features behind this integration.