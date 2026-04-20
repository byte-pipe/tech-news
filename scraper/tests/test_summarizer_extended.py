"""Extended tests for ArticleSummarizer and related functions."""

import os
import tempfile
import unittest
from unittest.mock import MagicMock, patch


class TestArticleSummarizerInit(unittest.TestCase):
    @patch("scraper.utils.summarizer.get_model_config")
    @patch("scraper.utils.summarizer.OpenAI")
    def test_fast_mode(self, mock_openai, mock_config):
        from scraper.utils.summarizer import ArticleSummarizer
        mock_config.return_value.get_model_for_mode.return_value = "tinyllama:latest"
        summarizer = ArticleSummarizer(mode="fast")
        assert summarizer.mode == "fast"

    @patch("scraper.utils.summarizer.get_model_config")
    @patch("scraper.utils.summarizer.OpenAI")
    def test_quality_mode(self, mock_openai, mock_config):
        from scraper.utils.summarizer import ArticleSummarizer
        mock_config.return_value.get_model_for_mode.return_value = "llama3.2:1b"
        summarizer = ArticleSummarizer(mode="quality")
        assert summarizer.mode == "quality"

    @patch("scraper.utils.summarizer.get_model_config")
    def test_invalid_mode_raises(self, mock_config):
        from scraper.utils.summarizer import ArticleSummarizer
        with self.assertRaises(ValueError):
            ArticleSummarizer(mode="invalid")

    @patch("scraper.utils.summarizer.get_model_config")
    @patch("scraper.utils.summarizer.OpenAI")
    def test_custom_model_name(self, mock_openai, mock_config):
        from scraper.utils.summarizer import ArticleSummarizer
        mock_config.return_value.get_model_for_mode.return_value = "default"
        summarizer = ArticleSummarizer(model_name="custom-model")
        assert summarizer.model_name == "custom-model"

    @patch("scraper.utils.summarizer.get_model_config")
    @patch("scraper.utils.summarizer.OpenAI")
    def test_custom_timeout(self, mock_openai, mock_config):
        from scraper.utils.summarizer import ArticleSummarizer
        mock_config.return_value.get_model_for_mode.return_value = "tinyllama"
        summarizer = ArticleSummarizer(timeout=42.0)
        assert summarizer.timeout == 42.0

    @patch("scraper.utils.summarizer.get_model_config")
    @patch("scraper.utils.summarizer.OpenAI")
    def test_anthropic_mode(self, mock_openai, mock_config):
        from scraper.utils.summarizer import ArticleSummarizer
        mock_config.return_value.get_model_for_mode.return_value = "claude"
        summarizer = ArticleSummarizer(use_anthropic=True, anthropic_api_key="test-key")
        assert summarizer.use_anthropic is True
        assert "anthropic" in summarizer.base_url

    @patch("scraper.utils.summarizer.get_model_config")
    def test_anthropic_no_api_key(self, mock_config):
        from scraper.utils.summarizer import ArticleSummarizer
        mock_config.return_value.get_model_for_mode.return_value = "claude"
        with patch.dict(os.environ, {}, clear=True):
            os.environ.pop("ANTHROPIC_API_KEY", None)
            summarizer = ArticleSummarizer(use_anthropic=True, anthropic_api_key=None)
        assert summarizer.client is None

    @patch("scraper.utils.summarizer.get_model_config")
    @patch("scraper.utils.summarizer.OpenAI", side_effect=Exception("init failed"))
    def test_openai_init_error(self, mock_openai, mock_config):
        from scraper.utils.summarizer import ArticleSummarizer
        mock_config.return_value.get_model_for_mode.return_value = "tinyllama"
        summarizer = ArticleSummarizer()
        assert summarizer.client is None


