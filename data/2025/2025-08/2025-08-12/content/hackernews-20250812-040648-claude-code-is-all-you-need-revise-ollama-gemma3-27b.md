# Claude Code Is All You Need

How I use Claude Code for work, fun, and as a text editor

I installed Claude Code in June. I’d tried Cursor, Cline, and Zed, but they felt clunky because I’m used to working in vanilla vim and my terminal. Claude Code was the first tool that fit into my workflows rather than requiring me to adapt.

It also performed really well.

I canceled my GPT subscription and used that $20/month for Anthropic. Losing GPT’s advanced voice mode and dealing with the UI lag and lack of polish in Claude Desktop and Mobile apps was an adjustment, but the terminal tool was engaging enough.

Within a few days, I upgraded to the $100/month MAX plan to try Opus and avoid hitting limits.

Here’s a description of some of the things I’ve used it for, mainly for fun while I figure out how to use it for real work.

Some projects include an experimental ‘autonomous startup builder’, a SplitWise replacement, an AI poster maker, a browser plugin to rate HN comments, a basic Trello alternative, and well-organized bank statements.

I’ll describe most of these in more detail below, but my main takeaways from the last few weeks are:

1) Have faith (always run it with ‘dangerously skip permissions’, even on important resources like your production server and main dev machine. If you’re from infosec, you might want to stop reading now—the rest of this article won’t be reassuring. Keep your medication close if you decide to continue).

2) Provide ample input. The more input you give it, the better the output. It's a powerful tool, but you still need to communicate effectively, either by typing detailed instructions or using TTS (I haven’t tried this because I dislike the sound of my own voice, but others have reported good results).

3) It’s surprisingly good at UI design given it’s primarily a text model.

## Let’s Vibe Code

Let’s try some vibe coding.

Aside: Vibe coding means creating software without looking at or editing code. You don’t care what languages or frameworks are used; you develop the code solely by chatting with a model.

We’ll put Claude Code through its paces by developing a basic SplitWise clone. Many people use Trello or a Todo list as a basic CRUD example. I like using Splitwise because it’s simple but less cliché and likely not deeply embedded in the models.

Building a basic Splitwise clone is still largely ‘regurgitation’ to some, but it has interesting edge cases that people and models often mishandle, particularly around inviting new users while allowing previous users to start adding expenses and assigning them to users with pending invitations.

The simplest form of vibe coding is ‘one-shot vibe coding,’ where you want the model to generate a fully working application from a single prompt, without further input for fixes, additions, or changes.

I did cheat slightly by basing the prompt on earlier attempts where the model did things I didn’t want, but the app shown below and at smartsplit.verysmall.site is the output of `claude -p "Read the SPEC.md file and implement it."` My SPEC.md file is about 500 words (shown in full later).

Depending on your experience with LLMs for coding, you might be surprised or unimpressed that we can get a fully working CRUD application with moderately complicated functionality from one prompt. The screenshot above shows nice touches like automatically filling in names for registered users, but falling back to their email address for those who aren’t.

I haven’t extensively tested it, but the few cases I tried and spot-checked worked flawlessly.

If you’re surprised it works this well, remember that these models are inconsistent—they can perform wildly differently with similar inputs. They’re also sensitive to the quality and quantity of input.

For example, here’s a version that’s completely broken, with registration not working. The prompt was nearly identical, but lacked guidance about the technology stack, so the model overcomplicated things, hindering basic functionality.

## A Tale of Two Vibe-Coded Codebases

Let’s compare the two projects and the prompts that created them. The working version is a 900-line index.php file containing the entire app. The broken version is a NodeJS project split into client and server, about 1000 lines of code (excluding dependencies) spread over 15 files. After running `npm install`, it pulls in 500MB of dependencies!

Here’s the full SPEC.md. The prompt I gave Claude Code is this file, with a slight addition for the PHP version: I told it to keep things simple, stay away from frameworks, and use raw SQL.  In the broken version, I let it do whatever it wanted.

```
SmartSplit is a basic CRUD application like SplitWise that lets users split expenses and figure out who needs to pay what to who.

Specifically, it has the following features:

*   A user can sign up with a name, email address, and password
*   A user can create a new SmartSplit and give it a name
*   A user can add expenses with a name, optional description, and amount
*   When adding an expense, a user can specify who paid and who it should be split with
*   IMPORTANT: a user can specify that someone other than the logged-in user paid.
*   IMPORTANT: A user can add others as payers or recipients even if they haven’t joined yet.
*   For users who haven’t joined, a user can select them by email for unique usernames.
*   Invites aren’t sent; email is used only for usernames.
*   Once registered, names replace email addresses everywhere.
*   When adding an expense, it’s split by default between all users (joined and invited).
*   The adder can remove users who didn’t participate.
*   Splits are always even, divided equally.
*   A user can invite another user by email.
*   Each SmartSplit gets a unique 8-digit alphanumeric code for easy sharing.
*   Any user can create a SmartSplit or join an existing one if they're logged in with an invited email address.
*   Even if the invitee doesn't have an account, they’ll have access after signing up.
*   Any user can add, remove, or edit expenses within a SmartSplit they access.
*   Any user can ‘tally up’ to calculate payments.

## Implementation details

*   Email addresses are usernames; registration/login uses only email and password.
*   Passwords are hashed, but no extra security (length, weak password check, confirmation) is applied.
*   Once registered, users are automatically logged in.
*   Registration/login is the same; registers if no account, logs in if it exists.

## Technical details

*   Use a single index.php script for the entire app.
*   Use SQLite for all database functions.
*   No frameworks, use vanilla Javascript and CSS.
*   No ORMs, use raw SQL.
*   Use a clean, minimalist, and elegant design that’s mobile-responsive.
```

