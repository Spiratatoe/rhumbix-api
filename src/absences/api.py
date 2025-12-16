import logging
from typing import List, Dict, Optional

from src.config import BASE_URL, API_KEY
from src.utils import get_all_paginated_results

# Configure logging
logging.basicConfig(level=logging.INFO)

ABSENCES_ENDPOINT = "/absences/"


def get_absences(
    page_size: Optional[int] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    is_approved: Optional[bool] = None,
    status: Optional[str] = None,
    employee: Optional[str] = None,
    last_updated: Optional[str] = None,
    include_deleted: Optional[bool] = None,
    group_id: Optional[List[int]] = None,
    include_subgroups: Optional[bool] = None,
) -> List[Dict]:
    """
    Retrieves a list of absences from the Rhumbix API, with extensive filtering options.

    Args:
        page_size (Optional[int]): Number of results to return per page.
        start_date (Optional[str]): Start date in YYYY-MM-DD format.
        end_date (Optional[str]): End date in YYYY-MM-DD format.
        is_approved (Optional[bool]): Filter for approved status.
        status (Optional[str]): Filter by status (e.g., 'PENDING', 'APPROVED').
                                Overrides is_approved if both are given.
        employee (Optional[str]): Filter by employee's company_supplied_id.
        last_updated (Optional[str]): Retrieve data updated after this datetime
                                    in YYYY-MM-DDThh:mm:ss.ffffffZ format.
        include_deleted (Optional[bool]): If true, retrieve deleted records.
        group_id (Optional[List[int]]): Filter by one or more group IDs.
        include_subgroups (Optional[bool]): If true and group_id is supplied,
                                           include subgroups in results.

    Returns:
        List[Dict]: A list of dictionaries, where each dictionary contains
                    the detailed information for an absence.

    Example Output:
        [
            {
                "work_shift_key": "4g0ZRM5y",
                "shift_date": "2025-12-09",
                "start_time": "2025-12-09T06:00:02.323544Z",
                "end_time": "2025-12-09T15:00:02.323544Z",
                "timezone": "America/Los_Angeles",
                "id": 88511,
                "employee": "GREATCO-FOREMAN-21",
                "is_approved": true,
                "status": "APPROVED",
                "type": "Sick",
                "code": "S",
                "last_updated": "2025-12-15T06:00:02.323544Z",
                "deleted_on": null
            }
        ]
    """
    url = f"{BASE_URL}{ABSENCES_ENDPOINT}"
    headers = {'x-api-key': API_KEY, 'Content-Type': 'application/json'}
    params = {
        "page_size": page_size,
        "start_date": start_date,
        "end_date": end_date,
        "is_approved": is_approved,
        "status": status,
        "employee": employee,
        "last_updated": last_updated,
        "include_deleted": include_deleted,
        "group_id": group_id,
        "include_subgroups": include_subgroups,
    }
    # Remove None values from params so they are not sent in the request
    params = {k: v for k, v in params.items() if v is not None}

    results = get_all_paginated_results(url, headers, params=params)

    return results
