---
title: 'The Github website is extremely slow on Safari · community · Discussion #170758 · GitHub'
url: https://github.com/orgs/community/discussions/170758
site_name: hackernews
fetched_at: '2025-08-28T22:02:04.079063'
original_url: https://github.com/orgs/community/discussions/170758
author: talboren
date: '2025-08-28'
description: The Github website is extremely slow on Safari
---

# GitHub Community

# The Github website is extremely slow on Safari#170758

Unanswered

 ghugues



 asked this question in

General

 The Github website is extremely slow on Safari


#170758

 ghugues


Aug 23, 2025

·

 27 comments

·

 35 replies


Return to top



Discussion options



Quote reply



edited

## ghuguesAug 23, 2025



-

### Select Topic Area

Bug

### Body

Over the past few months, Github has been getting slower and slower on Safari. It has now reached a point where it is unusable.

Displaying any pull request with more than a thousand lines changed or even browsing any file with a thousand or more lines of code is fully broken.

What happens:

* In Activity Monitor, the rendering process is running at 100%.
* Rendering the page is so slow, Safari displays blank space when scrolling up and down.
* Any interactive features like search is so slow it doesn't work.
* Pull request review is extremely painful (scrolling back and forth is impossible to do quickly, posting comments is extremely slow, even checking the "Viewed" checkbox sometimes takes several seconds, etc.).

I have a 16-inch MacBook Pro with a 16-cores Apple M4 Max and 48GB of RAM, using it plugged-in with performance mode enabled. It's one of the most powerful laptops on the market today. Github is the only website I know that doesn't run on it.

This is Safari specific, Google Chrome on the same machine performs way better (although it still struggles with very large pull requests). I'm using Safari 18.6 (20621.3.11.11.3) on macOS Sequoia 15.6 with no extensions installed.

BetaWas this translation helpful?Give feedback.



293


You must be logged in to vote


👍

257



😄

12



❤️

18



👀

7





All reactions

## Replies:27 comments·35 replies



Comment options



Quote reply

### github-actions[bot]botAug 23, 2025



-

💬 Your Product Feedback Has Been Submitted 🎉

Thank you for taking the time to share your insights with us! Your feedback is invaluable as we build a better GitHub experience for all our users.

Here's what you can expect moving forward ⏩

* Your input will be carefully reviewed and cataloged by members of our product teams.Due to the high volume of submissions, we may not always be able to provide individual responses.Rest assured, your feedback will help chart our course for product improvements.
* Due to the high volume of submissions, we may not always be able to provide individual responses.
* Rest assured, your feedback will help chart our course for product improvements.
* Other users may engage with your post, sharing their own perspectives or experiences.
* GitHub staff may reach out for further clarification or insight.We may 'Answer' your discussion if there is a current solution, workaround, or roadmap/changelog post related to the feedback.
* We may 'Answer' your discussion if there is a current solution, workaround, or roadmap/changelog post related to the feedback.

Where to look to see what's shipping 👀

* Read theChangelogfor real-time updates on the latest GitHub features, enhancements, and calls for feedback.
* Explore ourProduct Roadmap, which details upcoming major releases and initiatives.

What you can do in the meantime 💻

* Upvote and comment on other user feedback Discussions that resonate with you.
* Add more information at any point! Useful details include: use cases, relevant labels, desired outcomes, and any accompanying screenshots.

As a member of the GitHub community, your participation is essential. While we can't promise that every suggestion will be implemented, we want to emphasize that your feedback is instrumental in guiding our decisions and priorities.

Thank you once again for your contribution to making GitHub even better! We're grateful for your ongoing support and collaboration in shaping the future of our platform. ⭐

BetaWas this translation helpful?Give feedback.



1


You must be logged in to vote



All reactions

 9 replies






Show 4 previous replies



Comment options



Quote reply

#### rhysm94Aug 27, 2025



-

