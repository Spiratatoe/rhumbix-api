import logging
from typing import List, Dict, Optional

from src.config import BASE_URL, API_KEY
from src.utils import get_all_paginated_results

# Configure logging
logging.basicConfig(level=logging.INFO)

FIELD_FOLDERS_ENDPOINT = "/field_folders/"


def get_field_folders(
    page_size: Optional[int] = None,
    project: Optional[List[int]] = None,
    created_on_from: Optional[str] = None,
    created_on_to: Optional[str] = None,
    last_updated_from: Optional[str] = None,
    last_updated_to: Optional[str] = None,
) -> List[Dict]:
    """
    Retrieves a list of field folders from the Rhumbix API.

    Args:
        page_size (Optional[int]): Number of results to return per page.
        project (Optional[List[int]]): Filter by one or more project IDs.
        created_on_from (Optional[str]): Filter for items created after this datetime.
        created_on_to (Optional[str]): Filter for items created before this datetime.
        last_updated_from (Optional[str]): Filter for items updated after this datetime.
        last_updated_to (Optional[str]): Filter for items updated before this datetime.

    Returns:
        List[Dict]: A list of field folder dictionaries.
    """
    url = f"{BASE_URL}{FIELD_FOLDERS_ENDPOINT}"
    headers = {'x-api-key': API_KEY, 'Content-Type': 'application/json'}
    params = {
        "page_size": page_size,
        "project": project,
        "created_on_from": created_on_from,
        "created_on_to": created_on_to,
        "last_updated_from": last_updated_from,
        "last_updated_to": last_updated_to,
    }

    # Remove None values from params
    params = {k: v for k, v in params.items() if v is not None}

    results = get_all_paginated_results(url, headers, params=params)

    return results
