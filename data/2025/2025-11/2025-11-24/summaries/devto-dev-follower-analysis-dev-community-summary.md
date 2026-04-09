---
title: DEV Follower Analysis - DEV Community
url: https://dev.to/annavi11arrea1/dev-follower-analysis-4dhc
date: 2025-11-19
site: devto
model: llama3.2:1b
summarized_at: 2025-11-24T11:13:11.570073
screenshot: devto-dev-follower-analysis-dev-community.png
---

# DEV Follower Analysis - DEV Community

**Github User Extractors and Chart Output Analysis Via GraphQL**
=====================================================================================

### Overview

This GitHub project aims to extract meaningful data from contributors to DEV followers using a scraper, API access through developer tokens, and chart output analysis via GraphQL.

#### Key Points:

*   Use the `YOUR_API_KEY_HERE` (replace with actual API key) to interact with DEV's API.
*   Build a scraper to navigate to all GitHub users owned by DEV followers and collect publicly available user data.
*   Visit links of extracted followers to gather their languages and content types on GitHub.

### Structured Summary

#### **Data Collection**

*   No plug-and-play solution, requires creativity and scripting effort
*   API Key: Replace with actual API key from Developer Platform
*   Base URL: `https://dev.to/api/followers/users`

**スクレイPER Functions**
```markdown
- `fetchAllPages`: Fetches pages of results from DEV API
|------------------------------------------------|
| Parameters | Description                          |
|------------|----------------------------------------|
| API Key    | Replace with your actual API key       |
| PER_PAGE  | Number of users per page              |

async function fetchAllPages() {
  let allResults = [];
  let page = 1;

  // Loop through pages
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
        }
      });

      if (!response.ok) { throw new Error(`HTTP error! status: ${response.status}`); }

      // Parse JSON response
      const data = await response.json();

      console.log(data);

      if (!Array.isArray(data) || data.length === 0) {
        console.log("No more results to fetch.");
        break;
      }

      allResults = allResults.concat(data);
      console.log(`Fetched ${data.length} users (total: ${allResults.length})`);

      // Navigate to next page
      if (data.length < PER_PAGE) {
        console.log("Fetched the last page of results.");
        break;
      }

      page++;
    } catch (error) {
      console.error('Error fetching data:', error.message);
    }
  }

  return allResults;
}
```

#### **Chart Output Analysis**

```markdown
- **Variables**
  ```javascript
  const API_KEY = 'YOUR_API_KEY_HERE'; // Replace with actual API key
  const BASE_URL = 'https://dev.to/api/followers/users';
  const PER_PAGE = 1000; // DEV API limit
  const CHART_VARIABLES = ['followers', 'languages', 'contentTypes'];
```

- **Data Manipulation**
```markdown
// Extract meaningful data from followers (e.g., languages, content types)
const followersData = allResults.map(data => {
  return {
    name: data[0].username,
    language: data[1][0].language_name || '',
    contentType: data[2][0].content_type.name || ''
  };
});
```

- **Visualization**
```markdown
# Chart Output Analysis via GraphQL

## Example Code

```graphql
query {
  followersData (followersCount: $followersCount) {
    name
    language
    contentType
  }
  chartVars: $chalkVariables
}

type Query {
  chartData(followersData: [name, language, contentType])
}

scalar Int!
enum ChartValueType { COUNT, CREATIVITY}
input TypeOfData {
  type = String
  sort = Boolean
}
```

#### **Example Use Case**

*   Create a GraphQL schema to hold the data for analysis
```graphql
type Query {
  followersCount: Int!
  chartData(type: TypeOfData): [name: String, language: String, contentType: String]
}

type TypeOfData {}

input FollowersInput {
  type = String!
  sort = Boolean!'
}

query {
  followersCount: $followersCount

  $followersCount:
    query: followersCountQuery
    resolve: followersCountQuery
}
```
*   Create the GraphQL client to execute queries and retrieve data
```javascript
import { ApolloClient, InMemoryCache } from '@apollo/client';

const client = new ApolloClient({
  uri: 'https://your-graphql-scheme.com/graphql',
  cache: new InMemoryCache()
});

// Execute query to extract followers' data
client.query({
  query: ` ${graphql`query {
    followersCount (followersCount: $followersCount) {
      name
      language
      contentType
    }
  }${`
})(0, {
  variables (followersCount) {
    type = 'Int!';
    sort = true!
  }})`, errors: { stack: {} }, data: null};