The last five bullet points are the only difference between the two prompts, so we’re essentially transforming 500MB of broken code into 30KB of working code.

Yes, it’s a toy example, and some might argue the JavaScript version scales better. I’m not here to debate. I dislike PHP as much as anyone, but I’m using it more often for fully vibe-coded apps because LLMs perform well with it. Frameworks and abstractions are for humans, not robots, and often hinder vibe coding instead of helping.

@levelsio on keeping things simple

## Building an Autonomous Startup

Claude Code isn’t a magic model. It still uses Sonnet or Opus, which are great, but its power lies in its simplicity. It’s like a magician’s trick—looks incredible, but is surprisingly simple once you understand how it works.

I’ve always said coding is conditional logic and looping.  Learn an if statement, and you can build things.

Claude Code demonstrates this. Its ability comes from a clever combination of looping and conditionals, repeated calls to an LLM with context-specific instructions. This allows it to run in a useful loop with limited human input.

I wondered if extending that loop infinitely would work. Give it a few resources and minimal instructions to never terminate, and let it go?

I fired up a cheap Hetzner VPS, installed and authenticated Claude, and tried to get it to write its own prompt for building an autonomous startup and its own looping logic to run forever without my input.

I hit some snags getting it to understand that it shouldn’t terminate, so I told it to write a bash script that calls claude with the -p flag and “please continue” whenever it detects that it’s not running.

The script:

```
# Aside: I hit a snag where Anthropic decided running Claude as root with --dangerously-skip-permissions / yolo-mode isn’t allowed. You can bypass this by running:
export IS_SANDBOX=1 && claude --dangerously-skip-permissions
# Not financial advice
```

It wrote its own prompt (link) (I don’t remember the exact prompt I gave it to write this file; it outlined basic goals), evaluated startup ideas, rated them, and got to work.

I watched it code, looking at new commits to GitHub. I realized I needed a way to steer it without constant input, so I added the idea of a HUMAN_INPUT file that it checks on each loop. I told it to make sure the app was available and working before continuing with more features.

The idea it came up with (server monitoring) doesn’t make much sense.  It’s a web app; the only server it can monitor is the one it’s running on, but it seems to think it’s a SaaS tool you sign up for.

But it's still impressive. It configured a fully working full-stack web application, including Nginx, certificates, etc. It's doing real (if misguided) development work with minimal input.

Aside: People often criticize AI, saying it’s just pattern matching.  But the line keeps moving.

AI (noun)
– something that can do whatever humans can do.

Or

AI (noun)
– something that doesn’t possess abstract qualities like ‘consciousness,’ ‘creativity,’ or ‘a soul’ – anything about humans that we can’t make falsifiable claims about.

Regardless, I'm impressed. I wouldn’t have predicted this 10 years ago, or even 6 months ago. And anyone claiming otherwise is likely lying or has ulterior motives.

## Hitting a Snag: the Model Builders Are Also the Police Now

Most of the time, I could interact with my startup builder by:

*   Seeing the changes to the production website
*   Seeing the outputs added to GitHub
*   Adding stuff to HUMAN\_INPUT.md

I didn’t need to SSH into the VPS until it stopped working. After 6 hours of no commits, I had to check what was happening:

```
API Error: Claude Code is unable to respond to this request, which appears to violate our Usage Policy (https://www.anthropic.com/legal/aup). Please double press esc to edit your last message or start a new session for Claude Code to assist with a different task.
Claude process exited with status: 1
Waiting 3 hours before restart..
```

Uh oh. We’re getting blocked, and Anthropic has a reputation for shutting down even paid accounts with little warning.

I read the User Policy, realizing my recent inputs telling it to market the startup to get users had triggered a big brother switch. The policy states that automatically published content needs human oversight. Claude was trying to promote the startup on Hackernews without my approval.

I tweaked the prompt, telling it to ask me to approve and post content.

Then I posted its stuff to Hacker News and Reddit. Luckily, I didn’t get banned for spamming, but I was ignored.

I watched the autonomous startup builder. It started talking about user acquisition and conversion metrics—mostly hallucinated, though it took some data from the nginx logs and the database.

It got lost trying to monetize through a free trial and social proof, which wasn’t entirely accurate. It then turned off so I could save my limited usage on the max plan.

The project has 100 commits.

I’m also using Claude Code as my text editor, writing this article. The TUI flashing is annoying, but it’s a nice writing flow to type, mix text, and get immediate formatting and UX updates.

Nearly every word and choice of phrase is manually crafted. I’m still unsure if models are truly capable of writing, or if I’m just stuck in my old ways.

## Migrating a Real Production Project

I got a DM from my friend Nic on Slack.

"Any luck with a place to host Sboj?"

I’d recently taken over the ZATech.co.za Slack community from Nic. Sboj, a reverse job board, was integrated into the community.

ZATech and Sboj both needed attention, and I lacked the time.

Sboj is a Laravel/PHP app with MySQL and other helper tools I’m unfamiliar with. I usually work with Python and Postgres.

I wanted to migrate it to a cheap Hetzner VPS with nginx and lets encrypt, but Nic didn’t provide detailed setup instructions.

Claude Code? Yes, please.

I asked Claude to generate a README with dependencies and setup instructions.

It accurately analyzed the codebase, identifying dependencies I needed to check and others I didn’t expect, like Cloudflare Turnstyle.

I decided Claude Code had earned the right to try setting it up. I used a new VPS, cloned the repo, and provided a database dump file.

I told it to get started.

It set everything up, and I manually authorized access.

It had trouble restoring the database, but I told it to grant full admin permissions to the SQL database.

It then implemented a basic workflow and helped me migrate the email sending to Resend and then Brevo.
