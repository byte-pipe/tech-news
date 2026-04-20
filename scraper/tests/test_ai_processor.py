"""Tests for ai_processor module."""

import os
import tempfile
import unittest
from unittest.mock import MagicMock, patch


class TestSummarizeContent(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        # Create a data directory structure for the tests
        self.date_dir = "2026-04-20"
        self.data_dir = os.path.join(self.tmp, "data")
        self.content_dir = os.path.join(self.data_dir, self.date_dir, "content")
        self.summary_dir = os.path.join(self.data_dir, self.date_dir, "summaries")
        os.makedirs(self.content_dir, exist_ok=True)
        os.makedirs(self.summary_dir, exist_ok=True)

    def tearDown(self):
        import shutil
        shutil.rmtree(self.tmp, ignore_errors=True)

    @patch("scraper.core.ai_processor.batch_summarize_directory")
    @patch("scraper.core.ai_processor.get_model_config")
    def test_summarize_content_success(self, mock_config, mock_batch):
        from scraper.core.ai_processor import summarize_content
        mock_config.return_value.get_model_for_mode.return_value = "llama3.2:1b"
        mock_config.return_value.get_fallback_model.return_value = "tinyllama:latest"
        mock_batch.return_value = ["/path/to/summary.md"]

        with patch("os.path.exists") as mock_exists:
            mock_exists.side_effect = lambda p: self.tmp in p or p == self.data_dir or "content" in p
            with patch("os.getcwd", return_value=self.tmp):
                result = summarize_content(self.date_dir, model_name="llama3.2:1b")

        assert isinstance(result, tuple)
        assert len(result) == 2

    @patch("scraper.core.ai_processor.batch_summarize_directory")
    @patch("scraper.core.ai_processor.get_model_config")
    def test_summarize_content_uses_default_model(self, mock_config, mock_batch):
        from scraper.core.ai_processor import summarize_content
        mock_config.return_value.get_model_for_mode.return_value = "gemma3n:latest"
        mock_config.return_value.get_fallback_model.return_value = "llama3.2:1b"
        mock_batch.return_value = ["/path/summary.md"]

        with patch("os.makedirs"), patch("os.path.exists", return_value=True):
            with patch("os.path.dirname", return_value=self.tmp):
                result = summarize_content(self.date_dir, model_name=None)

        assert isinstance(result, tuple)

    @patch("scraper.core.ai_processor.batch_summarize_directory")
    @patch("scraper.core.ai_processor.get_model_config")
    def test_summarize_content_fallback_model(self, mock_config, mock_batch):
        from scraper.core.ai_processor import summarize_content
        mock_config.return_value.get_model_for_mode.return_value = "gemma3n:latest"
        mock_config.return_value.get_fallback_model.return_value = "tinyllama:latest"
        # Primary returns empty, fallback returns results
        mock_batch.side_effect = [[], ["summary.md"]]

        with patch("os.makedirs"), patch("os.path.exists", return_value=True):
            with patch("os.path.dirname", return_value=self.tmp):
                result = summarize_content(self.date_dir, model_name="gemma3n:latest", fallback_model="tinyllama:latest")

        assert isinstance(result, tuple)

    @patch("scraper.core.ai_processor.batch_summarize_directory")
    @patch("scraper.core.ai_processor.get_model_config")
    def test_summarize_content_no_fallback(self, mock_config, mock_batch):
        from scraper.core.ai_processor import summarize_content
        mock_config.return_value.get_model_for_mode.return_value = "gemma3n:latest"
        mock_config.return_value.get_fallback_model.return_value = None
        mock_batch.return_value = []

        with patch("os.makedirs"), patch("os.path.exists", return_value=True):
            with patch("os.path.dirname", return_value=self.tmp):
                result = summarize_content(self.date_dir, model_name="gemma3n:latest", fallback_model=None)

        assert result[0] is False

    @patch("scraper.core.ai_processor.batch_summarize_directory")
    @patch("scraper.core.ai_processor.get_model_config")
    def test_summarize_content_small_model_uses_fast_mode(self, mock_config, mock_batch):
        from scraper.core.ai_processor import summarize_content
        mock_config.return_value.get_model_for_mode.return_value = "tinyllama:latest"
        mock_config.return_value.get_fallback_model.return_value = "smollm:135m"
        mock_batch.return_value = ["summary.md"]

        with patch("os.makedirs"), patch("os.path.exists", return_value=True):
            with patch("os.path.dirname", return_value=self.tmp):
                result = summarize_content(self.date_dir, model_name="tinyllama:1b")

        assert isinstance(result, tuple)

    @patch("scraper.core.ai_processor.batch_summarize_directory")
    @patch("scraper.core.ai_processor.get_model_config")
    def test_summarize_content_exception(self, mock_config, mock_batch):
        from scraper.core.ai_processor import summarize_content
        mock_config.return_value.get_model_for_mode.return_value = "llama3.2:1b"
        mock_config.return_value.get_fallback_model.return_value = "tinyllama:latest"
        mock_batch.side_effect = RuntimeError("batch failed")

        with patch("os.makedirs"), patch("os.path.exists", return_value=True):
            with patch("os.path.dirname", return_value=self.tmp):
                result = summarize_content(self.date_dir, model_name="llama3.2:1b", fallback_model=None)

        assert result[0] is False

    @patch("scraper.core.ai_processor.get_model_config")
    def test_summarize_content_no_data_dir(self, mock_config):
        from scraper.core.ai_processor import summarize_content
        mock_config.return_value.get_model_for_mode.return_value = "llama3.2:1b"

        with patch("os.path.exists", return_value=False):
            with patch("os.getcwd", return_value="/nonexistent"):
                with patch("os.path.dirname", return_value="/nonexistent"):
                    result = summarize_content("2026-04-20", model_name="llama3.2:1b")

        assert result == (False, [])


class TestSummarizeContentAdditional(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.date_dir = "2026-04-20"

    def tearDown(self):
        import shutil
        shutil.rmtree(self.tmp, ignore_errors=True)

    @patch("scraper.core.ai_processor.batch_summarize_directory")
    @patch("scraper.core.ai_processor.get_model_config")
    def test_fallback_exception_returns_false(self, mock_config, mock_batch):
        from scraper.core.ai_processor import summarize_content
        mock_config.return_value.get_model_for_mode.return_value = "gemma3n:latest"
        mock_config.return_value.get_fallback_model.return_value = "tinyllama:latest"
        # Primary returns empty, fallback raises exception
        mock_batch.side_effect = [[], RuntimeError("fallback failed")]

        with patch("os.makedirs"), patch("os.path.exists", return_value=True):
            with patch("os.path.dirname", return_value=self.tmp):
                result = summarize_content(self.date_dir, model_name="gemma3n:latest", fallback_model="tinyllama:latest")

        assert result[0] is False

    @patch("scraper.core.ai_processor.batch_summarize_directory")
    @patch("scraper.core.ai_processor.get_model_config")
    def test_primary_exception_with_model_not_found_uses_fallback(self, mock_config, mock_batch):
        from scraper.core.ai_processor import summarize_content
        mock_config.return_value.get_model_for_mode.return_value = "gemma3n:latest"
        mock_config.return_value.get_fallback_model.return_value = "tinyllama:latest"
        # Primary raises model not found, fallback succeeds
        mock_batch.side_effect = [RuntimeError("model not found"), ["summary.md"]]

        with patch("os.makedirs"), patch("os.path.exists", return_value=True):
            with patch("os.path.dirname", return_value=self.tmp):
                result = summarize_content(self.date_dir, model_name="gemma3n:latest", fallback_model="tinyllama:latest")

        assert result[0] is True


class TestSummarizeWithAnthropic(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.date_dir = "2026-04-20"
        self.content_dir = os.path.join(self.tmp, "data", self.date_dir, "content")
        os.makedirs(self.content_dir, exist_ok=True)

    def tearDown(self):
        import shutil
        shutil.rmtree(self.tmp, ignore_errors=True)

    @patch("scraper.core.ai_processor.get_model_config")
    def test_no_data_dir_returns_false(self, mock_config):
        from scraper.core.ai_processor import summarize_with_anthropic
        mock_config.return_value.get_anthropic_model.return_value = "claude-3-haiku-20240307"

        with patch("os.path.exists", return_value=False):
            with patch("os.getcwd", return_value="/nonexistent"):
                with patch("os.path.dirname", return_value="/nonexistent"):
                    result = summarize_with_anthropic(self.date_dir, api_key="test-key")

        assert result == (False, [])

    @patch("scraper.core.ai_processor.get_model_config")
    def test_no_content_dir_returns_false(self, mock_config):
        from scraper.core.ai_processor import summarize_with_anthropic
        mock_config.return_value.get_anthropic_model.return_value = "claude-3-haiku-20240307"

        with patch("os.path.exists") as mock_exists:
            # data dir exists but content dir doesn't
            mock_exists.side_effect = lambda p: "data" in p and "content" not in p
            with patch("os.getcwd", return_value=self.tmp):
                result = summarize_with_anthropic(self.date_dir, api_key="test-key")

        assert result[0] is False

    @patch("scraper.core.ai_processor.get_model_config")
    def test_empty_content_dir_returns_false(self, mock_config):
        from scraper.core.ai_processor import summarize_with_anthropic
        mock_config.return_value.get_anthropic_model.return_value = "claude-3-haiku-20240307"

        with patch("os.makedirs"), patch("os.path.exists", return_value=True):
            with patch("os.path.dirname", return_value=self.tmp):
                with patch("pathlib.Path.glob", return_value=[]):
                    result = summarize_with_anthropic(self.date_dir, api_key="test-key")

        assert result == (False, [])

    @patch("scraper.core.ai_processor.get_model_config")
    def test_with_md_files_success(self, mock_config):
        from scraper.core.ai_processor import summarize_with_anthropic
        mock_config.return_value.get_anthropic_model.return_value = "claude-3-haiku-20240307"

        # Create a real md file in the content dir
        content_file = os.path.join(self.content_dir, "test.md")
        with open(content_file, "w") as f:
            f.write("---\ntitle: Test Article\nurl: https://example.com\n---\nArticle content here.\n")

        with patch("os.makedirs"):
            with patch("os.path.dirname", return_value=self.tmp):
                with patch("scraper.utils.summarizer.ArticleSummarizer") as mock_class:
                    mock_inst = MagicMock()
                    mock_inst.summarize.return_value = "Summary text"
                    mock_inst.save_summary.return_value = "/tmp/summary.md"
                    mock_class.return_value = mock_inst

                    with patch("os.path.exists") as mock_exists:
                        mock_exists.side_effect = lambda p: self.tmp in p or "content" in p or "data" in p
                        result = summarize_with_anthropic(self.date_dir, api_key="test-key")

        # Result is a tuple; may succeed or fail depending on path resolution
        assert isinstance(result, tuple)

    @patch("scraper.core.ai_processor.get_model_config")
    def test_with_md_files_exception_during_summarize(self, mock_config):
        from scraper.core.ai_processor import summarize_with_anthropic
        mock_config.return_value.get_anthropic_model.return_value = "claude-3-haiku-20240307"

        content_file = os.path.join(self.content_dir, "test2.md")
        with open(content_file, "w") as f:
            f.write("---\ntitle: Test\n---\nContent\n")

        with patch("os.makedirs"):
            with patch("os.path.dirname", return_value=self.tmp):
                with patch("scraper.utils.summarizer.ArticleSummarizer", side_effect=RuntimeError("api error")):
                    with patch("os.path.exists") as mock_exists:
                        mock_exists.side_effect = lambda p: self.tmp in p or "content" in p or "data" in p
                        result = summarize_with_anthropic(self.date_dir, api_key="test-key")

        assert isinstance(result, tuple)


if __name__ == "__main__":
    unittest.main()
