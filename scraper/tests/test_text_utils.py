"""Tests for text utility functions."""

import unittest

from scraper.utils.text_utils import clean_for_yaml, create_content_slug, normalize_whitespace


class TestNormalizeWhitespace(unittest.TestCase):
    def test_collapses_spaces(self):
        assert normalize_whitespace("hello   world") == "hello world"

    def test_collapses_newlines(self):
        assert normalize_whitespace("hello\n\nworld") == "hello world"

    def test_strips(self):
        assert normalize_whitespace("  hello  ") == "hello"

    def test_empty(self):
        assert normalize_whitespace("") == ""

    def test_none(self):
        assert normalize_whitespace(None) == ""


class TestCleanForYaml(unittest.TestCase):
    def test_truncates(self):
        result = clean_for_yaml("a" * 300, max_length=200)
        assert len(result) <= 203  # 200 + "..."
        assert result.endswith("...")

    def test_empty(self):
        assert clean_for_yaml("") == ""
        assert clean_for_yaml(None) == ""

    def test_short_string(self):
        assert clean_for_yaml("hello") == "hello"


class TestCreateContentSlug(unittest.TestCase):
    def test_simple_title(self):
        assert create_content_slug("Hello World") == "hello-world"

    def test_special_characters(self):
        assert create_content_slug("Hello! World @ 2026") == "hello-world-2026"

    def test_max_length(self):
        result = create_content_slug("a very long title " * 10, max_length=20)
        assert len(result) <= 20

    def test_no_trailing_hyphen(self):
        result = create_content_slug("hello world foo bar", max_length=11)
        assert not result.endswith("-")

    def test_empty_title_with_url(self):
        result = create_content_slug("", url="https://example.com/blog/my-article")
        assert result == "my-article"

    def test_empty_title_url_with_extension(self):
        result = create_content_slug("", url="https://example.com/page.html")
        assert result == "page"

    def test_empty_title_no_url(self):
        assert create_content_slug("") == "content"
        assert create_content_slug(None) == "content"

    def test_colons_in_title(self):
        result = create_content_slug("GitHub - anthropics/skills: Public repository")
        assert "github" in result
        assert "-" in result

    def test_unicode(self):
        result = create_content_slug("Programmer's Guide")
        assert result  # should produce something non-empty

    def test_hyphens_preserved(self):
        result = create_content_slug("my-existing-slug")
        assert result == "my-existing-slug"

    def test_multiple_spaces_collapsed(self):
        result = create_content_slug("hello    world")
        assert result == "hello-world"


if __name__ == "__main__":
    unittest.main()
