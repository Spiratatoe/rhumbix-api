import logging
from typing import List, Dict, Optional

from src.config import BASE_URL, API_KEY
from src.utils import get_all_paginated_results

# Configure logging
logging.basicConfig(level=logging.INFO)

COMPANIES_ENDPOINT = "/companies/"


def get_companies(
    page_size: Optional[int] = None,
    job_number: Optional[str] = None,
) -> List[Dict]:
    """
    Retrieves a list of companies from the Rhumbix API.

    Args:
        page_size (Optional[int]): Number of results to return per page.
        job_number (Optional[str]): Filter by a specific job number.

    Returns:
        List[Dict]: A list of dictionaries, where each dictionary contains
                    the information for a company.

    Example Output:
        [
            {
                "company_key": "AO5zQy7Z",
                "name": "Carolyn's Crushers"
            }
        ]
    """
    url = f"{BASE_URL}{COMPANIES_ENDPOINT}"
    headers = {'x-api-key': API_KEY, 'Content-Type': 'application/json'}
    params = {
        "page_size": page_size,
        "job_number": job_number,
    }
    # Remove None values from params
    params = {k: v for k, v in params.items() if v is not None}

    results = get_all_paginated_results(url, headers, params=params)

    return results
