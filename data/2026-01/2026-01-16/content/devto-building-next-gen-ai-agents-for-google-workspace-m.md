---
title: 'Building Next-Gen AI Agents for Google Workspace: MCP, A2A, and A2UI with Google Apps Script - DEV Community'
url: https://dev.to/gde/building-next-gen-ai-agents-for-google-workspace-mcp-a2a-and-a2ui-with-google-apps-script-299o
site_name: devto
fetched_at: '2026-01-16T11:07:16.001693'
original_url: https://dev.to/gde/building-next-gen-ai-agents-for-google-workspace-mcp-a2a-and-a2ui-with-google-apps-script-299o
author: Tanaike
date: '2026-01-10'
description: Abstract This article demonstrates how to implement Model Context Protocol (MCP),... Tagged with gemini, mcp, a2a, googleworkspace.
tags: '#gemini, #mcp, #a2a, #googleworkspace'
---

## Abstract

This article demonstrates how to implement Model Context Protocol (MCP), Agent-to-Agent (A2A), and Agent-to-UI (A2UI) utilizing Google Apps Script (GAS). By leveraging GAS, developers can overcome authentication bottlenecks, enabling seamless integration of AI agents with Google Workspace data for powerful, autonomous workflows and dynamic user interfaces.

## Introduction

The ecosystem of AI agents is evolving rapidly. To enable these agents to process complex tasks effectively, the Model Context Protocol (MCP) has emerged as a critical standard. MCP allows AI models, such as Large Language Models (LLMs), to connect and interact with external data sources, tools, and software applications in a standardized manner.Ref

Looking ahead, Agent2Agent (A2A) and Agent-to-User Interface (A2UI) protocols are expected to play pivotal roles. A2A refers to the autonomous communication and interaction between multiple AI agents without direct human intervention.RefMeanwhile, A2UI allows AI agents to construct interactive user interfaces using structured data (such as JSON) rather than static code. This enables an agent to generate a specific UI—like a restaurant booking form—on the fly, which the host application renders using native components.Ref

Integrating these technologies with Google Workspace unlocks limitless potential. Recently, a Gemini CLI extension including an MCP server for Workspace management was released.RefHowever, existing samples for MCP, A2A, and A2UI often face compatibility issues with Google Workspace, primarily due to complex scope authorization bottlenecks. Connecting from a local environment typically requires handling OAuth 2.0 or service accounts, which can hinder rapid development.

Google Apps Script (GAS) offers a robust solution to this challenge. As the only low-code platform designed to integrate, automate, and extend Google Workspace, GAS handles scope authorization seamlessly upon execution.RefConsequently, leveraging GAS significantly simplifies the implementation of MCP, A2A, and A2UI. This article introduces practical implementations of these protocols using Google Apps Script.

## Project Resources

* MCP & A2A Repository:https://github.com/tanaikech/a2a-for-google-apps-script
* A2UI Repository:https://github.com/tanaikech/A2UI-for-Google-Apps-Script

## Part 1: MCP (Model Context Protocol)

In this section, we will build an MCP server using Google Apps Script and test it using the Gemini CLI.

### Prerequisites

* Node.js is installed on your local machine.
* A valid Gemini API Key.Get one here.
* The Gemini CLI is installed.Ref

### 1. Server-Side Setup

#### 1.1 Copy the Demo Script

You can copy the A2A server template to your Google Drive by running the following GAS code:

function

myFunction
()

{


const

fileId

=

"
1mylSOTzCuui95Amk-kRufA9ffMqcnjqk8HSaoatoxaSPwkv-hg1q7uRC
"
;


const

file

=

DriveApp
.
getFileById
(
fileId
);


file
.
makeCopy
(
file
.
getName
());

}

Enter fullscreen mode

Exit fullscreen mode

RunmyFunctionto copy the sample A2A server to your root folder.

Alternatively, you can manually copy the scripts from theGitHub Repository. This example usesa2a-server/sample2/a2a-server.js, which integrates 160 tools fromToolsForMCPServer.

For developers wishing to use custom tools, a separate sample is available ata2a-server/sample1/a2a-server.js.

#### 1.2 Deploy as Web App

