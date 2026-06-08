---
title: How we turned the Replay keynote surprise into an open-source embedded playground - DEV Community
url: https://dev.to/temporalio/how-we-turned-the-replay-keynote-surprise-into-an-open-source-embedded-playground-49hm
site_name: devto
content_file: devto-how-we-turned-the-replay-keynote-surprise-into-an
fetched_at: '2026-06-08T11:00:04.784424'
original_url: https://dev.to/temporalio/how-we-turned-the-replay-keynote-surprise-into-an-open-source-embedded-playground-49hm
author: Shy Ruparel
date: '2026-06-02'
description: We handed out 2,000 tiny hackable computers at Replay. Now the whole ecosystem is open source. Here's the story of how we built and shipped them. Tagged with temporal, codesamples, contributions, durableexecution.
tags: '#temporal, #codesamples, #contributions, #durableexecution'
---

In thefirst post, I told the story of how the Replay badge went from "wouldn't it be cool if..." to thousands of circuit boards showing up at a developer conference.

This one is about what was hiding inside that surprise.

Samar Abbas, our CEO and co-founder announcing the Replay Badges

During the final keynote at Replay, our CEO and co-founder, Samar Abbas, came back on stage at the end of the session for a very "one more thing" kind of moment. He wanted to give Replay attendees one more place to deploy Temporal, then revealed that we had secretly manufactured 2,000 hardware badges for the people in attendance.

As attendees left the keynote hall, we handed them something that looked, at first glance, like a very over-engineered conference badge. Which, to be clear, it absolutely was. But it was also a tiny hackable computer: an ESP32-S3, an OLED screen, an LED matrix, buttons, joystick, motion sensor, haptics, IR, MicroPython, games, firmware updates, and enough sharp edges to remind me that embedded systems do not care about my feelings.

Now that the source is public onGitHubwith our docs live atbadge.temporal.io, I want to open the thing up and show you all the strange little systems inside it.

Because we did not just open source "some firmware."

We open sourced an entire ecosystem.

Our hard work visualized. These are the Temporal badges laid out and ready for attendees to grab after the day 2 keynote. A huge moment for me and the team!

Crowds swarming the tables to pick up their badges.

Attendees checking out their badges

## What we actually open sourced

When I say the badge is open source, I do not just mean "there is a folder of C++ somewhere." The public repo includes the firmware, hardware design package, fabrication files, docs site, release asset documentation, flashing tools, MicroPython examples, community app infrastructure, and enough context for someone else to pick up the project without needing to inherit every weird Slack thread, manufacturing panic, and half-obsolete architecture decision that got us here.

The public repo looks roughly like this:

firmware/ C++ runtime, MicroPython bridge, apps, Doom, OTA
hardware/ KiCad source, fab outputs, artwork, mechanical files
ignition/ Temporal-powered flashing workflows
docs/ public badge docs site
community_apps/ installable apps from contributors
data/ schedule, speaker, and floor bundles
release-assets/ firmware and factory image release notes

Enter fullscreen mode

Exit fullscreen mode

The goal was for the badge to stop being only a thing we handed out at Replay and become something people could inspect, modify, repair, reflash, extend, and, if they are brave enough, theoretically manufacture themselves.

The hardware package includes KiCad projects, fabrication outputs, BOM and CPL files, mechanical references, and artwork. In theory, you can take the files we published and manufacture your own badge.

In practice, this is where you discover that "open hardware" still means making friends with fab notes, component substitutions, assembly constraints, and files named things likeGBR_260331-R3.zip.

Which brings us to the first lesson.

## Hardware has different gravity

The hardware is where the project becomes physical. Every feature has to fit inside real power, space, component, manufacturing, and assembly constraints.

The badge runs on an ESP32-S3 module with 16 MB of flash and 8 MB of PSRAM. It has a 128x64 monochrome OLED, an 8x8 LED matrix, four face buttons, an analog joystick, an accelerometer, haptics, IR send and receive, USB-C, battery power, and a two-board assembly where the backplate is also part of the visual design.

That sounds like a spec list, but in hardware every bullet point is also a negotiation. The screen wants power. The LEDs want power. The battery wants to be treated like a tiny volatile roommate. The IR receiver wants timing. The buttons want debounce. The enclosure wants tolerances. The PCB wants trace routing. The manufacturer wants files in a very specific shape. The designer wants the badge to look like it belongs at Replay and not like a dev board fell into a lanyard.

