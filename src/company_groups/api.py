import logging
from typing import List, Dict, Optional

import pandas as pd
import requests

from src.config import BASE_URL, API_KEY
from src.utils import get_all_paginated_results

# Configure logging
logging.basicConfig(level=logging.INFO)

COMPANY_GROUPS_ENDPOINT = "/company_groups/"


def get_rhumbix_ou_list() -> List[Dict]:
    """
    Retrieves the list of Organizational Units (OUs) from the Rhumbix API.

    This function fetches all company groups, which represent OUs,
    and returns them as a list of dictionaries, each containing the 'id' and 'name' of an OU.

    Returns:
        List[Dict]: A list of dictionaries, where each dictionary represents an OU
                    with 'id' and 'name' keys. Returns an empty list if an error occurs.

    Example Output:
        [
            {'id': 1, 'name': 'OU Alpha'},
            {'id': 2, 'name': 'OU Beta'}
        ]
    """
    results = get_company_groups_details()

    if not results:
        return []

    ou_df = pd.DataFrame(results)
    if 'id' in ou_df.columns and 'name' in ou_df.columns:
        return ou_df[['id', 'name']].sort_values('name').to_dict('records')
    else:
        logging.error("Response data did not contain 'id' and 'name' columns.")
        return []


def get_company_groups_details(
    last_updated: Optional[str] = None, page_size: Optional[int] = None
) -> List[Dict]:
    """
    Retrieves a detailed list of company groups from the Rhumbix API.

    This function can be filtered by when the data was last updated and can
    specify the number of results to return per page.

    Args:
        last_updated (Optional[str]): Retrieve data that has changed after the
            specified last updated date in 'YYYY-MM-DDThh:mm:ss.ffffffZ' format
            (e.g., '2025-12-16T16:45:02.323544Z').
        page_size (Optional[int]): Number of results to return per page.

    Returns:
        List[Dict]: A list of dictionaries, where each dictionary contains
                    the detailed information for a company group.

    Example Output:
        [
            {
                "id": 3,
                "name": "Dolor",
                "description": "",
                "parent_id": null,
                "children_ids": [5, 6],
                "employees": ["GREATCO-FOREMAN-1", "GREATCO-FOREMAN-2"],
                "grants_employee_access": true,
                "grants_project_access": true,
                "cohorts": [],
                "cico_settings": {
                    "custom_address": "",
                    "enabled": true,
                    "meals_and_breaks": true,
                    "location": "CAPTURED",
                    "photo": "CAPTURED",
                    "radius": null,
                    "rounding_increment": 8,
                    "units": "MI",
                    "geofence": { ... }
                }
            }
        ]
    """
    url = f"{BASE_URL}{COMPANY_GROUPS_ENDPOINT}"
    headers = {'x-api-key': API_KEY, 'Content-Type': 'application/json'}
    params = {}
    if last_updated:
        params["last_updated"] = last_updated
    if page_size:
        params["page_size"] = page_size

    results = get_all_paginated_results(url, headers, params=params)

    return results

