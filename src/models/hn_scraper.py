import requests
import datetime
from typing import List
from bs4 import BeautifulSoup
from src.constants import *
from src.models.hn_entry import HackerNewsEntry
from src.utils.log_config import setup_logger

logger = setup_logger(__name__)

class HackerNewsScraper:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(HackerNewsScraper, cls).__new__(cls)
        return cls._instance

    def __init__(self, max_entries: int = HN_MAX_ENTRIES):
        self.last_fetch_time = datetime.datetime.min
        self.fetch_hn_entries(max_entries)

    def fetch_hn_entries(self, max_entries: int) -> None:
        """
        Fetches up to the specified number of entries from the YCombinator news page.

        Args:
            max_entries (int): The number of entries to fetch.

        Returns:
            list[HackerNewsEntry]: A list of HackerNewsEntry objects.
        """
        # # Check time difference
        # time_diff = datetime.datetime.now() - self.last_fetch_time
        # if time_diff.seconds < HN_FETCH_DELAY:
        #     logger.warning(f"Please wait for {HN_FETCH_DELAY - time_diff.seconds} seconds before fetching again.")
        #     return None

        # Fetch the HTML content
        response = requests.get(HN_URL, HN_HTTP_REQUEST_HEADER)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        title_containers = soup.find_all(HN_ENTRY_START_TAG, class_=HN_ENTRY_START_CLASS, limit=max_entries)
        
        # TODO: This is functional, but it would be better to have some indication
        # in constants.py of underlying HTML structure after each row to make it
        # more resilient to changes. Consider some refactoring.
        self.entries = []
        for container in title_containers:
            title: str | None = self._extract_title(container)
            order_num: int | None = self._extract_order_num(container)
            comment_count: int | None = None
            points: int | None = None
            subtext_container = container.find_next_sibling('tr').find('td', class_='subtext')
            if subtext_container:
                comment_count = self._extract_comment_count(subtext_container)
                points = self._extract_points(subtext_container)
            entry = HackerNewsEntry(title=title, order_num=order_num, comment_count=comment_count, points=points)
            self.entries.append(entry)
        self.last_fetch_time = datetime.datetime.now()

    def filter_by_title_length(self, word_limit: int) -> None:
        """
        Filters entries based on number of words in their titles.

        Args:
            word_limit (int): The number of words a title should exceed for the entry to be included in the result.

        Raises:
            TypeError: If entries is not a list or word_limit is not an integer.
        """
        # Check if the input is a list of HackerNewsEntry objects
        if not self._validate_hnentry_list_type(self.entries):
            raise TypeError("Expected a list of HackerNewsEntry, but got a different type.")

        # Check if word_limit is an integer
        if not isinstance(word_limit, int):
            raise TypeError("Expected 'word_limit' to be an integer.")

        # If word_limit is less than or equal to zero, return an empty list
        if word_limit <= 0:
            self.entries = []
        # Filter entries based on title length
        self.entries = [entry for entry in self.entries if len(entry.title.split()) > word_limit]

    def sort_by_comments(self) -> None:
        """
        Sorts entries based on their comment_count attribute in descending order.

        Args:
            None.

        Raises:
            TypeError: If the input is not a list or if any element in the list is not an instance of HackerNewsEntry.
        """
        # Check if the input is a list of HackerNewsEntry objects
        if not self._validate_hnentry_list_type(self.entries):
            raise TypeError("Expected a list of HackerNewsEntry, but got a different type.")
        # Sort the entries based on the comment_count attribute in descending order
        self.entries = sorted(self.entries, key=lambda x: x.comment_count, reverse=True)

    def sort_by_points(self) -> None:
        """
        Sorts entries by their points in descending order.
        """
        # Check if the input is a list of HackerNewsEntry objects
        if not self._validate_hnentry_list_type(self.entries):
            raise TypeError("Expected a list of HackerNewsEntry, but got a different type.")
        # Sort the entries based on points attribute in descending order
        self.entries = sorted(self.entries, key=lambda x: x.points, reverse=True)

    @staticmethod
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
    
    @staticmethod
    def _extract_numeric_chars(s: str) -> str:
        return ''.join(filter(str.isdigit, s))

    @staticmethod
    def _extract_title(container) -> str | None:
        title_container = container.find(HN_TITLE_TAG, class_=HN_TITLE_CLASS)
        return title_container.a.text if title_container and title_container.a else None

    @staticmethod
    def _extract_order_num(container) -> int | None:
        order_num_container = container.find(HN_ORDER_NUM_TAG, class_=HN_ORDER_NUM_CLASS)
        if order_num_container and any(char.isdigit() for char in order_num_container.text):
            return int(HackerNewsScraper._extract_numeric_chars(order_num_container.text))
        return None

    @staticmethod
    def _extract_comment_count(container) -> int | None:
        a_containers = container.find_all(HN_COMMENT_COUNT_TAG)
        for container in a_containers:
            if 'comment' in container.text and any(char.isdigit() for char in container.text):
                return int(HackerNewsScraper._extract_numeric_chars(container.text))
        return 0

    @staticmethod
    def _extract_points(container) -> int | None:
        points_container = container.find('span', class_='score')
        if points_container and any(char.isdigit() for char in points_container.text):
            return int(HackerNewsScraper._extract_numeric_chars(points_container.text))
        return None