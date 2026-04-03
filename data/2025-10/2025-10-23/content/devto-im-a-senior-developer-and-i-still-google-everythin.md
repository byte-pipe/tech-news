---
title: I'm a Senior Developer and I Still Google Everything (And That's Perfectly Normal) - DEV Community
url: https://dev.to/elvissautet/im-a-senior-developer-and-i-still-google-everything-and-thats-perfectly-normal-21a2
site_name: devto
fetched_at: '2025-10-23T11:13:16.785651'
original_url: https://dev.to/elvissautet/im-a-senior-developer-and-i-still-google-everything-and-thats-perfectly-normal-21a2
author: Elvis Sautet
date: '2025-10-22'
description: 'Yesterday, during a team standup, a junior developer asked me: "How do you remember all this stuff?"... Tagged with webdev, career, javascript, beginners.'
tags: '#webdev, #career, #javascript, #beginners'
---

Yesterday, during a team standup, a junior developer asked me: "How do you remember all this stuff?" I laughed. "I don't. I Google it. Every single day."

## Introduction: The Confession

Let me tell you a secret that nobody talks about in tech interviews or LinkedIn posts:

I'm a Senior Software Developer with 8 years of experience, and I Google basic stuff. Daily. Sometimes hourly.

Last Tuesday, I spent 20 minutes Googling "how to reverse an array in JavaScript" because I couldn't remember if it was.reverse()or.reversed()or.reverseArray().

It's.reverse().

I've used it a thousand times.

I still forgot.

And you know what? 58% of tech workers at companies like Google, Amazon, and Microsoft feel like impostors. That senior developer sitting next to you who seems to know everything? They're Googling basic syntax errors too.

This article is my confession. It's probably yours too. And it's time we stopped pretending.

## Part 1: Things I Googled This Week (I'm Not Kidding)

Let me open my browser history and expose myself. This is genuinely what I searched in the last 5 days:

### Monday

