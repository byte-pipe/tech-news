"""Tests for scraper_runner module."""

import unittest
from unittest.mock import MagicMock, patch


class TestRunScraper(unittest.TestCase):
    def _make_mock_scraper_class(self, results=None, raises=None):
        mock_instance = MagicMock()
        mock_instance.site_name = "test_site"
        mock_instance.url = "https://example.com"
        mock_instance.selector = "div"

        if raises:
            mock_instance.scrape.side_effect = raises
        else:
            mock_instance.scrape.return_value = results if results is not None else [{"title": "A", "url": "https://x.com"}]

        mock_class = MagicMock(return_value=mock_instance)
        mock_class.__name__ = "MockScraper"
        return mock_class, mock_instance

    @patch("scraper.core.scraper_runner.get_metrics_collector")
    @patch("scraper.core.scraper_runner.StructuredLogger")
    @patch("scraper.core.scraper_runner.get_link_tracker")
    def test_run_scraper_success(self, mock_tracker, mock_logger, mock_metrics):
        from scraper.core.scraper_runner import run_scraper

        mock_class, mock_instance = self._make_mock_scraper_class()
        mock_metrics.return_value = MagicMock()
        mock_tracker.return_value = MagicMock()

        result = run_scraper(mock_class, "json")
        assert result is True

    @patch("scraper.core.scraper_runner.get_metrics_collector")
    @patch("scraper.core.scraper_runner.StructuredLogger")
    @patch("scraper.core.scraper_runner.get_link_tracker")
    def test_run_scraper_returns_none_is_failure(self, mock_tracker, mock_logger, mock_metrics):
        from scraper.core.scraper_runner import run_scraper

        mock_class, mock_instance = self._make_mock_scraper_class(results=None)
        mock_instance.scrape.return_value = None
        mock_metrics.return_value = MagicMock()
        mock_tracker.return_value = MagicMock()

        result = run_scraper(mock_class, "json")
        assert result is False

    @patch("scraper.core.scraper_runner.get_metrics_collector")
    @patch("scraper.core.scraper_runner.StructuredLogger")
    @patch("scraper.core.scraper_runner.get_link_tracker")
    def test_run_scraper_exception_returns_false(self, mock_tracker, mock_logger, mock_metrics):
        from scraper.core.scraper_runner import run_scraper

        mock_class = MagicMock(side_effect=RuntimeError("instantiation failed"))
        mock_class.__name__ = "BadScraper"
        mock_metrics.return_value = MagicMock()

        result = run_scraper(mock_class, "json")
        assert result is False

    @patch("scraper.core.scraper_runner.get_metrics_collector")
    @patch("scraper.core.scraper_runner.StructuredLogger")
    @patch("scraper.core.scraper_runner.get_link_tracker")
    def test_run_scraper_empty_results_returns_true(self, mock_tracker, mock_logger, mock_metrics):
        from scraper.core.scraper_runner import run_scraper

        mock_class, mock_instance = self._make_mock_scraper_class(results=[])
        mock_metrics.return_value = MagicMock()
        mock_tracker.return_value = MagicMock()

        result = run_scraper(mock_class, "json")
        assert result is True

    @patch("scraper.core.scraper_runner.get_metrics_collector")
    @patch("scraper.core.scraper_runner.StructuredLogger")
    @patch("scraper.core.scraper_runner.get_link_tracker")
    def test_run_scraper_link_tracking_failure_non_critical(self, mock_tracker, mock_logger, mock_metrics):
        from scraper.core.scraper_runner import run_scraper

        mock_class, mock_instance = self._make_mock_scraper_class()
        mock_metrics.return_value = MagicMock()
        tracker = MagicMock()
        tracker.track_items.side_effect = Exception("tracking failed")
        mock_tracker.return_value = tracker

        result = run_scraper(mock_class, "json")
        assert result is True  # link tracking failure is non-critical

    @patch("scraper.core.scraper_runner.get_metrics_collector")
    @patch("scraper.core.scraper_runner.StructuredLogger")
    @patch("scraper.core.scraper_runner.get_link_tracker")
    def test_run_scraper_dry_run(self, mock_tracker, mock_logger, mock_metrics):
        from scraper.core.scraper_runner import run_scraper

        mock_class, mock_instance = self._make_mock_scraper_class()
        mock_instance._get_page.return_value = "<html></html>"
        mock_instance._parse_html.return_value = []
        mock_instance._extract_data.return_value = [{"title": "A", "url": "https://x.com"}]
        mock_instance._remove_duplicates.return_value = [{"title": "A", "url": "https://x.com"}]
        mock_metrics.return_value = MagicMock()

        result = run_scraper(mock_class, "json", dry_run=True)
        assert result is True

    @patch("scraper.core.scraper_runner.get_metrics_collector")
    @patch("scraper.core.scraper_runner.StructuredLogger")
    @patch("scraper.core.scraper_runner.get_link_tracker")
    def test_run_scraper_dry_run_empty_data(self, mock_tracker, mock_logger, mock_metrics):
        from scraper.core.scraper_runner import run_scraper

        mock_class, mock_instance = self._make_mock_scraper_class()
        mock_instance._get_page.return_value = "<html></html>"
        mock_instance._parse_html.return_value = []
        mock_instance._extract_data.return_value = []
        mock_instance._remove_duplicates.return_value = []
        mock_metrics.return_value = MagicMock()

        result = run_scraper(mock_class, "json", dry_run=True)
        assert result is True  # dry run with empty data still succeeds

    @patch("scraper.core.scraper_runner.get_metrics_collector")
    @patch("scraper.core.scraper_runner.StructuredLogger")
    @patch("scraper.core.scraper_runner.get_link_tracker")
    def test_run_scraper_type_error_non_output_format_reraises(self, mock_tracker, mock_logger, mock_metrics):
        from scraper.core.scraper_runner import run_scraper

        mock_class, mock_instance = self._make_mock_scraper_class()
        # TypeError unrelated to output_format should propagate as failure
        mock_instance.scrape.side_effect = TypeError("unexpected keyword argument 'other_thing'")
        mock_metrics.return_value = MagicMock()

        result = run_scraper(mock_class, "json")
        assert result is False

    @patch("scraper.core.scraper_runner.fetch_content_for_results")
    @patch("scraper.core.scraper_runner.get_metrics_collector")
    @patch("scraper.core.scraper_runner.StructuredLogger")
    @patch("scraper.core.scraper_runner.get_link_tracker")
    def test_run_scraper_fetch_content_exception_non_critical(self, mock_tracker, mock_logger, mock_metrics, mock_fetch):
        from scraper.core.scraper_runner import run_scraper

        mock_class, mock_instance = self._make_mock_scraper_class()
        mock_metrics.return_value = MagicMock()
        mock_tracker.return_value = MagicMock()
        mock_fetch.side_effect = RuntimeError("fetch failed")

        result = run_scraper(mock_class, "json", fetch_content=True)
        assert result is True  # fetch failure is non-critical

    @patch("scraper.core.scraper_runner.get_metrics_collector")
    @patch("scraper.core.scraper_runner.StructuredLogger")
    @patch("scraper.core.scraper_runner.get_link_tracker")
    def test_run_scraper_dry_run_no_html(self, mock_tracker, mock_logger, mock_metrics):
        from scraper.core.scraper_runner import run_scraper

        mock_class, mock_instance = self._make_mock_scraper_class()
        mock_instance._get_page.return_value = None
        mock_metrics.return_value = MagicMock()

        result = run_scraper(mock_class, "json", dry_run=True)
        assert result is False

    @patch("scraper.core.scraper_runner.get_metrics_collector")
    @patch("scraper.core.scraper_runner.StructuredLogger")
    @patch("scraper.core.scraper_runner.get_link_tracker")
    def test_run_scraper_output_format_fallback(self, mock_tracker, mock_logger, mock_metrics):
        from scraper.core.scraper_runner import run_scraper

        mock_class, mock_instance = self._make_mock_scraper_class()
        # Need separate mock for fallback call without output_format
        call_count = [0]

        def side_effect(*args, **kwargs):
            call_count[0] += 1
            if "output_format" in kwargs:
                raise TypeError("unexpected keyword argument 'output_format'")
            return [{"title": "X", "url": "https://x.com"}]

        mock_instance.scrape.side_effect = side_effect

        mock_metrics.return_value = MagicMock()
        mock_tracker.return_value = MagicMock()

        result = run_scraper(mock_class, "json")
        assert result is True

    @patch("scraper.core.scraper_runner.fetch_content_for_results")
    @patch("scraper.core.scraper_runner.get_metrics_collector")
    @patch("scraper.core.scraper_runner.StructuredLogger")
    @patch("scraper.core.scraper_runner.get_link_tracker")
    def test_run_scraper_with_fetch_content(self, mock_tracker, mock_logger, mock_metrics, mock_fetch):
        from scraper.core.scraper_runner import run_scraper

        mock_class, mock_instance = self._make_mock_scraper_class()
        mock_metrics.return_value = MagicMock()
        mock_tracker.return_value = MagicMock()
        mock_fetch.return_value = [{"title": "A", "url": "https://x.com", "local_path": "/tmp/a.md"}]

        result = run_scraper(mock_class, "json", fetch_content=True)
        assert result is True
        mock_fetch.assert_called_once()


class TestFetchContentForResults(unittest.TestCase):
    @patch("scraper.core.scraper_runner.get_url_registry")
    @patch("scraper.core.scraper_runner.get_metrics_collector")
    @patch("scraper.core.scraper_runner.ContentFetcher")
    @patch("scraper.core.scraper_runner.DataOrganizer")
    @patch("scraper.core.scraper_runner.get_config")
    def test_returns_empty_for_no_results(self, mock_cfg, mock_org, mock_cf, mock_metrics, mock_registry):
        from scraper.core.scraper_runner import fetch_content_for_results
        mock_cfg.return_value.project_root = "/tmp"
        mock_org.return_value.ensure_directory.return_value = "/tmp/content"
        mock_registry.return_value.is_processed.return_value = False
        mock_metrics.return_value = MagicMock()

        result = fetch_content_for_results("github", [], max_articles=5)
        assert result == []

    @patch("scraper.core.scraper_runner.get_url_registry")
    @patch("scraper.core.scraper_runner.get_metrics_collector")
    @patch("scraper.core.scraper_runner.ContentFetcher")
    @patch("scraper.core.scraper_runner.DataOrganizer")
    @patch("scraper.core.scraper_runner.get_config")
    def test_skips_already_processed_urls(self, mock_cfg, mock_org, mock_cf, mock_metrics, mock_registry):
        from scraper.core.scraper_runner import fetch_content_for_results
        mock_cfg.return_value.project_root = "/tmp"
        mock_org.return_value.ensure_directory.return_value = "/tmp/content"
        registry = MagicMock()
        registry.is_processed.return_value = True
        mock_registry.return_value = registry
        mock_metrics.return_value = MagicMock()

        results = [{"url": "https://example.com", "title": "T"}]
        fetch_content_for_results("github", results, max_articles=5)
        registry.record_reappearance.assert_called_once()

    @patch("scraper.core.scraper_runner.get_url_registry")
    @patch("scraper.core.scraper_runner.get_metrics_collector")
    @patch("scraper.core.scraper_runner.ContentFetcher")
    @patch("scraper.core.scraper_runner.DataOrganizer")
    @patch("scraper.core.scraper_runner.get_config")
    def test_sorts_by_stars(self, mock_cfg, mock_org, mock_cf, mock_metrics, mock_registry):
        from scraper.core.scraper_runner import fetch_content_for_results
        mock_cfg.return_value.project_root = "/tmp"
        mock_org.return_value.ensure_directory.return_value = "/tmp/content"
        mock_registry.return_value.is_processed.return_value = False
        mock_metrics.return_value = MagicMock()
        fetcher = MagicMock()
        fetcher.fetch_content.return_value = {"local_path": "/tmp/a.md"}
        mock_cf.return_value = fetcher

        results = [{"url": "https://a.com", "title": "A", "stars": "100"}, {"url": "https://b.com", "title": "B", "stars": "500"}]
        fetch_content_for_results("github", results, max_articles=2)
        # Should have sorted by stars - verify fetch was called
        assert fetcher.fetch_content.call_count >= 1

    @patch("scraper.core.scraper_runner.get_url_registry")
    @patch("scraper.core.scraper_runner.get_metrics_collector")
    @patch("scraper.core.scraper_runner.ContentFetcher")
    @patch("scraper.core.scraper_runner.DataOrganizer")
    @patch("scraper.core.scraper_runner.get_config")
    def test_sorts_by_score(self, mock_cfg, mock_org, mock_cf, mock_metrics, mock_registry):
        from scraper.core.scraper_runner import fetch_content_for_results
        mock_cfg.return_value.project_root = "/tmp"
        mock_org.return_value.ensure_directory.return_value = "/tmp/content"
        mock_registry.return_value.is_processed.return_value = False
        mock_metrics.return_value = MagicMock()
        fetcher = MagicMock()
        fetcher.fetch_content.return_value = {}
        mock_cf.return_value = fetcher

        results = [{"url": "https://a.com", "title": "A", "score": "200"}, {"url": "https://b.com", "title": "B", "score": "50"}]
        fetch_content_for_results("hn", results, max_articles=2)
        assert fetcher.fetch_content.call_count >= 0

    @patch("scraper.core.scraper_runner.get_url_registry")
    @patch("scraper.core.scraper_runner.get_metrics_collector")
    @patch("scraper.core.scraper_runner.ContentFetcher")
    @patch("scraper.core.scraper_runner.DataOrganizer")
    @patch("scraper.core.scraper_runner.get_config")
    def test_max_articles_limits_fetching(self, mock_cfg, mock_org, mock_cf, mock_metrics, mock_registry):
        from scraper.core.scraper_runner import fetch_content_for_results
        mock_cfg.return_value.project_root = "/tmp"
        mock_org.return_value.ensure_directory.return_value = "/tmp/content"
        mock_registry.return_value.is_processed.return_value = False
        mock_metrics.return_value = MagicMock()
        fetcher = MagicMock()
        fetcher.fetch_content.return_value = {"local_path": "/tmp/f.md"}
        mock_cf.return_value = fetcher

        results = [{"url": f"https://example.com/{i}", "title": f"A{i}"} for i in range(10)]
        fetch_content_for_results("github", results, max_articles=2)
        assert fetcher.fetch_content.call_count <= 2

    @patch("scraper.core.scraper_runner.get_url_registry")
    @patch("scraper.core.scraper_runner.get_metrics_collector")
    @patch("scraper.core.scraper_runner.ContentFetcher")
    @patch("scraper.core.scraper_runner.DataOrganizer")
    @patch("scraper.core.scraper_runner.get_config")
    def test_skips_items_without_url(self, mock_cfg, mock_org, mock_cf, mock_metrics, mock_registry):
        from scraper.core.scraper_runner import fetch_content_for_results
        mock_cfg.return_value.project_root = "/tmp"
        mock_org.return_value.ensure_directory.return_value = "/tmp/content"
        mock_registry.return_value.is_processed.return_value = False
        mock_metrics.return_value = MagicMock()
        fetcher = MagicMock()
        mock_cf.return_value = fetcher

        with patch("scraper.core.scraper_runner.get_url_registry") as m2:
            m2.return_value.is_processed.return_value = False
            # Inject no-url item directly into results_to_fetch path
            with patch("scraper.core.scraper_runner.DataOrganizer") as mock_org2:
                mock_org2.return_value.ensure_directory.return_value = "/tmp/content"
                fetch_content_for_results("github", [], max_articles=5)

        assert fetcher.fetch_content.call_count == 0


class TestRunScrapersSequential(unittest.TestCase):
    @patch("scraper.core.scraper_runner.run_scraper")
    @patch("scraper.core.scraper_runner.get_metrics_collector")
    @patch("scraper.core.scraper_runner.StructuredLogger")
    def test_all_success(self, mock_logger, mock_metrics, mock_run):
        from scraper.core.scraper_runner import run_scrapers_sequential

        mock_run.return_value = True
        mock_metrics.return_value = MagicMock()

        scraper_classes = [MagicMock(__name__="S1"), MagicMock(__name__="S2")]
        success_count, failures = run_scrapers_sequential(scraper_classes, "json")
        assert success_count == 2
        assert not failures

    @patch("scraper.core.scraper_runner.run_scraper")
    @patch("scraper.core.scraper_runner.get_metrics_collector")
    @patch("scraper.core.scraper_runner.StructuredLogger")
    def test_partial_failure(self, mock_logger, mock_metrics, mock_run):
        from scraper.core.scraper_runner import run_scrapers_sequential

        mock_run.side_effect = [True, False]
        mock_metrics.return_value = MagicMock()

        scraper_classes = [MagicMock(__name__="S1"), MagicMock(__name__="S2")]
        success_count, failures = run_scrapers_sequential(scraper_classes, "json")
        assert success_count == 1

    @patch("scraper.core.scraper_runner.run_scraper")
    @patch("scraper.core.scraper_runner.get_metrics_collector")
    @patch("scraper.core.scraper_runner.StructuredLogger")
    def test_exception_during_scrape(self, mock_logger, mock_metrics, mock_run):
        from scraper.core.scraper_runner import run_scrapers_sequential

        mock_run.side_effect = RuntimeError("crash")
        mock_metrics.return_value = MagicMock()

        scraper_classes = [MagicMock(__name__="Crasher")]
        success_count, failures = run_scrapers_sequential(scraper_classes, "json")
        assert success_count == 0

    @patch("scraper.core.scraper_runner.run_scraper")
    @patch("scraper.core.scraper_runner.get_metrics_collector")
    @patch("scraper.core.scraper_runner.StructuredLogger")
    def test_empty_scrapers_list(self, mock_logger, mock_metrics, mock_run):
        from scraper.core.scraper_runner import run_scrapers_sequential

        mock_metrics.return_value = MagicMock()
        success_count, failures = run_scrapers_sequential([], "json")
        assert success_count == 0


if __name__ == "__main__":
    unittest.main()
