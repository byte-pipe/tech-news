---
title: How to publish posts via the dev.to API - DEV Community
url: https://dev.to/julies1/how-to-publish-posts-via-the-devto-api-2fkd
date: 2026-10-21
site: devto
model: llama3.2:1b
summarized_at: 2026-10-22T16:12:57.516979
---

# How to publish posts via the dev.to API - DEV Community

**Using the dev.to API with Requests and python-frontmatter**

**Approach 1: Using curl from the command line**
```bash
# Get your dev.to API key
dev.to account settings > Extensions > DEV Community API Keys
Give your key a name and generate API Key
Expand Active API Keyslist
 Arrow next to your key → Expand Content

Replace YOUR_KEY with your actual API key
curl 
-X 
POST https://dev.to/api/articles
 
-H 
"api-key: YOUR_KEY"
 
-H 
"Content-Type: application/json"
 
-d 
 '''
{
 "article": {
 "title": "My First Post",
 "body_markdown": "# Hello\n\nThis is my post.",
 "tags": ["python", "api"],
 "published": false 
 }
 }
'
```

**Approach 2: Using a Python script using requests and python-frontmatter**

**Requirements**

Install the following packages:

```bash
pip install requests python-frontmatter
```

**script.py**
```python
import os
import json
import requests

def get_dev_to_api_key():
    dev_to_account_settings = open('dev_to_api_key.txt', 'r').read()
    dev_to_account_key = dev_to_account_settings.split('.')[0]
    return dev_to_account_key

def setup_dev_to_api():
    api_key = os.environ.get('DEV_TO_API_KEY')
    dev_to_settings = open('dev_to_settings.txt', 'r').read()
    dev_to_account_key = dev_to_settings.split('.')[0]
    return dev_to_account_key, api_key

def create_new_article():
    api_key = setup_dev_to_api()[1]
    dev_to_api_key, dev_to_settings = setup_dev_to_api()
    article_settings = open('article_settings.json', 'r').read()
    article_settings = json.loads(article_settings)
    
    api_url = 'https://dev.to/api/articles'
    api_headers = {
        'api-key': api_key,
        'Content-Type': 'application/json'
    }
    
    article_data = {
        'article': {
            'title': article_settings.get('title', ''),
            'body_markdown': '#' + article_settings.get('title') + '\n\n' + article_settings.get('body', '') + '.',
            'tags': article_settings.get('tags', []),
            'published': False
        }
    }
    
    for tag in article_settings.get('tags', []):
        api_data = {
            'tag': tag,
            'value': True
        }
        api_data['data']['tags'] = [api_data['tag']]
        for item in article_data['article'].get('tags', []):
            item['data']['options']['tag'].append(api_data)
        article_settings['data'].append(api_data)
    
    with open('article_settings.json', 'w') as output_file:
        json.dump(article_settings, output_file)

    return api_url, api_headers, article_data

def main():
    api_key = get_dev_to_api_key()
    dev_to_api_key, dev_to_settings = setup_dev_to_api()
    api_url, api_headers, article_data = create_new_article()
    
    headers = api_headers.copy()
    headers.update(api_headers)
    headers['Content-Type'] = 'application/json'
    
    response = requests.post(api_url, headers=headers, json=article_data)
    if response.status_code == 201:
        print('Article created successfully!')
    else:
        print(f'Failed to create article: {response.text}')

if __name__ == '__main__':
    main()
```

**Requirements**

Make sure to install the following packages:

```bash
pip install yaml
```

**script.py**

*   Get the dev.to API key by reading it from a file named `dev_to_api_key.txt`.
*   Initialize the API key and settings environment variables.
*   Create the article data with the required settings and tags.
*   Use the `requests` library to send a POST request to the API with the article data.
*   Print a success message with a 201 status code or an error message with a status code less than 201.

This script aims to provide a more scalable and automated solution for publishing posts on dev.to.