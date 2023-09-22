import pytest
from unittest.mock import patch, Mock
from requests.exceptions import HTTPError
from tests.constants import *
from tests.utils import *
from src.models.hn_scraper import HackerNewsScraper

def test_fetch_hn_entries():
    """
    Test the fetch_hn_entries function to ensure it correctly scrapes and processes HackerNews entries.

    This test uses a mocked version of the requests.get() method to return a sample HTML snippet from the YCombinator news page.
    Therefore, the fetch_hn_entries function MUST use requests.get().content to fetch the HTML content for this test to be valid.

    The test checks:
    - The number of entries returned matches the expected number.
    - The titles of the first and last entries match expected values, assuming the entries are in the correct order.
    - The order_num, points, and comment_count attributes of each entry are non-negative, ensuring proper scraping and assignment.

    Note: This test assumes that the sample HTML structure remains consistent with the current version of the YCombinator news page.
    If the structure of the YCombinator news page changes, this test may fail and the sample HTML (and possibly the scraper logic) will need to be updated.
    This test also assumes that fetch_hn_entries is called by the HackerNewsScraper class constructor on instantiation.
    """
    # Arrange
    mock_html_content = get_mocked_hn_html()
    expected_num_entries = MOCK_HTML_HN_ENTRIES_NUM_TO_FETCH
    
    # Mock HTTP request
    mock_response = Mock()
    mock_response.content = mock_html_content
    mock_response.raise_for_status.return_value = None
    with patch('src.models.hn_scraper.requests.get', return_value=mock_response):
        # Act
        HackerNewsScraper._instance = None
        scraper = HackerNewsScraper(max_entries=expected_num_entries)
        entries = scraper.entries

    # Assert
    assert validate_hnentry_list_type(entries), "Expected a list of HackerNewsEntry objects."
    assert len(entries) == expected_num_entries, f"Expected {expected_num_entries} entries, but got {len(entries)}"
    for i, (actual_entry, expected_entry) in enumerate(zip(entries, MOCK_HTML_EXPECTED_RETURN_VALUE)):
        assert actual_entry == expected_entry, f"Entry at index {i} does not match expected value. Got {actual_entry}, expected {expected_entry}"

def test_fetch_hn_entries_http_error():
    """
    Test fetch_hn_entries when an HTTP error occurs.
    The function should handle the error and not crash.
    Note: This test assumes that fetch_hn_entries is called by the HackerNewsScraper class constructor on instantiation.
    """
    # Arrange
    expected_num_entries = MOCK_HTML_HN_ENTRIES_NUM_TO_FETCH

    # Mock the requests.get method to raise an HTTPError
    with patch('src.models.hn_scraper.requests.get', side_effect=HTTPError("Mocked HTTP Error")):
        HackerNewsScraper._instance = None
        try:
            # Act
            HackerNewsScraper(max_entries=expected_num_entries)
        # Assert
        except HTTPError:
            pytest.fail("The method did not handle the HTTPError.")