If it's possible, I think that Chrome or another seperately installed browser would perform better

That's not a solution, at all. Not least because iOS browsers are all WebKit.

BetaWas this translation helpful?Give feedback.



All reactions



Comment options



Quote reply



edited

#### neon-sunsetAug 28, 2025



-

If it's possible, I think that Chrome or another seperately installed browser would perform better

chrome monoculture must stop, please do not suggest this

BetaWas this translation helpful?Give feedback.


👍

76



👎

2





All reactions



Comment options



Quote reply

#### AlekSiAug 28, 2025



-

BetaWas this translation helpful?Give feedback.


😄

46





All reactions



Comment options



Quote reply

#### EvilscaughtAug 28, 2025



-

I used to believe in a diversity of software, now I my beliefs are void. Google is life, Google is love.

BetaWas this translation helpful?Give feedback.



All reactions



Comment options



Quote reply

#### davidmatterAug 28, 2025



-

@willsmythethis issue seems to be only relevant if you're signed-in to GitHub. No issues for me in incognito mode. Also 18.6

BetaWas this translation helpful?Give feedback.



All reactions



Comment options



Quote reply



edited

### LeLunZAug 25, 2025



-

Having the same issue, where GitHub got slower and slower in safari.

For bigger PRs I can't edit anything or press on any buttons. Seems like such a big page breaks something?I just tried it from a current branch to a really old version of one of my projects, and there are 403 commits and 855 changed files. In such a case the GitHub UI becomes completely unusable.

I also disabled all content blockers and plugins for GitHub, didn't change anything :/

(using an M3 Pro Mac with 18GB Ram)

BetaWas this translation helpful?Give feedback.



24


You must be logged in to vote


❤️

13





All reactions

 0 replies




Comment options



Quote reply

### BrentMifsudAug 25, 2025



-

Same here.

Even small PRs I can't do anything. Adding reviewers, adding labels, etc... every action on the page takes many seconds. The page often locks up as well.

This wasnt an issue a few weeks ago.

BetaWas this translation helpful?Give feedback.



35


You must be logged in to vote


👍

3





All reactions

 2 replies




Comment options



Quote reply

#### willsmytheAug 27, 2025Maintainer



-

What version of Safari are you using?

BetaWas this translation helpful?Give feedback.



All reactions



Comment options



Quote reply

#### jasonkarnsAug 28, 2025



-

Version 18.6 (20621.3.11.11.3) for me

BetaWas this translation helpful?Give feedback.



All reactions



Comment options



Quote reply

### plusplusAug 26, 2025



-

Same - I don't know what's driving the engineering behind this, but it is embarrassing. It's just getting slower and slower for no appreciable benefit.

BetaWas this translation helpful?Give feedback.



28


You must be logged in to vote


👍

14





All reactions

 5 replies




Comment options



Quote reply

#### plusplusAug 26, 2025



-

Maybe copilot is rewriting it with no human reviews.

BetaWas this translation helpful?Give feedback.


👍

23



😄

16





All reactions



Comment options



Quote reply

#### mscuthbertAug 26, 2025



-

The number of bugs going unfixed suggests that AI is not being the order-of-magnitude improvement that Github and other companies imply that it is.

