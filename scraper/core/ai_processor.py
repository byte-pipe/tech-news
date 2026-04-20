"""
AI processing functionality separated from main.py.
"""

import logging
import os

from scraper.config.model_config import get_model_config
from scraper.utils.summarizer import batch_summarize_directory

logger = logging.getLogger(__name__)


def summarize_content(date_dir, model_name=None, max_files=0, fallback_model=None, progress_callback=None):
    """Summarize fetched article content using LLM.

    Args:
        date_dir: Date directory where content files are stored (YYYY-MM-DD format)
        model_name: Name of the LLM model to use (default: smollm:135m)
        max_files: Maximum number of files to summarize (0 for all)
        fallback_model: Model to use if primary model is unavailable (default: tinyllama:latest)

    Returns:
        Tuple of (success_flag, list_of_summary_files)
        If success_flag is False, the operation had critical errors
    """
    # Try multiple ways to find the project root to be compatible with different environments
    possible_roots = [
        # scraper/core/ai_processor.py -> project root is 2 levels up
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
        # One level up from scraper directory (might work in GitHub Actions)
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        # Current working directory might be project root in some environments
        os.getcwd(),
    ]

    # Try to find a valid data directory
    content_dir = None
    summary_dir = None

    for root in possible_roots:
        data_dir = os.path.join(root, "data")
        test_content_dir = os.path.join(data_dir, date_dir, "content")
        test_summary_dir = os.path.join(data_dir, date_dir, "summaries")

        logger.info(f"Checking for content in: {test_content_dir}")
        if os.path.exists(data_dir):
            # If we found the data directory, use these paths even if content dir doesn't exist yet
            content_dir = test_content_dir
            summary_dir = test_summary_dir

            # If we actually found the content directory, that's ideal
            if os.path.exists(test_content_dir):
                logger.info(f"Found content directory at: {test_content_dir}")
                break

    # Check if we found a suitable data directory
    if content_dir is None:
        logger.error("Could not find valid data directory in any location")
        return (False, [])

    # Check if content directory exists
    if not os.path.exists(content_dir):
        logger.warning(f"Content directory not found: {content_dir}")

        # Create the content directory anyway - maybe files will be there later
        try:
            os.makedirs(content_dir, exist_ok=True)
            logger.info(f"Created missing content directory: {content_dir}")
        except Exception as e:
            logger.error(f"Failed to create content directory: {str(e)}")

        # Warn if there are markdown files in the date directory but not in content/
        date_dir_path = os.path.dirname(content_dir)
        if os.path.exists(date_dir_path):
            md_files = [f for f in os.listdir(date_dir_path) if f.endswith(".md")]
            if md_files:
                logger.warning(f"Found {len(md_files)} markdown files in date directory but content/ dir is missing — these may not be article content files")

    # Create summaries directory if it doesn't exist
    os.makedirs(summary_dir, exist_ok=True)

    # Get model configuration
    config = get_model_config()

    # Use provided model or get default based on mode
    if model_name is None:
        # Default to quality mode
        model_name = config.get_model_for_mode("quality")

    # Use provided fallback or get from config
    if fallback_model is None:
        # Determine mode based on model to get appropriate fallback
        small_models = ["tinyllama", "smollm", "phi", "1b", "3b", "7b"]
        model_lower = model_name.lower()
        if any(small in model_lower for small in small_models):
            mode = "fast"
            fallback_model = config.get_fallback_model("fast")
        else:
            mode = "quality"
            fallback_model = config.get_fallback_model("quality")
    else:
        # Determine mode based on model
        small_models = ["tinyllama", "smollm", "phi", "1b", "3b", "7b"]
        model_lower = model_name.lower()
        mode = "fast" if any(small in model_lower for small in small_models) else "quality"

    # Summarize files
    logger.debug(f"Summarizing content files using {model_name} in {mode} mode")
    try:
        summary_files = batch_summarize_directory(content_dir, summary_dir, mode=mode, model_name=model_name, max_files=max_files, progress_callback=progress_callback)

        # If summarization fails, check if it was due to missing model and try fallback
        if not summary_files:
            # Look for specific error message in logs
            logger.warning(f"Primary model '{model_name}' summarization failed or produced no results")

            if fallback_model and fallback_model != model_name:
                logger.info(f"Attempting summarization with fallback model: {fallback_model}")
                try:
                    # Try again with fallback model
                    summary_files = batch_summarize_directory(content_dir, summary_dir, mode="fast", model_name=fallback_model, max_files=max_files, progress_callback=progress_callback)

                    if summary_files:
                        logger.info(f"Successfully created {len(summary_files)} summary files using fallback model {fallback_model}")
                        return (True, summary_files)
                    else:
                        logger.error("Fallback summarization completed but no summary files were generated")
                        return (False, [])
                except Exception as e:
                    logger.error(f"Error during fallback summarization with {fallback_model}: {str(e)}")
                    return (False, [])
            else:
                logger.error("No fallback model specified or same as primary model")
                return (False, [])

        logger.info(f"Successfully created {len(summary_files)} summary files")
        return (True, summary_files)
    except Exception as e:
        logger.error(f"Error during summarization: {str(e)}")

        # If this was a model not found error, try fallback
        error_str = str(e).lower()
        if "model not found" in error_str and fallback_model and fallback_model != model_name:
            logger.info(f"Attempting summarization with fallback model: {fallback_model}")
            try:
                # Try again with fallback model
                summary_files = batch_summarize_directory(content_dir, summary_dir, mode="fast", model_name=fallback_model, max_files=max_files, progress_callback=progress_callback)

                if summary_files:
                    logger.info(f"Successfully created {len(summary_files)} summary files using fallback model {fallback_model}")
                    return (True, summary_files)
                else:
                    logger.error("Fallback summarization completed but no summary files were generated")
            except Exception as e2:
                logger.error(f"Error during fallback summarization with {fallback_model}: {str(e2)}")

        return (False, [])


