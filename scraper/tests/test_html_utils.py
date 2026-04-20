"""Tests for HTML utility functions."""

import unittest

from bs4 import BeautifulSoup

from scraper.utils.html_utils import (
    create_soup,
    remove_unwanted_elements,
    safe_get_attribute,
    safe_get_text,
    select_elements,
    select_one_element,
)


class TestCreateSoup(unittest.TestCase):
    def test_valid_html(self):
        soup = create_soup("<html><body><p>Hello</p></body></html>")
        assert soup is not None
        assert soup.find("p").get_text() == "Hello"

    def test_empty_string(self):
        assert create_soup("") is None

    def test_none_input(self):
        assert create_soup(None) is None

    def test_returns_beautifulsoup(self):
        soup = create_soup("<p>test</p>")
        assert isinstance(soup, BeautifulSoup)

    def test_custom_parser(self):
        soup = create_soup("<p>hello</p>", parser="html.parser")
        assert soup is not None


class TestSelectElements(unittest.TestCase):
    def setUp(self):
        self.soup = BeautifulSoup('<div class="item"><p>A</p><p>B</p></div>', "html.parser")

    def test_finds_elements(self):
        elements = select_elements(self.soup, "p")
        assert len(elements) == 2

    def test_no_match(self):
        elements = select_elements(self.soup, "h1")
        assert elements == []

    def test_none_soup(self):
        assert select_elements(None, "p") == []

    def test_class_selector(self):
        elements = select_elements(self.soup, ".item")
        assert len(elements) == 1


class TestSelectOneElement(unittest.TestCase):
    def setUp(self):
        self.soup = BeautifulSoup("<div><p>First</p><p>Second</p></div>", "html.parser")

    def test_finds_first(self):
        el = select_one_element(self.soup, "p")
        assert el is not None
        assert el.get_text() == "First"

    def test_no_match_returns_none(self):
        assert select_one_element(self.soup, "h1") is None

    def test_none_soup_returns_none(self):
        assert select_one_element(None, "p") is None


class TestSafeGetText(unittest.TestCase):
    def setUp(self):
        self.soup = BeautifulSoup("<p>  Hello World  </p>", "html.parser")
        self.el = self.soup.find("p")

    def test_extracts_text(self):
        assert safe_get_text(self.el) == "Hello World"

    def test_strips_whitespace(self):
        assert "  " not in safe_get_text(self.el)

    def test_no_strip(self):
        result = safe_get_text(self.el, strip=False)
        assert "  " in result

    def test_none_element(self):
        assert safe_get_text(None) == ""

    def test_none_element_custom_default(self):
        assert safe_get_text(None, default="n/a") == "n/a"

    def test_empty_element(self):
        soup = BeautifulSoup("<p></p>", "html.parser")
        el = soup.find("p")
        assert safe_get_text(el) == ""


class TestSafeGetAttribute(unittest.TestCase):
    def setUp(self):
        self.soup = BeautifulSoup('<a href="https://example.com" class="link">text</a>', "html.parser")
        self.el = self.soup.find("a")

    def test_gets_href(self):
        assert safe_get_attribute(self.el, "href") == "https://example.com"

    def test_gets_class(self):
        result = safe_get_attribute(self.el, "class")
        assert "link" in result

    def test_missing_attribute(self):
        assert safe_get_attribute(self.el, "data-missing") == ""

    def test_missing_attribute_custom_default(self):
        assert safe_get_attribute(self.el, "data-missing", default="none") == "none"

    def test_none_element(self):
        assert safe_get_attribute(None, "href") == ""


class TestRemoveUnwantedElements(unittest.TestCase):
    def test_removes_script(self):
        soup = BeautifulSoup("<div><p>Keep</p><script>evil()</script></div>", "html.parser")
        result = remove_unwanted_elements(soup)
        assert result.find("script") is None
        assert result.find("p") is not None

    def test_removes_nav(self):
        soup = BeautifulSoup("<div><nav>menu</nav><p>content</p></div>", "html.parser")
        result = remove_unwanted_elements(soup)
        assert result.find("nav") is None

    def test_removes_by_class(self):
        soup = BeautifulSoup('<div><div class="ads">ad</div><p>content</p></div>', "html.parser")
        result = remove_unwanted_elements(soup)
        assert result.find(class_="ads") is None

    def test_custom_tags(self):
        soup = BeautifulSoup("<div><span>remove</span><p>keep</p></div>", "html.parser")
        result = remove_unwanted_elements(soup, tags_to_remove=["span"], classes_to_remove=[])
        assert result.find("span") is None
        assert result.find("p") is not None

    def test_none_soup_returns_none(self):
        assert remove_unwanted_elements(None) is None


class TestExceptionPaths(unittest.TestCase):
    """Cover exception-handler branches in html_utils."""

    def test_create_soup_exception_returns_none(self):
        from unittest.mock import patch
        with patch("scraper.utils.html_utils.BeautifulSoup", side_effect=Exception("parse error")):
            result = create_soup("<html>test</html>")
        assert result is None

    def test_select_elements_exception_returns_empty(self):
        from unittest.mock import MagicMock
        soup = MagicMock()
        soup.select.side_effect = Exception("select error")
        result = select_elements(soup, "div")
        assert result == []

    def test_select_one_element_exception_returns_none(self):
        from unittest.mock import MagicMock
        soup = MagicMock()
        soup.select_one.side_effect = Exception("select error")
        result = select_one_element(soup, "div")
        assert result is None

    def test_safe_get_text_exception_returns_default(self):
        from unittest.mock import MagicMock
        el = MagicMock()
        el.get_text.side_effect = Exception("text error")
        result = safe_get_text(el, default="fallback")
        assert result == "fallback"

    def test_safe_get_attribute_exception_returns_default(self):
        from unittest.mock import MagicMock
        el = MagicMock()
        el.has_attr.side_effect = Exception("attr error")
        result = safe_get_attribute(el, "href", default="none")
        assert result == "none"

    def test_remove_unwanted_elements_exception_returns_soup(self):
        from unittest.mock import MagicMock
        soup = MagicMock()
        soup.find_all.side_effect = Exception("find_all error")
        result = remove_unwanted_elements(soup)
        assert result is soup


if __name__ == "__main__":
    unittest.main()
