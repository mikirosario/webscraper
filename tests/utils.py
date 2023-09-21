from src.models.models import HackerNewsEntry

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
