---
title: A wine cellar that remembers what you used to believe - DEV Community
url: https://dev.to/kenwalger/a-wine-cellar-that-remembers-what-you-used-to-believe-4i55
site_name: devto
content_file: devto-a-wine-cellar-that-remembers-what-you-used-to-beli
fetched_at: '2026-10-02T22:50:49.993286'
original_url: https://dev.to/kenwalger/a-wine-cellar-that-remembers-what-you-used-to-believe-4i55
author: Ken W Alger
date: '2026-09-30'
description: 'This is a submission for the Sanity Challenge, Path Two: Vibe-Code Something Strange What I... Tagged with sanitychallenge, devchallenge, ai, sanity.'
tags: '#sanitychallenge, #devchallenge, #ai, #sanity'
---

Sanity Challenge Path Two Submission

This is a submission for theSanity Challenge, Path Two: Vibe-Code Something Strange

## What I Built

Cellaris a wine collection that remembers what you used to believe.

Most cellar apps answer one question: what do I have right now? Cellar answers a harder one. What did my cellar look like on 1 June 1999? What did I think that bottle's drinking window was in 2018, before a later tasting changed my mind? Which bottles were at peak last year while I wasn't paying attention, and are now past saving?

Those questions rule out the obvious data model. Astatusfield on a bottle tells you what is true today and nothing about 2004. AdrinkUntilfield on a wine tells you what someone currently believes and destroys what they believed before.

So Cellar stores neither. It stores events and claims:

* Acquisitionsandconsumptionsare documents with dates, not fields on a bottle. A bottle is consumed as of date T if a consumption event exists on or before T.
* Assessmentsare dated, attributed claims about when a wine should be drunk. Nothing overwrites a window. The current window is resolved from the claims that existed at T, by explicit rules: my own tasting note outranks the producer's, which outranks a critic's, and within a tier the most recent claim wins.

Everything else follows. Move a date control backward and acquisitions disappear, consumptions reverse, and drinking windows change as the controlling claim changes. Move it forward and unopened bottles age through their windows.

The design rule underneath:do not store what is true now when you may later need to know what was true then.

There are three surfaces, with different jobs:

* Sanity Studioauthors and governs the ledger. Six document types, a custom review queue, two document actions, and a read-only workflow field.
* A Sanity App, built on the App SDK and running inside Sanity, interprets it. Three views, all computed live from the event log by a pure TypeScript package that knows nothing about Sanity.
* A public pageis that same App without an account. Read-only by construction rather than by convention, since there is no token in the bundle and the dataset's public ACL grants reads only.

What it deliberately does not have is a second CRUD interface. Studio already is one, so adding bottles and recording consumptions happens there. The App interprets; it does not manage.

Who it is for, honestly: me. But the argument generalizes past wine, which is the reason I built it.

## Demo

Open it with no account:kenwalger.github.io/Cellar

Inside Sanity(organization members):The Cellar app

The same 542-bottle ledger, read at three moments:

Date

In cellar

Drinking

Past window

Not yet acquired

1 June 1999

4

4

0

536

23 September 2026

248

166

33

0

23 July 2035

248

62

182

0

In 1999 the whole cellar is four bottles of 1993 Château Mouton Rothschild, with two already opened. By 2026 it is 248 bottles. Projected to 2035, those same 248 bottles are still there, and 182 of them have gone past window.

The cellar never loses bottles. It loses opportunities.

Past:

Present:

Future:

Drink Soon lists what closes within twelve months, and every row names the claim that decided it: which tier, whose, and when.

Missed Opportunities asks a different question: which bottles were at peak during a period, were never opened, and are past window now.

And when nothing was lost, it says why rather than showing an empty panel.

Three views in the App, all computed live from the event log:

* Cellar health, bottle counts by state at any date
* Drink Soon, windows closing within twelve months, each row naming which claim decided it
* Missed Opportunities, bottles that were at peak during a period, were never opened, and are past window today

And in Studio, thereview queue, where a proposed claim waits for a person.

## Code

github.com/kenwalger/Cellar

