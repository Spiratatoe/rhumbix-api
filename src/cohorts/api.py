import logging
from typing import List, Dict, Optional, Any

from src.config import BASE_URL, API_KEY
from src.utils import get_all_paginated_results

# Configure logging
logging.basicConfig(level=logging.INFO)

COHORTS_ENDPOINT = "/cohorts/"


def get_cohorts(
    page_size: Optional[int] = None,
    last_updated: Optional[str] = None,
    **kwargs: Any,
) -> List[Dict]:
    """
    Retrieves a list of cohorts from the Rhumbix API, with support for custom field filtering.

    Args:
        page_size (Optional[int]): Number of results to return per page.
        last_updated (Optional[str]): Retrieve data updated after this datetime
                                    in YYYY-MM-DDThh:mm:ss.ffffffZ format.
        **kwargs: Catch-all for custom field filters. The key must be in the format
                  'custom_field_<field_name>', and the value can be a string or a
                  list of strings.
                  Example: get_cohorts(custom_field_zone_id="12345")
                  Example: get_cohorts(custom_field_zone_id=["12345", "54321"])

    Returns:
        List[Dict]: A list of dictionaries, where each dictionary contains
                    the detailed information for a cohort.

    Example Output:
        [
            {
                "id": 3,
                "name": "Sarah",
                "description": "Roofing",
                "is_hidden": true,
                "employees": ["GREATCO-FOREMAN-1"],
                "employee_permissions": ["GREATCO-FOREMAN-1", "GREATCO-FOREMAN-2"],
                "projects": [],
                "groups": ["Engineering", "Field Operations"],
                "custom_fields": {
                    "supervisor": "Sheila Rafter"
                }
            }
        ]
    """
    url = f"{BASE_URL}{COHORTS_ENDPOINT}"
    headers = {'x-api-key': API_KEY, 'Content-Type': 'application/json'}
    params = {
        "page_size": page_size,
        "last_updated": last_updated,
    }

    # Add any custom field filters from kwargs
    for key, value in kwargs.items():
        if key.startswith("custom_field_"):
            params[key] = value

    # Remove None values from params
    params = {k: v for k, v in params.items() if v is not None}

    results = get_all_paginated_results(url, headers, params=params)

    return results
