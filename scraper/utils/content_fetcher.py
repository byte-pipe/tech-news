"""
Content fetcher module for retrieving and extracting article content.

This module provides functionality to:
1. Fetch the full content of articles
2. Extract the main content from HTML
3. Convert HTML to clean markdown format
4. Save the content to disk with metadata
"""

import logging
import os
import re
from datetime import datetime
from typing import Dict, Optional
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

# Configure logging
logger = logging.getLogger(__name__)


class ContentFetcher:
    """Fetches and extracts content from web pages."""

    def __init__(self, project_root=None):
        """Initialize the content fetcher.

        Args:
            project_root: Root directory of the project. If None, it's automatically determined.
        """
        if project_root is None:
            # Get the project root directory (three levels up from this file)
            self.project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
        else:
            self.project_root = project_root

        self.session = requests.Session()
        self.session.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"})

    def fetch_content(self, url: str, site_name: str, metadata: Dict = None, force: bool = False, max_age_hours: int = 24) -> Dict:
        """Fetch and extract content from a URL.

        Args:
            url: The URL to fetch content from
            site_name: Name of the site being scraped
            metadata: Optional metadata about the article
            force: Ignored (kept for backward compatibility)
            max_age_hours: Ignored (kept for backward compatibility)

        Returns:
            Dictionary with article metadata and content information
        """
        if metadata is None:
            metadata = {}

        # Check if content file already exists to avoid duplicate fetching
        existing_file = self._check_existing_content(url, site_name)
        if existing_file and not force:
            logger.info(f"Content already exists for {url} at {existing_file}")
            metadata["local_path"] = existing_file
            metadata["cached"] = True

            # Try to read the existing content
            try:
                with open(existing_file, "r", encoding="utf-8") as f:
                    # Skip YAML frontmatter
                    in_frontmatter = False
                    content_lines = []

                    for line in f:
                        if line.strip() == "---":
                            if in_frontmatter:
                                in_frontmatter = False
                            else:
                                in_frontmatter = True
                            continue

                        if not in_frontmatter:
                            content_lines.append(line)

                    metadata["content"] = "".join(content_lines)
            except Exception as e:
                logger.error(f"Error reading existing content for {url}: {str(e)}")

            return metadata

        # Fetch the page content
        try:
            logger.info(f"Fetching content from {url}")
            response = self.session.get(url, timeout=30)
            response.raise_for_status()

            # Extract content
            soup = BeautifulSoup(response.content, "html.parser")
            extracted_content = self._extract_content(soup, url)
            markdown_content = self._html_to_markdown(extracted_content["content"])

            # Update metadata
            metadata.update(extracted_content["metadata"])
            metadata["content"] = markdown_content
            metadata["fetched_at"] = datetime.now().isoformat()

            # Save the content
            file_path = self._save_content(url, site_name, markdown_content, metadata)
            metadata["local_path"] = file_path

            logger.info(f"Successfully fetched and saved content from {url}")
            return metadata

        except requests.exceptions.RequestException as e:
            error_msg = f"Network error fetching {url}: {str(e)}"
            logger.error(error_msg)
            metadata["error"] = error_msg
            return metadata
        except Exception as e:
            error_msg = f"Error fetching content from {url}: {str(e)}"
            logger.error(error_msg)
            metadata["error"] = error_msg
            return metadata

    def _check_existing_content(self, url: str, site_name: str) -> Optional[str]:
        """Check if content for this URL already exists in today's folder.

        Args:
            url: The URL to check
            site_name: Name of the site

        Returns:
            Path to existing file if found, None otherwise
        """
        date_folder = datetime.now().strftime("%Y-%m-%d")
        content_dir = os.path.join(self.project_root, "data", date_folder, "content")

        if not os.path.exists(content_dir):
            return None

        # Create a slug from the URL to match against existing files
        parsed_url = urlparse(url)
        path_parts = parsed_url.path.strip("/").split("/")
        possible_slug = path_parts[-1] if path_parts else ""

        # Look for files that might match this URL
        for filename in os.listdir(content_dir):
            if filename.startswith(site_name) and filename.endswith(".md"):
                # Check if the slug matches
                if possible_slug and possible_slug in filename:
                    return os.path.join(content_dir, filename)

                # Read the file to check the URL in frontmatter
                try:
                    with open(os.path.join(content_dir, filename), "r", encoding="utf-8") as f:
                        lines = f.readlines()
                        for i, line in enumerate(lines):
                            if line.startswith("url:") and url in line:
                                return os.path.join(content_dir, filename)
                            # Stop after frontmatter ends
                            if i > 0 and line.strip() == "---":
                                break
                except Exception:
                    continue  # nosec B112 - legitimate use for iterating files

        return None

    def _extract_content(self, soup: BeautifulSoup, url: str) -> Dict:
        """Extract the main content from a web page.

        Args:
            soup: BeautifulSoup object of the page
            url: The URL of the page (for context)

        Returns:
            Dictionary with 'content' (BeautifulSoup object) and 'metadata' dict
        """
        metadata = {}

        # Extract metadata
        title_tag = soup.find("title")
        if title_tag:
            metadata["title"] = title_tag.get_text(strip=True)

        # Meta tags
        for meta in soup.find_all("meta"):
            if meta.get("name") == "description":
                metadata["description"] = meta.get("content", "")
            elif meta.get("name") == "author":
                metadata["author"] = meta.get("content", "")
            elif meta.get("property") == "og:title":
                metadata["og_title"] = meta.get("content", "")
            elif meta.get("property") == "article:published_time":
                metadata["published_date"] = meta.get("content", "")

        # Try to find the main content area
        # Common content selectors in order of preference
        content_selectors = [
            "main",
            "article",
            '[role="main"]',
            ".main-content",
            "#main-content",
            ".content",
            "#content",
            ".post-content",
            ".entry-content",
            ".article-content",
            ".markdown-body",  # GitHub
            ".blob-wrapper",  # GitHub code
            ".story-body",  # News sites
            ".article-body",
            "body",  # Fallback
        ]

        content = None
        for selector in content_selectors:
            content = soup.select_one(selector)
            if content:
                break

        if not content:
            content = soup.body if soup.body else soup

        # Remove unwanted elements
        for tag in content.find_all(["script", "style", "nav", "header", "footer", "aside", "iframe"]):
            tag.decompose()

        # Remove elements with certain classes
        unwanted_classes = ["sidebar", "navigation", "menu", "ads", "advertisement", "social-share", "comments", "related-posts"]
        for class_name in unwanted_classes:
            for element in content.find_all(class_=lambda x: x and class_name in x):
                element.decompose()

        return {"content": content, "metadata": metadata}

    def _html_to_markdown(self, soup_content) -> str:
        """Convert HTML content to markdown format with basic formatting.

        Args:
            soup_content: BeautifulSoup object containing the content

        Returns:
            Markdown-formatted string
        """
        if not soup_content:
            return ""

        try:
            # Create a copy to avoid modifying the original
            soup = BeautifulSoup(str(soup_content), "html.parser")

            # Simple approach: just get the text content
            # More complex conversions often cause the "Cannot replace an element" errors

            # Remove script and style elements first
            for element in soup(["script", "style"]):
                element.decompose()

            # Get text with basic preservation of structure
            lines = []

            # Process headers
            for i in range(1, 7):
                for header in soup.find_all(f"h{i}"):
                    text = header.get_text(strip=True)
                    if text:
                        lines.append(f"\n{'#' * i} {text}\n")
                        header.replace_with(f"\n{'#' * i} {text}\n")

            # Process paragraphs
            for p in soup.find_all("p"):
                text = p.get_text(strip=True)
                if text:
                    lines.append(f"\n{text}\n")
                    p.replace_with(f"\n{text}\n")

            # Process lists
            for ul in soup.find_all("ul"):
                for li in ul.find_all("li"):
                    text = li.get_text(strip=True)
                    if text:
                        lines.append(f"* {text}")
                ul.replace_with("\n".join(f"* {li.get_text(strip=True)}" for li in ul.find_all("li") if li.get_text(strip=True)))

            for ol in soup.find_all("ol"):
                items = []
                for i, li in enumerate(ol.find_all("li"), 1):
                    text = li.get_text(strip=True)
                    if text:
                        items.append(f"{i}. {text}")
                ol.replace_with("\n".join(items))

            # Get remaining text
            text = soup.get_text(separator="\n")

            # Clean up excessive whitespace
            text = re.sub(r"\n{3,}", "\n\n", text)
            text = re.sub(r" {2,}", " ", text)

            return text.strip()

        except Exception as e:
            logger.warning(f"Error in HTML to markdown conversion: {str(e)}. Falling back to simple text extraction.")
            # Fallback: just get plain text
            try:
                return soup_content.get_text(separator="\n", strip=True)
            except Exception:
                return str(soup_content)

    def _save_content(self, url: str, site_name: str, markdown_content: str, metadata: Dict) -> str:
        """Save the markdown content to a file with YAML frontmatter.

        Args:
            url: URL of the original content
            site_name: Name of the site the content was fetched from
            markdown_content: The markdown content to save
            metadata: Dictionary of metadata about the article

        Returns:
            Path to the saved file
        """
        # Create a folder for the content
        now = datetime.now()
        date_folder = now.strftime("%Y-%m-%d")
        timestamp = now.strftime("%Y%m%d-%H%M%S")

        # Create a slug from the title or URL
        title = metadata.get("title", "")
        if title:
            slug = re.sub(r"[^\w\s-]", "", title.lower())
            slug = re.sub(r"[\s-]+", "-", slug).strip("-")
            slug = slug[:50]  # Limit length
        else:
            # Use URL path as fallback
            parsed_url = urlparse(url)
            path = parsed_url.path.strip("/")
            slug = path.split("/")[-1]
            # Remove file extension if present
            slug = re.sub(r"\.[^.]+$", "", slug)
            # Sanitize
            slug = re.sub(r"[^\w\s-]", "", slug.lower())
            slug = re.sub(r"[\s-]+", "-", slug).strip("-")
            if not slug:
                slug = f"{site_name}-content"

        # Use organized directory structure
        from scraper.core.data_organizer import DataOrganizer

        data_organizer = DataOrganizer(self.project_root)
        try:
            data_organizer.create_organized_structure(date_folder)
            organized_dirs = data_organizer.get_organized_paths(date_folder)
            content_dir = organized_dirs["content"]
        except Exception as e:
            logger.error(f"Failed to create organized directory structure: {str(e)}")
            # Fallback to basic directory creation
            content_dir = os.path.join(self.project_root, "data", date_folder, "content")
            try:
                os.makedirs(content_dir, exist_ok=True)
                logger.warning(f"Using fallback content directory: {content_dir}")
            except Exception as fallback_error:
                logger.error(f"Critical: Failed to create content directory: {str(fallback_error)}")
                raise RuntimeError(f"Cannot create content directory: {str(fallback_error)}")

        # Create the file path
        file_path = os.path.join(content_dir, f"{site_name}-{timestamp}-{slug}.md")

        # Create YAML frontmatter
        frontmatter = {
            "title": metadata.get("title", ""),
            "url": url,
            "site_name": site_name,
            "fetched_at": now.isoformat(),
            "original_url": url,
        }

        # Add important metadata to frontmatter
        for key in ["author", "date", "published_date", "description", "tags", "keywords"]:
            if key in metadata and metadata[key]:
                frontmatter[key] = metadata[key]

        # Convert frontmatter to YAML
        frontmatter_str = "---\n"
        for key, value in frontmatter.items():
            if isinstance(value, list):
                frontmatter_str += f"{key}:\n"
                for item in value:
                    frontmatter_str += f"  - {item}\n"
            else:
                # Properly handle multi-line strings
                if isinstance(value, str) and ("\n" in value or ":" in value):
                    frontmatter_str += f"{key}: |\n"
                    for line in value.split("\n"):
                        frontmatter_str += f"  {line}\n"
                else:
                    frontmatter_str += f"{key}: {value}\n"
        frontmatter_str += "---\n\n"

        # Write to file
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(frontmatter_str)
            f.write(markdown_content)

        logger.info(f"Saved content to {file_path}")

        return file_path


def fetch_url_content(url: str, site_name: str, metadata: Dict = None, force: bool = False) -> Dict:
    """Convenience function to fetch content from a URL.

    Args:
        url: The URL to fetch content from
        site_name: Name of the site being scraped
        metadata: Optional metadata about the article
        force: Whether to force a refetch even if content exists

    Returns:
        Dictionary with article metadata and content information
    """
    fetcher = ContentFetcher()
    return fetcher.fetch_content(url, site_name, metadata, force)


# Example usage
if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    # Example URL
    url = "https://github.blog/2023-03-08-github-codeql-query-packs-code-scanning/"
    site_name = "github"

    # Fetch the content
    result = fetch_url_content(url, site_name)

    # Print some information
    print(f"Title: {result.get('title', '')}")
    print(f"Local path: {result.get('local_path', '')}")
    print(f"Content length: {len(result.get('content', ''))}")
