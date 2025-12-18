import logging
from typing import List, Dict, Optional

from src.config import BASE_URL, API_KEY
from src.utils import get_all_paginated_results

# Configure logging
logging.basicConfig(level=logging.INFO)

EMPLOYEE_SHIFT_DETAILS_ENDPOINT = "/employee_shift_details/"

def get_employee_shift_details(
    page_size: Optional[int] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    employee: Optional[str] = None,
    is_signed: Optional[bool] = None,
    last_updated: Optional[str] = None,
) -> List[Dict]:
    """
    Retrieves a list of employee shift details from the Rhumbix API.

    Args:
        page_size (Optional[int]): Number of results to return per page.
        start_date (Optional[str]): YYYY-MM-DD
        end_date (Optional[str]): YYYY-MM-DD
        employee (Optional[str]): Filter by employee.
        is_signed (Optional[bool]): Filter by signed status.
        last_updated (Optional[str]): Retrieve data updated after this datetime.

    Returns:
        List[Dict]: A list of employee shift detail dictionaries.
    """
    url = f"{BASE_URL}{EMPLOYEE_SHIFT_DETAILS_ENDPOINT}"
    headers = {'x-api-key': API_KEY, 'Content-Type': 'application/json'}
    params = {
        "page_size": page_size,
        "start_date": start_date,
        "end_date": end_date,
        "employee": employee,
        "is_signed": is_signed,
        "last_updated": last_updated,
    }

    # Remove None values from params
    params = {k: v for k, v in params.items() if v is not None}

    results = get_all_paginated_results(url, headers, params=params)

    return results