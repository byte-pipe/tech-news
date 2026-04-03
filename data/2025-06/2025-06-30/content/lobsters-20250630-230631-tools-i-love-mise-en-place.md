---
title: 'Tools I love: mise(-en-place)'
url: https://blog.vbang.dk/2025/06/29/tools-i-love-mise/
site_name: lobsters
fetched_at: '2025-06-30T23:06:31.835395'
original_url: https://blog.vbang.dk/2025/06/29/tools-i-love-mise/
date: '2025-06-30'
description: Once in a while you get introduced to a tool that instantly changes the way you work. For me, mise is one of those tools.
tags: devops, programming
---

29 Jun 2025

# Tools I love: mise(-en-place)

tools

cli

mise

Once in a while you get introduced to a tool that instantly changes the way you work. For me,miseis one of those tools.

mise is the logical conclusion to a lot of the meta-tooling that exists around language-specific version and package managers likeasdf,nvm,uv,pyenvetc. It makes it exceptionally easy to install, use, and manage software. It also allows you to manageenvironment variablesanddeclare tasks(run commands).

# Trying out new tools

The first step in getting an intuitive understanding of what mise can help you with is to use it to install a tool. Pick your favorite and try it out; it supportsa lot!

I recently read aboutjjinThorsten Ball’s newsletterand decided to try it out (again). I crossed my fingers and hoped thatjjwasone of the tools supported by miseand, to my delight, it was! The process looked something like this:

$
jj
command_not_found_handler:5:
command
not found: jj

$
mise use jj
mise ~/projects/examples_mise/mise.toml tools: jj@0.30.0

$
jj version
jj 0.30.0

$
cd
 ..

$
jj version
command_not_found_handler:5:
command
not found: jj

$
cd
eaxmples_mise

$
jj version
jj 0.30.0

As the above shows, with mise we’re just one command away from installing and trying out a new tool, e.g.mise use jj.

In the above we that mise printedmise ~/projects/examples_mise/mise.toml tools: jj@0.30.0. This tells us that mise has created (or updated) the mise configurationon that path.We also see that if we cd out of~/projects, thejjcommand is no longer available. If we cd back into~/projects/examples_mise, it becomes available again; unless you explicitly install tools globally, mise will only make the tools available which are mentioned in amise.tomlfile on the path from your current directory to the root of your file system. That of course means that we could potentially meet multiplemise.tomlfiles when going back up to the root of the file system. Mise handles this by concatting the configurations and overwriting conflicting configurations, letting the file furthest down the tree win.

This is a clever design as it allows us to configure different versions of the same tool to be available in different directories. Let’s have a look at what themise.tomlfile looks like:

[tools]

jj

=

"latest"

If we want a specific version ofjjto be installed in a specific directory, we just update the toml file to say e.g.jj = "0.30.0.

# Managing multiple versions of a tool

Let’s see what it looks like to use mise to manage Python versions for two projects with different requirements:

$
tree

.

├── project_new
│	└── mise.toml
└── project_old
 └── mise.toml

$
cat
project_new/mise.toml

[
tools]
python
=

"3.11"

$
cat
project_old/mise.toml

[
tools]
python
=

"3.8"

$
cd
project_new

$
python
--version

Python 3.11.13

$
cd
 ../project_old

$
python
--version

Python 3.8.20

When we cd into one of the directories listed above, mise automatically makes the version of the tool configured inmise.tomlavailable to us. If it isn’t already installed, mise will install it for us. The implication of this is that you can commit amise.tomlto your repository, and anyone that has mise installed will automatically get and use the expected dev tools when they enter the project directory. And when it’s time to upgrade a dev tool, you can just update the version number inmise.tomland everyone will start using the new version!

# Use in CI/CD pipelines

The fact that mise makes tools available to you according to themise.tomlfile in your current working directory has further implications: it’s not just developer machines that can benefit from using mise; CI/CD pipelines can benefit greatly as well! When you use mise in your pipelines, you avoid the problem of having out of sync versions between developer and build machines. You get to have a single place where you can configure the version of your dev tools everywhere!

As I mentioned in the beginning, besides managing dev tools, mise also allows you todeclare and run so-called tasks. Think of a task as an advanced invocation of a bash script. Even if we use tasks as just plain bash scripts (they can do a lot more), it can be a major advantage to declare common operations such as building, testing, linting etc. as mise tasks, since all developers get access to them and will run their commands in exactly the same way every time. If you’re diligent in your naming, you can even make the experience of building or testing across projects identical.

The following are examples of some very simple Python-related tasks declared inmise.toml:

[tasks.install-deps]

run

=

[
"uv pip install -r requirements.txt"
]

[tasks.test]

run

=

[
"pytest ."
]

Adding this tomise.tomlwill make the commandsmise install-depsandmise testavailable. Again, if you check this in to your repo, the commands will be available to all developers and pipelines. And reusing these names in your rust project means that you can use the same commands to tell cargo to install your crates or run your tests.

Once you’ve declared your tasks you should of course also use them in your CI/CD pipeline. Doing this makes you less dependent on the particular yaml syntax and arbitrary requirements of your provider, and makes it easier to move to another one if you need to. It also ensures that there’s a standard way to build and test your code, helping to further reduce the amount of “it works on my machine”.

There’s a lot of depth to what you can use mise to help you automate. It’s a lovely tool and I hope I’ve spiked your interest enough to give it a try!

# Security concerns

Although this is a very obvious problem, I want to make it explicit: a major concern of all software dependency management is control of your supply chain; how easy is it for somebody to insert malicious code into a binary you will run hugely impacts the integrity of your systems and data. Depending on your industry, it might not be feasible to use mise as it’s pretty opaque where your dependencies will be downloaded from.

I'm hoping to find the time to write a series of posts over the summer on tools that I love. Here's the first one which I fell in love with just 3 months ago: misehttps://blog.vbang.dk/2025/06/29/tools-i-love-mise/

— Michael Vinter Bang (@micvbang)
December 26, 2024
