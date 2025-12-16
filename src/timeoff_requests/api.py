import logging
from typing import List, Dict, Optional

from src.config import BASE_URL, API_KEY
from src.utils import get_all_paginated_results

# Configure logging
logging.basicConfig(level=logging.INFO)

TIMEOFF_REQUESTS_ENDPOINT = "/timeoff_requests/"


def get_timeoff_requests(
    page_size: Optional[int] = None,
    last_updated: Optional[str] = None,
    is_active: Optional[bool] = None,
    employee: Optional[List[str]] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    include_deleted: Optional[bool] = None,
) -> List[Dict]:
    """
    Retrieves a list of time off requests from the Rhumbix API.

    Args:
        page_size (Optional[int]): Number of results to return per page.
        last_updated (Optional[str]): Retrieve data updated after this datetime.
        is_active (Optional[bool]): Filter by active status.
        employee (Optional[List[str]]): Filter by one or more employee company-supplied IDs.
        start_date (Optional[str]): Retrieve requests from a specific start date in YYYY-MM-DD format.
        end_date (Optional[str]): Retrieve requests up to and including this end date in YYYY-MM-DD format.
        include_deleted (Optional[bool]): If true, retrieve deleted records.

    Returns:
        List[Dict]: A list of time off request dictionaries.
    """
    url = f"{BASE_URL}{TIMEOFF_REQUESTS_ENDPOINT}"
    headers = {'x-api-key': API_KEY, 'Content-Type': 'application/json'}
    params = {
        "page_size": page_size,
        "last_updated": last_updated,
        "is_active": is_active,
        "employee": employee,
        "start_date": start_date,
        "end_date": end_date,
        "include_deleted": include_deleted,
    }

    # Remove None values from params
    params = {k: v for k, v in params.items() if v is not None}

    results = get_all_paginated_results(url, headers, params=params)

    return results
