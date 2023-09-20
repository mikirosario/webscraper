import pytest
from src.utils.filters import *
from src.models.models import HackerNewsEntry

def test_filter_by_title_length_with_mixed_list():
    """
    Test filter_by_title_length with a valid list of entries with titles longer and shorter than the word limit.
    The function should return a list of entries with titles longer than the word limit.
    """
    # Arrange
    entries = [
    HackerNewsEntry("Short title", 1, 10, 100),
    HackerNewsEntry("This is a much longer title than the previous one", 2, 20, 200),
    HackerNewsEntry("Another short title", 3, 30, 300),
    HackerNewsEntry("Yet another very long title that exceeds the five-word limit", 4, 40, 400),
    ]
    # Act
    filtered_entries = filter_by_title_length(entries, 5)

    # Assert
        # Check if the returned value is a list
    assert isinstance(filtered_entries, list), f"Expected a list, but got {type(filtered_entries)}"
    for entry in filtered_entries:
        # Check that each value in the list is a HackerNewsEntry
        assert isinstance(entry, HackerNewsEntry), f"Expected a HackerNewsEntry object, but got {type(entry)}"
        # Check that each HackerNewsEntry in the list has a title with more than 5 words
        assert len(entry.title.split()) > 5, f"Title '{entry.title}' does not exceed 5 words."
        # Check that 2 entries are returned
    assert len(filtered_entries) == 2, f"Expected 2 entries, but got {len(filtered_entries)}"

def test_filter_by_title_length_with_empty_list():
    """
    Test filter_by_title_length with an empty list.
    The function should return an empty list.
    """
    # Arrange
    entries = []

    # Act
    filtered_entries = filter_by_title_length(entries, 5)

    # Assert
    assert filtered_entries == [], "Expected an empty list when input is empty."

def test_filter_by_title_length_with_all_short_titles():
    """
    Test filter_by_title_length with a valid list of entries with titles shorter than the word limit.
    The function should return an empty list.
    """

    # Arrange
    short_entries = [
        HackerNewsEntry("Short title", 1, 10, 100),
        HackerNewsEntry("Another short title", 3, 30, 300),
        ]
    
    # Act
    filtered_entries = filter_by_title_length(short_entries, 5)

    # Assert
    assert filtered_entries == [], "Expected an empty list when all titles are short."

def test_filter_by_title_length_with_invalid_entries_type():
    """
    Test filter_by_title_length when passing in an invalid entries type.
    The function should raise a type error exception.
    """
    # Arrange
    entries = "not a list"

    # Act and Assert
    with pytest.raises(TypeError):
        filter_by_title_length(entries, 5)

def test_filter_by_title_length_with_invalid_word_limit_type():
    """
    Test filter_by_title_length when passing in an invalid word limit type.
    The function should raise a type error exception.
    """

    # Arrange
    entries = [
    HackerNewsEntry("Short title", 1, 10, 100),
    HackerNewsEntry("Another short title", 3, 30, 300),
    ]

    # Act and Assert
    with pytest.raises(TypeError):
        filter_by_title_length(entries, "not an int")

def test_filter_by_title_length_with_word_limit_less_than_one():
    """
    Test filter_by_title_length when passing in a word limit less than one.
    The result should always be an empty list regardless of the input entries.
    """
    
    # Arrange
    entries = [
        HackerNewsEntry("Some title", 1, 10, 100),
        HackerNewsEntry("This is a much longer title than the previous one", 2, 20, 200),
        ]
    
    # Act
    filtered_entries_zero = filter_by_title_length(entries, 0)
    filtered_entries_neg = filter_by_title_length(entries, -5)

    # Assert
    assert filtered_entries_zero == [], "Expected an empty list for word_limit of 0."
    assert filtered_entries_neg == [], "Expected an empty list for negative word_limit."


def test_sort_by_comments():
    # Create some mock entries
    entries = [...]
    sorted_entries = sort_by_comments(entries)
    # Add assertions based on expected order

def test_sort_by_points():
    # Create some mock entries
    entries = [...]
    sorted_entries = sort_by_points(entries)
    # Add assertions based on expected order