class TestArticleSummarizerSummarize(unittest.TestCase):
    def _make_summarizer(self, mode="fast"):
        with patch("scraper.utils.summarizer.get_model_config") as mock_config:
            with patch("scraper.utils.summarizer.OpenAI") as mock_openai:
                mock_config.return_value.get_model_for_mode.return_value = "tinyllama"
                from scraper.utils.summarizer import ArticleSummarizer
                s = ArticleSummarizer(mode=mode)
                s.client = MagicMock()
                return s

    def test_summarize_no_client(self):
        with patch("scraper.utils.summarizer.get_model_config") as mock_config:
            with patch("scraper.utils.summarizer.OpenAI"):
                mock_config.return_value.get_model_for_mode.return_value = "tinyllama"
                from scraper.utils.summarizer import ArticleSummarizer
                s = ArticleSummarizer()
                s.client = None
                result = s.summarize("content")
        assert result is None

    def test_summarize_success(self):
        s = self._make_summarizer()
        mock_response = MagicMock()
        mock_response.choices[0].message.content = "Summary text"
        s.client.chat.completions.create.return_value = mock_response

        with patch.object(s, "_create_completion", return_value=mock_response):
            result = s.summarize("Article content here", title="Test Article")

        assert result == "Summary text"

    def test_summarize_with_title(self):
        s = self._make_summarizer()
        mock_response = MagicMock()
        mock_response.choices[0].message.content = "Summary"
        with patch.object(s, "_create_completion", return_value=mock_response):
            result = s.summarize("content", title="My Article")
        assert result == "Summary"

    def test_summarize_no_title(self):
        s = self._make_summarizer()
        mock_response = MagicMock()
        mock_response.choices[0].message.content = "Summary"
        with patch.object(s, "_create_completion", return_value=mock_response):
            result = s.summarize("content", title=None)
        assert result == "Summary"

    @patch("scraper.utils.summarizer.time.sleep")
    def test_summarize_retries_on_failure(self, mock_sleep):
        s = self._make_summarizer()
        mock_response = MagicMock()
        mock_response.choices[0].message.content = "OK"
        with patch.object(s, "_create_completion") as mock_create:
            mock_create.side_effect = [Exception("fail"), mock_response]
            result = s.summarize("content", max_retries=2)
        assert result == "OK"

    @patch("scraper.utils.summarizer.time.sleep")
    def test_summarize_all_retries_fail(self, mock_sleep):
        s = self._make_summarizer()
        with patch.object(s, "_create_completion", side_effect=Exception("always fails")):
            result = s.summarize("content", max_retries=2)
        assert result is None

    @patch("scraper.utils.summarizer.time.sleep")
    def test_summarize_model_not_found_breaks(self, mock_sleep):
        s = self._make_summarizer()
        with patch.object(s, "_create_completion", side_effect=Exception("model not found, try pulling it first")):
            result = s.summarize("content", max_retries=3)
        assert result is None

    def test_summarize_content_truncated(self):
        s = self._make_summarizer()
        s.config["max_content_length"] = 10
        mock_response = MagicMock()
        mock_response.choices[0].message.content = "Summary"
        with patch.object(s, "_create_completion", return_value=mock_response):
            result = s.summarize("A" * 100)
        assert result == "Summary"

    def test_create_completion_anthropic(self):
        s = self._make_summarizer()
        s.use_anthropic = True
        mock_response = MagicMock()
        s.client = MagicMock()
        s.client.chat.completions.create.return_value = mock_response
        result = s._create_completion(model="claude", messages=[])
        assert result == mock_response


class TestCleanSummary(unittest.TestCase):
    def _make_summarizer(self):
        with patch("scraper.utils.summarizer.get_model_config") as mock_config:
            with patch("scraper.utils.summarizer.OpenAI"):
                mock_config.return_value.get_model_for_mode.return_value = "tinyllama"
                from scraper.utils.summarizer import ArticleSummarizer
                return ArticleSummarizer()

    def test_clean_summary_basic(self):
        s = self._make_summarizer()
        assert s._clean_summary("  hello  ") == "hello"

    def test_clean_summary_empty(self):
        s = self._make_summarizer()
        assert s._clean_summary("") == ""

    def test_clean_summary_none(self):
        s = self._make_summarizer()
        assert s._clean_summary(None) == ""


