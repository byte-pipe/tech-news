---
title: More than 340 local news outlets are limiting the Internet Archive’s access to their journalism | Nieman Journalism Lab
url: https://www.niemanlab.org/2026/05/more-than-340-local-news-outlets-are-limiting-the-internet-archives-access-to-their-journalism/
site_name: hackernews_api
content_file: hackernews_api-more-than-340-local-news-outlets-are-limiting-the
fetched_at: '2026-05-22T11:58:09.491666'
original_url: https://www.niemanlab.org/2026/05/more-than-340-local-news-outlets-are-limiting-the-internet-archives-access-to-their-journalism/
author: jaredwiener
date: '2026-05-21'
description: McClatchy, Advance Local, Tribune Publishing and other major newspaper chains are restricting the nonprofit's archiving bots.
tags:
- hackernews
- trending
---

May 20, 2026, 5:03 p.m.

Aggregation & Discovery

## More than 340 local news outlets are limiting the Internet Archive’s access to their journalism

McClatchy, Advance Local, Tribune Publishing and other major newspaper chains are restricting the nonprofit’s archiving bots.

By 
Andrew Deck
 
and
 
Hanaa' Tameez

May 20, 2026, 5:03 p.m.
 

May 20, 2026, 5:03 p.m.

In January, Nieman Labbroke the storythat major news publishers — including The New York Times, The Guardian, and USA Today Co. — had started blocking the Internet Archive due to concerns that AI companies might scrape the nonprofit’s repositories for training data.

No news publisher has confirmed to Nieman Lab that an AI company has already scraped their content from the Wayback Machine. Still, in the five months since we published our story the number of news sites blocking the Internet Archive has continued to rise.

RELATED ARTICLENews publishers limit Internet Archive access due to AI scraping concernsAndrew DeckJanuary 28, 2026Overwhelmingly, these sites are local news outlets.

Our new analysis shows that more than 340 local news sites across the United States are now limiting the Internet Archive’s ability to access and preserve their stories. Many sites in our sample are owned by five of theseven largestlocal news publishers in the country: USA Today Co., McClatchy, Advance Local, MediaNews Group, and Tribune Publishing. The latter two are both subsidiaries of the “vulture hedge fund” Alden Global Capital.

Researchers, historians, and citizens around the world rely on the web archives of local news sites to do their work.

“Blocking the Internet Archive’s web crawlers threatens one of the most effective ways that we capture and store news content for the long term,”Edward McCain, a journalism librarian at the University of Missouri, said. “In the present we may have some workarounds, but in the long run, it weakens a vital link in primary source materials that we need to understand where we’ve been and where we want to go.”

Working journalists are among the most frequent users of the Wayback Machine’s local news archives. Over the last month,onlinepetitionshave called for news media companies to allow the Internet Archive to preserve their journalism.

“I cover news within a larger news desert in New York’s Rockland, Sullivan, and Rockland counties. This means I need to heavily rely on archival data of old news articles from now deceased, or zombie-fied, media outlets,” wrote B.J. Mendelson, the editor ofThe Monroe Gazettenewsletter, in one recentpetition signed by over 200 journalists. “Without the Internet Archive, my [work] would be incredibly difficult to do.”

RELATED ARTICLEJournalists champion Wayback Machine after news publishers limit article archivingAndrew DeckApril 15, 2026In the face of publisher concerns, theWayback Machine has highlighted its efforts to minimize abuse of its site, including implementing systems that limit bulk downloading and working with vendors like Cloudflare to monitor bot activity. “We are in conversation with many publishers and appreciate the opportunity to address their concerns,”Mark Graham, the founder of the Wayback Machine, told Nieman Lab, noting that the Internet Archive’s terms of use only permits using its collections for scholarship or research purposes.

Meredith Broussard, a data journalist and professor at New York University, said that as profit margins for news thin, it’s only become more important to news publishers to protect their intellectual property.

“This is the same fight that everybody has been having with the Internet Archive since its inception,” Broussard said. “Internet Archive is a very old-school, ‘information-should-be-free’ organization. But the people who are invested differently have different priorities. There are lots of different historical and legal and economic issues that are colliding in this situation. AI companies [are] the catalyst for the latest skirmish in a very old battle.”

