"""
Core scraper execution logic separated from main.py.
"""

import logging
import time
from datetime import datetime

from scraper.core.config import get_config
from scraper.core.data_organizer import DataOrganizer
from scraper.utils.content_fetcher import ContentFetcher
from scraper.utils.link_tracker import get_link_tracker
from scraper.utils.structured_logger import StructuredLogger, get_metrics_collector
from scraper.utils.url_registry import get_url_registry

logger = logging.getLogger(__name__)
structured_logger = StructuredLogger(__name__)


def run_scraper(scraper_class, output_format, dry_run=False, fetch_content=False, test_mode=False, test_output_dir=None, critical_failures=None):
    """Run a single scraper with proper error handling and logging.

    Args:
        scraper_class: The scraper class to instantiate and run
        output_format: Format to save the data in - one of 'markdown', 'json', or 'csv'
        dry_run: If True, don't save any files (preview mode)
        fetch_content: If True, fetch full article content
        test_mode: If True, run in test mode with separate output directory
        test_output_dir: Directory to use for test output when test_mode is True
        critical_failures: Dictionary to track critical failures (shared across functions)

    Returns:
        bool: True if the scraper ran successfully, False otherwise
    """
    if critical_failures is None:
        critical_failures = {}

    scraper_name = scraper_class.__name__
    start_time = time.time()
    metrics_collector = get_metrics_collector()
    items_count = 0
    error_msg = None

    try:
        # Initialize the scraper with test mode if specified
        scraper = scraper_class(test_mode=test_mode, test_output_dir=test_output_dir)
        structured_logger.add_context(scraper=scraper_name, dry_run=dry_run)

        with structured_logger.timer(f"scraper_{scraper_name}", log_start=False):
            if dry_run:
                logger.info(f"Starting scrape for {scraper.__class__.__name__} in DRY RUN mode")

                # For dry run, we need to be careful to avoid saving files
                # Get the data from the url but don't save it
                html = scraper._get_page(scraper.url)
                if not html:
                    error_msg = f"Could not fetch page for {scraper.__class__.__name__}"
                    logger.error(error_msg)
                    raise RuntimeError(error_msg)

                items = scraper._parse_html(html, scraper.selector)
                data = scraper._extract_data(items)

                # Just print some stats about what would be scraped
                if data:
                    data = scraper._remove_duplicates(data)
                    items_count = len(data)
                    logger.info(f"DRY RUN: Would save {items_count} items from {scraper.__class__.__name__}")

                    # Print a sample of what would be saved
                    if data:
                        sample = data[0]
                        fields = ", ".join(sample.keys())
                        logger.info(f"DRY RUN: Fields available: {fields}")

                        # Print a sample title
                        if "title" in sample:
                            logger.info(f"DRY RUN: Sample title: {sample['title']}")
                else:
                    logger.warning(f"DRY RUN: No data would be scraped from {scraper.__class__.__name__}")
            else:
                # Normal execution with file saving
                logger.info(f"Starting scrape for {scraper.__class__.__name__} (output format: {output_format})")
                # Try with output_format first, fall back to no args if that fails
                try:
                    results = scraper.scrape(output_format=output_format)
                except TypeError as e:
                    if "output_format" in str(e):
                        # Scraper doesn't accept output_format, call without it
                        results = scraper.scrape()
                        # Save with the requested format
                        if results and not dry_run:
                            scraper._save_data(results, output_format)
                            # Don't set results to None - we need it for content fetching!
                    else:
                        raise
                if results is None:
                    logger.error(f"Scraper {scraper.__class__.__name__} returned None (failure)")
                    raise RuntimeError(f"Scraper {scraper.__class__.__name__} failed")
                items_count = len(results)

                if items_count == 0:
                    logger.warning(f"Scraper {scraper.__class__.__name__} returned 0 items")

                # Track links in CSV
                if results:
                    try:
                        tracker = get_link_tracker()
                        tracker.track_items(results, scraper.site_name)
                    except Exception as e:
                        logger.warning(f"Link tracking failed: {e}")

                # Fetch content if requested
                if fetch_content and results:
                    try:
                        with structured_logger.timer(f"content_fetch_{scraper_name}"):
                            logger.info(f"Fetching content for {len(results)} items from {scraper.__class__.__name__}")
                            enhanced_results = fetch_content_for_results(scraper.site_name, results, max_articles=5, force=False)

                            # Check if content was fetched successfully
                            fetched_count = sum(1 for r in enhanced_results if r.get("local_path"))
                            if fetched_count == 0 and len(results) > 0:
                                logger.warning(f"⚠️  Could not fetch content for {scraper.__class__.__name__} (this is non-critical)")
                                # Don't track as critical failure - content fetching is optional
                            else:
                                logger.info(f"✅ Fetched content for {fetched_count}/{len(results)} items from {scraper.__class__.__name__}")
                                structured_logger.log_metric("content_fetched", fetched_count, scraper=scraper_name)
                    except Exception as e:
                        logger.warning(f"⚠️  Content fetching failed for {scraper.__class__.__name__}: {str(e)} (continuing anyway)")
                        # Content fetching is optional, so don't fail the scraper

        # Record successful completion
        duration = time.time() - start_time
        metrics_collector.record_scraper_run(scraper_name, success=True, items_count=items_count, duration=duration)
        structured_logger.log_scraper_result(scraper_name, success=True, items_count=items_count, duration=duration)

        logger.info(f"Completed scrape for {scraper.__class__.__name__}")
        return True

    except Exception as e:
        error_msg = str(e)
        logger.error(f"Error running {scraper_class.__name__}: {error_msg}")

        # Record failure
        duration = time.time() - start_time
        metrics_collector.record_scraper_run(scraper_name, success=False, duration=duration, error=error_msg)
        structured_logger.log_scraper_result(scraper_name, success=False, duration=duration, error=error_msg)

        return False