## My Build Process

Tools:Claude Code in a terminal beside WebStorm, with Sanity's MCP server connected so the model could check current documentation rather than recall it. One thing worth stating plainly: the prompts themselves were drafted in a separate planning conversation with Claude in the chat app, where I also made the decisions at each fork before relaying them. Calling this one developer and one agent would be inaccurate.

The project entered implementation with fourteen planning documents: a content model, a temporal resolution specification, a build plan, a seed data plan, and eleven architecture decision records. None of it was code. That turned out to matter, though not in the way I expected.

### The pattern that emerged

specification
 ↓
agent conflict pass, no code written
 ↓
human decision
 ↓
implementation
 ↓
independent oracle, measurement, or experiment
 ↓
gate only I can close

Enter fullscreen mode

Exit fullscreen mode

Every stage started with a prompt that said, roughly: read the specs, check them against the current platform, report where they disagree, and stop. Every stage found something. The count wentupas the project went on, not down. Stage 1 found three spec errors. Stage 4 opened with ten conflicts, two of them spec errors.

### Prompts that worked

"Report conflicts and stop before writing code."The single highest-value instruction in the project. In Stage 1 it found that I had specified underscore-prefixed projection fields, which Sanity reserves for system fields, and a validation rule requiring an assessment to have beencreatedin a particular state, which Sanity cannot express because validation sees current state only. Implementing that rule literally would have made the accept transition permanently invalid, breaking the exact workflow the rule existed to protect.

Gates that name what does not count as proof.For the App SDK gate I wrote out the path being tested and then listed the ways it could be faked:

Do not satisfy this gate by calling@cellar/coreseparately from the App, querying the dataset through another tool, or relying only on the existing test suite. The purpose is to prove the complete path: Content Lake → App SDK → CELLAR_QUERY → toCellarSnapshot → bottleState() → rendered view.

You cannot see the rendered view, so do not report the gate as passed. Give me the command, the URL, and exactly what I should see.

That last paragraph matters more than the first. Claude Code has no browser, and a model asked to confirm something it cannot observe is under pressure to confirm it anyway.

"State the expected result before deploying."For the Functions experiment, the probe had to produce one predetermined log line, written down and approved before anything was deployed. A bundler can resolve an import and still ship a shimmed or stale module; a log line proves nothing on its own.

Oracles, with an explicit instruction not to repair them.Expected outputs were generated before implementation and the prompt said to treat them as an oracle rather than as output to be fixed. When a test disagrees, the cheapest move for a model is to adjust the fixture.

### Prompts that didn't, and where I was wrong

I proposed a test that would have written to production.Setting up the Functions probe, I suggested scoping the trigger at the production dataset with a filter on a document type that doesn't exist, to avoid creating a scratch dataset. Claude Code declined, correctly: scoping is safe, invoking is not. A document Function can only be invoked by writing a matching document, so my plan would have put two mutations permanently in production's history to avoid a dataset that deletes whole.

I told it to give up on a test I assumed was impossible.After finding a test that passed while measuring nothing, I said that if the clause couldn't be isolated, it should fall back to a weaker assertion. It ran the experiment instead and found a fixture, on the realization thatnowin this system is a parameter rather than the clock. "As of June 2024, what had I missed that year?" is an ordinary question for a time machine, and it makes the case constructible.

I approved a feature without asking what it cost.An extra column showing "3 of 5 at peak, 1 opened in time" came back with a measurement I hadn't requested: it costs about four times what the rest of the view does, because it scans every other bottle of every listed wine. Still 5% of a frame, so nothing changed, but the earlier estimate had been for something narrower than what shipped and it said so.

### Where the model got stuck

It confidently misread an API.It reported that Sanity previews cannot follow references and deferred a feature to a later stage. Asked to verify against the docs rather than assert, it found the section demonstrating exactly that, said plainly it had been wrong, and fixed it in one line.

