"""
Logging utilities for the scraper package.

This module provides centralized logging configuration and utilities.
"""

import logging
from typing import Optional

from scraper.constants import LOG_FORMAT


def setup_logging(level: int = logging.INFO, format_str: str = LOG_FORMAT, logger_name: Optional[str] = None) -> logging.Logger:
    """Set up logging configuration and return a configured logger.

    Args:
        level: Logging level (default: INFO)
        format_str: Log format string (default: from constants)
        logger_name: Logger name (default: None for root logger)

    Returns:
        Configured logger instance
    """
    logging.basicConfig(level=level, format=format_str)

    if logger_name:
        return logging.getLogger(logger_name)
    return logging.getLogger()


def get_logger(name: str) -> logging.Logger:
    """Get a logger with the given name.

    Args:
        name: Logger name (typically __name__)

    Returns:
        Logger instance
    """
    return logging.getLogger(name)


def configure_scraper_logging() -> logging.Logger:
    """Configure logging for scraper execution with standard settings.

    Returns:
        Root logger instance
    """
    return setup_logging(level=logging.INFO, format_str=LOG_FORMAT)
