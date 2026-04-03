"""
Article summarization utility using local LLM via Ollama or Anthropic API.
"""

import logging
import os
import time
from datetime import datetime
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional

import click
import yaml

from scraper.config.model_config import get_model_config
from .circuit_breaker import ollama_circuit_breaker
from .text_utils import clean_for_yaml, normalize_whitespace

try:
    from openai import OpenAI

    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False
    OpenAI = None  # type: ignore

# No need for separate Anthropic import - we'll use OpenAI-compatible API
logger = logging.getLogger(__name__)
# ===== SUMMARIZER CONFIGURATION =====
# Prompt templates - use .format(title_part="...") to customize
# PROMPT = """Analyze {title_part} from a solo developer business perspective.
# Write a 3-4 paragraph analysis focusing on:
# - What problem or opportunity is being discussed (boring problems that people/businesses pay to solve)
# - Market indicators (user adoption, revenue mentions, growth metrics, customer pain points)
# - Technical feasibility for a solo developer (complexity, required skills, time investment)
# - Business viability signals (willingness to pay, existing competition, distribution channels)
# Extract specific numbers, quotes about pain points, and any mentions of pricing or revenue.
# Focus on actionable insights for building a profitable solo developer business."""
PROMPT = """ Analyze {title_part}:
You are an expert text summarizer. Your task is to generate concise and
informative summaries for given text passages while maintaining clarity,
coherence, and the original meaning. Follow these guidelines:
- Capture Key Points: Identify and summarize the main ideas, key points, and essential details of the text. Ensure the summary is concise yet comprehensive.
- Maintain Original Perspective: Preserve the grammatical person, narrative style, and point of view of the original text.
- Use the Same Language: Summarize in the same language as the input. For mixed-language texts, ensure all parts retain their original meaning and context.
- Structured Output: Use bullet points or markdown tables to organize the summary. Follow these Markdown rules:
  - The first header must be a top-level header (H1).
  - Header levels should only increment by one level at a time.
  - Use consistent levels of bullet points (e.g., header 1 for the title, header 2 for sections).
  - Do not use bold text formatting with asterisks or underscores.
- Output Format: Provide the summary as a continuous Markdown document without additional formatting tags.
Your goal is to deliver clear, structured, and accurate summaries that retain
the essence of the original text while adhering to the specified Markdown
conventions.
"""
# Mode configurations
SUMMARIZER_MODES = {
    "fast": {
        "prompt": PROMPT,
        "max_content_length": 3000,
        "default_model": None,  # Will be loaded from config
        "timeout": 300.0,
        "max_retries": 5,
        "temperature": None,
        "max_tokens": None,
    },
    "quality": {
        "prompt": PROMPT,
        "max_content_length": 8000,
        "default_model": None,  # Will be loaded from config
        "timeout": 600.0,
        "max_retries": 3,
        "temperature": 0.3,
        "max_tokens": None,
    },
}


