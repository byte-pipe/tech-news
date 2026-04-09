---
title: DEV Follower Analysis - DEV Community
url: https://dev.to/annavi11arrea1/dev-follower-analysis-4dhc
site_name: devto
fetched_at: '2025-11-22T11:06:29.032626'
original_url: https://dev.to/annavi11arrea1/dev-follower-analysis-4dhc
author: Anna Villarreal
date: '2025-11-19'
description: 'TLDR: Extract Github Users from DEV Followers and save to JSON for Chart Output Analysis Via GraphQL.... Tagged with graphql, node, chartjs, api.'
tags: '#graphql, #node, #chartjs, #api'
---

TLDR: Extract Github Users from DEV Followers and save to JSON for Chart Output Analysis Via GraphQL. Chart at Bottom.

#### Beginning Thoughts

Ever wonder who’s watching? At this moment, perhaps it is I.

I initially thought it would be cool to make a little dev followers badge to show on my profile website. While I realize that this number isn’t terribly meaningful in and of itself, it sparked a very in depth journey of scraping data for analysis. I realized that DEV has an api key available to members. You can gather some good things with this api.

What really became my goal was to extract meaningful data from my followers. What is my crowd? What kind of individuals do I attract with my posts? What languages and technologies do they use?

This is something that requires a little bit of digging. I built a scraper to navigate to all of my followers and collect publicly available user data. You know, the stuff you are already sharing with the planet. After I collected my data I figured I could visit their links and see what kind of languages they used on their github, or the type of content that they post to their personal websites.

I thought this deeper level of scraping would help me get a birds-eye view of what my followers are doing, as well as detect current trends on subjects I am interested in. There is a good chance some of my followers like the same things as me.

It's also interesting to note that I was in the middle of a 7 hour Node.js tutorial when I got derailed with excitement and started this project when the idea came to my head. Got distracted by another project in the middle of another project, typical.

#### Setting up Data Collection

SO there isn't a plug and play solution for this, you have to be a tiny bit creative. I will share one of my scripts with you to get you started on your own journey of personal analysis.

const fs = require('fs');
const path = require('path');

const API_KEY = 'YOUR_API_KEY_HERE'; // Replace with your actual API key
const BASE_URL = 'https://dev.to/api/followers/users';
const PER_PAGE = 1000; // dev.to limit

async function fetchAllPages() {
 let allResults = [];
 let page = 1;

 while (true) {
 const url = `${BASE_URL}?page=${page}&per_page=${PER_PAGE}`;
 console.log(`Fetching page ${page} from URL: ${url}`);
 try {
 const response = await fetch(url, {
 method: 'GET',
 headers: {
 'Content-Type': 'application/json',
 'api-key': API_KEY,
 'Access-Control-Allow-Headers': 'Content-Type, Authorization'
 },
 });

 if (!response.ok) { throw new Error(`HTTP error! status: ${response.status}`); }

 // stream consumer
 const data = await response.json();
 console.log(data);

 if (!Array.isArray(data) || data.length === 0) {
 console.log("No more results to fetch.");
 break;
 }

 allResults = allResults.concat(data);
 console.log(`Fetched ${data.length} users (total: ${allResults.length})`);

 if (data.length < PER_PAGE) {
 console.log("Fetched the last page of results.");
 break;
 }
 page++;

 // Optional: small delay to avoid hitting rate limits
 await new Promise(resolve => setTimeout(resolve, 200));

 } catch (error) {
 console.error("Error fetching data:", error);
 break;
 }
 }

 // Define the file path to save the response data
 const outputDir = path.join(__dirname, `followerdata`);
 fs.mkdirSync(outputDir, { recursive: true }); // Ensure the directory exists

 const filePath = path.join(outputDir, "all_followers.json");
 fs.writeFileSync(filePath, JSON.stringify(allResults, null, 2));

 console.log(`Saved ${allResults.length} followers to ${filePath}`);

 // return allResults;
}

