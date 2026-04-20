"""Tests for datetime utility functions."""

import unittest
from datetime import datetime

from scraper.utils.datetime_utils import (
    format_for_filename,
    get_current_datetime,
    get_date_and_timestamp,
    get_date_folder,
    get_iso_timestamp,
    get_timestamp,
    parse_date_folder,
)


class TestGetCurrentDatetime(unittest.TestCase):
    def test_returns_datetime(self):
        result = get_current_datetime()
        assert isinstance(result, datetime)

    def test_is_recent(self):
        now = datetime.now()
        result = get_current_datetime()
        delta = abs((result - now).total_seconds())
        assert delta < 5


class TestGetDateAndTimestamp(unittest.TestCase):
    def test_returns_tuple(self):
        result = get_date_and_timestamp()
        assert isinstance(result, tuple)
        assert len(result) == 2

    def test_date_format(self):
        date_folder, _ = get_date_and_timestamp()
        datetime.strptime(date_folder, "%Y-%m-%d")  # should not raise

    def test_timestamp_format(self):
        _, timestamp = get_date_and_timestamp()
        assert len(timestamp) > 0


class TestGetDateFolder(unittest.TestCase):
    def test_current_date(self):
        result = get_date_folder()
        datetime.strptime(result, "%Y-%m-%d")  # should not raise

    def test_specific_date(self):
        dt = datetime(2026, 4, 20)
        result = get_date_folder(dt)
        assert result == "2026-04-20"

    def test_specific_date_leading_zeros(self):
        dt = datetime(2026, 1, 5)
        result = get_date_folder(dt)
        assert result == "2026-01-05"


class TestGetTimestamp(unittest.TestCase):
    def test_returns_string(self):
        result = get_timestamp()
        assert isinstance(result, str)

    def test_specific_datetime(self):
        dt = datetime(2026, 4, 20, 12, 30, 45)
        result = get_timestamp(dt)
        assert "20260420" in result

    def test_no_arg_uses_now(self):
        result = get_timestamp()
        assert len(result) > 0


class TestGetIsoTimestamp(unittest.TestCase):
    def test_returns_iso_format(self):
        dt = datetime(2026, 4, 20, 12, 0, 0)
        result = get_iso_timestamp(dt)
        assert result == "2026-04-20T12:00:00"

    def test_no_arg_uses_now(self):
        result = get_iso_timestamp()
        assert "T" in result


class TestParseDateFolder(unittest.TestCase):
    def test_valid_date(self):
        result = parse_date_folder("2026-04-20")
        assert result == datetime(2026, 4, 20)

    def test_invalid_date_raises(self):
        with self.assertRaises(ValueError):
            parse_date_folder("not-a-date")

    def test_wrong_format_raises(self):
        with self.assertRaises(ValueError):
            parse_date_folder("20260420")


class TestFormatForFilename(unittest.TestCase):
    def test_returns_string(self):
        result = format_for_filename()
        assert isinstance(result, str)

    def test_specific_datetime(self):
        dt = datetime(2026, 4, 20, 10, 5, 3)
        result = format_for_filename(dt)
        assert "20260420" in result


if __name__ == "__main__":
    unittest.main()