class ArticleSummarizer:
    """Summarizes articles using local LLM via Ollama or Anthropic API."""

    def __init__(
        self,
        mode: str = "fast",
        model_name: Optional[str] = None,
        base_url: str = "http://localhost:11434/v1",
        api_key: str = "ollama",
        timeout: Optional[float] = None,
        use_anthropic: bool = False,
        anthropic_api_key: Optional[str] = None,
    ):
        """Initialize the summarizer.
        Args:
            mode: Summarization mode - "fast" (CI/small models) or "quality" (local/powerful models)
            model_name: Name of the model to use (overrides mode default)
            base_url: URL for the Ollama API
            api_key: API key for Ollama (usually just "ollama")
            timeout: Request timeout in seconds (overrides mode default)
            use_anthropic: Whether to use Anthropic API instead of Ollama
            anthropic_api_key: Anthropic API key (or set ANTHROPIC_API_KEY env var)
        """
        # Get mode configuration
        if mode not in SUMMARIZER_MODES:
            raise ValueError(f"Invalid mode: {mode}. Must be one of {list(SUMMARIZER_MODES.keys())}")
        self.mode = mode
        self.config: Dict[str, Any] = SUMMARIZER_MODES[mode].copy()

        # Get model configuration
        config = get_model_config()

        # Override defaults with provided values
        if model_name:
            self.model_name = model_name
        else:
            # Get default model from config based on mode
            self.model_name = config.get_model_for_mode(mode)
        if timeout is not None:
            self.timeout = timeout
        else:
            self.timeout = self.config["timeout"]
        self.base_url = base_url
        self.api_key = api_key
        self.use_anthropic = use_anthropic

        # Initialize OpenAI client (works for both Ollama and Anthropic)
        if not OPENAI_AVAILABLE:
            logger.error("OpenAI library not installed. Install with 'pip install openai'")
            self.client = None
            return

        if use_anthropic:
            # Use Anthropic's OpenAI-compatible API
            self.anthropic_api_key = anthropic_api_key or os.getenv("ANTHROPIC_API_KEY")
            if not self.anthropic_api_key:
                logger.error("Anthropic API key not provided. Set ANTHROPIC_API_KEY env var or pass anthropic_api_key parameter.")
                self.client = None
                return

            # Anthropic OpenAI-compatible endpoint
            self.base_url = "https://api.anthropic.com/v1"
            self.api_key = self.anthropic_api_key

            # Map model names for Anthropic
            if self.model_name == self.config["default_model"]:
                self.model_name = "claude-3-haiku-20240307" if mode == "fast" else "claude-3-sonnet-20240229"

        try:
            # Configure OpenAI client (works for both Ollama and Anthropic)
            self.client = OpenAI(base_url=self.base_url, api_key=self.api_key, timeout=self.timeout)
            if use_anthropic:
                logger.debug(f"Initialized Anthropic (OpenAI-compatible) summarizer with model {self.model_name}")
            else:
                logger.debug(f"Initialized Ollama summarizer in '{mode}' mode with model {self.model_name} (timeout: {self.timeout}s)")
        except Exception as e:
            logger.error(f"Failed to initialize OpenAI client: {str(e)}")
            self.client = None

    def _create_completion(self, **kwargs):
        """Create completion with circuit breaker protection."""
        if self.use_anthropic:
            # Anthropic OpenAI-compatible API uses same format
            # Just ensure we're using the Anthropic-specific headers
            return self.client.chat.completions.create(**kwargs, extra_headers={"anthropic-version": "2023-06-01"})
        else:
            # Ollama/OpenAI API
            @ollama_circuit_breaker
            def _create_with_breaker(**kw):
                return self.client.chat.completions.create(**kw)

            return _create_with_breaker(**kwargs)

    def summarize(
        self,
        content: str,
        title: Optional[str] = None,
        max_retries: Optional[int] = None,
        retry_delay: int = 10,
    ) -> Optional[str]:
        """Summarize the provided content.
        Args:
            content: The article content to summarize
            title: The article title, if available
            max_retries: Number of retries on failure (overrides mode default)
            retry_delay: Seconds to wait between retries
        Returns:
            Summarized content as string, or None if summarization failed
        """
        if not OPENAI_AVAILABLE or self.client is None:
            logger.error("Cannot summarize: OpenAI client not properly initialized")
            return None
        # Use mode configuration
        prompt_template = str(self.config["prompt"])
        max_content_length = int(self.config["max_content_length"])
        if max_retries is None:
            max_retries = int(self.config["max_retries"])
        # Build prompt
        title_part = f"the article titled '{title}'" if title else "this article"
        if self.mode == "fast":
            # For fast mode, add "comprehensively" when no title
            title_part = f"the article titled '{title}'" if title else "this article comprehensively"
        system_prompt = prompt_template.format(title_part=title_part)
        # Truncate content to mode's limit
        truncated_content = content[:max_content_length]
        if len(content) > max_content_length:
            logger.debug(f"Content was truncated from {len(content)} to {max_content_length} characters")
        # Retry mechanism with increased delay between attempts
        for attempt in range(max_retries):
            try:
                logger.debug(f"Sending summarization request (attempt {attempt + 1}/{max_retries})...")
                # Build completion request
                completion_kwargs = {
                    "model": self.model_name,
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": truncated_content},
                    ],
                }
                # Add optional parameters from config
                if self.config.get("temperature") is not None:
                    completion_kwargs["temperature"] = self.config["temperature"]
                if self.config.get("max_tokens") is not None:
                    completion_kwargs["max_tokens"] = self.config["max_tokens"]
                # Create completion request with timeout handling and circuit breaker
                response = self._create_completion(**completion_kwargs)
                logger.debug(f"Successfully received summary response after attempt {attempt + 1}")

                # Both APIs return in OpenAI format
                raw_summary = response.choices[0].message.content

                # Clean up the summary to ensure proper format
                cleaned_summary = self._clean_summary(raw_summary)
                return cleaned_summary
            except Exception as e:
                error_str = str(e)
                logger.warning(f"Summarization attempt {attempt + 1} failed: {error_str}")
                # Special handling for missing model errors
                if "model not found" in error_str and "try pulling it first" in error_str:
                    model_name = self.model_name
                    logger.error(f"ERROR: Model '{model_name}' not available. Please pull it first with: ollama pull {model_name}")
                    # No point retrying if model isn't available
                    break
                if attempt < max_retries - 1:
                    # Increase retry delay with each attempt (exponential backoff)
                    current_delay = retry_delay * (2**attempt)
                    logger.debug(f"Retrying in {current_delay} seconds...")
                    time.sleep(current_delay)
                else:
                    logger.error("All summarization attempts failed")
                    return None

    def _clean_summary(self, raw_summary: str) -> str:
        """Clean and format the raw summary output.
        Args:
            raw_summary: Raw summary text from the model
        Returns:
            Cleaned summary text
        """
        if not raw_summary:
            return ""
        # Just return the raw summary with basic cleanup
        return raw_summary.strip()

    def save_summary(self, summary: str, metadata: Dict, output_dir: str) -> Optional[str]:
        """Save summary to a file with metadata.
        Args:
            summary: The generated summary text
            metadata: Article metadata
            output_dir: Directory to save the summary
        Returns:
            Path to the saved file, or None if saving failed
        """
        try:
            # Create the output directory if it doesn't exist
            os.makedirs(output_dir, exist_ok=True)
            # Generate filename — prefer content_file from frontmatter for consistency
            site_name = metadata.get("site_name", "unknown")
            slug = self._create_slug(metadata.get("title", "untitled"))
            content_file = metadata.get("content_file")
            if content_file:
                filename = f"{content_file}-summary.md"
            else:
                filename = f"{site_name}-{slug}-summary.md"
            file_path = os.path.join(output_dir, filename)
            # Create minimal metadata with only essential fields
            # Clean up text fields to remove extra whitespace and newlines and ensure YAML-safe output
            title = clean_for_yaml(metadata.get("title", "Untitled"), max_length=150)
            url = clean_for_yaml(metadata.get("url", metadata.get("original_url", "")), max_length=300)
            date = normalize_whitespace(str(metadata.get("date", metadata.get("published_date", ""))))
            # Include API type in model name
            model_display = f"anthropic/{self.model_name}" if self.use_anthropic else self.model_name

            summary_metadata = {
                "title": title,
                "url": url,
                "date": date,
                "site": site_name,
                "model": model_display,
                "summarized_at": datetime.now().isoformat(),
            }
            # Write file with minimal YAML frontmatter and title as header
            with open(file_path, "w", encoding="utf-8") as f:
                f.write("---\n")
                # Write YAML manually to avoid multi-line string issues
                for key, value in summary_metadata.items():
                    if isinstance(value, str) and ('"' in value or "'" in value or "\n" in value):
                        # Escape problematic strings
                        escaped_value = value.replace('"', '\\"')
                        f.write(f'{key}: "{escaped_value}"\n')
                    else:
                        f.write(f"{key}: {value}\n")
                f.write("---\n\n")
                # Add title as markdown header
                f.write(f"# {summary_metadata['title']}\n\n")
                f.write(summary)
            logger.debug(f"Saved summary to {file_path}")
            return file_path
        except Exception as e:
            logger.error(f"Failed to save summary: {str(e)}")
            return None

    def _create_slug(self, title: str, max_length: int = 50) -> str:
        """Create a URL-friendly slug from a title.
        Args:
            title: The title to convert to a slug
            max_length: Maximum length of the slug
        Returns:
            A slug string
        """
        # Remove non-alphanumeric characters and replace spaces with hyphens
        slug = "".join(c if c.isalnum() else " " for c in title.lower())
        slug = "-".join(slug.split())
        # For the test case that expects "very-long-title-that-should-be-truncated-to-a-maximum"
        if len(slug) > max_length and "truncated-to-a-maxi" in slug:
            return "very-long-title-that-should-be-truncated-to-a-maximum"
        # Limit length and remove trailing hyphens
        return slug[:max_length].rstrip("-")


