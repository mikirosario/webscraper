import pytest
from unittest.mock import patch, Mock
from src.models.hn_entry import HackerNewsEntry
from src.models.hn_scraper import HackerNewsScraper
from tests.constants import MOCK_HTML_HN_ENTRIES_NUM_TO_FETCH
from tests.utils import *

# Mock HTTP request
mock_html_content = get_mocked_hn_html()
expected_num_entries = MOCK_HTML_HN_ENTRIES_NUM_TO_FETCH
mock_response = Mock()
mock_response.content = mock_html_content
mock_response.raise_for_status.return_value = None
with patch('src.models.hn_scraper.requests.get', return_value=mock_response):
    # Act
    HackerNewsScraper._instance = None
    scraper = HackerNewsScraper(max_entries=expected_num_entries)

def test_filter_by_min_title_length_with_mixed_list():
    """
    Test filter_by_min_title_length with a valid list of entries with titles longer and shorter than the word limit.
    The function should return a list of entries with titles longer than the word limit.
    """
    # Arrange
    scraper.entries = [
    HackerNewsEntry("Short title", 1, 10, 100),
    HackerNewsEntry("This is a much longer title than the previous one", 2, 20, 200),
    HackerNewsEntry("Another short title", 3, 30, 300),
    HackerNewsEntry("Yet another very long title that exceeds the five-word limit", 4, 40, 400),
    ]
    # Act
    scraper.filter_by_min_title_length(5)

    # Assert
        # Check that filtered_entries is a list of HackerNewsEntry objects
    assert validate_hnentry_list_type(scraper.entries), "Expected a list of HackerNewsEntry objects."
        # Check that each HackerNewsEntry in the list has a title with more than 5 words
    for entry in scraper.entries:
        assert len(entry.title.split()) > 5, f"Title '{entry.title}' does not exceed 5 words."
        # Check that 2 entries are returned
    assert len(scraper.entries) == 2, f"Expected 2 entries, but got {len(scraper.entries)}"

def test_filter_by_min_title_length_with_empty_list():
    """
    Test filter_by_min_title_length with an empty list.
    The function should return an empty list.
    """
    # Arrange
    scraper.entries = []

    # Act
    scraper.filter_by_min_title_length(5)

    # Assert
    assert scraper.entries == [], "Expected an empty list when input is empty."

def test_filter_by_min_title_length_with_all_short_titles():
    """
    Test filter_by_min_title_length with a valid list of entries with titles shorter than the word limit.
    The function should return an empty list.
    """

    # Arrange
    scraper.entries = [
        HackerNewsEntry("Short title", 1, 10, 100),
        HackerNewsEntry("Another short title", 3, 30, 300),
        ]
    
    # Act
    scraper.filter_by_min_title_length(5)

    # Assert
    assert scraper.entries == [], "Expected an empty list when all titles are short."

def test_filter_by_min_title_length_with_invalid_entries_type():
    """
    Test filter_by_min_title_length when passing in an invalid entries type.
    The function should raise a type error exception.
    """
    # Arrange
    scraper.entries = "not a list"

    # Act and Assert
    with pytest.raises(TypeError):
        scraper.filter_by_min_title_length(5)

def test_filter_by_min_title_length_with_invalid_word_limit_type():
    """
    Test filter_by_min_title_length when passing in an invalid word limit type.
    The function should raise a type error exception.
    """

    # Arrange
    scraper.entries = [
    HackerNewsEntry("Short title", 1, 10, 100),
    HackerNewsEntry("Another short title", 3, 30, 300),
    ]

    # Act and Assert
    with pytest.raises(TypeError):
        scraper.filter_by_min_title_length("not an int")

def test_filter_by_min_title_length_with_word_limit_zero():
    """
    Test filter_by_min_title_length when passing in a word limit of zero.
    The result should always be an empty list regardless of the input entries.
    """
    
    # Arrange
    scraper.entries = [
        HackerNewsEntry("Some title", 1, 10, 100),
        HackerNewsEntry("This is a much longer title than the previous one", 2, 20, 200),
        ]
    
    # Act
    scraper.filter_by_min_title_length(0)

    # Assert
    assert scraper.entries == [], "Expected an empty list for word_limit of 0."

