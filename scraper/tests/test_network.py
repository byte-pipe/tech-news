"""Tests for network utility functions."""

import unittest
from unittest.mock import MagicMock, patch

import requests

from scraper.utils.network import create_session, fetch_json_with_retry, fetch_with_retry


class TestCreateSession(unittest.TestCase):
    def test_returns_session(self):
        session = create_session()
        assert isinstance(session, requests.Session)

    def test_has_http_adapter(self):
        session = create_session()
        assert "http://" in session.adapters
        assert "https://" in session.adapters

    def test_custom_retries(self):
        session = create_session(retries=5)
        assert isinstance(session, requests.Session)

    def test_custom_backoff(self):
        session = create_session(backoff_factor=1.0)
        assert isinstance(session, requests.Session)


class TestFetchWithRetry(unittest.TestCase):
    def _make_response(self, text="content", status_code=200):
        resp = MagicMock()
        resp.text = text
        resp.status_code = status_code
        resp.raise_for_status = MagicMock()
        return resp

    @patch("scraper.utils.network.create_session")
    def test_successful_fetch(self, mock_create_session):
        mock_session = MagicMock()
        mock_session.get.return_value = self._make_response("hello")
        mock_create_session.return_value = mock_session

        result = fetch_with_retry("https://example.com")
        assert result == "hello"

    @patch("scraper.utils.network.create_session")
    @patch("scraper.utils.network.time.sleep")
    def test_retries_on_failure(self, mock_sleep, mock_create_session):
        mock_session = MagicMock()
        mock_session.get.side_effect = [
            requests.RequestException("fail"),
            self._make_response("success"),
        ]
        mock_create_session.return_value = mock_session

        result = fetch_with_retry("https://example.com", retries=2, delay=0)
        assert result == "success"

    @patch("scraper.utils.network.create_session")
    @patch("scraper.utils.network.time.sleep")
    def test_returns_none_after_all_retries_fail(self, mock_sleep, mock_create_session):
        mock_session = MagicMock()
        mock_session.get.side_effect = requests.RequestException("always fails")
        mock_create_session.return_value = mock_session

        result = fetch_with_retry("https://example.com", retries=2, delay=0)
        assert result is None

    @patch("scraper.utils.network.create_session")
    def test_passes_headers(self, mock_create_session):
        mock_session = MagicMock()
        mock_session.get.return_value = self._make_response()
        mock_create_session.return_value = mock_session

        fetch_with_retry("https://example.com", headers={"User-Agent": "test"})
        mock_session.headers.update.assert_called_once_with({"User-Agent": "test"})

    @patch("scraper.utils.network.create_session")
    def test_no_headers_no_update(self, mock_create_session):
        mock_session = MagicMock()
        mock_session.get.return_value = self._make_response()
        mock_create_session.return_value = mock_session

        fetch_with_retry("https://example.com", headers=None)
        mock_session.headers.update.assert_not_called()


class TestFetchJsonWithRetry(unittest.TestCase):
    def _make_response(self, data=None, status_code=200):
        resp = MagicMock()
        resp.json.return_value = data or {"key": "value"}
        resp.status_code = status_code
        resp.raise_for_status = MagicMock()
        return resp

    @patch("scraper.utils.network.create_session")
    def test_successful_fetch(self, mock_create_session):
        mock_session = MagicMock()
        mock_session.get.return_value = self._make_response({"result": 42})
        mock_create_session.return_value = mock_session

        result = fetch_json_with_retry("https://api.example.com/data")
        assert result == {"result": 42}

    @patch("scraper.utils.network.create_session")
    def test_passes_headers(self, mock_create_session):
        mock_session = MagicMock()
        mock_session.get.return_value = self._make_response({"ok": True})
        mock_create_session.return_value = mock_session

        fetch_json_with_retry("https://api.example.com/data", headers={"Authorization": "Bearer token"})
        mock_session.headers.update.assert_called_once_with({"Authorization": "Bearer token"})

    @patch("scraper.utils.network.create_session")
    @patch("scraper.utils.network.time.sleep")
    def test_returns_none_on_all_failures(self, mock_sleep, mock_create_session):
        mock_session = MagicMock()
        mock_session.get.side_effect = requests.RequestException("fail")
        mock_create_session.return_value = mock_session

        result = fetch_json_with_retry("https://api.example.com/data", retries=1, delay=0)
        assert result is None

    @patch("scraper.utils.network.create_session")
    @patch("scraper.utils.network.time.sleep")
    def test_retries_on_value_error(self, mock_sleep, mock_create_session):
        mock_session = MagicMock()
        bad_resp = MagicMock()
        bad_resp.raise_for_status = MagicMock()
        bad_resp.json.side_effect = ValueError("not json")
        good_resp = self._make_response({"ok": True})

        mock_session.get.side_effect = [bad_resp, good_resp]
        mock_create_session.return_value = mock_session

        result = fetch_json_with_retry("https://api.example.com", retries=2, delay=0)
        assert result == {"ok": True}


if __name__ == "__main__":
    unittest.main()
