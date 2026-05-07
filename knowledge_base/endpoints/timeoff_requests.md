# Time Off Requests

- **Function:** `get_timeoff_requests` (in `src/timeoff_requests/api.py`)
- **HTTP path:** `/timeoff_requests/` (full URL = `${RHUMBIX_BASE_URL}/timeoff_requests/`)
- **Returns:** `List[Dict]` — paginated, all pages collected.

## Import

```python
from src.timeoff_requests.api import get_timeoff_requests
```

## Parameters

All optional. `None` values are stripped. Booleans are sent when not `None`.

| Name | Type | Notes |
|---|---|---|
| page_size | int | Results per page. |
| last_updated | str | Datetime, `YYYY-MM-DDThh:mm:ss.ffffffZ`. |
| is_active | bool | Filter by active status. |
| employee | List[str] | One or more employee `company_supplied_id`s. |
| start_date | str | YYYY-MM-DD. |
| end_date | str | YYYY-MM-DD (inclusive). |
| include_deleted | bool | If true, retrieve deleted records. |

## Example call

```python
rows = get_timeoff_requests(start_date="2024-02-01", end_date="2024-02-29")
```

## Output shape

No captured sample. Run once and inspect; common Rhumbix fields include `id`, `created_on`, `last_updated`.

## Failure modes

- Network / non-2xx -> `get_all_paginated_results` logs and returns `[]`.
- Empty list is ambiguous (no records vs. error) — check logs.
- 401/403 -> bad `RHUMBIX_API_KEY`. 400 -> unknown filter or malformed date.
