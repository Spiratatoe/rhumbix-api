import logging
from typing import List, Dict, Optional

from src.config import BASE_URL, API_KEY
from src.utils import get_all_paginated_results

# Configure logging
logging.basicConfig(level=logging.INFO)

EMPLOYEES_ENDPOINT = "/employees/"


def get_employees(
    page_size: Optional[int] = None,
    last_updated: Optional[str] = None,
    is_active: Optional[bool] = None,
    company_supplied_id: Optional[List[str]] = None,
    group_id: Optional[List[int]] = None,
    include_subgroups: Optional[bool] = None,
    email_address: Optional[str] = None,
    phone_number: Optional[str] = None,
    include_deleted: Optional[bool] = None,
) -> List[Dict]:
    """
    Retrieves a list of employees from the Rhumbix API.

    Args:
        page_size (Optional[int]): Number of results to return per page.
        last_updated (Optional[str]): Retrieve data updated after this datetime.
        is_active (Optional[bool]): Filter by active status.
        company_supplied_id (Optional[List[str]]): Filter by one or more company-supplied IDs.
        group_id (Optional[List[int]]): Filter by one or more group IDs.
        include_subgroups (Optional[bool]): If true and group_id is supplied, include subgroups.
        email_address (Optional[str]): Filter by email address.
        phone_number (Optional[str]): Filter by phone number.
        include_deleted (Optional[bool]): If true, retrieve deleted records.

    Returns:
        List[Dict]: A list of employee dictionaries.
    """
    url = f"{BASE_URL}{EMPLOYEES_ENDPOINT}"
    headers = {'x-api-key': API_KEY, 'Content-Type': 'application/json'}
    params = {
        "page_size": page_size,
        "last_updated": last_updated,
        "is_active": is_active,
        "company_supplied_id": company_supplied_id,
        "group_id": group_id,
        "include_subgroups": include_subgroups,
        "email_address": email_address,
        "phone_number": phone_number,
        "include_deleted": include_deleted,
    }

    # Remove None values from params
    params = {k: v for k, v in params.items() if v is not None}

    results = get_all_paginated_results(url, headers, params=params)

    return results
