import logging
from typing import List, Dict, Optional

from src.config import BASE_URL, API_KEY
from src.utils import get_all_paginated_results

# Configure logging
logging.basicConfig(level=logging.INFO)

WORKFLOW_ENTRIES_ENDPOINT = "/workflow_entries/"

def get_workflow_entries(
    page_size: Optional[int] = None,
    job_number: Optional[str] = None,
    created_start_date: Optional[str] = None,
    created_end_date: Optional[str] = None,
    schema_id: Optional[int] = None,
    schema_name: Optional[str] = None,
    variants: Optional[str] = None,
    last_updated: Optional[str] = None,
    status: Optional[str] = None,
    include_deleted: Optional[bool] = None,
    is_active: Optional[bool] = None,
    expiration: Optional[int] = None,
) -> List[Dict]:
    """
    Retrieves a list of workflow entries from the Rhumbix API.

    Args:
        page_size (Optional[int]): Number of results to return per page.
        job_number (Optional[str]): Filter by job number.
        created_start_date (Optional[str]): YYYY-MM-DD
        created_end_date (Optional[str]): YYYY-MM-DD
        schema_id (Optional[int]): Filter by schema ID.
        schema_name (Optional[str]): Filter by schema name.
        variants (Optional[str]): Filter by variants.
        last_updated (Optional[str]): Retrieve data updated after this datetime.
        status (Optional[str]): Filter by status.
        include_deleted (Optional[bool]): If true, retrieve deleted records.
        is_active (Optional[bool]): Filter by active status.
        expiration (Optional[int]): Filter by expiration.

    Returns:
        List[Dict]: A list of workflow entry dictionaries.
    """
    url = f"{BASE_URL}{WORKFLOW_ENTRIES_ENDPOINT}"
    headers = {'x-api-key': API_KEY, 'Content-Type': 'application/json'}
    params = {
        "page_size": page_size,
        "job_number": job_number,
        "created_start_date": created_start_date,
        "created_end_date": created_end_date,
        "schema_id": schema_id,
        "schema_name": schema_name,
        "variants": variants,
        "last_updated": last_updated,
        "status": status,
        "include_deleted": include_deleted,
        "is_active": is_active,
        "expiration": expiration,
    }

    # Remove None values from params
    params = {k: v for k, v in params.items() if v is not None}

    results = get_all_paginated_results(url, headers, params=params)

    return results