1. Open the script editor in your copied project.
2. ClickDeploy>New deployment.
3. SelectWeb Appas the type.
4. Set "Execute as" toMe.
5. Set "Who has access" toAnyone.
6. ClickDeployand copy the Web App URL (https://script.google.com/macros/s/###/exec).

Note: Whenever you modify the code, you must deploy a new version to reflect the changes.Reference.

#### 1.3 Configure the Script

Locate the configuration object in your GAS project and update the variables:

const

object

=

{


apiKey
:

"
{apiKey}
"
,

// Your API key for using Gemini API.


model
:

"
models/gemini-3-flash-preview
"
,


accessKey
:

"
sample
"
,

// Optional: Access key for requesting Web Apps.


webAppsUrl
:

"
https://script.google.com/macros/s/###/exec
"
,

// Your deployed Web App URL.


// logSpreadsheetId: "{spreadsheetId}", // Optional: Store logs in Google Spreadsheet.

};

Enter fullscreen mode

Exit fullscreen mode

* Set your Gemini API key inapiKey.
* Set your access key (default issample).
* Set your Web App URL inwebAppsUrl.

After updating the script, remember to redeploy the Web App.

### 2. Client-Side Setup

Navigate to the.geminidirectory on your local machine and updatesettings.json. Replace{Your value}with your specific details.

{


"security"
:

{


"auth"
:

{


"selectedType"
:

"{Your value}"


}


},


"ui"
:

{


"theme"
:

"{Your value}"


},


"mcpServers"
:

{


"gas_web_apps"
:

{


"command"
:

"npx"
,


"args"
:

[


"mcp-remote"
,


"https://script.google.com/macros/s/{Your value}/exec?accessKey=sample"


],


"timeout"
:

300000


}


}

}

Enter fullscreen mode

Exit fullscreen mode

Launch the Gemini CLI and run the command/mcp. You should see the connected status. You can now use the tools immediately because the authorization process was handled during the GAS Web App deployment.

## Part 2: A2A (Agent-to-Agent)

### 1. Server-Side Setup

If you have successfully completed the MCP test above, your server is ready. The GAS Web App configured in the previous section functions as both an MCP server and an A2A server. No further server-side configuration is required.

### 2. Client-Side Setup

#### 2.1 Clone Repository and Install Dependencies

Execute the following commands in your terminal:

git clone https://github.com/tanaikech/a2a-for-google-apps-script

cd
a2a-for-google-apps-script/a2a-client
npm
install

Enter fullscreen mode

Exit fullscreen mode

The directory contains:

* a2a-client: Node.js sample client scripts.
* a2a-server: Google Apps Script Web App server samples.

#### 2.2 The Proxy Script

The current@a2a-js/sdkversion automatically strips query parameters and redirects to a/.well-known/path. To resolve this, the providedclientGas.jsacts as a proxy. It intercepts the fetch API, allowing the SDK to communicate correctly with GAS's dynamic URLs.

Authentication Note:This script uses the Google Cloud SDK (gcloud CLI) to retrieve access tokens. Ensure you have authorized thehttps://www.googleapis.com/auth/drive.readonlyorhttps://www.googleapis.com/auth/drivescope. This is required to access the GAS Web App path/.well-known/agent-card.json.

#### 2.3 Set Environment Variables

Create a.envfile in thea2a-clientdirectory:

GEMINI_API_KEY="YOUR_KEY"
GEMINI_MODEL="gemini-3-flash-preview"
A2A_WEB_APPS_URL="https://script.google.com/macros/s/{Your value}/exec?accessKey=sample"

Enter fullscreen mode

Exit fullscreen mode

EnsureA2A_WEB_APPS_URLincludes your access key as a query parameter. This sample uses a single A2A server. To use multiple servers, define additional variables and register them usingnew FunctionToolin the client script.

#### 2.4 Testing

#### Terminal Test

Run the basic connectivity test:

npm run test1

Enter fullscreen mode

Exit fullscreen mode

Expected output:

Prompt: How much is 10 yen in USD?
Response: 10 yen is approximately **0.0641 USD**...
Prompt: What is the weather forecast for Tokyo?
Response: The weather forecast for Tokyo... is clear sky.

Enter fullscreen mode

Exit fullscreen mode

#### Browser/ADK Test

This test utilizes the Agent Development Kit (ADK) to provide a chat interface:

npm run test2

Enter fullscreen mode

Exit fullscreen mode

Openhttp://localhost:8000in your browser.

Example 1: Simple Workflow

Prompt:

I want to cook miso soup.
To achieve this goal, create a new Google Spreadsheet,
generate a roadmap for cooking miso soup in the spreadsheet,
and return the Spreadsheet URL.

Enter fullscreen mode

Exit fullscreen mode

The browser demonstrates the agent processing the prompt via the A2A server.

The resulting roadmap in the Spreadsheet:

Example 2: Complex Workflow

Prompt:

Write a comprehensive article about developing Google Apps Script (GAS) using generative AI.
The article should include an introductory overview, formatted lists for best practices,
and a table comparing different AI-assisted coding techniques.
Once generated, please create a new Google Document, insert the content, convert the Google Document to a PDF file,
and send an email to `tanaike@hotmail.com` including the shareable URL of the PDF file by giving a suitable title and email body.

Enter fullscreen mode

Exit fullscreen mode

The browser visualizes the processing steps:

This task requires coordination between the Docs API, Drive API, and Gmail API. While this might trigger a Tool Selection Issue (TSI) in standard environments, the GAS A2A server handles the deterministic selection seamlessly.

The generated PDF:

The email received:

Dear Tanaike,

Please find attached the PDF document containing the comprehensive article on "Leveraging Generative AI for Google Apps Script Development". The shareable URL for the PDF is https://drive.google.com/file/d/###/view?usp=sharing.

Best regards,
Your AI Assistant

Enter fullscreen mode

Exit fullscreen mode

## Part 3: A2UI (Agent-to-User Interface)

In theofficial A2UI sample (Restaurant finder), the client communicates via A2A protocols. In this GAS-optimized implementation, we reduce HTTP overhead by allowing the client (HTML) to communicate directly with the AI agent usinggoogle.script.run.

### 1. Sample Script

Copy the Google Spreadsheet containing the necessary scripts:

https://docs.google.com/spreadsheets/d/1csYUJO8LzcEFPkt_ickIkdsGZsvim6lb1OEQZHUkB3c/copy

After copying, open the script editor and set yourapiKeyinmain.gs.

Alternatively, access the code via theGitHub Repository.

### 2. Deploy as Web App

1. Open the script editor in your project.
2. ClickDeploy>New deployment.
3. SelectWeb App.
4. Set "Execute as" toMe.
5. Set "Who has access" toOnly myself. (Restrict access to yourself for testing as the owner).
6. ClickDeployand copy the Web App URL.

Note: You can use the dev mode URL (.../dev) for testing. Updates require a new deployment.Reference.

### 3. Testing

#### Sample 1: Restaurant Finder

This test reproduces the official "A2UI Restaurant finder" sample.

Open your Web App URL. You will see the interface:

Enter: "Find 3 Chinese restaurants in New York" and clickSend.

ClickBook Nowfor "Han Dynasty". The agent generates a reservation UI.

Fill in the details and clickSubmit Reservation. The server processes the request.

Using Spreadsheet Data:While the sample uses hard-coded data inexecuteGetRestaurants, GAS allows you to fetch this from a Spreadsheet easily. If you have a sheet formatted like this:

You can replace the data source with:

const

allRestaurants

=

((
_
)

=>

{


const

sheet

=

SpreadsheetApp
.
getActiveSpreadsheet
().
getSheetByName
(
"
Sheet1
"
);


const

[
header
,

...
values
]

=

sheet
.
getDataRange
().
getDisplayValues
();


const

obj

=

values
.
map
((
e
)

=>


header
.
reduce
((
o
,

h
,

j
)

=>

((
o
[
h
]

=

e
[
j
]),

o
),

{})


);


return

obj
;

})();

Enter fullscreen mode

Exit fullscreen mode

#### Sample 2: Budget Simulator

Copy the Budget Simulator Spreadsheet:

https://docs.google.com/spreadsheets/d/1HEfmSD9WMqQfy39aEZEjz7ggFeiZIx0_b2oKkrReEpk/copy

Set yourapiKeyinmain.gsafter copying.

This sample implements an "Interactive smart household account book and budget simulator". Ensure "Sheet1" contains the initial budget data:

Deploy as a Web App and open the URL.

Enter:Check this month's budget. A2UI displays a pie chart and category list based on the spreadsheet data.

Enter: "What would happen if I reduced my dining out expenses by 10,000 yen and put the money towards savings?"

The graph updates to simulate the proposal.

ClickUpdate sheet with this budget proposal. GAS updates the cells, and a notification confirms the action.

The new data is appended to "Sheet1":

## Summary

* MCP, A2A, and A2UI represent the future of AI interoperability, enabling agents to connect with tools, collaborate with each other, and generate dynamic user interfaces.
* Google Apps Script provides a unique advantage by resolving complex OAuth 2.0 authorization bottlenecks native to local environments.
* Implementing MCP servers on GAS allows for seamless integration between the Gemini CLI and Google Workspace data.
* A2A on GAS facilitates autonomous multi-agent workflows, capable of executing complex tasks like generating documents and sending emails without human intervention.
* A2UI combined with GAS allows agents to build interactive, data-driven interfaces on the fly, directly connected to live Spreadsheet data.

## Appendix

I am exploring taking advantage of Google Apps Script. The summary of this can be seenhttps://github.com/tanaikech/taking-advantage-of-google-apps-script.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