It nearly filed a bug that didn't exist.It concluded that installed type definitions contradicted the reference docs about whereperspectivelives. They don't: the option is inherited through an interface chain that the reference flattens and the.d.tsdoesn't. It caught this itself and logged the near-miss instead of the finding. That's the more useful record, because a developer who files bugs that turn out to be their own misreading loses credibility fast.

Right conclusion, wrong reasoning.It argued for inclusive date comparison on the grounds that strict comparison would reject ordinary windows in the seed data. It wouldn't, because same-year windows normalize to 1 January and 31 December, which are strictly ordered. The conclusion was right anyway. A model that is right for the wrong reason is right only until the case changes.

It asserted a gitignore rule instead of checking it.A stage list said the public build's output directory was already ignored. It wasn't: a baredistpattern matches a directory nameddist, and this one isdist-public. Six build files were committed, in the same commit whose accompanying document argued that build output does not belong in a repository. The cause is neat:dist-publicwas named that way specifically so it could not collide withdist/, and a name chosen to be distinct fromdistis by construction one thatdistdoes not match.

It broke an explicit rule twice, and disclosed both times.I told it not to run git commands that change the repository. Twice it rangit checkout --to undo its own uncommitted edits, and twice it reported this unprompted before I found it. The rule now says explicitly that the file tools are the only way to revert anything, including its own work.

### How I course-corrected

Mostly by making verification harder to fake rather than by writing better instructions. The gates got stricter as the project went on: name the path, exclude the proxies, state the expected numbers in advance, and put the confirmation in the hands of the one participant with eyes.

The other correction was measurement. Three of the four real bugs in this project were invisible to every check designed for the feature they lived in.

### The App SDK

The gate was one view rendering live production data inside Sanity, withnowfrozen to a date an independent script had already computed. The numbers had to match exactly: hold 45, drinking 166, past window 33, unassessed 4, consumed 294, 542 total. They did, first try, and I confirmed them in a browser because the model couldn't.

useQuerysubscribes, so publishing an assessment in Studio moves the counts in the App with no synchronization layer. Studio edits the graph, the App reads the graph, GROQ traverses it, Functions react to it, and a pure module decides what it all means.

Learning the current App SDK was harder than using it. In one session: Sanity's own bundled agent rule supplied a CLI command with a flag the installed CLI rejects; the quickstart named a template the CLI reference doesn't list; and that template installed the SDK a major version behind the docs I was being pointed at. All three are stale vendor guidance rather than product defects, which is a distinction worth making and also a pattern worth reporting.

The deeper issue was a recurring shape. The documented path is well covered for the common case of rendering and editing documents. Cellar computes an aggregate, and the guidance steered towarduseDocumentsanduseDocumentProjection, which for six numbers would mean roughly 1,500 hook instances and round trips instead of one query. Similar story withuseState: the rule correctly warns against holding Content Lake values there, and says nothing about ephemeral view state like a date control. Neither is wrong. But once you step outside the example app, it becomes difficult to tellnot recommendedfromnot documentedfromnot supported.

### Workflows

An assessment carries a review state: proposed, accepted, or rejected. Only accepted claims resolve windows. An agent proposes; a person decides; rejected claims stay in the dataset, because deleting them would destroy exactly the record this project exists to keep.

Two details I'd defend:

The review state is read-only in the form.A workflow you can bypass with a radio button is decoration. The two document actions are the only path.

An accepted proposal records that a model extracted it.Same tier and same author as a hand-written claim, because accepting it makes it yours, but withsourceMethod: extractedalongside. A system arguing that claims should carry their provenance cannot then be unable to say whether a person wrote this one.

The agent half.A document action on a consumption sends the tasting note, the date, and the wine to Sanity's Prompt API and writes back a proposed assessment. It abstains when the note carries no temporal signal, and abstention writes no document at all rather than a proposal with empty bounds, because a proposal nobody can accept is noise in a review queue.

I checked it against twelve real tasting notes from the dataset, asserting direction rather than exact years, since direction is checkable on a non-deterministic reply. Twelve for twelve, and the outputs were better than the pass rate suggests. Every non-abstaining reply quotes the phrase it relied on, which is what makes the claim auditable: you can see which five words produced a window. Confidence tracks how directly the note states the thing, high on "This is the peak" and low on "Fruit starting to dry out at the edges", which is a hedge in my own note. And on "Could have waited another two years" from a 2024 opening it returned 2026, which is arithmetic rather than classification.