In January, Nieman Lab used journalistBen Welsh‘sdatabase of 1,167 news websites‘ robots.txt files to determine which sites were disallowing the Internet Archive. At the time, the Internet Archive did not respond to requests to confirm which crawling bots it was using, so we identified four bots that the AI user agent watchdog serviceDark Visitorshad associated with them. (You can find our full methodologyhere.)

Wefoundthat 241 news websites disallowed at least one Internet Archive-affiliated crawling bot. About 80% of these sites belonged to USA Today Co., the company formerly known as Gannett.

By May, we found that an additional 141 news websites disallowed at least one Internet Archive-affiliated bot, increasing the total number of sites in our sample to 382. Some of these additions appeared in Welsh’s database. We found others by checking robots.txt files ourselves. Our final sample includes sites in 10 countries, though the vast majority (93%) are based in the United States.

Of the 382 news sites in our updated sample, 342 are local. Of course, our data doesn’t include all the local news outlets in the United States, but it shows that many of the country’s largest local news publishers are at least attempting to limit Internet Archive access.

The scraping bots we tracked in our new analysis are Heritrix, My-heritrix-crawler, heritrix/3.3.0, Archive-It, archive.org_bot, ia_archiver-web.archive.org, and Special_archiver. (We included Archive-It, archive.org_bot, ia_archiver-web.archive.org, and Special_archiver in our January analysis. After confirming that the bot Heritrix and its variationsbelongto the Internet Archive, we added them.)

Graham told Nieman Lab that the Wayback Machine doesn’t use the bots “ia_archiver,” “ia_archiverbot” or “ia_archiver-web.archive.org.”

Third-party websites and internet forums have regularly documented “ia_archiver-web.archive.org” as an alleged user agent of the Wayback Machine. We continue to include “ia_archiver-web.archive.org” in our dataset because news publishers are disallowing the bot under the assumption that it is used by the Internet Archive.

Our full dataset can be viewed in the table below:

### “The threat is definitely not the Internet Archive”

At least 13 Advance Local news sites, including The Cleveland Plain Dealer (Cleveland.com), The Patriot-News (PennLive.com), and The Oregonian (OregonLive.com), have added the Internet Archive’s user agents in their robots.txt files.

Advance Local — a subsidiary of Advance Publications, the Newshouse family-owned media giant — confirmed to Nieman Lab it began hard-blocking the Internet Archive last August. It took the action preemptively, without evidence that its content had been scraped by an AI company via the Wayback Machine.

“This is part of a broader effort to protect the value of our published work from unfair third‑party use. This decision is not specific to the Wayback Machine,” said Christine deWit, a spokesperson for Advance Local, in a statement.

RELATED ARTICLEAfter 25 years, Brewster Kahle and the Internet Archive are still working to democratize knowledgeJoshua BentonMarch 24, 2022Alden Global Capital is another major local news chain that has rolled out new restrictions on the Internet Archive. About 60 of those sites are owned by MediaNews Group, the Alden subsidiary that operates dailies across the country, including The Mercury News, the Denver Post, and the New York Daily News. Another seven publications are operated by Tribune Publishing, most notably the Chicago Tribune.

Alden has beencriticizedfor aggressively acquiring U.S. newspapers and stripping them of resources for short-term profits. Alden did not respond to requests for comment.

In July 2025, Alden ranan editorialin more than 60 of its daily newspapers openly criticizing OpenAI and other AI companies that have used news content to train their models without compensation. “Securing permission from, and fairly compensating, those publishers who created this great foundation of knowledge is the right, just and American thing to do,” read the editorial. Both Alden publishers are part of the majorcopyright infringement suitagainst OpenAI and Microsoft that includes The New York Times and is currently winding its way through federal court.

Some independent local publishers, like The Baltimore Banner, are open to AI chatbots surfacing their stories without licensing deals. But they’re still concerned that a “back door” like the Wayback Machine’s might hurt their chances at being cited properly.

Last year, The Banner worked with the companyDataDometo analyze crawler activity on its site. The findings were striking: about 25% of The Banner’s site traffic was coming from bots, including crawlers operated by the Internet Archive, according toBiswajit Ganguly, the chief technology officer and AI strategist at the Banner.

Based on that analysis, The Banner started blocking the Internet Archive, later adding one of its crawlers toits robots.txt file. It still lets major AI companies through, including crawlers used by ChatGPT and Claude.

