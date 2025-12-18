import logging
from typing import List, Dict, Optional

from src.config import BASE_URL, API_KEY
from src.utils import get_all_paginated_results

# Configure logging
logging.basicConfig(level=logging.INFO)

SHIFT_EXTRA_ENTRIES_ENDPOINT = "/shift_extra_entries/"

def get_shift_extra_entries(
    page_size: Optional[int] = None,
    job_number: Optional[str] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    is_approved: Optional[bool] = None,
    status: Optional[str] = None,
    employee: Optional[str] = None,
    last_updated: Optional[str] = None,
    is_active: Optional[bool] = None,
    work_shift_keys: Optional[List[int]] = None,
    include_deleted: Optional[bool] = None,
) -> List[Dict]:
    """
    Retrieves a list of shift extra entries from the Rhumbix API.

    Args:
        page_size (Optional[int]): Number of results to return per page.
        job_number (Optional[str]): Filter by job number.
        start_date (Optional[str]): YYYY-MM-DD
        end_date (Optional[str]): YYYY-MM-DD
        is_approved (Optional[bool]): Filter by approval status.
        status (Optional[str]): Filter by status.
        employee (Optional[str]): Filter by employee.
        last_updated (Optional[str]): Retrieve data updated after this datetime.
        is_active (Optional[bool]): Filter by active status.
        work_shift_keys (Optional[List[int]]): Filter by work shift keys.
        include_deleted (Optional[bool]): If true, retrieve deleted records.

    Returns:
        List[Dict]: A list of shift extra entry dictionaries.
    """
    url = f"{BASE_URL}{SHIFT_EXTRA_ENTRIES_ENDPOINT}"
    headers = {'x-api-key': API_KEY, 'Content-Type': 'application/json'}
    params = {
        "page_size": page_size,
        "job_number": job_number,
        "start_date": start_date,
        "end_date": end_date,
        "is_approved": is_approved,
        "status": status,
        "employee": employee,
        "last_updated": last_updated,
        "is_active": is_active,
        "work_shift_keys": work_shift_keys,
        "include_deleted": include_deleted,
    }

    # Remove None values from params
    params = {k: v for k, v in params.items() if v is not None}

    results = get_all_paginated_results(url, headers, params=params)

    return results
