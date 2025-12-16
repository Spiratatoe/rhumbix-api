import logging
from typing import List, Dict, Optional

from src.config import BASE_URL, API_KEY
from src.utils import get_all_paginated_results

# Configure logging
logging.basicConfig(level=logging.INFO)

EQUIPMENT_ENDPOINT = "/equipment/"


def get_equipment(
    page_size: Optional[int] = None,
    last_updated: Optional[str] = None,
    name: Optional[str] = None,
    is_active: Optional[bool] = None,
    equipment_category: Optional[List[int]] = None,
    include_deleted: Optional[bool] = None,
) -> List[Dict]:
    """
    Retrieves a list of equipment from the Rhumbix API.

    Args:
        page_size (Optional[int]): Number of results to return per page.
        last_updated (Optional[str]): Retrieve data updated after this datetime.
        name (Optional[str]): Filter by equipment name.
        is_active (Optional[bool]): Filter by active status.
        equipment_category (Optional[List[int]]): Filter by one or more equipment category IDs.
        include_deleted (Optional[bool]): If true, retrieve deleted records.

    Returns:
        List[Dict]: A list of equipment dictionaries.
    """
    url = f"{BASE_URL}{EQUIPMENT_ENDPOINT}"
    headers = {'x-api-key': API_KEY, 'Content-Type': 'application/json'}
    params = {
        "page_size": page_size,
        "last_updated": last_updated,
        "name": name,
        "is_active": is_active,
        "equipment_category": equipment_category,
        "include_deleted": include_deleted,
    }

    # Remove None values from params
    params = {k: v for k, v in params.items() if v is not None}

    results = get_all_paginated_results(url, headers, params=params)

    return results