As Ganguly explains it, the new restrictions on the Wayback Machine are less about negotiating licensing deals or preventing The Banner’s stories from appearing in AI products, and more about ensuring those products trace information back to The Banner instead of linking to sites that aggregate its work.

“We didn’t want the bots to be trained on our content, and then spit out answers based on the content without any kind of references, link, or attribution to our sources,” said Ganguly. “If ChatGPT finds something in the Wayback Machine…we were not sure how well it would be attributed back to us.”

He added that The Banner is still gathering information on how AI search products interact with news about the Baltimore region and the publication is open to lifting its block down the line.

“The threat is definitely not the Internet Archive,” Ganguly said. “But it’s a question of how the other actors are going to provide references or attributions and links back to the real creator of the content.”

### Blocking as leverage for payment

Local publishers aren’t the only ones ramping up these efforts. Condé Nast, another arm of Advance Publications, has rolled out a coordinated effort to disallow the Internet Archive.Vogue,The New Yorker,Pitchfork,Vanity Fair,Bon Appetit, andWiredcurrently disallow four crawling bots from our list. (Last month, Wiredcovered the existential threatthese blocks pose to the Internet Archive). Condé Nast did not respond to a request for comment.

The Atlantic has been working with Cloudflare to block the Internet Archive since last summer and added one of the Internet Archive’s crawlers to its robots.txt file in an update earlier this year, according to Anna Bross, The Atlantic’s SVP of communications. She said the decision is part of the outlet’s “aggressive” blocking policy.

“Our default is to block: No one should be scraping The Atlantic’s journalism without permission, regardless of the use,” Bross said.

The Atlantic’s CEONick Thompsoncommented on our January reportingin a video posted to LinkedInin April. He said blocking the Internet Archive is important for publishers that want to maintain leverage when negotiating licensing with big AI companies.

“Because of the damages that can be done when you let all your content be scraped, because of all the leverage you lose, there will be worthy products that you previously gave your data to and now you can’t,” said Thompson.

Major international publishers have also started to block the Internet Archive, including the leading newspaper in Brazil,Folha de S.Paulo. Folha added three Internet Archive user agents to its robots.txt file in February.

“Folha believes that the sustainability of professional journalism — the very material the public record seeks to preserve — depends on protecting intellectual property,” saidSérgio Dávila, Folha’s editor-in-chief. “If AI companies wish to use this archive for training, they must enter into licensing agreements rather than rely on third-party repositories.”

Dávila noted that Folha invests in its own digital archive,Acervo Folha, which includes digitized editions of print issues going back to the paper’s founding in 1921. Access to Acervo Folha is available to paying subscribers.

### What can be done?

Archiving is expensive; the technical infrastructure, storage, and expertise can be cost-prohibitive to smaller news organizations.

Before the rise of digital news, many papersmaintained physical archives, often staffed with in-house librarians. Today, due to the contraction of the newspaper industry, most of those dedicated archiving roles are gone and the move to digital publishing has only complicated the issue.

RELATED ARTICLETo preserve their work — and drafts of history — journalists take archiving into their own handsHanaa' TameezJuly 31, 2024

A new content management system (CMS)can often lead to major archival losses. In 2024,thousands of articlesvanished from the sites of the Daily Hampshire Gazette and the Greenfield Recorder in Western Massachusettsduring a CMS switch. When publications close many former owners don’t want to shoulder the cost of maintaining a site. In 2022, a decade after The Hook, a Charlottesville weekly, went under, its archived site went offline,along with over 22,000 stories.

The Internet Archive is often touted as a hero of the web for taking on the Herculean task of preserving the entirety of the internet, and for stepping in when news organizations fail to preserve their own work.

In December, the Internet Archive partnered with the Poynter Institute and Investigative Reporters and Editors to train a cohort of 33 local and national news outlets on how to develop and implement an archiving strategy. Theinitiative, funded through a Press Forward grant, aims to train 300 newsrooms in digital preservation and in using the Internet Archive’s services by the end of 2027.

Most of theinitial cohortis made up of independent and nonprofit local newsrooms, including Outlier Media, Charlottesville Tomorrow, and The 51st. Wired is the only publication in our dataset restricting Internet Archive access that is participating in the program.

