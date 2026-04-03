---
title: Web search · Ollama Blog
url: https://ollama.com/blog/web-search
date: 2025-09-26
site: hackernews
model: llama3.2:1b
summarized_at: 2025-09-26T11:15:13.876750
screenshot: hackernews-web-search-ollama-blog.png
---

# Web search · Ollama Blog

# Web Search with Ollama API

## Introduction to Ollama's Web Search API

The Ollama web search API provides a powerful and efficient way to integrate machine learning models into web applications. Utilizing the latest information from the web, this API can help reduce hallucinations and improve accuracy in various applications.

### Key Features of Ollama's Web Search API

- **Generous Free Tier**: A generous free tier is available for individual users to use web searches.
- **Higher Rate Limits**: Higher rate limits are also available via Ollama’s cloud, suitable for more resource-intensive applications.
- **Deep Tool Integrations**: Web search capabilities can be integrated seamlessly with Ollama’s Python and JavaScript libraries.

### Getting Started with Ollama's Web Search API

1.  Verify Your Account: Create an API key from your Ollama account to enable access to the web search API.
2.  Set API Headers: Use a Bearer token in your API requests as the authentication method.
3.  CURL Example:
    *   ```bash
curl --header "Authorization: Bearer $OLLAMA_API_KEY" \
     https://ollama.com/api/web_search \
      --data '{
        "query": "what is ollama"
      }'
```

### Python and JavaScript API Calls

To use the web search API from your applications, include following code snippets:

#### **Python Code**
```python
import ollama

# Set up API credentials
ollama.api_key = "your_api_key"

# Perform a basic HTTP request with curl-like syntax
response = ollama.web_search(query="what is ollama")
print(response)
```

-   Alternatively, use libraries like `requests` or `urllib3` to simplify the process.
```python
import requests

api_key = "your_api_key"
response = requests.post(
    f"https://ollama.com/api/web_search",
    headers={"Authorization": f"Bearer {api_key}"},
    data={"query": "what is ollama"},
)
print(response.json())
```

#### **JavaScript Code**
```javascript
// Set API credentials with Ollama's JavaScript library
const client = new Ollama();

// Use the Ollama web search function
client.webSearch({ query: "what is ollama" })
  .then((result) => {
    console.log(result);
  })
  .catch((error) => {
    console.error(error);
  });
```

### Example Web Search Results

*   [Ollama](https://ollama.com/)
*   [What is Ollama? Introduction to the AI model management tool](https://www.hostinger.com/tutorials/what-is-ollama)
*   [Ollama Explained: Transforming AI Accessibility and Language Processing](https://www.geeksforgeeks.org/artificial-intelligence/ollama-explained-transforming-ai-accessibility-and-language-processing/)
