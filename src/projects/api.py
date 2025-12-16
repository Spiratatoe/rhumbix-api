import logging
from typing import List, Dict, Optional, Any

from src.config import BASE_URL, API_KEY
from src.utils import get_all_paginated_results

# Configure logging
logging.basicConfig(level=logging.INFO)

PROJECTS_ENDPOINT = "/projects/"


def get_projects(
    page_size: Optional[int] = None,
    last_updated: Optional[str] = None,
    job_number: Optional[List[str]] = None,
    name: Optional[str] = None,
    is_active: Optional[bool] = None,
    include_deleted: Optional[bool] = None,
    **kwargs: Any,
) -> List[Dict]:
    """
    Retrieves a list of projects from the Rhumbix API.

    Args:
        page_size (Optional[int]): Number of results to return per page.
        last_updated (Optional[str]): Retrieve data updated after this datetime.
        job_number (Optional[List[str]]): Filter by one or more job numbers.
        name (Optional[str]): Filter by project name.
        is_active (Optional[bool]): Filter by active status.
        include_deleted (Optional[bool]): If true, retrieve deleted records.
        **kwargs: Catch-all for custom field filters (e.g., custom_field_zone_id="123").

    Returns:
        List[Dict]: A list of project dictionaries.
    """
    url = f"{BASE_URL}{PROJECTS_ENDPOINT}"
    headers = {'x-api-key': API_KEY, 'Content-Type': 'application/json'}
    params = {
        "page_size": page_size,
        "last_updated": last_updated,
        "job_number": job_number,
        "name": name,
        "is_active": is_active,
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