As Broussard, the NYU professor, points out, while the Internet Archive is one of the few efforts to make archivesfree, it isn’t the only effort to archive news. News publishers have long licensed their journalism to commercial archives like ProQuest and LexisNexis, which are often available in libraries, universities, and for individual subscriptions. They’re not free, but they do exist. At least several publications in our sample appear in ProQuest databases, including the Chicago Tribune, The Baltimore Sun, Honolulu Civil Beat, and USA Today.

Economic incentives are a valid reason for publishers to want to keep their contents out of the Internet Archive, Broussard said, but news outlets should have a long-term, multifaceted preservation strategy. Even with a plan in place, the reality for many publishers is that it’s unlikely that they’ll be able to save everything.

“Every news organization, especially local news organizations, generally launch thinking, ‘we’re going to put stuff on the internet and it’s going to be there forever,’ and that’s not true,” Broussard said. “Anybody who told you the internet is forever lied.”

Correction: An earlier version of this story stated that NOLA.com was owned by Advance Local. It is currently owned by Georges Media Group.

Photo of Internet Archive servers byScott Beal/Laughing Squidused under a Creative Commons license.

Andrew Deck
 is a staff writer covering AI at Nieman Lab. Have tips about how AI is being used in your newsroom? You can reach Andrew via 
email
, 
Bluesky
, or Signal (+1 203-841-6241).
Hanaa' Tameez
 is a staff writer at Nieman Lab. You can reach her via 
email
 (
[email protected]
), 
Bluesky DM
 (@hanaatameez.bsky.social), or on 
Signal
 (@hanaatameez.01).

POSTED
     
May 20, 2026
, 5:03 p.m.

SEE MORE ON
 
Aggregation & Discovery

advance local
AI
archives
Conde Nast
digital archives
Folha de S.Paulo
generative AI
intellectual property
Internet Archive
licensing deals
local news
The Atlantic
The Baltimore Banner
Wayback Machine
Wired

Show tags
Hide tags

  TWITTER

  FACEBOOK

  EMAIL

  SHARE ON FACEBOOK

  TWEET

 

Join the 60,000 who get the freshest future-of-journalism news in our daily email.

		As goes CBS Radio News, so goes the idea that news media should serve the public interest		
That the airwaves should be defined by more than a quest for profit was once a bipartisan view. 

		James Murdoch buys up half of Vox Media, grabbing New York and podcasts, but leaving The Verge and SB Nation		
Is he buying The Hundred and leaving Vaulter behind?

		Tech journalist Joanna Stern on leaving the Wall Street Journal and moving on to New Things		
“We’ve been describing it as tech journalism for humans who like fun.”

Matthew Jordan
As goes CBS Radio News, so goes the idea that news media should serve the public interest
That the airwaves should be defined by more than a quest for profit was once a bipartisan view. 
Joshua Benton
James Murdoch buys up half of Vox Media, grabbing New York and podcasts, but leaving The Verge and SB Nation
Is he buying The Hundred and leaving Vaulter behind?
Neel Dhanesha
Tech journalist Joanna Stern on leaving the Wall Street Journal and moving on to New Things
“We’ve been describing it as tech journalism for humans who like fun.”

* Subscribe
* Twitter
* Facebook
* RSS
* About
* Contact
* Archives

Help advance the Nieman Foundation’s mission “to promote and elevate the standards of journalism” 
by making a donation
.

To promote and elevate the standards of journalism

 

Covering thought leadership in journalism

 

Pushing to the future of journalism

 

Exploring the art and craft of story

 

© 2026 by the President and Fellows of Harvard College
  /  
Some rights reserved

Harvard
 
Trademark
 
Privacy
 
Digital Accessibility

Walter Lippmann House
    
One Francis Ave.
    
Cambridge, MA 02138
    
617 495 2237

The Nieman Journalism Lab is a collaborative attempt to figure out how quality journalism can survive and thrive in the Internet age.

It’s a project of theNieman Foundation for Journalism at Harvard University.

Follow us

* Subscribe to our email
* Follow us on Twitter
* Like us on Facebook
* Download our iPhone app
* Subscribe via RSS

Subscribe to our work →

The basics

* About us
* Contact
* Archives

Projects

* Encyclo
* Fuego
* Tweet archive

About us →

Director

Joshua Benton

Staff writers

Justin Ellis

Caroline O’Donovan

© President and Fellows of Harvard College, unless otherwise noted. 
Some rights reserved.