Our hardware guys did not believe I was going to be useful writing code at first, which is fair. From their perspective, I was a DevRel person walking into a hardware project with a lot of opinions and an alarming amount of confidence. It took them seeing my personal hardware hacking setup: the bench, the parts, the alarming amount of half-finished projects, and the Gridfinity-filled tool chest to become fully confident in me. After that, the dynamic changed a little. I was still learning their world, but I was not a tourist in hardware.

I also want to be clear about something: at the beginning, I did not understand half of the hardware file types involved.

KiCad projects, Gerbers, CPLs, fab zips, board backups, assembly exports, pick-and-place files — all of it looked like someone had taken a normal software repo and fed it through a manufacturing portal.

Our hardware consultants were moving fast in the tools they actually use. That matters. Hardware collaboration is not shaped like web app collaboration. A lot of hardware work naturally happens through big generated files, CAD exports, board snapshots, and zip packages that are meant for humans, factories, and design tools, not for a tidy Git history.

They also contributed to the C firmware along the way, so the Git problem was not just "how do I store board files?" It was also "how do I rebase active firmware changes from people who are simultaneously thinking about traces, components, and whether a factory can actually assemble this thing?"

So, somehow, my job became translating all of that into Git: rebasing branches, separating source from generated artifacts, preserving the files a manufacturer would need, and cleaning the history enough that a future human could make sense of it. At some point the hardware guys started referring to me as the Merge Czar, which is not a job title I expected to earn on a PCB project, but here we are.

There is a commit in the hardware history literally titled "i got spooked by the datasheet." I respect that commit deeply. That is hardware development in one sentence. You read something, your stomach drops a little, and suddenly there is a new BOM, a new CPL, a new Gerber package, and an R number attached to the end of the filename.

Software teams debate commit hygiene. Hardware teams have fab revisions.

Both are valid. One of them is just much heavier on zip files.

## Firmware as joy infrastructure

The firmware had two jobs that were always in tension: create joy and delight for attendees, and make the badge easy enough to hack on that the delight could keep going after Replay.

A Replay attendee putting our fun firmware to good use

At first glance, firmware sounds like the boring layer. It is not. It is the layer that decides whether the badge feels alive.

The native C++ firmware handles boot, the OLED UI, inputs, LED animations, haptics, IR, storage, OTA updates, app launching, power behavior, the file system, and the basic resource ownership rules that keep everything from stepping on everything else.

This is where the badge became less like a single Arduino sketch and more like a tiny operating environment.

Every fun thing on the badge wants to own the same small set of resources. The screen. The buttons. The joystick. The LED matrix. The IR receiver. The filesystem. Memory. Time.

If you launch a MicroPython app, who owns the OLED? If Doom starts, what happens to the scheduler? What even is a scheduler? If an LED animation is running in the background, what happens when a game wants to take over the matrix? If IR is listening, how long can Python go without polling before frames start getting dropped? If a file is being written, what happens if power gets weird?

These are not abstract architecture questions. These are "why is this thing frozen in my hand?" questions.

The public firmware is organized into subsystems because eventually it had to be. Hardware, UI, screens, IR, boops, MicroPython, OTA, LED runtime, identity, storage, and infrastructure all got their own homes. That structure was earned, mostly by discovering what happens when too many responsibilities live in one place and then you add a deadline, a battery, and 2,000 units.

The firmware is where the badge learned how to be playful without being fragile.

Mostly.

## The badge is not a browser tab

Most of my recent software life has been in environments where memory is something you notice when the bill arrives, the page gets slow, or a process gets very dramatic in production.

Embedded work does not let you be that vague.

On paper, the badge has 16 MB of flash and 8 MB of PSRAM. It also has the ESP32-S3's 512 KB of on-chip SRAM, which is technically true in the same way that an apartment technically has floor space before you move in. By the time the runtime, stacks, radios, buffers, static data, and display code take their share, the actual headroom feels much smaller.

That sounds like a lot if you are thinking "tiny conference badge." It sounds like nothing if you are thinking "computer that runs a UI, games, Python apps, a file system, OTA updates, IR, LED animations, and Doom."

The useful mental model is that flash is the badge's persistent storage. It survives power loss and holds the firmware, OTA update slots, filesystem image, apps, data bundles, and Doom's resources. FatFS is a partition of that flash presented like a tiny disk, which is why MicroPython apps can feel like files you can inspect and edit even though underneath it is all still a carefully partitioned chunk of SPI flash.

