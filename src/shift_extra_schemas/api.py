import logging
from typing import List, Dict, Optional

from src.config import BASE_URL, API_KEY
from src.utils import get_all_paginated_results

# Configure logging
logging.basicConfig(level=logging.INFO)

SHIFT_EXTRA_SCHEMAS_ENDPOINT = "/shift_extra_schemas/"

def get_shift_extra_schemas(
    page_size: Optional[int] = None,
) -> List[Dict]:
    """
    Retrieves a list of shift extra schemas from the Rhumbix API.

    Args:
        page_size (Optional[int]): Number of results to return per page.

    Returns:
        List[Dict]: A list of shift extra schema dictionaries.
    """
    url = f"{BASE_URL}{SHIFT_EXTRA_SCHEMAS_ENDPOINT}"
    headers = {'x-api-key': API_KEY, 'Content-Type': 'application/json'}
    params = {
        "page_size": page_size,
    }

    # Remove None values from params
    params = {k: v for k, v in params.items() if v is not None}

    results = get_all_paginated_results(url, headers, params=params)

    return results