fetchAllPages()
 .catch(error => console.error("Failed to fetch all pages:", error));

Enter fullscreen mode

Exit fullscreen mode

#### Custom Output Files

There are several different scripts I made, each building off one another with a different purpose. I made a file that put all the usernames in an object, another where I went through and collected only the usernames whose profile contained a link to a github. I used my new collection of github users to feed yet another scraper, to find all of the languages used among my DEV followers.

I wanted to take that data and create some charts to offer visually appealing meaning. I explored different types of charts. Now I know there are probably some fancy analysis tool out there, but I wanted to learn how to navigate custom data by myself. An interesting and useful tool I used was cheerio, a module that helps you navigate the DOM in search of particular data. It took me a little bit of time to figure out how to grab everything the way I wanted, but it was so exciting when I got it to work! There is something satisfying about watching lines in the terminal fly up the screen with everything functioning as you wanted it too. Deep satisfaction.

Become one with the Cheerio:Cheerio

#### Navigating Data on Github

So after trying to use cheerio to scrape for language tags on github, I got nothing but empty objects. I was a little annoyed to wake up in the morning to see a giant list of empty objects. I soon realized that this was because those tags load up after the page loads. So then, to the github API. I was swiftly cut off by rate limiting, so make sure to use an API key before you even bother with a large amount of data.

Even with the API key, I was still hitting rate limits. (More on this later) That was a bit annoying, especially when trying to debug. After further refinement and waiting a bit, I was able to pull repo information. It was at this moment I soon learned how much information I was actually pulling. I can say it was more than I needed. However, It was interesting to note all of the information I was able to pull from a repo. Depending on the user and number of repos, this could become wild very quickly. What am I gonna do with 50 URLs for each repo? Absolutely unnecessary for my use case.

#### GraphQL

Upon searching for a solution to another problem, I stumbled into GraphQL. With GraphQL you can process all repositories for each user in a single request per user, even when your input file contains URLs instead of usernames, like my json file for example.

Hmm, that's interesting for sure. While investigating this, I learned that Github handles requests a little differently than GraphQL. GraphQL is a little bit stricter.

#### Don’t forget to install your packages

But let me share some comedy. There I was, thinking I could use .env to fetch my GITHUB_TOKEN - over and over! I got so frustrated I pulled out AI and went in circles with ChatGPT. After switching from ChatGPT to Claude code I discovered I was not actually pulling my api key. I cannot believe I didn’t install the package. SHAME!

insert feelings of stupidity here and a moment of silence for time lost

Wow look at that, after properly assigning my environment variable it starts doing things! Don’t wait, install the package.

...At least the existing code was meticulously gone through with a fine tooth comb, free of impurities.

I wasdeceivedby my own self. Ithoughtthat my environment variable was working when doing API requests because Github allows you to access certain public resources without authentication. However, when using GraphQL, you need to use authenticated requests. This ultimately led me to discover my error. This also explains why I was running into rate limit problems when I was actually trying to control them. I sneakily fooled myself. I guess we are at that point then, better watch out for myself.

#### Additional Fun tool: Rainbow CSV

Rainbow CSV Extension in VSCode

I discovered a tool called Rainbow CSV. It’s an extension for VSCode, a mini query language console where you can run queries on your csv data. It just so happens that was my chosen output format for the language data. Isn’t that nice and cozy?

Rainbow CSV Preview

So much excitement.

So the data from my query returns user, language, and then edges. Edges in this case means bytes of data. So we can determine how many bytes of data a user has written or used in their repos.

Then, we can take that data and sum it up into a neat little chart. For this, I tried using Chart.js. It was simple to implement for a quick data visual. I counted total edges (bytes) of data found per language discovered among my followers repos.

#### Surprises

I did not expect that my followers were C aficionados... by an astounding landslide compared to the rest of the languages. As someone who has primarily worked on front end stuff, I was a bit shocked. Perhaps it is time to learn C?

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