Internal SRAM is the tiny fast workbench where the firmware keeps the things it needs right now: task stacks, driver state, Wi-Fi and TLS buffers, timing-sensitive code paths, and anything that really cannot tolerate being slow or weirdly placed. PSRAM is the bigger folding table next to it. It gives us breathing room for larger allocations like the MicroPython heap, app metadata, editor buffers, and Doom, but it is still external RAM, not a free substitute for internal SRAM.

The public firmware gives MicroPython a 2 MB heap from PSRAM. That is the friendly layer where people can write apps. But the native firmware still needs memory too: task stacks, display buffers, IR queues, JSON-ish state, app registries, file buffers, OTA metadata, Doom resources, and all the small allocations you do not think about until the badge starts behaving like it has developed opinions.

On the web, if you accidentally allocate a few extra objects in a render loop, maybe Chrome sighs at you. On the badge, you feel it immediately. A garbage collection pause is not just an implementation detail when the UI is trying to stay responsive and timing-sensitive hardware is still running.

So memory became a design material.

We reused buffers. We avoided giant temporary objects. We cared about whether something lived in internal RAM or PSRAM. We had to think about what survived reboot, what survived a firmware flash, and what would be wiped when the filesystem was replaced. We built helpers likeGCTickerandDualScreenSessionso MicroPython games could keep running without making garbage collection everyone else's problem.

This is also where I learned about MessagePack. MessagePack is a binary serialization format: it carries JSON-shaped data like arrays, maps, strings, numbers, and booleans, but encodes it as compact bytes, completely dropping the benefit of being human-readable text, while keeping all the other benefits of JSON. It exists for the moments when you still want something portable and language-friendly, but you care more about size and parsing cost than being able to open the payload in a text editor.

Before this project, I had almost exclusively reached for JSON because JSON is just what we all use. It is readable, debuggable, and extremely convenient. It is not what you want on a tiny device. The badge still generates JSON versions of the schedule, speaker, and floor data so humans can inspect the output, but the firmware consumes a MessagePack bundle instead. In the public data package, those JSON files are about 35.9 KB together; the packed bundle is about 20.6 KB. Saving roughly 43 percent on one data bundle is not life-changing on a laptop or server. On the badge, it was one more place where the project taught me that every comfortable default has a cost.

## Doom wanted everything

The OLED framebuffer is only 1024 bytes, which is adorable right up until you remember that every byte has to be drawn, rotated, copied, or handed across a boundary at the right time. The IR receive queue is small enough that "read your frames promptly" is not a suggestion. The LED matrix is tiny, but animations still want timing.

Doom is probably the best way to explain how quickly the badge stopped feeling spacious. The shareware WAD, which is Doom's asset bundle, is 4,196,020 bytes. It does not live inside the firmware binary; it lives on the flash-backed FatFS partition next to the MicroPython apps and data files. Even there, it takes up about two-thirds of the badge's 6 MB filesystem partition and almost exactly one quarter of the entire 16 MB flash chip.

The compiled Doom code and static data contribute on the order of another 330 KB to the firmware, which is about 12 percent of the current firmware image, or about 8 percent of one OTA app slot. At runtime, Doom's zone allocator reserves 2 MB of PSRAM before you count the screen buffers, luma buffer, and OLED buffer. It also uses a 24 KB internal SRAM stack for its own FreeRTOS task. FreeRTOS is the little real-time operating system under the firmware; a task is its version of a thread.

And yes, we had to leave room for OTA. That was the part of the memory map that made the flash budget feel much less like "16 MB" and much more like "two carefully guarded parking spaces." The production partition table has two app slots, each about 3.875 MB, so the badge can keep the currently running firmware while writing the next firmware image into the other slot. The current firmware binary is about 2.8 MB, which is already around 68 percent of one slot. If the firmware grows past the slot size, OTA does not happen. It does not matter that there is technically flash elsewhere; the update has to fit in the slot.

This was one of the most difficult parts of the project for our entire team. It forced embedded humility.

Every allocation felt physical.

## C++ as the kernel, MicroPython as the place I wanted to play

When I do hardware hacking for myself, I usually reach for MicroPython or CircuitPython. That is the layer where I feel fast and curious instead of precious. I can make an LED blink, read a sensor, draw something on a screen, and keep going before my brain has time to turn the whole thing into a software architecture dissertation.

So part of the badge goal was selfish in the best way: I wanted a surface where I could contribute comfortably.

But I also wanted that for everyone else.

