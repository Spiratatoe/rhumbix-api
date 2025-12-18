import logging
from typing import List, Dict, Optional

from src.config import BASE_URL, API_KEY
from src.utils import get_all_paginated_results

# Configure logging
logging.basicConfig(level=logging.INFO)

EQUIPMENT_PRICING_ENDPOINT = "/equipment_pricing/"

def get_equipment_pricing(
    page_size: Optional[int] = None,
    equipment: Optional[List[str]] = None,
) -> List[Dict]:
    """
    Retrieves a list of equipment pricing records from the Rhumbix API.

    Args:
        page_size (Optional[int]): Number of results to return per page.
        equipment (Optional[List[str]]): Filter by one or more equipment IDs.

    Returns:
        List[Dict]: A list of equipment pricing dictionaries.
    """
    url = f"{BASE_URL}{EQUIPMENT_PRICING_ENDPOINT}"
    headers = {'x-api-key': API_KEY, 'Content-Type': 'application/json'}
    params = {
        "page_size": page_size,
        "equipment": equipment,
    }

    # Remove None values from params
    params = {k: v for k, v in params.items() if v is not None}

    results = get_all_paginated_results(url, headers, params=params)

    return results
