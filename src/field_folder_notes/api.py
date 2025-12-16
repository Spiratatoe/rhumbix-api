import logging
from typing import List, Dict, Optional

from src.config import BASE_URL, API_KEY
from src.utils import get_all_paginated_results

# Configure logging
logging.basicConfig(level=logging.INFO)

FIELD_FOLDER_NOTES_ENDPOINT = "/field_folder_notes/"


def get_field_folder_notes(
    page_size: Optional[int] = None,
    project: Optional[List[int]] = None,
    author: Optional[List[int]] = None,
    shift_date_from: Optional[str] = None,
    shift_date_to: Optional[str] = None,
    created_on_from: Optional[str] = None,
    created_on_to: Optional[str] = None,
    last_updated_from: Optional[str] = None,
    last_updated_to: Optional[str] = None,
    is_private: Optional[bool] = None,
    is_daily_report: Optional[bool] = None,
    has_photos: Optional[bool] = None,
    has_files: Optional[bool] = None,
    has_weather: Optional[bool] = None,
    has_delays: Optional[bool] = None,
    has_visitors: Optional[bool] = None,
    has_tags: Optional[bool] = None,
    tags: Optional[List[str]] = None,
    cost_codes: Optional[List[str]] = None,
    equipment: Optional[List[int]] = None,
    employees: Optional[List[str]] = None,
    note_type: Optional[List[str]] = None,
    include_deleted: Optional[bool] = None,
) -> List[Dict]:
    """
    Retrieves a list of field folder notes from the Rhumbix API.

    Args:
        page_size, project, author, shift_date_from, shift_date_to,
        created_on_from, created_on_to, last_updated_from, last_updated_to,
        is_private, is_daily_report, has_photos, has_files, has_weather,
        has_delays, has_visitors, has_tags, tags, cost_codes, equipment,
        employees, note_type, include_deleted: Various filters for the query.

    Returns:
        List[Dict]: A list of field folder note dictionaries.
    """
    url = f"{BASE_URL}{FIELD_FOLDER_NOTES_ENDPOINT}"
    headers = {'x-api-key': API_KEY, 'Content-Type': 'application/json'}
    params = {
        "page_size": page_size,
        "project": project,
        "author": author,
        "shift_date_from": shift_date_from,
        "shift_date_to": shift_date_to,
        "created_on_from": created_on_from,
        "created_on_to": created_on_to,
        "last_updated_from": last_updated_from,
        "last_updated_to": last_updated_to,
        "is_private": is_private,
        "is_daily_report": is_daily_report,
        "has_photos": has_photos,
        "has_files": has_files,
        "has_weather": has_weather,
        "has_delays": has_delays,
        "has_visitors": has_visitors,
        "has_tags": has_tags,
        "tags": tags,
        "cost_codes": cost_codes,
        "equipment": equipment,
        "employees": employees,
        "note_type": note_type,
        "include_deleted": include_deleted,
    }

    # Remove None values from params
    params = {k: v for k, v in params.items() if v is not None}

    results = get_all_paginated_results(url, headers, params=params)

    return results
