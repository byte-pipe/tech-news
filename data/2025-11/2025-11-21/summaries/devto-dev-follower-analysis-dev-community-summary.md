---
title: DEV Follower Analysis - DEV Community
url: https://dev.to/annavi11arrea1/dev-follower-analysis-4dhc
date: 2025-11-19
site: devto
model: llama3.2:1b
summarized_at: 2025-11-21T11:13:02.913726
screenshot: devto-dev-follower-analysis-dev-community.png
---

# DEV Follower Analysis - DEV Community

## Github Followers Webpage Analysis and Data Export via GraphQL

### Introduction to DEV Follower Analysis
The article explores a personal analysis project on extracting meaningful data from GitHub followers using the DEV API. The goal is to create a badge showing profile information, detect trends, and identify common interests among followers.

### Setting up Data Collection and Web Scraping Tool

*   To start, we need to install necessary modules: `fs` for file system operations and `path` for path manipulation.
*   Define the API key from DEV community as an environment variable `API_KEY`.
*   Set variables for base URL, number of per-page limit, and scraper function.
*   Implement a while loop to fetch pages until all results are collected.

```javascript
// Import necessary modules
const fs = require('fs');
const path = require('path');

// Define API key from DEV community as an environment variable
const API_KEY = process.env.DEV_API_KEY;

// Set variables for base URL, number of per-page limit, and scraper function
const BASE_URL = 'https://dev.to/api/followers/users';
const PER_PAGE = 1000;
let page = 1;

async function fetchAllPages() {
    // Initialize empty array to store results
    let allResults = [];

    while (true) {
        // Construct URL for current page with per-page limit and API key
        const url = `${BASE_URL}?page=${page}&per_page=${PER_PAGE}`;
        console.log(`Fetching page ${page} from URL: ${url}`);

        try {
            // Fetch data from the constructed URL
            const response = await fetch(url, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'api-key': API_KEY,
                    'Access-Control-Allow-Headers': 'Content-Type, Authorization'
                }
            });

            if (!response.ok) {
                // Throw Error with HTTP error status code
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();

            console.log(data);

            if (!Array.isArray(data) || data.length === 0) {
                // Log message to let the writer know there are no more results for this page
                console.log("No more results to fetch.");
                break;
            }

            // Concatenate user result arrays
            allResults = allResults.concat(data);

            console.log(`Fetched ${data.length} users (total: ${allResults.length})`);

        // Log and break in case of HTTP error status 404, which is the default response from DEV API after no pages are returned
                if (data.length < PER_PAGE) {
                    console.log("Fetched the last page of results.");
                    break;
                }

            page++;

            // Op
```

### JSON Export for Chart Output Via GraphQL

*   Create a new function to export data in JSON format.
*   Add an `export` section with the following structure: `{allResults, page, pageNumber}`.

```javascript
// Function to export data in JSON format
export async function exportData() {
    const jsonData = allResults.filter((user) => user.githubProfileUrl !== null);
    return { jsonData, pageNumber: page };
}
```

*   In the main script, call this new `exportData` function and process the result.

```javascript
// Main script to run analysis and export data in JSON format
(async () => {
    try {
        const followers = await fetchAllPages();
        const importResult = await importData(followers);
        console.log(importResult);

        // Export JSON content via GraphQL API
        const graphqlEndpoint = `https://dev-community.com/graphql?input=%7B%22query%22%3A%22query%20%7C%20get%20users%20by%20followers%20for%20the%20current%20user%2C%20(limit:100)%20%7D`;
        const graphqlSubscription = await importData(graphqlEndpoint);

        console.log(graphqlSubscription);

    } catch (error) {
            console.error(error);
}
```