(See also#167400)

BetaWas this translation helpful?Give feedback.


👍

12





All reactions



Comment options



Quote reply

#### willsmytheAug 27, 2025Maintainer



-

What version of Safari are you using?

BetaWas this translation helpful?Give feedback.



All reactions



Comment options



Quote reply



edited

#### wavdedAug 28, 2025



-

@willsmythe, I've tried the following Safari versions, same issues present in all:

* Version 18.6 (20621.3.11.11.3) - MacOS 18.6.1 Safari
* Version 26.0 (21622.1.22.11.12) - MacOS 26 Beta 8 Safari
* Release 226 (WebKit 21623.1.3.19.1) - Safari Tech Preview

For me the issue is reproduced just by loading GH dashboard and hit/and starting to type in the search bar, the whole UI slows to a crawl.

BetaWas this translation helpful?Give feedback.


👍

1





All reactions



Comment options



Quote reply



edited

#### karlcowAug 28, 2025



-

@willsmytheThis is not a regression in Safari. This is a change in the CSS of GitHub, which unfortunately hits a specific performance issue of Safari. You can contact me directly if you want.I gave information onhttps://github.com/orgs/community/discussions/170922

The two main perf bugs from WebKit have been fixed this week, but they will not be available until the next release. It would be great if GitHub frontend teams could mitigate the issue in the meantime. Also, do not hesitate to contact me for the next release if you identify perf issues before releasing to the public. That would be great to be able to better plan in advance for this kind of issue.

BetaWas this translation helpful?Give feedback.


👍

2



❤️

4



👀

4





All reactions



Comment options



Quote reply



edited

### sospedraAug 26, 2025



-

Same problem over here. Renders GitHub completely useless. Nothing works. Totally frozen.

BetaWas this translation helpful?Give feedback.



18


You must be logged in to vote



All reactions

 1 reply




Comment options



Quote reply

#### msheikhmsh-blipAug 27, 2025



-

Hope So Github will Resolve it soon

BetaWas this translation helpful?Give feedback.


👍

1





All reactions



Comment options



Quote reply

### rjernstAug 26, 2025



-

AFAICT this extends to all API actions triggered by the UI. Case in point, I just went to subscribe tothis issuein Safari, and it took more than 20 seconds before the button state switched to "Unsubscribe". I'm now writing this comment in Chrome... 👎

BetaWas this translation helpful?Give feedback.



17


You must be logged in to vote



All reactions

 0 replies




Comment options



Quote reply



edited

### wavdedAug 26, 2025



-

Our team has noticed this as well, very sluggish UI in general. Especially noticeable on pull requests and autocomplete boxes like/shortcut and command palette.

BetaWas this translation helpful?Give feedback.



15


You must be logged in to vote



All reactions

 0 replies




Comment options



Quote reply

### migueldeicazaAug 26, 2025



-

It can take up to 10 seconds for this page to load on an M3 Ultra:

https://github.com/kg/runtime/blob/73fb0e3f00cff127e996b36c493949fa7b2c38e8/src/coreclr/vm/interpexec.cpp

When I trace it, sometimes a long chunk of time is spent waiting for a network resource called "collect" that hangs the UI.

This is a trace with the Safari Tech Preview, which does not show that network hang, but it is just as slow:

The above on Safari preview, takes about 5 seconds for the first page display, it does something else, and it is still a bit hiccupy for a few more seconds.

At second 10, I started a "two page downs", and you can see it takes it about 2 seconds to render two page downs.

BetaWas this translation helpful?Give feedback.



40


You must be logged in to vote


👍

12





All reactions

 0 replies




Comment options



Quote reply

### shiltianAug 27, 2025



-

It only took about a year to go from visibly slow but usable to now annoying and completely unusable. I had to install a 3rd-party app on my Mac to automatically open all GitHub URLs in Chrome. ¯_(ツ)_/¯

BetaWas this translation helpful?Give feedback.



8


You must be logged in to vote


👍

3





All reactions

 4 replies




Comment options



Quote reply

#### salzigAug 27, 2025



-

a "protocol url router"? Sounds interesting, mind sharing?

BetaWas this translation helpful?Give feedback.



All reactions



Comment options



Quote reply

#### salzigAug 27, 2025



-

I was curious and foundhttps://github.com/johnste/finicky.

BetaWas this translation helpful?Give feedback.



All reactions



Comment options



Quote reply

#### shiltianAug 27, 2025



-

Yes, something similar to that. I'm usinghttps://sindresorhus.com/velja.

BetaWas this translation helpful?Give feedback.


👍

3





All reactions



Comment options



Quote reply

#### jasonkarnsAug 28, 2025



-

I currently use Choosy, but now I’m curious to look at these others.https://choosy.app/

BetaWas this translation helpful?Give feedback.



All reactions



Comment options



Quote reply



edited

### karlcowAug 27, 2025



-

This is probably related to some type or combinations of CSS selectors.https://github.com/orgs/community/discussions/170922

BetaWas this translation helpful?Give feedback.



7


You must be logged in to vote


👍

7





All reactions

 0 replies




Comment options



Quote reply

### felixbarnyAug 27, 2025



-

For folks looking for a temporary workaround to add labels in Safari: After creating the issue/PR go to theIssues/Pull requeststab, select the checkbox of the one you want to add a label to and use theLabelsdropdown on the table header. This works a bit better.

BetaWas this translation helpful?Give feedback.



1


You must be logged in to vote


👍

1



😄

2





All reactions

 0 replies




Comment options



Quote reply

### vlad-ivanov-nameAug 27, 2025



-

after stumbling upon yet another page struggling to render i decided to check the web inspector and it looks like at least some of the performance problems (in code browser) are caused by excessive compositing

github

vs codeberg / forgejo

maybe there's some deeper reason but github right now is literally the only website i have performance problems with in safari so in a way it's somewhat impressive

BetaWas this translation helpful?Give feedback.



14


You must be logged in to vote


👍

27



😄

9





All reactions

 1 reply




Comment options



Quote reply

#### Nemo64Aug 28, 2025



-

Actually, the issue is simple. Safari runstransformrequests on the GPU only.And Github positions every text line usingtransform: translateY, forcing Safari to create thousands of layers.Chrome only creates layers when transforms are animated or change though JavaScript. That is an optimisation that WebKit is currently missing.

Workaround is simple.Pause JavaScript execution (the page does lazy loading, that resets the workaround) and then run[...document.querySelectorAll('[style*="translateY("]')].forEach(e => {e.style.position = 'relative'; e.style.top = e.style.transform.match(/translateY\(([^)]+)\)/)[1]; e.style.transform = 'none'})It's not perfectly positioned but the page is fast afterwards.

