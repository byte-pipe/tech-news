---
title: DEV Follower Analysis - DEV Community
url: https://dev.to/annavi11arrea1/dev-follower-analysis-4dhc
date: 2025-11-19
site: devto
model: llama3.2:1b
summarized_at: 2025-11-23T11:13:12.511252
screenshot: devto-dev-follower-analysis-dev-community.png
---

# DEV Follower Analysis - DEV Community

**Github User Followers Analysis**

#### Key Points:

* The article discusses a journey to analyze Github user followers and their activity on various subjects.
* The objective is to extract meaningful data from followers to gain insight into their interests and behaviors.
* A custom script is provided to collect publicly available user data, including language and technology usage.

**Data Collection Process:**

1. Collecting publically available Github user data using the DEV API for Members with an api key.
2. Scanning through each follower's website and visiting their GitHub repository to gather information on languages used and types of content posted.

**Main Issues Identified:**

* The initial project concept was driven out by excitement, rather than a clear goal.
* A plug-and-play solution using the DEV API is not straightforward and requires creativity.
* Handling errors due to HTTP responses and custom header requests.

**Technical Details:**

* Utilizing Node.js for scripting and API interactions
* Employing async/await syntax for handling concurrent requests
* JSON data processing for convenience

#### GitHub User Followers List Format:

| Github Username | Languages Used | Content Types |
| --- | --- | --- |
| ... | ... | ... |

### Results Data Structure:
```markdown
const {
  UsersResult: { data },
} = fetchAllPages();

// Example results object
{
  "total": 500,
  "data": [
    {
      "username": ".githubuser1",
      "languages": ["javascript", "typescript"],
      "contentTypes": ["blog posts", "git issues"]
    },
    // ...
  ]
}
```

#### Analysis Potential:

* Gaining insights into user interests and behaviors through follower demographics
* Identifying emerging trends in certain subjects or topics

**Future Improvements:**

* Developing a more tailored scraper solution using DEV's API directly.
* In-depth exploration of Github repositories to gather additional data on content types.

**Code Snippets (sample) :**

```javascript
const fs = require('fs');
const path = require('path');

// Fetch followers from DEV API for Members with an api key
async function fetchAllPages(apiKey) {
  const BASE_URL = 'https://dev.to/api/followers/users';
  let results;

try {
    // Construct initial query URL
    const urlRegex = /\.user_(.*)\.(.+)$/g;
    const pageMatch = urlRegex.exec(`${BASE_URL}?page=${1}&per_page=${2}`);

    if (pageMatch) {
      console.log(`Fetching page ${pageMatch[1]} from URL: ${urlMatch[0]}`);

    try {
        // Send request, process data, fetch next results
        const response = await fetch(urlRegex.exec(`https://dev.to/api/followers/users?page=${2}&per_page=1000&api-key=${apiKey}`).href);

       let allResults = [];
     let page = 1;

if (!response.ok) { throw new Error(`HTTP error! status: ${response.status}`); }

    // stream consumer
        const data = await response.json();```