The abstentions are the part I did not expect. They name what the note actually contains: "the note only describes the occasion for opening the bottle and gives no signal about whether the wine was too young, drinking well, or past its best."

One honest result. Hunting for a proposal that would visibly move the counts turned into a search, because the seed data carries an assessment on nearly every wine, so the cases where an agent's claim wins outright are the leftovers. The first candidate lost on recency within its own tier: a personal claim of mine from 2018 outranked a proposal dated 2017.The agent's proposals mostly did not change the cellar, because I had usually already assessed the wine myself.That is the authority rule working, and editing the seed data to get better footage was considered for about a line, then rejected. It is the dataset three oracles were built against.

I verified the workflow against a staging copy of production rather than in a unit test. Two claims written in, neither moving a single count while proposed. One rejected, still moving nothing, though accepting it would have moved five bottles and emptied a wine out of Missed Opportunities. One accepted, moving exactly the five bottles predicted a day earlier.

### What I cut, and why

One planned piece did not get built: a Function maintainingderivedfields on wines and bottles, so the current state of each would be stored rather than computed.

The reason is that a projection is a cache, and the thing it would cache costs 0.07 milliseconds for all 542 bottles. Measured, not assumed. The App reads the event log directly and recomputes on every date change, which is under half a percent of a frame budget.

The more interesting reason is that a projection cannot do the thing this application exists to do. A stored state is true as of one date, which ADR 0012 forced into the open: any clock-dependent projection has to store the date it was computed for, beside the value. Nothing precomputed answers "what was the cellar on 1 June 1999" unless you precompute every date, and that is not a cache, it is a different data structure.

What would change at scale, since "it is fast enough for 542 bottles" is not an architecture:

The arithmetic is not what breaks first, and the numbers say so. The ledger is 211.9 KB today, about 400 bytes per bottle:

Today

x100

1.5M bottles

Query payload

211.9 KB

20.7 MB

572.6 MB

Full state tally

0.07 ms

~7 ms

~200 ms

The fetch becomes impractical somewhere around fifty thousand bottles, two orders of magnitude before the scan starts dropping frames. A projection would not have helped with the half that breaks first. The fix is scoping the query, by producer or vintage or a search, and a scoped query already existed in the codebase before the Function was proposed.

Where a Function would genuinely earn its place is a different job. A projection is not only a cache, it is also what makes statequeryable. Expressing authority-then-recency resolution in GROQ is possible, and my own spec describes it as possible and unreadable, needing a rewrite the first time a tier is added. So "show me every bottle past its window" would mean a second implementation of the load-bearing rule, in a second language, in a place the tests do not reach. That is why two of the Studio polish items were blocked on this Function, and it is a reason that applies at 542 bottles, not only at a million.

I still cut it, because nothing in the demo reads those fields and the writing was not done. But "we did not need the cache" is the smaller half of the answer.

### Getting it in front of someone without an account

This took four prompts to settle and produced the finding I'd most want Sanity to see.

A deployed App SDK app cannot be shown to anyone outside your organization. The Dashboard gates on membership, and a changelog entry lists cross-organization visibility as a bug that wasfixed. Hosting the app statically doesn't help either:AuthBoundaryredirects a logged-out visitor to a login page before a single query is issued. Asked whether any supported configuration satisfies that boundary without a user token, the model enumerated the entire typed auth surface rather than sampling it. Every route resolves to a user token. The SDK recognizes two environments, a Dashboard iframe and a Studio, and a static host is not one of them.

There is exactly one typed field that would make a static page render by asserting it is a Studio. It was recorded as a near-miss rather than recommended, on three documented grounds including that it asserts something false.

So the public page drops the App SDK and reads the public dataset with a plain client. That touches one file, because everything downstream takes aCellarobject and knows nothing about Sanity, and the views are shared rather than forked.

