import logging
from typing import List, Dict, Optional

from src.config import BASE_URL, API_KEY
from src.utils import get_all_paginated_results

# Configure logging
logging.basicConfig(level=logging.INFO)

TIMEKEEPING_ENTRIES_ENDPOINT = "/timekeeping_entries/"

def get_timekeeping_entries(
    page_size: Optional[int] = None,
    job_number: Optional[str] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    is_approved: Optional[bool] = None,
    status: Optional[str] = None,
    employee: Optional[str] = None,
    foreman: Optional[str] = None,
    last_updated: Optional[str] = None,
    include_deleted: Optional[bool] = None,
) -> List[Dict]:
    """
    Retrieves a list of timekeeping entries from the Rhumbix API.

    Args:
        page_size (Optional[int]): Number of results to return per page.
        job_number (Optional[str]): Filter by job number.
        start_date (Optional[str]): YYYY-MM-DD
        end_date (Optional[str]): YYYY-MM-DD
        is_approved (Optional[bool]): Filter by approval status.
        status (Optional[str]): Filter by status.
        employee (Optional[str]): Filter by employee.
        foreman (Optional[str]): Filter by foreman.
        last_updated (Optional[str]): Retrieve data updated after this datetime.
        include_deleted (Optional[bool]): If true, retrieve deleted records.

    Returns:
        List[Dict]: A list of timekeeping entry dictionaries.
    """
    url = f"{BASE_URL}{TIMEKEEPING_ENTRIES_ENDPOINT}"
    headers = {'x-api-key': API_KEY, 'Content-Type': 'application/json'}
    params = {
        "page_size": page_size,
        "job_number": job_number,
        "start_date": start_date,
        "end_date": end_date,
        "is_approved": is_approved,
        "status": status,
        "employee": employee,
        "foreman": foreman,
        "last_updated": last_updated,
        "include_deleted": include_deleted,
    }

    # Remove None values from params
    params = {k: v for k, v in params.items() if v is not None}

    results = get_all_paginated_results(url, headers, params=params)

    return results
