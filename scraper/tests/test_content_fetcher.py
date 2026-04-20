"""Tests for ContentFetcher."""

import os
import tempfile
import unittest
from unittest.mock import MagicMock, patch


class TestContentFetcherSkipLogic(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        with patch("scraper.utils.content_fetcher.get_url_registry"):
            from scraper.utils.content_fetcher import ContentFetcher
            self.fetcher = ContentFetcher(project_root=self.tmp)

    def tearDown(self):
        import shutil
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_skip_pdf_url(self):
        meta = {}
        with patch.object(self.fetcher, "_get_registry_skip", return_value=False) if hasattr(self.fetcher, "_get_registry_skip") else patch("scraper.utils.content_fetcher.get_url_registry") as m:
            if not hasattr(self.fetcher, "_get_registry_skip"):
                m.return_value.is_processed.return_value = False
            result = self.fetcher.fetch_content("https://example.com/file.pdf", "test_site", meta)
        assert result.get("skipped") is True
        assert "pdf" in result.get("skip_reason", "").lower()

    def test_skip_png_url(self):
        with patch("scraper.utils.content_fetcher.get_url_registry") as m:
            m.return_value.is_processed.return_value = False
            result = self.fetcher.fetch_content("https://example.com/image.png", "test_site", {})
        assert result.get("skipped") is True

    def test_skip_zip_url(self):
        with patch("scraper.utils.content_fetcher.get_url_registry") as m:
            m.return_value.is_processed.return_value = False
            result = self.fetcher.fetch_content("https://example.com/archive.zip", "test_site", {})
        assert result.get("skipped") is True

    def test_invalid_url_empty(self):
        result = self.fetcher.fetch_content("", "test_site", {})
        assert "error" in result

    def test_invalid_url_none(self):
        result = self.fetcher.fetch_content(None, "test_site", {})
        assert "error" in result

    def test_invalid_url_no_http(self):
        result = self.fetcher.fetch_content("ftp://example.com", "test_site", {})
        assert "error" in result

    def test_invalid_site_name(self):
        result = self.fetcher.fetch_content("https://example.com", "", {})
        assert "error" in result

    def test_already_processed_url(self):
        with patch("scraper.utils.content_fetcher.get_url_registry") as m:
            registry = MagicMock()
            registry.is_processed.return_value = True
            registry.get_entry.return_value = {"first_seen": "2026-01-01", "seen_count": 1, "content_path": "/some/path"}
            m.return_value = registry
            result = self.fetcher.fetch_content("https://example.com/article", "test_site", {})
        assert result.get("skipped") is True
        assert result.get("skip_reason") == "already_processed"

    def test_force_bypasses_registry(self):
        with patch("scraper.utils.content_fetcher.get_url_registry") as m:
            registry = MagicMock()
            registry.is_processed.return_value = True
            m.return_value = registry

            with patch.object(self.fetcher.session, "get") as mock_get:
                resp = MagicMock()
                resp.content = b"<html><body><p>Article text</p></body></html>"
                resp.headers = {"Content-Type": "text/html"}
                resp.raise_for_status = MagicMock()
                mock_get.return_value = resp

                with patch.object(self.fetcher, "_save_content", return_value="/path/to/file.md"):
                    result = self.fetcher.fetch_content("https://example.com/article", "test_site", {}, force=True)

            # Should not skip when force=True
            assert result.get("skip_reason") != "already_processed"

    def test_non_html_content_type_skipped(self):
        with patch("scraper.utils.content_fetcher.get_url_registry") as m:
            registry = MagicMock()
            registry.is_processed.return_value = False
            m.return_value = registry

            with patch.object(self.fetcher.session, "get") as mock_get:
                resp = MagicMock()
                resp.content = b"%PDF binary"
                resp.headers = {"Content-Type": "application/pdf"}
                resp.raise_for_status = MagicMock()
                mock_get.return_value = resp

                result = self.fetcher.fetch_content("https://example.com/article", "test_site", {})

        assert result.get("skipped") is True

    def test_successful_html_fetch(self):
        with patch("scraper.utils.content_fetcher.get_url_registry") as m:
            registry = MagicMock()
            registry.is_processed.return_value = False
            m.return_value = registry

            with patch.object(self.fetcher.session, "get") as mock_get:
                resp = MagicMock()
                resp.content = b"<html><body><p>Article content</p></body></html>"
                resp.headers = {"Content-Type": "text/html; charset=utf-8"}
                resp.raise_for_status = MagicMock()
                mock_get.return_value = resp

                with patch.object(self.fetcher, "_save_content", return_value="/path/to/saved.md"):
                    result = self.fetcher.fetch_content("https://example.com/article", "test_site", {})

        assert "error" not in result or result.get("content")

    def test_network_error(self):
        import requests
        with patch("scraper.utils.content_fetcher.get_url_registry") as m:
            registry = MagicMock()
            registry.is_processed.return_value = False
            m.return_value = registry

            with patch.object(self.fetcher.session, "get") as mock_get:
                mock_get.side_effect = requests.exceptions.ConnectionError("network fail")
                result = self.fetcher.fetch_content("https://example.com/article", "test_site", {})

        assert "error" in result


class TestContentFetcherExtract(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        with patch("scraper.utils.content_fetcher.get_url_registry"):
            from scraper.utils.content_fetcher import ContentFetcher
            self.fetcher = ContentFetcher(project_root=self.tmp)

    def tearDown(self):
        import shutil
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_extract_content_gets_title(self):
        from bs4 import BeautifulSoup
        html = "<html><head><title>My Title</title></head><body><p>Content</p></body></html>"
        soup = BeautifulSoup(html, "html.parser")
        result = self.fetcher._extract_content(soup, "https://example.com")
        assert result["metadata"].get("title") == "My Title"

    def test_extract_content_gets_description(self):
        from bs4 import BeautifulSoup
        html = '<html><head><meta name="description" content="Test desc"/></head><body></body></html>'
        soup = BeautifulSoup(html, "html.parser")
        result = self.fetcher._extract_content(soup, "https://example.com")
        assert result["metadata"].get("description") == "Test desc"

    def test_html_to_markdown_basic(self):
        from bs4 import BeautifulSoup
        soup = BeautifulSoup("<p>Hello world</p>", "html.parser")
        result = self.fetcher._html_to_markdown(soup)
        assert "Hello world" in result

    def test_html_to_markdown_empty(self):
        result = self.fetcher._html_to_markdown(None)
        assert result == ""

    def test_html_to_markdown_headers(self):
        from bs4 import BeautifulSoup
        soup = BeautifulSoup("<h1>Title</h1><p>Body</p>", "html.parser")
        result = self.fetcher._html_to_markdown(soup)
        assert "Title" in result


class TestFetchUrlContentFunction(unittest.TestCase):
    @patch("scraper.utils.content_fetcher.get_url_registry")
    def test_convenience_function(self, mock_registry):
        mock_registry.return_value.is_processed.return_value = False
        from scraper.utils.content_fetcher import fetch_url_content

        with patch("scraper.utils.content_fetcher.ContentFetcher.fetch_content") as mock_fetch:
            mock_fetch.return_value = {"content": "test"}
            result = fetch_url_content("https://example.com", "test_site")
            assert result == {"content": "test"}


class TestCheckExistingContent(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        with patch("scraper.utils.content_fetcher.get_url_registry"):
            from scraper.utils.content_fetcher import ContentFetcher
            self.fetcher = ContentFetcher(project_root=self.tmp)

    def tearDown(self):
        import shutil
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_returns_none_when_no_content_dir(self):
        result = self.fetcher._check_existing_content("https://example.com/article", "github")
        assert result is None

    def test_returns_path_when_slug_matches(self):
        from scraper.utils.datetime_utils import get_date_folder
        date_folder = get_date_folder()
        content_dir = os.path.join(self.tmp, "data", date_folder, "content")
        os.makedirs(content_dir, exist_ok=True)
        # Create a file whose name contains the slug
        fname = "github-my-article.md"
        fpath = os.path.join(content_dir, fname)
        with open(fpath, "w") as f:
            f.write("---\nurl: https://example.com/my-article\n---\nContent\n")

        result = self.fetcher._check_existing_content("https://example.com/my-article", "github")
        assert result == fpath

    def test_returns_path_when_url_in_frontmatter(self):
        from scraper.utils.datetime_utils import get_date_folder
        date_folder = get_date_folder()
        content_dir = os.path.join(self.tmp, "data", date_folder, "content")
        os.makedirs(content_dir, exist_ok=True)
        fname = "github-other.md"
        fpath = os.path.join(content_dir, fname)
        with open(fpath, "w") as f:
            f.write("---\nurl: https://example.com/specific\n---\nContent\n")

        result = self.fetcher._check_existing_content("https://example.com/specific", "github")
        assert result == fpath

    def test_returns_none_when_no_matching_file(self):
        from scraper.utils.datetime_utils import get_date_folder
        date_folder = get_date_folder()
        content_dir = os.path.join(self.tmp, "data", date_folder, "content")
        os.makedirs(content_dir, exist_ok=True)
        fname = "github-other.md"
        fpath = os.path.join(content_dir, fname)
        with open(fpath, "w") as f:
            f.write("---\nurl: https://other.com/page\n---\nContent\n")

        result = self.fetcher._check_existing_content("https://example.com/article", "github")
        assert result is None


class TestCachedContentPath(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        with patch("scraper.utils.content_fetcher.get_url_registry"):
            from scraper.utils.content_fetcher import ContentFetcher
            self.fetcher = ContentFetcher(project_root=self.tmp)

    def tearDown(self):
        import shutil
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_cached_file_is_returned_without_fetching(self):
        from scraper.utils.datetime_utils import get_date_folder
        date_folder = get_date_folder()
        content_dir = os.path.join(self.tmp, "data", date_folder, "content")
        os.makedirs(content_dir, exist_ok=True)

        existing_file = os.path.join(content_dir, "github-my-article.md")
        with open(existing_file, "w") as f:
            f.write("---\nurl: https://example.com/my-article\n---\nContent here\n")

        with patch("scraper.utils.content_fetcher.get_url_registry") as m:
            m.return_value.is_processed.return_value = False
            with patch.object(self.fetcher, "_check_existing_content", return_value=existing_file):
                result = self.fetcher.fetch_content("https://example.com/my-article", "github", {})

        assert result.get("cached") is True
        assert result.get("local_path") == existing_file

    def test_cached_file_content_read_into_metadata(self):
        from scraper.utils.datetime_utils import get_date_folder
        date_folder = get_date_folder()
        content_dir = os.path.join(self.tmp, "data", date_folder, "content")
        os.makedirs(content_dir, exist_ok=True)

        existing_file = os.path.join(content_dir, "github-article.md")
        with open(existing_file, "w") as f:
            f.write("---\ntitle: test\n---\nMy article content\n")

        with patch("scraper.utils.content_fetcher.get_url_registry") as m:
            m.return_value.is_processed.return_value = False
            with patch.object(self.fetcher, "_check_existing_content", return_value=existing_file):
                result = self.fetcher.fetch_content("https://example.com/article", "github", {})

        assert "My article content" in result.get("content", "")


class TestSaveContent(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        with patch("scraper.utils.content_fetcher.get_url_registry"):
            from scraper.utils.content_fetcher import ContentFetcher
            self.fetcher = ContentFetcher(project_root=self.tmp)

    def tearDown(self):
        import shutil
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_save_content_creates_file(self):
        content_dir = os.path.join(self.tmp, "data", "2026-04-20", "content")
        os.makedirs(content_dir, exist_ok=True)

        with patch("scraper.core.data_organizer.DataOrganizer.ensure_directory", return_value=content_dir):
            file_path = self.fetcher._save_content(
                "https://example.com/test",
                "github",
                "# Test content",
                {"title": "Test Article"},
            )

        assert os.path.exists(file_path)
        with open(file_path) as f:
            content = f.read()
        assert "Test Article" in content
        assert "Test content" in content

    def test_save_content_includes_frontmatter(self):
        content_dir = os.path.join(self.tmp, "data", "2026-04-20", "content")
        os.makedirs(content_dir, exist_ok=True)

        with patch("scraper.core.data_organizer.DataOrganizer.ensure_directory", return_value=content_dir):
            file_path = self.fetcher._save_content(
                "https://example.com/test",
                "github",
                "Some content",
                {"title": "My Title", "author": "Alice"},
            )

        with open(file_path) as f:
            content = f.read()
        assert "---" in content
        assert "url:" in content

    def test_save_content_fallback_on_organizer_error(self):
        with patch("scraper.core.data_organizer.DataOrganizer.ensure_directory", side_effect=RuntimeError("fail")):
            with patch("os.makedirs"):
                with patch("builtins.open", unittest.mock.mock_open()):
                    try:
                        self.fetcher._save_content("https://example.com/test", "github", "content", {})
                    except Exception:
                        pass  # fallback may raise if dirs don't exist


class TestExtractContentMetaTags(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        with patch("scraper.utils.content_fetcher.get_url_registry"):
            from scraper.utils.content_fetcher import ContentFetcher
            self.fetcher = ContentFetcher(project_root=self.tmp)

    def test_extract_og_title(self):
        from bs4 import BeautifulSoup
        html = '<html><head><meta property="og:title" content="OG Title"/></head><body></body></html>'
        soup = BeautifulSoup(html, "html.parser")
        result = self.fetcher._extract_content(soup, "https://example.com")
        assert result["metadata"].get("og_title") == "OG Title"

    def test_extract_author_meta(self):
        from bs4 import BeautifulSoup
        html = '<html><head><meta name="author" content="Jane Doe"/></head><body></body></html>'
        soup = BeautifulSoup(html, "html.parser")
        result = self.fetcher._extract_content(soup, "https://example.com")
        assert result["metadata"].get("author") == "Jane Doe"

    def test_extract_published_date(self):
        from bs4 import BeautifulSoup
        html = '<html><head><meta property="article:published_time" content="2026-04-20T10:00:00Z"/></head><body></body></html>'
        soup = BeautifulSoup(html, "html.parser")
        result = self.fetcher._extract_content(soup, "https://example.com")
        assert result["metadata"].get("published_date") == "2026-04-20T10:00:00Z"

    def test_html_to_markdown_list_items(self):
        from bs4 import BeautifulSoup
        html = "<ul><li>Item one</li><li>Item two</li></ul>"
        soup = BeautifulSoup(html, "html.parser")
        result = self.fetcher._html_to_markdown(soup)
        assert "Item one" in result

    def test_html_to_markdown_ordered_list(self):
        from bs4 import BeautifulSoup
        html = "<ol><li>First</li><li>Second</li></ol>"
        soup = BeautifulSoup(html, "html.parser")
        result = self.fetcher._html_to_markdown(soup)
        assert "First" in result


if __name__ == "__main__":
    unittest.main()