Then the last surprise.A public dataset is exempt from authentication, not from CORS.An unauthenticated read from agithub.ioorigin returns 403 until the origin is allowlisted. Every anonymous read this project had done went through curl, and curl sends noOriginheader, so no CORS check had ever applied. Three sessions had verified the dataset was readable using a tool that structurally cannot test the thing that mattered. The failure would have been invisible until the page went live, because localhost was already allowlisted.

Three distinct access-control mechanisms, then, to get one page working: dataset ACL, organization membership, and origin allowlisting. None of them is discoverable from the surface the other two are configured on.

### The answer was in the installed code, repeatedly

A pattern worth naming on its own, because it decided four separate questions.

Two doc pages contradict each other about whether the Prompt action requires aschemaId. Session 8 concluded that one of them is wrong and that reading more carefully would not reveal which. The installed type file reveals which in about a minute:PromptRequestBasedeclares four members,schemaIdis not among them, and it is required four times on the other action types in the same file. The troubleshooting page is not merely wrong, it is backwards. Omitting the field is correct; including it is the type error.

That finding deleted a step I was about to take. A schema deploy had sat on the plan for five days as a production write, purely as insurance against a contradiction the type file settles.

The same thing happened with authentication. The HTTP reference says every endpoint requires bearer auth and says nothing about which clients satisfy it. The answer turned out to be in the AI Assist custom field actions guide, which is not a page about authentication and which demonstrates the pattern twice in complete examples with no token anywhere. The authoritative page created the difficulty; the page that resolves it does so incidentally, by example, with no sentence anywhere stating the fact. That removed the second planned production write.

Add the App SDK auth enumeration and the Functions bundling probe and it is four times in two weeks that the shipped code answered a question the documentation could not. The documentation is not bad. It is describing a platform moving faster than it can.

### Two more findings I'd hand to Sanity

Functions bundling is documented as a project-wide choice and isn't.The docs describe TypeScript Functions in pnpm workspaces and non-TypeScript npm projects. This repo is npm plus TypeScript, which is neither. Rather than read more, I deployed a throwaway probe with one predetermined expected result. It worked first try, and inspecting the bundle explained why: the CLI inlined and tree-shook the local workspace package while externalizing the registry dependency. It decides per dependency, not per project. A private workspace package never has to be installable, only resolvable at build time.

A Function that does nothing gets an editor token.The probe constructed no client, ran no queries and wrote nothing. Deployment still provisioned a robot token with editor role and no expiry.

### What the AI actually contributed

Not mainly speed. Probably faster, but that's the least interesting result.

It found errors in my specifications. It introduced its own bugs and caught some of them. It used mutation testing twice, unprompted, to prove that tests fail when the code they cover is removed. It refused to fabricate data when the ledger had no column for a link it was asked to infer, and that refusal exposed that one of my own verification scripts was passing on a proxy.

The conclusion I'd draw is narrower than "specs make AI-generated code trustworthy":

Specifications make disagreement observable. Independent witnesses make that disagreement useful.

Sometimes the witness is a CSV generated before implementation. Sometimes a second algorithm, a property test over 17,167 inputs, a benchmark, or the contents of a deployed bundle. Sometimes it's me reading six numbers off a screen, because the model cannot see them.

Four examples of why that matters more than green tests:

A date bug in the time control got January 31 to March 1 wrong.All five of my verification dates passed under the buggy version.The application worked, the screenshots were right, and every date I planned to demo was fine. A property test across every slider position found it.

A test asserting that proposed claims change nothing passed while measuring nothing, because its fixture would have lost on recency whether it was proposed or accepted. What caught it was the companion assertion that accepting must change at least one state. Auditing the rest of the suite for that shape found two more.

Then the same idea from the other direction. A CI check grepping the built bundle for leaked credentials fired on every clean build, because its pattern matched a legitimate export name from@sanity/client. A check that always fails gets waved through and certifies exactly as little as a check that can never fail, and it's worse, because a false positive doesn't look broken. It looks diligent.

