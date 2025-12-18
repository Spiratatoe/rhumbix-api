import logging
from typing import List, Dict, Optional

from src.config import BASE_URL, API_KEY
from src.utils import get_all_paginated_results

# Configure logging
logging.basicConfig(level=logging.INFO)

EMAIL_ALERTS_ENDPOINT = "/email_alerts/"

def get_email_alerts(
    page_size: Optional[int] = None,
    job_number: Optional[str] = None,
    company_supplied_id: Optional[str] = None,
) -> List[Dict]:
    """
    Retrieves a list of email alerts from the Rhumbix API.

    Args:
        page_size (Optional[int]): Number of results to return per page.
        job_number (Optional[str]): Filter by job number.
        company_supplied_id (Optional[str]): Filter by company supplied ID.

    Returns:
        List[Dict]: A list of email alert dictionaries.
    """
    url = f"{BASE_URL}{EMAIL_ALERTS_ENDPOINT}"
    headers = {'x-api-key': API_KEY, 'Content-Type': 'application/json'}
    params = {
        "page_size": page_size,
        "job_number": job_number,
        "company_supplied_id": company_supplied_id,
    }

    # Remove None values from params
    params = {k: v for k, v in params.items() if v is not None}

    results = get_all_paginated_results(url, headers, params=params)

    return results
