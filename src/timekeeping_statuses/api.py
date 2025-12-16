import logging
from typing import List, Dict, Optional

from src.config import BASE_URL, API_KEY
from src.utils import get_all_paginated_results

# Configure logging
logging.basicConfig(level=logging.INFO)

TIMEKEEPING_STATUSES_ENDPOINT = "/timekeeping_statuses/"


def get_timekeeping_statuses(
    page_size: Optional[int] = None,
    last_updated: Optional[str] = None,
    is_active: Optional[bool] = None,
) -> List[Dict]:
    """
    Retrieves a list of timekeeping statuses from the Rhumbix API.

    Args:
        page_size (Optional[int]): Number of results to return per page.
        last_updated (Optional[str]): Retrieve data updated after this datetime.
        is_active (Optional[bool]): Filter by active status.

    Returns:
        List[Dict]: A list of timekeeping status dictionaries.
    """
    url = f"{BASE_URL}{TIMEKEEPING_STATUSES_ENDPOINT}"
    headers = {'x-api-key': API_KEY, 'Content-Type': 'application/json'}
    params = {
        "page_size": page_size,
        "last_updated": last_updated,
        "is_active": is_active,
    }

    # Remove None values from params
    params = {k: v for k, v in params.items() if v is not None}

    results = get_all_paginated_results(url, headers, params=params)

    return results