BetaWas this translation helpful?Give feedback.


👀

2





All reactions



Comment options



Quote reply



edited

### naikrovekAug 27, 2025



-

Does this happen with the New Files Changed experience only, or does it happen no matter what you have that set to? It's a preview feature you can turn on and off by going to "Feature Preview" when you click your avatar icon.

BetaWas this translation helpful?Give feedback.



1


You must be logged in to vote



All reactions

 2 replies




Comment options



Quote reply

#### rhysm94Aug 27, 2025



-

It happens for me in both experiences.

BetaWas this translation helpful?Give feedback.


👍

3





All reactions



Comment options



Quote reply

#### shiltianAug 27, 2025



-

Both for me as well

BetaWas this translation helpful?Give feedback.


👍

2





All reactions



Comment options



Quote reply

### jasoncharnesAug 27, 2025



-

As someone who writes bugs for a living I'm careful to complain. That said, this has become a real pain point for me, personally.

It's not uncommon for me to do the following things opening a PR:

* Changing the base branch
* Writing the description
* Toggling the create button between draft and ready to review
* Assigning reviewers
* Assigning myself

I do this several times a day and within the last few weeks the page will lock upeverytime. Sometimes I'll refresh the browser and even that takes a while to perform. Historically I've had no issues with this in Safari.

BetaWas this translation helpful?Give feedback.



14


You must be logged in to vote



All reactions

 0 replies




Comment options



Quote reply



edited

### pannousAug 27, 2025



-

Better slow than not loading at all. E.g.https://github.com/pannous/hieros/wiki/1

"The wiki page took too long to render."

2600 characters in 10 seconds should be doable despite unicode?

BetaWas this translation helpful?Give feedback.



1


You must be logged in to vote


👎

9





All reactions

 1 reply