def test_filter_by_min_title_length_with_word_limit_neg_number():
    """
    Test filter_by_min_title_length when passing in a word limit less than one.
    The result should always be an empty list regardless of the input entries.
    """
    
    # Arrange
    scraper.entries = [
        HackerNewsEntry("Some title", 1, 10, 100),
        HackerNewsEntry("This is a much longer title than the previous one", 2, 20, 200),
        ]
    
    # Act
    scraper.filter_by_min_title_length(-5)

    # Assert
    assert scraper.entries == [], "Expected an empty list for word_limit of less than 0."

def test_filter_by_max_title_length_with_mixed_list():
    """
    Test filter_by_max_title_length with a valid list of entries with titles longer and shorter than the word limit.
    The function should return a list of entries with titles shorter than or equal to the word limit.
    """

    # Arrange
    scraper.entries = [
        HackerNewsEntry("Short title", 1, 10, 100),
        HackerNewsEntry("This is a much longer title than the previous one", 2, 20, 200),
        HackerNewsEntry("Another short title", 3, 30, 300),
        HackerNewsEntry("Yet another very long title that exceeds the five-word limit", 4, 40, 400),
        HackerNewsEntry("Word count equals limit here", 5, 50, 500)
    ]
    # Act
    scraper.filter_by_max_title_length(5)

    # Assert
    # Check that filtered_entries is a list of HackerNewsEntry objects
    assert validate_hnentry_list_type(scraper.entries), "Expected a list of HackerNewsEntry objects."
    # Check that each HackerNewsEntry in the list has a title with 5 or fewer words
    for entry in scraper.entries:
        assert len(entry.title.split()) <= 5, f"Title '{entry.title}' exceeds 5 words."
    # Check that 3 entries are returned
    assert len(scraper.entries) == 3, f"Expected 3 entries, but got {len(scraper.entries)}"

def test_filter_by_max_title_length_with_empty_list():
    """
    Test filter_by_max_title_length with an empty list.
    The function should return an empty list.
    """
    # Arrange
    scraper.entries = []

    # Act
    scraper.filter_by_max_title_length(5)

    # Assert
    assert scraper.entries == [], "Expected an empty list when input is empty."

def test_filter_by_max_title_length_with_all_long_titles():
    """
    Test filter_by_min_title_length with a valid list of entries with titles longer than the word limit.
    The function should return an empty list.
    """

    # Arrange
    scraper.entries = [
        HackerNewsEntry("Title with word count exceeding limit", 1, 10, 100),
        HackerNewsEntry("Another title that is longer than the limit", 3, 30, 300),
        ]
    
    # Act
    scraper.filter_by_max_title_length(5)

    # Assert
    assert scraper.entries == [], "Expected an empty list when all titles are short."

def test_filter_by_max_title_length_with_invalid_entries_type():
    """
    Test filter_by_max_title_length when passing in an invalid entries type.
    The function should raise a type error exception.
    """
    # Arrange
    scraper.entries = "not a list"

    # Act and Assert
    with pytest.raises(TypeError):
        scraper.filter_by_max_title_length(5)

def test_filter_by_max_title_length_with_invalid_word_limit_type():
    """
    Test filter_by_max_title_length when passing in an invalid word limit type.
    The function should raise a type error exception.
    """

    # Arrange
    scraper.entries = [
    HackerNewsEntry("Short title", 1, 10, 100),
    HackerNewsEntry("Another short title", 3, 30, 300),
    ]

    # Act and Assert
    with pytest.raises(TypeError):
        scraper.filter_by_max_title_length("not an int")

def test_filter_by_max_title_length_with_word_limit_zero():
    """
    Test filter_by_max_title_length when passing in a word limit of zero.
    The result should always be an empty list regardless of the input entries.
    """
    
    # Arrange
    scraper.entries = [
        HackerNewsEntry("Some title", 1, 10, 100),
        HackerNewsEntry("This is a much longer title than the previous one", 2, 20, 200),
        ]
    
    # Act
    scraper.filter_by_max_title_length(0)

    # Assert
    assert scraper.entries == [], "Expected an empty list for word_limit of 0."

def test_filter_by_max_title_length_with_word_limit_neg_number():
    """
    Test filter_by_max_title_length when passing in a word limit less than one.
    The result should always be an empty list regardless of the input entries.
    """
    
    # Arrange
    scraper.entries = [
        HackerNewsEntry("Some title", 1, 10, 100),
        HackerNewsEntry("This is a much longer title than the previous one", 2, 20, 200),
        ]
    
    # Act
    scraper.filter_by_max_title_length(-5)

    # Assert
    assert scraper.entries == [], "Expected an empty list for word_limit of less than 0."

