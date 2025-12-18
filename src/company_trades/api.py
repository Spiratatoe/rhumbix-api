import logging
from typing import List, Dict, Optional

from src.config import BASE_URL, API_KEY
from src.utils import get_all_paginated_results

# Configure logging
logging.basicConfig(level=logging.INFO)

COMPANY_TRADES_ENDPOINT = "/company_trades/"

def get_company_trades(
    page_size: Optional[int] = None,
) -> List[Dict]:
    """
    Retrieves a list of company trades from the Rhumbix API.

    Args:
        page_size (Optional[int]): Number of results to return per page.

    Returns:
        List[Dict]: A list of company trade dictionaries.
    """
    url = f"{BASE_URL}{COMPANY_TRADES_ENDPOINT}"
    headers = {'x-api-key': API_KEY, 'Content-Type': 'application/json'}
    params = {
        "page_size": page_size,
    }

    # Remove None values from params
    params = {k: v for k, v in params.items() if v is not None}

    results = get_all_paginated_results(url, headers, params=params)

    return results
