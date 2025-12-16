import logging
from typing import List, Dict, Optional

from src.config import BASE_URL, API_KEY
from src.utils import get_all_paginated_results

# Configure logging
logging.basicConfig(level=logging.INFO)

BUDGETS_ENDPOINT = "/budgets/"


def get_budgets(
    page_size: Optional[int] = None,
    job_number: Optional[str] = None,
    source: Optional[str] = None,
    last_updated: Optional[str] = None,
    cost_code: Optional[str] = None,
) -> List[Dict]:
    """
    Retrieves a list of budgets from the Rhumbix API, with filtering options.

    Args:
        page_size (Optional[int]): Number of results to return per page.
        job_number (Optional[str]): Filter by a specific job number.
        source (Optional[str]): Filter by budget source. Valid options: "ERP", "FIELD".
        last_updated (Optional[str]): Retrieve data updated after this datetime
                                    in YYYY-MM-DDThh:mm:ss.ffffffZ format.
        cost_code (Optional[str]): Filter by the code field of the budget's cost code.

    Returns:
        List[Dict]: A list of dictionaries, where each dictionary contains
                    the detailed information for a budget.

    Example Output:
        [
            {
                "job_number": "7269636",
                "cost_code": "ABC.123.UNME",
                "quantities": 1700,
                "hours": 80,
                "source": "FIELD"
            },
            {
                "job_number": "7269636",
                "cost_code": "YYZ.1981.RUSH",
                "quantities": 700,
                "hours": 100,
                "source": "FIELD"
            }
        ]
    """
    url = f"{BASE_URL}{BUDGETS_ENDPOINT}"
    headers = {'x-api-key': API_KEY, 'Content-Type': 'application/json'}
    params = {
        "page_size": page_size,
        "job_number": job_number,
        "source": source,
        "last_updated": last_updated,
        "cost_code": cost_code,
    }
    # Remove None values from params so they are not sent in the request
    params = {k: v for k, v in params.items() if v is not None}

    results = get_all_paginated_results(url, headers, params=params)

    return results