Not everyone who gets excited by a weird piece of hardware wants to become an embedded C developer before they can make it do something personal. The badge needed a low-friction layer for people who wanted to write apps, make tiny games, animate the LEDs, draw on the OLED, use the IMU, trigger haptics, or send IR without rebuilding the firmware.

That is what MicroPython is for.

The trick was not "put Python on a badge." The trick was deciding what Python should never be responsible for.

C++ owns the scary stuff: timing-sensitive hardware, resource ownership, storage safety, recovery paths, native UI, device lifecycle, and the pieces that need to survive a Python script doing something ambitious. MicroPython gets the friendly APIs: draw text, set pixels, read buttons, move a cursor, rumble the haptics, send IR, store app state, write a little game.

That meant I also had to learn how to expose C++ functions as MicroPython functions. If MicroPython apps were going to feel like they belonged on the badge, they needed to use the same UI primitives as the native firmware: layout helpers, button prompts, icon drawing, storage helpers, input handling, and all the small pieces that make an app feel consistent instead of like a loose script that happened to run on the same hardware.

I did not expect to spend as much time as I did on glyphs.

At 128x64 pixels, a button icon is not just decoration. It is either legible or it is dust. We tested version after version of the tiny glyphs for the physical buttons because those shapes were part of the language of the badge. The first version used a Nintendo-style button layout. Then we swapped toward a PlayStation/Xbox convention. Then we discovered that most of us had already internalized the Switch version so deeply that the "more standard" mapping felt wrong, and we changed it back.

That is firmware work too. Not glamorous, exactly, but it is the difference between a hackable thing and a thing people can actually use.

For a tiny app, the badge can feel almost casual:

oled_clear
()

oled_println
(
"
Hello, Replay
"
)

oled_show
()

led_override_begin
()

led_show_image
(
IMG_HEART
)

led_override_end
()

Enter fullscreen mode

Exit fullscreen mode

You can connect over USB, use JumperIDE, inspect files, run scripts through the REPL, and iterate without treating the firmware like a locked box.

That is the part I care about most. The C++ runtime makes the badge stable enough to trust. MicroPython makes it personal enough to love.

## Games, Doom, and hidden delight

The games were partly technical demos, partly love letters to weird handheld games, and partly a way to hide little moments of surprise inside the badge.

Replay attendees doing exactly what I hoped they would! Playing with the badges

I grew up loving Nintendo DS games that treated hardware constraints as creative prompts instead of limitations. Games likeHenry HatsworthandThe World Ends with Youwere always doing something strange with two screens, odd controls, timing, and divided attention. The device shaped the play.

So once the badge had an OLED screen, joystick, buttons, accelerometer, haptics, and an LED matrix, my brain went directly to "what can this do that a normal screen cannot?"

That is how you end up with Flappy Asteroids: Flappy Bird on the lower LED matrix, Asteroids on the top OLED, and absolutely no mercy anywhere.

The current record is 27 seconds, which I understand as a number but not as a human achievement. I made the thing and I cannot reliably survive five.

Breaksnake, IR Block Battle, Synth, the drawing tools, the LED toys, the community apps — they all served the same purpose. They made the badge feel discoverable. I wanted people to keep finding things. A menu item. A hidden interaction. A weird little game. Something that made them turn to the person next to them and say, "wait, this does what?"

And then there is Doom.

Doom is funny because getting Doom running on strange hardware is almost a genre of engineering by itself. It is a joke, but it is also a test. Can the device handle input ownership? Can it render fast enough? Can it allocate the buffers? Can it pause the normal badge services and restore them afterward? Can the partition layout hold the WAD? Can release tooling distribute the pieces correctly?

On the badge, Doom runs as a guest mode. It takes over the screen and input, uses PSRAM for large buffers, renders a 160x100 view down to the 128x64 monochrome OLED, drives the LED matrix as part of the HUD, and then has to cleanly hand the device back when you are done.

That forced architectural honesty. Resource ownership stopped being theoretical once a 1993 game wanted to borrow the entire badge.

I highly recommend adding a ridiculous feature to your embedded project if you want to find out whether your abstractions are real.

## Temporal flashing Temporal badges

Flashing one badge is a command.

Flashing thousands of badges is a distributed systems problem wearing a USB cable.

At some point, manually flashing badges stops being a developer workflow and starts being a production line. You need to detect devices, build firmware, prepare the filesystem image, flash in parallel, retry failures, verify boot, sync clocks, keep logs, and know which unit failed without squinting at a dozen terminal windows.

So I built Ignition.

