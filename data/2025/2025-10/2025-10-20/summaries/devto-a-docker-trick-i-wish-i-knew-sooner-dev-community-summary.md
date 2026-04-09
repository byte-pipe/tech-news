---
title: A Docker Trick I Wish I Knew Sooner - DEV Community
url: https://dev.to/joybtw/a-docker-trick-i-wish-i-knew-sooner-23of
date: 2025-10-16
site: devto
model: llama3.2:1b
summarized_at: 2025-10-20T11:17:16.324828
screenshot: devto-a-docker-trick-i-wish-i-knew-sooner-dev-community.png
---

# A Docker Trick I Wish I Knew Sooner - DEV Community

# Using ADD Instruction for Efficient File Download with Docker

Docker simplifies file download by utilizing the `ADD` instruction, which fetches remote files directly without requiring external packages like `curl` or `wget`.

## Directly Adding a Remote File to an Image

The provided example demonstrates this straightforward approach using the `FROM`, `WORKDIR`, `ADD`, and `EXPOSE` directives:

*   `FROM alpine:latest`: Sets the base image used for our container.
*   `WORKDIR /app`: Configures the working directory in the new image at `/app`.
*   `RUN apk add --no-cache curl`, installs the `curl` package without caching:
    ```
 RUN apk add --no-cache
             curl
```
This step initializes the container with the desired packages available globally, making it easier to manage dependencies.
*   `ADD https://example.com/anotherfile.json /app/anotherfile.json`: Downloads a separate file from an external source and adds itself to the `/app` directory in the image.

## Comparison with Using Curl or Wget

For comparison, the original code using `curl` and `wget` demonstrates how these tools are often used:
*   `FROM alpine:latest`
*   `WORKDIR /app`
*   `RUN apk add --no-cache curl`, installs `curl` and allows the download of a file from a URL.
    ```
 RUN apk add
             --no-cache
             curl

RUN curl \
         -sS \
         https://example.com/somefile.txt \
         -o \
         /app/somefile.txt
```

## Advantages and Use Cases

-   **Smaller Image Size:** Using `ADD` results in a smaller image size, making it suitable for optimization when building Docker images.

-   **Fewer Dependencies:** By not requiring external packages like `curl`, the Docker build process becomes simpler and more streamlined.

### Best Practices

-   **Use ADD for Remote Files Only:** Employing `ADD` is particularly advisable when downloading files from the internet, as it avoids unnecessary installation of extra tools or packages.

### Additional Considerations

-   **Authentication and Security:** Be mindful of security concerns when using external services. Verify authentication methods to ensure data integrity and comply with any necessary regulations.
-   **Complexity:** Recognize that complex workflows or multiple steps may necessitate the use of `curl` for handling headers, authentication, retries, or additional processing steps.

Docker's implementation of the `ADD` instruction makes it an effective choice for efficiently downloading remote files, leading to a leaner and simpler Docker image.
