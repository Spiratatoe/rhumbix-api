import logging
from typing import List, Dict, Optional

from src.config import BASE_URL, API_KEY
from src.utils import get_all_paginated_results

# Configure logging
logging.basicConfig(level=logging.INFO)

EMPLOYEE_SHIFTS_AND_BREAKS_ENDPOINT = "/employee_shifts_and_breaks/"

def get_employee_shifts_and_breaks(
    page_size: Optional[int] = None,
    employee: Optional[str] = None,
    end_date: Optional[str] = None,
    is_approved: Optional[bool] = None,
    last_updated: Optional[str] = None,
    start_date: Optional[str] = None,
    status: Optional[str] = None,
    work_shift_keys: Optional[List[int]] = None,
    include_deleted: Optional[bool] = None,
) -> List[Dict]:
    """
    Retrieves a list of employee shifts and breaks from the Rhumbix API.

    Args:
        page_size (Optional[int]): Number of results to return per page.
        employee (Optional[str]): Filter by employee.
        end_date (Optional[str]): YYYY-MM-DD
        is_approved (Optional[bool]): Filter by approval status.
        last_updated (Optional[str]): Retrieve data updated after this datetime.
        start_date (Optional[str]): YYYY-MM-DD
        status (Optional[str]): Filter by status.
        work_shift_keys (Optional[List[int]]): Filter by work shift keys.
        include_deleted (Optional[bool]): If true, retrieve deleted records.

    Returns:
        List[Dict]: A list of employee shift and break dictionaries.
    """
    url = f"{BASE_URL}{EMPLOYEE_SHIFTS_AND_BREAKS_ENDPOINT}"
    headers = {'x-api-key': API_KEY, 'Content-Type': 'application/json'}
    params = {
        "page_size": page_size,
        "employee": employee,
        "end_date": end_date,
        "is_approved": is_approved,
        "last_updated": last_updated,
        "start_date": start_date,
        "status": status,
        "work_shift_keys": work_shift_keys,
        "include_deleted": include_deleted,
    }

    # Remove None values from params
    params = {k: v for k, v in params.items() if v is not None}

    results = get_all_paginated_results(url, headers, params=params)

    return results
