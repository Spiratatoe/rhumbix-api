import logging
from typing import List, Dict, Optional

from src.config import BASE_URL, API_KEY
from src.utils import get_all_paginated_results

# Configure logging
logging.basicConfig(level=logging.INFO)

EMPLOYEES_PRICING_ENDPOINT = "/employees_pricing/"

def get_employees_pricing(
    page_size: Optional[int] = None,
    employees: Optional[List[str]] = None,
) -> List[Dict]:
    """
    Retrieves a list of employee pricing records from the Rhumbix API.

    Args:
        page_size (Optional[int]): Number of results to return per page.
        employees (Optional[List[str]]): Filter by one or more employee IDs.

    Returns:
        List[Dict]: A list of employee pricing dictionaries.
    """
    url = f"{BASE_URL}{EMPLOYEES_PRICING_ENDPOINT}"
    headers = {'x-api-key': API_KEY, 'Content-Type': 'application/json'}
    params = {
        "page_size": page_size,
        "employees": employees,
    }

    # Remove None values from params
    params = {k: v for k, v in params.items() if v is not None}

    results = get_all_paginated_results(url, headers, params=params)

    return results
