# Employee Shift Details

- **Function:** `get_employee_shift_details` (in `src/employee_shift_details/api.py`)
- **HTTP path:** `/employee_shift_details/` (full URL = `${RHUMBIX_BASE_URL}/employee_shift_details/`)
- **Returns:** `List[Dict]` — paginated, all pages collected.

## Import

```python
from src.employee_shift_details.api import get_employee_shift_details
```

## Parameters

All optional. `None` values are stripped. Booleans are sent when not `None`.

| Name | Type | Notes |
|---|---|---|
| page_size | int | Results per page. |
| start_date | str | YYYY-MM-DD. |
| end_date | str | YYYY-MM-DD. |
| employee | str | Filter by employee. |
| is_signed | bool | Filter by signed status. |
| last_updated | str | Datetime, `YYYY-MM-DDThh:mm:ss.ffffffZ`. |

## Example call

```python
rows = get_employee_shift_details(start_date="2024-02-01", end_date="2024-02-29")
```

## Output shape

No captured sample. Run once and inspect; common Rhumbix fields include `id`, `created_on`, `last_updated`.

## Failure modes

- Network / non-2xx -> `get_all_paginated_results` logs and returns `[]`.
- Empty list is ambiguous (no records vs. error) — check logs.
- 401/403 -> bad `RHUMBIX_API_KEY`. 400 -> unknown filter or malformed date.
