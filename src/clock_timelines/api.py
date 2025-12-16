import logging
from typing import List, Dict, Optional

from src.config import BASE_URL, API_KEY
from src.utils import get_all_paginated_results

# Configure logging
logging.basicConfig(level=logging.INFO)

CLOCK_TIMELINES_ENDPOINT = "/clock_in_clock_out_timelines/"


def get_clock_in_clock_out_timelines(
    page_size: Optional[int] = None,
    foreman: Optional[List[str]] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    job_number: Optional[List[str]] = None,
    worker: Optional[List[str]] = None,
) -> List[Dict]:
    """
    Retrieves a list of clock-in/clock-out timelines from the Rhumbix API.

    Args:
        page_size (Optional[int]): Number of results to return per page.
        foreman (Optional[List[str]]): Filter by one or more foreman company-supplied IDs.
        start_date (Optional[str]): Retrieve data from a specific start date in YYYY-MM-DD format.
        end_date (Optional[str]): Retrieve data up to and including this end date in YYYY-MM-DD format.
        job_number (Optional[List[str]]): Filter by one or more job numbers.
        worker (Optional[List[str]]): Filter by one or more worker company-supplied IDs.

    Returns:
        List[Dict]: A list of dictionaries, where each dictionary contains
                    the detailed information for a clock timeline.

    Example Output:
        [
            {
              "id": 1234,
              "working_minutes": 420,
              "break_minutes": 0,
              "meal_minutes": 60,
              "job_numbers": [
                "7269636"
              ],
              "worker": "GREATCO-EMP-26",
              "foreman": "GREATCO-FOREMAN-21",
              "shift_date": "2025-12-15",
              "start_time": "2025-12-15T07:30:02.323544Z",
              "end_time": "2025-12-15T15:30:02.323544Z",
              "entry_ids": [
                1234, 1235, 1237, 1239
              ]
            }
        ]
    """
    url = f"{BASE_URL}{CLOCK_TIMELINES_ENDPOINT}"
    headers = {'x-api-key': API_KEY, 'Content-Type': 'application/json'}
    params = {
        "page_size": page_size,
        "foreman": foreman,
        "start_date": start_date,
        "end_date": end_date,
        "job_number": job_number,
        "worker": worker,
    }
    # Remove None values from params
    params = {k: v for k, v in params.items() if v is not None}

    results = get_all_paginated_results(url, headers, params=params)

    return results