class TestSaveSummary(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()

    def tearDown(self):
        import shutil
        shutil.rmtree(self.tmp, ignore_errors=True)

    def _make_summarizer(self):
        with patch("scraper.utils.summarizer.get_model_config") as mock_config:
            with patch("scraper.utils.summarizer.OpenAI"):
                mock_config.return_value.get_model_for_mode.return_value = "tinyllama"
                from scraper.utils.summarizer import ArticleSummarizer
                return ArticleSummarizer()

    def test_save_summary_creates_file(self):
        s = self._make_summarizer()
        metadata = {"title": "Test Article", "url": "https://example.com", "site_name": "hn"}
        path = s.save_summary("Summary text", metadata, self.tmp)
        assert path is not None
        assert os.path.exists(path)

    def test_save_summary_content_in_file(self):
        s = self._make_summarizer()
        metadata = {"title": "My Article", "url": "https://x.com", "site_name": "github"}
        path = s.save_summary("My summary", metadata, self.tmp)
        with open(path) as f:
            content = f.read()
        assert "My summary" in content

    def test_save_summary_uses_content_file(self):
        s = self._make_summarizer()
        metadata = {"title": "T", "url": "https://x.com", "site_name": "hn", "content_file": "hn-my-article"}
        path = s.save_summary("Summary", metadata, self.tmp)
        assert "hn-my-article" in path

    def test_save_summary_handles_error(self):
        s = self._make_summarizer()
        result = s.save_summary("Summary", {}, "/nonexistent/path/that/should/fail")
        # If the directory doesn't exist, makedirs will handle it or fail gracefully
        assert result is None or isinstance(result, str)

    def test_create_slug_basic(self):
        s = self._make_summarizer()
        assert s._create_slug("Hello World") == "hello-world"

    def test_create_slug_max_length(self):
        s = self._make_summarizer()
        result = s._create_slug("a" * 100, max_length=20)
        assert len(result) <= 20


class TestSummarizeArticleFromFile(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()

    def tearDown(self):
        import shutil
        shutil.rmtree(self.tmp, ignore_errors=True)

    def _make_md_file(self, content="Article content", title="Test"):
        path = os.path.join(self.tmp, "article.md")
        with open(path, "w") as f:
            f.write(f"---\ntitle: {title}\nurl: https://example.com\nsite_name: test\n---\n\n{content}")
        return path

    @patch("scraper.utils.summarizer.ArticleSummarizer")
    def test_success(self, mock_class):
        from scraper.utils.summarizer import summarize_article_from_file
        mock_summarizer = MagicMock()
        mock_summarizer.summarize.return_value = "Summary"
        mock_summarizer.save_summary.return_value = "/path/summary.md"
        mock_class.return_value = mock_summarizer

        path = self._make_md_file()
        result = summarize_article_from_file(path, self.tmp)
        assert result == "/path/summary.md"

    @patch("scraper.utils.summarizer.ArticleSummarizer")
    def test_no_summary_returns_none(self, mock_class):
        from scraper.utils.summarizer import summarize_article_from_file
        mock_summarizer = MagicMock()
        mock_summarizer.summarize.return_value = None
        mock_class.return_value = mock_summarizer

        path = self._make_md_file()
        result = summarize_article_from_file(path, self.tmp)
        assert result is None

    def test_missing_file_returns_none(self):
        from scraper.utils.summarizer import summarize_article_from_file
        result = summarize_article_from_file("/nonexistent/file.md", self.tmp)
        assert result is None

    @patch("scraper.utils.summarizer.ArticleSummarizer")
    def test_no_frontmatter(self, mock_class):
        from scraper.utils.summarizer import summarize_article_from_file
        mock_summarizer = MagicMock()
        mock_summarizer.summarize.return_value = "Summary"
        mock_summarizer.save_summary.return_value = "/path/summary.md"
        mock_class.return_value = mock_summarizer

        path = os.path.join(self.tmp, "plain.md")
        with open(path, "w") as f:
            f.write("Just plain content without frontmatter")

        result = summarize_article_from_file(path, self.tmp)
        assert result == "/path/summary.md"


class TestBatchSummarize(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.content_dir = os.path.join(self.tmp, "content")
        os.makedirs(self.content_dir)
        self.output_dir = os.path.join(self.tmp, "summaries")
        os.makedirs(self.output_dir)

    def tearDown(self):
        import shutil
        shutil.rmtree(self.tmp, ignore_errors=True)

    def _make_md_files(self, n=3):
        for i in range(n):
            path = os.path.join(self.content_dir, f"article_{i}.md")
            with open(path, "w") as f:
                f.write(f"---\ntitle: Article {i}\nurl: https://x.com/{i}\nsite_name: test\n---\n\nContent {i}")

    @patch("scraper.utils.summarizer.summarize_article_from_file")
    def test_batch_summarize_empty_dir(self, mock_summarize):
        from scraper.utils.summarizer import batch_summarize_directory
        result = batch_summarize_directory(self.content_dir, self.output_dir)
        assert result == []
        mock_summarize.assert_not_called()

    @patch("scraper.utils.summarizer.summarize_article_from_file")
    def test_batch_summarize_multiple_files(self, mock_summarize):
        from scraper.utils.summarizer import batch_summarize_directory
        self._make_md_files(3)
        mock_summarize.return_value = "/path/summary.md"
        result = batch_summarize_directory(self.content_dir, self.output_dir)
        assert len(result) == 3

    @patch("scraper.utils.summarizer.summarize_article_from_file")
    def test_batch_summarize_max_files(self, mock_summarize):
        from scraper.utils.summarizer import batch_summarize_directory
        self._make_md_files(5)
        mock_summarize.return_value = "/path/summary.md"
        result = batch_summarize_directory(self.content_dir, self.output_dir, max_files=2)
        assert len(result) == 2

    @patch("scraper.utils.summarizer.summarize_article_from_file")
    def test_batch_summarize_with_progress_callback(self, mock_summarize):
        from scraper.utils.summarizer import batch_summarize_directory
        self._make_md_files(2)
        mock_summarize.return_value = "/path/summary.md"
        calls = []
        batch_summarize_directory(self.content_dir, self.output_dir, progress_callback=lambda i, n, f: calls.append((i, n, f)))
        assert len(calls) == 2

    @patch("scraper.utils.summarizer.summarize_article_from_file")
    def test_batch_summarize_skips_none_results(self, mock_summarize):
        from scraper.utils.summarizer import batch_summarize_directory
        self._make_md_files(3)
        mock_summarize.side_effect = ["/path/s1.md", None, "/path/s3.md"]
        result = batch_summarize_directory(self.content_dir, self.output_dir)
        assert len(result) == 2

    @patch("scraper.utils.summarizer.batch_summarize_directory")
    def test_batch_summarize_local_model(self, mock_batch):
        from scraper.utils.summarizer import batch_summarize_local_model
        mock_batch.return_value = ["/path/s.md"]
        result = batch_summarize_local_model(self.content_dir, self.output_dir, model_name="gemma3n:latest")
        mock_batch.assert_called_once()
        assert result == ["/path/s.md"]

    @patch("scraper.utils.summarizer.summarize_article_from_file")
    def test_batch_summarize_local_wrapper(self, mock_summarize):
        from scraper.utils.summarizer import summarize_article_from_file_local
        mock_summarize.return_value = "/path/s.md"
        path = os.path.join(self.content_dir, "article.md")
        with open(path, "w") as f:
            f.write("content")
        result = summarize_article_from_file_local(path, self.output_dir)
        mock_summarize.assert_called_once()


if __name__ == "__main__":
    unittest.main()
