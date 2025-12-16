import logging
from typing import List, Dict, Optional

import requests

# Configure logging
logging.basicConfig(level=logging.INFO)


def get_all_paginated_results(url: str, headers: Dict[str, str], params: Optional[Dict[str, any]] = None) -> List[Dict]:
    """
    Handles pagination for Rhumbix API endpoints.

    Args:
        url (str): The initial URL to fetch data from.
        headers (Dict[str, str]): The request headers, including the API key.
        params (Optional[Dict[str, any]]): The request parameters.

    Returns:
        List[Dict]: A list of all results from all pages. Returns an empty list on error.
    """
    all_results = []
    while url:
        try:
            response = requests.get(url=url, headers=headers, params=params)
            response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

            data = response.json()
            all_results.extend(data.get('results', []))
            url = data.get('next')
            params = None  # Params are included in the 'next' URL

        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching data from Rhumbix API: {e}")
            return []  # Return empty list on error

    return all_results
