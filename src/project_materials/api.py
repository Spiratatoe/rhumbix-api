import logging
from typing import List, Dict, Optional

from src.config import BASE_URL, API_KEY
from src.utils import get_all_paginated_results

# Configure logging
logging.basicConfig(level=logging.INFO)

PROJECT_MATERIALS_ENDPOINT = "/project_materials/"

def get_project_materials(
    page_size: Optional[int] = None,
    materials: Optional[List[str]] = None,
    job_numbers: Optional[List[str]] = None,
) -> List[Dict]:
    """
    Retrieves a list of project materials from the Rhumbix API.

    Args:
        page_size (Optional[int]): Number of results to return per page.
        materials (Optional[List[str]]): Filter by one or more material IDs.
        job_numbers (Optional[List[str]]): Filter by one or more job numbers.

    Returns:
        List[Dict]: A list of project material dictionaries.
    """
    url = f"{BASE_URL}{PROJECT_MATERIALS_ENDPOINT}"
    headers = {'x-api-key': API_KEY, 'Content-Type': 'application/json'}
    params = {
        "page_size": page_size,
        "materials": materials,
        "job_numbers": job_numbers,
    }

    # Remove None values from params
    params = {k: v for k, v in params.items() if v is not None}

    results = get_all_paginated_results(url, headers, params=params)

    return results