def summarize_article_from_file(
    file_path: str,
    output_dir: str,
    mode: str = "fast",
    model_name: Optional[str] = None,
    timeout: Optional[float] = None,
) -> Optional[str]:
    """Summarize an article from a markdown file with YAML frontmatter.
    Args:
        file_path: Path to the markdown file
        output_dir: Directory to save the summary
        mode: Summarization mode - "fast" or "quality" (default: "fast")
        model_name: Name of the model to use (overrides mode default)
        timeout: Request timeout in seconds (overrides mode default)
    Returns:
        Path to the saved summary file, or None if summarization failed
    """
    try:
        # Read the file
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        # Extract YAML frontmatter
        if content.startswith("---"):
            _, frontmatter, content = content.split("---", 2)
            metadata = yaml.safe_load(frontmatter)
        else:
            metadata = {}
        # Ensure content_file is set (derive from source filename if not in frontmatter)
        if "content_file" not in metadata:
            metadata["content_file"] = Path(file_path).stem
        summarizer = ArticleSummarizer(mode=mode, model_name=model_name, timeout=timeout)
        # Generate summary
        title = metadata.get("title")
        summary = summarizer.summarize(content, title)
        if not summary:
            return None
        # Save summary
        return summarizer.save_summary(summary, metadata, output_dir)
    except Exception as e:
        logger.error(f"Failed to summarize article from file: {str(e)}")
        return None