* "css flex align items centre not working" (I forgot to setdisplay: flex with a height of 100dvh)
* "typescript interface vs type" (for the 100th time)
* "how to exit vim" (I'm a senior dev, I still get trapped in vim)

### Tuesday

* "react useEffect cleanup function" (I know this. I just... needed to check)
* "git revert vs reset vs restore" (which one deletes the commit again?)
* "javascript sort array of objects by date" (is it ascending or descending by default?)

### Wednesday

* "how to center a div" (the classic)
* "nodejs read file" (is itfs.readFileorfs.readFileSync? I always forget)

### Thursday

* "docker compose up vs docker-compose up" (dash or no dash?)
* "sql join types visual" (I need that Venn diagram every time)
* "regex email validation" (never memorizing this, ever)

### Friday

* "how to undo git commit not pushed yet" (this is literally my most-searched query)
* "javascript array methods cheat sheet" (map, filter, reduce... which does what again?)
* "css grid template columns" (repeat(auto-fit, minmax... something something)

Every. Single. Week.

And I'm supposed to be the "expert" on my team.

## Part 2: The Lies We Tell in Job Interviews

Here's what I said in my last job interview:

Interviewer:"How proficient are you with React?"

Me:"Very proficient. I've been using React for 5 years."

Here's what I didn't say:

Me (internal monologue):"I use React daily but I still Google 'how does useContext work' every time I need it because I never use Context. I copy-paste the same useEffect patterns from previous projects. And don't even get me started on useReducer."

Interviewer:"What's your experience with TypeScript?"

Me:"Extensive. I've migrated several projects to TypeScript."

Translation:"I know how to add types to function parameters. For anything complex, I Google it or typeanyand move on. The TypeScript error messages might as well be in ancient Greek."

Interviewer:"How comfortable are you with algorithms?"

Me:"Comfortable. I understand time complexity and can implement common algorithms."

Translation:"I Googled 'binary search tree implementation' last week and copy-pasted it. I couldn't write it from scratch to save my life. Big O notation? I vaguely remember it from CS50."

We're all playing the same game. Pretending we know more than we do.

## Part 3: What "Senior Developer" Actually Means

Here's what people think "Senior Developer" means:

❌ Memorized every programming language❌ Never makes mistakes❌ Writes perfect code on the first try❌ Never needs Stack Overflow❌ Knows all the answers

Here's what "Senior Developer"actuallymeans:

✅ Knows WHAT to Google✅ Can read documentation (even when it sucks)✅ Has made every mistake already (so knows what NOT to do)✅ Can debug efficiently✅ Knows when to ask for help

The difference between junior and senior isn't knowledge. It'spattern recognition and problem-solving speed.

### Real Scenario: Junior vs Senior Dev

Problem:"The button isn't submitting the form."

Junior Developer:

1. Panics
2. Googles "button not working"
3. Reads 10 unrelated Stack Overflow posts
4. Tries random solutions
5. Breaks something else
6. 3 hours later: still broken

Senior Developer:

1. Opens dev console (first instinct)
2. Sees error: "form.submit is not a function"
3. Googles exact error message
4. Finds Stack Overflow answer immediately
5. Realizes there's a variable namedsubmitconflicting with the native method
6. Fixes in 5 minutes

Did the senior developer know the answer?Nope.

Did they know how to find it?Yep.

That's the difference.

## Part 4: The Stuff I Google Repeatedly (And Never Remember)

Even experienced developers can't remember loads of stuff because you don't use everything on a daily basis. Here are things I've Googled more than 50 times each:

### 1. Git Commands

# Things I Google constantly:

git revert
git reset
git cherry-pick
git rebase
git stash pop vs git stash apply

Enter fullscreen mode

Exit fullscreen mode

I've been using Git for 9 years. I still can't remember the difference betweenreset --soft,reset --mixed, andreset --hard.

Every time I need to undo something, it's back to Google: "git undo last commit but keep changes"

### 2. CSS Flexbox vs Grid

/* I have this Googled monthly: */

.container

{


display
:

flex
;


justify-content
:

???

/* center? space-between? I forget */


align-items
:

???

/* center? stretch? help */

}

Enter fullscreen mode

Exit fullscreen mode

I've built 100+ responsive layouts. I still need that visual guide every time.

### 3. Array Methods

// Which one flattens arrays?

.
flat
()

.
flatMap
()

.
flatten
()

// this doesn't exist but I Google it anyway

// Which one adds items?

.
push
()

// mutates

.
concat
()

// doesn't mutate

// I mix these up constantly

Enter fullscreen mode

Exit fullscreen mode

### 4. Async/Await vs Promises

// Every few months I forget:

async

function

getData
()

{


const

response

=

await

fetch
(
url
)


const

data

=

await

response
.
json
()


return

data

}

// vs

function

getData
()

{


return

fetch
(
url
)


.
then
(
response

=>

response
.
json
())


.
then
(
data

=>

data
)

}

Enter fullscreen mode

Exit fullscreen mode

I know both work. I forget which is better for what. Google knows though.

### 5. Regular Expressions

// I will NEVER memorize regex

const

emailRegex

=

/^
[^\s
@
]
+@
[^\s
@
]
+
\.[^\s
@
]
+$/

// Googled this 10000 times

// Also this:

const

phoneRegex

=

??
?

// No idea, straight to Google

Enter fullscreen mode

Exit fullscreen mode

Anyone who says they don't Google regex is lying.

## Part 5: The Google Hall of Shame

Let me share the most embarrassing things I've Googled as a "senior" developer:

### The Basics I Should Know

1. "how to declare a variable in javascript"(I panicked. Is itvar,let, orconst? In 2025, I still second-guess myself)
2. "what is the difference between undefined and null"(I know this. I teach this. I still Google it to confirm)
3. "how to write a for loop"(Classic syntax?forEach?map? I blanked during a coding interview)

### The "I Should Be Fired" Searches

1. "how to open terminal on mac"(I was showing my screen in a meeting. I froze. Couldn't remember the shortcut)
2. "javascript how to add two numbers"(In my defense, I was exhausted. Also, I forgot if+works for strings too)
3. "what is html"(I was writing documentation and second-guessed the definition. Imposter syndrome hit hard)

### The Honest Ones

1. "senior developer imposter syndrome"(This led me down a rabbit hole of "am I even qualified for my job?")
2. "is it normal to Google everything as a programmer"(Spoiler: Yes. Googling is a skill, and being good at it is what makes you a good programmer)
3. "how to quit vim"(:q!or:wq? Or is it:exit? Help.)

## Part 6: Why Juniors Think We're Wizards

Junior developers watch me work and think I'm some kind of coding wizard.

What they see:

* I type fast
* I fix bugs quickly
* I write code confidently
* I rarely get stuck

What's actually happening:

* I type fast because I've copy-pasted this pattern 1000 times
* I fix bugs quickly because I've created this exact bug before
* I write code confidently because I Googled the solution 5 minutes ago
* I rarely get stuck because I know how to Google efficiently

### The Illusion of Speed

In scripted tutorial videos, developers work super fast because they've built the application already and know how to overcome issues. But in reality, things take way longer.

What juniors see in tutorials:"I'll build this authentication system in 10 minutes!"

Reality:

* 2 hours Googling JWT implementation
* 1 hour debugging why tokens aren't being sent
* 30 minutes figuring out CORS
* 1 hour realizing you forgot to hash passwords
* 4 hours total

## Part 7: The Truth About "Knowing" vs "Finding"

Watching experienced developers making mistakes, running in the wrong direction, or searching on Google can be very helpful for a junior developer.

Here's the dirty secret of software development:

You don't need to know everything. You need to know how to find everything.

### What I Actually Memorized (Short List)

* Basic syntax (variables, functions, loops)
* Core concepts (scope, hoisting, closures)
* How to use a debugger
* How to read error messages
* How to Google effectively

### What I Google Every Time (Long List)

* Everything else

It's impossible for any developer to know everything. The tech stack is too big. Frameworks update too fast. Languages add new features constantly.

If you're memorizing APIs, you're doing it wrong.

## Part 8: The Art of Googling (A Senior Skill)

Let me teach you the actual senior-level skill:how to Google like a pro.

### Level 1: Junior Googling

Search:"button not working"

Results:10 million irrelevant results

Time wasted:2 hours

### Level 2: Mid-Level Googling

Search:"react button onclick not working"

Results:Better, but still generic

Time wasted:30 minutes

### Level 3: Senior Googling

Search:"react button onclick event.target undefined typescript"

Results:Exact Stack Overflow answer

Time saved:2 minutes

### The Senior Developer Google Formula

1. Include the technology:"react" not just "javascript"
2. Include the error message:Exact text from console
3. Include the context:"typescript" if relevant
4. Add the year:"2025" to filter old answers

Example:

❌ "how to fetch data"
✅ "react 19 fetch data async await typescript 2025"

Enter fullscreen mode

Exit fullscreen mode

### Advanced Techniques

Use site operators:

site:stackoverflow.com react hooks
site:github.com typescript error

Enter fullscreen mode

Exit fullscreen mode

Use quotes for exact matches:

"TypeError: Cannot read property 'map' of undefined"

Enter fullscreen mode

Exit fullscreen mode

Exclude results:

react hooks -class components

Enter fullscreen mode

Exit fullscreen mode

Being good at Googling saves a lot of development time.

## Part 9: The Imposter Syndrome Talk

Let's address the elephant in the room:imposter syndrome.

If you've ever felt like a fraud wondering "am I really a Developer, what do I know, I only know StackOverflow, YouTube and googling," you're not alone.

### My Imposter Syndrome Moments

Monday morning standup:

Manager:"Great work on the API integration, Elvis!"

Me (externally):"Thanks, it was straightforward."

Me (internally):"I copy-pasted 80% from Stack Overflow and don't fully understand how JWT works but it passed the tests so… 🤷‍♂️"

Code review:

Junior Dev:"Wow, how did you know to use a WeakMap here?"

Me (externally):"Performance optimization."

Me (internally):"I Googled 'javascript memory leak fix' and clicked the first link."

Technical interview (as interviewer):

Candidate:"I don't remember the exact syntax for reduce..."

Me (externally):"That's fine, understanding the concept matters."

Me (internally):"Bro, I Google reduce EVERY TIME. You're good."

### The Reality Check

58% of tech employees at Google, Microsoft, Amazon, Facebook, and Apple face imposter syndrome.

That CTO who speaks confidently?They wake up in cold sweats wondering if they've made a terrible mistake.

That architect everyone admires?They're Googling basic syntax errors.

You're not alone. You're normal.

## Part 10: What I Wish I Knew as a Junior Developer

If I could go back and talk to my junior self, here's what I'd say:

### 1. Googling is a Feature, Not a Bug

Junior me:"I shouldn't need to Google this. Real developers know this stuff."

Senior me:"Real developers know HOW to Google. The ones who pretend they don't are lying."

### 2. You'll Forget Syntax—And That's Fine

Even experienced devs can't remember loads of stuff because you don't use everything daily, so you forget things.

I've forgotten React Context syntax at least 50 times. Each time I look it up or copy-paste from another file in the project.

### 3. Copy-Pasting Isn't Cheating

Junior me:"I should write everything from scratch to really learn."

Senior me:"I've copy-pasted entire authentication systems. Just understand what you're pasting."

### 4. Nobody Knows Everything

It is impossible to stay on top of everything in tech. Technology evolves so quickly—no one can truly grasp all technologies and concepts.

Your job isn't to know everything. Your job is tosolve problems.

### 5. Mistakes Are Part of the Job

Even experienced developers spend hours on simple bugs, run in the wrong direction, and make mistakes.

Last week I spent 3 hours debugging code before realizing I had a typo in a variable name.

userIdvsusreId

Three. Hours.

I'm a senior developer.

## Part 11: Things That Actually Make You Senior

Since we've established that "knowing everything" isn't the marker of seniority, what is?

### You're a Senior Developer When:

1. You know what you don't knowJuniors fake confidence. Seniors admit ignorance and Google it.
2. You can read error messagesJuniors panic. Seniors read the stack trace and Google the exact error.
3. You've debugged the same bug beforePattern recognition. You've seen this movie.
4. You know when to ask for helpJuniors struggle for days alone. Seniors ask after 30 minutes of Googling.
5. You can explain complex things simplyBecause you've Googled it so many times, you actually understand it now.
6. You write code others can maintainBecause you've had to maintain terrible code (yours from 2 years ago).
7. You embrace not knowing"I don't know, let me Google it" isn't shameful—it's honest.

## Part 12: A Day in the Life (Real Talk)

Let me walk you through yesterday. A typical "senior developer" day:

### 9:00 AM - Morning Standup

What I said:"I'll finish the payment integration today."

What I meant:"I'll Google how to integrate Stripe for the 5th time because I forget every time."

### 10:00 AM - Start Coding

Google Search #1:"stripe payment intent react"Google Search #2:"stripe webhook signature verification"Google Search #3:"stripe test card numbers"

(I Google this EVERY project)

### 11:30 AM - Bug Appears

Error:Cannot read property 'amount' of undefined

My process:

1. Stare at code (2 minutes)
2. Addconsole.logeverywhere (5 minutes)
3. Google the error (30 seconds)
4. Find Stack Overflow answer
5. Realize I forgot to check if the object exists before accessing it
6. Face-palm
7. Addif (payment?.amount)check
8. Fixed

Total time:8 minutes

Junior developer time:Would've been 2 hours

Why?Not because I'm smarter. Because I've made this mistake 100 times.

### 2:00 PM - Code Review

Junior's code:

const

data

=

response
.
data
.
users
.
map
(
user

=>

user
.
name
)

Enter fullscreen mode

Exit fullscreen mode

My review:"What if response.data.users is undefined?"

Junior:"Oh! I didn't think of that."

What I didn't say:"I forgot to check this last week and crashed production. I learned the hard way. Now you don't have to."

### 4:00 PM - Architecture Meeting

Manager:"How should we structure the microservices?"

What I said:"We should use an event-driven architecture with a message queue."

What happened 5 minutes before:I Googled "microservice communication patterns" and read the first article.

### 5:00 PM - Helping a Junior

Junior:"How do you remember all these commands?"

Me:"I don't. I have a cheat sheet."

Me (shows bookmarks folder):

* Git Commands Cheat Sheet
* CSS Flexbox Guide
* JavaScript Array Methods
* React Hooks Patterns
* Common Regex Patterns

Junior:"Wait, you use cheat sheets?"

Me:"Every. Single. Day."

## Part 13: The Resources I Actually Use

Let me share my secret weapons (aka bookmarks I visit daily):

### My Top 10 Most-Visited Sites

1. Stack Overflow- Obviously
2. MDN Web Docs- For JavaScript/CSS reference
3. React Documentation- When Stack Overflow isn't enough
4. CSS-Tricks- For all CSS questions
5. regex101.com- Because regex is impossible
6. caniuse.com- "Can I use this CSS property?"
7. npm trends- Comparing package popularity
8. GitHub- Reading other people's code
9. DevDocs.io- All documentation in one place
10. ChatGPT/Claude- The new Google (don't judge me)

### My Chrome Bookmarks Bar

📁 Daily Use
 ├─ "git commands"
 ├─ "flex vs grid"
 ├─ "array methods"
 ├─ "async await examples"
 └─ "typescript utility types"

📁 Regex (never memorizing)
 ├─ "email validation"
 ├─ "phone number"
 └─ "url pattern"

📁 Interview Prep (for when I interview)
 ├─ "big O cheat sheet"
 ├─ "system design"
 └─ "behavioral questions"

Enter fullscreen mode

Exit fullscreen mode

## Part 14: When NOT Googling is Actually Bad

Here's a controversial take:There are times when you SHOULDN'T Google.

### Times to Figure It Out Yourself

1. Learning fundamentalsIf you're learning JavaScript and Google "how to write a function" every time, you're not learning. Practice until it sticks.
2. Debugging your own codeBefore Googling, try to understand the error yourself. Read the message. Check the line number. Think.
3. Understanding core conceptsDon't just Google "what is closure." Experiment. Break things. Understand WHY.

### The Balance

* Bad:Google every single line of code
* Good:Google when stuck after 15 minutes
* Best:Google to learn patterns, then implement yourself

## Part 15: My Advice to Junior Developers

Based on the reality that forgetting syntax daily and making mistakes is exactly what developers do, here's my advice:

### 1. Stop Feeling Guilty About Googling

All of us developers rely on Stack Overflow, YouTube, and Google. It's not a weakness—it's the job.

### 2. Build a Personal Knowledge Base

Keep notes on things you Google repeatedly:

# Git Commands I Always Forget

## Undo last commit (keep changes)

git reset --soft HEAD~1

## Undo last commit (discard changes)

git reset --hard HEAD~1

## View commit history

git log --oneline --graph

Enter fullscreen mode

Exit fullscreen mode

### 3. Learn to Read Documentation

Stack Overflow is great, but the official docs are better for understanding.

### 4. Embrace Being Uncomfortable

If you're in a room where you're not the smartest person, it means you're learning and expanding yourself.

### 5. Ask "Dumb" Questions

That "dumb" question? Three other people are wondering the same thing but are too scared to ask.

### 6. Pair Program with Seniors

Watching experienced developers make mistakes, run in the wrong direction, or search on Google can be very helpful.

You'll realize we're all just figuring it out as we go.

## Conclusion: The Liberation of Admitting You Don't Know

Here's what I want you to take away from this:

You are not an imposter for Googling things.

You are not less skilled because you forget syntax.

You are not a bad developer because you don't know everything.

You're human. And with all the information we learn continuously and countless hours spent debugging, how can we expect to memorize everything?

I've been a professional developer for 10 years. I lead a team. I make six figures. I've shipped products used by millions.

And I Google "how to center a div" at least once a month.

The difference between junior and senior isn't knowledge—it's knowing how to find knowledge fast.

So the next time you find yourself frantically Googling something "basic," remember:

Somewhere, a senior developer at Google is Googling the exact same thing.

Welcome to software development. Now stop feeling guilty and keep Googling.

## Your Turn: What Do You Google?

I showed you mine, now show me yours. What's the most embarrassing thing you've Googled as a developer?

Comment below or tweet at me@elvisautetwith your most-Googled searches. Let's normalize this.

Most Googled Hall of Fame submissions:

* "how to exit vim"
* "git push force"
* "javascript sort descending"
* "css vertical align"
* "regex email"

What's yours? 👇

## Resources (That I Google Daily)

* MDN Web Docs
* Stack Overflow
* DevDocs.io
* CSS-Tricks
* React Documentation

## About the Author

I'm Elvis Autet (@elvisautet), a Senior Full-Stack Developer with 8 years of experience and a shameless Google addiction. I've Googled "how to reverse an array" more times than I can count, and I'm not ashamed anymore.

Follow me on X:@elvisautetfor more honest developer content and terrible admissions about things I've Googled.

If this article made you feel less alone in your Googling habits,share it with a fellow developerwho needs to hear this. We're all in this together.

P.S.I Googled "how to write a good blog conclusion" before writing this. 😂

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (21 comments)


For further actions, you may consider blocking this person and/orreporting abuse
