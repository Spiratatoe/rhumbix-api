import logging
from typing import List, Dict, Optional

from src.config import BASE_URL, API_KEY
from src.utils import get_all_paginated_results

# Configure logging
logging.basicConfig(level=logging.INFO)

MATERIAL_PRICING_ENDPOINT = "/material_pricing/"

def get_material_pricing(
    page_size: Optional[int] = None,
    materials: Optional[List[str]] = None,
) -> List[Dict]:
    """
    Retrieves a list of material pricing records from the Rhumbix API.

    Args:
        page_size (Optional[int]): Number of results to return per page.
        materials (Optional[List[str]]): Filter by one or more material IDs.

    Returns:
        List[Dict]: A list of material pricing dictionaries.
    """
    url = f"{BASE_URL}{MATERIAL_PRICING_ENDPOINT}"
    headers = {'x-api-key': API_KEY, 'Content-Type': 'application/json'}
    params = {
        "page_size": page_size,
        "materials": materials,
    }

    # Remove None values from params
    params = {k: v for k, v in params.items() if v is not None}

    results = get_all_paginated_results(url, headers, params=params)

    return results
