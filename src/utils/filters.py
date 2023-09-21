from typing import List
from models.models import HackerNewsEntry

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
    # Check if the input is a list of HackerNewsEntry objects
    if not _validate_hnentry_list_type(entries):
        raise TypeError("Expected a list of HackerNewsEntry, but got a different type.")

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
    # Check if the input is a list of HackerNewsEntry objects
    if not _validate_hnentry_list_type(entries):
        raise TypeError("Expected a list of HackerNewsEntry, but got a different type.")
    # Sort the list based on the comment_count attribute in descending order
    sorted_entries = sorted(entries, key=lambda x: x.comment_count, reverse=True)

    return sorted_entries

def sort_by_points(entries: List[HackerNewsEntry]) -> List[HackerNewsEntry]:
    """
    Sorts a list of HackerNewsEntry objects by their points in descending order.

    Args:
        entries (List[HackerNewsEntry]): A list of HackerNewsEntry objects.

    Returns:
        List[HackerNewsEntry]: A list of HackerNewsEntry objects sorted by points in descending order.
    """
    # Check if the input is a list of HackerNewsEntry objects
    if not _validate_hnentry_list_type(entries):
        raise TypeError("Expected a list of HackerNewsEntry, but got a different type.")

    return sorted(entries, key=lambda x: x.points, reverse=True)

def _validate_hnentry_list_type(entries: any) -> bool:
    """
    Validate if the given variable 'entries' is a list of HackerNewsEntry objects.

    Args:
        entries (Any): The variable to validate.

    Returns:
        bool: True if entries is a list of HackerNewsEntry objects, False otherwise.
    """
    if not isinstance(entries, list):
        return False

    return all(isinstance(entry, HackerNewsEntry) for entry in entries)