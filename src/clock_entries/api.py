import logging
from typing import List, Dict, Optional

from src.config import BASE_URL, API_KEY
from src.utils import get_all_paginated_results

# Configure logging
logging.basicConfig(level=logging.INFO)

CLOCK_ENTRIES_ENDPOINT = "/clock_in_clock_out_entries/"


def get_clock_in_clock_out_entries(
    page_size: Optional[int] = None,
    last_updated: Optional[str] = None,
    worker: Optional[List[str]] = None,
    start_time: Optional[str] = None,
    end_time: Optional[str] = None,
    only_edited: Optional[bool] = None,
    entry_id: Optional[List[str]] = None,
    include_deleted: Optional[bool] = None,
) -> List[Dict]:
    """
    Retrieves a list of clock-in/clock-out entries from the Rhumbix API.

    Args:
        page_size (Optional[int]): Number of results to return per page.
        last_updated (Optional[str]): Retrieve data updated after this datetime.
        worker (Optional[List[str]]): Filter by one or more worker company-supplied IDs.
        start_time (Optional[str]): Retrieve entries with entered_time after this datetime.
        end_time (Optional[str]): Retrieve entries with entered_time before this datetime.
        only_edited (Optional[bool]): If true, return only edited entries.
        entry_id (Optional[List[str]]): Filter by a list of entry IDs.
        include_deleted (Optional[bool]): If true, retrieve deleted records.

    Returns:
        List[Dict]: A list of dictionaries, where each dictionary contains
                    the detailed information for a clock entry.

    Example Output:
        [
            {
                "calculated_values": {
                    "job_number": "job #1",
                    "foreman": "emp #1"
                },
                "client_created_on": "2025-12-15T07:30:02.323544Z",
                "created_by": "emp #1",
                "created_on": "2025-12-15T07:30:02.323544Z",
                "current_shift_date": "2025-12-15",
                "deleted_on": null,
                "entered_time": "2025-12-15T07:30:02.323544Z",
                "entry_id": 908,
                "entry_type": "CLOCK_IN",
                ...
            }
        ]
    """
    url = f"{BASE_URL}{CLOCK_ENTRIES_ENDPOINT}"
    headers = {'x-api-key': API_KEY, 'Content-Type': 'application/json'}
    params = {
        "page_size": page_size,
        "last_updated": last_updated,
        "worker": worker,
        "start_time": start_time,
        "end_time": end_time,
        "only_edited": only_edited,
        "entry_id": entry_id,
        "include_deleted": include_deleted,
    }
    # Remove None values from params
    params = {k: v for k, v in params.items() if v is not None}

    results = get_all_paginated_results(url, headers, params=params)

    return results
