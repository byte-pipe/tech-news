---
title: Zed Is Our Office — Zed's Blog
url: https://zed.dev/blog/zed-is-our-office
site_name: hackernews
fetched_at: '2025-11-14T11:07:48.872214'
original_url: https://zed.dev/blog/zed-is-our-office
author: sagacity
date: '2025-11-14'
published_date: 11/13/2025
description: 'From the Zed Blog: A look at how we use Zed''s native collaboration features to run our entire company.'
---

← Back to Blog

# Zed Is Our Office

It's Monday, 12 PM ET, and the entire Zed Industries team is piled into our weekly all-hands meeting.
Some teammates jot down their schedule deviations, while others detail what they intend to focus on for the week.Nathanjust wrapped up top-of-mind announcements andMorganis sharing trends from our metrics and covering operational updates.
Meanwhile I'm preparing user quotes from the last week to share out, and others add topics to theDiscussionssection.

Throughout the meeting, screens are being shared, various voices are popping in and out of the conversation, and our notes are growing rapidly as dozens of cursors are concurrently editing the same file in real-time.

This entire meeting is taking place inside Zed.

Our weekly "all hands" Monday meeting in Zed

Our mission from the beginning has been to engineer an editor that will be:

1. Responsive: The latency between keystroke and re-render should be imperceptible.
2. Focused: The interface should offer minimal distractions and stay out of the code's way.
3. Collaborative: Working with teammates should feel no different than sitting next to them in the office.

Setting the first two properties aside, let's focus on collaboration.

## Collaboration Built into Zed's DNA

We've been dreaming of building the ultimate collaborative editor for years.
The roots of this vision go back to Nathan's early days atPivotal Labs, wherepair programming with two keyboards plugged into the same computerwas the standard practice.
We set out to recreate that seamless collaboration experience—but for distributed teams.

But wait... doesn't this technology already exist in other editors?

Yes!
If you've been a developer long enough, you might recall theteletypepackage forAtom—both built by Zed's founders.
Teletype enabled developers to share "portals" into their workspaces, which was an initial step towards Zed's collaborative vision.
Despiteattemptsto make Atom—anElectronapplication—more responsive, it never reached the performance standards the team yearned for.
Nathan left the Atom team and eventually began work ongpui, Zed's GPU-accelerated UI rendering framework, written in Rust, and Atom would later besunset by GitHubafter.
No more Atom, no more Teletype.

Other editors have added their versions of collaboration, but the landscape still falls short.
Setup is just tedious enough to be a hassle; you often have to install extensions, and paste links into a terminal or editor every time you want to share.
Concurrent edits don't merge cleanly, performance degrades quickly as more collaborators join, and worst of all, you often resort to sharing your screen over a Slack or Zoom anyway.

We engineered Zed from the ground up to be collaborative—it isnota bolt-on serviceoran afterthought.

LeveragingCRDTsas our core data structure, we ensure conflict-free and eventually consistent properties where everyone's changes merge seamlessly and converge to the same state.
You shouldn't have to worry about performing cursor gymnastics in order to avoid fatal flaws in the collaboration service.
Our architecture provides low latency, whether coworkers are in the same office or across an ocean, and performance remains snappy whether you're working in a pair or mob programming.

Setup is effortless: no extensions to install, no per-session links to copy and paste; only your GitHub handle is required.
And with built-in audio and automatic switching to screensharing, there's no need to fall back to external tools when you need to communicate work happening outside the editor.

We built Zed's collaboration service primarily for ourselves, so we can effectively build Zed, in Zed, together.
This isn't just a feature for us—it'svitalfor how we work.
We've both benefited and find great joy in using Zed's collaboration service, and we think you will too!

## A Speed Run of Zed's Collaboration Tools

Overview of collaboration