def fetch_content_for_results(site_name, results, max_articles=5, force=False):
    """Fetch and store the full content for scraped results.

    Args:
        site_name: Name of the site the results are from
        results: List of dictionaries containing scraped data
        max_articles: Maximum number of articles to fetch content for
        force: If True, force refetch even if content is already cached

    Returns:
        List of dictionaries with enhanced content information
    """
    logger.info("Using organized data structure for content fetching")

    # Use centralized configuration for consistent paths
    config = get_config()
    logger.info(f"Using project root for content fetching: {config.project_root}")
    content_fetcher = ContentFetcher(project_root=str(config.project_root))

    # Use DataOrganizer to ensure proper directory structure
    data_organizer = DataOrganizer(config)
    now = datetime.now()
    date_folder = now.strftime("%Y-%m-%d")

    # Create content directory for content fetching
    try:
        content_dir = data_organizer.ensure_directory(date_folder, "content")
        logger.info(f"Using organized content directory: {content_dir}")
    except Exception as e:
        logger.error(f"Failed to create organized directory structure: {str(e)}")
        # Use ScraperConfig for fallback directory creation
        try:
            fallback_content_dir = config.get_fallback_directory("content", date_folder)
            logger.warning(f"Using fallback content directory: {fallback_content_dir}")
        except Exception as fallback_error:
            logger.error(f"Critical: Failed to create even fallback directory structure: {str(fallback_error)}")
            raise RuntimeError(f"Cannot create required directories: {str(fallback_error)}")

    # Sort results by some measure of importance (if available)
    # GitHub: stars, HN: points, etc.
    if results and isinstance(results[0], dict):
        if "stars" in results[0]:
            results.sort(key=lambda x: int(str(x.get("stars", "0")).replace("k", "000").replace(".", "")), reverse=True)
        elif "score" in results[0] or "points" in results[0]:
            key = "score" if "score" in results[0] else "points"
            # Handle both string and integer values for API scrapers
            results.sort(key=lambda x: int(str(x.get(key, "0")).replace("k", "000").replace(".", "")) if isinstance(x.get(key), (str, int)) else 0, reverse=True)
        elif "today_stars" in results[0]:
            results.sort(key=lambda x: int(str(x.get("today_stars", "0")).replace("k", "000").replace(".", "")), reverse=True)

    # Select top N *new* URLs (skip already-processed ones)
    registry = get_url_registry(str(config.project_root))
    results_to_fetch = []
    for result in results:
        if max_articles > 0 and len(results_to_fetch) >= max_articles:
            break
        url = result.get("url", "")
        if not url:
            continue
        if not force and registry.is_processed(url):
            registry.record_reappearance(url)
            continue
        results_to_fetch.append(result)

    if not results_to_fetch and results:
        logger.info(f"All {len(results)} URLs from {site_name} already processed, no new content to fetch")

    fetched_count = 0
    enhanced_results = []
    metrics_collector = get_metrics_collector()

    for i, result in enumerate(results_to_fetch):
        if "url" not in result or not result["url"]:
            logger.warning(f"Skipping content fetch for item {i+1} from {site_name} - no URL found")
            enhanced_results.append(result)
            continue

        try:
            with structured_logger.timer("fetch_single_content", log_start=False):
                logger.info(f"Fetching content for item {i+1}/{len(results_to_fetch)} from {site_name}: {result.get('title', result['url'])}")

                fetch_start = time.time()
                enhanced_result = content_fetcher.fetch_content(result["url"], site_name, result, force=force)
                fetch_duration = time.time() - fetch_start

                # Record HTTP request metrics
                success = "local_path" in enhanced_result
                metrics_collector.record_http_request(status_code=200 if success else None, success=success, duration=fetch_duration)

                # Record operation duration
                metrics_collector.record_operation_duration("content_fetch", fetch_duration)

                # Log where the content was saved
                if "local_path" in enhanced_result:
                    logger.info(f"Content saved to: {enhanced_result['local_path']}")
                    structured_logger.log_http_request(method="GET", url=result["url"], status_code=200, duration=fetch_duration)

                enhanced_results.append(enhanced_result)
                fetched_count += 1

        except Exception as e:
            logger.error(f"Error fetching content for {result.get('title', result['url'])}: {str(e)}")
            enhanced_results.append(result)

            # Record failed HTTP request
            metrics_collector.record_http_request(success=False)
            structured_logger.log_http_request(method="GET", url=result.get("url", "unknown"), error=str(e))

    logger.info(f"Fetched content for {fetched_count}/{len(results_to_fetch)} items from {site_name}")
    return enhanced_results