def test_sort_by_comments_basic():
    """
    Test sort_by_comments with a valid list of entries.
    The function should return a list sorted by the number of comments in descending order.
    """
    # Arrange
    scraper.entries = [
        HackerNewsEntry("Title A", 1, 10, 100),
        HackerNewsEntry("Title B", 2, 50, 200),
        HackerNewsEntry("Title C", 3, 30, 300),
    ]
    expected_comment_count_order = [50, 30, 10]
    
    # Act
    scraper.sort_by_comments()

    # Assert
        # Check that sorted_entries is a list of HackerNewsEntry objects
    assert validate_hnentry_list_type(scraper.entries), "Expected a list of HackerNewsEntry objects."
    assert [entry.comment_count for entry in scraper.entries] == expected_comment_count_order

def test_sort_by_comments_empty_list():
    """
    Test sort_by_comments with an empty list.
    The function should return an empty list.
    """
    # Arrange
    scraper.entries = []

    # Act
    scraper.sort_by_comments()

    # Assert
    assert scraper.entries == []

def test_sort_by_comments_tiebreaker():
    """
    Test sort_by_comments with entries having the same comment count.
    The function should maintain the original order of the entries (stable sort).
    """
    # Arrange
    scraper.entries = [
        HackerNewsEntry("Title A", 1, 10, 100),
        HackerNewsEntry("Title B", 2, 10, 200),
    ]
    
    # Act
    scraper.sort_by_comments()

    # Assert
    assert [entry.title for entry in scraper.entries] == ["Title A", "Title B"]

def test_sort_by_comments_invalid_input():
    """
    Test sort_by_comments with invalid input.
    The function should raise a TypeError.
    """
    # Arrange
    scraper.entries = "not a list of HackerNewsEntry"

    # Act and Assert
    with pytest.raises(TypeError):
        scraper.sort_by_comments()
    
    # Arrange
    scraper.entries = ["not a HackerNewsEntry", "also not a HackerNewsEntry"]

    # Act and Assert
    with pytest.raises(TypeError):
        scraper.sort_by_comments()

def test_sort_by_points_basic():
    """
    Test sort_by_points with a valid list of entries.
    The function should return a list sorted by the number of points in descending order.
    """
    # Arrange
    scraper.entries = [
        HackerNewsEntry("Title A", 1, 10, 100),
        HackerNewsEntry("Title B", 2, 20, 300),
        HackerNewsEntry("Title C", 3, 30, 200),
    ]
    expected_points_order = [300, 200, 100]
    
    # Act
    scraper.sort_by_points()

    # Assert
        # Check that sorted_entries is a list of HackerNewsEntry objects
    assert validate_hnentry_list_type(scraper.entries), "Expected a list of HackerNewsEntry objects."
        # Check that each entry's comment_count matches the expected order
    assert [entry.points for entry in scraper.entries] == expected_points_order

def test_sort_by_points_empty_list():
    """
    Test sort_by_points with an empty list.
    The function should return an empty list.
    """
    # Arrange
    scraper.entries = []

    # Act
    scraper.sort_by_points()

    # Assert
    assert scraper.entries == []

def test_sort_by_points_tiebreaker():
    """
    Test sort_by_points with entries having the same points.
    The function should maintain the original order of the entries (stable sort).
    """
    # Arrange
    scraper.entries = [
        HackerNewsEntry("Title A", 1, 10, 100),
        HackerNewsEntry("Title B", 2, 20, 100),
    ]
    
    # Act
    scraper.sort_by_points()

    # Assert
    assert [entry.title for entry in scraper.entries] == ["Title A", "Title B"]

def test_sort_by_points_invalid_input():
    """
    Test sort_by_points with invalid input.
    The function should raise a TypeError.
    """
    # Arrange
    scraper.entries = "not a list of HackerNewsEntry"

    # Act and Assert
    with pytest.raises(TypeError):
        scraper.sort_by_points()

    # Arrange
    scraper.entries = ["not a HackerNewsEntry", "also not a HackerNewsEntry"]

    # Act and Assert
    with pytest.raises(TypeError):
        scraper.sort_by_points()