Comment options



Quote reply

#### nightpoolAug 27, 2025



-

This is off-topic, please make another thread for non-safari issues.

BetaWas this translation helpful?Give feedback.


👍

1





All reactions



Comment options



Quote reply

### winston-riley-zocdocAug 27, 2025



-

Similar problem here, starting a few weeks ago, its effectively impossible to label PRs in safari.

BetaWas this translation helpful?Give feedback.



2


You must be logged in to vote



All reactions

 0 replies




Comment options



Quote reply



edited

### vinnymacAug 27, 2025



-

I now usehttps://graphite.devinstead of GitHub because their UI works fine in Safari, they support stacked PRs, and many features GitHub does not, such as actually scrolling me to the comment I was linked to 😮

Might be a helpful workaround for anyone who uses Safari as their daily driver.

BetaWas this translation helpful?Give feedback.



1


You must be logged in to vote


👎

61



😄

1





All reactions

 0 replies




Comment options



Quote reply

### superkuhAug 27, 2025



-

And don't even think of trying to read the github website with a screen reader for accessibility for the visually impaired. If you don't runalljavascript with a bleeding edge browser then there's no text to read at all. In this sense the github website has become extremely slow during the Microsoft ownership period: the text never shows up.

BetaWas this translation helpful?Give feedback.



9


You must be logged in to vote



All reactions

 1 reply




Comment options



Quote reply

#### adincebicAug 27, 2025



-

I can confirm that accessing github with voiceover on Safari has gotten extremely slow.

BetaWas this translation helpful?Give feedback.



All reactions



Comment options



Quote reply

### xoxorwrAug 27, 2025



-

It's not just Safari, Github is slow, world class developpers can't be bothered to care about performance

Perhaps it's time to start shrinking your salaries, since money doesn't seem to translate to better software it seems

BetaWas this translation helpful?Give feedback.



9


You must be logged in to vote


👎

6



😄

2



😕

1



👀

2





All reactions

 0 replies




Comment options



Quote reply

### drborgesAug 27, 2025



-

This may be related tothis webkit bugI opened a few days ago. A fix has been released but I have not heard anything about a new Safari release yet.

BetaWas this translation helpful?Give feedback.



14


You must be logged in to vote


❤️

3





All reactions

 1 reply




Comment options



Quote reply

#### karlcowAug 27, 2025



-

seehttps://github.com/orgs/community/discussions/170922

BetaWas this translation helpful?Give feedback.



All reactions



Comment options



Quote reply

### bpavukAug 27, 2025



-

vibe-coded.I'm on GitLab now.

BetaWas this translation helpful?Give feedback.



7


You must be logged in to vote


👍

1



😄

1





All reactions

 0 replies




Comment options



Quote reply

### lukehefsonAug 27, 2025



-

I’m also seeing this slowdown quite a bit. For me it’s been noticeable on Safari for a long time, especially in PRs, but over the past few days the entire site feels sluggish as hell. Chrome is much better.

(For context: I was previously a PM at GitHub and often advocated for and discovered Safari bugs during my time there, so hopefully anyone on staff here who knows me will understand I’m not posting lightly!)

BetaWas this translation helpful?Give feedback.



9


You must be logged in to vote


❤️

3





All reactions

 6 replies






Show 1 previous reply



Comment options



Quote reply

#### rhysm94Aug 27, 2025



-

To be more explicit. It feels like a change was implemented in the last week thatreallytanked performance on Safari.

This lines up with my experience. Initially the new files experience seemed to improve things, but in the last week, I've noticed the changed files feature is unbelievably sluggish. I can barely scroll through more than a few hundred lines of change, and the page locks up.

BetaWas this translation helpful?Give feedback.


👍

2





All reactions



Comment options



Quote reply



edited

#### karlcowAug 27, 2025



-

To be more explicit. It feels like a change was implemented in the last week thatreallytanked performance on Safari.