def run_scrapers_sequential(scrapers, output_format, dry_run=False, fetch_content=False, max_articles=5):
    """Run multiple scrapers sequentially (replaced parallel execution for stability)."""
    critical_failures = {}
    get_metrics_collector()

    with structured_logger.timer("sequential_scraper_execution"):
        success_count = 0
        failed_scrapers = []

        for scraper_class in scrapers:
            scraper_name = scraper_class.__name__
            logger.info(f"Running scraper: {scraper_name}")

            try:
                # Run the scraper
                success = run_scraper(scraper_class, output_format, dry_run, fetch_content, test_mode=False, test_output_dir=None, critical_failures=critical_failures)

                if success:
                    success_count += 1
                    logger.info(f"✅ {scraper_name} completed successfully")
                else:
                    failed_scrapers.append(scraper_name)
                    logger.error(f"❌ {scraper_name} failed")

            except Exception as e:
                logger.error(f"Scraper {scraper_name} failed with exception: {e}")
                failed_scrapers.append(scraper_name)
                critical_failures[f"execution_error_{scraper_name}"] = str(e)

        # Log execution summary
        structured_logger.log_metric("sequential_execution_complete", success_count, total_scrapers=len(scrapers), failed_scrapers=len(failed_scrapers), failure_names=",".join(failed_scrapers) if failed_scrapers else None)

        logger.info(f"Completed {success_count}/{len(scrapers)} scrapers successfully")

    return success_count, critical_failures


# Keep the old name as an alias for backward compatibility
run_scrapers_parallel = run_scrapers_sequential
