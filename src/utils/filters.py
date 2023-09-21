from typing import List
from src.models.models import HackerNewsEntry

from typing import List

def filter_by_title_length(entries: List[HackerNewsEntry], word_limit: int) -> List[HackerNewsEntry]:
    """
    Filters a list of HackerNewsEntry objects based on number of words in their titles.

    Args:
        entries (List[HackerNewsEntry]): A list of HackerNewsEntry objects to be filtered.
        word_limit (int): The number of words a title should exceed for the entry to be included in the result.

    Returns:
        List[HackerNewsEntry]: A list of HackerNewsEntry objects with titles exceeding the word_limit.

    Raises:
        TypeError: If entries is not a list or word_limit is not an integer.
    """
    # Check if entries is a list
    if not isinstance(entries, list):
        raise TypeError("Expected 'entries' to be a list.")

    # Check if word_limit is an integer
    if not isinstance(word_limit, int):
        raise TypeError("Expected 'word_limit' to be an integer.")

    # If word_limit is less than or equal to zero, return an empty list
    if word_limit <= 0:
        return []

    # Filter entries based on title length
    return [entry for entry in entries if len(entry.title.split()) > word_limit]

def sort_by_comments(entries: List[HackerNewsEntry]) -> List[HackerNewsEntry]:
    """
    Sorts a list of HackerNewsEntry objects based on their comment_count attribute in descending order.

    Args:
        entries (List[HackerNewsEntry]): A list of HackerNewsEntry objects to be sorted.

    Returns:
        List[HackerNewsEntry]: A sorted list of HackerNewsEntry objects.

    Raises:
        TypeError: If the input is not a list or if any element in the list is not an instance of HackerNewsEntry.
    """
    # Check if the input is a list
    if not isinstance(entries, list):
        raise TypeError("Expected a list of HackerNewsEntry, but got a different type.")

    # Check if all elements in the list are instances of HackerNewsEntry
    for entry in entries:
        if not isinstance(entry, HackerNewsEntry):
            raise TypeError("All elements in the list should be instances of HackerNewsEntry.")

    # Sort the list based on the comment_count attribute in descending order
    sorted_entries = sorted(entries, key=lambda x: x.comment_count, reverse=True)

    return sorted_entries

def sort_by_points(entries):
    {
    # ...
    }
