import logging
from typing import List, Dict, Optional

from src.config import BASE_URL, API_KEY
from src.utils import get_all_paginated_results

# Configure logging
logging.basicConfig(level=logging.INFO)

GROUPS_ENDPOINT = "/groups/"


def get_groups(
    page_size: Optional[int] = None,
    name: Optional[str] = None,
    last_updated: Optional[str] = None,
    include_deleted: Optional[bool] = None,
) -> List[Dict]:
    """
    Retrieves a list of groups from the Rhumbix API.

    Args:
        page_size (Optional[int]): Number of results to return per page.
        name (Optional[str]): Filter by group name.
        last_updated (Optional[str]): Retrieve data updated after this datetime.
        include_deleted (Optional[bool]): If true, retrieve deleted records.

    Returns:
        List[Dict]: A list of group dictionaries.
    """
    url = f"{BASE_URL}{GROUPS_ENDPOINT}"
    headers = {'x-api-key': API_KEY, 'Content-Type': 'application/json'}
    params = {
        "page_size": page_size,
        "name": name,
        "last_updated": last_updated,
        "include_deleted": include_deleted,
    }

    # Remove None values from params
    params = {k: v for k, v in params.items() if v is not None}

    results = get_all_paginated_results(url, headers, params=params)

    return results
