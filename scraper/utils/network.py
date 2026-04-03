"""
Network utilities for the scraper with retry functionality.
"""

import logging
import time

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

logger = logging.getLogger(__name__)


def create_session(retries=3, backoff_factor=0.3, status_forcelist=(500, 502, 503, 504)):
    """
    Create a requests session with retry functionality.

    Args:
        retries (int): Number of retries to attempt
        backoff_factor (float): Backoff factor between retries
        status_forcelist (tuple): HTTP status codes to retry on

    Returns:
        requests.Session: Configured session object
    """
    session = requests.Session()

    # Configure retry strategy
    retry_strategy = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )

    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    return session


def fetch_with_retry(url, headers=None, timeout=30, retries=3, delay=1):
    """
    Fetch a URL with retry functionality.

    Args:
        url (str): URL to fetch
        headers (dict, optional): Request headers
        timeout (int): Request timeout in seconds
        retries (int): Number of manual retries (in addition to session retries)
        delay (int): Delay between retries in seconds

    Returns:
        str: Response text if successful, None otherwise
    """
    session = create_session(retries=retries)

    if headers:
        session.headers.update(headers)

    for attempt in range(retries + 1):
        try:
            logger.info(f"Fetching URL: {url} (Attempt {attempt + 1}/{retries + 1})")
            response = session.get(url, timeout=timeout)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            if attempt < retries:
                error_type = type(e).__name__
                logger.warning(f"Request failed: {error_type}: {str(e)}, retrying in {delay} seconds...")
                time.sleep(delay)
                # Increase delay for next retry (exponential backoff)
                delay *= 2
            else:
                logger.error(f"Failed to fetch {url} after {retries + 1} attempts: {str(e)}")
                return None


def fetch_json_with_retry(url, headers=None, timeout=30, retries=3, delay=1):
    """
    Fetch a JSON URL with retry functionality.

    Args:
        url (str): URL to fetch
        headers (dict, optional): Request headers
        timeout (int): Request timeout in seconds
        retries (int): Number of retries
        delay (int): Delay between retries in seconds

    Returns:
        dict: JSON response if successful, None otherwise
    """
    session = create_session(retries=retries)

    if headers:
        session.headers.update(headers)

    for attempt in range(retries + 1):
        try:
            logger.info(f"Fetching JSON from URL: {url} (Attempt {attempt + 1}/{retries + 1})")
            response = session.get(url, timeout=timeout)
            response.raise_for_status()
            return response.json()
        except (requests.RequestException, ValueError) as e:
            if attempt < retries:
                error_type = type(e).__name__
                logger.warning(f"Request failed: {error_type}: {str(e)}, retrying in {delay} seconds...")
                time.sleep(delay)
                # Increase delay for next retry (exponential backoff)
                delay *= 2
            else:
                logger.error(f"Failed to fetch JSON from {url} after {retries + 1} attempts: {str(e)}")
                return None
