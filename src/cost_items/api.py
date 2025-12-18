import logging
from typing import List, Dict, Optional

from src.config import BASE_URL, API_KEY
from src.utils import get_all_paginated_results

# Configure logging
logging.basicConfig(level=logging.INFO)

COST_ITEMS_ENDPOINT = "/cost_items/"

def get_cost_items(
    page_size: Optional[int] = None,
    job_number: Optional[str] = None,
    change_order_key: Optional[str] = None,
    is_active: Optional[bool] = None,
    last_updated: Optional[str] = None,
) -> List[Dict]:
    """
    Retrieves a list of cost items from the Rhumbix API.

    Args:
        page_size (Optional[int]): Number of results to return per page.
        job_number (Optional[str]): Filter by job number.
        change_order_key (Optional[str]): Filter by change order key.
        is_active (Optional[bool]): Filter by active status.
        last_updated (Optional[str]): Retrieve data updated after this datetime.

    Returns:
        List[Dict]: A list of cost item dictionaries.
    """
    url = f"{BASE_URL}{COST_ITEMS_ENDPOINT}"
    headers = {'x-api-key': API_KEY, 'Content-Type': 'application/json'}
    params = {
        "page_size": page_size,
        "job_number": job_number,
        "change_order_key": change_order_key,
        "is_active": is_active,
        "last_updated": last_updated,
    }

    # Remove None values from params
    params = {k: v for k, v in params.items() if v is not None}

    results = get_all_paginated_results(url, headers, params=params)

    return results
