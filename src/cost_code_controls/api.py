import logging
from typing import List, Dict, Optional

from src.config import BASE_URL, API_KEY
from src.utils import get_all_paginated_results

# Configure logging
logging.basicConfig(level=logging.INFO)

COST_CODE_CONTROLS_ENDPOINT = "/cost_code_controls/"

def get_cost_code_controls(
    page_size: Optional[int] = None,
    is_active: Optional[bool] = None,
    labor_type: Optional[str] = None,
    cost_code_type: Optional[str] = None,
) -> List[Dict]:
    """
    Retrieves a list of cost code controls from the Rhumbix API.

    Args:
        page_size (Optional[int]): Number of results to return per page.
        is_active (Optional[bool]): Filter by active status.
        labor_type (Optional[str]): Filter by labor type.
        cost_code_type (Optional[str]): Filter by cost code type.

    Returns:
        List[Dict]: A list of cost code control dictionaries.
    """
    url = f"{BASE_URL}{COST_CODE_CONTROLS_ENDPOINT}"
    headers = {'x-api-key': API_KEY, 'Content-Type': 'application/json'}
    params = {
        "page_size": page_size,
        "is_active": is_active,
        "labor_type": labor_type,
        "cost_code_type": cost_code_type,
    }

    # Remove None values from params
    params = {k: v for k, v in params.items() if v is not None}

    results = get_all_paginated_results(url, headers, params=params)

    return results