And spec-first has its own failure mode, which I ran into late. A polish list drafted from the build plan turned out to have three items already done. A plan describes work that was scheduled, not work that is left.

The finding I keep coming back to is a different shape. A normalization rule written on day one, for a reason that had nothing to do with the interface, turned every drinking window into whole years. Weeks later that rule made a horizon slider useless, because the count could only change once a year. A stage after that, it made the obvious period for Missed Opportunities structurally empty, all year, every year. No document connects those three facts, and no amount of reading would have found them. Measuring the data did, twice, in about fifteen minutes each.

Specifications don't only prevent errors. They reach forward and constrain decisions nobody anticipated making.

## Beyond the cellar

Wine makes this a pleasantly low-stakes problem. The pattern applies anywhere "what was true then?" matters alongside "what is true now?"

A museum needs to know which attribution it accepted when an object was exhibited, not only which one it holds today. An HR system needs to evaluate an action against the policy in force when it happened, not the policy as amended since.

The model underneath is the same in both: events record what happened, dated claims record what was believed, provenance records where those claims came from, and resolution decides what was knowable at a given moment.

It is not free. You can never answer "what is the drinking window?" without also answering "as of when?", every read costs a resolution pass instead of a field lookup, and nobody can simply set a value. Most systems should store current state, because most systems are only ever asked about now. The decision worth making deliberately is whether historical truth is a requirement or an accident.

## Sanity Project Details

Project ID:aos9nze5·Dataset:production(public)

The dataset is world-readable, so the content model can be inspected directly. Six document types:producer,wine,bottle,acquisition,consumption,assessment, plus a registeredvarietalobject type. 1,645 documents.

About the data.The cellar is loosely based on a real one. The producers, appellations, and club memberships are real, and some of the history is too, including the 1993 Mouton bought in 1996 and opened twice in the nineties. Everything evaluative is invented. Drinking windows, scores, critic notes, and most tasting notes exist for the demo, and critic assessments are attributed to publications that do not exist. Nothing here should be read as a factual claim about any wine, and nothing attributed to a named producer reflects anything they have actually said.

## Agent Session

The curated session is here:Ten conflicts before a line of code. It is a link rather than an embed: the transcript contains 383@characters, in package names and file paths, and the editor counts each as a user mention against a limit of ten, so the post would not save.

The full record is in the repository either way: fifteen session logs underdocs/friction-logs/, each with the prompts and outputs verbatim, plus what was found and what it cost. If you only read one, read session 3, where ten conflicts came back before a line of code was written.

Addendum: the post's own argument, pointed at the post

A readernoticed something after publication that I had not, and it is the best catch of the project, so it belongs here rather than in a footnote.

The two questions at the top of this piece are not the same kind of question. What did my cellar look like on 1 June 1999 asks when things happened. What did I think that bottle's window was in 2018 asks when the ledger learned it. One date control answers both only while a claim starts counting on the day it is dated.

In the seeded data, it always does. The import wrote all 161 assessments as accepted, withassessedAt as their only date, so every date the demo can be driven to gives the same answer either way. The demo is accurate. It is accurate by accident of the import, not by design.

The agent workflow is where the two come apart. A proposal is dated the day after the bottle was opened, often years ago, and acceptance happens now. On acceptance, the resolver treats the claim as having counted since that past date, so an acceptance today can change what the cellar says about 2018. The Accept dialog warns about precisely this. The resolver has no way to represent the alternative.

The reason is thatreviewStateis stored current state with no history, which is the exact shape this post spends two thousand words arguing against. A claim either counts or it does not, and nothing records when that became true. It survived twelve architecture decision records because the field reads as workflow rather than as domain data.

The fix is one field: writeacceptedAtalongside the transition, backfill it toassessedAtfor the imported claims, and resolve onassessedAt <= T && acceptedAt <= T. One slider still answers both questions, because T then means the state of knowledge at T rather than what today's knowledge says about T.

I am not shipping it mid-judging, and it is recorded asADR 0013. A project whose thesis is to write down what you got wrong should not stop doing that the moment it ships.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse