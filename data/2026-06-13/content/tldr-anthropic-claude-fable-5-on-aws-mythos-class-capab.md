---
title: 'Anthropic Claude Fable 5 on AWS: Mythos-class capabilities with built-in safeguards now available | AWS News Blog'
url: https://aws.amazon.com/blogs/aws/anthropic-claude-fable-5-on-aws-mythos-class-capabilities-with-built-in-safeguards-now-available/
site_name: tldr
content_file: tldr-anthropic-claude-fable-5-on-aws-mythos-class-capab
fetched_at: '2026-06-13T11:40:02.714530'
original_url: https://aws.amazon.com/blogs/aws/anthropic-claude-fable-5-on-aws-mythos-class-capabilities-with-built-in-safeguards-now-available/
date: '2026-06-13'
published_date: '2026-06-09T10:40:31-07:00'
description: 'Anthropic Claude Fable 5 on AWS: Mythos-class capabilities with built-in safeguards now available (3 minute read)'
tags:
- tldr
---

## AWS News Blog

# Anthropic Claude Fable 5 on AWS: Mythos-class capabilities with built-in safeguards now available

Updated on June, 12, 2026 – Claude Fable 5 and Claude Mythos 5 on Amazon Bedrock access unavailableTo support compliance with the US Government export control directive, Anthropic has asked AWS to revoke access to Claude Fable 5 and Claude Mythos 5 for all users. All other models, including Opus4.8, are not affected and you can continue using them in full confidence. Please view theAnthropic statementfor further details.

Today, we’re announcing the availability ofClaude Fable 5onAmazon BedrockandClaude Platform on AWS. Claude Fable 5 makes Mythos-level capabilities available to customers, with strong safeguards designed to make it safe for broader use. Fable 5 is state-of-the-art on nearly all tested benchmarks and delivers exceptional performance in software engineering, knowledge work tasks, and vision – built for ambitious, long running work.

With Claude Fable 5 on Bedrock, you can build within your existing AWS environment and scale inference workloads. You can also use Claude Fable 5 through the Claude Platform on AWS, giving you Anthropic’s native platform experience.

According to Anthropic, Claude Fable 5 represents a step-change in what you can accomplish with AI models. Here is what makes this model different:

* Long-running, asynchronous execution— Claude Fable 5 handles complex tasks that previous models could not sustain, executing coding and knowledge work tasks for extended periods without intervention.
* Advanced vision capabilities— Claude Fable 5 understands diagrams, charts, and tables nested in files and PDFs. This opens up research and document-heavy work in finance, legal, analytics, architecture, and gaming. In coding, the model implements designs with high fidelity and uses vision to critique its output against goals.
* Proactive self-verification— The model updates its own skills based on learnings and develops its own harnesses and evaluations.

Claude Fable 5 includes safeguards that limit its performance in specific areas where misuse risk is elevated. Harmful prompts related to cybersecurity, biology, chemistry, and health fall back to receive a response from Opus 4.8 instead. Anthropic is able to expand access to nearly all of Claude Fable 5’s state-of-the-art capabilities by developing more powerful safeguards. The same model without these limits isClaude Mythos 5and it will only be available to a small group of vetted customers.

Claude Fable 5 model in actionYou can use Claude Fable 5 in both Amazon Bedrock and Claude Platform on AWS. This post covers guidance on how to access and use on Amazon Bedrock. For guidance on the Claude Platform on AWS, visit thedocumentationto learn more.

To get started with Amazon Bedrock, you can access the model programmatically now using theAnthropic Messages APIto call thebedrock-runtimeorbedrock-mantleendpoints through Anthropic SDK. You can also keep using theInvokeandConverse APIonbedrock-runtimethrough theAWS Command Line Interface (AWS CLI)andAWS SDK.

Configure data retention settingIn order to access Claude Fable 5 model, you must opt into data sharing by using theData Retention APIand settingprovider_data_sharebefore you can invoke the models. There is no console user interface for this setting at launch.

This mode allows Amazon Bedrock to retain and share your inference data with model providers per their requirements. Anthropic requires 30-day inputs and outputs retention, as well as human review. To learn more, visit theAmazon Bedrock abuse detection.

Here is a sample script to set data retention for thebedrock-mantleengine.

curl -X PUT https://bedrock-mantle.us-east-1.api.aws/v1/data_retention \
 -H "x-api-key: <your-bedrock-api-key>" \ 
 -H "Content-Type: application/json" \
 -d '{ "mode": "provider_data_share" }'

If you want to use thebedrock-runtimeengine, run this sample script.

curl -X PUT https://bedrock.us-east-1.amazonaws.com/data-retention \
 -H "Authorization: Bearer <your_bearer_token>" \
 -H "Content-Type: application/json" \
 -d '{ "mode": "provider_data_share" }'

Updated on Jun 10, 2026— You can also use AWS SigV4 (Signature Version 4) to call the data retention API. Configure your AWS CLI or AWS SDK using environment variables.

export AWS_ACCESS_KEY_ID=your_access_key_id
export AWS_SECRET_ACCESS_KEY=your_secret_access_key
export AWS_SESSION_TOKEN=your_session_token

First, retrieve your current Bedrock data retention settings.

curl -s https://bedrock.us-east-1.amazonaws.com/data-retention \
 --aws-sigv4 "aws:amz:us-east-1:bedrock" \
 --user "$AWS_ACCESS_KEY_ID:$AWS_SECRET_ACCESS_KEY" \
 -H "x-amz-security-token: $AWS_SESSION_TOKEN"

This should return something like this:{"mode":"inherit","updatedAt":null}and update the data retention settings.

curl -s -X PUT https://bedrock.us-east-1.amazonaws.com/data-retention \
 --aws-sigv4 "aws:amz:us-east-1:bedrock" \
 --user "$AWS_ACCESS_KEY_ID:$AWS_SECRET_ACCESS_KEY" \
 -H "x-amz-security-token: $AWS_SESSION_TOKEN" \
 -H "Content-Type: application/json" \
 -d '{"mode":"provider_data_share"}'

If everything worked as expected, you should receive a response like:{"mode":"provider_data_share","updatedAt":"2026-06-10T16:51:39.331Z"}.

The latest AWS CLI supports configuring the data retention setting. Set your bearer API key as an environment variable after you generate a API key in theBedrock console.

export AWS_BEARER_TOKEN_BEDROCK=bedrock-api-key-XXXXXXXXXX

Run the following CLI command to use the Claude Fable 5 model.

aws bedrock put-account-data-retention \ 
 --mode provider_data_share

To learn more, visit theData Retention APIon the Amazon Bedrock User Guide.

How to use the Claude Fable 5 modelLet’s start with Anthropic SDK for Python using the Messages API onbedrock-mantleendpoint. Install Anthropic SDK.

pip install anthropic

Here is a sample Python code to call Claude Fable 5 model:

import anthropic

client = anthropic.Anthropic(
 base_url="https://bedrock-mantle.us-east-1.api.aws/anthropic",
 api_key= <your-bedrock-api-key>
)

message = client.messages.create( 
 model="anthropic.claude-fable-5", 
	 max_tokens=4096, 
	 messages=[ 
	 { "role": "user", 
		 "content": "Design a distributed architecture on AWS in Python that should support 100k requests per second across multiple geographic regions", 
		 }, 
	 ], 
)

print(message.content[0].text)

To learn more, check outAnthropic Messages API code examplesandnotebook examplesfor multiple use cases and a variety of programming languages.

You can use Claude Fable 5 in theBedrock console. ChooseClaude Fable 5in thePlaygroundand test it.

You can also use Claude Fable 5 with the Invoke API and Converse API onbedrock-runtimeendpoint. Here’s an example to call Converse API for a unified multi-model experience using the AWS SDK for Python (Boto3):

import boto3 
bedrock_runtime = boto3.client("bedrock-runtime", region_name="us-east-1") 
response = bedrock_runtime.converse( 
 modelId="global.anthropic.claude-fable-5", 
 messages=[ 
 { 
 "role": "user", 
 "content": [ 
 { 
 "text": "Design a distributed architecture on AWS in Python that should support 100k requests per second across multiple geographic regions." 
 } 
 ] 
 } 
 ], 
 inferenceConfig={ 
 "maxTokens": 4096 
 } 
) 
print(response["output"]["message"]["content"][0]["text"]) 

To learn more, visitcode examplesthat show how to use Amazon Bedrock Runtime with AWS SDKs.

Things to knowLet me share some important technical details that I think you’ll find useful.

* Model access— Claude Fable 5 access is gradually expanding for all AWS accounts. If your account doesn’t have access yet, it will be enabled soon depending on your Bedrock usage. If you want to get access to this model quickly, contact your usual AWS Support.
* Pricing— When a harmful prompt is routed to Opus 4.8 instead of Fable 5, you pay only Opus prices. If a request is blocked mid-conversation, initial tokens are charged at Fable rates and subsequent tokens at Opus rates. To learn more, visit theAmazon Bedrock pricingpage.
* Data retention— For Fable 5, Mythos 5, and future models on Bedrock with similar or higher capability levels, Anthropic will require 30-day retention for all traffic on Mythos-class models. Retaining data for a limited period allows Anthropic to detect patterns of misuse that are not visible from a single exchange. Once you opt into data retention, your data will leave AWS’s data and security boundary.
* Claude Mythos 5 on Bedrock (Limited Preview)— You can also use Anthropic’s most capable model for cybersecurity and life sciences, including vulnerability discovery, drug design, and biodefense screening. Access is currently limited due to the dual-use nature of these domains. To learn more, visit themodel card documentation.

Now availableAnthropic’s Claude Fable 5 model is available today on Amazon Bedrock in the US East (N. Virginia) and Europe (Stockholm) Regions; check thefull list of Regionsfor future updates. Claude Fable 5 is also available on the Claude Platform on AWS in North America, South America, Europe, and Asia Pacific.

Give Claude Fable 5 a try with the Amazon Bedrock APIs, in theClaude Platform on AWS, and send feedback toAWS re:Post for Amazon Bedrockor through your usual AWS Support contacts.

—Channy

Updated on June 9, 2026— 1) Updated the console screenshot. You can use the console onbedrock-runtimeengine. The console support onbedrock-mantleis coming soon. 2) Fixed the right model id in the sample code, 3) Fixed correctprovider_data_shareparameter, 4) Add a data retention setting script forbedrock-runtimeengine.

Updated on June 10, 2026—Added how to configure data retention setting through AWS SigV4 and AWS CLI.