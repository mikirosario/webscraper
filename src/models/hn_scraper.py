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

    def apply_filters(self, some_filter_criteria):
        # Apply filters to self.entries based on the criteria
        self.entries = [entry for entry in self.entries if ...]
    
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