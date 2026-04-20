"""Tests for HackerNewsScraper._extract_data."""

import unittest

from bs4 import BeautifulSoup


def _make_hn_item(title="Test Article", url="https://example.com", item_id="12345", points="100", comments="50"):
    html = f"""
    <tr class="athing" id="{item_id}">
      <td class="titleline">
        <a href="{url}">{title}</a>
      </td>
    </tr>
    """
    subtext_html = f"""
    <tr>
      <td class="subtext">
        <span class="score" id="score_{item_id}">{points} points</span>
        <a class="hnuser">testuser</a>
        <span class="age"><a href="/item?id={item_id}">2 hours ago</a></span>
        <a href="/item?id={item_id}">{comments} comments</a>
      </td>
    </tr>
    """
    return html, subtext_html


class TestHackerNewsScraper(unittest.TestCase):
    def setUp(self):
        from scraper.scrapers.hackernews import HackerNewsScraper
        self.scraper = HackerNewsScraper(test_mode=True, test_output_dir="/tmp")

    def _make_soup_items(self, title="Test", url="https://example.com", points="100", comments="10"):
        full_html = f"""
        <table>
          <tr class="athing" id="99">
            <td class="titleline"><a href="{url}">{title}</a></td>
          </tr>
          <tr>
            <td class="subtext">
              <span class="score">_{points}_ points</span>
              <a class="hnuser">author</a>
              <span class="age"><a>3 hours ago</a></span>
              <a>{comments} comments</a>
            </td>
          </tr>
        </table>
        """
        soup = BeautifulSoup(full_html, "html.parser")
        return list(soup.find_all("tr", class_="athing"))

    def test_extract_data_basic(self):
        items = self._make_soup_items(title="HN Article", url="https://hn.com/article")
        result = self.scraper._extract_data(items)
        assert len(result) == 1
        assert result[0]["title"] == "HN Article"

    def test_extract_data_captures_url(self):
        items = self._make_soup_items(url="https://specific.com/page")
        result = self.scraper._extract_data(items)
        assert "specific.com" in result[0]["url"]

    def test_extract_data_empty_list(self):
        result = self.scraper._extract_data([])
        assert result == []

    def test_extract_data_no_next_sibling_skipped(self):
        html = '<tr class="athing" id="1"><td><a href="https://x.com">Title</a></td></tr>'
        soup = BeautifulSoup(html, "html.parser")
        items = [soup.find("tr")]
        result = self.scraper._extract_data(items)
        assert result == []

    def test_extract_data_no_subtext_skipped(self):
        full_html = """
        <table>
          <tr class="athing" id="2">
            <td class="titleline"><a href="https://x.com">Title</a></td>
          </tr>
          <tr><td>no subtext here</td></tr>
        </table>
        """
        soup = BeautifulSoup(full_html, "html.parser")
        items = list(soup.find_all("tr", class_="athing"))
        result = self.scraper._extract_data(items)
        assert result == []

    def test_extract_data_comment_count_extraction(self):
        # No span.age wrapper so a:last-child selector picks the comment link
        html = "<table><tr class=\"athing\" id=\"5\"><td class=\"titleline\"><a href=\"https://x.com\">Title</a></td></tr>"
        html += "<tr><td class=\"subtext\"><span class=\"score\">42 points</span><a class=\"hnuser\">user</a>1 hour ago<a>17 comments</a></td></tr></table>"
        soup = BeautifulSoup(html, "html.parser")
        items = list(soup.find_all("tr", class_="athing"))
        result = self.scraper._extract_data(items)
        assert len(result) == 1
        assert result[0]["comments"] == "17"

    def test_extract_data_discussion_url_contains_id(self):
        html = "<table><tr class=\"athing\" id=\"9999\"><td class=\"titleline\"><a href=\"https://x.com\">Title</a></td></tr>"
        html += "<tr><td class=\"subtext\"><span class=\"score\">10 points</span><a class=\"hnuser\">user</a>1 hour ago<a>5 comments</a></td></tr></table>"
        soup = BeautifulSoup(html, "html.parser")
        items = list(soup.find_all("tr", class_="athing"))
        result = self.scraper._extract_data(items)
        assert "9999" in result[0]["discussion_url"]

    def test_extract_data_item_exception_skipped(self):
        from unittest.mock import patch
        # Patching extract_title to raise to trigger inner except (lines 59-60)
        with patch.object(self.scraper, "extract_title", side_effect=RuntimeError("bad")):
            full_html = "<table><tr class=\"athing\" id=\"1\"><td></td></tr><tr><td class=\"subtext\"></td></tr></table>"
            soup = BeautifulSoup(full_html, "html.parser")
            items = list(soup.find_all("tr", class_="athing"))
            result = self.scraper._extract_data(items)
        assert isinstance(result, list)


if __name__ == "__main__":
    unittest.main()
