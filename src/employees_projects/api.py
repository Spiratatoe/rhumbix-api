import logging
from typing import List, Dict, Optional

from src.config import BASE_URL, API_KEY
from src.utils import get_all_paginated_results

# Configure logging
logging.basicConfig(level=logging.INFO)

EMPLOYEES_PROJECTS_ENDPOINT = "/employees_projects/"

def get_employees_projects(
    page_size: Optional[int] = None,
    employees: Optional[List[str]] = None,
    job_numbers: Optional[List[str]] = None,
) -> List[Dict]:
    """
    Retrieves a list of employee-project mappings from the Rhumbix API.

    Args:
        page_size (Optional[int]): Number of results to return per page.
        employees (Optional[List[str]]): Filter by one or more employee IDs.
        job_numbers (Optional[List[str]]): Filter by one or more job numbers.

    Returns:
        List[Dict]: A list of employee-project mapping dictionaries.
    """
    url = f"{BASE_URL}{EMPLOYEES_PROJECTS_ENDPOINT}"
    headers = {'x-api-key': API_KEY, 'Content-Type': 'application/json'}
    params = {
        "page_size": page_size,
        "employees": employees,
        "job_numbers": job_numbers,
    }

    # Remove None values from params
    params = {k: v for k, v in params.items() if v is not None}

    results = get_all_paginated_results(url, headers, params=params)

    return results
