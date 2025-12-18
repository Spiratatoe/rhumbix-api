import logging
from typing import List, Dict, Optional

from src.config import BASE_URL, API_KEY
from src.utils import get_all_paginated_results

# Configure logging
logging.basicConfig(level=logging.INFO)

EMPLOYEE_SHIFTS_AND_BREAKS_HISTORY_ENDPOINT = "/employee_shifts_and_breaks/history/"

def get_employee_shifts_and_breaks_history(
    page_size: Optional[int] = None,
    ids: Optional[List[int]] = None,
    history_start_date: Optional[str] = None,
    history_end_date: Optional[str] = None,
    history_type: Optional[str] = None,
) -> List[Dict]:
    """
    Retrieves a list of employee shift and break history records from the Rhumbix API.

    Args:
        page_size (Optional[int]): Number of results to return per page.
        ids (Optional[List[int]]): Filter by one or more shift extra entry IDs.
        history_start_date (Optional[str]): Retrieve history from this date onwards.
        history_end_date (Optional[str]): Retrieve history up to this date.
        history_type (Optional[str]): Filter by history type (e.g., CREATED, UPDATED, DELETED).

    Returns:
        List[Dict]: A list of employee shift and break history dictionaries.
    """
    url = f"{BASE_URL}{EMPLOYEE_SHIFTS_AND_BREAKS_HISTORY_ENDPOINT}"
    headers = {'x-api-key': API_KEY, 'Content-Type': 'application/json'}
    params = {
        "page_size": page_size,
        "ids": ids,
        "history_start_date": history_start_date,
        "history_end_date": history_end_date,
        "history_type": history_type,
    }

    # Remove None values from params
    params = {k: v for k, v in params.items() if v is not None}

    results = get_all_paginated_results(url, headers, params=params)

    return results