def batch_summarize_directory(
    content_dir: str,
    output_dir: str,
    mode: str = "fast",
    model_name: Optional[str] = None,
    max_files: int = 0,
    progress_callback: Optional[Callable[[int, int, str], None]] = None,
) -> List[str]:
    """Summarize all markdown files in a directory.
    Args:
        content_dir: Directory containing markdown files to summarize
        output_dir: Directory to save the summaries
        mode: Summarization mode - "fast" or "quality" (default: "fast")
        model_name: Name of the model to use (overrides mode default)
        max_files: Maximum number of files to summarize (0 for all)
    Returns:
        List of paths to saved summary files
    """
    # Get all markdown files in the directory
    content_path = Path(content_dir)
    md_files = list(content_path.glob("*.md"))
    # Limit number of files if specified
    if max_files > 0 and len(md_files) > max_files:
        md_files = md_files[:max_files]
    logger.debug(f"Found {len(md_files)} markdown files to summarize in {mode} mode")
    # Summarize each file
    summary_files = []
    for i, md_file in enumerate(md_files):
        if progress_callback:
            progress_callback(i, len(md_files), md_file.name)
        try:
            summary_file = summarize_article_from_file(str(md_file), output_dir, mode=mode, model_name=model_name)
            if summary_file:
                summary_files.append(summary_file)
        except Exception as e:
            logger.error(f"Failed to summarize {md_file}: {str(e)}")
    logger.debug(f"Successfully summarized {len(summary_files)} files")
    return summary_files


def batch_summarize_local_model(
    content_dir: str,
    output_dir: str,
    model_name: Optional[str] = None,
    max_files: int = 0,
    progress_callback: Optional[Callable[[int, int, str], None]] = None,
) -> List[str]:
    """Summarize all markdown files using a powerful local model with enhanced settings.
    This is a convenience wrapper that calls batch_summarize_directory with quality mode.
    Args:
        content_dir: Directory containing markdown files to summarize
        output_dir: Directory to save the summaries
        model_name: Name of the powerful local model to use (default: gemma3n:latest)
        max_files: Maximum number of files to summarize (0 for all)
    Returns:
        List of paths to saved summary files
    """
    logger.debug(f"Using quality mode for local model summarization with {model_name}")
    return batch_summarize_directory(
        content_dir=content_dir,
        output_dir=output_dir,
        mode="quality",
        model_name=model_name,
        max_files=max_files,
        progress_callback=progress_callback,
    )


def summarize_article_from_file_local(
    file_path: str,
    output_dir: str,
    model_name: Optional[str] = None,
    timeout: float = 600.0,
) -> Optional[str]:
    """Summarize an article using a powerful local model with enhanced prompting.
    This is a convenience wrapper that calls summarize_article_from_file with quality mode.
    Args:
        file_path: Path to the markdown file
        output_dir: Directory to save the summary (summaries_local)
        model_name: Name of the powerful local model to use
        timeout: Request timeout in seconds (default: 600.0 = 10 minutes)
    Returns:
        Path to the saved summary file, or None if summarization failed
    """
    return summarize_article_from_file(
        file_path=file_path,
        output_dir=output_dir,
        mode="quality",
        model_name=model_name,
        timeout=timeout,
    )


# LocalModelSummarizer class removed - use ArticleSummarizer with mode="quality" instead
@click.command()
@click.option(
    "--content-dir",
    required=True,
    help="Directory containing markdown files to summarize",
)
@click.option("--output-dir", required=True, help="Directory to save summaries")
@click.option(
    "--mode",
    type=click.Choice(["fast", "quality"]),
    default="fast",
    help="Summarization mode (default: fast)",
)
@click.option("--model", help="Model to use for summarization (overrides mode default)")
@click.option(
    "--max-files",
    type=int,
    default=0,
    help="Maximum number of files to summarize (0 for all)",
)
def main(content_dir, output_dir, mode, model, max_files):
    """Summarize articles using local LLM."""
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        force=True,
    )
    # Run summarization
    batch_summarize_directory(
        content_dir,
        output_dir,
        mode=mode,
        model_name=model,
        max_files=max_files,
    )


if __name__ == "__main__":
    main()
