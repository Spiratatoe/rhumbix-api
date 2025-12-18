import logging
from typing import List, Dict, Optional

from src.config import BASE_URL, API_KEY
from src.utils import get_all_paginated_results

# Configure logging
logging.basicConfig(level=logging.INFO)

PROJECT_EQUIPMENT_ENDPOINT = "/project_equipment/"

def get_project_equipment(
    page_size: Optional[int] = None,
    equipment: Optional[List[str]] = None,
    job_numbers: Optional[List[str]] = None,
) -> List[Dict]:
    """
    Retrieves a list of project equipment from the Rhumbix API.

    Args:
        page_size (Optional[int]): Number of results to return per page.
        equipment (Optional[List[str]]): Filter by one or more equipment IDs.
        job_numbers (Optional[List[str]]): Filter by one or more job numbers.

    Returns:
        List[Dict]: A list of project equipment dictionaries.
    """
    url = f"{BASE_URL}{PROJECT_EQUIPMENT_ENDPOINT}"
    headers = {'x-api-key': API_KEY, 'Content-Type': 'application/json'}
    params = {
        "page_size": page_size,
        "equipment": equipment,
        "job_numbers": job_numbers,
    }

    # Remove None values from params
    params = {k: v for k, v in params.items() if v is not None}

    results = get_all_paginated_results(url, headers, params=params)

    return results
