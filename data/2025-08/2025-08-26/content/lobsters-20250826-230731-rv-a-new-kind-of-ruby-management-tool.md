---
title: rv, a new kind of Ruby management tool
url: https://andre.arko.net/2025/08/25/rv-a-new-kind-of-ruby-management-tool/
site_name: lobsters
fetched_at: '2025-08-26T23:07:31.298799'
original_url: https://andre.arko.net/2025/08/25/rv-a-new-kind-of-ruby-management-tool/
author: André Arko
date: '2025-08-26'
published_date: '2025-08-25T23:21:07-07:00'
tags: ruby
---

25 Aug 2025

## rv, a new kind of Ruby management tool

For the last ten years or so of working on Bundler, I’ve had a wish rattling around: I want a better dependency manager. It doesn’t just manage your gems, it manages your ruby versions, too. It doesn’t just manage your ruby versions, it installs pre-compiled rubies so you don’t have to wait for ruby to compile from source every time. And more than all of that, it makes it completely trivial to run any script or tool written in ruby, even if that script or tool needs a different ruby than your application does.

During all those years of daydreaming, I’ve been hoping someone else would build this tool and I could just use it. Then I discovered that someonedidbuild it… but for Python. It’s calleduv, and almost exactly one year agoversion 0.3 shippedwith all the features I had wished for, and even a few more that I hadn’t thought to wish for.

Originally created as an alternative topip,poetry, and all the other Python dependency managers,uvgrew to encompass several existing tools, and has a few completely new tricks up its sleeve.

At this point, I’ve been usinguvfor almost a year and I have to say, it is really, really good. The combination of speed, reliability, and functionality creates a spectacularly good experience. No more changing a package as you install something new only to realize later you broke something old, no more setting up dependencies manually only to have the cronned script break later.

About a month ago, I decided that if there was no tool like this for Ruby, I would make one rather than keep dreaming about it. I want to bring all the tricks and innovations ofcargo,npm, anduvinto a tool for Ruby:rv.

The first and biggest trick is simply how fast everything is becauservis written in Rust, likeuvis. We expect to be able to silently run equivalents of bothrvm installandbundle installat the beginning of everybundle exec, with everything still feeling faster than it ever has before.

The next innovation isrvx/rv tool run, inspired byuvx/uv tool run. It’s likenpx/npm execorgem exec, but with superpowers. Any CLI command can run directly and immediately. No messing around with versions or dependencies, because they get installed as part of running the command. It will also be impossible for a CLI tool to conflict with your current project’s Ruby or gems, because the tool’s Ruby and gems will be installed in a separate and isolated environment.

Closely related torv tool runisrv tool install, which lets you install any gem as a CLI tool with its own separate, isolated Ruby and gems. Want to use thegistgem, even while working on an app that needs a different Ruby? No problem.rv tool install gist, and then you have agistcommand that you can run anywhere, whether you’re in another Ruby app or not.

Another “powered up” feature is script support, where a single file script contains the information from.ruby-version, fromGemfile, and fromGemfile.lock, together with the code. You can simplyrv run script.rb, and you get the Ruby you need, the gems with versions you need, and the script runs.

Ultimately, though, the biggest change from anything that exists today is combining all these tools together into one place. By managing both Ruby versions and gems at once,rvis a tool that can just run whatever you want to run. Whether it’s a CLI tool, a webapp, or a random script,rvwill always ensure your entire environment is correct as part of running the command.

Our end goal is a completely new kind of management tool, where you don’t need to install rvm and then install ruby and then update rubygems and then update bundler and then bundle install your gems and then run your actual command—you just run your command, and everything is handled.

Not a version manager, or a dependency manager, but both of those things and more. I’m currently calling this category a “language manager”, but if you have a better name idea, let me know!

After a few weeks, the team now includesSamuel Giddinsfrom the RubyGems team, andSam Stephenson, the original creator ofrbenv. We have the first step in the plan working:rvcan auto-switch between installed Ruby versions in zsh, but most importantlyit can install precompiled Ruby 3.4.x on macOS and Ubuntu in one second flat.

If you just want to try what we have so far,check out thervrepo. You can also read more aboutour future plans.

Meanwhile, if your company could use faster, more productive developers,let’s talk. We can definitely make that happen.

updated 2025-08-26:uv exec(which doesn’t exist) replaced withuvx, which does exist. thanks@xor.blueand@edmorleyfor pointing that out.
