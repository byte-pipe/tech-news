"""
Common constants used across the scraper package.

This module centralizes frequently used constants to promote DRY principles.
"""

# User agents
DEFAULT_USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

# Timeout values
DEFAULT_REQUEST_TIMEOUT = 30  # seconds
SUMMARIZER_TIMEOUT = 300.0  # seconds
ENHANCED_SUMMARIZER_TIMEOUT = 600.0  # seconds

# Retry values
DEFAULT_MAX_RETRIES = 3
SUMMARIZER_MAX_RETRIES = 5
ENHANCED_SUMMARIZER_MAX_RETRIES = 3

# Circuit breaker defaults
CIRCUIT_BREAKER_FAILURE_THRESHOLD = 5
CIRCUIT_BREAKER_RECOVERY_TIMEOUT = 60  # seconds
CIRCUIT_BREAKER_EXPECTED_EXCEPTION = Exception

# File extensions
MARKDOWN_EXTENSION = ".md"
JSON_EXTENSION = ".json"
CSV_EXTENSION = ".csv"

# Date formats
DATE_FOLDER_FORMAT = "%Y-%m-%d"
TIMESTAMP_FORMAT = "%Y%m%d-%H%M%S"
ISO_FORMAT = "%Y-%m-%dT%H:%M:%S"

# Logging format
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# Magic numbers
MAX_FILENAME_LENGTH = 50
MAX_DESCRIPTION_LENGTH = 150
GITHUB_STARS_MULTIPLIER = 1000  # for converting 'k' notation
