import logging
from typing import List, Dict, Optional

import requests

from src.config import BASE_URL, API_KEY
from src.utils import get_all_paginated_results

# Configure logging
logging.basicConfig(level=logging.INFO)

DELETED_TIMEKEEPING_ENTRIES_ENDPOINT = "/deleted_timekeeping_entries/"

def get_deleted_timekeeping_entries(
    history_start_date: Optional[str] = None,
    history_end_date: Optional[str] = None,
) -> List[Dict]:
    """
    Retrieves a list of deleted timekeeping entries from the Rhumbix API.

    Args:
        history_start_date (Optional[str]): Retrieve history from this date onwards.
        history_end_date (Optional[str]): Retrieve history up to this date.

    Returns:
        List[Dict]: A list of deleted timekeeping entry dictionaries.
    """
    url = f"{BASE_URL}{DELETED_TIMEKEEPING_ENTRIES_ENDPOINT}"
    headers = {'x-api-key': API_KEY, 'Content-Type': 'application/json'}
    params = {
        "history_start_date": history_start_date,
        "history_end_date": history_end_date,
    }

    # Remove None values from params
    params = {k: v for k, v in params.items() if v is not None}

    results = get_all_paginated_results(url, headers, params=params)

    return results
