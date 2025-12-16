import logging
from typing import List, Dict, Optional, Any

from src.config import BASE_URL, API_KEY
from src.utils import get_all_paginated_results

# Configure logging
logging.basicConfig(level=logging.INFO)

COST_CODES_ENDPOINT = "/cost_codes/"


def get_cost_codes(
    page_size: Optional[int] = None,
    job_number: Optional[List[str]] = None,
    last_updated: Optional[str] = None,
    is_active: Optional[bool] = None,
    code: Optional[str] = None,
    description: Optional[str] = None,
    has_budgets: Optional[bool] = None,
    include_deleted: Optional[bool] = None,
    **kwargs: Any,
) -> List[Dict]:
    """
    Retrieves a list of cost codes from the Rhumbix API.

    Args:
        page_size (Optional[int]): Number of results to return per page.
        job_number (Optional[List[str]]): Filter by one or more job numbers.
        last_updated (Optional[str]): Retrieve data updated after this datetime.
        is_active (Optional[bool]): Filter by active status.
        code (Optional[str]): Filter by cost code.
        description (Optional[str]): Filter by description.
        has_budgets (Optional[bool]): Filter for cost codes that have budgets.
        include_deleted (Optional[bool]): If true, retrieve deleted records.
        **kwargs: Catch-all for custom field filters (e.g., custom_field_zone_id="123").

    Returns:
        List[Dict]: A list of cost code dictionaries.
    """
    url = f"{BASE_URL}{COST_CODES_ENDPOINT}"
    headers = {'x-api-key': API_KEY, 'Content-Type': 'application/json'}
    params = {
        "page_size": page_size,
        "job_number": job_number,
        "last_updated": last_updated,
        "is_active": is_active,
        "code": code,
        "description": description,
        "has_budgets": has_budgets,
        "include_deleted": include_deleted,
    }

    # Add any custom field filters from kwargs
    for key, value in kwargs.items():
        if key.startswith("custom_field_"):
            params[key] = value

    # Remove None values from params
    params = {k: v for k, v in params.items() if v is not None}

    results = get_all_paginated_results(url, headers, params=params)

    return results
