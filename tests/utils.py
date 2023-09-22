import os
from pathlib import Path
from tests.constants import MOCK_HTML_FILE_RELATIVE_PATH
from src.models.hn_entry import HackerNewsEntry

# Auxiliary Functions
def validate_hnentry_list_type(entries: any) -> bool:
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

def get_mocked_hn_html() -> str:
    current_file_dir = Path(os.path.dirname(os.path.abspath(__file__)))
    mock_file_path = current_file_dir / MOCK_HTML_FILE_RELATIVE_PATH
    with open(mock_file_path, "r", encoding="utf-8") as file:
        return file.read()
