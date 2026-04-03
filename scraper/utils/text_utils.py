import re
from urllib.parse import urlparse


def normalize_whitespace(text):
    return re.sub(r"\s+", " ", text).strip() if text else ""


def clean_for_yaml(text, max_length=200):
    if not text:
        return ""
    cleaned = normalize_whitespace(text)
    if len(cleaned) > max_length:
        cleaned = cleaned[:max_length].rstrip() + "..."
    return cleaned


def create_content_slug(title, url=None, max_length=50):
    """Create a consistent URL-friendly slug from a title or URL.

    Args:
        title: Article title to slugify.
        url: Fallback URL if title is empty.
        max_length: Maximum slug length.

    Returns:
        A lowercase hyphen-separated slug string.
    """
    source = title
    if not source and url:
        parsed = urlparse(url)
        path = parsed.path.strip("/")
        source = path.split("/")[-1] if path else ""
        source = re.sub(r"\.[^.]+$", "", source)  # remove file extension

    if not source:
        return "content"

    slug = re.sub(r"[^\w\s-]", "", source.lower())
    slug = re.sub(r"[\s-]+", "-", slug).strip("-")
    return slug[:max_length].rstrip("-")
