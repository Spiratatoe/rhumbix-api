import logging
from typing import List, Dict, Optional

from src.config import BASE_URL, API_KEY
from src.utils import get_all_paginated_results

# Configure logging
logging.basicConfig(level=logging.INFO)

PICKLISTS_ENDPOINT = "/picklists/"

def get_picklists(
    page_size: Optional[int] = None,
    is_active: Optional[bool] = None,
    last_updated: Optional[str] = None,
) -> List[Dict]:
    """
    Retrieves a list of picklists from the Rhumbix API.

    Args:
        page_size (Optional[int]): Number of results to return per page.
        is_active (Optional[bool]): Filter by active status.
        last_updated (Optional[str]): Retrieve data updated after this datetime.

    Returns:
        List[Dict]: A list of picklist dictionaries.
    """
    url = f"{BASE_URL}{PICKLISTS_ENDPOINT}"
    headers = {'x-api-key': API_KEY, 'Content-Type': 'application/json'}
    params = {
        "page_size": page_size,
        "is_active": is_active,
        "last_updated": last_updated,
    }

    # Remove None values from params
    params = {k: v for k, v in params.items() if v is not None}

    results = get_all_paginated_results(url, headers, params=params)

    return results
