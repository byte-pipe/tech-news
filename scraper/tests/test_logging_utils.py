"""Tests for logging utility functions."""

import logging
import unittest

from scraper.utils.logging_utils import configure_scraper_logging, get_logger, setup_logging


class TestSetupLogging(unittest.TestCase):
    def test_returns_logger(self):
        logger = setup_logging()
        assert isinstance(logger, logging.Logger)

    def test_with_logger_name(self):
        logger = setup_logging(logger_name="test_logger")
        assert logger.name == "test_logger"

    def test_without_logger_name_returns_root(self):
        logger = setup_logging()
        assert logger is logging.getLogger()

    def test_debug_level(self):
        logger = setup_logging(level=logging.DEBUG, logger_name="test_debug_level")
        assert logger.name == "test_debug_level"

    def test_info_level(self):
        logger = setup_logging(level=logging.INFO, logger_name="test_info_level")
        assert logger.name == "test_info_level"


class TestGetLogger(unittest.TestCase):
    def test_returns_named_logger(self):
        logger = get_logger("my_module")
        assert logger.name == "my_module"

    def test_same_name_same_instance(self):
        logger1 = get_logger("shared")
        logger2 = get_logger("shared")
        assert logger1 is logger2

    def test_different_names_different_loggers(self):
        logger1 = get_logger("module_a")
        logger2 = get_logger("module_b")
        assert logger1 is not logger2

    def test_returns_logger_instance(self):
        logger = get_logger("test")
        assert isinstance(logger, logging.Logger)


class TestConfigureScraperLogging(unittest.TestCase):
    def test_returns_logger(self):
        logger = configure_scraper_logging()
        assert isinstance(logger, logging.Logger)

    def test_idempotent(self):
        logger1 = configure_scraper_logging()
        logger2 = configure_scraper_logging()
        assert logger1 is logger2


if __name__ == "__main__":
    unittest.main()
