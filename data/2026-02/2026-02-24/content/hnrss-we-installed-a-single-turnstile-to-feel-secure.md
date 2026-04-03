---
title: We installed a single turnstile to feel secure
url: https://idiallo.com/blog/installed-single-turnstile-for-security-theater
site_name: hnrss
content_file: hnrss-we-installed-a-single-turnstile-to-feel-secure
fetched_at: '2026-02-24T20:24:12.050471'
original_url: https://idiallo.com/blog/installed-single-turnstile-for-security-theater
date: '2026-02-22'
description: Security theater makes us feel safe, but it does nothing to keep us more secure. In this story I contrast real security work that was neglected with the theater
tags:
- hackernews
- hnrss
---

After the acquisition by a much larger company, security became a top priority. Our company occupied three tall buildings, each at least 13 stories high. Key card readers were installed next to every entrance, every elevator car, and even at the parking lot entrance, which itself was eight stories tall.

The parking lot system was activated first. If you wanted to park your car, you needed to scan your pass. It didn't take long for lines to start forming, but they were still manageable.

Then the doors were activated. I would often forget my key card on my desk and get stuck in the stairwell. After lunch, I'd climb the stairs all the way to the 11th floor, only to find myself locked out at the door. Fortunately, the buildings were full of people, and there was always someone to open the door for me. I'd slip in suspiciously while they contemplated the email that clearly said not to let anyone in with your own card.

While we were battling to get used to the key cards, the company was installing turnstiles on the ground floor of every building. They looked futuristic, but I was already anticipating a problem the designers hadn't considered. Each building had 13 floors. Each floor was full of employees. Hundreds of employees per building would each have to scan their card to get in.

I'm a software engineer. I understand that security isn't an optional feature you build on top of your application. Instead, you need to implement safeguards at the foundation. In fact, one of the most important applications I was working on was a tool to manage how different teams retrieved their tasks from Jira. If you've read this blog before, you know I always complain about Jira.

Anyway, the original designer of this application must have been pressed for time. Each action in the app required a call to the Jira endpoint, which needed authentication. He never saved the auth token returned by the API. Instead, each call had to re-authenticate and then perform its task.

Did he ask the user to reenter the password every single time? No, he was smarter than that. Did he save the credentials in the database in plain text? He might havebeen an intern, but he wasn't crazy. No! Instead, he saved the username and password in the cookies. But for good measures, it was base64 encoded.

Eventually, we received the email. All turnstiles were going to be activated. The following Monday, they would run in mock mode, where the turnstiles would remain open, but we'd have to scan and wait for the beep and green light before entering.

I arrived at 8:30am. I met my colleagues and hundreds of other employees in the lobby. When the first person scanned their card, the machine beeped and turned green. We all clapped in celebration. We took turns making our way to the machine. Beep, turn green, next. But it grumbled for some employees and turned red. That was fine though, it was mock day. We all went about our day.

The next day, when I came to work, I remained in my car, stuck in line for the parking lot for at least 10 minutes. Looking outside, I saw long lines of people circling each building.

I managed to park my car and discovered that the line of people extended all the way down to the parking level. I waited in line for at least 30 minutes just to make it to the lobby. I texted my manager that I'd be late for the daily standup because I was stuck in line. She didn't text back. Instead, she waved at me from the front of the line. Scanning was already slow, you had to wait to be approved. But once you passed the turnstile, there was another line for the elevators. The elevator key card readers were also active.

Imagine a couple dozen people all trying to squeeze into crowded elevators, each going to a different floor, and each trying to scan their key card to access their floor because someone who wasn't authorized for that floor couldn't scan it for them. Some elevator doors opened with a few people already inside because they couldn't scan their cards in the crowd, so they'd gone back down for a second attempt. In other words, it was complete chaos.

It took more than an hour to go from the parking lot to my desk on the 11th floor.

The next day, I decided to save time and take an Uber to work. Those were the days when anUber ride cost only $3. I thought I was being smart, but another hundred people or so had the same idea. We had a pile of Uber rides lining up outside, each trying to drop off their riders and blocking the way to the parking lot, causing yet another traffic jam. Inside the building, it was still the same chaos. I only saved a few minutes.

On the third day, they shut down the turnstiles. They clearly weren't working. They also disabled the key card readers in the elevators. It was a relief.

Security was supposedly a priority, yet nobody ever talked about the Jira credentials saved in cookies. I received significant pushback when I requested we install a Redis service to store the generated auth tokens. I had to write entire documents to justify using it and request enterprise support from a vendor. After a month, the security issue was fixed to no fanfare.

We did, however, receive an email celebrating the installation of three new turnstiles in the lobby. They never turned the elevator key card readers back on. They remained dormant, a reminder of the mess we'd gone through.

The turnstiles were visible. They were expensive. They disrupted everyone's day and made headlines in company-wide emails. Management could point to them and say that we're taking security seriously. Meanwhile, thousands of employees had their Jira credentials stored in cookies. A vulnerability that could expose our entire project management system. But that fix required documentation, vendor approval, a month of convincing people it mattered. A whole lot of begging.

Security theater checks a box. It makes people feel like something is being done. Real security is invisible. It's reviewing code, implementing proper authentication, storing tokens correctly. It doesn't come with a ribbon-cutting ceremony or a celebratory email. It's just good engineering that nobody notices when it's done right. But security theater is impossible to miss.

Did you like this article?You can buy me a coffee.Share your insightful comments here.

### Join my newsletter

Subscribe

JavaScript is required to combat spammers.

Follow me onTwitter,Spotify, orRSS
						Feed

## On a related note, here are some interesting articles.

### Why we are hiring Angular Experts

A few years ago, a meeting was held about an issue the QA team was facing. The JIRA work-flow had become too overwhelming. It was tedious to create the hundreds of sub-tasks that sometimes accompanied each feature development. The summer was approaching, so the decision was made to use the resources from the summer internship programs to snatch one of those under graduate and have him build a new system, independent of jira, to solve the problem.

### How to self-publish a book in 7 years

If you ever think about becoming a writer, then go ahead and type a single character on Google. Before your finger is off the key, Google will recommend hundreds if not thousands of material. Not just any material, good material. There are classes on Udemy, there are videos on YouTube, there are well written articles from prominent bloggers. You can join forums, clubs, guilds. There is no shortage of information to turn a complete newbie into a respectable author.

### Is Blogging Dead?

When I started 2025, I set myself a simple challenge: write consistently and see if I could reclaim some of the audience this blog once had. In 2024, I had published just 4 posts and had only a handful of RSS subscribers. It felt like shouting into the void.



				View all articles


### Comments
