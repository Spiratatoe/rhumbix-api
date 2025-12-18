import logging
from typing import List, Dict, Optional

from src.config import BASE_URL, API_KEY
from src.utils import get_all_paginated_results

# Configure logging
logging.basicConfig(level=logging.INFO)

NOTES_ENDPOINT = "/notes/"

def get_notes(
    page_size: Optional[int] = None,
    job_number: Optional[str] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    last_updated: Optional[str] = None,
) -> List[Dict]:
    """
    Retrieves a list of notes from the Rhumbix API.

    Args:
        page_size (Optional[int]): Number of results to return per page.
        job_number (Optional[str]): Filter by job number.
        start_date (Optional[str]): YYYY-MM-DD
        end_date (Optional[str]): YYYY-MM-DD
        last_updated (Optional[str]): Retrieve data updated after this datetime.

    Returns:
        List[Dict]: A list of note dictionaries.
    """
    url = f"{BASE_URL}{NOTES_ENDPOINT}"
    headers = {'x-api-key': API_KEY, 'Content-Type': 'application/json'}
    params = {
        "page_size": page_size,
        "job_number": job_number,
        "start_date": start_date,
        "end_date": end_date,
        "last_updated": last_updated,
    }

    # Remove None values from params
    params = {k: v for k, v in params.items() if v is not None}

    results = get_all_paginated_results(url, headers, params=params)

    return results
