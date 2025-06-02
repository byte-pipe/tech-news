"""
AI processing functionality separated from main.py.
"""

import logging
import os

from scraper.utils.summarizer import batch_summarize_directory

logger = logging.getLogger(__name__)


def summarize_content(date_dir, model_name="tinyllama:1.1b", max_files=0, fallback_model="smollm:135m"):
    """Summarize fetched article content using LLM.

    Args:
        date_dir: Date directory where content files are stored (YYYY-MM-DD format)
        model_name: Name of the LLM model to use (default: smollm:135m)
        max_files: Maximum number of files to summarize (0 for all)
        fallback_model: Model to use if primary model is unavailable (default: tinyllama:1.1b)

    Returns:
        Tuple of (success_flag, list_of_summary_files)
        If success_flag is False, the operation had critical errors
    """
    # Try multiple ways to find the project root to be compatible with different environments
    possible_roots = [
        # Same as ContentFetcher (works in local dev)
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))),
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

        # Look for content files directly in the date directory as fallback
        date_dir_path = os.path.dirname(content_dir)
        if os.path.exists(date_dir_path):
            logger.info(f"Checking for content files directly in date directory: {date_dir_path}")
            md_files = [f for f in os.listdir(date_dir_path) if f.endswith(".md")]
            if md_files:
                logger.info(f"Found {len(md_files)} markdown files in date directory")
                # We found some files, but they're not in the content directory
                # Copy them to the content directory
                try:
                    for file in md_files:
                        src = os.path.join(date_dir_path, file)
                        dst = os.path.join(content_dir, file)
                        import shutil

                        shutil.copy2(src, dst)
                    logger.info(f"Copied {len(md_files)} files to content directory")
                except Exception as e:
                    logger.error(f"Failed to copy files to content directory: {str(e)}")

    # Create summaries directory if it doesn't exist
    os.makedirs(summary_dir, exist_ok=True)

    # Summarize files
    logger.info(f"Summarizing content files using {model_name}")
    try:
        summary_files = batch_summarize_directory(content_dir, summary_dir, model_name=model_name, max_files=max_files)

        # If summarization fails, check if it was due to missing model and try fallback
        if not summary_files:
            # Look for specific error message in logs
            logger.warning(f"Primary model '{model_name}' summarization failed or produced no results")

            if fallback_model and fallback_model != model_name:
                logger.info(f"Attempting summarization with fallback model: {fallback_model}")
                try:
                    # Try again with fallback model
                    summary_files = batch_summarize_directory(content_dir, summary_dir, model_name=fallback_model, max_files=max_files)

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
                summary_files = batch_summarize_directory(content_dir, summary_dir, model_name=fallback_model, max_files=max_files)

                if summary_files:
                    logger.info(f"Successfully created {len(summary_files)} summary files using fallback model {fallback_model}")
                    return (True, summary_files)
                else:
                    logger.error("Fallback summarization completed but no summary files were generated")
            except Exception as e2:
                logger.error(f"Error during fallback summarization with {fallback_model}: {str(e2)}")

        return (False, [])


def summarize_with_local_model(date_dir=None, model_name="gemma2:27b", max_files=0, only_latest=True):
    """Summarize content using a powerful local model with enhanced quality.

    Args:
        date_dir: Date directory to process (None for today)
        model_name: Name of the powerful local model to use
        max_files: Maximum number of files to summarize (0 for all)
        only_latest: If True, only process today's content

    Returns:
        Tuple of (success_flag, list_of_summary_files)
    """
    # Determine date directory
    if date_dir is None:
        from datetime import datetime

        date_dir = datetime.now().strftime("%Y-%m-%d")

    logger.info(f"Running local model summarization with {model_name}")

    # Find project root and content directory
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    data_dir = os.path.join(project_root, "data")
    content_dir = os.path.join(data_dir, date_dir, "content")

    # Create local summaries directory (separate from CI summaries)
    local_summary_dir = os.path.join(data_dir, date_dir, "summaries_local")
    os.makedirs(local_summary_dir, exist_ok=True)

    logger.info(f"Content directory: {content_dir}")
    logger.info(f"Local summary directory: {local_summary_dir}")

    if not os.path.exists(content_dir):
        logger.error(f"Content directory not found: {content_dir}")
        return (False, [])

    # Check for content files
    content_files = [f for f in os.listdir(content_dir) if f.endswith(".md")]
    if not content_files:
        logger.error(f"No content files found in {content_dir}")
        return (False, [])

    logger.info(f"Found {len(content_files)} content files to process")

    # Summarize files with enhanced settings for local model
    try:
        # Import the batch summarization function
        from scraper.utils.summarizer import batch_summarize_local_model

        summary_files = batch_summarize_local_model(content_dir=content_dir, output_dir=local_summary_dir, model_name=model_name, max_files=max_files)

        if summary_files:
            logger.info(f"✅ Successfully created {len(summary_files)} local model summaries")
            return (True, summary_files)
        else:
            logger.error("No summary files were generated with local model")
            return (False, [])

    except Exception as e:
        logger.error(f"Error during local model summarization: {str(e)}")
        return (False, [])