* 1: The collaboration panel is opened by clicking the people icon in the status bar, and becomes accessible after you have signed in through the GitHub authentication flow.
* 2: This area houses virtual rooms called "channels" that are organized in a hierarchical structure.
* 3: Create top-level channels by clicking the+button.
Create nested children channels by right clicking an existing channel and selecting theNew Subchanneloption.
* 4: GitHub avatars show who is in which channel.
Click a channel's name to join it.
* 5: Click the document icon to access its "channel notes," which serves as metadata associated with the channel.
* 6: Once in a channel, mute/unmute your voice via the microphone icon.
* 7: Allow others the option to view your screen.
* 8: Channels areproject agnostic.
Projects are voluntarily sharedthroughthem via theSharebutton in the title bar.
Channels can be public (🛜) or restricted to specific members (#️⃣), and include a permissions system withGuest,Member, andAdminroles.
* 9: Click an avatar in the title bar to follow a teammate.
If you are following someone who is sharing their screen, Zed will automatically switch between following their cursor in your Zed instance and their screen share, depending on whether they are focused on Zed or another application.

See ourFAQson data and privacy regarding collaboration.

## Our Virtual Office

Our office is Zed's collaboration panel.

A sliver of Zed Industries' channel tree

Our channel treehas been through many iterations as our company has grown, but what we have today is a structure flexible enough to accommodate many forms of collaboration.
Our channel tree is used for:

* Company-wide discussions
* Working on projects
* Individual focus time

### Company-Wide Discussion Spaces

While any channel can technically be categorized and used as a "meeting" space, we have a few designated for "all-hands" meetings.
These channels are used for checking in, knowledge dissemination, and reflection.
Projects aren't typically shared through these meetings; the work happens directly in channel notes.
Some examples:

* Every Monday, we jump into thethis weekchannel to discuss our plans for the week, review metrics, and discuss any pressing matters we need to act on.# Monday, November 10, 2025## Schedule Deviations...## Focus Areas-Max: edit predictions-Katie: Git, student plan, RBAC, blogggsssss-David: Git (Multibuffer perf)-Lukas: Windows / Multibuffer-Ben: ACP + Meetup-Cole: side-by-side diff, git PRs-Ben K: zeta2-Julia: windows bugs-Anthony: git work 😀-Smit: community board, issues replies, pr triage-Finn: Community board, extension org CI-Bennet: AI Quality, setting up evals-Conrad : Extension store test; move auto-updated to cloud-Antonio: Meetup + DeltaDB-Mikayla: Multi Agent-Kirill: rainbow brackets; PRs-Lena: github issues visibility, community board-Oleksiy: zeta2-Dino: community board, issues replies, pairing on runnables and performance-Joseph: Community, building zed in zed blog-Mary: PM hiring, BE## Biz Corner...
* Theretrospectiveschannel is occupied every 6 weeks.
In this meeting, every staff member is encouraged to add bullet points under categories likewhat went well?andwhat could have gone better?, and upvote which items we will discuss during this time slot to learn from.# Friday, September 19, 2025### What went well-⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ We keep launching-⭐⭐⭐⭐⭐⭐⭐⭐⭐ ACP Launch amazingly positively received-⭐⭐⭐⭐⭐⭐⭐⭐ Serious traction on DeltaDB-⭐⭐⭐⭐⭐⭐⭐ Loving the progress on Windows and excited about the launch-⭐⭐⭐⭐⭐ Investment in Cloud really feels like it's paying off with this billing work-⭐⭐⭐⭐ Edit prediction progress-⭐⭐⭐ Better stability in our dependencies (esp tree-sitter, no more segfaults hooray)-⭐⭐ New team members are doing great-⭐⭐ Strong strong engagement via PRs (and many merged)-⭐ Getting Codex ACP integration off the ground has been smoother sailing than Claude Code, thanks to codex-rs being open-source (1000%)...### What could have gone better-⭐⭐⭐⭐⭐⭐⭐⭐⭐ We had multiple regressions that @Kirill spotted in nightly but made it to stable-Auto-update-Throwing away unnamed buffers=> action item: ping @first-responders-⭐⭐⭐⭐⭐⭐⭐⭐⭐ Auto-update breakage (I know a subset already retro'd on this)-We have a test for this now-I think we needed to experience this once in order to realize we needed to add testing here-⭐⭐⭐⭐⭐ PR backlog is growing again :/-⭐⭐ Wish there was a windows laptop I could buy that is good
* Meetings don't have to be a drag.
Thedemoschannel is used every Friday and is considered by the team to be a "banger."
Staff members hop in, volunteer to show off a cool feature or bug fix they worked on, and get real-time feedback from the rest of the team.Lukas shares a feature in the Friday demos meeting

In addition to channels for specific company-wide meetings, we have a handful ofgeneralized meeting roomsfor one-offs that don't fit elsewhere and don't demand a dedicated space.

Our generalized meeting rooms (featuring a lonely developer, looking to pair)

For a company building a text editor, it felt right to name these meeting spaces after legendary typing machines of the past.

### Project-Specific Spaces

We structure channels and teams around specific projects, and it's where the bulk of our collaboration happens.
Projects typically group multiple features needed for larger initiatives, such asgit 1.0,edit predictions v2,delta db, andcloud.
In these channels, a project member acts as host by sharing their Zed codebase instance for the team to collaborate on.
Channel notes will typically include a list of the members on the project, goals, links toGitHub Issues/Discussions/ project boards that we are aiming to tackle in this effort, and the overall progress of the project.

## Git 1.0



Team: Cole, Anthony, Cameron, Jakub, David

Related:



-
 Git 1.0 Board: https://github.com/orgs/zed-industries/projects/48/views/1



## Done 🎉 (celebrate then move to bottom)



...



# Key:



-
 [
D
] - Needs design

-
 [
*
] - In progress

-
 [
x
] - Done

-
 [
-
] - Paused



## Phase 1 (diffs):



-
 [
*
] [@jakub @david] Make the project diff consistently snappy, eliminate beachballs

 -
 [
*
] [
@david
] Make multibuffer 'loading' incremental

 -
 [
*
] [
@david
] Add benchmark for
`DisplayMap`
 snapshot on many file multi buffers



...



## Phase 2 (merge conflicts):



-
 [
D
] Make our merge conflicts not feel like engineer UI

 -
 🎨 conflict region highlighting

 -
 Highlight diff3 markers: https://github.com/zed-industries/zed/issues/34813.

 -
 More helpful labels for the two sides of each conflict region

-
 Add a three-way conflict resolution UI



...



## Phase 3 (panel / location / traversal):



-
 [
D
] Commit Log

 -
 https://github.com/zed-industries/zed/discussions/26511

-
 [
D
] File history UI

 -
 https://github.com/zed-industries/zed/issues/16827

 -
 Joseph: Local file history could be supported by DeltaDB

 -
 Make past commit diff more interactive (editor::OpenExcerpts, file history integration)

-
 [
D
] Separate staged/unstaged diffs (feature): https://github.com/zed-industries/zed/issues/26560.



...

Subchannels are often used to organize meeting spaces for individual components of the project.

The git 1.0 channel and its subchannels

Not all project-based channels focus on features we are adding to Zed; many exist to support non-development work like marketing, community, and metrics.

Many of our project channels are public, you can joinour channel tree, read the notes, and learn about how we build Zed, just like@FalbertengoDev.

@FalbertengoDev discovers Zed's public channels

### Personal Focus Spaces

In our tree, we have apeoplechannel.
Staff members are encouraged to add a subchannel named after themselves here.
These are our personal workspaces—our "virtual cubicles."
When a teammate is in a personal channel, it tends to send the signal: "I need some heads-down focus time to get this task over the line, but you're welcome to drop by if you need something."
Everyone on the team utilizes these slightly differently. I frequently use my channel to organize content for blog posts I want to work on.

Fun fact:This blog post was initially outlined in myblogsubchannel.

Our people channel

Astute observers might notice there are no avatars next to these channels in the above screenshot.
It isn't uncommon for these to be unoccupied because the team generally prefers to collaborate when possible!

Our virtual office is not so different from any other in-person office—we have designated spaces for meetings, working on projects, and individual focus time.
We've structured our channel tree to support workflows that empower us to operate our company, but you can structure yours however best fits your team's needs.

## Where We Are Heading

While collaboration in Zed has given us the ability to run Zed Industries from within Zed, it merelyscratchesthe surface ofhow we envision working as a team.
We're building toward a future where collaboration is continuous conversation, not discrete commits—where every discussion, edit, and insight remains linked to the code as it evolves, accessible to both teammates and AI agents.

Getting here hasn't been a straight line.
Over the years, we've paused work on collaboration to focus on features users frequently requested—agent-powered tooling,debugging,Windows support, andgit support—but our primary goals for Zedhave not changed.
As we reach parity with other editors on table-stakes features, these detours are becoming less frequent, opening us up to refocus on what we're most excited about: building the greatest multiplayer software development tool.

Collaboration as it stands today is consideredalpha, and for the time being, is free for all to use!
Peruse thesource code.

### Looking for a better editor?

You can try Zed today on macOS, Windows, or Linux.Download now!

### We are hiring!

If you're passionate about the topics we cover on our blog, please considerjoining our teamto help us ship the future of software development.
