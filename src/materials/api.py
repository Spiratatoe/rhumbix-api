import logging
from typing import List, Dict, Optional

from src.config import BASE_URL, API_KEY
from src.utils import get_all_paginated_results

# Configure logging
logging.basicConfig(level=logging.INFO)

MATERIALS_ENDPOINT = "/materials/"

def get_materials(
    page_size: Optional[int] = None,
    last_updated: Optional[str] = None,
    is_active: Optional[bool] = None,
) -> List[Dict]:
    """
    Retrieves a list of materials from the Rhumbix API.

    Args:
        page_size (Optional[int]): Number of results to return per page.
        last_updated (Optional[str]): Retrieve data updated after this datetime.
        is_active (Optional[bool]): Filter by active status.

    Returns:
        List[Dict]: A list of material dictionaries.
    """
    url = f"{BASE_URL}{MATERIALS_ENDPOINT}"
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