Ignition is the Temporal-powered flashing system in the public repo. It runs locally, no cloud required, and uses Temporal workflows to orchestrate the build and flash pipeline. It can download the latest factory image from GitHub Releases, detect connected badges over USB, start child workflows per badge, flash firmware and apps in parallel, verify the badge booted, sync the clock, and show progress through workflow history and activity heartbeats.

The point was not that existing factory flashing tools are bad. The factory already has tools that can write bytes to chips very efficiently. Ignition wrapped that kind of work in a software-shaped control plane: retries, per-badge state, logs, boot verification, clock sync, and a visible history of what happened to each physical device. That is the difference between "we flashed a batch" and "we know which badges flashed, which ones failed, why they failed, and where to pick back up."

In other words, at some point the badge project became Temporal enough that we needed Temporal to ship the Temporal badge.

Which is objectively too on the nose, but I am choosing to embrace it.

The funny thing is that this was not just brand poetry. It was useful. Temporal gave us retries, status, history, and a durable mental model for a process that involved physical devices being plugged in and unplugged in batches. The same tool we talk about for long-running software processes turned out to be a pretty good fit for "please flash this table full of 32 tiny computers and tell me which ones survived."

And now that same tool is in the public repo. You can use it to flash one badge on your desk, which is calmer than what we were doing with it, but spiritually related.

## The open-source victory lap

Getting the badge ready for open source was the victory lap after shipping these crazy things.

It was also a second engineering project.

Locally on my machine, this project lived in what I called the omni directory, which is exactly as ominous as it sounds. I have no idea how anyone else structured their copy of the work, but mine had firmware repos, hardware repos, prototype repos, QA firmware, flashing tools, event tooling, design assets, worktrees, specs, agent reports, old branches, website QA code, and the printing software I had to build for our badge generator all piled into one place.

Some of that belonged in the public artifact. Some of it very much did not. Some of it was useful context. Some of it was archaeology. Some of it was a reminder that every ambitious project creates a wake behind it.

So open sourcing the badge meant curating.

We had to remove private and event-only context. We had to make the docs usable. We had to separate source from generated artifacts. We had to package release images. We had to publish the hardware files in a form that was useful without dumping every temporary file a design tool had ever breathed on. We had to preserve licensing and third-party notices, especially because Doom brings its own legal furniture. We had to create a Community Apps path, contribution rules, and review checks so the badge could grow without turning into a tiny chaos machine.

We also had to decide what future contributors, human or AI, actually need to know.

One underrated part of the cleanup was producing a small memory layer for future agents. Not the whole project history. Not every false start. Not every conversation. Just enough context to know where the important code lives, which repos matter, what the architectural boundaries are, what old branches mean, and which parts should be treated as historical sediment instead of active direction.

That feels like a very 2026 kind of maintainability problem.

Open source is no longer only about code being available. It is about whether the next person, or the next coding agent helping that person, can arrive in the project and become useful before they get overwhelmed. As my colleagueCornelia Davisput it in a line that has been rattling around in my head for months: "We are no longer just teaching humans, we are teaching agents now."

The public repo is not the whole messy garage. It is the workbench after we cleaned it enough that someone else could actually build something there.

## The second life of the badge

The badge did its job at Replay if it made people smile.

And something that made me smile — after all the hard work, seeing the badges in the wild hanging around attendees necks

It keeps doing its job if people keep changing it.

That was the whole point. We did not want to make 2,000 objects that felt magical for three days and then became drawer fossils. The badge has a second life because the firmware is open, the hardware files are there, the docs are readable, MicroPython is embedded, and the community app path exists.

Badge.temporal.io

You can reflash it. You can write an app. You can install community apps. You can inspect the hardware. You can try to manufacture one if you are feeling brave. You can make the LED matrix do something wonderful or cursed. You can build a tiny game. You can make an IR remote. You can find some corner of the device we did not fully explore and make it yours.

If the first life of the badge was surprise, I hope the second life is mischief.

Everything you need is atbadge.temporal.ioand all the code is up onGitHubready for you to clone.

github.com/temporal-community/badge.temporal.io

We have also made updates since Replay, so even if your badge worked perfectly at the conference, you will want to update your firmware.

Flash it, fork it, write an app, inspect the hardware files, submit a PR with a Community App or a fix, or send us something weird enough that I have to stop what I am doing and try it.You can submit any cool stuff in thisSlackchannel.

We also have a few extras, and we will be sharing them with people at our San Francisco events over the next few months. So if you missed Replay,come find us.

There may still be a tiny hackable computer waiting for you to put your name on it.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse