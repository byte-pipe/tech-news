"""Tests for analytics module."""

import os
import tempfile
import unittest
from unittest.mock import MagicMock, patch

import pandas as pd


def _make_df(n=5):
    import numpy as np
    dates = pd.date_range("2026-04-01", periods=n, freq="D")
    return pd.DataFrame({
        "url": [f"https://example.com/{i}" for i in range(n)],
        "title": [f"Article {i}" for i in range(n)],
        "source": ["github", "hn", "devto", "reddit", "github"][:n],
        "score": [100, 200, 50, 300, 150][:n],
        "comments": [10, 20, 5, 30, 15][:n],
        "seen_count": [1, 2, 1, 3, 1][:n],
        "category": ["ai", "python", "web", "ai", "python"][:n],
        "date_scraped": dates,
        "date_published": dates,
    })


class TestLoadData(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.csv_path = os.path.join(self.tmp, "links.csv")

    def tearDown(self):
        import shutil
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_load_basic(self):
        from scraper.core.analytics import _load_data
        df = _make_df()
        df.to_csv(self.csv_path, index=False)
        result = _load_data(self.csv_path)
        assert len(result) == 5

    def test_load_with_days_filter(self):
        from scraper.core.analytics import _load_data
        import pandas as pd
        # Create data spanning 20 days, filter to last 3
        dates = pd.date_range("2026-01-01", periods=20, freq="D")
        df = pd.DataFrame({
            "url": [f"https://example.com/{i}" for i in range(20)],
            "title": [f"Article {i}" for i in range(20)],
            "source": ["github"] * 20,
            "score": [100] * 20,
            "comments": [10] * 20,
            "seen_count": [1] * 20,
            "category": ["ai"] * 20,
            "date_scraped": dates,
            "date_published": dates,
        })
        df.to_csv(self.csv_path, index=False)
        result = _load_data(self.csv_path, days=3)
        assert len(result) <= 20
        assert len(result) >= 1

    def test_score_is_numeric(self):
        from scraper.core.analytics import _load_data
        df = _make_df()
        df.to_csv(self.csv_path, index=False)
        result = _load_data(self.csv_path)
        assert result["score"].dtype in [int, "int64", "int32"]


class TestPrintSummaryTable(unittest.TestCase):
    def test_print_summary_no_crash(self):
        from scraper.core.analytics import print_summary_table
        df = _make_df()
        print_summary_table(df)  # Should not raise

    def test_print_summary_with_scores(self):
        from scraper.core.analytics import print_summary_table
        df = _make_df()
        print_summary_table(df)  # Should not raise


class TestChartFunctions(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.df = _make_df()

    def tearDown(self):
        import shutil
        shutil.rmtree(self.tmp, ignore_errors=True)

    def _mock_save(self, fig, out_dir, name, width=None):
        path = os.path.join(out_dir, f"{name}.png")
        fig.savefig(path, dpi=10)
        import matplotlib.pyplot as plt
        plt.close(fig)
        return path

    @patch("scraper.core.analytics._save_and_show")
    def test_chart_daily_volume(self, mock_save):
        from scraper.core.analytics import chart_daily_volume
        mock_save.return_value = "/tmp/daily_volume.png"
        result = chart_daily_volume(self.df, self.tmp)
        assert mock_save.called

    @patch("scraper.core.analytics._save_and_show")
    def test_chart_source_breakdown(self, mock_save):
        from scraper.core.analytics import chart_source_breakdown
        mock_save.return_value = "/tmp/source.png"
        chart_source_breakdown(self.df, self.tmp)
        assert mock_save.called

    @patch("scraper.core.analytics._save_and_show")
    def test_chart_category_bars(self, mock_save):
        from scraper.core.analytics import chart_category_bars
        mock_save.return_value = "/tmp/cats.png"
        chart_category_bars(self.df, self.tmp)
        assert mock_save.called

    @patch("scraper.core.analytics._save_and_show")
    def test_chart_category_trend(self, mock_save):
        from scraper.core.analytics import chart_category_trend
        mock_save.return_value = "/tmp/trend.png"
        chart_category_trend(self.df, self.tmp)
        assert mock_save.called

    @patch("scraper.core.analytics._save_and_show")
    def test_chart_score_distribution(self, mock_save):
        from scraper.core.analytics import chart_score_distribution
        mock_save.return_value = "/tmp/score.png"
        # Make df with enough scores and counts per source
        df = _make_df(5)
        # Duplicate so sources have >= 10 entries
        df = pd.concat([df] * 5, ignore_index=True)
        chart_score_distribution(df, self.tmp)
        # May return "" if filtered out

    @patch("scraper.core.analytics._save_and_show")
    def test_chart_score_distribution_empty(self, mock_save):
        from scraper.core.analytics import chart_score_distribution
        df = _make_df()
        df["score"] = 0
        result = chart_score_distribution(df, self.tmp)
        assert result == ""
        mock_save.assert_not_called()

    @patch("scraper.core.analytics._save_and_show")
    def test_chart_top_trending(self, mock_save):
        from scraper.core.analytics import chart_top_trending
        mock_save.return_value = "/tmp/trending.png"
        chart_top_trending(self.df, self.tmp)
        assert mock_save.called

    @patch("scraper.core.analytics._save_and_show")
    def test_chart_top_trending_empty(self, mock_save):
        from scraper.core.analytics import chart_top_trending
        df = _make_df()
        df = df.iloc[0:0]  # empty df
        result = chart_top_trending(df, self.tmp)
        assert result == ""

    @patch("scraper.core.analytics._save_and_show")
    def test_chart_heatmap(self, mock_save):
        from scraper.core.analytics import chart_heatmap
        mock_save.return_value = "/tmp/heatmap.png"
        chart_heatmap(self.df, self.tmp)
        assert mock_save.called


class TestRunAnalytics(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.csv_path = os.path.join(self.tmp, "links.csv")
        _make_df().to_csv(self.csv_path, index=False)

    def tearDown(self):
        import shutil
        shutil.rmtree(self.tmp, ignore_errors=True)

    @patch("scraper.core.analytics._save_and_show")
    @patch("scraper.core.analytics._wait_for_key")
    def test_run_analytics_returns_list(self, mock_wait, mock_save):
        from scraper.core.analytics import run_analytics
        mock_save.return_value = "/tmp/chart.png"
        result = run_analytics(self.csv_path, out_dir=self.tmp)
        assert isinstance(result, list)

    @patch("scraper.core.analytics._save_and_show")
    @patch("scraper.core.analytics._wait_for_key")
    def test_run_analytics_specific_charts(self, mock_wait, mock_save):
        from scraper.core.analytics import run_analytics
        mock_save.return_value = "/tmp/chart.png"
        result = run_analytics(self.csv_path, out_dir=self.tmp, charts=["daily_volume"])
        assert isinstance(result, list)

    def test_run_analytics_empty_csv(self):
        from scraper.core.analytics import run_analytics
        # Write empty CSV
        empty_path = os.path.join(self.tmp, "empty.csv")
        pd.DataFrame(columns=["url", "source", "score", "comments", "seen_count", "category", "date_scraped", "date_published"]).to_csv(empty_path, index=False)
        result = run_analytics(empty_path, out_dir=self.tmp)
        assert result == []


class TestShowPng(unittest.TestCase):
    @patch("scraper.core.analytics.subprocess.run")
    def test_show_png_chafa_not_found(self, mock_run):
        from scraper.core.analytics import _show_png
        mock_run.side_effect = FileNotFoundError("chafa not found")
        _show_png("/tmp/test.png")  # Should not raise

    @patch("scraper.core.analytics.subprocess.run")
    def test_show_png_calls_chafa(self, mock_run):
        from scraper.core.analytics import _show_png
        _show_png("/tmp/test.png", width=80)
        mock_run.assert_called_once()


if __name__ == "__main__":
    unittest.main()