yes recent changes in GitHub UI have hit a bug in Safari with CSS selectors.https://github.com/orgs/community/discussions/170922

BetaWas this translation helpful?Give feedback.


👍

1





All reactions



Comment options



Quote reply

#### lukehefsonAug 28, 2025



-

Thanks@karlcow- good to know@WebKitare doing what you can too!

BetaWas this translation helpful?Give feedback.



All reactions



Comment options



Quote reply

#### lukehefsonAug 28, 2025



-

This lines up with my experience. Initially the new files experience seemed to improve things, but in the last week, I've noticed the changed files feature is unbelievably sluggish. I can barely scroll through more than a few hundred lines of change, and the page locks up.

Yeah it's definitely the files experience. But I've also noticed sluggishness all around the past week or so. For example: In any comment box, when you start to type something that autocompleted (like an @mention), the character rendering slows riiiiight doooooown.

BetaWas this translation helpful?Give feedback.



All reactions



Comment options



Quote reply

#### lukehefsonAug 28, 2025



-

When I worked at GitHub I know that there was scant testing of non-Chrome browsers. At the time we relied largely on GitHub employees who use Safari (like myself) to report oddities. I would hope that in 2025 GitHub is taking multi-browser testing a bit more seriously.But if it's not— at the very least I would like to think that there are more Safari users working at GitHub in 2025 who are internally pushing to get this resolved!

BetaWas this translation helpful?Give feedback.


👍

1





All reactions



Comment options



Quote reply

### rv-ragulAug 27, 2025



-

I am also experiencing the similar rendering issue in safari

BetaWas this translation helpful?Give feedback.



2


You must be logged in to vote



All reactions

 0 replies




Comment options



Quote reply

### canpoyrazogluAug 27, 2025



-

As a Safari-only user, I didn't know it was a problem only occurring on Safari. I'm not having problems on any other sites so it's probably GH.

What's more interesting is that one of the top sites used by programmers is not testing one of the most common tasks on the website with one of the most common browsers.

Hope it gets fixed soon. Any large PRs is unworkable with Safari.

BetaWas this translation helpful?Give feedback.



6


You must be logged in to vote



All reactions

 1 reply




Comment options



Quote reply

#### uson1xAug 27, 2025



-

Wow I did not know this problem was only in safari. I assumed GitHub UI is just super slow and nobody cared.And it has been like that for a... year? Or more?It did get faster with latest PR review UI update, but still rather slow right now

BetaWas this translation helpful?Give feedback.


👍

2





All reactions



Comment options



Quote reply



edited

### zerobiasAug 28, 2025



-

Browser native back button is broken on iOS safari too. When the one navigate source code usually it doesn’t do anything but change url. Hitting back several times with no effect and reloading page in disgust leading to jump to arbitrary url in history.

Reconsider your approach to frontend development, please

BetaWas this translation helpful?Give feedback.



3


You must be logged in to vote


👍

1





All reactions

 0 replies




Comment options



Quote reply

### dlvhdrAug 28, 2025



-

Until this is fixed you can try some faster frontends like a TUIhttps://github.com/dlvhdr/gh-dash

BetaWas this translation helpful?Give feedback.



3


You must be logged in to vote



All reactions

 0 replies




Comment options



Quote reply

### el1s7Aug 28, 2025



-

Because Safari sucks, like most of Apple's software. And any dev using it and not accepting this, is in denial.

Go ahead, bring me the dislikes (hopefully the emoji interaction is still working in your Safari).

BetaWas this translation helpful?Give feedback.



6


You must be logged in to vote


👎

31





All reactions

 1 reply




Comment options



Quote reply

#### erhosenAug 28, 2025



-

It's weird that you call yourself a dev, considering your poor GitHub activity 🤔

BetaWas this translation helpful?Give feedback.


👀

1





All reactions

Sign up for free

to join this conversation on GitHub
.
 Already have an account?

Sign in to comment
