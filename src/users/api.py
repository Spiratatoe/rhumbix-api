import logging
from typing import List, Dict, Optional

from src.config import BASE_URL, API_KEY
from src.utils import get_all_paginated_results

# Configure logging
logging.basicConfig(level=logging.INFO)

USERS_ENDPOINT = "/users/"


def get_users(
    page_size: Optional[int] = None,
    last_updated: Optional[str] = None,
    email: Optional[str] = None,
) -> List[Dict]:
    """
    Retrieves a list of users from the Rhumbix API.

    Args:
        page_size (Optional[int]): Number of results to return per page.
        last_updated (Optional[str]): Retrieve data updated after this datetime.
        email (Optional[str]): Filter by user email address.

    Returns:
        List[Dict]: A list of user dictionaries.
    """
    url = f"{BASE_URL}{USERS_ENDPOINT}"
    headers = {'x-api-key': API_KEY, 'Content-Type': 'application/json'}
    params = {
        "page_size": page_size,
        "last_updated": last_updated,
        "email": email,
    }

    # Remove None values from params
    params = {k: v for k, v in params.items() if v is not None}

    results = get_all_paginated_results(url, headers, params=params)

    return results