def summarize_with_anthropic(date_dir, api_key=None, model=None, max_files=0, progress_callback=None):
    """Summarize content using Anthropic's Claude API.

    Args:
        date_dir: Date directory where content files are stored (YYYY-MM-DD format)
        api_key: Anthropic API key (or set ANTHROPIC_API_KEY env var)
        model: Claude model to use (default: claude-3-haiku-20240307)
        max_files: Maximum number of files to summarize (0 for all)
        progress_callback: Optional callback for progress updates

    Returns:
        Tuple of (success_flag, list_of_summary_files)
    """
    # Try multiple ways to find the project root
    possible_roots = [
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        os.getcwd(),
    ]

    # Try to find a valid data directory
    content_dir = None
    summary_dir = None

    for root in possible_roots:
        data_dir = os.path.join(root, "data")
        test_content_dir = os.path.join(data_dir, date_dir, "content")
        test_summary_dir = os.path.join(data_dir, date_dir, "summaries_anthropic")

        logger.info(f"Checking for content in: {test_content_dir}")
        if os.path.exists(data_dir):
            content_dir = test_content_dir
            summary_dir = test_summary_dir

            if os.path.exists(test_content_dir):
                logger.info(f"Found content directory at: {test_content_dir}")
                break

    if content_dir is None:
        logger.error("Could not find valid data directory in any location")
        return (False, [])

    if not os.path.exists(content_dir):
        logger.error(f"Content directory not found: {content_dir}")
        return (False, [])

    # Create summaries_anthropic directory if it doesn't exist
    os.makedirs(summary_dir, exist_ok=True)

    # Get model configuration
    config = get_model_config()

    # Use provided model or get default from config
    if model is None:
        model = config.get_anthropic_model(premium=False)

    # Summarize files
    logger.info(f"Summarizing content files using Anthropic {model}")
    try:
        # Import the ArticleSummarizer class directly to use Anthropic
        from pathlib import Path

        from scraper.utils.summarizer import ArticleSummarizer

        # Get all markdown files in the directory
        content_path = Path(content_dir)
        md_files = list(content_path.glob("*.md"))

        # Limit number of files if specified
        if max_files > 0 and len(md_files) > max_files:
            md_files = md_files[:max_files]

        logger.info(f"Found {len(md_files)} markdown files to summarize with Anthropic")

        # Summarize each file
        summary_files = []
        for i, md_file in enumerate(md_files):
            if progress_callback:
                progress_callback(i, len(md_files), md_file.name)

            try:
                # Read the file
                with open(str(md_file), "r", encoding="utf-8") as f:
                    content = f.read()

                # Extract YAML frontmatter
                import yaml

                if content.startswith("---"):
                    _, frontmatter, content = content.split("---", 2)
                    metadata = yaml.safe_load(frontmatter) or {}
                else:
                    metadata = {}

                # Initialize Anthropic summarizer
                summarizer = ArticleSummarizer(mode="quality", model_name=model, use_anthropic=True, anthropic_api_key=api_key)  # Always use quality mode for Anthropic

                # Generate summary
                title = metadata.get("title")
                summary = summarizer.summarize(content, title)
                if summary:
                    # Save summary
                    saved_file = summarizer.save_summary(summary, metadata, summary_dir)
                    if saved_file:
                        summary_files.append(saved_file)

                # Add a small delay to avoid rate limits
                if i < len(md_files) - 1:
                    import time

                    time.sleep(0.5)

            except Exception as e:
                logger.error(f"Failed to summarize {md_file} with Anthropic: {str(e)}")

        if summary_files:
            logger.info(f"Successfully created {len(summary_files)} Anthropic summaries")
            return (True, summary_files)
        else:
            logger.error("No summary files were generated with Anthropic")
            return (False, [])

    except Exception as e:
        logger.error(f"Error during Anthropic summarization: {str(e)}")
        return (False, [])
