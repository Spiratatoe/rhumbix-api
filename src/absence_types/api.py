import logging
from typing import List, Dict, Optional

from src.config import BASE_URL, API_KEY
from src.utils import get_all_paginated_results

# Configure logging
logging.basicConfig(level=logging.INFO)

ABSENCE_TYPES_ENDPOINT = "/absence_types/"


def get_absence_types(page_size: Optional[int] = None) -> List[Dict]:
    """
    Retrieves a list of absence types from the Rhumbix API.

    Args:
        page_size (Optional[int]): Number of results to return per page.

    Returns:
        List[Dict]: A list of dictionaries, where each dictionary contains
                    the details for an absence type. Returns an empty list on error.

    Example Output:
        [
            {
                "name": "Sick",
                "code": "S",
                "is_active": true,
                "created_by": "GREATCO-ADMIN-12"
            }
        ]
    """
    url = f"{BASE_URL}{ABSENCE_TYPES_ENDPOINT}"
    headers = {'x-api-key': API_KEY, 'Content-Type': 'application/json'}
    params = {}
    if page_size:
        params["page_size"] = page_size

    results = get_all_paginated_results(url, headers, params=params)

    return results
